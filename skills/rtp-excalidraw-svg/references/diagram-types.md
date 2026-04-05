# Diagram Type Catalog

## 1. Layer Cards (Architecture Diagrams)

**Story:** "These layers build on each other. Nothing ships without passing through all of them."

**Layout:** 2-3 large cards horizontally, connected by labeled arrows.
Each card has a colored header bar, subtitle, description, and chip tags.

**Dimensions:** 1200 × 600-720px

**Structure:**
```
[Header Band with title + depth label]

[Card 1: Layer A]  →feeds→  [Card 2: Layer B]  →feeds→  [Card 3: Layer C]
 Header bar (teal)            Header bar (purple)          Header bar (amber)
 Subtitle                     Subtitle                     Subtitle
 Description                  Description                  Description
 [chip] [chip] [chip]         [chip] [chip]                [chip] [chip]

[Story callout: "Why this architecture matters"]

[Footer]
```

**When to use:** System architecture, skill/layer maps, build pipelines,
maturity models, any "A feeds B feeds C" narrative.

---

## 2. Grid Cards (Feature Catalogs)

**Story:** "Here's the complete set. Each one is distinct. Pick what you need."

**Layout:** 2×3, 3×3, or 4×2 grid of uniform cards with colored headers.
Row 2 can have fewer cards (centered).

**Dimensions:** 1200 × 500-680px

**Structure:**
```
[Header Band]

[Card] [Card] [Card] [Card]    ← Row 1 (4 cards @ 270px)
  [Card] [Card] [Card]         ← Row 2 (3 cards, centered)

[Story callout]
[Footer]
```

**Card sizing:**
- 4 per row: 270px wide, 20px gap → starts at x=40, 330, 620, 910
- 3 per row: 270px wide, centered → starts at x=135, 465, 795
- 2 per row (wide): 555px wide → starts at x=40, 615

**When to use:** Skill catalogs, tool comparisons, feature lists,
option menus, team capabilities.

---

## 3. Flow Chain (Process Flows)

**Story:** "Start here. End there. Each step transforms the input."

**Layout:** Horizontal chain of boxes connected by arrows.
Optional branching with decision diamonds or split paths.

**Dimensions:** 1200 × 300-500px

**Structure:**
```
[Header Band]

[Start Box] → [Step 1] → [Step 2] → [Step 3] → [End Box]
  "input"      "verb"     "verb"     "verb"     "output"

[Before/After comparison or Story callout]
[Footer]
```

**Box sizing:** 180-200px wide, 48-54px tall, 12px rounded corners.
Arrow spacing: 25-30px gap between box edge and arrow tip.

**When to use:** Import chains, data pipelines, user journeys,
deployment flows, decision processes.

---

## 4. Grouped Sections (Plugin/Domain Maps)

**Story:** "Five domains, each with its own specialization. Together they cover everything."

**Layout:** Large containers with colored borders, each holding
a subtitle and multiple chip tags. Containers stack or tile.

**Dimensions:** 1200 × 600-820px

**Structure:**
```
[Header Band]

[Container 1: Domain A]     [Container 2: Domain B]
 Header bar (color A)        Header bar (color B)
 Description                 Description
 [chip] [chip] [chip]        [chip] [chip]
 [chip] [chip]               [chip]
 Insight line                 Insight line

[Container 3] [Container 4] [Container 5]
 ...           ...            ...

[Story callout]
[Footer]
```

**Container sizing:**
- 2 per row: 555px wide
- 3 per row: 370px wide

**When to use:** Plugin catalogs, department structures, domain maps,
multi-team overviews, capability matrices.

---

## 5. Workflow Selection (Decision Menus)

**Story:** "Six paths. Each for a different situation. Choose yours."

**Layout:** 2×3 grid of workflow cards, each with:
- Colored header bar with workflow name
- Skill count badge (top-right)
- One-sentence description
- Key skills as chips
- "Best for:" guidance line

**Dimensions:** 1200 × 640-740px

**Structure:**
```
[Header Band with "Quick Check — Executive Summary"]

[Workflow 1] [Workflow 2] [Workflow 3]    ← Row 1
[Workflow 4] [Workflow 5] [Workflow 6]    ← Row 2

[How-to-choose guidance box]
[Footer]
```

**Card sizing:** 370px wide, 200px tall, each with different header color.

**When to use:** Workflow menus, playbook selection, decision trees
where the first choice is "which path am I on?"

---

## 6. Walkthrough (Step-by-Step Example)

**Story:** "Here's exactly what happens when you ask X. Watch the chain fire."

**Layout:** Vertical stack of 2-4 large panels (one per layer/stage),
each containing 3-4 output lines showing what each sub-skill produces.
Connected by vertical arrows between panels.

**Dimensions:** 1200 × 600-700px

**Structure:**
```
[Header Band]

[User prompt bubble — dark, centered]
         ↓
[Panel 1: Stage A — wide, light tinted]
 skill-name-1: "output quote"
 skill-name-2: "output quote"
 skill-name-3: "output quote"
         ↓
[Panel 2: Stage B — different color]
 ...
         ↓
[Panel 3: Stage C — different color]
 ...

[Before/After punchline]
```

**Panel sizing:** 1000px wide (centered at x=100), 112-136px tall.
Skill name in bold color, quote in body text.

**When to use:** Worked examples, import chain demonstrations,
"what actually happens" explanations, debug traces.

---

## 7. Comparison (Before/After, With/Without)

**Story:** "This is the gap. This is what closes it."

**Layout:** Two panels side by side. Left panel red-tinted (problem/without).
Right panel green-tinted (solution/with).

**Dimensions:** 1200 × 200-400px (often used as a section within a larger diagram)

**Structure:**
```
[Red panel: "Without X"]        [Green panel: "With X"]
 Headline                        Headline
 Specific bad outcome             Specific good outcome
```

**Panel sizing:** Each ~530px wide with 20px gap between them.

**When to use:** Value propositions, before/after comparisons,
risk/mitigation pairs, old-process vs new-process.

---

## Combining Types

Most real diagrams combine 2-3 types. Common combinations:

| Primary | Combined with | Example |
|---------|--------------|---------|
| Layer Cards | Flow Chain | Architecture overview with import chain at bottom |
| Grid Cards | Story Callout | Skill catalog with "why this matters" conclusion |
| Walkthrough | Comparison | Worked example ending with before/after punchline |
| Workflow Selection | How-to-choose box | Decision menu with guidance section |
| Grouped Sections | Insight lines | Domain map where each section has its own punchline |

The rule: **the combination should serve the story, not show off technique.**
If two types can tell the story, use one. Add the second only if it adds clarity.
