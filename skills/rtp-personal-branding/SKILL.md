---
name: ravi-personal-branding
version: 2.0
description: Ravi Teja Palanki's complete design system for every visual surface — website (ravitejapalanki.com), presentations (Gamma, PowerPoint), documents (Word), diagrams, article pages. Dark + light themes properly separated. Nine creative principles that govern every choice. V2.0 incorporates V8 homepage patterns: suspension bridge SVG, data packet stream, scramble counters, scroll-written quote, hand-drawn highlight, 3D pop browser frame, premium glass cards, floating iso planes, and the product-signature footer.
author: Ravi Teja Palanki
created: 17 April 2026
updated: 17 April 2026 (v2.0 — V8 upgrade + multi-medium + creative principles)
supersedes: learn-site-design (v2.0), ravi-personal-branding (v1.0)
---

# Ravi Personal Branding — v2.0

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
- Footer: "Crafted with intent by Ravi Teja Palanki" signature

*Cross-medium:* Every slide deck section needs ONE signature visual. Every Word doc section gets ONE editorial moment (blockquote, pullquote, or custom SVG).

### 1.3 Progressive Disclosure Through Scroll Position
Quote illuminates word-by-word based on scroll %. Cards slide as physical objects during recession stacking. Line-draw underlines stagger at 0.4s, 0.8s, 1.2s. The reader sets the pace.

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

## 7. Animation System — Canonical Keyframes

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
| Writing landing (production) | `1_Projects/my-personal-website/reference/production-landing.html` |
| Article transform script | `1_Projects/my-personal-website/scripts/apply-gold-template.py` |
| Lovable specs (11 files + harness) | `1_Projects/my-personal-website/lovable/` |

**When in doubt, the canonical HTML files win over any written description.**

---

## 14. Version History

| Version | Date | Change |
|---------|------|--------|
| 2.0 | 17 APR 2026 | V8 upgrade — suspension bridge SVG, data packet stream, scramble counter dashboard, scroll-written quote, hand-drawn purple-to-rose highlight, 3D pop browser frame, premium glass cards with 40px rounded-top, floating iso planes, product-signature footer, Lenis smooth scroll. Added Design Philosophy (9 creative principles) + multi-medium guidance (HTML/Gamma/PPT/Word). |
| 1.0 | 17 APR 2026 | Initial unified skill superseding learn-site-design v2.0 |
| — (learn-site-design v2.0) | 15 APR 2026 | Expanded to full ravitejapalanki.com (deprecated) |
| — (learn-site-design v1.0) | 12 APR 2026 | learn subdomain only (deprecated) |
