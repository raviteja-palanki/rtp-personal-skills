# Local style and motion catalog

Reference revision 1.0.1 — reviewed 13 September 2026. These ten presets preserve the earlier local skill. They are creative directions, not a claim that the current upstream project uses the same names or ships these exact templates.

## Ten style directions

| Preset | Visual language | Typical use and restraint |
|---|---|---|
| **Neon Cyber** | Dark surfaces, cyan/magenta accents, monospace details, optional grid or glow | Technical material; keep particles and glitch effects optional and text stable |
| **Midnight Executive** | Navy or charcoal, gold or silver accents, serif display with clear body type | Executive or investor briefings; check contrast instead of assuming gold is readable |
| **Deep Space** | Dark canvas, sparse light points, large type, generous space | Vision or keynote material; static depth can replace parallax |
| **Terminal Green** | Dark background, green accents, monospace type, restrained terminal references | Engineering talks; retain readable text without scramble or typing delays |
| **Paper & Ink** | Off-white, dark type, serif headings, minimal motion | Academic, literary, or reflective strategy material |
| **Swiss Modern** | Clear grid, geometric type, bold color roles, precise alignment | Product and design explanations where structure matters |
| **Soft Pastel** | Light color families, soft shapes, approachable type | Teaching and creative material; dark text and calm motion preserve readability |
| **Warm Editorial** | Cream, strong type hierarchy, images and pull quotes, one accent | Brand or narrative presentations; preserve source meaning in selected quotations |
| **Brutalist** | High-contrast black and white, oversized type, deliberate asymmetry | A strong editorial stance; avoid overlap that hides information |
| **Gradient Wave** | Gradients, clean type, optional flowing backgrounds | Product launches; continuous movement needs an appropriate pause or static option |

Mood prompts can suggest a starting point: **Impressed/Confident** → Midnight Executive or Swiss Modern; **Excited/Energized** → Neon Cyber or Gradient Wave; **Calm/Focused** → Paper & Ink or a restrained Soft Pastel; **Inspired/Moved** → Deep Space or Warm Editorial. Earlier mood labels such as “Corporate Elegant,” “Clean Minimal,” “Kinetic Motion,” and “Atmospheric” were descriptions, not additional packaged presets.

Use the user's active brand and template before these options. Three previews are useful when comparing directions, but repeating a style-selection exercise after a clear choice adds work without improving the deck.

## Typography and visual variety

The earlier skill suggested these pairings as exploration candidates: Clash Display + Satoshi, Cormorant Garamond + DM Sans, Syne + General Sans, Instrument Serif + Cabinet Grotesk, and Space Mono + Switzer. Check current availability, licenses, required weights, file size, and fallback behavior before choosing one. Remote font loading conflicts with an unqualified offline/self-contained claim.

A strong deck may use asymmetry, whitespace, consistent cards, image-led layouts, or a centered opening. Use repetition to establish structure and variation to explain changes in the story. A memorable visual moment is welcome when it earns its place; it is not compulsory. No font, blue accent, purple gradient, or stock-image category independently proves poor quality or AI authorship.

## Motion patterns and their boundaries

| Pattern | Use | Implementation check |
|---|---|---|
| Fade and slide up | Introduce a content group | A historical 30-pixel offset is optional; final content remains visible if setup fails |
| Scale in | Bring attention to a card or image | A 90% starting scale is an example; avoid disorienting zoom |
| Left/right entrance | Reveal related panels in order | Keep reading order and reduced-motion behavior intact |
| Blur in | A brief atmospheric reveal | Blur can be costly and temporarily unreadable; provide a clear static state |
| Stagger | Show a short sequence | Delays such as 0.1, 0.2, and 0.3 seconds are examples, not an unbounded chain |
| Gradient, noise, grid, grain | Add background texture | Keep low contrast decoration separate from readable foreground content |
| Tilt or magnetic effect | Optional pointer feedback | Preserve a stable click target and keyboard equivalent |
| Counter | Illustrate a measured quantity | Expose the final value accessibly and avoid announcing every intermediate number |
| Text scramble or typewriter | A short stylistic moment | Do not delay access to essential information or generate distracting announcements |

The earlier effect-to-feeling examples remain useful directions: cinematic slow fades around 1–1.5 seconds; technical glows and grids; playful spring-like easing; professional transitions around 200–300 milliseconds; calm minimal movement; and editorial image/type composition. None of these timings is a universal rule or evidence of an emotional outcome. Match movement to purpose, honor reduced motion, and provide controls for applicable ongoing animation.

Keep JavaScript animation, CSS transitions, observer state, and print styles aligned. Disabling a canvas with CSS can hide it without stopping its computation; stop or avoid the work as appropriate. Prefer measured performance decisions over assuming that every narrow viewport is a weak device.
