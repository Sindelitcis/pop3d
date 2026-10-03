// Pop3D — site. Motor 3D próprio (WebGL2): cada foto vem em camadas (fundo, meio, frente), cada camada vira
// uma malha com a profundidade do Depth Pro e o que estava escondido atrás dos objetos já vem reconstruído.
// A tela funciona como uma janela de verdade: o que está atrás do vidro fica dentro da moldura, o que está
// na frente pode sair dela. Sem WebGL2, fica a foto comum.
(() => {
  "use strict";
  const RAIZ = document.documentElement.dataset.raiz || "";
  const TX = window.POP3D_TEXTOS || {};
  const REDUZIR = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const TOQUE = matchMedia("(hover: none)").matches;
  const DPR = Math.min(window.devicePixelRatio || 1, TOQUE ? 1.75 : 2);
  const agora = () => performance.now();
  // qualidade adaptativa: se o aparelho não acompanhar, a resolução do 3D baixa aos poucos (até a metade)
  let QUAL = 1;

  // ------------------------------------------------------------------ para onde a pessoa está "olhando"
  // mouse (PC), inclinação do celular, ou um balanço lento quando ninguém mexe
  const olho = { x: 0, y: 0, alvoX: 0, alvoY: 0, mexeu: -1e9, giro: false };
  addEventListener("pointermove", e => {
    if (e.pointerType === "touch") return;
    olho.alvoX = e.clientX / innerWidth * 2 - 1;
    olho.alvoY = e.clientY / innerHeight * 2 - 1;
    olho.mexeu = agora();
  }, { passive: true });
  let base = null;
  function aoGirar(e) {
    if (e.beta == null) return;
    if (!base) base = { b: e.beta, g: e.gamma };
    base.b += (e.beta - base.b) * 0.004;        // a posição "neutra" acompanha devagar o jeito de segurar
    base.g += (e.gamma - base.g) * 0.004;
    olho.alvoX = Math.max(-1, Math.min(1, (e.gamma - base.g) / 18));
    olho.alvoY = Math.max(-1, Math.min(1, (e.beta - base.b) / 18));
    olho.mexeu = agora();
    olho.giro = true;
  }
  if (window.DeviceOrientationEvent) {
    if (typeof DeviceOrientationEvent.requestPermission === "function") {
      addEventListener("touchend", function pedir() {
        removeEventListener("touchend", pedir);
        DeviceOrientationEvent.requestPermission().then(r => { if (r === "granted") addEventListener("deviceorientation", aoGirar); }).catch(() => {});
      });
    } else addEventListener("deviceorientation", aoGirar);
  }
  function olhar(t, fase) {
    const parado = Math.min(1, Math.max(0, (agora() - olho.mexeu - 2200) / 1800));
    const bx = Math.sin(t * 0.00031 + fase) * 0.85 + Math.sin(t * 0.00071 + fase * 2.1) * 0.15;
    const by = Math.sin(t * 0.00043 + fase * 1.7) * 0.55;
    return [olho.x * (1 - parado) + bx * parado, olho.y * (1 - parado) + by * parado];
  }

  // ------------------------------------------------------------------ matemática mínima (matrizes 4x4, coluna a coluna)
  function mul(a, b) {
    const o = new Float32Array(16);
    for (let c = 0; c < 4; c++) for (let r = 0; r < 4; r++) {
      o[c * 4 + r] = a[r] * b[c * 4] + a[4 + r] * b[c * 4 + 1] + a[8 + r] * b[c * 4 + 2] + a[12 + r] * b[c * 4 + 3];
    }
    return o;
  }
  function frustum(l, r, b, t, n, f) {
    return new Float32Array([2 * n / (r - l), 0, 0, 0, 0, 2 * n / (t - b), 0, 0,
      (r + l) / (r - l), (t + b) / (t - b), -(f + n) / (f - n), -1, 0, 0, -2 * f * n / (f - n), 0]);
  }
  function olharPara(e, a) {
    let zx = e[0] - a[0], zy = e[1] - a[1], zz = e[2] - a[2];
    let n = Math.hypot(zx, zy, zz); zx /= n; zy /= n; zz /= n;
    let xx = zz, xy = 0, xz = -zx;               // cima = (0, 1, 0)
    n = Math.hypot(xx, xy, xz) || 1; xx /= n; xy /= n; xz /= n;
    const yx = zy * xz - zz * xy, yy = zz * xx - zx * xz, yz = zx * xy - zy * xx;
    return new Float32Array([xx, yx, zx, 0, xy, yy, zy, 0, xz, yz, zz, 0,
      -(xx * e[0] + xy * e[1] + xz * e[2]), -(yx * e[0] + yy * e[1] + yz * e[2]), -(zx * e[0] + zy * e[1] + zz * e[2]), 1]);
  }

  // ------------------------------------------------------------------ shaders
  const VS_CAMADA = `#version 300 es
precision highp float;
in vec2 aP;
uniform sampler2D uProf;
uniform vec4 uCanal;
uniform mat4 uPV;
uniform vec2 uMeio;
uniform float uForca, uFoco, uSep, uDist;
out vec2 vUv; out float vZ; out float vD;
void main() {
  vUv = aP;
  float d = dot(textureLod(uProf, aP, 0.0), uCanal);
  vD = d;
  float z = (d - uFoco) * uForca + uSep;
  vZ = z;
  // compensa a perspectiva: com a câmera no centro, a cena fica idêntica à foto (nada encolhe nem sobra borda)
  float k = (uDist - (z - uSep)) / uDist;
  gl_Position = uPV * vec4((aP.x * 2.0 - 1.0) * uMeio.x * k, (1.0 - aP.y * 2.0) * uMeio.y * k, z, 1.0);
}`;
  const FS_COMUM = `
uniform vec4 uJan; uniform float uRaio, uUsaJan, uForca;
float caixa(vec2 p, vec4 r, float raio) {
  vec2 c = (r.xy + r.zw) * 0.5, h = (r.zw - r.xy) * 0.5 - raio, q = abs(p - c) - h;
  return length(max(q, 0.0)) + min(max(q.x, q.y), 0.0) - raio;
}
float janela(float z) {
  if (uUsaJan < 0.001) return 1.0;
  float dentro = 1.0 - smoothstep(-0.8, 0.8, caixa(gl_FragCoord.xy, uJan, uRaio));
  float frente = smoothstep(0.0, max(uForca, 0.05) * 0.1, z);    // na frente do vidro: pode sair da moldura
  return mix(1.0, max(dentro, frente), uUsaJan);
}`;
  const FS_CAMADA = `#version 300 es
precision highp float;
in vec2 vUv; in float vZ; in float vD;
uniform sampler2D uCor;
uniform float uMapa, uVarre, uAlfa, uBorda, uNevoaF, uBrilho, uContorno;
uniform vec3 uNevoa;
out vec4 cor;
${FS_COMUM}
vec3 turbo(float x) {
  x = clamp(x, 0.0, 1.0);
  vec4 v4 = vec4(1.0, x, x * x, x * x * x);
  vec2 v2 = v4.zw * v4.z;
  return clamp(vec3(
    dot(v4, vec4(0.13572138, 4.61539260, -42.66032258, 132.13108234)) + dot(v2, vec2(-152.94239396, 59.28637943)),
    dot(v4, vec4(0.09140261, 2.19418839, 4.84296658, -14.18503333)) + dot(v2, vec2(4.27729857, 2.82956604)),
    dot(v4, vec4(0.10667330, 12.64194608, -60.58204836, 110.36276771)) + dot(v2, vec2(-89.90310912, 27.34824973))), 0.0, 1.0);
}
void main() {
  vec4 c = texture(uCor, vUv);
  // nada é cortado: as bordas vêm do recorte de cada camada (alfa suave, na resolução da foto)
  float a = 1.0;
  vec2 e = min(vUv, 1.0 - vUv);
  a *= smoothstep(0.0, uBorda, min(e.x, e.y));
  a *= janela(vZ) * uAlfa;
  vec3 rgb = c.rgb;
  if (uMapa > 0.001) {
    float m = uMapa * step(vUv.x, uVarre);
    rgb = mix(rgb, turbo(vD) * c.a, m);
    float linha = exp(-pow((vUv.x - uVarre) * 90.0, 2.0)) * step(uVarre, 0.999) * uMapa;
    rgb += vec3(0.55, 0.85, 1.0) * linha * c.a * 1.4;
  }
  rgb = mix(rgb, uNevoa * c.a, clamp((1.0 - vD) * uNevoaF, 0.0, 1.0));
  if (uContorno > 0.001) {
    // vista explodida: contorno de luz em cada camada (silhueta e borda da foto)
    float sil = clamp(fwidth(c.a) * 3.0, 0.0, 1.0);
    float borda = 1.0 - smoothstep(0.0, 0.006, min(e.x, e.y));
    rgb += vec3(0.45, 0.65, 1.0) * max(sil, borda * c.a) * uContorno * 0.9;
    rgb *= 1.0 - 0.25 * uContorno * (1.0 - vD);
  }
  rgb *= uBrilho;
  cor = vec4(rgb, c.a) * a;
  if (cor.a < 0.002) discard;
}`;
  const VS_PART = `#version 300 es
precision highp float;
in vec4 aQ;
uniform mat4 uPV; uniform vec2 uMeio; uniform vec2 uZ;
uniform float uT, uTam, uVel, uCai;
out float vA; out float vZ; out float vS;
void main() {
  float s = aQ.w;
  float t = uT * 0.001 * uVel;
  float x = fract(aQ.x + sin(t * 0.3 + s * 37.0) * 0.012 + t * 0.004 * (s - 0.5));
  float y = mix(fract(aQ.y + t * 0.006 * (0.4 + s)), 1.0 - fract(aQ.y + t * 0.03 * (0.5 + s)), uCai);
  vec3 p = vec3((x * 2.0 - 1.0) * uMeio.x * 1.08, (y * 2.0 - 1.0) * uMeio.y * 1.05, mix(uZ.x, uZ.y, aQ.z));
  vec4 c = uPV * vec4(p, 1.0);
  gl_Position = c;
  gl_PointSize = uTam * (0.45 + s * s) / c.w;
  vA = 0.25 + 0.75 * (0.5 + 0.5 * sin(uT * 0.0016 * (0.4 + s) + s * 91.0));
  vZ = p.z; vS = s;
}`;
  const FS_PART = `#version 300 es
precision highp float;
in float vA; in float vZ; in float vS;
uniform vec3 uCor1, uCor2; uniform float uForte;
out vec4 cor;
${FS_COMUM}
void main() {
  vec2 q = gl_PointCoord * 2.0 - 1.0;
  float r = dot(q, q);
  float a = exp(-r * 4.0) + exp(-r * 40.0) * 0.6;
  a *= vA * uForte * janela(vZ);
  cor = vec4(mix(uCor1, uCor2, vS) * a, 0.0);
}`;

  function programa(gl, vs, fs) {
    const p = gl.createProgram();
    for (const [tipo, src] of [[gl.VERTEX_SHADER, vs], [gl.FRAGMENT_SHADER, fs]]) {
      const s = gl.createShader(tipo);
      gl.shaderSource(s, src); gl.compileShader(s);
      if (!gl.getShaderParameter(s, gl.COMPILE_STATUS)) throw new Error(gl.getShaderInfoLog(s));
      gl.attachShader(p, s);
    }
    gl.linkProgram(p);
    if (!gl.getProgramParameter(p, gl.LINK_STATUS)) throw new Error(gl.getProgramInfoLog(p));
    const u = {};
    const n = gl.getProgramParameter(p, gl.ACTIVE_UNIFORMS);
    for (let i = 0; i < n; i++) { const nome = gl.getActiveUniform(p, i).name; u[nome] = gl.getUniformLocation(p, nome); }
    return { p, u };
  }

  // ------------------------------------------------------------------ dados das cenas
  let indice = null;
  const pegarIndice = () => indice || (indice = fetch(RAIZ + "cenas/cenas.json").then(r => r.json()));
  const imagens = new Map();
  function imagem(url) {
    if (!imagens.has(url)) imagens.set(url, new Promise((ok, erro) => {
      const im = new Image();
      im.decoding = "async";
      im.onload = () => ok(im); im.onerror = erro;
      im.src = url;
    }));
    return imagens.get(url);
  }

  const PARTICULAS = {
    poeira:   { n: 260, cor1: [1.0, 0.86, 0.55], cor2: [1.0, 0.98, 0.85], tam: 26, vel: 1, cai: 0, forte: 0.55 },
    vagalume: { n: 120, cor1: [0.75, 1.0, 0.45], cor2: [1.0, 0.9, 0.4], tam: 34, vel: 1.4, cai: 0, forte: 0.9 },
    neve:     { n: 320, cor1: [0.9, 0.95, 1.0], cor2: [1.0, 1.0, 1.0], tam: 18, vel: 0.6, cai: 1, forte: 0.55 },
    brilho:   { n: 200, cor1: [1.0, 0.75, 0.45], cor2: [1.0, 0.55, 0.85], tam: 30, vel: 0.8, cai: 0, forte: 0.7 },
    luzes:    { n: 220, cor1: [0.45, 0.75, 1.0], cor2: [1.0, 0.55, 0.9], tam: 28, vel: 0.5, cai: 0, forte: 0.45 },
  };

  // ------------------------------------------------------------------ um palco = um canvas com uma cena
  const palcos = [];
  let ativos = 0;
  const LIMITE = TOQUE ? 6 : 10;      // navegadores aguentam ~16 contextos WebGL; folga para não perder nenhum

  class Palco {
    constructor(el) {
      this.el = el;
      this.nome = el.dataset.cena;
      this.janelaEl = el.querySelector("[data-janela]") || el;
      this.canvas = el.querySelector("canvas");
      this.op = {
        forca: parseFloat(el.dataset.forca || ".35"), foco: el.dataset.foco, amp: parseFloat(el.dataset.amp || "1"),
        margem: parseFloat(el.dataset.margem || "0"), raio: parseFloat(el.dataset.raio || "18"),
        part: el.dataset.particulas, nevoa: parseFloat(el.dataset.nevoa || "0"), modo: el.dataset.modo || "janela",
      };
      this.fase = Math.random() * 10;
      this.local = { x: 0, y: 0, alvoX: 0, alvoY: 0, dentro: false };
      this.visivel = false; this.perto = false; this.gl = null; this.pronto = false;
      this.progresso = 0; this.divisa = 0.5; this.anaglifo = false;
      if (!TOQUE) {
        el.addEventListener("pointermove", e => {
          const r = this.janelaEl.getBoundingClientRect();
          this.local.alvoX = ((e.clientX - r.left) / r.width) * 2 - 1;
          this.local.alvoY = ((e.clientY - r.top) / r.height) * 2 - 1;
          this.local.dentro = true;
        });
        el.addEventListener("pointerleave", () => { this.local.dentro = false; this.local.alvoX = 0; this.local.alvoY = 0; });
      }
    }

    async iniciar() {
      if (this.gl || this.iniciando) return;
      this.iniciando = true;
      try {
        const idx = await pegarIndice();
        const info = idx[this.nome];
        if (!info) return;
        this.info = info;
        this.medir();
        const pequena = info.pequena && this.cw * DPR < 1250;
        const suf = pequena ? "_p" : "";
        const pasta = `${RAIZ}cenas/${this.nome}/`;
        const urls = [pasta + `p${suf}.webp`];
        for (let i = 0; i < info.camadas; i++) urls.push(pasta + `c${i}${suf}.webp`);
        const ims = await Promise.all(urls.map(imagem));
        if (!this.perto) return;
        if (ativos >= LIMITE) liberarLonge(this);
        this.montar(ims);
      } catch (e) {
        console.warn("Pop3D: cena", this.nome, e);
        this.el.classList.add("sem-3d");
      } finally { this.iniciando = false; }
    }

    montar(ims) {
      const gl = this.canvas.getContext("webgl2", { premultipliedAlpha: true, antialias: true, alpha: true });
      if (!gl) { this.el.classList.add("sem-3d"); return; }
      this.gl = gl; ativos++;
      this.canvas.addEventListener("webglcontextlost", e => { e.preventDefault(); this.soltar(true); }, { once: true });
      this.pc = programa(gl, VS_CAMADA, FS_CAMADA);
      this.pp = programa(gl, VS_PART, FS_PART);
      const tex = (im, cor) => {
        const t = gl.createTexture();
        gl.bindTexture(gl.TEXTURE_2D, t);
        gl.pixelStorei(gl.UNPACK_PREMULTIPLY_ALPHA_WEBGL, cor);
        gl.pixelStorei(gl.UNPACK_COLORSPACE_CONVERSION_WEBGL, cor ? gl.BROWSER_DEFAULT_WEBGL : gl.NONE);
        gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, gl.RGBA, gl.UNSIGNED_BYTE, im);
        gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE);
        gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
        gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
        if (cor) {
          gl.generateMipmap(gl.TEXTURE_2D);
          gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR_MIPMAP_LINEAR);
          const an = gl.getExtension("EXT_texture_filter_anisotropic");
          if (an) gl.texParameterf(gl.TEXTURE_2D, an.TEXTURE_MAX_ANISOTROPY_EXT, 4);
        } else gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR);
        return t;
      };
      this.tProf = tex(ims[0], false);
      this.tCor = ims.slice(1).map(im => tex(im, true));

      // malha: uma grade fininha (cada célula tem poucos pixels, então os degraus cortados ficam estreitos)
      const asp = this.info.w / this.info.h;
      const nx = Math.round(Math.min(TOQUE ? 200 : 300, Math.max(90, this.jw / 3.2))), ny = Math.max(2, Math.round(nx / asp));
      const v = new Float32Array((nx + 1) * (ny + 1) * 2);
      let k = 0;
      for (let j = 0; j <= ny; j++) for (let i = 0; i <= nx; i++) { v[k++] = i / nx; v[k++] = j / ny; }
      const ind = new Uint32Array(nx * ny * 6);
      k = 0;
      for (let j = 0; j < ny; j++) for (let i = 0; i < nx; i++) {
        const a = j * (nx + 1) + i, b = a + 1, c = a + nx + 1, d = c + 1;
        ind[k++] = a; ind[k++] = c; ind[k++] = b; ind[k++] = b; ind[k++] = c; ind[k++] = d;
      }
      this.nInd = ind.length;
      this.vao = gl.createVertexArray();
      gl.bindVertexArray(this.vao);
      gl.bindBuffer(gl.ARRAY_BUFFER, gl.createBuffer());
      gl.bufferData(gl.ARRAY_BUFFER, v, gl.STATIC_DRAW);
      const loc = gl.getAttribLocation(this.pc.p, "aP");
      gl.enableVertexAttribArray(loc);
      gl.vertexAttribPointer(loc, 2, gl.FLOAT, false, 0, 0);
      gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, gl.createBuffer());
      gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, ind, gl.STATIC_DRAW);

      const tp = PARTICULAS[this.op.part];
      if (tp && !REDUZIR) {
        const n = Math.round(tp.n * (TOQUE ? 0.6 : 1));
        const q = new Float32Array(n * 4);
        for (let i = 0; i < n * 4; i++) q[i] = Math.random();
        this.part = { tp, n, vao: gl.createVertexArray() };
        gl.bindVertexArray(this.part.vao);
        gl.bindBuffer(gl.ARRAY_BUFFER, gl.createBuffer());
        gl.bufferData(gl.ARRAY_BUFFER, q, gl.STATIC_DRAW);
        const lq = gl.getAttribLocation(this.pp.p, "aQ");
        gl.enableVertexAttribArray(lq);
        gl.vertexAttribPointer(lq, 4, gl.FLOAT, false, 0, 0);
      }
      gl.bindVertexArray(null);
      const c = this.info.cortes;
      this.foco = this.op.foco != null ? parseFloat(this.op.foco) : (c[c.length - 1] || 0.5);
      this.nascer = agora();
      this.pronto = true;
      this.el.classList.add("com-3d");
    }

    soltar(perdido) {
      if (!this.gl) return;
      if (!perdido) { const ext = this.gl.getExtension("WEBGL_lose_context"); if (ext) ext.loseContext(); }
      this.gl = null; this.pronto = false; this.part = null; ativos--;
      // canvas novo: um contexto perdido não volta no mesmo elemento
      const novo = this.canvas.cloneNode(false);
      this.canvas.replaceWith(novo); this.canvas = novo;
      this.el.classList.remove("com-3d");
    }

    medir() {
      const r = this.canvas.getBoundingClientRect(), j = this.janelaEl.getBoundingClientRect();
      this.cw = Math.max(1, r.width); this.ch = Math.max(1, r.height);
      this.jx = j.left - r.left; this.jy = j.top - r.top; this.jw = Math.max(1, j.width); this.jh = Math.max(1, j.height);
      const E = DPR * QUAL;
      this.E = E;
      const w = Math.round(this.cw * E), h = Math.round(this.ch * E);
      if (this.canvas.width !== w || this.canvas.height !== h) { this.canvas.width = w; this.canvas.height = h; }
    }

    camera(ex, ey, giro) {
      // mundo: a janela tem altura 2 no plano z = 0; a foto cobre a janela (com uma folga para a câmera andar)
      const asp = this.info.w / this.info.h, jasp = this.jw / this.jh;
      const folga = 1.05 + 0.03 * this.op.amp;
      const s = (asp > jasp ? 2 / this.jh : 2 * asp / this.jw) / folga;     // mundo por pixel
      this.meio = [asp, 1];
      const cx0 = this.jx + this.jw / 2, cy0 = this.jy + this.jh / 2;
      const X0 = -cx0 * s, X1 = (this.cw - cx0) * s, Y0 = -(this.ch - cy0) * s, Y1 = cy0 * s;
      const H = this.jh * s;
      const D = H * 1.7;
      this.dist = D;
      const amp = H * 0.16 * this.op.amp;
      const ox = ex * amp, oy = -ey * amp * 0.7;
      const n = D * 0.05, f = D * 8;
      if (!giro) {
        const P = frustum((X0 - ox) * n / D, (X1 - ox) * n / D, (Y0 - oy) * n / D, (Y1 - oy) * n / D, n, f);
        return mul(P, new Float32Array([1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, -ox, -oy, -D, 1]));
      }
      // giro (a cena vista de lado): câmera em órbita, afastando um pouco para caber tudo
      const [yaw, pitch, zoom] = giro;
      const R = D * zoom;
      const e = [Math.sin(yaw) * Math.cos(pitch) * R + ox * 0.3, Math.sin(pitch) * R + oy * 0.3, Math.cos(yaw) * Math.cos(pitch) * R];
      const P = frustum(X0 * n / D, X1 * n / D, Y0 * n / D, Y1 * n / D, n, f);
      return mul(P, olharPara(e, [0, 0, -H * 0.08 * (zoom - 1)]));
    }

    desenhar(t) {
      const gl = this.gl;
      if (!gl || !this.pronto) return;
      this.medir();
      // suaviza a entrada (global ou do mouse em cima do próprio cartão)
      const [gx, gy] = olhar(t, this.fase);
      const L = this.local;
      L.x += ((L.dentro ? L.alvoX : 0) - L.x) * 0.08; L.y += ((L.dentro ? L.alvoY : 0) - L.y) * 0.08;
      let ex = L.dentro ? L.x * 1.25 : gx, ey = L.dentro ? L.y * 1.25 : gy;
      if (REDUZIR) { ex *= 0.25; ey *= 0.25; }
      const surgir = Math.min(1, (agora() - this.nascer) / 1400);
      const ease = 1 - Math.pow(1 - surgir, 3);

      gl.viewport(0, 0, this.canvas.width, this.canvas.height);
      gl.clearColor(0, 0, 0, 0);
      gl.clear(gl.COLOR_BUFFER_BIT);
      gl.enable(gl.BLEND);
      gl.blendFunc(gl.ONE, gl.ONE_MINUS_SRC_ALPHA);

      const p = this.op.modo === "historia" ? historia(this.progresso) : null;
      // tela estreita (celular): a maquete aberta precisa de mais distância para caber de lado a lado
      const giro = p ? [p.yaw, p.pitch, p.zoom * (1 + p.abre * Math.max(0, Math.min(0.8, (760 - this.cw) / 500)))] : null;
      const forcaBase = this.op.forca * 2 * (p ? p.forca : 1) * (0.35 + 0.65 * ease);
      const jan = [this.jx * this.E, (this.ch - this.jy - this.jh) * this.E, (this.jx + this.jw) * this.E, (this.ch - this.jy) * this.E];
      const comum = { jan, forcaBase, p, ease };

      if (this.op.modo === "comparar") {
        // à esquerda da linha: a tela plana de sempre; à direita: com profundidade
        const xd = Math.round((this.jx + this.jw * this.divisa) * this.E);
        gl.enable(gl.SCISSOR_TEST);
        gl.scissor(0, 0, xd, this.canvas.height);
        this.passada(this.camera(0, 0, null), { ...comum, forcaBase: 0, plano: true });
        gl.scissor(xd, 0, this.canvas.width - xd, this.canvas.height);
        this.passada(this.camera(ex * 1.2, ey * 1.2, null), comum);
        gl.disable(gl.SCISSOR_TEST);
      } else if (this.anaglifo) {
        const sep = 0.55;
        gl.colorMask(true, false, false, true);
        this.passada(this.camera(ex - sep, ey, giro), comum);
        gl.colorMask(false, true, true, true);
        this.passada(this.camera(ex + sep, ey, giro), comum);
        gl.colorMask(true, true, true, true);
      } else {
        this.passada(this.camera(ex, ey, giro), comum);
      }
    }

    passada(PV, { jan, forcaBase, p, ease, plano }) {
      const gl = this.gl, u = this.pc.u;
      gl.useProgram(this.pc.p);
      gl.bindVertexArray(this.vao);
      gl.uniformMatrix4fv(u.uPV, false, PV);
      gl.uniform2f(u.uMeio, this.meio[0], this.meio[1]);
      gl.uniform4f(u.uJan, ...jan);
      gl.uniform1f(u.uRaio, this.op.raio * this.E);
      gl.uniform1f(u.uUsaJan, this.op.margem > 0 ? (p ? 1 - p.abre : 1) : 0);
      gl.uniform1f(u.uMapa, p ? p.mapa : 0);
      gl.uniform1f(u.uVarre, p ? p.varre : 0);
      gl.uniform1f(u.uBorda, this.op.margem > 0 ? 0.035 : 0.0001);
      gl.uniform3f(u.uNevoa, 0.55, 0.62, 0.78);
      gl.uniform1f(u.uNevoaF, this.op.nevoa);
      gl.uniform1f(u.uBrilho, plano ? 0.82 : 1.0);
      gl.uniform1f(u.uContorno, p ? p.contorno : 0);
      gl.uniform1f(u.uFoco, this.foco);
      gl.uniform1f(u.uDist, this.dist);
      gl.activeTexture(gl.TEXTURE0); gl.bindTexture(gl.TEXTURE_2D, this.tProf);
      gl.uniform1i(u.uProf, 0); gl.uniform1i(u.uCor, 1);
      const n = this.tCor.length;
      const zFrente = ((this.info.cortes[n - 2] ?? this.foco) - this.foco) * forcaBase;
      for (let i = 0; i < n; i++) {
        if (i === n - 1 && this.part) this.particulas(PV, jan, forcaBase, -1e3, zFrente, p);
        gl.useProgram(this.pc.p); gl.bindVertexArray(this.vao);
        const sep = p ? p.sep * (i - (n - 1) / 2) * 2 : 0;
        gl.uniform4f(u.uCanal, i === 0 ? 1 : 0, i === 1 ? 1 : 0, i === 2 ? 1 : 0, 0);
        gl.uniform1f(u.uForca, forcaBase);
        gl.uniform1f(u.uSep, sep);
        gl.uniform1f(u.uAlfa, i === 0 ? 1 : Math.min(1, ease * 1.3));
        gl.activeTexture(gl.TEXTURE1); gl.bindTexture(gl.TEXTURE_2D, this.tCor[i]);
        gl.drawElements(gl.TRIANGLES, this.nInd, gl.UNSIGNED_INT, 0);
      }
      if (this.part) this.particulas(PV, jan, forcaBase, zFrente, 1e3, p);
    }

    particulas(PV, jan, forca, zmin, zmax, p) {
      const gl = this.gl, u = this.pp.u, tp = this.part.tp;
      // volume das partículas: do fundo até um pouco na frente do vidro, cortado no intervalo pedido
      const z0 = Math.max(zmin, -forca * 0.9), z1 = Math.min(zmax, forca * 0.55);
      if (z1 <= z0) return;
      gl.useProgram(this.pp.p);
      gl.bindVertexArray(this.part.vao);
      gl.blendFunc(gl.ONE, gl.ONE);
      gl.uniformMatrix4fv(u.uPV, false, PV);
      gl.uniform2f(u.uMeio, this.meio[0], this.meio[1]);
      gl.uniform2f(u.uZ, z0, z1);
      gl.uniform1f(u.uT, agora() + this.fase * 1e5);
      gl.uniform1f(u.uTam, tp.tam * this.E * (this.jh / 520));
      gl.uniform1f(u.uVel, tp.vel);
      gl.uniform1f(u.uCai, tp.cai);
      gl.uniform3f(u.uCor1, ...tp.cor1); gl.uniform3f(u.uCor2, ...tp.cor2);
      gl.uniform1f(u.uForte, tp.forte * (p ? p.part : 1));
      gl.uniform4f(u.uJan, ...jan);
      gl.uniform1f(u.uRaio, this.op.raio * this.E);
      gl.uniform1f(u.uUsaJan, this.op.margem > 0 ? (p ? 1 - p.abre : 1) : 0);
      gl.uniform1f(u.uForca, forca);
      gl.drawArrays(gl.POINTS, 0, this.part.n);
      gl.blendFunc(gl.ONE, gl.ONE_MINUS_SRC_ALPHA);
    }
  }

  // a história ("a mágica por dentro"): de 0 a 1 conforme a rolagem
  function historia(f) {
    const etapa = (a, b) => Math.min(1, Math.max(0, (f - a) / (b - a)));
    const suave = x => x * x * (3 - 2 * x);
    const varre = suave(etapa(0.12, 0.34));                                  // 2: a IA "enxerga" a profundidade
    const abre = suave(etapa(0.4, 0.58)) * (1 - suave(etapa(0.8, 0.94)));   // 3: camadas vistas de lado
    const mapa = Math.min(1, etapa(0.1, 0.14)) * (1 - suave(etapa(0.44, 0.56)));
    const relevo = 0.03 + 0.97 * suave(etapa(0.16, 0.4));                    // 1: plana; o relevo nasce com o scanner
    return {
      varre, mapa, abre,
      yaw: -abre * 1.0, pitch: abre * 0.17, zoom: 1 + abre * 1.05,
      sep: abre * 0.85, forca: relevo * (1 - abre * 0.75), part: (0.3 + 0.7 * relevo) * (1 - abre * 0.5),
      contorno: abre,
    };
  }

  function liberarLonge(exceto) {
    const longe = palcos.filter(p => p.gl && p !== exceto && !p.visivel)
      .sort((a, b) => Math.abs(b.el.getBoundingClientRect().top) - Math.abs(a.el.getBoundingClientRect().top));
    while (ativos >= LIMITE && longe.length) longe.shift().soltar(false);
  }

  // ------------------------------------------------------------------ monta os palcos da página
  const els = document.querySelectorAll("[data-cena]");
  const teste = document.createElement("canvas").getContext("webgl2");
  if (!teste) document.documentElement.classList.add("sem-webgl2");
  else {
    const ext = teste.getExtension("WEBGL_lose_context"); if (ext) ext.loseContext();
    const perto = new IntersectionObserver(es => es.forEach(e => {
      const p = e.target._palco;
      p.perto = e.isIntersecting;
      if (p.perto) p.iniciar();
    }), { rootMargin: "120% 0px" });
    const vis = new IntersectionObserver(es => es.forEach(e => { e.target._palco.visivel = e.isIntersecting; }), { rootMargin: "10% 0px" });
    els.forEach(el => {
      const p = new Palco(el);
      el._palco = p;
      palcos.push(p);
      perto.observe(el); vis.observe(el);
    });
    // solta quem ficou muito longe (o celular agradece)
    setInterval(() => {
      for (const p of palcos) {
        if (!p.gl || p.visivel) continue;
        const r = p.el.getBoundingClientRect();
        if (r.bottom < -innerHeight * 2.5 || r.top > innerHeight * 3.5) p.soltar(false);
      }
    }, 2000);
  }

  // história: progresso pela rolagem da seção
  const hist = document.querySelector(".historia");
  const passosHist = hist ? hist.querySelectorAll("[data-passo]") : [];
  function rolarHistoria() {
    if (!hist) return;
    const r = hist.getBoundingClientRect();
    const f = Math.min(1, Math.max(0, -r.top / Math.max(1, r.height - innerHeight)));
    const p = hist.querySelector("[data-cena]")?._palco;
    if (p) p.progresso = f;
    const atual = f < 0.1 ? 0 : f < 0.38 ? 1 : f < 0.78 ? 2 : 3;
    passosHist.forEach((el, i) => el.classList.toggle("atual", i === atual));
    hist.style.setProperty("--prog", f.toFixed(4));
    hist.style.setProperty("--abre", historia(f).abre.toFixed(3));
  }

  // laço único: um quadro por vez para todos os palcos visíveis
  let tAnt = 0, lento = 0;
  function laco(t) {
    const dt = t - tAnt; tAnt = t;
    if (dt > 0 && dt < 250 && !document.hidden) {
      lento = lento * 0.96 + (dt > 26 ? 0.04 : 0);
      if (lento > 0.55 && QUAL > 0.5) { QUAL = Math.max(0.5, QUAL - 0.15); lento = 0; }
    }
    olho.x += (olho.alvoX - olho.x) * (olho.giro ? 0.12 : 0.06);
    olho.y += (olho.alvoY - olho.y) * (olho.giro ? 0.12 : 0.06);
    rolarHistoria();
    for (const p of palcos) if (p.visivel && p.pronto) p.desenhar(t);
    requestAnimationFrame(laco);
  }
  requestAnimationFrame(laco);

  // ------------------------------------------------------------------ óculos vermelho e azul
  const bAna = document.getElementById("anaglifo");
  if (bAna) bAna.addEventListener("click", () => {
    const p = document.querySelector("[data-cena='heroi']")?._palco;
    if (!p) return;
    p.anaglifo = !p.anaglifo;
    bAna.classList.toggle("ativo", p.anaglifo);
  });

  // ------------------------------------------------------------------ comparação: arrastar a linha
  const comp = document.querySelector(".comparar");
  if (comp) {
    let arrastando = false, tocou = false;
    const por = f => {
      comp.style.setProperty("--divisa", f);
      if (comp._palco) comp._palco.divisa = f;
    };
    const porX = x => { const r = comp.getBoundingClientRect(); por(Math.min(0.97, Math.max(0.03, (x - r.left) / r.width))); };
    comp.addEventListener("pointerdown", e => { arrastando = tocou = true; comp.setPointerCapture(e.pointerId); porX(e.clientX); });
    comp.addEventListener("pointermove", e => { if (arrastando) porX(e.clientX); });
    addEventListener("pointerup", () => { arrastando = false; });
    // sozinha ela passeia até alguém pegar
    const ini = agora();
    (function passear() {
      if (tocou) return;
      const r = comp.getBoundingClientRect();
      if (r.top < innerHeight && r.bottom > 0) por(0.5 + Math.sin((agora() - ini) / 1700) * 0.3);
      requestAnimationFrame(passear);
    })();
  }

  // ------------------------------------------------------------------ cartões: inclinação 3D com o mouse e brilho que segue o cursor
  if (!TOQUE && !REDUZIR) document.querySelectorAll(".cartao").forEach(c => {
    c.addEventListener("pointermove", e => {
      const r = c.getBoundingClientRect();
      const x = (e.clientX - r.left) / r.width, y = (e.clientY - r.top) / r.height;
      c.style.setProperty("--mx", (x * 100).toFixed(1) + "%");
      c.style.setProperty("--my", (y * 100).toFixed(1) + "%");
      c.style.transform = `perspective(1000px) rotateX(${(0.5 - y) * 6}deg) rotateY(${(x - 0.5) * 8}deg)`;
    });
    c.addEventListener("pointerleave", () => { c.style.transform = ""; });
  });

  // ------------------------------------------------------------------ céu estrelado do fundo (profundidade até no fundo da página)
  const ceu = document.getElementById("estrelas");
  if (ceu && !REDUZIR) {
    const g = ceu.getContext("2d");
    let W = 0, H = 0;
    const N = TOQUE ? 90 : 190, E = Math.min(DPR, 1.5);
    const est = Array.from({ length: N }, () => ({ x: Math.random(), y: Math.random(), z: Math.random() ** 1.6, f: Math.random() * 6.28 }));
    const tam = () => { W = ceu.width = Math.round(innerWidth * E); H = ceu.height = Math.round(innerHeight * E); };
    tam(); addEventListener("resize", tam);
    (function quadro(t) {
      g.clearRect(0, 0, W, H);
      const rol = scrollY / Math.max(1, innerHeight);
      for (const s of est) {
        const prof = 0.15 + s.z * 0.85;
        const x = (((s.x + olho.x * 0.012 * prof) % 1) + 1) % 1 * W;
        const y = (((s.y - rol * 0.06 * prof + olho.y * 0.01 * prof) % 1) + 1) % 1 * H;
        const a = (0.25 + 0.75 * prof) * (0.6 + 0.4 * Math.sin(t * 0.0012 + s.f));
        g.fillStyle = `rgba(200,215,255,${(a * 0.7).toFixed(3)})`;
        g.beginPath(); g.arc(x, y, (0.4 + prof * 1.3) * E, 0, 6.2832); g.fill();
      }
      requestAnimationFrame(quadro);
    })(0);
  }

  // ------------------------------------------------------------------ aparecer ao rolar
  const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add("visto"); io.unobserve(e.target); } }),
    { threshold: 0.12 });
  document.querySelectorAll(".aparece").forEach(el => io.observe(el));

  // ------------------------------------------------------------------ botão de download: a versão mais nova publicada
  (async () => {
    const botoes = document.querySelectorAll("[data-baixar]");
    if (!botoes.length) return;
    try {
      const r = await fetch("https://api.github.com/repos/Sindelitcis/pop3d/releases/latest");
      if (r.status === 404) {
        botoes.forEach(b => { b.classList.add("desligado"); b.querySelector("span").textContent = TX.em_breve || "Em breve"; });
        document.querySelectorAll("[data-baixar-detalhe]").forEach(d => d.textContent = TX.forno || "");
        return;
      }
      const d = await r.json();
      const exe = (d.assets || []).find(a => /\.exe$/i.test(a.name));
      const celular = /Android|iPhone|iPad|Mobile/i.test(navigator.userAgent);
      botoes.forEach(b => { b.href = exe ? exe.browser_download_url : d.html_url; });
      const mb = exe ? ` · ${Math.round(exe.size / 1e6)} MB` : "";
      document.querySelectorAll("[data-baixar-detalhe]").forEach(el => {
        el.textContent = celular ? (TX.no_pc || "") : `${TX.versao || "Versão"} ${d.tag_name.replace(/^v/i, "")}${mb} · Windows 10 / 11`;
      });
    } catch (e) { /* sem a API: o link para a página de versões continua valendo */ }
  })();

  // ------------------------------------------------------------------ idioma: escolha guardada (o português redireciona na 1ª visita)
  document.querySelectorAll("[data-idioma]").forEach(a => a.addEventListener("click", () => {
    try { localStorage.setItem("pop3d_idioma", a.dataset.idioma); } catch (e) {}
  }));
})();
