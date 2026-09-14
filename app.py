import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Aviral Bagjani | AI & GenAI Systems Engineer",
    page_icon="⚡",
    layout="wide",
)

# Strip Streamlit default padding and chrome so the 3D portfolio spans edge-to-edge
st.markdown("""
<style>
    header[data-testid="stHeader"] { display: none !important; }
    #MainMenu { display: none !important; }
    footer { display: none !important; }
    .block-container { padding: 0 !important; margin: 0 !important; max-width: 100vw !important; }
    iframe { border: none !important; width: 100vw !important; height: 100vh !important; }
</style>
""", unsafe_allow_html=True)

PORTFOLIO = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Aviral Bagjani — AI & GenAI Systems Engineer</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
<!-- Three.js & GSAP -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>

<style>
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
body{
  background:#030712;
  color:#f3f4f6;
  font-family:'Space Grotesk',sans-serif;
  overflow:hidden;
  height:100vh;
  width:100vw;
}
::selection{background:#6366f1;color:#fff}

/* BACKGROUND 3D CANVAS */
#canvas3d{
  position:fixed;
  inset:0;
  z-index:0;
  pointer-events:auto;
}

/* SCROLL CONTAINER */
#frame{
  position:relative;
  z-index:1;
  height:100vh;
  overflow-y:scroll;
  scrollbar-width:none;
}
#frame::-webkit-scrollbar{display:none}

/* PRELOADER */
#loader{
  position:fixed;inset:0;z-index:999;background:#030712;
  display:flex;flex-direction:column;align-items:center;justify-content:center;gap:18px;
  transition:opacity .7s ease,visibility .7s;
}
#loader.hide{opacity:0;visibility:hidden}
.loader-logo{font-family:'JetBrains Mono',monospace;font-size:1.1rem;letter-spacing:.35em;color:#38bdf8}
.loader-bar{width:240px;height:2px;background:rgba(255,255,255,.08);border-radius:2px;overflow:hidden}
.loader-bar i{display:block;height:100%;width:35%;background:linear-gradient(90deg,#6366f1,#38bdf8,#818cf8);animation:slide 1.2s ease-in-out infinite}
@keyframes slide{0%{transform:translateX(-100%)}100%{transform:translateX(320%)}}

/* CUSTOM GLOW CURSOR */
#cursor{
  position:fixed;width:28px;height:28px;border:1.5px solid rgba(56,189,248,.8);border-radius:50%;
  pointer-events:none;z-index:990;transform:translate(-50%,-50%);
  transition:width .2s,height .2s,background .2s,border-color .2s;mix-blend-mode:screen;
}
#cursor.hot{width:56px;height:56px;background:rgba(56,189,248,.18);border-color:#818cf8}
#cursor-dot{
  position:fixed;width:5px;height:5px;background:#38bdf8;border-radius:50%;
  pointer-events:none;z-index:991;transform:translate(-50%,-50%);
}

/* TOP HUD NAVIGATION */
nav{
  position:sticky;top:0;z-index:100;display:flex;justify-content:space-between;align-items:center;
  padding:16px 5vw;backdrop-filter:blur(20px);background:rgba(3,7,18,.75);
  border-bottom:1px solid rgba(255,255,255,.08);
}
.brand{display:flex;align-items:center;gap:12px}
.logo{font-family:'JetBrains Mono',monospace;font-weight:700;color:#f3f4f6;font-size:1.1rem;letter-spacing:-.02em}
.logo span{color:#38bdf8}
.badge-ping{display:inline-flex;align-items:center;gap:6px;padding:3px 10px;border-radius:99px;font-size:.7rem;font-family:'JetBrains Mono',monospace;background:rgba(34,197,94,.1);border:1px solid rgba(34,197,94,.3);color:#4ade80}
.badge-ping i{width:6px;height:6px;border-radius:50%;background:#4ade80;box-shadow:0 0 8px #4ade80;animation:pulse 1.8s infinite}
@keyframes pulse{50%{opacity:.3}}

.hud-telemetry{
  display:flex;align-items:center;gap:16px;
  font-family:'JetBrains Mono',monospace;font-size:.75rem;
}
.hud-pill{
  padding:5px 12px;border-radius:8px;background:rgba(56,189,248,.08);
  border:1px solid rgba(56,189,248,.25);color:#38bdf8;
}
.audio-toggle{
  background:transparent;border:1px solid rgba(255,255,255,.15);color:#94a3b8;
  padding:5px 12px;border-radius:8px;cursor:pointer;font-family:'JetBrains Mono',monospace;
  font-size:.75rem;transition:.2s;display:flex;align-items:center;gap:6px;
}
.audio-toggle:hover{border-color:#38bdf8;color:#38bdf8}

.nav-links a{color:#94a3b8;text-decoration:none;margin-left:24px;font-size:.86rem;transition:.2s}
.nav-links a:hover{color:#38bdf8}
.nav-links a b{color:#6366f1;font-family:'JetBrains Mono',monospace;margin-right:4px}

/* HERO SECTION */
.hero{min-height:94vh;display:flex;flex-direction:column;justify-content:center;padding:0 6vw;position:relative}
.hero-tag{
  display:inline-flex;align-items:center;gap:10px;padding:6px 16px;border-radius:99px;
  font-family:'JetBrains Mono',monospace;font-size:.78rem;color:#93c5fd;
  background:rgba(59,130,246,.08);border:1px solid rgba(59,130,246,.28);width:fit-content;margin-bottom:24px;
}
.hero h1{font-size:clamp(2.7rem,6.8vw,5.2rem);font-weight:700;line-height:1.05;letter-spacing:-.04em;margin-bottom:18px;max-width:880px}
.hero h1 .grad{
  background:linear-gradient(120deg,#818cf8 0%,#38bdf8 50%,#c084fc 100%);
  -webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;
}
.typer{font-family:'JetBrains Mono',monospace;font-size:clamp(1.05rem,2.2vw,1.4rem);color:#38bdf8;min-height:1.6em;margin-bottom:22px}
.typer::after{content:'▍';animation:blink 1s infinite}
@keyframes blink{50%{opacity:0}}
.hero p.desc{max-width:640px;color:#9ca3af;line-height:1.75;font-size:1.03rem;margin-bottom:34px}
.hero p.desc b{color:#f3f4f6}

.btn-row{display:flex;gap:14px;flex-wrap:wrap}
.btn{padding:13px 26px;border-radius:12px;text-decoration:none;font-weight:600;font-size:.9rem;transition:.25s;cursor:pointer;display:inline-flex;align-items:center;gap:8px}
.btn-solid{background:linear-gradient(120deg,#6366f1,#38bdf8);color:#fff;box-shadow:0 8px 24px -8px rgba(99,102,241,.6)}
.btn-solid:hover{transform:translateY(-3px);box-shadow:0 14px 32px -8px rgba(99,102,241,.85)}
.btn-ghost{border:1px solid rgba(255,255,255,.16);color:#f3f4f6;background:rgba(255,255,255,.02);backdrop-filter:blur(8px)}
.btn-ghost:hover{border-color:#38bdf8;color:#38bdf8;transform:translateY(-3px)}

.hero-hint{
  position:absolute;bottom:30px;right:6vw;font-family:'JetBrains Mono',monospace;font-size:.72rem;
  color:#64748b;letter-spacing:.15em;display:flex;align-items:center;gap:8px;
}
.hero-hint .ring{width:8px;height:8px;border-radius:50%;border:1.5px solid #38bdf8;animation:pulse 1.5s infinite}

/* SECTIONS */
section{padding:90px 6vw;max-width:1180px;margin:0 auto;position:relative}
.sec-tag{font-family:'JetBrains Mono',monospace;color:#38bdf8;font-size:.78rem;letter-spacing:.25em;margin-bottom:10px}
.sec-title{font-size:clamp(1.9rem,3.8vw,2.7rem);letter-spacing:-.03em;margin-bottom:44px}
.sec-title em{font-style:normal;color:#38bdf8}

/* METRICS STATS */
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:16px;margin-bottom:20px}
.stat{background:rgba(15,23,42,.65);border:1px solid rgba(255,255,255,.08);border-radius:18px;padding:26px 22px;text-align:center;backdrop-filter:blur(14px);transition:.3s}
.stat:hover{transform:translateY(-5px);border-color:rgba(56,189,248,.5);box-shadow:0 15px 35px -15px rgba(56,189,248,.3)}
.stat .n{font-family:'JetBrains Mono',monospace;font-size:2.2rem;font-weight:700;background:linear-gradient(120deg,#38bdf8,#818cf8);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.stat .l{font-size:.78rem;color:#94a3b8;margin-top:6px;letter-spacing:.03em}

/* PROJECT CARDS */
.card{position:relative;background:rgba(15,23,42,.65);border:1px solid rgba(255,255,255,.08);border-radius:22px;padding:36px;margin-bottom:26px;backdrop-filter:blur(16px);overflow:hidden;transition:border-color .3s,box-shadow .3s,transform .3s}
.card:hover{border-color:rgba(56,189,248,.55);box-shadow:0 24px 50px -18px rgba(56,189,248,.35)}
.card::before{
  content:'';position:absolute;top:var(--mx,-1000px);left:var(--my,-1000px);width:450px;height:450px;
  background:radial-gradient(circle,rgba(56,189,248,.14),transparent 70%);transform:translate(-50%,-50%);
  pointer-events:none;border-radius:50%;
}
.card h3{font-size:1.4rem;margin-bottom:6px;color:#fff}
.card .role{color:#818cf8;font-size:.92rem;font-family:'JetBrains Mono',monospace;margin-bottom:14px}
.card p{color:#94a3b8;line-height:1.75;font-size:.96rem}
.card p b{color:#f3f4f6}
.tags{display:flex;flex-wrap:wrap;gap:8px;margin-top:22px}
.tag{font-family:'JetBrains Mono',monospace;font-size:.72rem;color:#cbd5e1;background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.1);padding:5px 12px;border-radius:8px}
.tag.hi{color:#38bdf8;border-color:rgba(56,189,248,.4);background:rgba(56,189,248,.09)}

/* ========================================================
   AKASH-INSPIRED 3D INTERACTIVE KEYBOARD ARSENAL
   ======================================================== */
.keyboard-section-wrapper{
  background:rgba(15,23,42,.7);border:1px solid rgba(56,189,248,.25);
  border-radius:24px;padding:32px;backdrop-filter:blur(20px);position:relative;overflow:hidden;
  box-shadow:0 20px 60px -20px rgba(56,189,248,.2);
}
.keyboard-telemetry-header{
  display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;
  border-bottom:1px solid rgba(255,255,255,.08);padding-bottom:18px;margin-bottom:24px;
}
.kb-title-block h3{font-size:1.25rem;font-weight:700;color:#fff;display:flex;align-items:center;gap:10px}
.kb-title-block p{font-size:.82rem;color:#94a3b8;font-family:'JetBrains Mono',monospace;margin-top:4px}
.kb-live-inspect{
  background:rgba(56,189,248,.08);border:1px solid rgba(56,189,248,.3);
  padding:8px 16px;border-radius:10px;font-family:'JetBrains Mono',monospace;
  font-size:.8rem;color:#38bdf8;display:flex;align-items:center;gap:10px;
}

/* 3D Keyboard Scene Container */
#keyboard-3d-viewport{
  width:100%;height:380px;border-radius:18px;background:rgba(3,7,18,.8);
  border:1px solid rgba(255,255,255,.06);position:relative;overflow:hidden;
}
.kb-instructions{
  position:absolute;bottom:14px;left:18px;z-index:5;
  font-family:'JetBrains Mono',monospace;font-size:.72rem;color:#64748b;
  display:flex;align-items:center;gap:8px;background:rgba(3,7,18,.6);
  padding:4px 10px;border-radius:6px;border:1px solid rgba(255,255,255,.05);
}

/* Dynamic Skill Telemetry Inspector Panel */
.skill-detail-panel{
  margin-top:20px;background:rgba(10,16,32,.85);border:1px solid rgba(255,255,255,.08);
  border-radius:16px;padding:20px 24px;transition:all .3s ease;
}
.skill-detail-panel.active-glow{
  border-color:rgba(56,189,248,.6);box-shadow:0 0 30px rgba(56,189,248,.15);
}
.skill-header-row{display:flex;justify-content:space-between;align-items:center;margin-bottom:8px}
.skill-name-txt{font-size:1.1rem;font-weight:700;color:#38bdf8;font-family:'JetBrains Mono',monospace}
.skill-level-txt{font-family:'JetBrains Mono',monospace;font-size:.82rem;color:#4ade80}
.skill-desc-txt{color:#94a3b8;font-size:.9rem;line-height:1.6}
.skill-meter-track{margin-top:12px;height:5px;background:rgba(255,255,255,.07);border-radius:3px;overflow:hidden}
.skill-meter-fill{height:100%;width:80%;background:linear-gradient(90deg,#38bdf8,#818cf8);transition:width .6s cubic-bezier(.16,1,.3,1)}

/* TIMELINE */
.tl{position:relative;padding-left:36px}
.tl::before{content:'';position:absolute;left:9px;top:6px;bottom:6px;width:2px;background:linear-gradient(180deg,#38bdf8,#818cf8,transparent)}
.tl-item{position:relative;margin-bottom:34px}
.tl-item::before{content:'';position:absolute;left:-32px;top:6px;width:14px;height:14px;border-radius:50%;background:#030712;border:2px solid #38bdf8;box-shadow:0 0 12px rgba(56,189,248,.8)}
.tl-item .when{font-family:'JetBrains Mono',monospace;font-size:.76rem;color:#a78bfa;margin-bottom:6px}

/* ACHIEVEMENTS */
.ach{display:flex;align-items:center;gap:18px;background:rgba(15,23,42,.65);border:1px solid rgba(255,255,255,.08);border-radius:18px;padding:22px 26px;margin-bottom:16px;transition:.3s}
.ach:hover{transform:translateX(8px);border-color:rgba(56,189,248,.45)}
.ach .ico{font-size:1.8rem}

/* CONTACT */
#contact{text-align:center;padding-bottom:120px}
#contact .big{font-size:clamp(2rem,4.8vw,3.4rem);letter-spacing:-.03em;margin-bottom:18px}
#contact .big .grad{background:linear-gradient(120deg,#818cf8,#38bdf8);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.socials{display:flex;gap:14px;justify-content:center;flex-wrap:wrap;margin-top:34px}
.socials a{padding:13px 26px;border-radius:12px;border:1px solid rgba(255,255,255,.14);color:#f3f4f6;text-decoration:none;font-size:.9rem;transition:.25s;background:rgba(255,255,255,.02);backdrop-filter:blur(8px)}
.socials a:hover{border-color:#38bdf8;color:#38bdf8;transform:translateY(-3px);box-shadow:0 12px 28px -8px rgba(56,189,248,.45)}

/* REVEAL ON SCROLL */
.rv{opacity:0;transform:translateY(32px);transition:opacity .8s ease,transform .8s ease}
.rv.in{opacity:1;transform:translateY(0)}

footer{padding:26px 5vw;border-top:1px solid rgba(255,255,255,.06);display:flex;justify-content:space-between;align-items:center;font-size:.78rem;color:#64748b;font-family:'JetBrains Mono',monospace}
</style>
</head>

<body>
<div id="loader">
  <div class="loader-logo">AVIRAL&nbsp;BAGJANI&nbsp;//&nbsp;QUANTUM&nbsp;CORE</div>
  <div class="loader-bar"><i></i></div>
</div>

<div id="cursor"></div>
<div id="cursor-dot"></div>

<!-- BACKGROUND 3D CANVAS FOR ENVIRONMENT & CHOREOGRAPHED SCENE -->
<div id="canvas3d"></div>

<div id="frame">
  <!-- NAVIGATION -->
  <nav>
    <div class="brand">
      <div class="logo">aviral<span>.</span>ai</div>
      <div class="badge-ping"><i></i><span>SYSTEMS ACTIVE</span></div>
    </div>
    
    <div class="hud-telemetry">
      <div class="hud-pill" id="nav-stage-hud">STAGE // 00: ORBITAL TERMINAL</div>
      <button class="audio-toggle" id="audio-btn" onclick="toggleAudio()">
        <span id="audio-ico">🔊</span> <span id="audio-lbl">AUDIO ON</span>
      </button>
    </div>

    <div class="nav-links">
      <a href="#work"><b>01.</b>Projects</a>
      <a href="#skills"><b>02.</b>3D Arsenal</a>
      <a href="#exp"><b>03.</b>Experience</a>
      <a href="#contact"><b>04.</b>Contact</a>
    </div>
  </nav>

  <!-- HERO -->
  <div class="hero">
    <div class="hero-tag">
      <span style="color:#38bdf8">●</span> B.Tech (ECE), IIIT Bhagalpur · Class of 2026
    </div>
    <h1>Hi, I'm <span class="grad">Aviral Bagjani</span>.<br>I architect AI systems that <span class="grad">ship to production.</span></h1>
    <div class="typer" id="typer"></div>
    <p class="desc">
      Specialized in <b>multi-agent graph orchestration</b> with LangGraph &amp; MCP,
      <b>low-latency agentic RAG</b> on Qdrant + Redis, and production <b>LLM guardrails</b> with DeepEval &amp; NeMo.
      Former AI Engineering Intern at <b>Zeepty</b>. LeetCode <b>Knight (1784)</b>.
    </p>
    <div class="btn-row">
      <a class="btn btn-solid" href="https://github.com/aviral-dot" target="_blank" rel="noopener">Explore GitHub →</a>
      <a class="btn btn-ghost" href="https://www.linkedin.com/in/aviral-bagjani-a02049259/" target="_blank" rel="noopener">Connect on LinkedIn</a>
    </div>
    <div class="hero-hint">
      <div class="ring"></div>
      <span>3D SCENE RESPONDS TO SCROLL &amp; CURSOR</span>
    </div>
  </div>

  <!-- STATS -->
  <section>
    <div class="stats rv">
      <div class="stat"><div class="n" data-count="1784">0</div><div class="l">LeetCode Knight · 500+ Solved</div></div>
      <div class="stat"><div class="n" data-count="2.12" data-dec="2">0</div><div class="l">End-to-End RAG Latency (s)</div></div>
      <div class="stat"><div class="n" data-count="70" data-suffix="%">0</div><div class="l">LLM Cost Reduction via Redis Locks</div></div>
      <div class="stat"><div class="n" data-count="95" data-suffix="%">0</div><div class="l">Adversarial Attacks Blocked (NeMo)</div></div>
    </div>
  </section>

  <!-- PROJECTS -->
  <section id="work">
    <div class="sec-tag rv">// 01 — FLAGSHIP PRODUCTION SYSTEMS</div>
    <h2 class="sec-title rv">Engineered for <em>scale &amp; resilience.</em></h2>
    
    <div class="card rv">
      <h3>AgentFlow — Autonomous Planner-Executor Multi-Agent Platform</h3>
      <div class="role">LangGraph · Model Context Protocol (MCP) · FastAPI · NeMo · DeepEval</div>
      <p>Orchestrated <b>3 autonomous workflows</b> (deep research, blog synthesis, transactional email) with human-in-the-loop validation checkpoints.
      Integrated <b>2 external tool ecosystems (Tavily + Gmail) through MCP</b>, achieving <b>20/20 end-to-end runs</b> with zero state corruption.
      Hardened with 2-stage NeMo guardrails, JWT authentication &amp; LangSmith telemetry — slashing <b>15 minutes of research-to-draft to under 2 minutes</b>.</p>
      <div class="tags">
        <span class="tag hi">LangGraph</span><span class="tag hi">Model Context Protocol</span><span class="tag">FastAPI</span>
        <span class="tag">PostgreSQL</span><span class="tag">NeMo Guardrails</span><span class="tag">Groq</span>
        <span class="tag">LiteLLM</span><span class="tag">DeepEval</span><span class="tag">Streamlit</span>
      </div>
    </div>

    <div class="card rv">
      <h3>RAGFury — Production Agentic RAG Pipeline at 2.12s</h3>
      <div class="role">Qdrant Cloud · Redis Single-Flight Locking · LangSmith · Groq</div>
      <p>Engineered an agentic RAG system with <b>hybrid sparse/dense vector search &amp; citation-grounded generation</b> over a
      <b>600-document Qdrant index</b> at <b>2.12s</b> average response latency. Implemented <b>Redis single-flight distributed locking</b> and
      user-scoped cache layers: <b>2.8s → 0.8s</b> on repeated queries and <b>70% lower inference cost</b>.
      Enforced <b>4-component DeepEval gates</b> with NeMo blocking <b>&gt;95% adversarial prompt injections</b>.</p>
      <div class="tags">
        <span class="tag hi">Qdrant Cloud</span><span class="tag hi">Redis Locking</span><span class="tag">LangChain</span>
        <span class="tag">LangGraph</span><span class="tag">LangSmith</span><span class="tag">PostgreSQL</span>
        <span class="tag">NeMo Guardrails</span><span class="tag">FastAPI</span>
      </div>
    </div>
  </section>

  <!-- 3D INTERACTIVE KEYBOARD & TECHNICAL ARSENAL -->
  <section id="skills">
    <div class="sec-tag rv">// 02 — INTERACTIVE ARSENAL</div>
    <h2 class="sec-title rv">The 3D <em>Skill Matrix.</em></h2>
    
    <div class="keyboard-section-wrapper rv">
      <div class="keyboard-telemetry-header">
        <div class="kb-title-block">
          <h3>⌨️ INTERACTIVE 3D MECHANICAL KEYCAP ARSENAL</h3>
          <p>Every keycap is a specialized production tool. Hover or click keys to depress switches &amp; inspect telemetry.</p>
        </div>
        <div class="kb-live-inspect" id="kb-active-chip">
          <span>ACTIVE SWITCH:</span> <b id="kb-chip-label">LANGGRAPH (CYCLE DAGS)</b>
        </div>
      </div>

      <!-- 3D KEYBOARD VIEWPORT -->
      <div id="keyboard-3d-viewport">
        <div class="kb-instructions">
          <span>🎮 CLICK / DRAG TO ROTATE KEYBOARD · CLICK KEYCAPS TO DEPRESS</span>
        </div>
      </div>

      <!-- DYNAMIC TELEMETRY PANEL -->
      <div class="skill-detail-panel" id="skill-inspector">
        <div class="skill-header-row">
          <div class="skill-name-txt" id="insp-name">LangGraph &amp; Multi-Agent Workflows</div>
          <div class="skill-level-txt" id="insp-stat">95% PRODUCTION READINESS</div>
        </div>
        <div class="skill-desc-txt" id="insp-desc">
          Stateful cyclic DAG orchestration, checkpointing, multi-worker delegation, and human-in-the-loop review nodes.
        </div>
        <div class="skill-meter-track">
          <div class="skill-meter-fill" id="insp-fill" style="width: 95%;"></div>
        </div>
      </div>
    </div>
  </section>

  <!-- EXPERIENCE -->
  <section id="exp">
    <div class="sec-tag rv">// 03 — TIMELINE &amp; IMPACT</div>
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
          <p>CGPA <b>6.95</b> (till 8th semester). Coursework: Data Structures &amp; Algorithms, Database Management Systems, Operating Systems, Machine Learning, Computer Networks.</p>
        </div>
      </div>
    </div>

    <div class="sec-tag rv" style="margin-top:50px">// ACHIEVEMENTS</div>
    <div class="ach rv"><div class="ico">⚔️</div><div><b>LeetCode Knight</b> — Rating 1784, 500+ algorithmic problems solved.</div></div>
    <div class="ach rv"><div class="ico">🎯</div><div><b>JEE Main 2022</b> — AIR 52,750 (95.44 percentile) among 1.2M+ candidates.</div></div>
  </section>

  <!-- CONTACT -->
  <section id="contact">
    <div class="sec-tag rv">// 04 — TRANSMISSION</div>
    <h2 class="big rv">Let's build something<br><span class="grad">intelligent together.</span></h2>
    <p class="desc rv" style="margin:0 auto;text-align:center;max-width:550px">
      Actively seeking AI / GenAI / LLM Systems Engineering roles for 2026.<br>
      My transmission line is open.
    </p>
    <div class="socials rv">
      <a href="mailto:aviralbharti832002@gmail.com">✉️ aviralbharti832002@gmail.com</a>
      <a href="https://www.linkedin.com/in/aviral-bagjani-a02049259/" target="_blank" rel="noopener">💼 LinkedIn Profile</a>
      <a href="https://github.com/aviral-dot" target="_blank" rel="noopener">💻 GitHub — aviral-dot</a>
    </div>
  </section>

  <footer>
    <div>© 2026 AVIRAL BAGJANI · ALL SYSTEMS OPERATIONAL</div>
    <div>THREE.JS DUAL-VIEWPORT WEBGL ENGINE</div>
  </footer>
</div>

<script>
/* ========================================================
   SYNTHESIZED WEB AUDIO SOUND SYSTEM (NO EXTERNAL FILES)
   ======================================================== */
let audioEnabled = true;
let audioCtx = null;
function initAudio() {
  if (!audioCtx) {
    audioCtx = new (window.AudioContext || window.webkitAudioContext)();
  }
}
function playMechanicalClick(freq = 800, dur = 0.04) {
  if (!audioEnabled) return;
  try {
    initAudio();
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    osc.type = 'triangle';
    osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(120, audioCtx.currentTime + dur);
    gain.gain.setValueAtTime(0.15, audioCtx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + dur);
    osc.connect(gain);
    gain.connect(audioCtx.destination);
    osc.start();
    osc.stop(audioCtx.currentTime + dur);
  } catch(e){}
}
function playChime(freq = 520) {
  if (!audioEnabled) return;
  try {
    initAudio();
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    osc.type = 'sine';
    osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
    gain.gain.setValueAtTime(0.08, audioCtx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.0001, audioCtx.currentTime + 0.35);
    osc.connect(gain);
    gain.connect(audioCtx.destination);
    osc.start();
    osc.stop(audioCtx.currentTime + 0.35);
  } catch(e){}
}
function toggleAudio() {
  audioEnabled = !audioEnabled;
  document.getElementById('audio-ico').textContent = audioEnabled ? '🔊' : '🔇';
  document.getElementById('audio-lbl').textContent = audioEnabled ? 'AUDIO ON' : 'MUTED';
  if(audioEnabled) playChime(660);
}

/* ========================================================
   BACKGROUND 3D SCENE: ORBITING HOLOGRAPHIC TERMINAL
   ======================================================== */
const bgContainer = document.getElementById('canvas3d');
const bgScene = new THREE.Scene();
const bgCam = new THREE.PerspectiveCamera(50, window.innerWidth / window.innerHeight, 0.1, 100);
bgCam.position.set(0, 0, 7.5);

const bgRen = new THREE.WebGLRenderer({ antialias: true, alpha: true });
bgRen.setSize(window.innerWidth, window.innerHeight);
bgRen.setPixelRatio(Math.min(window.devicePixelRatio, 2));
bgContainer.appendChild(bgRen.domElement);

// Lighting
const ambLight = new THREE.AmbientLight(0xffffff, 0.85);
bgScene.add(ambLight);
const cyanSpot = new THREE.PointLight(0x38bdf8, 3.8, 35);
cyanSpot.position.set(5, 6, 6);
bgScene.add(cyanSpot);
const purpleSpot = new THREE.PointLight(0xa78bfa, 3.2, 35);
purpleSpot.position.set(-6, -4, 4);
bgScene.add(purpleSpot);

// 1. Particle Cloud Matrix
const STAR_COUNT = 1500;
const starGeo = new THREE.BufferGeometry();
const starPos = new Float32Array(STAR_COUNT * 3);
const starColors = new Float32Array(STAR_COUNT * 3);
const col1 = new THREE.Color('#38bdf8'), col2 = new THREE.Color('#818cf8'), col3 = new THREE.Color('#c084fc');

for (let i = 0; i < STAR_COUNT; i++) {
  starPos[i*3] = (Math.random() - 0.5) * 36;
  starPos[i*3+1] = (Math.random() - 0.5) * 32;
  starPos[i*3+2] = (Math.random() - 0.5) * 25 - 2;
  const c = [col1, col2, col3][i % 3];
  starColors[i*3] = c.r; starColors[i*3+1] = c.g; starColors[i*3+2] = c.b;
}
starGeo.setAttribute('position', new THREE.BufferAttribute(starPos, 3));
starGeo.setAttribute('color', new THREE.BufferAttribute(starColors, 3));
const starsMat = new THREE.PointsMaterial({ size: 0.045, vertexColors: true, transparent: true, opacity: 0.8 });
const starField = new THREE.Points(starGeo, starsMat);
bgScene.add(starField);

// 2. STAGE 0: HERO QUANTUM HOLOGRAM CORE
const heroGroup = new THREE.Group();
heroGroup.position.set(3.2, 0.2, 0);

const polyGeo = new THREE.IcosahedronGeometry(1.65, 2);
const polyMat = new THREE.MeshStandardMaterial({
  color: 0x38bdf8, wireframe: true, transparent: true, opacity: 0.45, roughness: 0.1, metalness: 0.8
});
const heroPoly = new THREE.Mesh(polyGeo, polyMat);
heroGroup.add(heroPoly);

const ringG1 = new THREE.TorusGeometry(2.2, 0.03, 16, 100);
const ringM1 = new THREE.MeshBasicMaterial({ color: 0x818cf8 });
const ring1 = new THREE.Mesh(ringG1, ringM1);
ring1.rotation.x = Math.PI / 3;
heroGroup.add(ring1);

const ringG2 = new THREE.TorusGeometry(2.45, 0.02, 16, 100);
const ringM2 = new THREE.MeshBasicMaterial({ color: 0x38bdf8 });
const ring2 = new THREE.Mesh(ringG2, ringM2);
ring2.rotation.y = Math.PI / 4;
heroGroup.add(ring2);

const coreOcta = new THREE.Mesh(
  new THREE.OctahedronGeometry(0.85, 0),
  new THREE.MeshStandardMaterial({ color: 0x0284c7, roughness: 0.2, emissive: 0x0369a1, emissiveIntensity: 0.9 })
);
heroGroup.add(coreOcta);
bgScene.add(heroGroup);

// 3. STAGE 1: MULTI-AGENT SYNAPSE GRAPH
const projectCluster = new THREE.Group();
projectCluster.position.set(-3.2, -4.8, -1);
const clusterNodes = [];
for (let i = 0; i < 8; i++) {
  const sMesh = new THREE.Mesh(
    new THREE.SphereGeometry(0.18, 16, 16),
    new THREE.MeshStandardMaterial({ color: i % 2 === 0 ? 0x38bdf8 : 0x818cf8, emissive: 0x0284c7 })
  );
  const ang = (i / 8) * Math.PI * 2;
  sMesh.position.set(Math.cos(ang) * 1.6, Math.sin(ang) * 1.6, (Math.random() - 0.5) * 1.2);
  clusterNodes.push(sMesh);
  projectCluster.add(sMesh);
}
const lineMat = new THREE.LineBasicMaterial({ color: 0x38bdf8, transparent: true, opacity: 0.35 });
for (let i = 0; i < clusterNodes.length; i++) {
  const p1 = clusterNodes[i].position;
  const p2 = clusterNodes[(i + 3) % clusterNodes.length].position;
  const lineGeo = new THREE.BufferGeometry().setFromPoints([p1, p2]);
  projectCluster.add(new THREE.Line(lineGeo, lineMat));
}
bgScene.add(projectCluster);

// 4. STAGE 2: KNOT REACTOR
const knotGroup = new THREE.Group();
knotGroup.position.set(3.4, -9.8, -1);
const knot = new THREE.Mesh(
  new THREE.TorusKnotGeometry(1.4, 0.3, 120, 16),
  new THREE.MeshStandardMaterial({ color: 0x6366f1, wireframe: true, transparent: true, opacity: 0.4 })
);
knotGroup.add(knot);
bgScene.add(knotGroup);

// 5. STAGE 3: EXPERIENCE HELIX
const helixGroup = new THREE.Group();
helixGroup.position.set(-3.2, -15.0, -1);
for (let i = 0; i < 20; i++) {
  const bMesh = new THREE.Mesh(
    new THREE.BoxGeometry(0.18, 0.18, 0.18),
    new THREE.MeshBasicMaterial({ color: i % 2 === 0 ? 0x38bdf8 : 0xa78bfa, wireframe: true })
  );
  const t = i * 0.42;
  bMesh.position.set(Math.cos(t) * 1.3, i * 0.26 - 2.6, Math.sin(t) * 1.3);
  helixGroup.add(bMesh);
}
bgScene.add(helixGroup);

// 6. STAGE 4: CONTACT BEACON
const beaconGroup = new THREE.Group();
beaconGroup.position.set(0, -20.5, 0);
const beacon = new THREE.Mesh(
  new THREE.DodecahedronGeometry(1.8, 1),
  new THREE.MeshStandardMaterial({ color: 0x38bdf8, wireframe: true, transparent: true, opacity: 0.5 })
);
beaconGroup.add(beacon);
bgScene.add(beaconGroup);

/* ========================================================
   THE 3D INTERACTIVE MECHANICAL KEYBOARD (LOCAL VIEWPORT)
   ======================================================== */
const kbViewport = document.getElementById('keyboard-3d-viewport');
const kbScene = new THREE.Scene();
const kbCam = new THREE.PerspectiveCamera(45, kbViewport.clientWidth / kbViewport.clientHeight, 0.1, 100);
kbCam.position.set(0, 4.2, 5.2);
kbCam.lookAt(0, -0.2, 0);

const kbRen = new THREE.WebGLRenderer({ antialias: true, alpha: true });
kbRen.setSize(kbViewport.clientWidth, kbViewport.clientHeight);
kbRen.setPixelRatio(Math.min(window.devicePixelRatio, 2));
kbViewport.appendChild(kbRen.domElement);

// Keyboard Lighting
const kbAmb = new THREE.AmbientLight(0xffffff, 0.75);
kbScene.add(kbAmb);
const kbKeyLight = new THREE.PointLight(0x38bdf8, 3.5, 25);
kbKeyLight.position.set(0, 5, 3);
kbScene.add(kbKeyLight);
const kbUnderLight = new THREE.PointLight(0x818cf8, 2.5, 20);
kbUnderLight.position.set(0, -1, 0);
kbScene.add(kbUnderLight);

// Keyboard Chassis Baseplate
const kbChassis = new THREE.Group();
const plateGeo = new THREE.BoxGeometry(6.6, 0.35, 3.2);
const plateMat = new THREE.MeshStandardMaterial({
  color: 0x090d16, roughness: 0.4, metalness: 0.85
});
const chassisMesh = new THREE.Mesh(plateGeo, plateMat);
chassisMesh.position.y = -0.2;
kbChassis.add(chassisMesh);

// Glowing Neon Bevel Rim around keyboard
const rimGeo = new THREE.BoxGeometry(6.75, 0.05, 3.35);
const rimMat = new THREE.MeshBasicMaterial({ color: 0x38bdf8, wireframe: true });
const rimMesh = new THREE.Mesh(rimGeo, rimMat);
rimMesh.position.y = -0.05;
kbChassis.add(rimMesh);

// Keycap definitions (Your Production Skills)
const SKILLS_KEY_DATA = [
  // ROW 1
  { label: "LANGGRAPH", row: 0, col: 0, level: "95%", desc: "Stateful cyclic multi-agent DAGs, human-in-the-loop gates, and checkpoint persistence." },
  { label: "MCP", row: 0, col: 1, level: "94%", desc: "Model Context Protocol bridges for dynamic tool orchestration (Tavily, Gmail, Filesystems)." },
  { label: "QDRANT", row: 0, col: 2, level: "92%", desc: "Hybrid sparse/dense vector indexing, payload filters, and sub-second semantic retrieval." },
  { label: "REDIS LOCK", row: 0, col: 3, level: "90%", desc: "Single-flight distributed locking & cache shields reducing redundant LLM calls by 70%." },
  // ROW 2
  { label: "DEEPEVAL", row: 1, col: 0, level: "92%", desc: "Automated test suites evaluating G-Eval, Hallucination, Task Completion & Answer Relevance." },
  { label: "NEMO", row: 1, col: 1, level: "95%", desc: "Self-correcting guardrails blocking >95% jailbreaks, prompt injections, and sensitive data leakage." },
  { label: "FASTAPI", row: 1, col: 2, level: "93%", desc: "High-throughput asynchronous APIs, streaming SSE completions, and Pydantic validation." },
  { label: "LANGSMITH", row: 1, col: 3, level: "88%", desc: "End-to-end trace observability, token cost attribution, and latency debugging." },
  // ROW 3
  { label: "POSTGRES", row: 2, col: 0, level: "86%", desc: "Relational persistence, user sessions, conversation history, and transaction safety." },
  { label: "DOCKER", row: 2, col: 1, level: "85%", desc: "Containerized reproducible agent runtimes, microservices networking, and cloud deploys." },
  { label: "LEETCODE", row: 2, col: 2, level: "1784", desc: "Knight badge, 500+ solved across graph theory, dynamic programming, and binary search." },
  { label: "PYTORCH", row: 2, col: 3, level: "84%", desc: "Model fine-tuning, embeddings generation, vector transformations, and tensor operations." }
];

// Helper to create texture for key legends
function makeKeyTexture(text) {
  const cv = document.createElement('canvas');
  cv.width = 256; cv.height = 256;
  const ctx = cv.getContext('2d');
  ctx.fillStyle = '#0f172a';
  ctx.fillRect(0, 0, 256, 256);
  // Border
  ctx.strokeStyle = '#38bdf8';
  ctx.lineWidth = 10;
  ctx.strokeRect(6, 6, 244, 244);
  // Text
  ctx.fillStyle = '#f8fafc';
  ctx.font = 'bold 30px "JetBrains Mono", monospace';
  ctx.textAlign = 'center';
  ctx.textBaseline = 'middle';
  ctx.fillText(text, 128, 128);
  return new THREE.CanvasTexture(cv);
}

const keycapMeshes = [];
const startX = -2.25;
const startZ = -1.0;
const stepX = 1.5;
const stepZ = 1.0;

SKILLS_KEY_DATA.forEach((key, idx) => {
  const keyGroup = new THREE.Group();
  const capGeo = new THREE.BoxGeometry(1.22, 0.45, 0.78);
  const keyTex = makeKeyTexture(key.label);
  
  const capMat = [
    new THREE.MeshStandardMaterial({ color: 0x1e293b, metalness: 0.6, roughness: 0.3 }),
    new THREE.MeshStandardMaterial({ color: 0x1e293b, metalness: 0.6, roughness: 0.3 }),
    new THREE.MeshStandardMaterial({ map: keyTex, metalness: 0.3, roughness: 0.4 }), // Top with legend
    new THREE.MeshStandardMaterial({ color: 0x0f172a }),
    new THREE.MeshStandardMaterial({ color: 0x1e293b }),
    new THREE.MeshStandardMaterial({ color: 0x1e293b }),
  ];
  const capMesh = new THREE.Mesh(capGeo, capMat);
  capMesh.position.y = 0.22;
  keyGroup.add(capMesh);

  // Underglow light prism
  const glowGeo = new THREE.BoxGeometry(1.28, 0.05, 0.84);
  const glowMat = new THREE.MeshBasicMaterial({ color: 0x38bdf8, transparent: true, opacity: 0.35 });
  const glowMesh = new THREE.Mesh(glowGeo, glowMat);
  glowMesh.position.y = 0.02;
  keyGroup.add(glowMesh);

  const posX = startX + key.col * stepX;
  const posZ = startZ + key.row * stepZ;
  keyGroup.position.set(posX, 0, posZ);

  keyGroup.userData = {
    originalY: 0,
    depressedY: -0.16,
    data: key,
    glowMesh: glowMesh,
    capMesh: capMesh
  };

  kbChassis.add(keyGroup);
  keycapMeshes.push(keyGroup);
});

// Tilt the entire keyboard slightly towards user
kbChassis.rotation.x = 0.22;
kbScene.add(kbChassis);

/* ========================================================
   KEYBOARD RAYCASTING & INTERACTION
   ======================================================== */
const raycaster = new THREE.Raycaster();
const kbMouse = new THREE.Vector2(-999, -999);
let hoveredKey = null;

const chipLabel = document.getElementById('kb-chip-label');
const inspName = document.getElementById('insp-name');
const inspStat = document.getElementById('insp-stat');
const inspDesc = document.getElementById('insp-desc');
const inspFill = document.getElementById('insp-fill');
const inspectorPanel = document.getElementById('skill-inspector');

function triggerKeyAction(keyGroup) {
  if (!keyGroup) return;
  const k = keyGroup.userData.data;
  
  // Audio click sound
  playMechanicalClick(950, 0.05);

  // Update Telemetry Panel
  chipLabel.textContent = `${k.label} (ACTIVE)`;
  inspName.textContent = k.label;
  inspStat.textContent = `${k.level} PROFICIENCY`;
  inspDesc.textContent = k.desc;
  const numericVal = parseInt(k.level) || 95;
  inspFill.style.width = numericVal + '%';

  inspectorPanel.classList.add('active-glow');
  setTimeout(() => inspectorPanel.classList.remove('active-glow'), 400);

  // Animate Keycap Switch Press Down & Bounce Up
  gsap.killTweensOf(keyGroup.position);
  gsap.to(keyGroup.position, {
    y: keyGroup.userData.depressedY,
    duration: 0.06,
    yoyo: true,
    repeat: 1,
    ease: "power2.inOut",
    onComplete: () => {
      keyGroup.position.y = 0;
    }
  });

  // Flash Underglow
  keyGroup.userData.glowMesh.material.color.setHex(0x4ade80);
  setTimeout(() => keyGroup.userData.glowMesh.material.color.setHex(0x38bdf8), 350);
}

kbViewport.addEventListener('mousemove', (e) => {
  const rect = kbViewport.getBoundingClientRect();
  kbMouse.x = ((e.clientX - rect.left) / rect.width) * 2 - 1;
  kbMouse.y = -((e.clientY - rect.top) / rect.height) * 2 + 1;
});

kbViewport.addEventListener('mouseleave', () => {
  kbMouse.x = -999; kbMouse.y = -999;
  if (hoveredKey) {
    hoveredKey.userData.glowMesh.material.opacity = 0.35;
    hoveredKey = null;
  }
});

kbViewport.addEventListener('click', () => {
  if (hoveredKey) {
    triggerKeyAction(hoveredKey);
  }
});

/* ========================================================
   FRAME SCROLL & CAMERA CHOREOGRAPHY
   ======================================================== */
const frame = document.getElementById('frame');
const stageHud = document.getElementById('nav-stage-hud');
let scrollY = 0;
let maxScroll = 1;

frame.addEventListener('scroll', () => {
  scrollY = frame.scrollTop;
  maxScroll = frame.scrollHeight - frame.clientHeight;
  const progress = scrollY / (maxScroll || 1);

  if (progress < 0.22) stageHud.textContent = "STAGE // 00: ORBITAL TERMINAL";
  else if (progress < 0.48) stageHud.textContent = "STAGE // 01: MULTI-AGENT SYNAPSE";
  else if (progress < 0.72) stageHud.textContent = "STAGE // 02: 3D ARSENAL MATRIX";
  else if (progress < 0.88) stageHud.textContent = "STAGE // 03: CAREER HELIX";
  else stageHud.textContent = "STAGE // 04: QUANTUM BEACON";
});

/* ========================================================
   MOUSE PARALLAX & TICK ANIMATION LOOP
   ======================================================== */
let mx = 0, my = 0, tx = 0, ty = 0;
const cur = document.getElementById('cursor');
const curDot = document.getElementById('cursor-dot');

window.addEventListener('mousemove', (e) => {
  mx = (e.clientX / window.innerWidth - 0.5) * 2;
  my = (e.clientY / window.innerHeight - 0.5) * 2;
  cur.style.left = e.clientX + 'px';
  cur.style.top = e.clientY + 'px';
  curDot.style.left = e.clientX + 'px';
  curDot.style.top = e.clientY + 'px';

  document.querySelectorAll('.card, .stat, .keyboard-section-wrapper').forEach(c => {
    const r = c.getBoundingClientRect();
    c.style.setProperty('--mx', (e.clientX - r.left) + 'px');
    c.style.setProperty('--my', (e.clientY - r.top) + 'px');
  });
});

function animate() {
  requestAnimationFrame(animate);

  // Smooth mouse interpolation
  tx += (mx - tx) * 0.05;
  ty += (my - ty) * 0.05;

  // Background camera choreography along scroll
  const scrollProg = scrollY / (maxScroll || 1);
  const targetCamY = -scrollProg * 20.5;
  bgCam.position.y += (targetCamY - bgCam.position.y) * 0.06;
  bgCam.position.x = tx * 0.8;
  bgCam.lookAt(0, bgCam.position.y, 0);

  // Background geometries subtle rotation
  starField.rotation.y += 0.0006;
  starField.rotation.x = ty * 0.04;
  heroPoly.rotation.x += 0.003;
  heroPoly.rotation.y += 0.005;
  ring1.rotation.z += 0.012;
  ring2.rotation.z -= 0.009;
  coreOcta.rotation.x -= 0.006;
  projectCluster.rotation.y += 0.007;
  knot.rotation.x += 0.005;
  knot.rotation.y += 0.008;
  helixGroup.rotation.y += 0.01;
  beacon.rotation.y += 0.006;

  bgRen.render(bgScene, bgCam);

  // 3D Keyboard Scene Update
  raycaster.setFromCamera(kbMouse, kbCam);
  const flatMeshes = [];
  keycapMeshes.forEach(grp => grp.traverse(child => {
    if (child.isMesh) {
      child.parentGroup = grp;
      flatMeshes.push(child);
    }
  }));

  const intersects = raycaster.intersectObjects(flatMeshes);
  if (intersects.length > 0) {
    const hitGroup = intersects[0].object.parentGroup;
    if (hitGroup && hitGroup !== hoveredKey) {
      if (hoveredKey) hoveredKey.userData.glowMesh.material.opacity = 0.35;
      hoveredKey = hitGroup;
      hoveredKey.userData.glowMesh.material.opacity = 0.9;
      playMechanicalClick(1100, 0.02);
    }
  } else if (hoveredKey) {
    hoveredKey.userData.glowMesh.material.opacity = 0.35;
    hoveredKey = null;
  }

  // Gentle idle oscillation of keyboard
  kbChassis.rotation.y = tx * 0.15;
  kbChassis.rotation.x = 0.22 - ty * 0.1;
  kbRen.render(kbScene, kbCam);
}
animate();

// Resize handling
window.addEventListener('resize', () => {
  bgCam.aspect = window.innerWidth / window.innerHeight;
  bgCam.updateProjectionMatrix();
  bgRen.setSize(window.innerWidth, window.innerHeight);

  kbCam.aspect = kbViewport.clientWidth / kbViewport.clientHeight;
  kbCam.updateProjectionMatrix();
  kbRen.setSize(kbViewport.clientWidth, kbViewport.clientHeight);
});

/* ========================================================
   CURSOR, PRELOADER, TYPING & NUMERICAL COUNTERS
   ======================================================== */
document.querySelectorAll('a, button, .card, .stat, #keyboard-3d-viewport').forEach(el => {
  el.addEventListener('mouseenter', () => cur.classList.add('hot'));
  el.addEventListener('mouseleave', () => cur.classList.remove('hot'));
});

window.addEventListener('load', () => {
  setTimeout(() => {
    document.getElementById('loader').classList.add('hide');
    playChime(440);
  }, 1200);
});

// Roles typing loop
const roles = [
  'Multi-Agent Systems Engineer (LangGraph & MCP).',
  'Agentic RAG Architect (Qdrant & Redis Locks).',
  'LLM Evals & Guardrails Builder (DeepEval & NeMo).',
  'LeetCode Knight · 1784 (500+ Solved).'
];
let rIdx = 0, cIdx = 0, deleting = false;
const typerEl = document.getElementById('typer');
function typeRole() {
  const curStr = roles[rIdx];
  typerEl.textContent = deleting ? curStr.slice(0, --cIdx) : curStr.slice(0, ++cIdx);
  let sp = deleting ? 30 : 60;
  if (!deleting && cIdx === curStr.length) { sp = 1900; deleting = true; }
  else if (deleting && cIdx === 0) { deleting = false; rIdx = (rIdx + 1) % roles.length; sp = 350; }
  setTimeout(typeRole, sp);
}
typeRole();

// Intersection Observer for scroll animations
const observer = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (!e.isIntersecting) return;
    e.target.classList.add('in');
    e.target.querySelectorAll('.n[data-count]').forEach(num => {
      if (num.dataset.done) return;
      num.dataset.done = '1';
      const target = parseFloat(num.dataset.count);
      const dec = +(num.dataset.dec || 0);
      const suf = num.dataset.suffix || '';
      const startT = performance.now();
      const dur = 1400;
      function step(now) {
        const p = Math.min((now - startT) / dur, 1);
        const ease = 1 - Math.pow(1 - p, 3);
        num.textContent = (target * ease).toFixed(dec) + suf;
        if (p < 1) requestAnimationFrame(step);
      }
      requestAnimationFrame(step);
    });
    observer.unobserve(e.target);
  });
}, { threshold: 0.16 });
document.querySelectorAll('.rv').forEach(el => observer.observe(el));
</script>
</body>
</html>
"""

components.html(PORTFOLIO, height=3300, scrolling=False)









