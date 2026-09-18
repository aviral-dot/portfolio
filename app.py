
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
<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&family=JetBrains+Mono:wght@500;700&display=swap"><link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
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
  transition:opacity .25s ease,visibility .25s;pointer-events:none;
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

/* HERO PHOTO */
.hero-photo{
  position:absolute;
  right:7vw;
  top:50%;
  transform:translateY(-52%);
  width:clamp(200px,19vw,300px);
  aspect-ratio:195/243;
  object-fit:cover;
  border-radius:26px;
  border:1px solid rgba(99,102,241,.45);
  box-shadow:0 0 0 1px rgba(255,255,255,.05),0 24px 60px -18px rgba(56,189,248,.45),0 0 90px -20px rgba(99,102,241,.55);
  z-index:2;
  background:#0b1120;
}
.hero-photo-wrap{
  position:absolute;
  right:7vw;
  top:50%;
  transform:translateY(-52%);
  z-index:2;
  padding:8px;
  border-radius:30px;
  background:linear-gradient(140deg,rgba(99,102,241,.55),rgba(56,189,248,.25) 45%,rgba(192,132,252,.4));
}
.hero-photo-wrap img{
  display:block;
  width:clamp(230px,22vw,340px);
  aspect-ratio:195/243;
  object-fit:cover;
  border-radius:22px;
  background:#0b1120;
}
@media(max-width:920px){
  .hero-photo-wrap{
    position:relative;
    right:auto;top:auto;transform:none;
    margin-bottom:30px;
    width:fit-content;
  }
  .hero-photo-wrap img{width:170px}
}

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

/* 3D Neural Core & Agent DAG Viewport */
#keyboard-3d-viewport {
  width: 100%;
  height: 480px;
  border-radius: 20px;
  background: radial-gradient(circle at 50% 50%, rgba(15, 23, 42, 0.75) 0%, rgba(3, 7, 18, 0.95) 100%);
  border: 1px solid rgba(56, 189, 248, 0.2);
  box-shadow: 0 0 50px rgba(56, 189, 248, 0.08) inset, 0 20px 50px rgba(0, 0, 0, 0.6);
  position: relative;
  overflow: hidden;
}

.neural-hud-overlay {
  position: absolute;
  top: 16px;
  left: 18px;
  right: 18px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  pointer-events: none;
  z-index: 10;
}

.neural-status-badge {
  display: flex;
  align-items: center;
  gap: 8px;
  background: rgba(10, 16, 32, 0.85);
  border: 1px solid rgba(56, 189, 248, 0.35);
  padding: 6px 14px;
  border-radius: 9999px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.75rem;
  color: #38bdf8;
  backdrop-filter: blur(8px);
  box-shadow: 0 0 15px rgba(56, 189, 248, 0.2);
}

.neural-pulse-dot {
  width: 8px;
  height: 8px;
  background: #38bdf8;
  border-radius: 50%;
  box-shadow: 0 0 10px #38bdf8;
  animation: pulse-dot 1.4s ease-in-out infinite;
}

@keyframes pulse-dot {
  0%, 100% { transform: scale(1); opacity: 1; }
  50% { transform: scale(1.6); opacity: 0.4; }
}

.neural-mode-switchers {
  display: flex;
  gap: 8px;
  pointer-events: auto;
}

.mode-btn {
  background: rgba(15, 23, 42, 0.8);
  border: 1px solid rgba(255, 255, 255, 0.12);
  color: #94a3b8;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.72rem;
  padding: 6px 12px;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.25s ease;
  backdrop-filter: blur(8px);
}

.mode-btn:hover {
  border-color: #38bdf8;
  color: #f8fafc;
  box-shadow: 0 0 15px rgba(56, 189, 248, 0.25);
}

.mode-btn.active {
  background: rgba(56, 189, 248, 0.15);
  border-color: #38bdf8;
  color: #38bdf8;
  box-shadow: 0 0 20px rgba(56, 189, 248, 0.3);
}

.neural-action-btn {
  background: linear-gradient(135deg, rgba(99, 102, 241, 0.25), rgba(56, 189, 248, 0.25));
  border: 1px solid rgba(56, 189, 248, 0.5);
  color: #f8fafc;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.75rem;
  font-weight: 700;
  padding: 6px 14px;
  border-radius: 8px;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 6px;
  transition: all 0.25s ease;
  pointer-events: auto;
}

.neural-action-btn:hover {
  background: linear-gradient(135deg, rgba(99, 102, 241, 0.45), rgba(56, 189, 248, 0.45));
  box-shadow: 0 0 25px rgba(56, 189, 248, 0.4);
  transform: translateY(-1px);
}

.kb-instructions {
  position: absolute;
  bottom: 14px;
  left: 18px;
  z-index: 5;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.72rem;
  color: #64748b;
  display: flex;
  align-items: center;
  gap: 8px;
  background: rgba(3, 7, 18, 0.75);
  padding: 5px 12px;
  border-radius: 8px;
  border: 1px solid rgba(255, 255, 255, 0.08);
  pointer-events: none;
}

.neural-telemetry-hud {
  position: absolute;
  bottom: 14px;
  right: 18px;
  z-index: 5;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.7rem;
  color: #4ade80;
  background: rgba(3, 7, 18, 0.75);
  padding: 5px 12px;
  border-radius: 8px;
  border: 1px solid rgba(74, 222, 128, 0.2);
  pointer-events: none;
}

/* Dynamic Skill Telemetry Inspector Panel */
.skill-detail-panel {
  margin-top: 20px;
  background: rgba(10, 16, 32, 0.9);
  border: 1px solid rgba(56, 189, 248, 0.2);
  border-radius: 18px;
  padding: 24px 28px;
  transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
  position: relative;
  overflow: hidden;
}

.skill-detail-panel::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0; height: 2px;
  background: linear-gradient(90deg, transparent, #38bdf8, #818cf8, transparent);
}

.skill-detail-panel.active-glow {
  border-color: rgba(56, 189, 248, 0.8);
  box-shadow: 0 0 40px rgba(56, 189, 248, 0.25), 0 10px 30px rgba(0, 0, 0, 0.5);
  transform: translateY(-2px);
}
.skill-header-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
  flex-wrap: wrap;
  gap: 10px;
}
.skill-name-txt {
  font-size: 1.25rem;
  font-weight: 700;
  color: #38bdf8;
  font-family: 'JetBrains Mono', monospace;
  display: flex;
  align-items: center;
  gap: 10px;
}
.skill-badge-category {
  font-size: 0.68rem;
  padding: 2px 8px;
  background: rgba(99, 102, 241, 0.2);
  border: 1px solid rgba(99, 102, 241, 0.4);
  border-radius: 4px;
  color: #a5b4fc;
  font-weight: 500;
}
.skill-level-txt {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.85rem;
  color: #4ade80;
  display: flex;
  align-items: center;
  gap: 6px;
}
.skill-desc-txt {
  color: #cbd5e1;
  font-size: 0.95rem;
  line-height: 1.65;
}
.skill-meta-row {
  display: flex;
  gap: 20px;
  margin-top: 14px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.78rem;
  color: #94a3b8;
  flex-wrap: wrap;
}
.skill-meta-item b {
  color: #f1f5f9;
}
.skill-meter-track {
  margin-top: 16px;
  height: 6px;
  background: rgba(255, 255, 255, 0.08);
  border-radius: 4px;
  overflow: hidden;
  position: relative;
}
.skill-meter-fill {
  height: 100%;
  width: 95%;
  background: linear-gradient(90deg, #6366f1, #38bdf8, #4ade80);
  transition: width 0.6s cubic-bezier(0.16, 1, 0.3, 1);
  box-shadow: 0 0 12px rgba(56, 189, 248, 0.5);
}

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
    <div class="hero-photo-wrap">
      <img src="data:image/png;base64,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" alt="Aviral Bagjani">
    </div>
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
    <div class="sec-tag rv">// 02 — AUTONOMOUS 3D ARSENAL</div>
    <h2 class="sec-title rv">Neural Core &amp; <em>Agent DAG Matrix.</em></h2>
    
    <div class="keyboard-section-wrapper rv">
      <div class="keyboard-telemetry-header">
        <div class="kb-title-block">
          <h3>⚡ HOLOGRAPHIC MULTI-AGENT SYNAPTIC MATRIX</h3>
          <p>Real-time 3D synaptic orchestration graph. Nodes represent production systems; glowing laser synapses trace active data pipelines.</p>
        </div>
        <div class="kb-live-inspect" id="kb-active-chip">
          <span>ACTIVE SYNAPSE:</span> <b id="kb-chip-label">LANGGRAPH (CYCLE DAGS)</b>
        </div>
      </div>

      <!-- 3D NEURAL DAG VIEWPORT -->
      <div id="keyboard-3d-viewport">
        <!-- TOP HUD CONTROLS -->
        <div class="neural-hud-overlay">
          <div class="neural-status-badge">
            <span class="neural-pulse-dot"></span>
            <span id="neural-status-text">NEURAL SYNAPSE // ACTIVE</span>
          </div>
          <div class="neural-mode-switchers">
            <button class="mode-btn active" id="btn-mode-constellation" onclick="setTopology('constellation')">🌌 CONSTELLATION</button>
            <button class="mode-btn" id="btn-mode-dag" onclick="setTopology('dag')">⚡ AGENT DAG</button>
            <button class="mode-btn" id="btn-mode-ring" onclick="setTopology('ring')">🪐 ORBITAL</button>
            <button class="neural-action-btn" id="btn-trigger-run" onclick="triggerAgentRun()">
              <span>⚡</span> PULSE RUN
            </button>
          </div>
        </div>

        <!-- BOTTOM HUD TELEMETRY -->
        <div class="kb-instructions">
          <span>🎮 DRAG TO ORBIT · SCROLL TO ZOOM · HOVER / CLICK NODES TO LOCK FOCUS</span>
        </div>
        <div class="neural-telemetry-hud" id="neural-fps-hud">
          SYNAPSES: 14 // LATENCY: 12ms // STABLE
        </div>
      </div>

      <!-- DYNAMIC TELEMETRY PANEL -->
      <div class="skill-detail-panel" id="skill-inspector">
        <div class="skill-header-row">
          <div class="skill-name-txt" id="insp-name">
            <span>LangGraph &amp; Multi-Agent Workflows</span>
            <span class="skill-badge-category" id="insp-cat">AGENTIC ORCHESTRATION</span>
          </div>
          <div class="skill-level-txt" id="insp-stat">● 95% PRODUCTION READINESS</div>
        </div>
        <div class="skill-desc-txt" id="insp-desc">
          Stateful cyclic multi-agent DAGs, human-in-the-loop review nodes, checkpoint persistence, and distributed worker delegation.
        </div>
        <div class="skill-meta-row">
          <div class="skill-meta-item">ARCHITECTURE ROLE: <b id="insp-role">CORE ORCHESTRATOR</b></div>
          <div class="skill-meta-item">PIPELINE CONNECTIONS: <b id="insp-conn">MCP, REDIS LOCK, QDRANT, NEMO</b></div>
          <div class="skill-meta-item">BENCHMARK: <b id="insp-bench">&lt; 140ms DISPATCH</b></div>
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
bgRen.setPixelRatio(Math.min(window.devicePixelRatio || 1, 1.5));
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
/* ========================================================
   AUTONOMOUS 3D NEURAL CORE & SYNAPTIC AGENT DAG MATRIX
   ======================================================== */
const kbViewport = document.getElementById('keyboard-3d-viewport');
let kbInitialized = false;

function initNeuralMatrix() {
  if (kbInitialized || !kbViewport) return;
  kbInitialized = true;
  const kbScene = new THREE.Scene();
const kbCam = new THREE.PerspectiveCamera(45, kbViewport.clientWidth / kbViewport.clientHeight, 0.1, 100);
kbCam.position.set(0, 3.2, 7.8);
kbCam.lookAt(0, 0, 0);

const kbRen = new THREE.WebGLRenderer({ antialias: true, alpha: true });
kbRen.setSize(kbViewport.clientWidth, kbViewport.clientHeight);
kbRen.setPixelRatio(Math.min(window.devicePixelRatio || 1, 1.5));
kbViewport.appendChild(kbRen.domElement);

// Lighting
const kbAmb = new THREE.AmbientLight(0xffffff, 0.9);
kbScene.add(kbAmb);
const kbCoreLight = new THREE.PointLight(0x38bdf8, 4, 30);
kbCoreLight.position.set(0, 0, 0);
kbScene.add(kbCoreLight);
const kbAccentLight = new THREE.PointLight(0x818cf8, 3, 25);
kbAccentLight.position.set(4, 5, 4);
kbScene.add(kbAccentLight);
const kbGreenLight = new THREE.PointLight(0x4ade80, 2, 20);
kbGreenLight.position.set(-4, -4, -3);
kbScene.add(kbGreenLight);

// Group containing entire Neural Cosmos
const cosmosGroup = new THREE.Group();
kbScene.add(cosmosGroup);

/* ========================================================
   1. HOLOGRAPHIC QUANTUM AI CORE (Center Reactor)
   ======================================================== */
const coreGroup = new THREE.Group();
cosmosGroup.add(coreGroup);

// Inner Core: Faceted Glowing Icosahedron
const innerCoreGeo = new THREE.IcosahedronGeometry(0.85, 1);
const innerCoreMat = new THREE.MeshStandardMaterial({
  color: 0x0f172a,
  roughness: 0.1,
  metalness: 0.9,
  emissive: 0x38bdf8,
  emissiveIntensity: 0.6
});
const innerCoreMesh = new THREE.Mesh(innerCoreGeo, innerCoreMat);
coreGroup.add(innerCoreMesh);

// Outer Wireframe Hologram Shield
const coreWireGeo = new THREE.IcosahedronGeometry(1.05, 1);
const coreWireMat = new THREE.MeshBasicMaterial({
  color: 0x38bdf8,
  wireframe: true,
  transparent: true,
  opacity: 0.55
});
const coreWireMesh = new THREE.Mesh(coreWireGeo, coreWireMat);
coreGroup.add(coreWireMesh);

// Center Glowing Point Light Spark
const coreGlowGeo = new THREE.SphereGeometry(0.4, 16, 16);
const coreGlowMat = new THREE.MeshBasicMaterial({
  color: 0xffffff,
  transparent: true,
  opacity: 0.8
});
const coreGlowMesh = new THREE.Mesh(coreGlowGeo, coreGlowMat);
coreGroup.add(coreGlowMesh);

// 3 Gyroscopic Quantum Orbital Rings
const ringMaterials = [
  new THREE.MeshBasicMaterial({ color: 0x38bdf8, transparent: true, opacity: 0.65, side: THREE.DoubleSide }),
  new THREE.MeshBasicMaterial({ color: 0x818cf8, transparent: true, opacity: 0.55, side: THREE.DoubleSide }),
  new THREE.MeshBasicMaterial({ color: 0x4ade80, transparent: true, opacity: 0.45, side: THREE.DoubleSide })
];
const rings = [];
const ringRadii = [1.4, 1.85, 2.3];
ringRadii.forEach((rad, i) => {
  const ringGeo = new THREE.RingGeometry(rad, rad + 0.04, 64);
  const ringMesh = new THREE.Mesh(ringGeo, ringMaterials[i]);
  ringMesh.rotation.x = (i + 1) * 0.7;
  ringMesh.rotation.y = (i + 1) * 0.5;
  coreGroup.add(ringMesh);
  rings.push(ringMesh);
});

/* ========================================================
   2. SKILLS DATA DEFINITION (AI & GenAI Systems)
   ======================================================== */
const SKILLS_KEY_DATA = [
  {
    id: "langgraph",
    label: "LANGGRAPH",
    full: "LangGraph Multi-Agent Workflows",
    cat: "AGENTIC ORCHESTRATION",
    level: "95%",
    role: "CORE ORCHESTRATOR",
    conn: "MCP, REDIS LOCK, QDRANT, NEMO",
    bench: "< 140ms DISPATCH",
    desc: "Stateful cyclic multi-agent DAGs, human-in-the-loop review nodes, checkpoint persistence, and distributed worker delegation.",
    color: 0x38bdf8,
    constellation: { x: -2.6, y: 1.1, z: 0.8 },
    dag: { x: -3.2, y: 1.2, z: 0 },
    ring: { x: 3.2, y: 0.6, z: 0 }
  },
  {
    id: "mcp",
    label: "MCP",
    full: "Model Context Protocol Tooling",
    cat: "TOOL PROTOCOL",
    level: "94%",
    role: "AGENT TOOL BRIDGE",
    conn: "LANGGRAPH, FASTAPI, REDIS LOCK",
    bench: "DYNAMIC DISCOVERY",
    desc: "Model Context Protocol bridges for dynamic tool orchestration (Tavily search, Gmail integration, terminal & filesystems).",
    color: 0x60a5fa,
    constellation: { x: -1.8, y: 2.2, z: -0.6 },
    dag: { x: -1.6, y: 1.6, z: -0.3 },
    ring: { x: 2.6, y: -1.8, z: 0.4 }
  },
  {
    id: "qdrant",
    label: "QDRANT",
    full: "Qdrant Vector DB & Hybrid Search",
    cat: "VECTOR RETRIEVAL",
    level: "92%",
    role: "EMBEDDING STORE",
    conn: "LANGGRAPH, PYTORCH, FASTAPI",
    bench: "24ms SEMANTIC LATENCY",
    desc: "Hybrid dense/sparse vector indexing, payload metadata filters, and sub-second semantic retrieval pipelines.",
    color: 0x38bdf8,
    constellation: { x: -2.7, y: -0.9, z: 0.5 },
    dag: { x: -1.6, y: 0.0, z: 0.4 },
    ring: { x: 0.8, y: -3.0, z: -0.3 }
  },
  {
    id: "redis",
    label: "REDIS LOCK",
    full: "Redis Distributed Lock & Cache Shield",
    cat: "CACHE & CONCURRENCY",
    level: "90%",
    role: "DISTRIBUTED LOCK",
    conn: "LANGGRAPH, MCP, FASTAPI",
    bench: "-70% REDUNDANT CALLS",
    desc: "Single-flight distributed locking & cache shields preventing duplicate LLM executions and ensuring session consistency.",
    color: 0xf87171,
    constellation: { x: -0.6, y: 2.6, z: 0.7 },
    dag: { x: 0.0, y: 1.8, z: -0.4 },
    ring: { x: -1.8, y: -2.6, z: 0.5 }
  },
  {
    id: "nemo",
    label: "NEMO GUARD",
    full: "NeMo Guardrails & Safety",
    cat: "AI SAFETY & SHIELDS",
    level: "95%",
    role: "SECURITY BOUNDARY",
    conn: "LANGGRAPH, DEEPEVAL, FASTAPI",
    bench: ">95% JAILBREAK BLOCKED",
    desc: "Programmable guardrail colang flows blocking prompt injections, toxic outputs, and proprietary data exfiltration.",
    color: 0x4ade80,
    constellation: { x: 0.7, y: 2.5, z: -0.5 },
    dag: { x: 0.0, y: 0.2, z: 0.6 },
    ring: { x: -3.2, y: -0.7, z: -0.4 }
  },
  {
    id: "deepeval",
    label: "DEEPEVAL",
    full: "DeepEval Automated Unit Tests",
    cat: "AI EVALUATION",
    level: "92%",
    role: "EVALUATION HARNESS",
    conn: "NEMO, LANGSMITH, PYTORCH",
    bench: "G-EVAL / HALLUCINATION",
    desc: "Automated regression suites evaluating Answer Relevancy, G-Eval task metrics, and hallucination containment.",
    color: 0xa78bfa,
    constellation: { x: 2.0, y: 2.1, z: 0.8 },
    dag: { x: 1.6, y: 1.4, z: -0.3 },
    ring: { x: -2.7, y: 1.7, z: 0.3 }
  },
  {
    id: "langsmith",
    label: "LANGSMITH",
    full: "LangSmith Traces & Observability",
    cat: "LLM OBSERVABILITY",
    level: "88%",
    role: "TRACE TELEMETRY",
    conn: "LANGGRAPH, DEEPEVAL, DOCKER",
    bench: "TOKEN & LATENCY AUDIT",
    desc: "End-to-end multi-agent execution traces, token consumption attribution, and production latency debugging.",
    color: 0xfbbf24,
    constellation: { x: 2.8, y: 1.0, z: -0.7 },
    dag: { x: 1.6, y: -0.2, z: 0.4 },
    ring: { x: -0.9, y: 3.1, z: -0.5 }
  },
  {
    id: "fastapi",
    label: "FASTAPI",
    full: "FastAPI Asynchronous Gateway",
    cat: "BACKEND RUNTIME",
    level: "93%",
    role: "API GATEWAY",
    conn: "LANGGRAPH, POSTGRES, DOCKER",
    bench: "SSE STREAMING ENGINE",
    desc: "High-throughput asynchronous Python microservices with streaming Server-Sent Events and strict Pydantic schemas.",
    color: 0x2dd4bf,
    constellation: { x: 0.8, y: -2.4, z: 0.8 },
    dag: { x: 0.0, y: -1.6, z: -0.2 },
    ring: { x: 1.2, y: 2.9, z: 0.6 }
  },
  {
    id: "pytorch",
    label: "PYTORCH",
    full: "PyTorch & Tensor Operations",
    cat: "DEEP LEARNING",
    level: "84%",
    role: "MODEL ENGINE",
    conn: "QDRANT, DEEPEVAL, FASTAPI",
    bench: "EMBEDDING OPTIMIZED",
    desc: "Embeddings projection, tensor transformations, LoRA fine-tuning, and neural representation modeling.",
    color: 0xf97316,
    constellation: { x: -1.9, y: -2.3, z: -0.6 },
    dag: { x: -1.6, y: -1.6, z: 0.2 },
    ring: { x: 2.8, y: 1.5, z: -0.4 }
  },
  {
    id: "postgres",
    label: "POSTGRES",
    full: "PostgreSQL & Relational Data",
    cat: "DATA PERSISTENCE",
    level: "86%",
    role: "TRANSACTION STATE",
    conn: "FASTAPI, DOCKER, REDIS",
    bench: "ACID TRANSACTIONS",
    desc: "User sessions, relational conversation storage, durable state tracking, and audited metadata tables.",
    color: 0x38bdf8,
    constellation: { x: 2.1, y: -2.1, z: -0.5 },
    dag: { x: 1.6, y: -1.6, z: -0.3 },
    ring: { x: 0.0, y: 3.3, z: 0.0 }
  },
  {
    id: "docker",
    label: "DOCKER",
    full: "Docker Containers & Networking",
    cat: "CLOUD DEPLOYMENT",
    level: "85%",
    role: "CONTAINER RUNTIME",
    conn: "FASTAPI, POSTGRES, LANGSMITH",
    bench: "REPRODUCIBLE AGENTS",
    desc: "Reproducible containerized runtimes for multi-agent microservices, private bridge networks, and cloud deploys.",
    color: 0x38bdf8,
    constellation: { x: 2.7, y: -0.8, z: 0.7 },
    dag: { x: 3.2, y: -0.8, z: 0.1 },
    ring: { x: -3.0, y: 0.0, z: 0.6 }
  },
  {
    id: "leetcode",
    label: "LEETCODE",
    full: "LeetCode Knight (Rating 1784)",
    cat: "ALGORITHMS & DSA",
    level: "1784",
    role: "COMPLEXITY MASTERY",
    conn: "LANGGRAPH, PYTORCH, FASTAPI",
    bench: "500+ PROBLEMS SOLVED",
    desc: "Knight badge (top 6%), graph algorithms, dynamic programming, shortest-path traversals, and scalable system logic.",
    color: 0xeab308,
    constellation: { x: 0.0, y: -2.7, z: -0.9 },
    dag: { x: 3.2, y: 1.0, z: -0.2 },
    ring: { x: 0.0, y: -3.3, z: 0.0 }
  }
];

// Helper: 3D Billboard Canvas Sprite for Node Labels
function makeTextSprite(message, colorHex) {
  const cv = document.createElement('canvas');
  cv.width = 512;
  cv.height = 128;
  const ctx = cv.getContext('2d');
  
  // Background pill
  ctx.fillStyle = 'rgba(10, 16, 32, 0.85)';
  ctx.strokeStyle = colorHex;
  ctx.lineWidth = 4;
  ctx.beginPath();
  if (ctx.roundRect) {
    ctx.roundRect(16, 16, 480, 96, 48);
  } else {
    ctx.rect(16, 16, 480, 96);
  }
  ctx.fill();
  ctx.stroke();

  // Text
  ctx.fillStyle = '#f8fafc';
  ctx.font = 'bold 44px "JetBrains Mono", monospace';
  ctx.textAlign = 'center';
  ctx.textBaseline = 'middle';
  ctx.fillText(message, 256, 64);

  const tex = new THREE.CanvasTexture(cv);
  const spriteMat = new THREE.SpriteMaterial({ map: tex, transparent: true, opacity: 0.88 });
  const sprite = new THREE.Sprite(spriteMat);
  sprite.scale.set(1.4, 0.35, 1);
  return sprite;
}

/* ========================================================
   3. SPAWN 3D HOLOGRAPHIC SKILL NODES
   ======================================================== */
const skillNodes = [];

SKILLS_KEY_DATA.forEach((data) => {
  const nodeGroup = new THREE.Group();
  
  // Outer Diamond / Octahedron Crystalline Shell
  const gemGeo = new THREE.OctahedronGeometry(0.38, 0);
  const gemMat = new THREE.MeshStandardMaterial({
    color: 0x0f172a,
    emissive: data.color,
    emissiveIntensity: 0.45,
    roughness: 0.2,
    metalness: 0.8
  });
  const gemMesh = new THREE.Mesh(gemGeo, gemMat);
  nodeGroup.add(gemMesh);

  // Wireframe Halo
  const wireGeo = new THREE.OctahedronGeometry(0.48, 0);
  const wireMat = new THREE.MeshBasicMaterial({
    color: data.color,
    wireframe: true,
    transparent: true,
    opacity: 0.65
  });
  const wireMesh = new THREE.Mesh(wireGeo, wireMat);
  nodeGroup.add(wireMesh);

  // Floating Overhead Label Sprite
  const hexStr = '#' + data.color.toString(16).padStart(6, '0');
  const sprite = makeTextSprite(data.label, hexStr);
  sprite.position.y = 0.65;
  nodeGroup.add(sprite);

  // Initial Position: Constellation mode
  nodeGroup.position.set(data.constellation.x, data.constellation.y, data.constellation.z);

  // Store metadata
  nodeGroup.userData = {
    data: data,
    gemMesh: gemMesh,
    wireMesh: wireMesh,
    sprite: sprite,
    baseColor: data.color,
    targetPos: { ...data.constellation },
    origScale: 1
  };

  cosmosGroup.add(nodeGroup);
  skillNodes.push(nodeGroup);
});

/* ========================================================
   4. SYNAPTIC LASER DAG CONNECTIONS & DATA PACKETS
   ======================================================== */
const SYNAPSE_CONNECTIONS = [
  ["langgraph", "mcp"],
  ["langgraph", "redis"],
  ["langgraph", "qdrant"],
  ["langgraph", "nemo"],
  ["mcp", "fastapi"],
  ["qdrant", "pytorch"],
  ["qdrant", "fastapi"],
  ["nemo", "deepeval"],
  ["deepeval", "langsmith"],
  ["fastapi", "postgres"],
  ["fastapi", "docker"],
  ["langsmith", "docker"],
  ["leetcode", "langgraph"],
  ["leetcode", "pytorch"]
];

const synapseLines = [];
const dataPackets = [];

// Create Synapse Lines
SYNAPSE_CONNECTIONS.forEach(([fromId, toId]) => {
  const fromNode = skillNodes.find(n => n.userData.data.id === fromId);
  const toNode = skillNodes.find(n => n.userData.data.id === toId);
  if (!fromNode || !toNode) return;

  const points = [fromNode.position.clone(), toNode.position.clone()];
  const lineGeo = new THREE.BufferGeometry().setFromPoints(points);
  const lineMat = new THREE.LineBasicMaterial({
    color: 0x38bdf8,
    transparent: true,
    opacity: 0.35,
    linewidth: 2
  });
  const lineMesh = new THREE.Line(lineGeo, lineMat);
  cosmosGroup.add(lineMesh);

  synapseLines.push({
    mesh: lineMesh,
    fromNode: fromNode,
    toNode: toNode
  });

  // Glowing traveling photon packet
  const packetGeo = new THREE.SphereGeometry(0.06, 8, 8);
  const packetMat = new THREE.MeshBasicMaterial({ color: 0x4ade80 });
  const packetMesh = new THREE.Mesh(packetGeo, packetMat);
  cosmosGroup.add(packetMesh);

  dataPackets.push({
    mesh: packetMesh,
    fromNode: fromNode,
    toNode: toNode,
    progress: Math.random(),
    speed: 0.006 + Math.random() * 0.008
  });
});

/* ========================================================
   5. TOPOLOGY MORPHING ENGINE (Constellation / DAG / Ring)
   ======================================================== */
let currentTopology = 'constellation';

window.setTopology = function(mode) {
  currentTopology = mode;
  document.querySelectorAll('.mode-btn').forEach(btn => btn.classList.remove('active'));
  const activeBtn = document.getElementById('btn-mode-' + mode);
  if (activeBtn) activeBtn.classList.add('active');

  const hudTxt = document.getElementById('neural-status-text');
  if (hudTxt) {
    if (mode === 'constellation') hudTxt.textContent = "NEURAL CONSTELLATION // 3D MATRIX";
    if (mode === 'dag') hudTxt.textContent = "AGENTIC DAG // PIPELINE STAGES";
    if (mode === 'ring') hudTxt.textContent = "ORBITAL RUNTIME // GYROSCOPIC";
  }

  // Morph each node with GSAP
  skillNodes.forEach((node, i) => {
    const target = node.userData.data[mode];
    if (target) {
      gsap.to(node.position, {
        x: target.x,
        y: target.y,
        z: target.z,
        duration: 1.2,
        delay: i * 0.03,
        ease: "power3.inOut"
      });
    }
  });

  playChime(560);
};

/* ========================================================
   6. TRIGGER AGENT RUN: SHOCKWAVE PULSE
   ======================================================== */
window.triggerAgentRun = function() {
  playChime(880);
  
  // Core flare up
  gsap.to(innerCoreMesh.scale, { x: 1.8, y: 1.8, z: 1.8, duration: 0.2, yoyo: true, repeat: 1, ease: "power2.out" });
  gsap.to(coreWireMesh.scale, { x: 2.2, y: 2.2, z: 2.2, duration: 0.35, yoyo: true, repeat: 1, ease: "power2.out" });

  // Camera pulse
  gsap.to(kbCam.position, { z: 6.8, duration: 0.25, yoyo: true, repeat: 1, ease: "power2.inOut" });

  // Flash all synapse lines and nodes
  synapseLines.forEach((syn, idx) => {
    syn.mesh.material.color.setHex(0x4ade80);
    syn.mesh.material.opacity = 0.9;
    setTimeout(() => {
      syn.mesh.material.color.setHex(0x38bdf8);
      syn.mesh.material.opacity = 0.35;
    }, 450 + idx * 30);
  });

  // Stagger scale bump on skill nodes
  skillNodes.forEach((node, i) => {
    gsap.to(node.scale, {
      x: 1.45, y: 1.45, z: 1.45,
      duration: 0.18,
      delay: 0.1 + i * 0.02,
      yoyo: true,
      repeat: 1,
      ease: "back.out(2)"
    });
  });

  const hudStatus = document.getElementById('neural-status-text');
  if (hudStatus) {
    const orig = hudStatus.textContent;
    hudStatus.textContent = "⚡ AGENT RUNNING: 100% PIPELINE SYNAPSE SURGE";
    setTimeout(() => hudStatus.textContent = orig, 1800);
  }
};

/* ========================================================
   7. INTERACTIVE RAYCASTING, HOVER & FOCUS
   ======================================================== */
const raycaster = new THREE.Raycaster();
const kbMouse = new THREE.Vector2(-999, -999);
let hoveredNode = null;

const chipLabel = document.getElementById('kb-chip-label');
const inspName = document.getElementById('insp-name');
const inspStat = document.getElementById('insp-stat');
const inspDesc = document.getElementById('insp-desc');
const inspFill = document.getElementById('insp-fill');
const inspCat = document.getElementById('insp-cat');
const inspRole = document.getElementById('insp-role');
const inspConn = document.getElementById('insp-conn');
const inspBench = document.getElementById('insp-bench');
const skillInspector = document.getElementById('skill-inspector');

function selectSkillNode(nodeGroup) {
  const d = nodeGroup.userData.data;

  // Sound effect
  playChime(640);

  // Update Telemetry Panel
  if (chipLabel) chipLabel.textContent = d.full.toUpperCase();
  if (inspName) {
    inspName.innerHTML = `<span>${d.full}</span><span class="skill-badge-category">${d.cat}</span>`;
  }
  if (inspStat) inspStat.textContent = `● ${d.level} PRODUCTION READINESS`;
  if (inspDesc) inspDesc.textContent = d.desc;
  if (inspRole) inspRole.textContent = d.role;
  if (inspConn) inspConn.textContent = d.conn;
  if (inspBench) inspBench.textContent = d.bench;
  if (inspFill) {
    const pct = parseInt(d.level) || 95;
    inspFill.style.width = Math.min(pct, 100) + '%';
  }

  // Active glow trigger
  if (skillInspector) {
    skillInspector.classList.add('active-glow');
    setTimeout(() => skillInspector.classList.remove('active-glow'), 500);
  }

  // Node scale bounce & halo flare
  gsap.killTweensOf(nodeGroup.scale);
  gsap.to(nodeGroup.scale, {
    x: 1.4, y: 1.4, z: 1.4,
    duration: 0.15,
    yoyo: true,
    repeat: 1,
    ease: "power2.out",
    onComplete: () => {
      nodeGroup.scale.set(1, 1, 1);
    }
  });

  // Highlight connected lines
  synapseLines.forEach(syn => {
    if (syn.fromNode === nodeGroup || syn.toNode === nodeGroup) {
      syn.mesh.material.color.setHex(0x4ade80);
      syn.mesh.material.opacity = 0.95;
      setTimeout(() => {
        syn.mesh.material.color.setHex(0x38bdf8);
        syn.mesh.material.opacity = 0.35;
      }, 700);
    }
  });
}

function updateKbRaycast() {
  raycaster.setFromCamera(kbMouse, kbCam);
  
  // Test intersection against all node groups
  const testMeshes = skillNodes.map(n => n.userData.gemMesh);
  const intersects = raycaster.intersectObjects(testMeshes);

  if (intersects.length > 0) {
    const hitMesh = intersects[0].object;
    const hitGroup = hitMesh.parent;

    if (hoveredNode !== hitGroup) {
      // Reset previous
      if (hoveredNode) {
        gsap.to(hoveredNode.scale, { x: 1, y: 1, z: 1, duration: 0.2 });
        hoveredNode.userData.wireMesh.material.color.setHex(hoveredNode.userData.baseColor);
        hoveredNode.userData.wireMesh.material.opacity = 0.65;
      }
      hoveredNode = hitGroup;
      gsap.to(hoveredNode.scale, { x: 1.25, y: 1.25, z: 1.25, duration: 0.2, ease: "power2.out" });
      hoveredNode.userData.wireMesh.material.color.setHex(0x4ade80);
      hoveredNode.userData.wireMesh.material.opacity = 1;
      kbViewport.style.cursor = 'pointer';
    }
  } else {
    if (hoveredNode) {
      gsap.to(hoveredNode.scale, { x: 1, y: 1, z: 1, duration: 0.2 });
      hoveredNode.userData.wireMesh.material.color.setHex(hoveredNode.userData.baseColor);
      hoveredNode.userData.wireMesh.material.opacity = 0.65;
      hoveredNode = null;
      kbViewport.style.cursor = 'default';
    }
  }
}

// Mouse events on Viewport
kbViewport.addEventListener('mousemove', (e) => {
  const rect = kbViewport.getBoundingClientRect();
  kbMouse.x = ((e.clientX - rect.left) / rect.width) * 2 - 1;
  kbMouse.y = -((e.clientY - rect.top) / rect.height) * 2 + 1;
});

kbViewport.addEventListener('mouseleave', () => {
  kbMouse.x = -999;
  kbMouse.y = -999;
});

kbViewport.addEventListener('click', () => {
  if (hoveredNode) {
    selectSkillNode(hoveredNode);
  }
});

/* ========================================================
   8. 3D ORBIT DRAG & ZOOM CONTROLS
   ======================================================== */
let isDraggingKb = false;
let prevMouseX = 0;
let prevMouseY = 0;
let targetRotY = 0;
let targetRotX = 0;

kbViewport.addEventListener('mousedown', (e) => {
  if (e.target.closest('.neural-hud-overlay')) return;
  isDraggingKb = true;
  prevMouseX = e.clientX;
  prevMouseY = e.clientY;
});

window.addEventListener('mouseup', () => {
  isDraggingKb = false;
});

window.addEventListener('mousemove', (e) => {
  if (!isDraggingKb) return;
  const deltaX = e.clientX - prevMouseX;
  const deltaY = e.clientY - prevMouseY;
  targetRotY += deltaX * 0.008;
  targetRotX += deltaY * 0.008;
  targetRotX = Math.max(-0.6, Math.min(0.6, targetRotX));
  prevMouseX = e.clientX;
  prevMouseY = e.clientY;
});

// Mouse wheel zoom
kbViewport.addEventListener('wheel', (e) => {
  e.preventDefault();
  kbCam.position.z += e.deltaY * 0.003;
  kbCam.position.z = Math.max(4.5, Math.min(10.5, kbCam.position.z));
}, { passive: false });

/* ========================================================
   9. RENDER & ANIMATION LOOP
   ======================================================== */
let clock = new THREE.Clock();

function animateKb() {
  requestAnimationFrame(animateKb);
  const delta = clock.getDelta();
  const time = clock.getElapsedTime();

  // Subtle continuous ambient rotation
  if (!isDraggingKb) {
    targetRotY += 0.0025;
  }
  cosmosGroup.rotation.y += (targetRotY - cosmosGroup.rotation.y) * 0.08;
  cosmosGroup.rotation.x += (targetRotX - cosmosGroup.rotation.x) * 0.08;

  // Quantum core dynamic rotation & pulsing
  innerCoreMesh.rotation.y += 0.015;
  innerCoreMesh.rotation.x += 0.01;
  coreWireMesh.rotation.y -= 0.02;
  coreWireMesh.rotation.z += 0.015;

  rings[0].rotation.z += 0.02;
  rings[1].rotation.x += 0.025;
  rings[2].rotation.y += 0.018;

  // Float nodes gently
  skillNodes.forEach((node, idx) => {
    node.position.y += Math.sin(time * 2 + idx) * 0.0015;
    node.userData.gemMesh.rotation.y += 0.015;
    node.userData.wireMesh.rotation.y -= 0.02;
  });

  // Update Synapse Line Points
  synapseLines.forEach(syn => {
    const pos = syn.mesh.geometry.attributes.position;
    pos.setXYZ(0, syn.fromNode.position.x, syn.fromNode.position.y, syn.fromNode.position.z);
    pos.setXYZ(1, syn.toNode.position.x, syn.toNode.position.y, syn.toNode.position.z);
    pos.needsUpdate = true;
  });

  // Travel Data Packets
  dataPackets.forEach(pkt => {
    pkt.progress += pkt.speed;
    if (pkt.progress > 1) pkt.progress = 0;

    const p1 = pkt.fromNode.position;
    const p2 = pkt.toNode.position;
    pkt.mesh.position.lerpVectors(p1, p2, pkt.progress);
  });

  updateKbRaycast();
  kbRen.render(kbScene, kbCam);
}
animateKb();
} // End initNeuralMatrix

// PROGRESSIVE BOOT: Boot 3D Matrix on idle or when scrolled near
if ('IntersectionObserver' in window && kbViewport) {
  const kbObserver = new IntersectionObserver((entries) => {
    if (entries[0].isIntersecting) {
      initNeuralMatrix();
      kbObserver.disconnect();
    }
  }, { rootMargin: '300px' });
  kbObserver.observe(kbViewport);
}
// Fallback: init after 400ms idle so it's pre-rendered for instant interaction
setTimeout(initNeuralMatrix, 400);

window.addEventListener('resize', () => {
  if (!kbViewport) return;
  kbCam.aspect = kbViewport.clientWidth / kbViewport.clientHeight;
  kbCam.updateProjectionMatrix();
  kbRen.setSize(kbViewport.clientWidth, kbViewport.clientHeight);
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

// INSTANT LOADER DISMISSAL: Show hero immediately without artificial delays
function hideLoaderFast() {
  const l = document.getElementById('loader');
  if (l && !l.classList.contains('hide')) {
    l.classList.add('hide');
    try { playChime(440); } catch(e){}
  }
}
if (document.readyState === 'complete' || document.readyState === 'interactive') {
  setTimeout(hideLoaderFast, 150);
} else {
  document.addEventListener('DOMContentLoaded', () => setTimeout(hideLoaderFast, 150));
  window.addEventListener('load', () => setTimeout(hideLoaderFast, 80));
}
setTimeout(hideLoaderFast, 600); // Fail-safe max timeout

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



# import streamlit as st
# import streamlit.components.v1 as components

# st.set_page_config(
#     page_title="Aviral Bagjani | AI & GenAI Systems Engineer",
#     page_icon="⚡",
#     layout="wide",
# )

# # Strip Streamlit default padding and chrome so the 3D portfolio spans edge-to-edge
# st.markdown("""
# <style>
#     header[data-testid="stHeader"] { display: none !important; }
#     #MainMenu { display: none !important; }
#     footer { display: none !important; }
#     .block-container { padding: 0 !important; margin: 0 !important; max-width: 100vw !important; }
#     iframe { border: none !important; width: 100vw !important; height: 100vh !important; }
# </style>
# """, unsafe_allow_html=True)

# PORTFOLIO = r"""<!DOCTYPE html>
# <html lang="en">
# <head>
# <meta charset="UTF-8">
# <meta name="viewport" content="width=device-width, initial-scale=1.0">
# <title>Aviral Bagjani — AI & GenAI Systems Engineer</title>
# <link rel="preconnect" href="https://fonts.googleapis.com">
# <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
# <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
# <!-- Three.js & GSAP -->
# <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
# <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>

# <style>
# *{margin:0;padding:0;box-sizing:border-box}
# html{scroll-behavior:smooth}
# body{
#   background:#030712;
#   color:#f3f4f6;
#   font-family:'Space Grotesk',sans-serif;
#   overflow:hidden;
#   height:100vh;
#   width:100vw;
# }
# ::selection{background:#6366f1;color:#fff}

# /* BACKGROUND 3D CANVAS */
# #canvas3d{
#   position:fixed;
#   inset:0;
#   z-index:0;
#   pointer-events:auto;
# }

# /* SCROLL CONTAINER */
# #frame{
#   position:relative;
#   z-index:1;
#   height:100vh;
#   overflow-y:scroll;
#   scrollbar-width:none;
# }
# #frame::-webkit-scrollbar{display:none}

# /* PRELOADER */
# #loader{
#   position:fixed;inset:0;z-index:999;background:#030712;
#   display:flex;flex-direction:column;align-items:center;justify-content:center;gap:18px;
#   transition:opacity .7s ease,visibility .7s;
# }
# #loader.hide{opacity:0;visibility:hidden}
# .loader-logo{font-family:'JetBrains Mono',monospace;font-size:1.1rem;letter-spacing:.35em;color:#38bdf8}
# .loader-bar{width:240px;height:2px;background:rgba(255,255,255,.08);border-radius:2px;overflow:hidden}
# .loader-bar i{display:block;height:100%;width:35%;background:linear-gradient(90deg,#6366f1,#38bdf8,#818cf8);animation:slide 1.2s ease-in-out infinite}
# @keyframes slide{0%{transform:translateX(-100%)}100%{transform:translateX(320%)}}

# /* CUSTOM GLOW CURSOR */
# #cursor{
#   position:fixed;width:28px;height:28px;border:1.5px solid rgba(56,189,248,.8);border-radius:50%;
#   pointer-events:none;z-index:990;transform:translate(-50%,-50%);
#   transition:width .2s,height .2s,background .2s,border-color .2s;mix-blend-mode:screen;
# }
# #cursor.hot{width:56px;height:56px;background:rgba(56,189,248,.18);border-color:#818cf8}
# #cursor-dot{
#   position:fixed;width:5px;height:5px;background:#38bdf8;border-radius:50%;
#   pointer-events:none;z-index:991;transform:translate(-50%,-50%);
# }

# /* TOP HUD NAVIGATION */
# nav{
#   position:sticky;top:0;z-index:100;display:flex;justify-content:space-between;align-items:center;
#   padding:16px 5vw;backdrop-filter:blur(20px);background:rgba(3,7,18,.75);
#   border-bottom:1px solid rgba(255,255,255,.08);
# }
# .brand{display:flex;align-items:center;gap:12px}
# .logo{font-family:'JetBrains Mono',monospace;font-weight:700;color:#f3f4f6;font-size:1.1rem;letter-spacing:-.02em}
# .logo span{color:#38bdf8}
# .badge-ping{display:inline-flex;align-items:center;gap:6px;padding:3px 10px;border-radius:99px;font-size:.7rem;font-family:'JetBrains Mono',monospace;background:rgba(34,197,94,.1);border:1px solid rgba(34,197,94,.3);color:#4ade80}
# .badge-ping i{width:6px;height:6px;border-radius:50%;background:#4ade80;box-shadow:0 0 8px #4ade80;animation:pulse 1.8s infinite}
# @keyframes pulse{50%{opacity:.3}}

# .hud-telemetry{
#   display:flex;align-items:center;gap:16px;
#   font-family:'JetBrains Mono',monospace;font-size:.75rem;
# }
# .hud-pill{
#   padding:5px 12px;border-radius:8px;background:rgba(56,189,248,.08);
#   border:1px solid rgba(56,189,248,.25);color:#38bdf8;
# }
# .audio-toggle{
#   background:transparent;border:1px solid rgba(255,255,255,.15);color:#94a3b8;
#   padding:5px 12px;border-radius:8px;cursor:pointer;font-family:'JetBrains Mono',monospace;
#   font-size:.75rem;transition:.2s;display:flex;align-items:center;gap:6px;
# }
# .audio-toggle:hover{border-color:#38bdf8;color:#38bdf8}

# .nav-links a{color:#94a3b8;text-decoration:none;margin-left:24px;font-size:.86rem;transition:.2s}
# .nav-links a:hover{color:#38bdf8}
# .nav-links a b{color:#6366f1;font-family:'JetBrains Mono',monospace;margin-right:4px}

# /* HERO SECTION */
# .hero{min-height:94vh;display:flex;flex-direction:column;justify-content:center;padding:0 6vw;position:relative}
# .hero-tag{
#   display:inline-flex;align-items:center;gap:10px;padding:6px 16px;border-radius:99px;
#   font-family:'JetBrains Mono',monospace;font-size:.78rem;color:#93c5fd;
#   background:rgba(59,130,246,.08);border:1px solid rgba(59,130,246,.28);width:fit-content;margin-bottom:24px;
# }
# .hero h1{font-size:clamp(2.7rem,6.8vw,5.2rem);font-weight:700;line-height:1.05;letter-spacing:-.04em;margin-bottom:18px;max-width:880px}
# .hero h1 .grad{
#   background:linear-gradient(120deg,#818cf8 0%,#38bdf8 50%,#c084fc 100%);
#   -webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;
# }
# .typer{font-family:'JetBrains Mono',monospace;font-size:clamp(1.05rem,2.2vw,1.4rem);color:#38bdf8;min-height:1.6em;margin-bottom:22px}
# .typer::after{content:'▍';animation:blink 1s infinite}
# @keyframes blink{50%{opacity:0}}
# .hero p.desc{max-width:640px;color:#9ca3af;line-height:1.75;font-size:1.03rem;margin-bottom:34px}
# .hero p.desc b{color:#f3f4f6}

# /* HERO PHOTO */
# .hero-photo{
#   position:absolute;
#   right:7vw;
#   top:50%;
#   transform:translateY(-52%);
#   width:clamp(200px,19vw,300px);
#   aspect-ratio:195/243;
#   object-fit:cover;
#   border-radius:26px;
#   border:1px solid rgba(99,102,241,.45);
#   box-shadow:0 0 0 1px rgba(255,255,255,.05),0 24px 60px -18px rgba(56,189,248,.45),0 0 90px -20px rgba(99,102,241,.55);
#   z-index:2;
#   background:#0b1120;
# }
# .hero-photo-wrap{
#   position:absolute;
#   right:7vw;
#   top:50%;
#   transform:translateY(-52%);
#   z-index:2;
#   padding:8px;
#   border-radius:30px;
#   background:linear-gradient(140deg,rgba(99,102,241,.55),rgba(56,189,248,.25) 45%,rgba(192,132,252,.4));
# }
# .hero-photo-wrap img{
#   display:block;
#   width:clamp(230px,22vw,340px);
#   aspect-ratio:195/243;
#   object-fit:cover;
#   border-radius:22px;
#   background:#0b1120;
# }
# @media(max-width:920px){
#   .hero-photo-wrap{
#     position:relative;
#     right:auto;top:auto;transform:none;
#     margin-bottom:30px;
#     width:fit-content;
#   }
#   .hero-photo-wrap img{width:170px}
# }

# .btn-row{display:flex;gap:14px;flex-wrap:wrap}
# .btn{padding:13px 26px;border-radius:12px;text-decoration:none;font-weight:600;font-size:.9rem;transition:.25s;cursor:pointer;display:inline-flex;align-items:center;gap:8px}
# .btn-solid{background:linear-gradient(120deg,#6366f1,#38bdf8);color:#fff;box-shadow:0 8px 24px -8px rgba(99,102,241,.6)}
# .btn-solid:hover{transform:translateY(-3px);box-shadow:0 14px 32px -8px rgba(99,102,241,.85)}
# .btn-ghost{border:1px solid rgba(255,255,255,.16);color:#f3f4f6;background:rgba(255,255,255,.02);backdrop-filter:blur(8px)}
# .btn-ghost:hover{border-color:#38bdf8;color:#38bdf8;transform:translateY(-3px)}

# .hero-hint{
#   position:absolute;bottom:30px;right:6vw;font-family:'JetBrains Mono',monospace;font-size:.72rem;
#   color:#64748b;letter-spacing:.15em;display:flex;align-items:center;gap:8px;
# }
# .hero-hint .ring{width:8px;height:8px;border-radius:50%;border:1.5px solid #38bdf8;animation:pulse 1.5s infinite}

# /* SECTIONS */
# section{padding:90px 6vw;max-width:1180px;margin:0 auto;position:relative}
# .sec-tag{font-family:'JetBrains Mono',monospace;color:#38bdf8;font-size:.78rem;letter-spacing:.25em;margin-bottom:10px}
# .sec-title{font-size:clamp(1.9rem,3.8vw,2.7rem);letter-spacing:-.03em;margin-bottom:44px}
# .sec-title em{font-style:normal;color:#38bdf8}

# /* METRICS STATS */
# .stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:16px;margin-bottom:20px}
# .stat{background:rgba(15,23,42,.65);border:1px solid rgba(255,255,255,.08);border-radius:18px;padding:26px 22px;text-align:center;backdrop-filter:blur(14px);transition:.3s}
# .stat:hover{transform:translateY(-5px);border-color:rgba(56,189,248,.5);box-shadow:0 15px 35px -15px rgba(56,189,248,.3)}
# .stat .n{font-family:'JetBrains Mono',monospace;font-size:2.2rem;font-weight:700;background:linear-gradient(120deg,#38bdf8,#818cf8);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
# .stat .l{font-size:.78rem;color:#94a3b8;margin-top:6px;letter-spacing:.03em}

# /* PROJECT CARDS */
# .card{position:relative;background:rgba(15,23,42,.65);border:1px solid rgba(255,255,255,.08);border-radius:22px;padding:36px;margin-bottom:26px;backdrop-filter:blur(16px);overflow:hidden;transition:border-color .3s,box-shadow .3s,transform .3s}
# .card:hover{border-color:rgba(56,189,248,.55);box-shadow:0 24px 50px -18px rgba(56,189,248,.35)}
# .card::before{
#   content:'';position:absolute;top:var(--mx,-1000px);left:var(--my,-1000px);width:450px;height:450px;
#   background:radial-gradient(circle,rgba(56,189,248,.14),transparent 70%);transform:translate(-50%,-50%);
#   pointer-events:none;border-radius:50%;
# }
# .card h3{font-size:1.4rem;margin-bottom:6px;color:#fff}
# .card .role{color:#818cf8;font-size:.92rem;font-family:'JetBrains Mono',monospace;margin-bottom:14px}
# .card p{color:#94a3b8;line-height:1.75;font-size:.96rem}
# .card p b{color:#f3f4f6}
# .tags{display:flex;flex-wrap:wrap;gap:8px;margin-top:22px}
# .tag{font-family:'JetBrains Mono',monospace;font-size:.72rem;color:#cbd5e1;background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.1);padding:5px 12px;border-radius:8px}
# .tag.hi{color:#38bdf8;border-color:rgba(56,189,248,.4);background:rgba(56,189,248,.09)}

# /* ========================================================
#    AKASH-INSPIRED 3D INTERACTIVE KEYBOARD ARSENAL
#    ======================================================== */
# .keyboard-section-wrapper{
#   background:rgba(15,23,42,.7);border:1px solid rgba(56,189,248,.25);
#   border-radius:24px;padding:32px;backdrop-filter:blur(20px);position:relative;overflow:hidden;
#   box-shadow:0 20px 60px -20px rgba(56,189,248,.2);
# }
# .keyboard-telemetry-header{
#   display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;
#   border-bottom:1px solid rgba(255,255,255,.08);padding-bottom:18px;margin-bottom:24px;
# }
# .kb-title-block h3{font-size:1.25rem;font-weight:700;color:#fff;display:flex;align-items:center;gap:10px}
# .kb-title-block p{font-size:.82rem;color:#94a3b8;font-family:'JetBrains Mono',monospace;margin-top:4px}
# .kb-live-inspect{
#   background:rgba(56,189,248,.08);border:1px solid rgba(56,189,248,.3);
#   padding:8px 16px;border-radius:10px;font-family:'JetBrains Mono',monospace;
#   font-size:.8rem;color:#38bdf8;display:flex;align-items:center;gap:10px;
# }

# /* 3D Keyboard Scene Container */
# #keyboard-3d-viewport{
#   width:100%;height:380px;border-radius:18px;background:rgba(3,7,18,.8);
#   border:1px solid rgba(255,255,255,.06);position:relative;overflow:hidden;
# }
# .kb-instructions{
#   position:absolute;bottom:14px;left:18px;z-index:5;
#   font-family:'JetBrains Mono',monospace;font-size:.72rem;color:#64748b;
#   display:flex;align-items:center;gap:8px;background:rgba(3,7,18,.6);
#   padding:4px 10px;border-radius:6px;border:1px solid rgba(255,255,255,.05);
# }

# /* Dynamic Skill Telemetry Inspector Panel */
# .skill-detail-panel{
#   margin-top:20px;background:rgba(10,16,32,.85);border:1px solid rgba(255,255,255,.08);
#   border-radius:16px;padding:20px 24px;transition:all .3s ease;
# }
# .skill-detail-panel.active-glow{
#   border-color:rgba(56,189,248,.6);box-shadow:0 0 30px rgba(56,189,248,.15);
# }
# .skill-header-row{display:flex;justify-content:space-between;align-items:center;margin-bottom:8px}
# .skill-name-txt{font-size:1.1rem;font-weight:700;color:#38bdf8;font-family:'JetBrains Mono',monospace}
# .skill-level-txt{font-family:'JetBrains Mono',monospace;font-size:.82rem;color:#4ade80}
# .skill-desc-txt{color:#94a3b8;font-size:.9rem;line-height:1.6}
# .skill-meter-track{margin-top:12px;height:5px;background:rgba(255,255,255,.07);border-radius:3px;overflow:hidden}
# .skill-meter-fill{height:100%;width:80%;background:linear-gradient(90deg,#38bdf8,#818cf8);transition:width .6s cubic-bezier(.16,1,.3,1)}

# /* TIMELINE */
# .tl{position:relative;padding-left:36px}
# .tl::before{content:'';position:absolute;left:9px;top:6px;bottom:6px;width:2px;background:linear-gradient(180deg,#38bdf8,#818cf8,transparent)}
# .tl-item{position:relative;margin-bottom:34px}
# .tl-item::before{content:'';position:absolute;left:-32px;top:6px;width:14px;height:14px;border-radius:50%;background:#030712;border:2px solid #38bdf8;box-shadow:0 0 12px rgba(56,189,248,.8)}
# .tl-item .when{font-family:'JetBrains Mono',monospace;font-size:.76rem;color:#a78bfa;margin-bottom:6px}

# /* ACHIEVEMENTS */
# .ach{display:flex;align-items:center;gap:18px;background:rgba(15,23,42,.65);border:1px solid rgba(255,255,255,.08);border-radius:18px;padding:22px 26px;margin-bottom:16px;transition:.3s}
# .ach:hover{transform:translateX(8px);border-color:rgba(56,189,248,.45)}
# .ach .ico{font-size:1.8rem}

# /* CONTACT */
# #contact{text-align:center;padding-bottom:120px}
# #contact .big{font-size:clamp(2rem,4.8vw,3.4rem);letter-spacing:-.03em;margin-bottom:18px}
# #contact .big .grad{background:linear-gradient(120deg,#818cf8,#38bdf8);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
# .socials{display:flex;gap:14px;justify-content:center;flex-wrap:wrap;margin-top:34px}
# .socials a{padding:13px 26px;border-radius:12px;border:1px solid rgba(255,255,255,.14);color:#f3f4f6;text-decoration:none;font-size:.9rem;transition:.25s;background:rgba(255,255,255,.02);backdrop-filter:blur(8px)}
# .socials a:hover{border-color:#38bdf8;color:#38bdf8;transform:translateY(-3px);box-shadow:0 12px 28px -8px rgba(56,189,248,.45)}

# /* REVEAL ON SCROLL */
# .rv{opacity:0;transform:translateY(32px);transition:opacity .8s ease,transform .8s ease}
# .rv.in{opacity:1;transform:translateY(0)}

# footer{padding:26px 5vw;border-top:1px solid rgba(255,255,255,.06);display:flex;justify-content:space-between;align-items:center;font-size:.78rem;color:#64748b;font-family:'JetBrains Mono',monospace}
# </style>
# </head>

# <body>
# <div id="loader">
#   <div class="loader-logo">AVIRAL&nbsp;BAGJANI&nbsp;//&nbsp;QUANTUM&nbsp;CORE</div>
#   <div class="loader-bar"><i></i></div>
# </div>

# <div id="cursor"></div>
# <div id="cursor-dot"></div>

# <!-- BACKGROUND 3D CANVAS FOR ENVIRONMENT & CHOREOGRAPHED SCENE -->
# <div id="canvas3d"></div>

# <div id="frame">
#   <!-- NAVIGATION -->
#   <nav>
#     <div class="brand">
#       <div class="logo">aviral<span>.</span>ai</div>
#       <div class="badge-ping"><i></i><span>SYSTEMS ACTIVE</span></div>
#     </div>
    
#     <div class="hud-telemetry">
#       <div class="hud-pill" id="nav-stage-hud">STAGE // 00: ORBITAL TERMINAL</div>
#       <button class="audio-toggle" id="audio-btn" onclick="toggleAudio()">
#         <span id="audio-ico">🔊</span> <span id="audio-lbl">AUDIO ON</span>
#       </button>
#     </div>

#     <div class="nav-links">
#       <a href="#work"><b>01.</b>Projects</a>
#       <a href="#skills"><b>02.</b>3D Arsenal</a>
#       <a href="#exp"><b>03.</b>Experience</a>
#       <a href="#contact"><b>04.</b>Contact</a>
#     </div>
#   </nav>

#   <!-- HERO -->
#   <div class="hero">
#     <div class="hero-photo-wrap">
#       <img src="data:image/png;base64,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" alt="Aviral Bagjani">
#     </div>
#     <div class="hero-tag">
#       <span style="color:#38bdf8">●</span> B.Tech (ECE), IIIT Bhagalpur · Class of 2026
#     </div>
#     <h1>Hi, I'm <span class="grad">Aviral Bagjani</span>.<br>I architect AI systems that <span class="grad">ship to production.</span></h1>
#     <div class="typer" id="typer"></div>
#     <p class="desc">
#       Specialized in <b>multi-agent graph orchestration</b> with LangGraph &amp; MCP,
#       <b>low-latency agentic RAG</b> on Qdrant + Redis, and production <b>LLM guardrails</b> with DeepEval &amp; NeMo.
#       Former AI Engineering Intern at <b>Zeepty</b>. LeetCode <b>Knight (1784)</b>.
#     </p>
#     <div class="btn-row">
#       <a class="btn btn-solid" href="https://github.com/aviral-dot" target="_blank" rel="noopener">Explore GitHub →</a>
#       <a class="btn btn-ghost" href="https://www.linkedin.com/in/aviral-bagjani-a02049259/" target="_blank" rel="noopener">Connect on LinkedIn</a>
#     </div>
#     <div class="hero-hint">
#       <div class="ring"></div>
#       <span>3D SCENE RESPONDS TO SCROLL &amp; CURSOR</span>
#     </div>
#   </div>

#   <!-- STATS -->
#   <section>
#     <div class="stats rv">
#       <div class="stat"><div class="n" data-count="1784">0</div><div class="l">LeetCode Knight · 500+ Solved</div></div>
#       <div class="stat"><div class="n" data-count="2.12" data-dec="2">0</div><div class="l">End-to-End RAG Latency (s)</div></div>
#       <div class="stat"><div class="n" data-count="70" data-suffix="%">0</div><div class="l">LLM Cost Reduction via Redis Locks</div></div>
#       <div class="stat"><div class="n" data-count="95" data-suffix="%">0</div><div class="l">Adversarial Attacks Blocked (NeMo)</div></div>
#     </div>
#   </section>

#   <!-- PROJECTS -->
#   <section id="work">
#     <div class="sec-tag rv">// 01 — FLAGSHIP PRODUCTION SYSTEMS</div>
#     <h2 class="sec-title rv">Engineered for <em>scale &amp; resilience.</em></h2>
    
#     <div class="card rv">
#       <h3>AgentFlow — Autonomous Planner-Executor Multi-Agent Platform</h3>
#       <div class="role">LangGraph · Model Context Protocol (MCP) · FastAPI · NeMo · DeepEval</div>
#       <p>Orchestrated <b>3 autonomous workflows</b> (deep research, blog synthesis, transactional email) with human-in-the-loop validation checkpoints.
#       Integrated <b>2 external tool ecosystems (Tavily + Gmail) through MCP</b>, achieving <b>20/20 end-to-end runs</b> with zero state corruption.
#       Hardened with 2-stage NeMo guardrails, JWT authentication &amp; LangSmith telemetry — slashing <b>15 minutes of research-to-draft to under 2 minutes</b>.</p>
#       <div class="tags">
#         <span class="tag hi">LangGraph</span><span class="tag hi">Model Context Protocol</span><span class="tag">FastAPI</span>
#         <span class="tag">PostgreSQL</span><span class="tag">NeMo Guardrails</span><span class="tag">Groq</span>
#         <span class="tag">LiteLLM</span><span class="tag">DeepEval</span><span class="tag">Streamlit</span>
#       </div>
#     </div>

#     <div class="card rv">
#       <h3>RAGFury — Production Agentic RAG Pipeline at 2.12s</h3>
#       <div class="role">Qdrant Cloud · Redis Single-Flight Locking · LangSmith · Groq</div>
#       <p>Engineered an agentic RAG system with <b>hybrid sparse/dense vector search &amp; citation-grounded generation</b> over a
#       <b>600-document Qdrant index</b> at <b>2.12s</b> average response latency. Implemented <b>Redis single-flight distributed locking</b> and
#       user-scoped cache layers: <b>2.8s → 0.8s</b> on repeated queries and <b>70% lower inference cost</b>.
#       Enforced <b>4-component DeepEval gates</b> with NeMo blocking <b>&gt;95% adversarial prompt injections</b>.</p>
#       <div class="tags">
#         <span class="tag hi">Qdrant Cloud</span><span class="tag hi">Redis Locking</span><span class="tag">LangChain</span>
#         <span class="tag">LangGraph</span><span class="tag">LangSmith</span><span class="tag">PostgreSQL</span>
#         <span class="tag">NeMo Guardrails</span><span class="tag">FastAPI</span>
#       </div>
#     </div>
#   </section>

#   <!-- 3D INTERACTIVE KEYBOARD & TECHNICAL ARSENAL -->
#   <section id="skills">
#     <div class="sec-tag rv">// 02 — INTERACTIVE ARSENAL</div>
#     <h2 class="sec-title rv">The 3D <em>Skill Matrix.</em></h2>
    
#     <div class="keyboard-section-wrapper rv">
#       <div class="keyboard-telemetry-header">
#         <div class="kb-title-block">
#           <h3>⌨️ INTERACTIVE 3D MECHANICAL KEYCAP ARSENAL</h3>
#           <p>Every keycap is a specialized production tool. Hover or click keys to depress switches &amp; inspect telemetry.</p>
#         </div>
#         <div class="kb-live-inspect" id="kb-active-chip">
#           <span>ACTIVE SWITCH:</span> <b id="kb-chip-label">LANGGRAPH (CYCLE DAGS)</b>
#         </div>
#       </div>

#       <!-- 3D KEYBOARD VIEWPORT -->
#       <div id="keyboard-3d-viewport">
#         <div class="kb-instructions">
#           <span>🎮 CLICK / DRAG TO ROTATE KEYBOARD · CLICK KEYCAPS TO DEPRESS</span>
#         </div>
#       </div>

#       <!-- DYNAMIC TELEMETRY PANEL -->
#       <div class="skill-detail-panel" id="skill-inspector">
#         <div class="skill-header-row">
#           <div class="skill-name-txt" id="insp-name">LangGraph &amp; Multi-Agent Workflows</div>
#           <div class="skill-level-txt" id="insp-stat">95% PRODUCTION READINESS</div>
#         </div>
#         <div class="skill-desc-txt" id="insp-desc">
#           Stateful cyclic DAG orchestration, checkpointing, multi-worker delegation, and human-in-the-loop review nodes.
#         </div>
#         <div class="skill-meter-track">
#           <div class="skill-meter-fill" id="insp-fill" style="width: 95%;"></div>
#         </div>
#       </div>
#     </div>
#   </section>

#   <!-- EXPERIENCE -->
#   <section id="exp">
#     <div class="sec-tag rv">// 03 — TIMELINE &amp; IMPACT</div>
#     <h2 class="sec-title rv">Experience &amp; <em>education.</em></h2>
#     <div class="tl">
#       <div class="tl-item rv">
#         <div class="when">APR 2025 — JUL 2025</div>
#         <div class="card">
#           <h3>AI Engineering Intern @ Zeepty</h3>
#           <p>• Applied <b>semantic creator/product matching</b> and personalized LLM outreach across <b>500+ combinations</b>, improving relevant-match retrieval by <b>25%</b>.<br>
#           • Refined prompts and retrieved context for creator outreach, lifting response relevance by <b>15%</b> across 20+ scenarios.</p>
#           <div class="tags"><span class="tag hi">Semantic Search</span><span class="tag">Prompt Engineering</span><span class="tag">LLM Outreach</span></div>
#         </div>
#       </div>
#       <div class="tl-item rv">
#         <div class="when">NOV 2022 — MAY 2026</div>
#         <div class="card">
#           <h3>B.Tech, Electronics &amp; Communication — IIIT Bhagalpur</h3>
#           <p>CGPA <b>6.95</b> (till 8th semester). Coursework: Data Structures &amp; Algorithms, Database Management Systems, Operating Systems, Machine Learning, Computer Networks.</p>
#         </div>
#       </div>
#     </div>

#     <div class="sec-tag rv" style="margin-top:50px">// ACHIEVEMENTS</div>
#     <div class="ach rv"><div class="ico">⚔️</div><div><b>LeetCode Knight</b> — Rating 1784, 500+ algorithmic problems solved.</div></div>
#     <div class="ach rv"><div class="ico">🎯</div><div><b>JEE Main 2022</b> — AIR 52,750 (95.44 percentile) among 1.2M+ candidates.</div></div>
#   </section>

#   <!-- CONTACT -->
#   <section id="contact">
#     <div class="sec-tag rv">// 04 — TRANSMISSION</div>
#     <h2 class="big rv">Let's build something<br><span class="grad">intelligent together.</span></h2>
#     <p class="desc rv" style="margin:0 auto;text-align:center;max-width:550px">
#       Actively seeking AI / GenAI / LLM Systems Engineering roles for 2026.<br>
#       My transmission line is open.
#     </p>
#     <div class="socials rv">
#       <a href="mailto:aviralbharti832002@gmail.com">✉️ aviralbharti832002@gmail.com</a>
#       <a href="https://www.linkedin.com/in/aviral-bagjani-a02049259/" target="_blank" rel="noopener">💼 LinkedIn Profile</a>
#       <a href="https://github.com/aviral-dot" target="_blank" rel="noopener">💻 GitHub — aviral-dot</a>
#     </div>
#   </section>

#   <footer>
#     <div>© 2026 AVIRAL BAGJANI · ALL SYSTEMS OPERATIONAL</div>
#     <div>THREE.JS DUAL-VIEWPORT WEBGL ENGINE</div>
#   </footer>
# </div>

# <script>
# /* ========================================================
#    SYNTHESIZED WEB AUDIO SOUND SYSTEM (NO EXTERNAL FILES)
#    ======================================================== */
# let audioEnabled = true;
# let audioCtx = null;
# function initAudio() {
#   if (!audioCtx) {
#     audioCtx = new (window.AudioContext || window.webkitAudioContext)();
#   }
# }
# function playMechanicalClick(freq = 800, dur = 0.04) {
#   if (!audioEnabled) return;
#   try {
#     initAudio();
#     const osc = audioCtx.createOscillator();
#     const gain = audioCtx.createGain();
#     osc.type = 'triangle';
#     osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
#     osc.frequency.exponentialRampToValueAtTime(120, audioCtx.currentTime + dur);
#     gain.gain.setValueAtTime(0.15, audioCtx.currentTime);
#     gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + dur);
#     osc.connect(gain);
#     gain.connect(audioCtx.destination);
#     osc.start();
#     osc.stop(audioCtx.currentTime + dur);
#   } catch(e){}
# }
# function playChime(freq = 520) {
#   if (!audioEnabled) return;
#   try {
#     initAudio();
#     const osc = audioCtx.createOscillator();
#     const gain = audioCtx.createGain();
#     osc.type = 'sine';
#     osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
#     gain.gain.setValueAtTime(0.08, audioCtx.currentTime);
#     gain.gain.exponentialRampToValueAtTime(0.0001, audioCtx.currentTime + 0.35);
#     osc.connect(gain);
#     gain.connect(audioCtx.destination);
#     osc.start();
#     osc.stop(audioCtx.currentTime + 0.35);
#   } catch(e){}
# }
# function toggleAudio() {
#   audioEnabled = !audioEnabled;
#   document.getElementById('audio-ico').textContent = audioEnabled ? '🔊' : '🔇';
#   document.getElementById('audio-lbl').textContent = audioEnabled ? 'AUDIO ON' : 'MUTED';
#   if(audioEnabled) playChime(660);
# }

# /* ========================================================
#    BACKGROUND 3D SCENE: ORBITING HOLOGRAPHIC TERMINAL
#    ======================================================== */
# const bgContainer = document.getElementById('canvas3d');
# const bgScene = new THREE.Scene();
# const bgCam = new THREE.PerspectiveCamera(50, window.innerWidth / window.innerHeight, 0.1, 100);
# bgCam.position.set(0, 0, 7.5);

# const bgRen = new THREE.WebGLRenderer({ antialias: true, alpha: true });
# bgRen.setSize(window.innerWidth, window.innerHeight);
# bgRen.setPixelRatio(Math.min(window.devicePixelRatio, 2));
# bgContainer.appendChild(bgRen.domElement);

# // Lighting
# const ambLight = new THREE.AmbientLight(0xffffff, 0.85);
# bgScene.add(ambLight);
# const cyanSpot = new THREE.PointLight(0x38bdf8, 3.8, 35);
# cyanSpot.position.set(5, 6, 6);
# bgScene.add(cyanSpot);
# const purpleSpot = new THREE.PointLight(0xa78bfa, 3.2, 35);
# purpleSpot.position.set(-6, -4, 4);
# bgScene.add(purpleSpot);

# // 1. Particle Cloud Matrix
# const STAR_COUNT = 1500;
# const starGeo = new THREE.BufferGeometry();
# const starPos = new Float32Array(STAR_COUNT * 3);
# const starColors = new Float32Array(STAR_COUNT * 3);
# const col1 = new THREE.Color('#38bdf8'), col2 = new THREE.Color('#818cf8'), col3 = new THREE.Color('#c084fc');

# for (let i = 0; i < STAR_COUNT; i++) {
#   starPos[i*3] = (Math.random() - 0.5) * 36;
#   starPos[i*3+1] = (Math.random() - 0.5) * 32;
#   starPos[i*3+2] = (Math.random() - 0.5) * 25 - 2;
#   const c = [col1, col2, col3][i % 3];
#   starColors[i*3] = c.r; starColors[i*3+1] = c.g; starColors[i*3+2] = c.b;
# }
# starGeo.setAttribute('position', new THREE.BufferAttribute(starPos, 3));
# starGeo.setAttribute('color', new THREE.BufferAttribute(starColors, 3));
# const starsMat = new THREE.PointsMaterial({ size: 0.045, vertexColors: true, transparent: true, opacity: 0.8 });
# const starField = new THREE.Points(starGeo, starsMat);
# bgScene.add(starField);

# // 2. STAGE 0: HERO QUANTUM HOLOGRAM CORE
# const heroGroup = new THREE.Group();
# heroGroup.position.set(3.2, 0.2, 0);

# const polyGeo = new THREE.IcosahedronGeometry(1.65, 2);
# const polyMat = new THREE.MeshStandardMaterial({
#   color: 0x38bdf8, wireframe: true, transparent: true, opacity: 0.45, roughness: 0.1, metalness: 0.8
# });
# const heroPoly = new THREE.Mesh(polyGeo, polyMat);
# heroGroup.add(heroPoly);

# const ringG1 = new THREE.TorusGeometry(2.2, 0.03, 16, 100);
# const ringM1 = new THREE.MeshBasicMaterial({ color: 0x818cf8 });
# const ring1 = new THREE.Mesh(ringG1, ringM1);
# ring1.rotation.x = Math.PI / 3;
# heroGroup.add(ring1);

# const ringG2 = new THREE.TorusGeometry(2.45, 0.02, 16, 100);
# const ringM2 = new THREE.MeshBasicMaterial({ color: 0x38bdf8 });
# const ring2 = new THREE.Mesh(ringG2, ringM2);
# ring2.rotation.y = Math.PI / 4;
# heroGroup.add(ring2);

# const coreOcta = new THREE.Mesh(
#   new THREE.OctahedronGeometry(0.85, 0),
#   new THREE.MeshStandardMaterial({ color: 0x0284c7, roughness: 0.2, emissive: 0x0369a1, emissiveIntensity: 0.9 })
# );
# heroGroup.add(coreOcta);
# bgScene.add(heroGroup);

# // 3. STAGE 1: MULTI-AGENT SYNAPSE GRAPH
# const projectCluster = new THREE.Group();
# projectCluster.position.set(-3.2, -4.8, -1);
# const clusterNodes = [];
# for (let i = 0; i < 8; i++) {
#   const sMesh = new THREE.Mesh(
#     new THREE.SphereGeometry(0.18, 16, 16),
#     new THREE.MeshStandardMaterial({ color: i % 2 === 0 ? 0x38bdf8 : 0x818cf8, emissive: 0x0284c7 })
#   );
#   const ang = (i / 8) * Math.PI * 2;
#   sMesh.position.set(Math.cos(ang) * 1.6, Math.sin(ang) * 1.6, (Math.random() - 0.5) * 1.2);
#   clusterNodes.push(sMesh);
#   projectCluster.add(sMesh);
# }
# const lineMat = new THREE.LineBasicMaterial({ color: 0x38bdf8, transparent: true, opacity: 0.35 });
# for (let i = 0; i < clusterNodes.length; i++) {
#   const p1 = clusterNodes[i].position;
#   const p2 = clusterNodes[(i + 3) % clusterNodes.length].position;
#   const lineGeo = new THREE.BufferGeometry().setFromPoints([p1, p2]);
#   projectCluster.add(new THREE.Line(lineGeo, lineMat));
# }
# bgScene.add(projectCluster);

# // 4. STAGE 2: KNOT REACTOR
# const knotGroup = new THREE.Group();
# knotGroup.position.set(3.4, -9.8, -1);
# const knot = new THREE.Mesh(
#   new THREE.TorusKnotGeometry(1.4, 0.3, 120, 16),
#   new THREE.MeshStandardMaterial({ color: 0x6366f1, wireframe: true, transparent: true, opacity: 0.4 })
# );
# knotGroup.add(knot);
# bgScene.add(knotGroup);

# // 5. STAGE 3: EXPERIENCE HELIX
# const helixGroup = new THREE.Group();
# helixGroup.position.set(-3.2, -15.0, -1);
# for (let i = 0; i < 20; i++) {
#   const bMesh = new THREE.Mesh(
#     new THREE.BoxGeometry(0.18, 0.18, 0.18),
#     new THREE.MeshBasicMaterial({ color: i % 2 === 0 ? 0x38bdf8 : 0xa78bfa, wireframe: true })
#   );
#   const t = i * 0.42;
#   bMesh.position.set(Math.cos(t) * 1.3, i * 0.26 - 2.6, Math.sin(t) * 1.3);
#   helixGroup.add(bMesh);
# }
# bgScene.add(helixGroup);

# // 6. STAGE 4: CONTACT BEACON
# const beaconGroup = new THREE.Group();
# beaconGroup.position.set(0, -20.5, 0);
# const beacon = new THREE.Mesh(
#   new THREE.DodecahedronGeometry(1.8, 1),
#   new THREE.MeshStandardMaterial({ color: 0x38bdf8, wireframe: true, transparent: true, opacity: 0.5 })
# );
# beaconGroup.add(beacon);
# bgScene.add(beaconGroup);

# /* ========================================================
#    THE 3D INTERACTIVE MECHANICAL KEYBOARD (LOCAL VIEWPORT)
#    ======================================================== */
# const kbViewport = document.getElementById('keyboard-3d-viewport');
# const kbScene = new THREE.Scene();
# const kbCam = new THREE.PerspectiveCamera(45, kbViewport.clientWidth / kbViewport.clientHeight, 0.1, 100);
# kbCam.position.set(0, 4.2, 5.2);
# kbCam.lookAt(0, -0.2, 0);

# const kbRen = new THREE.WebGLRenderer({ antialias: true, alpha: true });
# kbRen.setSize(kbViewport.clientWidth, kbViewport.clientHeight);
# kbRen.setPixelRatio(Math.min(window.devicePixelRatio, 2));
# kbViewport.appendChild(kbRen.domElement);

# // Keyboard Lighting
# const kbAmb = new THREE.AmbientLight(0xffffff, 0.75);
# kbScene.add(kbAmb);
# const kbKeyLight = new THREE.PointLight(0x38bdf8, 3.5, 25);
# kbKeyLight.position.set(0, 5, 3);
# kbScene.add(kbKeyLight);
# const kbUnderLight = new THREE.PointLight(0x818cf8, 2.5, 20);
# kbUnderLight.position.set(0, -1, 0);
# kbScene.add(kbUnderLight);

# // Keyboard Chassis Baseplate
# const kbChassis = new THREE.Group();
# const plateGeo = new THREE.BoxGeometry(6.6, 0.35, 3.2);
# const plateMat = new THREE.MeshStandardMaterial({
#   color: 0x090d16, roughness: 0.4, metalness: 0.85
# });
# const chassisMesh = new THREE.Mesh(plateGeo, plateMat);
# chassisMesh.position.y = -0.2;
# kbChassis.add(chassisMesh);

# // Glowing Neon Bevel Rim around keyboard
# const rimGeo = new THREE.BoxGeometry(6.75, 0.05, 3.35);
# const rimMat = new THREE.MeshBasicMaterial({ color: 0x38bdf8, wireframe: true });
# const rimMesh = new THREE.Mesh(rimGeo, rimMat);
# rimMesh.position.y = -0.05;
# kbChassis.add(rimMesh);

# // Keycap definitions (Your Production Skills)
# const SKILLS_KEY_DATA = [
#   // ROW 1
#   { label: "LANGGRAPH", row: 0, col: 0, level: "95%", desc: "Stateful cyclic multi-agent DAGs, human-in-the-loop gates, and checkpoint persistence." },
#   { label: "MCP", row: 0, col: 1, level: "94%", desc: "Model Context Protocol bridges for dynamic tool orchestration (Tavily, Gmail, Filesystems)." },
#   { label: "QDRANT", row: 0, col: 2, level: "92%", desc: "Hybrid sparse/dense vector indexing, payload filters, and sub-second semantic retrieval." },
#   { label: "REDIS LOCK", row: 0, col: 3, level: "90%", desc: "Single-flight distributed locking & cache shields reducing redundant LLM calls by 70%." },
#   // ROW 2
#   { label: "DEEPEVAL", row: 1, col: 0, level: "92%", desc: "Automated test suites evaluating G-Eval, Hallucination, Task Completion & Answer Relevance." },
#   { label: "NEMO", row: 1, col: 1, level: "95%", desc: "Self-correcting guardrails blocking >95% jailbreaks, prompt injections, and sensitive data leakage." },
#   { label: "FASTAPI", row: 1, col: 2, level: "93%", desc: "High-throughput asynchronous APIs, streaming SSE completions, and Pydantic validation." },
#   { label: "LANGSMITH", row: 1, col: 3, level: "88%", desc: "End-to-end trace observability, token cost attribution, and latency debugging." },
#   // ROW 3
#   { label: "POSTGRES", row: 2, col: 0, level: "86%", desc: "Relational persistence, user sessions, conversation history, and transaction safety." },
#   { label: "DOCKER", row: 2, col: 1, level: "85%", desc: "Containerized reproducible agent runtimes, microservices networking, and cloud deploys." },
#   { label: "LEETCODE", row: 2, col: 2, level: "1784", desc: "Knight badge, 500+ solved across graph theory, dynamic programming, and binary search." },
#   { label: "PYTORCH", row: 2, col: 3, level: "84%", desc: "Model fine-tuning, embeddings generation, vector transformations, and tensor operations." }
# ];

# // Helper to create texture for key legends
# function makeKeyTexture(text) {
#   const cv = document.createElement('canvas');
#   cv.width = 256; cv.height = 256;
#   const ctx = cv.getContext('2d');
#   ctx.fillStyle = '#0f172a';
#   ctx.fillRect(0, 0, 256, 256);
#   // Border
#   ctx.strokeStyle = '#38bdf8';
#   ctx.lineWidth = 10;
#   ctx.strokeRect(6, 6, 244, 244);
#   // Text
#   ctx.fillStyle = '#f8fafc';
#   ctx.font = 'bold 30px "JetBrains Mono", monospace';
#   ctx.textAlign = 'center';
#   ctx.textBaseline = 'middle';
#   ctx.fillText(text, 128, 128);
#   return new THREE.CanvasTexture(cv);
# }

# const keycapMeshes = [];
# const startX = -2.25;
# const startZ = -1.0;
# const stepX = 1.5;
# const stepZ = 1.0;

# SKILLS_KEY_DATA.forEach((key, idx) => {
#   const keyGroup = new THREE.Group();
#   const capGeo = new THREE.BoxGeometry(1.22, 0.45, 0.78);
#   const keyTex = makeKeyTexture(key.label);
  
#   const capMat = [
#     new THREE.MeshStandardMaterial({ color: 0x1e293b, metalness: 0.6, roughness: 0.3 }),
#     new THREE.MeshStandardMaterial({ color: 0x1e293b, metalness: 0.6, roughness: 0.3 }),
#     new THREE.MeshStandardMaterial({ map: keyTex, metalness: 0.3, roughness: 0.4 }), // Top with legend
#     new THREE.MeshStandardMaterial({ color: 0x0f172a }),
#     new THREE.MeshStandardMaterial({ color: 0x1e293b }),
#     new THREE.MeshStandardMaterial({ color: 0x1e293b }),
#   ];
#   const capMesh = new THREE.Mesh(capGeo, capMat);
#   capMesh.position.y = 0.22;
#   keyGroup.add(capMesh);

#   // Underglow light prism
#   const glowGeo = new THREE.BoxGeometry(1.28, 0.05, 0.84);
#   const glowMat = new THREE.MeshBasicMaterial({ color: 0x38bdf8, transparent: true, opacity: 0.35 });
#   const glowMesh = new THREE.Mesh(glowGeo, glowMat);
#   glowMesh.position.y = 0.02;
#   keyGroup.add(glowMesh);

#   const posX = startX + key.col * stepX;
#   const posZ = startZ + key.row * stepZ;
#   keyGroup.position.set(posX, 0, posZ);

#   keyGroup.userData = {
#     originalY: 0,
#     depressedY: -0.16,
#     data: key,
#     glowMesh: glowMesh,
#     capMesh: capMesh
#   };

#   kbChassis.add(keyGroup);
#   keycapMeshes.push(keyGroup);
# });

# // Tilt the entire keyboard slightly towards user
# kbChassis.rotation.x = 0.22;
# kbScene.add(kbChassis);

# /* ========================================================
#    KEYBOARD RAYCASTING & INTERACTION
#    ======================================================== */
# const raycaster = new THREE.Raycaster();
# const kbMouse = new THREE.Vector2(-999, -999);
# let hoveredKey = null;

# const chipLabel = document.getElementById('kb-chip-label');
# const inspName = document.getElementById('insp-name');
# const inspStat = document.getElementById('insp-stat');
# const inspDesc = document.getElementById('insp-desc');
# const inspFill = document.getElementById('insp-fill');
# const inspectorPanel = document.getElementById('skill-inspector');

# function triggerKeyAction(keyGroup) {
#   if (!keyGroup) return;
#   const k = keyGroup.userData.data;
  
#   // Audio click sound
#   playMechanicalClick(950, 0.05);

#   // Update Telemetry Panel
#   chipLabel.textContent = `${k.label} (ACTIVE)`;
#   inspName.textContent = k.label;
#   inspStat.textContent = `${k.level} PROFICIENCY`;
#   inspDesc.textContent = k.desc;
#   const numericVal = parseInt(k.level) || 95;
#   inspFill.style.width = numericVal + '%';

#   inspectorPanel.classList.add('active-glow');
#   setTimeout(() => inspectorPanel.classList.remove('active-glow'), 400);

#   // Animate Keycap Switch Press Down & Bounce Up
#   gsap.killTweensOf(keyGroup.position);
#   gsap.to(keyGroup.position, {
#     y: keyGroup.userData.depressedY,
#     duration: 0.06,
#     yoyo: true,
#     repeat: 1,
#     ease: "power2.inOut",
#     onComplete: () => {
#       keyGroup.position.y = 0;
#     }
#   });

#   // Flash Underglow
#   keyGroup.userData.glowMesh.material.color.setHex(0x4ade80);
#   setTimeout(() => keyGroup.userData.glowMesh.material.color.setHex(0x38bdf8), 350);
# }

# kbViewport.addEventListener('mousemove', (e) => {
#   const rect = kbViewport.getBoundingClientRect();
#   kbMouse.x = ((e.clientX - rect.left) / rect.width) * 2 - 1;
#   kbMouse.y = -((e.clientY - rect.top) / rect.height) * 2 + 1;
# });

# kbViewport.addEventListener('mouseleave', () => {
#   kbMouse.x = -999; kbMouse.y = -999;
#   if (hoveredKey) {
#     hoveredKey.userData.glowMesh.material.opacity = 0.35;
#     hoveredKey = null;
#   }
# });

# kbViewport.addEventListener('click', () => {
#   if (hoveredKey) {
#     triggerKeyAction(hoveredKey);
#   }
# });

# /* ========================================================
#    FRAME SCROLL & CAMERA CHOREOGRAPHY
#    ======================================================== */
# const frame = document.getElementById('frame');
# const stageHud = document.getElementById('nav-stage-hud');
# let scrollY = 0;
# let maxScroll = 1;

# frame.addEventListener('scroll', () => {
#   scrollY = frame.scrollTop;
#   maxScroll = frame.scrollHeight - frame.clientHeight;
#   const progress = scrollY / (maxScroll || 1);

#   if (progress < 0.22) stageHud.textContent = "STAGE // 00: ORBITAL TERMINAL";
#   else if (progress < 0.48) stageHud.textContent = "STAGE // 01: MULTI-AGENT SYNAPSE";
#   else if (progress < 0.72) stageHud.textContent = "STAGE // 02: 3D ARSENAL MATRIX";
#   else if (progress < 0.88) stageHud.textContent = "STAGE // 03: CAREER HELIX";
#   else stageHud.textContent = "STAGE // 04: QUANTUM BEACON";
# });

# /* ========================================================
#    MOUSE PARALLAX & TICK ANIMATION LOOP
#    ======================================================== */
# let mx = 0, my = 0, tx = 0, ty = 0;
# const cur = document.getElementById('cursor');
# const curDot = document.getElementById('cursor-dot');

# window.addEventListener('mousemove', (e) => {
#   mx = (e.clientX / window.innerWidth - 0.5) * 2;
#   my = (e.clientY / window.innerHeight - 0.5) * 2;
#   cur.style.left = e.clientX + 'px';
#   cur.style.top = e.clientY + 'px';
#   curDot.style.left = e.clientX + 'px';
#   curDot.style.top = e.clientY + 'px';

#   document.querySelectorAll('.card, .stat, .keyboard-section-wrapper').forEach(c => {
#     const r = c.getBoundingClientRect();
#     c.style.setProperty('--mx', (e.clientX - r.left) + 'px');
#     c.style.setProperty('--my', (e.clientY - r.top) + 'px');
#   });
# });

# function animate() {
#   requestAnimationFrame(animate);

#   // Smooth mouse interpolation
#   tx += (mx - tx) * 0.05;
#   ty += (my - ty) * 0.05;

#   // Background camera choreography along scroll
#   const scrollProg = scrollY / (maxScroll || 1);
#   const targetCamY = -scrollProg * 20.5;
#   bgCam.position.y += (targetCamY - bgCam.position.y) * 0.06;
#   bgCam.position.x = tx * 0.8;
#   bgCam.lookAt(0, bgCam.position.y, 0);

#   // Background geometries subtle rotation
#   starField.rotation.y += 0.0006;
#   starField.rotation.x = ty * 0.04;
#   heroPoly.rotation.x += 0.003;
#   heroPoly.rotation.y += 0.005;
#   ring1.rotation.z += 0.012;
#   ring2.rotation.z -= 0.009;
#   coreOcta.rotation.x -= 0.006;
#   projectCluster.rotation.y += 0.007;
#   knot.rotation.x += 0.005;
#   knot.rotation.y += 0.008;
#   helixGroup.rotation.y += 0.01;
#   beacon.rotation.y += 0.006;

#   bgRen.render(bgScene, bgCam);

#   // 3D Keyboard Scene Update
#   raycaster.setFromCamera(kbMouse, kbCam);
#   const flatMeshes = [];
#   keycapMeshes.forEach(grp => grp.traverse(child => {
#     if (child.isMesh) {
#       child.parentGroup = grp;
#       flatMeshes.push(child);
#     }
#   }));

#   const intersects = raycaster.intersectObjects(flatMeshes);
#   if (intersects.length > 0) {
#     const hitGroup = intersects[0].object.parentGroup;
#     if (hitGroup && hitGroup !== hoveredKey) {
#       if (hoveredKey) hoveredKey.userData.glowMesh.material.opacity = 0.35;
#       hoveredKey = hitGroup;
#       hoveredKey.userData.glowMesh.material.opacity = 0.9;
#       playMechanicalClick(1100, 0.02);
#     }
#   } else if (hoveredKey) {
#     hoveredKey.userData.glowMesh.material.opacity = 0.35;
#     hoveredKey = null;
#   }

#   // Gentle idle oscillation of keyboard
#   kbChassis.rotation.y = tx * 0.15;
#   kbChassis.rotation.x = 0.22 - ty * 0.1;
#   kbRen.render(kbScene, kbCam);
# }
# animate();

# // Resize handling
# window.addEventListener('resize', () => {
#   bgCam.aspect = window.innerWidth / window.innerHeight;
#   bgCam.updateProjectionMatrix();
#   bgRen.setSize(window.innerWidth, window.innerHeight);

#   kbCam.aspect = kbViewport.clientWidth / kbViewport.clientHeight;
#   kbCam.updateProjectionMatrix();
#   kbRen.setSize(kbViewport.clientWidth, kbViewport.clientHeight);
# });

# /* ========================================================
#    CURSOR, PRELOADER, TYPING & NUMERICAL COUNTERS
#    ======================================================== */
# document.querySelectorAll('a, button, .card, .stat, #keyboard-3d-viewport').forEach(el => {
#   el.addEventListener('mouseenter', () => cur.classList.add('hot'));
#   el.addEventListener('mouseleave', () => cur.classList.remove('hot'));
# });

# window.addEventListener('load', () => {
#   setTimeout(() => {
#     document.getElementById('loader').classList.add('hide');
#     playChime(440);
#   }, 1200);
# });

# // Roles typing loop
# const roles = [
#   'Multi-Agent Systems Engineer (LangGraph & MCP).',
#   'Agentic RAG Architect (Qdrant & Redis Locks).',
#   'LLM Evals & Guardrails Builder (DeepEval & NeMo).',
#   'LeetCode Knight · 1784 (500+ Solved).'
# ];
# let rIdx = 0, cIdx = 0, deleting = false;
# const typerEl = document.getElementById('typer');
# function typeRole() {
#   const curStr = roles[rIdx];
#   typerEl.textContent = deleting ? curStr.slice(0, --cIdx) : curStr.slice(0, ++cIdx);
#   let sp = deleting ? 30 : 60;
#   if (!deleting && cIdx === curStr.length) { sp = 1900; deleting = true; }
#   else if (deleting && cIdx === 0) { deleting = false; rIdx = (rIdx + 1) % roles.length; sp = 350; }
#   setTimeout(typeRole, sp);
# }
# typeRole();

# // Intersection Observer for scroll animations
# const observer = new IntersectionObserver((entries) => {
#   entries.forEach(e => {
#     if (!e.isIntersecting) return;
#     e.target.classList.add('in');
#     e.target.querySelectorAll('.n[data-count]').forEach(num => {
#       if (num.dataset.done) return;
#       num.dataset.done = '1';
#       const target = parseFloat(num.dataset.count);
#       const dec = +(num.dataset.dec || 0);
#       const suf = num.dataset.suffix || '';
#       const startT = performance.now();
#       const dur = 1400;
#       function step(now) {
#         const p = Math.min((now - startT) / dur, 1);
#         const ease = 1 - Math.pow(1 - p, 3);
#         num.textContent = (target * ease).toFixed(dec) + suf;
#         if (p < 1) requestAnimationFrame(step);
#       }
#       requestAnimationFrame(step);
#     });
#     observer.unobserve(e.target);
#   });
# }, { threshold: 0.16 });
# document.querySelectorAll('.rv').forEach(el => observer.observe(el));
# </script>
# </body>
# </html>
# """

# components.html(PORTFOLIO, height=3300, scrolling=False)










