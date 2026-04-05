---
name: rtp-frontend-slides
description: "RTP skill: rtp-frontend-slides"
---

# Frontend Slides — Build Beautiful HTML Presentations with AI

A complete guide to creating stunning, zero-dependency HTML slide decks from scratch or by converting PowerPoint files. Designed for non-designers who want production-quality presentations without knowing CSS or JavaScript. Works with any AI coding assistant (Claude, ChatGPT, Copilot, Gemini, Perplexity, etc.).

Based on the open-source [frontend-slides](https://github.com/zarazhangrui/frontend-slides) project by Zara Zhang (MIT License), enhanced with accessibility best practices, performance patterns, and an expanded design system.

---

## What This Approach Does

You describe what your presentation is about and how you want it to feel. The AI generates a self-contained HTML file with inline CSS and JavaScript — no build tools, no npm, no frameworks. The result is a single file with smooth animations, keyboard/touch navigation, responsive design, and accessibility support that will work unchanged a decade from now.

The core insight is "show, don't tell." Rather than asking you to pick between abstract labels like "minimalist" or "bold," the process generates 3 visual previews so you can react to what you actually see. Most people can't articulate design preferences in words, but they know immediately what they like when they see it.

---

## The Process

The workflow has six phases. Depending on your starting point, you may skip some.

### Phase 0 — Detect Mode

Three entry points exist. **New Presentation** starts from scratch with your content. **PPT Conversion** takes an existing PowerPoint and transforms it into an animated web deck. **Enhancement** takes an existing HTML presentation and improves its styling, animations, or accessibility.

### Phase 1 — Content Discovery

Before any design work happens, the content needs to be understood. Three questions matter: What is this presentation for (pitch deck, teaching, conference talk, internal meeting)? How long should it be (5–10 slides, 10–20, or 20+)? Do you have content ready, or do you need help structuring it?

If you have images, they get evaluated for quality and relevance before anything else. The key principle is co-design: images shape the slide structure from the start, not as an afterthought. Three good product screenshots mean three feature slides anchored by those screenshots. A clear logo means it goes on the title and closing slides. A blurry or irrelevant image gets excluded with an explanation. If you have no images, CSS-generated visuals (gradients, shapes, patterns, typography) provide all the visual interest needed.

### Phase 2 — Style Discovery

This is the "show, don't tell" phase. You pick the feeling you want the audience to have — Impressed/Confident, Excited/Energized, Calm/Focused, or Inspired/Moved — and the AI generates three distinct single-slide HTML previews. Each preview is a self-contained title slide showing the typography, color palette, animation style, and overall aesthetic. You pick the one you like, say what you'd change, or ask to mix elements from multiple previews.

The mood-to-style mapping works like this: Impressed/Confident maps to Corporate Elegant, Dark Executive, or Clean Minimal. Excited/Energized maps to Neon Cyber, Bold Gradients, or Kinetic Motion. Calm/Focused maps to Paper & Ink, Soft Muted, or Swiss Minimal. Inspired/Moved maps to Cinematic Dark, Warm Editorial, or Atmospheric.

### Phase 3 — Generate the Presentation

The full presentation gets built as a single HTML file with all CSS and JavaScript inline. Every slide fits exactly within one viewport — no scrolling within slides, ever. This is non-negotiable. If content overflows, it splits into multiple slides.

### Phase 4 — PPT Conversion (if applicable)

For PowerPoint conversion, Python with the `python-pptx` library extracts all text, images, speaker notes, and slide structure. The extracted content gets confirmed with you, then rebuilt in the chosen web style.

### Phase 5 — Delivery

The finished file opens in the browser. Navigation works via arrow keys, spacebar, scroll wheel, touch/swipe, or clicking navigation dots. You get a summary of the file, style, and slide count, plus instructions for customizing colors, fonts, and animation timings by editing CSS variables.

---

## Design System: 10 Curated Style Presets

Each style is inspired by real design references. Abstract shapes only — no generic illustrations.

### Dark Themes

**Neon Cyber** — Futuristic and techy. Cyan/magenta neon glows on deep dark backgrounds. Particle system canvas effects. Monospace accent fonts. Grid patterns. Glitch text reveals. Good for: AI, developer tools, startup pitches in technical spaces.

**Midnight Executive** — Premium corporate feel. Deep navy and charcoal with gold or silver accents. Serif display type paired with clean sans-serif body. Subtle fade animations. Good for: investor pitches, executive briefings, financial presentations.

**Deep Space** — Cinematic and vast. Near-black backgrounds with distant light points. Slow parallax-style depth. Large-scale typography with generous whitespace. Good for: keynotes, inspirational talks, company vision decks.

**Terminal Green** — Developer-focused hacker aesthetic. Black backgrounds with phosphor green text. Monospace throughout. Typewriter/text-scramble reveals. Scanline overlay effects. Good for: technical talks, engineering team updates, open-source project presentations.

### Light Themes

**Paper & Ink** — Editorial and literary. Off-white backgrounds with deep black type. Serif headlines with refined spacing. Minimal motion — content-first. Good for: academic presentations, book-related talks, strategy decks that need to feel thoughtful.

**Swiss Modern** — Clean Bauhaus-inspired geometry. Bold primary colors on white. Strong grid system. Geometric sans-serif typography. Precise, deliberate animations. Good for: design talks, product presentations, anything where clarity is paramount.

**Soft Pastel** — Friendly and playful. Light pastel backgrounds with rounded shapes. Bouncy spring-easing animations. Rounded sans-serif fonts. Good for: educational content, creative pitches, anything targeting a non-technical audience.

**Warm Editorial** — Magazine-style sophistication. Warm cream backgrounds with dark type. Strong typography hierarchy with pull quotes. Image-text interplay. One bold accent color. Good for: marketing presentations, brand decks, storytelling-heavy talks.

### Specialty Themes

**Brutalist** — Raw, bold, and attention-grabbing. High contrast black-and-white with one aggressive accent. Oversized type. Deliberately "imperfect" layout. Good for: creative agencies, provocative talks, anything that needs to stand out from polished corporate decks.

**Gradient Wave** — Modern SaaS aesthetic. Flowing multi-color gradients on dark backgrounds. Smooth, continuous motion. Clean sans-serif type. Good for: product launches, SaaS demos, modern startup pitches.

---

## Anti-AI-Slop Design Principles

Generic AI-generated presentations share recognizable patterns that signal "a machine made this." Avoiding them is critical for credibility.

**Never use:**
- Purple gradients on white backgrounds (the single most common AI slide aesthetic)
- Inter, Roboto, Arial, or system fonts as primary typefaces
- Standard blue as the primary accent color
- Predictable centered hero layouts with generic icon grids
- Cookie-cutter card components with identical structure
- Stock-photo-style decorative illustrations

**Instead, use:**
- Distinctive font pairings from Fontshare or Google Fonts: Clash Display + Satoshi, Cormorant Garamond + DM Sans, Syne + General Sans, Instrument Serif + Cabinet Grotesk, Space Mono + Switzer
- Cohesive color themes with personality (not just a primary + neutral palette)
- Atmospheric backgrounds: gradient meshes, noise textures, geometric patterns, layered transparencies
- At least one signature visual moment that makes the deck memorable
- Layout variety: asymmetry, overlap, grid-breaking elements, unexpected whitespace

---

## Technical Requirements: The Non-Negotiables

### Viewport Fitting

Every slide must fit exactly in one viewport height. The mandatory CSS:

```css
html { scroll-snap-type: y mandatory; scroll-behavior: smooth; }
.slide {
    width: 100vw;
    height: 100vh;
    height: 100dvh;    /* dynamic viewport for mobile */
    overflow: hidden;   /* no overflow, ever */
    scroll-snap-align: start;
    display: flex;
    flex-direction: column;
    position: relative;
}
```

Content limits per slide: Title slides get 1 heading + 1 subtitle. Content slides get 1 heading + max 5 bullets OR 1 heading + 1 paragraph + 1 visual. Grid slides max out at 4 cards. If content doesn't fit, split into more slides.

### Responsive Typography

All font sizes and spacing must use `clamp()` for smooth scaling between mobile and desktop:

```css
:root {
    --title-size: clamp(1.5rem, 5vw, 4rem);
    --h2-size: clamp(1.25rem, 3.5vw, 2.5rem);
    --body-size: clamp(0.75rem, 1.5vw, 1.125rem);
    --slide-padding: clamp(1rem, 4vw, 4rem);
}
```

Height-based breakpoints handle short screens (landscape phones, tablets): at `max-height: 700px` padding and font sizes shrink; at `max-height: 600px` decorative elements hide; at `max-height: 500px` everything compresses to minimum.

### Navigation

Every presentation ships with: keyboard navigation (arrows, space, Escape), touch/swipe support, mouse wheel scrolling, visual progress bar, clickable navigation dots, and a keyboard hint that fades after 3 seconds.

### Accessibility (WCAG 2.2 AA)

Mandatory accessibility features:

- Semantic HTML structure: `<section>` for slides, `<nav>` for navigation, proper heading hierarchy
- `aria-label` on all slides and navigation controls
- `role="progressbar"` on the progress indicator
- Full keyboard operability without requiring a mouse
- `prefers-reduced-motion` media query that disables all transitions, hides particle canvases, and removes staggered delays
- Color contrast ratios of at least 4.5:1 for body text and 3:1 for large text
- Visible focus indicators on all interactive elements
- Touch targets at least 24x24 CSS pixels

### Performance

- Animate only `transform` and `opacity` (GPU-composited properties)
- Use `will-change` sparingly, only on elements about to animate
- Throttle scroll and mousemove event handlers
- Disable particle systems, parallax, and canvas effects on mobile (`@media (max-width: 768px)`)
- Keep total file size under 100KB for text-only presentations

### CSS Gotcha

Never negate CSS functions directly. Writing `-clamp(...)` is silently ignored by browsers with no error. Always use `calc(-1 * clamp(...))` instead.

---

## Animation Patterns

**Entrance animations** trigger when slides scroll into view via Intersection Observer:

- **Fade + Slide Up** (default): Elements start invisible and 30px below, then animate to visible at their natural position. This is the workhorse — use it for most content.
- **Scale In**: Elements start at 90% scale and fade in. Good for cards and images.
- **Slide from Left/Right**: Horizontal movement for side-by-side reveals.
- **Blur In**: Elements start blurred and sharpen into focus. Good for dramatic reveals.

**Stagger children** by adding incremental `transition-delay` (0.1s, 0.2s, 0.3s...) to sequential elements within a slide. This creates a cascading reveal effect.

**Background effects** add atmosphere without heavy assets: gradient meshes (layered radial-gradients at low opacity), noise textures (inline SVG data URIs), grid patterns (repeating linear-gradients at 3% opacity), grain overlays (tiny repeating noise patterns).

**Interactive effects** for engagement: 3D tilt cards that respond to mouse position, magnetic buttons that subtly follow cursor proximity, counter animations that count up to a target number, text scramble reveals that cycle through random characters before settling.

---

## Effect → Feeling Quick Reference

**Dramatic/Cinematic**: Slow fades (1–1.5s), large scale transitions, dark backgrounds with spotlights, parallax depth, serif display fonts.

**Techy/Futuristic**: Neon glows, particle systems, grid patterns, monospace accents, cyan/magenta/electric blue palette, glitch effects.

**Playful/Friendly**: Bouncy spring easing, rounded everything, pastels and bright primaries, floating/bobbing motion, large border-radius.

**Professional/Corporate**: Subtle fast animations (200–300ms), clean sans-serif, navy/slate/charcoal, precise alignment, data visualization focus.

**Calm/Minimal**: Near-imperceptible motion, high whitespace, muted palette, serif body text, generous padding, zero decoration.

**Editorial/Magazine**: Strong typography hierarchy, pull quotes, image-text interplay, grid-breaking layouts, serif headlines + sans body, black-and-white with one accent.

---

## Troubleshooting Quick Fixes

**Fonts not loading**: Verify the Fontshare or Google Fonts URL is correct and the font names in CSS match exactly.

**Animations not triggering**: Confirm the Intersection Observer JavaScript is running and that the `.visible` class is being added to slides when they enter the viewport.

**Scroll snap broken**: Check that `scroll-snap-type: y mandatory` is on `html`, and every `.slide` has `scroll-snap-align: start`.

**Content overflows a slide**: Split into multiple slides. Never allow scrolling within a single slide.

**Mobile rendering issues**: Disable heavy effects (particles, canvas, parallax) at the 768px width breakpoint. Test touch/swipe events.

**Slow performance**: Use `will-change` only where needed. Animate only `transform` and `opacity`. Throttle scroll/mousemove handlers. Reduce particle counts on mobile.

---

## How to Use This Guide

**With any AI assistant**: Paste this document (or relevant sections) into your conversation and ask the AI to create a presentation following these guidelines. Example prompts:

- "Using the frontend-slides approach described here, create a 10-slide pitch deck for a fintech startup. I want it to feel Excited/Energized."
- "Convert the content below into an HTML presentation using the Midnight Executive style from this guide: [your bullet points]"
- "Generate 3 style preview HTML files for a calm, minimal conference talk."

**With Claude Code**: Install as a skill at `~/.claude/skills/frontend-slides/` and invoke with `/frontend-slides`.

**Standalone**: Use as a reference while hand-coding or pair-programming HTML presentations.

---

## Version History

- 3.0.0 — Enhanced with WCAG 2.2 accessibility requirements, performance optimization patterns, expanded anti-AI-slop guidelines, height-based responsive breakpoints, image co-design pipeline, CSS gotcha documentation, and universal AI compatibility
- 2.0.0 — Original frontend-slides by @zarazhangrui with 10 style presets, PPT conversion, viewport fitting
- 1.0.0 — Initial release

## License

MIT — Use it, modify it, share it.

## Credits

Original project by [@zarazhangrui](https://github.com/zarazhangrui/frontend-slides). Enhanced version incorporates accessibility guidance from W3C WAI, animation performance patterns from Google's Core Web Vitals research, and design anti-patterns from the frontend-design community.
