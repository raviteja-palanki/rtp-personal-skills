---
name: ravi-personal-branding
version: 1.0
description: Complete design language for ravitejapalanki.com — dark cinematic landing (homepage, profile, writing hub) plus light editorial article pages. Covers both dark and light themes with full component catalog, animation system, and page recipes. Canonical source for every visual decision across the site ecosystem.
author: Ravi Teja Palanki
created: 17 April 2026
supersedes: learn-site-design (v2.0)
---

# Ravi Personal Branding

The single source of truth for every visual decision across **ravitejapalanki.com** — homepage, profile, writing hub, series pages, and article reading experiences.

**When to activate:** Any task that touches the personal website's visual layer — building new pages, refining existing ones, creating diagrams, writing skill-adjacent HTML, or answering "what's the right way to do X on Ravi's site?"

**Canonical reference files:**
- Homepage: `1_Projects/my-personal-website/prototype/homepage-final.html`
- Article page: `1_Projects/my-personal-website/reference/BLOG-POST-TEMPLATE.html`
- Production landing (writing section): `1_Projects/my-personal-website/reference/production-landing.html`

**Site architecture:**
```
ravitejapalanki.com/                                → Homepage (the gateway)
ravitejapalanki.com/profile                         → Digital resume
ravitejapalanki.com/writing                         → Writing hub landing
ravitejapalanki.com/writing/evals                   → AI Evals series hub
ravitejapalanki.com/writing/evals/:slug             → Eval article
ravitejapalanki.com/writing/agentic-stack           → Agentic Stack series hub
ravitejapalanki.com/writing/agentic-stack/:slug     → Agentic article
ravitejapalanki.com/writing/harness-engineering     → Harness Engineering series hub
ravitejapalanki.com/writing/harness-engineering/:slug → Harness episode
```

---

## 1. The Identity System — 4 Colors

Each color carries meaning from the AI production architecture framework. They are never decorative. They are never flat background fills.

| Role | Hex | CSS var | Where it appears |
|------|-----|---------|------------------|
| **Model** (intelligence) | `#9D4EDD` landing / `#8121D8` article | `--color-model` | Level badges, article callouts, drop caps, progress bars, series accent for AI Evals |
| **Harness** (guardrails, warnings) | `#F43F5E` landing / `#E11D48` article | `--color-harness` | Anti-pattern cards, mistake borders, severity badges, series accent for Harness Engineering |
| **Tools** (capabilities) | `#F59E0B` | `--color-tools` | Amber accents, L3 badges, engineering-domain cards |
| **Environment** (context, hero) | `#06B6D4` landing / `#00E5FF` article | `--color-env` | Editorial cyan line, "CHASM" stroke, highlight text, meta-row dots |

**Functional colors:**
- Success: `#059669` / `#10B981` (emerald) — pass states, expected-behavior boxes
- Info callout: `#EFF6FF` bg, `#1E3A8A` text, `#3B82F6` accent

**Color rules — never break:**
- Colors appear only as accents: borders, glows, text highlights, tiny fills. Never as flat backgrounds.
- Red is EXCLUSIVELY anti-patterns, mistakes, warnings. Never positive.
- On dark: border accents, text-shadow glows, radial-gradient overlays at 4-15% opacity.
- On white: border-left accents, tinted backgrounds at 4-12% opacity, text color.

---

## 2. Per-Series Accent Overrides (Article Pages)

Each deep dive series takes over `--color-model` and `--color-model-light` to tint every article in its own accent without changing structure.

| Series | `--color-model` | `--color-model-light` | Drop-cap gradient end |
|--------|-----------------|-----------------------|----------------------|
| AI Evals | `#8121D8` (deep purple) | `rgba(129, 33, 216, 0.12)` | `#C084FC` |
| Agentic Stack | `#0891B2` (deep cyan) | `rgba(8, 145, 178, 0.12)` | `#67E8F9` |
| Harness Engineering | `#E11D48` (rose-red) | `rgba(225, 29, 72, 0.12)` | `#FB7185` |

Also swap the **rocket exhaust gradient** color per series:
- Default (evals): `rgba(129, 33, 216, 0.8)`
- Agentic: `rgba(8, 145, 178, 0.8)`
- Harness: `rgba(225, 29, 72, 0.8)`

---

## 3. Typography — 4 Fonts

| Font | CSS var | Role | Weights |
|------|---------|------|---------|
| **Inter** | `--font-sans` | Display titles (900), UI labels, eyebrows | 300, 400, 500, 600, 700, 800, 900 |
| **Instrument Serif** | `--font-display` | Editorial moments, hero titles, article H2s, quotes, drop caps, signatures, nav brand on article pages | 400, 400 italic |
| **Newsreader** | `--font-body` | Long-form body, editorial paragraphs, descriptions on dark sections | 200-800 variable, optical size 6-72 |
| **JetBrains Mono** | `--font-mono` | Labels, tags, badges, topic pills, code, meta | 400, 500, 700, 800 |

**Typography rules — never break:**
- Inter 900 ONLY for display titles (uppercase, `letter-spacing: -0.03em`, `line-height: 0.95`).
- Instrument Serif NEVER for body text. Only for: hero titles, article section H2s, massive quotes, drop caps, card titles, signatures, nav brand on article pages.
- Newsreader ONLY for body prose. Never for labels, UI, or titles.
- JetBrains Mono for ALL labels, tags, and metadata. Font-weight 700-800, uppercase, `letter-spacing: 0.15em`.
- On dark backgrounds: minimum font-weight 400. Inter 300 washes out.

---

## 4. DARK THEME (Landing / Homepage / Profile / Writing Hub / Series Pages / Article Heroes)

### CSS Variables
```css
:root {
    /* Backgrounds */
    --bg-base: #030407;        /* Landing pages, section base */
    --bg-surface: #0a0b10;     /* Card surfaces, folder cards */
    --bg-elevated: #11131a;    /* Nested elevated surfaces */

    /* Article hero-specific (darker for contrast against paper canvas) */
    /* Use --bg-base: #020305 on article pages */

    /* Text hierarchy */
    --text-pure: #FFFFFF;      /* Display titles, hero text */
    --text-main: #F9FAFB;      /* Primary body on dark */
    --text-muted: #D1D5DB;     /* Secondary text, editorial lead, card body */
    --text-faint: #9CA3AF;     /* Eyebrow labels, meta text */

    /* Borders */
    --border-dim: rgba(255, 255, 255, 0.1);
    --border-glow: rgba(255, 255, 255, 0.15);
}
```

### Ambient Layers (Fixed Across Every Dark Page)

**Noise overlay** (z-index 9999):
```css
.noise-overlay {
    position: fixed; inset: 0;
    background: url("data:image/svg+xml,...fractalNoise baseFrequency=0.8 numOctaves=4...");
    opacity: 0.04-0.05;
    mix-blend-mode: multiply;  /* or overlay on article pages */
    pointer-events: none;
}
```
On article pages, add: `animation: noiseShift 8s steps(10) infinite`.

**Dynamic ambient glow** (landing pages only, z-index 0):
```css
.glow-bg {
    position: fixed; inset: 0; pointer-events: none;
    background:
        radial-gradient(circle at 80% 0%, rgba(157, 78, 221, 0.06) 0%, transparent 50%),
        radial-gradient(circle at 20% 100%, rgba(6, 182, 212, 0.04) 0%, transparent 50%);
    transition: background 0.5s ease;
}
```
JS on mousemove (desktop only) repositions both gradients to follow the cursor — purple tracks `(x%, y%)`, cyan tracks `(100-x%, 100-y%)`.

### Readability Verification (Dark Mode)
| Combination | Ratio |
|-------------|-------|
| `#FFFFFF` on `#030407` | 20.3:1 |
| `#F9FAFB` on `#030407` | 19.6:1 |
| `#D1D5DB` on `#030407` | 14.8:1 |
| `#9CA3AF` on `#030407` | 8.9:1 |

All pass WCAG AAA.

---

## 5. LIGHT THEME (Article Reading — Paper Canvas Overlay)

### CSS Variables
```css
:root {
    /* Paper backgrounds */
    --bg-paper: #FCFDFD;        /* Primary paper — microscopically off-white for eye comfort */
    --bg-cream: #F8F7F4;        /* Spec cards only — intentional warm cream */
    --bg-faint: #F3F4F6;        /* Secondary bg, archive */

    /* 5-tier tactile ink system (richer than 4-tier landing grays) */
    --ink-pure: #000000;
    --ink-main: #111318;        /* Headings, titles */
    --ink-body: #202226;        /* Body text — rich warm dark for long-form reading */
    --ink-faint: #5A5D67;
    --ink-muted: #8E93A0;
}
```

### Paper Canvas (the signature overlay)
```css
.paper-canvas {
    position: relative; z-index: 20;
    background: var(--bg-paper);
    margin-top: -12vh;                    /* Overlaps dark hero by 12% of viewport */
    border-radius: 40px 40px 0 0;         /* Rounded top corners only */
    padding: 6rem var(--px) 8rem;
    /* Hyper-realistic edge: heavy drop shadow + inset highlights */
    box-shadow:
        0 -40px 100px rgba(0,0,0,0.8),
        inset 0 1px 1px rgba(255,255,255,1),
        inset 0 2px 4px rgba(255,255,255,0.5);
    /* Microscopic dot grid — working notebook texture */
    background-image: radial-gradient(rgba(0,0,0,0.03) 1px, transparent 1px);
    background-size: 32px 32px;
    background-position: center top;
}
```

### Reading Layout
- `.text-col` — `max-width: 660px` (optimal 65-75 character reading line)
- `.bleed-wide` — `width: 100%`, `margin: 6rem 0` (diagrams, cards, specs break out)
- Parent `.content-layout` — `max-width: 960px`, `margin: 0 auto`, `align-items: center`

### Readability Verification (Light Mode)
| Combination | Ratio |
|-------------|-------|
| `#000000` on `#FCFDFD` | 20.9:1 |
| `#111318` on `#FCFDFD` | 18.2:1 |
| `#202226` on `#FCFDFD` | 14.5:1 |
| `#5A5D67` on `#FCFDFD` | 6.5:1 |

All pass WCAG AA; top three pass AAA.

---

## 6. Component Catalog

### 6.1 Nav (Two Variants)

**Homepage / Profile / Writing Hub variant** — left brand + right links + CTA:
```css
nav {
    position: fixed; top: 0; left: 0; right: 0;
    padding: 1.5rem var(--px);  /* tightens to 1rem on scroll > 50px */
    display: flex; justify-content: space-between; align-items: center;
    z-index: 1000;
    backdrop-filter: blur(12px);
    background: linear-gradient(to bottom, rgba(3,4,7,0.9), rgba(3,4,7,0));
    border-bottom: 1px solid rgba(255,255,255,0.06);
    transition: padding 0.4s var(--ease-cinematic), background 0.4s var(--ease-cinematic);
}
.nav-brand {
    font-family: var(--font-sans); font-weight: 800;
    font-size: 1.2rem; letter-spacing: -0.02em;
    color: var(--text-pure);
}
.nav-link {
    font-family: var(--font-sans); font-weight: 600; font-size: 0.85rem;
    color: var(--text-main);
    padding-bottom: 4px; position: relative;
}
/* Animated underline on hover — origin flips from right to left */
.nav-link::after {
    content: ''; position: absolute; bottom: 0; left: 0;
    width: 100%; height: 2px; background: var(--text-pure);
    transform: scaleX(0); transform-origin: right;
    transition: transform 0.4s var(--ease-cinematic);
}
.nav-link:hover::after { transform: scaleX(1); transform-origin: left; }
.nav-cta {
    font-family: var(--font-mono); font-weight: 700; font-size: 0.72rem;
    text-transform: uppercase; letter-spacing: 0.08em;
    color: var(--bg-base); background: var(--text-pure);
    padding: 0.6rem 1.4rem; border-radius: 50px;
    transition: all 0.4s var(--ease-spring);
}
.nav-cta:hover { transform: translateY(-2px); box-shadow: 0 5px 20px rgba(255,255,255,0.2); }
```

**Article page variant** — left brand (Newsreader italic) + right single CTA (frosted glass):
```css
nav {
    position: fixed; top: 0; left: 0; right: 0;
    padding: 1.5rem var(--px);
    background: linear-gradient(to bottom, rgba(2,3,5,0.95) 0%, transparent 100%);
    /* NO backdrop-blur, NO border-bottom — relies on gradient fade */
    z-index: 1000;
}
.nav-brand {
    font-family: var(--font-body);  /* Newsreader */
    font-style: italic;
    font-size: 1.4rem;              /* Larger, softer than homepage */
    font-weight: 500;
    letter-spacing: -0.01em;
    color: #FFFFFF;
}
.nav-cta {
    /* Frosted glass variant — becomes opaque white on hover */
    font-family: var(--font-sans); font-weight: 700; font-size: 0.75rem;
    text-transform: uppercase; letter-spacing: 0.05em;
    color: #FFFFFF !important;
    background: rgba(255, 255, 255, 0.15);
    border: 1px solid rgba(255, 255, 255, 0.4);
    backdrop-filter: blur(12px);
    padding: 0.5rem 1.4rem; border-radius: 50px;
}
.nav-cta:hover {
    transform: translateY(-2px);
    background: #FFFFFF; color: #000000 !important;
    border-color: #FFFFFF;
    box-shadow: 0 4px 20px rgba(255,255,255,0.4);
}
```

### 6.2 Rocket Engine Progress Bar (Article Pages)

The signature reading-progress indicator. Replaces the old simple comet.

```css
.progress-bar-container {
    position: fixed; top: 12px; left: 12px; right: 12px; height: 3px;
    background: rgba(255, 255, 255, 0.08);
    z-index: 10005; border-radius: 4px;
}
/* On mobile (<1024px): full-width, top 0, no border-radius, 4px height */

.progress-bar {
    height: 100%;
    background: linear-gradient(90deg, transparent, #F59E0B, var(--color-model));
    width: 0%;
    transition: width 0.1s linear;
    border-radius: 4px;
    box-shadow: 0 0 10px var(--color-model-light);
}

.rocket-assembly {
    position: absolute; right: -8px; top: 50%;
    transform: translate(50%, -50%) rotate(0deg);
    display: flex; align-items: center;
    transition: transform 0.4s var(--ease-spring);
}
/* Flips 180deg on scroll reverse (JS-driven) */

.rocket-exhaust {
    width: 40px; height: 2px;
    background: linear-gradient(90deg, transparent, rgba(129, 33, 216, 0.8), #FFF);
    margin-right: -4px;
    border-radius: 4px 0 0 4px;
}
.rocket-exhaust::after {
    content: ''; position: absolute; right: 0; top: 50%;
    width: 10px; height: 6px; background: #FFFFFF; border-radius: 50%;
    filter: drop-shadow(0 0 6px var(--color-model)) blur(1px);
    animation: enginePulse 0.4s ease-in-out infinite alternate;
    transform: translateY(-50%);
}
@keyframes enginePulse {
    0% { opacity: 0.6; transform: translateY(-50%) scale(0.8); }
    100% { opacity: 1; transform: translateY(-50%) scale(1.3); }
}
.rocket-icon {
    width: 18px; height: 18px; color: #FFFFFF;
    filter: drop-shadow(0 0 4px rgba(255,255,255,0.6));
    transform: rotate(45deg);  /* Dart-point angle */
}
```

**SVG used:**
```html
<svg class="rocket-icon" viewBox="0 0 24 24" fill="currentColor">
    <path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"/>
</svg>
```

### 6.3 Topic Pill (Frosted Glass)
```css
.topic-pill {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.15);
    color: #FFFFFF;
    padding: 0.7rem 2.2rem; border-radius: 999px;
    font-family: var(--font-mono); font-size: 0.75rem; font-weight: 700;
    text-transform: uppercase; letter-spacing: 0.2em;
    backdrop-filter: blur(12px);
    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
}
```

### 6.4 Hero Meta Row (Dark Pill with Cyan Dot)
```css
.meta-row {
    display: inline-flex; gap: 1.5rem; align-items: center;
    font-family: var(--font-mono); font-size: 0.85rem; font-weight: 700;
    color: #FFFFFF;
    text-transform: uppercase; letter-spacing: 0.15em;
    background: rgba(0, 0, 0, 0.85);
    padding: 0.8rem 2rem; border-radius: 50px;
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255,255,255,0.2);
    box-shadow: 0 10px 40px rgba(0,0,0,0.8);
}
.meta-row .dot {
    color: var(--color-env); font-weight: 900; font-size: 1.2rem; line-height: 0;
}
```

### 6.5 Credential Badges (Homepage Hero)
```css
.badge {
    font-family: var(--font-mono); font-weight: 700; font-size: 0.65rem;
    text-transform: uppercase; letter-spacing: 0.08em;
    padding: 0.5rem 0.8rem; border-radius: 50px;
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.1);
    backdrop-filter: blur(10px);
    color: var(--text-pure);
    display: flex; align-items: center; gap: 0.4rem;
}
.badge-dot {
    width: 6px; height: 6px; border-radius: 50%; background: currentColor;
    box-shadow: 0 0 10px currentColor;
}
.badge-cyan .badge-dot { color: var(--color-env); }
.badge-purple .badge-dot { color: var(--color-model); }
.badge-amber .badge-dot { color: var(--color-tools); }
```

### 6.6 3D Isometric Stack (Homepage + Writing Landing)
```
Container: perspective 1200px, 600px height
.iso-plane: rotateX(60deg) rotateZ(-45deg), 320x240px, transform-style: preserve-3d
Layers (Z-axis):
  Top    → translateZ(120px), cyan border+glow
  Upper  → translateZ(40px), red border+glow (writing site) / purple (homepage)
  Lower  → translateZ(-40px), amber border+glow
  Bottom → translateZ(-120px), purple (writing site) / red (homepage)
Core beam: 3px vertical gradient, cyan glow, through center
Each layer: 1px border in identity color (0.6 opacity), inset box-shadow glow,
            CSS grid overlay (20x20px, 10% opacity, currentColor)
Center text: Inter 900, 65-80px, white, triple cyan text-shadow
```

Mouse parallax (desktop >1024px): adjusts rotateX/Z by ±0.05-0.15deg per pixel offset. Spring ease 1.5s on mouseleave.

### 6.7 Sticky Card Stack (with 3D Tilt)
```
Each card: position: sticky, height 75vh, 24px border-radius
Box-shadow: 0 -40px 80px rgba(3,4,7,0.95)  /* creates stacking depth */
transform-style: preserve-3d

Sticky offsets (desktop):
  Card 1: top 100px    /* mobile: 90px */
  Card 2: top 160px    /* mobile: 150px */
  Card 3: top 220px    /* mobile: 210px */
  Card 4: top 280px    /* mobile: 270px */

Titles: Inter 800 (homepage) or Instrument Serif 400 (writing site)
Body: Newsreader 400, var(--text-muted)

Folder tab (top-right): JetBrains Mono 800, identity color, 8px glowing dot
```

3D tilt interaction (desktop only, on mousemove):
```js
rotateX = ((y - centerY) / centerY) * -2
rotateY = ((x - centerX) / centerX) * 2
card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.02, 1.02, 1.02)`
// Children lift: translateZ(30px)
```
Spring-ease snap-back on mouseleave (0.5s `--ease-spring`).

### 6.8 Deep Dive Hero with Recession Stacking (Homepage + Writing)
```
Each section: position: sticky, top: 0, height: 100vh
Increasing z-index per section (31, 32, 33, 34)
Background image: inset -50px, grayscale 100%, contrast 120%, opacity 0.25, mix-blend-mode luminosity
Gradient overlay: radial from identity color (15% opacity) to base
```

Recession animation (scroll-driven, `requestAnimationFrame`):
```js
// When current section is pinned (rect.top <= 0) and next is entering:
progress = 1 - (Math.max(0, nextRect.top) / window.innerHeight)
scale = 1 - (progress * 0.08)
y = progress * 40
opacity = 1 - (progress * 0.8)
bgScale = 1.05 - (progress * 0.05)
bgBrightness = 1 - progress
```

### 6.9 SVG Stat Ring (Homepage Proof Points)
```
Container: clamp(100px, 30vw, 140px) square
SVG circles: r=45, stroke-width 4
.bg: stroke rgba(255,255,255,0.05)
.progress: stroke-dasharray 283; stroke-dashoffset 283 → 0 on reveal
  Transition: 2s var(--ease-cinematic)
Color variants: .color-cyan/purple/amber/red with matching drop-shadow filter (8px glow)
Stat value centered: JetBrains Mono 800, clamp(1.8-2.5rem)
```

JS counter: increments 0 → target over 40 frames at 30ms intervals, triggered by IntersectionObserver at 50% threshold.

### 6.10 Learning Objectives Block
```css
.learning-block {
    background: #FFFFFF;
    border: 1px solid #E5E7EB;
    border-radius: 20px;
    padding: 5rem;
    box-shadow: 0 30px 60px rgba(0,0,0,0.03), inset 0 2px 4px rgba(0,0,0,0.02);
}
.learning-num {
    font-family: var(--font-display); font-size: 2.8rem;
    color: var(--ink-faint);  /* Default */
    transition: color 0.4s ease;
}
.learning-item:hover .learning-num { color: var(--color-model); }

.learning-text {
    font-family: var(--font-body); font-size: 1.35rem;
    line-height: 1.6; color: var(--ink-body); font-weight: 400;
}
```

### 6.11 Blueprint Diagram (Concept / Fig 1)
The premium "definition + vs comparison" diagram.

```css
.svg-replica-1 {
    padding: 5rem;
    background: #FAFAFA;                  /* Lighter than paper for contrast */
    border: 1px solid #E5E7EB;
    border-radius: 24px;
    perspective: 1200px;
    /* Dot grid background (blueprint paper) */
    background-image: radial-gradient(#D1D5DB 1px, transparent 1px);
    background-size: 24px 24px;
    position: relative; overflow: hidden;
}
/* Radial series-color glow from top-center */
.svg-replica-1::before {
    content: ''; position: absolute; top: 30%; left: 50%;
    width: 80%; height: 80%;
    background: radial-gradient(circle, var(--color-model-light) 0%, transparent 60%);
    transform: translate(-50%, -50%); z-index: 0; pointer-events: none;
}

.svg-1-def-box {
    /* Dark inset — the "definition on chalkboard" moment */
    background: var(--ink-main);
    border-radius: 20px; padding: 4rem 3rem;
    color: #FFF;
    box-shadow: 0 20px 50px rgba(0,0,0,0.2), inset 0 1px 1px rgba(255,255,255,0.05);
    transform-style: preserve-3d;
}
.svg-1-def-box:hover { transform: translateY(-5px) rotateX(2deg); }

.svg-1-def-label {  /* Eyebrow */
    font-family: var(--font-mono); font-weight: 800;
    color: var(--color-env);  /* Cyan — the environment color */
    letter-spacing: 0.2em;
}
.svg-1-def-title {
    font-family: var(--font-display);
    font-size: clamp(2.5rem, 5vw, 3.5rem);
    color: #FFF;
}

.svg-1-split {
    display: grid; grid-template-columns: 1fr auto 1fr;
    gap: 1.5rem; align-items: center;
}
.vs-divider {
    font-family: var(--font-mono); font-weight: 800;
    background: #FFF; border: 1px solid #E5E7EB;
    width: 48px; height: 48px; border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    box-shadow: 0 10px 20px rgba(0,0,0,0.05);
}

.interactive-card {
    background: rgba(255,255,255,0.8);
    backdrop-filter: blur(12px);
    border: 1px solid #E5E7EB;
    border-radius: 16px;
    padding: 3.5rem 2.5rem;
    transform-style: preserve-3d;
}
.interactive-card.eval {
    border: 2px solid var(--color-model);  /* Series accent */
    background: #FFF;
}
/* Card icon (SVG) + label + sentence */
```

### 6.12 Practice Diagram (Pass/Fail Comparison / Fig 2)
```css
.svg-replica-2 {
    padding: 5rem; background: #FFFFFF;
    border: 1px solid #E5E7EB; border-radius: 24px;
    perspective: 1200px;
}
.svg-2-card.pass { border: 2px solid var(--color-success); }
.svg-2-card.fail { border: 2px solid var(--color-harness); }
.svg-2-card-head.pass { background: var(--color-success); color: #FFF; }
.svg-2-card-head.fail { background: var(--color-harness); color: #FFF; }
.svg-2-pill.pass { color: var(--color-success); background: rgba(5, 150, 105, 0.08); }
.svg-2-pill.fail { color: var(--color-harness); background: var(--color-harness-light); }
.svg-2-result {
    font-family: var(--font-display); font-size: 3rem;
    /* pass = success color, fail = harness color */
}
```

Both diagrams get 3D tilt interaction (same pattern as sticky cards, ±4deg rotation).

### 6.13 Mistake Card (Anti-Pattern)
```css
.mistake-card {
    padding: 4.5rem; background: #FFFFFF;
    border: 1px solid rgba(225, 29, 72, 0.15);
    border-left: 6px solid var(--color-harness);
    border-radius: 12px;
    box-shadow: 0 20px 40px var(--color-harness-light);
    position: relative; overflow: hidden;
}
/* ANTI-PATTERN watermark */
.mistake-card::before {
    content: 'ANTI-PATTERN';
    position: absolute; top: -10%; right: -5%;
    font-family: var(--font-sans); font-weight: 900; font-size: 8rem;
    color: rgba(225, 29, 72, 0.03);
    transform: rotate(-10deg);
    pointer-events: none;
}
.mistake-icon {
    background: var(--color-harness); color: white;
    width: 32px; height: 32px; border-radius: 50%;
    box-shadow: 0 4px 10px rgba(225, 29, 72, 0.3);
}
.mistake-card h3 {
    font-family: var(--font-sans); font-size: 1.8rem; font-weight: 700;
    color: #881337;  /* Deep rose */
}
.mistake-card p {
    font-family: var(--font-body); font-size: 1.35rem;
    color: #9F1239;  /* Rose body */
}
```

### 6.14 Spec Card (Dark Terminal)
```css
.spec-card {
    background: #0A0C10;  /* Near-black */
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 12px;
    color: #E2E2E9;
}
.spec-header {
    background: #111318;
    display: flex; align-items: center; gap: 1.5rem;
    padding: 1.2rem 2rem;
}
.mac-dot.r { background: #FF5F56; }  /* Red */
.mac-dot.y { background: #FFBD2E; }  /* Yellow */
.mac-dot.g { background: #27C93F; }  /* Green */

.spec-content.input-box {
    font-family: var(--font-mono); font-size: 1rem;
    color: #61AFEF;  /* Blue — terminal prompt */
    background: #15171E; padding: 2rem;
    border-radius: 6px;
    border: 1px solid rgba(255,255,255,0.05);
}
.spec-content.expected-box {
    font-family: var(--font-sans);
    background: rgba(5, 150, 105, 0.1);
    border-left: 4px solid var(--color-success);
    color: #A7F3D0;  /* Light emerald */
}
.spec-content.expected-box strong { color: #34D399; }

.severity-badge {
    background: var(--color-harness); color: #FFFFFF;
    font-family: var(--font-mono); font-size: 0.75rem; font-weight: 800;
    padding: 0.4rem 1.2rem; border-radius: 999px;
    text-transform: uppercase; letter-spacing: 0.1em;
}
```

### 6.15 Drop Cap (Article Opening Paragraph)
```css
.drop-cap::first-letter {
    float: left;
    font-family: var(--font-display);
    font-size: 6.8rem; line-height: 0.7;
    padding-top: 0.08em; padding-right: 0.12em;
    /* Gradient uses series accent */
    background: linear-gradient(135deg, var(--color-model), /* lighter end */);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
```
Gradient end per series: AI Evals `#C084FC`, Agentic Stack `#67E8F9`, Harness `#FB7185`.

### 6.16 Wet-Ink Highlighter
```css
mark.pastel-highlight {
    background-color: transparent;
    background-image: linear-gradient(110deg,
        transparent 2%,
        var(--color-model-light) 5%,
        var(--color-model-light) 95%,
        transparent 98%);
    background-size: 0% 100%;  /* Starts empty */
    background-repeat: no-repeat;
    background-position: left center;
    transition: background-size 1.2s var(--ease-cinematic);
    padding: 0.1em 0.2em; border-radius: 4px;
    mix-blend-mode: multiply;  /* Authentic ink-on-paper */
    box-decoration-break: clone;
}
mark.pastel-highlight.visible { background-size: 100% 100%; }
```
Triggered by IntersectionObserver at 15% threshold.

### 6.17 Up Next Card (Liquid Border Expand)
```css
.next-card {
    background: #FFFFFF; border: 1px solid #E5E7EB;
    padding: 5rem 4rem; border-radius: 24px;
    transition: all 0.6s var(--ease-cinematic);
    position: relative; overflow: hidden;
}
.next-card::before {
    content: ''; position: absolute; inset: 0;
    border: 3px solid var(--color-model);
    border-radius: 24px;
    opacity: 0; transform: scale(0.98);
    transition: all 0.6s var(--ease-cinematic);
}
.next-card:hover {
    transform: translateY(-8px) scale(1.01);
    box-shadow: 0 40px 80px var(--color-model-light);
    border-color: transparent;
}
.next-card:hover::before { opacity: 1; transform: scale(1); }
.next-card:hover .next-arrow {
    background: var(--color-model); color: white;
    transform: translateX(8px);
}
.next-title {
    font-family: var(--font-display); font-size: 4.2rem;
    font-weight: 400; color: var(--ink-main);
}
```

### 6.18 Magnetic Back Button (Top + Bottom of Article)
```css
.magnetic-btn {
    display: inline-flex; align-items: center; gap: 0.75rem;
    background: transparent; color: var(--ink-faint);
    padding: 0.8rem 1.5rem; border-radius: 999px;
    font-family: var(--font-sans); font-size: 0.9rem; font-weight: 600;
    border: 1px solid #D1D5DB;
    transition: background 0.4s, border-color 0.4s, color 0.4s, box-shadow 0.4s;
}
.magnetic-btn:hover {
    border-color: var(--ink-main); color: var(--ink-main);
    background: #FFFFFF;
    box-shadow: 0 10px 20px rgba(0,0,0,0.04);
}
.magnetic-btn svg { transition: transform 0.4s var(--ease-cinematic); }
.magnetic-btn:hover svg { transform: translateX(-4px); }
```

Magnetic physics (desktop >768px only):
```js
btn.addEventListener('mousemove', (e) => {
    const rect = btn.getBoundingClientRect();
    const x = e.clientX - rect.left - rect.width / 2;
    const y = e.clientY - rect.top - rect.height / 2;
    btn.style.transform = `translate(${x * 0.15}px, ${y * 0.15}px)`;
    content.style.transform = `translate(${x * 0.08}px, ${y * 0.08}px)`;
});
// mouseleave: spring snap back 0.5s
```

### 6.19 Footer Signature
```css
.signature {
    font-family: var(--font-display); font-style: italic;
    font-size: 3.5rem; color: var(--ink-main);
    letter-spacing: -0.02em;
}
.copyright {
    font-family: var(--font-mono); font-size: 0.85rem;
    color: var(--ink-muted); font-weight: 600;
    text-transform: uppercase; letter-spacing: 0.15em;
}
```

---

## 7. Animation System

### 7.1 Core Easing Curves
```css
--ease-cinematic: cubic-bezier(0.16, 1, 0.3, 1);        /* Apple deceleration */
--ease-spring:    cubic-bezier(0.175, 0.885, 0.32, 1.1); /* Overshoot spring */
```

### 7.2 Keyframe Animations

**blurReveal** — hero content entry:
```css
@keyframes blurReveal {
    0% { opacity: 0; transform: translateY(30px) scale(0.98); filter: blur(8px); }
    100% { opacity: 1; transform: translateY(0) scale(1); filter: blur(0); }
}
/* Applied via: animation: blurReveal 1.2s var(--ease-cinematic) forwards */
/* Staggered delays: 0.1s, 0.2s, 0.3s */
```

**palankiReveal** — homepage name letter-spacing squeeze:
```css
@keyframes palankiReveal {
    0% { opacity: 0; filter: blur(12px); transform: scale(1.1) translateY(20px); letter-spacing: -0.1em; }
    100% { opacity: 1; filter: blur(0); transform: scale(1) translateY(0); letter-spacing: -0.03em; }
}
```

**pulseCyan** — PALANKI ghost pulse (via `::after` pseudo-element):
```css
@keyframes pulseCyan {
    0%, 100% { opacity: 0.2; filter: blur(2px); transform: scale(1); }
    50% { opacity: 0.8; filter: blur(8px); transform: scale(1.02); }
}
/* 4s infinite, starts at 1.5s delay */
```

**drawLine** — cyan underline on "Bridger." text:
```css
@keyframes drawLine {
    0% { transform: scaleX(0); }
    100% { transform: scaleX(1); }
}
/* Applied to ::after pseudo, transform-origin: left */
```

**scaleYIn** — editorial cyan vertical line:
```css
@keyframes scaleYIn {
    0% { transform: scaleY(0); opacity: 0; }
    100% { transform: scaleY(1); opacity: 1; }
}
```

**enginePulse** — rocket engine exhaust flame:
```css
@keyframes enginePulse {
    0% { opacity: 0.6; transform: translateY(-50%) scale(0.8); }
    100% { opacity: 1; transform: translateY(-50%) scale(1.3); }
}
/* 0.4s ease-in-out infinite alternate */
```

**noiseShift** — ambient noise texture drift (article pages):
```css
@keyframes noiseShift {
    0% { background-position: 0 0; }
    100% { background-position: 100% 100%; }
}
/* 8s steps(10) infinite */
```

**slowZoom** — hero background image Ken Burns:
```css
@keyframes slowZoom {
    0% { transform: scale(1); }
    100% { transform: scale(1.1); }
}
/* 30s linear infinite alternate */
```

### 7.3 Scroll-Driven Animations

**Cinematic reveal** (`.reveal` class):
```css
.reveal {
    opacity: 0;
    transform: translateY(40px) scale(0.98);
    filter: blur(4px);
    transition: opacity 1.2s var(--ease-cinematic),
                transform 1.2s var(--ease-cinematic),
                filter 1.2s var(--ease-cinematic);
    will-change: opacity, transform, filter;
}
.reveal.visible { opacity: 1; transform: translateY(0) scale(1); filter: blur(0); }
```
IntersectionObserver at 10-15% threshold, -10% root margin.

**Line-draw** (staggered cyan underlines on inline words):
```css
.line-draw::after {
    /* 2px cyan line, scaleX 0 → 1, transform-origin: left */
    transition: transform 0.8s var(--ease-cinematic);
}
.reveal.visible .line-draw:nth-of-type(1)::after { transition-delay: 0.8s; transform: scaleX(1); }
.reveal.visible .line-draw:nth-of-type(2)::after { transition-delay: 1.2s; transform: scaleX(1); }
.reveal.visible .line-draw:nth-of-type(3)::after { transition-delay: 1.6s; transform: scaleX(1); }
```

**Quote line reveal** — each `.quote-line > span` translates up individually:
```css
.quote-line span {
    display: block; transform: translateY(100%); opacity: 0;
    transition: transform 1s var(--ease-cinematic),
                opacity 1s var(--ease-cinematic);
}
.the-why.visible .quote-line span { transform: translateY(0); opacity: 1; }
.quote-line:nth-child(1) span { transition-delay: 0.1s; }
.quote-line:nth-child(2) span { transition-delay: 0.2s; }
```

### 7.4 Interactive Physics (JS-Driven, Desktop Only)

**3D isometric stack hover** (homepage hero viz):
- On mousemove: adjust rotateX/Z by ±0.05-0.15deg per pixel offset from center
- `transition: none` during move
- Spring ease 1.5s on mouseleave back to base `rotateX(60deg) rotateZ(-45deg)`

**Recession stacking** (deep dive sections):
- Formula: `scale = 1 - progress * 0.08`, `y = progress * 40`, `opacity = 1 - progress * 0.8`
- Background darkens: `brightness(1 - progress)`
- Run in `requestAnimationFrame` with `ticking` guard for 60fps

**Magnetic button physics**:
- Button translates at `0.15x` cursor offset from center
- Inner `.magnetic-content` translates at `0.08x` (creates depth)
- On mouseleave: spring snap-back 0.5s

**Folder card 3D tilt**:
- `rotateX/Y ±2-4deg` per card based on cursor position
- `scale3d(1.02, 1.02, 1.02)` on hover
- Children `translateZ(30px)` for depth lift
- Spring snap-back on mouseleave

**Dynamic ambient glow** (homepage only):
- Mouse position determines dual radial gradient centers
- Purple tracks `(x%, y%)`, cyan tracks `(100-x%, 100-y%)`
- Transition 0.5s

**Nav tightening** (scroll > 50px, desktop >768px):
- Padding reduces from `1.5rem` to `1rem`
- Background solidifies from gradient to `rgba(3,4,7,0.85)`

**Rocket flip** (scroll reverse):
- Track `lastScroll`; if `winScroll > lastScroll` → rotate 0deg
- If `winScroll < lastScroll` → rotate 180deg (flip)

### 7.5 Ironclad Rule

**No other animations.** No parallax on body content. No auto-playing hero videos. No spinner loaders. No confetti. No animation libraries (GSAP, Framer, Lottie). CSS + IntersectionObserver + requestAnimationFrame only.

---

## 8. Page Recipes

### Recipe: Homepage (`/`)
1. Dark canvas + noise + dynamic mouse-following glow
2. Hero: grid 1.2fr/0.8fr — "RAVI TEJA / PALANKI" (palankiReveal + pulseCyan ghost) + "AI-fluent product leader. The Bridger." (drawLine on Bridger.) + editorial lead/sub (line-draw words) + frosted badges + 3D isometric stack (STRATEGY/PRODUCT/ENGINEERING/DELIVERY, "AI PM" center)
3. Bridger: sticky card stack (3 cards: Engineering/Design/Business, with 3D tilt)
4. Two Paths: recession stacking (2 sticky 100vh sections: My Profile → Working Notes)
5. Proof Points: SVG ring counters (4 stats with counting animation)
6. Quote: line-by-line reveal
7. Article teaser: dark-to-white gradient + browser frame + Benchmarks ≠ Evals preview
8. Footer: LinkedIn | GitHub | Contact

### Recipe: Profile (`/profile`)
See `1_Projects/my-personal-website/lovable/04-PROFILE-PAGE-SPEC.md`. Uses folder-card 3D tilt for product cards (not sticky), SVG ring stats, timeline for career arc.

### Recipe: Writing Landing (`/writing`)
1. Dark canvas (noise + static glow)
2. Hero: grid 1.2fr/0.8fr, "THE AI / PRODUCTION / CHASM" + editorial block + 3D viz (MODEL/HARNESS/TOOLS/ENVIRONMENT, "AI" center)
3. Architecture: sticky card stack (4 cards with 3D tilt)
4. Anti-patterns: 3 red-accented cards (fixed 3-col grid)
5. Deep dives: recession stacking (4 sticky 100vh sections — Evals, Agentic, Strategy [soon], Leadership [soon])
6. Quote: Instrument Serif massive quote
7. Reading transition: gradient + browser frame + article preview
8. Footer

### Recipe: Series Hub (`/writing/evals`, `/writing/agentic-stack`, `/writing/harness-engineering`)
1. Dark canvas throughout (no white sections)
2. Series hero: 70vh, breadcrumb + display title + lead + stats
3. Level sections: badge + header + topic card grid (auto-fill 340px)
4. Reading guide: path recommendation cards
5. CTA: quote + start button
6. Footer

**Harness Engineering variant:** No levels — sequential 8-episode guide layout. See `11-HARNESS-ENGINEERING-SPEC.md`.

### Recipe: Article Reading Page
**Canonical template:** `reference/BLOG-POST-TEMPLATE.html`

1. Rocket progress bar (fixed, top)
2. Noise overlay (fixed)
3. Nav: brand (Newsreader italic) + single "Connect With Me ↗" CTA
4. Hero: 90vh, dark, Unsplash bg (grayscale, luminosity), topic pill + Instrument Serif title + meta pill with cyan dot
5. Paper canvas overlay: `margin-top: -12vh`, 40px rounded top, dot grid
6. Content layout (max 960px):
   - Top back-nav (magnetic)
   - Learning objectives block
   - Body sections (H2 Instrument Serif + Newsreader paragraphs, drop cap on first)
   - Diagrams (svg-replica-1, mistake-card, spec-card, svg-replica-2 as needed)
   - References
   - Up Next card (liquid border)
   - Bottom back-nav (magnetic)
   - Footer signature
7. Per-series accent override via `--color-model` + `--color-model-light`
8. Transform existing articles via `1_Projects/my-personal-website/scripts/apply-gold-template.py`

---

## 9. Per-Series Asset Map

| Series | Article route | Hero Unsplash theme | Count |
|--------|---------------|---------------------|-------|
| AI Evals | `/writing/evals/:slug` | Blueprint / measurement / observatory | 30 articles + 150 built diagrams |
| Agentic Stack | `/writing/agentic-stack/:slug` | Abstract neural / circuits / data | 35 articles (diagrams pending) |
| Harness Engineering | `/writing/harness-engineering/:slug` | Industrial machinery / factory floor | 1 built + 7 planned (16 SVGs spec'd) |

Backup safety: transformation script creates `.bak` files alongside originals for every write.

---

## 10. Readability Rules (Non-Negotiable)

1. **Minimum font sizes on dark backgrounds:** Body 1.15rem (Newsreader). Smaller text only for mono labels and meta (0.75rem with tight letter-spacing).
2. **Minimum font-weight on dark:** 400. Inter 300 is allowed ONLY for `--text-muted` or brighter.
3. **Minimum contrast:** WCAG AA (4.5:1) for body text. AAA (7:1) target for main text.
4. **Maximum line length:** 660px (optimal 65-75 chars). Enforced by `.text-col`.
5. **Line-height on body:** 1.7-1.8 for Newsreader paragraphs.
6. **Touch targets on mobile:** 44x44px minimum. Applies to nav links, CTA buttons, card tap areas.
7. **No pure black on pure white.** Use `#111318` on `#FCFDFD` for titles.
8. **No text below 0.65rem.** Even smallest labels stay legible.
9. **Hyphens on display titles:** `overflow-wrap: break-word; word-wrap: break-word; hyphens: auto; max-width: 100%;` prevents overflow on narrow viewports.

---

## 11. Responsive Breakpoints

### At 1024px (layout collapse)
```css
@media (max-width: 1024px) {
    .hero { grid-template-columns: 1fr; padding-top: 8rem; gap: 3rem; }
    .chasm-schematic { height: 400px; }
    .iso-plane { transform: rotateX(60deg) rotateZ(-45deg) scale(0.8); }
    .folder-card { height: auto; min-height: 50vh; padding: 3rem 2.5rem; margin-bottom: 5vh; }
    .card-1 { top: 90px; } .card-2 { top: 150px; } .card-3 { top: 210px; }
    .paths-container { padding-bottom: 10vh; }
    .path-hero { height: auto; min-height: 80vh; position: relative; box-shadow: none; }
    .signal-grid { grid-template-columns: repeat(2, 1fr); }
    .bleed-wide { margin: 4rem 0; }
    .svg-replica-1, .svg-replica-2 { padding: 3rem 2rem; }
    .progress-bar-container { top: 0; left: 0; right: 0; border-radius: 0; height: 4px; }
}
```

### At 768px (mobile refinement)
```css
@media (max-width: 768px) {
    nav { padding: 1.25rem var(--px) !important; background: rgba(3,4,7,0.9) !important; }
    .nav-link { display: none; }  /* Only brand + CTA visible */
    .hero-titles .title-display { font-size: clamp(3rem, 11vw, 4.5rem); }
    .iso-plane { transform: rotateX(60deg) rotateZ(-45deg) scale(0.6); }
    .article-title { font-size: 3.5rem; overflow-wrap: break-word; }
    .paper-canvas { padding: 3rem 1.2rem 5rem; margin-top: -5vh; border-radius: 30px 30px 0 0; }
    .text-col h2 { font-size: 2.8rem; margin: 4rem 0 2rem; }
    .drop-cap::first-letter { font-size: 5rem; }
    .learning-block { padding: 2.5rem 1.5rem; }
    .learning-item { flex-direction: column; gap: 0.8rem; }
    .mistake-card { padding: 2.5rem 1.5rem; border-left-width: 4px; }
    .spec-body { padding: 2rem 1.5rem; }
    .spec-header { flex-direction: column; align-items: flex-start; gap: 1rem; }
    .svg-1-split, .svg-2-grid { grid-template-columns: 1fr; gap: 1.5rem; }
    .interactive-card { width: 100%; }
    .next-card { padding: 3rem 2rem; }
    .next-title { font-size: 3rem; }
    .signature { font-size: 2.8rem; }
    .meta-row { font-size: 0.7rem; padding: 0.6rem 1.2rem; gap: 0.8rem; flex-wrap: wrap; }
    .footer-links { flex-direction: column; gap: 1.5rem; }
}
```

### Mobile Optimization Checklist
- [ ] Body `scrollWidth` equals `viewport width` (no horizontal overflow)
- [ ] All titles have `overflow-wrap: break-word`
- [ ] Touch targets minimum 44x44
- [ ] Magnetic button physics disabled (<768px)
- [ ] 3D card tilt disabled (<1024px)
- [ ] 3D isometric mouse parallax disabled (<1024px)
- [ ] Custom cursor disabled (<1025px)
- [ ] Nav links hidden on <768px — only brand + CTA
- [ ] Grids collapse to single column
- [ ] `clamp()` sizing on all text
- [ ] Newsreader body line-height ≥ 1.6

---

## 12. What This Skill Does NOT Cover

- **Content voice and writing style** — see `ravi-thinking-skills` and `rtp-deep-dive-writer`
- **Article editorial structure** (story → core idea → trap → in practice) — see `rtp-deep-dive-writer`
- **Lovable-specific build instructions** (React component conversion, routing) — see `1_Projects/my-personal-website/lovable/` specs
- **SVG diagram design content** — per-article specs in `SVG-VISUAL-PLAN.md` for harness, evals diagrams already built in each article's HTML
- **Profile page deep content** — see `lovable/04-PROFILE-PAGE-SPEC.md`
- **Article content map** — see `lovable/09-CONTENT-MAP.md` (all 70 article routes)

---

## 13. Canonical References

| Artifact | Path |
|----------|------|
| Homepage HTML (final) | `1_Projects/my-personal-website/prototype/homepage-final.html` |
| Blog post template (gold standard) | `1_Projects/my-personal-website/reference/BLOG-POST-TEMPLATE.html` |
| Production writing landing | `1_Projects/my-personal-website/reference/production-landing.html` |
| Article reference (approved) | `1_Projects/my-personal-website/reference/REFERENCE-article-page.html` |
| Transformation script | `1_Projects/my-personal-website/scripts/apply-gold-template.py` |
| Lovable build specs (11 files) | `1_Projects/my-personal-website/lovable/00-10-*.md` |
| Harness episode spec | `1_Projects/my-personal-website/lovable/11-HARNESS-ENGINEERING-SPEC.md` |

When in doubt, the canonical HTML files win over any written description.
