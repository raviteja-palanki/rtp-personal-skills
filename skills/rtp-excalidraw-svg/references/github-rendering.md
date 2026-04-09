# GitHub SVG Rendering Reference

## What Works on GitHub
- `<img src="filename.svg">` in README (relative paths)
- `<img>` tags with `?sanitize=true` for raw URLs
- Basic shapes: `<rect>`, `<circle>`, `<ellipse>`, `<line>`, `<path>`, `<polygon>`
- `<text>`, `<tspan>` with inline attributes
- `<g>` grouping with transforms
- `viewBox` + responsive sizing
- Inline `style` attributes on elements

## What GitHub Strips (SVG Sanitizer)
- `<script>` tags — completely removed
- `<foreignObject>` — stripped (no HTML-in-SVG)
- Event handlers (`onclick`, `onmouseover`)
- External CSS `<link>` references
- `<use>` with external href
- CSS animations and `@keyframes` inside `<style>` blocks
- `<filter>` elements MAY be stripped — test your specific filter

## Shadow Filter Fallback
If `<filter>` is stripped by GitHub, shadows disappear silently. Fallback:
```xml
<!-- Instead of filter="url(#s)", use a visible stroke as shadow substitute -->
<rect x="102" y="102" width="270" height="170" rx="14" fill="#E5E7EB" opacity="0.3"/>
<rect x="100" y="100" width="270" height="170" rx="14" fill="#FFFFFF" stroke="#E5E7EB" stroke-width="1.5"/>
```

## Embedding SVGs in README
```markdown
<img src="01-architecture-overview.svg" alt="Architecture Overview" width="100%">

<!-- For raw GitHub URLs -->
<img src="https://raw.githubusercontent.com/user/repo/main/diagram.svg?sanitize=true" alt="Diagram">
```

**Always set `alt` text** that describes the diagram's key takeaway, not its structure.

---

## Accessibility

### Baseline SVG Accessibility (Always Include)
```xml
<svg xmlns="http://www.w3.org/2000/svg" role="img"
     aria-label="{ONE_SENTENCE_TAKEAWAY}"
     viewBox="0 0 1200 {HEIGHT}" width="1200" height="{HEIGHT}">
  <title>{DIAGRAM_TITLE}</title>
  <desc>{2-3 sentence description of what the diagram shows and its key insight}</desc>
</svg>
```

- `role="img"` tells screen readers this is one image, not a tree of shapes
- `<title>` = the diagram's heading (matches the visible title)
- `<desc>` = what a colleague would say if describing this diagram out loud
- `aria-label` = the one-sentence takeaway for quick scanning

### Text Summary Below Embedded SVGs
```markdown
<img src="01-overview.svg" alt="Three-layer architecture: thinking feeds judgment, judgment feeds craft">

> **Visual summary:** The system uses three layers — Thinking (7 foundational skills),
> Judgment (25 domain plugins), and Craft (8 output skills).
```

---

## Text Encoding & Special Characters

- `&` → `&amp;`, `<` → `&lt;`, `>` → `&gt;`
- Quotes in attributes: use `&quot;` or switch quote style
- Emoji: work in SVG `<text>` but increase file size — use sparingly
- Math symbols: use Unicode directly (`→`, `×`, `≤`)
- Monospace: `font-family="Consolas, Monaco, monospace"` — only for code literals inside callout boxes

---

## Multi-Diagram Strategy

When content is too rich for one SVG:

1. **Break by story, not by data.** Each SVG = one narrative.
2. **Name sequentially:** `01-overview.svg`, `02-detail.svg`, `03-example.svg`
3. **Each stands alone.** Viewer should understand without seeing others.
4. **Consistent color mapping.** Teal = thinking in diagram 1 → teal = thinking everywhere.
5. **Maximum 6 diagrams per set.** More than that = architecture needs simplification.
