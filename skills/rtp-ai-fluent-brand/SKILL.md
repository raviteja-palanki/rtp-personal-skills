---
name: rtp-ai-fluent-brand
version: v1.0.1_latest
description: 'Apply the AI Fluent Product Leadership visual identity to program materials, presentations, landing pages, documents, diagrams, and email templates. Use its dark and parchment palettes, restrained gold accents, Cormorant Garamond headings, Inter body text, and JetBrains Mono data labels. Establish the medium and active project design system before styling. This is the program identity; rtp-personal-branding and the current website specification govern Ravi''s broader surfaces where they apply. Includes exact tokens, component recipes, responsive typography, motion guidance, and accessibility checks. Preserve brand character while verifying actual color pairs, readable text, keyboard use, and reduced-motion behavior. Read the bundled token and component reference when implementing the design.'
---

# AI Fluent Product Leadership brand system

Give AI Fluent materials a calm, recognizable identity: warm gold accents, layered dark surfaces or parchment backgrounds, and typography that makes the content easy to follow. The brand name is **AI Fluent Product Leadership** and its tagline is **Fluency through deliberate practice**.

Use this skill for the AI Fluent program identity. The previous label "ravi-personal-branding v2.x" blurred two systems. `rtp-personal-branding` is the broader cross-medium guide, and its current website specification governs work on Ravi's main site. Identify the actual surface and existing design contract before applying this palette. A user-requested or established project style takes precedence over a generic brand default.

The [token and component reference](references/tokens-and-components.md) contains the complete palette, typography, spacing, CSS recipes, measured color examples, and motion rules. The seven separate reference files listed in the old skill were not present in the searched library. This bundled reference replaces those broken pointers; it does not claim to recover missing documents.

## 1. Choose the medium and theme

For AI Fluent web or presentation work, dark is the usual starting point for hero areas, showcases, learning environments, and immersive content. Parchment suits documents, print, email, forms, and sustained reading. A form or long article does not need to switch themes automatically; follow its surrounding project and the user's preference.

Check the actual medium. CSS pixels describe web layout, not point sizes in a printed document or the legibility of a projected slide. Email clients may ignore custom fonts, gradients, or motion. Use reliable fallbacks and inspect the delivered format.

For Ravi's main website, read the relevant files under `1_Projects/1_my-personal-website/1_My Series-MD-FILES/My Design language_website/` through `rtp-personal-branding`. Do not replace its newer editorial palette, fonts, or series accents with this program palette without a task-specific reason.

## 2. Apply three design principles

**Make reading comfortable.** Keep sufficient contrast, useful hierarchy, and room for text to reflow. The brand aims for at least 7:1 contrast for primary text where practical. Check small captions, labels, controls, and footers too. No palette guarantees readability at every size, device, or viewing condition.

**Use emphasis sparingly.** Aim for no more than three prominent gold emphasis groups in one coherent screen or slide: for example a frame label, key result, and primary action. Count related decorative parts as a group rather than as separate pixels. Do not hide focus, status, or a necessary chart distinction to meet an arbitrary count. Empty space and restrained effects should help the content, not make it sparse by rule.

**Create depth through tonal differences.** The deepest program background is `#0A0A0A`, with `#121212`, `#151515`, and `#1A1A1A` surfaces. Subtle highlights, borders, and shadows can separate layers. Avoid replacing the palette with pure black or pure white as a default; these colors are not universally inaccessible, and may remain in source assets, shadows, forced-color modes, or another project's required style. Do not justify the brand choice with an unsupported claim that black always causes halation.

## 3. Set typography and layout

Use Cormorant Garamond for program display text and headings, Inter for body and interface text, and JetBrains Mono for data or code. Preserve the reference's fallback stacks when these fonts are unavailable. Load fonts through the host project's approved method rather than assuming they exist on every device.

For ordinary web body text, start at 16–18 CSS pixels, with line height around 1.5–1.75 and a reading measure around 45–65 characters. These are brand defaults, not universal WCAG thresholds. Captions and labels may be smaller when they remain comfortably readable. Large display text with tight line height needs particular checking for clipped accents, descenders, and wrapped lines.

Use the supplied spacing tokens consistently. The palette follows an 8-pixel rhythm with some 4-pixel and optical exceptions; the legacy `--space-36` token is 140 pixels. Do not silently convert it to 144 while claiming to preserve the existing design. Use responsive padding and actual layout needs instead of forcing a 24-pixel gap between every small component.

## 4. Use components and motion with a clear purpose

The reference preserves gold and outline buttons, dark and parchment cards, takeaway boxes, labels, glow levels, and theme overrides. Its light gold button uses dark ink text to repair the original low-contrast white label. Use semantic text and focus tokens so theme changes do not turn a dark foreground into light text on a gold background.

Keep controls operable by keyboard, with visible focus and clear labels. Use a 44-by-44 CSS-pixel target as the program's preferred touch size where appropriate. WCAG 2.2's AA target-size criterion has a 24-by-24 minimum with specified exceptions; do not present the brand's 44-pixel preference as that criterion.

Use motion to show a state change, connection, or progression. The reference durations are 150, 300, and 500 milliseconds; the old 200–800-only checklist contradicted its own tokens. Choose timing for the interaction. Ease-out is a useful default; linear timing can represent genuine continuous progress. An attention pulse or parallax effect is optional, and a static state often communicates better.

Honor reduced-motion preferences, preserve essential information without animation, and keep normal scrolling usable. Do not add scroll snapping, progress indicators, or parallax merely because an old reference title mentioned them. Avoid hiding content until an effect runs.

For images, use appropriate cropping, useful alternative text, and layouts that do not put essential text over an unpredictable background. For charts and diagrams, keep labels, units, and evidence conditions visible, and never encode meaning with color alone. Use the appropriate diagram or artifact skill for execution.

## 5. Check accessibility against the actual result

Measure foreground against the background immediately behind it, including gradients, opacity, hover, focus, selected, and disabled states. A contrast ratio belongs to a pair, not a color token. The reference's rounded example ratios are documentation aids; test thresholds using unrounded values.

For web text, WCAG 2.2 AA generally requires 4.5:1 for normal text and 3:1 for large text. AAA's text-contrast criterion uses 7:1 and 4.5:1 respectively, with defined exceptions. Meeting one contrast criterion does not establish whole-page conformance. Large text is generally at least 18 points, or 14 points bold; do not classify a small lightweight label as large text.

Check visible keyboard focus, semantic controls, accessible names, reflow, text resizing, and reduced motion as relevant to the surface. Low-contrast dust and sand colors are for nonessential decoration or truly inactive elements; do not use them for required captions, instructions, or attribution. A disabled control exemption does not make nearby explanatory text exempt.

## 6. Keep the brand voice and attribution appropriate

Use the shared writing skill for calm, clear practitioner language. Capitalize AI Fluent as its name. Explain deliberate practice, context engineering, and production quality when relevant rather than inserting them as slogans or unsupported claims of readiness.

For standalone program materials, use the attribution **Ravi Teja Palanki • AI Fluent Product Leadership** where it belongs. A program footer can use Inter with a restrained gold separator and sufficiently contrasting text. Put it in normal document flow or the medium's appropriate footer area. The old fixed position 80 pixels from the left was a layout example, not a safe rule for all screens and slides. Avoid duplicating a surrounding template's attribution or adding a promotional footer to a private personal email.

## 7. Verify and hand off

Inspect the output in its intended medium. Confirm the active design system, accurate content, legible text, consistent palette and type, useful spacing, appropriate gold emphasis, operable controls, and a usable reduced-motion or static state. Check phone or narrow layouts and the actual export where relevant. Do not claim visual or accessibility testing that was not performed.

Deliver the artifact and state any material rendering or verification limit. The desired effect is confident, considered communication; imagined prestige or a "rare book" impression is not an objective acceptance test.

Standards checked 13 Sep 2026: W3C guidance on [minimum text contrast](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html), [enhanced text contrast](https://www.w3.org/WAI/WCAG22/Understanding/contrast-enhanced.html), [minimum target size](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html), and [animation from interactions](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html). These define the cited accessibility distinctions, not the brand's aesthetic preferences.

**Revision 1.0.1, 13 Sep 2026.** Preserves the program palette, type scale, tokens, components, motion vocabulary, and attribution. Separates program and website systems, repairs contrast examples and missing references, and makes accessibility checks consistent with the actual component behavior.
