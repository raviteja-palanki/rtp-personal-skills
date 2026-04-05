# Visual Summary Protocol

## Purpose
Every skill output should end with an Excalidraw SVG visual summary — a single, beautiful diagram that captures the essence of the analysis in a glanceable image. This makes every deliverable dramatically more impactful.

## When to generate a visual summary
- After completing ANY skill's primary analysis or output
- When the output contains a framework, decision, comparison, flow, or architecture
- When the user would benefit from a "one-image takeaway" of the work

## How to create the visual summary

### Step 1: Identify the story
Read the skill's output and find the single most important insight. This becomes the diagram's title.

### Step 2: Pick a pattern
Match the output type to the best visual pattern:

| Output type | Best pattern | Elements |
|------------|-------------|----------|
| PRD / Feature spec | Flow Chain | Problem → Solution → Metrics → Risk |
| Strategy / Roadmap | Layer Cake or Timeline | Phases with key decisions |
| Analysis / Research | Grid of Equals | Key findings as equal-weight cards |
| Comparison / Decision | Contrast Panel | Option A vs. Option B |
| Architecture / Design | Grouped Containers | Components + connections |
| Sprint / Planning | Timeline + Capacity Bar | Tasks + capacity visualization |
| Stakeholder Update | Step-by-Step Flow | What happened → what's next |
| Evaluation / Metrics | Grid + Callout | Metric cards + insight punchline |
| Safety / Trust | Layer Cake | Risk layers with mitigations |
| Agent Design | Agent Loop | User → Agent → Tools → Result cycle |

### Step 3: Apply the excalidraw-svg design system
- Use `Quick Check — Executive Summary` depth label
- Maximum 6-8 elements (ruthlessly prioritize)
- Title = the document's thesis, not its name
- Include a punchline callout with the "so what?"
- Follow all color, typography, and layout rules from SKILL.md

### Step 4: Name and embed
- File: `{skill-output-name}-visual-summary.svg`
- Place at the top of the output or immediately after the executive summary

## The visual summary instruction (add to every skill)
```
## VISUAL SUMMARY
After completing the primary output, invoke the excalidraw-svg skill to create a single Excalidraw SVG visual summary. This diagram captures the essence of the analysis in one glanceable image. Follow the Visual Summary Protocol in excalidraw-svg/references/visual-summary-protocol.md.
```
