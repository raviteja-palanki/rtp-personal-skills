---
name: rtp-lucid-boards
version: v1.4.1_latest
description: 'Create or review Lucidchart teaching boards for classroom projection, wall display, grayscale handouts, or Word and PowerPoint inserts. Start with one clear teaching claim, choose a layout that expresses its relationships, and size the actual delivered text for its viewing distance and printed dimensions. Use a small palette, strong text contrast, clear labels, and generous spacing. Verify the live document and each exported asset; record the five review perspectives and any untested conditions honestly. Includes a readability checklist, review sheet, import and export guidance, and source notes. Use for a Lucid board, not general website or slide styling. Pairs with rtp-thinking-writing for copy, rtp-excalidraw-svg for article diagrams, rtp-frontend-slides for a sequenced talk, and branding or UX skills for relevant visual principles.'
---
# Lucid teaching boards

Make the teaching claim easy to understand and read in the setting where the board will be used. A classroom poster, projected page, and A4 handout may carry the same idea but need different sizes or layouts. Check the delivered artifact rather than relying on how large the editor looks.

This skill grew from a September 2, 2026 TAPMI board review: nested pale boxes, shrinking text, repeated labels, and unnecessary arrows made the material difficult to read. Preserve that lesson by checking the actual failure modes. “World-class” is an aspiration, not a score an agent can verify by declaration.

## Establish the use before drawing

Read the task, teaching material, and relevant project instructions. Determine:

- the claim or relationship the learner should understand;
- wall, projector, handout, Word insert, or board-as-slide use;
- viewing distance, output dimensions, orientation, and likely color or grayscale reproduction;
- the requested live Lucid document and local deliverables;
- the content source and any qualification or citation the learner needs to interpret it correctly.

Infer known details from the project. Ask only for missing constraints that materially change the design. For TAPMI, use light paper and dark ink as the starting point because projection and photocopying matter. A dark field can support contrast within that page. The broader branding default does not override the actual classroom requirement.

Use `rtp-thinking-writing` to improve the claim before layout. The board should simplify its expression without changing the underlying evidence or teaching a stronger causal claim. Keep detailed notes nearby, but retain an essential qualification or compact source reference on the board when removing it would mislead.

## Apply the right design principles

| Artifact | Relevant approach |
|---|---|
| Lucid teaching board | Readable claim, clear relationships, output-size checks, and contrast that survives reproduction |
| Article or GitHub diagram | `rtp-excalidraw-svg`; use its current delivered-size guidance rather than copying a historical 13px rule |
| Sequenced talk with notes | `rtp-frontend-slides` or the requested presentation tool; choose theme and depth for that talk |
| Product interface | `rtp-ux-design-systems` and applicable branding; navigation and interaction needs differ |
| Student worksheet | A suitable Word/PDF workflow, with space and instructions for the learner’s responses |

A board inserted into a slide can remain the board; do not add decorative slide chrome automatically. Match its aspect ratio or preserve margins rather than crop or stretch the content. A worksheet and a board can complement one another.

Lucid’s guidance emphasizes clarity, consistency, and contrast. C4 contributes explicit scope and understandable notation; Duarte’s Glance Test encourages a quickly understood main point. These are useful principles, not evidence that only one layout or platform can succeed. See [source notes](references/SOURCES.md) for their scope and the historical practitioner examples.

## Write the copy before sizing the fields

List the claim, labels, supporting text, and takeaway. Begin with these **editing targets** and retain necessary meaning:

| Role | Starting word budget | Starting source type size for the historical 1920 × 1080 board | Weight |
|---|---:|---:|---|
| Main claim | 12 | 56–72 pt | 700–800 |
| Field label | 3 | 48–64 pt | 700–800 |
| Supporting text per field | 40 | 28–36 pt | 500–600 |
| Footer takeaway | 18 | 28–32 pt | 600 |
| Optional course/session label | 8 | 24–28 pt | 600 |

These sizes are a starting hierarchy, **not proof of final print size or distance readability**. The prior 18–22 pt course label conflicted with the skill’s 24 pt source minimum; the starting range now resolves that conflict. For this board style, keep meaningful source text at least 24 pt or the correctly converted equivalent, then check the final destination. A separately designed handout may use its own readable type hierarchy rather than a blindly reduced poster.

Verify which units the actual tool uses. Pixels, points, font em size, and visible letter height are different quantities. A 72 pt font has a one-inch em size before scaling; its letters need not be one inch tall. A 1920-pixel export does not specify a physical page size. For example, a 32-pixel font em in a 1920-pixel-wide image placed ten inches wide becomes about **12 pt** on paper. Raising raster resolution alone does not enlarge that type.

If the content does not fit, simplify the wording, change the layout, enlarge the destination, or divide the material. Do not let automatic fitting silently defeat the chosen type size. One idea can require more than one sentence; a second comma is not a layout failure. Prefer familiar labels over opaque coined terms, generic headings such as “Overview,” or decorative punctuation. Avoid unnecessary repeated course labels, emoji, author-name openings, and decorative countdowns. Keep notation that the subject actually requires.

## Choose a layout that preserves the relationship

Start with four useful board types:

| Type | Use it for | Design guidance |
|---|---|---|
| Two fields | A contrast such as browse/pay or intended/actual work | Use clearly labeled fields; a light and a dark field can reinforce the difference. Arrows are unnecessary unless a real relationship needs them. |
| Ladder | An ordered sequence or successive conditions | Use aligned bands, visible step numbers, and explicit stop or continuation meaning. |
| 2 × 2 | Four categories or a genuine two-axis comparison | Name the axes when they exist; do not imply a matrix relationship if these are simply four categories. |
| Table | Repeated comparable attributes or steps | Keep columns few and cells concise. Align values and headers; subtle row separation may print better than alternating heavy dark fills. |

These are starting patterns, not an exhaustive set of permitted diagrams. A flowchart is appropriate when branching or process logic is the teaching point. A comparison does not need to become a flowchart. Preserve important relationships even when another layout is needed.

Give each page a short, informative tab name. An eight-word target encourages clarity but does not require splitting a coherent page merely because its name is longer. Keep one main teaching purpose and a consistent level of detail; move secondary discussion to another page or the notes.

## Make contrast and grouping do useful work

Use one or two typefaces and a small palette. Start with no more than two saturated color families plus ink and paper. Apply colors consistently and explain their meaning through labels, position, shape, or a legend as needed. Hue alone must not carry a required distinction.

For the TAPMI style, start with heading ink `#111318`, body ink `#202226`, and white on sufficiently dark fields. Choose text color from the **actual foreground/background contrast**, not a rough HSL “50% gray” rule or a color’s name. The same hue can be light or dark. `#5A5D67` remains a possible document-caption color; avoid weakening important board text merely to make it look secondary.

Useful calculated sRGB examples:

| Text / field | Contrast ratio | Use |
|---|---:|---|
| `#111318` / yellow `#F0E442` | 14.05:1 | Strong starting combination |
| White / yellow `#F0E442` | 1.32:1 | Insufficient for text |
| `#111318` / gold `#F5C400` | 11.31:1 | Strong starting combination |
| White / gold `#F5C400` | 1.64:1 | Insufficient for text |
| White / blue `#0072B2` | 5.19:1 | Useful starting combination |
| `#111318` / blue `#0072B2` | 3.58:1 | Weaker choice; use white for this board style |

Use the familiar 4.5:1 normal-text and 3:1 large-text web contrast criteria as useful checks for a digital asset, while recognizing that projector washout, paper, ink, and viewing conditions require inspection too. They do not certify print readability. “Never white on gold” applies to the bright examples above; a sufficiently dark gold can support white. Check the actual pair.

The Okabe–Ito palette remains available: `#E69F00`, `#56B4E9`, `#009E73`, `#F0E442`, `#0072B2`, `#D55E00`, `#CC79A7`, `#000000`. It is not a guarantee that every pair has suitable text contrast or remains distinct in grayscale. Use only the colors the board needs.

Favor generous spacing, aligned edges, and clearly grouped text. Remove shapes that add no meaning. Use visible borders where they aid reproduction, checking their final thickness rather than assuming a three-pixel source stroke always survives. Omit decorative shadows, glass effects, mesh backgrounds, and icons that merely repeat their labels. Adjacent lightness differences can help separate fields; color science does not require every page to contain a dark panel.

Prefer one text-bearing shape per simple field where the tool supports it. Intentional layering and separate editable text are acceptable when they render correctly. The defect to prevent is clipping or unintended overlap. Align supporting text consistently beneath its label; top alignment is a good starting point for tall fields. Centering is appropriate when it serves the composition.

## Build and verify one representative page

1. Write and check the teaching claim and its necessary context.
2. Choose the layout, output dimensions, and copy hierarchy.
3. Establish colors and an additional encoding for meaningful distinctions.
4. Build the first representative page using the available Lucid interface. Keep controlled positioning and typography; disable automatic behavior that disrupts them.
5. Inspect the live result and export the actual page. Check the imported type size, wrapping, colors, clipping, and page bounds.
6. Inspect the delivered asset at its intended size, including grayscale where required. A mental grayscale estimate is not the completed test.
7. Complete the five-perspective review below and repair concrete failures.
8. Save the source, assets, and review evidence. Expand the proven layout to other pages, checking every export.

For a new TAPMI board style, validate S01 page 1 before multiplying its layout. This prevents repeating a defect; it does not forbid saving drafts or preparing independent copy while a render issue is being resolved. Do not rerun reviews that add no evidence merely to obtain a perfect-looking number.

Follow [import, export, and sizing guidance](references/lucid-mechanics.md). The current connector may differ from the one used in September 2026. Tool names in old notes are not proof that those tools are available now.

## Review through five perspectives

Use [the review sheet](references/judge-panel.md) and its [readability inspection](references/readability-gate.md). Review the specific exported file and its destination; also check that the live Lucid source agrees.

| Perspective | What to establish |
|---|---|
| Back-row learner | The claim, essential labels, and takeaway can be read and understood at the intended distance or handout size. |
| Print producer | The delivered type and lines are legible; grayscale preserves necessary distinctions; nothing clips or disappears. |
| Lucid practitioner | Shapes, text, and relationships remain editable and correctly rendered; layout choices fit the teaching task. |
| Copy editor | The claim is accurate, concise, natural, and supported; shortening has not removed a decisive qualification. |
| Poster designer | Hierarchy, alignment, grouping, and empty space guide attention to the meaning. |

The historical TAPMI score convention is **10 in every perspective before marking a board final**. Make it concrete: 10 means the defined checks pass on the identified artifact with no known material defect. It does not mean objective perfection or five independent people approved it. Record reviewer identity and review method; one agent using five perspectives is a self-review. Never invent student testing or a physical print test.

A failing perspective needs a specific repair, not an average that conceals it. An unperformed condition is **not tested**, not 10. Save the draft and report the unresolved condition accurately. If the task requires real-room or physical-print validation and that cannot be performed, deliver the reviewable work with that validation pending rather than claiming completion. A simulated test can support judgment but should be labeled as such.

## Save useful, traceable deliverables

For TAPMI, place `lucid-file/` at the session root, outside `supporting/`:

```text
S<NN>-.../lucid-file/
  LUCID.md              live URLs, document/page IDs, output sizes, status
  document.json         actual import source, when Standard Import is used
  import.lucid          import package and required assets, when applicable
  png/p01.png           actual exported page or explicitly labeled reconstruction
  png/p01-gray.png      grayscale inspection copy, when required
  judge-panel.md        per-page review, evidence, open issues
```

Store any separate print PDF or handout variant with its own size and review status. `LUCID.md` should distinguish live edits, original import data, and locally reconstructed images. If a live document changed after import, an old `document.json` is not an exact current backup. Record the difference or update the reconstruction source. Lucid itself notes that imports can render differently as the product evolves.

For Word, insert the verified asset at the planned dimensions and inspect the resulting page. For a board-as-slide presentation, preserve the whole board and avoid unplanned decorations. Confirm a usable local file exists; an image visible in chat is not necessarily a saved file. Do not claim a live Lucid document exists if only a local draft was created.

## Keep the original lesson, qualify the example

The historical S01 “browse versus pay” layout used an ink header, a yellow BROWSE field with ink text, a blue PAY field with white text, and a takeaway footer. It illustrates a simple comparison that should survive grayscale. Its claim—“The model was fine. The step was wrong.”—and the related Instant Checkout conclusion must be checked against the teaching evidence before reuse; attractive composition does not establish that causal explanation.

The original report concerned 19 TAPMI MBA-AI&DS students. Treat that as historical class context, not a standing audience count or a claim that those students tested this revision. A learner’s inability to retell the intended point should prompt an investigation of copy, design, background knowledge, and test conditions. It is useful feedback, not proof that a checklist was disobeyed.

Editorial revision: September 13, 2026. Important delivery and review conditions now precede source history. Original source links and research limitations remain in the companion notes.
