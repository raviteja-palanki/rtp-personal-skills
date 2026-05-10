---
name: rtp-design-spec
description: Generates and validates DESIGN.md format files — Google Labs' emerging standard for describing design systems to coding agents. Use when handing a design system to engineering, when documenting a brand for AI consumption, when standardizing tokens across products. Triggers on "design.md", "design tokens", "design spec", "DESIGN.md", "tokens.json", "Tailwind config from design", "agent-readable design system."
---
# design-spec — Agent-Portable Design Systems

A skill for producing and validating `DESIGN.md` files. DESIGN.md is Google Labs' format spec (`@google/design.md`, alpha) for describing a design system as one Markdown file: YAML frontmatter for tokens, prose for rationale. The output is meant to be consumed by coding agents (Claude Code, Cursor, v0, Bolt, Gemini Code Assist) so they produce on-brand UI without reading a 50-page Figma file.

This skill does NOT design systems from scratch. It encodes existing systems into a portable format, validates them against the spec, and exports them to Tailwind / DTCG / Figma.

---

## DEPTH DECISION

Three depths. Pick before writing.

| Depth | When | What you ship |
|---|---|---|
| **Frontmatter-only** | The system has tokens but no prose discipline yet, or you need a quick handoff to one agent | YAML frontmatter only. Skip prose sections. Lints will warn on `missing-typography` if absent. |
| **Standard** | The system has tokens AND opinions about how they're used | Frontmatter + 4 sections: Overview, Colors, Typography, Components. Skip Layout/Elevation/Shapes/Don'ts if not load-bearing. |
| **Full** | The system is the visual identity of a product or brand and needs to survive multi-agent handoffs | Frontmatter + all 8 sections. Lint-clean. Token references resolve. Contrast checked. |

Default to **Standard**. Upgrade to Full only when the system is the contract between design and engineering for a real product. Frontmatter-only is for prototypes and one-off agent briefs.

---

## THE STRUCTURAL INSIGHT

Most design system documentation is written for one of two audiences: humans (style guides, brand books) or engineers (Storybook, Tailwind config, Figma libraries). Both fail the third audience that now matters more than either: **coding agents**.

A coding agent given a 50-page Figma file with auto-layout, variants, and prose annotations gets it wrong half the time. The same agent given a DESIGN.md produces consistent UI in 30 seconds — every time, across sessions, across providers.

The 0.1% angle: **AI-agent-portable design.** DESIGN.md is the contract between a brand and the agents that will produce surfaces in that brand's voice. The skill is not about making design systems — it's about making them survive the human → AI handoff.

This is why every section has prescribed structure, why tokens use `{path.to.token}` references instead of hard-coded values, why a `primary` color is required even for monochrome systems. The format optimizes for one thing: an agent reading it cold and producing on-brand output without escalating questions.

The corollary: a design system that can't be expressed as a clean DESIGN.md probably isn't a design system. It's a collection of opinions.

---

## THE FORMAT IN ONE PAGE

A DESIGN.md file has two layers separated by `---` fences.

**Layer 1 — YAML frontmatter (machine-readable tokens):**
```yaml
---
version: alpha          # optional, current spec version
name: <string>          # required
description: <string>   # optional one-liner
colors:
  <token-name>: "#RRGGBB"
typography:
  <token-name>:
    fontFamily: <string>
    fontSize: <Dimension>      # 48px, 3rem, 1.5em
    fontWeight: <number>       # 400, 700, 900
    lineHeight: <number|Dim>   # 1.6 (multiplier) or 24px
    letterSpacing: <Dimension> # -0.02em, 0.1em
    fontFeature: <string>      # optional, font-feature-settings
    fontVariation: <string>    # optional, font-variation-settings
rounded:
  <scale>: <Dimension>     # sm: 4px, md: 8px, full: 9999px
spacing:
  <scale>: <Dimension>     # base: 16px, gutter: 24px
components:
  <component-name>:
    backgroundColor: <Color | "{colors.primary}">
    textColor: <Color | "{colors.on-primary}">
    typography: "{typography.label-md}"
    rounded: "{rounded.sm}"
    padding: <Dimension>
    height: <Dimension>
    width: <Dimension>
    size: <Dimension>
---
```

**Layer 2 — Markdown body (8 sections in order):**
1. `## Overview` (or "Brand & Style") — personality, audience, emotional response
2. `## Colors` — palette rationale and roles
3. `## Typography` — font choices and hierarchy
4. `## Layout` (or "Layout & Spacing") — grid model, spacing rhythm
5. `## Elevation & Depth` — shadows, tonal layers, glass
6. `## Shapes` — corner radius philosophy
7. `## Components` — how atoms compose
8. `## Do's and Don'ts` — guardrails

**Reference syntax:** `{path.to.token}` resolves at lint time. Examples: `{colors.primary}`, `{rounded.lg}`, `{typography.body-md}`, `{spacing.md}`.

**Color format:** `#RRGGBB` hex in sRGB only. No `rgba()`, no `hsl()` in token values (use them in prose for transparency notes).

**Dimension format:** Number + unit. Valid units: `px`, `em`, `rem`. Unitless `lineHeight` is a fontSize multiplier (CSS best practice).

---

## THE 8 SECTIONS WALKTHROUGH

### 1. Overview (also "Brand & Style")
**Goes here:** Brand personality, target audience, emotional response, the one-line aesthetic ("Architectural minimalism meets journalistic gravitas").
**Does NOT go here:** Specific colors, font names, component examples. Keep it tonal. The agent uses Overview when no specific rule applies — it's the fallback.
**Example tone:** "The UI evokes a premium matte finish — a high-end broadsheet or contemporary gallery. Trustworthy, restrained, expert."
**Canonical token names:** none — this is pure prose.

### 2. Colors
**Goes here:** Color palette explanation. Which color drives interaction, which carries text, which is decorative. Why each choice exists.
**Does NOT go here:** The literal hex values (those live in YAML frontmatter and are referenced by name in prose). Don't list every shade — only the semantic roles.
**Example tone:** "Primary (#1A1C1E) is deep ink for headlines. Tertiary (#B8422E) is the sole driver for interaction — used exclusively for primary actions."
**Canonical token names:** `primary`, `secondary`, `tertiary`, `neutral`, `surface`, `on-surface`, `error`. Material-derived systems also use `on-primary`, `surface-container`, `inverse-surface`, `outline`.

### 3. Typography
**Goes here:** Font family choices, the rationale (why this serif, why this sans), how weight maps to hierarchy.
**Does NOT go here:** Every font size in pixels (frontmatter has them). Don't enumerate 15 levels — describe the system.
**Example tone:** "Public Sans Semi-Bold for headlines establishes institutional voice. Space Grotesk in uppercase for technical metadata evokes a digital stopwatch."
**Canonical token names:** `display-lg`, `display-md`, `headline-lg`, `headline-md`, `headline-sm`, `title-lg`, `title-md`, `body-lg`, `body-md`, `body-sm`, `label-lg`, `label-md`, `label-sm`. Most systems use 9-15 levels.

### 4. Layout (also "Layout & Spacing")
**Goes here:** Grid model (fluid vs. fixed-max-width), spacing rhythm (8px base?), gutter philosophy, density vs. breath.
**Does NOT go here:** Component-specific padding (that goes in Components). Don't conflate page layout with element padding.
**Example tone:** "Fluid grid for mobile, fixed-max-width 1200px for desktop. Strict 8px scale, 4px half-step for micro-adjustments."
**Canonical token names:** `xs`, `sm`, `md`, `lg`, `xl`, plus semantic ones like `gutter`, `margin`, `container-padding`, `section-margin`.

### 5. Elevation & Depth
**Goes here:** How visual hierarchy is conveyed. Shadow specs, tonal layers, glass effects, border-only flat designs.
**Does NOT go here:** Z-index values (those are implementation). Don't describe specific component shadows here — describe the SYSTEM (e.g., "all elevated surfaces use blurred ambient shadows tinted with primary").
**Example tone:** "Depth through tonal layers, not heavy shadows. Background uses soft off-white; primary content sits on pure white cards."
**Canonical token names:** No standard tokens yet (the spec is still alpha here). Most systems describe levels in prose: Level 1 (base), Level 2 (card), Level 3 (modal).

### 6. Shapes
**Goes here:** Corner radius philosophy. Why 4px vs. 16px. Where shapes get sharper or softer.
**Does NOT go here:** Every component's corner radius (frontmatter `rounded` has them). Describe the language, not the inventory.
**Example tone:** "Architectural sharpness — minimal 4px corners for engineered feel. Buttons and cards never exceed 8px."
**Canonical token names:** `none` (0), `sm`, `md`, `lg`, `xl`, `full` (9999px). Some systems add `DEFAULT` or component-scoped names like `card-recession`.

### 7. Components
**Goes here:** How atoms compose. Which components are heroes, how variants relate, interaction state grouping.
**Does NOT go here:** Layout of specific pages (that's not in the spec — keep it to atom-level patterns).
**Example tone:** "The card-profile is the hero container with rounded-xl and a tinted ambient shadow. card-walk-stat uses high-contrast secondary for data viz."
**Canonical token names:** Common atoms: `button-primary`, `button-secondary`, `button-ghost`, `card-default`, `input-field`, `chip`, `badge`, `list-item`, `nav-link`. Variants follow the pattern `{component}-{state}`: `button-primary-hover`, `button-primary-active`, `button-primary-disabled`.

### 8. Do's and Don'ts
**Goes here:** Practical guardrails. What to never combine. What contrast ratios to maintain. Maximum simultaneous accents.
**Does NOT go here:** Brand personality reminders ("be friendly!"). Make every line actionable.
**Example tone:**
- "Do use primary color only for the single most important action per screen"
- "Don't mix rounded and sharp corners in the same view"
- "Do maintain WCAG AA contrast (4.5:1) for body text"
- "Don't use more than two font weights on a single screen"
**Canonical token names:** none — this is rules, not tokens.

---

## TOKEN COMPOSITION RULES

The format only works if tokens compose cleanly. Five rules.

**Rule 1 — Primary always exists.** Even monochrome systems need a `primary` color. Linter throws `missing-primary` warning otherwise, and downstream agents auto-generate one (which produces drift across surfaces).

**Rule 2 — References go one level deep, not zero, not three.**
```yaml
# CORRECT — direct reference to a primitive
button-primary:
  backgroundColor: "{colors.primary}"

# WRONG — reference to a group, not a value
button-primary:
  backgroundColor: "{colors}"

# AVOID — chained references work but obscure intent
colors:
  brand: "#9D4EDD"
  primary: "{colors.brand}"   # works but the linter prefers direct
```

**Rule 3 — Components reference, never duplicate.** If three components use the same purple, all three reference `{colors.primary}` — never copy `#9D4EDD` into each. When the brand color shifts, one edit propagates.

**Rule 4 — Variant components share a name root.** Hover, active, disabled, pressed: all named `{component}-{state}`. The agent matches the root and treats them as a state machine.

**Rule 5 — Orphan tokens are a smell.** A color defined in `colors:` but never referenced by any component is dead weight. The linter emits `orphaned-tokens` (warning). Either reference it from a component or delete it.

**Failure modes when these rules break:**
- Broken `{colors.primary-60}` reference when only `colors.primary` exists → linter error, agent picks a fallback that drifts from brand
- Two colors named `accent` and `secondary-accent` with no usage → agent treats them interchangeably, surfaces become inconsistent
- Component declares hex literal instead of token reference → brand color update misses that component, you get a one-off purple in the wild

---

## LINTING RULES

The `@google/design.md` CLI runs eight rules against any DESIGN.md. Each emits structured findings (severity + path + message).

| Rule | Severity | What it catches | Why it matters |
|---|---|---|---|
| `broken-ref` | error | A `{path.to.token}` that doesn't resolve to any defined token | Agents will pick a fallback color, drifting from brand. Hard fail. |
| `missing-primary` | warning | Colors defined but no `primary` key | Agents auto-generate a primary, which is unpredictable across runs |
| `contrast-ratio` | warning | Component `backgroundColor`/`textColor` pair below WCAG AA (4.5:1) | Accessibility regression — body text becomes unreadable |
| `orphaned-tokens` | warning | A color token defined but never used in any component | Dead weight; suggests the system is bloated or the token is mis-named |
| `token-summary` | info | Counts tokens defined per section | Sanity check — a system with 60 colors and 2 typography levels is unbalanced |
| `missing-sections` | info | Optional sections (`spacing`, `rounded`) absent when other tokens exist | Surfaces gaps that agents will paper over with defaults |
| `missing-typography` | warning | Colors defined but typography is empty | Agents pick default fonts (usually system-ui), which guarantees brand drift |
| `section-order` | warning | Markdown sections appear out of canonical order | Some consumers parse top-to-bottom; out-of-order sections may be skipped |

**Run command:**
```bash
npx @google/design.md lint DESIGN.md --format json
```

Exit code `1` if any error finding, `0` otherwise. Wire this into CI for any project shipping a DESIGN.md.

---

## EXPORT PATHS

DESIGN.md is the source. Three outputs derive from it.

### Tailwind theme config
```bash
npx @google/design.md export --format tailwind DESIGN.md > tailwind.theme.json
```
**Pros:** Drops directly into `tailwind.config.js` under `theme.extend`. Coding agents using Tailwind get tokens as utility classes (`bg-primary`, `text-on-primary`, `rounded-card-recession`).
**Cons:** Tailwind doesn't support every DESIGN.md construct (e.g., `fontFeature` strings need manual mapping). Component tokens flatten — Tailwind has no native concept of `button-primary-hover` as a single object.
**Use when:** The codebase is Tailwind-first and you want tokens as classes.

### DTCG tokens.json
```bash
npx @google/design.md export --format dtcg DESIGN.md > tokens.json
```
**Pros:** Compatible with Style Dictionary, Tokens Studio, Specify. Becomes the lingua franca for any design tool that supports the W3C Design Tokens Format Module.
**Cons:** DTCG is also a moving spec — verify the consumer supports the version emitted. Component tokens may not round-trip into Figma cleanly.
**Use when:** The consumer is Figma Tokens Studio, Style Dictionary, or any non-Tailwind tooling.

### Figma variables (manual)
**There is no auto-export to Figma.** The mapping is manual but mechanical.

| DESIGN.md | Figma Variable Type | Figma Collection |
|---|---|---|
| `colors.<name>` | Color | Colors |
| `rounded.<scale>` | Number (px) | Radius |
| `spacing.<scale>` | Number (px) | Spacing |
| `typography.<name>.fontFamily` | String | Type/Family |
| `typography.<name>.fontSize` | Number (px) | Type/Size |
| `typography.<name>.fontWeight` | Number | Type/Weight |
| `components.<name>.<prop>` | Mode-bound aliased variable | Components |

**Pros:** Designers can pull tokens into Figma with full mode support (light/dark).
**Cons:** Manual. Drift between DESIGN.md and Figma is a real risk. Treat DESIGN.md as canonical and re-sync Figma on every brand release.
**Use when:** Designers and engineers must share a token vocabulary.

---

## RAVI'S DESIGN DNA AS DESIGN.MD

Ravi's `ravi-personal-branding` (v2.1) is 1,251 lines. The frontmatter below is the agent-readable distillation. Pair with the markdown sections in the enhanced `ravi-personal-branding` skill.

```yaml
---
version: alpha
name: Ravi Personal Branding
description: >
  Architectural minimalism meets warm intelligence. Premium matte aesthetic with four
  semantic color identities (Model/Harness/Tools/Environment), four-typeface stack,
  recession glass cards, paper canvas overlay.
colors:
  primary: "#9D4EDD"        # Aureate Purple — Model (intelligence, drop caps, evals accent)
  secondary: "#F43F5E"      # Crimson Rose — Harness (warnings, anti-patterns, harness series)
  tertiary: "#F59E0B"       # Amber — Tools (capabilities, L3 badges, systems accent)
  quaternary: "#06B6D4"     # Cyan — Environment (default homepage hero, CTA halos)
  success: "#10B981"
  surface-light: "#FCFDFD"
  surface-dark: "#030407"
  on-surface-light: "#202226"
  on-surface-dark: "#F9FAFB"
typography:
  display:
    fontFamily: Instrument Serif
    fontSize: 4.5rem
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.02em
  h1:
    fontFamily: Inter
    fontSize: 4rem
    fontWeight: 900
    lineHeight: 0.95
    letterSpacing: -0.03em
  body-md:
    fontFamily: Newsreader
    fontSize: 1.2rem
    fontWeight: 400
    lineHeight: 1.7
  meta:
    fontFamily: JetBrains Mono
    fontSize: 0.75rem
    fontWeight: 700
    letterSpacing: 0.15em
rounded:
  sm: 4px                  # neon highlight, pastel highlight
  md: 12px                 # folder cards
  lg: 20px                 # level badges
  card-recession: 40px     # signature 40px rounded-top recession glass
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 32px
  xl: 64px
components:
  card-glass:
    backgroundColor: "{colors.surface-dark}"
    rounded: "{rounded.card-recession}"
    padding: 32px
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "#FFFFFF"
    typography: "{typography.meta}"
    rounded: "{rounded.sm}"
    padding: 12px
---
```

The pairing principle: frontmatter is the contract; prose is the rationale. An agent given this frontmatter alone can build a passable Ravi-branded surface. Adding the 8 prose sections (in `ravi-personal-branding` v2.1+) closes the gap from passable to on-brand.

---

## DELIVERABLE FORMAT

Every `design-spec` task produces one or more of:

1. **A complete `DESIGN.md` file** — frontmatter + 8 sections, lint-clean against `@google/design.md`, ready to commit alongside the codebase or brand kit.
2. **A frontmatter-only spec** — when the system is being prototyped or handed to a single agent for a specific surface.
3. **A lint report** — when an existing DESIGN.md is being audited. Emit findings with file path, severity, and one-line fixes.
4. **An export bundle** — `tailwind.theme.json` + `tokens.json` + Figma mapping table when the system is being shipped to an engineering team.
5. **A migration map** — when converting an existing skill (like `ravi-personal-branding`) into DESIGN.md, produce a mapping table from existing tokens to DESIGN.md tokens, flagging any concept that doesn't fit (animations, scroll-driven effects).

**Quality bar:** the file passes `npx @google/design.md lint --format json` with zero errors and either zero warnings or warnings that are explicitly justified in the prose.

---

## RED TEAM — When DESIGN.md Is the Wrong Tool

DESIGN.md is alpha and opinionated. Three classes of system where it will fail:

**1. Animation-heavy systems.** DESIGN.md has no concept of motion tokens (duration, easing, keyframe patterns). Ravi's own brand has 8+ named keyframes (`palankiReveal`, `pulseCyan`, `dataStream`, `recession`, `floatIso`). The format silently drops them. If motion IS the brand — Stripe's old payment flow, Linear's hover physics, anything where signature animations carry identity — DESIGN.md captures only the static skeleton. Document motion separately and reference it from prose.

**2. Interaction-as-identity systems.** Glassmorphism with `backdrop-filter` chains, magnetic button physics, scroll-driven recession stacking, parallax — none of these have token primitives in the spec. You can stuff `backdrop-filter: blur(32px)` into a component's `backgroundColor` as a string, but the linter won't validate it and downstream consumers won't reproduce it. For these systems, ship DESIGN.md for the static layer + a separate motion spec.

**3. Accessibility-critical systems.** DESIGN.md lints contrast for component backgroundColor/textColor pairs but doesn't model focus rings, screen reader labels, motion-reduced fallbacks, or color-blindness palettes. For systems with WCAG AA+ as a hard floor (government, healthcare, education), DESIGN.md is necessary but not sufficient. Pair it with WCAG audit prose and tested component fallbacks.

**4. Brand-only documentation.** If the audience is humans reading a brand book — voice, tone, photography style, illustration treatment, video editing standards — DESIGN.md is the wrong format. It's a UI design system spec, not a brand identity guide. Use Brand.md or a traditional brand book.

**5. Pre-token systems.** A system with 4 ad-hoc colors and no naming discipline shouldn't be force-fit into DESIGN.md. The format presupposes a system with semantic roles. Trying to write DESIGN.md for a chaotic palette produces a chaotic DESIGN.md. Stabilize the system first; encode it second.

**The honest read:** DESIGN.md is the right tool for the contract between a static design system and the agents that will produce surfaces in that system. It is not a brand book, a motion spec, an accessibility audit, or a pre-system grooming exercise. Used inside its envelope, it survives the human → AI handoff better than any alternative. Used outside, it's friction without payoff.

---

## REFERENCES

- Spec: `https://github.com/google-labs-code/design.md/blob/main/docs/spec.md`
- CLI: `npm install @google/design.md` or `npx @google/design.md`
- Examples: `paws-and-paths`, `atmospheric-glass`, `totality-festival` in the design.md repo
- Companion skill: `ravi-personal-branding` v2.1+ — section "DESIGN.md Export — Agent-Portable Design System"
- Sister skill: `learn-site-design` — for learn.ravitejapalanki.com tokens (4-color identity #9D4EDD/#F43F5E/#F59E0B/#06B6D4)
