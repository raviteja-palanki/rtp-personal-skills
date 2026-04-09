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

## IDEO DESIGN DIRECTOR REVIEW

Before creating any diagram, internalize these five principles from IDEO Design Director methodology. They separate functional diagrams from ones that influence decisions.

### 1. Human-Centered Framing
Diagrams are not system dumps. They answer the viewer's question, not the system's structure.

**Wrong:** "Here are all the components."
**Right:** "Here's what the viewer needs to decide / understand / build."

Example: Instead of showing "Orchestrator → LLM → Tool Calling → State Management → Execution," frame it as "How does the orchestrator handle a real request? Watch step-by-step."

### 2. Prototype Thinking
First diagrams are prototypes. Expect 2-3 iterations. Build for feedback, not perfection.

- Start rough. Get the story right first.
- After feedback: refine layout, tighten copy, polish colors.
- Never spend 2 hours perfecting a layout before getting feedback — you'll throw it away anyway.

### 3. Show, Don't Tell
Use visual metaphors. A funnel IS the story of filtering. A bridge IS connection. A layer cake IS inheritance.

**Anti-pattern:** Text-heavy boxes with arrows labeled "sends," "receives," "processes." That's a data structure diagram, not a story.

**Pattern:** The shape, color, and flow carry meaning. Text amplifies, not explains.

### 4. Emotional Design
Diagrams should make the viewer FEEL something:
- **Confidence:** Clear path forward, no ambiguity.
- **Urgency:** Red highlights what breaks. Moss highlights what works.
- **Clarity:** Even complex systems feel understandable.

If a diagram doesn't create an emotional response, it's a data dump. Rework it.

### 5. The "Walk the Wall" Test
Would this diagram survive being printed at A3 and pinned to a wall in your office? Would someone walking by stop, read it, and get the main point in 10 seconds?

If yes, it works. If no, simplify the story or split into multiple diagrams.

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
  <text x="{CENTER}" y="62" text-anchor="middle" fill="#5F6B7A" font-size="15" font-family="Inter, sans-serif">{DEPTH_LABEL} · {SUBTITLE}</text>

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

**Quick reference — the 8 Luminous Pastel families (solid headers + optional gradient accents):**

| Semantic | Header solid | Accent gradient | Card bg | Chip bg | Chip border | Text dark | Text medium |
|----------|--------------|-----------------|---------|---------|-------------|-----------|-------------|
| Rose Quartz (thinking) | `#D4789B` | `#E8A0BF` → `#D4789B` | `#FFF5F8` | `#FFE4ED` | `#F5B8CB` | `#8B3A5A` | `#A64D6E` |
| Wisteria (judgment) | `#9478B8` | `#B8A0D6` → `#9478B8` | `#F8F5FF` | `#EDE5F8` | `#CDBEE8` | `#5B3E7A` | `#7556A0` |
| Honey Amber (craft) | `#D4A54A` | `#E8C170` → `#D4A54A` | `#FFFCF5` | `#FFF3D6` | `#F0D78A` | `#7A5A1E` | `#946E2A` |
| Celadon (eval/quality) | `#6BA898` | `#8CC5B0` → `#6BA898` | `#F2FAF6` | `#DFF0E8` | `#A8D4C0` | `#2E6B54` | `#3D8068` |
| Glacier (tech/data) | `#5A9ABE` | `#7CB8D8` → `#5A9ABE` | `#F3F9FD` | `#DFF0FA` | `#A4D2E8` | `#2A5F7A` | `#3A7598` |
| Coral (agents/danger) | `#D47B64` | `#E89880` → `#D47B64` | `#FFF7F4` | `#FFE8E0` | `#F0BCA8` | `#8B4434` | `#A45840` |
| Moss (success) | `#7BA86C` | `#9AC08A` → `#7BA86C` | `#F5FAF2` | `#E2F0D8` | `#B0D4A0` | `#3A5E2E` | `#4E7A40` |
| Neutral (structure) | — | — | `#FFFFFF` | `#F8F7F5` | `#E2DFD8` | `#1B1B1F` | `#4A4540` |

**Selection rule:** Pick 2-3 primary families per diagram. Use solid header colors for primary fill. Optional gradient accents below for visual richness. Use neutral for structure.

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

**Updated approach for readability:** Solid header color (the darker endpoint of each family's gradient) with optional gradient accent bar below.

```xml
<!-- Standard card: 270px wide, height varies -->
<rect x="{X}" y="{Y}" width="270" height="{H}" rx="14" fill="#FFFFFF" stroke="{BORDER}" stroke-width="2" filter="url(#s)"/>
<!-- Solid colored header bar (high-contrast, WCAG-compliant) -->
<rect x="{X}" y="{Y}" width="270" height="44" rx="14" fill="{HEADER_SOLID_COLOR}"/>
<!-- Optional gradient accent bar below for visual richness -->
<rect x="{X}" y="{Y+44}" width="270" height="12" rx="0" fill="url(#{FAMILY}-accent)"/>
<!-- Header text (white on solid color = guaranteed readability) -->
<text x="{CENTER_X}" y="{Y+29}" text-anchor="middle" fill="#FFFFFF" font-size="16" font-weight="700" font-family="Inter, sans-serif">{CARD_TITLE}</text>
```

**Color selection:** Use the darker endpoint (gradient end color) as `HEADER_SOLID_COLOR`. See color-palette.md for specific hex values per family.

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

### Pattern: The Deliverable Map
Show agents/skills and what tangible outputs each produces. Critical for communicating value when describing multi-agent systems.
Story: "Each agent does something specific. Here's what you GET from each."
Use for: skill/agent system diagrams, service catalogs, capability maps, orchestrator systems.
Key elements:
- Agent/skill card with colored header
- "Delivers:" section below the description
- 2-3 deliverables shown as document-chip items (small page-shaped icons with labels)
- Deliverable items use semantic color matching the agent's header
- Optional: estimate cards below each deliverable (time estimate, complexity)

Example structure:
```xml
<!-- Agent card with deliverables section -->
<rect x="100" y="100" width="270" height="200" rx="14" fill="#FFFFFF" stroke="#E2DFD8" stroke-width="2" filter="url(#s)"/>
<rect x="100" y="100" width="270" height="44" rx="14" fill="#D4789B"/>
<text x="235" y="129" text-anchor="middle" fill="#FFFFFF" font-size="16" font-weight="700">Agent Name</text>

<!-- Description -->
<text x="120" y="160" fill="#1B1B1F" font-size="13" font-weight="600">Delivers:</text>

<!-- Deliverable chips -->
<rect x="120" y="175" width="120" height="24" rx="6" fill="#FFE4ED" stroke="#F5B8CB" stroke-width="1"/>
<text x="180" y="188" text-anchor="middle" fill="#8B3A5A" font-size="11" font-weight="600">PRD + Spec</text>

<rect x="120" y="205" width="120" height="24" rx="6" fill="#FFE4ED" stroke="#F5B8CB" stroke-width="1"/>
<text x="180" y="218" text-anchor="middle" fill="#8B3A5A" font-size="11" font-weight="600">Risk Register</text>

<rect x="120" y="235" width="120" height="24" rx="6" fill="#FFE4ED" stroke="#F5B8CB" stroke-width="1"/>
<text x="180" y="248" text-anchor="middle" fill="#8B3A5A" font-size="11" font-weight="600">Validation Report</text>
```

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

## EXECUTIVE STORYTELLING

When diagrams are shared in boardrooms, pitch decks, or strategic reviews, they need different framing. This section is not about system internals — it's about outcomes and decisions.

### The "Boardroom Test"
Would this diagram work in a board presentation? No jargon. No system internals. Only outcomes and decisions.

**Bad:** "Orchestrator receives task, invokes LLM with context window constraint, tool-calls execute asynchronously."
**Good:** "The system handles complex tasks step-by-step. Each step completes before moving forward. Failures are caught early."

**The question:** Does the board member immediately understand what this solves FOR THEM? Not what it does. What value it creates.

### Narrative Arc for Business Audiences

Every diagram aimed at executives should follow this three-act structure. Use color to reinforce the narrative:

1. **Problem** — What breaks without this? (Red/Coral if it's a pain point)
2. **Mechanism** — How does it work? (Blue/Neutral if it's explanation)
3. **Impact** — What becomes possible? (Green/Moss for the payoff)

The color carries the narrative. An executive should see the progression without reading a word.

### The "So What?" Must Be Unavoidable

After explaining the mechanism, the callout box at the bottom must be the most visually prominent element (after the title).

**Rule:** The punchline callout gets:
- Larger font (16px+ vs. 13px body text)
- Brightest color (often Moss for positive, Coral for risk)
- Bold weight (700+)
- Specific number if possible: "49% error reduction" > "significant improvement"

### Data Points as Persuasion

Include 1-2 specific numbers per diagram:
- "Over 90% of evaluations surface this issue within 2 rounds"
- "Typical ROI payoff: 4 weeks"
- "Reduces manual review from 6 hours to 18 minutes"

Numbers are far more persuasive than adjectives. "Dramatic" means nothing. "3.2x faster" means action.

### Executive Callout Box Format

```xml
<!-- Executive "so what?" box at bottom -->
<rect x="100" y="720" width="1000" height="80" rx="14" fill="#F5FAF2" stroke="#B0D4A0" stroke-width="2" filter="url(#s)"/>
<text x="600" y="750" text-anchor="middle" fill="#3A5E2E" font-size="18" font-weight="800" font-family="Inter, sans-serif">Result: 49% reduction in manual review time</text>
<text x="600" y="778" text-anchor="middle" fill="#4A4540" font-size="14" font-family="Inter, sans-serif">First-time adoption: 2 weeks. Full ROI: 6 months.</text>
```

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

### Validated Pattern: Curved Bezier Arrows
**Confirmed effective:** Curved bezier arrows with labeled midpoints are the preferred connection style across diagrams. They communicate relationships clearly without visual harshness, and they have been validated in interview and presentation contexts. Keep using this — it works.

---

### Arrow Types and When to Use Them

| Arrow type | SVG approach | When to use |
|-----------|-------------|-------------|
| Straight horizontal | `M x1,y L x2,y` | Same-row connections, flow chains |
| Straight vertical | `M x,y1 L x,y2` | Parent-child, top-down hierarchies |
| Curved (bezier) | `M x1,y1 C cx1,cy1 cx2,cy2 x2,y2` | Layer-to-layer flows, import chains |
| Elbowed (L-shaped) | `M x1,y1 L x1,y2 L x2,y2` | Cross-lane routing, avoiding overlaps |

### Arrow Routing Rules

1. **Never accept crossing arrows.** If two arrows must cross, rearrange the elements. Crossing arrows signal a layout problem, not an arrow problem.
2. **Arrow gap:** Leave 25-30px between the source element's edge and the arrow start. Same for the target.
3. **Arrowhead sizing:** 10-12px for standard arrows. Use `<polygon>` not `<marker>` for consistent rendering across browsers.
4. **Labels on arrows:** Place midway along the path, 12px above the line. Use 11px font, bold weight, in the semantic color of the connection.
5. **Curved arrows with waypoints:** For connections that need to route around obstacles:
   ```xml
   <!-- Curve around an obstacle: control points push the curve away -->
   <path d="M 200,300 C 200,250 400,250 400,300" stroke="#9CA3AF" stroke-width="2" fill="none"/>
   ```
6. **Elbowed arrows for cross-lane routing:**
   ```xml
   <!-- L-shaped: down then right -->
   <path d="M 200,300 L 200,400 L 500,400" stroke="#9CA3AF" stroke-width="2" fill="none" stroke-linejoin="round"/>
   ```

---

## STEP 7: QUALITY GATE (Mandatory — Run After Every SVG)

**Stop. Verify ALL of these before sharing the SVG.** This is not optional.

### Text & Readability
- [ ] **No truncated text.** Every label fits within its container. Run the sizing rule: `width = max(160, textLength × 9)`.
- [ ] Background is `#FAFAF8` (warm off-white), never pure white or dark
- [ ] All body text is `#1B1B1F` or `#5F6B7A` — never grey-on-grey
- [ ] Minimum font size is 11px; body text is 13-14px
- [ ] White text ONLY appears on solid color header bars (with font-weight 700+ and size 16px+)
- [ ] Every text element has `font-family="Inter, Segoe UI, sans-serif"`

### Layout & Spacing
- [ ] **No overlapping elements.** Check every element pair — rectangles, text, chips. Zero tolerance.
- [ ] **No arrow-text overlap.** Arrows must not pass through text labels or card bodies.
- [ ] Width is 1200px, height ≤ 900px
- [ ] Consistent spacing: 20-40px gaps between sibling elements, 60px between tiers
- [ ] All cards use `filter="url(#s)"` for consistent shadows
- [ ] Rounded corners: 14-16px for cards, 8px for chips, 18px for badges

### Border Padding Verification (The Four-Edge Gate)
**Check all four edges explicitly. This is where SVGs most often fail.**
- [ ] **TOP edge:** No element (rect, text, chip) starts above y=50. Title text baseline ≥ y=60.
- [ ] **BOTTOM edge:** No element extends below `(viewBox height - 50)`. Footer text baseline + font-size must be ≤ `(viewBox height - 40)`. This is the #1 failure — footers and bottom callouts overflow or collide with content above them.
- [ ] **LEFT edge:** No element starts before x=50. Text anchored `text-anchor="start"` must have x ≥ 50.
- [ ] **RIGHT edge:** No element (rect x + width, or text x + estimated text width) extends past `(viewBox width - 50)`.
- [ ] **Bottom callout/footer clearance:** If the diagram has a footer, attribution, or bottom callout box, verify ≥ 30px clear space between the lowest content element and the top of the footer. Footers must never overlap the last row of cards.
- [ ] **Verification method:** For every text element near an edge (within 80px), manually check: `element_y + font_size < viewBox_height - 40`. For rects: `rect_y + rect_height < viewBox_height - 50`.

### Arrows & Connections
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
- [ ] Callout or comparison box delivers the "so what?" at the bottom
- [ ] Footer includes attribution or context
- [ ] Headlines reframe, not describe
- [ ] No filler words: leverage, utilize, comprehensive, robust, streamline
- [ ] Specific numbers used where possible
- [ ] Card descriptions are 2-3 lines maximum

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
