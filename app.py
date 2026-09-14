import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="AVIRAL // NEURAL CORE OS",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Strip default Streamlit margins and containers
st.markdown("""
<style>
    header[data-testid="stHeader"], footer, #MainMenu { display: none !important; }
    .block-container { padding: 0 !important; margin: 0 !important; max-width: 100vw !important; }
    iframe { border: none !important; width: 100vw !important; height: 100vh !important; }
</style>
""", unsafe_allow_html=True)

CYBER_DECK_HTML = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Aviral Bagjani — Autonomous Systems Deck</title>
<link href="https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@300;400;500;600;700&family=JetBrains+Mono:wght@300;400;500;700&display=swap" rel="stylesheet">
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<style>
* { margin: 0; padding: 0; box-sizing: border-box; user-select: none; }
body {
    background-color: #020408;
    color: #e2e8f0;
    font-family: 'Chakra Petch', sans-serif;
    overflow: hidden;
    height: 100vh;
    width: 100vw;
}

/* Background canvas */
#canvas-3d {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: 1;
}

/* Scanline and Vignette overlays */
.crt-overlay {
    position: fixed;
    inset: 0;
    pointer-events: none;
    z-index: 2;
    background: radial-gradient(circle at center, transparent 60%, rgba(0, 0, 0, 0.75) 100%),
                linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.25) 50%);
    background-size: 100% 100%, 100% 4px;
}

/* HUD Frame */
.hud-layer {
    position: fixed;
    inset: 0;
    z-index: 10;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 24px 32px;
    pointer-events: none;
}
.hud-layer * { pointer-events: auto; }

/* Top Telemetry Bar */
.telemetry-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: rgba(10, 15, 29, 0.75);
    border: 1px solid rgba(56, 189, 248, 0.2);
    border-radius: 12px;
    padding: 12px 24px;
    backdrop-filter: blur(14px);
    box-shadow: 0 0 30px rgba(56, 189, 248, 0.08);
}
.hud-identity {
    display: flex;
    align-items: center;
    gap: 16px;
}
.hud-pulse {
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background: #38bdf8;
    box-shadow: 0 0 12px #38bdf8;
    animation: pulse 1.6s infinite;
}
@keyframes pulse { 0%, 100% { opacity: 0.3; transform: scale(0.9); } 50% { opacity: 1; transform: scale(1.15); } }

.hud-name {
    font-size: 1.15rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    color: #ffffff;
    font-family: 'JetBrains Mono', monospace;
}
.hud-name span { color: #38bdf8; }
.telemetry-metrics {
    display: flex;
    gap: 28px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.8rem;
    color: #94a3b8;
}
.telemetry-item b { color: #38bdf8; font-weight: 600; }

.audio-toggle {
    background: rgba(56, 189, 248, 0.08);
    border: 1px solid rgba(56, 189, 248, 0.3);
    color: #38bdf8;
    padding: 6px 14px;
    border-radius: 8px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.75rem;
    cursor: pointer;
    transition: all 0.2s;
}
.audio-toggle:hover { background: rgba(56, 189, 248, 0.2); }

/* Main Stage / Center Layout */
.main-stage {
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 100%;
    padding: 20px 0;
}

/* Left Node Directory */
.node-selector {
    width: 290px;
    background: rgba(8, 12, 22, 0.75);
    border: 1px solid rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(16px);
    border-radius: 16px;
    padding: 20px;
    display: flex;
    flex-direction: column;
    gap: 10px;
}
.node-selector-title {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.75rem;
    letter-spacing: 0.15em;
    color: #64748b;
    margin-bottom: 6px;
}
.node-btn {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: rgba(255, 255, 255, 0.02);
    border: 1px solid rgba(255, 255, 255, 0.06);
    padding: 12px 14px;
    border-radius: 10px;
    color: #cbd5e1;
    cursor: pointer;
    font-family: 'Chakra Petch', sans-serif;
    font-size: 0.95rem;
    font-weight: 500;
    transition: all 0.25s ease;
}
.node-btn:hover, .node-btn.active {
    background: rgba(56, 189, 248, 0.12);
    border-color: #38bdf8;
    color: #ffffff;
    box-shadow: 0 0 20px rgba(56, 189, 248, 0.2);
    transform: translateX(4px);
}
.node-btn span.tag {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.7rem;
    padding: 2px 6px;
    border-radius: 4px;
    background: rgba(255, 255, 255, 0.06);
    color: #94a3b8;
}

/* Center Interactive Instruction Hint */
.center-nav-hint {
    position: absolute;
    bottom: 110px;
    left: 50%;
    transform: translateX(-50%);
    color: #64748b;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.75rem;
    letter-spacing: 0.2em;
    pointer-events: none;
    animation: float 2.5s ease-in-out infinite;
}
@keyframes float { 0%, 100% { transform: translate(-50%, 0); } 50% { transform: translate(-50%, -6px); } }

/* Right Holographic Info Screen */
.hologram-screen {
    width: 440px;
    max-height: 75vh;
    overflow-y: auto;
    background: linear-gradient(135deg, rgba(10, 16, 32, 0.85) 0%, rgba(5, 8, 16, 0.95) 100%);
    border: 1px solid rgba(56, 189, 248, 0.3);
    box-shadow: 0 0 40px rgba(56, 189, 248, 0.12);
    backdrop-filter: blur(20px);
    border-radius: 18px;
    padding: 28px;
    scrollbar-width: thin;
    scrollbar-color: #38bdf8 transparent;
}
.screen-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    padding-bottom: 14px;
    margin-bottom: 16px;
}
.screen-sys-id {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.75rem;
    color: #38bdf8;
    letter-spacing: 0.1em;
}
.screen-title {
    font-size: 1.6rem;
    font-weight: 700;
    color: #ffffff;
    line-height: 1.15;
    margin-bottom: 8px;
}
.screen-subtitle {
    font-size: 0.9rem;
    color: #94a3b8;
    margin-bottom: 18px;
}
.stat-pill-row {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 10px;
    margin-bottom: 18px;
}
.stat-pill {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.06);
    border-radius: 10px;
    padding: 10px 14px;
}
.stat-pill .val {
    font-family: 'JetBrains Mono', monospace;
    font-size: 1.25rem;
    font-weight: 700;
    color: #38bdf8;
}
.stat-pill .lbl {
    font-size: 0.7rem;
    color: #64748b;
    text-transform: uppercase;
}
.screen-body {
    font-size: 0.9rem;
    color: #cbd5e1;
    line-height: 1.6;
    margin-bottom: 20px;
}
.screen-body ul {
    margin-left: 18px;
    margin-top: 8px;
}
.screen-body li {
    margin-bottom: 6px;
}
.tech-chips {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    margin-bottom: 22px;
}
.chip {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.7rem;
    padding: 4px 10px;
    border-radius: 6px;
    background: rgba(56, 189, 248, 0.08);
    border: 1px solid rgba(56, 189, 248, 0.2);
    color: #7dd3fc;
}

/* Interactive Simulator Box */
.sim-box {
    background: rgba(0, 0, 0, 0.4);
    border: 1px dashed rgba(56, 189, 248, 0.35);
    border-radius: 10px;
    padding: 14px;
    margin-bottom: 18px;
}
.sim-title {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.75rem;
    color: #38bdf8;
    margin-bottom: 8px;
    display: flex;
    justify-content: space-between;
}
.sim-trigger {
    width: 100%;
    background: linear-gradient(135deg, #0284c7 0%, #6366f1 100%);
    border: none;
    color: #ffffff;
    padding: 10px;
    border-radius: 8px;
    font-family: 'Chakra Petch', sans-serif;
    font-weight: 600;
    font-size: 0.85rem;
    cursor: pointer;
    transition: transform 0.2s, box-shadow 0.2s;
}
.sim-trigger:hover {
    transform: translateY(-2px);
    box-shadow: 0 0 15px rgba(2, 132, 199, 0.6);
}
.sim-output {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.75rem;
    color: #a5f3fc;
    background: #050811;
    border-radius: 6px;
    padding: 10px;
    margin-top: 10px;
    display: none;
    line-height: 1.5;
}

/* Bottom Action Bar */
.bottom-dock {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: rgba(10, 15, 29, 0.75);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 12px;
    padding: 12px 24px;
    backdrop-filter: blur(14px);
}
.dock-links {
    display: flex;
    gap: 14px;
}
.dock-btn {
    text-decoration: none;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.8rem;
    color: #e2e8f0;
    padding: 8px 16px;
    border-radius: 8px;
    border: 1px solid rgba(255, 255, 255, 0.15);
    background: rgba(255, 255, 255, 0.03);
    transition: all 0.2s;
    display: flex;
    align-items: center;
    gap: 8px;
}
.dock-btn:hover {
    border-color: #38bdf8;
    color: #38bdf8;
    box-shadow: 0 0 15px rgba(56, 189, 248, 0.25);
}
.dock-btn.primary {
    background: #0284c7;
    border-color: #38bdf8;
    color: #ffffff;
}
.dock-btn.primary:hover {
    background: #0369a1;
}

@media (max-width: 900px) {
    .node-selector { display: none; }
    .hologram-screen { width: 100%; max-height: 60vh; }
    .telemetry-metrics { display: none; }
}
</style>
</head>
<body>

<div id="canvas-3d"></div>
<div class="crt-overlay"></div>

<div class="hud-layer">
    <!-- Top Telemetry -->
    <div class="telemetry-bar">
        <div class="hud-identity">
            <div class="hud-pulse"></div>
            <div class="hud-name">AVIRAL BAGJANI <span>// ARCHITECT</span></div>
        </div>
        <div class="telemetry-metrics">
            <div class="telemetry-item">LEETCODE: <b>KNIGHT (1784)</b></div>
            <div class="telemetry-item">RAG LATENCY: <b>2.12s</b></div>
            <div class="telemetry-item">EVAL GATE: <b>DEEPEVAL &ge;80%</b></div>
            <div class="telemetry-item">INSTITUTE: <b>IIIT BHAGALPUR</b></div>
        </div>
        <button class="audio-toggle" id="audio-toggle">AUDIO: PROCEDURAL [OFF]</button>
    </div>

    <!-- Center Stage -->
    <div class="main-stage">
        <!-- Node Directory -->
        <div class="node-selector">
            <div class="node-selector-title">NEURAL COGNITIVE NODES</div>
            <button class="node-btn active" onclick="selectNode('agentflow')">
                <span>01. AGENTFLOW</span>
                <span class="tag">LANGGRAPH</span>
            </button>
            <button class="node-btn" onclick="selectNode('ragfury')">
                <span>02. RAGFURY</span>
                <span class="tag">QDRANT/REDIS</span>
            </button>
            <button class="node-btn" onclick="selectNode('zeepty')">
                <span>03. ZEEPTY EXP</span>
                <span class="tag">INTERNSHIP</span>
            </button>
            <button class="node-btn" onclick="selectNode('stack')">
                <span>04. CORE STACK</span>
                <span class="tag">EVALS/GENAI</span>
            </button>
            <button class="node-btn" onclick="selectNode('bio')">
                <span>05. PROFILE/EDU</span>
                <span class="tag">IIIT/ACADEMICS</span>
            </button>
        </div>

        <div class="center-nav-hint">&larr; ROTATE 3D CONSTELLATION WITH MOUSE &rarr;</div>

        <!-- Hologram Information Panel -->
        <div class="hologram-screen" id="hologram-panel">
            <!-- Dynamic Content Injected Here -->
        </div>
    </div>

    <!-- Bottom Dock -->
    <div class="bottom-dock">
        <div style="font-family:'JetBrains Mono',monospace; font-size:0.75rem; color:#64748b;">
            STATUS: READY TO DEPLOY FOR ENTERPRISE AI / GENAI ROLES
        </div>
        <div class="dock-links">
            <a href="https://github.com/aviral-dot" target="_blank" class="dock-btn primary">
                <span>💻 GITHUB (aviral-dot)</span>
            </a>
            <a href="https://www.linkedin.com/in/aviral-bagjani-a02049259/" target="_blank" class="dock-btn">
                <span>💼 LINKEDIN PROFILE</span>
            </a>
            <a href="mailto:aviralbharti832002@gmail.com" class="dock-btn">
                <span>✉️ TRANSMIT EMAIL</span>
            </a>
        </div>
    </div>
</div>

<script>
/* ========================================================
   WEB AUDIO API PROCEDURAL SYNTHESIZER
   ======================================================== */
let audioCtx = null;
let soundEnabled = false;

document.getElementById('audio-toggle').addEventListener('click', () => {
    if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    soundEnabled = !soundEnabled;
    const btn = document.getElementById('audio-toggle');
    if (soundEnabled) {
        btn.textContent = "AUDIO: PROCEDURAL [ON]";
        btn.style.borderColor = "#38bdf8";
        btn.style.boxShadow = "0 0 15px rgba(56, 189, 248, 0.4)";
        playTone(660, 0.08, 'sine');
    } else {
        btn.textContent = "AUDIO: PROCEDURAL [OFF]";
        btn.style.borderColor = "";
        btn.style.boxShadow = "";
    }
});

function playTone(freq = 440, duration = 0.05, type = 'sine') {
    if (!soundEnabled || !audioCtx) return;
    try {
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = type;
        osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
        gain.gain.setValueAtTime(0.04, audioCtx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.0001, audioCtx.currentTime + duration);
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start();
        osc.stop(audioCtx.currentTime + duration);
    } catch(e){}
}

/* ========================================================
   NEURAL NODE DATA REPOSITORY
   ======================================================== */
const nodeData = {
    agentflow: {
        sysId: "SYS-NODE // 01 [MULTI-AGENT]",
        title: "AgentFlow Orchestration",
        subtitle: "Autonomous Planner-Executor Engine with Model Context Protocol",
        stats: [
            { val: "20 / 20", lbl: "State Tests Passed" },
            { val: "< 2 min", lbl: "15-min Workflow Cut" },
            { val: "91%", lbl: "Answer Relevance" },
            { val: "84%", lbl: "Task Completion" }
        ],
        body: `
            Orchestrated a 3-workflow autonomous system (deep research, blog synthesis, email outreach) utilizing <b>LangGraph</b> state graphs with human-in-the-loop gates.<br><br>
            • Integrated external tool ecosystems (Tavily search & Gmail API) using Anthropic's <b>Model Context Protocol (MCP)</b> without corruption across multi-step cycles.<br>
            • Enforced 2-stage <b>NeMo Guardrails</b> for zero-leakage security and <b>DeepEval</b> automated test suites scoring 87% content quality.
        `,
        chips: ["LangGraph", "FastAPI", "Model Context Protocol", "NeMo Guardrails", "DeepEval", "Groq", "LiteLLM", "PostgreSQL"],
        simName: "MULTI-AGENT DISPATCH SIMULATOR",
        simBtn: "EXECUTE PLANNER &rarr; MCP TOOL PIPELINE",
        simAction: runAgentFlowSim
    },
    ragfury: {
        sysId: "SYS-NODE // 02 [RETRIEVAL]",
        title: "RAGFury Agentic Engine",
        subtitle: "High-Throughput Citation RAG with Single-Flight Locking",
        stats: [
            { val: "2.12s", lbl: "E2E Hybrid Latency" },
            { val: "70%", lbl: "Inference Cost Cut" },
            { val: "0.80s", lbl: "Cached Repeat Query" },
            { val: "> 95%", lbl: "Adversarial Blocked" }
        ],
        body: `
            Deployed an enterprise-grade agentic RAG system with hybrid dense+sparse retrieval and citation-grounded generation over a 600-document Qdrant Cloud index.<br><br>
            • Built <b>Redis distributed single-flight locking</b> and scoped caching, crushing latency from 2.8s to 0.8s and stopping redundant LLM calls.<br>
            • Formed 4-component <b>DeepEval</b> regression suites (78–92% evaluation gates) and <b>LangSmith</b> token cost tracing.
        `,
        chips: ["Qdrant Cloud", "Redis Single-Flight", "LangChain", "LangGraph", "Groq", "NeMo Defense", "FastAPI"],
        simName: "LOW-LATENCY RAG BENCHMARK",
        simBtn: "SIMULATE REDIS LOCKING & RETRIEVAL",
        simAction: runRAGFurySim
    },
    zeepty: {
        sysId: "SYS-NODE // 03 [INDUSTRY]",
        title: "Zeepty AI Internship",
        subtitle: "Creator-Commerce Outreach & Semantic Retrieval Engine",
        stats: [
            { val: "+25%", lbl: "Match Retrieval Lift" },
            { val: "+15%", lbl: "Outreach Relevance" },
            { val: "500+", lbl: "Creator Combinations" },
            { val: "Apr–Jul 25", lbl: "Tenure" }
        ],
        body: `
            Worked as AI Engineering Intern optimizing creator-commerce intelligence systems.<br><br>
            • Applied semantic embeddings across 500+ creator and product combinations to lift relevant match retrieval by 25%.<br>
            • Refined prompt orchestration and dynamic retrieval contexts for outbound creator partnerships, lifting response relevance by 15% across 20+ production scenarios.
        `,
        chips: ["Semantic Search", "Prompt Engineering", "Vector Embeddings", "LLM Outreach Pipelines"],
        simName: "SEMANTIC MATCH BENCHMARK",
        simBtn: "RUN SEMANTIC MATCH VERIFICATION",
        simAction: runZeeptySim
    },
    stack: {
        sysId: "SYS-NODE // 04 [COMPETENCIES]",
        title: "Technical Arsenal",
        subtitle: "Production AI Infrastructure, Evals & Software Architecture",
        stats: [
            { val: "1784", lbl: "LeetCode Knight" },
            { val: "500+", lbl: "Problems Solved" },
            { val: "3+", lbl: "Vector Databases" },
            { val: "Top 4.5%", lbl: "JEE Main 2022" }
        ],
        body: `
            <b>AI/GenAI:</b> LLMs, LangGraph, LangChain, CrewAI, MCP, Fine-Tuning, Qdrant, Neo4j, PyTorch.<br>
            <b>Reliability & Ops:</b> NeMo Guardrails, DeepEval regression testing, LangSmith telemetry, LiteLLM.<br>
            <b>Backend & Cloud:</b> Python, C++, SQL, FastAPI, Redis, PostgreSQL, AWS, Docker, Kubernetes, Git, CI/CD.
        `,
        chips: ["Python", "C++", "LangGraph", "FastAPI", "Redis", "Docker", "AWS", "NeMo", "DeepEval", "Qdrant"],
        simName: "LEETCODE / SYSTEMS TEST",
        simBtn: "BENCHMARK ALGORITHMIC PROFICIENCY",
        simAction: runStackSim
    },
    bio: {
        sysId: "SYS-NODE // 05 [ACADEMICS]",
        title: "Aviral Bagjani",
        subtitle: "IIIT Bhagalpur — Electronics & Communication (2022–2026)",
        stats: [
            { val: "6.95", lbl: "CGPA (8th Sem)" },
            { val: "52,750", lbl: "JEE Main AIR" },
            { val: "2026", lbl: "Graduation Year" },
            { val: "Calcutta/Remote", lbl: "Location" }
        ],
        body: `
            Electronics & Communication Engineering student at <b>Indian Institute of Information Technology Bhagalpur</b>.<br><br>
            • Rigorous coursework in Data Structures & Algorithms, DBMS, Operating Systems, Machine Learning, and Computer Networks.<br>
            • Built proven competitive programming credentials (LeetCode Knight, 1784 rating, 500+ problems).
        `,
        chips: ["IIIT Bhagalpur", "B.Tech ECE", "LeetCode Knight", "Algorithms", "Systems Design"],
        simName: "VERIFY CREDENTIALS",
        simBtn: "DISPLAY ACADEMIC & CONTEST TELEMETRY",
        simAction: runBioSim
    }
};

/* ========================================================
   RENDER SELECTED NODE
   ======================================================== */
let activeNodeKey = 'agentflow';

function selectNode(key) {
    activeNodeKey = key;
    playTone(520, 0.05, 'triangle');

    // Update button states
    document.querySelectorAll('.node-btn').forEach((btn, idx) => {
        const keys = ['agentflow', 'ragfury', 'zeepty', 'stack', 'bio'];
        if (keys[idx] === key) btn.classList.add('active');
        else btn.classList.remove('active');
    });

    const data = nodeData[key];
    const panel = document.getElementById('hologram-panel');

    let statsHtml = '';
    data.stats.forEach(s => {
        statsHtml += `
            <div class="stat-pill">
                <div class="val">${s.val}</div>
                <div class="lbl">${s.lbl}</div>
            </div>
        `;
    });

    let chipsHtml = '';
    data.chips.forEach(c => {
        chipsHtml += `<span class="chip">${c}</span>`;
    });

    panel.innerHTML = `
        <div class="screen-header">
            <span class="screen-sys-id">${data.sysId}</span>
            <span style="font-family:'JetBrains Mono'; font-size:0.75rem; color:#10b981;">● ONLINE</span>
        </div>
        <div class="screen-title">${data.title}</div>
        <div class="screen-subtitle">${data.subtitle}</div>
        <div class="stat-pill-row">${statsHtml}</div>
        <div class="screen-body">${data.body}</div>
        <div class="tech-chips">${chipsHtml}</div>
        <div class="sim-box">
            <div class="sim-title">
                <span>// ${data.simName}</span>
                <span style="color:#64748b;">MOCK RUNTIME</span>
            </div>
            <button class="sim-trigger" id="sim-btn" onclick="nodeData['${key}'].simAction()">${data.simBtn}</button>
            <div class="sim-output" id="sim-out"></div>
        </div>
    `;

    // Rotate camera toward corresponding 3D target
    targetCamAngle(key);
}

// Initial render
selectNode('agentflow');

/* ========================================================
   INTERACTIVE SIMULATOR RUNNERS
   ======================================================== */
function runAgentFlowSim() {
    playTone(880, 0.08, 'sawtooth');
    const out = document.getElementById('sim-out');
    out.style.display = 'block';
    out.innerHTML = `[0.00s] Initializing LangGraph state graph...<br>`;
    setTimeout(() => {
        playTone(920, 0.04);
        out.innerHTML += `[0.34s] NeMo Guardrail: Query sanitization passed (0 adversarial tokens).<br>`;
    }, 280);
    setTimeout(() => {
        playTone(1050, 0.05);
        out.innerHTML += `[0.82s] MCP Dispatch: Tavily search returned 6 live citations.<br>`;
    }, 600);
    setTimeout(() => {
        playTone(1200, 0.08);
        out.innerHTML += `[1.41s] DeepEval Gate: Task completion 84% &gt; threshold 80% [PASS].<br>`;
        out.innerHTML += `<b style="color:#34d399;">&check; Workflow completed in 1.41s. Human-in-the-loop draft generated.</b>`;
    }, 950);
}

function runRAGFurySim() {
    playTone(750, 0.08, 'sawtooth');
    const out = document.getElementById('sim-out');
    out.style.display = 'block';
    out.innerHTML = `[0.00s] User query received: "Compare Redis single-flight with semaphore"<br>`;
    setTimeout(() => {
        playTone(820, 0.05);
        out.innerHTML += `[0.04s] Redis single-flight lock acquired. Suppressed 4 duplicate concurrent workers.<br>`;
    }, 250);
    setTimeout(() => {
        playTone(980, 0.05);
        out.innerHTML += `[0.61s] Qdrant Cloud hybrid search: 5 chunks matched (top score 0.942).<br>`;
    }, 550);
    setTimeout(() => {
        playTone(1280, 0.08);
        out.innerHTML += `[0.80s] Groq inference stream complete with 3 verified citations.<br>`;
        out.innerHTML += `<b style="color:#38bdf8;">&check; Latency: 0.80s (Saved 70% inference cost via distributed lock).</b>`;
    }, 850);
}

function runZeeptySim() {
    playTone(600, 0.06);
    const out = document.getElementById('sim-out');
    out.style.display = 'block';
    out.innerHTML = `[EMBED] Generating 1536-dim vector for Creator Profile...<br>`;
    setTimeout(() => {
        out.innerHTML += `[RETRIEVAL] Matching against 500+ commerce brand campaigns...<br>`;
        out.innerHTML += `<b style="color:#34d399;">&check; Semantic match lift confirmed: +25% top-k relevance.</b>`;
    }, 500);
}

function runStackSim() {
    playTone(700, 0.06);
    const out = document.getElementById('sim-out');
    out.style.display = 'block';
    out.innerHTML = `[LEETCODE] Rating: 1784 (Knight Tier, Top 5% globally).<br>`;
    out.innerHTML += `[DSA] 500+ problems solved across Graph, DP, Tree structures.<br>`;
    out.innerHTML += `<b style="color:#38bdf8;">&check; Strong systems foundation verified.</b>`;
}

function runBioSim() {
    playTone(550, 0.06);
    const out = document.getElementById('sim-out');
    out.style.display = 'block';
    out.innerHTML = `[DEGREE] B.Tech in Electronics & Communication — IIIT Bhagalpur.<br>`;
    out.innerHTML += `[EXAM] JEE Main AIR 52,750 out of 1.2M+ candidates (95.44%ile).<br>`;
    out.innerHTML += `<b style="color:#38bdf8;">&check; Ready to join forward-thinking AI teams.</b>`;
}

/* ========================================================
   THREE.JS 3D CONSTELLATION & INTERACTIVE CORE
   ======================================================== */
const container = document.getElementById('canvas-3d');
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(50, window.innerWidth / window.innerHeight, 0.1, 1000);
camera.position.set(0, 0, 9);

const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
container.appendChild(renderer.domElement);

// Node 3D Coordinates & Meshes
const nodePositions = {
    agentflow: new THREE.Vector3(-2.8, 1.2, 0),
    ragfury:   new THREE.Vector3(2.8, 1.2, 0),
    zeepty:    new THREE.Vector3(-2.2, -1.8, 0),
    stack:     new THREE.Vector3(2.2, -1.8, 0),
    bio:       new THREE.Vector3(0, 0, 1.2)
};

const nodeSpheres = {};
const group = new THREE.Group();
scene.add(group);

// Central Quantum Core Icosahedron
const coreGeo = new THREE.IcosahedronGeometry(1.2, 1);
const coreMat = new THREE.MeshBasicMaterial({
    color: 0x0284c7,
    wireframe: true,
    transparent: true,
    opacity: 0.25
});
const coreMesh = new THREE.Mesh(coreGeo, coreMat);
group.add(coreMesh);

// Glowing Nodes
Object.keys(nodePositions).forEach(key => {
    const pos = nodePositions[key];
    const sGeo = new THREE.SphereGeometry(0.24, 16, 16);
    const sMat = new THREE.MeshBasicMaterial({ color: 0x38bdf8 });
    const sMesh = new THREE.Mesh(sGeo, sMat);
    sMesh.position.copy(pos);
    group.add(sMesh);

    // Outer wire ring
    const rGeo = new THREE.RingGeometry(0.32, 0.36, 24);
    const rMat = new THREE.MeshBasicMaterial({ color: 0x818cf8, side: THREE.DoubleSide });
    const rMesh = new THREE.Mesh(rGeo, rMat);
    rMesh.position.copy(pos);
    group.add(rMesh);

    nodeSpheres[key] = { mesh: sMesh, ring: rMesh };
});

// Connecting Synapse Lines
const lineMat = new THREE.LineBasicMaterial({ color: 0x38bdf8, transparent: true, opacity: 0.25 });
const connections = [
    ['agentflow', 'bio'],
    ['ragfury', 'bio'],
    ['zeepty', 'bio'],
    ['stack', 'bio'],
    ['agentflow', 'ragfury'],
    ['zeepty', 'stack']
];

connections.forEach(([n1, n2]) => {
    const points = [nodePositions[n1], nodePositions[n2]];
    const lGeo = new THREE.BufferGeometry().setFromPoints(points);
    const line = new THREE.Line(lGeo, lineMat);
    group.add(line);
});

// Surrounding Particle Field
const pCount = 700;
const pGeo = new THREE.BufferGeometry();
const pPos = new Float32Array(pCount * 3);
for (let i = 0; i < pCount * 3; i += 3) {
    pPos[i] = (Math.random() - 0.5) * 22;
    pPos[i+1] = (Math.random() - 0.5) * 16;
    pPos[i+2] = (Math.random() - 0.5) * 16 - 2;
}
pGeo.setAttribute('position', new THREE.BufferAttribute(pPos, 3));
const pMat = new THREE.PointsMaterial({ color: 0x38bdf8, size: 0.035, transparent: true, opacity: 0.55 });
const pMesh = new THREE.Points(pGeo, pMat);
group.add(pMesh);

// Mouse Interaction & Parallax
let mouseX = 0, mouseY = 0;
let targetRotX = 0, targetRotY = 0;

window.addEventListener('mousemove', (e) => {
    mouseX = (e.clientX / window.innerWidth - 0.5) * 2;
    mouseY = (e.clientY / window.innerHeight - 0.5) * 2;
});

function targetCamAngle(key) {
    const pos = nodePositions[key];
    targetRotY = -pos.x * 0.15;
    targetRotX = pos.y * 0.15;
}

function animate() {
    requestAnimationFrame(animate);

    // Smooth rotation lerp
    group.rotation.y += (mouseX * 0.4 + targetRotY - group.rotation.y) * 0.04;
    group.rotation.x += (-mouseY * 0.4 + targetRotX - group.rotation.x) * 0.04;

    coreMesh.rotation.y += 0.005;
    coreMesh.rotation.x += 0.003;
    pMesh.rotation.y += 0.0006;

    // Pulse active node
    Object.keys(nodeSpheres).forEach(k => {
        const ring = nodeSpheres[k].ring;
        ring.rotation.z += 0.02;
        if (k === activeNodeKey) {
            nodeSpheres[k].mesh.scale.set(1.4, 1.4, 1.4);
            nodeSpheres[k].mesh.material.color.setHex(0x34d399);
        } else {
            nodeSpheres[k].mesh.scale.set(1, 1, 1);
            nodeSpheres[k].mesh.material.color.setHex(0x38bdf8);
        }
    });

    renderer.render(scene, camera);
}
animate();

window.addEventListener('resize', () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
});
</script>
</body>
</html>
"""

components.html(CYBER_DECK_HTML, height=920, scrolling=False)

