# Principles, materials, and spatial practice

## Ten Rams-inspired questions

1. Does innovation solve a relevant problem rather than merely add novelty?
2. Does the product help someone accomplish a useful goal?
3. Does aesthetic quality support the experience?
4. Can people understand its behavior, with suitable guidance where needed?
5. Does it support the work without demanding needless attention?
6. Are capabilities, status, progress and claims honest?
7. Will the design remain maintainable and useful as conditions change?
8. Are consequential details and edge cases addressed?
9. What performance, energy, asset and lifecycle costs can be reduced?
10. What can be simplified without losing meaning or control?

These are digital adaptations, not verbatim quotations or proof that the named designer evaluated an artifact.

## Complementary lenses

Norman: assess first impression, actual behavior and later reflection separately. Alexander: fit patterns to living context rather than assembling a catalog mechanically. Ive: ask whether choices form a coherent whole, without assuming only one good solution exists. Chimero: respect the medium's capabilities—fluidity and accessibility on the web, page boundaries in print, viewing distance on stage.

Tufte: reduce distracting decoration, make comparisons easy with small multiples, and use layering/separation to make evidence legible. A repeated card structure can be exactly right for comparison; do not reject it solely because a model often generates it. White space and borders can carry information about grouping and navigation.

Bringhurst and Butterick provide typography perspectives; type scale, line length and rhythm must still be tested with the real content. The original modular examples 1.25, 1.333 and 1.618 remain possible ratios, not quality proofs. Nathan Curtis and Chimero motivate deliberate spacing; no universal 4/24/64px semantic law follows.

## Material snippets

The original glass-like and depth-card CSS are retained as examples. They are not a reproduction of a proprietary renderer or a measured performance claim. Add solid-background fallbacks, visible focus, readable foreground colors and motion-preference handling when used in an interactive component.

```css
.liquid-glass {
  background: rgba(255, 255, 255, 0.12);
  backdrop-filter: blur(40px) saturate(180%) brightness(1.1);
  border: 1px solid rgba(255, 255, 255, 0.18);
  border-radius: 22px;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.25),
    inset 0 -1px 0 rgba(0, 0, 0, 0.05), 0 8px 32px rgba(0, 0, 0, 0.12);
}
```

```css
.depth-card {
  background: #161618;
  border: 1px solid rgba(255, 255, 255, 0.055);
  box-shadow: 0 0 0 1px rgba(0,0,0,0.3), 0 2px 4px rgba(0,0,0,0.2), 0 12px 24px rgba(0,0,0,0.2);
}
```

The glass example uses 40px blur, saturation/brightness adjustment, a 22px radius and inset/drop shadows. The dark card uses #161618 on a #0A0A0B reference surface with a subtle border and layered shadows. These are alternative material treatments; saying “no shadows” while specifying several would be contradictory.

## Techniques to consider, not defaults

- Bento: asymmetric content groups; original 16–24px gaps and 20–28px radii are examples. Match cells to actual content and meaning.
- Variable type: animate an available weight/width/slant axis only when useful, without layout instability or motion barriers.
- Neubrutalism: strong boundaries, hard shadows and bright colors can suit a chosen identity; the original `border: 3px solid #000; box-shadow: 6px 6px 0 #000` is an example, not a universal developer-tool treatment.
- Noise: use sparingly and inspect the render. An overlay is optional, not a certificate of craftsmanship.
- Motion: anticipation, follow-through and staging can clarify interaction. Delay must not obstruct action; a static accessible state remains necessary.
