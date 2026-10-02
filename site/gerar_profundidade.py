# Prepara as imagens do site: versão leve para a web (WebP) + mapa de profundidade feito pela IA do Pop3D
# (perto = claro, longe = escuro). Roda com o Python do Pop3D:
#   D:\Estudio\ia\video\nunif\.venv\Scripts\python.exe gerar_profundidade.py
import os
import sys
import time

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, r"D:\Estudio\ia\video\nunif")
SAIDA = os.path.join(AQUI, "..", "docs", "img")
ESCOLHIDAS = {   # nome no site: (arquivo original, largura máxima)
    "heroi": ("bunny2.png", 1920),
    "filme": ("bunny1.png", 1280),
    "filme2": ("bunny3.png", 1280),
    "baloes": ("baloes2.jpg", 1600),
    "lago": ("lago3.jpg", 1280),
    "praia": ("praia2.jpg", 1280),
    "cachorro": ("cachorro1.jpg", 1600),
    "filhote": ("cachorro2.jpg", 1280),
    "festa": ("bolo2.jpg", 1280),
    "jogo": ("jogo1.jpg", 1280),
    "cidade": ("cidade1.jpg", 1280),
    "cascata": ("cascata2.jpg", 1280),
    "tulipas": ("flores3.jpg", 1280),
}


def main():
    import torch
    import torch.nn.functional as F
    from PIL import Image
    from iw3.desktop import utils as DU
    import torchvision.transforms.functional as TF

    os.makedirs(SAIDA, exist_ok=True)
    args = DU.create_parser().parse_args(["--depth-model", "VDA_Metric_L", "--resolution", "518"])
    DU.set_state_args(args)
    dm = args.state["depth_model"]
    dm.load(gpu=args.gpu, resolution=args.resolution)
    for nome, (arq, larg) in ESCOLHIDAS.items():
        im = Image.open(os.path.join(AQUI, "originais", arq)).convert("RGB")
        if im.width > larg:
            im = im.resize((larg, round(im.height * larg / im.width)), Image.LANCZOS)
        im.save(os.path.join(SAIDA, f"{nome}.webp"), quality=82, method=6)
        # a IA olha uma cópia menor (rápido e cabe na memória); o mapa sai na metade do tamanho da foto
        peq = im.resize((1024, round(im.height * 1024 / im.width)), Image.LANCZOS) if im.width > 1024 else im
        x = TF.to_tensor(peq).to(args.state["device"])
        t0 = time.time()
        dm.reset()
        with torch.inference_mode():
            for _ in range(2):   # modelo de vídeo: algumas "repetições" do mesmo quadro estabilizam a memória dele
                d = dm.infer(x, tta=False, low_vram=False, enable_amp=True, edge_dilation=0, depth_aa=False)
        d = d.float().squeeze()
        d = (d - d.min()) / (d.max() - d.min() + 1e-6)
        if dm.is_metric():   # métrico = distância (perto é pequeno): inverte para perto = claro
            d = 1.0 - d
        d = F.interpolate(d[None, None], size=(im.height // 2, im.width // 2), mode="area")[0, 0]
        Image.fromarray((d.clamp(0, 1) * 255).round().byte().cpu().numpy(), "L").save(
            os.path.join(SAIDA, f"{nome}_prof.png"), optimize=True)
        print("ok", nome, im.size, f"{time.time() - t0:.1f} s", flush=True)


if __name__ == "__main__":
    main()
