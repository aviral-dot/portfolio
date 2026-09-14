import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Aviral Bagjani | AI & GenAI Systems Engineer",
    page_icon="⚡",
    layout="wide",
)

# Kill Streamlit chrome so the portfolio owns the whole screen
st.markdown("""
<style>
    header[data-testid="stHeader"] { display: none !important; }
    #MainMenu { display: none !important; }
    footer { display: none !important; }
    .block-container { padding: 0 !important; margin: 0 !important; max-width: 100vw !important; }
    iframe { border: none !important; width: 100vw !important; }
</style>
""", unsafe_allow_html=True)

PORTFOLIO = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Aviral Bagjani — AI & GenAI Engineer</title>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<style>
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
body{background:#04060c;color:#e5e7eb;font-family:'Space Grotesk',sans-serif;overflow:hidden;height:100vh;width:100vw}
::selection{background:#6366f1;color:#fff}

#bg3d{position:fixed;inset:0;z-index:0;pointer-events:none}
#frame{position:relative;z-index:1;height:100vh;overflow-y:scroll;scrollbar-width:none}
#frame::-webkit-scrollbar{display:none}

/* ---------- PRELOADER ---------- */
#loader{position:fixed;inset:0;z-index:99;background:#04060c;display:flex;flex-direction:column;
  align-items:center;justify-content:center;gap:18px;transition:opacity .7s ease,visibility .7s}
#loader.hide{opacity:0;visibility:hidden}
.loader-name{font-family:'JetBrains Mono',monospace;font-size:1rem;letter-spacing:.4em;color:#818cf8;
  overflow:hidden;white-space:nowrap;width:0;animation:type 1.4s steps(22) forwards}
@keyframes type{to{width:340px}}
.loader-bar{width:220px;height:2px;background:rgba(255,255,255,.08);border-radius:2px;overflow:hidden}
.loader-bar i{display:block;height:100%;width:40%;background:linear-gradient(90deg,#6366f1,#38bdf8);
  animation:slide 1.2s ease-in-out infinite}
@keyframes slide{0%{transform:translateX(-100%)}100%{transform:translateX(350%)}}

/* ---------- CURSOR ---------- */
#cursor{position:fixed;width:32px;height:32px;border:1.5px solid rgba(56,189,248,.8);border-radius:50%;
  pointer-events:none;z-index:98;transform:translate(-50%,-50%);transition:width .2s,height .2s,background .2s;mix-blend-mode:screen}
#cursor.hot{width:56px;height:56px;background:rgba(56,189,248,.15);border-color:#818cf8}

/* ---------- NAV ---------- */
nav{position:sticky;top:0;z-index:10;display:flex;justify-content:space-between;align-items:center;
  padding:20px 6vw;backdrop-filter:blur(16px);background:rgba(4,6,12,.65);border-bottom:1px solid rgba(255,255,255,.06)}
.logo{font-family:'JetBrains Mono',monospace;font-weight:700;color:#a5b4fc;font-size:1.05rem;letter-spacing:-.02em}
.logo span{color:#38bdf8}
.nav-links a{color:#94a3b8;text-decoration:none;margin-left:26px;font-size:.88rem;transition:.2s}
.nav-links a:hover{color:#38bdf8}
.nav-links a b{color:#6366f1;font-family:'JetBrains Mono',monospace;font-weight:500;margin-right:4px}

.hud-indicator{
  font-family:'JetBrains Mono',monospace;font-size:.72rem;color:#38bdf8;
  padding:6px 14px;border-radius:20px;border:1px solid rgba(56,189,248,.25);background:rgba(56,189,248,.06);
}

/* ---------- HERO ---------- */
.hero{min-height:92vh;display:flex;flex-direction:column;justify-content:center;padding:0 6vw;position:relative}
.pill{display:inline-flex;align-items:center;gap:9px;padding:7px 16px;border-radius:99px;font-size:.78rem;
  font-family:'JetBrains Mono',monospace;color:#93c5fd;background:rgba(59,130,246,.08);
  border:1px solid rgba(59,130,246,.28);width:fit-content;margin-bottom:24px}
.pill .dot{width:7px;height:7px;border-radius:50%;background:#34d399;box-shadow:0 0 10px #34d399;animation:pulse 1.8s infinite}
@keyframes pulse{50%{opacity:.3}}

.hero h1{font-size:clamp(2.6rem,6.5vw,5rem);font-weight:700;line-height:1.06;letter-spacing:-.04em;margin-bottom:14px;max-width:850px}
.hero h1 .grad{background:linear-gradient(120deg,#818cf8 0%,#38bdf8 50%,#a78bfa 100%);
  -webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}

.typer{font-family:'JetBrains Mono',monospace;font-size:clamp(1rem,2.2vw,1.35rem);color:#38bdf8;
  min-height:1.6em;margin-bottom:20px}
.typer::after{content:'▍';animation:blink 1s infinite}
@keyframes blink{50%{opacity:0}}

.hero p.desc{max-width:620px;color:#9ca3af;line-height:1.7;font-size:1.02rem;margin-bottom:34px}
.hero p.desc b{color:#e5e7eb}

.btn-row{display:flex;gap:14px;flex-wrap:wrap}
.btn{padding:13px 26px;border-radius:12px;text-decoration:none;font-weight:600;font-size:.9rem;transition:.25s;cursor:pointer;border:none}
.btn-solid{background:linear-gradient(120deg,#6366f1,#38bdf8);color:#fff;box-shadow:0 8px 24px -8px rgba(99,102,241,.6)}
.btn-solid:hover{transform:translateY(-3px);box-shadow:0 14px 32px -8px rgba(99,102,241,.8)}
.btn-ghost{border:1px solid rgba(255,255,255,.18);color:#e5e7eb;background:transparent}
.btn-ghost:hover{border-color:#38bdf8;color:#38bdf8;transform:translateY(-3px)}

.hero-hint-pill{
  position:absolute;bottom:26px;right:6vw;font-family:'JetBrains Mono',monospace;
  font-size:.72rem;color:#64748b;letter-spacing:.15em;animation:bob 2.2s ease-in-out infinite;
}
@keyframes bob{0%,100%{transform:translateY(0)}50%{transform:translateY(-6px)}}

/* ---------- SECTIONS ---------- */
section{padding:90px 6vw;max-width:1150px;margin:0 auto}
.sec-tag{font-family:'JetBrains Mono',monospace;color:#38bdf8;font-size:.8rem;letter-spacing:.2em;margin-bottom:10px}
.sec-title{font-size:clamp(1.7rem,3.6vw,2.5rem);letter-spacing:-.03em;margin-bottom:44px}
.sec-title em{font-style:normal;color:#38bdf8}

/* stats */
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:16px;margin-bottom:20px}
.stat{background:rgba(13,20,36,.55);border:1px solid rgba(255,255,255,.07);border-radius:16px;
  padding:26px 20px;text-align:center;backdrop-filter:blur(12px);transition:.3s}
.stat:hover{transform:translateY(-5px);border-color:rgba(56,189,248,.45)}
.stat .n{font-family:'JetBrains Mono',monospace;font-size:2.1rem;font-weight:700;
  background:linear-gradient(120deg,#38bdf8,#818cf8);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.stat .l{font-size:.76rem;color:#9ca3af;margin-top:6px;letter-spacing:.04em}

/* cards / projects */
.card{position:relative;background:rgba(13,20,36,.65);border:1px solid rgba(255,255,255,.08);border-radius:20px;
  padding:36px;margin-bottom:26px;backdrop-filter:blur(14px);overflow:hidden;
  transform-style:preserve-3d;transition:border-color .3s,box-shadow .3s,transform .3s}
.card:hover{border-color:rgba(56,189,248,.5);box-shadow:0 24px 50px -20px rgba(56,189,248,.35)}

.card::before{
  content:'';position:absolute;top:var(--mx,-1000px);left:var(--my,-1000px);width:400px;height:400px;
  background:radial-gradient(circle,rgba(56,189,248,.12),transparent 70%);transform:translate(-50%,-50%);
  pointer-events:none;border-radius:50%;
}

.card h3{font-size:1.35rem;margin-bottom:6px;color:#fff}
.card .role{color:#818cf8;font-size:.9rem;font-family:'JetBrains Mono',monospace;margin-bottom:14px}
.card p{color:#94a3b8;line-height:1.7;font-size:.96rem}
.card p b{color:#f1f5f9}
.tags{display:flex;flex-wrap:wrap;gap:8px;margin-top:20px}
.tag{font-family:'JetBrains Mono',monospace;font-size:.72rem;color:#cbd5e1;
  background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.1);padding:5px 12px;border-radius:8px}
.tag.hi{color:#38bdf8;border-color:rgba(56,189,248,.35);background:rgba(56,189,248,.08)}

/* ========================================================
   CREATIVE & ANIMATED TECHNICAL STACK SECTION
   ======================================================== */
.stack-interactive-container {
  display: grid;
  grid-template-columns: 1.15fr 0.85fr;
  gap: 24px;
  align-items: center;
  margin-top: 10px;
}
@media (max-width: 900px) {
  .stack-interactive-container { grid-template-columns: 1fr; }
  #stack-reactor-canvas { height: 260px !important; }
}

/* Category Filter Matrix */
.stack-matrix-nav {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  margin-bottom: 22px;
}
.matrix-btn {
  background: rgba(13,20,36,0.6);
  border: 1px solid rgba(255,255,255,0.08);
  color: #94a3b8;
  padding: 8px 16px;
  border-radius: 10px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.78rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.25s ease;
}
.matrix-btn:hover, .matrix-btn.active {
  background: rgba(56,189,248,0.14);
  border-color: #38bdf8;
  color: #ffffff;
  box-shadow: 0 0 20px rgba(56,189,248,0.25);
  transform: translateY(-2px);
}

/* Cybernetic Skill Block Cards */
.skills-telemetry-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 12px;
}
.telemetry-node {
  background: rgba(10, 16, 32, 0.7);
  border: 1px solid rgba(255, 255, 255, 0.07);
  border-radius: 14px;
  padding: 16px 20px;
  backdrop-filter: blur(12px);
  position: relative;
  overflow: hidden;
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}
.telemetry-node:hover {
  border-color: rgba(56,189,248,0.5);
  transform: translateX(6px);
  box-shadow: 0 8px 30px -10px rgba(56,189,248,0.3);
}
.telemetry-node::before {
  content: '';
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  width: 4px;
  background: linear-gradient(180deg, #38bdf8, #818cf8);
}
.node-top-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 6px;
}
.node-label {
  font-size: 1.05rem;
  font-weight: 700;
  color: #ffffff;
  display: flex;
  align-items: center;
  gap: 10px;
}
.node-spec {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.75rem;
  color: #38bdf8;
  padding: 3px 8px;
  border-radius: 6px;
  background: rgba(56,189,248,0.1);
}
.node-desc {
  font-size: 0.88rem;
  color: #94a3b8;
  line-height: 1.5;
  margin-bottom: 10px;
}
.signal-bar-track {
  height: 5px;
  background: rgba(255,255,255,0.06);
  border-radius: 4px;
  overflow: hidden;
  position: relative;
}
.signal-bar-fill {
  height: 100%;
  width: 0;
  border-radius: 4px;
  background: linear-gradient(90deg, #38bdf8, #818cf8);
  transition: width 1.2s cubic-bezier(0.16, 1, 0.3, 1);
}

/* 3D Reactor Canvas Container */
.reactor-card {
  background: rgba(13,20,36,0.55);
  border: 1px solid rgba(56,189,248,0.25);
  border-radius: 20px;
  padding: 24px;
  backdrop-filter: blur(14px);
  position: relative;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  box-shadow: 0 0 40px rgba(56,189,248,0.08);
}
#stack-reactor-canvas {
  width: 100%;
  height: 380px;
}
.reactor-caption {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.75rem;
  color: #64748b;
  letter-spacing: 0.1em;
  margin-top: 8px;
}

/* timeline */
.tl{position:relative;padding-left:36px}
.tl::before{content:'';position:absolute;left:9px;top:6px;bottom:6px;width:2px;
  background:linear-gradient(180deg,#38bdf8,#818cf8,transparent)}
.tl-item{position:relative;margin-bottom:34px}
.tl-item::before{content:'';position:absolute;left:-32px;top:6px;width:14px;height:14px;border-radius:50%;
  background:#04060c;border:2px solid #38bdf8;box-shadow:0 0 12px rgba(56,189,248,.8)}
.tl-item .when{font-family:'JetBrains Mono',monospace;font-size:.76rem;color:#a78bfa;margin-bottom:6px}

/* achievements */
.ach{display:flex;align-items:center;gap:18px;background:rgba(13,20,36,.55);
  border:1px solid rgba(255,255,255,.07);border-radius:16px;padding:22px 26px;margin-bottom:16px;transition:.3s}
.ach:hover{transform:translateX(8px);border-color:rgba(56,189,248,.4)}
.ach .ico{font-size:1.6rem}

/* contact */
#contact{text-align:center;padding-bottom:120px}
#contact .big{font-size:clamp(1.9rem,4.5vw,3.2rem);letter-spacing:-.03em;margin-bottom:18px}
#contact .big .grad{background:linear-gradient(120deg,#818cf8,#38bdf8);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.socials{display:flex;gap:14px;justify-content:center;flex-wrap:wrap;margin-top:32px}
.socials a{padding:12px 24px;border-radius:12px;border:1px solid rgba(255,255,255,.15);color:#e5e7eb;
  text-decoration:none;font-size:.88rem;transition:.25s;background:rgba(255,255,255,.02)}
.socials a:hover{border-color:#38bdf8;color:#38bdf8;transform:translateY(-3px);box-shadow:0 10px 25px -8px rgba(56,189,248,.4)}

/* reveal */
.rv{opacity:0;transform:translateY(34px);transition:opacity .8s ease,transform .8s ease}
.rv.in{opacity:1;transform:translateY(0)}

footer{padding:26px 6vw;border-top:1px solid rgba(255,255,255,.06);display:flex;justify-content:space-between;
  font-size:.78rem;color:#4b5563;font-family:'JetBrains Mono',monospace}
</style>
</head>
<body>

<div id="bg3d"></div>
<div id="cursor"></div>

<div id="loader">
  <div class="loader-name">AVIRAL&nbsp;BAGJANI&nbsp;//&nbsp;AI&nbsp;ENGINEER</div>
  <div class="loader-bar"><i></i></div>
</div>

<div id="frame">
<nav>
  <div class="logo">aviral<span>.</span>ai</div>
  <div class="hud-indicator" id="section-hud">STAGE // 00: HERO CORE</div>
  <div class="nav-links">
    <a href="#work"><b>01.</b>Projects</a>
    <a href="#skills"><b>02.</b>Stack</a>
    <a href="#exp"><b>03.</b>Experience</a>
    <a href="#contact"><b>04.</b>Contact</a>
  </div>
</nav>

<!-- HERO -->
<div class="hero" id="hero-section">
  <div class="pill"><span class="dot"></span>Open to AI / GenAI Engineering roles · 2026</div>
  <h1>Hi, I'm <span class="grad">Aviral Bagjani</span>.<br>I build AI systems that <span class="grad">ship to production.</span></h1>
  <div class="typer" id="typer"></div>
  <p class="desc">Final-year <b>B.Tech (ECE), IIIT Bhagalpur</b>. I engineer <b>multi-agent orchestration</b> with LangGraph &amp; MCP,
  <b>low-latency agentic RAG</b> on Qdrant + Redis, and wrap everything in <b>evaluation-driven guardrails</b> — DeepEval &amp; NeMo.
  Former AI Engineering Intern at <b>Zeepty</b>. LeetCode <b>Knight (1784)</b>.</p>
  <div class="btn-row">
    <a class="btn btn-solid" href="https://github.com/aviral-dot" target="_blank" rel="noopener">View My Code →</a>
    <a class="btn btn-ghost" href="https://www.linkedin.com/in/aviral-bagjani-a02049259/" target="_blank" rel="noopener">Connect on LinkedIn</a>
  </div>
  <div class="hero-hint-pill">3D CAMERA REACTS TO SCROLL &amp; MOUSE ↓</div>
</div>

<!-- STATS -->
<section>
  <div class="stats rv">
    <div class="stat"><div class="n" data-count="1784">0</div><div class="l">LeetCode Knight · 500+ solved</div></div>
    <div class="stat"><div class="n" data-count="2.12" data-dec="2">0</div><div class="l">End-to-end RAG latency (s)</div></div>
    <div class="stat"><div class="n" data-count="70">0</div><div class="l">LLM inference cost cut (%)</div></div>
    <div class="stat"><div class="n" data-count="95" data-suffix="%">0</div><div class="l">Adversarial queries blocked</div></div>
  </div>
</section>

<!-- PROJECTS -->
<section id="work">
  <div class="sec-tag rv">// 01 — FLAGSHIP SYSTEMS</div>
  <h2 class="sec-title rv">Things I've <em>built & deployed.</em></h2>

  <div class="card rv tilt">
    <h3>AgentFlow — Planner-Executor Multi-Agent Platform</h3>
    <div class="role">LangGraph · MCP · FastAPI · NeMo · DeepEval</div>
    <p>Orchestrated <b>3 autonomous workflows</b> (research, blog generation, email) with human-in-the-loop approval.
    Wired <b>2 external tool ecosystems (Tavily + Gmail) through MCP</b>, completing <b>20/20 end-to-end runs</b> with zero state corruption.
    Hardened with 2-stage NeMo guardrails, JWT auth &amp; LangSmith observability — cutting <b>15 minutes of research-to-draft to under 2 minutes</b>.</p>
    <div class="tags">
      <span class="tag hi">LangGraph</span><span class="tag hi">MCP</span><span class="tag">FastAPI</span>
      <span class="tag">PostgreSQL</span><span class="tag">NeMo Guardrails</span><span class="tag">Groq</span>
      <span class="tag">LiteLLM</span><span class="tag">DeepEval</span><span class="tag">Streamlit</span>
    </div>
  </div>

  <div class="card rv tilt">
    <h3>RAGFury — Production Agentic RAG at 2.12s</h3>
    <div class="role">Qdrant · Redis single-flight · LangSmith · Groq</div>
    <p>Deployed a production-grade Agentic RAG with <b>hybrid retrieval &amp; citation-grounded generation</b> over a
    <b>600-document Qdrant index</b> at <b>2.12s</b> end-to-end latency. Built <b>Redis single-flight distributed locking</b> +
    user-scoped caching: <b>2.8s → 0.8s</b> on repeated queries and <b>70% lower inference cost</b>.
    Enforced <b>4-component DeepEval gates</b> (78–92% scores) with NeMo blocking <b>&gt;95% adversarial queries</b>.</p>
    <div class="tags">
      <span class="tag hi">Qdrant Cloud</span><span class="tag hi">Redis Locking</span><span class="tag">LangChain</span>
      <span class="tag">LangGraph</span><span class="tag">LangSmith</span><span class="tag">PostgreSQL</span>
      <span class="tag">NeMo Guardrails</span><span class="tag">FastAPI</span>
    </div>
  </div>
</section>

<!-- UPGRADED CREATIVE TECHNICAL STACK SECTION -->
<section id="skills">
  <div class="sec-tag rv">// 02 — TECHNICAL ARSENAL</div>
  <h2 class="sec-title rv">Neural Architecture &amp; <em>Production Stack.</em></h2>

  <!-- Interactive Category Matrix Selector -->
  <div class="stack-matrix-nav rv">
    <button class="matrix-btn active" onclick="filterStack('all')">ALL ECOSYSTEMS</button>
    <button class="matrix-btn" onclick="filterStack('genai')">01. GENAI &amp; AGENTS</button>
    <button class="matrix-btn" onclick="filterStack('rag')">02. RAG &amp; VECTOR RETRIEVAL</button>
    <button class="matrix-btn" onclick="filterStack('evals')">03. EVALS &amp; GUARDRAILS</button>
    <button class="matrix-btn" onclick="filterStack('infra')">04. BACKEND &amp; SYSTEMS</button>
  </div>

  <div class="stack-interactive-container">
    <!-- Telemetry Cards Column -->
    <div class="skills-telemetry-grid" id="telemetry-grid">
      
      <!-- Node 1 -->
      <div class="telemetry-node rv" data-cat="genai">
        <div class="node-top-row">
          <div class="node-label">🤖 LangGraph &amp; Model Context Protocol (MCP)</div>
          <div class="node-spec">95% MASTERY</div>
        </div>
        <div class="node-desc">Multi-agent planner-executor state machines, cyclic DAGs, human-in-the-loop review, and external tool bridges.</div>
        <div class="signal-bar-track"><div class="signal-bar-fill" data-w="95"></div></div>
      </div>

      <!-- Node 2 -->
      <div class="telemetry-node rv" data-cat="rag">
        <div class="node-top-row">
          <div class="node-label">⚡ Qdrant Cloud &amp; Redis Distributed Locking</div>
          <div class="node-spec">92% MASTERY</div>
        </div>
        <div class="node-desc">Hybrid sparse/dense vector search, single-flight locks cutting redundant calls by 70%, and sliding-window rate limiters.</div>
        <div class="signal-bar-track"><div class="signal-bar-fill" data-w="92"></div></div>
      </div>

      <!-- Node 3 -->
      <div class="telemetry-node rv" data-cat="evals">
        <div class="node-top-row">
          <div class="node-label">🛡️ DeepEval Evals &amp; NeMo Guardrails</div>
          <div class="node-spec">90% MASTERY</div>
        </div>
        <div class="node-desc">Regression test suites (Task Completion, Answer Relevance), 2-stage input sanitization blocking &gt;95% prompt injections.</div>
        <div class="signal-bar-track"><div class="signal-bar-fill" data-w="90"></div></div>
      </div>

      <!-- Node 4 -->
      <div class="telemetry-node rv" data-cat="infra">
        <div class="node-top-row">
          <div class="node-label">⚙️ FastAPI, C++, SQL &amp; LeetCode Knight</div>
          <div class="node-spec">94% MASTERY</div>
        </div>
        <div class="node-desc">High-throughput asynchronous backends, graph algorithms, dynamic programming, 500+ coding challenges solved.</div>
        <div class="signal-bar-track"><div class="signal-bar-fill" data-w="94"></div></div>
      </div>

      <!-- Node 5 -->
      <div class="telemetry-node rv" data-cat="infra">
        <div class="node-top-row">
          <div class="node-label">☁️ Docker, Kubernetes &amp; LangSmith Observability</div>
          <div class="node-spec">86% MASTERY</div>
        </div>
        <div class="node-desc">Container orchestration, token usage cost telemetry, CI/CD automated deployment pipelines.</div>
        <div class="signal-bar-track"><div class="signal-bar-fill" data-w="86"></div></div>
      </div>

    </div>

    <!-- 3D Reactor Widget Column -->
    <div class="reactor-card rv">
      <div style="font-family:'JetBrains Mono',monospace; font-size:0.8rem; color:#38bdf8; font-weight:700;">
        // 3D NEURAL REACTOR
      </div>
      <div id="stack-reactor-canvas"></div>
      <div class="reactor-caption">ORBITING SATELLITE NODES // INTERACTIVE FOCUS</div>
    </div>
  </div>
</section>

<!-- EXPERIENCE -->
<section id="exp">
  <div class="sec-tag rv">// 03 — JOURNEY</div>
  <h2 class="sec-title rv">Experience &amp; <em>education.</em></h2>
  <div class="tl">
    <div class="tl-item rv">
      <div class="when">APR 2025 — JUL 2025</div>
      <div class="card">
        <h3>AI Engineering Intern @ Zeepty</h3>
        <p>• Applied <b>semantic creator/product matching</b> and personalized LLM outreach across <b>500+ combinations</b>, improving relevant-match retrieval by <b>25%</b>.<br>
        • Refined prompts and retrieved context for creator outreach, lifting response relevance by <b>15%</b> across 20+ scenarios.</p>
        <div class="tags"><span class="tag hi">Semantic Search</span><span class="tag">Prompt Engineering</span><span class="tag">LLM Outreach</span></div>
      </div>
    </div>
    <div class="tl-item rv">
      <div class="when">NOV 2022 — MAY 2026</div>
      <div class="card">
        <h3>B.Tech, Electronics &amp; Communication — IIIT Bhagalpur</h3>
        <p>CGPA <b>6.95</b> (till 8th semester). Coursework: DSA, DBMS, Operating Systems, Machine Learning, Computer Networks.</p>
      </div>
    </div>
  </div>

  <div class="sec-tag rv" style="margin-top:50px">// ACHIEVEMENTS</div>
  <div class="ach rv"><div class="ico">⚔️</div><div><b>LeetCode Knight</b> — Rating 1784, 500+ problems solved.</div></div>
  <div class="ach rv"><div class="ico">🎯</div><div><b>JEE Main 2022</b> — AIR 52,750 (95.44 percentile) among 1.2M+ candidates.</div></div>
</section>

<!-- CONTACT -->
<section id="contact">
  <div class="sec-tag rv">// 04 — GET IN TOUCH</div>
  <h2 class="big rv">Let's build something<br><span class="grad">intelligent together.</span></h2>
  <p class="desc rv" style="margin:0 auto;text-align:center">Hiring for AI / GenAI / LLM engineering roles?
  My inbox is open — let's talk.</p>
  <div class="socials rv">
    <a href="mailto:aviralbharti832002@gmail.com">✉️ aviralbharti832002@gmail.com</a>
    <a href="https://www.linkedin.com/in/aviral-bagjani-a02049259/" target="_blank" rel="noopener">💼 LinkedIn</a>
    <a href="https://github.com/aviral-dot" target="_blank" rel="noopener">💻 GitHub — aviral-dot</a>
  </div>
</section>

<footer>
  <div>© 2026 AVIRAL BAGJANI</div>
  <div>BUILT WITH STREAMLIT + THREE.JS 3D ENGINE</div>
</footer>
</div>

<script>
/* ========================================================
   SECTION-AWARE CHOREOGRAPHED THREE.JS 3D SCENE
   ======================================================== */
const bg = document.getElementById('bg3d');
const scene = new THREE.Scene();
const cam = new THREE.PerspectiveCamera(55, window.innerWidth / window.innerHeight, 0.1, 100);
cam.position.set(0, 0, 7);

const ren = new THREE.WebGLRenderer({ antialias: true, alpha: true });
ren.setSize(window.innerWidth, window.innerHeight);
ren.setPixelRatio(Math.min(window.devicePixelRatio, 2));
bg.appendChild(ren.domElement);

// Lighting
const ambientLight = new THREE.AmbientLight(0xffffff, 0.7);
scene.add(ambientLight);

const cyanLight = new THREE.PointLight(0x38bdf8, 3.5, 40);
cyanLight.position.set(5, 5, 5);
scene.add(cyanLight);

const purpleLight = new THREE.PointLight(0x818cf8, 3.0, 40);
purpleLight.position.set(-5, -5, 3);
scene.add(purpleLight);

// 1. GLOBAL COSMIC PARTICLE GALAXY
const N = 1200;
const pos = new Float32Array(N * 3), col = new Float32Array(N * 3);
const c1 = new THREE.Color('#6366f1'), c2 = new THREE.Color('#38bdf8'), c3 = new THREE.Color('#a78bfa');
for(let i = 0; i < N; i++){
  pos[i*3] = (Math.random() - 0.5) * 32;
  pos[i*3+1] = (Math.random() - 0.5) * 28;
  pos[i*3+2] = (Math.random() - 0.5) * 20 - 2;
  const c = [c1, c2, c3][i % 3];
  col[i*3] = c.r; col[i*3+1] = c.g; col[i*3+2] = c.b;
}
const pg = new THREE.BufferGeometry();
pg.setAttribute('position', new THREE.BufferAttribute(pos, 3));
pg.setAttribute('color', new THREE.BufferAttribute(col, 3));
const stars = new THREE.Points(pg, new THREE.PointsMaterial({ size: 0.045, vertexColors: true, transparent: true, opacity: 0.85 }));
scene.add(stars);

// 2. STAGE 0: HERO QUANTUM CORE (Right Side of Hero)
const heroCoreGroup = new THREE.Group();
heroCoreGroup.position.set(3.0, 0.2, 0);

const icoGeo = new THREE.IcosahedronGeometry(1.6, 2);
const icoMat = new THREE.MeshStandardMaterial({
  color: 0x38bdf8, wireframe: true, transparent: true, opacity: 0.4, roughness: 0.2, metalness: 0.8
});
const heroIco = new THREE.Mesh(icoGeo, icoMat);
heroCoreGroup.add(heroIco);

const ringGeo1 = new THREE.TorusGeometry(2.1, 0.035, 16, 90);
const ringMat1 = new THREE.MeshBasicMaterial({ color: 0x818cf8 });
const heroRing1 = new THREE.Mesh(ringGeo1, ringMat1);
heroRing1.rotation.x = Math.PI / 3;
heroCoreGroup.add(heroRing1);

const ringGeo2 = new THREE.TorusGeometry(2.35, 0.025, 16, 90);
const ringMat2 = new THREE.MeshBasicMaterial({ color: 0x38bdf8 });
const heroRing2 = new THREE.Mesh(ringGeo2, ringMat2);
heroRing2.rotation.y = Math.PI / 4;
heroCoreGroup.add(heroRing2);

const innerGeo = new THREE.OctahedronGeometry(0.85, 0);
const innerMat = new THREE.MeshStandardMaterial({
  color: 0x0284c7, roughness: 0.1, metalness: 0.9, emissive: 0x0369a1, emissiveIntensity: 0.8
});
const heroInner = new THREE.Mesh(innerGeo, innerMat);
heroCoreGroup.add(heroInner);
scene.add(heroCoreGroup);

// 3. STAGE 1: PROJECTS SYNAPSE GRAPH
const projectGraphGroup = new THREE.Group();
projectGraphGroup.position.set(-3.2, -4.5, -1);

const synNodes = [];
for (let i = 0; i < 7; i++) {
  const snGeo = new THREE.SphereGeometry(0.18, 16, 16);
  const snMat = new THREE.MeshStandardMaterial({ color: i % 2 === 0 ? 0x38bdf8 : 0x818cf8, emissive: 0x0284c7 });
  const snMesh = new THREE.Mesh(snGeo, snMat);
  const ang = (i / 7) * Math.PI * 2;
  snMesh.position.set(Math.cos(ang) * 1.5, Math.sin(ang) * 1.5, (Math.random() - 0.5) * 1.2);
  synNodes.push(snMesh);
  projectGraphGroup.add(snMesh);
}
const lMat = new THREE.LineBasicMaterial({ color: 0x38bdf8, transparent: true, opacity: 0.35 });
for (let i = 0; i < synNodes.length; i++) {
  const p1 = synNodes[i].position;
  const p2 = synNodes[(i + 2) % synNodes.length].position;
  const lineG = new THREE.BufferGeometry().setFromPoints([p1, p2]);
  projectGraphGroup.add(new THREE.Line(lineG, lMat));
}
scene.add(projectGraphGroup);

// 4. STAGE 2: SKILLS CYBER TORUS ENGINE
const skillsTorusGroup = new THREE.Group();
skillsTorusGroup.position.set(3.4, -9.5, -1);
const knotGeo = new THREE.TorusKnotGeometry(1.4, 0.32, 120, 16);
const knotMat = new THREE.MeshStandardMaterial({
  color: 0x6366f1, wireframe: true, transparent: true, opacity: 0.38
});
const skillsTorus = new THREE.Mesh(knotGeo, knotMat);
skillsTorusGroup.add(skillsTorus);
scene.add(skillsTorusGroup);

// 5. STAGE 3: EXPERIENCE MILESTONE HELIX
const expHelixGroup = new THREE.Group();
expHelixGroup.position.set(-3.2, -14.5, -1);
for (let i = 0; i < 18; i++) {
  const hGeo = new THREE.BoxGeometry(0.18, 0.18, 0.18);
  const hMat = new THREE.MeshBasicMaterial({ color: i % 2 === 0 ? 0x38bdf8 : 0xa78bfa, wireframe: true });
  const hMesh = new THREE.Mesh(hGeo, hMat);
  const t = i * 0.45;
  hMesh.position.set(Math.cos(t) * 1.2, i * 0.28 - 2.5, Math.sin(t) * 1.2);
  expHelixGroup.add(hMesh);
}
scene.add(expHelixGroup);

// 6. STAGE 4: CONTACT QUANTUM BEACON
const contactBeaconGroup = new THREE.Group();
contactBeaconGroup.position.set(0, -19.5, 0);
const beaconGeo = new THREE.DodecahedronGeometry(1.8, 1);
const beaconMat = new THREE.MeshStandardMaterial({
  color: 0x38bdf8, wireframe: true, transparent: true, opacity: 0.45
});
const beaconMesh = new THREE.Mesh(beaconGeo, beaconMat);
contactBeaconGroup.add(beaconMesh);
scene.add(contactBeaconGroup);

// 7. INTERACTIVE CLICK EXPLOSION PARTICLES
const clickParticles = [];
function triggerShockwave(x, y) {
  const count = 28;
  for (let i = 0; i < count; i++) {
    const geo = new THREE.SphereGeometry(0.04, 8, 8);
    const mat = new THREE.MeshBasicMaterial({ color: 0x38bdf8 });
    const p = new THREE.Mesh(geo, mat);
    p.position.set((x / window.innerWidth - 0.5) * 10, (-y / window.innerHeight + 0.5) * 8, 2);
    const angle = Math.random() * Math.PI * 2;
    const speed = 0.04 + Math.random() * 0.08;
    p.userData = { vx: Math.cos(angle) * speed, vy: Math.sin(angle) * speed, life: 1.0 };
    scene.add(p);
    clickParticles.push(p);
  }
}
window.addEventListener('click', (e) => triggerShockwave(e.clientX, e.clientY));

/* ========================================================
   LOCAL 3D NEURAL REACTOR IN TECHNICAL STACK
   ======================================================== */
const reactorContainer = document.getElementById('stack-reactor-canvas');
const rScene = new THREE.Scene();
const rCam = new THREE.PerspectiveCamera(50, reactorContainer.clientWidth / (reactorContainer.clientHeight || 380), 0.1, 100);
rCam.position.z = 4.8;

const rRen = new THREE.WebGLRenderer({ antialias: true, alpha: true });
rRen.setSize(reactorContainer.clientWidth, reactorContainer.clientHeight || 380);
rRen.setPixelRatio(Math.min(window.devicePixelRatio, 2));
reactorContainer.appendChild(rRen.domElement);

const rCoreGeo = new THREE.IcosahedronGeometry(0.85, 1);
const rCoreMat = new THREE.MeshStandardMaterial({ color: 0x38bdf8, wireframe: true, emissive: 0x0284c7, emissiveIntensity: 0.5 });
const rCoreMesh = new THREE.Mesh(rCoreGeo, rCoreMat);
rScene.add(rCoreMesh);

const rLight = new THREE.PointLight(0x38bdf8, 2, 20);
rLight.position.set(2, 3, 3);
rScene.add(rLight);

// Orbital satellites inside reactor
const rSats = [];
for (let i = 0; i < 8; i++) {
  const satG = new THREE.TetrahedronGeometry(0.12, 0);
  const satM = new THREE.MeshBasicMaterial({ color: i % 2 === 0 ? 0x38bdf8 : 0x818cf8, wireframe: true });
  const satMesh = new THREE.Mesh(satG, satM);
  const ang = (i / 8) * Math.PI * 2;
  satMesh.userData = { angle: ang, dist: 1.6 + (i % 3) * 0.25, speed: 0.02 + (i * 0.003) };
  rSats.push(satMesh);
  rScene.add(satMesh);
}

function animateReactor() {
  requestAnimationFrame(animateReactor);
  rCoreMesh.rotation.x += 0.006;
  rCoreMesh.rotation.y += 0.009;

  rSats.forEach(s => {
    s.userData.angle += s.userData.speed;
    s.position.x = Math.cos(s.userData.angle) * s.userData.dist;
    s.position.y = Math.sin(s.userData.angle) * s.userData.dist * 0.6;
    s.position.z = Math.sin(s.userData.angle * 2) * 0.5;
    s.rotation.x += 0.04;
  });

  rRen.render(rScene, rCam);
}
animateReactor();

/* ========================================================
   SCROLL POSITION & SECTION RECOGNITION
   ======================================================== */
const frame = document.getElementById('frame');
const hud = document.getElementById('section-hud');
let scrollY = 0;
let maxScroll = 1;

frame.addEventListener('scroll', () => {
  scrollY = frame.scrollTop;
  maxScroll = frame.scrollHeight - frame.clientHeight;
  const progress = scrollY / (maxScroll || 1);

  if (progress < 0.2) hud.textContent = "STAGE // 00: QUANTUM HERO CORE";
  else if (progress < 0.45) hud.textContent = "STAGE // 01: MULTI-AGENT SYNAPSE";
  else if (progress < 0.65) hud.textContent = "STAGE // 02: NEURAL TECH REACTOR";
  else if (progress < 0.85) hud.textContent = "STAGE // 03: CAREER HELIX";
  else hud.textContent = "STAGE // 04: QUANTUM BEACON";
});

/* ========================================================
   MOUSE PARALLAX & TICK LOOP
   ======================================================== */
let mx = 0, my = 0, tx = 0, ty = 0;
const cur = document.getElementById('cursor');

window.addEventListener('mousemove', e => {
  mx = (e.clientX / window.innerWidth - 0.5) * 2;
  my = (e.clientY / window.innerHeight - 0.5) * 2;
  cur.style.left = e.clientX + 'px';
  cur.style.top = e.clientY + 'px';

  document.querySelectorAll('.card, .telemetry-node').forEach(c => {
    const r = c.getBoundingClientRect();
    c.style.setProperty('--mx', (e.clientX - r.left) + 'px');
    c.style.setProperty('--my', (e.clientY - r.top) + 'px');
  });
});

function tick(){
  requestAnimationFrame(tick);
  tx += (mx - tx) * 0.05;
  ty += (my - ty) * 0.05;

  const scrollProgress = scrollY / (maxScroll || 1);
  const targetCamY = -scrollProgress * 19.5;
  cam.position.y += (targetCamY - cam.position.y) * 0.06;
  cam.position.x = tx * 0.8;
  cam.lookAt(0, cam.position.y, 0);

  stars.rotation.y += 0.0006;
  stars.rotation.x = ty * 0.05;

  heroIco.rotation.x += 0.003;
  heroIco.rotation.y += 0.005;
  heroRing1.rotation.z += 0.012;
  heroRing2.rotation.z -= 0.009;
  heroInner.rotation.x -= 0.007;
  heroInner.rotation.y += 0.008;

  projectGraphGroup.rotation.y += 0.008;
  projectGraphGroup.rotation.x += 0.004;

  skillsTorus.rotation.x += 0.006;
  skillsTorus.rotation.y += 0.009;

  expHelixGroup.rotation.y += 0.01;

  beaconMesh.rotation.y += 0.005;
  beaconMesh.rotation.x += 0.003;

  for (let i = clickParticles.length - 1; i >= 0; i--) {
    const p = clickParticles[i];
    p.position.x += p.userData.vx;
    p.position.y += p.userData.vy;
    p.userData.life -= 0.02;
    p.scale.set(p.userData.life, p.userData.life, p.userData.life);
    if (p.userData.life <= 0) {
      scene.remove(p);
      clickParticles.splice(i, 1);
    }
  }

  ren.render(scene, cam);
}
tick();

window.addEventListener('resize', () => {
  cam.aspect = window.innerWidth / window.innerHeight;
  cam.updateProjectionMatrix();
  ren.setSize(window.innerWidth, window.innerHeight);

  rCam.aspect = reactorContainer.clientWidth / (reactorContainer.clientHeight || 380);
  rCam.updateProjectionMatrix();
  rRen.setSize(reactorContainer.clientWidth, reactorContainer.clientHeight || 380);
});

/* ========================================================
   STACK CATEGORY MATRIX FILTERING
   ======================================================== */
function filterStack(cat) {
  document.querySelectorAll('.matrix-btn').forEach(btn => {
    btn.classList.toggle('active', btn.getAttribute('onclick').includes(`'${cat}'`));
  });

  document.querySelectorAll('.telemetry-node').forEach(node => {
    if (cat === 'all' || node.dataset.cat === cat) {
      node.style.display = 'block';
      setTimeout(() => {
        node.style.opacity = '1';
        node.style.transform = 'translateY(0)';
      }, 50);
    } else {
      node.style.opacity = '0';
      node.style.transform = 'translateY(10px)';
      setTimeout(() => { node.style.display = 'none'; }, 200);
    }
  });

  // Pulse reactor core on filter
  rCoreMesh.scale.set(1.3, 1.3, 1.3);
  setTimeout(() => rCoreMesh.scale.set(1, 1, 1), 300);
}

/* ========================================================
   CURSOR, PRELOADER, TYPING & COUNTERS
   ======================================================== */
document.querySelectorAll('a, .btn, .card, .matrix-btn, .telemetry-node').forEach(el => {
  el.addEventListener('mouseenter', () => cur.classList.add('hot'));
  el.addEventListener('mouseleave', () => cur.classList.remove('hot'));
});

window.addEventListener('load', () => setTimeout(() => document.getElementById('loader').classList.add('hide'), 1500));

const roles = [
  'Multi-Agent Systems Engineer (LangGraph & MCP).',
  'Agentic RAG Architect (Qdrant & Redis Locks).',
  'LLM Evals & Guardrails Builder (DeepEval & NeMo).',
  'LeetCode Knight · 1784 (500+ Solved).'
];
let ri = 0, ci = 0, del = false;
const tEl = document.getElementById('typer');
(function type(){
  const w = roles[ri];
  tEl.textContent = del ? w.slice(0, --ci) : w.slice(0, ++ci);
  let sp = del ? 35 : 65;
  if(!del && ci === w.length){ sp = 1800; del = true; }
  else if(del && ci === 0){ del = false; ri = (ri + 1) % roles.length; sp = 350; }
  setTimeout(type, sp);
})();

const io = new IntersectionObserver(es => {
  es.forEach(e => {
    if(!e.isIntersecting) return;
    e.target.classList.add('in');
    e.target.querySelectorAll('.n[data-count]').forEach(n => {
      if(n.dataset.done) return; n.dataset.done = 1;
      const target = parseFloat(n.dataset.count), dec = +(n.dataset.dec || 0), suf = n.dataset.suffix || '';
      const t0 = performance.now(), dur = 1500;
      (function step(t){
        const p = Math.min((t - t0) / dur, 1), e2 = 1 - Math.pow(1 - p, 3);
        n.textContent = (target * e2).toFixed(dec) + suf;
        if(p < 1) requestAnimationFrame(step);
      })(t0);
    });
    e.target.querySelectorAll('.signal-bar-fill').forEach(f => f.style.width = f.dataset.w + '%');
    io.unobserve(e.target);
  });
}, { threshold: 0.18 });

document.querySelectorAll('.rv').forEach(el => io.observe(el));

document.querySelectorAll('.tilt').forEach(c => {
  c.addEventListener('mousemove', e => {
    const r = c.getBoundingClientRect(), x = (e.clientX - r.left) / r.width - 0.5, y = (e.clientY - r.top) / r.height - 0.5;
    c.style.transform = `perspective(900px) rotateY(${x * 6}deg) rotateX(${-y * 6}deg) translateY(-4px)`;
  });
  c.addEventListener('mouseleave', () => c.style.transform = '');
});
</script>
</body>
</html>
"""

components.html(PORTFOLIO, height=3100, scrolling=False)






