# Color relationships, palettes, and perception

Use this reference to generate and inspect a palette. Treat named effects as aids to observation, not a diagnosis of what every viewer feels. Check the result in its actual context.

## OKLCH and practical limits

OKLCH expresses lightness L, chroma C and hue h. L commonly ranges from 0 to 1 (or 0–100%); chroma is nonnegative, with the usable range depending on lightness, hue and target gamut; hue is an angle. It is designed for improved perceptual uniformity, not perfect equality of apparent brightness across all conditions. HSL remains useful syntax but its numeric lightness is not perceptual lightness.

```css
/* Comparable OKLCH lightness; inspect actual gamut and appearance. */
--blue: oklch(70% 0.15 250);
--green: oklch(70% 0.15 155);
--orange: oklch(70% 0.15 55);
--purple: oklch(70% 0.15 300);
```

Starting anchors: near-white L≈0.97–0.98 with very low chroma; dark body text on light L≈0.20–0.25; secondary text L≈0.45–0.55 only after contrast testing. The older L-difference shortcuts of 0.40 for AA and 0.55 for AAA **are not valid contrast tests**. Neither chroma 0.3 nor 0.4 is a universal gamut boundary. Warm/cool hue ranges are rough descriptions and depend on context.

[CSS Color 4](https://www.w3.org/TR/css-color-4/) defines OKLCH and gamut mapping. Choose interpolation and target gamut deliberately; OKLCH interpolation does not guarantee every gradient is vivid, in gamut or free from an unwanted middle color.

## Albers' interaction lenses

- **Simultaneous contrast:** compare a sample against different surrounds; its apparent lightness or hue may change.
- **Quantity:** a thin saturated accent and a large field of the same color have different visual weight. Evaluate area and placement.
- **Transparency and overlap:** inspect the actual composite colors, legibility and layer cues. The software's blending and the viewer's interpretation are related but distinct.
- **Relativity:** a token value stays fixed while appearance changes with neighbors, display and illumination. Evaluate applications as well as swatches.
- **Bezold effect:** changing a repeated element or outline can change the composition's apparent color relationships. Recheck the whole pattern after a palette edit.
- **Deception exercises:** compare one sample on two backgrounds, or adjust surrounds to make two samples appear more alike. Use the result to notice context, not to claim every fixed-token system is inconsistent.
- **Vibrating boundaries:** some strong hue contrasts with weak luminance separation are uncomfortable or hard to resolve. Avoid relying on them for text or essential boundaries; test any expressive use.

These are adaptations of the observational tradition in *Interaction of Color*. A written explanation does not substitute for viewing the experiment.

## Perception concepts: preserve the phenomenon, bound the explanation

**Opponent processing** is a useful background model for chromatic relationships. It does not establish that red/green always creates maximum tension or that blue/yellow inherently signals luxury.

**Warm advancing/cool receding** is a common design observation affected by context, saturation, depth cues and visual conditions. The old one-line retinal-focus and atmospheric explanation was too categorical; do not use it as a universal physiological mechanism.

**Helmholtz–Kohlrausch effect** concerns brightness judgments for chromatic versus achromatic stimuli. It does not establish a universal twofold effect, a fixed dark-mode chroma reduction, or that a WCAG-passing blue necessarily feels lower contrast. Treat perceived brightness, luminance and legibility as distinct.

**Chromatic adaptation** reminds us that ambient conditions and surrounding colors affect appearance. Dark-mode design should be tested independently; it need not always shift blues toward cyan or reds toward orange. Reusing a semantic token with a different theme value is a design choice to verify.

**Gradients and sunset palettes** can evoke atmosphere, continuity or warmth for some audiences. Claims that a particular gradient activates a specific beneficial V1 response, or that sunsets are universally pleasant because of evolutionary safety, are not established by this skill. Use audience evidence rather than those explanations.

The original softer sunset example remains `#FBBF24 → #F472B6 → #818CF8 → #6366F1`; the saturated comparison is `#FF0000 → #FF00FF → #0000FF`. Either may suit a deliberate purpose; “premium” and “cheap” are contextual judgments.

## Build a palette from a seed

1. Convert the actual seed with a reliable color tool; do not treat a remembered approximation for `#2563EB` as its exact conversion.
2. A ten-step lightness scaffold is 0.97, 0.93, 0.87, 0.78, 0.68, 0.55, 0.45, 0.35, 0.25, 0.15. Adjust the steps for their roles.
3. Reduce chroma as needed near gamut limits. Even at L=0.97, the usable chroma depends on hue and display; the old 0.04–0.06 range is only an example.
4. Optional hue shifts of a few degrees can refine the scale. Adding five degrees does not always mean “warmer,” and subtracting five does not always mean “cooler.” Inspect the hue itself.
5. Try tinted neutrals around C=0.01–0.02 where they serve the identity, then compare against neutral grays.
6. Map colors to semantic roles and test every meaningful foreground/background/state pair under the applicable contrast method. APCA Lc 75/60/45 were earlier examples, not universal body/heading/decorative pass thresholds.
7. Check light/dark themes, color-vision differences, overlays, disabled states, and exported or printed appearance as relevant.

The original twelve semantic roles remain useful: bg-primary/secondary/tertiary; text-primary/secondary/tertiary; border-primary/secondary; accent-primary/muted; status-success/error. Use enough roles for the product rather than an arbitrary minimum token count.

[Radix's twelve-step scale](https://www.radix-ui.com/colors/docs/palette-composition/understanding-the-scale) assigns intended uses and qualified pairings. Its stated APCA Lc60/Lc90 relationship concerns steps 11/12 over step 2 in the same scale; it is not a guarantee for arbitrary combinations. shadcn and Tailwind are other implementation approaches, with version-specific conventions.

## Brand discipline and palette stories

A recognizable accent benefits from deliberate restriction, consistent semantic use, appropriate contrast and repeated association. Theme variants and functional status colors can coexist with that identity. The old claim that every strong interface uses exactly 70/20/10 color area is unsupported; retain that ratio only as an optional composition exercise.

Reference examples from the original skill include Stripe purple/navy (`#635BFF`, `#0A2540`), Spotify green (`#1DB954`), Ferrari red, Claude terracotta/paper (`#C96442`, `#F5F4ED`), Linear dark neutral (`#0A0A0B`), and warm Notion versus cool Linear neutrals. These are illustrative interpretations, not newly checked current brand tokens or proof that a color causes trust, focus or exclusivity. The company snapshot may describe a different date, route or palette; check before resolving a discrepancy.

An optional progression is welcome `#FFF7ED + #F97316`, setup `#F8FAFC + #3B82F6`, completion `#FFFBEB + #F59E0B`, then neutral main application. Keep action and status meanings stable throughout; a color story must not make the same control change meaning unpredictably.

The original palette alternatives remain useful: warm/cool balance, restrained monochrome, dark galleries with vivid imagery, and metallic-style gradient cards. None is inherently better for all audiences.

## Gradient and material recipes

**Aurora/mesh:** overlapping radial gradients can create atmosphere. Example palettes:

- Enterprise: `#635BFF`, `#0A2540`, `#00D4AA`, `#80E9FF`.
- Cool: `#7B68EE`, `#4ECDC4`, `#45B7D1`, `#96CEB4`.
- Warm: `#FF6B95`, `#FECA57`, `#FF9FF3`, `#F368E0`.

The legacy recipe used 30–50% layers on dark, blur around 60px and optional contrast/saturation adjustments. These are starting values. A CSS approximation is not verified evidence of Stripe's current WebGL implementation.

**Grain:** an SVG feTurbulence overlay around 0.02–0.04 opacity can add subtle texture; 0.08–0.15 is more pronounced. Test blending, contrast and performance. Noise may mask visible banding but does not guarantee its removal, and every gradient does not need grain.

**Glass:** backdrop blur around 24px with saturation adjustment and a subtle border can define a floating surface. Two or three layers may already be visually or computationally excessive. Check the actual composition rather than treating layer count as a performance proof.

**Depth:** a gentle top highlight, such as `linear-gradient(180deg,rgba(255,255,255,0.04),transparent)`, can suggest a surface. Stronger hierarchy may need a boundary or shadow. Context determines whether lighter appears nearer.

**Interpolation:** two to four stops and moderate hue travel are reasonable experiments, not universal quality thresholds. Inspect the chosen shorter/longer hue path and gamut; complementary stops need not be categorically forbidden.

**Display P3:** can represent some colors outside sRGB. Do not describe this as an exact 25% increase in the number of colors a person sees. Supply a deliberate sRGB fallback and test the target display:

```css
.hero { background: #635BFF; }
@supports (color: color(display-p3 1 0 0)) {
  @media (color-gamut: p3) {
    .hero { background: color(display-p3 0.35 0.33 1); }
  }
}
```

The two sample values are different authored colors, not a claimed exact conversion. Check visual continuity and contrast in both paths.
