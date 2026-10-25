import streamlit as st

st.set_page_config(
    page_title="Mythri Potluri | AI Agent Portfolio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, .stApp {
    background-color: #0A0F1E !important;
    font-family: 'Inter', -apple-system, sans-serif;
    color: #E2E8F0;
}

#MainMenu, footer, header, .stDeployButton { visibility: hidden !important; display: none !important; }
[data-testid="stToolbar"] { display: none !important; }
.stDecoration { display: none !important; }
section[data-testid="stSidebar"] { display: none !important; }
.block-container { padding: 0 !important; max-width: 100% !important; }

@keyframes gradientShift {
    0%   { background-position: 0% 50%; }
    50%  { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(20px); }
    to   { opacity: 1; transform: translateY(0); }
}
@keyframes pulseDot {
    0%, 100% { opacity: 1; }
    50%       { opacity: 0.4; }
}

/* ── Recruiter Profile Bar ── */
.profile-bar {
    background: linear-gradient(135deg, #0D1627 0%, #111827 100%);
    border-bottom: 1px solid rgba(99,102,241,0.18);
    padding: 18px 48px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 16px;
    position: relative;
    z-index: 10;
}

.profile-bar::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; height: 2px;
    background: linear-gradient(90deg, #6366F1, #06B6D4, #8B5CF6, #6366F1);
    background-size: 200% 100%;
    animation: gradientShift 4s linear infinite;
}

.profile-left { display: flex; flex-direction: column; gap: 4px; }

.profile-name {
    font-size: 20px;
    font-weight: 900;
    color: #FFFFFF;
    letter-spacing: 1.5px;
    line-height: 1;
    text-transform: uppercase;
}

.profile-title-tag {
    font-size: 12px;
    color: #94A3B8;
    font-weight: 400;
    display: flex;
    align-items: center;
    gap: 10px;
}

.profile-title-tag .sep { color: #334155; }

.available-badge {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    background: rgba(34,197,94,0.10);
    border: 1px solid rgba(34,197,94,0.25);
    color: #4ADE80;
    padding: 2px 10px;
    border-radius: 20px;
    font-size: 10px;
    font-weight: 600;
    letter-spacing: 0.5px;
}

.av-dot {
    width: 5px; height: 5px;
    border-radius: 50%;
    background: #22C55E;
    animation: pulseDot 2s ease infinite;
}

.profile-links {
    display: flex;
    align-items: center;
    gap: 8px;
    flex-wrap: wrap;
}

.p-link {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 7px 14px;
    border-radius: 8px;
    font-size: 12px;
    font-weight: 600;
    text-decoration: none !important;
    transition: all 0.15s ease;
    cursor: pointer;
    min-height: 34px;
    border: 1px solid transparent;
}

.p-link:active { transform: scale(0.94); }

.p-link-li {
    background: rgba(10,102,194,0.15);
    border-color: rgba(10,102,194,0.35);
    color: #60A5FA !important;
}
.p-link-li:hover { background: rgba(10,102,194,0.28); border-color: rgba(10,102,194,0.6); }

.p-link-gh {
    background: rgba(255,255,255,0.05);
    border-color: rgba(255,255,255,0.12);
    color: #CBD5E1 !important;
}
.p-link-gh:hover { background: rgba(255,255,255,0.10); border-color: rgba(255,255,255,0.22); }

.p-link-pf {
    background: rgba(139,92,246,0.12);
    border-color: rgba(139,92,246,0.3);
    color: #C4B5FD !important;
}
.p-link-pf:hover { background: rgba(139,92,246,0.22); border-color: rgba(139,92,246,0.5); }

.p-link-em {
    background: rgba(6,182,212,0.10);
    border-color: rgba(6,182,212,0.25);
    color: #67E8F9 !important;
}
.p-link-em:hover { background: rgba(6,182,212,0.20); border-color: rgba(6,182,212,0.45); }


/* ── Hero ── */
.hero-wrap {
    background: linear-gradient(135deg, #0A0F1E 0%, #0D1B3E 40%, #0A0F1E 100%);
    background-size: 300% 300%;
    animation: gradientShift 14s ease infinite;
    padding: 56px 40px 52px;
    text-align: center;
    border-bottom: 1px solid rgba(99,102,241,0.12);
    position: relative;
    overflow: hidden;
}

/* ── Summary section ── */
.hero-summary-wrap {
    max-width: 720px;
    margin: 0 auto 40px;
    background: rgba(99,102,241,0.05);
    border: 1px solid rgba(99,102,241,0.15);
    border-radius: 14px;
    padding: 20px 28px;
    animation: fadeInUp 0.6s ease 0.15s both;
}

.hero-summary-eyebrow {
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #6366F1;
    margin-bottom: 10px;
    font-family: 'JetBrains Mono', monospace;
}

.hero-summary-text {
    font-size: 15px;
    color: #CBD5E1;
    line-height: 1.75;
    font-weight: 400;
}

.hero-summary-text strong {
    color: #E2E8F0;
    font-weight: 600;
}
.hero-wrap::before {
    content: '';
    position: absolute; inset: 0;
    background:
        radial-gradient(ellipse 60% 40% at 20% 20%, rgba(99,102,241,0.10) 0%, transparent 70%),
        radial-gradient(ellipse 50% 35% at 80% 80%, rgba(6,182,212,0.07) 0%, transparent 70%);
    pointer-events: none;
}

.hero-badge {
    display: inline-block;
    background: rgba(99,102,241,0.12);
    border: 1px solid rgba(99,102,241,0.35);
    color: #A5B4FC;
    padding: 5px 16px;
    border-radius: 20px;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 24px;
    animation: fadeInUp 0.6s ease both;
}
.hero-title {
    font-size: clamp(30px, 5vw, 66px);
    font-weight: 900;
    line-height: 1.05;
    margin-bottom: 20px;
    background: linear-gradient(135deg, #FFFFFF 0%, #C7D2FE 40%, #67E8F9 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    letter-spacing: -1px;
    animation: fadeInUp 0.6s ease 0.1s both;
}
.hero-subtitle {
    font-size: 16px;
    color: #94A3B8;
    max-width: 540px;
    margin: 0 auto 44px;
    line-height: 1.75;
    animation: fadeInUp 0.6s ease 0.2s both;
}
.tech-badges {
    display: flex;
    justify-content: center;
    gap: 10px;
    flex-wrap: wrap;
    margin-bottom: 44px;
    animation: fadeInUp 0.6s ease 0.3s both;
}
.tech-badge {
    display: inline-flex;
    align-items: center;
    gap: 7px;
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    color: #94A3B8;
    padding: 7px 14px;
    border-radius: 8px;
    font-size: 12px;
    font-weight: 500;
    font-family: 'JetBrains Mono', monospace;
}
.tb-dot { width: 6px; height: 6px; border-radius: 50%; flex-shrink: 0; }

.hero-stats {
    display: flex;
    justify-content: center;
    max-width: 500px;
    margin: 0 auto;
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 14px;
    overflow: hidden;
    background: rgba(255,255,255,0.02);
    animation: fadeInUp 0.6s ease 0.4s both;
}
.stat-box { flex: 1; padding: 20px 16px; text-align: center; border-right: 1px solid rgba(255,255,255,0.06); }
.stat-box:last-child { border-right: none; }
.stat-num { font-size: 30px; font-weight: 900; line-height: 1; margin-bottom: 6px; display: block; }
.stat-lbl { font-size: 10px; font-weight: 600; letter-spacing: 1.5px; text-transform: uppercase; color: #475569; display: block; }

/* Tabs */
.stTabs [data-baseweb="tab-list"] {
    background: transparent !important;
    border-bottom: 1px solid rgba(255,255,255,0.07) !important;
    padding: 0 40px !important;
    gap: 4px !important;
}
.stTabs [data-baseweb="tab"] {
    background: transparent !important;
    color: #64748B !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 14px !important;
    font-weight: 600 !important;
    padding: 16px 24px !important;
    border-radius: 0 !important;
    border: none !important;
    border-bottom: 2px solid transparent !important;
    margin-bottom: -1px !important;
    transition: color 0.2s !important;
}
.stTabs [data-baseweb="tab"]:hover { color: #CBD5E1 !important; }
.stTabs [aria-selected="true"] {
    color: #E2E8F0 !important;
    border-bottom: 2px solid #6366F1 !important;
    background: transparent !important;
}
.stTabs [data-baseweb="tab-panel"] { background: transparent !important; padding: 0 !important; }
.stTabs [data-baseweb="tab-highlight"],
.stTabs [data-baseweb="tab-border"] { display: none !important; }

/* Domain section */
.domain-wrap { padding: 40px 40px 60px; animation: fadeInUp 0.4s ease both; }
.domain-tag {
    display: inline-block;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    padding: 4px 12px;
    border-radius: 4px;
    margin-bottom: 12px;
}
.domain-title { font-size: 26px; font-weight: 800; color: #F1F5F9; margin-bottom: 8px; letter-spacing: -0.5px; }
.domain-desc { font-size: 14px; color: #64748B; line-height: 1.7; max-width: 680px; margin-bottom: 32px; }

/* Card grid */
.agents-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; }

/* Agent card */
.agent-card {
    background: rgba(255,255,255,0.025);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 16px;
    overflow: hidden;
    transition: transform 0.25s ease, border-color 0.25s ease, box-shadow 0.25s ease;
    display: flex;
    flex-direction: column;
}
.agent-card:hover {
    transform: translateY(-5px);
    border-color: rgba(255,255,255,0.14);
    box-shadow: 0 20px 40px rgba(0,0,0,0.4);
}
.card-hdr {
    padding: 22px 22px 20px;
    position: relative;
    overflow: hidden;
}
.card-hdr::before {
    content: '';
    position: absolute; inset: 0;
    background-image: linear-gradient(rgba(255,255,255,0.04) 1px, transparent 1px),
                      linear-gradient(90deg, rgba(255,255,255,0.04) 1px, transparent 1px);
    background-size: 20px 20px;
    pointer-events: none;
}
.card-hdr::after {
    content: '';
    position: absolute;
    bottom: 0; left: 0; right: 0; height: 1px;
    background: rgba(0,0,0,0.25);
}
.card-id { font-family: 'JetBrains Mono', monospace; font-size: 10px; font-weight: 600; letter-spacing: 2px; text-transform: uppercase; opacity: 0.7; margin-bottom: 8px; position: relative; }
.card-name { font-size: 17px; font-weight: 700; color: #FFFFFF; line-height: 1.3; margin-bottom: 14px; position: relative; }
.trigger-pill { display: inline-flex; align-items: center; gap: 6px; background: rgba(0,0,0,0.3); border: 1px solid rgba(255,255,255,0.12); border-radius: 20px; padding: 4px 12px; font-size: 11px; font-weight: 500; color: rgba(255,255,255,0.6); position: relative; }
.t-dot { width: 5px; height: 5px; border-radius: 50%; background: #22C55E; animation: pulseDot 2s ease infinite; }

/* Card body */
.card-body { padding: 20px 22px; flex: 1; display: flex; flex-direction: column; }
.xyz-row { display: flex; gap: 10px; align-items: flex-start; margin-bottom: 10px; }
.xyz-lbl { font-size: 9px; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; padding: 3px 8px; border-radius: 4px; min-width: 62px; text-align: center; flex-shrink: 0; margin-top: 2px; font-family: 'JetBrains Mono', monospace; }
.lp { background: rgba(239,68,68,0.12); color: #FCA5A5; border: 1px solid rgba(239,68,68,0.2); }
.lb { background: rgba(99,102,241,0.12); color: #A5B4FC; border: 1px solid rgba(99,102,241,0.2); }
.ls { background: rgba(34,197,94,0.12); color: #86EFAC; border: 1px solid rgba(34,197,94,0.2); }
.xyz-txt { font-size: 12.5px; color: #CBD5E1; line-height: 1.65; }

.card-div { height: 1px; background: rgba(255,255,255,0.05); margin: 14px 0; }
.wf-label { font-size: 10px; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; color: #475569; margin-bottom: 10px; font-family: 'JetBrains Mono', monospace; }
.uc-title { font-size: 10px; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; color: #475569; margin-bottom: 10px; font-family: 'JetBrains Mono', monospace; margin-top: 14px; }
.uc-row { display: flex; align-items: flex-start; gap: 8px; margin-bottom: 7px; }
.uc-dot { width: 5px; height: 5px; border-radius: 50%; margin-top: 6px; flex-shrink: 0; }
.uc-txt { font-size: 12px; color: #94A3B8; line-height: 1.55; }
.uc-co { font-weight: 600; color: #CBD5E1; }
.metrics-row { display: flex; gap: 8px; margin-top: auto; padding-top: 14px; }
.m-chip { background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.07); border-radius: 6px; padding: 7px 10px; font-size: 11px; color: #64748B; font-family: 'JetBrains Mono', monospace; flex: 1; text-align: center; }
.m-val { display: block; font-size: 14px; font-weight: 700; color: #CBD5E1; margin-bottom: 2px; }
.n8n-btn { display: block; text-align: center; padding: 11px 20px; border-radius: 9px; font-size: 13px; font-weight: 600; text-decoration: none; margin-top: 14px; color: white !important; transition: opacity 0.2s; min-height: 44px; line-height: 22px; }
.n8n-btn:hover { opacity: 0.85; color: white !important; text-decoration: none !important; }

/* Domain color themes */
.shot { width:100%; display:block; border-radius:10px; border:1px solid rgba(255,255,255,0.10); margin:8px 0 14px; }
.hc-hdr { background: linear-gradient(135deg, #0C4A6E 0%, #134E4A 100%); }
.hc-id { color: #67E8F9; }
.hc-tag { background: rgba(6,182,212,0.12); color: #67E8F9; border: 1px solid rgba(6,182,212,0.25); }
.hc-ttl { color: #67E8F9; }
.hc-dot { background: #06B6D4; }
.hc-btn { background: linear-gradient(135deg, #0369A1, #0F766E); }
.hc-val { color: #67E8F9; }

.tr-hdr { background: linear-gradient(135deg, #7C2D12 0%, #78350F 100%); }
.tr-id { color: #FDBA74; }
.tr-tag { background: rgba(249,115,22,0.12); color: #FDBA74; border: 1px solid rgba(249,115,22,0.25); }
.tr-ttl { color: #FDBA74; }
.tr-dot { background: #F97316; }
.tr-btn { background: linear-gradient(135deg, #C2410C, #B45309); }
.tr-val { color: #FDBA74; }

.cn-hdr { background: linear-gradient(135deg, #3B1702 0%, #2E1065 100%); }
.cn-id { color: #FDE68A; }
.cn-tag { background: rgba(234,179,8,0.12); color: #FDE68A; border: 1px solid rgba(234,179,8,0.25); }
.cn-ttl { color: #FDE68A; }
.cn-dot { background: #EAB308; }
.cn-btn { background: linear-gradient(135deg, #92400E, #5B21B6); }
.cn-val { color: #FDE68A; }

/* Footer */
.portfolio-footer { background: rgba(0,0,0,0.25); border-top: 1px solid rgba(255,255,255,0.05); padding: 40px; text-align: center; }
.footer-repos { display: flex; justify-content: center; gap: 12px; margin-bottom: 20px; flex-wrap: wrap; }
.repo-link { display: inline-block; background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); border-radius: 8px; padding: 8px 16px; font-size: 12px; font-weight: 500; color: #94A3B8 !important; text-decoration: none !important; font-family: 'JetBrains Mono', monospace; transition: all 0.2s; }
.repo-link:hover { background: rgba(255,255,255,0.07); color: #E2E8F0 !important; }
.footer-credit { font-size: 13px; color: #475569; }
.footer-credit a { color: #6366F1 !important; text-decoration: none; font-weight: 500; }

@media (max-width: 900px) {
    .agents-grid { grid-template-columns: 1fr !important; }
    .hero-wrap, .domain-wrap { padding-left: 20px; padding-right: 20px; }
    .stTabs [data-baseweb="tab-list"] { padding: 0 20px !important; }
}
</style>
""", unsafe_allow_html=True)


# ─── SVG WORKFLOW BUILDER ─────────────────────────────────────────────────────

def build_workflow_svg(steps: list, dc: tuple, agent_id: str) -> str:
    """
    Build a visual SVG flowchart.
    dc = (decision_bg, decision_border, warn_bg, warn_text, warn_border)
    steps = list of {"label", "type", "branches":[{"label","type","side_label"}]}
    """
    W = 280
    NW = 188      # full-width node width
    NH = 34       # node height
    CX = W // 2  # 140
    YGAP = 14    # gap between nodes (arrow space)
    BW2 = 118    # branch node width (2-branch)
    BW3 = 82     # branch node width (3-branch)

    mid = "m" + agent_id.lower().replace("-", "")  # unique marker ID

    # (bg, text, border, radius)
    NODE_STYLES = {
        "trigger":  ("#172554", "#7DD3FC", "#1D4ED8", 7),
        "process":  ("#0F1629", "#94A3B8", "#1E293B", 7),
        "ai":       ("#1E1247", "#C4B5FD", "#4338CA", 7),
        "decision": (dc[0],     "#FFFFFF",  dc[1],    7),
        "ok":       ("#052E16", "#4ADE80", "#166534", 7),
        "warn":     (dc[2],     dc[3],     dc[4],    7),
        "neutral":  ("#0F172A", "#475569", "#1E293B", 7),
    }

    # Small type label shown inside node (top-left corner tiny text)
    TYPE_LABELS = {
        "trigger":  "TRIGGER",
        "process":  "STEP",
        "ai":       "CLAUDE",
        "decision": "ROUTE",
        "ok":       "OUTPUT",
        "warn":     "OUTPUT",
        "neutral":  "OUTPUT",
    }

    def rect_node(x, y, w, h, ntype, label):
        bg, fg, border, rx = NODE_STYLES[ntype]
        # Type micro-label
        type_lbl = TYPE_LABELS[ntype]
        type_fg = {
            "trigger": "#3B82F6", "process": "#334155", "ai": "#6D28D9",
            "decision": "rgba(255,255,255,0.4)", "ok": "#166534",
            "warn": "rgba(255,255,255,0.35)", "neutral": "#1E293B",
        }.get(ntype, "#334155")

        # Main label — split into 2 lines if long
        words = label.split()
        if len(label) <= 22 or len(words) <= 2:
            lines = [label]
        else:
            mid_idx = len(words) // 2
            lines = [" ".join(words[:mid_idx]), " ".join(words[mid_idx:])]

        text_parts = []
        if len(lines) == 1:
            text_parts.append(
                f'<text x="{x + w//2}" y="{y + h//2 + 4}" text-anchor="middle" '
                f'fill="{fg}" font-size="10" font-family="Inter,sans-serif" font-weight="600">{lines[0]}</text>'
            )
        else:
            text_parts.append(
                f'<text x="{x + w//2}" y="{y + h//2 - 3}" text-anchor="middle" '
                f'fill="{fg}" font-size="9.5" font-family="Inter,sans-serif" font-weight="600">{lines[0]}</text>'
            )
            text_parts.append(
                f'<text x="{x + w//2}" y="{y + h//2 + 10}" text-anchor="middle" '
                f'fill="{fg}" font-size="9.5" font-family="Inter,sans-serif" font-weight="600">{lines[1]}</text>'
            )

        rect = (
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
            f'fill="{bg}" stroke="{border}" stroke-width="1"/>'
        )
        type_text = (
            f'<text x="{x+6}" y="{y+8}" fill="{type_fg}" '
            f'font-size="6.5" font-family="JetBrains Mono,monospace" font-weight="700">{type_lbl}</text>'
        )
        return rect + type_text + "".join(text_parts)

    def arrow_line(x1, y1, x2, y2):
        return (
            f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
            f'stroke="rgba(255,255,255,0.2)" stroke-width="1.5" '
            f'marker-end="url(#{mid})"/>'
        )

    def side_label(x, y, txt):
        return (
            f'<text x="{x}" y="{y}" text-anchor="middle" '
            f'fill="#475569" font-size="8.5" font-family="Inter,sans-serif" '
            f'font-weight="500" font-style="italic">{txt}</text>'
        )

    parts = []
    y = 10

    for i, step in enumerate(steps):
        ntype = step["type"]
        branches = step.get("branches", [])

        if ntype == "decision" and branches:
            # Draw decision node
            parts.append(rect_node(CX - NW // 2, y, NW, NH, ntype, step["label"]))
            dy = y  # decision node top

            nb = len(branches)
            branch_y = dy + NH + 28

            if nb == 2:
                lx = 10
                rx = W - 10 - BW2
                lcx = lx + BW2 // 2
                rcx = rx + BW2 // 2

                # Left branch arrow + label
                parts.append(arrow_line(CX, dy + NH, lcx, branch_y))
                sl = branches[0].get("side_label", "Yes")
                parts.append(side_label(lcx, branch_y - 8, sl))
                parts.append(rect_node(lx, branch_y, BW2, NH, branches[0]["type"], branches[0]["label"]))

                # Right branch arrow + label
                parts.append(arrow_line(CX, dy + NH, rcx, branch_y))
                sr = branches[1].get("side_label", "No")
                parts.append(side_label(rcx, branch_y - 8, sr))
                parts.append(rect_node(rx, branch_y, BW2, NH, branches[1]["type"], branches[1]["label"]))

                y = branch_y + NH + 8

            elif nb == 3:
                xs = [4, (W - BW3) // 2, W - 4 - BW3]
                for bx, branch in zip(xs, branches):
                    bcx = bx + BW3 // 2
                    parts.append(arrow_line(CX, dy + NH, bcx, branch_y))
                    sl = branch.get("side_label", "")
                    parts.append(side_label(bcx, branch_y - 8, sl))
                    parts.append(rect_node(bx, branch_y, BW3, NH, branch["type"], branch["label"]))
                y = branch_y + NH + 8

        else:
            # Regular node
            parts.append(rect_node(CX - NW // 2, y, NW, NH, ntype, step["label"]))
            if i + 1 < len(steps):
                parts.append(arrow_line(CX, y + NH, CX, y + NH + YGAP))
            y += NH + YGAP

    total_h = y + 6

    svg = (
        f'<svg viewBox="0 0 {W} {total_h}" xmlns="http://www.w3.org/2000/svg" '
        f'style="width:100%;display:block;border-radius:10px;">'
        f'<defs>'
        f'<marker id="{mid}" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">'
        f'<path d="M0,0 L0,6 L8,3 z" fill="rgba(255,255,255,0.3)"/>'
        f'</marker>'
        f'</defs>'
        f'<rect width="{W}" height="{total_h}" fill="rgba(0,0,0,0.28)" rx="10"/>'
        + "".join(parts)
        + f'</svg>'
    )
    return svg


# ─── DATA ─────────────────────────────────────────────────────────────────────

# domain_colors = (decision_bg, decision_border, warn_bg, warn_text, warn_border)
HC = ("#0C4A6E", "#0369A1", "#134E4A", "#5EEAD4", "#0D9488")
TR = ("#7C2D12", "#C2410C", "#78350F", "#FCD34D", "#B45309")
CN = ("#3B1702", "#B45309", "#2E1065", "#C4B5FD", "#7C3AED")

AGENTS = {
    "healthcare": [
        {
            "id": "HC-1",
            "name": "Patient Discharge &amp; Care Continuity",
            "trigger": "Webhook", "trigger_label": "POST Request",
            "nodes": 11,
            "problem": "Hospitals discharge many patients every day, and high risk cases can slip through without timely follow up, which raises the chance of readmission.",
            "built": "A webhook agent that normalizes each discharge, has Claude assess readmission risk with a structured output, and routes the case by risk level.",
            "solved": "High risk patients trigger an urgent email to the physician, medium risk patients get a follow up reminder email, and low risk discharges are logged with a routine care plan.",
            "workflow_steps": [
                {"label": "EHR Discharge Event", "type": "trigger"},
                {"label": "Normalize Payload", "type": "process"},
                {"label": "Claude Risk Assessment", "type": "ai"},
                {"label": "Risk Level Router", "type": "decision", "branches": [
                    {"label": "Email Physician", "type": "warn", "side_label": "High"},
                    {"label": "Follow-up Email", "type": "neutral", "side_label": "Medium"},
                    {"label": "Log Care Plan", "type": "ok", "side_label": "Low"},
                ]},
            ],
            "dc": HC,
            "companies": [
                ("Hospital systems", "post discharge follow up for cardiac patients"),
                ("Health networks", "same day nurse callbacks for CHF and COPD patients"),
                ("Telehealth platforms", "virtual follow up scheduling at discharge"),
            ],
            "n8n_url": "https://github.com/mythrip11/ai-agent-portfolio/blob/main/workflows/healthcare/HC-1_patient-discharge-care-continuity.json",
        },
        {
            "id": "HC-2",
            "name": "Insurance Prior Authorization Automation",
            "trigger": "Webhook", "trigger_label": "Auth Requests",
            "nodes": 11,
            "problem": "Providers spend a lot of time assembling prior authorization requests by hand, which delays patient procedures.",
            "built": "An agent that checks coverage (mock eligibility step), has Claude evaluate the clinical notes against medical necessity criteria, and submits to the payer (mock step) when they are met.",
            "solved": "Requests that meet the criteria are submitted and confirmed by email. Requests with gaps get an email listing exactly which documents are missing, and inactive coverage gets its own notice.",
            "workflow_steps": [
                {"label": "Auth Request Webhook", "type": "trigger"},
                {"label": "Check Eligibility (mock)", "type": "process"},
                {"label": "Claude Medical Necessity", "type": "ai"},
                {"label": "Criteria Met?", "type": "decision", "branches": [
                    {"label": "Submit to Payer", "type": "ok", "side_label": "Yes"},
                    {"label": "Email Missing Docs", "type": "neutral", "side_label": "No"},
                ]},
            ],
            "dc": HC,
            "companies": [
                ("Payer teams", "pre screen high volume imaging and orthopedic requests"),
                ("Provider offices", "cut the back and forth on routine outpatient procedures"),
                ("EHR integrated clinics", "trigger requests directly from intake forms"),
            ],
            "n8n_url": "https://github.com/mythrip11/ai-agent-portfolio/blob/main/workflows/healthcare/HC-2_insurance-prior-authorization.json",
        },
        {
            "id": "HC-3",
            "name": "Clinical Trial Recruitment &amp; Screening",
            "trigger": "Schedule", "trigger_label": "Daily at 8am",
            "nodes": 10,
            "problem": "Research teams often screen patient charts by hand to find trial candidates, which is slow and can miss eligible patients.",
            "built": "A daily agent that pulls a patient list (mock EHR), splits it into one item per patient, and has Claude screen each one against trial inclusion and exclusion criteria.",
            "solved": "Eligible patients get a personalized outreach email and are logged as candidates. Ineligible patients are logged with the reason.",
            "workflow_steps": [
                {"label": "Daily 8am Scheduler", "type": "trigger"},
                {"label": "Fetch Patients (mock EHR)", "type": "process"},
                {"label": "Split Patients", "type": "process"},
                {"label": "Claude Trial Screening", "type": "ai"},
                {"label": "Eligible?", "type": "decision", "branches": [
                    {"label": "Send Outreach Email", "type": "ok", "side_label": "Yes"},
                    {"label": "Log Ineligible", "type": "neutral", "side_label": "No"},
                ]},
            ],
            "dc": HC,
            "companies": [
                ("Research teams", "automate recruitment screening across partner clinics"),
                ("Trial platforms", "feed screening results into trial management systems"),
                ("Academic medical centers", "run nightly screens across concurrent trials"),
            ],
            "n8n_url": "https://github.com/mythrip11/ai-agent-portfolio/blob/main/workflows/healthcare/HC-3_clinical-trial-recruitment.json",
        },
    ],
    "transportation": [
        {
            "id": "TR-4",
            "name": "Fleet Predictive Maintenance",
            "trigger": "Schedule", "trigger_label": "Every Hour",
            "nodes": 10,
            "problem": "Fleet maintenance is often reactive, so breakdowns and missed deliveries happen before anyone looks at the warning signs in the telematics data.",
            "built": "An hourly agent that reads telematics for each vehicle (mock data), has Claude analyze sensor readings and fault codes, and returns urgency, the likely failing component, and a recommended action.",
            "solved": "At risk vehicles get a mock service appointment, timed by urgency, and the fleet manager is emailed the details. Healthy vehicles are logged.",
            "workflow_steps": [
                {"label": "Hourly Scheduler", "type": "trigger"},
                {"label": "Fetch Telemetry (mock)", "type": "process"},
                {"label": "Split Vehicles", "type": "process"},
                {"label": "Claude Maintenance Analysis", "type": "ai"},
                {"label": "Maintenance Needed?", "type": "decision", "branches": [
                    {"label": "Schedule + Alert", "type": "warn", "side_label": "Yes"},
                    {"label": "Log Healthy", "type": "ok", "side_label": "No"},
                ]},
            ],
            "dc": TR,
            "companies": [
                ("Truck fleets", "act on engine and brake warnings before a breakdown"),
                ("Delivery fleets", "monitor van health across many vehicles"),
                ("Transit operators", "prioritize maintenance by urgency"),
            ],
            "n8n_url": "https://github.com/mythrip11/ai-agent-portfolio/blob/main/workflows/transportation/TR-4_fleet-predictive-maintenance.json",
        },
        {
            "id": "TR-5",
            "name": "Dynamic Route Optimization &amp; Exception",
            "trigger": "Schedule", "trigger_label": "Every 15 Min",
            "nodes": 12,
            "problem": "When weather or traffic incidents hit, dispatchers reroute drivers by hand and customers often hear nothing until a delivery is already late.",
            "built": "An agent that checks every active delivery against traffic and weather (mock data) every 15 minutes and has Claude decide whether the delay is significant. Express and time sensitive cargo has a lower threshold.",
            "solved": "For significant delays it picks an alternate route and new ETA, updates dispatch (mock), and emails the driver and the customer. On time deliveries are logged.",
            "workflow_steps": [
                {"label": "Every 15 Minutes", "type": "trigger"},
                {"label": "Fetch Deliveries (mock)", "type": "process"},
                {"label": "Traffic + Weather (mock)", "type": "process"},
                {"label": "Claude Delay Assessment", "type": "ai"},
                {"label": "Significant Delay?", "type": "decision", "branches": [
                    {"label": "Reroute + Notify", "type": "warn", "side_label": "Yes"},
                    {"label": "Log On-Time", "type": "ok", "side_label": "No"},
                ]},
            ],
            "dc": TR,
            "companies": [
                ("Parcel carriers", "reroute around corridor wide weather events"),
                ("Same day delivery", "correct ETAs before customers ask"),
                ("LTL carriers", "reduce customer service load during weather delays"),
            ],
            "n8n_url": "https://github.com/mythrip11/ai-agent-portfolio/blob/main/workflows/transportation/TR-5_dynamic-route-optimization.json",
        },
        {
            "id": "TR-6",
            "name": "Freight Exception &amp; Carrier Resolution",
            "trigger": "Schedule", "trigger_label": "Every Hour",
            "nodes": 13,
            "problem": "Freight teams triage a steady stream of shipment exceptions by hand, and high value or time critical cargo can be escalated too late.",
            "built": "An hourly agent that reads in transit shipments with exceptions (mock TMS data) and has Claude classify each as critical, standard, or low, using cargo value, delay, and SLA deadline.",
            "solved": "Critical exceptions open a mock case and email the account manager and the customer. Standard exceptions open a case and email the customer. Low severity exceptions are logged.",
            "workflow_steps": [
                {"label": "Hourly Scheduler", "type": "trigger"},
                {"label": "Fetch Exceptions (mock)", "type": "process"},
                {"label": "Claude Severity Class", "type": "ai"},
                {"label": "Exception Severity", "type": "decision", "branches": [
                    {"label": "Alert AM", "type": "warn", "side_label": "Critical"},
                    {"label": "Notify Customer", "type": "neutral", "side_label": "Standard"},
                    {"label": "Log Only", "type": "ok", "side_label": "Low"},
                ]},
            ],
            "dc": TR,
            "companies": [
                ("Freight brokers", "triage weather and carrier delay exceptions"),
                ("LTL carriers", "escalate high value exceptions to key account managers"),
                ("Shippers", "notify customers about critical B2B delivery problems"),
            ],
            "n8n_url": "https://github.com/mythrip11/ai-agent-portfolio/blob/main/workflows/transportation/TR-6_freight-exception-management.json",
        },
    ],
    "construction": [
        {
            "id": "C-7",
            "name": "Site Safety Compliance &amp; OSHA Reporting",
            "trigger": "Schedule", "trigger_label": "Daily at 7am",
            "nodes": 11,
            "problem": "Contractors collect many site inspection reports every day, and deciding which findings are OSHA reportable, filing them, and assigning corrective actions is manual and easy to delay.",
            "built": "A daily agent that reads inspection reports (mock data) and has Claude decide whether each finding is OSHA reportable, with the violation type, standard area, severity, and corrective actions.",
            "solved": "Reportable findings get a mock incident report and an alert email to the project manager. Minor findings are logged and the project manager is notified by email.",
            "workflow_steps": [
                {"label": "Daily Scheduler", "type": "trigger"},
                {"label": "Fetch Inspections (mock)", "type": "process"},
                {"label": "Claude OSHA Review", "type": "ai"},
                {"label": "OSHA Reportable?", "type": "decision", "branches": [
                    {"label": "File Report + Alert PM", "type": "warn", "side_label": "Yes"},
                    {"label": "Log + Notify PM", "type": "neutral", "side_label": "No"},
                ]},
            ],
            "dc": CN,
            "companies": [
                ("General contractors", "triage daily inspection findings across many sites"),
                ("Safety teams", "flag fall protection and excavation hazards for same day action"),
                ("Project platforms", "pull inspection data from a safety system and file reports"),
            ],
            "n8n_url": "https://github.com/mythrip11/ai-agent-portfolio/blob/main/workflows/construction/C-7_site-safety-osha-reporting.json",
        },
        {
            "id": "C-8",
            "name": "Subcontractor Invoice Reconciliation",
            "trigger": "Schedule", "trigger_label": "Weekly Monday",
            "nodes": 12,
            "problem": "Finance teams check subcontractor invoices against the contract Schedule of Values by hand, which is slow and lets overbilling and missing compliance documents slip through.",
            "built": "A weekly agent that reads pending invoices and matching contract data (mock ERP data) and has Claude compare billed progress to actual progress, check insurance and lien waivers, and calculate retainage.",
            "solved": "Approved invoices get a mock payment voucher with retainage withheld. Overbilled or incomplete invoices are flagged and the subcontractor is emailed each discrepancy.",
            "workflow_steps": [
                {"label": "Weekly Scheduler", "type": "trigger"},
                {"label": "Fetch Invoices (mock)", "type": "process"},
                {"label": "Fetch Contract SOV (mock)", "type": "process"},
                {"label": "Claude Reconciliation", "type": "ai"},
                {"label": "Approved?", "type": "decision", "branches": [
                    {"label": "Create Voucher", "type": "ok", "side_label": "Yes"},
                    {"label": "Flag + Notify Sub", "type": "warn", "side_label": "No"},
                ]},
            ],
            "dc": CN,
            "companies": [
                ("Construction finance", "reconcile pay applications against the contract"),
                ("Project controls", "catch overbilling before payment"),
                ("ERP integrations", "push approved vouchers to an accounting system"),
            ],
            "n8n_url": "https://github.com/mythrip11/ai-agent-portfolio/blob/main/workflows/construction/C-8_subcontractor-invoice-reconciliation.json",
        },
        {
            "id": "C-9",
            "name": "Material Procurement &amp; Supply Forecasting",
            "trigger": "Schedule", "trigger_label": "Daily at 6am",
            "nodes": 12,
            "problem": "Material shortages are often discovered only when a crew shows up and the material is not on site, which stalls work.",
            "built": "A daily agent that reads upcoming material needs per project, adds stock and supplier lead times (mock data), and has Claude decide which shortages are critical, meaning an order placed today would arrive late.",
            "solved": "Projects with a critical shortage get a mock purchase order and an alert email to the project manager. Fully covered projects are logged and get a daily summary email.",
            "workflow_steps": [
                {"label": "Daily Scheduler", "type": "trigger"},
                {"label": "Fetch Schedules + Stock (mock)", "type": "process"},
                {"label": "Claude Cross-Reference", "type": "ai"},
                {"label": "Critical Shortage?", "type": "decision", "branches": [
                    {"label": "Create POs + Alert PM", "type": "warn", "side_label": "Yes"},
                    {"label": "Daily Summary", "type": "ok", "side_label": "No"},
                ]},
            ],
            "dc": CN,
            "companies": [
                ("General contractors", "prevent steel and concrete shortages on fast moving projects"),
                ("Procurement teams", "run a daily check across every active project"),
                ("Project and ERP platforms", "pull schedules from one system and push orders to another"),
            ],
            "n8n_url": "https://github.com/mythrip11/ai-agent-portfolio/blob/main/workflows/construction/C-9_material-procurement-supply-forecasting.json",
        },
    ],
}

DOMAIN_META = {
    "healthcare": {
        "label": "Healthcare",
        "tag": "hc-tag", "ttl": "hc-ttl", "hdr": "hc-hdr",
        "id_cls": "hc-id", "dot": "hc-dot", "btn": "hc-btn", "val": "hc-val",
        "desc": "Three agents for patient discharge triage, insurance prior authorization, and clinical trial recruitment, built on n8n and Claude and tested with fictional data.",
    },
    "transportation": {
        "label": "Transportation",
        "tag": "tr-tag", "ttl": "tr-ttl", "hdr": "tr-hdr",
        "id_cls": "tr-id", "dot": "tr-dot", "btn": "tr-btn", "val": "tr-val",
        "desc": "Three agents that predict fleet maintenance needs, reroute deliveries around delays, and escalate freight exceptions by severity, built on n8n and Claude and tested with fictional data.",
    },
    "construction": {
        "label": "Construction",
        "tag": "cn-tag", "ttl": "cn-ttl", "hdr": "cn-hdr",
        "id_cls": "cn-id", "dot": "cn-dot", "btn": "cn-btn", "val": "cn-val",
        "desc": "Three agents for OSHA reportability review, subcontractor invoice reconciliation, and material shortage forecasting, built on n8n and Claude and tested with fictional data.",
    },
}


# ─── HTML BUILDERS ────────────────────────────────────────────────────────────

def esc(text: str) -> str:
    return (
        str(text)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def build_card(agent: dict, m: dict) -> str:
    svg = build_workflow_svg(agent["workflow_steps"], agent["dc"], agent["id"])

    companies_html = "".join(
        f'<div class="uc-row">'
        f'<div class="uc-dot {m["dot"]}"></div>'
        f'<div class="uc-txt"><span class="uc-co">{esc(co)}</span> &mdash; {esc(desc)}</div>'
        f'</div>'
        for co, desc in agent["companies"]
    )

    return (
        f'<div class="agent-card">'

        f'<div class="card-hdr {m["hdr"]}">'
        f'<div class="card-id {m["id_cls"]}">{esc(agent["id"])}</div>'
        f'<div class="card-name">{agent["name"]}</div>'
        f'<span class="trigger-pill"><span class="t-dot"></span>'
        f'{esc(agent["trigger"])} &middot; {esc(agent["trigger_label"])}</span>'
        f'</div>'

        f'<div class="card-body">'

        f'<div class="xyz-row"><span class="xyz-lbl lp">Problem</span>'
        f'<span class="xyz-txt">{esc(agent["problem"])}</span></div>'
        f'<div class="xyz-row"><span class="xyz-lbl lb">Built</span>'
        f'<span class="xyz-txt">{esc(agent["built"])}</span></div>'
        f'<div class="xyz-row"><span class="xyz-lbl ls">Outcome</span>'
        f'<span class="xyz-txt">{esc(agent["solved"])}</span></div>'

        f'<div class="card-div"></div>'

        f'<div class="wf-label">How It Works</div>'
        f'{svg}'

        f'<div class="wf-label">n8n Canvas</div>'
        f'<img class="shot" src="https://raw.githubusercontent.com/mythrip11/ai-agent-portfolio/main/screenshots/{esc(agent["id"])}.png" alt="{esc(agent["id"])} workflow in n8n" />'

        f'<div class="uc-title">Where This Pattern Applies</div>'
        f'{companies_html}'

        f'<div class="metrics-row">'
        f'<div class="m-chip"><span class="m-val">{esc(str(agent["nodes"]))}</span>nodes</div>'
        f'<div class="m-chip"><span class="m-val {m["val"]}">&#10003;</span>tested, fictional data</div>'
        f'</div>'

        f'<a class="n8n-btn {m["btn"]}" href="{esc(agent["n8n_url"])}" target="_blank">'
        f'View Workflow on GitHub &#8594;</a>'

        f'</div>'
        f'</div>'
    )


def render_domain(domain_key: str):
    m = DOMAIN_META[domain_key]
    agents = AGENTS[domain_key]
    cards_html = "".join(build_card(a, m) for a in agents)

    html = (
        f'<div class="domain-wrap">'
        f'<div class="domain-tag {m["tag"]}">{esc(m["label"])}</div>'
        f'<div class="domain-title {m["ttl"]}">{esc(m["label"])} AI Agents</div>'
        f'<div class="domain-desc">{esc(m["desc"])}</div>'
        f'<div class="agents-grid">{cards_html}</div>'
        f'</div>'
    )
    st.markdown(html, unsafe_allow_html=True)


# ─── PROFILE BAR ──────────────────────────────────────────────────────────────

st.markdown(
    '<div class="profile-bar">'

    # Left — name + subtitle + badge
    '<div class="profile-left">'
    '<div class="profile-name">MYTHRI POTLURI</div>'
    '<div class="profile-title-tag">'
    'Workflow Automation'
    '<span class="sep">|</span>'
    '&#128205; New York City, New York'
    '<span class="sep">|</span>'
    '<span class="available-badge"><span class="av-dot"></span>Open to Opportunities</span>'
    '</div>'
    '</div>'

    # Right — contact links
    '<div class="profile-links">'
    '<a class="p-link p-link-li" href="https://www.linkedin.com/in/mythripotluri1/" target="_blank">'
    '&#128101; LinkedIn'
    '</a>'
    '<a class="p-link p-link-gh" href="https://github.com/mythrip11" target="_blank">'
    '&#9670; GitHub'
    '</a>'
    '<a class="p-link p-link-pf" href="https://mythri-portfolio-cyan.vercel.app/" target="_blank">'
    '&#9632; Portfolio'
    '</a>'
    '<a class="p-link p-link-em" href="mailto:mythrip11@gmail.com">'
    '&#9993; Email'
    '</a>'
    '</div>'

    '</div>',
    unsafe_allow_html=True,
)


# ─── HERO ─────────────────────────────────────────────────────────────────────

st.markdown(
    '<div class="hero-wrap">'
    '<div class="hero-badge">n8n &middot; Claude &middot; Tested with Fictional Data</div>'
    '<div class="hero-title">AI Agent Portfolio</div>'

    # Catchy recruiter summary
    '<div class="hero-summary-wrap">'
    '<div class="hero-summary-eyebrow">About This Portfolio</div>'
    '<div class="hero-summary-text">'
    'Every workflow here was built and run end to end in n8n, using fictional data and mock source systems. '
    'They bring AI into <strong>healthcare, logistics, and construction</strong>, '
    'industries where automation still feels foreign and the wins are massive.'
    '</div>'
    '</div>'

    '<div class="tech-badges">'
    '<span class="tech-badge"><span class="tb-dot" style="background:#6366F1"></span>n8n</span>'
    '<span class="tech-badge"><span class="tb-dot" style="background:#10B981"></span>Claude</span>'
    '<span class="tech-badge"><span class="tb-dot" style="background:#F97316"></span>Gmail</span>'
    '<span class="tech-badge"><span class="tb-dot" style="background:#8B5CF6"></span>Webhook + Schedule</span>'
    '</div>'
    '<div class="hero-stats">'
    '<div class="stat-box">'
    '<span class="stat-num" style="background:linear-gradient(135deg,#fff,#A5B4FC);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;">9</span>'
    '<span class="stat-lbl">AI Agents</span>'
    '</div>'
    '<div class="stat-box">'
    '<span class="stat-num" style="background:linear-gradient(135deg,#fff,#67E8F9);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;">3</span>'
    '<span class="stat-lbl">Industries</span>'
    '</div>'
    '<div class="stat-box">'
    '<span class="stat-num" style="background:linear-gradient(135deg,#fff,#86EFAC);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;">Claude</span>'
    '<span class="stat-lbl">Powered</span>'
    '</div>'
    '</div>'
    '</div>',
    unsafe_allow_html=True,
)


# ─── TABS ─────────────────────────────────────────────────────────────────────

tab_hc, tab_tr, tab_cn = st.tabs([
    "  Healthcare  ",
    "  Transportation  ",
    "  Construction  ",
])

with tab_hc:
    render_domain("healthcare")

with tab_tr:
    render_domain("transportation")

with tab_cn:
    render_domain("construction")


# ─── FOOTER ───────────────────────────────────────────────────────────────────

st.markdown(
    '<div class="portfolio-footer">'
    '<div class="footer-repos">'
    '<a class="repo-link" href="https://github.com/mythrip11/ai-agent-portfolio/tree/main/workflows/healthcare" target="_blank">workflows/healthcare</a>'
    '<a class="repo-link" href="https://github.com/mythrip11/ai-agent-portfolio/tree/main/workflows/transportation" target="_blank">workflows/transportation</a>'
    '<a class="repo-link" href="https://github.com/mythrip11/ai-agent-portfolio/tree/main/workflows/construction" target="_blank">workflows/construction</a>'
    '<a class="repo-link" href="https://github.com/mythrip11/ai-agent-portfolio" target="_blank">github/ai-agent-portfolio</a>'
    '</div>'
    '<div class="footer-credit">'
    'Built by <a href="https://mythri-portfolio-cyan.vercel.app/" target="_blank">Mythri Potluri</a>'
    ' &nbsp;&middot;&nbsp; New York City, NY &nbsp;&middot;&nbsp; '
    '<a href="mailto:mythrip11@gmail.com">mythrip11@gmail.com</a>'
    ' &nbsp;&middot;&nbsp; n8n + Claude &nbsp;&middot;&nbsp; '
    'Built with <a href="https://n8n.io" target="_blank">n8n</a>'
    '</div>'
    '</div>',
    unsafe_allow_html=True,
)
