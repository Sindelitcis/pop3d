# Cenas 3D do site: cada foto vira camadas (fundo, meio, frente) com profundidade própria e o que fica
# escondido atrás dos objetos reconstruído pela IA. No navegador, cada camada vira uma malha 3D: quando a
# câmera se mexe aparece fundo de verdade, sem pixel esticado.
#   Profundidade: Depth Pro (Apple), na resolução nativa de 1536.  Preenchimento: LaMa (big-lama).
#   Modelos em site/modelos (fora do git). Roda com o Python do Pop3D:
#   D:\Estudio\ia\video\nunif\.venv\Scripts\python.exe gerar_cenas.py [nome ...] [--rapido]
import json
import os
import sys
import time

import cv2
import numpy as np
import torch
import torch.nn.functional as F
from PIL import Image

AQUI = os.path.dirname(os.path.abspath(__file__))
MODELOS = os.path.join(AQUI, "modelos")
REPO_DP = r"D:\Estudio\ia\video\nunif\iw3\pretrained_models\hub\nagadomi_ml-depth-pro_iw3_main"
SAIDA = os.path.join(AQUI, "..", "docs", "cenas")
PROVAS = os.path.join(AQUI, "provas")          # folhas de conferência (fora do git)

# nome: arquivo, largura final, recorte (x0, y0, x1, y1 em fração), cortes de profundidade (None = automático)
CENAS = {
    "heroi":    dict(arq="bunny2.png", larg=1920, camadas=3),
    "filme":    dict(arq="bunny3.png", larg=1600, camadas=3),
    "turma":    dict(arq="bunny1.png", larg=1600, camadas=3),
    "spring":   dict(arq="spring1.png", larg=1600, camadas=3, ceu=True, recorte=(0.0, 0.062, 1.0, 0.9)),
    "baloes":   dict(arq="baloes2.jpg", larg=1920, camadas=3, ceu=True),
    "praia":    dict(arq="praia2.jpg", larg=1600, camadas=3, ceu=True),
    "coqueiros": dict(arq="praia3.jpg", larg=1600, camadas=3, ceu=True),
    "cachorro": dict(arq="cachorro1.jpg", larg=1600, camadas=3, recorte=(0.0, 0.42, 1.0, 0.86)),
    "filhote":  dict(arq="cachorro2.jpg", larg=1600, camadas=3),
    "festa":    dict(arq="bolo3.jpg", larg=1600, camadas=3),
    "jogo":     dict(arq="jogo1.jpg", larg=1600, camadas=3),
    "cidade":   dict(arq="cidade1.jpg", larg=1600, camadas=3),
    "cascata":  dict(arq="cascata2.jpg", larg=1600, camadas=3),
    "lago":     dict(arq="lago3.jpg", larg=1600, camadas=3, ceu=True),
    "tulipas":  dict(arq="flores3.jpg", larg=1600, camadas=3, ceu=True),
    "gato":     dict(arq="gato2.jpg", larg=1400, camadas=3, recorte=(0.0, 0.12, 1.0, 0.82)),
}
PEQUENA = 960          # versão para celular


def carregar_profundidade(dev):
    torch.hub.set_dir(os.path.join(MODELOS, "hub"))
    sys.path.insert(0, REPO_DP)
    from depth_pro import create_model_and_transforms
    m, _ = create_model_and_transforms(device=dev, precision=torch.float16, img_size=384)
    return m.eval()


@torch.inference_mode()
def profundidade(modelo, rgb, dev):
    """rgb uint8 HxWx3 -> disparidade float32 HxW (perto = grande), com média do espelhado.
    O modelo foi treinado com a foto esticada num quadrado de 1536 (é o jeito oficial)."""
    H, W = rgb.shape[:2]
    x = torch.from_numpy(rgb).to(dev).permute(2, 0, 1)[None].float().div(255)
    x = F.interpolate((x - 0.5) / 0.5, size=(1536, 1536), mode="bicubic", align_corners=False, antialias=True)
    x = torch.cat([x, x.flip(3)]).half()
    inv, _fov = modelo(x)
    inv = inv.float()
    inv = (inv[0:1] + inv[1:2].flip(3)) * 0.5
    inv = F.interpolate(inv, size=(H, W), mode="bicubic", align_corners=False)
    guia = torch.from_numpy(rgb).to(dev).permute(2, 0, 1)[None].float().div(255)
    inv = filtro_guiado(guia, inv, max(2, round(max(H, W) / 480)), 2e-4)
    return inv[0, 0].clamp_min(0).cpu().numpy()


def _caixa(x, r):
    return F.avg_pool2d(F.pad(x, (r, r, r, r), mode="replicate"), 2 * r + 1, stride=1)


def filtro_guiado(I, p, r, eps):
    """Filtro guiado com guia colorida (He et al.): alinha as bordas da profundidade com as da foto.
    I: 1x3xHxW, p: 1x1xHxW."""
    escala = p.abs().amax() + 1e-9
    p = p / escala
    mI, mp = _caixa(I, r), _caixa(p, r)
    cov = _caixa(I * p, r) - mI * mp                        # 1x3
    var = {}
    for a in range(3):
        for b in range(a, 3):
            var[a, b] = _caixa(I[:, a:a + 1] * I[:, b:b + 1], r) - mI[:, a:a + 1] * mI[:, b:b + 1]
    S = torch.stack([torch.cat([var[min(a, b), max(a, b)] for b in range(3)], 1) for a in range(3)], 1)  # 1x3x3xHxW
    S = S.permute(0, 3, 4, 1, 2) + eps * torch.eye(3, device=I.device)
    A = torch.linalg.solve(S, cov.permute(0, 2, 3, 1)[..., None])[..., 0].permute(0, 3, 1, 2)  # 1x3xHxW
    b = mp - (A * mI).sum(1, keepdim=True)
    q = (_caixa(A, r) * I).sum(1, keepdim=True) + _caixa(b, r)
    return q * escala


def normalizar(d):
    lo, hi = np.percentile(d, 0.5), np.percentile(d, 99.7)
    return np.clip((d - lo) / (hi - lo + 1e-9), 0, 1).astype(np.float32)


def otsu_multi(d, k):
    """k-1 cortes que separam melhor o histograma da profundidade (Otsu multinível, força bruta em 128 faixas)."""
    hist, bordas = np.histogram(d, bins=128, range=(0, 1))
    p = hist / hist.sum()
    centros = (bordas[:-1] + bordas[1:]) / 2
    cp, cm = np.cumsum(p), np.cumsum(p * centros)

    def var(a, b):          # variância entre classes da faixa [a, b)
        w = cp[b - 1] - (cp[a - 1] if a else 0)
        if w <= 1e-9:
            return 0.0
        mu = (cm[b - 1] - (cm[a - 1] if a else 0)) / w
        return w * mu * mu
    melhor, cortes = -1, None
    if k == 2:
        for i in range(4, 124):
            v = var(0, i) + var(i, 128)
            if v > melhor:
                melhor, cortes = v, [i]
    else:
        for i in range(4, 120):
            for j in range(i + 4, 124):
                v = var(0, i) + var(i, j) + var(j, 128)
                if v > melhor:
                    melhor, cortes = v, [i, j]
    return [float(bordas[c]) for c in cortes]


def suavizar_mascara(m, raio):
    """máscara bool -> alfa float com borda macia de ~raio px."""
    a = m.astype(np.float32)
    if raio > 0:
        a = cv2.GaussianBlur(a, (0, 0), raio)
    return a


def estender(valor, valida):
    """Preenche onde valida == False continuando os valores de dentro. Encosta sem degrau na borda (copia o
    vizinho válido mais perto) e vai alisando conforme se afasta: a malha não ganha "escadinha" na borda."""
    if valida.all():
        return valor
    if not valida.any():
        return np.full_like(valor, float(valor.mean()))
    fora = (~valida).astype(np.uint8)
    dist, lab = cv2.distanceTransformWithLabels(fora, cv2.DIST_L2, 5, labelType=cv2.DIST_LABEL_PIXEL)
    vals = valor[fora == 0]                    # os rótulos seguem a ordem de varredura dos pixels válidos
    cheio = vals[np.clip(lab - 1, 0, len(vals) - 1)].astype(np.float32)
    liso = cv2.GaussianBlur(cheio, (0, 0), max(4, valor.shape[1] / 300))
    w = np.clip(dist / max(10, valor.shape[1] / 120), 0, 1)
    return np.where(valida, valor, cheio * (1 - w) + liso * w).astype(np.float32)


def ceu(rgb):
    """Céu: região lisa e clara (ou azulada) ligada à borda de cima. O modelo de profundidade às vezes
    puxa o céu em volta de uma cabeça para perto (um "halo"); o céu de verdade fica no infinito."""
    H, W = rgb.shape[:2]
    f = rgb.astype(np.float32) / 255
    lum = f.mean(2)
    m1 = cv2.blur(lum, (7, 7))
    desvio = np.sqrt(np.maximum(cv2.blur(lum * lum, (7, 7)) - m1 * m1, 0))
    azul = (f[..., 2] >= f[..., 0] - 0.02) & (f[..., 2] >= f[..., 1] - 0.06)
    cand = (desvio < 0.022) & (lum > 0.38) & (azul | (f.max(2) - f.min(2) < 0.12))
    cand = cv2.morphologyEx(cand.astype(np.uint8), cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    n, lab = cv2.connectedComponents(cand, connectivity=4)
    topo = set(np.unique(lab[0, :])) - {0}
    m = np.isin(lab, list(topo)) if topo else np.zeros((H, W), bool)
    # preenche furinhos (nuvens com textura) sem invadir objetos grandes
    m = cv2.morphologyEx(m.astype(np.uint8), cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9))).astype(bool)
    return m


class Preenchedor:
    def __init__(self, dev):
        self.dev = dev
        self.m = torch.jit.load(os.path.join(MODELOS, "big-lama.pt"), map_location=dev).eval()

    @torch.inference_mode()
    def __call__(self, rgb, buraco, lado=1280):
        """rgb uint8 HxWx3, buraco bool HxW -> rgb com o buraco reconstruído."""
        H, W = buraco.shape
        if not buraco.any():
            return rgb
        esc = min(1.0, lado / max(H, W))
        h, w = int(round(H * esc / 8)) * 8, int(round(W * esc / 8)) * 8
        img = torch.from_numpy(rgb).to(self.dev).permute(2, 0, 1)[None].float().div(255)
        msk = torch.from_numpy(buraco.astype(np.float32)).to(self.dev)[None, None]
        img_p = F.interpolate(img, size=(h, w), mode="area")
        msk_p = (F.interpolate(msk, size=(h, w), mode="area") > 0.01).float()
        out = self.m(img_p, msk_p).clamp(0, 1)
        out = F.interpolate(out, size=(H, W), mode="bicubic", align_corners=False).clamp(0, 1)
        # costura macia: dentro do buraco vale a IA, fora a foto original
        k = torch.from_numpy(suavizar_mascara(buraco, 1.5)).to(self.dev)[None, None].clamp(0, 1)
        k = torch.maximum(k, msk)
        res = img * (1 - k) + out * k
        return (res[0].permute(1, 2, 0).cpu().numpy() * 255 + 0.5).astype(np.uint8)


def recorte(rgb, mascara, dev):
    """Borda da camada como num recorte profissional: o filtro guiado pela foto (matting) faz o alfa seguir
    o contorno de verdade (pelo, cabelo, folha), suave e na resolução da foto."""
    H, W = mascara.shape
    r = max(3, round(W / 380))
    I = torch.from_numpy(rgb).to(dev).permute(2, 0, 1)[None].float().div(255)
    p = torch.from_numpy(mascara.astype(np.float32)).to(dev)[None, None]
    a = filtro_guiado(I, p, r, 1e-3)[0, 0].clamp(0, 1).cpu().numpy()
    el = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (4 * r + 1,) * 2)
    certo_dentro = cv2.erode(mascara.astype(np.uint8), el).astype(bool)
    certo_fora = ~cv2.dilate(mascara.astype(np.uint8), el).astype(bool)
    a = np.where(certo_dentro, 1.0, np.where(certo_fora, 0.0, a))
    a = cv2.GaussianBlur(a.astype(np.float32), (0, 0), 0.7)
    return np.clip((a - 0.04) / 0.92, 0, 1).astype(np.float32)


def descontaminar(cor, alfa):
    """Na borda, o pixel da foto mistura a cor do objeto com a do fundo; se ficar assim, o fundo antigo
    aparece como uma auréola quando a camada se mexe. A borda passa a usar a cor do objeto mais perto."""
    dentro = alfa > 0.985
    if not dentro.any():
        return cor
    fora = (~dentro).astype(np.uint8)
    _, lab = cv2.distanceTransformWithLabels(fora, cv2.DIST_L2, 5, labelType=cv2.DIST_LABEL_PIXEL)
    vals = cor[fora == 0]
    perto = vals[np.clip(lab - 1, 0, len(vals) - 1)]
    m = ((alfa > 0.003) & ~dentro)[..., None]
    w = np.clip(1.0 - alfa, 0, 1)[..., None] ** 0.5         # quanto mais transparente, mais do objeto
    mist = (cor.astype(np.float32) * (1 - w) + perto.astype(np.float32) * w)
    return np.where(m, mist, cor).clip(0, 255).astype(np.uint8)


def cena(nome, cfg, mdp, lama, dev):
    t0 = time.time()
    im = Image.open(os.path.join(AQUI, "originais", cfg["arq"])).convert("RGB")
    if cfg.get("recorte"):
        x0, y0, x1, y1 = cfg["recorte"]
        im = im.crop((round(x0 * im.width), round(y0 * im.height), round(x1 * im.width), round(y1 * im.height)))
    larg = cfg["larg"]
    if im.width > larg:
        im = im.resize((larg, round(im.height * larg / im.width)), Image.LANCZOS)
    rgb = np.asarray(im).copy()
    H, W = rgb.shape[:2]

    d = normalizar(profundidade(mdp, rgb, dev))
    if cfg.get("ceu"):
        mc = ceu(rgb)
        d = np.where(mc, 0.0, d).astype(np.float32)
    k = cfg.get("camadas", 3)
    cortes = cfg.get("cortes") or otsu_multi(d, k)
    rot = np.zeros((H, W), np.uint8)
    for c in cortes:
        rot += (d >= c).astype(np.uint8)
    # tira ilhas minúsculas de uma camada (ruído na fronteira): abre e fecha um pouco
    el = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    for i in range(1, k):
        m = (rot >= i).astype(np.uint8)
        m = cv2.morphologyEx(cv2.morphologyEx(m, cv2.MORPH_OPEN, el), cv2.MORPH_CLOSE, el)
        rot = np.where(m.astype(bool), np.maximum(rot, i), np.minimum(rot, i - 1)).astype(np.uint8)
    pasta = os.path.join(SAIDA, nome)
    os.makedirs(pasta, exist_ok=True)
    cores, profs, alfas = [], [], []
    dil = max(3, round(W / 400))
    for i in range(k):
        # camada i: o que tem profundidade >= corte i; o que está na frente dela (rot > i) é reconstruído
        frente = rot > i
        buraco = cv2.dilate(frente.astype(np.uint8), cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2 * dil + 1,) * 2)).astype(bool)
        cor = lama(rgb, buraco) if i < k - 1 else rgb
        # profundidade da camada: a real onde ela aparece; atrás dos objetos da frente, continua a superfície dela
        propria = rot == i
        pi = estender(d, propria & ~buraco if (propria & ~buraco).any() else propria)
        if i < k - 1:
            pi = np.where(frente, np.minimum(pi, cortes[i] if i < len(cortes) else 1.0), pi)
        pi = np.where(propria, d, pi)
        # a malha nunca rasga: degraus que sobram dentro da camada viram uma curva suave
        pi = cv2.GaussianBlur(pi.astype(np.float32), (0, 0), max(3.0, W / 170))
        if i == 0:
            alfa = np.ones((H, W), np.float32)
        else:
            # atrás dos objetos da frente, a camada só continua perto de onde ela existe de verdade;
            # mais longe fica transparente e quem aparece é o fundo
            dist = cv2.distanceTransform((~propria).astype(np.uint8), cv2.DIST_L2, 5)
            existe = propria | (frente & (dist < max(8, W * 0.035)))
            alfa = recorte(rgb, existe, dev)
            cor = descontaminar(cor, alfa)
        cores.append(cor)
        profs.append(pi)
        alfas.append(alfa)

    def salvar(lw, sufixo):
        lh = round(H * lw / W)
        for i in range(k):
            c = cv2.resize(cores[i], (lw, lh), interpolation=cv2.INTER_AREA) if lw != W else cores[i]
            if i == 0:
                Image.fromarray(c).save(os.path.join(pasta, f"c{i}{sufixo}.webp"), quality=86, method=6)
            else:
                a = cv2.resize(alfas[i], (lw, lh), interpolation=cv2.INTER_AREA) if lw != W else alfas[i]
                rgba = np.dstack([c, (np.clip(a, 0, 1) * 255 + 0.5).astype(np.uint8)])
                Image.fromarray(rgba, "RGBA").save(os.path.join(pasta, f"c{i}{sufixo}.webp"), quality=86, method=6)
        # profundidades das camadas juntas numa imagem (R, G, B = camada 0, 1, 2), metade do tamanho
        pw, ph = max(2, lw // 2), max(2, lh // 2)
        canais = [cv2.resize(profs[i], (pw, ph), interpolation=cv2.INTER_AREA) for i in range(k)]
        while len(canais) < 3:
            canais.append(canais[-1])
        pack = (np.clip(np.dstack(canais[:3]), 0, 1) * 255 + 0.5).astype(np.uint8)
        Image.fromarray(pack, "RGB").save(os.path.join(pasta, f"p{sufixo}.webp"), lossless=True, quality=100, method=6)
        return lw, lh

    salvar(W, "")
    if W > PEQUENA:
        salvar(PEQUENA, "_p")

    # folha de conferência: foto, profundidade, camadas reconstruídas
    os.makedirs(PROVAS, exist_ok=True)
    tw = 640
    th = round(H * tw / W)
    pecas = [cv2.resize(rgb, (tw, th)),
             cv2.resize(cv2.applyColorMap((d * 255).astype(np.uint8), cv2.COLORMAP_TURBO)[..., ::-1], (tw, th))]
    for i in range(k):
        xadrez = ((np.indices((th, tw)).sum(0) // 16) % 2 * 60 + 40).astype(np.uint8)[..., None].repeat(3, 2)
        a = cv2.resize(alfas[i], (tw, th))[..., None]
        pecas.append((cv2.resize(cores[i], (tw, th)) * a + xadrez * (1 - a)).astype(np.uint8))
    folha = np.concatenate([np.concatenate(pecas[j:j + 2] if j + 1 < len(pecas) else [pecas[j], np.zeros_like(pecas[j])], 1)
                            for j in range(0, len(pecas), 2)], 0)
    Image.fromarray(folha).save(os.path.join(PROVAS, f"{nome}.jpg"), quality=85)
    print(f"ok {nome} {W}x{H} cortes={[round(c, 3) for c in cortes]} {time.time() - t0:.1f} s", flush=True)
    return {"w": W, "h": H, "camadas": k, "cortes": [round(c, 4) for c in cortes], "pequena": W > PEQUENA}


def main():
    nomes = [a for a in sys.argv[1:] if not a.startswith("--")] or list(CENAS)
    dev = torch.device("cuda")
    mdp = carregar_profundidade(dev)
    lama = Preenchedor(dev)
    indice_arq = os.path.join(SAIDA, "cenas.json")
    indice = json.load(open(indice_arq, encoding="utf-8")) if os.path.exists(indice_arq) else {}
    for n in nomes:
        indice[n] = cena(n, CENAS[n], mdp, lama, dev)
    os.makedirs(SAIDA, exist_ok=True)
    with open(indice_arq, "w", encoding="utf-8") as f:
        json.dump(dict(sorted(indice.items())), f, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
