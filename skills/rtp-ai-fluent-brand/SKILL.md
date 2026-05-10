---
name: rtp-ai-fluent-brand
description: 'Complete visual identity system for AI Fluent Product Leadership — "ravi-personal-branding (v2.x)." Use when creating ANY visual content: presentations, websites, landing pages, artifacts, HTML, React, documents, PDFs, social graphics, infographics, or emails. Triggers include: (1) Any content for Ravi Teja Palanki or AI Fluent, (2) Dark theme with gold/premium aesthetics, (3) Presentations or slides, (4) Landing pages or marketing content, (5) Data visualizations or infographics, (6) Component styling or UI design. Provides exact color hex values, typography specs, spacing systems, component classes, animation timing, and accessibility standards. Core principles: readability is sacred, restraint signals mastery, gold appears maximum 3× per view.'
---
# AI Fluent Brand System — ravi-personal-branding (v2.x)

> *"Design is not just what it looks like and feels like. Design is how it works."* — Steve Jobs

A premium visual identity where **golden knowledge** illuminates against considered darkness.

---

## The Three Absolutes

Before any specification, internalize these non-negotiable principles:

### 1. READABILITY IS SACRED
If text cannot be read effortlessly at any size on any device, the design has failed.
- Primary text: minimum 7:1 contrast ratio (WCAG AAA)
- Body text: minimum 16px on all devices
- Line length: 45-65 characters maximum
- Line height: minimum 1.5 for body text

### 2. RESTRAINT SIGNALS MASTERY
Amateur designers add. Masters subtract.
- **Gold appears maximum 3× per view** (frame label, one data point, one emphasized phrase)
- Every animation must serve meaning, never decoration
- White space is not empty — it's active design

### 3. DARKNESS HAS DIMENSION
The background is not flat. It breathes.
- **Never use pure black (#000000)** — causes halation, eliminates shadow depth
- Use `#0A0A0A` as the deepest layer
- Shadows on dark backgrounds require LIGHT, not darkness

---

## Quick Reference: The Essential Numbers

### Brand Identity
- **Brand Name:** AI FLUENT Product Leadership
- **Tagline:** "Fluency through deliberate practice"
- **Visual System:** ravi-personal-branding (v2.x)

### Primary Colors

| Token | Hex | HSL | Usage |
|-------|-----|-----|-------|
| `--gold` | `#D4AF37` | 43 72% 52% | Primary accent, CTAs, headlines |
| `--gold-light` | `#E6C77A` | 43 65% 65% | Hover states, highlights |
| `--gold-dark` | `#B89A2E` | 43 75% 40% | Active states, depth |
| `--gold-deep` | `#8A6B1F` | 42 75% 31% | Shadows, deep accents |

### Secondary Accents

| Token | Hex | Usage |
|-------|-----|-------|
| `--teal` | `#50C9B0` | Technology/innovation indicators |
| `--teal-bright` | `#6FDFC9` | Highlights, interactive elements |
| `--purple` | `#8B6EC4` | Multi-agent theme, depth |
| `--purple-bright` | `#A890D9` | Highlights, premium features |

### Dark Theme Foundation

| Token | Hex | Usage |
|-------|-----|-------|
| `--void` | `#0A0A0A` | Body background (deepest) |
| `--codex` | `#121212` | Section backgrounds |
| `--dusk` | `#1A1A1A` | Card backgrounds |
| `--charcoal-deep` | `#151515` | Primary dark surface |

### Text Colors

| Token | Hex | Contrast | Usage |
|-------|-----|----------|-------|
| `--text-parchment` | `#F5F0E6` | 14.2:1 | Headlines, key statements |
| `--text-ivory` | `#DDD8CC` | 10.8:1 | Body text |
| `--text-stone` | `#A9A49A` | 6.1:1 | Captions, metadata |
| `--text-dust` | `#6E6A62` | 3.5:1 | Watermarks, disabled |

### Typography

| Role | Font | Size (Desktop) | Weight | Line Height |
|------|------|----------------|--------|-------------|
| Display | Cormorant Garamond | `clamp(52px, 10vw, 110px)` | 300 | 0.95 |
| H1 | Cormorant Garamond | `clamp(36px, 5vw, 60px)` | 400 | 1.1 |
| H2 | Cormorant Garamond | `clamp(28px, 3.5vw, 44px)` | 500 | 1.15 |
| H3 | Cormorant Garamond | `clamp(22px, 2.5vw, 32px)` | 500 | 1.25 |
| Body | Inter | `clamp(16px, 1.1vw, 18px)` | 400 | 1.75 |
| Label | Inter | 12px | 600 | - |
| Data/Code | JetBrains Mono | 14-16px | 500 | 1.5 |

### Spacing (8px Grid)

| Token | Value | Usage |
|-------|-------|-------|
| `--space-4` | 16px | Between elements |
| `--space-6` | 24px | Minimum component gap, mobile padding |
| `--space-8` | 32px | Card padding |
| `--space-16` | 64px | Desktop horizontal padding |
| `--space-20` | 80px | Mobile vertical section padding |
| `--space-36` | 140px | Desktop vertical section padding |

### Content Widths

| Container | Max Width | Usage |
|-----------|-----------|-------|
| `--content-narrow` | 520px | Single column, focused reading |
| `--content-default` | 640px | Standard content |
| `--content-wide` | 720px | Wider content with visuals |
| `--content-max` | 920px | Full-width sections |

---

## Core CSS Variables Block

```css
:root {
  /* BACKGROUNDS */
  --void: #0A0A0A;
  --codex: #121212;
  --dusk: #1A1A1A;
  --charcoal-deep: #151515;
  
  /* TEXT */
  --foreground: #F5F0E6;
  --text-ivory: #DDD8CC;
  --text-stone: #A9A49A;
  --text-dust: #6E6A62;
  
  /* GOLD PALETTE */
  --gold: #D4AF37;
  --gold-light: #E6C77A;
  --gold-dark: #B89A2E;
  --gold-deep: #8A6B1F;
  --gold-glow: #E5C04D;
  
  /* SECONDARY ACCENTS */
  --teal: #50C9B0;
  --teal-bright: #6FDFC9;
  --purple: #8B6EC4;
  --purple-bright: #A890D9;
  
  /* STATUS */
  --status-success: #4CAF50;
  --status-danger: #EF5350;
  --status-warning: #FFA726;
  
  /* TYPOGRAPHY */
  --font-display: "Cormorant Garamond", Georgia, serif;
  --font-body: "Inter", -apple-system, sans-serif;
  --font-mono: "JetBrains Mono", Consolas, monospace;
  
  /* ANIMATION */
  --ease: cubic-bezier(0.16, 1, 0.3, 1);
  --ease-out: cubic-bezier(0.33, 1, 0.68, 1);
  --ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1);
  --duration-fast: 150ms;
  --duration-normal: 300ms;
  --duration-slow: 500ms;
}
```

---

## Component Quick Reference

### Buttons
```css
.btn-premium-gold {
  background: linear-gradient(135deg, var(--gold-dark), var(--gold), var(--gold-light));
  color: var(--void);
  padding: 12px 24px;
  border-radius: 8px;
  font-weight: 600;
  box-shadow: 0 0 20px rgba(212, 175, 55, 0.25);
}

.btn-premium-outline {
  background: transparent;
  border: 1px solid rgba(212, 175, 55, 0.5);
  color: var(--gold);
  padding: 12px 24px;
  border-radius: 8px;
}
```

### Cards (The Critical Shadow Formula)
```css
.card-premium {
  background: var(--dusk);
  border-radius: 12px;
  padding: 24px;
  /* THE CRITICAL DARK THEME SHADOW */
  box-shadow:
    inset 0 0 0.5px 1px rgba(255, 255, 255, 0.075),
    0 0 0 1px rgba(0, 0, 0, 0.05),
    0 3.5px 6px rgba(0, 0, 0, 0.09);
}
```

### Takeaway Boxes
```css
.takeaway {
  border-left: 3px solid var(--gold);
  background: linear-gradient(90deg, rgba(212, 175, 55, 0.08), transparent);
  padding: 16px 24px;
  border-radius: 0 8px 8px 0;
}
```

### Labels
```css
.label {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(80, 201, 176, 0.15);
  color: var(--teal-bright);
  padding: 4px 12px;
  border-radius: 9999px;
  font-size: 12px;
  font-weight: 600;
  text-transform: uppercase;
}

.label::before {
  content: '';
  width: 6px;
  height: 6px;
  background: currentColor;
  border-radius: 50%;
  animation: pulse 2s infinite;
}
```

---

## Gold Glow System

```css
/* Subtle glow — general emphasis */
--glow-gold-subtle: 0 0 15px rgba(212, 175, 55, 0.15), 0 0 30px rgba(212, 175, 55, 0.08);

/* Medium glow — important elements */
--glow-gold-medium: 0 0 20px rgba(212, 175, 55, 0.25), 0 0 40px rgba(212, 175, 55, 0.15);

/* Intense glow — CTAs, hero moments */
--glow-gold-intense: 0 0 20px rgba(212, 175, 55, 0.35), 0 0 40px rgba(212, 175, 55, 0.25), 0 0 60px rgba(212, 175, 55, 0.15);

/* Text glow */
--glow-gold-text: 0 0 10px rgba(212, 175, 55, 0.30), 0 0 20px rgba(212, 175, 55, 0.20);
```

---

## When to Use Dark vs Light Theme

**Use Dark Theme (ravi-personal-branding dark theme) For:**
- Hero sections with video backgrounds
- Feature showcase sections
- Module learning environments
- Premium content areas
- Presentations and slides
- Evening/immersive reading experiences

**Use Light Theme (The Parchment Mode) For:**
- Form sections (registration, contact)
- FAQ and documentation sections
- Long-form reading content
- Print-friendly materials
- Daytime/productivity contexts
- Email templates and newsletters

### Light Theme Foundation

| Token | Hex | Usage |
|-------|-----|-------|
| `--bg-champagne` | `#FAF7F2` | Page background (warmest layer) |
| `--bg-parchment` | `#F5EFE3` | Card and section backgrounds |
| `--bg-linen` | `#EDE7D9` | Subtle contrast surfaces |
| `--bg-cream` | `#FEFDFB` | Input fields, elevated surfaces |

### Light Theme Text Colors

| Token | Hex | Contrast on #FAF7F2 | Usage |
|-------|-----|---------------------|-------|
| `--text-ink` | `#1A1715` | 15.8:1 | Headlines, primary text |
| `--text-charcoal` | `#3D3733` | 10.2:1 | Body text |
| `--text-walnut` | `#6B6259` | 5.3:1 | Captions, metadata |
| `--text-sand` | `#A39B90` | 3.2:1 | Watermarks, disabled |

### Light Theme Gold Accents

| Token | Hex | Usage |
|-------|-----|-------|
| `--gold-on-light` | `#B89A2E` | Primary accent (darker gold for light backgrounds) |
| `--gold-on-light-hover` | `#9A7F1E` | Hover states |
| `--gold-on-light-subtle` | `rgba(184, 154, 46, 0.12)` | Tinted backgrounds |

### Light Theme Component Patterns

```css
/* Light mode card */
.card-parchment {
  background: #F5EFE3;
  border-radius: 12px;
  padding: 24px;
  box-shadow:
    0 1px 3px rgba(26, 23, 21, 0.06),
    0 4px 12px rgba(26, 23, 21, 0.04);
}

/* Light mode takeaway */
.takeaway-light {
  border-left: 3px solid #B89A2E;
  background: linear-gradient(90deg, rgba(184, 154, 46, 0.08), transparent);
  padding: 16px 24px;
  border-radius: 0 8px 8px 0;
}

/* Light mode button */
.btn-gold-light {
  background: linear-gradient(135deg, #B89A2E, #D4AF37);
  color: #FEFDFB;
  padding: 12px 24px;
  border-radius: 8px;
  font-weight: 600;
  box-shadow: 0 2px 8px rgba(184, 154, 46, 0.2);
}
```

### Light Theme CSS Variables

```css
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
}
```

### Design Principles — Apple/IDEO Alignment

Both themes follow these principles drawn from the best of Apple's Human Interface Guidelines and IDEO's design thinking:

1. **Clarity over decoration.** Every visual element communicates. If it doesn't teach, guide, or delight, it's noise.
2. **Deference to content.** The UI frames content — it never competes with it. Backgrounds recede; text commands attention.
3. **Depth through subtlety.** Shadows, gradients, and layering create hierarchy without heaviness. Apple uses translucency; we use warm tonal shifts.
4. **Consistency breeds confidence.** Same gold accent, same type scale, same spacing grid across both themes. Switching themes should feel like dimming the lights — the room stays the same.
5. **Touch targets matter.** Minimum 44px for interactive elements. Generous padding. Nothing cramped.
6. **Motion with purpose.** Every animation tells the user something: "this appeared," "this is connected to that," "you're moving forward." No animation for its own sake.

---

## Brand Voice

**Tone:**
- Authoritative but accessible
- Premium without being pretentious
- Expert with practitioner credibility
- Forward-looking with current relevance

**Key Phrases:**
- "AI Fluent" (always capitalized)
- "Deliberate practice" (methodology cornerstone)
- "Context Engineering" (technical framework)
- "Production-grade" (quality standard)

**Avoid:**
- Buzzwords without substance
- Overpromising outcomes
- Generic AI hype language
- Technical jargon without explanation

---

## Accessibility Standards

### Focus States
```css
:focus-visible {
  outline: 2px solid var(--gold);
  outline-offset: 3px;
  border-radius: 4px;
}
```

### Reduced Motion
All animations respect `prefers-reduced-motion: reduce`

### Contrast Requirements
- Minimum 4.5:1 for body text
- Minimum 3:1 for large text
- Never use pure black text on dark backgrounds

---

## Brand Attribution

All materials include this footer:
```
Ravi Teja Palanki • AI Fluent Product Leadership
```
- Font: 12px Inter
- Color: `#6E6A62` (Dust)
- Separator: Gold dot (`#D4AF37`)
- Position: Fixed bottom-left, 80px from left edge

---

## Reference Files

Load the appropriate reference based on task:

| When You Need To... | Load This Reference |
|---------------------|---------------------|
| Full color specifications, gradients, shadows | [references/color-system.md](references/color-system.md) |
| Typography scale, font loading, text styles | [references/typography-system.md](references/typography-system.md) |
| Animation timing, keyframes, scroll effects | [references/animation-system.md](references/animation-system.md) |
| UI components: buttons, cards, forms, navigation | [references/component-library.md](references/component-library.md) |
| Images, screenshots, galleries, media treatments | [references/image-media-treatments.md](references/image-media-treatments.md) |
| Charts, diagrams, timelines, data viz | [references/infographic-patterns.md](references/infographic-patterns.md) |
| Parallax, scroll snapping, progress indicators | [references/parallax-scroll-system.md](references/parallax-scroll-system.md) |

---

## Validation Checklist

Before finalizing ANY visual output:

### Color & Contrast
- [ ] No pure black (#000000) anywhere
- [ ] No pure white (#FFFFFF) for text
- [ ] Primary text contrast ≥ 7:1
- [ ] Gold appears ≤ 3 times per view

### Typography
- [ ] Body text ≥ 16px on all devices
- [ ] Line height ≥ 1.5 for body
- [ ] Headlines: Cormorant Garamond
- [ ] Body: Inter

### Animation
- [ ] All durations 200-800ms
- [ ] Using ease-out (never linear)
- [ ] `prefers-reduced-motion` respected

### Layout
- [ ] All spacing multiples of 8px
- [ ] Minimum 24px component gaps
- [ ] Content never touches edges

---

## The Ultimate Test

Before shipping any design:

1. **Can I read every piece of text effortlessly?** If no, fix it.
2. **Does every element earn its place?** If unsure, remove it.
3. **Does gold appear more than 3 times?** If yes, reduce.
4. **Would this feel appropriate in a rare book?** If no, refine.
5. **Does the design feel inevitable?** As if no other treatment was possible?

The goal is not to impress. The goal is to communicate with such clarity and beauty that the design becomes invisible — leaving only the content, perfectly delivered.

---

*"Simplicity is the ultimate sophistication."* — Leonardo da Vinci
