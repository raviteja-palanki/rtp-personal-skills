# Optional borders and LinkedIn cover reference

These treatments were recorded for Ravi's personal collateral. Use them only when the current brief permits; they do not override website series locks, a client identity, the resume system or a teaching palette. A border is optional, not proof that an artifact carries the brand correctly.

## Five-segment personal bar

Colors in order: #8B5CF6 purple, #14B8A6 teal, #06B6D4 cyan, #F59E0B amber, #EC4899 pink. Equal segments; for a 1200px canvas each is 240px. The original sizing guidance is 6–8px height on large canvases and 4–5px near 800px; adapt to final placed size. An optional bottom bar uses about 20% opacity.

```xml
<rect x="0" y="0" width="20%" height="6" fill="#8B5CF6"/>
<rect x="20%" y="0" width="20%" height="6" fill="#14B8A6"/>
<rect x="40%" y="0" width="20%" height="6" fill="#06B6D4"/>
<rect x="60%" y="0" width="20%" height="6" fill="#F59E0B"/>
<rect x="80%" y="0" width="20%" height="6" fill="#EC4899"/>
```

## Three restrained gradient options

These preserve the prior violet, cyan/violet and neutral-slate choices, formerly called Warm Professional, Cool Executive and Neutral Authority. The labels describe intended mood, not measured psychological effects. The stops reduce opacity but do not actually reach fully transparent. Define each gradient in SVG defs with a unique ID, then reference it from the intended border shape.

```xml
<linearGradient id="border" x1="0%" x2="100%">
  <stop offset="0%" stop-color="#6366F1" stop-opacity="0.8"/>
  <stop offset="50%" stop-color="#8B5CF6" stop-opacity="0.6"/>
  <stop offset="100%" stop-color="#A78BFA" stop-opacity="0.4"/>
</linearGradient>
```

```xml
<linearGradient id="border" x1="0%" x2="100%">
  <stop offset="0%" stop-color="#0EA5E9" stop-opacity="0.7"/>
  <stop offset="50%" stop-color="#6366F1" stop-opacity="0.5"/>
  <stop offset="100%" stop-color="#8B5CF6" stop-opacity="0.3"/>
</linearGradient>
```

```xml
<linearGradient id="border" x1="0%" x2="100%">
  <stop offset="0%" stop-color="#64748B" stop-opacity="0.6"/>
  <stop offset="100%" stop-color="#94A3B8" stop-opacity="0.3"/>
</linearGradient>
```

## LinkedIn profile cover

[LinkedIn’s current help](https://www.linkedin.com/help/linkedin/answer/a568217/?lang=en-US), checked September 13, 2026, recommends 1584×396 pixels, JPG or PNG, smaller than 8MB. It states appearance varies with browser window and screen resolution. Therefore the prior fixed 568×264 photo overlap and x=300–1300/y=20–300 “all devices” safe zone are **not verified universal bounds**; they also overlap in part. Preview the actual profile on the relevant desktop/mobile layouts.

The April 2026 design snapshot was white with the five-color top bar, “Think > Judge > Ship” in Inter 76px/800, colored word underlines, forward chevrons and a return arc from Ship to Think, plus “AI PRODUCT MANAGER” at 24px/600 in #6B7280 and an optional faded bottom bar. It used a content center around x=810 and reserved generous lower space. Those are historical design coordinates, not platform requirements or a newly checked current banner.

Start with a short readable headline (the old range was 60–76px, roughly three to five words) and supporting line around 20–24px. Check their final mobile size and cropping. JPEG quality 95 and a 200KB target were local export preferences, not LinkedIn requirements; prioritize legibility within the actual size limit.

## Produce and check the artifact

Use the actual editable SVG or design source when it exists. A Pillow redraw is a separate raster implementation, not an SVG export, and should be labeled accordingly. The old sample only drew the bars after loading fonts; it did not render the promised headline, subtitle, underlines or arrows. Do not present it as a complete banner generator.

When implementing a dedicated renderer, expand a user-font path before loading it, inspect the font's actual variation axes rather than assuming their order, measure and draw the real text, and render every intended element. For example, `Path(font_path).expanduser()` resolves a tilde; axis settings must follow the font's reported axis names and bounds. Verify installed dependencies and licensing before use.

For five raster segments, use adjacent integer boundaries from `round(i * width / 5)` to `round((i + 1) * width / 5) - 1`; this avoids overlapping inclusive rectangle endpoints. Composite the optional bottom bar onto the actual background instead of treating an RGB color as though it carried opacity.

Inspect the exported image, dimensions, file size, text contrast and crop previews. Preserve an editable source and versioned output. A historic destination was `~/Desktop/Claude/linkedin-cover.jpg`; use the user’s current requested destination and avoid overwriting the only approved copy. Upload or replace the public profile cover only when that action is authorized. Current interface labels can change; use the actual LinkedIn cover controls rather than a stale settings path.
