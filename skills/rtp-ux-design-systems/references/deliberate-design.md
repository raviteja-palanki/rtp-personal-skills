# Deliberate design: review defaults without inventing bans

Read six signals before choosing a style: artifact kind, the user's tone words, references, audience, existing assets, and practical constraints. State the design read when it helps alignment. Resolve only consequential uncertainty; neither zero questions nor exactly one is a universal requirement.

## Three optional dials

| Dial | Low | High | Historical seed |
|---|---|---|---:|
| DESIGN_VARIANCE | Symmetric, predictable | Expressive, asymmetric | 8 |
| MOTION_INTENSITY | Static | Elaborate choreography | 6 |
| VISUAL_DENSITY | Spacious | Compact information | 4 |

These 1–10 values are a design shorthand, not measured user preferences or mandatory defaults. Original examples: minimalist 5–6/3–4/2–3; premium consumer 7–8/5–7/3–4; experimental 9–10/8–10/3–4; trust-focused 3–4/2–3/4–5. Choose from the actual brief. A preservation redesign follows existing choices; an overhaul does not automatically need +2 motion or variance. Accessibility overrides an inappropriate effect at every setting.

## Named default cautions

**Automatic tech styling:** question an unexplained purple/blue glow, centered dark mesh hero, three equal feature cards, glass everywhere, endless motion, or Inter/slate pairing. Each can still be appropriate. Reuse is not evidence that a human or model made the design.

**Serif discipline:** choose a serif for a clear brand/editorial reason, not because “premium” appeared in the prompt. Fraunces and Instrument Serif are not universally banned; Instrument Serif is part of Ravi's governing brand. Geist Display, Cabinet Grotesk, PP Neue Montreal and GT Walsheim are alternatives whose license and available files need checking.

**The Lila caution:** neutral bases with one intentional accent can avoid an automatic AI-purple aesthetic. If violet is part of the brand or task, use it well. Functional and data colors may require several hues.

**Warm consumer palette caution:** the inherited defaults to examine were backgrounds #f5f1ea/#f7f5f1/#fbf8f1/#efeae0/#ece6db, accents #b08947/#b6553a/#9a2436/#9c6e2a and text #1a1714/#1a1814. They are not forbidden colors. Consider silver/smoke, forest/bone/amber, black/tan, cobalt/cream, terracotta/slate or restrained monochrome when they fit. Do not change an accepted identity merely to avoid using a palette twice.

**Consistency:** keep roles and a coherent radius system stable. A deliberate mixture of sharp and rounded elements or warm and cool neutrals can be valid. Document the rule rather than demanding one radius or one temperature everywhere.

## Layout checks and their boundaries

| Original check | Useful interpretation |
|---|---|
| Hero fits viewport; two-line headline; 20-word subtext | Keep the main message and action discoverable, but allow scrolling, translation, zoom and necessary qualification. A four-line heading can be correct. |
| Four hero text elements; one primary/one secondary CTA | Reduce competing priorities; retain essential trust, pricing or consequence information when the decision requires it. |
| One eyebrow per three sections | Avoid redundant labels; repeated taxonomy or editorial kickers can be useful and may be brand-required. |
| No third zigzag; each layout family once; eight sections need four families | Check monotony without sacrificing consistent reading or comparable small multiples. Do not force novelty by counting layouts. |
| No split header by default | Use columns when they support reading order and a meaningful relationship. |
| Desktop nav one line, maximum 80px | Avoid accidental wrap; a planned multi-row or expanded navigation can be valid. |
| Bento cells exactly match content | Avoid empty decorative placeholders unless their purpose is explicit; do not omit real content to fit a grid. |
| No centering above variance 4 | Alignment follows content, reading order and the brief; a dial does not prohibit a centered layout. |

## Complete interaction states

Implement relevant loading, empty, error, pressed, focus, disabled, partial and successful states. A skeleton can preserve layout; a spinner can honestly represent indeterminate work. Neither is universally required. Visible feedback does not have to move physically.

Buttons need readable text on their actual background. On photographic backgrounds, provide a stable contrast treatment when needed. CTA labels should describe the action; more than three words or wrapping under zoom/localization is not a failure. Repeated placement of the same action is fine when wording and destination remain consistent.

Forms need programmatic labels, readable helper/error text and visible focus. Above-input labels are a useful default; an accessible checkbox or compact specialized control can use another arrangement. A placeholder is not the sole label. Assess text and required non-text boundaries using their respective criteria.

## Provenance

The previous skill attributed this lens to “taste-skill by Sam Rowe.” That authorship could not be verified in this pass. The public [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) repository contains the matching 8/6/4 dials and related v1 anti-default concepts, under MIT copyright 2026 Leonxlnx. The current wording is a context-sensitive adaptation of the supplied local material, not an endorsement of every upstream instruction or an assertion that the entire local section has a single confirmed origin. The verified license is included in `../licenses/taste-skill-MIT.txt`.
