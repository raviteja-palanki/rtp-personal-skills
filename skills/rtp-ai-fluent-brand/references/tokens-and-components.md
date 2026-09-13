# AI Fluent tokens and component recipes

Companion revision 1.0.1, 13 Sep 2026. These are program identity defaults. Check the active project and medium before applying them. Original color hex values remain the source of truth; HSL values below are recalculated equivalents rather than the inconsistent values in the earlier skill.

## Palette

| Token | Hex | Approximate HSL | Role |
|---|---|---|---|
| `--gold` | `#D4AF37` | 45.86 64.61% 52.35% | Main dark-theme accent |
| `--gold-light` | `#E6C77A` | 42.78 68.35% 69.02% | Highlight |
| `--gold-dark` | `#B89A2E` | 46.96 60% 45.10% | Darker accent |
| `--gold-deep` | `#8A6B1F` | 42.62 63.31% 33.14% | Deep accent |
| `--gold-glow` | `#E5C04D` | | Glow color |
| `--teal` / `--teal-bright` | `#50C9B0` / `#6FDFC9` | | Secondary technology or interaction accents |
| `--purple` / `--purple-bright` | `#8B6EC4` / `#A890D9` | | Secondary accents, including multi-agent topics where the project uses that mapping |
| `--status-success` | `#4CAF50` | | Success, with a text or icon label |
| `--status-danger` | `#EF5350` | | Error or danger, with a text or icon label |
| `--status-warning` | `#FFA726` | | Warning, with a text or icon label |

Do not assume a secondary or status color is suitable for small text on every surface. A series may have its own semantic accent lock.

| Dark token | Value | Use |
|---|---|---|
| `--void` | `#0A0A0A` | Deep background |
| `--codex` | `#121212` | Section background |
| `--dusk` | `#1A1A1A` | Card background |
| `--charcoal-deep` | `#151515` | Alternate surface |
| `--foreground` / `--text-parchment` | `#F5F0E6` | Main text |
| `--text-ivory` | `#DDD8CC` | Body text |
| `--text-stone` | `#A9A49A` | Secondary readable text |
| `--text-dust` | `#6E6A62` | Nonessential decoration or inactive elements |

| Parchment token | Value | Use |
|---|---|---|
| `--bg-champagne` | `#FAF7F2` | Main background |
| `--bg-parchment` | `#F5EFE3` | Card or section |
| `--bg-linen` | `#EDE7D9` | Alternate surface |
| `--bg-cream` | `#FEFDFB` | Elevated or input surface |
| `--text-ink` | `#1A1715` | Main text |
| `--text-charcoal` | `#3D3733` | Body text |
| `--text-walnut` | `#6B6259` | Secondary readable text |
| `--text-sand` | `#A39B90` | Nonessential decoration or inactive elements |
| `--gold-on-light` | `#B89A2E` | Decorative accent or button fill, not ordinary text |
| `--gold-on-light-hover` | `#9A7F1E` | Darker accent; check text use |
| `--gold-on-light-subtle` | `rgba(184,154,46,.12)` | Tint |

## Typography and spacing

| Role | Font | Original web size | Weight | Line height |
|---|---|---|---|---|
| Display | Cormorant Garamond | `clamp(52px, 10vw, 110px)` | 300 | .95 |
| H1 | Cormorant Garamond | `clamp(36px, 5vw, 60px)` | 400 | 1.1 |
| H2 | Cormorant Garamond | `clamp(28px, 3.5vw, 44px)` | 500 | 1.15 |
| H3 | Cormorant Garamond | `clamp(22px, 2.5vw, 32px)` | 500 | 1.25 |
| Body | Inter | `clamp(16px, 1.1vw, 18px)` | 400 | 1.75 |
| Label | Inter | 12px | 600 | Set explicitly for legibility; 1.5 is a starting point |
| Data or code | JetBrains Mono | 14–16px | 500 | 1.5 |

Retain these as starting recipes. Fixed pixel values in fluid type still need testing under text resizing, wrapping, and zoom; use an appropriate rem-based implementation when the host design requires it. Tight display leading can need adjustment for several lines or particular glyphs.

| Token | Value | Intended role |
|---|---|---|
| `--space-4` | 16px | Element spacing |
| `--space-6` | 24px | Typical gap or narrow-screen padding |
| `--space-8` | 32px | Spacious card padding |
| `--space-16` | 64px | Desktop horizontal padding |
| `--space-20` | 80px | Mobile vertical section spacing |
| `--space-36` | 140px | Legacy desktop vertical section spacing; an optical exception |
| `--content-narrow` | 520px | Focused column |
| `--content-default` | 640px | Standard content |
| `--content-wide` | 720px | Wider content with visuals |
| `--content-max` | 920px | Broad sections |

Container values are maxima, not fixed widths on a small screen. The original card recipes use 24px padding; choose 24 or 32 consistently with the desired density.

## Core CSS tokens

```css
:root {
  --void: #0A0A0A;
  --codex: #121212;
  --dusk: #1A1A1A;
  --charcoal-deep: #151515;
  --foreground: #F5F0E6;
  --text-parchment: #F5F0E6;
  --text-ivory: #DDD8CC;
  --text-stone: #A9A49A;
  --text-dust: #6E6A62;
  --gold: #D4AF37;
  --gold-light: #E6C77A;
  --gold-dark: #B89A2E;
  --gold-deep: #8A6B1F;
  --gold-glow: #E5C04D;
  --teal: #50C9B0;
  --teal-bright: #6FDFC9;
  --purple: #8B6EC4;
  --purple-bright: #A890D9;
  --status-success: #4CAF50;
  --status-danger: #EF5350;
  --status-warning: #FFA726;

  --bg-champagne: #FAF7F2;
  --bg-parchment: #F5EFE3;
  --bg-linen: #EDE7D9;
  --bg-cream: #FEFDFB;
  --text-ink: #1A1715;
  --text-charcoal: #3D3733;
  --text-walnut: #6B6259;
  --text-sand: #A39B90;
  --gold-on-light: #B89A2E;
  --gold-on-light-hover: #9A7F1E;
  --gold-on-light-subtle: rgba(184,154,46,.12);

  --font-display: "Cormorant Garamond", Georgia, serif;
  --font-body: "Inter", -apple-system, sans-serif;
  --font-mono: "JetBrains Mono", Consolas, monospace;
  --space-4: 16px;
  --space-6: 24px;
  --space-8: 32px;
  --space-16: 64px;
  --space-20: 80px;
  --space-36: 140px;
  --content-narrow: 520px;
  --content-default: 640px;
  --content-wide: 720px;
  --content-max: 920px;

  --ease: cubic-bezier(.16,1,.3,1);
  --ease-out: cubic-bezier(.33,1,.68,1);
  --ease-spring: cubic-bezier(.34,1.56,.64,1);
  --duration-fast: 150ms;
  --duration-normal: 300ms;
  --duration-slow: 500ms;
  --glow-gold-subtle: 0 0 15px rgba(212,175,55,.15), 0 0 30px rgba(212,175,55,.08);
  --glow-gold-medium: 0 0 20px rgba(212,175,55,.25), 0 0 40px rgba(212,175,55,.15);
  --glow-gold-intense: 0 0 20px rgba(212,175,55,.35), 0 0 40px rgba(212,175,55,.25), 0 0 60px rgba(212,175,55,.15);
  --glow-gold-text: 0 0 10px rgba(212,175,55,.30), 0 0 20px rgba(212,175,55,.20);

  --button-ink: #1A1715;
  --accent-text: #D4AF37;
  --focus-color: #E6C77A;
  --label-color: #6FDFC9;
}

[data-theme="light"] {
  --void: #FAF7F2;
  --codex: #F5EFE3;
  --dusk: #EDE7D9;
  --charcoal-deep: #FEFDFB;
  --foreground: #1A1715;
  --text-ivory: #3D3733;
  --text-stone: #6B6259;
  --text-dust: #A39B90;
  --gold: #B89A2E;
  --gold-light: #D4AF37;
  --gold-dark: #9A7F1E;
  --gold-deep: #7A6518;
  --accent-text: #7A6518;
  --focus-color: #7A6518;
  --label-color: #1A1715;
}
```

The semantic additions keep button ink stable across themes and give light-theme links, focus, and labels suitable starting colors. Theme overrides preserve original values; test components wherever backgrounds differ from the examples below.

## Component recipes

```css
.btn-premium-gold,
.btn-gold-light {
  background: linear-gradient(135deg, #B89A2E, #D4AF37, #E6C77A);
  color: var(--button-ink);
  padding: 12px 24px;
  min-height: 44px;
  min-width: 44px;
  border-radius: 8px;
  font-weight: 600;
  box-shadow: 0 0 20px rgba(212,175,55,.25);
}
.btn-gold-light {
  background: linear-gradient(135deg, #B89A2E, #D4AF37);
  box-shadow: 0 2px 8px rgba(184,154,46,.2);
}
.btn-premium-outline {
  background: transparent;
  border: 1px solid var(--accent-text);
  color: var(--accent-text);
  padding: 12px 24px;
  min-height: 44px;
  min-width: 44px;
  border-radius: 8px;
}
.card-premium {
  background: var(--dusk);
  border-radius: 12px;
  padding: 24px;
  box-shadow:
    inset 0 0 .5px 1px rgba(255,255,255,.075),
    0 0 0 1px rgba(0,0,0,.05),
    0 3.5px 6px rgba(0,0,0,.09);
}
.card-parchment {
  background: #F5EFE3;
  color: #3D3733;
  border-radius: 12px;
  padding: 24px;
  box-shadow: 0 1px 3px rgba(26,23,21,.06), 0 4px 12px rgba(26,23,21,.04);
}
.takeaway,
.takeaway-light {
  border-left: 3px solid var(--gold);
  background: linear-gradient(90deg, rgba(212,175,55,.08), transparent);
  padding: 16px 24px;
  border-radius: 0 8px 8px 0;
}
.takeaway-light {
  border-left-color: #B89A2E;
  background: linear-gradient(90deg, rgba(184,154,46,.08), transparent);
}
.label {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(80,201,176,.15);
  color: var(--label-color);
  padding: 4px 12px;
  border-radius: 9999px;
  font-size: 12px;
  line-height: 1.5;
  font-weight: 600;
  text-transform: uppercase;
}
.label::before {
  content: "";
  width: 6px;
  height: 6px;
  flex: 0 0 6px;
  background: currentColor;
  border-radius: 50%;
}
:focus-visible {
  outline: 2px solid var(--focus-color);
  outline-offset: 3px;
}
```

Apply button classes to real buttons or links with correct semantics, not a clickable unlabelled container. Check hover, active, disabled, focus, wrapping, and keyboard behavior in the host implementation. The original outline's half-opacity gold is strengthened here so the boundary is not needlessly faint.

Labels are static by default. The original indefinite pulse had no supplied keyframes and conflicted with the purpose-only motion rule. If a state change needs attention, use a brief, finite effect that preserves the label and has a reduced-motion alternative. A style recipe cannot supply application behavior by itself.

## Motion, media, and scrolling

Use the timing and easing tokens as a vocabulary. The spring curve is available for appropriate physical movement, not a requirement for every component. A known percentage of continuous progress can use linear timing. Keep meaning available without an animation or hover effect.

For nonessential effects created with this program layer, scope reduced-motion handling to their actual classes. For example:

```css
@media (prefers-reduced-motion: reduce) {
  .ai-fluent-motion {
    animation: none;
    transition: none;
    transform: none;
    opacity: 1;
  }
  .ai-fluent-scroll {
    scroll-behavior: auto;
  }
}
```

Apply these classes deliberately. Also check JavaScript-driven motion and any essential transforms before disabling them. Keep parallax optional, ordinary scrolling available, and text accessible without waiting for a reveal. Do not use motion as the sole status signal.

Use images with an intentional crop and meaningful alternative text when they convey information. Keep captions readable, screenshots large enough to interpret, and charts labeled with units and sources. A gallery needs keyboard-accessible controls when interactive. These principles replace missing reference pointers; they are not claims that a complete gallery or chart library is bundled here.

## Contrast calculations and corrections

Calculated September 13 using WCAG relative luminance for opaque sRGB pairs. Values are rounded for display; assess pass/fail using full precision. Actual gradients, transparency, image backgrounds, and UI states need separate checking.

| Text | On `#0A0A0A` | On `#1A1A1A` |
|---|---:|---:|
| Parchment `#F5F0E6` | 17.43:1 | 15.32:1 |
| Ivory `#DDD8CC` | 13.92:1 | 12.24:1 |
| Stone `#A9A49A` | 7.98:1 | 7.01:1 |
| Dust `#6E6A62` | 3.68:1 | 3.23:1 |
| Gold `#D4AF37` | 9.42:1 | 8.28:1 |

| Text | On champagne `#FAF7F2` |
|---|---:|
| Ink `#1A1715` | 16.69:1 |
| Charcoal `#3D3733` | 10.96:1 |
| Walnut `#6B6259` | 5.59:1 |
| Sand `#A39B90` | 2.57:1 |
| Gold-on-light `#B89A2E` | 2.55:1 |
| Hover gold `#9A7F1E` | 3.62:1 |
| Deep light-theme gold `#7A6518` | 5.31:1 |

White-cream text `#FEFDFB` on the old gold button endpoints yields only about 2.68:1 and 2.07:1. Ink `#1A1715` yields about 6.54:1 and 8.48:1 against those same endpoints. The updated button fixes the ordinary-text contrast problem; it does not establish all-state or whole-product accessibility.

Use stone for a small dark-theme attribution and walnut or darker text on parchment. A visible footer containing useful attribution is not a watermark merely because it is small. Recheck print exports and projected slides rather than assuming the web contrast calculation proves their readability.
