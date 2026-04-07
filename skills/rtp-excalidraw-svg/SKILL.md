---
name: excalidraw-svg
description: "Excalidraw SVG diagrams: pastel, readable text, storytelling. Diagrams, flowcharts, architecture, infographics, flows, maps. Use when: visual explanation or output enhancer for PRD/spec/analysis. Triggers: 'diagram', 'flowchart', 'visual', 'architecture'"
---

# Excalidraw SVG — Visual Storytelling System

Production-tested design system for creating beautiful, readable SVG diagrams
with Excalidraw-inspired aesthetics, embedded copywriting, and visual narrative structure.

## CORE PHILOSOPHY

Three non-negotiable principles from Apple's design team, adapted for diagrams:

1. **Readability is sacred.** If text can't be read at a glance, it doesn't exist. Dark text on light backgrounds. Minimum 11px, prefer 13-16px for body. Never grey-on-grey.
2. **Every diagram tells one story.** Not a data dump. One narrative arc: setup → tension → resolution. The viewer should know the takeaway in 3 seconds.
3. **Restraint signals mastery.** Maximum 5 colors per diagram. One accent color draws the eye. White space is a design element, not wasted space.

---

## STEP 1: STORY ARCHITECTURE (Before touching SVG)

Before writing any SVG code, answer these three questions:

1. **What's the one sentence this diagram communicates?**
   Write it down. If you can't say it in one sentence, you need multiple diagrams.

2. **What's the viewer's journey?**
   - Entry point (where eyes land first — usually top-left or center)
   - Flow direction (left→right for processes, top→down for hierarchies)
   - Punchline (the insight, comparison, or "aha" — usually bottom or right)

3. **What's the depth label?**
   Every diagram gets ONE of these at the top:
   - `Depth — Comprehensive` (detailed breakdown, multiple sections)
   - `Quick Check — Executive Summary` (high-level overview, scannable)

### Copywriting Rules for Diagram Text

Apply Rory Sutherland's reframing principle: **don't describe what it does, reveal what's counterintuitive about it.**

| Bad (describes) | Good (reframes) |
|-----------------|-----------------|
| "Evaluates AI readiness" | "Most teams overshoot. This right-sizes the investment." |
| "Processes user feedback" | "99% collect feedback. 10-20% reaches the model." |
| "Monitors production" | "Catches the failures that don't trigger errors." |
| "Strategy planning tool" | "Strategy with an expiration date." |

Rules:
- Headlines: 5-8 words. Verb-forward or insight-forward. Never abstract nouns.
- Subtitles: One sentence that creates tension or curiosity.
- Card body: 2-3 lines max. Specific numbers beat adjectives.
- Callout boxes: The "so what?" — why this matters to the viewer.
- Never use: "leverage", "utilize", "comprehensive", "robust", "streamline", "empower".

---

## STEP 2: CHOOSE A DIAGRAM TYPE

Read [references/diagram-types.md](references/diagram-types.md) for the full catalog.

Quick selection:

| Use case | Type | Key feature |
|----------|------|-------------|
| System architecture | **Layer Cards** | Colored header bars, skill/component chips |
| Process flow | **Flow Chain** | Horizontal boxes with arrows, entry→exit |
| Comparison | **Side-by-Side** | Two panels, red vs. green, before/after |
| Hierarchy | **Nested Groups** | Outer container with inner cards |
| Timeline/sequence | **Step Ladder** | Numbered vertical or horizontal steps |
| Feature catalog | **Grid Cards** | 2x3 or 3x4 grid of uniform cards |
| Relationship map | **Hub-Spoke** | Central node with radiating connections |

---

## STEP 3: APPLY THE DESIGN SYSTEM

### SVG Boilerplate

Every SVG starts with this exact structure:

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" width="{WIDTH}" height="{HEIGHT}">
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
  <text x="{CENTER}" y="62" text-anchor="middle" fill="#374151" font-size="15" font-family="Inter, sans-serif">{DEPTH_LABEL} · {SUBTITLE}</text>

  <!-- Content area -->
  ...

  <!-- Footer -->
  <text x="{CENTER}" y="{HEIGHT - 30}" text-anchor="middle" fill="#9CA3AF" font-size="12" font-family="Inter, sans-serif">{FOOTER_TEXT}</text>
</svg>
```

### Dimensions

| Content | Width | Height range |
|---------|-------|-------------|
| Simple (1-4 elements) | 1200 | 400-520 |
| Medium (5-8 elements) | 1200 | 520-720 |
| Complex (9+ elements) | 1200 | 720-900 |

Width is ALWAYS 1200px. This renders perfectly on GitHub READMEs, documentation sites, and most screens. Never exceed 900px height — break into multiple diagrams instead.

### The Color System

See [references/color-palette.md](references/color-palette.md) for the complete palette.

**Quick reference — the 8 semantic color families:**

| Semantic | Header fill | Card bg | Chip bg | Chip border | Text dark | Text medium |
|----------|------------|---------|---------|-------------|-----------|-------------|
| Teal (thinking/foundation) | `#14B8A6` | `#F0FDFA` | `#CCFBF1` | `#5EEAD4` | `#0F766E` | `#0D9488` |
| Purple (judgment/decision) | `#8B5CF6` | `#F5F3FF` | `#EDE9FE` | `#C4B5FD` | `#6D28D9` | `#7C3AED` |
| Amber (craft/output) | `#F59E0B` | `#FFFBEB` | `#FEF3C7` | `#FCD34D` | `#B45309` | `#92400E` |
| Cyan (eval/quality) | `#06B6D4` | `#ECFEFF` | `#ECFEFF` | `#67E8F9` | `#0E7490` | `#0E7490` |
| Pink (agents/autonomy) | `#EC4899` | `#FCE7F3` | `#FCE7F3` | `#F9A8D4` | `#9D174D` | `#9D174D` |
| Red (danger/incident) | `#EF4444` | `#FEF2F2` | `#FEF2F2` | `#FCA5A5` | `#991B1B` | `#DC2626` |
| Green (success/positive) | `#16A34A` | `#F0FDF4` | `#D1FAE5` | `#86EFAC` | `#065F46` | `#16A34A` |
| Neutral (structure) | `#6B7280` | `#FFFFFF` | `#F9FAFB` | `#E5E7EB` | `#1B1B1F` | `#5F6B7A` |

**Selection rule:** Pick 2-3 primary families per diagram. Use one for emphasis. Neutral for structure.

### Typography Scale

| Element | Size | Weight | Color | Use |
|---------|------|--------|-------|-----|
| Diagram title | 28-30px | 800 | `#1B1B1F` or semantic dark | One per diagram |
| Section header | 17-20px | 700-800 | White (on colored bar) | Card/section titles |
| Card subtitle | 14-15px | 600-700 | Semantic dark color | Below header bar |
| Body text | 13-14px | 400 | `#5F6B7A` | Descriptions, explanations |
| Chip/tag text | 10-12px | 600 | Semantic medium color | Skill names, labels, tags |
| Footer/meta | 11-12px | 400 | `#9CA3AF` | Attribution, pagination |

**Font stack:** `Inter, Segoe UI, sans-serif` — always. Never use monospace for display. Only for code literals.

### Card Component

The fundamental building block. Excalidraw-inspired: rounded, shadowed, colored header bar.

```xml
<!-- Standard card: 270px wide, height varies -->
<rect x="{X}" y="{Y}" width="270" height="{H}" rx="14" fill="#FFFFFF" stroke="{BORDER}" stroke-width="2" filter="url(#s)"/>
<!-- Colored header bar (two rects to get flat bottom on header) -->
<rect x="{X}" y="{Y}" width="270" height="44" rx="14" fill="{HEADER_COLOR}"/>
<rect x="{X}" y="{Y+30}" width="270" height="14" fill="{HEADER_COLOR}"/>
<!-- Header text (white on color) -->
<text x="{CENTER_X}" y="{Y+29}" text-anchor="middle" fill="#FFFFFF" font-size="16" font-weight="700" font-family="Inter, sans-serif">{CARD_TITLE}</text>
```

Card widths: `230` (compact), `270` (standard), `340-370` (wide), `545-555` (half-width).

### Chip/Tag Component

For skill names, labels, categories inside cards:

```xml
<rect x="{X}" y="{Y}" width="{W}" height="26-30" rx="8" fill="{CHIP_BG}" stroke="{CHIP_BORDER}" stroke-width="1"/>
<text x="{CENTER_X}" y="{Y+18}" text-anchor="middle" fill="{CHIP_TEXT}" font-size="11" font-weight="600" font-family="Inter, sans-serif">{LABEL}</text>
```

### Arrow/Flow Component

For connecting elements:

```xml
<!-- Simple horizontal arrow -->
<path d="M {X1} {Y} L {X2} {Y}" stroke="#9CA3AF" stroke-width="2" fill="none"/>
<polygon points="{X2},{Y-5} {X2+10},{Y} {X2},{Y+5}" fill="#9CA3AF"/>

<!-- Labeled arrow (with "feeds" or similar) -->
<path d="M {X1} {Y} C ..." stroke="{COLOR}" stroke-width="3" fill="none" stroke-linecap="round"/>
<polygon points="..." fill="{COLOR}"/>
<text x="{MID_X}" y="{Y-12}" text-anchor="middle" fill="{COLOR}" font-size="11" font-weight="700" font-family="Inter, sans-serif">{LABEL}</text>
```

### Story Callout Box

For the "why this matters" punchline at the bottom of a diagram:

```xml
<rect x="{X}" y="{Y}" width="{W}" height="76" rx="14" fill="{TINTED_BG}" stroke="{BORDER}" stroke-width="2" filter="url(#s)"/>
<text x="{CENTER}" y="{Y+30}" text-anchor="middle" fill="{DARK_TEXT}" font-size="16" font-weight="700" font-family="Inter, sans-serif">{HEADLINE}</text>
<text x="{CENTER}" y="{Y+54}" text-anchor="middle" fill="#78716C" font-size="14" font-family="Inter, sans-serif">{INSIGHT_LINE}</text>
```

### Before/After Comparison

Red panel (bad) and green panel (good), side by side:

```xml
<!-- Bad outcome -->
<rect x="{X}" y="{Y}" width="{W/2 - 20}" height="62" rx="14" fill="#FEF2F2" stroke="#FCA5A5" stroke-width="2" filter="url(#s)"/>
<text x="{X+20}" y="{Y+24}" fill="#DC2626" font-size="15" font-weight="800" font-family="Inter, sans-serif">{BAD_LABEL}</text>
<text x="{X+20}" y="{Y+46}" fill="#6B7280" font-size="14" font-family="Inter, sans-serif">{BAD_DESCRIPTION}</text>

<!-- Good outcome -->
<rect x="{X + W/2 + 10}" y="{Y}" width="{W/2 - 20}" height="62" rx="14" fill="#F0FDF4" stroke="#86EFAC" stroke-width="2" filter="url(#s)"/>
<text x="{X + W/2 + 30}" y="{Y+24}" fill="#16A34A" font-size="15" font-weight="800" font-family="Inter, sans-serif">{GOOD_LABEL}</text>
<text x="{X + W/2 + 30}" y="{Y+46}" fill="#1B1B1F" font-size="14" font-weight="500" font-family="Inter, sans-serif">{GOOD_DESCRIPTION}</text>
```

---

## STEP 4: VISUAL STORYTELLING PATTERNS

### Pattern: The Layer Cake
Show 2-4 horizontal layers that build on each other, connected by arrows.
Story: "Each layer inherits from the one above."
Use for: architectures, pipelines, maturity models.

### Pattern: The Grid of Equals
2×3 or 3×3 grid of identically-sized cards, each with a colored header.
Story: "Here are your options. Pick the one that fits."
Use for: feature catalogs, workflow menus, tool comparisons.

### Pattern: The Funnel
Wide at the top, narrow at the bottom. Each stage filters or refines.
Story: "Many inputs, one output. Here's what survives each filter."
Use for: decision processes, user journeys, data pipelines.

### Pattern: The Hub-Spoke
Central element with radiating connections.
Story: "Everything connects to this core concept."
Use for: system diagrams, team structures, dependency maps.

### Pattern: The Timeline
Horizontal or vertical sequence of numbered steps with connecting lines.
Story: "First this, then this, then this."
Use for: onboarding flows, deployment processes, incident response.

### Pattern: The Contrast
Two panels side by side — one problem, one solution.
Story: "This is what happens without. This is what happens with."
Use for: before/after, with/without, old/new comparisons.

### Pattern: The Step-by-Step Flow (Anthropic-style)
Vertical sequence of interaction cards with step labels on the left, role badges on the right, and dashed curved arrows for return flows. Each card has a colored left border indicating the actor (purple=user, amber=agent, teal=server, green=done).
Story: "Watch how the system handles this real request, step by step."
Use for: agent loops, API call sequences, customer support flows, end-to-end examples.
Key elements:
- Step numbers as labels on the left margin (STEP 1, STEP 2...)
- Colored left-border bars on each card (4-6px wide)
- Role badges (pill shapes) on the right margin
- Dashed curved arrows for return/result flows
- Final card gets a tinted background (green) for resolution

### Pattern: The Grouped Containers (ByteByteGo-style)
Dashed-border containers grouping related elements, with labeled headers on each group. Elements within containers use solid borders.
Story: "Here's how the pieces cluster — and here's what connects the clusters."
Use for: system design, microservices architecture, platform overviews.
Key elements:
- Outer containers with dashed borders and rounded corners
- Group labels as chips/badges on container top-left
- Inner elements as solid-border cards
- Cross-container arrows show integration points
- Icon integration for recognizable services (databases, queues, APIs)

### Pattern: The Comparison Panel (Side-by-Side Architecture)
Two large panels side by side, each showing a complete system. Connected by a "vs" element in the center. Each panel has its own color family.
Story: "These look similar but serve different purposes — here's the real difference."
Use for: Load balancer vs. API gateway, monolith vs. microservices, REST vs. GraphQL.
Key elements:
- Each panel gets its own accent color (e.g., green vs. blue)
- Matching structure makes differences obvious
- Punchline callout at bottom explains when to use which
- Color-coded left accent bars on titles

### Pattern: The Agent Loop
Central loop with LLM at center, showing the cycle: user message → LLM decision → tool call → server execution → result feeds back to LLM. Side panel shows exit conditions.
Story: "It's not one call — it's a loop that keeps going until the job is done."
Use for: AI agent architectures, agentic workflows, autonomous systems.
Key elements:
- Circular dashed arrow showing the iteration loop
- Central LLM card with amber border
- Side panel with "EXITS WHEN" conditions
- Green for success exit, amber for limit hit, red for error

### Pattern: The Context/Capacity Bar
Horizontal stacked bar showing how capacity fills over time. Each segment is a different color. A vertical dashed line marks the limit. Warning callout below.
Story: "Everything has a budget — here's how fast yours gets spent."
Use for: context windows, resource allocation, budget visualization, sprint capacity.
Key elements:
- Horizontal bar with colored segments growing left to right
- Vertical dashed line at the capacity limit
- Labels below each segment
- Contrast callout boxes below (neutral vs. red warning)

### Pattern: The Attribution/Flow Graph
Multi-path routing diagram where inputs on the left flow through processing nodes to outputs on the right. Each path gets its own color. Shared intermediate nodes show convergence.
Story: "Multiple inputs, shared processing, divergent outputs — trace any path."
Use for: data pipelines, feature attribution, multi-language flows, dependency graphs.
Key elements:
- Color-coded paths (one color per input category)
- Shared zones with translucent background
- Solid arrows for direct flow, dashed for indirect/inferred
- Input labels left, output labels right

---

## STEP 5: LAYOUT PLANNING (Before Writing SVG Code)

**Plan the coordinate grid on paper before writing a single `<rect>`.** This prevents the #1 cause of bad diagrams: overlapping elements.

### Sizing Rules

**Element width:**
```
width = max(160, longestLabelTextLength × 9)
```
Always round up to the nearest 10px. For cards with body text, use the longer of the title or the longest body line.

**Element height by content:**
| Content | Height |
|---------|--------|
| Title only | 48-60px |
| Title + subtitle | 70-80px |
| Title + subtitle + description | 90-110px |
| Title + subtitle + description + chips | 130-170px |
| Full card (header + body + chips + insight) | 170-220px |

**Background zone padding:** 50px on all four sides minimum between the outermost elements and the SVG edge.

### Coordinate Grid Planning

Before writing SVG code, sketch a tier-based layout:

```
Tier 0 (y=90):   [Header band — always present]
Tier 1 (y=110):  [Row 1 elements — top content cards]
Tier 2 (y=310):  [Row 2 elements — second row or connectors]
Tier 3 (y=510):  [Row 3 elements — callout/comparison]
Footer (y=H-40): [Attribution line]
```

**Vertical spacing between tiers:** 60px minimum (more for complex diagrams).
**Horizontal spacing between siblings:** 20-40px gap between cards. For 4 cards at 270px wide: x = 40, 330, 620, 910.

### Layout Verification

After planning, check:
- Do all elements fit within the 1200px width (with 40px left/right margin)?
- Is the total height ≤ 900px? If not, split into multiple SVGs.
- Are connected elements close enough that arrows won't cross unrelated content?

---

## STEP 6: ARROW ROUTING & CONNECTIONS

### Arrow Types and When to Use Them

| Arrow type | SVG approach | When to use |
|-----------|-------------|-------------|
| Hand-drawn curve (DEFAULT) | `M x1,y1 C cx1,cy1 cx2,cy2 x2,y2` | **All connections.** This is the default. |
| Elbowed (L-shaped) | `M x1,y1 L x1,y2 L x2,y2` | Cross-lane routing, avoiding overlaps |

**CRITICAL: Never use straight `<line>` elements for arrows.** Straight lines look mechanical and tool-generated. Always use `<path>` with cubic bezier curves (`C`) that have control points offset 5-15px from the straight-line path. This creates the organic, hand-drawn feel that separates artisan craft from tool output.

### The Hand-Drawn Arrow Formula

For a vertical arrow from (x, y1) to (x, y2):
```xml
<!-- Organic vertical arrow — control points wobble 3px left/right -->
<path d="M x,y1 C x+3,y1+h/3 x-3,y1+2h/3 x,y2" stroke="#B0B8C4" stroke-width="2.5" stroke-dasharray="5,4" fill="none" stroke-linecap="round"/>
<polygon points="x-6,y2-3 x,y2+8 x+6,y2-3" fill="#B0B8C4"/>
```

For a diagonal arrow from (x1, y1) to (x2, y2):
```xml
<!-- Organic diagonal — single control point creates a gentle arc -->
<path d="M x1,y1 C midX-10,midY+8 midX+10,midY-8 x2,y2" stroke="#B0B8C4" stroke-width="2" fill="none" stroke-linecap="round"/>
```

### Arrow Styling Rules

1. **Always `stroke-linecap="round"`.** This is non-negotiable. Square caps look mechanical.
2. **Arrow color: `#B0B8C4`** — darker than `#D1D5DB` (old default), visible at small sizes, but still recedes behind content.
3. **Stroke width: 2-2.5px** for arrows, 2px for connection lines. Thinner disappears at GitHub rendering scale.
4. **Dashed arrows: `stroke-dasharray="5,4"`** — slightly longer dashes than the old `4,3`, more organic rhythm.
5. **Endpoint dots: `r="3.5"` circles** in `#B0B8C4` — marks where connections land. Slightly larger than before.
6. **Never accept crossing arrows.** If two arrows must cross, rearrange the elements.
7. **Arrow gap:** Leave 25-30px between the source element's edge and the arrow start.
8. **Arrowhead sizing:** 10-12px. Use `<polygon>` not `<marker>` for consistent browser rendering.
9. **Labels on arrows:** Place midway along the path, 12px above the line. 11px font, bold, semantic color.

---

## STEP 7: QUALITY GATE (Mandatory — Run After Every SVG)

**Stop. Verify ALL of these before sharing the SVG.** This is not optional.

### Text & Readability
- [ ] **No truncated text.** Every label fits within its container. Run the sizing rule: `width = max(160, textLength × 9)`.
- [ ] Background is `#FAFAF8` (warm off-white), never pure white or dark
- [ ] **Body text is `#374151`** (not `#5F6B7A` — that's too faint at GitHub scale). Dark enough to read at any zoom level.
- [ ] **Secondary/meta text is `#6B7280`** (not `#9CA3AF` — that vanishes at small sizes). Footers, faded skill lists, step labels.
- [ ] Minimum font size is 11px; body text is 13-14px
- [ ] White text ONLY appears on solid color header bars (with font-weight 700+ and size 16px+)
- [ ] Every text element has `font-family="Inter, Segoe UI, sans-serif"`

### Layout & Spacing
- [ ] **No overlapping elements.** Check every element pair — rectangles, text, chips. Zero tolerance.
- [ ] **No arrow-text overlap.** Arrows must not pass through text labels or card bodies.
- [ ] Width is 1200px, height ≤ 900px
- [ ] Background zone padding: ≥ 50px from outermost elements to SVG edges
- [ ] Consistent spacing: 20-40px gaps between sibling elements, 60px between tiers
- [ ] All cards use `filter="url(#s)"` for consistent shadows
- [ ] Rounded corners: 14-16px for cards, 8px for chips, 18px for badges

### Arrows & Connections
- [ ] **No straight `<line>` arrows.** All connections use `<path>` with bezier curves. No exceptions.
- [ ] All paths have `stroke-linecap="round"` — square caps look mechanical.
- [ ] Arrow stroke color is `#B0B8C4` (not `#D1D5DB` — too faint at small sizes).
- [ ] Arrow stroke width is 2-2.5px (not 1.5 — disappears at GitHub scale).
- [ ] **No crossing arrows.** If arrows cross, rearrange elements first.
- [ ] Arrow gaps: 25-30px clearance from element edges
- [ ] Every arrow has a visible arrowhead (polygon, not marker)
- [ ] Arrow labels positioned midway, 12px above the line

### Color Discipline
- [ ] Maximum 3 color families per diagram (plus neutral)
- [ ] Each color family used consistently (header = saturated, bg = pastel, text = dark)
- [ ] No two adjacent elements share the same color family unless intentional grouping

### Story & Copy
- [ ] Depth label present at top (Comprehensive or Executive Summary)
- [ ] One clear narrative arc: setup → content → punchline
- [ ] **Punchline callout box contains a memorable, quotable line** — the kind of sentence people screenshot. Not a summary. An insight.
- [ ] Footer includes attribution or context
- [ ] Headlines reframe, not describe
- [ ] No filler words: leverage, utilize, comprehensive, robust, streamline
- [ ] Specific numbers used where possible
- [ ] Card descriptions are 2-3 lines maximum

### The Quotable Punchline Test
Every diagram's callout box must pass this test: **would someone screenshot this line and share it?** If not, rewrite it.

Good punchlines:
- "These don't produce documents. They produce confidence that the documents are worth writing."
- "The ask was vague. The output was surgical."
- "A framework that doesn't know its own limits is more dangerous than having no framework at all."

Bad punchlines (summaries, not insights):
- "All five domains are covered in the judgment layer."
- "The system produces ship-ready artifacts."
- "Every skill has been tested and validated."

### Final Sanity Check
- [ ] Open in browser — all text readable without zooming
- [ ] Squint test — can you still read the key message?
- [ ] 3-second test — is the story obvious to a first-time viewer?
- [ ] No orphaned elements (floating text, disconnected arrows, dead-end paths)

---

## STEP 8: ITERATIVE REFINEMENT WORKFLOW

Complex diagrams rarely come out perfect on the first pass. Use this loop:

### The Describe → Evaluate → Fix → Verify Loop

1. **Describe** — Write the SVG code for the full diagram.
2. **Evaluate** — Run every item in the Quality Gate (Step 7). Be ruthless.
3. **Fix** — Address each failure. Common fixes:
   - Text overflow → shorten label OR widen container using sizing rule
   - Overlap → increase tier spacing OR rearrange grid positions
   - Crossing arrows → swap element positions until arrows flow cleanly
   - Readability failure → check color pairing against palette reference
4. **Verify** — Re-run the Quality Gate. Repeat until zero failures.

### Common Iteration Patterns

| Problem found | Root cause | Fix strategy |
|--------------|-----------|-------------|
| Cards overlapping | Didn't plan coordinate grid | Go back to Step 5, sketch tier layout |
| Text truncated in cards | Card width too narrow for content | Apply `width = max(160, textLength × 9)` |
| Arrows crossing each other | Elements in wrong positions | Swap positions so flow direction is consistent |
| Diagram exceeds 900px height | Too much content for one SVG | Split into 2 diagrams by story arc |
| Colors feel chaotic | More than 3 color families | Reduce to 2-3 families, use neutral for structure |
| Callout box feels disconnected | Placed too far from content it references | Move within 20px of the element it comments on |

### When to Split vs. When to Simplify

- **Split** when you have two distinct stories (e.g., architecture + worked example)
- **Simplify** when you have one story with too many details (e.g., show top 5-8 items, not all 25)
- **Never** try to fix a too-complex diagram by shrinking text or reducing spacing — that's a readability death spiral

---

## STEP 9: MULTI-DIAGRAM STRATEGY

When content is too rich for one SVG (often the case):

1. **Break by story, not by data.** Each SVG = one narrative.
2. **Name sequentially:** `01-overview.svg`, `02-detail.svg`, `03-example.svg`
3. **Each stands alone.** Viewer should understand one diagram without seeing others.
4. **Consistent color mapping.** If teal = thinking in diagram 1, teal = thinking everywhere.
5. **Maximum 6 diagrams per set.** If you need more, your architecture needs simplification.

### Naming convention

```
{NN}-{descriptive-slug}.svg

01-architecture-overview.svg
02-thinking-layer.svg
03-judgment-layer.svg
04-workflow-paths.svg
05-import-chain.svg
```

---

## ERROR RECOVERY

### Common SVG rendering issues

| Problem | Cause | Fix |
|---------|-------|-----|
| Text overflows card | Text width exceeds card width | Apply sizing rule: `width = max(160, textLength × 9)` |
| Text truncated or clipped | Container too small for content | Recalculate: count characters × 9, add 40px padding |
| Elements overlap | No coordinate grid planning | Go back to Step 5, plan tiers with 60px vertical gaps |
| Arrows cross each other | Element positions create crossing paths | Swap element positions until all arrows flow one direction |
| Arrow passes through text | Arrow route not planned | Use elbowed routing (Step 6) to route around obstacles |
| Shadow filter missing | `filter="url(#s)"` references undefined filter | Ensure `<defs>` block with filter `id="s"` exists at top |
| Colors look washed out | Using the pastel bg color for text | Use the dark text color from the color family |
| Card headers have rounded bottom | Only one rect for header | Use two overlapping rects (rounded + flat bottom filler) |
| Text invisible | White text on white or light background | White text only on saturated header bars (700+ weight, 16px+) |
| Diagram too tall for GitHub | Height exceeds comfortable scroll | Break into multiple SVGs, max 900px each |
| Chips overflow card width | Too many chips in one row | Wrap to multiple rows, or reduce chip count to 3-4 per row |
| Spacing looks uneven | Mixed gap sizes between elements | Standardize: 20px within groups, 40px between groups, 60px between tiers |

### Testing

Open the SVG in a browser to verify rendering. Check:
1. All text readable without zooming
2. Color contrast passes squint test (squint at screen — can you still read it?)
3. Story arc clear: "What is this about?" answerable in 3 seconds
4. No orphaned elements (floating text, disconnected arrows)
5. No overlapping elements (check every pair of rects, especially near edges)
6. All arrows flow in a consistent direction (no backtracking)
7. Sizing rule holds: every container is wide enough for its longest text line

---

## GITHUB SVG RENDERING

GitHub sanitizes SVGs aggressively. Know what survives and what doesn't.

### What works on GitHub
- `<img src="filename.svg">` in README (relative paths)
- `<img>` tags with `?sanitize=true` for raw URLs
- Basic shapes: `<rect>`, `<circle>`, `<ellipse>`, `<line>`, `<path>`, `<polygon>`
- `<text>`, `<tspan>` with inline attributes
- `<g>` grouping with transforms
- `viewBox` + responsive sizing
- Inline `style` attributes on elements

### What GitHub strips (SVG sanitizer removes these)
- `<script>` tags — completely removed
- `<foreignObject>` — stripped (no HTML-in-SVG)
- Event handlers (`onclick`, `onmouseover`)
- External CSS `<link>` references
- `<use>` with external href
- CSS animations and `@keyframes` inside `<style>` blocks
- `<filter>` elements MAY be stripped — test your specific filter

### Shadow filter fallback
If `<filter>` is stripped by GitHub, your shadows will disappear silently. Fallback:
```xml
<!-- Instead of filter="url(#s)", use a visible stroke as shadow substitute -->
<rect x="102" y="102" width="270" height="170" rx="14" fill="#E5E7EB" opacity="0.3"/>  <!-- shadow rect offset -->
<rect x="100" y="100" width="270" height="170" rx="14" fill="#FFFFFF" stroke="#E5E7EB" stroke-width="1.5"/>
```

### Embedding SVGs in README
```markdown
<!-- Best approach: relative path with img tag -->
<img src="01-architecture-overview.svg" alt="Architecture Overview" width="100%">

<!-- For raw GitHub URLs, add sanitize parameter -->
<img src="https://raw.githubusercontent.com/user/repo/main/diagram.svg?sanitize=true" alt="Diagram">
```

**Always set `alt` text** that describes the diagram's key takeaway, not its structure.

---

## ACCESSIBILITY

### Baseline SVG accessibility (always include)
```xml
<svg xmlns="http://www.w3.org/2000/svg" role="img"
     aria-label="{ONE_SENTENCE_TAKEAWAY}"
     viewBox="0 0 1200 {HEIGHT}" width="1200" height="{HEIGHT}">
  <title>{DIAGRAM_TITLE}</title>
  <desc>{2-3 sentence description of what the diagram shows and its key insight}</desc>
  ...
</svg>
```

Rules:
- `role="img"` tells screen readers this is one image, not a tree of shapes
- `<title>` = the diagram's heading (matches the visible title)
- `<desc>` = what a colleague would say if describing this diagram out loud
- `aria-label` = the one-sentence takeaway for quick scanning
- For purely decorative diagrams (rare): use `aria-hidden="true"` instead

### Text in accompanying documents
When embedding an SVG in a README or document, always include a text summary below:
```markdown
<img src="01-overview.svg" alt="Three-layer architecture: thinking feeds judgment, judgment feeds craft">

> **Visual summary:** The system uses three layers — Thinking (7 foundational skills),
> Judgment (25 domain plugins), and Craft (8 output skills). Each layer imports from
> the one above, so a PRD arrives pre-tested against first principles.
```

---

## TEXT ENCODING & SPECIAL CHARACTERS

- Always use proper XML character escaping: `&` → `&amp;`, `<` → `&lt;`, `>` → `&gt;`
- For quotes in attributes: use `&quot;` or switch quote style
- Emoji work in SVG `<text>` elements but increase file size — use sparingly and only when they add genuine clarity
- Math symbols: use Unicode directly (`→` for arrows, `×` for multiply, `≤` for less-equal)
- Monospace text for code literals: `font-family="Consolas, Monaco, monospace"` — use only inside callout boxes for API names, commands, etc.

---

## SIZING UPPER BOUNDS

The sizing formula `width = max(160, textLength × 9)` needs an upper bound to prevent runaway card widths:

```
width = min(max(160, textLength × 9), 520)
```

If text exceeds 520px width:
1. **First choice:** Shorten the text. Better copy is shorter copy.
2. **Second choice:** Break into 2 lines using `<tspan>` elements with `dy="18"`.
3. **Third choice:** Use a wider card format (half-width: 545px) and treat it as a section header, not a card.
4. **Never:** Let a single card exceed 520px unless it's a full-width callout box.

---

## SPACING HIERARCHY (Definitive Reference)

| Context | Gap | When to use |
|---------|-----|-------------|
| Inside card (text padding) | 16px | Between text lines, chip to text |
| Within a group (sibling cards in same row) | 20px | Cards that belong together |
| Between groups (two sets of related cards) | 40px | Visually separate but connected |
| Between tiers/layers | 60px | Major structural breaks |
| Card internal padding (edges to content) | 16-20px | Left/right/bottom margins inside cards |
| Background zone to SVG edge | 50px min | Breathing room around all content |
| Arrow label to arrow line | 12px | Labels above connection paths |
| Chip to chip (horizontal) | 8-10px | Tags/labels inside a card row |

---

## VISUAL SUMMARY MODE (Cross-Skill Integration)

**This is the killer feature.** When ANY other skill produces output, the excalidraw-svg skill can create a visual summary that makes the deliverable 10x more impactful.

### How it works
After a skill generates its primary output (PRD, spec, analysis, roadmap, etc.), create ONE Excalidraw SVG that captures the essence of that output in a single glanceable image.

### Visual summary guidelines
1. **Pick the right pattern:** Match the output type to a visual pattern:
   - PRD/Spec → Flow Chain (user problem → solution → metrics)
   - Strategy/Roadmap → Layer Cake or Timeline
   - Analysis/Research → Grid of Equals (key findings as cards)
   - Comparison/Decision → Contrast Panel (option A vs. option B)
   - Architecture/System Design → Grouped Containers or Hub-Spoke
   - Sprint Plan → Timeline with capacity bar
   - Stakeholder Update → Step-by-Step Flow (what happened → what's next)

2. **Content rules for summaries:**
   - Maximum 6-8 elements — ruthlessly prioritize
   - Each element = one key insight, not a data dump
   - Title = the document's thesis, not its name
   - Use the "Quick Check — Executive Summary" depth label
   - Include a punchline callout with the "so what?"

3. **File naming:** `{output-name}-visual-summary.svg`
   Example: `ai-code-review-prd-visual-summary.svg`

4. **Embedding:** Place the SVG at the top of the document or immediately after the executive summary section.

### Example: Visual summary for a PRD
```
Title: "AI Code Review — Why the 10-minute review window changes everything"
Depth: Quick Check — Executive Summary
Pattern: Flow Chain (4 boxes)
Elements:
  1. Problem card: "Reviews take 4 hours → PR authors context-switch 3x"
  2. Solution card: "AI pre-review in 10 min → human reviews only the judgment calls"
  3. Metrics card: "Target: 60% reduction in review cycle time"
  4. Risk callout: "False positive rate must stay below 5% or devs ignore it"
Punchline: "The goal isn't replacing reviewers — it's giving them a head start."
```

---

## EXCALIDRAW LIBRARY REFERENCE

See [references/excalidraw-libraries.md](references/excalidraw-libraries.md) for the full catalog of 40+ Excalidraw component libraries and external resources. Key categories:

| Category | Best libraries | Use when |
|----------|---------------|----------|
| Architecture | Software Architecture, System Design Components | System design, microservices, cloud |
| Cloud | AWS Icons, Azure Icons, GCP/Google Icons | Cloud infrastructure diagrams |
| UI/UX | Forms, Basic UX Wireframing, Lo-Fi Kit | Wireframes, prototypes, user flows |
| Data/AI | Data Viz, Deep Learning, Data Platform | ML pipelines, data architecture |
| People | Stick Figures, Storytelling, Collaboration | User journeys, team structures |
| Icons | Software Logos, Technology Logos, Awesome Icons | Any diagram needing recognizable branding |
| Modeling | UML & ER, Decision Flow Control, C4 | Technical modeling, entity relationships |
| Strategy | Business Model Templates, Customer Journey | Business strategy, product planning |
