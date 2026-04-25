#!/usr/bin/env python3
"""
Raviteja Palanki — AI Product Leader Resume v16
DEFINITIVE BUILD — Fresh from v15 base with ALL consolidated feedback.

Font: Lato (Google Font, professional, full Unicode)
Paper: A4 (Indian standard, taller = more breathing room)
Design: Apple-level spacing, balanced columns, pixel-perfect
"""

import sys
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ━━━ FONT REGISTRATION ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FDIR = "/usr/share/fonts/truetype/lato/"
pdfmetrics.registerFont(TTFont("Lato",   FDIR + "Lato-Regular.ttf"))
pdfmetrics.registerFont(TTFont("LatoB",  FDIR + "Lato-Bold.ttf"))
pdfmetrics.registerFont(TTFont("LatoI",  FDIR + "Lato-Italic.ttf"))
pdfmetrics.registerFont(TTFont("LatoSB", FDIR + "Lato-Semibold.ttf"))
pdfmetrics.registerFont(TTFont("LatoL",  FDIR + "Lato-Light.ttf"))

F    = "Lato"       # Regular
FB   = "LatoB"      # Bold
FI   = "LatoI"      # Italic
FSB  = "LatoSB"     # Semibold
FL   = "LatoL"      # Light

# ━━━ COLOUR PALETTE (v15 matched, Salesforce fixed) ━━━━━━━━━━━━━━━━━━━━━━━━
DEEP_TEAL      = HexColor("#1B5E5E")
MID_TEAL       = HexColor("#237878")
LIGHT_TEAL_BG  = HexColor("#ECF6F6")
BLACK          = HexColor("#1A1A1A")
DARK_GRAY      = HexColor("#2D2D2D")
MID_GRAY       = HexColor("#5A5A5A")
LIGHT_GRAY     = HexColor("#999999")
RULE_COLOR     = HexColor("#D0D0D0")
TAG_TEXT       = HexColor("#1B5E5E")
WHITE          = HexColor("#FFFFFF")

# Badge colours
BADGE_TEAL     = HexColor("#1B5E5E")    # Perplexity
BADGE_GOLD     = HexColor("#C9962A")    # Lovable
BADGE_BLUE     = HexColor("#0176D3")    # Salesforce (brand blue, NOT red)
GOLD_BG        = HexColor("#FFF5E0")
GOLD_TEXT      = HexColor("#8B6914")
PRO_BG         = HexColor("#E4F0F0")
PRO_TEXT       = MID_TEAL
MAX_BG         = GOLD_BG
MAX_TEXT       = GOLD_TEXT

# ━━━ PAGE LAYOUT (A4) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
W, H    = A4                    # 595.28 × 841.89 pt
ML      = 42                    # margin left
MR      = 42                    # margin right
MT      = 36                    # margin top
MB      = 28                    # margin bottom
CW      = W - ML - MR           # ~511 content width

LEFT_W  = 312                   # left column width
GAP     = 17                    # column gap
RIGHT_W = CW - LEFT_W - GAP    # ~182 right column width
RIGHT_X = ML + LEFT_W + GAP    # right column x start

FOOTER_Y = MB + 4


# ━━━ DRAWING HELPERS ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def rrect(c, x, y, w, h, r, fill=None, stroke=None, sw=0.5):
    p = c.beginPath()
    p.roundRect(x, y, w, h, r)
    if fill:
        c.setFillColor(fill)
    if stroke:
        c.setStrokeColor(stroke)
        c.setLineWidth(sw)
    c.drawPath(p, fill=1 if fill else 0, stroke=1 if stroke else 0)


def bullet_dot(c, x, y, r=1.2):
    """Small filled teal circle bullet."""
    c.setFillColor(MID_TEAL)
    c.circle(x + r, y + 2, r, fill=1, stroke=0)


def tag(c, x, y, text, fs=5.8, bg=LIGHT_TEAL_BG, tc=TAG_TEXT):
    c.setFont(F, fs)
    tw = c.stringWidth(text, F, fs)
    px, py = 5.5, 2.5
    w, h = tw + px * 2, fs + py * 2
    rrect(c, x, y - py - 0.5, w, h, 3, fill=bg)
    c.setFillColor(tc)
    c.drawString(x + px, y, text)
    return w


def badge(c, x, y, text, bg, fs=6.8):
    c.setFont(FB, fs)
    tw = c.stringWidth(text, FB, fs)
    px, py = 8, 3.5
    w = tw + px * 2
    h = fs + py * 2
    rrect(c, x, y - py - 1, w, h, 4, fill=bg)
    c.setFillColor(WHITE)
    c.drawString(x + px, y, text)
    return w


def sec_hdr(c, x, y, text, line_w=None):
    c.setFont(FB, 10)
    c.setFillColor(DEEP_TEAL)
    c.drawString(x, y, text)
    lw = line_w or (c.stringWidth(text, FB, 10) + 2)
    c.setStrokeColor(DEEP_TEAL)
    c.setLineWidth(1.0)
    c.line(x, y - 4, x + lw, y - 4)
    return y - 18


def rsec_hdr(c, x, y, text):
    c.setFont(FB, 8.5)
    c.setFillColor(DEEP_TEAL)
    c.drawString(x, y, text)
    tw = c.stringWidth(text, FB, 8.5)
    c.setStrokeColor(DEEP_TEAL)
    c.setLineWidth(0.8)
    c.line(x, y - 3.5, x + tw + 2, y - 3.5)
    return y - 15


def wrap(c, text, font, fs, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if c.stringWidth(t, font, fs) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_bullet(c, x, y, text, max_w, fs=6.8, ld=9.2, color=DARK_GRAY):
    indent = 11
    bullet_dot(c, x + 1, y)
    lines = wrap(c, text, F, fs, max_w - indent)
    c.setFont(F, fs)
    c.setFillColor(color)
    for line in lines:
        c.drawString(x + indent, y, line)
        y -= ld
    return y


def draw_link(c, x, y, text, url, fs=5.8):
    """Small teal link with ↗ prefix."""
    c.setFont(F, fs)
    c.setFillColor(MID_TEAL)
    full = "\u2197 " + text
    c.drawString(x, y, full)
    tw = c.stringWidth(full, F, fs)
    aw = c.stringWidth("\u2197 ", F, fs)
    c.setStrokeColor(MID_TEAL)
    c.setLineWidth(0.3)
    c.line(x + aw, y - 1, x + tw, y - 1)
    c.linkURL(url, (x, y - 2, x + tw, y + fs + 1), relative=0)
    return tw


def links_row(c, x, y, links, fs=5.8, gap=9):
    lx = x
    for text, url in links:
        tw = draw_link(c, lx, y, text, url, fs=fs)
        lx += tw + gap
    return y - 11


# ━━━ URLS (ALL CORRECTED) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
URL_TRACKWISE   = "https://www.spartasystems.com/trackwise/"
URL_DMS         = "https://www.spartasystems.com/document-management-software/"
URL_TMS         = "https://www.spartasystems.com/training-management-software/"
URL_EU_MIR      = "https://www.spartasystems.com/post-market-surveillance/"
URL_BAT_PROD    = "https://process.honeywell.com/us/en/industries/sheet-manufacturing/lithium-ion-batteries"
URL_PI_PROD     = "https://www.honeywellforge.ai/us/en/products/industrial-operations/honeywell-forge-performance-plus-for-industrials-production-intelligence"
URL_WA_PROD     = "https://automation.honeywell.com/content/process/us/en/solutions/honeywell-forge/honeywell-forge-worker-assist.html"
URL_WA_APP      = "https://apps.apple.com/in/app/honeywell-forge-worker-assist/id1555134286?platform=iphone"
URL_BRILLIO     = "https://www.brillio.com"
URL_BRILLIO_PE  = "https://www.brillio.com/services/product-and-platform-engineering/"
URL_GITHUB      = "https://github.com/raviteja-palanki/rtp-personal-skills"
URL_PP          = "https://productpatterns.in"
URL_PP_GITHUB   = "https://github.com/raviteja-palanki/Patterns"
URL_LEARN       = "https://learn.ravitejapalanki.com"
URL_SUBSTACK    = "https://ravitejapalanki.substack.com"
URL_LINKEDIN    = "https://www.linkedin.com/in/ravipalanki/"
URL_WEBSITE     = "https://ravitejapalanki.com"
URL_TAPMI_AI    = "https://www.tapmi.edu.in/mba-ai/"
URL_LADC        = "https://www.tapmi.edu.in/ladc/"
URL_PROFILE     = "https://ravitejapalanki.com/profile"


# ━━━ MAIN BUILD ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def build(output_path=None):
    if output_path is None:
        output_path = os.environ.get("RESUME_OUTPUT_PATH", "Raviteja_Palanki_AI_PM_Resume.pdf")
    out = output_path
    c = canvas.Canvas(out, pagesize=A4)
    c.setTitle("Raviteja Palanki \u2014 AI Product Leader")
    c.setAuthor("Raviteja Palanki")

    y = H - MT

    # ═══════════════════════════════════════════════════════════════════════════
    # HEADER
    # ═══════════════════════════════════════════════════════════════════════════

    c.setFont(FB, 24)
    c.setFillColor(BLACK)
    c.drawString(ML, y, "Raviteja Palanki")

    c.setFont(F, 7.5)
    c.setFillColor(MID_GRAY)
    c.drawRightString(W - MR, y + 2, "+91-7026334917")
    c.drawRightString(W - MR, y - 10, "ravi.carpediem7@gmail.com")
    c.drawRightString(W - MR, y - 22, "Bangalore, India")
    y -= 17

    c.setFont(FI, 10.5)
    c.setFillColor(MID_TEAL)
    c.drawString(ML, y, "AI Product Leader")
    y -= 16

    c.setFont(F, 8)
    c.setFillColor(DARK_GRAY)
    c.drawString(ML, y,
        "Ships Reliable, Human-Centered AI Products at Scale  \u00b7  0-to-1 Builder  \u00b7  12+ Years Enterprise B2B")
    y -= 18

    bx = ML
    bx += badge(c, bx, y, "Perplexity AI Business Fellow 2025", BADGE_TEAL) + 7
    bx += badge(c, bx, y, "Lovable L4 Platinum Builder", BADGE_GOLD) + 7
    badge(c, bx, y, "Salesforce Agentforce Specialist", BADGE_BLUE)
    y -= 18

    lx = ML
    tw = draw_link(c, lx, y, "My LinkedIn", URL_LINKEDIN, fs=7.2)
    lx += tw + 16
    draw_link(c, lx, y, "My Website", URL_WEBSITE, fs=7.2)
    y -= 14

    c.setStrokeColor(RULE_COLOR)
    c.setLineWidth(0.4)
    c.line(ML, y, W - MR, y)
    y -= 12

    # ═══════════════════════════════════════════════════════════════════════════
    # PROFILE
    # ═══════════════════════════════════════════════════════════════════════════

    profile = [
        "12+ years building and shipping enterprise B2B products across industrial, life sciences, and energy verticals at Fortune 100 scale.",
        "From 0-to-1 products to scaling adoption globally.",
        "Technical depth in AI: shipped Gen AI products (RAG, LLMs, context engineering), built full-stack apps, and designed for decision velocity at enterprise scale.",
    ]
    for p in profile:
        y = draw_bullet(c, ML, y, p, CW, fs=7.5, ld=10, color=DARK_GRAY)
        y -= 2
    y -= 3

    c.setFont(FB, 7.5)
    c.setFillColor(BLACK)
    c.drawString(ML, y, "Advisory Board Member")
    aw = c.stringWidth("Advisory Board Member", FB, 7.5)
    c.setFont(F, 7.5)
    c.setFillColor(DARK_GRAY)
    mid = " \u2014 MBA in AI at TAPMI (alma mater)    "
    c.drawString(ML + aw, y, mid)
    mx = ML + aw + c.stringWidth(mid, F, 7.5)
    draw_link(c, mx, y, "TAPMI Programme", URL_TAPMI_AI, fs=7)
    y -= 14

    c.setStrokeColor(RULE_COLOR)
    c.setLineWidth(0.4)
    c.line(ML, y, W - MR, y)
    y -= 14

    # ═══════════════════════════════════════════════════════════════════════════
    # TWO-COLUMN LAYOUT
    # ═══════════════════════════════════════════════════════════════════════════

    col_top = y
    ly = col_top
    ry = col_top

    # ───────────────────────────────────────────────────────────────────────────
    # LEFT COLUMN: EXPERIENCE
    # ───────────────────────────────────────────────────────────────────────────

    ly = sec_hdr(c, ML, ly, "EXPERIENCE", LEFT_W)

    # ─── HONEYWELL ────────────────────────────────────────────────────────────
    c.setFont(FB, 9.5)
    c.setFillColor(BLACK)
    c.drawString(ML, ly, "HONEYWELL")
    hw = c.stringWidth("HONEYWELL  ", FB, 9.5)
    c.setFont(F, 7.5)
    c.setFillColor(MID_GRAY)
    c.drawString(ML + hw, ly + 0.5, "2021 \u2013 Present")
    ly -= 12
    c.setFont(F, 7)
    c.setFillColor(DARK_GRAY)
    c.drawString(ML, ly, "Sr. Technical PM  |  Led 5+ Enterprise B2B Products  |  200+ Customers")
    ly -= 16

    # --- TrackWise Digital ---
    c.setFont(FB, 8)
    c.setFillColor(BLACK)
    c.drawString(ML, ly, "TrackWise Digital \u2014 Life Sciences")
    ttw = c.stringWidth("TrackWise Digital \u2014 Life Sciences  ", FB, 8)
    c.setFont(F, 7)
    c.setFillColor(MID_GRAY)
    c.drawString(ML + ttw, ly + 0.5, "2025\u2013Present")
    dend = ML + ttw + c.stringWidth("2025\u2013Present  ", F, 7) + 5
    tag(c, dend, ly - 0.5, "Salesforce")
    ly -= 10
    c.setFont(FI, 6.5)
    c.setFillColor(MID_GRAY)
    c.drawString(ML, ly, "Honeywell Connected Life Sciences (HCLS)")
    ly -= 12

    for b in [
        "Document Management System: Enterprise document lifecycle & audit readiness for global pharma",
        "Training Management System: Compliance training for regulated teams",
        "EU Manufacturer Incident Report (MIR): Post-market surveillance for global pharma \u2014 AI-assisted analysis and faster delivery turnarounds for meeting regulatory updates",
    ]:
        ly = draw_bullet(c, ML, ly, b, LEFT_W)
        ly -= 2

    ly = links_row(c, ML + 4, ly, [
        ("DMS", URL_DMS), ("TMS", URL_TMS),
        ("EU MIR", URL_EU_MIR), ("TrackWise", URL_TRACKWISE),
    ])
    ly -= 8

    # --- Battery MXP ---
    c.setFont(FB, 8)
    c.setFillColor(BLACK)
    c.drawString(ML, ly, "Battery MXP \u2014 Manufacturing Execution System (MES)")
    ttw = c.stringWidth("Battery MXP \u2014 Manufacturing Execution System (MES)  ", FB, 8)
    c.setFont(F, 7)
    c.setFillColor(MID_GRAY)
    c.drawString(ML + ttw, ly + 0.5, "2023\u20132025")
    ly -= 10
    c.setFont(FI, 6.5)
    c.setFillColor(MID_GRAY)
    c.drawString(ML, ly, "Honeywell Connected Industrial (HCI)")
    org_end = ML + c.stringWidth("Honeywell Connected Industrial (HCI)   ", FI, 6.5) + 4
    tag(c, org_end, ly - 1, "Battery Manufacturing")
    ly -= 12

    for b in [
        "Built 0-to-1 MES for battery gigafactories \u2014 $100M+ revenue opportunity",
        "Orchestrated first alpha from HCI group in 15 months | Team filed 2 patents with Honeywell Fellows",
    ]:
        ly = draw_bullet(c, ML, ly, b, LEFT_W)
        ly -= 2

    ly = links_row(c, ML + 4, ly, [
        ("Press Release", URL_BAT_PROD), ("Product Page", URL_BAT_PROD),
    ])
    ly -= 8

    # --- Production Intelligence ---
    c.setFont(FB, 8)
    c.setFillColor(BLACK)
    c.drawString(ML, ly, "Production Intelligence \u2014 Gen AI")
    ttw = c.stringWidth("Production Intelligence \u2014 Gen AI  ", FB, 8)
    c.setFont(F, 7)
    c.setFillColor(MID_GRAY)
    c.drawString(ML + ttw, ly + 0.5, "2022\u20132024")
    dend = ML + ttw + c.stringWidth("2022\u20132024  ", F, 7) + 5
    tag(c, dend, ly - 0.5, "Azure AI Foundry")
    ly -= 10
    c.setFont(FI, 6.5)
    c.setFillColor(MID_GRAY)
    c.drawString(ML, ly, "Honeywell Connected Industrial (HCI)")
    ly -= 12

    ly = draw_bullet(c, ML, ly,
        "Shipped enterprise AI assistant (OpenAI APIs, React, multi-DB RAG) for Plant Managers, Operators & Supervisors \u2014 designed hallucination guardrails and eval frameworks for response accuracy in safety-critical industrial operations",
        LEFT_W)
    ly -= 2
    ly = draw_bullet(c, ML, ly,
        "Early mover in industrial Gen AI | 40% adoption lift | 30% faster decisions \u2014 championed Responsible AI by design for regulated environments",
        LEFT_W)
    ly -= 2

    ly = links_row(c, ML + 4, ly, [
        ("Press Release", URL_PI_PROD), ("Product Page", URL_PI_PROD),
    ])
    ly -= 8

    # --- Worker Assist ---
    c.setFont(FB, 8)
    c.setFillColor(BLACK)
    c.drawString(ML, ly, "Worker Assist \u2014 Connected Worker")
    ttw = c.stringWidth("Worker Assist \u2014 Connected Worker  ", FB, 8)
    c.setFont(F, 7)
    c.setFillColor(MID_GRAY)
    c.drawString(ML + ttw, ly + 0.5, "2021\u20132022")
    dend = ML + ttw + c.stringWidth("2021\u20132022  ", F, 7) + 5
    tag(c, dend, ly - 0.5, "React + .NET")
    ly -= 10
    c.setFont(FI, 6.5)
    c.setFillColor(MID_GRAY)
    c.drawString(ML, ly, "Honeywell Connected Industrial (HCI)")
    ly -= 12

    for b in [
        "Solo PM coordinating 30+ cross-functional stakeholders",
        "Android \u00b7 iOS \u00b7 Realwear \u00b7 Web App \u2014 shipped across all modalities",
        "5 releases in 12 months | 5x user adoption growth (500 \u2192 2,500 industrial users)",
    ]:
        ly = draw_bullet(c, ML, ly, b, LEFT_W)
        ly -= 2

    ly = links_row(c, ML + 4, ly, [
        ("Product Page", URL_WA_PROD), ("App Store", URL_WA_APP),
    ])
    ly -= 10

    # ─── BRILLIO ──────────────────────────────────────────────────────────────
    c.setFont(FB, 9.5)
    c.setFillColor(BLACK)
    c.drawString(ML, ly, "BRILLIO")
    hw = c.stringWidth("BRILLIO  ", FB, 9.5)
    c.setFont(F, 7.5)
    c.setFillColor(MID_GRAY)
    c.drawString(ML + hw, ly + 0.5, "2016\u20132021")
    ly -= 12
    c.setFont(F, 7)
    c.setFillColor(DARK_GRAY)
    c.drawString(ML, ly, "Lead Product Owner, Product Engineering")
    ly -= 12

    for b in [
        "Led modernization of 5+ legacy enterprise apps to Azure Cloud SaaS (Sempra Energy) | Led 3 scrum teams (20+)",
        "Pre-Sales Lead (For Product Engg. Service Line): 85% win ratio | Contributed to 15% company revenue growth",
    ]:
        ly = draw_bullet(c, ML, ly, b, LEFT_W)
        ly -= 2

    ly = links_row(c, ML + 4, ly, [
        ("brillio.com", URL_BRILLIO), ("Product Engineering", URL_BRILLIO_PE),
    ])
    ly -= 10

    # ─── TATA MOTORS ──────────────────────────────────────────────────────────
    c.setFont(FB, 9.5)
    c.setFillColor(BLACK)
    c.drawString(ML, ly, "TATA MOTORS")
    hw = c.stringWidth("TATA MOTORS  ", FB, 9.5)
    c.setFont(F, 7.5)
    c.setFillColor(MID_GRAY)
    c.drawString(ML + hw, ly + 0.5, "2012\u20132014")
    ly -= 12
    c.setFont(F, 7)
    c.setFillColor(DARK_GRAY)
    c.drawString(ML, ly, "Assistant Manager, Engine Factory")
    ly -= 12

    for b in [
        "Youngest floor manager: scaled robotic production to World Class Quality",
        "Reduced defect complaints 20% in 3 months",
    ]:
        ly = draw_bullet(c, ML, ly, b, LEFT_W)
        ly -= 2

    left_end = ly

    # ───────────────────────────────────────────────────────────────────────────
    # RIGHT COLUMN
    # ───────────────────────────────────────────────────────────────────────────

    # ─── AI PORTFOLIO ─────────────────────────────────────────────────────────
    ry = rsec_hdr(c, RIGHT_X, ry, "AI PORTFOLIO")

    # Claude Cowork Skills
    c.setFont(FB, 7)
    c.setFillColor(BLACK)
    c.drawString(RIGHT_X, ry, "Claude Cowork Skills")
    ry -= 9.5
    desc_lines = [
        "66 custom skills for AI PM workflows \u2014 a composable",
        "operating system with 3 layers (Thinking \u2192 Judgment",
        "\u2192 Craft), 5 plugins, and a self-correcting orchestrator.",
        "Built as an installable Claude plugin.",
    ]
    for line in desc_lines:
        c.setFont(F, 6.2)
        c.setFillColor(MID_GRAY)
        c.drawString(RIGHT_X, ry, line)
        ry -= 8
    draw_link(c, RIGHT_X, ry, "GitHub", URL_GITHUB, fs=5.8)
    ry -= 16

    # Product Patterns (two links: website + GitHub)
    c.setFont(FB, 7)
    c.setFillColor(BLACK)
    c.drawString(RIGHT_X, ry, "Product Patterns")
    ry -= 9.5
    for line in wrap(c, "RAG + knowledge graph product with LLM evals built in", F, 6.2, RIGHT_W):
        c.setFont(F, 6.2)
        c.setFillColor(MID_GRAY)
        c.drawString(RIGHT_X, ry, line)
        ry -= 8
    lxp = RIGHT_X
    tw = draw_link(c, lxp, ry, "productpatterns.in", URL_PP, fs=5.8)
    lxp += tw + 5
    draw_link(c, lxp, ry, "GitHub", URL_PP_GITHUB, fs=5.8)
    ry -= 16

    # AI Learning (special: 2 links)
    c.setFont(FB, 7)
    c.setFillColor(BLACK)
    c.drawString(RIGHT_X, ry, "AI Learning")
    ry -= 9.5
    for line in wrap(c, "Sharing AI knowledge publicly \u2014 frameworks, lessons, and insights", F, 6.2, RIGHT_W):
        c.setFont(F, 6.2)
        c.setFillColor(MID_GRAY)
        c.drawString(RIGHT_X, ry, line)
        ry -= 8
    lx2 = RIGHT_X
    tw = draw_link(c, lx2, ry, "learn.ravitejapalanki.com", URL_LEARN, fs=5.8)
    lx2 += tw + 5
    draw_link(c, lx2, ry, "Substack", URL_SUBSTACK, fs=5.8)
    ry -= 24

    # ─── TOOL STACK ───────────────────────────────────────────────────────────
    ry = rsec_hdr(c, RIGHT_X, ry, "TOOL STACK")

    tools = [
        [("Claude", "PRO"), ("Perplexity", "MAX")],
        [("NotebookLM", "PRO"), ("Lovable", "PRO"), ("Gamma", None)],
        [("N8N", None), ("Emergent", None), ("Notion AI", None), ("MS Copilot", None)],
        [("JIRA", None), ("Confluence", None), ("Azure", None)],
    ]
    for row in tools:
        tx = RIGHT_X
        for name, lbl in row:
            c.setFont(F, 6)
            c.setFillColor(DARK_GRAY)
            c.drawString(tx, ry, name)
            tx += c.stringWidth(name, F, 6) + 2
            if lbl:
                c.setFont(FB, 4.5)
                bw = c.stringWidth(lbl, FB, 4.5)
                pad = 2.5
                bg = PRO_BG if lbl == "PRO" else MAX_BG
                tc = PRO_TEXT if lbl == "PRO" else MAX_TEXT
                rrect(c, tx, ry - 1.5, bw + pad * 2, 7, 2, fill=bg)
                c.setFillColor(tc)
                c.drawString(tx + pad, ry, lbl)
                tx += bw + pad * 2 + 5
            else:
                tx += 6
        ry -= 12
    ry -= 12

    # ─── COMPETENCIES ─────────────────────────────────────────────────────────
    ry = rsec_hdr(c, RIGHT_X, ry, "COMPETENCIES")

    comps = [
        "Cross-functional Leadership",
        "Large Language Models",
        "RAG & Context Engineering",
        "Prompt Engineering",
        "Eval Frameworks",
        "Human-in-the-Loop",
        "Responsible AI",
        "AI User Experience",
        "0-to-1 Product Strategy",
        "AI Product Strategy & Roadmaps",
        "Enterprise B2B SaaS",
        "Agile at Scale \u00b7 SAFe",
    ]
    cx = RIGHT_X
    for comp in comps:
        c.setFont(F, 5.6)
        tw = c.stringWidth(comp, F, 5.6) + 10
        if cx + tw > RIGHT_X + RIGHT_W:
            cx = RIGHT_X
            ry -= 13
        tag(c, cx, ry, comp, fs=5.6)
        cx += tw + 3
    ry -= 24

    # ─── CERTIFICATIONS ───────────────────────────────────────────────────────
    ry = rsec_hdr(c, RIGHT_X, ry, "CERTIFICATIONS")

    for cert in [
        "Salesforce Agentforce Specialist",
        "SAFe\u00ae Product Owner / Product Manager",
        "SAFe\u00ae Agilist",
        "Professional Scrum Product Owner\u2122",
        "Marshall Goldsmith Coaching Collection",
    ]:
        c.setFont(F, 6.2)
        c.setFillColor(MID_GRAY)
        c.drawString(RIGHT_X, ry, "\u00b7")
        c.setFillColor(DARK_GRAY)
        c.drawString(RIGHT_X + 6, ry, cert)
        ry -= 11
    ry -= 12

    # ─── EDUCATION ────────────────────────────────────────────────────────────
    ry = rsec_hdr(c, RIGHT_X, ry, "EDUCATION")

    # TAPMI
    c.setFont(FB, 7)
    c.setFillColor(BLACK)
    c.drawString(RIGHT_X, ry, "T.A. Pai Mgmt. Institute (TAPMI)")
    ry -= 10
    c.setFont(F, 6.5)
    c.setFillColor(DARK_GRAY)
    c.drawString(RIGHT_X, ry, "MBA \u2014 Marketing & Finance")
    mw = c.stringWidth("MBA \u2014 Marketing & Finance  ", F, 6.5)
    c.setFont(F, 5.8)
    c.setFillColor(MID_GRAY)
    c.drawString(RIGHT_X + mw, ry, "(Top 25 MBA, India)")
    ry -= 10

    # LADC achievement with inline link
    c.setFont(F, 6.2)
    c.setFillColor(DARK_GRAY)
    prefix = "Led the setup of a pioneering "
    c.drawString(RIGHT_X, ry, prefix)
    px = RIGHT_X + c.stringWidth(prefix, F, 6.2)
    c.setFillColor(MID_TEAL)
    lt1 = "Leadership Advisory"
    c.drawString(px, ry, lt1)
    lt1w = c.stringWidth(lt1, F, 6.2)
    c.setStrokeColor(MID_TEAL)
    c.setLineWidth(0.3)
    c.line(px, ry - 1, px + lt1w, ry - 1)
    ry -= 8.5
    lt2 = "Development Centre"
    c.setFillColor(MID_TEAL)
    c.setFont(F, 6.2)
    c.drawString(RIGHT_X, ry, lt2)
    lt2w = c.stringWidth(lt2, F, 6.2)
    c.line(RIGHT_X, ry - 1, RIGHT_X + lt2w, ry - 1)
    c.setFillColor(DARK_GRAY)
    c.drawString(RIGHT_X + lt2w, ry, " at TAPMI")
    c.linkURL(URL_LADC, (RIGHT_X, ry - 2, RIGHT_X + RIGHT_W, ry + 18), relative=0)
    ry -= 16

    # NIT
    c.setFont(FB, 7)
    c.setFillColor(BLACK)
    c.drawString(RIGHT_X, ry, "NIT Jamshedpur")
    ry -= 10
    c.setFont(F, 6.5)
    c.setFillColor(DARK_GRAY)
    c.drawString(RIGHT_X, ry, "B.Tech (Hons.) \u2014 EEE")
    btw = c.stringWidth("B.Tech (Hons.) \u2014 EEE  ", F, 6.5)
    c.setFont(F, 5.8)
    c.setFillColor(MID_GRAY)
    c.drawString(RIGHT_X + btw, ry, "(Top 15 Engineering, India)")

    right_end = ry

    # ═══════════════════════════════════════════════════════════════════════════
    # FOOTER
    # ═══════════════════════════════════════════════════════════════════════════
    c.setFont(F, 6)
    c.setFillColor(LIGHT_GRAY)
    c.drawString(ML, FOOTER_Y, "Ravi Teja Palanki")
    c.setFillColor(MID_TEAL)
    ft = "ravitejapalanki.com/profile"
    c.drawRightString(W - MR, FOOTER_Y, ft)
    fw = c.stringWidth(ft, F, 6)
    c.linkURL(URL_PROFILE, (W - MR - fw, FOOTER_Y - 2, W - MR, FOOTER_Y + 7), relative=0)

    # ═══════════════════════════════════════════════════════════════════════════
    # DESIGN REVIEW
    # ═══════════════════════════════════════════════════════════════════════════
    safe_zone = FOOTER_Y + 20
    total_h = col_top - FOOTER_Y
    l_used = col_top - left_end
    r_used = col_top - right_end
    diff = abs(left_end - right_end)

    print("=" * 60)
    print("  DESIGN REVIEW PASS 1: Boundaries")
    print("=" * 60)
    print(f"  Left  ends at y={left_end:.0f}  |  {left_end - safe_zone:.0f}pt above safe zone  {'✓' if left_end > safe_zone else '✗'}")
    print(f"  Right ends at y={right_end:.0f}  |  {right_end - safe_zone:.0f}pt above safe zone  {'✓' if right_end > safe_zone else '✗'}")
    print(f"  Column diff: {diff:.0f}pt  {'✓ balanced' if diff < 50 else '⚠ unbalanced'}")

    print()
    print("=" * 60)
    print("  DESIGN REVIEW PASS 2: Proportions")
    print("=" * 60)
    print(f"  Column height available: {total_h:.0f}pt")
    print(f"  Left  uses: {l_used:.0f}pt ({l_used/total_h*100:.0f}%)")
    print(f"  Right uses: {r_used:.0f}pt ({r_used/total_h*100:.0f}%)")
    print(f"  Left  breathing room: {left_end - FOOTER_Y:.0f}pt")
    print(f"  Right breathing room: {right_end - FOOTER_Y:.0f}pt")
    print(f"  Font: Lato (Google Font)")
    print(f"  Paper: A4 ({W:.0f} × {H:.0f} pt)")
    print(f"  Salesforce badge: Salesforce Blue (#0176D3)")

    c.save()
    print(f"\n✓ Saved: {out}")


if __name__ == "__main__":
    out_path = sys.argv[1] if len(sys.argv) > 1 else None
    build(out_path)
