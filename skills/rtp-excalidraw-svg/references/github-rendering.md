# SVG portability and GitHub review

Reference revision 1.4.1 — reviewed 13 September 2026.

Use a conservative static SVG profile for a diagram that must travel between README images, browsers, presentation tools, and exports. That is a portability choice; it is not a list of everything the SVG standard permits.

## Build a dependable static image

Prefer basic shapes, paths, text, spans, groups, local definitions, and explicit presentation attributes. Include `xmlns="http://www.w3.org/2000/svg"`, a meaningful `viewBox`, and suitable dimensions or a deliberate host sizing rule. An SVG without explicit width and height does not inevitably render at zero size, but undefined sizing can cause inconsistent presentation.

Use six-digit hex plus separate opacity when that improves exporter compatibility:

| Original alpha notation | Portable split, rounded |
|---|---|
| `#00000010` | `fill="#000000" fill-opacity="0.063"` |
| `#00000018` | `fill="#000000" fill-opacity="0.094"` |
| `#00000020` | `fill="#000000" fill-opacity="0.125"` |
| `#9478B830` | `fill="#9478B8" fill-opacity="0.188"` |

For a shadow, use `flood-color` and `flood-opacity` instead of the fill attributes. The alpha byte is divided by 255; values shown above are rounded approximations. A decorative shadow may use:

```xml
<filter id="shadow" x="-10%" y="-15%" width="125%" height="140%">
  <feDropShadow dx="2" dy="3" stdDeviation="4"
                flood-color="#000000" flood-opacity="0.09"/>
</filter>
```

Check filter bounds and the rendered result. Keep borders or background separation sufficient if a filter disappears. A simple offset rectangle is an alternative shadow:

```xml
<rect x="102" y="102" width="270" height="170" rx="14" fill="#E5E7EB" opacity="0.3"/>
<rect x="100" y="100" width="270" height="170" rx="14" fill="#FFFFFF" stroke="#E5E7EB" stroke-width="1.5"/>
```

## Separate validity from destination support

SVG supports CSS styles, classes, and presentation attributes; [the SVG 2 styling specification](https://www.w3.org/TR/SVG2/styling.html) explains their roles. Eight-digit hex and `rgba()` are valid color notations under [CSS Color 4](https://www.w3.org/TR/css-color-4/). Their presence alone is not proof that a file is invalid or will fail on GitHub.

Scripts, event handlers, external styles or fonts, external `<use>` references, `<foreignObject>`, filters, and animation can behave differently when the same SVG is opened as a document or embedded as an image. Avoid relying on active behavior for a static explanation. Do not assume a list of sanitizer behavior from an old incident applies to every GitHub image route.

`<marker>` is a valid arrow mechanism; polygons are a useful fallback. A namespace declaration such as `xmlns:xlink` is not inherently a parse error: remove it only when unused, or migrate related attributes coherently. Emoji depend on font and renderer support; replace them if inconsistent, rather than asserting they always work or always fail. Use SVG geometry for corners (`rx`/`ry`), not an HTML box's `border-radius` as a substitute.

## Embed and verify

GitHub documents support for SVG in its [non-code file guidance](https://docs.github.com/en/repositories/working-with-files/using-files/working-with-non-code-files). Use a repository-relative image link where suitable:

```markdown
![Thinking informs judgment, which guides the final artifact.](01-overview.svg)
```

A raw URL with `?sanitize=true` is not a universal fix or a guarantee of rendering. Confirm the committed asset path and the actual README preview when GitHub delivery is part of the task. A local preview verifies local rendering only; do not publish merely to run a check if publication is outside the request.

For inline or standalone SVG, give the image an accessible name and description:

```xml
<svg xmlns="http://www.w3.org/2000/svg" role="img"
     aria-labelledby="diagram-title diagram-description"
     viewBox="0 0 1200 600" width="1200" height="600">
  <title id="diagram-title">From question to artifact</title>
  <desc id="diagram-description">Thinking clarifies the question. Judgment selects an approach. Craft produces the artifact and its verification record.</desc>
</svg>
```

Use unique IDs when multiple inline SVGs share a page. The snippet demonstrates metadata, not a complete visible diagram. For `<img>` embeds, provide host `alt` text and a nearby longer text explanation when the content requires it. Avoid hard-coded historical skill counts unless the current inventory has been checked.

Escape `&`, `<`, and attribute quotes correctly. Unicode arrows and mathematical symbols are valid when the chosen font supports them. Check the XML with an available parser, then inspect every modified SVG at its intended display size. A search for portability-sensitive constructs can guide review; a matched pattern is not automatically a defect and an empty search is not proof of rendering correctness.

For a related set, divide by reader question, use descriptive ordered filenames, and preserve semantic color mappings. Add enough views to explain the material without imposing a six-diagram quota.
