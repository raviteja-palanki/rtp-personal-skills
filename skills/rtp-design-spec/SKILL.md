---
name: rtp-design-spec
description: 'Encode an existing design system as DESIGN.md so people and coding agents can find exact tokens, understand their purpose, and apply them consistently. Use for design-to-engineering handoffs, agent-readable brand guidance, token audits, or Tailwind and DTCG exports. Triggers include "design.md", "design tokens", "design spec", "tokens.json", and "Tailwind config from design". Read the current brand and project implementation first; preserve their decisions and identify gaps instead of inventing a replacement system. Choose a token-only, standard, or full handoff; validate references and supported formats, check the intended consumer, and document motion, interaction, and accessibility work that the format cannot verify.'
author: Ravi Teja Palanki
version: v1.0.1_latest
created: 25 APR 2026
updated: 25 APR 2026
---

# Design Spec — Make a design system usable across handoffs

Create or review `DESIGN.md`: exact design tokens in YAML, with Markdown explaining their roles. The useful outcome is a handoff that preserves design decisions and exposes unresolved ones. A readable file can reduce guesswork; it cannot guarantee identical output across agents or replace a rendered review.

This skill encodes an existing system. If the task also needs new design decisions, develop those with the appropriate brand or UX skill and distinguish approved choices from proposals. The file format is maintained by Google Labs and remains **alpha**; verify the version of the tool that will consume it.

## 1. Establish the source and scope

Read the applicable brand guide, current project specifications, and implemented tokens. Record the source revision, intended surface, themes, and export destination. Resolve conflicting values before declaring a canonical file; a historical example does not override a newer project decision. For Ravi's website, check its current design-language documents and CSS. For AI-Fluent material, use that program's brand guidance.

Confirm whether `DESIGN.md` will be the maintained source or a generated view of another source, such as a token repository. State the synchronization direction and owner. Do not replace an existing source-of-truth arrangement simply because this skill produces Markdown.

Choose the smallest useful depth:

| Depth | Use it when | Deliver |
|---|---|---|
| Token-only | Exact values are enough for the bounded handoff | YAML tokens, with assumptions or omissions recorded in the handoff |
| Standard — default | Readers need values and the main usage decisions | Tokens plus Overview, Colors, Typography, and Components |
| Full | The handoff needs the complete visual system | Tokens and all eight sections below, with applicable implementation references |

These are working levels, not three levels of format conformance. A full document is not automatically safer than a concise, accurate one. An audit may need only findings, and an export task may need no prose rewrite.

## 2. Encode values without changing their meaning

The frontmatter of the **generated DESIGN.md** is separate from this skill's Claude frontmatter. Preserve the latter when editing the skill.

```yaml
---
version: alpha
name: Example System
description: A short description of the existing visual identity.
colors:
  primary: "#1A1C1E"
  on-primary: "#FFFFFF"
typography:
  body-md:
    fontFamily: Public Sans
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
rounded:
  none: 0px
  sm: 4px
spacing:
  md: 16px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px
---
```

This is a syntax example, not a replacement palette or proof that Public Sans is available in the target app. Use the source system's names and values. Typography also supports `fontFeature` and `fontVariation`; retain these when relevant and check their export mapping. Component properties include `backgroundColor`, `textColor`, `typography`, `rounded`, `padding`, `height`, `width`, and `size`.

Use explicit units for dimensions: `px`, `em`, or `rem`. A unitless `lineHeight` is a multiplier. Current alpha also permits numeric spacing values, such as column counts; do not turn a ratio into pixels during export. Current color support extends beyond six-digit hex to valid CSS colors. Quote hex strings in YAML. Confirm that the specific parser, exporter, and destination support the chosen notation. See the [format specification](https://github.com/google-labs-code/design.md/blob/main/docs/spec.md).

Apply five composition checks:

1. **Give the primary role an explicit meaning.** The documented format expects a primary palette, and the linter warns when colors lack `primary`. Map the existing role; do not invent an accent merely to remove a warning. Explain a deliberately limited palette or unsupported mapping.
2. **Reference the right value.** `{colors.primary}` points to a color; `{colors}` points to a group and is not a substitute. A component's typography may reference a composite such as `{typography.body-md}`. Keep aliases understandable, resolvable, and free of cycles; an arbitrary one-hop limit is not a design requirement.
3. **Share values when they share a meaning.** Components that use the same brand role should reference its token. Two roles may happen to have the same value and still deserve separate names because they can change independently.
4. **Group variants consistently.** Names such as `button-primary-hover`, `button-primary-active`, and `button-primary-disabled` make relationships visible. Describe focus, loading, pressed, and error states where applicable. Naming a state does not implement its behavior or keyboard interaction.
5. **Investigate apparently unused tokens.** A color unused by the file's components may serve a chart, an unlisted component, another theme, or a downstream consumer. Map it, document the dependency, or remove it only after checking actual use. A lint warning alone is not proof of dead content.

A broken reference should lead to a repair or an explicit unresolved finding. It should not invite an agent to silently choose a fallback. Similarly, explain the difference between `accent` and `secondary-accent` if both exist; names without roles leave the important decision unstated.

## 3. Put usage decisions where readers expect them

Use `##` headings in this order for the sections included. Keep exact values authoritative in tokens and explain application in prose. Repeating a value for clarity is allowed, but it creates another place to keep synchronized. The following examples illustrate the kind of decision to describe; they are not universal visual rules.

| Section | Explain | Keep distinct |
|---|---|---|
| **Overview** or **Brand & Style** | Audience, personality, and desired experience; for example, a restrained editorial surface | The overall direction versus detailed component specifications |
| **Colors** | Text, surface, interaction, status, and decorative roles; where each palette belongs | A color's role versus its numerical value; decorative accents versus essential status cues |
| **Typography** | Font purpose, hierarchy, fallback behavior, and loaded weights | Reading text versus headings and metadata; the actual family versus a hoped-for font |
| **Layout** or **Layout & Spacing** | Grid, maximum width, responsive behavior, density, gutters, and spacing rhythm | Page structure versus individual component padding |
| **Elevation & Depth** or **Elevation** | Tonal layers, borders, shadows, blur, and the hierarchy they express | Visual depth versus stacking behavior; link implementation details when needed |
| **Shapes** | Radius choices and where sharp, soft, or pill shapes belong | Shared shape rules versus a complete component inventory |
| **Components** | How tokens combine, which elements dominate, and how variants relate | Reusable components versus a specific page composition |
| **Do's and Don'ts** | Concrete combinations to use or avoid, with relevant exceptions | Testable guidance versus repeated personality adjectives |

Common vocabulary includes color roles `primary`, `secondary`, `tertiary`, `neutral`, `surface`, `on-surface`, and `error`; some systems add `on-primary`, `surface-container`, `inverse-surface`, and `outline`. Typography can use `display-lg/md`, `headline-lg/md/sm`, `title-lg/md`, `body-lg/md/sm`, and `label-lg/md/sm`. Keep a simpler hierarchy when that is what the system uses; nine to fifteen levels is not a quota.

Spacing commonly uses `xs` through `xl`, with semantic names such as `gutter`, `margin`, `container-padding`, or `section-margin`. Radius names may include `none`, `sm` through `xl`, `full`, `DEFAULT`, or a meaningful component-specific name. Preserve the difference between a scale step and a contextual role.

Component examples include primary, secondary, and ghost buttons; cards; inputs; chips; badges; list items; and navigation links. Explain special components such as a profile card or walk-stat card through their purpose and token relationships. A rule limiting accent groups or font weights should reflect the actual brand; do not impose a two-weight limit or ban mixed corner shapes on every product.

## 4. Validate the file and the handoff

Use the project's installed, versioned CLI when available. If installing a dependency is necessary, follow the project's package policy and record the version used. The documented invocation is:

```bash
npx @google/design.md lint DESIGN.md --format json
```

Review all findings. The original eight checks remain useful: `broken-ref`, `missing-primary`, `contrast-ratio`, `orphaned-tokens`, `token-summary`, `missing-sections`, `missing-typography`, and `section-order`. They examine reference resolution, palette and type omissions, declared component contrast, unused color references, token counts, missing groups, and document order. Counts describe the file; they do not by themselves prove a balanced design.

As checked on 13 September 2026, the CLI documents eleven rules, adding `unknown-key`, `token-like-ignored`, and `omitted-rules`. The optional `omitted` field records intentionally excluded token groups. Use it for a real scope decision, not to conceal a missing requirement. The [current CLI reference](https://github.com/google-labs-code/design.md#cli-reference) lists commands and severities.

Record the tool version, file tested, result, and unresolved findings. Aim for zero errors and reviewed warnings. If the tool could not run, say so; a manual reading is not a successful CLI run. An error-free exit does not mean warnings are absent. Export success is also not a substitute for linting.

Then check what the file cannot establish: fonts actually load, the intended theme resolves, text and controls remain readable, interaction states work, and the exported values reach the rendered surface. A contrast check on declared text/background pairs is a useful test, not a complete WCAG audit. Transparent colors, gradients, images, and dynamic backgrounds need checks in their rendered context.

## 5. Export for the actual consumer

Choose the requested output; do not create every format by default. Write exports to a new or reviewed destination so a failed conversion cannot destroy a maintained file.

| Destination | Export or mapping | Follow-up |
|---|---|---|
| Tailwind v3 | `npx @google/design.md export --format json-tailwind DESIGN.md` | Inspect the emitted configuration shape before merging into the existing configuration |
| Tailwind v4 | `npx @google/design.md export --format css-tailwind DESIGN.md` | Review the `@theme` output against the project's existing CSS token mappings |
| DTCG | `npx @google/design.md export --format dtcg DESIGN.md` | Check the emitted dialect, alias handling, and destination's import support |
| Figma | Use the available integration or a documented mapping | Check value types, units, property bindings, modes, and synchronization ownership |

`tailwind` remains an alias for the JSON export. It is not the v4 CSS export. Ravi's current website design-language specification uses Tailwind v4 and CSS-based configuration; do not introduce `tailwind.config.js` merely to follow an old example.

For Tailwind, verify font feature and variation settings and component states separately; an exported token is not a complete component. For DTCG consumers such as Style Dictionary or Tokens Studio, compatibility depends on the versions and mappings actually used. DTCG 2025.10 is a stable Community Group report, not a W3C Standard; see its [published status](https://www.designtokens.org/tr/2025.10/format/#status-of-this-document).

For a manual Figma handoff, a useful starting map is colors to Color variables, spacing and radii to numeric values, font families to strings, and font sizes and weights to appropriate numeric properties. These are mapping candidates, not a promise that every Figma property supports the same binding. Resolve `em` and `rem` against an explicit base when pixels are required. Map each component property to its compatible variable or style; “mode-bound aliased variable” is not a universal variable type. Verify any import plugin before describing it as automatic or lossless.

## 6. Preserve what sits outside the format

Five cases need additional work:

- **Motion:** preserve duration, easing, triggers, keyframes, and reduced-motion behavior in a linked motion specification. Historical Ravi examples include `palankiReveal`, `pulseCyan`, `dataStream`, `recession`, and `floatIso`; verify current names before use.
- **Interaction:** glass effects, magnetic buttons, scroll-driven stacking, and parallax need implementation guidance. A CSS declaration such as `backdrop-filter: blur(32px)` is not a valid substitute for a color token.
- **Accessibility:** link requirements and tested behaviors for keyboard use, focus, labels, contrast, zoom, and motion. DESIGN.md can contribute to that work; it is not a prerequisite for accessible design or evidence of conformance.
- **Wider brand identity:** voice, photography, illustration, and video guidance can remain in a brand book. Link the relevant source instead of forcing every discipline into UI tokens.
- **Unsettled design choices:** identify inconsistent names, values, and roles, then resolve or label them. A provisional token inventory can help that discussion; do not present it as an approved system.

The [Ravi migration example](references/ravi-design-example.md) preserves the earlier skill's token values for comparison. Use it to understand mapping, then reconcile it with the current brand and website before applying it.

## Deliver the requested artifact with its verification status

Provide the appropriate `DESIGN.md`, token-only file, lint report, export bundle, or migration map. A migration map should show the source item, destination token or section, changed meaning if any, and items retained elsewhere. For an audit, give the path, finding, consequence, and suggested repair.

State what was checked, what remains unresolved, and which file owns future changes. “Ready for implementation” should mean the receiving team can follow the decisions and see the gaps; it should not imply that a generated interface has already passed visual, behavioral, or accessibility testing.

Revision note: wording and compatibility review completed 13 September 2026. Original `created` and `updated` frontmatter values are preserved; this revision is identified by the increased skill version.
