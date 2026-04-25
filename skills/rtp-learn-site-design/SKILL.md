---
name: rtp-learn-site-design
version: 2.0
description: Codified design language for ravitejapalanki.com — the full design system for the personal homepage, dark cinematic landing pages, editorial article pages, and interactive topic hubs. Covers the homepage (gateway), profile page, and writing section. A sub-skill of the UX Design agent.
author: Ravi Teja Palanki
created: 12 April 2026
updated: 15 April 2026
format: skill-definition
status: active
---

# Ravi's Personal Website Design Language

The complete design system for ravitejapalanki.com — all three sections: homepage (the gateway), profile (digital resume), and writing hub (working notes). This skill encodes every visual decision, every animation technique, every typographic rule, and every interaction pattern — learned from building the "AI Production Chasm" landing page, the personal homepage, and the "Benchmarks vs. Evals" article page.

**When to activate:** Any time the task involves building, extending, or modifying pages for ravitejapalanki.com, or when Ravi asks for "the site style" on any project. This skill is the UX Design agent's sub-specialist for Ravi's personal website ecosystem.

**Site architecture:**
```
ravitejapalanki.com/                          → Homepage (the gateway)
ravitejapalanki.com/profile                   → Digital resume
ravitejapalanki.com/writing                   → Writing hub landing
ravitejapalanki.com/writing/evals             → AI Evals series hub
ravitejapalanki.com/writing/evals/:slug       → Individual eval article
ravitejapalanki.com/writing/agentic-stack     → Agentic Stack series hub
ravitejapalanki.com/writing/agentic-stack/:slug → Individual agentic article
```

**Canonical reference HTML:** `1_Projects/my-personal-website/prototype/homepage-final.html`

---

## 1. The Identity System — 4 Colors, 4 Fonts, 1 Philosophy

### The 4 Architecture Colors

Every color maps to a component of the "AI Production Chasm" framework. They are not decorative — they carry meaning.

| Name | Hex | Role | Where It Appears |
|------|-----|------|------------------|
| **Model** | `#9D4EDD` | The intelligence layer | Level badges, article callouts, drop caps, progress bars, topic pills |
| **Harness** | `#F43F5E` | Guardrails, anti-patterns, mistakes | Warning cards, "Common Mistake" labels, red left borders, severity badges |
| **Tools** | `#F59E0B` | Capabilities, APIs, instruments | Tool-related content, L3 level badges, amber deep dive gradients |
| **Environment** | `#06B6D4` | Deployment context, hero accent | Hero cyan line, "CHASM" hollow stroke, nav credential, highlight text |

**Additional functional colors:**
- Success/pass: `#10B981` (emerald) — pass badges, expected-behavior boxes
- Info callout: `#EFF6FF` bg, `#1E3A8A` text, `#3B82F6` accent

**Color rules (never break):**
- These 4 colors appear ONLY as accents: borders, glows, text highlights, small fills. Never as flat background fills.
- Red is EXCLUSIVELY for anti-patterns, mistakes, and warnings. Never positive.
- On dark backgrounds, colors appear as: border accents, text-shadow glows, radial gradient overlays at 6-15% opacity.
- On white backgrounds, colors appear as: border-left accents, tinted backgrounds at 4-12% opacity, text color.

### The 4 Fonts

| Font | CSS Variable | Role | Weights |
|------|-------------|------|---------|
| **Inter** | `--font-sans` | Display titles (900), UI labels, headings | 300-900 |
| **Instrument Serif** | `--font-display` | Editorial moments, hero titles, article H2s, quotes, drop caps, signatures | 400, 400i |
| **Newsreader** | `--font-body` | Long-form article body text (reading pages only) | 200-800, variable |
| **JetBrains Mono** | `--font-mono` | Labels, tags, badges, metadata, code, eyebrows | 400, 500, 700, 800 |

**Typography rules:**
- Inter 900 ONLY for display titles (uppercase, letter-spacing -0.03em, line-height 0.95)
- Instrument Serif NEVER for body text. Only for: hero titles, article section H2s, massive quotes, drop caps, card titles, signatures.
- Newsreader ONLY on article reading pages. Landing page and topic hubs use Inter for body.
- JetBrains Mono for ALL labels, tags, and metadata. Font-weight 700-800, uppercase, letter-spacing 0.15em.

---

## 2. The Dark Canvas — Landing Page & Topic Hub Foundation

### Background Stack

```css
--bg-base: #030407;    /* The void — near-black with slight blue */
--bg-surface: #0a0b10; /* Card backgrounds */
```

Three texture layers applied to EVERY dark page:
1. **Noise overlay** (fixed, full viewport): SVG fractalNoise, 4% opacity, `mix-blend-mode: multiply`
2. **Ambient glow** (fixed): Two radial gradients — harness color at top-right (3% opacity), env color at bottom-left (3% opacity)
3. **Section-specific radial gradients** on deep dive heroes

### Text Hierarchy on Dark

| Level | Hex | Usage |
|-------|-----|-------|
| Pure | `#FFFFFF` | Display titles, hero text, emphasis |
| Main | `#F9FAFB` | Primary body text on dark |
| Muted | `#D1D5DB` | Secondary text, editorial lead, card body |
| Faint | `#9CA3AF` | Tertiary text, eyebrow labels, meta |

**Critical readability rule:** Minimum font-weight 400 on dark backgrounds. Inter 300 is allowed but only for text-muted or brighter.

### Border System

```css
--border-dim: rgba(255, 255, 255, 0.1);
```

Borders are always translucent white at low opacity. Never solid colors. `border-dim` for cards; slightly higher for hover states.

---

## 3. The White Canvas — Article Reading Pages

### Paper Overlay Architecture

The article page's most distinctive feature: a white paper canvas that **physically overlays the dark hero** as the user scrolls.

```css
.paper-canvas {
  margin-top: -10vh;              /* Overlaps hero by 10% of viewport */
  border-radius: 40px 40px 0 0;  /* Rounded top corners only */
  background: #FCFDFD;            /* Microscopic off-white, not pure white */
  background-image: radial-gradient(rgba(0,0,0,0.04) 1px, transparent 1px);
  background-size: 32px 32px;     /* Dot grid — working notebook texture */
  box-shadow: 0 -30px 80px rgba(0,0,0,0.6);
}
.paper-canvas::before {           /* Soft light-edge highlight */
  content: ''; position: absolute; top: 0; left: 0; right: 0; height: 1px;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.8), transparent);
}
```

### Text Hierarchy on White (5-tier Tactile Inks)

| Level | Hex | Usage |
|-------|-----|-------|
| Pure | `#000000` | Strong emphasis in body |
| Main | `#111318` | Headings, titles |
| Body | `#1A1C20` | Newsreader body paragraphs |
| Faint | `#5A5D67` | Secondary text, labels |
| Muted | `#8E93A0` | Meta, timestamps, credits |

### Reading Layout

- `.text-col`: 640px max-width (65-75 character optimal reading line)
- `.bleed-wide`: 960px max-width (diagrams, cards, specs break out of text column)
- Both centered within `.content-layout` (960px container)

---

## 4. Signature Design Techniques

### 4a. The Hollow Text Technique

Display titles use a 2px stroke with transparent fill to create the "CHASM" effect:

```css
.text-hollow { color: transparent; -webkit-text-stroke: 2px var(--text-pure); }
.text-hollow.accent-cyan { -webkit-text-stroke: 2px var(--color-env); }
.text-hollow.accent-purple { -webkit-text-stroke: 2px var(--color-model); }
.text-hollow.accent-red { -webkit-text-stroke: 2px var(--color-harness); }
```

**When to use:** The last line of a multi-line display title. "CHASM" is hollow cyan. "THAT'S IT." is hollow purple. "PRODUCTION." is hollow red. The hollow line is always the emotional payoff.

### 4b. The 3D Isometric Stack Visualization

A CSS 3D perspective visualization of four translucent planes:

```
Container: perspective 1200px, 600px height
Iso plane: rotateX(60deg) rotateZ(-45deg), 320x240px
Layers (Z-axis positioning):
  Environment: translateZ(120px) — cyan, top
  Harness:     translateZ(40px)  — red
  Tools:       translateZ(-40px) — amber
  Model:       translateZ(-120px) — purple, bottom
```

Each layer has:
- 1px border in identity color (0.6 opacity)
- Inset box-shadow glow in identity color
- CSS grid overlay (20x20px, 10% opacity, currentColor)
- Layer label: JetBrains Mono 11px, 700, 4px letter-spacing, text-shadow glow

Core beam: 3px vertical gradient through the stack, cyan glow.
"AI" text: Inter 900, 80px, white with cyan triple text-shadow.

**Mouse parallax (desktop only):** Adjusts rotateX/Z by ±0.15° per pixel from center. `transition: none` during move, spring-ease 1.5s on mouseleave.

**Homepage variant:** Layers are STRATEGY (cyan), PRODUCT (purple), ENGINEERING (amber), DELIVERY (red). Center text: "AI PM" (65px). Same visual treatment, different content.

### 4c. Sticky Card Stack

4 architecture cards that stack as user scrolls, each revealing 60px of the card below.

```
Card 1 (Model):       top: 100px, purple border
Card 2 (Harness):     top: 160px, red border + stronger gradient
Card 3 (Tools):       top: 220px, amber border
Card 4 (Environment): top: 280px, cyan border
```

Each card: 75vh height, 24px radius, `box-shadow: 0 -40px 80px rgba(3,4,7,0.95)` (creates the stacking depth). `transform-style: preserve-3d` for 3D tilt interaction.

Card titles: Inter 800 (clamp 2.2-3.5rem), NOT Instrument Serif. Body: Newsreader 400.

Folder tab (top-right): JetBrains Mono 800, identity color, with 8px glowing dot.

**3D tilt interaction (desktop only):** On mousemove, card tilts ±2° via `perspective(1000px) rotateX/Y`, scales to `scale3d(1.02, 1.02, 1.02)`. Children `translateZ(30px)` for depth. Spring-ease snap-back on mouseleave.

**Homepage variant:** 3 cards (Engineering/cyan, Design/purple, Business/amber) at offsets 100/160/220px.

### 4d. Deep Dive Recession Stacking

4 full-viewport (100vh) sections that are ALL `position: sticky; top: 0`. As the next section scrolls up, the current one:
- Scales down (1 → 0.92)
- Translates up (0 → 40px)
- Fades out (1 → 0.2 opacity)
- Background image darkens (brightness 1 → 0)

Creates a "deck of cards being peeled back" effect. Each section has increasing z-index (31, 32, 33, 34).

### 4e. The Dark-to-White Reading Transition

A multi-stop gradient that transitions from the dark site to the white article preview:

```css
background: linear-gradient(180deg,
  #030407 0%, #0B0D12 15%, #1A1C24 35%,
  #5A5D67 60%, #F3F4F6 85%, #FCFDFD 100%);
```

Contains a browser frame mockup (macOS chrome, 16px radius) that reveals with the cinematic blur animation. The frame shows an article preview with a fade-to-white overlay and CTA button.

### 4f. Frosted Glass Pills

Topic pills on deep dive sections use frosted glass:

```css
background: rgba(255,255,255,0.03);
border: 1px solid rgba(255,255,255,0.15);
backdrop-filter: blur(12px);
box-shadow: 0 4px 20px rgba(0,0,0,0.4);
```

Each pill gets a series-specific border color at 0.4 opacity and matching tinted text.

---

## 5. Animation System

### 5a. Cinematic Blur Reveal (Primary)

```css
.reveal {
  opacity: 0;
  transform: translateY(40px) scale(0.98);
  filter: blur(4px);
  transition: opacity 1s var(--ease-cinematic),
              transform 1s var(--ease-cinematic),
              filter 1s var(--ease-cinematic);
}
.reveal.visible { opacity: 1; transform: translateY(0) scale(1); filter: blur(0); }
```

**Easing:** `--ease-cinematic: cubic-bezier(0.16, 1, 0.3, 1)` — Apple's deceleration curve. Everything enters fast, settles slow.

Triggered by IntersectionObserver at 10% threshold, -10% root margin.

### 5b. palankiReveal (Homepage Name Animation)

A distinctive name reveal with blur, scale overshoot, and letter-spacing squeeze:

```css
@keyframes palankiReveal {
  0% { opacity: 0; filter: blur(12px); transform: scale(1.1) translateY(20px); letter-spacing: -0.1em; }
  100% { opacity: 1; filter: blur(0); transform: scale(1) translateY(0); letter-spacing: -0.03em; }
}
```

Combined with a pulsing cyan ghost pseudo-element (`::after` using `data-text` attribute):

```css
@keyframes pulseCyan {
  0%, 100% { opacity: 0.2; filter: blur(2px); transform: scale(1); }
  50% { opacity: 0.8; filter: blur(8px); transform: scale(1.02); }
}
.palanki-text::after { content: attr(data-text); animation: pulseCyan 4s ease-in-out infinite 1.5s; }
```

### 5b2. drawLine Animation

Cyan underline draws from left on "Bridger." text:

```css
@keyframes drawLine { 0% { transform: scaleX(0); } 100% { transform: scaleX(1); } }
.italic-serif::after { /* 2px cyan line */ animation: drawLine 1s var(--ease-cinematic) 0.8s forwards; }
```

### 5b3. line-draw Class (Staggered Inline Underlines)

Key words in body text get cyan underlines that reveal on scroll with staggered delays:

```css
.line-draw::after { /* 2px cyan line, scaleX(0) → scaleX(1) */ }
.reveal.visible .line-draw:nth-of-type(1)::after { transition-delay: 0.8s; }
.reveal.visible .line-draw:nth-of-type(2)::after { transition-delay: 1.2s; }
.reveal.visible .line-draw:nth-of-type(3)::after { transition-delay: 1.6s; }
```

### 5b4. Dynamic Ambient Glow

The background glow follows mouse position (desktop only):

```javascript
document.addEventListener('mousemove', (e) => {
  const x = (e.clientX / window.innerWidth) * 100;
  const y = (e.clientY / window.innerHeight) * 100;
  glowBg.style.background = `radial-gradient(circle at ${x}% ${y}%, ...)`;
});
```

### 5b5. Dynamic Nav Tightening

Nav padding and background solidify on scroll past 50px:

```javascript
if(window.scrollY > 50) { nav.style.padding = '1rem var(--px)'; nav.style.background = 'rgba(3,4,7,0.85)'; }
```

### 5b6. SVG Ring Counters

Proof point stats use SVG circles with animated stroke-dashoffset + JS counting:

```css
.svg-stat-ring .progress { stroke-dasharray: 283; stroke-dashoffset: 283; transition: stroke-dashoffset 2s var(--ease-cinematic); }
.reveal.visible .svg-stat-ring .progress { stroke-dashoffset: 0; }
```

Colored variants: `.color-cyan`, `.color-purple`, `.color-amber`, `.color-red` with matching `drop-shadow` filters.

JS counter increments from 0 to target over 40 frames at 30ms intervals.

### 5b7. Quote Line-by-Line Reveal

Quote text splits into `.quote-line > span` blocks that slide up from `translateY(100%)`:

```css
.quote-line span { transform: translateY(100%); opacity: 0; transition: 1s var(--ease-cinematic); }
.the-why.visible .quote-line span { transform: translateY(0); opacity: 1; }
.quote-line:nth-child(1) span { transition-delay: 0.1s; }
.quote-line:nth-child(2) span { transition-delay: 0.2s; color: var(--text-faint); font-style: italic; }
```

### 5c. Cyan Line Scale-Y

The editorial block's cyan vertical line scales in from top:

```css
@keyframes scaleYIn {
  0% { transform: scaleY(0); opacity: 0; }
  100% { transform: scaleY(1); opacity: 1; }
}
/* Applied with: animation: scaleYIn 1s var(--ease-cinematic) 0.5s both */
```

### 5d. Hero Curtain Fade (Article Pages)

On article pages, the entire hero section fades to opacity 0 as the user scrolls. Complete by ~60% viewport scroll. Combined with parallax on the background image (0.4x speed + subtle scale increase).

### 5e. Wet-Ink Highlighter (Article Pages)

```css
mark.pastel-highlight {
  background-image: linear-gradient(110deg, transparent 2%,
    var(--color-model-light) 5%, rgba(157,78,221,0.15) 95%, transparent 98%);
  background-size: 0% 100%;
  mix-blend-mode: multiply;  /* The authentic ink-on-paper look */
  transition: background-size 1.4s var(--ease-cinematic);
}
mark.pastel-highlight.visible { background-size: 100% 100%; }
```

### 5f. Magnetic Button Physics (Desktop Only)

Buttons with `.magnetic-btn > .magnetic-content` track the cursor:
- Button: translates at 0.15x mouse offset
- Content: translates at 0.08x mouse offset (creates depth)
- On leave: spring-ease snap back (`--ease-spring: cubic-bezier(0.175, 0.885, 0.32, 1.1)`)
- Disable on mobile (< 768px)

### 5g. Comet Progress Bar (Article Pages)

Purple progress bar (3px) with a radial gradient glow head:

```css
.progress-bar::after {
  width: 40px;
  background: radial-gradient(ellipse right, rgba(255,255,255,1) 0%, transparent 100%);
  box-shadow: 0 0 12px var(--color-model), 0 0 20px var(--color-model);
  border-radius: 50%; transform: translateX(50%);
}
```

---

## 6. Component Catalog

### Navigation
- Fixed, `backdrop-filter: blur(12px)`, gradient fade from base to transparent
- Dynamic tightening on scroll (padding 1.5rem → 1rem, bg solidifies at 50px)
- Brand: full name "Ravi Teja Palanki" (Inter 800, 1.2rem, hover opacity 0.7)
- Right links: "My Profile" (/profile), "My AI Learnings" (/writing) — Inter 600, 0.85rem, with animated underline on hover (scaleX 0→1, transform-origin flips from right to left)
- CTA button: "Connect With Me ↗" (JetBrains Mono 700, 0.72rem, white bg, dark text, pill, hover translateY -2px + glow shadow)
- On article pages: `mix-blend-mode: difference` (auto-adapts to dark/white)
- Mobile (768px): nav links hidden, only brand + CTA visible

### Eyebrow Label
- JetBrains Mono 700, 0.75rem, uppercase, 0.15em spacing
- Extending line: `::after` with gradient from `border-dim` to transparent
- Format: `01 // THE ARCHITECTURE`

### CTA Button
- Pill: 50px radius, Inter 800, 0.95rem, uppercase, `overflow: hidden`
- White on dark: `background: #FFFFFF; color: #000000`
- Hover: translateY(-4px), heavy white glow shadow, bg shifts to #F3F4F6
- SVG arrow icon (24x18, stroke 2.5): `transition: transform 0.4s var(--ease-spring) 0.1s`, hover translateX(6px)
- Magnetic physics: `.magnetic-btn > .magnetic-content` — button 0.15x, content 0.08x mouse offset, spring snap-back
- Disabled: frosted glass, white text, 0.3 opacity border

### Credential Badges
- Frosted glass: `backdrop-filter: blur(10px)`, `background: rgba(255,255,255,0.05)`, `border: 1px solid rgba(255,255,255,0.1)`
- Unified white text. Colored dots only (6px, box-shadow glow in identity color)
- Cyan dot: Perplexity Fellow. Purple dot: Honeywell. Amber dot: Lovable.
- Hover: border brightens to rgba(255,255,255,0.4)

### SVG Stat Ring
- Container: `clamp(100px, 30vw, 140px)` square, centered
- SVG: two circles (r=45), `transform: rotate(-90deg)`
- `.bg`: `stroke: rgba(255,255,255,0.05)`, stroke-width 4
- `.progress`: `stroke-dasharray: 283; stroke-dashoffset: 283`, transitions to 0 on reveal
- Color variants: `.color-cyan/purple/amber/red` with matching `drop-shadow` filter (8px, 0.6 opacity)
- Centered stat value: JetBrains Mono 800, clamp(1.8-2.5rem)
- JS counter: increments from 0 to target over 40 frames at 30ms

### Anti-Pattern Cards
- 4px red left border, surface bg, 12px radius
- Red "ANTI-PATTERN" label with 6px glowing dot
- Hover: red border spread, translateY(-6px), red shadow tint

### Browser Frame Mockup
- 16px radius, `#E5E7EB` chrome, red/yellow/green dots (12px)
- Content: article preview with Newsreader body, Instrument Serif title
- Preview fade: gradient overlay + floating CTA button

---

## 7. Responsive Rules

**Single breakpoint approach:** Major changes at 1024px; refinements at 768px.

At 1024px:
- Hero: single column (grid collapses)
- 3D viz: scale(0.8)
- Sticky cards: auto height, tighter offsets (90/150/210/270px)
- Anti-pattern grid: 2 columns
- Deep dives: relative positioning (no sticky stacking)

At 768px:
- Nav CTA: smaller padding
- 3D viz: scale(0.6)
- Cards: minimal padding
- Anti-pattern grid: single column
- Article meta: vertical stack
- Footer links: vertical stack

**Fluid sizing throughout:** All text uses `clamp()`. All padding uses `clamp()` or `var(--px): clamp(1.25rem, 6vw, 6rem)`.

---

## 8. Page Type Recipes

### Recipe: Homepage (/)
1. Dark canvas (noise + dynamic mouse-following glow + base)
2. Hero: grid 1.2fr/0.8fr — "RAVI TEJA / PALANKI" (palankiReveal + pulseCyan) + "AI-fluent product leader. The Bridger." (drawLine on Bridger) + editorial lead/sub (line-draw class) + frosted glass badges + 3D isometric stack (STRATEGY/PRODUCT/ENGINEERING/DELIVERY, "AI PM" center)
3. Bridger: sticky card stack (3 cards: Engineering/Design/Business, with 3D tilt interaction)
4. Two Paths: recession stacking (2 sticky 100vh sections: My Profile → Working Notes)
5. Proof Points: SVG ring counters (4 stats with counting animation)
6. Quote: line-by-line reveal ("top 0.1% AI product leader — merging human judgement with machine intelligence")
7. Article teaser: dark-to-white gradient + browser frame + Benchmarks ≠ Evals preview
8. Footer links (LinkedIn | GitHub | Contact: ravi.aifluentproduct@gmail.com)

### Recipe: Writing Landing Page (/writing)
1. Dark canvas (noise + glow + base)
2. Hero: grid 1.2fr/0.8fr, display titles + editorial block + 3D viz
3. Architecture: sticky card stack (4 cards)
4. Anti-patterns: 3 red-accented cards (fixed 3-col grid)
5. Deep dives: recession stacking (4 sticky 100vh sections)
6. Quote: Instrument Serif massive quote
7. Reading transition: gradient + browser frame + article preview
8. Footer links

### Recipe: Series Hub Page
1. Dark canvas throughout (no white sections)
2. Series hero: 70vh, breadcrumb + display title + lead + stats
3. Level sections: badge + header + topic card grid (auto-fill 340px)
4. Reading guide: path recommendation cards
5. CTA: quote + start button
6. Footer

### Recipe: Article Reading Page
1. Dark hero: 88vh, background image, gradient overlay, parallax + curtain fade
2. Paper canvas overlay: rounded corners, dot grid, margin-top -10vh
3. Content layout: 640px text / 960px bleed
4. Components: learning block, body text (Newsreader), diagrams (interactive HTML), mistake card, spec card, up-next card
5. Comet progress bar + magnetic back button
6. Footer: italic signature

---

## 9. DESIGN.md Compatibility

This design system is exportable as a `DESIGN.md` (Google Labs format) for agent consumption. When an AI agent (Claude, Cursor, v0, Bolt) is generating a prototype that should match the learn site, it needs the design tokens in a structured frontmatter format the agent can parse and apply.

The pattern: ship the same design system as both this skill (for humans and design discussions) AND a `DESIGN.md` artifact (for agents generating code). Both stay in sync — when the design tokens shift here, they shift in `DESIGN.md`.

Reference the new `design-spec` skill being built in parallel for the full DESIGN.md authoring guide. This section gives the export-ready frontmatter for the learn site's tokens.

### YAML Frontmatter — Learn Site Tokens

```yaml
---
name: learn-site-design
version: 2.0
purpose: Cinematic editorial design system for ravitejapalanki.com
audience: Editorial readers, AI PMs, technical leaders

colors:
  identity:
    model: "#9D4EDD"      # Purple — intelligence layer, primary identity
    harness: "#F43F5E"    # Red — anti-patterns, mistakes, warnings only
    tools: "#F59E0B"      # Amber — capabilities, APIs, instruments
    environment: "#06B6D4" # Cyan — deployment, hero accent
  functional:
    success: "#10B981"    # Emerald — pass states only
    info_bg: "#EFF6FF"
    info_text: "#1E3A8A"
    info_accent: "#3B82F6"
  dark_canvas:
    bg_base: "#030407"    # Near-black with slight blue
    bg_surface: "#0a0b10"
    text_pure: "#FFFFFF"
    text_main: "#F9FAFB"
    text_muted: "#D1D5DB"
    text_faint: "#9CA3AF"

fonts:
  display:
    family: "Inter"
    weights: [300, 400, 500, 600, 700, 800, 900]
    role: "Display titles, UI labels, headings"
  editorial:
    family: "Instrument Serif"
    weights: [400]
    italics: true
    role: "Hero titles, article H2s, drop caps, signatures"
  body:
    family: "Newsreader"
    weights: [200, 300, 400, 500, 600, 700, 800]
    variable: true
    role: "Long-form article body (reading pages only)"
  mono:
    family: "JetBrains Mono"
    weights: [400, 500, 700, 800]
    role: "Labels, tags, badges, metadata, code"

typography_rules:
  - rule: "Inter 900 ONLY for display titles"
    properties: "uppercase, letter-spacing -0.03em, line-height 0.95"
  - rule: "Instrument Serif NEVER for body text"
    use: "hero titles, article H2s, quotes, drop caps, signatures"
  - rule: "Newsreader ONLY on article reading pages"
    fallback: "Inter for landing/topic hubs"
  - rule: "JetBrains Mono for ALL labels, tags, metadata"
    properties: "font-weight 700-800, uppercase, letter-spacing 0.15em"

color_rules:
  - "Identity colors appear ONLY as accents (borders, glows, text highlights, small fills) — never as flat background fills"
  - "Red is EXCLUSIVELY for anti-patterns, mistakes, warnings — never positive"
  - "On dark backgrounds: borders, text-shadow glows, radial gradients at 6-15% opacity"
  - "On white backgrounds: border-left accents, tinted backgrounds at 4-12% opacity, text color"

signature_techniques:
  - "Cinematic blur animations on hero entrances"
  - "3D isometric CSS visualizations (no canvas/WebGL)"
  - "Sticky card stacks for layered storytelling"
  - "Deep dive recession stacking (4 sticky 100vh sections)"
  - "Dark-to-white transitions at section breaks"
  - "Paper canvas overlay (rounded corners, dot grid)"
  - "Magnetic button physics (cursor attraction)"
  - "Wet-ink highlighters on key phrases"
  - "Comet progress bars (article reading)"

responsive:
  breakpoints:
    desktop: "default"
    tablet: "1024px"
    mobile: "768px"
  fluid_sizing: "All text and padding use clamp()"
---
```

### Why DESIGN.md Matters

When an agent generates a prototype using the vibe-coding pattern (see the `prompt-craft` skill), it needs the design system in structured form. Pasting this entire SKILL.md into the prompt is wasteful — most of the content is editorial guidance the agent doesn't need.

The DESIGN.md frontmatter gives the agent:
- Exact hex codes for the four identity colors
- Font names and weights with their exact roles
- The non-negotiable rules (red = warnings only, Newsreader = article body only)
- Signature techniques the agent should use to make outputs feel like learn-site outputs

The agent generates a prototype using these tokens, and the result looks like the learn site without the agent ever reading the editorial sections of this skill.

### When to Use Which Format

- **This SKILL.md** — for design discussions, building new pages by hand, training a new designer, troubleshooting why a section feels off
- **DESIGN.md frontmatter** — for agent-driven prototyping, vibe-coding, or any scenario where an LLM is generating code that should match the learn-site visual identity

Keep both in sync. When tokens change here, they change in DESIGN.md. The cross-reference to the `design-spec` skill (in parallel) covers the maintenance protocol — versioning, change-tracking, and the agent-consumption tests that confirm the frontmatter still produces correct outputs.

---

## 10. What This Skill Does NOT Cover

- Content writing style (see `ravi-thinking-skills`)
- Article structure / editorial voice (see `rtp-deep-dive-writer`)
- SVG diagram design (see `excalidraw-svg` for hand-drawn, `SVG-REVISION-PLAN.md` for evals diagrams)
- Lovable-specific build instructions (see `lovable/` folder in `1_Projects/my-personal-website/`)
- Profile page deep content (see `04-PROFILE-PAGE-SPEC.md` in the lovable folder)
- Writing section content map (see `09-CONTENT-MAP.md` — all 70 article routes)
