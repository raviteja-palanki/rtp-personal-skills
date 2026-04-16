---
name: ravi-personal-branding
version: 2.1
description: Ravi Teja Palanki's complete design system for every visual surface — website (ravitejapalanki.com), presentations (Gamma, PowerPoint), documents (Word), diagrams, article pages. Dark + light themes properly separated. Nine creative principles that govern every choice. V2.1 adds 5 components from DEEP-DIVE-HUB-TEMPLATE: Live Trace observability engine, per-level semantic animated SVG badges, card laser on hover, status ring indicator, spotlight 3D tilt card.
author: Ravi Teja Palanki
created: 17 April 2026
updated: 17 April 2026 (v2.1 — added 5 components from DEEP-DIVE-HUB-TEMPLATE: Live Trace engine, semantic badges, card laser, status ring, spotlight 3D tilt)
supersedes: learn-site-design (v2.0), ravi-personal-branding (v1.0)
---

# Ravi Personal Branding — v2.1

The single source of truth for every visual decision Ravi makes — across HTML, Gamma presentations, PowerPoint decks, Word documents, diagrams, and article pages. This is not just a CSS catalog. It's the creative operating system.

**When to activate:**
- Building or updating ravitejapalanki.com
- Designing a Gamma presentation template
- Creating PowerPoint slides
- Writing Word documents for external audiences
- Building custom SVG diagrams or visualizations
- Any task where visual output carries Ravi's brand

**Every visual agent invokes this skill first.** Presentation Builder, Diagram Builder, UX Design Agent, Article Writer — all route through this before producing visual output.

**Canonical reference files:**
- Homepage (V8, cinematic landing): `1_Projects/my-personal-website/prototype/homepage-final.html`
- Blog post template (gold standard): `1_Projects/my-personal-website/reference/BLOG-POST-TEMPLATE.html`
- Deep-dive hub template (gold standard, v2.1 source): `1_Projects/my-personal-website/reference/DEEP-DIVE-HUB-TEMPLATE.html`
- Writing section landing: `1_Projects/my-personal-website/reference/production-landing.html`

---

## 1. The Creative Lens — Nine Principles

These are the principles behind every design choice. Internalize them; they explain why the CSS looks the way it does, and they transfer to Gamma slides, Word docs, and PowerPoint the same way they transfer to HTML.

### 1.1 Every Animation Has a Purpose
The rocket flips 180° on scroll reverse because direction matters. The scramble counter creates anticipation before revealing the real number. The quote illuminates word-by-word to force reading pace. No decoration.

*Cross-medium:* In Gamma, use scroll-triggered reveals, never auto-playing carousels. In PPT, animations serve narrative — never "just to make it move."

### 1.2 Signature Moments Per Section
Every major section has ONE stunning element that makes someone stop scrolling:
- Hero: suspension bridge SVG drawn beneath "The Bridger."
- Architecture: frosted glass sticky cards with identity-colored gradient tops
- Telemetry: scramble counter + "Metric_01 [Years]" dashboard framing
- The Why: word-by-word scroll-written quote + hand-drawn purple-to-rose highlight
- Two Paths: premium glass cards with 40px rounded top edge sliding over each other
- Article teaser: 3D pop browser frame (`rotateX(15deg) translateY(100px) scale(0.9)` entry)
- Deep-dive hub: Live Trace observability engine as hero background + per-level semantic SVG badges (reticle for L1, neural network for L2, isometric layers for L3, anomaly waveform for L4)
- Footer: "Crafted with intent by Ravi Teja Palanki" signature

*Cross-medium:* Every slide deck section needs ONE signature visual. Every Word doc section gets ONE editorial moment (blockquote, pullquote, or custom SVG).

### 1.3 Progressive Disclosure Through Scroll Position
Quote illuminates word-by-word based on scroll %. Cards slide as physical objects during recession stacking. Line-draw underlines stagger at 0.4s, 0.8s, 1.2s. The reader sets the pace. At the micro level, status ring indicators give each topic card a tiny breathing signal (draft / published / updated) — the same principle, expressed at 14px.

*Cross-medium:* In Gamma, use scroll-linked reveals. In PPT, use sequential animations with consistent timing. In Word, let layout force pacing — deliberate use of page breaks, pull quotes, full-width images.

### 1.4 Physical Materiality Over Flatness
Frosted glass (backdrop-filter blur 32px). Inset highlight shadows (`inset 0 1px 1px rgba(255,255,255,0.15)`). Premium card physics (40px rounded-top, inset light edge, 100px drop shadow). Surfaces feel touchable, not designed.

*Cross-medium:* In Gamma/PPT, cards need subtle shadows and slight elevation — never pure flat rectangles. Word docs use hairline borders + soft tinted backgrounds for callouts, not box outlines.

### 1.5 Typography as Three Rhythms
Instrument Serif italic (editorial) + Inter 900 uppercase (display) + JetBrains Mono caps (metadata). Three distinct beats that never blur into homogeneity.

*Cross-medium:* Every slide, every doc uses exactly these four fonts. Headings in Inter 900 or Instrument Serif. Body in Newsreader. Labels and data in JetBrains Mono. Never substitute.

### 1.6 Telemetry Over Statistics
Stats aren't "12 years experience" — they're "Metric_01 [Years] · 12+ · B2B Product Experience" in mono + scramble reveal. Feels like a systems dashboard, not a resume.

*Cross-medium:* In PPT, KPI slides use dashboard framing (`METRIC_NN`, `[UNIT]`, scramble-to-value). In Gamma, counter animations. In Word, metrics get their own structured table with mono labels.

### 1.7 Smooth Scroll as Baseline
Lenis smooth scroll (`@studio-freight/lenis`) replaces native. Every scroll interaction becomes cinematic by default.

*Cross-medium:* In PPT, transitions default to Morph or Fade (0.6-0.8s cubic-bezier easing), never Bounce or Wipe. In Gamma, cinematic scroll mode.

### 1.8 Tension Between Density and Breath
Sticky card stacks = dense. Quote section (`padding: 15vh 20vh`) = cavernous. The breathing rhythm between sections is itself a design element.

*Cross-medium:* In PPT, never pack six bullets on a slide. One signature idea per slide, then let whitespace carry weight. In Word, double-page spreads with a quote page alone are acceptable for emphasis.

### 1.9 Signature Closers
"This website is my product work. / Crafted with intent by *Ravi Teja Palanki*." The artifact IS the signature. No marketing speak.

*Cross-medium:* Every PPT deck ends with the same signature line. Every Word doc cover/closer uses Instrument Serif for the name. The signature carries across mediums unchanged.

---

## 2. The Identity System — 4 Colors

Every color carries meaning. Never decorative. Never flat background fills on any medium.

| Role | Website hex | Article hex | Meaning | Where |
|------|-------------|-------------|---------|-------|
| **Model** (intelligence) | `#9D4EDD` | `#8121D8` | The thinking layer | Drop caps, callouts, Evals series accent |
| **Harness** (guardrails) | `#F43F5E` | `#E11D48` | Warnings, anti-patterns | Mistake cards, Harness series accent |
| **Tools** (capabilities) | `#F59E0B` | `#F59E0B` | Amber — systems + engineering | L3 badges, amber accents |
| **Environment** (context) | `#06B6D4` | `#00E5FF` | Hero, cyan line, CTA halos | Default homepage accent |

**Functional:** Success `#059669` / `#10B981` (emerald). Info `#1E3A8A` text on `#EFF6FF` bg.

**Rules — never break:**
- Colors appear only as accents. Never flat background fills.
- Red is EXCLUSIVELY anti-patterns, warnings, mistakes. Never positive.
- On dark: border accents, text-shadow glows, radial gradients at 4-15% opacity.
- On light: border-left accents, tinted bg at 4-12% opacity, text color.

**Per-series accent override (articles + topic-specific presentations):**

| Series | `--color-model` | `--color-model-light` | Drop-cap gradient end |
|--------|-----------------|-----------------------|----------------------|
| AI Evals | `#8121D8` | `rgba(129, 33, 216, 0.12)` | `#C084FC` |
| Agentic Stack | `#0891B2` | `rgba(8, 145, 178, 0.12)` | `#67E8F9` |
| Harness Engineering | `#E11D48` | `rgba(225, 29, 72, 0.12)` | `#FB7185` |

---

## 3. Typography — 4 Fonts, Universal Across Mediums

| Font | CSS var | Role | Where |
|------|---------|------|-------|
| **Inter** | `--font-sans` | Display titles (900), UI, eyebrows | 300–900 weights |
| **Instrument Serif** | `--font-display` | Editorial moments, hero titles, quotes, drop caps, signatures, nav brand on articles | 400, 400 italic |
| **Newsreader** | `--font-body` | Body prose on both dark and light | 300, 400, 500, italic variants |
| **JetBrains Mono** | `--font-mono` | Labels, tags, metadata, code | 400, 500, 700, 800 |

**Cross-medium mandate:**
- **PowerPoint:** Install all 4 fonts on your machine. Every slide uses them natively. Never substitute with Arial/Calibri.
- **Gamma:** Load all 4 as Google Fonts in the theme settings.
- **Word:** Install all 4. Document styles map exactly — Heading 1 = Inter 900, Heading 2 = Instrument Serif 400, Body = Newsreader 400, Code/Metadata = JetBrains Mono.

**Typography rules — never break:**
- Inter 900 ONLY for display titles (uppercase, `letter-spacing: -0.03em`, `line-height: 0.95`).
- Instrument Serif NEVER for body prose. Only editorial moments.
- Newsreader ONLY for body prose on both themes.
- JetBrains Mono for ALL labels, tags, badges, code, meta. Font-weight 700–800. Uppercase. `letter-spacing: 0.15em`.
- Minimum font-weight 400 on dark. Inter 300 washes out.

---

## 4. DARK THEME — Default for Website, Presentations

**Default medium:** HTML landing pages, Gamma presentations, PowerPoint decks, dashboard visuals.

### 4.1 CSS Variables
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

### 4.2 Ambient Layers (Every Dark Page)

**Noise overlay** (z-index 9999):
```css
.noise-overlay {
    position: fixed; inset: 0;
    background: url("data:image/svg+xml,...fractalNoise baseFrequency=0.8 numOctaves=3...");
    opacity: 0.04;
    mix-blend-mode: screen;   /* V8 change — was multiply. Screen is lighter. */
    pointer-events: none;
}
```

**Ambient glow** (z-index 0, fixed):
```css
.glow-bg {
    position: fixed; inset: 0; pointer-events: none;
    background:
        radial-gradient(circle at 80% 0%, rgba(157, 78, 221, 0.08) 0%, transparent 50%),
        radial-gradient(circle at 20% 100%, rgba(6, 182, 212, 0.06) 0%, transparent 50%);
}
```

### 4.3 Readability (Dark Mode)
| Combination | Ratio |
|-------------|-------|
| `#FFFFFF` on `#030407` | 20.3:1 |
| `#F9FAFB` on `#030407` | 19.6:1 |
| `#D1D5DB` on `#030407` | 14.8:1 |
| `#9CA3AF` on `#030407` | 8.9:1 |

All pass WCAG AAA. For presentations viewed on projectors, enforce min `#D1D5DB` — never `#9CA3AF` for body text on a stage.

---

## 5. LIGHT THEME — Default for Word Documents, Blog Posts

**Default medium:** Word documents, article reading pages, printed materials.

### 5.1 CSS Variables
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

### 5.2 Paper Canvas (Signature Overlay on Article Pages)
```css
.paper-canvas {
    background: var(--bg-paper);
    margin-top: -12vh;                       /* Overlaps dark hero */
    border-radius: 40px 40px 0 0;
    padding: 6rem var(--px) 8rem;
    box-shadow:
        0 -40px 100px rgba(0,0,0,0.8),
        inset 0 1px 1px rgba(255,255,255,1),
        inset 0 2px 4px rgba(255,255,255,0.5);
    /* Dot grid — notebook texture */
    background-image: radial-gradient(rgba(0,0,0,0.03) 1px, transparent 1px);
    background-size: 32px 32px;
}
```

### 5.3 Reading Layout
- `.text-col` — `max-width: 660px` (65–75 char optimal line)
- `.bleed-wide` — `width: 100%; margin: 6rem 0` (diagrams break out)
- Parent `.content-layout` — `max-width: 960px; margin: 0 auto`

### 5.4 Readability (Light Mode)
| Combination | Ratio |
|-------------|-------|
| `#000000` on `#FCFDFD` | 20.9:1 |
| `#111318` on `#FCFDFD` | 18.2:1 |
| `#202226` on `#FCFDFD` | 14.5:1 |
| `#5A5D67` on `#FCFDFD` | 6.5:1 |

All pass WCAG AA; top three pass AAA. For Word printing, body stays `#202226` — never `#5A5D67`.

---

## 6. Component Catalog (V8)

### 6.1 Nav — Two Variants

**Homepage / Profile / Writing Hub** — brand + links + CTA:
```css
nav {
    position: fixed; top: 0; padding: 1.5rem var(--px);
    backdrop-filter: blur(12px);
    background: linear-gradient(to bottom, rgba(3,4,7,0.95), rgba(3,4,7,0));
    transition: padding 0.4s var(--ease-cinematic), background 0.4s var(--ease-cinematic);
}
nav.scrolled { padding: 1rem var(--px); background: rgba(3,4,7,0.85); }

.nav-brand {
    /* V8 update: Newsreader italic, not Inter */
    font-family: var(--font-body); font-style: italic; font-weight: 500;
    font-size: 1.5rem; letter-spacing: -0.01em;
    color: var(--text-pure);
}

.nav-link { font-family: var(--font-sans); font-weight: 600; font-size: 0.85rem; color: var(--text-main); }
.nav-link::after { /* cyan underline, scaleX 0→1 with origin flip */
    background: var(--color-env);  /* V8: cyan, not white */
}

.nav-cta {
    /* White pill with dark text */
    font-family: var(--font-mono); font-weight: 800; font-size: 0.72rem;
    background: var(--text-pure); color: var(--bg-base);
    padding: 0.7rem 1.5rem; border-radius: 50px;
    text-transform: uppercase; letter-spacing: 0.08em;
}
```

**Article page** — brand + single frosted CTA:
```css
.nav-cta {  /* Frosted variant for articles */
    background: rgba(255, 255, 255, 0.15);
    border: 1px solid rgba(255, 255, 255, 0.4);
    backdrop-filter: blur(12px);
    color: #FFFFFF !important;
}
.nav-cta:hover {
    background: #FFFFFF; color: #000000 !important;
    border-color: #FFFFFF;
}
```

### 6.2 Hero Name — `palankiReveal` + Cyan Ghost

Palanki hollow stroke with pulsing cyan echo:
```css
.palanki-text { position: relative; display: inline-block; }
.palanki-text::after {
    content: attr(data-text);  /* Clones text via data-text attribute */
    position: absolute; left: 0; top: 0;
    color: transparent; -webkit-text-stroke: 2px var(--color-env);
    opacity: 0; animation: pulseCyan 4s ease-in-out infinite 1.5s;
    z-index: -1; pointer-events: none;
}
@keyframes pulseCyan {
    0%, 100% { opacity: 0.2; filter: blur(2px); transform: scale(1); }
    50% { opacity: 0.8; filter: blur(8px); transform: scale(1.02); }
}
```

### 6.3 Suspension Bridge SVG (The Signature Under "Bridger.")

This is the V8 crown jewel. An 180×45px SVG of a suspension bridge with deck, towers, sweeping cables, and 11 vertical suspenders. Animates via stroke-dashoffset on reveal.

```html
<svg class="bridge-schematic" viewBox="0 0 300 70">
    <!-- Deck -->
    <line x1="0" y1="55" x2="300" y2="55" stroke="rgba(6,182,212,0.4)" stroke-width="1.5"/>
    <line x1="0" y1="60" x2="300" y2="60" stroke="rgba(6,182,212,0.2)" stroke-width="1"/>
    <!-- Towers -->
    <path d="M 75 10 L 75 65 M 225 10 L 225 65" stroke="var(--color-env)" stroke-width="1.5" opacity="0.8"/>
    <polyline points="70 65 75 10 80 65" stroke="var(--color-env)" stroke-width="0.5" fill="none" opacity="0.4"/>
    <polyline points="220 65 225 10 230 65" stroke="var(--color-env)" stroke-width="0.5" fill="none" opacity="0.4"/>
    <!-- Main sweeping cables -->
    <path d="M 0 45 Q 75 10 150 50 Q 225 10 300 45" stroke="var(--color-env)" stroke-width="1.5" fill="none" opacity="0.7"/>
    <!-- 11 vertical suspenders at varying heights -->
    <line x1="20" y1="36" ... />  <!-- See homepage-final.html for full coords -->
</svg>
```

```css
.bridge-schematic path, .bridge-schematic line, .bridge-schematic polyline {
    stroke-dasharray: 600; stroke-dashoffset: 600;
}
.reveal-up.is-visible .bridge-schematic path,
.reveal-up.is-visible .bridge-schematic line,
.reveal-up.is-visible .bridge-schematic polyline {
    animation: drawBridge 2.5s var(--ease-cinematic) forwards 0.8s;
}
@keyframes drawBridge { to { stroke-dashoffset: 0; } }
```

### 6.4 3D Isometric Stack with Floating Planes + Data Stream

**Floating iso planes** (V8 upgrade):
```css
@keyframes floatIso { 0%, 100% { transform: translateZ(var(--tz)); } 50% { transform: translateZ(calc(var(--tz) + 12px)); } }
.iso-layer {
    animation: floatIso 6s ease-in-out infinite;
    /* Each layer gets a staggered animation-delay: 0s, 0.5s, 1s, 1.5s */
}
.iso-strategy { --tz: 110px; animation-delay: 0s; }
.iso-product { --tz: 40px; animation-delay: 0.5s; }
.iso-engineering { --tz: -30px; animation-delay: 1s; }
.iso-delivery { --tz: -100px; animation-delay: 1.5s; }
```

**Core beam with data packets** (V8 signature):
```css
.core-beam {
    /* 4px vertical laser through the stack */
    width: 4px; height: 450px;
    background: linear-gradient(to bottom, transparent 0%, #FFF 20%, var(--color-env) 50%, #FFF 80%, transparent 100%);
    box-shadow: 0 0 20px var(--color-env), 0 0 40px rgba(6,182,212,0.8), 0 0 60px rgba(6,182,212,0.5);
    border-radius: 50px;
    animation: pulseBeam 3s ease-in-out infinite;
}
.data-packet {
    position: absolute; left: -1px; width: 6px; height: 35px; background: #FFF;
    box-shadow: 0 0 15px #FFF, 0 0 30px var(--color-env), 0 0 50px var(--color-env);
    animation: dataStream 2.5s linear infinite;
    border-radius: 10px;
}
.data-packet:nth-child(2) { animation-delay: 0.8s; height: 45px; }
.data-packet:nth-child(3) { animation-delay: 1.6s; height: 25px; }

@keyframes dataStream {
    0% { top: -10%; opacity: 0; transform: scaleY(0.8); }
    15% { opacity: 1; transform: scaleY(1.5); }
    85% { opacity: 1; transform: scaleY(1.5); }
    100% { top: 110%; opacity: 0; transform: scaleY(0.8); }
}
```

### 6.5 Sticky Card Stack (Frosted Glass, V8)
```css
.folder-card {
    position: sticky; height: 75vh;
    backdrop-filter: blur(32px); -webkit-backdrop-filter: blur(32px);
    border: 1px solid rgba(255,255,255,0.1);
    border-top: 1px solid rgba(255,255,255,0.25);  /* Brighter top edge = light catching */
    box-shadow: inset 0 1px 1px rgba(255,255,255,0.15), 0 30px 60px rgba(0,0,0,0.8);
    border-radius: 12px;
}
/* Identity-colored gradient top */
.card-1 { border-top: 2px solid var(--color-env); background: linear-gradient(145deg, rgba(6,182,212,0.08) 0%, rgba(10,11,16,0.6) 100%); }
.card-2 { border-top: 2px solid var(--color-model); background: linear-gradient(145deg, rgba(157,78,221,0.08) 0%, rgba(10,11,16,0.6) 100%); }
.card-3 { border-top: 2px solid var(--color-tools); background: linear-gradient(145deg, rgba(245,158,11,0.08) 0%, rgba(10,11,16,0.6) 100%); }

/* Titles: Instrument Serif on homepage, NOT Inter */
.folder-card h3 {
    font-family: var(--font-display);
    font-size: clamp(3rem, 5vw, 4.5rem);
    font-weight: 400;
    letter-spacing: -0.02em;
}
```

### 6.6 Telemetry Stat Grid (V8 Dashboard Framing)

Replaces the older SVG ring stats. This is the signature for proof points.

```css
.telemetry-grid {
    display: grid; grid-template-columns: repeat(4, 1fr);
    gap: 1px;  /* 1px gap creates thin divider lines */
    background: var(--border-dim);
    border: 1px solid var(--border-dim);
}
.telemetry-box {
    background: radial-gradient(circle at top right, rgba(255,255,255,0.02), transparent 80%), var(--bg-surface);
    padding: 4rem 2rem;
    transition: all 0.5s var(--ease-cinematic);
}
.telemetry-box:hover {
    background: radial-gradient(circle at top right, rgba(255,255,255,0.08), transparent 80%), var(--bg-surface);
    border-color: rgba(255,255,255,0.15);
    transform: translateY(-8px); z-index: 10;
    box-shadow: 0 20px 40px rgba(0,0,0,0.6);
}
.t-header {
    /* V8 signature: "Metric_01" + "[Years]" mono dashboard framing */
    font-family: var(--font-mono); font-size: 0.7rem;
    color: var(--text-faint); text-transform: uppercase; letter-spacing: 0.15em;
    display: flex; justify-content: space-between;
}
.t-value {
    font-family: var(--font-sans); font-size: clamp(3rem, 4vw, 4.5rem);
    font-weight: 900; letter-spacing: -0.04em;
}
```

**Scramble counter JS** (1.2s anticipation reveal):
```js
const duration = 1200;
const startTime = performance.now();
function updateCounter(currentTime) {
    const elapsed = currentTime - startTime;
    if (elapsed < duration) {
        counter.innerText = Math.floor(Math.random() * target * 2);  // Scramble
        requestAnimationFrame(updateCounter);
    } else {
        counter.innerText = target;  // Lock final value
    }
}
```

### 6.7 The Why — Scroll-Written Quote + Hand-Drawn Highlight

**Word-by-word scroll illumination:**
```css
.q-word {
    opacity: 0.15;  /* Dim until activated */
    transition: opacity 0.4s ease, text-shadow 0.4s ease;
    display: inline-block;
}
.q-word.lit {
    opacity: 1;
    text-shadow: 0 0 15px rgba(255,255,255,0.4);
}
```

```js
// JS: based on container's rect.top, calculate progress 0-1, light that many words
const progress = Math.min(1, Math.max(0, (start - rect.top) / (start - end)));
const activeWords = Math.floor(progress * qWords.length);
qWords.forEach((word, i) => word.classList.toggle('lit', i <= activeWords));
```

**Hand-drawn highlight** (purple-to-rose marker sweep, 2.5s slow draw):
```css
.hand-drawn-highlight::before {
    content: ''; position: absolute; bottom: 0.08em; left: -2%;
    width: 0; height: 45%;
    background: linear-gradient(90deg, var(--color-model), #F43F5E);
    opacity: 0.85; z-index: -1;
    transform: rotate(-1deg);  /* Handwritten feel — slight angle */
    border-radius: 6px;
    transition: width 2.5s var(--ease-cinematic) 0.3s;
}
.highlight-wrapper.is-visible .hand-drawn-highlight::before {
    width: 104%;  /* Slightly overshoot — authentic marker feel */
}
```

### 6.8 Premium Glass Cards — Recession Stacking

V8 upgrade: paths are physical cards with rounded-top, inset light edge, massive drop shadow.

```css
.path-hero {
    position: sticky; top: 0; height: 100vh;
    background: var(--bg-base);
    border-top: 1px solid rgba(255,255,255,0.2);   /* Light edge */
    border-radius: 40px 40px 0 0;                  /* Physical card feel */
    box-shadow:
        0 -40px 100px rgba(0,0,0,1),               /* Massive drop shadow */
        inset 0 1px 2px rgba(255,255,255,0.3);     /* Light catching top */
}
.path-hero:first-child {
    /* First card integrates with page — no curve */
    border-radius: 0; border-top: none; box-shadow: none;
}
```

**Recession animation** (scroll-driven, `requestAnimationFrame`):
```js
progress = 1 - (Math.max(0, nextRect.top) / window.innerHeight)
scale = 1 - (progress * 0.08)
y = progress * 40
opacity = 1 - (progress * 0.8)
contentWrapper.style.transform = `translate3d(0, ${y}px, 0) scale(${scale})`
contentWrapper.style.opacity = opacity
```

### 6.9 3D Pop Browser Frame (V8)

Browser frame entry animation — rotates in from 15deg with translateY + scale:
```css
.browser-container { perspective: 1200px; }
.browser-pop {
    opacity: 0;
    transform: rotateX(15deg) translateY(100px) scale(0.9);
    transition: all 1.2s cubic-bezier(0.175, 0.885, 0.32, 1.1);  /* Spring */
    transform-origin: bottom center;
}
.browser-pop.is-visible {
    opacity: 1;
    transform: rotateX(0deg) translateY(0) scale(1);
}
```

**macOS chrome** — gradient bar, slightly lifted:
```css
.browser-chrome {
    background: linear-gradient(to bottom, #2a2d36, #1a1c23);
    border-bottom: 1px solid #000;
    box-shadow: inset 0 1px 0 rgba(255,255,255,0.05);
}
.browser-dot.r { background: #FF5F56; }
.browser-dot.y { background: #FFBD2E; }
.browser-dot.g { background: #27C93F; }
```

### 6.10 Neon Highlight (Dark Mode Articles Inside Browser Frame)
```css
mark.neon-highlight {
    background: transparent;
    background-image: linear-gradient(110deg, transparent 2%, rgba(157,78,221,0.2) 5%, rgba(157,78,221,0.4) 95%, transparent 98%);
    color: #FFF;
    padding: 0.1em 0.3em; border-radius: 4px;
}
```

### 6.11 Pastel Highlight (Light Mode Articles — Paper Canvas)
```css
mark.pastel-highlight {
    background-image: linear-gradient(110deg, transparent 2%, var(--color-model-light) 5%, var(--color-model-light) 95%, transparent 98%);
    background-size: 0% 100%;  /* Animates to 100% on scroll */
    transition: background-size 1.2s var(--ease-cinematic);
    mix-blend-mode: multiply;  /* Ink-on-paper */
    padding: 0.1em 0.2em; border-radius: 4px;
}
mark.pastel-highlight.visible { background-size: 100% 100%; }
```

### 6.12 Product Signature Footer (V8)
```html
<footer>
    <div class="footer-links">...</div>
    <div class="footer-signature">
        <div>This website is my product work.</div>
        <div>Crafted with intent by <span class="sig-name">Ravi Teja Palanki</span></div>
    </div>
</footer>
```
```css
.footer-signature {
    font-family: var(--font-body); font-style: italic;
    color: var(--text-faint); font-size: 1.15rem;
}
.sig-name {
    font-family: var(--font-display);
    font-size: 2rem;
    color: var(--text-pure);
    font-style: normal;  /* The name is strong, not italic */
}
```

### 6.13 Other Core Components
- **Topic pill** — frosted glass, mono caps, 0.2em letter-spacing
- **Credential badge** — frosted with colored dot glow (cyan/purple/amber)
- **Rocket progress bar** — article-page only (not on homepage V8)
- **Mistake card** — red left border, ANTI-PATTERN watermark (article pages)
- **Spec card** — dark terminal with mac dots, blue mono input, emerald expected (article pages)
- **Blueprint diagram (svg-replica-1)** — dot grid bg, dark def-box with cyan label, VS circle, interactive cards with 3D tilt
- **Practice diagram (svg-replica-2)** — pass/fail comparison cards
- **Up Next card** — liquid border expand on hover
- **Magnetic back button** — physics-based hover tracking

Full CSS in `BLOG-POST-TEMPLATE.html` for article-page components.

---

## 6B. Deep-Dive Hub Components (v2.1 — Components #31–#35)

Five components introduced with `DEEP-DIVE-HUB-TEMPLATE.html`. These power the series hub pages (/writing/evals, /writing/agentic-stack, /writing/harness-engineering). They are **HTML-primary** — most do not port cleanly to Gamma / PPT / Word. Where cross-medium use is possible, it's called out.

### 6.14 Component #31 — Live Trace Observability Engine

**Purpose:** Animated SVG background that simulates live observability traces — vertical spine with lateral branches, data pulses, node rectangles labeled `span: INPUT`, `span: RETRIEVE`, `EVAL: PASS`. Makes the hub page feel like a running system, not a brochure.

**When to use:** HTML hero backgrounds for technical series hubs (evals, agentic stack, observability topics). One per page — it IS the signature. Do not reuse on other sections.

**Cross-medium:** HTML only. Do not port to PPT/Gamma (animation fidelity won't survive) or Word (static image loses the point). In Gamma, use a static export as a section-divider visual if absolutely needed.

**Structure:**
```html
<svg class="trace-engine" viewBox="0 0 600 800" preserveAspectRatio="xMidYMid meet">
  <defs>
    <linearGradient id="traceGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%"   stop-color="#06B6D4" stop-opacity="0"/>
      <stop offset="20%"  stop-color="#06B6D4" stop-opacity="0.8"/>
      <stop offset="50%"  stop-color="#9D4EDD" stop-opacity="0.8"/>
      <stop offset="80%"  stop-color="#F59E0B" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#F59E0B" stop-opacity="0"/>
    </linearGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="4" result="coloredBlur"/>
      <feMerge><feMergeNode in="coloredBlur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <g stroke="url(#traceGrad)" stroke-width="2" fill="none" filter="url(#glow)">
    <path d="M 300 50 L 300 750" class="trace-path"/>
    <path d="M 300 200 C 400 200 450 250 450 300" class="trace-path" style="animation-delay: 0.7s;"/>
    <path d="M 300 400 C 200 400 150 450 150 500" class="trace-path" style="animation-delay: 0.9s;"/>
    <path d="M 300 600 C 400 600 400 650 400 700" class="trace-path" style="animation-delay: 1.1s;"/>
  </g>
  <path d="M 300 50 L 300 750" stroke="#FFF" stroke-width="3" fill="none" class="trace-pulse"/>
  <g fill="rgba(10,11,16,0.8)" stroke="rgba(255,255,255,0.2)" stroke-width="1">
    <rect x="240" y="80"  width="120" height="30" rx="4" class="trace-node"/>
    <rect x="390" y="285" width="120" height="30" rx="4" class="trace-node"/>
    <rect x="90"  y="485" width="120" height="30" rx="4" class="trace-node"/>
    <rect x="340" y="685" width="120" height="30" rx="4" stroke="#06B6D4" class="trace-node"/>
  </g>
  <g fill="#6B7280" class="trace-text">
    <text x="250" y="100">span: INPUT</text>
    <text x="400" y="305">span: RETRIEVE</text>
    <text x="100" y="505">span: GENERATE</text>
    <text x="350" y="705" fill="#06B6D4">EVAL: PASS</text>
  </g>
</svg>
```

```css
.trace-engine {
    position: absolute; top: 5%; right: -5vw;
    width: 60vw; height: 90vh; max-width: 800px;
    pointer-events: none; z-index: 0; opacity: 0.8;
    filter: drop-shadow(0 0 20px rgba(157,78,221,0.2));
}
.trace-path  { stroke-dasharray: 1000; stroke-dashoffset: 1000; animation: drawTrace 3s var(--ease-cinematic) forwards 0.5s; }
.trace-pulse { stroke-dasharray: 20 100; animation: flowData 2s linear infinite; }
.trace-node  { transform-origin: center; transform-box: fill-box; animation: nodePulse 3s ease-in-out infinite; }
.trace-node:nth-child(even) { animation-delay: 1.5s; }
.trace-text  { font-family: var(--font-mono); font-size: 10px; font-weight: 700; letter-spacing: 0.1em; opacity: 0; animation: fadeIn 1s forwards 2s; }

@keyframes drawTrace { to { stroke-dashoffset: 0; } }
@keyframes flowData  { from { stroke-dashoffset: 120; } to { stroke-dashoffset: 0; } }
@keyframes nodePulse { 0%, 100% { transform: scale(1); opacity: 0.6; } 50% { transform: scale(1.1); opacity: 1; filter: drop-shadow(0 0 10px currentColor); } }
@keyframes fadeIn    { to { opacity: 0.7; } }

/* Mobile — hide or heavily fade */
@media (max-width: 1024px) { .trace-engine { opacity: 0.3; right: -20vw; } }
@media (max-width:  768px) { .trace-engine { display: none; } }
```

**Parameter knobs:**
- **Gradient stops** — change the three mid-colors to match series accent (Evals=purple, Agentic=cyan, Harness=rose)
- **`--trace-engine opacity`** — 0.8 on dark hero; drop to 0.4 if hero text contrast struggles
- **Animation delays on `.trace-path`** — stagger 0.2s increments; matches trace debugger UX
- **Node count** — 3 to 5 rectangles. More than 5 reads as clutter.

**Performance note (important):** The Live Trace engine uses an SVG `feGaussianBlur` filter (`stdDeviation: 4`) on infinite-loop animated paths. This is GPU-expensive on low-end devices and can tank LCP by 200-400ms if placed in the hero viewport on mobile. Mitigations:
- `display: none` on `<768px` (already in the template — keep it)
- `opacity: 0.3` and move off-canvas on `<1024px`
- Never place this component above the fold on pages where LCP matters for SEO
- If the page has Lighthouse issues, first candidate to remove

**Anti-pattern:** Don't put this behind body copy. It's a hero-only signature. Don't use it on non-technical pages (About, Contact) — the "span: INPUT / EVAL: PASS" metaphor is confusing without the observability context.

**Companion components:** Pairs with per-level semantic badges (#32) and the hub hero layout. The trace visual legitimizes the deep-dive framing.

---

### 6.15 Component #32 — Per-Level Semantic Animated SVG Badges

**Purpose:** Each progression level (L1/L2/L3/L4) gets a distinct 100x100 SVG badge whose visual metaphor ENCODES the level's meaning. Not decorative. L1 = targeting reticle (foundations, finding your footing). L2 = neural-network graph (the practice, building systems). L3 = isometric stacked layers (architecture, production). L4 = anomaly waveform (the leading edge, unsolved territory).

**When to use:** Deep-dive hub pages, curriculum pages, any place with 3-5 ordered levels that each carry distinct meaning. The visual metaphor must be obvious — if the badge needs explanation, it failed.

**Cross-medium:** HTML primary. Static PNG exports work in Gamma / PPT / Word as decorative section dividers — but the animation is what sells them. In Word, use them flat with a 1px stroke to stay on-brand.

**Structure — container:**
```html
<div class="level-badge">
    L1  <!-- visible label behind the SVG -->
    <svg class="badge-svg" viewBox="0 0 100 100">
      <!-- level-specific content — see below -->
    </svg>
</div>
```

```css
.level-badge {
    flex-shrink: 0; width: 80px; height: 80px; border-radius: 20px;
    background: var(--level-bg);            /* per-level tint at 5% opacity */
    border: 1px solid rgba(255,255,255,0.1);
    display: flex; align-items: center; justify-content: center;
    font-family: var(--font-mono); font-size: 1.5rem; font-weight: 800;
    color: var(--level-color);
    box-shadow: 0 10px 30px rgba(0,0,0,0.5), inset 0 1px 1px rgba(255,255,255,0.2);
    position: relative; overflow: hidden;
}
.badge-svg { position: absolute; inset: 0; width: 100%; height: 100%; opacity: 0.6; z-index: -1; }

/* Per-level color + background mapping */
#level-1 { --level-color: #06B6D4; --level-bg: rgba(6, 182, 212, 0.05); }
#level-2 { --level-color: #9D4EDD; --level-bg: rgba(157, 78, 221, 0.05); }
#level-3 { --level-color: #F59E0B; --level-bg: rgba(245, 158, 11, 0.05); }
#level-4 { --level-color: #F43F5E; --level-bg: rgba(244, 63, 94, 0.05); }
```

**L1 — Targeting Reticle** (foundations, aim at the fundamentals):
```html
<svg class="badge-svg" viewBox="0 0 100 100">
  <pattern id="gridL1" width="10" height="10" patternUnits="userSpaceOnUse">
    <path d="M 10 0 L 0 0 0 10" fill="none" stroke="currentColor" stroke-width="0.5" opacity="0.2"/>
  </pattern>
  <rect width="100" height="100" fill="url(#gridL1)"/>
  <g class="l1-reticle" style="transform-origin: 50% 50%;">
    <circle cx="50" cy="50" r="20" fill="none" stroke="currentColor" stroke-width="1.5"/>
    <circle cx="50" cy="50" r="10" fill="none" stroke="currentColor" stroke-width="0.5"/>
    <line x1="20" y1="50" x2="40" y2="50" stroke="currentColor" stroke-width="1.5"/>
    <line x1="60" y1="50" x2="80" y2="50" stroke="currentColor" stroke-width="1.5"/>
    <line x1="50" y1="20" x2="50" y2="40" stroke="currentColor" stroke-width="1.5"/>
    <line x1="50" y1="60" x2="50" y2="80" stroke="currentColor" stroke-width="1.5"/>
    <circle cx="50" cy="50" r="2" fill="currentColor"/>
  </g>
</svg>
```
```css
.l1-reticle { transform-origin: center; animation: l1Scan 4s cubic-bezier(0.68, -0.55, 0.265, 1.55) infinite; }
@keyframes l1Scan { 0%, 100% { transform: scale(1) rotate(0deg); } 50% { transform: scale(0.6) rotate(90deg); stroke: #FFF; } }
```

**L2 — Neural Network** (the practice, building connected systems):
```html
<svg class="badge-svg" viewBox="0 0 100 100">
  <path d="M 20 50 L 40 30 L 70 40 L 85 70" stroke="currentColor" stroke-width="1.5" fill="none" opacity="0.3"/>
  <path d="M 20 50 L 40 70 L 70 60 L 85 30" stroke="currentColor" stroke-width="2" fill="none" class="l2-path"/>
  <circle cx="20" cy="50" r="4" fill="currentColor" opacity="0.5"/>
  <circle cx="40" cy="30" r="4" fill="currentColor" opacity="0.5"/>
  <circle cx="70" cy="40" r="4" fill="currentColor" opacity="0.5"/>
  <circle cx="85" cy="70" r="4" fill="currentColor" opacity="0.5"/>
  <circle cx="40" cy="70" r="5" fill="currentColor" class="l2-node" style="animation-delay: 0s;"/>
  <circle cx="70" cy="60" r="5" fill="currentColor" class="l2-node" style="animation-delay: 0.5s;"/>
  <circle cx="85" cy="30" r="5" fill="currentColor" class="l2-node" style="animation-delay: 1s;"/>
</svg>
```
```css
.l2-path { stroke-dasharray: 50; stroke-dashoffset: 50; animation: l2Flow 2s ease-in-out infinite; }
.l2-node { animation: l2Pulse 2s ease-in-out infinite; }
@keyframes l2Flow  { to { stroke-dashoffset: -50; } }
@keyframes l2Pulse { 50% { fill: #FFF; filter: drop-shadow(0 0 5px #FFF); } }
```

**L3 — Isometric Stacked Layers** (architecture, production infrastructure):
```html
<svg class="badge-svg" viewBox="0 0 100 100" style="transform: translateY(5px);">
  <g class="l3-layer-bot"><path d="M 50 60 L 80 75 L 50 90 L 20 75 Z" fill="none" stroke="currentColor" stroke-width="2" opacity="0.3"/></g>
  <g class="l3-layer-mid"><path d="M 50 40 L 80 55 L 50 70 L 20 55 Z" fill="none" stroke="currentColor" stroke-width="2" opacity="0.6"/></g>
  <g class="l3-layer-top"><path d="M 50 20 L 80 35 L 50 50 L 20 35 Z" fill="currentColor" opacity="0.5"/></g>
</svg>
```
```css
.l3-layer-top { animation: l3Float 3s ease-in-out infinite alternate; }
.l3-layer-mid { animation: l3Float 3s ease-in-out infinite alternate 0.5s; }
.l3-layer-bot { animation: l3Float 3s ease-in-out infinite alternate 1s; }
@keyframes l3Float { 0% { transform: translateY(0); } 100% { transform: translateY(-4px); } }
```

**L4 — Anomaly Waveform** (leading edge, unsolved territory — a flat baseline with one spike):
```html
<svg class="badge-svg" viewBox="0 0 100 100">
  <line x1="10" y1="50" x2="90" y2="50" stroke="currentColor" stroke-width="1" opacity="0.3"/>
  <path d="M 10 50 Q 20 50 30 50 T 45 50 T 50 20 T 55 50 T 70 50 T 90 50" fill="none" stroke="currentColor" stroke-width="2" class="l4-wave"/>
  <circle cx="50" cy="20" r="4" class="l4-spike"/>
</svg>
```
```css
.l4-wave  { stroke-dasharray: 200; stroke-dashoffset: 200; animation: l4Sweep 3s linear infinite; }
.l4-spike { opacity: 0; animation: l4Alert 3s linear infinite; }
@keyframes l4Sweep { to { stroke-dashoffset: 0; } }
@keyframes l4Alert { 45%, 55% { opacity: 1; fill: #FFF; } }
```

**Parameter knobs:**
- **`--level-color`** — override per series (Harness series might swap L2 purple for rose)
- **Badge size** — 80px desktop, 60px mobile (already set)
- **Animation timing** — all between 2-4s. Faster feels frantic; slower feels dead.

**Anti-pattern:** Don't invent a 5th metaphor for a 5th level. The 4-level system is the ceiling for mental-model compression. If you have 5 levels, collapse two. Don't swap metaphors across series — the reticle/network/layers/waveform quartet is the brand signature.

**Companion components:** Pairs with `.level-section` + `.topic-grid` layout (see DEEP-DIVE-HUB-TEMPLATE.html lines 189-240). Works inside the Live Trace engine background (#31).

---

### 6.16 Component #33 — Card Laser on Hover

**Purpose:** Horizontal beam of light that shoots across the top edge of a card when hovered. Not a border — a beam. Makes the card feel scanned / activated.

**When to use:** Topic cards on hub pages. Product cards. Any place where hover needs to signal "this is live/interactive" without adding chrome. Max 2 per viewport — more and the eye can't track any of them.

**Cross-medium:** HTML only. Does not translate.

**Structure:**
```html
<a href="..." class="topic-card">
    <div class="card-laser"></div>
    <!-- card contents -->
</a>
```

```css
.topic-card { position: relative; overflow: hidden; }

.card-laser {
    position: absolute;
    top: 0; left: -100%;
    width: 50%; height: 2px;
    background: linear-gradient(90deg, transparent, var(--level-color), #FFF);
    opacity: 0; z-index: 5;
}

.topic-card:hover .card-laser {
    animation: shootLaser 0.8s ease-out forwards;
    opacity: 1;
}

@keyframes shootLaser {
    0%   { left: -50%; }
    100% { left: 150%; }
}
```

**Parameter knobs:**
- **`width: 50%`** — length of the beam. 50% feels right; below 30% reads as a dot; above 70% loses speed.
- **`height: 2px`** — don't exceed 3px. A thicker beam reads as a loading bar, not light.
- **`0.8s ease-out`** — slower than 0.8s feels lazy; faster than 0.5s is imperceptible.
- **Gradient** — `transparent → level-color → #FFF`. The white tip IS the beam effect. Don't reverse it.

**Anti-pattern:** Don't place laser on sides or bottom — the eye expects horizontal top sweep (UI convention from terminal/CRT). Don't loop the animation on non-hover — relentless motion kills focus. Don't use on cards that already have glow or border-color hover transitions — compounding effects cancel each other.

**Companion components:** Pairs with status ring (#34) and `::after` radial glow. The laser is the fast signal; the glow is the sustain.

---

### 6.17 Component #34 — Status Ring Indicator

**Purpose:** 14px micro-ring on each topic card. Empty state = draft. Filled state = published / active. On hover, ring lights up to level color. The card's status is visible at a glance, without labels.

**When to use:** Topic cards, content catalogs, task lists — anywhere the reader wants to scan "what's ready" vs "what's coming." The micro-version of Progressive Disclosure (principle 1.3).

**Cross-medium:** HTML primary. Can translate to Word as a small colored bullet before item titles, or to PPT as a small circle shape in card corners. Loses the hover animation but keeps the information density.

**Structure:**
```html
<div class="topic-num-wrapper">
    <div class="status-ring"></div>
    <span class="topic-num">TOPIC_01</span>
</div>
```

```css
.status-ring {
    width: 14px; height: 14px; border-radius: 50%;
    border: 2px solid rgba(255,255,255,0.1);
    position: relative;
    display: flex; align-items: center; justify-content: center;
}
.status-ring::after {
    content: '';
    width: 6px; height: 6px; border-radius: 50%;
    background: transparent;
    transition: all 0.3s ease;
}

/* Hover state — fills the ring center with level color */
.topic-card:hover .status-ring {
    border-color: var(--level-color);
    box-shadow: 0 0 10px var(--level-color);
}
.topic-card:hover .status-ring::after {
    background: var(--level-color);
}
```

**State variants (not yet in template — add as needed):**
```css
.status-ring.published::after { background: var(--level-color); }      /* Default filled */
.status-ring.updated          { border-color: #F59E0B; }                /* Amber border — "new" */
.status-ring.updated::after   { background: #F59E0B; animation: pulseDot 2s ease-in-out infinite; }
.status-ring.coming           { border-style: dashed; }                 /* Draft/upcoming */

@keyframes pulseDot { 0%, 100% { opacity: 1; } 50% { opacity: 0.4; } }
```

**Parameter knobs:**
- **Ring size** — 14px is the minimum that reads clearly. Do not shrink below 12px.
- **Inner dot size** — 6px inside 14px ring = 43% fill. Don't exceed 50% or it looks like a filled button.
- **Border opacity** — 0.1 at rest is the right whisper. Any brighter and the ring pulls focus from the card title.

**Anti-pattern:** Don't use more than 3 states (published / updated / coming). A 4th state confuses scanning. Don't label the states next to the ring ("Draft", "Published") — that defeats the micro-signal. If you need labels, use a different component.

**Companion components:** Pairs with card laser (#33) — laser fires on hover, ring fills on hover, card elevates on hover. The three combine into a single "activated" moment.

---

### 6.18 Component #35 — Spotlight 3D Tilt Card

**Purpose:** Cards that track the cursor with a subtle 3D rotation AND a soft radial spotlight that follows the mouse position. Two physical cues: the card tilts toward you, and a warm light spot under your cursor. Used for "reading guide" path cards where the reader is making a choice — the tilt rewards exploration.

**When to use:** Navigation / decision cards (path selection, step choices, persona routing). Hero feature tiles. Not for topic grids with 6+ cards — the effect only works when there's room to see each card in full, roughly 2x2 or 1x4 layouts.

**Cross-medium:** HTML only. Requires mouse tracking.

**Structure:**
```html
<div class="guide-grid">
    <div class="guide-card">
        <span class="guide-label">Path 01</span>
        <p class="guide-desc"><strong>New to evals?</strong><br>Start at Level 1, Topic 1.</p>
    </div>
    <!-- more cards -->
</div>
```

```css
.guide-grid {
    display: grid; grid-template-columns: repeat(2, 1fr);
    gap: 2rem; max-width: 1000px; margin: 0 auto;
    perspective: 1000px;                           /* REQUIRED — enables 3D on children */
}

.guide-card {
    background: rgba(255,255,255,0.02);
    border: 1px solid var(--border-dim); border-radius: 16px;
    padding: 3rem;
    display: flex; flex-direction: column; gap: 1rem;
    backdrop-filter: blur(12px);
    position: relative; overflow: hidden;
    transform-style: preserve-3d;                   /* REQUIRED */
    transition: transform 0.1s ease, box-shadow 0.3s ease;
    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    will-change: transform;
}
.guide-card:hover { box-shadow: 0 20px 50px rgba(0,0,0,0.8); border-color: rgba(255,255,255,0.15); }

/* Spotlight — radial gradient following mouse via CSS custom props */
.guide-card::before {
    content: ''; position: absolute; inset: 0;
    background: radial-gradient(800px circle at var(--mouse-x) var(--mouse-y), rgba(255,255,255,0.06), transparent 40%);
    opacity: 0; transition: opacity 0.3s;
    z-index: 0; pointer-events: none;
}
.guide-card:hover::before { opacity: 1; }

/* Lift card contents into 3D — gives depth */
.guide-card > * { position: relative; z-index: 1; transform: translateZ(20px); }
```

**JS — cursor tracking (tilt + spotlight):**
```js
document.querySelectorAll('.guide-card').forEach(card => {
    card.addEventListener('mousemove', e => {
        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;

        // Spotlight follow
        card.style.setProperty('--mouse-x', `${x}px`);
        card.style.setProperty('--mouse-y', `${y}px`);

        // 3D tilt (disable on mobile)
        if (window.innerWidth > 768) {
            const centerX = rect.width / 2;
            const centerY = rect.height / 2;
            const rotateX = ((y - centerY) / centerY) * -4;  // -4 to +4 deg
            const rotateY = ((x - centerX) / centerX) *  4;
            card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.02, 1.02, 1.02)`;
        }
    });
    card.addEventListener('mouseleave', () => {
        if (window.innerWidth > 768) {
            card.style.transform = `perspective(1000px) rotateX(0) rotateY(0) scale3d(1, 1, 1)`;
        }
    });
});

/* Mobile — disable transform entirely */
@media (max-width: 768px) { .guide-card { transform: none !important; } }
```

**Parameter knobs:**
- **Tilt range `±4deg`** — the limit of "subtle." Above 6deg it feels like a toy, not a document.
- **Scale on hover `1.02`** — just enough to signal elevation. 1.05 is too much.
- **Spotlight radius `800px`** — wider than the card, so the highlight feels like ambient light, not a flashlight.
- **Spotlight opacity `0.06`** — whisper. Anything brighter reads as a glare.
- **`translateZ(20px)`** — content lifts out of card surface. 20px is the sweet spot; below 10px the depth is imperceptible.

**Anti-pattern:** Don't combine with card laser (#33) on the same card — too many simultaneous hover effects. Don't use on mobile — touch devices have no hover, and mousemove-style tilt is a cognitive load on scroll. Don't set `perspective` on the card itself — it must be on the parent grid, or all children tilt on their own axis.

**Performance note:** The `mousemove` listener fires continuously on hover. If the page has 8+ spotlight tilt cards, throttle with `requestAnimationFrame` or the main thread chokes on scroll. For typical hub pages (4 cards in the reading guide), no throttling needed.

**Companion components:** Pairs with glass-blur backgrounds and guide labels. Best on dark surfaces (`#030407`) where the spotlight effect has room to breathe.

---

### 7.1 Easing
```css
--ease-cinematic: cubic-bezier(0.16, 1, 0.3, 1);        /* Apple deceleration */
--ease-spring:    cubic-bezier(0.175, 0.885, 0.32, 1.1); /* Spring overshoot */
```

### 7.2 V8 Keyframes (New)
```css
@keyframes floatIso { 0%, 100% { transform: translateZ(var(--tz)); } 50% { transform: translateZ(calc(var(--tz) + 12px)); } }

@keyframes dataStream {
    0% { top: -10%; opacity: 0; transform: scaleY(0.8); }
    15% { opacity: 1; transform: scaleY(1.5); }
    85% { opacity: 1; transform: scaleY(1.5); }
    100% { top: 110%; opacity: 0; transform: scaleY(0.8); }
}

@keyframes pulseBeam {
    0%, 100% { opacity: 0.7; box-shadow: 0 0 15px var(--color-env), 0 0 30px rgba(6,182,212,0.5); }
    50% { opacity: 1; box-shadow: 0 0 30px var(--color-env), 0 0 60px rgba(6,182,212,0.9); }
}

@keyframes drawBridge { to { stroke-dashoffset: 0; } }
```

### 7.3 Existing Keyframes (Preserved)
- `blurReveal` (1.2s entry — hero content)
- `palankiReveal` (1.5s — name letter-spacing squeeze)
- `pulseCyan` (4s infinite — PALANKI ghost pulse)
- `drawLine` (1s — cyan underline scaleX)
- `scaleYIn` (1s — editorial cyan vertical line)
- `enginePulse` (0.4s alternate — rocket flame, article pages)
- `noiseShift` (8s steps — ambient noise drift, article pages)
- `slowZoom` (30s alternate — hero bg Ken Burns, article pages)

### 7.4 Scroll-Driven & Interactive (JS)
- **Lenis smooth scroll** — V8 baseline (`@studio-freight/lenis@1.0.42`)
- **`.reveal-up` / `.reveal-lines`** — IntersectionObserver 0.1 threshold, -10% rootMargin
- **Scramble counter** — 1.2s random scramble then lock
- **Scroll-written quote** — word-by-word illumination by scroll %
- **Recession stacking** — GPU-accelerated `translate3d + scale` on path cards
- **3D pop reveal** — browser-frame rotates in from 15deg
- **Nav tightening** — scroll >50px: padding 1.5rem → 1rem, bg solid
- **Magnetic buttons** — (article pages) button 0.15x + content 0.08x cursor offset

### 7.5 Rule
No other animations. No parallax on body content. No spinner loaders. No auto-playing hero videos. No animation libraries beyond Lenis (smooth scroll only).

---

## 8. Multi-Medium Application

### 8.1 Website (HTML) — Primary Canvas
- Reference files: `homepage-final.html`, `BLOG-POST-TEMPLATE.html`
- Dark theme default. Article reading pages are the only light-mode surfaces.

### 8.2 Gamma Presentations — Dark Theme Default
- **Theme setup:** Load 4 Google Fonts. Set dark mode. Background `#030407`.
- **Slide structure:**
  - Title slide → giant Inter 900 + Instrument Serif italic subtitle + frosted badges + bridge SVG as decoration
  - Section divider → hollow-stroke number + eyebrow label
  - Content slide → one headline + one visual or three max bullets. Never six bullets.
  - KPI slide → telemetry grid framing: "METRIC_01 [UNIT]" + value + label
  - Quote slide → Instrument Serif 4vw, cavernous padding, hand-drawn highlight on key phrase
  - Closer → product signature ("Crafted with intent by *Ravi Teja Palanki*")
- **Animations:** Scroll-linked reveals only. No auto-play, no bounce.

### 8.3 PowerPoint — Dark Theme Default
- **Master slide:** `#030407` background, Inter/Instrument Serif/JetBrains Mono/Newsreader loaded
- **Section transitions:** Morph or Fade (0.6s). Never Bounce, Dissolve, Wipe, or any "flashy" transition.
- **Color palette:** Only the 4 identity colors as accents. Never flat color backgrounds.
- **Typography rule:** Inter 900 for titles (uppercase, -0.03em tracking). Newsreader for body. Mono for metadata. Instrument Serif italic for quotes and editorial moments.
- **Signature elements:** Every deck includes bridge SVG (as a decorative header) + frosted glass badges on the title slide + product signature closer.

### 8.4 Word Documents — Light Theme Default
- **Paper:** `#FCFDFD` background. Never pure white.
- **Document styles:**
  - Heading 1 → Inter 900, `clamp(2.5rem, ..., 4rem)`, uppercase, -0.03em tracking, `#111318`
  - Heading 2 → Instrument Serif 400, 2.8rem, `#111318`
  - Body → Newsreader 400, 1.2rem, line-height 1.7, `#202226`
  - Meta / captions → JetBrains Mono 700, 0.75rem, uppercase, 0.15em tracking, `#5A5D67`
  - Blockquote → Instrument Serif italic, left border 4px in `--color-model`
  - Code block → JetBrains Mono on `#F8F7F4` (cream)
- **Accent use:** Purple left borders for callouts. Red borders ONLY for warnings.
- **Signature:** Every document closes with "Ravi Teja Palanki" in Instrument Serif.

### 8.5 Diagrams (Excalidraw / SVG)
- Use Excalidraw hand-drawn aesthetic for harness series
- Use the V8 blueprint aesthetic (dot grid bg, dark def-box, VS circle) for concept diagrams
- See `excalidraw-svg` skill for drawing rules; this skill supplies the color palette

---

## 9. Page Recipes

### 9.1 Homepage (V8 — `/`)
1. Dark canvas (`#030407`) + noise overlay + ambient glow
2. Nav: fixed, Newsreader italic brand, 3 nav items + white CTA pill
3. **Hero** (grid 1.15fr/0.85fr):
   - Left: "RAVI TEJA / PALANKI" (palankiReveal + pulseCyan ghost) + editorial block with suspension bridge SVG under "The Bridger." + line-draw emphasis words + frosted badges
   - Right: 3D isometric stack (STRATEGY/PRODUCT/ENGINEERING/DELIVERY with floatIso) + core beam + 3 data packets
4. **The Bridger** — sticky card stack (3 frosted glass cards with identity gradients)
5. **Telemetry** — 4-box dashboard grid with "METRIC_NN [UNIT]" headers and scramble counters
6. **The Why** — word-by-word scroll-written quote + hand-drawn purple-to-rose highlight + CTA
7. **Two Paths** — premium glass cards with 40px rounded-top edge, recession stacking
8. **Article teaser** — 3D pop browser frame with neon highlight
9. **Footer** — product signature

### 9.2 Profile (`/profile`)
See `lovable/04-PROFILE-PAGE-SPEC.md`. Uses folder-card 3D tilt for product cards (sequential, not sticky).

### 9.3 Writing Landing (`/writing`)
7 sections: hero → architecture (sticky cards) → anti-patterns → deep dives (recession) → quote → reading transition → archive. See `production-landing.html`.

### 9.4 Series Hub (`/writing/{evals,agentic-stack,harness-engineering}`)
Dark throughout. Series hero + level sections + reading guide + CTA. Harness variant uses sequential 8-episode layout.

### 9.5 Article Reading Page
Canonical template: `BLOG-POST-TEMPLATE.html`. Rocket progress bar, paper canvas overlay, learning objectives, body sections, mistake/spec/blueprint diagrams, up next, back nav, footer signature. Per-series accent override.

---

## 10. Responsive Breakpoints

### `@media (max-height: 850px) and (min-width: 1025px)` — Short desktops
Compacts hero: padding 6rem, title 5.5rem, italic-serif 3.2rem, viz scaled 0.85x.

### `@media (max-width: 1024px)` — Tablet
Hero collapses to single column (text-align center). Chasm viz scales to 0.8. Telemetry 2 cols. Nav links hide. Path heroes lose sticky and rounded corners.

### `@media (max-width: 768px)` — Mobile
Nav brand 1.2rem. Chasm 0.65 scale. Telemetry 1 col. Quote font 1.8rem. Hand-drawn highlight allows wrap. Signature stacks.

### Mobile Checklist
- [ ] `document.body.scrollWidth === window.innerWidth` (no horizontal overflow)
- [ ] Touch targets ≥ 44×44px
- [ ] Magnetic button physics disabled (<768px)
- [ ] 3D tilt disabled (<1024px)
- [ ] Smooth-scroll touchMultiplier 2 (Lenis config)
- [ ] `clamp()` on every text size
- [ ] `overflow-wrap: break-word` on display titles

---

## 11. Readability Rules (Non-Negotiable Across All Mediums)

1. Minimum body size 1.15rem (HTML/Gamma) / 11pt (PPT/Word)
2. Minimum font-weight 400 on dark
3. WCAG AA minimum (4.5:1), AAA target (7:1) for main body
4. Maximum line length 660px (65–75 chars)
5. Line-height ≥ 1.7 for Newsreader body
6. Touch targets ≥ 44×44 on mobile
7. No pure black on pure white (use `#111318` on `#FCFDFD`)
8. No text below 0.65rem
9. Display titles get `overflow-wrap: break-word; hyphens: auto; max-width: 100%`

---

## 12. What This Skill Does NOT Cover

- **Content voice** — see `ravi-thinking-skills`
- **Article editorial structure** — see `rtp-deep-dive-writer`
- **Lovable-specific build** — see `1_Projects/my-personal-website/lovable/` specs
- **Diagram content (per-article specs)** — see series-specific `SVG-VISUAL-PLAN.md` files
- **Profile deep content** — see `lovable/04-PROFILE-PAGE-SPEC.md`
- **Content map** — see `lovable/09-CONTENT-MAP.md`

---

## 13. Canonical References

| Artifact | Path |
|----------|------|
| Homepage (V8, canonical) | `1_Projects/my-personal-website/prototype/homepage-final.html` |
| Blog post template (gold standard) | `1_Projects/my-personal-website/reference/BLOG-POST-TEMPLATE.html` |
| Deep-dive hub template (gold standard — v2.1 source) | `1_Projects/my-personal-website/reference/DEEP-DIVE-HUB-TEMPLATE.html` |
| Writing landing (production) | `1_Projects/my-personal-website/reference/production-landing.html` |
| Article transform script | `1_Projects/my-personal-website/scripts/apply-gold-template.py` |
| Lovable specs (11 files + harness) | `1_Projects/my-personal-website/lovable/` |

**When in doubt, the canonical HTML files win over any written description.**

---

## 14. Version History

| Version | Date | Change |
|---------|------|--------|
| 2.1 | 17 APR 2026 | Added 5 components from `DEEP-DIVE-HUB-TEMPLATE.html` — #31 Live Trace observability engine (animated SVG background simulating spans + evals), #32 per-level semantic animated SVG badges (L1 reticle / L2 neural network / L3 isometric layers / L4 anomaly waveform), #33 card laser on hover (beam shoot across top edge), #34 status ring indicator (14px ring micro-signal for card state), #35 spotlight 3D tilt card (cursor-tracked radial gradient + subtle rotateX/Y). Updated Creative Principles 1.2 (added hub page signatures) and 1.3 (status rings as micro-disclosure). Added `DEEP-DIVE-HUB-TEMPLATE.html` to canonical references. |
| 2.0 | 17 APR 2026 | V8 upgrade — suspension bridge SVG, data packet stream, scramble counter dashboard, scroll-written quote, hand-drawn purple-to-rose highlight, 3D pop browser frame, premium glass cards with 40px rounded-top, floating iso planes, product-signature footer, Lenis smooth scroll. Added Design Philosophy (9 creative principles) + multi-medium guidance (HTML/Gamma/PPT/Word). |
| 1.0 | 17 APR 2026 | Initial unified skill superseding learn-site-design v2.0 |
| — (learn-site-design v2.0) | 15 APR 2026 | Expanded to full ravitejapalanki.com (deprecated) |
| — (learn-site-design v1.0) | 12 APR 2026 | learn subdomain only (deprecated) |
