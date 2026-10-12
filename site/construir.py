# Monta o site do Pop3D (pasta docs, publicada pelo GitHub Pages) em todos os idiomas (textos.IDIOMAS).
# Uso: python construir.py   (depois é só commit + push no repositório pop3d)
import html
import json
import os

import re

import gerar_cenas
import privacidade
import textos

AQUI = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.join(AQUI, "..", "docs")
LINGUAS = ("pt", "en", "es", "fr", "de", "it", "uk")
PASTA = {"pt": "", "en": "en/", "es": "es/", "fr": "fr/", "de": "de/", "it": "it/", "uk": "uk/"}
PRIV = {"pt": "privacidade.html", "en": "privacy.html", "es": "privacidad.html", "fr": "confidentialite.html",
        "de": "datenschutz.html", "it": "privacy.html", "uk": "konfidentsiinist.html"}
NOME = {o: o.upper() for o in LINGUAS}
NATIVO = {"pt": "Português", "en": "English", "es": "Español", "fr": "Français", "de": "Deutsch", "it": "Italiano",
          "uk": "Українська"}
HREFLANG = {"pt": "pt-BR", "en": "en", "es": "es", "fr": "fr", "de": "de", "it": "it", "uk": "uk"}
ROTULO = {"pt": "Idioma", "en": "Language", "es": "Idioma", "fr": "Langue", "de": "Sprache", "it": "Lingua", "uk": "Мова"}
INDICE = json.load(open(os.path.join(DOCS, "cenas", "cenas.json"), encoding="utf-8"))
BAIXAR = "https://github.com/Sindelitcis/pop3d/releases/latest/download/"

def redirecionar(lingua):
    """1ª visita: vai para o idioma de quem chegou. Vale o idioma do navegador; o país (pelo fuso horário do
    aparelho, sem consultar servidor nenhum) decide quando o navegador está no inglês padrão. Quem escolhe à
    mão no seletor de idioma fica com a escolha guardada."""
    subir = "../" if PASTA[lingua] else ""
    alvos = {o: (subir + PASTA[o]) or "./" for o in LINGUAS}
    return r"""<script>
  (function () {
    try {
      if (localStorage.getItem("pop3d_idioma")) return;
      var aqui = "%s", alvos = %s;
      var fuso = (Intl.DateTimeFormat().resolvedOptions().timeZone || "");
      var ptFuso = /^(America\/(Sao_Paulo|Bahia|Fortaleza|Recife|Belem|Maceio|Manaus|Cuiaba|Campo_Grande|Porto_Velho|Boa_Vista|Rio_Branco|Araguaina|Santarem|Noronha|Eirunepe)|Europe\/Lisbon|Atlantic\/(Azores|Madeira)|Africa\/(Luanda|Maputo))$/;
      var esFuso = /^(Europe\/Madrid|Atlantic\/Canary|Africa\/Ceuta|America\/(Mexico_City|Cancun|Merida|Monterrey|Matamoros|Chihuahua|Ciudad_Juarez|Hermosillo|Mazatlan|Tijuana|Bahia_Banderas|Bogota|Lima|Santiago|Punta_Arenas|Buenos_Aires|Argentina\/.+|Caracas|Montevideo|Asuncion|La_Paz|Guayaquil|Guatemala|El_Salvador|Tegucigalpa|Managua|Costa_Rica|Panama|Havana|Santo_Domingo|Puerto_Rico)|Pacific\/Galapagos)$/;
      var outrosFuso = {fr: /^Europe\/(Paris|Monaco)$/, de: /^Europe\/(Berlin|Busingen|Vienna|Vaduz)$/,
                        it: /^Europe\/(Rome|San_Marino|Vatican)$/, uk: /^Europe\/(Kyiv|Kiev|Uzhgorod|Zaporozhye|Simferopol)$/};
      var langs = navigator.languages && navigator.languages.length ? navigator.languages : [navigator.language || ""];
      var quer = null;
      for (var i = 0; i < langs.length && !quer; i++) {
        var l = String(langs[i]).toLowerCase().slice(0, 2);
        if (alvos.hasOwnProperty(l)) quer = l;
      }
      if (!quer || quer === "en") {
        if (ptFuso.test(fuso)) quer = "pt"; else if (esFuso.test(fuso)) quer = "es";
        else for (var o in outrosFuso) if (outrosFuso[o].test(fuso)) quer = o;
      }
      quer = quer || "en";
      if (quer !== aqui) location.replace(alvos[quer] + location.hash);
    } catch (e) {}
  })();
</script>""" % (lingua, json.dumps(alvos))


def versao():
    """Muda quando o CSS ou o JS mudam: o navegador não fica com a versão velha guardada."""
    import hashlib
    h = hashlib.sha1()
    for arq in ("css/site.css", "js/pop3d.js", "cenas/cenas.json"):
        h.update(open(os.path.join(DOCS, arq), "rb").read())
    return h.hexdigest()[:8]


def preencher(modelo, valores):
    for _ in range(2):   # duas passadas: textos que citam outros campos (ex.: link da privacidade dentro de uma dúvida)
        for k, v in valores.items():
            modelo = modelo.replace("{{" + k + "}}", str(v))
    return modelo


def creditos(lingua):
    dados = json.load(open(os.path.join(AQUI, "creditos.json"), encoding="utf-8"))
    linhas = []
    modelo = open(os.path.join(AQUI, "modelo.html"), encoding="utf-8").read()
    cenas = sorted(set(re.findall(r'data-cena="([^"]+)"', modelo)))
    usados = sorted({gerar_cenas.CENAS[c]["arq"] for c in cenas})
    for arq in usados:
        c = dados.get(arq)
        if not c:
            continue
        titulo = html.escape(c["titulo"].replace("File:", "").rsplit(".", 1)[0])
        autor = html.escape(c["autor"] or "?")
        linhas.append(f'<p><a href="{html.escape(c["pagina"])}">{titulo}</a> · {autor} · {html.escape(c["licenca"])}</p>')
    nota = {"pt": "Fotos do Wikimedia Commons. Efeitos 3D feitos com inteligência artificial (profundidade: Depth Pro, da Apple; fundos reconstruídos: LaMa).",
            "en": "Photos from Wikimedia Commons. 3D effects made with artificial intelligence (depth: Apple's Depth Pro; rebuilt backgrounds: LaMa).",
            "es": "Fotos de Wikimedia Commons. Efectos 3D hechos con inteligencia artificial (profundidad: Depth Pro, de Apple; fondos reconstruidos: LaMa).",
            "fr": "Photos de Wikimedia Commons. Effets 3D réalisés avec l'intelligence artificielle (profondeur : Depth Pro, d'Apple ; arrière-plans reconstruits : LaMa).",
            "de": "Fotos von Wikimedia Commons. 3D-Effekte mit künstlicher Intelligenz erstellt (Tiefe: Depth Pro von Apple; rekonstruierte Hintergründe: LaMa).",
            "it": "Foto da Wikimedia Commons. Effetti 3D realizzati con l'intelligenza artificiale (profondità: Depth Pro, di Apple; sfondi ricostruiti: LaMa).",
            "uk": "Фото з Wikimedia Commons. 3D-ефекти створено штучним інтелектом (глибина: Depth Pro від Apple; відновлений фон: LaMa)."}[lingua]
    bunny = ("<p>Big Buck Bunny © 2008 Blender Foundation · www.bigbuckbunny.org · CC BY 3.0</p>"
             "<p>Spring © 2019 Blender Animation Studio · CC BY 4.0</p>")
    return f"<p>{nota}</p>{bunny}" + "".join(linhas)


GLOBO = ('<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/>'
         '<path d="M3 12h18M12 3c2.6 2.6 3.8 5.6 3.8 9s-1.2 6.4-3.8 9c-2.6-2.6-3.8-5.6-3.8-9S9.4 5.6 12 3z"/></svg>')
SETA = '<svg class="seta" viewBox="0 0 24 24" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg>'


def seletor(lingua, pagina):
    """Seletor de idioma: um botão pequeno (globo + PT) que abre a lista com o nome de cada idioma na própria
    língua. Com 7 idiomas, os botões lado a lado poluíam o topo; o menu fica do mesmo tamanho com quantos houver."""
    subir = "../" if PASTA[lingua] else ""
    itens = []
    for outra in LINGUAS:
        destino = subir + PASTA[outra] + ("" if pagina == "inicio" else PRIV[outra])
        destino = destino or "./"
        ativo = ' class="ativo" aria-current="page"' if outra == lingua else ""
        itens.append(f'<a href="{destino}" data-idioma="{outra}"{ativo} hreflang="{HREFLANG[outra]}" lang="{HREFLANG[outra]}">'
                     f'<span>{NATIVO[outra]}</span><small>{NOME[outra]}</small></a>')
    return (f'<details class="idiomas"><summary aria-label="{ROTULO[lingua]}: {NATIVO[lingua]}" title="{ROTULO[lingua]}">'
            f'{GLOBO}<span>{NOME[lingua]}</span>{SETA}</summary>'
            f'<div class="idiomas-menu">{"".join(itens)}</div></details>')


def alternativos(pagina):
    """<link rel="alternate" hreflang>: o Google mostra a versão certa para cada pessoa."""
    linhas = []
    for o in LINGUAS:
        url = "https://pop3d.quest/" + PASTA[o] + ("" if pagina == "inicio" else PRIV[o])
        linhas.append(f'<link rel="alternate" hreflang="{HREFLANG[o]}" href="{url}">')
    url_en = "https://pop3d.quest/" + PASTA["en"] + ("" if pagina == "inicio" else PRIV["en"])
    linhas.append(f'<link rel="alternate" hreflang="x-default" href="{url_en}">')
    return "\n".join(linhas)


def pilha(nome, tamanhos, extra, raiz):
    """As camadas de uma cena (fundo, meio, frente), uma imagem por cima da outra. Paradas, já formam a foto
    original; o pop3d.js só as desloca. O navegador escolhe sozinho a resolução certa (srcset)."""
    c = INDICE[nome]
    k = c["camadas"]
    limites = [0.0] + c["cortes"] + [1.0]
    z = ",".join(f"{(limites[i] + limites[i + 1]) / 2:.3f}" for i in range(k))
    ja = "ja" in extra
    imgs = []
    for i in range(k):
        base = f"{raiz}cenas/{nome}/c{i}"
        if c["pequena"]:
            fontes = f'src="{base}_p.webp" srcset="{base}_p.webp 960w, {base}.webp {c["w"]}w" sizes="{tamanhos}"'
        else:
            fontes = f'src="{base}.webp"'
        carga = (' fetchpriority="high"' if i == 0 else "") if ja else ' loading="lazy"'
        imgs.append(f'<img class="cam" {fontes} width="{c["w"]}" height="{c["h"]}" alt="" decoding="async"{carga}>')
    if "mapa" in extra:
        imgs.append(f'<img class="mapa" src="{raiz}cenas/{nome}/d.webp" alt="" decoding="async" loading="lazy">'
                    '<i class="varredura"></i>')
    return f'<div class="pilha" data-z="{z}" aria-hidden="true">' + "".join(imgs) + "</div>"


def pilhas(texto, raiz):
    return re.sub(r"\{\{pilha:([a-z0-9]+)\|([^|}]*)\|?([a-z,]*)\}\}",
                  lambda m: pilha(m.group(1), m.group(2), m.group(3).split(","), raiz), texto)


def faq(itens):
    return "\n".join(f'<details class="aparece"><summary>{p}</summary><p>{r}</p></details>' for p, r in itens)


def pagina_privacidade(lingua, t):
    p = privacidade.IDIOMAS[lingua]
    raiz = "../" if PASTA[lingua] else ""
    return f"""<!doctype html>
<html lang="{t['html_lang']}" data-raiz="{raiz}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{p['titulo']} · Pop3D</title>
<meta name="theme-color" content="#07080d">
<link rel="icon" href="{raiz}favicon.ico">
{alternativos('privacidade')}
<link rel="stylesheet" href="{raiz}css/site.css?v={versao()}">
</head>
<body>
<header class="rolou"><div class="faixa">
  <a class="marca" href="./"><i>3D</i>Pop3D</a>
  <nav>{seletor(lingua, 'privacidade')}</nav>
</div></header>
<main class="texto-legal">
  <h1>{p['titulo']}</h1>
  <p class="data">{p['atualizada']} {privacidade.DATA[lingua]}</p>
  {p['corpo']}
</main>
<footer><div class="faixa"><span>© 2026 Pop3D</span><a href="./">{p['inicio']}</a></div></footer>
<script src="{raiz}js/pop3d.js?v={versao()}" defer></script>
</body>
</html>
"""


def main():
    modelo = open(os.path.join(AQUI, "modelo.html"), encoding="utf-8").read()
    for lingua, t in textos.IDIOMAS.items():
        pasta = os.path.join(DOCS, PASTA[lingua])
        os.makedirs(pasta, exist_ok=True)
        valores = {k: v for k, v in t.items() if isinstance(v, str)}
        valores.update(
            raiz="../" if PASTA[lingua] else "",
            inicio="./",
            redirecionar=redirecionar(lingua),
            idiomas=seletor(lingua, "inicio"),
            alternativos=alternativos("inicio"),
            duvidas=faq(t["faq"]),
            versao=versao(),
            url_instalador=BAIXAR + "Pop3D_Instalador.exe",
            url_apk=BAIXAR + "Pop3D-Quest.apk",
            url_loja="https://www.meta.com/experiences/1331076283427448/",
            creditos=creditos(lingua),
            url_privacidade=PRIV[lingua],
            textos_js=json.dumps(dict(t["js"], obrigado=t["obrigado"]), ensure_ascii=False),
        )
        saida = pilhas(preencher(modelo, valores), valores["raiz"])
        assert "{{" not in saida, [l for l in saida.splitlines() if "{{" in l][:3]
        open(os.path.join(pasta, "index.html"), "w", encoding="utf-8", newline="\n").write(saida)
        open(os.path.join(pasta, PRIV[lingua]), "w", encoding="utf-8", newline="\n").write(pagina_privacidade(lingua, t))
        print("ok", lingua)


if __name__ == "__main__":
    main()
