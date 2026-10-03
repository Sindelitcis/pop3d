// Pop3D — site. As cenas 3D são fotos em camadas (fundo, meio, frente) feitas offline com IA: a profundidade do
// Depth Pro separa a foto e o LaMa reconstrói o que estava escondido atrás de cada camada. Aqui só deslizamos
// as camadas, como se a tela fosse uma janela: o que está longe anda com a sua cabeça, o que está perto anda
// ao contrário. É só mover imagens (o navegador faz isso na placa de vídeo, sem esforço), então fica nítido na
// resolução original e leve em qualquer aparelho. Sem JavaScript, as camadas paradas já formam a foto.
(() => {
  "use strict";
  const TX = window.POP3D_TEXTOS || {};
  const REDUZIR = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const TOQUE = matchMedia("(hover: none)").matches;
  const agora = () => performance.now();
  const lim = (v, a, b) => Math.max(a, Math.min(b, v));
  const suave = (a, b, x) => { const t = lim((x - a) / (b - a), 0, 1); return t * t * (3 - 2 * t); };

  // ------------------------------------------------------------------ onde está a cabeça de quem olha
  // PC: o mouse. Celular: a inclinação do aparelho (ou um balanço lento). A rolagem também conta: cada cena
  // é vista de cima quando está embaixo na tela e de baixo quando está em cima, como uma janela de verdade.
  const olho = { x: innerWidth / 2, y: innerHeight / 2, mouse: false, gx: 0, gy: 0, giro: false };
  addEventListener("pointermove", e => {
    if (e.pointerType === "touch") return;
    olho.x = e.clientX; olho.y = e.clientY; olho.mouse = true;
    acordar();
  }, { passive: true });
  let base = null;
  function aoGirar(e) {
    if (e.beta == null) return;
    if (!base) base = { b: e.beta, g: e.gamma };
    base.b += (e.beta - base.b) * 0.004;          // o "neutro" acompanha devagar o jeito de segurar
    base.g += (e.gamma - base.g) * 0.004;
    olho.gx = lim((e.gamma - base.g) / 16, -1, 1);
    olho.gy = lim((e.beta - base.b) / 16, -1, 1);
    olho.giro = true;
    acordar();
  }
  if (TOQUE && window.DeviceOrientationEvent && !REDUZIR) {
    if (typeof DeviceOrientationEvent.requestPermission === "function") {
      addEventListener("touchend", function pedir() {
        removeEventListener("touchend", pedir);
        DeviceOrientationEvent.requestPermission().then(r => { if (r === "granted") addEventListener("deviceorientation", aoGirar); }).catch(() => {});
      });
    } else addEventListener("deviceorientation", aoGirar);
  }

  // ------------------------------------------------------------------ uma cena em camadas
  class Cena {
    constructor(el) {
      this.el = el;
      this.modo = el.dataset.modo || "";
      this.janela = el.querySelector(".janela");
      this.pilhas = [...el.querySelectorAll(".pilha")];
      this.cams = [...this.pilhas[0].querySelectorAll(".cam")];
      this.z = this.pilhas[0].dataset.z.split(",").map(Number);
      this.amp = +el.dataset.amp || 0.06;
      this.foco = el.dataset.foco != null ? +el.dataset.foco : 1;
      this.fase = Math.random() * 6.28;
      this.vx = 0; this.vy = 0;
      this.visivel = false;
      this.ultimo = "";
      if (this.modo === "historia") {
        this.mapa = el.querySelector(".mapa");
        this.varredura = el.querySelector(".varredura");
        this.secao = el.closest(".historia");
      }
      this.medir();
      if (el.hasAttribute("data-saltar")) this.saltar();
    }
    medir() {
      const r = this.el.getBoundingClientRect();
      this.w = r.width || 1; this.h = r.height || 1;
      // quanto a camada que mais anda pode andar; a pilha toda cresce um tantinho para a borda nunca aparecer
      const d = Math.max(...this.z.map(z => Math.abs(this.foco - z)));
      const mx = d * this.amp, my = d * this.amp * 0.62 * this.w / this.h;
      this.zoom = this.modo === "historia" ? 1 : 1 + 2.1 * Math.max(mx, my);
      this.ultimo = "";
      this.planaPronta = false;
      if (this.fora) this.recortarFora();
    }
    // a camada da frente sai da moldura: fica fora da janela, recortada só nos lados em que ela encosta na
    // borda da foto (senão apareceria o corte reto da imagem flutuando fora da tela)
    saltar() {
      const frente = this.cams[this.cams.length - 1];
      this.fora = document.createElement("div");
      this.fora.className = "pilha fora";
      this.fora.setAttribute("aria-hidden", "true");
      this.janela.after(this.fora);
      this.fora.appendChild(frente);
      this.toca = [true, true, true, true];
      const ver = () => {
        try {
          const iw = frente.naturalWidth, ih = frente.naturalHeight;
          const k = Math.max(this.w / iw, this.h / ih);
          const sw = this.w / k, sh = this.h / k;
          const cw = 160, ch = Math.max(8, Math.round(160 * this.h / this.w));
          const c = document.createElement("canvas"); c.width = cw; c.height = ch;
          const g = c.getContext("2d", { willReadFrequently: true });
          const pos = getComputedStyle(frente).objectPosition.split(" ").map(v => parseFloat(v) / 100);
          // a imagem inteira, posicionada como o object-fit: cover a mostra (sem retângulo de origem: com srcset, o
          // tamanho "natural" já vem corrigido pela densidade e não bate com os pixels de verdade)
          const e = cw / sw;
          g.drawImage(frente, -(iw - sw) * (pos[0] || 0.5) * e, -(ih - sh) * (pos[1] || 0.5) * e, iw * e, ih * e);
          const a = g.getImageData(0, 0, cw, ch).data;
          const borda = (x0, y0, dx, dy, n) => {
            let q = 0;
            for (let i = 0; i < n; i++) if (a[((y0 + dy * i) * cw + x0 + dx * i) * 4 + 3] > 90) q++;
            return q / n > 0.015;
          };
          this.toca = [borda(0, 1, 1, 0, cw), borda(cw - 2, 0, 0, 1, ch), borda(0, ch - 2, 1, 0, cw), borda(1, 0, 0, 1, ch)];
        } catch (e) { /* sem ler a imagem: recorta nos quatro lados, como uma cena comum */ }
        this.recortarFora();
      };
      // enquanto a imagem não chega, recorta nos quatro lados; o navegador pode trocar de resolução (srcset), então confere de novo
      this.recortarFora();
      const tentar = () => (frente.decode ? frente.decode() : Promise.resolve()).then(() => { if (frente.naturalWidth) ver(); }).catch(() => {});
      tentar();
      frente.addEventListener("load", tentar);
    }
    recortarFora() {
      const r = parseFloat(getComputedStyle(this.janela).borderTopLeftRadius) || 0;
      const l = this.toca.map(t => t ? "0" : "-40%");
      this.fora.style.clipPath = `inset(${l[0]} ${l[1]} ${l[2]} ${l[3]} round ${r}px)`;
    }
    // vx, vy: de onde a pessoa olha para esta cena (-1 a 1)
    mirar(t, dt) {
      const r = this.el.getBoundingClientRect();
      const cx = r.left + r.width / 2, cy = r.top + r.height / 2;
      let ox, oy;
      if (olho.mouse) { ox = olho.x; oy = olho.y; }
      else {
        const balanco = olho.giro ? 0 : Math.sin(t * 0.00042 + this.fase) * 0.55 + Math.sin(t * 0.00097 + this.fase * 2) * 0.12;
        ox = innerWidth / 2 + (olho.gx + balanco) * innerWidth * 0.5;
        oy = innerHeight / 2 + olho.gy * innerHeight * 0.5;
      }
      const ax = lim((ox - cx) / (innerWidth * 0.5), -1, 1);
      const ay = lim((oy - cy) / (innerHeight * 0.62), -1, 1);
      const k = 1 - Math.exp(-dt / (olho.giro ? 90 : 150));
      this.vx += (ax - this.vx) * k;
      this.vy += (ay - this.vy) * k;
      this.topo = r.top; this.altura = r.height;
    }
    // deslocamento de cada camada: longe anda com a cabeça, perto anda ao contrário
    passo(i, forca) {
      const f = (this.foco - this.z[i]) * this.amp * forca;
      return [this.vx * f * this.w, this.vy * f * this.w * 0.62];
    }
    aplicar() {
      if (this.modo === "historia") return this.aplicarHistoria();
      let empurra = 0;
      if (this.el.hasAttribute("data-empurrar")) empurra = lim((innerHeight - this.topo) / (innerHeight + this.altura), 0, 1);
      const chave = `${this.vx.toFixed(4)}|${this.vy.toFixed(4)}|${empurra.toFixed(3)}|${this.w}`;
      if (chave === this.ultimo) return false;
      this.ultimo = chave;
      for (let i = 0; i < this.cams.length; i++) {
        const [dx, dy] = this.passo(i, 1);
        const s = this.zoom * (1 + empurra * 0.07 * this.z[i]);
        this.cams[i].style.transform = `translate3d(${dx.toFixed(2)}px,${dy.toFixed(2)}px,0) scale(${s.toFixed(4)})`;
      }
      if (this.pilhas[1] && !this.planaPronta) {     // comparação: o lado plano fica parado, do mesmo tamanho
        this.pilhas[1].querySelectorAll(".cam").forEach(c => { c.style.transform = `scale(${this.zoom.toFixed(4)})`; });
        this.planaPronta = true;
      }
      return true;
    }
    // a mágica por dentro: foto plana → varredura da profundidade → camadas abertas de lado → tudo junto em 3D
    aplicarHistoria() {
      const sec = this.secao;
      const r = sec.getBoundingClientRect();
      const p = lim(-r.top / Math.max(1, r.height - innerHeight), 0, 1);
      const varre = suave(0.14, 0.4, p);
      const abre = suave(0.46, 0.62, p) * (1 - suave(0.76, 0.9, p));
      const mapa = varre * (1 - suave(0.44, 0.54, p));
      const relevo = 0.12 + 0.88 * suave(0.82, 0.96, p);
      sec.style.setProperty("--prog", p.toFixed(4));
      const passo = p < 0.12 ? 0 : p < 0.44 ? 1 : p < 0.76 ? 2 : 3;
      if (passo !== this.passoAtual) {
        this.passoAtual = passo;
        sec.querySelectorAll("[data-passo]").forEach((li, i) => li.classList.toggle("atual", i === passo));
      }
      const chave = `${p.toFixed(4)}|${this.vx.toFixed(4)}|${this.vy.toFixed(4)}|${this.w}`;
      if (chave === this.ultimo) return false;
      this.ultimo = chave;
      const estreito = this.w < 700;
      const giro = abre * (estreito ? 30 : 36), incl = abre * (estreito ? 8 : 10);
      this.janela.style.transform = `rotateX(${incl.toFixed(2)}deg) rotateY(${giro.toFixed(2)}deg) scale(${(1 - abre * (estreito ? 0.2 : 0.1)).toFixed(4)})`;
      const sep = this.w * (estreito ? 0.75 : 0.62) * abre;
      for (let i = 0; i < this.cams.length; i++) {
        const [dx, dy] = this.passo(i, relevo);
        this.cams[i].style.transform = `translate3d(${dx.toFixed(2)}px,${dy.toFixed(2)}px,${((this.z[i] - 0.5) * sep).toFixed(1)}px)`;
      }
      if (this.mapa) {
        this.mapa.style.opacity = mapa.toFixed(3);
        this.mapa.style.clipPath = `inset(0 ${((1 - varre) * 100).toFixed(2)}% 0 0 round 20px)`;
        this.mapa.style.transform = `translateZ(${(0.4 * sep).toFixed(1)}px)`;
        this.varredura.style.opacity = varre > 0.001 && varre < 0.999 ? "1" : "0";
        this.varredura.style.transform = `translateX(${(varre * this.w).toFixed(1)}px)`;
      }
      return true;
    }
  }

  const cenas = REDUZIR ? [] : [...document.querySelectorAll("[data-cena]")].filter(el => el.querySelector(".pilha[data-z]")).map(el => new Cena(el));
  const vistas = new IntersectionObserver(es => {
    for (const e of es) {
      const c = e.target._cena;
      c.visivel = e.isIntersecting;
      c.el.classList.toggle("viva", e.isIntersecting);
      if (e.isIntersecting) acordar();
    }
  }, { rootMargin: "160px 0px" });
  cenas.forEach(c => { c.el._cena = c; vistas.observe(c.el); });
  if ("ResizeObserver" in window) {
    const ro = new ResizeObserver(es => { es.forEach(e => e.target._cena && e.target._cena.medir()); acordar(); });
    cenas.forEach(c => ro.observe(c.el));
  }
  if (REDUZIR) document.querySelectorAll("[data-passo]").forEach(li => li.classList.add("atual"));

  // ------------------------------------------------------------------ um laço só, e só enquanto algo se mexe
  let rodando = false, tAnt = 0, parado = 0;
  function acordar() {
    if (rodando || !cenas.length) return;
    rodando = true; parado = 0; tAnt = agora();
    requestAnimationFrame(quadro);
  }
  function quadro(t) {
    const dt = lim(t - tAnt, 1, 64); tAnt = t;
    let mexeu = false, alguma = false;
    for (const c of cenas) {
      if (!c.visivel) continue;
      alguma = true;
      c.mirar(t, dt);
      if (c.aplicar()) mexeu = true;
    }
    const balanca = !olho.mouse && !olho.giro && TOQUE;
    parado = mexeu || balanca ? 0 : parado + 1;
    if (!alguma || parado > 20 || document.hidden) { rodando = false; return; }
    requestAnimationFrame(quadro);
  }
  addEventListener("scroll", acordar, { passive: true });
  addEventListener("resize", acordar);
  document.addEventListener("visibilitychange", acordar);
  acordar();

  // ------------------------------------------------------------------ comparação: arrastar a linha
  const comp = document.querySelector(".comparar");
  if (comp) {
    let arrastando = false, tocou = false, ver = false;
    const por = f => comp.style.setProperty("--divisa", f.toFixed(4));
    const porX = x => { const r = comp.getBoundingClientRect(); por(lim((x - r.left) / r.width, 0.03, 0.97)); };
    comp.addEventListener("pointerdown", e => { arrastando = tocou = true; comp.setPointerCapture(e.pointerId); porX(e.clientX); });
    comp.addEventListener("pointermove", e => { if (arrastando) porX(e.clientX); });
    addEventListener("pointerup", () => { arrastando = false; });
    // sozinha ela passeia devagar enquanto está na tela, até alguém pegar
    const ini = agora();
    const passear = () => {
      if (tocou || !ver) return;
      por(0.5 + Math.sin((agora() - ini) / 2200) * 0.26);
      requestAnimationFrame(passear);
    };
    if (!REDUZIR) new IntersectionObserver(es => { ver = es[0].isIntersecting; if (ver) requestAnimationFrame(passear); }).observe(comp);
  }

  // ------------------------------------------------------------------ cartões: inclinam de leve com o mouse
  if (!TOQUE && !REDUZIR) document.querySelectorAll(".cartao").forEach(c => {
    c.addEventListener("pointermove", e => {
      const r = c.getBoundingClientRect();
      const x = (e.clientX - r.left) / r.width, y = (e.clientY - r.top) / r.height;
      c.style.transform = `perspective(1100px) rotateX(${((0.5 - y) * 4).toFixed(2)}deg) rotateY(${((x - 0.5) * 5).toFixed(2)}deg)`;
    });
    c.addEventListener("pointerleave", () => { c.style.transform = ""; });
  });

  // ------------------------------------------------------------------ aparecer ao rolar
  const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add("visto"); io.unobserve(e.target); } }),
    { threshold: 0.12 });
  document.querySelectorAll(".aparece").forEach(el => io.observe(el));

  // ------------------------------------------------------------------ download: link direto do instalador mais novo
  // O botão já aponta para .../releases/latest/download/Pop3D_Instalador.exe (sempre a versão mais nova).
  // Aqui só completamos a versão e o tamanho, e mostramos o que fazer depois de baixar.
  (async () => {
    const botoes = document.querySelectorAll("[data-baixar]");
    if (!botoes.length) return;
    const detalhes = document.querySelectorAll("[data-baixar-detalhe]");
    const celular = /Android|iPhone|iPad|Mobile/i.test(navigator.userAgent);
    if (celular) detalhes.forEach(d => d.textContent = TX.no_pc || "");
    botoes.forEach(b => b.addEventListener("click", () => { if (!celular && !b.classList.contains("desligado")) avisar(); }));
    try {
      const r = await fetch("https://api.github.com/repos/Sindelitcis/pop3d/releases/latest");
      if (r.status === 404) {
        botoes.forEach(b => { b.classList.add("desligado"); b.querySelector("span").textContent = TX.em_breve || "Em breve"; });
        detalhes.forEach(d => d.textContent = TX.forno || "");
        document.querySelectorAll(".link-apk").forEach(a => a.hidden = true);
        return;
      }
      if (!r.ok) return;
      const d = await r.json();
      const exe = (d.assets || []).find(a => /\.exe$/i.test(a.name));
      if (exe) botoes.forEach(b => { b.href = exe.browser_download_url; });
      if (!(d.assets || []).some(a => /\.apk$/i.test(a.name))) document.querySelectorAll(".link-apk").forEach(a => a.hidden = true);
      if (!celular) {
        const mb = exe ? ` · ${Math.max(1, Math.round(exe.size / 1e6))} MB` : "";
        detalhes.forEach(el => { el.textContent = `${TX.versao || "Versão"} ${d.tag_name.replace(/^v/i, "")}${mb} · Windows 10 / 11 · NVIDIA RTX`; });
      }
    } catch (e) { /* sem a API, o link direto continua valendo */ }
  })();
  let aviso = null;
  function avisar() {
    if (!TX.obrigado) return;
    if (!aviso) {
      aviso = document.createElement("div");
      aviso.className = "aviso-baixar";
      aviso.setAttribute("role", "status");
      aviso.innerHTML = `<p>${TX.obrigado}</p><button type="button" aria-label="OK">×</button>`;
      aviso.querySelector("button").addEventListener("click", () => aviso.classList.remove("aberto"));
      document.body.appendChild(aviso);
    }
    requestAnimationFrame(() => aviso.classList.add("aberto"));
    clearTimeout(aviso._t);
    aviso._t = setTimeout(() => aviso.classList.remove("aberto"), 14000);
  }

  // ------------------------------------------------------------------ idioma: escolha guardada (a 1ª visita vai sozinha para o idioma certo)
  document.querySelectorAll("[data-idioma]").forEach(a => a.addEventListener("click", () => {
    try { localStorage.setItem("pop3d_idioma", a.dataset.idioma); } catch (e) {}
  }));
})();
