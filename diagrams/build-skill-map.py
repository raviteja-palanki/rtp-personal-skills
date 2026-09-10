#!/usr/bin/env python3
"""Generate diagrams/skill-map.svg from the skills actually in this repo.

The map went stale because it was hand-drawn: on 11 SEP 2026 it advertised
`Learn-site design`, archived two months earlier, and omitted ten skills that
ship, including `rtp-thinking-writing`, the default writing gate. Hand-editing
ninety boxes is what caused that, so the map is generated now.

Design tokens are lifted verbatim from the hand-drawn v1 so the output is
visually identical apart from the corrected content.

Usage:
    build-skill-map.py           write skill-map.svg
    build-skill-map.py --check   exit 1 if the committed SVG is out of date
"""
import os, re, sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SKILLS = REPO / "skills"
OUT = Path(__file__).resolve().parent / "skill-map.svg"
CHECK = "--check" in sys.argv

# ── design tokens, taken from the hand-drawn original ──────────────────────
W, PAD = 1400, 40
COLS = [257, 547, 837, 1127]
BOX_W, BOX_H, BOX_RX, ROW_PITCH = 278, 34, 9, 44
PANEL_GAP, SECTION_GAP = 16, 60
BG, INK, MUTED, PANEL_STROKE = "#FAFAF8", "#1B1B1F", "#5F6B7A", "#EDEDEA"

THEME = {
    "THINK": ("#14B8A6", "#0F766E", "#F0FDFA"),
    "JUDGE": ("#8B5CF6", "#6D28D9", "#F5F3FF"),
    "CRAFT": ("#F59E0B", "#B45309", "#FFFBEB"),
    "PLUS":  ("#6B7280", "#374151", "#F9FAFB"),
}

# ── where each skill sits, and the name shown on the box ───────────────────
# layer -> section -> [(mirror folder, display name)]
LAYOUT = [
 ("THINK", [
   ("FRAME THE PROBLEM", [
     ("rtp-first-principles","First principles"), ("rtp-bias-spotter","Bias spotter"),
     ("rtp-stress-test","Stress test"), ("rtp-problem-type","Problem type"),
     ("rtp-falsification","Falsification"), ("rtp-judgment-guard","Judgment guard"),
     ("rtp-determinism-compass","Determinism compass"), ("rtp-dual-lens","Dual lens"),
     ("rtp-gossip-mode","Gossip mode"), ("rtp-alignment-check","Alignment check")]),
   ("KNOW THE USER AND THE FIT", [
     ("rtp-problem-ai-fit","Problem-AI fit"), ("rtp-jtbd-analysis","JTBD analysis"),
     ("rtp-failure-modes","Failure modes"), ("rtp-feedback-flywheel","Feedback flywheel"),
     ("rtp-feedback-triage","Feedback triage"), ("rtp-interview-synthesis","Interview synthesis"),
     ("rtp-invisible-stack","Invisible stack"), ("rtp-needs-guard","Needs guard"),
     ("rtp-opportunity-solution-tree","Opportunity tree"), ("rtp-ai-product-taste","AI product taste"),
     ("rtp-ai-use-case-readiness","Use-case readiness"), ("rtp-ai-ux-patterns","AI UX patterns"),
     ("rtp-attitudinal-segmentation","Attitudinal segments"), ("rtp-uncertainty-research","Uncertainty research")]),
 ]),
 ("JUDGE", [
   ("STRATEGY", [
     ("rtp-moat-finder","Moat finder"), ("rtp-build-or-buy","Build or buy"),
     ("rtp-token-economics","Token economics"), ("rtp-strategy-canvas","Strategy canvas"),
     ("rtp-signal-scanner","Signal scanner"), ("rtp-capability-tracking","Capability tracking"),
     ("rtp-adoption-launch","Adoption launch"), ("rtp-ai-portfolio-management","Portfolio management"),
     ("rtp-purpose-dialogue","Purpose dialogue"), ("rtp-trendslop-check","Trendslop check"),
     ("rtp-vision-setting","Vision setting"), ("rtp-marketing-to-ai-agents","Marketing to AI agents")]),
   ("AGENTS", [
     ("rtp-autonomy-spectrum","Autonomy spectrum"), ("rtp-agent-harness","Agent harness"),
     ("rtp-agent-ecosystem","Agent ecosystem"), ("rtp-tool-architecture","Tool architecture"),
     ("rtp-multi-modal-product-design","Multi-modal design"),
     ("rtp-harness-operating-model","Harness operating model")]),
   ("SAFETY AND TRUST", [
     ("rtp-safety-by-design","Safety by design"), ("rtp-safety-as-moat","Safety as moat"),
     ("rtp-trust-ladder","Trust ladder"), ("rtp-trust-under-fog","Trust under fog"),
     ("rtp-agent-risk","Agent risk"), ("rtp-breach-ready","Breach ready"),
     ("rtp-responsible-ai-program","Responsible AI")]),
   ("EVALS AND QUALITY", [
     ("rtp-eval-framework","Eval framework"), ("rtp-eval-driven-development","Eval-driven development"),
     ("rtp-ai-product-metrics","AI product metrics"), ("rtp-confidence-tuner","Confidence tuner"),
     ("rtp-production-observability","Production observability"),
     ("rtp-gen-ai-experimentation","Gen-AI experimentation"),
     ("rtp-observability-stack","Observability stack")]),
 ]),
 ("CRAFT", [
   ("SHIP-READY DOCUMENTS", [
     ("rtp-ai-prd","AI-PRD"), ("rtp-agent-spec","Agent spec"), ("rtp-cost-model","Cost model"),
     ("rtp-ship-decision","Ship decision"), ("rtp-stakeholder-communications","Stakeholder comms"),
     ("rtp-context-spec","Context spec"), ("rtp-prompt-craft","Prompt craft"),
     ("rtp-prompt-as-product","Prompt as product"), ("rtp-competitive-map","Competitive map"),
     ("rtp-fit-signal","Fit signal"), ("rtp-user-stories","User stories")]),
 ]),
 ("PLUS", [
   ("EVERYTHING ELSE I DO", [
     ("rtp-thinking-writing","Thinking and writing"), ("rtp-humanizer","Humanizer"),
     ("rtp-thinking-skills","Thinking skills"), ("rtp-email-mastery","Email mastery"),
     ("rtp-personal-branding","Personal branding"), ("rtp-ux-design-systems","UX design systems"),
     ("rtp-deep-dive-writer","Deep-dive writer"), ("rtp-excalidraw-svg","Excalidraw SVG"),
     ("rtp-lucid-boards","Lucid boards"), ("rtp-frontend-slides","Frontend slides"),
     ("rtp-cinematic-presentations","Cinematic presentations"), ("rtp-ai-fluent-brand","AI Fluent brand"),
     ("rtp-design-spec","Design spec"), ("rtp-readme-storytelling","README storytelling"),
     ("rtp-research-synthesiser","Research synthesiser"), ("rtp-research-librarian","Research librarian"),
     ("rtp-hbr-research","HBR research"), ("rtp-claude-admin","Claude admin"),
     ("rtp-product-thinking","Product thinking"), ("rtp-ravis-resume-builder","Resume builder"),
     ("rtp-interview-skill","Interview skill"), ("rtp-skill-refresh","Skill refresh")]),
 ]),
]
ORCHESTRATOR = "rtp-aipm-orchestrator"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def audit():
    """The layout must name every skill in the repo, exactly once, and no others."""
    on_disk = {d for d in os.listdir(SKILLS) if (SKILLS / d / "SKILL.md").exists()}
    placed = [f for _, secs in LAYOUT for _, items in secs for f, _ in items]
    dupes = {f for f in placed if placed.count(f) > 1}
    placed_set = set(placed) | {ORCHESTRATOR}
    missing = sorted(on_disk - placed_set)
    ghosts = sorted(placed_set - on_disk)
    return sorted(on_disk), missing, ghosts, sorted(dupes)


def build():
    on_disk, missing, ghosts, dupes = audit()
    if missing or ghosts or dupes:
        print("LAYOUT IS OUT OF SYNC WITH THE REPO, refusing to draw a wrong map:")
        for m in missing: print(f"  MISSING from layout: {m}")
        for g in ghosts:  print(f"  IN LAYOUT, NOT ON DISK: {g}")
        for d in dupes:   print(f"  PLACED TWICE: {d}")
        sys.exit(2)

    total = len(on_disk)
    o = []
    y = 172
    panels = []
    for layer, sections in LAYOUT:
        accent, dark, tint = THEME[layer]
        py, body, count = y, [], 0
        cy = py + 30
        for title, items in sections:
            body.append(f'<text x="259" y="{cy}" fill="{accent}" font-size="12.5" '
                        f'font-weight="800" letter-spacing="1">{esc(title)}</text>')
            ry = cy + 10
            for i, (_, label) in enumerate(items):
                col = COLS[i % 4]
                if i and i % 4 == 0:
                    ry += ROW_PITCH
                body.append(f'<rect x="{col}" y="{ry}" width="{BOX_W}" height="{BOX_H}" rx="{BOX_RX}" '
                            f'fill="{tint}" stroke="{accent}" stroke-width="1.3"/>')
                body.append(f'<text x="{col + BOX_W/2:.1f}" y="{ry + 22.5}" text-anchor="middle" '
                            f'fill="{dark}" font-size="14" font-weight="600">{esc(label)}</text>')
                count += 1
            cy = ry + SECTION_GAP
        ph = (ry + BOX_H + 14) - py
        panels.append((layer, py, ph, accent, dark, tint, count, body))
        y = py + ph + PANEL_GAP

    height = y - PANEL_GAP + 60
    o.append(f'<svg viewBox="0 0 {W} {height}" xmlns="http://www.w3.org/2000/svg" '
             f'font-family="Inter, -apple-system, sans-serif" role="img" '
             f'aria-label="The full map of {total} skills">')
    o.append('<defs><filter id="s" x="-15%" y="-15%" width="130%" height="130%">'
             '<feDropShadow dx="1.5" dy="2.5" stdDeviation="3.5" flood-color="#00000015"/></filter></defs>')
    o.append(f'<rect width="{W}" height="{height}" rx="16" fill="{BG}"/>')
    o.append(f'<text x="700" y="54" text-anchor="middle" fill="{INK}" font-size="30" '
             f'font-weight="800">The full map: {total} skills</text>')
    o.append(f'<text x="700" y="82" text-anchor="middle" fill="{MUTED}" font-size="15">'
             f'Every name below is a real, versioned skill. The orchestrator composes them.</text>')
    o.append(f'<rect x="{PAD}" y="104" width="{W-2*PAD}" height="46" rx="14" fill="{INK}" filter="url(#s)"/>')
    o.append('<text x="700" y="133" text-anchor="middle" fill="#FFFFFF" font-size="15" font-weight="700">'
             'The Orchestrator: reads the situation, composes the right skills, reviews the output</text>')

    for layer, py, ph, accent, dark, tint, count, body in panels:
        o.append(f'<rect x="{PAD}" y="{py}" width="{W-2*PAD}" height="{ph}" rx="14" fill="#FFFFFF" '
                 f'stroke="{PANEL_STROKE}" stroke-width="1.5" filter="url(#s)"/>')
        o.append(f'<rect x="{PAD}" y="{py}" width="195" height="{ph}" rx="14" fill="{tint}"/>'
                 f'<rect x="221" y="{py}" width="14" height="{ph}" fill="{tint}"/>')
        o.append(f'<rect x="{PAD}" y="{py}" width="6" height="{ph}" rx="3" fill="{accent}"/>')
        o.append(f'<text x="66" y="{py+46}" fill="{dark}" font-size="24" font-weight="800">{layer}</text>')
        o.append(f'<text x="66" y="{py+72}" fill="{accent}" font-size="14" font-weight="700">{count} skills</text>')
        o.extend(body)

    o.append(f'<text x="700" y="{height-24}" text-anchor="middle" fill="#9CA3AF" font-size="13">'
             f'Every rule states when it fails. Every number carries its evidence tier. '
             f'Everything reads in plain language.</text>')
    o.append('</svg>')
    return "\n".join(o) + "\n", total, [(p[0], p[6]) for p in panels]


if __name__ == "__main__":
    svg, total, counts = build()
    if CHECK:
        cur = OUT.read_text() if OUT.exists() else ""
        if cur.strip() != svg.strip():
            print("skill-map.svg is OUT OF DATE. Run build-skill-map.py.")
            sys.exit(1)
        print(f"skill-map.svg current · {total} skills · " +
              " · ".join(f"{l} {c}" for l, c in counts))
    else:
        OUT.write_text(svg)
        print(f"wrote skill-map.svg · {total} skills · " +
              " · ".join(f"{l} {c}" for l, c in counts))
