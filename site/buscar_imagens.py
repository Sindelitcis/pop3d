# Busca imagens de licença livre no Wikimedia Commons (domínio público, CC0, CC-BY; sem "SA" nem "NC"),
# baixa em 2560 px de largura e guarda o crédito de cada uma (creditos.json) para o rodapé do site.
import json
import os
import re
import subprocess
import time
import urllib.parse

AQUI = os.path.dirname(os.path.abspath(__file__))
PASTA = os.path.join(AQUI, "originais")
API = "https://commons.wikimedia.org/w/api.php"
UA = {"User-Agent": "Pop3D-site/1.0 (https://pop3d.quest)"}
BUSCAS = {
    "bunny": "Big Buck Bunny screenshot",
    "sintel": "Sintel open movie still",
    "tears": "Tears of Steel still",
    "spring": "Spring Blender open movie",
    "lago": "mountain lake reflection featured picture",
    "praia": "tropical beach palm trees",
    "cidade": "Tokyo street night",
    "cachorro": "golden retriever portrait",
    "cascata": "waterfall forest",
    "baloes": "hot air balloons Cappadocia",
    "bolo": "birthday cake candles",
    "jogo": "SuperTuxKart screenshot",
    "flores": "tulip field",
    "gato": "cat portrait close-up",
}
LIVRE = re.compile(r"^(cc0|public domain|pd|cc by \d|cc-by-\d|cc by\b)", re.I)


def api(**p):
    p.update(format="json")
    url = API + "?" + urllib.parse.urlencode(p)
    return json.loads(baixar(url))


def baixar(url):
    """curl do Windows (usa os certificados do sistema; o Python deste PC tem uma lista antiga)."""
    r = subprocess.run(["curl", "-sSL", "--max-time", "60", "-A", UA["User-Agent"], url], capture_output=True)
    if r.returncode != 0:
        raise IOError(r.stderr.decode(errors="replace"))
    return r.stdout


def limpar_html(s):
    return re.sub(r"<[^>]+>", "", s or "").strip()


def main():
    os.makedirs(PASTA, exist_ok=True)
    creditos = {}
    for nome, busca in BUSCAS.items():
        d = api(action="query", generator="search", gsrsearch=f"filetype:bitmap {busca}", gsrnamespace=6, gsrlimit=25,
                prop="imageinfo", iiprop="url|size|extmetadata|mime", iiurlwidth=2560)
        paginas = sorted((d.get("query") or {}).get("pages", {}).values(), key=lambda p: p.get("index", 99))
        achadas = 0
        for p in paginas:
            ii = (p.get("imageinfo") or [{}])[0]
            meta = ii.get("extmetadata", {})
            lic = limpar_html(meta.get("LicenseShortName", {}).get("value"))
            if not LIVRE.match(lic) or "SA" in lic.upper().replace("USA", "") or "NC" in lic.upper():
                continue
            if ii.get("width", 0) < 1600 or ii.get("mime") not in ("image/jpeg", "image/png"):
                continue
            achadas += 1
            arq = f"{nome}{achadas}.jpg" if ii["mime"] == "image/jpeg" else f"{nome}{achadas}.png"
            with open(os.path.join(PASTA, arq), "wb") as f:
                f.write(baixar(ii.get("thumburl") or ii["url"]))
            creditos[arq] = {"titulo": p["title"], "autor": limpar_html(meta.get("Artist", {}).get("value"))[:120],
                             "licenca": lic, "pagina": ii.get("descriptionurl")}
            print(f"{arq:16s} {lic:22s} {p['title'][:70]}")
            time.sleep(0.5)
            if achadas >= 3:
                break
        if not achadas:
            print(f"(nada livre para {nome})")
    json.dump(creditos, open(os.path.join(AQUI, "creditos.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
