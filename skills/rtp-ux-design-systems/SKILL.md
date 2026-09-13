---
name: rtp-ux-design-systems
version: v1.3.1_latest
description: 'Design, review, or explore a visual system for a specific audience and task. Use for UI/UX, dashboards, components, diagrams, presentations, or comparisons of company design patterns. Combine color, typography, layout, material, motion, and clear interface copy with practical usability and accessibility checks. Use OKLCH as a palette tool while validating actual contrast, gamut, and rendered states. Read selected company references as inspiration snapshots, not guaranteed current production specifications. For Ravi’s own surfaces, follow the current personal-branding and project guidance before borrowing another aesthetic. Choose purposeful patterns instead of automatic gradients, card grids, or arbitrary novelty. Includes seven design lenses, three working modes, a company-reference index, research bookmarks, and scoped border/LinkedIn examples. Recommend a direction with reasons and report only the checks actually performed.'
---
# UX design systems

Design something that helps the intended person accomplish the intended task. Make a considered choice, explain the important trade-off, and use the finished artifact to test the choice. Color, type, space, material, motion and words work together; none can compensate for a missing action or unreadable information.

This skill offers **Design, Review and Inspire** modes and seven lenses. It draws on Rams, Albers, Tufte, Norman, Alexander and other practitioners as perspectives, not as proof of what any named designer would approve. The company library provides examples to read when relevant; its presence does not mean every system is current or has been reviewed in this session.

## Start with the person, task and governing design

Identify the page or artifact kind, audience, user goal, requested tone, reference signals, existing brand assets, platform and consequential constraints. Use context already supplied. Ask a concise question only if an unresolved choice would materially change the design; do not force a fixed questionnaire.

For a substantial design, state a short design read: “This is a control dashboard for plant managers, with visible status, fast recovery and restrained visual hierarchy.” A small fix can proceed directly without a ceremonial preamble.

**For Ravi's own surfaces**, read the current `rtp-personal-branding` and applicable project specification. His website's fourteen-part design pack is at `1_Projects/1_my-personal-website/1_My Series-MD-FILES/My Design language_website/`. Its series colors, editorial mag-* layer and motion guidance govern current website work. Documents normally use light surfaces; websites and decks normally use dark. The established resume and a requested teaching/client identity can have their own rules.

Company examples, anti-default preferences and the older rainbow/gradient borders do not override that authority. You can design new work within Ravi's identity, not merely review it. For other clients, their brief, accessibility needs and platform constraints remain binding; “non-Ravi” does not mean unconstrained.

## Choose a working mode

| Mode | Process | Useful result |
|---|---|---|
| **Design** | Read the brief; select relevant precedents; develop a coherent system; implement or specify it; check the result | The requested artifact or a project design contract with rationale |
| **Review** | Inspect the actual artifact; identify task and hierarchy; assess color/type/layout/states; prioritize concrete fixes | Specific findings tied to elements and consequences, with verification status |
| **Inspire** | Compare different approaches to the same need; explore a few coherent directions; recommend one | Usually two or three directions with palette, type, layout, mood, trade-offs and selection basis |

Three to five reference systems can help a substantial design; five to ten may help broad exploration. These are optional ranges, not quotas. One well-matched precedent or no external precedent can suffice. Read the selected files fully before using their detailed claims, and inspect current primary product guidance when freshness matters.

A project `DESIGN.md` can cover the original nine areas: visual theme, color, typography, component styling, layout, depth/elevation, do/don't guidance, responsive behavior, and implementation guidance for the next agent. These are a useful document outline, not the Google alpha schema. Use `rtp-design-spec` when machine-readable DESIGN.md or token export is required.

## Seven design lenses

### 1. Color relationships

Design the relationship between foreground, background, neighbors, area and state. OKLCH can make palette construction more predictable than HSL, but equal lightness coordinates do not guarantee identical perceived brightness or accessible contrast. Check the actual rendered pair and display gamut.

Use semantic roles—backgrounds, text, borders, interaction accents and status—so light/dark themes can map them deliberately. A single signature accent is a useful strategy, not a prohibition on functional colors or Ravi's series system. Do not explain user trust through an unsupported story about the emotional power of a hex value.

The [color reference](references/color-and-perception.md) retains Albers' interaction lenses, perception concepts, palette steps, gradient families, example colors, wide-gamut guidance and their practical limits.

### 2. Space and information

Use grouping, alignment, hierarchy and reading order to make the task clear. Tufte's data-ink, chartjunk, small multiples, and layering/separation help assess whether a visual choice aids interpretation. Borders, whitespace, orientation cues and restrained ornament can be useful; “every non-data pixel is waste” is not a universal interface rule.

Design readable body text early. A roughly 45–75-character measure can be a useful starting point for prose, with the actual language, font, device and reading task checked. Current Ravi editorial pages use their 68ch specification. Use a coherent rhythm and, where helpful, a modular type scale such as 1.25 or 1.333; a mathematical ratio does not itself establish good typography.

Inter, Satoshi, Geist, Cabinet Grotesk and Plus Jakarta Sans remain reference choices. Check licensing, available weights and the specific file's variable axes. Spacing examples—4px for a tight relationship, 24px for a related group, 64px for a section—illustrate hierarchy rather than fixed semantics. Dense expert workflows may need less whitespace than a reading page.

### 3. Material and motion

Use depth to communicate layering, focus and interaction. Glass, luminance-separated cards, inset light and shadows are options. A CSS backdrop blur is a glass-like approximation, not proof of Apple's Liquid Glass rendering method. Keep text contrast stable over changing backgrounds, supply a solid fallback, and measure effects on the intended device.

Use anticipation, follow-through and staging to support orientation and feedback. Timing examples such as 150ms feedback, 200–300ms micro-interaction and 500ms transition are starting points; the governing system may specify another duration. Interruptibility, responsiveness and motion preferences matter more than insisting every transition uses a spring.

Stop nonessential continuous motion when appropriate; reduced-motion support includes JavaScript loops, canvas and scrolling as well as CSS. Content must remain visible if enhancement fails. The [principles and material reference](references/principles-and-material.md) preserves the original material snippets and all philosophical lenses.

### 4. Product design principles

Use Rams' ten principles as questions about innovation, usefulness, aesthetics, understandability, unobtrusiveness, honesty, longevity, thoroughness, environmental impact and restraint. A tutorial can be appropriate for an unfamiliar task; its existence does not prove design failure. A status explanation is not evidence of the model's internal reasoning, and a simulated progress percentage is not honest measurement.

Norman's visceral, behavioral and reflective lenses help separate first impression, actual use and the user's later interpretation. A trustworthy appearance does not establish a trustworthy system. Alexander's context-sensitive patterns and Chimero's medium-aware design discourage mechanical component assembly. Ive's “inevitable” idea is an optional coherence question, not a finish line requiring imagined celebrity approval.

### 5. Current techniques and AI interaction

Bento grids, variable-font motion, neubrutalism, noise, glass and mesh gradients are available techniques, not universal current trends or guarantees of quality. Use a method when it suits the task and verify current implementation details. A playful visual language is not automatically forbidden in enterprise work; readability and consequence still govern.

For AI interfaces, design the full useful cycle:

- **Input:** make context, selected files, permissions and constraints understandable.
- **Work in progress:** show actual observable steps and allow stopping where supported. Avoid inventing detailed progress or presenting generated narration as a verified execution trace.
- **Streaming:** preserve reading position when the user scrolls away; render partial blocks safely; support copying when useful with incomplete status made clear. Do not expose active unsafe markup.
- **Review/action:** preview consequential changes, identify what approval authorizes, and distinguish approval before action from review afterward.
- **Result:** show evidence and source access where useful, plus partial, failed, stale or uncertain results rather than only a polished success state.
- **Recovery:** offer correction, retry, undo or compensation where actually supported. Some actions cannot be reversed; communicate that before commitment and apply appropriate safeguards.

Claude's conversation/artifact split, Perplexity's source-led search and Cursor's contextual inputs are reference patterns, not a newly verified claim about their current interfaces. Grok/X patterns matter when they match Ravi's actual audience and task. Use `rtp-autonomy-spectrum`, `rtp-tool-architecture`, `rtp-confidence-tuner` and the relevant safety/evaluation skills to connect the UI to real capabilities. Geoffrey Litt's malleable-software idea invites user reshaping with clear permissions and recovery.

### 6. Interface writing

Choose words that describe the real action and result. “Create project” may be clearer than “Get started”; “Submit application” may be exactly right when submission is the consequential action. Avoid a universal hierarchy in which a more energetic label is automatically better.

Lead with a relevant outcome, without promising an unmeasured benefit. Empty states explain what is absent and a feasible next step. Error messages identify the problem, preserve useful input, and offer recovery without blame. A loading label says what is known; “Reading 847 files” is appropriate only when that count and operation are real.

Keep tooltips brief, but move essential instructions into persistent text rather than hiding them to obey a one-sentence limit. Use explicit form labels; placeholders are not labels. Warmth should fit the stakes. A cheerful apology after data loss can be jarring; clear, accountable language is more useful. “File uploaded” is concise status wording, not grammatically proof of active voice.

### 7. Deliberate choices instead of defaults

Notice when a familiar pattern has appeared without a reason: purple mesh hero, equal feature cards, glass on every surface, endless small animation, or an automatic font pairing. Ask whether it helps this audience. Familiarity is not a defect; consistent controls, repeated layouts and standard components often make a product easier to use.

The [anti-default reference](references/deliberate-design.md) retains the three dials, named palette/font cautions, layout checks and interaction-state requirements. It distinguishes preferences from requirements. Do not force asymmetry, novelty, new colors or short labels at the expense of comprehension, zoom, translation or the governing brand.

## Review the finished artifact

Inspect the actual output, not only its source. A brief first impression helps identify hierarchy, but it is not a user study or a two-second pass/fail test. Check the following at a depth appropriate to the artifact:

| Area | Check |
|---|---|
| Task and truth | Main action/outcome is clear; content and progress/status claims are accurate |
| Governing design | Correct theme, token roles, approved exceptions and series identity |
| Contrast | Actual foreground/background and interactive states meet the applicable standard |
| Typography | Readable final size, hierarchy, wrapping, supported fonts and meaningful metadata |
| Layout | Reading order, grouping, alignment, space and content survive real viewport/page constraints |
| Interaction | Keyboard, focus, touch, labels, loading/empty/error/partial/success and recovery states |
| Motion/material | Useful layering, reduced-motion path, static fallback and measured performance |
| Export | Correct dimensions, complete content, font/glyph fidelity and functioning links where supported |

Use WCAG 2.2 requirements for the applicable web check. AA normal text needs 4.5:1; large text needs 3:1 and means at least 18pt (24 CSS px), or 14pt bold (about 18.67 CSS px). A blanket “18px+” threshold is wrong. Assess required non-text controls and indicators separately, and do not claim a complete accessibility audit from contrast alone.

APCA may supplement typography assessment with its own method and text-size/weight guidance. It does not replace a requested WCAG 2.x conformance check. The [WCAG 3 publication checked on September 13](https://www.w3.org/TR/2026/WD-wcag-3.0-20260910/) remains a Working Draft.

For SVG, validate XML and inspect the rendered drawing at its final placed size. Distinguish accidental border/text collision from intentional containment, shared boundaries or connector junctions; use the current `rtp-excalidraw-svg` guidance. For documents, slides and spreadsheets, use their native production checks. Do not require an alternate theme that was neither requested nor supported.

Give actionable feedback: element, problem, consequence, specific fix and verification. Prioritize a blocked task or unreadable control above cosmetic preference. If the user authorized reversible fixes, apply and recheck them. Report self-review as self-review; do not imply a separate UX agent or actual design leader approved the artifact. Mark untested conditions explicitly.

## Reference use, integration and learning

The [reference index](references/sources-and-companies.md) lists **58 local company snapshots**, counted in this revision, along with all original learning-source families. Select by the problem: color, type, layout, dark mode, warm tone, luxury, or developer workflow. Borrow a principle with its context, not a whole competitor identity. A showroom's minimal control layout is a poor assumption for an industrial control panel unless the actual task supports it.

This skill can support orchestrator visual work, UI sections of PRDs, agent status and approval design, competitor interpretation, safety-critical warnings, slides and diagrams. Use it when a visual review adds value; a simple factual answer does not require it. Specific team titles are roles in the workflow, not proof that separate agents are running.

For personal banners and approved diagram signatures, see [borders and LinkedIn cover guidance](references/borders-and-linkedin.md). It preserves the five-segment bar and three gradient options while identifying their scope and current platform limits.

Record meaningful feedback Ravi accepted, changed or rejected, with the artifact and context. Distinguish a local choice from a standing preference and review false-positive design warnings. Persist supported preferences through the authorized knowledge process; do not promise automatic memory or infer a new rule after every session. Read relevant Novel Insights as bounded hypotheses: explanation may change acceptance and error detection differently, so visual trust is not a safety result.

Editorial revision: September 13, 2026. Seven lenses, three modes, all reference families and signature examples remain. Current source precedence, accessibility, color-science limits, realistic AI states and evidence of verification come before aesthetic recipes.
