---
name: rtp-excalidraw-svg
version: v1.4.1_latest
description: 'Create or revise readable SVG diagrams with an Excalidraw-inspired pastel style and a clear visual story. Use for architecture, flowcharts, comparisons, timelines, relationship maps, agent workflows, and visual explanations of a PRD, specification, or analysis. Start with the reader’s question, preserve the meaning of labels and connections, size the layout around the text, and verify the rendered result at its intended display size. Use the applicable brand palette, check actual contrast, and distinguish portable SVG conventions from platform restrictions. This produces SVG; it does not imply an editable Excalidraw scene. Add a summary diagram when it helps the reader or the user requests one, rather than automatically adding an image to every answer.'
---

# Excalidraw SVG — Explain through a clear visual story

Help the reader understand a relationship, make a decision, or follow a process. Use restrained pastel surfaces, readable text, and deliberate spacing. The diagram should remain accurate when its decoration is removed.

This skill creates SVG with an Excalidraw-inspired aesthetic. If the user needs editable Excalidraw elements, confirm the required native format and use a suitable workflow; a hand-authored SVG is not automatically an editable scene. Use the current project or brand specification when it differs from these defaults.

## 1. Choose the story and audience

Before drawing, identify the reader's question, the main takeaway, and where the diagram will appear. A component inventory may be exactly what an engineer needs; an executive comparison may need a conclusion first. Do not force every technical diagram into a problem–solution sales narrative.

Write the main point in one sentence to establish focus. Then identify the visual entry, flow direction, and endpoint. Several related details can support that point; split genuinely different questions into separate views. “Quick Check — Executive Summary” and “Depth — Comprehensive” are available labels when depth helps readers orient themselves, not mandatory text on every image.

Use these five review lenses, informed by human-centered design practice:

1. **Reader's purpose:** show what the viewer needs to understand, decide, or build.
2. **Prototype early:** settle the structure before polishing. Invite feedback when it will affect the design; two or three rounds are a useful expectation, not a required ritual.
3. **Use visual form meaningfully:** a funnel can show narrowing; layers can show containment or dependencies. Do not imply inheritance, sequence, or causality unless the system actually has it.
4. **Support an appropriate response:** make risk visible and the next step understandable. Do not manufacture urgency or hide uncertainty to make the viewer feel confident.
5. **Check the viewing setting:** a wall poster needs distance readability; a README needs legibility at its embedded width. Use the A3 “walk the wall” test when print is relevant.

These are design lenses, not evidence of an IDEO review or an external endorsement.

## 2. Write the labels before sizing the boxes

Draft the title, node labels, connector labels, and any takeaway. Prefer clear actions and specific relationships. A surprising interpretation can help when it is supported; descriptive headings are often the most useful choice for architecture and reference material.

Aim for short headlines and two or three body lines per card. Expand or split the layout when more detail is necessary. Keep technical terms that matter and explain unfamiliar ones once. Do not replace an exact term such as `robust statistics` because a prose preference discourages generic “robust” claims.

Use numbers only when sourced, calculated, or explicitly illustrative. The earlier copy examples “99% collect feedback,” “10–20% reaches the model,” and “3.2x faster” were not evidence; do not reuse them as facts. A truthful qualitative label is better than invented precision. Preserve denominators, conditions, and uncertainty when shortening a claim.

An executive problem → mechanism → impact view can use Coral → Neutral/Glacier → Moss. Pair colors with labels, shapes, or positioning so the relationship remains clear without color. Do not use a red/green comparison to imply that a nuanced choice has one universally bad option.

## 3. Select a pattern that matches the relationship

| Need | Pattern | What to make explicit |
|---|---|---|
| Architecture | Layer Cards or Nested Groups | Dependencies, boundaries, and direction |
| Process | Flow Chain | Inputs, transformations, branches, and outputs |
| Comparison | Side-by-Side | Equivalent criteria, trade-offs, and scope |
| Sequence | Timeline or Step Ladder | Order and any real timing constraints |
| Catalog | Grid Cards | Grouping, selection criteria, and whether the set is complete |
| Relationships | Hub-Spoke | What each connection means; direction if relevant |
| Agent workflow | Agentic Loop | Tools, review points, stopping conditions, and failed exits |
| Capacity or budget | Context Bar | Units, denominator, used capacity, and limit |
| Agent outputs | Deliverable Map | Owner, artifact, recipient, and handoff |
| Selection or worked example | Workflow Menu or Walkthrough | Which route applies or what actually happens in order |

The [pattern catalog](references/diagram-types.md) gives layouts and composition guidance. Use a funnel for narrowing choices or inputs. Combine patterns only when each adds information; avoid implying equal importance merely because cards have equal size.

## 4. Apply the visual system consistently

The default canvas is warm off-white `#FAFAF8`, with dark text and pastel cards. Use two or three semantic families plus neutral in most diagrams, with one clear emphasis. More colors are justified when they encode necessary categories; fewer are often enough. Count meaningful categories, not individual tint values.

The main palette is **Luminous Pastel**: Rose Quartz for thinking, Wisteria for judgment, Honey Amber for craft, Celadon for evaluation, Glacier for technical material, Coral for agents or risk, Moss for outcomes, and Neutral for structure. The [palette reference](references/color-palette.md) contains exact values and the earlier brighter palette for maintaining existing work. Choose one mapping and keep it consistent across a set. A palette preference does not override a current brand contract.

Use `Inter, Segoe UI, sans-serif` as the default stack, allowing the actual fallback to affect measurements. Code literals may use a legible monospace stack. Fonts named in SVG are not necessarily installed or loadable in an image viewer.

The earlier 1200-unit templates used titles at 28–30, section headings at 17–20, subtitles at 14–15, body text at 13–14, and chips or metadata at 10–12. Treat these as historical starting points, not readability guarantees. A 14-unit label becomes roughly 7 CSS pixels when a 1200-unit diagram is displayed at 600 pixels. Set type for the **delivered size**, increasing it or reducing density as needed. Avoid essential information that requires readers to open a larger image just to read the explanation.

Use actual foreground/background contrast. White on a saturated-looking bar is not automatically readable. For ordinary text, target at least 4.5:1; the 3:1 large-text exception requires a sufficiently large rendered size, approximately 24 CSS pixels regular or 18.67 bold. A 16-pixel bold header does not qualify. Check meaningful connectors and boundaries as well. See the corrected calculations in the palette reference and [W3C's contrast guidance](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html).

## 5. Fit geometry to the content

Plan rows, columns, text baselines, and connector lanes before placing shapes. A 1200-unit canvas is a convenient default; typical heights are 400–520 for simple, 520–720 for medium, and 720–900 for detailed views. Use another aspect ratio or a taller view when the destination warrants it. Split a dense diagram when that improves navigation, rather than enforcing a 900-unit ceiling at the expense of clarity.

Measure text with the intended font where possible. Character-count estimates such as seven units per character at size 13 are only rough planning aids; proportional glyphs, weight, fallback fonts, and wrapping can change the result. Add padding to the measured text width. If a label does not fit, edit without changing its meaning, wrap it, widen the card, or change the layout. Shrinking essential text is a last resort that still must pass the delivered-size review.

For a 1200-unit canvas with 50-unit side margins:

- Four 260-unit cards with 20-unit gaps start at **50, 330, 610, 890**; the last ends at 1150.
- Three 340-unit cards with 40-unit gaps start at **50, 430, 810**.
- Two 535-unit cards with a 30-unit gap start at **50 and 615**.

Reserve larger lanes when connectors need arrowheads or labels. Do not force an arrow with two 25-unit clearances into a 20-unit gap.

Useful starting dimensions are 48–60 high for a title-only card, 70–80 for title and subtitle, 90–110 with a short description, and 170–220 for a header, body, and chips. Recompute after choosing real text and font sizes. Cards commonly use 14–16-unit radii, chips 8, inner padding 16–20, chip gaps 8–10, group gaps around 40, and tier gaps around 60. These values are adjustable relationships, not an independent checklist that can contradict the layout.

Keep meaningful content inside the selected margins. Backgrounds and decorative bands may intentionally reach the canvas edge; a header bar containing its own text is intentional containment, not an overlap error. Measure actual text bounds, strokes, and shadows near edges. Keep a clear gap, normally at least 30 units, between the final content row and any footer, then confirm it visually.

Cards, chips, takeaway callouts, and before/after panels are the main building blocks. A callout may be omitted when the title or diagram already communicates the conclusion. Add a subtle shadow only if it helps separation; preserve a visible border if the target renderer drops the filter.

## 6. Route connections without changing the system

Use straight lines for simple connections, elbows for lanes, and curves for return paths or relationships that benefit from them. There is no universally best arrow style. Keep endpoints unambiguous and labels clear of both lines and nearby text.

Reduce crossings through layout changes. If a real network cannot be shown without crossings, distinguish crossings from junctions and consider a separate detail view. Do not delete an important edge to satisfy a no-crossings rule.

Leave enough clearance for the actual arrowhead, commonly 10–12 units, and place labels near the relevant segment with a readable background if needed. Polygon arrowheads are a portable option; standard SVG markers are also valid and should be tested in the destination. Show bidirectional relationships or undirected associations accurately rather than assigning an arbitrary arrow.

## 7. Build portable, accessible SVG

Include the SVG namespace, a coherent `viewBox`, and deliberate intrinsic or host sizing. Give a standalone diagram a useful title, description, and accessible name. When embedded as an image, provide meaningful `alt` text in the host document; do not rely on the image's internal description being exposed identically in every viewer.

For broadly portable static diagrams, prefer shapes, `<text>`, `<tspan>`, explicit presentation attributes, and local definitions. Escape XML characters in text and attributes. Use a descriptive text equivalent for a complex diagram, including information needed to understand it without seeing the image.

The [GitHub rendering reference](references/github-rendering.md) distinguishes conservative portability choices from SVG validity. `<style>`, classes, `rgba()`, eight-digit hex, markers, and namespaced links are not inherently invalid SVG. External resources and image-host restrictions can still change the result. Verify the intended embedding path; a local `<object>` preview and a README `<img>` are different environments.

## 8. Review the rendered result

Parse the XML, then inspect the actual image. Static validation cannot establish line spacing, clipping, font fallback, or visual hierarchy. Review at the intended embedded size and at a larger inspection size. For a set of edited SVGs, an HTML review page is a convenient way to inspect all changed files; a direct browser or target-app preview is equally valid.

Check these five areas:

1. **Meaning:** the title, claims, numbers, groupings, and edge directions match the source. Limitations remain visible where they affect interpretation.
2. **Reading:** every essential label is legible; line spacing and contrast work with the actual font. Nothing is truncated or hidden behind an element.
3. **Geometry:** containers fit their text; edges and footer have clearance; crossings and intentional overlaps are understandable.
4. **Portability and access:** the destination renders the file, the image has an accessible description, and losing a decorative shadow does not lose meaning.
5. **Focus:** the reader can identify the main point and follow the relevant route. A brief glance is a useful design check, not a claimed three-second user-study result.

Correct failures and review the changed regions plus any layout they affect. Finish with a pass over the complete image. If rendering is unavailable, provide the draft with that specific limitation; do not label a source-only check as a completed visual review.

## 9. Apply the post-edit discipline

Edits can break a layout that previously fit. Keep these five lessons from the earlier Harness V2 revision cycle:

- **Render after edits:** inspect the final modified files, including their actual embedding mode. A local HTML harness may help, but its filename and port are not requirements.
- **Check multiline text:** three-line bodies deserve particular attention. Compare baselines within the same text block; a line height near 1.5 times the font size is a useful body-text starting point. Font metrics and the final render decide whether spacing works. Merge lines only when the combined line fits and retains the meaning.
- **Translate jargon sparingly:** a shared caption can explain a row of related terms. Add individual glosses when necessary, keeping them readable; do not hide essential explanations in tiny, low-contrast italics.
- **Read from the audience's perspective:** expand unfamiliar acronyms at first use, keep useful technical anchors visible, and use action labels such as “runs before the model call.” Decide familiarity from the audience, not from a universal claim that every PM knows or does not know IAM.
- **Protect the essence:** additions should improve the explanation, accessibility, or required attribution. Remove redundancy before adding clutter, while preserving necessary exceptions and relationships.

An example gloss such as “Ralph Loop — resume after stop” needs checking against the particular workflow; a convenient phrase is not a universal definition.

## 10. Deliver in the right context

Provide the SVG and, when useful, its text explanation or preview. Identify any rendering checks that could not be completed. Use a meaningful filename; related views can use `01-overview.svg`, `02-detail.svg`, and `03-example.svg` without an arbitrary maximum set size.

For another skill's output, follow the [visual-summary protocol](references/visual-summary-protocol.md) when a visual adds understanding or is requested. Do not automatically append an SVG to every response or promise a tenfold improvement.

For libraries and inspiration, consult the [resource catalog](references/excalidraw-libraries.md). Preserve applicable third-party attribution. Where appropriate for Ravi's standalone work, include `© Raviteja Palanki, AI Product Manager`; a descriptive footer may be more useful for internal documentation, and Ravi's footer does not replace a source creator's license requirements.

Revision 1.4.1 — wording, geometry, palette, and rendering guidance reviewed 13 September 2026. Historical production lessons are retained as lessons, not as proof that every new diagram is already tested.
