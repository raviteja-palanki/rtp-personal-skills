# Visual summary protocol

Reference revision 1.4.1 — reviewed 13 September 2026.

Create a visual summary when the user asks for one or when a framework, comparison, dependency, or flow becomes easier to understand visually. A brief answer, simple edit, or already clear list may need no image. Complete the requested primary artifact without treating a diagram as an automatic requirement of every skill.

Read the source output and identify the important takeaway. Preserve its evidence, trade-offs, and unresolved conditions. Choose the pattern that represents the relationship accurately:

| Output | Starting pattern | Show |
|---|---|---|
| PRD or feature specification | Flow Chain | Problem, proposed behavior, outcome checks, and relevant risk |
| Strategy or roadmap | Layers or Timeline | Decisions, dependencies, and phases |
| Research or analysis | Grouped Cards | Findings with their relative weight and limits |
| Comparison or decision | Contrast Panels | Options against comparable criteria |
| Architecture | Grouped Containers | Components, boundaries, and connections |
| Planning | Timeline and Capacity Bar | Work, dependencies, units, and capacity |
| Stakeholder update | Sequence | What changed and the next decision |
| Evaluation or metrics | Metric Cards and Callout | Measures, denominators, and interpretation |
| Safety or trust | Layers | Risks, controls, remaining exposure, and ownership |
| Agent design | Agentic Loop | Request, tools, review, output, and stop or failure paths |

Six to eight major elements are a useful starting limit for a summary. Keep more when omission would distort the conclusion; otherwise provide a separate detail view. Use a takeaway title and a callout only when they add distinct information. The label “Quick Check — Executive Summary” is optional.

Apply the main skill's text, geometry, contrast, and rendered-review guidance. Name the file `{output-name}-visual-summary.svg` when that convention fits the project. Place it near the explanation it supports and provide useful alternative text. Do not insert an image into another application or publish it unless the user has authorized that action.

For other skills, a reusable instruction is: “Where a diagram would make this result easier to understand, create a visual summary using the Excalidraw SVG skill. Preserve the source's meaning and verification limits, and follow the destination's artifact requirements.”
