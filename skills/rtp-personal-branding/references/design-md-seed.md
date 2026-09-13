# DESIGN.md seed and adaptation notes

The complete original token groups and component records below are retained as a **legacy V8 seed**. It is not the canonical current website specification or a newly linted export. Use `rtp-design-spec` to adapt it to the installed alpha format, validate references and supported properties, and inspect the resulting UI.

The website's current series colors are #9D4EDD / #F43F5E / #F59E0B / #06B6D4. The seed's darker `series-*` values originated in light-article styling; do not use them for small text on dark cards without checking contrast. `success` green and the mistake-card red also fail normal-text contrast on light paper. Use dark readable text with the color as a labeled accent, or a measured accessible variant. The highlight records describe translucent compositions in comments; a flat exported fill does not recreate them.

Some fields are project extensions: typography `fontFeature`, component `size`, and spacing tokens must be checked against the actual parser/exporter. `rgba()` is valid CSS color syntax; unsupported lint analysis is not a contrast pass. An unused token is not automatically a defect. No 30-second build promise, lint success, or pixel fidelity is established by this file.

```yaml
---
version: alpha
name: Ravi Personal Branding legacy V8 seed
description: >
  Architectural minimalism meets warm intelligence. Premium matte aesthetic with four
  semantic color identities (Model/Harness/Tools/Environment), four-typeface stack,
  recession glass cards with 40px rounded-top, paper canvas overlay for light surfaces.
colors:
  primary: "#9D4EDD"             # Aureate Purple — Model (intelligence, drop caps, evals accent)
  secondary: "#F43F5E"            # Crimson Rose — Harness (warnings, anti-patterns, harness series)
  tertiary: "#F59E0B"             # Amber — Tools (capabilities, L3 badges, systems accent)
  quaternary: "#06B6D4"           # Cyan — Environment (default homepage hero, CTA halos)
  success: "#10B981"              # Emerald (functional, positive states)
  surface-dark-base: "#030407"    # Landing / homepage / presentations
  surface-dark-card: "#0a0b10"    # Folder cards, telemetry boxes
  surface-dark-elevated: "#11131a" # Nested elevated surfaces (rare)
  surface-light-paper: "#FCFDFD"  # Off-white paper canvas for articles
  surface-light-cream: "#F8F7F4"  # Spec cards, code blocks
  on-surface-dark: "#F9FAFB"      # Primary body on dark
  on-surface-dark-muted: "#D1D5DB" # Secondary text on dark
  on-surface-dark-faint: "#9CA3AF" # Eyebrow labels, meta on dark
  on-surface-light: "#202226"     # Body text on paper (warm dark, long-form)
  on-surface-light-heading: "#111318" # Headings, titles on paper
  on-surface-light-faint: "#5A5D67"   # Meta on paper
  series-evals: "#8121D8"         # AI Evals series accent (per-series override)
  series-agentic: "#0891B2"       # Agentic Stack series accent
  series-harness: "#E11D48"       # Harness Engineering series accent
typography:
  display:
    fontFamily: Instrument Serif
    fontSize: 4.5rem
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.02em
  display-italic:
    fontFamily: Instrument Serif
    fontSize: 4.5rem
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.02em
    fontFeature: "'ital' 1"
  h1:
    fontFamily: Inter
    fontSize: 4rem
    fontWeight: 900
    lineHeight: 0.95
    letterSpacing: -0.03em
  h2:
    fontFamily: Instrument Serif
    fontSize: 2.8rem
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.01em
  body-md:
    fontFamily: Newsreader
    fontSize: 1.2rem
    fontWeight: 400
    lineHeight: 1.7
  body-sm:
    fontFamily: Newsreader
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
  label-md:
    fontFamily: Inter
    fontSize: 0.85rem
    fontWeight: 600
    lineHeight: 1.4
  meta:
    fontFamily: JetBrains Mono
    fontSize: 0.75rem
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0.15em
  meta-sm:
    fontFamily: JetBrains Mono
    fontSize: 0.7rem
    fontWeight: 800
    lineHeight: 1.4
    letterSpacing: 0.15em
rounded:
  sm: 4px                  # neon highlight, pastel highlight, mistake card border-radius
  md: 12px                 # folder cards, blueprint diagram boxes
  lg: 16px                 # paper canvas inner cards
  xl: 20px                 # level badges (L1/L2/L3/L4)
  pill: 50px               # nav CTA pill
  card-recession: 40px     # signature 40px rounded-top recession glass cards
  full: 9999px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 32px
  xl: 64px
  hero-px: 6rem            # hero left/right padding via --px
  text-col-max: 660px      # 65–75 char optimal line
  content-max: 960px       # article content layout
components:
  card-glass-recession:
    backgroundColor: "{colors.surface-dark-base}"
    rounded: "{rounded.card-recession}"
    padding: 32px
  card-folder-frosted:
    backgroundColor: "{colors.surface-dark-card}"
    textColor: "{colors.on-surface-dark}"
    rounded: "{rounded.md}"
    padding: 32px
  card-folder-frosted-evals:
    backgroundColor: "{colors.surface-dark-card}"
    textColor: "{colors.on-surface-dark}"
    # 2px top border accent in {colors.primary} — purple gradient at 8% mixed into surface
  card-folder-frosted-harness:
    backgroundColor: "{colors.surface-dark-card}"
    textColor: "{colors.on-surface-dark}"
    # 2px top border accent in {colors.secondary} — rose gradient at 8% mixed into surface
  card-folder-frosted-tools:
    backgroundColor: "{colors.surface-dark-card}"
    textColor: "{colors.on-surface-dark}"
    # 2px top border accent in {colors.tertiary} — amber gradient at 8% mixed into surface
  callout-success:
    backgroundColor: "{colors.surface-light-paper}"
    textColor: "{colors.success}"
    rounded: "{rounded.sm}"
    padding: 12px
  callout-elevated:
    backgroundColor: "{colors.surface-dark-elevated}"
    textColor: "{colors.on-surface-dark-muted}"
    rounded: "{rounded.md}"
    padding: 24px
  meta-faint-dark:
    backgroundColor: "{colors.surface-dark-base}"
    textColor: "{colors.on-surface-dark-faint}"
    typography: "{typography.meta}"
  spec-card:
    backgroundColor: "{colors.surface-light-cream}"
    textColor: "{colors.on-surface-light-heading}"
    rounded: "{rounded.md}"
    padding: 24px
  meta-light:
    backgroundColor: "{colors.surface-light-paper}"
    textColor: "{colors.on-surface-light-faint}"
    typography: "{typography.meta}"
  badge-series-evals:
    backgroundColor: "{colors.surface-dark-card}"
    textColor: "{colors.series-evals}"
    typography: "{typography.label-md}"
    rounded: "{rounded.xl}"
  badge-series-agentic:
    backgroundColor: "{colors.surface-dark-card}"
    textColor: "{colors.series-agentic}"
    typography: "{typography.label-md}"
    rounded: "{rounded.xl}"
  badge-series-harness:
    backgroundColor: "{colors.surface-dark-card}"
    textColor: "{colors.series-harness}"
    typography: "{typography.label-md}"
    rounded: "{rounded.xl}"
  card-paper-canvas:
    backgroundColor: "{colors.surface-light-paper}"
    textColor: "{colors.on-surface-light}"
    rounded: "{rounded.card-recession}"
    padding: 96px
  button-primary:
    backgroundColor: "{colors.on-surface-dark}"
    textColor: "{colors.surface-dark-base}"
    typography: "{typography.meta-sm}"
    rounded: "{rounded.pill}"
    padding: 12px
  button-primary-hover:
    backgroundColor: "{colors.quaternary}"
    textColor: "{colors.surface-dark-base}"
  button-frosted:
    backgroundColor: "rgba(255, 255, 255, 0.15)"
    textColor: "{colors.on-surface-dark}"
    rounded: "{rounded.pill}"
    padding: 12px
  badge-level:
    backgroundColor: "{colors.surface-dark-card}"
    textColor: "{colors.quaternary}"
    typography: "{typography.label-md}"
    rounded: "{rounded.xl}"
    padding: 8px
    size: 80px
  highlight-neon:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-surface-dark}"
    rounded: "{rounded.sm}"
    # In CSS: rendered at 0.4 opacity over dark via gradient
  highlight-pastel:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-surface-light}"
    rounded: "{rounded.sm}"
    # In CSS: rendered at 0.12 opacity with mix-blend-mode multiply
  drop-cap-evals:
    backgroundColor: "{colors.surface-dark-base}"
    textColor: "{colors.primary}"
    typography: "{typography.display}"
  mistake-card:
    backgroundColor: "{colors.surface-light-paper}"
    textColor: "{colors.secondary}"
    rounded: "{rounded.sm}"
    padding: 16px
    # Red left border in {colors.secondary} — anti-pattern marker
  badge-l3-tools:
    backgroundColor: "{colors.surface-dark-card}"
    textColor: "{colors.tertiary}"
    typography: "{typography.label-md}"
    rounded: "{rounded.xl}"
    size: 80px
---
```

## Preserve the design intent when translating

- Brand and style: restrained editorial hierarchy with clear systems metadata; dark web/decks, light documents and approved paper reading surfaces.
- Colors: four meaningful identities, explicit functional states, stable current website series assignments, measured contrast.
- Typography: four roles; preserve code casing and use real available font weights. Avoid forcing every font onto every slide.
- Layout: the seed retains 4/8/16/32/64px spacing, 660px reading width and 960px content width. These are legacy values; the current website's mag-* tokens govern there.
- Elevation: glass/recession and paper are available template effects. Current editorial default cards use hairlines, reserving shadows for hover or floating surfaces.
- Shapes: the full 4/12/16/20/40/50/9999px legacy radius set remains. Square mobile dialogs or flat first cards can be legitimate exceptions.
- Components: retain glass and folder cards, buttons, level badges, highlights, callouts, metadata, spec card, paper canvas, drop cap and mistake card. Match semantic meaning and placement, not merely token names.
- Good practice: accurate content, available fonts, correct theme, accessible accents, measured final output, and a fitting authored signature. Avoid hype, arbitrary color reassignment, unreadable small text or unsupported fidelity claims.

Static tokens do not encode motion, scroll behavior, glass composition, full SVGs, responsive states, keyboard interaction, or print adaptation. Supply the relevant component guidance alongside the seed. The reference's `button-primary` is light fill with dark text; reversing that description does not describe its actual record.
