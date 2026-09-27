# Palette and contrast

Dark and light token groups retained from V8. Scope each theme to its surface; do not paste both :root declarations as if they represented one simultaneous theme. The current website uses #1A1C20 for mock body text; the cross-medium document treatment retains #202226. The legacy #8E93A0 light ink is suitable only where a low-contrast nonessential/disabled treatment is appropriate, not ordinary captions.

```css
:root {
    /* Backgrounds */
    --bg-base: #030407;        /* Landing / homepage / presentations */
    --bg-surface: #0a0b10;     /* Cards, folder cards, telemetry boxes */
    --bg-elevated: #11131a;    /* Nested elevated surfaces (rare) */
    /* Article hero variant: use #020305 (slightly darker for paper contrast) */

    /* Text hierarchy */
    --text-pure: #FFFFFF;      /* Display titles, hero emphasis */
    --text-main: #F9FAFB;      /* Primary body on dark */
    --text-muted: #D1D5DB;     /* Secondary text, editorial lead */
    --text-faint: #9CA3AF;     /* Eyebrow labels, meta */

    /* Borders */
    --border-dim: rgba(255, 255, 255, 0.1);
    --border-glow: rgba(255, 255, 255, 0.15);
    --border-bright: rgba(255, 255, 255, 0.25);  /* Frosted glass top edges */

    /* Selection */
    /* ::selection { background: rgba(6, 182, 212, 0.3); color: #FFF; } */
}
```

```css
:root {
    /* Paper */
    --bg-paper: #FCFDFD;        /* Microscopically off-white — eye comfort */
    --bg-cream: #F8F7F4;        /* Spec cards / code blocks only */
    --bg-faint: #F3F4F6;        /* Secondary bg, archive */

    /* 5-tier ink system */
    --ink-pure: #000000;
    --ink-main: #111318;        /* Headings, titles */
    --ink-body: #202226;        /* Body text — warm dark for long-form */
    --ink-faint: #5A5D67;       /* Meta */
    --ink-muted: #8E93A0;       /* Captions, timestamps */
}
```

## Recalculated solid-color ratios

Computed from sRGB relative luminance on September 13, 2026. Values do not include opacity, gradients, blending, projectors, or printing. Normal-text AA needs 4.5:1 and AAA 7:1; large-text thresholds are 3:1 and 4.5:1. A 14px label is not WCAG large text.

| Foreground | Background | Ratio |
|---|---|---:|
| `#FFFFFF` | `#030407` | 20.50:1 |
| `#F9FAFB` | `#030407` | 19.62:1 |
| `#D1D5DB` | `#030407` | 13.91:1 |
| `#9CA3AF` | `#030407` | 8.08:1 |
| `#9D4EDD` | `#030407` | 4.46:1 |
| `#F43F5E` | `#030407` | 5.58:1 |
| `#F59E0B` | `#030407` | 9.55:1 |
| `#06B6D4` | `#030407` | 8.44:1 |
| `#000000` | `#FCFDFD` | 20.61:1 |
| `#111318` | `#FCFDFD` | 18.23:1 |
| `#202226` | `#FCFDFD` | 15.63:1 |
| `#1A1C20` | `#FCFDFD` | 16.74:1 |
| `#5A5D67` | `#FCFDFD` | 6.45:1 |
| `#8E93A0` | `#FCFDFD` | 3.02:1 |
| `#F43F5E` | `#FCFDFD` | 3.60:1 |
| `#10B981` | `#FCFDFD` | 2.49:1 |
| `#8121D8` | `#0A0B10` | 2.94:1 |
| `#0891B2` | `#0A0B10` | 5.34:1 |
| `#E11D48` | `#0A0B10` | 4.19:1 |

For a projected deck, prefer brighter secondary text and verify at the actual viewing distance; an on-screen ratio does not establish projection readability. Status rings and series colors need labels or other distinguishable cues.

Primary accessibility references: [WCAG 2.2](https://www.w3.org/TR/WCAG22/) and [Pause, Stop, Hide](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html). CSS perspective can be shared by a parent property or applied through a transform function; see [MDN perspective](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/perspective).
