---
name: rtp-cinematic-presentations
description: |
  World-class cinematic HTML/React presentation system based on The Aureate Codex v8 design system. Use when creating: (1) HTML slide decks or presentations, (2) React/JSX presentation artifacts, (3) Pitch decks, keynotes, or investor presentations, (4) Masterclass or course content, (5) Product launches with cinematic feel, (6) Any multi-slide visual content requiring premium dark aesthetics. Provides 20+ slide templates, exact CSS with gold/teal/purple accent system, scroll-snap navigation, data-reveal animation system, glassmorphism components, and production-tested responsive scaling. Features ambient glow effects, mesh gradients, pulsing labels, and framework diagrams.
---

# Cinematic Presentations Skill

> *"The goal is not to impress. The goal is to communicate with such clarity and beauty that the design becomes invisible."*

A world-class presentation system based on The Aureate Codex v8. Production-tested on masterclass content.

---

## The Three Absolutes

### 1. READABILITY IS SACRED
- Headlines: minimum 36px (mobile), 48px+ (desktop)
- Body text: minimum 16px (mobile), 18px+ (desktop)
- Contrast ratio: 7:1 minimum for primary text
- Line height: 1.65+ for body text

### 2. RESTRAINT SIGNALS MASTERY
Gold appears **maximum 3× per slide**:
- Frame label or badge
- One key data point OR emphasized word
- CTA button (if present)

Teal and Purple are supporting accents — use sparingly for categorization.

### 3. DARKNESS HAS DIMENSION
Never use pure black (#000000). Layer backgrounds with subtle depth:
- `--void: #020202` (deepest)
- `--codex: #060606` (primary background)
- `--velvet: #0A0A0A` (elevated surfaces)
- `--dusk: #101010` (cards, inputs)

---

## Quick Start: Complete HTML Boilerplate

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>Presentation Title | Ravi Teja Palanki</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400;1,500&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <style>/* CSS from references/complete-css.md */</style>
</head>
<body>
  <!-- Progress Bar -->
  <div class="progress"><div class="progress__bar" id="progress"></div></div>
  
  <!-- Navigation -->
  <nav class="nav">
    <button class="nav__btn" id="prevBtn">←</button>
    <div class="nav__counter"><span class="current" id="currentSlide">1</span> / <span id="totalSlides">--</span></div>
    <button class="nav__btn" id="nextBtn">→</button>
  </nav>
  
  <!-- Slides -->
  <section class="slide" id="slide-1">...</section>
  
  <script>/* JS from references/navigation-js.md */</script>
</body>
</html>
```

---

## Essential CSS Variables

```css
:root {
  /* ═══════════════════════════════════════════
     DEPTH PALETTE — The Void
     ═══════════════════════════════════════════ */
  --void: #020202;      /* Deepest - never go darker */
  --codex: #060606;     /* Primary slide background */
  --velvet: #0A0A0A;    /* Elevated surfaces */
  --dusk: #101010;      /* Cards, inputs */
  --twilight: #161616;  /* Higher elevation */
  --mist: #1E1E1E;      /* Modals, overlays */
  --ash: #2A2A2A;       /* Borders, subtle */
  --slate: #404040;     /* Disabled states */

  /* ═══════════════════════════════════════════
     TEXT PALETTE — The Illumination
     ═══════════════════════════════════════════ */
  --white: #FFFFFF;     /* Pure white (use sparingly) */
  --parchment: #FAFAF9; /* Headlines, CTAs */
  --ivory: #F5F4F2;     /* Body text */
  --cream: #E8E7E5;     /* Secondary text */
  --stone: #B8B7B5;     /* Captions, metadata */
  --dust: #8A8988;      /* Disabled, watermarks */

  /* ═══════════════════════════════════════════
     GOLD TREASURY — Primary Brand
     ═══════════════════════════════════════════ */
  --gold-deep: #8B6914;   /* Shadows, pressed */
  --gold: #D4A726;        /* THE primary gold */
  --gold-bright: #F0C94C; /* Hover, emphasis */
  --gold-pale: #FBE98A;   /* Glows, highlights */
  --gold-glow: rgba(212, 167, 38, 0.15);

  /* ═══════════════════════════════════════════
     TEAL ACCENT — Technology/Progress
     ═══════════════════════════════════════════ */
  --teal: #2DD4BF;        /* Primary teal */
  --teal-bright: #5EEAD4; /* Hover, emphasis */
  --teal-deep: #14B8A6;   /* Pressed states */
  --teal-glow: rgba(45, 212, 191, 0.12);

  /* ═══════════════════════════════════════════
     PURPLE ACCENT — Depth/Premium
     ═══════════════════════════════════════════ */
  --purple: #8B5CF6;        /* Primary purple */
  --purple-bright: #A78BFA; /* Hover, emphasis */
  --purple-deep: #7C3AED;   /* Pressed states */
  --purple-glow: rgba(139, 92, 246, 0.10);

  /* ═══════════════════════════════════════════
     STATUS COLORS
     ═══════════════════════════════════════════ */
  --success: #4ADE80;
  --danger: #F87171;
  --warning: #FBBF24;

  /* ═══════════════════════════════════════════
     TYPOGRAPHY
     ═══════════════════════════════════════════ */
  --font-display: 'Cormorant Garamond', Georgia, serif;
  --font-body: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  --font-mono: 'JetBrains Mono', 'Fira Code', monospace;

  /* ═══════════════════════════════════════════
     GLASSMORPHISM
     ═══════════════════════════════════════════ */
  --glass-bg: rgba(16, 16, 16, 0.75);
  --glass-border: rgba(255, 255, 255, 0.08);
  --glass-blur: 24px;

  /* ═══════════════════════════════════════════
     ANIMATION
     ═══════════════════════════════════════════ */
  --ease: cubic-bezier(0.16, 1, 0.3, 1);
  --ease-out: cubic-bezier(0.33, 1, 0.68, 1);
  --ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1);
}
```

---

## Typography Scale (Fluid with clamp())

| Class | Size | Font | Use |
|-------|------|------|-----|
| `.display` | clamp(52px, 10vw, 110px) | Cormorant 300 | Hero titles |
| `.h1` | clamp(36px, 5vw, 60px) | Cormorant 400 | Section titles |
| `.h2` | clamp(28px, 3.5vw, 44px) | Cormorant 500 | Slide headers |
| `.h3` | clamp(22px, 2.5vw, 32px) | Cormorant 500 | Card titles |
| `.h4` | clamp(18px, 1.8vw, 24px) | Cormorant 600 | Subheads |
| `.lead` | clamp(17px, 1.4vw, 20px) | Inter 400 | Intro text |
| `.body` | clamp(16px, 1.1vw, 18px) | Inter 400 | Body text |
| `.caption` | clamp(13px, 0.9vw, 15px) | Inter 400 | Metadata |
| `.stat` | clamp(64px, 12vw, 130px) | JetBrains 700 | Big numbers |

---

## The Label System (Pulsing Teal Badge)

The signature label with animated pulse dot:

```css
.label {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--teal);
  padding: 8px 16px;
  background: var(--teal-glow);
  border: 1px solid rgba(45, 212, 191, 0.25);
  border-radius: 24px;
  margin-bottom: 20px;
}

.label::before {
  content: '';
  width: 8px;
  height: 8px;
  background: var(--teal);
  border-radius: 50%;
  animation: pulse 2s ease-in-out infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 1; transform: scale(1); }
  50% { opacity: 0.4; transform: scale(0.7); }
}
```

---

## The data-reveal Animation System

The production-tested reveal system using Intersection Observer:

```css
[data-reveal] {
  opacity: 0;
  transition: opacity 650ms var(--ease), transform 650ms var(--ease);
}

[data-reveal="up"] { transform: translateY(35px); }
[data-reveal="down"] { transform: translateY(-25px); }
[data-reveal="left"] { transform: translateX(35px); }
[data-reveal="right"] { transform: translateX(-35px); }
[data-reveal="scale"] { transform: scale(0.95); }
[data-reveal="fade"] { transform: none; }

[data-reveal].visible {
  opacity: 1;
  transform: none;
}

/* Stagger delays */
[data-delay="100"] { transition-delay: 100ms; }
[data-delay="200"] { transition-delay: 200ms; }
[data-delay="300"] { transition-delay: 300ms; }
[data-delay="400"] { transition-delay: 400ms; }
[data-delay="500"] { transition-delay: 500ms; }
[data-delay="600"] { transition-delay: 600ms; }
[data-delay="700"] { transition-delay: 700ms; }
[data-delay="800"] { transition-delay: 800ms; }
```

### Usage
```html
<h2 class="h1" data-reveal="up">Title</h2>
<p class="lead" data-reveal="up" data-delay="100">Subtitle</p>
<div class="card" data-reveal="up" data-delay="200">Content</div>
```

---

## Progress Bar (Tri-Color Gradient)

```css
.progress {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: rgba(255, 255, 255, 0.03);
  z-index: 9999;
}

.progress__bar {
  height: 100%;
  background: linear-gradient(90deg, var(--purple), var(--teal), var(--gold));
  width: 0%;
  transition: width 100ms linear;
}
```

---

## Ambient Glow Effects

```css
.glow {
  position: absolute;
  border-radius: 50%;
  filter: blur(100px);
  pointer-events: none;
  z-index: 1;
  opacity: 0.6;
}

.glow--gold { 
  background: radial-gradient(circle, rgba(212, 167, 38, 0.25) 0%, transparent 70%); 
}
.glow--teal { 
  background: radial-gradient(circle, rgba(45, 212, 191, 0.18) 0%, transparent 70%); 
}
.glow--purple { 
  background: radial-gradient(circle, rgba(139, 92, 246, 0.15) 0%, transparent 70%); 
}
```

### Usage
```html
<div class="glow glow--gold" style="width: 500px; height: 500px; top: 20%; right: -100px;"></div>
```

---

## 20+ Slide Templates

### See [references/slide-templates.md](references/slide-templates.md) for complete HTML

1. **Cover Slide** — Hero with mesh gradient animation
2. **Section Divider** — Module number + title
3. **Statement Slide** — Single big idea
4. **Two-Column Split** — Text + visual
5. **Three-Column Grid** — Features/pillars
6. **Data/Stats Slide** — Big numbers with glow
7. **Quote Slide** — Attributed quote with bordeaux border
8. **Compare Cards** — Before/After with danger/success
9. **Timeline Slide** — Vertical gold spine
10. **Scaffold/Pyramid** — Layer diagram (gold/teal/purple)
11. **Mnemonic Slide** — Framework acronym rows
12. **Loop Diagram** — 3C loop boxes with arrows
13. **Context Window** — Code block visualization
14. **Checklist Slide** — Actionable items
15. **Profile Cards** — Credential/journey cards
16. **Gallery Grid** — Image showcase
17. **Takeaway Box** — Gold emphasis callout
18. **Pricing Tabs** — Tabbed pricing display
19. **CTA Slide** — Call-to-action with buttons
20. **Closing Slide** — Thank you + pyramid + links

---

## Core Components

### Card System

```css
.card {
  background: linear-gradient(145deg, rgba(30, 30, 30, 0.9) 0%, rgba(22, 22, 22, 0.95) 100%);
  border: 1px solid rgba(255, 255, 255, 0.06);
  border-radius: 16px;
  padding: 28px;
  transition: all 300ms var(--ease);
}

.card:hover {
  transform: translateY(-4px);
  border-color: rgba(255, 255, 255, 0.1);
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.3);
}

.card--gold {
  border-color: rgba(212, 167, 38, 0.15);
  background: linear-gradient(145deg, rgba(212, 167, 38, 0.05) 0%, rgba(22, 22, 22, 0.95) 100%);
}

.card--teal {
  border-color: rgba(45, 212, 191, 0.15);
  background: linear-gradient(145deg, rgba(45, 212, 191, 0.05) 0%, rgba(22, 22, 22, 0.95) 100%);
}

.card--purple {
  border-color: rgba(139, 92, 246, 0.15);
  background: linear-gradient(145deg, rgba(139, 92, 246, 0.05) 0%, rgba(22, 22, 22, 0.95) 100%);
}
```

### Glassmorphism Navigation

```css
.nav {
  position: fixed;
  top: 20px;
  right: 20px;
  display: flex;
  align-items: center;
  gap: 4px;
  z-index: 1000;
  background: var(--glass-bg);
  backdrop-filter: blur(var(--glass-blur));
  -webkit-backdrop-filter: blur(var(--glass-blur));
  padding: 6px;
  border-radius: 50px;
  border: 1px solid var(--glass-border);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5);
}

.nav__btn {
  width: 40px;
  height: 40px;
  background: transparent;
  border: none;
  border-radius: 50%;
  color: var(--stone);
  cursor: pointer;
  transition: all 200ms var(--ease);
}

.nav__btn:hover {
  background: var(--gold-glow);
  color: var(--gold);
}

.nav__counter {
  font-family: var(--font-mono);
  font-size: 14px;
  color: var(--dust);
}

.nav__counter .current {
  color: var(--teal-bright);
}
```

### Takeaway Box

```css
.takeaway {
  padding: 24px;
  background: linear-gradient(135deg, rgba(212, 167, 38, 0.05) 0%, transparent 100%);
  border-left: 3px solid var(--gold);
  border-radius: 0 14px 14px 0;
}

.takeaway p {
  font-size: 16px;
  line-height: 1.75;
  color: var(--ivory);
}

.takeaway em {
  color: var(--gold-bright);
  font-style: normal;
}
```

### Compare Cards (Before/After)

```css
.compare-card--before {
  background: linear-gradient(135deg, rgba(248, 113, 113, 0.06) 0%, var(--dusk) 100%);
  border: 1px solid rgba(248, 113, 113, 0.12);
}

.compare-card--after {
  background: linear-gradient(135deg, rgba(74, 222, 128, 0.06) 0%, var(--dusk) 100%);
  border: 1px solid rgba(74, 222, 128, 0.12);
}
```

### Scaffold/Pyramid Layers

```css
.scaffold__layer--1 {
  background: linear-gradient(135deg, rgba(212, 167, 38, 0.1) 0%, rgba(212, 167, 38, 0.03) 100%);
  border: 1px solid rgba(212, 167, 38, 0.2);
  max-width: 520px; /* Narrowest - top */
}

.scaffold__layer--2 {
  background: linear-gradient(135deg, rgba(45, 212, 191, 0.08) 0%, rgba(45, 212, 191, 0.02) 100%);
  border: 1px solid rgba(45, 212, 191, 0.15);
  max-width: 620px; /* Middle */
}

.scaffold__layer--3 {
  background: linear-gradient(135deg, rgba(139, 92, 246, 0.08) 0%, rgba(139, 92, 246, 0.02) 100%);
  border: 1px solid rgba(139, 92, 246, 0.15);
  max-width: 720px; /* Widest - bottom */
}
```

---

## Cover Slide Animation

The hero slide with animated mesh gradient:

```css
.cover__mesh {
  position: absolute;
  inset: 0;
  background: 
    radial-gradient(ellipse 80% 60% at 30% 20%, rgba(212, 167, 38, 0.08) 0%, transparent 50%),
    radial-gradient(ellipse 60% 50% at 70% 80%, rgba(45, 212, 191, 0.06) 0%, transparent 40%),
    radial-gradient(ellipse 50% 40% at 50% 50%, rgba(139, 92, 246, 0.05) 0%, transparent 40%);
  animation: meshMove 25s ease-in-out infinite alternate;
}

@keyframes meshMove {
  0% { transform: scale(1) rotate(0deg); opacity: 0.7; }
  100% { transform: scale(1.1) rotate(3deg); opacity: 1; }
}

.cover__grid {
  position: absolute;
  inset: 0;
  background-image: 
    linear-gradient(rgba(212, 167, 38, 0.03) 1px, transparent 1px),
    linear-gradient(90deg, rgba(212, 167, 38, 0.03) 1px, transparent 1px);
  background-size: 60px 60px;
  animation: gridPulse 8s ease-in-out infinite;
}

@keyframes gridPulse {
  0%, 100% { opacity: 0.3; }
  50% { opacity: 0.6; }
}
```

---

## Reference Files

| Task | Reference |
|------|-----------|
| Complete CSS with all variables | [references/complete-css.md](references/complete-css.md) |
| All 20+ slide template HTML | [references/slide-templates.md](references/slide-templates.md) |
| Full component library | [references/components.md](references/components.md) |
| JavaScript navigation system | [references/navigation-js.md](references/navigation-js.md) |
| React implementation | [references/react-components.md](references/react-components.md) |
| Special diagrams & visualizations | [references/diagrams.md](references/diagrams.md) |

---

## Validation Checklist

### Visual
- [ ] No pure black (#000000) — use `--void: #020202`
- [ ] Gold appears ≤3× per slide
- [ ] Headlines use Cormorant Garamond
- [ ] Body text uses Inter
- [ ] Code/numbers use JetBrains Mono
- [ ] Contrast ratio ≥7:1 for text

### Animation
- [ ] Using `data-reveal` system
- [ ] Stagger delays 100ms apart
- [ ] `prefers-reduced-motion` respected
- [ ] No animation >1s duration

### Layout
- [ ] Scroll-snap enabled on desktop
- [ ] Scroll-snap disabled on mobile (<768px)
- [ ] Progress bar visible
- [ ] Navigation accessible

### Brand
- [ ] Teal used for labels/progress
- [ ] Gold used for emphasis/CTAs
- [ ] Purple used for depth/foundation layers
- [ ] Footer attribution present

---

## The Ultimate Test

1. **Can every word be read instantly?** If not, increase size/contrast.
2. **Does gold mark only what matters most?** If overused, reduce.
3. **Does the animation serve the narrative?** If decorative, remove.
4. **Would this feel appropriate in a TED talk?** If not, refine.
5. **Does it feel inevitable?** As if no other treatment was possible?
