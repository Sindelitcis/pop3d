// Pop3D — a "mágica" do site: fotos com profundidade de verdade (mapa de profundidade feito pela IA do Pop3D),
// que se mexem com o mouse, o toque ou o giro do celular. Sem bibliotecas: WebGL puro + um pouco de CSS 3D.
(() => {
  "use strict";
  const reduzir = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const raiz = document.documentElement.dataset.raiz || "";

  // ------------------------------------------------------------------ entrada: mouse, toque e giroscópio
  const alvo = { x: 0, y: 0 };            // -1..1 (para onde a pessoa "olha")
  let ultimoGesto = -1e9;
  addEventListener("pointermove", e => {
    alvo.x = (e.clientX / innerWidth) * 2 - 1;
    alvo.y = (e.clientY / innerHeight) * 2 - 1;
    ultimoGesto = performance.now();
  }, { passive: true });
  let base = null;
  addEventListener("deviceorientation", e => {
    if (e.gamma == null) return;
    if (!base) base = { b: e.beta, g: e.gamma };
    alvo.x = Math.max(-1, Math.min(1, (e.gamma - base.g) / 18));
    alvo.y = Math.max(-1, Math.min(1, (e.beta - base.b) / 18));
    ultimoGesto = performance.now();
  }, { passive: true });
  // iPhone pede permissão para o giroscópio: pede no primeiro toque
  addEventListener("touchend", function pedir() {
    removeEventListener("touchend", pedir);
    if (typeof DeviceOrientationEvent !== "undefined" && DeviceOrientationEvent.requestPermission) {
      DeviceOrientationEvent.requestPermission().catch(() => {});
    }
  }, { once: true });

  // sem gesto há um tempo: um balanço suave sozinho (no celular parado e para quem só está lendo)
  function olhar(t, fase = 0) {
    const parado = performance.now() - ultimoGesto > 2500;
    if (reduzir) return { x: 0, y: 0 };
    if (parado) return { x: Math.sin(t / 2100 + fase) * 0.7, y: Math.sin(t / 2900 + fase * 1.7) * 0.35 };
    return alvo;
  }

  // ------------------------------------------------------------------ WebGL: foto + profundidade
  const VERT = `attribute vec2 p; varying vec2 uv; void main(){ uv = p * .5 + .5; uv.y = 1. - uv.y; gl_Position = vec4(p, 0., 1.); }`;
  const FRAG = `precision mediump float;
    varying vec2 uv;
    uniform sampler2D img, prof;
    uniform vec2 olho;       // para onde está olhando (-1..1)
    uniform float forca;     // quanto a imagem "anda" (fração da largura)
    uniform float foco;      // profundidade que fica parada (a "tela")
    uniform vec4 moldura;    // x0,y0,x1,y1: dentro dela a foto toda; fora, só o que está bem perto (sai da tela)
    uniform float limiar;    // o que é "perto o bastante" para sair da moldura
    uniform float corte;     // 0 = normal; >0 = comparação: à esquerda deste x a imagem fica plana
    uniform float anaglifo;  // 1 = modo óculos vermelho/azul
    uniform vec2 escala;     // "cover": recorte da foto para caber no quadro
    vec2 ajustar(vec2 u){ return (u - .5) * escala + .5; }
    float P(vec2 u){ return texture2D(prof, ajustar(u)).r; }
    vec2 deslocar(vec2 u, vec2 o){
      // parallax em 3 passos (refina onde cada ponto "estaria" visto deste ângulo)
      vec2 q = u;
      for (int i = 0; i < 3; i++) { q = u - o * (P(q) - foco); }
      return q;
    }
    vec4 ver(vec2 o){
      vec2 q = deslocar(uv, o);
      float d = P(q);
      vec4 c = texture2D(img, ajustar(q));
      bool dentro = uv.x > moldura.x && uv.x < moldura.z && uv.y > moldura.y && uv.y < moldura.w;
      float a = 1.;
      if (!dentro) {
        a = smoothstep(limiar, limiar + .08, d);
        // some devagar perto da borda da imagem (não aparece o "corte" da foto)
        vec2 b = min(uv, 1. - uv);
        a *= smoothstep(0., .06, min(b.x, b.y));
      }
      return vec4(c.rgb, c.a * a);
    }
    void main(){
      vec2 o = olho * forca;
      if (corte > 0. && uv.x < corte) o = vec2(0.);
      if (anaglifo > .5) {
        vec4 e = ver(o - vec2(forca * .9, 0.)), dd = ver(o + vec2(forca * .9, 0.));
        float le = dot(e.rgb, vec3(.299, .587, .114));
        gl_FragColor = vec4(le, dd.g, dd.b, max(e.a, dd.a));
      } else {
        gl_FragColor = ver(o);
      }
    }`;

  function carregar(src) {
    return new Promise((ok, erro) => { const i = new Image(); i.decoding = "async"; i.onload = () => ok(i); i.onerror = erro; i.src = src; });
  }

  class Profundo {
    constructor(canvas, op = {}) {
      this.c = canvas;
      this.op = Object.assign({ forca: .035, foco: .5, moldura: [0, 0, 1, 1], limiar: 2, fase: Math.random() * 6 }, op);
      this.visivel = false;
      this.olho = { x: 0, y: 0 };
      this.corte = 0;
      this.anaglifo = 0;
      const gl = this.gl = canvas.getContext("webgl", { premultipliedAlpha: false, alpha: true, antialias: false });
      if (!gl) { canvas.classList.add("sem-webgl"); return; }
      const sh = (tipo, src) => { const s = gl.createShader(tipo); gl.shaderSource(s, src); gl.compileShader(s); return s; };
      const pr = this.pr = gl.createProgram();
      gl.attachShader(pr, sh(gl.VERTEX_SHADER, VERT)); gl.attachShader(pr, sh(gl.FRAGMENT_SHADER, FRAG));
      gl.linkProgram(pr); gl.useProgram(pr);
      const b = gl.createBuffer(); gl.bindBuffer(gl.ARRAY_BUFFER, b);
      gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 1, -1, -1, 1, 1, 1]), gl.STATIC_DRAW);
      const p = gl.getAttribLocation(pr, "p"); gl.enableVertexAttribArray(p); gl.vertexAttribPointer(p, 2, gl.FLOAT, false, 0, 0);
      this.u = {};
      for (const n of ["img", "prof", "olho", "forca", "foco", "moldura", "limiar", "corte", "anaglifo", "escala"]) this.u[n] = gl.getUniformLocation(pr, n);
      gl.enable(gl.BLEND); gl.blendFunc(gl.SRC_ALPHA, gl.ONE_MINUS_SRC_ALPHA);
      new IntersectionObserver(es => { this.visivel = es[0].isIntersecting; }, { rootMargin: "100px" }).observe(canvas);
      new ResizeObserver(() => this.medir()).observe(canvas);
    }
    textura(i, unidade) {
      const gl = this.gl, t = gl.createTexture();
      gl.activeTexture(gl.TEXTURE0 + unidade); gl.bindTexture(gl.TEXTURE_2D, t);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR); gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE); gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
      gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, gl.RGBA, gl.UNSIGNED_BYTE, i);
    }
    async abrir(nome) {
      if (!this.gl) return this;
      const [i, d] = await Promise.all([carregar(`${raiz}img/${nome}.webp`), carregar(`${raiz}img/${nome}_prof.png`)]);
      this.proporcao = i.width / i.height;
      this.textura(i, 0); this.textura(d, 1);
      this.pronta = true;
      this.medir();
      this.c.classList.add("pronta");
      return this;
    }
    medir() {
      const r = this.c.getBoundingClientRect(), dpr = Math.min(devicePixelRatio || 1, 2);
      this.c.width = Math.max(2, Math.round(r.width * dpr)); this.c.height = Math.max(2, Math.round(r.height * dpr));
      if (this.gl) this.gl.viewport(0, 0, this.c.width, this.c.height);
      // "cover": a foto preenche o quadro sem distorcer (o que sobra fica de fora)
      if (this.op.molduraEl) {   // a "tela" desenhada no CSS: o efeito usa a posição real dela (muda no celular)
        const m = this.op.molduraEl.getBoundingClientRect(), b = 3;   // 3 px para dentro: a borda da tela aparece
        this.op.moldura = [(m.left + b - r.left) / r.width, (m.top + b - r.top) / r.height,
                           (m.right - b - r.left) / r.width, (m.bottom - b - r.top) / r.height];
      }
      const q = r.width / Math.max(1, r.height), f = this.proporcao || q;
      this.escala = q > f ? [1, f / q] : [q / f, 1];
    }
    quadro(t) {
      if (!this.pronta || !this.visivel) return;
      const o = olhar(t, this.op.fase);
      this.olho.x += (o.x - this.olho.x) * .08; this.olho.y += (o.y - this.olho.y) * .08;
      const gl = this.gl, u = this.u, m = this.op.moldura;
      gl.useProgram(this.pr);
      gl.uniform1i(u.img, 0); gl.uniform1i(u.prof, 1);
      gl.activeTexture(gl.TEXTURE0);
      gl.uniform2f(u.olho, this.olho.x, this.olho.y * .6);
      gl.uniform1f(u.forca, this.op.forca); gl.uniform1f(u.foco, this.op.foco);
      gl.uniform4f(u.moldura, m[0], m[1], m[2], m[3]); gl.uniform1f(u.limiar, this.op.limiar);
      gl.uniform1f(u.corte, this.corte); gl.uniform1f(u.anaglifo, this.anaglifo);
      gl.uniform2f(u.escala, this.escala[0], this.escala[1]);
      gl.clearColor(0, 0, 0, 0); gl.clear(gl.COLOR_BUFFER_BIT);
      gl.drawArrays(gl.TRIANGLE_STRIP, 0, 4);
    }
  }

  const cenas = [];
  function laco(t) { for (const c of cenas) c.quadro(t); requestAnimationFrame(laco); }
  requestAnimationFrame(laco);

  // herói: a foto dentro da "tela" e o que está perto sai pra fora dela
  const heroi = document.querySelector("#heroi-3d");
  if (heroi) {
    const m = .1;
    const h = new Profundo(heroi, { forca: .045, foco: .42, moldura: [m, m * 1.25, 1 - m, 1 - m * 1.25], limiar: .62,
                                    molduraEl: heroi.parentElement.querySelector(".tela-moldura") });
    h.abrir(heroi.dataset.foto).then(() => cenas.push(h));
    const botao = document.querySelector("#anaglifo");
    if (botao) botao.addEventListener("click", () => {
      h.anaglifo = h.anaglifo ? 0 : 1;
      botao.classList.toggle("ativo", !!h.anaglifo);
      document.body.classList.toggle("modo-anaglifo", !!h.anaglifo);
    });
  }

  // cartões: cada um com a sua foto em profundidade
  document.querySelectorAll("canvas[data-foto]:not(#heroi-3d):not(#comparar-3d)").forEach(c => {
    const p = new Profundo(c, { forca: +(c.dataset.forca || .03), foco: +(c.dataset.foco || .5) });
    p.abrir(c.dataset.foto).then(() => cenas.push(p));
  });

  // comparação: arraste a linha — à esquerda a tela plana de sempre, à direita o Pop3D
  const comp = document.querySelector("#comparar-3d");
  if (comp) {
    const p = new Profundo(comp, { forca: .04, foco: .45 });
    p.corte = .5;
    p.abrir(comp.dataset.foto).then(() => cenas.push(p));
    const caixa = comp.parentElement, linha = caixa.querySelector(".comparar-linha");
    const mover = x => {
      const r = caixa.getBoundingClientRect();
      const f = Math.max(.04, Math.min(.96, (x - r.left) / r.width));
      p.corte = f; linha.style.left = (f * 100) + "%";
    };
    let arrastando = false;
    caixa.addEventListener("pointerdown", e => { arrastando = true; caixa.setPointerCapture(e.pointerId); mover(e.clientX); });
    caixa.addEventListener("pointermove", e => { if (arrastando) mover(e.clientX); });
    caixa.addEventListener("pointerup", () => { arrastando = false; });
  }

  // ------------------------------------------------------------------ camadas: a foto desmontada, vista "de lado"
  const diorama = document.querySelector(".diorama[data-foto]");
  if (diorama) montarDiorama(diorama);

  async function montarDiorama(el) {
    const nome = el.dataset.foto, N = 7;
    const [i, d] = await Promise.all([carregar(`${raiz}img/${nome}.webp`), carregar(`${raiz}img/${nome}_prof.png`)]);
    const W = 800, H = Math.round(W * i.height / i.width);
    const ler = img => { const c = document.createElement("canvas"); c.width = W; c.height = H; const x = c.getContext("2d"); x.drawImage(img, 0, 0, W, H); return x.getImageData(0, 0, W, H); };
    const cor = ler(i), prof = ler(d);
    const palco = el.querySelector(".diorama-palco");
    palco.style.aspectRatio = `${W} / ${H}`;
    const planos = [];
    for (let k = 0; k < N; k++) {
      const c = document.createElement("canvas"); c.width = W; c.height = H;
      const x = c.getContext("2d"), out = x.createImageData(W, H);
      const ini = k / N, fim = (k + 1) / N;
      for (let p = 0; p < W * H; p++) {
        const v = prof.data[p * 4] / 255;
        // cada camada pega a sua faixa de profundidade (com borda suave); a do fundo pega tudo atrás
        const a = k === 0 ? (v < fim ? 1 : Math.max(0, 1 - (v - fim) * 30)) : (v >= ini - .015 && v < fim + .015 ? 1 : 0);
        out.data[p * 4] = cor.data[p * 4]; out.data[p * 4 + 1] = cor.data[p * 4 + 1]; out.data[p * 4 + 2] = cor.data[p * 4 + 2];
        out.data[p * 4 + 3] = a * 255;
      }
      x.putImageData(out, 0, 0);
      c.className = "diorama-plano";
      palco.appendChild(c);
      planos.push(c);
    }
    el.classList.add("pronta");
    // a rolagem da página gira o diorama: de frente (uma foto comum) até de lado (as camadas separadas)
    function atualizar() {
      const r = el.getBoundingClientRect();
      const total = r.height - innerHeight;
      let f = total > 0 ? Math.min(1, Math.max(0, -r.top / total)) : .5;
      if (reduzir) f = .55;
      const abre = Math.sin(Math.min(1, f / .8) * Math.PI / 2 * (f < .8 ? 1 : 1));
      const giro = abre * 58, afasta = abre;
      const passo = palco.clientWidth * .13;   // distância entre as camadas: proporcional ao tamanho (celular ou PC)
      palco.style.transform = `scale(${1 - abre * .22}) rotateY(${-giro}deg) rotateX(${abre * 8}deg)`;
      planos.forEach((c, k) => { c.style.transform = `translateZ(${(k - (N - 1) / 2) * passo * afasta}px)`; });
      el.style.setProperty("--abre", abre.toFixed(3));
      requestAnimationFrame(atualizar);
    }
    requestAnimationFrame(atualizar);
  }

  // ------------------------------------------------------------------ aparecer ao rolar (fallback para quem não tem CSS com rolagem)
  const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add("visto"); io.unobserve(e.target); } }),
    { threshold: .15 });
  document.querySelectorAll(".aparece").forEach(el => io.observe(el));

  // ------------------------------------------------------------------ botão de download: a versão mais nova publicada
  (async () => {
    const botoes = document.querySelectorAll("[data-baixar]");
    if (!botoes.length) return;
    const tx = window.POP3D_TEXTOS || {};
    try {
      const r = await fetch("https://api.github.com/repos/Sindelitcis/pop3d/releases/latest");
      if (r.status === 404) {
        botoes.forEach(b => { b.classList.add("desligado"); b.querySelector("span").textContent = tx.em_breve || "Em breve"; });
        document.querySelectorAll("[data-baixar-detalhe]").forEach(d => d.textContent = tx.forno || "");
        return;
      }
      const d = await r.json();
      const exe = (d.assets || []).find(a => /\.exe$/i.test(a.name));
      const celular = /Android|iPhone|iPad|Mobile/i.test(navigator.userAgent);
      botoes.forEach(b => { b.href = exe ? exe.browser_download_url : d.html_url; });
      const mb = exe ? ` · ${Math.round(exe.size / 1e6)} MB` : "";
      document.querySelectorAll("[data-baixar-detalhe]").forEach(el => {
        el.textContent = celular ? (tx.no_pc || "") : `${tx.versao || "Versão"} ${d.tag_name.replace(/^v/i, "")}${mb} · Windows 10 / 11`;
      });
    } catch (e) { /* sem a API: o link para a página de versões continua valendo */ }
  })();

  // ------------------------------------------------------------------ idioma: escolha guardada (o português redireciona na 1ª visita)
  document.querySelectorAll("[data-idioma]").forEach(a => a.addEventListener("click", () => {
    try { localStorage.setItem("pop3d_idioma", a.dataset.idioma); } catch (e) {}
  }));
})();
