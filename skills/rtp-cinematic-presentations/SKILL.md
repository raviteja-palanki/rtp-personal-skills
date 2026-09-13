---
name: rtp-cinematic-presentations
version: v1.0.1_latest
description: |
  Design cinematic HTML or React presentations for keynotes, pitches, masterclasses, product launches, and related slide content. Begin with the audience, narrative, delivery mode, and active brand system. Use restrained emphasis, readable typography, layered surfaces, purposeful motion, and clear navigation. Includes 20 slide-pattern recipes and a legacy gold, teal, and purple CSS palette with component and reveal styles. Read the presentation reference before implementation; the CSS is a starting layer, not a complete slide runtime. Preserve zoom, keyboard use, reduced-motion behavior, and readable content without scripting. Use rtp-personal-branding for the current cross-medium or website design contract and rtp-ai-fluent-brand for program-specific identity. Verify the actual deck and its intended export rather than treating the template as production-tested.
---

# Cinematic presentations

Build a presentation whose sequence, typography, visuals, and pacing make the idea easier to understand. A cinematic treatment should serve the message and the audience's control of the experience.

Use this skill for HTML or React slide experiences. For PowerPoint, Gamma, or PDF, carry over the narrative and design principles through the appropriate artifact workflow; browser CSS does not provide native editing or guarantee a faithful export.

Read [Presentation recipes and implementation](references/presentation-recipes.md) when building. The accompanying [CSS recipes](references/cinematic.css) preserve the original visual vocabulary with usability repairs. Six companion files promised by the earlier skill were not found in the searched library. This package provides 20 pattern recipes and implementation requirements; it does not claim to contain a complete HTML or React template library or tested navigation runtime.

## 1. Establish the story and delivery conditions

Identify the audience, purpose, time available, key decision or learning outcome, and supplied evidence. Determine whether the deck supports a speaker, is read independently, or must work as a static export. A self-paced or exported deck needs the explanation that a live speaker would otherwise provide.

Plan the argument before styling. Give each slide a clear job: establish the problem, explain a mechanism, compare choices, show evidence, practice a decision, or complete the story. Keep qualifications near the claims they change. Label illustrative numbers, attribute quotes, and preserve exact evidence conditions.

For teaching, ensure the learner has the exercise inputs when needed. For an investor or product pitch, distinguish current capabilities, demonstrated results, projections, and planned work. A reveal cannot turn an uncertain number into established evidence.

## 2. Choose the active visual identity

Use `rtp-personal-branding` for Ravi's current cross-medium guidance and canonical website specification, or `rtp-ai-fluent-brand` for AI Fluent program work. Preserve an explicit user choice and the existing project's design contract.

The bundled cinematic palette is a **legacy deck variant**, not identical to either guide: its main gold is `#D4A726`, and its deepest surface is `#020202`. Keep it when revising a deck that uses it, or select it deliberately for a new deck. Do not silently mix it with the AI Fluent program's `#D4AF37` palette or replace the website's current editorial type system.

Three principles guide the treatment:

- **Readability:** Size text for the actual screen and viewing distance. The old 16–18px body sizes suit some browser reading; projected slides usually need a different scale. Aim for strong primary-text contrast, with 7:1 as a brand target, and check every meaningful label against its actual background.
- **Restraint:** Use roughly three prominent gold emphasis groups per slide as a compositional guide. Preserve necessary focus, status, and chart meaning even when that requires more. Teal and purple support distinctions rather than decorate every surface.
- **Depth:** Use the supplied tonal layers, subtle borders, and limited glow. The palette's near-black choice is an aesthetic preference, not a general claim that pure black is inaccessible. Opaque surfaces are often clearer than glass when backgrounds are busy.

## 3. Select the slide patterns the lesson needs

The reference preserves these 20 patterns: cover, section divider, statement, text-and-visual split, column grid, statistics, quote, comparison, timeline, scaffold or pyramid, mnemonic, loop, context window, checklist, profile, gallery, takeaway, pricing tabs, action, and closing.

Choose by function and adapt counts to the content. A three-column recipe does not require three ideas; a pyramid should represent a real hierarchy. An arrow must mean a sequence, dependency, or transition the explanation supports. A framework acronym is useful only when its terms help the audience reason.

Provide a complete static state for every pattern. Replace interactive pricing tabs with visible comparison content in an export. Keep sources and accessible descriptions readable. A profile slide must use supported credentials, and a closing slide need not contain a sales request or thank-you formula.

## 4. Implement navigation as usable behavior

The reference includes a document outline and a navigation contract. Use ordinary scrolling as the baseline. Add previous and next controls, a slide counter, and progress when they improve orientation. Give buttons accessible names and visible focus, provide sensible boundary states, and keep them from covering content at narrow widths or zoom.

Preserve browser zoom. Do not use `user-scalable=no` or a maximum scale of one. Avoid fixed slide heights that clip overflowing content. Scroll snapping is optional; use it only if it does not prevent reading a tall slide. The legacy breakpoint was 768px, a starting point to test rather than a device definition.

Keep keyboard shortcuts scoped to the presentation. Do not intercept typing, editable content, browser shortcuts, or an embedded control's own keys. In a React implementation, clean up listeners and observers when components unmount and keep state synchronized with manual scrolling and history where supported.

## 5. Make motion optional and truthful

The CSS retains the six `data-reveal` directions and 100–800ms stagger values, using a 650ms reveal transition. Use only the delays the narration needs. A 100ms progress transition can be linear when it represents continuous progress.

Content is visible by default. Add a pending reveal state only after the observer is ready, and reveal it if setup fails or the content receives focus. Keep reduced-motion and print states fully visible. Do not leave information at zero opacity while relying on an absent script to display it.

Static label dots, mesh, grid, and glow are the defaults. Optional pulse, mesh movement, and grid keyframes remain available. The original 25-second mesh and 8-second grid conflicted with its "no animation over one second" checklist. Judge motion by its purpose, control, and accessibility rather than that arbitrary limit. Ongoing nonessential movement needs appropriate pause or stop behavior; reduced-motion support alone is not a substitute for every applicable requirement.

Do not use animated counters to imply a live measurement or invent intermediate values that could be mistaken for data. Reduce motion, glow, and blur when they distract, obscure text, or perform poorly on the target device.

## 6. Verify the deck and its export

Check the actual presentation, not only the source or a title slide. Review every slide for accurate content, legible type, clipping, overlap, focus visibility, and coherent pacing. Test navigation boundaries, manual scrolling, keyboard operation, narrow layout, zoom, missing fonts, reduced motion, and disabled scripting where relevant.

If exporting, verify that all content appears, controls do not print as clutter, and color and pagination remain readable. A projected deck, browser deck, and PDF can need different adaptations. State which modes were checked and which remain unverified.

Use a meaningful attribution appropriate to the selected brand and delivery context. Deliver the requested artifact with a concise note on material choices or limitations. Claims such as "world-class," "production-tested," or "TED-ready" are not verification evidence and should not replace these checks.

Sources checked 13 Sep 2026: W3C guidance on [resizing text](https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html), [pause, stop, and hide](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html), and [animation from interactions](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html). These inform the accessibility conditions; they do not prescribe a visual style.

**Revision 1.0.1, 13 Sep 2026.** Preserves all 20 slide patterns, legacy tokens, component styles, reveal vocabulary, and visual effects. Clarifies brand precedence, unavailable resources, navigation requirements, zoom, default visibility, motion control, and export checks.
