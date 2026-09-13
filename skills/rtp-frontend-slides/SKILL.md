---
name: rtp-frontend-slides
version: v1.0.1_latest
description: 'Build or improve HTML presentations, including faithful conversions of PowerPoint content. Use for pitch decks, teaching, conference talks, internal presentations, or an existing web deck that needs clearer design, navigation, or accessibility. Follow six phases: identify the mode, understand and inventory the content, choose a visual direction, build the deck, verify it, and deliver it. Default to one HTML file with inline CSS and JavaScript and no framework or build requirement. Use visual previews when the style is undecided; follow an established brand without repeating that choice. Preserve readable content at small sizes and zoom, provide keyboard access and reduced-motion behavior, and verify the intended browser and offline requirements. A single file with remote fonts or media is not fully self-contained.'
---

# Frontend Slides — Make an HTML deck people can present and read

Turn a clear story into a browser presentation with readable slides, dependable navigation, and a deliberate visual identity. Default to plain HTML, inline CSS, and inline JavaScript. Use one file where practical; no framework or build step is required for the delivered deck.

This local skill adapts Zara Zhang's [frontend-slides project](https://github.com/zarazhangrui/frontend-slides). The local version and style catalog are maintained separately from upstream. It is guidance for creating and checking a deck, not a bundled implementation or a guarantee that any assistant can run the necessary tools.

## Phase 0 — Identify the mode and delivery conditions

Use **New Presentation**, **PowerPoint Conversion**, or **Enhancement of Existing HTML**. Read the supplied deck or project before changing it. Preserve the source and existing working behavior during conversion or enhancement.

Establish the audience, purpose, presentation setting, time or slide budget, available content, and current brand. Infer what is clear from the request; ask only about gaps that affect the result. An explicitly requested HTML deck stays HTML. If the user needs editable PowerPoint or Google Slides, use the appropriate presentation workflow rather than silently substituting a web page.

Decide whether the deck must work offline, be printed, or be hosted. One HTML file can still depend on remote fonts, images, video, or APIs. For a genuinely self-contained delivery, embed suitable licensed assets or use local system fonts and verify it with the network unavailable. If media warrants an accompanying folder, explain that packaging choice. Publishing is a separate action governed by the user's request.

## Phase 1 — Understand and inventory the content

Identify the central message and the progression of evidence or decisions. Write slide takeaways before adding effects. A five-to-ten-slide overview, a ten-to-twenty-slide talk, and a longer teaching deck need different pacing; these ranges are planning prompts, not fixed categories.

Review images early so they can shape the story. Product screenshots can anchor relevant demonstrations, while a logo may belong on the opening or closing slide. Do not create three feature slides merely because three screenshots exist. Explain a quality problem when it affects use; preserve an essential low-resolution image with an appropriate treatment or request a better source instead of silently discarding it.

Without supplied images, use typography, diagrams, CSS shapes, or other relevant visuals. Photographs and illustrations are valid when they explain the subject; abstract decoration is not a substitute for necessary evidence.

For **PowerPoint conversion**, perform extraction here, before styling or rebuilding:

1. Inventory the slide count and order, visible text, images, charts, tables, groups, links, media, notes, and important relationships.
2. Use available tools such as `python-pptx` for supported extraction. Its [documentation](https://python-pptx.readthedocs.io/en/latest/) notes that the format has unsupported features; parsing text and pictures does not prove that every object or behavior was recovered.
3. Render or inspect the source slides to detect omissions and ordering problems. Record unsupported animations, SmartArt, embedded objects, or media as applicable, without claiming all files have these issues.
4. Resolve meaningful ambiguities and keep a source-to-output map. Ask about substantive editorial changes when needed; do not require reconfirmation of an already authorized faithful conversion.
5. Keep speaker notes and hidden material separate from the public audience deck unless their inclusion is intended. Content hidden in HTML remains readable in the file source.

## Phase 2 — Choose the visual direction

When the user has supplied a brand, template, or clear preference, follow it. When the direction is undecided, offer three distinct visual previews so the user can react to actual typography, color, density, and motion. A title slide can demonstrate atmosphere, but include representative dense content when that is necessary to judge readability. Do not complete dependent styling while a required preference is still pending.

The [style and motion reference](references/styles-and-motion.md) preserves ten local presets and example font pairings. Match them to the audience's needs: confidence, energy, calm, or an editorial story. These are design intentions, not guaranteed emotional effects or claims about what most people can articulate.

Use a coherent visual hierarchy and enough layout variety to support the content. Blue accents, Inter, Arial, system fonts, centered titles, and repeated cards are all valid choices when they serve the brand and task. Their presence does not establish AI authorship or poor quality. Avoid empty ornament, generic claims, and variation added only to look unconventional.

## Phase 3 — Build a readable deck with progressive enhancement

Use semantic HTML and a clear document title and language. Give slides meaningful headings and navigation controls visible or accessible names. Content should be readable before optional animation initializes and if JavaScript fails.

### Fit slides without hiding content

For the intended presentation viewport, aim for one complete slide per screen. Start with a heading and a small number of points, or a heading, short paragraph, and visual. Five bullets and four cards are useful density prompts, not permission to hide a sixth essential point.

If content is too dense, simplify faithfully, move detail into an explicitly included appendix or notes, or split the slide. At narrow widths, short screens, or browser zoom, allow a readable scrolling or document mode. A fixed height with `overflow: hidden` must not make content or focused controls inaccessible.

This is a starting layout, not a complete deck implementation:

```css
:root {
  --title-size: clamp(2rem, 5vw, 4rem);
  --h2-size: clamp(1.5rem, 3.5vw, 2.5rem);
  --body-size: clamp(1rem, 1.5vw, 1.25rem);
  --slide-padding: clamp(1rem, 4vw, 4rem);
}
* { box-sizing: border-box; }
html { scroll-snap-type: y proximity; }
.slide {
  width: 100%;
  min-height: 100vh;
  min-height: 100dvh;
  padding: var(--slide-padding);
  scroll-snap-align: start;
  display: flex;
  flex-direction: column;
  position: relative;
}
@media (max-width: 48rem), (max-height: 40rem) {
  html { scroll-snap-type: none; }
  .slide { min-height: auto; }
}
@media (prefers-reduced-motion: reduce) {
  html { scroll-behavior: auto; }
  .slide-reveal, .deck-decoration {
    animation: none !important;
    transition: none !important;
    transform: none !important;
    opacity: 1 !important;
    filter: none !important;
  }
}
@media print {
  html { scroll-snap-type: none; }
  .slide { min-height: auto; break-after: page; }
  .deck-navigation, .deck-decoration { display: none !important; }
  .slide-reveal { opacity: 1 !important; transform: none !important; filter: none !important; }
}
```

Use the class names consistently if adopting this snippet. JavaScript-driven canvas or motion needs its own reduced-motion handling; the CSS does not stop a running script. Inspect print output because a long slide can span pages even with a page-break rule.

Use responsive type and spacing that suit the content; `clamp()` is useful but not mandatory for every value. On short screens, remove unnecessary decoration or switch layouts before compressing text. Do not disable browser zoom. A negative function value should be written as `calc(-1 * clamp(...))`, not `-clamp(...)`.

### Make navigation predictable

Provide previous/next controls, a way to identify the current slide, and keyboard navigation. Navigation dots, a progress bar, swipe, wheel behavior, and shortcut hints are optional enhancements appropriate to the deck. A large deck may need an outline instead of dozens of dots.

Handle arrows or Space only when they should navigate the deck. Preserve typing, focused controls, browser shortcuts, and ordinary reading scroll. Do not trap focus, suppress every touch gesture, or advance multiple slides on one trackpad movement. Give Escape an actual documented action, such as closing an overlay; do not advertise a shortcut with no behavior. Keep help discoverable even if an initial hint fades.

If using a progress bar, provide its accessible name and current, minimum, and maximum values, or use an appropriate native element. A decorative line need not pretend to be an interactive control. For slide changes, keep visual state, focus behavior, and the reading order coherent without repeatedly announcing the entire slide.

### Add motion only after content works

Fade/slide, scale, horizontal reveals, and blur are available patterns. Stagger related elements sparingly. Keep important content visible by default; activate hidden pending states only after the observer or animation system is ready, and restore visibility on failure or when focus reaches the content.

Honor reduced-motion preferences for transitions, stagger delays, scroll behavior, parallax, and canvas effects. Avoid flashing and provide a way to pause applicable ongoing movement. Particle systems and magnetic buttons are optional, not required markers of quality. Prefer a stable control target over an effect that makes it harder to click.

For performance, favor `transform` and `opacity` where suitable; do not promise they are always GPU-composited or cost-free. Use `will-change` briefly and only where useful. Schedule expensive event work carefully, stop offscreen or hidden-tab animation, and profile effects that use blur, filters, or canvas. A 768-pixel breakpoint can be a fallback, but width is not a reliable measure of device capability or user preference.

## Phase 4 — Verify content, behavior, and presentation

Review every slide in the browser, not just the opening view. Check a representative desktop, narrow screen, short landscape view, and enlarged text or zoom. Confirm:

- All intended content, assets, source labels, and meaningful conversion details are present; numbers and claims remain accurate.
- Slides read clearly, controls stay reachable, text does not clip, and layout changes preserve order.
- Keyboard use, visible focus, slide controls, links, and any touch behavior work without trapping the reader.
- Contrast meets the applicable criteria, and essential information does not rely on color alone. The usual AA text thresholds are 4.5:1 for ordinary text and 3:1 for qualifying large text; size is judged as delivered.
- Targets satisfy applicable WCAG 2.2 AA sizing and spacing criteria; 24 by 24 CSS pixels is the minimum target criterion with exceptions, not a complete accessibility audit. Larger targets can be easier to use.
- Reduced motion, unavailable fonts, script failure, and offline requirements have sensible outcomes.
- Print or PDF output, when requested, includes all slides without hidden reveal states or navigation clutter.

A semantic `<section>`, an ARIA label, and a few media queries do not establish WCAG conformance. Record the checks actually performed and any remaining limits. A text-only file under 100 KB is a useful original size target, not a reason to drop content, notices, or accessibility features. Report meaningful asset costs and optimize them where worthwhile.

## Phase 5 — Deliver the usable artifact

Open or preview the deck when available. Provide the file, slide count, chosen style, essential navigation guidance, and any required companion assets. State material conversion gaps or checks that could not run. Keep customization instructions practical; explain CSS variables only when the user wants to edit the implementation.

If fonts fail, check the requested family and loaded assets, then verify the fallback and offline behavior. If animation fails, restore content visibility before repairing the observer. If navigation or snapping causes inaccessible content, fix the layout or use the reading mode instead of forcing mandatory snapping. If the deck is slow, reduce or remove expensive effects and measure again.

Example requests include “Create a ten-slide pitch deck in the current brand,” “Convert this PowerPoint into a Midnight Executive HTML deck,” and “Show three calm visual directions for this conference talk.” The command name depends on the host installation; this local skill is named `rtp-frontend-slides`, while the upstream plugin has its own namespaced command. Do not rename or reinstall the local skill just to match an upstream example.

## Provenance and maintenance

This revision is **v1.0.1_latest**, reviewed 13 September 2026. The earlier body listed 1.0.0, 2.0.0, and 3.0.0 milestones without a verified mapping to this local frontmatter or upstream releases. Treat those as historical narrative, not installed version identifiers. The current skill version is the frontmatter value.

The upstream project is MIT-licensed. Preserve its copyright and license notices when redistributing covered material; see the bundled [upstream license](references/upstream-LICENSE.txt). This does not grant rights to unrelated fonts, photographs, logos, or presentation content. The local design and accessibility additions are guidance to validate, not a promise of unchanged browser behavior ten years from now.
