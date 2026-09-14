import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Aviral Bagjani | AI & GenAI Systems Engineer",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Strip default Streamlit margins and containers
st.markdown("""
<style>
    header[data-testid="stHeader"], footer, #MainMenu { display: none !important; }
    .block-container { padding: 0 !important; margin: 0 !important; max-width: 100vw !important; }
    iframe { border: none !important; width: 100vw !important; }
</style>
""", unsafe_allow_html=True)

PORTFOLIO_CODE = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Aviral Bagjani — AI Systems Engineer</title>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
    background-color: #03060d;
    color: #e2e8f0;
    font-family: 'Plus Jakarta Sans', sans-serif;
    overflow-x: hidden;
}

/* 3D WebGL Canvas Layer */
#webgl-canvas {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: 0;
    pointer-events: none;
}

/* Foreground Content */
.content-wrapper {
    position: relative;
    z-index: 2;
    max-width: 1180px;
    margin: 0 auto;
    padding: 0 28px;
}

/* Custom Interactive Cursor */
#custom-cursor {
    position: fixed;
    width: 32px;
    height: 32px;
    border: 1.5px solid #38bdf8;
    border-radius: 50%;
    pointer-events: none;
    z-index: 999;
    transform: translate(-50%, -50%);
    transition: width 0.2s, height 0.2s, background 0.2s;
    mix-blend-mode: screen;
}
#custom-cursor.active {
    width: 54px;
    height: 54px;
    background: rgba(56, 189, 248, 0.2);
    border-color: #818cf8;
}

/* Navigation Bar */
nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 26px 0;
    border-bottom: 1px solid rgba(255, 255, 255, 0.06);
    backdrop-filter: blur(12px);
    position: sticky;
    top: 0;
    z-index: 100;
}
.brand-logo {
    font-family: 'JetBrains Mono', monospace;
    font-size: 1.1rem;
    font-weight: 700;
    color: #ffffff;
    letter-spacing: -0.02em;
}
.brand-logo span { color: #38bdf8; }
.nav-links a {
    color: #94a3b8;
    text-decoration: none;
    margin-left: 28px;
    font-size: 0.9rem;
    font-weight: 500;
    transition: color 0.2s;
}
.nav-links a:hover { color: #38bdf8; }
.nav-links a b { color: #6366f1; font-family: 'JetBrains Mono', monospace; margin-right: 4px; }

/* Hero Section */
.hero-section {
    min-height: 92vh;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 40px;
    padding: 40px 0;
}
.hero-left {
    flex: 1.1;
    max-width: 640px;
}
.hero-right {
    flex: 0.9;
    height: 500px;
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
}

.status-pill {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    background: rgba(56, 189, 248, 0.08);
    border: 1px solid rgba(56, 189, 248, 0.28);
    color: #7dd3fc;
    padding: 7px 16px;
    border-radius: 9999px;
    font-size: 0.8rem;
    font-family: 'JetBrains Mono', monospace;
    margin-bottom: 24px;
}
.status-pill .pulse-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #10b981;
    box-shadow: 0 0 10px #10b981;
    animation: pulse 1.8s infinite;
}
@keyframes pulse { 0%, 100% { opacity: 0.3; } 50% { opacity: 1; } }

h1 {
    font-size: clamp(2.8rem, 6vw, 4.4rem);
    font-weight: 800;
    line-height: 1.06;
    letter-spacing: -0.04em;
    margin-bottom: 16px;
}
.gradient-text {
    background: linear-gradient(135deg, #ffffff 20%, #94a3b8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.gradient-highlight {
    background: linear-gradient(135deg, #38bdf8 0%, #818cf8 50%, #c084fc 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.typewriter-text {
    font-family: 'JetBrains Mono', monospace;
    font-size: clamp(1.05rem, 2.2vw, 1.35rem);
    color: #38bdf8;
    margin-bottom: 22px;
    min-height: 1.6em;
}
.typewriter-text::after {
    content: '|';
    animation: blink 0.9s infinite;
}
@keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }

.hero-description {
    font-size: 1.05rem;
    line-height: 1.7;
    color: #94a3b8;
    margin-bottom: 34px;
}
.hero-description b { color: #f1f5f9; }

.cta-group {
    display: flex;
    gap: 16px;
    flex-wrap: wrap;
}
.btn-primary {
    background: linear-gradient(135deg, #0284c7 0%, #6366f1 100%);
    color: #ffffff;
    padding: 13px 28px;
    border-radius: 12px;
    font-weight: 600;
    font-size: 0.92rem;
    text-decoration: none;
    box-shadow: 0 10px 25px -8px rgba(2, 132, 199, 0.6);
    transition: all 0.25s ease;
}
.btn-primary:hover {
    transform: translateY(-3px);
    box-shadow: 0 15px 35px -8px rgba(2, 132, 199, 0.8);
}
.btn-secondary {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.15);
    color: #ffffff;
    padding: 13px 28px;
    border-radius: 12px;
    font-weight: 600;
    font-size: 0.92rem;
    text-decoration: none;
    transition: all 0.25s ease;
}
.btn-secondary:hover {
    border-color: #38bdf8;
    color: #38bdf8;
    transform: translateY(-3px);
}

/* 3D Interaction Card Overlay in Hero */
.canvas-hint-pill {
    position: absolute;
    bottom: 20px;
    background: rgba(10, 16, 32, 0.7);
    border: 1px solid rgba(56, 189, 248, 0.25);
    padding: 8px 16px;
    border-radius: 20px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.75rem;
    color: #94a3b8;
    backdrop-filter: blur(8px);
    pointer-events: none;
    animation: floatHint 2.4s ease-in-out infinite;
}
@keyframes floatHint {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-5px); }
}

/* Metrics Bar */
.metrics-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
    gap: 18px;
    margin: 40px 0 90px;
}
.metric-tile {
    background: rgba(13, 20, 36, 0.6);
    border: 1px solid rgba(255, 255, 255, 0.07);
    border-radius: 16px;
    padding: 24px;
    backdrop-filter: blur(10px);
    transition: transform 0.25s, border-color 0.25s;
}
.metric-tile:hover {
    transform: translateY(-4px);
    border-color: rgba(56, 189, 248, 0.4);
}
.metric-number {
    font-family: 'JetBrains Mono', monospace;
    font-size: 2.2rem;
    font-weight: 800;
    background: linear-gradient(135deg, #38bdf8, #818cf8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.metric-label {
    font-size: 0.85rem;
    color: #94a3b8;
    margin-top: 6px;
}

/* Section Common Styling */
.section-wrapper {
    padding: 70px 0;
}
.section-eyebrow {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.8rem;
    color: #38bdf8;
    letter-spacing: 0.15em;
    margin-bottom: 10px;
}
.section-heading {
    font-size: clamp(2rem, 4vw, 2.7rem);
    font-weight: 700;
    letter-spacing: -0.03em;
    margin-bottom: 38px;
}

/* Project Cards with Spotlight Hover */
.project-card {
    position: relative;
    background: rgba(13, 20, 36, 0.65);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 20px;
    padding: 38px;
    margin-bottom: 30px;
    backdrop-filter: blur(14px);
    overflow: hidden;
    transition: transform 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease;
}
.project-card:hover {
    transform: translateY(-5px);
    border-color: rgba(56, 189, 248, 0.45);
    box-shadow: 0 20px 45px -15px rgba(56, 189, 248, 0.25);
}
.project-card::before {
    content: '';
    position: absolute;
    top: var(--mouse-y, -1000px);
    left: var(--mouse-x, -1000px);
    width: 400px;
    height: 400px;
    background: radial-gradient(circle, rgba(56, 189, 248, 0.12), transparent 70%);
    transform: translate(-50%, -50%);
    pointer-events: none;
    border-radius: 50%;
}

.project-title {
    font-size: 1.55rem;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 6px;
}
.project-role {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.88rem;
    color: #818cf8;
    margin-bottom: 16px;
}
.project-summary {
    color: #94a3b8;
    line-height: 1.7;
    font-size: 1rem;
    margin-bottom: 22px;
}
.project-summary b { color: #f1f5f9; }

.badges-container {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-top: 14px;
}
.tech-badge {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.75rem;
    padding: 5px 12px;
    border-radius: 8px;
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(255, 255, 255, 0.09);
    color: #cbd5e1;
}
.tech-badge.highlight {
    background: rgba(56, 189, 248, 0.08);
    border-color: rgba(56, 189, 248, 0.3);
    color: #38bdf8;
}

/* Two Column Grid */
.two-col-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 26px;
}
@media (max-width: 820px) {
    .two-col-grid { grid-template-columns: 1fr; }
    .hero-section { flex-direction: column; }
    .hero-right { width: 100%; height: 360px; }
}

/* Skills Progress */
.skill-item {
    margin-bottom: 22px;
}
.skill-header {
    display: flex;
    justify-content: space-between;
    font-size: 0.9rem;
    margin-bottom: 8px;
}
.skill-bar-track {
    height: 7px;
    background: rgba(255, 255, 255, 0.06);
    border-radius: 6px;
    overflow: hidden;
}
.skill-bar-fill {
    height: 100%;
    width: 0;
    border-radius: 6px;
    background: linear-gradient(90deg, #38bdf8, #818cf8);
    transition: width 1.5s cubic-bezier(0.16, 1, 0.3, 1);
}

/* Timeline */
.timeline {
    position: relative;
    padding-left: 36px;
}
.timeline::before {
    content: '';
    position: absolute;
    left: 10px;
    top: 6px;
    bottom: 6px;
    width: 2px;
    background: linear-gradient(180deg, #38bdf8, #818cf8, transparent);
}
.timeline-card {
    position: relative;
    margin-bottom: 34px;
}
.timeline-card::before {
    content: '';
    position: absolute;
    left: -32px;
    top: 6px;
    width: 14px;
    height: 14px;
    border-radius: 50%;
    background: #03060d;
    border: 2px solid #38bdf8;
    box-shadow: 0 0 12px #38bdf8;
}
.timeline-period {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.78rem;
    color: #818cf8;
    margin-bottom: 6px;
}

/* Contact Banner */
.contact-banner {
    text-align: center;
    background: linear-gradient(135deg, rgba(13, 20, 36, 0.75) 0%, rgba(8, 12, 22, 0.9) 100%);
    border: 1px solid rgba(56, 189, 248, 0.25);
    border-radius: 24px;
    padding: 60px 30px;
    margin: 40px 0 80px;
    backdrop-filter: blur(16px);
}
.contact-banner h2 {
    font-size: clamp(2rem, 4vw, 3rem);
    margin-bottom: 16px;
    letter-spacing: -0.03em;
}
.social-links-row {
    display: flex;
    justify-content: center;
    gap: 16px;
    flex-wrap: wrap;
    margin-top: 32px;
}

footer {
    display: flex;
    justify-content: space-between;
    padding: 30px 0;
    border-top: 1px solid rgba(255, 255, 255, 0.06);
    font-size: 0.85rem;
    color: #64748b;
    font-family: 'JetBrains Mono', monospace;
}
</style>
</head>
<body>

<div id="webgl-canvas"></div>
<div id="custom-cursor"></div>

<div class="content-wrapper">
    <nav>
        <div class="brand-logo">aviral<span>.ai //</span></div>
        <div class="nav-links">
            <a href="#projects"><b>01.</b>Projects</a>
            <a href="#skills"><b>02.</b>Stack</a>
            <a href="#experience"><b>03.</b>Experience</a>
            <a href="#contact"><b>04.</b>Contact</a>
        </div>
    </nav>

    <!-- HERO SECTION WITH CENTER-STAGE 3D ARTIFACT -->
    <section class="hero-section">
        <div class="hero-left">
            <div class="status-pill">
                <span class="pulse-dot"></span>
                <span>OPEN FOR AI / GENAI ROLES · 2026</span>
            </div>
            <h1 class="gradient-text">
                Engineering <span class="gradient-highlight">Autonomous</span> Multi-Agent &amp; RAG Systems.
            </h1>
            <div class="typewriter-text" id="typewriter"></div>
            <p class="hero-description">
                I'm <b>Aviral Bagjani</b> — final-year B.Tech at <b>IIIT Bhagalpur</b>. I build production-grade
                agentic architectures with <b>LangGraph</b>, <b>Model Context Protocol (MCP)</b>, and low-latency
                vector indexing on <b>Qdrant + Redis</b>, reinforced by <b>DeepEval</b> automated evals and <b>NeMo Guardrails</b>.
            </p>
            <div class="cta-group">
                <a href="https://github.com/aviral-dot" target="_blank" class="btn-primary">View GitHub Code &rarr;</a>
                <a href="https://www.linkedin.com/in/aviral-bagjani-a02049259/" target="_blank" class="btn-secondary">LinkedIn Profile</a>
            </div>
        </div>

        <div class="hero-right" id="hero-3d-anchor">
            <div class="canvas-hint-pill">&larr; MOVE MOUSE TO ROTATE 3D CORE &rarr;</div>
        </div>
    </section>

    <!-- METRICS STRIP -->
    <div class="metrics-grid">
        <div class="metric-tile">
            <div class="metric-number" data-target="1784">0</div>
            <div class="metric-label">LeetCode Knight (500+ Solved)</div>
        </div>
        <div class="metric-tile">
            <div class="metric-number" data-target="2.12" data-decimals="2">0</div>
            <div class="metric-label">Production RAG Latency (Seconds)</div>
        </div>
        <div class="metric-tile">
            <div class="metric-number" data-target="70" data-suffix="%">0</div>
            <div class="metric-label">LLM Cost Cut (Redis Single-Flight)</div>
        </div>
        <div class="metric-tile">
            <div class="metric-number" data-target="95.4" data-suffix="%">0</div>
            <div class="metric-label">JEE Main AIR 52,750 (Top 4.5%)</div>
        </div>
    </div>

    <!-- PROJECTS SECTION -->
    <section id="projects" class="section-wrapper">
        <div class="section-eyebrow">// 01 — FLAGSHIP PRODUCTION SYSTEMS</div>
        <h2 class="section-heading">Architected &amp; Deployed</h2>

        <!-- Project 1: AgentFlow -->
        <div class="project-card">
            <div class="project-title">AgentFlow — Planner-Executor Autonomous Platform</div>
            <div class="project-role">LangGraph · Model Context Protocol · FastAPI · NeMo Guardrails · DeepEval</div>
            <p class="project-summary">
                Orchestrated an end-to-end multi-agent planner-executor engine across <b>3 specialized pipelines</b>
                (deep research, technical blog synthesis, and personalized email outreach) with human-in-the-loop validation.<br><br>
                • Integrated external tool ecosystems (Tavily search &amp; Gmail API) via <b>Anthropic's Model Context Protocol (MCP)</b>,
                achieving <b>20/20 end-to-end test runs without state corruption</b> across multi-turn tool calls.<br>
                • Hardened with 2-stage <b>NeMo Guardrails</b> and structured <b>DeepEval</b> regression test suites,
                achieving <b>84% task completion</b>, <b>91% answer relevance</b>, and <b>87% blog quality</b>,
                cutting research-to-draft workflows from 15 minutes to <b>under 2 minutes</b>.
            </p>
            <div class="badges-container">
                <span class="tech-badge highlight">LangGraph</span>
                <span class="tech-badge highlight">Model Context Protocol</span>
                <span class="tech-badge">FastAPI</span>
                <span class="tech-badge">NeMo Guardrails</span>
                <span class="tech-badge">DeepEval</span>
                <span class="tech-badge">PostgreSQL</span>
                <span class="tech-badge">Groq</span>
                <span class="tech-badge">LiteLLM</span>
            </div>
        </div>

        <!-- Project 2: RAGFury -->
        <div class="project-card">
            <div class="project-title">RAGFury — Low-Latency Agentic Retrieval Pipeline</div>
            <div class="project-role">Qdrant Cloud · Redis Single-Flight Locks · LangSmith · Groq</div>
            <p class="project-summary">
                Engineered a production-grade agentic RAG system with hybrid dense+sparse retrieval and citation-grounded generation,
                achieving <b>2.12s end-to-end latency</b> across a 600-document Qdrant Cloud index.<br><br>
                • Accelerated repeat queries with <b>Redis distributed single-flight locking</b> and scoped caching,
                crushing latency from <b>2.8s to 0.8s</b> and cutting LLM inference costs by <b>70%</b> by eliminating concurrent duplicate executions.<br>
                • Hardened against adversarial attacks with NeMo Guardrails (blocking <b>&gt;95% malicious queries</b>),
                and integrated a 4-component DeepEval suite (78–92% evaluation gates) with <b>LangSmith</b> token cost tracing.
            </p>
            <div class="badges-container">
                <span class="tech-badge highlight">Qdrant Cloud</span>
                <span class="tech-badge highlight">Redis Single-Flight</span>
                <span class="tech-badge">LangChain / LangGraph</span>
                <span class="tech-badge">LangSmith</span>
                <span class="tech-badge">Groq</span>
                <span class="tech-badge">Adversarial Defense</span>
            </div>
        </div>
    </section>

    <!-- SKILLS SECTION -->
    <section id="skills" class="section-wrapper">
        <div class="section-eyebrow">// 02 — TECHNICAL ARSENAL</div>
        <h2 class="section-heading">Core Competencies</h2>
        <div class="two-col-grid">
            <div class="project-card">
                <h3 style="margin-bottom: 20px; color:#ffffff;">AI / Generative AI Systems</h3>
                <div class="skill-item">
                    <div class="skill-header"><span>LangGraph, LangChain, Multi-Agent MCP</span><span style="color:#38bdf8;">95%</span></div>
                    <div class="skill-bar-track"><div class="skill-bar-fill" data-width="95%"></div></div>
                </div>
                <div class="skill-item">
                    <div class="skill-header"><span>Agentic RAG &amp; Vector Databases (Qdrant, Neo4j)</span><span style="color:#38bdf8;">92%</span></div>
                    <div class="skill-bar-track"><div class="skill-bar-fill" data-width="92%"></div></div>
                </div>
                <div class="skill-item">
                    <div class="skill-header"><span>NeMo Guardrails &amp; DeepEval Evals</span><span style="color:#38bdf8;">90%</span></div>
                    <div class="skill-bar-track"><div class="skill-bar-fill" data-width="90%"></div></div>
                </div>
                <div class="skill-item">
                    <div class="skill-header"><span>LangSmith, LiteLLM &amp; Observability</span><span style="color:#38bdf8;">88%</span></div>
                    <div class="skill-bar-track"><div class="skill-bar-fill" data-width="88%"></div></div>
                </div>
            </div>

            <div class="project-card">
                <h3 style="margin-bottom: 20px; color:#ffffff;">Backend &amp; Infrastructure</h3>
                <div class="skill-item">
                    <div class="skill-header"><span>Python, C++, SQL (DSA &amp; Systems)</span><span style="color:#818cf8;">95%</span></div>
                    <div class="skill-bar-track"><div class="skill-bar-fill" data-width="95%"></div></div>
                </div>
                <div class="skill-item">
                    <div class="skill-header"><span>FastAPI, PostgreSQL &amp; Redis Locks</span><span style="color:#818cf8;">90%</span></div>
                    <div class="skill-bar-track"><div class="skill-bar-fill" data-width="90%"></div></div>
                </div>
                <div class="skill-item">
                    <div class="skill-header"><span>Docker, Kubernetes, AWS &amp; CI/CD</span><span style="color:#818cf8;">82%</span></div>
                    <div class="skill-bar-track"><div class="skill-bar-fill" data-width="82%"></div></div>
                </div>
                <div class="skill-item">
                    <div class="skill-header"><span>Git, GitHub Actions &amp; Vercel</span><span style="color:#818cf8;">86%</span></div>
                    <div class="skill-bar-track"><div class="skill-bar-fill" data-width="86%"></div></div>
                </div>
            </div>
        </div>
    </section>

    <!-- EXPERIENCE SECTION -->
    <section id="experience" class="section-wrapper">
        <div class="section-eyebrow">// 03 — EXPERIENCE &amp; ACADEMICS</div>
        <h2 class="section-heading">Background</h2>
        <div class="timeline">
            <div class="timeline-card">
                <div class="timeline-period">APR 2025 – JUL 2025</div>
                <div class="project-card" style="margin-bottom:0;">
                    <div class="project-title">Zeepty — AI Engineering Intern</div>
                    <p class="project-summary">
                        • Engineered semantic creator/product embeddings across <b>500+ combinations</b>, improving relevant match retrieval by <b>25%</b>.<br>
                        • Optimized LLM-generated creator outreach by refining prompt chains and context retrieval, increasing response relevance by <b>15%</b> across 20+ production scenarios.
                    </p>
                </div>
            </div>

            <div class="timeline-card">
                <div class="timeline-period">NOV 2022 – MAY 2026</div>
                <div class="project-card" style="margin-bottom:0;">
                    <div class="project-title">IIIT Bhagalpur — B.Tech Electronics &amp; Communication</div>
                    <p class="project-summary">
                        <b>CGPA: 6.95 / 10</b> (till 8th semester).<br>
                        Coursework: Data Structures &amp; Algorithms, Database Management Systems, Machine Learning, Operating Systems, Computer Networks.
                    </p>
                </div>
            </div>
        </div>
    </section>

    <!-- CONTACT BANNER -->
    <div class="contact-banner" id="contact">
        <div class="section-eyebrow">// 04 — READY TO CONNECT</div>
        <h2>Let's build something <span class="gradient-highlight">intelligent.</span></h2>
        <p style="color:#94a3b8; max-width:600px; margin:0 auto; line-height:1.7;">
            Looking for an engineer who knows how to move beyond basic prompts and build reliable, low-latency, and hardened AI systems?
        </p>
        <div class="social-links-row">
            <a href="mailto:aviralbharti832002@gmail.com" class="btn-primary">✉️ aviralbharti832002@gmail.com</a>
            <a href="https://www.linkedin.com/in/aviral-bagjani-a02049259/" target="_blank" class="btn-secondary">💼 LinkedIn Profile</a>
            <a href="https://github.com/aviral-dot" target="_blank" class="btn-secondary">💻 GitHub (aviral-dot)</a>
        </div>
    </div>

    <footer>
        <div>&copy; 2026 AVIRAL BAGJANI</div>
        <div>BUILT WITH STREAMLIT &amp; THREE.JS</div>
    </footer>
</div>

<script>
/* ========================================================
   HIGH-FIDELITY THREE.JS 3D QUANTUM ARTIFACT
   ======================================================== */
const canvasContainer = document.getElementById('webgl-canvas');
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(50, window.innerWidth / window.innerHeight, 0.1, 1000);
camera.position.z = 8;

const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
canvasContainer.appendChild(renderer.domElement);

// Dynamic Lighting
const ambientLight = new THREE.AmbientLight(0xffffff, 0.6);
scene.add(ambientLight);

const pointLight = new THREE.PointLight(0x38bdf8, 2.8, 50);
pointLight.position.set(5, 5, 5);
scene.add(pointLight);

const purpleLight = new THREE.PointLight(0x818cf8, 2.5, 50);
purpleLight.position.set(-5, -5, 3);
scene.add(purpleLight);

// Core 3D Group
const main3DGroup = new THREE.Group();
scene.add(main3DGroup);

// 1. Outer Geodesic Wireframe Sphere
const outerGeo = new THREE.IcosahedronGeometry(2.0, 2);
const outerMat = new THREE.MeshStandardMaterial({
    color: 0x38bdf8,
    wireframe: true,
    transparent: true,
    opacity: 0.35,
    roughness: 0.2,
    metalness: 0.8
});
const outerSphere = new THREE.Mesh(outerGeo, outerMat);
main3DGroup.add(outerSphere);

// 2. Middle Glowing Torus Rings (Orbitals)
const ringGeo1 = new THREE.TorusGeometry(2.35, 0.04, 16, 100);
const ringMat1 = new THREE.MeshBasicMaterial({ color: 0x818cf8 });
const ring1 = new THREE.Mesh(ringGeo1, ringMat1);
ring1.rotation.x = Math.PI / 3;
main3DGroup.add(ring1);

const ringGeo2 = new THREE.TorusGeometry(2.6, 0.03, 16, 100);
const ringMat2 = new THREE.MeshBasicMaterial({ color: 0x38bdf8 });
const ring2 = new THREE.Mesh(ringGeo2, ringMat2);
ring2.rotation.y = Math.PI / 4;
main3DGroup.add(ring2);

// 3. Inner Glowing Pulsating Plasma Core
const coreGeo = new THREE.OctahedronGeometry(1.0, 0);
const coreMat = new THREE.MeshStandardMaterial({
    color: 0x0284c7,
    wireframe: false,
    roughness: 0.1,
    metalness: 0.9,
    emissive: 0x0369a1,
    emissiveIntensity: 0.6
});
const innerCore = new THREE.Mesh(coreGeo, coreMat);
main3DGroup.add(innerCore);

// 4. Orbiting Satellite Crystals
const satellites = [];
for (let i = 0; i < 6; i++) {
    const sGeo = new THREE.TetrahedronGeometry(0.18, 0);
    const sMat = new THREE.MeshBasicMaterial({ color: i % 2 === 0 ? 0x38bdf8 : 0xc084fc, wireframe: true });
    const sat = new THREE.Mesh(sGeo, sMat);
    const angle = (i / 6) * Math.PI * 2;
    sat.userData = { angle: angle, distance: 3.1, speed: 0.015 + (i * 0.003) };
    satellites.push(sat);
    main3DGroup.add(sat);
}

// 5. Starfield Particles in background
const pCount = 800;
const pGeo = new THREE.BufferGeometry();
const pPos = new Float32Array(pCount * 3);
for (let i = 0; i < pCount * 3; i += 3) {
    pPos[i] = (Math.random() - 0.5) * 30;
    pPos[i+1] = (Math.random() - 0.5) * 30;
    pPos[i+2] = (Math.random() - 0.5) * 20 - 4;
}
pGeo.setAttribute('position', new THREE.BufferAttribute(pPos, 3));
const pMat = new THREE.PointsMaterial({ color: 0x818cf8, size: 0.035, transparent: true, opacity: 0.65 });
const particles = new THREE.Points(pGeo, pMat);
scene.add(particles);

// Position initially aligned with right hero side on desktop
function updateCorePosition() {
    if (window.innerWidth > 820) {
        main3DGroup.position.set(2.4, 0.4, 0);
        main3DGroup.scale.set(1.15, 1.15, 1.15);
    } else {
        main3DGroup.position.set(0, 0, -2);
        main3DGroup.scale.set(0.85, 0.85, 0.85);
    }
}
updateCorePosition();

// Mouse & Scroll Parallax
let mouseX = 0, mouseY = 0;
let targetRotX = 0, targetRotY = 0;
let scrollProgress = 0;

window.addEventListener('mousemove', (e) => {
    mouseX = (e.clientX / window.innerWidth - 0.5) * 2;
    mouseY = (e.clientY / window.innerHeight - 0.5) * 2;

    // Custom cursor move
    const cursor = document.getElementById('custom-cursor');
    cursor.style.left = e.clientX + 'px';
    cursor.style.top = e.clientY + 'px';

    // Spotlight on cards
    document.querySelectorAll('.project-card').forEach(card => {
        const rect = card.getBoundingClientRect();
        card.style.setProperty('--mouse-x', (e.clientX - rect.left) + 'px');
        card.style.setProperty('--mouse-y', (e.clientY - rect.top) + 'px');
    });
});

window.addEventListener('scroll', () => {
    const totalHeight = document.documentElement.scrollHeight - window.innerHeight;
    scrollProgress = window.scrollY / (totalHeight || 1);
});

// Render Loop
function animate() {
    requestAnimationFrame(animate);

    targetRotY += (mouseX * 0.8 - targetRotY) * 0.05;
    targetRotX += (mouseY * 0.8 - targetRotX) * 0.05;

    // Rotations
    outerSphere.rotation.x += 0.003;
    outerSphere.rotation.y += 0.005;
    innerCore.rotation.x -= 0.008;
    innerCore.rotation.y += 0.009;

    ring1.rotation.z += 0.012;
    ring2.rotation.z -= 0.009;

    // Orbiting satellites
    satellites.forEach(sat => {
        sat.userData.angle += sat.userData.speed;
        sat.position.x = Math.cos(sat.userData.angle) * sat.userData.distance;
        sat.position.y = Math.sin(sat.userData.angle) * sat.userData.distance * 0.6;
        sat.position.z = Math.sin(sat.userData.angle) * 1.2;
        sat.rotation.x += 0.03;
    });

    // Subtly rotate and shift based on scroll
    main3DGroup.rotation.y = targetRotY + (scrollProgress * Math.PI * 1.5);
    main3DGroup.rotation.x = targetRotX;
    particles.rotation.y += 0.0006;

    renderer.render(scene, camera);
}
animate();

window.addEventListener('resize', () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
    updateCorePosition();
});

/* ========================================================
   TYPEWRITER CYCLING EFFECT
   ======================================================== */
const roles = [
    "Multi-Agent Orchestration (LangGraph & MCP)",
    "Agentic RAG Architect (Qdrant & Redis)",
    "LLM Evals & Guardrails (DeepEval & NeMo)",
    "LeetCode Knight (Rating 1784, 500+ Solved)"
];
let rIdx = 0, cIdx = 0, isDeleting = false;
const typer = document.getElementById('typewriter');

function runTypewriter() {
    const current = roles[rIdx];
    typer.textContent = isDeleting ? current.substring(0, cIdx--) : current.substring(0, cIdx++);

    let speed = isDeleting ? 30 : 65;
    if (!isDeleting && cIdx === current.length) {
        speed = 1800;
        isDeleting = true;
    } else if (isDeleting && cIdx === 0) {
        isDeleting = false;
        rIdx = (rIdx + 1) % roles.length;
        speed = 350;
    }
    setTimeout(runTypewriter, speed);
}
runTypewriter();

/* ========================================================
   INTERSECTION OBSERVER: ANIMATE COUNTERS & SKILLS
   ======================================================== */
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            // Numbers
            entry.target.querySelectorAll('.metric-number').forEach(el => {
                if (el.dataset.done) return;
                el.dataset.done = 'true';
                const target = parseFloat(el.dataset.target);
                const dec = parseInt(el.dataset.decimals || '0');
                const suffix = el.dataset.suffix || '';
                const start = performance.now();
                const dur = 1500;
                function tickNum(now) {
                    const progress = Math.min((now - start) / dur, 1);
                    const val = target * (1 - Math.pow(1 - progress, 3));
                    el.textContent = val.toFixed(dec) + suffix;
                    if (progress < 1) requestAnimationFrame(tickNum);
                }
                requestAnimationFrame(tickNum);
            });

            // Skill bars
            entry.target.querySelectorAll('.skill-bar-fill').forEach(bar => {
                bar.style.width = bar.dataset.width;
            });
        }
    });
}, { threshold: 0.15 });

document.querySelectorAll('.metrics-grid, .two-col-grid').forEach(el => observer.observe(el));

// Custom cursor hover states
document.querySelectorAll('a, button, .project-card').forEach(el => {
    el.addEventListener('mouseenter', () => document.getElementById('custom-cursor').classList.add('active'));
    el.addEventListener('mouseleave', () => document.getElementById('custom-cursor').classList.remove('active'));
});
</script>
</body>
</html>
"""

components.html(PORTFOLIO_CODE, height=2750, scrolling=False)
