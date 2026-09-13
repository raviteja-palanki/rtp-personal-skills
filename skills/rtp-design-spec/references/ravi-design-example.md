# Ravi design migration example

Reference revision 1.0.1, reviewed 13 September 2026.

This is the earlier skill’s illustration, preserved for migration comparison. Its values and comments are historical examples, not confirmation of the current website’s approved palette or component implementation. In particular, conceptual Model/Harness/Tools/Environment colors must not silently replace a page or series accent mapping. Read the current personal-branding skill and the project’s design-language documents first.

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

Before applying this example, check the four loaded font families and weights, the compact H1 line height, metadata size, the actual light and dark surfaces, and component contrast. Convert the button’s literal white to an explicit semantic token if that is the approved foreground role. The `card-recession` radius alone does not describe top-only rounding, blur, borders, layering, or scrolling behavior; those require the implementation guidance. A color palette called “Aureate Purple” here is a legacy label, not evidence that it shares AI-Fluent’s gold palette.

The current personal-branding guidance also covers the learn site; do not reactivate the archived `rtp-learn-site-design` skill. The prior source cited upstream examples named `paws-and-paths`, `atmospheric-glass`, and `totality-festival`; browse the current upstream examples directory before relying on those paths.
