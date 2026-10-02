# Monta o site do Pop3D (pasta docs, publicada pelo GitHub Pages) nos três idiomas.
# Uso: python construir.py   (depois é só commit + push no repositório pop3d)
import html
import json
import os

import gerar_profundidade
import privacidade
import textos

AQUI = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.join(AQUI, "..", "docs")
PASTA = {"pt": "", "en": "en/", "es": "es/"}
PRIV = {"pt": "privacidade.html", "en": "privacy.html", "es": "privacidad.html"}
NOME = {"pt": "PT", "en": "EN", "es": "ES"}

REDIRECIONAR = """<script>
  // 1ª visita de quem não fala português: vai para o idioma dela (a escolha manual fica guardada e vale depois)
  try {
    const salvo = localStorage.getItem("pop3d_idioma"), lingua = (navigator.language || "").toLowerCase();
    if (!salvo && !lingua.startsWith("pt")) location.replace(lingua.startsWith("es") ? "es/" : "en/");
  } catch (e) {}
</script>"""


def preencher(modelo, valores):
    for _ in range(2):   # duas passadas: textos que citam outros campos (ex.: link da privacidade dentro de uma dúvida)
        for k, v in valores.items():
            modelo = modelo.replace("{{" + k + "}}", str(v))
    return modelo


def creditos(lingua):
    dados = json.load(open(os.path.join(AQUI, "creditos.json"), encoding="utf-8"))
    linhas = []
    usados = sorted({arq for arq, _ in gerar_profundidade.ESCOLHIDAS.values()})
    for arq in usados:
        c = dados.get(arq)
        if not c:
            continue
        titulo = html.escape(c["titulo"].replace("File:", "").rsplit(".", 1)[0])
        autor = html.escape(c["autor"] or "?")
        linhas.append(f'<p><a href="{html.escape(c["pagina"])}">{titulo}</a> · {autor} · {html.escape(c["licenca"])}</p>')
    nota = {"pt": "Fotos do Wikimedia Commons. Os mapas de profundidade foram feitos pelo Pop3D.",
            "en": "Photos from Wikimedia Commons. Depth maps made by Pop3D.",
            "es": "Fotos de Wikimedia Commons. Los mapas de profundidad fueron hechos por Pop3D."}[lingua]
    bunny = "<p>Big Buck Bunny © 2008 Blender Foundation · www.bigbuckbunny.org · CC BY 3.0</p>"
    return f"<p>{nota}</p>{bunny}" + "".join(linhas)


def seletor(lingua, pagina):
    """Links PT · EN · ES apontando para a mesma página nos outros idiomas."""
    subir = "../" if PASTA[lingua] else ""
    partes = []
    for outra in ("pt", "en", "es"):
        destino = subir + PASTA[outra] + ("" if pagina == "inicio" else PRIV[outra])
        destino = destino or "./"
        ativo = ' class="ativo"' if outra == lingua else ""
        partes.append(f'<a href="{destino}" data-idioma="{outra}"{ativo} hreflang="{outra}">{NOME[outra]}</a>')
    return "".join(partes)


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
<link rel="stylesheet" href="{raiz}css/site.css">
</head>
<body>
<header class="rolou"><div class="faixa">
  <a class="marca" href="./"><i>3D</i>Pop3D</a>
  <nav><span class="idiomas">{seletor(lingua, 'privacidade')}</span></nav>
</div></header>
<main class="texto-legal">
  <h1>{p['titulo']}</h1>
  <p class="data">{p['atualizada']} {privacidade.DATA[lingua]}</p>
  {p['corpo']}
</main>
<footer><div class="faixa"><span>© 2026 Pop3D</span><a href="./">{p['inicio']}</a></div></footer>
<script src="{raiz}js/pop3d.js" defer></script>
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
            redirecionar=REDIRECIONAR if lingua == "pt" else "",
            idiomas=seletor(lingua, "inicio"),
            duvidas=faq(t["faq"]),
            creditos=creditos(lingua),
            url_privacidade=PRIV[lingua],
            textos_js=json.dumps(t["js"], ensure_ascii=False),
        )
        saida = preencher(modelo, valores)
        assert "{{" not in saida, [l for l in saida.splitlines() if "{{" in l][:3]
        open(os.path.join(pasta, "index.html"), "w", encoding="utf-8", newline="\n").write(saida)
        open(os.path.join(pasta, PRIV[lingua]), "w", encoding="utf-8", newline="\n").write(pagina_privacidade(lingua, t))
        print("ok", lingua)


if __name__ == "__main__":
    main()
