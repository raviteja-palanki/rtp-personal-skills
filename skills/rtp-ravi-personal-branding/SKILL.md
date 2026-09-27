---
name: rtp-personal-branding
version: v2.2.1_latest
description: 'Apply Ravi Teja Palanki’s visual identity to websites, presentations, documents, diagrams, and article pages, including learn.ravitejapalanki.com. Start with the medium and current project specification. Use light documents and dark websites or decks by default, with the four brand typefaces and meaningful color accents. For website work, the fourteen-part editorial design specification governs current styling; the older V8 components remain a reusable reference, with conflicts and accessibility requirements made explicit. Includes palettes, typography, layouts, motion, signature components, page recipes, and a DESIGN.md seed. Pair with rtp-ux-design-systems for usability, rtp-excalidraw-svg for diagrams, and rtp-design-spec for portable tokens. Preserve readability, truthful content, keyboard access, and motion preferences; check the rendered result in its actual medium.'
---
# Ravi personal branding

Create a recognizable Ravi Teja Palanki surface that is clear, restrained, and comfortable to use. Typography, meaningful color, editorial rhythm, and a considered signature carry the identity. Choose effects for their contribution to the reader's task.

Use this skill when the output carries Ravi's brand: his website or learn subdomain, an article, deck, document, diagram, or visualization. A requested client or teaching identity may take precedence; do not force this palette onto unrelated work.

## Resolve the medium and source first

1. Follow Ravi's current request and the relevant project brief.
2. For website work, read the relevant files in `1_Projects/1_my-personal-website/1_My Series-MD-FILES/My Design language_website/`. This fourteen-part specification governs the current editorial website. Its implemented code provides evidence of current behavior, not automatic permission to preserve a defect.
3. Use this skill for cross-medium application. Its older V8 components are examples to adapt, not a competing website specification. If a specification contains a calculation error or makes text inaccessible, correct the implementation and record the discrepancy.
4. Check the destination's actual capabilities and assets. Project paths are relative to Ravi's Claude workspace; a plugin installation does not include that workspace. When a referenced project file is missing, locate its current replacement or state the gap. Do not claim to have opened it.

| Surface | Default | Apply |
|---|---|---|
| Website and technical hubs | Dark editorial canvas | Current fourteen-part website specification |
| Embedded article paper or browser mock | Light reading surface inside dark shell | Current article template and approved series styling |
| Word, PDF, printed document | Light | Native document styles, readable print hierarchy |
| PowerPoint or Gamma | Dark | Native deck theme, deliberate pacing, viewing-distance checks |
| Diagrams | Match destination | Brand accents plus diagram semantics and actual final size |
| Learn subdomain | Follow its current brief | This skill replaces the archived learn-site-design skill |

Do not apply a screen's pixel measurements directly to Word or PowerPoint. Use points and page or slide dimensions there. An 11pt document body is not a suitable default for a projected slide.

## Nine creative principles

1. **Give motion a purpose.** Indicate arrival, direction, focus, or state. Let people read at their own pace; meaning must survive without animation.
2. **Choose a signature moment.** A bridge, editorial quote, diagram, or considered layout can distinguish a major section. It need not be animated, and every minor section does not need ornament.
3. **Reveal detail progressively.** Sequence content when it aids understanding. Preserve access to the complete text, keyboard navigation, and a readable static state.
4. **Use material cues selectively.** Glass, inset light, paper, and depth are available for appropriate surfaces. Current editorial pages primarily use hairlines; flat layouts can be correct.
5. **Keep four typographic roles distinct.** Inter supplies UI and occasional strong display; Instrument Serif supplies editorial display; Newsreader supplies prose; JetBrains Mono supplies metadata and code.
6. **Frame metrics clearly.** Telemetry labels such as `METRIC_01 [YEARS]` can organize evidence. Verify the number, unit, population, and date. Decorative live traces are illustrations, not real monitoring data.
7. **Make navigation feel controlled.** Smooth scrolling is optional implementation behavior, not a substitute for native scrolling or accessibility. Disable it for reduced motion and where it interferes with use.
8. **Balance density with space.** Group related material and create pauses between ideas. Split content when necessary without dropping a qualification to satisfy a bullet quota.
9. **Close with a fitting signature.** Use “Crafted with intent by Ravi Teja Palanki” where an authored artifact benefits from it. The website-specific line “This website is my product work” belongs on the website, not automatically on every document.

The historic signature set remains available: suspension bridge; architecture cards; telemetry grid; highlighted quote; stacked path cards; browser-frame article teaser; Live Trace hero; four semantic level badges; and the signature footer. Their mechanics are in [the component catalog](references/component-catalog.md).

## Current website language

The aesthetic combines Apple's restraint, the New Yorker's editorial hierarchy, and terminal-like metadata. Its ten principles are editorial priority, a dark canvas, stable series colors, four purposeful typefaces, generous reading space, functional motion, grid alignment, tabular numbers, distinctive imagery, and readability above decoration.

| Specification | Read it for |
|---|---|
| 00 overview; 01 principles | Purpose, routes, design priorities |
| 02 color; 03 typography | Current semantic tokens, series roles, font loading and scale |
| 04 spacing/grid; 05 motion | Layout, breakpoints, elevation, easing and motion preferences |
| 06 components; 07 navigation; 08 search | Reusable UI, focus, shell, search states |
| 09 templates; 10 editorial | Page recipes and writing conventions |
| 11 accessibility/performance; 12 SEO; 13 implementation | Measured checks, metadata, actual framework and integration |

The existing website pack specifies TanStack Start, React, Tailwind v4 CSS tokens, and an article iframe pattern. Check the project's current dependencies before implementation; a brand skill does not establish a software version or make owned content inherently safe. Validate iframe message origin, sender, and height before using it.

### Color and meaning

| Identity | Website / current series | Older light-article accent | Meaning |
|---|---|---|---|
| Model / AI Evals | `#9D4EDD` | `#8121D8` | Intelligence, evaluation |
| Harness / Harness Engineering | `#F43F5E` | `#E11D48` | Guardrails, risk |
| Tools / AI PM OS | `#F59E0B` | `#F59E0B` | Capabilities, strategy |
| Environment / Agentic Stack | `#06B6D4` | `#0891B2` or legacy `#00E5FF` | Context, systems |
| Frontier Companies | Neutral white | Follow the page template | The record |

Keep website series assignments stable; use cyan for shared interaction accents where specified. Red can identify the Harness series without implying every item is an error. Functional warning, error, success, and selection states need explicit semantics beyond series identity. Success colors remain `#059669` / `#10B981`; the light informational pairing remains `#1E3A8A` on `#EFF6FF`.

Use accents, tints, borders, and restrained glows rather than large saturated decorative areas. A legitimate button fill or small status mark is allowed. Do not blend series colors on current editorial pages merely because an older V8 illustration does so. Measure the actual text/background pair, including translucency.

### Typography and layout

| Family | Role | Working guidance |
|---|---|---|
| Instrument Serif | Editorial titles, quotes, drop caps, signatures | 400, upright or italic; not long body prose |
| Newsreader | Body and lede | Usually 400+, readable leading; preserve italic emphasis |
| Inter | UI, short text; occasional display | UI uses appropriate weights; 900 is the strong display treatment |
| JetBrains Mono | Metadata, labels, tabular data, code | Use available weights; uppercase short metadata where useful, never alter code or identifiers |

Load the intended fonts where the destination supports them and their licensing permits. Avoid adding a fifth design family. If a font is unavailable or an export substitutes it, resolve it or document a deliberate fallback and inspect the result. Do not claim every platform supports four independently assigned families.

Current website layout uses `--mag-max: 1440px`, `--mag-measure: 68ch`, `--mag-gutter: clamp(1.25rem,6vw,8rem)`, and `--mag-band: clamp(6rem,12vw,12rem)`. The grid has twelve columns from 900px and six below, with article 7+meta 3, hub 4+4+4 or 6+6, and hero span 10 offset 1. Numbered rows use `3rem 1fr auto`. Put adjacent `.mag-section` blocks inside `.mag-shell`; hairlines separate them.

Use Instrument Serif display `clamp(3rem,8vw,7.5rem)` and title `clamp(2rem,4vw,3.5rem)`; Newsreader body 1.125rem/1.7 and lede `clamp(1.15rem,1.6vw,1.4rem)`/1.55. Mono kickers use the specified small scale with sufficient contrast and zoom support. Small metadata is not a suitable size for substantive prose. Use tabular numerals, balanced headings, and wrapping that survives narrow viewports. Uppercase Inter display is a documented special treatment; it does not require every heading or code sample to be uppercase.

Current cards use 16px radii, level badges 20px, and pills 999px. Shadows are reserved for hover and floating surfaces. The older 40px paper/recession edge and 660px reading column remain useful in their original templates, not automatic overrides of the magazine layout. A mobile full-screen dialog can have square corners.

### Motion and editorial conventions

Current website easing is `cubic-bezier(0.16,1,0.3,1)` for reveals and `cubic-bezier(0.175,0.885,0.32,1.1)` for hover. The duration ladder is 150/250/400/800/1000/1400ms, with a 1600ms duration ceiling. Stagger delay is separate from duration; avoid cumulative waits that obstruct access. The older infinite loops, 2.5-second sweeps, extra easing curves, and mandatory Lenis package are not current defaults.

Render content visibly before adding animation. If JavaScript, an observer, or a motion library fails, text and navigation remain available. Reduced-motion handling must stop JavaScript animation and scrolling as well as CSS. Do not retain an indefinitely moving decoration merely because it passes a CSS check.

Write the content first. Use concrete, accurately supported facts; first person where Ravi is the author; canonical product casing; meaningful link labels; and no decorative emoji or reading-time chips. Follow the writing skill for voice and the page brief for length. The website's reference targets are 1–3 sentences for hub blurbs, 1,200–2,800 words for articles, and a one-sentence hero lede up to 28 words. Split or extend deliberately when the content requires it.

Use a drop cap at most once, up to two pull quotes, and up to three line-draw emphasis words per paragraph. Do not combine line-draw and pastel highlight on the same word. Keep quotations exact; do not turn an authored analysis or illustrative number into Ravi's work history.

## Adapt to the medium

**Website:** use the current shell and page recipe. Keep article paper within the approved reading treatment; match routes to the current source rather than older `/agentic-stack` or `/harness-engineering` aliases. The component catalog retains homepage, profile, writing hub, series hub, and article recipes for reference.

**Gamma and PowerPoint:** set the intended dark theme and available brand fonts. Use a title, section divider, content/diagram, telemetry, quote, and closer pattern as appropriate. Native Fade or Morph can support pacing; choose supported effects rather than assuming CSS easing transfers. Aim for one clear idea per slide; size text for the audience and projection distance. Static bridge or badge exports are valid when they communicate clearly.

**Word and PDF:** use light paper, dark body ink `#202226`, Inter H1, Instrument Serif H2/quotes, Newsreader body, and mono metadata. Translate hierarchy into native point sizes and paragraph styles; CSS `clamp()` and `rem` are not Word measurements. Start around 11–12pt for normal document body and inspect the chosen font and print size. White paper is acceptable when the printer or document system cannot reproduce a tinted page reliably. Use cream code blocks, restrained callout borders, and an appropriate signature.

**Diagrams:** match the surrounding surface and use `rtp-excalidraw-svg`. The hand-drawn Harness and technical blueprint styles remain options. Color does not replace labels, connector meaning, or readable type at final placed size.

## Check the actual result

Confirm hierarchy, content accuracy, final text size, font substitution, wrapping, navigation, keyboard focus, status meaning, motion preferences, narrow-screen reflow, and export or print readability. Check touch controls against Ravi's preferred 44×44 CSS-pixel target; WCAG 2.2's AA minimum is 24×24 with defined exceptions, not a universal 44px rule. Provide text or an accessible name for status; a faint ring alone is insufficient.

Use [the palette and contrast reference](references/palette-and-contrast.md) for recalculated solid-color values. Normal text needs at least 4.5:1 for WCAG AA; large text has different thresholds. Font size 14px does not make low contrast acceptable. The same color on a tinted or translucent surface needs another calculation.

Website budgets remain project targets: initial-route JavaScript ≤180kB gzipped, LCP ≤1.8s on the specified 4G device profile, CLS ≤0.02, and lazy search index <250kB gzipped. Measure the actual build; do not claim a fixed 200–400ms cost for an SVG effect or call budgets achieved without evidence.

For portable tokens, use [the DESIGN.md seed](references/design-md-seed.md) with `rtp-design-spec`. A parse, lint, token export, screenshot, and device test establish different things. Report the checks actually performed and any unresolved substitution or rendering condition.

Use `rtp-thinking-writing` for voice, `rtp-deep-dive-writer` for article structure, `rtp-ux-design-systems` for usability, and the relevant presentation or document skill for production. This skill preserves the brand; it does not authorize publishing or invent experience claims.

## Version record

v2.2.1 — September 13, 2026: reorganized by source precedence and medium; retained all component mechanics and token groups in references; corrected contrast, accessibility, code-example boundaries, and conflicting legacy rules. Historical v2.2 DESIGN.md export (April 25), v2.1 hub components and v2.0 V8 system (April 17), and v1.0 consolidation remain the lineage. Learn-site-design v1.0 (April 12) and v2.0 (April 15) were superseded; its formal archive on July 18, 2026 remains retired.
