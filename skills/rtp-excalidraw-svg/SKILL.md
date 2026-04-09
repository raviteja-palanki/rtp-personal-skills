---
name: excalidraw-svg
version: 1.2.0
description: "Excalidraw SVG diagrams: pastel, readable text, storytelling. Diagrams, flowcharts, architecture, infographics, flows, maps. Use when: visual explanation or output enhancer for PRD/spec/analysis. Triggers: 'diagram', 'flowchart', 'visual', 'architecture'"
---

# Excalidraw SVG — Visual Storytelling System v1.2

Production-tested design system for creating beautiful, readable SVG diagrams
with Excalidraw-inspired aesthetics, embedded copywriting, and visual narrative structure.

> **v1.2 restructure:** Core workflow + single quality gate in this file.
> Reference material (colors, patterns, GitHub rendering, libraries) in `references/`.

---

## CORE PHILOSOPHY

Three non-negotiable principles:

1. **Readability is sacred.** If text can't be read at a glance, it doesn't exist. Dark text on light backgrounds. Minimum 11px, prefer 13-16px for body. Never grey-on-grey.
2. **Every diagram tells one story.** Not a data dump. One narrative arc: setup → tension → resolution. The viewer should know the takeaway in 3 seconds.
3. **Restraint signals mastery.** Maximum 5 colors per diagram. One accent color draws the eye. White space is a design element, not wasted space.

---

## IDEO DESIGN DIRECTOR REVIEW

Before creating any diagram, internalize these five principles. They separate functional diagrams from ones that influence decisions.

### 1. Human-Centered Framing
Diagrams answer the viewer's question, not the system's structure.

**Wrong:** "Here are all the components."
**Right:** "Here's what the viewer needs to decide / understand / build."

### 2. Prototype Thinking
First diagrams are prototypes. Expect 2-3 iterations. Build for feedback, not perfection. Never spend 2 hours perfecting a layout before getting feedback.

### 3. Show, Don't Tell
Use visual metaphors. A funnel IS filtering. A bridge IS connection. A layer cake IS inheritance.

**Anti-pattern:** Text-heavy boxes with arrows labeled "sends," "receives," "processes." That's a data structure, not a story.

### 4. Emotional Design
Diagrams should make the viewer FEEL something:
- **Confidence:** Clear path forward, no ambiguity.
- **Urgency:** Red highlights what breaks. Moss highlights what works.
- **Clarity:** Even complex systems feel understandable.

### 5. The "Walk the Wall" Test
Would this diagram survive being printed at A3 and pinned to a wall? Would someone walking by get the main point in 10 seconds? If no, simplify or split.

---

## STEP 1: STORY ARCHITECTURE (Before Touching SVG)

Answer three questions before writing any SVG code:

1. **What's the one sentence this diagram communicates?**
   If you can't say it in one sentence, you need multiple diagrams.

2. **What's the viewer's journey?**
   - Entry point (where eyes land first — usually top-left or center)
   - Flow direction (left→right for processes, top→down for hierarchies)
   - Punchline (the insight, comparison, or "aha" — usually bottom or right)

3. **What's the depth label?**
   - `Depth — Comprehensive` (detailed breakdown, multiple sections)
   - `Quick Check — Executive Summary` (high-level overview, scannable)

### Copywriting Rules

Apply Rory Sutherland's reframing principle: **don't describe what it does, reveal what's counterintuitive.**

| Bad (describes) | Good (reframes) |
|-----------------|-----------------|
| "Evaluates AI readiness" | "Most teams overshoot. This right-sizes the investment." |
| "Processes user feedback" | "99% collect feedback. 10-20% reaches the model." |
| "Strategy planning tool" | "Strategy with an expiration date." |

- Headlines: 5-8 words. Verb-forward or insight-forward.
- Card body: 2-3 lines max. Specific numbers beat adjectives.
- Callout boxes: The "so what?" — why this matters to the viewer.
- Never use: "leverage", "utilize", "comprehensive", "robust", "streamline", "empower".

### Executive Framing

When diagrams are shared in boardrooms, use a three-act color narrative:
1. **Problem** — What breaks without this? (Coral)
2. **Mechanism** — How does it work? (Neutral/Blue)
3. **Impact** — What becomes possible? (Moss)

The color carries the story. An executive should see the progression without reading a word. Include 1-2 specific numbers per diagram — "3.2x faster" beats "dramatic improvement."

---

## STEP 2: CHOOSE A DIAGRAM TYPE

| Use case | Type | Key feature |
|----------|------|-------------|
| System architecture | **Layer Cards** | Colored header bars, skill/component chips |
| Process flow | **Flow Chain** | Horizontal boxes with arrows, entry→exit |
| Comparison | **Side-by-Side** | Two panels, red vs. green, before/after |
| Hierarchy | **Nested Groups** | Outer container with inner cards |
| Timeline/sequence | **Step Ladder** | Numbered vertical or horizontal steps |
| Feature catalog | **Grid Cards** | 2x3 or 3x4 grid of uniform cards |
| Relationship map | **Hub-Spoke** | Central node with radiating connections |
| Agent workflow | **Agentic Loop** | Circular dashed arrow, LLM card, exit conditions |
| Capacity/budget | **Context Bar** | Horizontal stacked bar with limit line |
| Agent outputs | **Deliverable Map** | Agent cards with deliverable chips below |

Full patterns with code examples: [references/diagram-types.md](references/diagram-types.md)

---

## STEP 3: DESIGN SYSTEM

### SVG Boilerplate

Every SVG starts with this exact structure:

```xml
<svg xmlns="http://www.w3.org/2000/svg" role="img"
     aria-label="{ONE_SENTENCE_TAKEAWAY}"
     viewBox="0 0 {WIDTH} {HEIGHT}" width="{WIDTH}" height="{HEIGHT}">
  <title>{DIAGRAM_TITLE}</title>
  <desc>{2-3 sentence description}</desc>
  <defs>
    <filter id="s" x="-4%" y="-4%" width="108%" height="108%">
      <feDropShadow dx="2" dy="3" stdDeviation="4" flood-color="#00000018"/>
    </filter>
  </defs>

  <!-- Background: warm off-white, NOT pure white -->
  <rect width="{WIDTH}" height="{HEIGHT}" rx="16" fill="#FAFAF8"/>

  <!-- Header band with depth label -->
  <rect x="0" y="0" width="{WIDTH}" height="80" rx="16" fill="{HEADER_TINT}"/>
  <rect x="0" y="60" width="{WIDTH}" height="20" fill="{HEADER_TINT}"/>
  <text x="{CENTER}" y="36" text-anchor="middle" fill="{HEADER_TEXT}" font-size="28" font-weight="800" font-family="Inter, Segoe UI, sans-serif">{TITLE}</text>
  <text x="{CENTER}" y="62" text-anchor="middle" fill="#5F6B7A" font-size="15" font-family="Inter, sans-serif">{DEPTH_LABEL} · {SUBTITLE}</text>

  <!-- Content area -->
  ...

  <!-- Footer — must be ≥40px from viewBox bottom -->
  <text x="{CENTER}" y="{HEIGHT - 50}" text-anchor="middle" fill="#9CA3AF" font-size="12" font-family="Inter, sans-serif">{FOOTER_TEXT}</text>
</svg>
```

### Dimensions

| Content | Width | Height range |
|---------|-------|-------------|
| Simple (1-4 elements) | 1200 | 400-520 |
| Medium (5-8 elements) | 1200 | 520-720 |
| Complex (9+ elements) | 1200 | 720-900 |

Width is ALWAYS 1200px. Never exceed 900px height — break into multiple diagrams instead.

### Color System

8 Luminous Pastel families. Pick 2-3 per diagram. Full palette: [references/color-palette.md](references/color-palette.md)

| Semantic | Header solid | Card bg | Text dark | Use for |
|----------|-------------|---------|-----------|---------|
| Rose Quartz | `#D4789B` | `#FFF5F8` | `#8B3A5A` | Thinking, analysis |
| Wisteria | `#9478B8` | `#F8F5FF` | `#5B3E7A` | Judgment, decisions |
| Honey Amber | `#D4A54A` | `#FFFCF5` | `#7A5A1E` | Craft, output |
| Celadon | `#6BA898` | `#F2FAF6` | `#2E6B54` | Eval, quality |
| Glacier | `#5A9ABE` | `#F3F9FD` | `#2A5F7A` | Tech, data |
| Coral | `#D47B64` | `#FFF7F4` | `#8B4434` | Agents, danger |
| Moss | `#7BA86C` | `#F5FAF2` | `#3A5E2E` | Success, outcome |
| Neutral | — | `#FFFFFF` | `#1B1B1F` | Structure |

### Typography Scale

| Element | Size | Weight | Color |
|---------|------|--------|-------|
| Diagram title | 28-30px | 800 | `#1B1B1F` or semantic dark |
| Section header | 17-20px | 700-800 | White (on colored bar) |
| Card subtitle | 14-15px | 600-700 | Semantic dark |
| Body text | 13-14px | 400 | `#5F6B7A` |
| Chip/tag text | 10-12px | 600 | Semantic medium |
| Footer/meta | 11-12px | 400 | `#9CA3AF` |

**Font stack:** `Inter, Segoe UI, sans-serif` — always.

### Components

**Card** (the fundamental building block):
```xml
<rect x="{X}" y="{Y}" width="270" height="{H}" rx="14" fill="#FFFFFF" stroke="{BORDER}" stroke-width="2" filter="url(#s)"/>
<rect x="{X}" y="{Y}" width="270" height="44" rx="14" fill="{HEADER_SOLID_COLOR}"/>
<text x="{CENTER_X}" y="{Y+29}" text-anchor="middle" fill="#FFFFFF" font-size="16" font-weight="700" font-family="Inter, sans-serif">{TITLE}</text>
```
Card widths: `230` (compact), `270` (standard), `340-370` (wide), `545-555` (half-width).

**Chip/Tag:**
```xml
<rect x="{X}" y="{Y}" width="{W}" height="26" rx="8" fill="{CHIP_BG}" stroke="{CHIP_BORDER}" stroke-width="1"/>
<text x="{CENTER_X}" y="{Y+18}" text-anchor="middle" fill="{CHIP_TEXT}" font-size="11" font-weight="600" font-family="Inter, sans-serif">{LABEL}</text>
```

**Callout Box** (the "so what?" punchline):
```xml
<rect x="{X}" y="{Y}" width="{W}" height="76" rx="14" fill="{TINTED_BG}" stroke="{BORDER}" stroke-width="2" filter="url(#s)"/>
<text x="{CENTER}" y="{Y+30}" text-anchor="middle" fill="{DARK_TEXT}" font-size="16" font-weight="700" font-family="Inter, sans-serif">{HEADLINE}</text>
<text x="{CENTER}" y="{Y+54}" text-anchor="middle" fill="#78716C" font-size="14" font-family="Inter, sans-serif">{INSIGHT}</text>
```

**Before/After Comparison:**
```xml
<!-- Bad (red) -->
<rect x="{X}" y="{Y}" width="{W/2-20}" height="62" rx="14" fill="#FEF2F2" stroke="#FCA5A5" stroke-width="2" filter="url(#s)"/>
<!-- Good (green) -->
<rect x="{X+W/2+10}" y="{Y}" width="{W/2-20}" height="62" rx="14" fill="#F0FDF4" stroke="#86EFAC" stroke-width="2" filter="url(#s)"/>
```

---

## STEP 4: VISUAL PATTERNS (Quick Reference)

Each pattern has a story it tells. Pick the one that fits YOUR narrative.

| Pattern | Story | Best for |
|---------|-------|----------|
| **Layer Cake** | "Each layer inherits from the one above" | Architectures, pipelines, maturity |
| **Grid of Equals** | "Here are your options" | Feature catalogs, tool comparisons |
| **Funnel** | "Many inputs, one output" | Decision processes, data pipelines |
| **Hub-Spoke** | "Everything connects to this core" | System diagrams, dependency maps |
| **Timeline** | "First this, then this" | Onboarding, deployment, incident response |
| **Contrast** | "Without vs. with" | Before/after, problem/solution |
| **Step-by-Step Flow** | "Watch the system handle a real request" | Agent loops, API sequences |
| **Agentic Loop** | "Iterate until exit conditions met" | AI agent architectures |
| **Deliverable Map** | "Here's what you GET from each agent" | Skill/service catalogs |

Full code examples for each: [references/diagram-types.md](references/diagram-types.md)

---

## STEP 5: LAYOUT & SPACING

**Plan the coordinate grid before writing a single `<rect>`.** This prevents overlapping elements.

### Sizing Rules

**Width:** `min(max(160, textLength × 9), 520)`. If text exceeds 520px: shorten it, break into 2 lines with `<tspan dy="18">`, or use a half-width card (545px).

**Height by content:**
| Content | Height |
|---------|--------|
| Title only | 48-60px |
| Title + subtitle | 70-80px |
| Title + subtitle + description | 90-110px |
| Full card (header + body + chips) | 170-220px |

### Spacing Hierarchy

| Context | Gap |
|---------|-----|
| Inside card (text padding) | 16px |
| Sibling cards (same row) | 20-40px |
| Between groups | 40px |
| Between tiers/layers | 60px |
| Card internal padding | 16-20px |
| Background to SVG edge | **50px minimum** |
| Arrow label to line | 12px |
| Chip to chip | 8-10px |

### Coordinate Grid Template

```
Tier 0 (y=0-80):   Header band
Tier 1 (y=110):    Row 1 content cards
Tier 2 (y=310):    Row 2 or connectors
Tier 3 (y=510):    Row 3 or callout
Footer (y=H-50):   Attribution line
```

**4 cards at 270px wide:** x = 40, 330, 620, 910 (within 1200px with 40px margins).

### Layout Verification

Before writing SVG:
- All elements fit within 1200px width (50px left/right margins)?
- Total height ≤ 900px? If not, split.
- Connected elements close enough that arrows won't cross unrelated content?

---

## STEP 6: ARROWS & CONNECTIONS

| Arrow type | SVG | When |
|-----------|-----|------|
| Straight horizontal | `M x1,y L x2,y` | Same-row connections |
| Straight vertical | `M x,y1 L x,y2` | Parent-child hierarchies |
| Curved bezier | `M x1,y1 C cx1,cy1 cx2,cy2 x2,y2` | Layer-to-layer flows |
| Elbowed (L-shaped) | `M x1,y1 L x1,y2 L x2,y2` | Cross-lane routing |

**Validated:** Curved bezier arrows with labeled midpoints are the preferred style. Confirmed effective in interview and presentation contexts.

### Routing Rules

1. **Never accept crossing arrows.** Rearrange elements instead.
2. **Arrow gap:** 25-30px from element edge to arrow start/end.
3. **Arrowhead:** 10-12px. Use `<polygon>` not `<marker>`.
4. **Labels:** Midway along path, 12px above, 11px bold in semantic color.

---

## STEP 7: QUALITY GATE (Mandatory — The Single Source of Truth)

**Stop. Run every check before sharing. Zero exceptions.**

### Text & Readability
- [ ] No truncated text. Sizing rule: `width = min(max(160, textLength × 9), 520)`
- [ ] Background is `#FAFAF8` (warm off-white)
- [ ] Body text is `#1B1B1F` or `#5F6B7A` — never grey-on-grey
- [ ] Minimum font size 11px; body 13-14px
- [ ] White text ONLY on solid color headers (weight 700+, size 16px+)
- [ ] Every text element: `font-family="Inter, Segoe UI, sans-serif"`

### Border Padding Verification (The Four-Edge Gate)
**This is where SVGs most often fail. Check all four edges explicitly.**
- [ ] **TOP:** No element starts above y=50. Title baseline ≥ y=60.
- [ ] **BOTTOM:** No element extends below `(viewBox height - 50)`. Footer baseline + font-size ≤ `(viewBox height - 40)`. Footers must NEVER collide with the last row of content.
- [ ] **LEFT:** No element starts before x=50.
- [ ] **RIGHT:** No element (rect x + width, text x + estimated width) extends past `(viewBox width - 50)`.
- [ ] **Footer clearance:** ≥ 30px between lowest content and top of footer.
- [ ] **Verification:** For every element near an edge (within 80px), manually compute: `element_y + height < viewBox_height - 50`.

### Layout & Spacing
- [ ] No overlapping elements — check every pair. Zero tolerance.
- [ ] No arrow-text overlap.
- [ ] Width 1200px, height ≤ 900px.
- [ ] Consistent gaps: 20-40px siblings, 60px tiers.
- [ ] All cards use `filter="url(#s)"`.
- [ ] Rounded corners: 14-16px cards, 8px chips.

### Arrows
- [ ] No crossing arrows.
- [ ] 25-30px clearance from element edges.
- [ ] Every arrow has a visible `<polygon>` arrowhead.
- [ ] Labels positioned midway, 12px above.

### Color
- [ ] Maximum 3 color families per diagram (plus neutral).
- [ ] Each family used consistently (header = saturated, bg = pastel, text = dark).

### Story & Copy
- [ ] Depth label present at top.
- [ ] One clear narrative arc.
- [ ] Callout box delivers the "so what?"
- [ ] Headlines reframe, not describe.
- [ ] No filler words.
- [ ] Specific numbers where possible.
- [ ] Card descriptions 2-3 lines max.

### Final Sanity
- [ ] Open in browser — all text readable without zooming.
- [ ] Squint test — key message still readable.
- [ ] 3-second test — story obvious to first-time viewer.
- [ ] No orphaned elements.
- [ ] "Walk the Wall" test — works at A3 poster size.

---

## STEP 8: ITERATE

Complex diagrams rarely come out perfect. Use this loop:

1. **Write** the SVG.
2. **Run the Quality Gate** (Step 7). Be ruthless.
3. **Fix** each failure:
   - Text overflow → shorten label OR widen container
   - Overlap → increase tier spacing OR rearrange grid
   - Crossing arrows → swap element positions
   - Bottom padding failure → increase viewBox height
4. **Re-run** the Quality Gate. Repeat until zero failures.

**When to split vs. simplify:**
- **Split** when you have two distinct stories
- **Simplify** when one story has too many details (show top 5-8, not all 25)
- **Never** fix complexity by shrinking text or reducing spacing — that's a readability death spiral

---

## CROSS-SKILL VISUAL SUMMARIES

When ANY other skill produces output (PRD, spec, analysis), create ONE Excalidraw SVG capturing the essence in a single glanceable image. This makes every deliverable 10x more impactful.

Full protocol: [references/visual-summary-protocol.md](references/visual-summary-protocol.md)

Quick rules:
- Maximum 6-8 elements — ruthlessly prioritize
- Title = the document's thesis, not its name
- Use "Quick Check — Executive Summary" depth label
- File naming: `{output-name}-visual-summary.svg`

---

## REFERENCE FILES

| File | Content | When to read |
|------|---------|-------------|
| [color-palette.md](references/color-palette.md) | Full 8-family palette with all shade variants | When choosing colors |
| [diagram-types.md](references/diagram-types.md) | Pattern catalog with XML code examples | When building a specific pattern |
| [github-rendering.md](references/github-rendering.md) | GitHub SVG sanitizer, accessibility, text encoding | When preparing for GitHub |
| [excalidraw-libraries.md](references/excalidraw-libraries.md) | 40+ Excalidraw component libraries | When looking for visual inspiration |
| [visual-summary-protocol.md](references/visual-summary-protocol.md) | Cross-skill visual summary rules | When enhancing other skill output |

---

## COPYRIGHT

Where appropriate, include: `© Raviteja Palanki, AI Product Manager`

Use on standalone showcase pieces, hero images, and externally-shared diagrams. Skip on internal documentation diagrams where a descriptive footer is more useful.

---

*Excalidraw SVG v1.2.0 | Restructured 9 APR 2026 | Ravi Teja Palanki*
