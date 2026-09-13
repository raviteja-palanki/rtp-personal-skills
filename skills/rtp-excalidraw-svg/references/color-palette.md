# Color palette reference

Reference revision 1.4.1 — reviewed 13 September 2026.

## Choose one palette deliberately

The earlier main skill and this companion contained different color systems. Both are retained here with distinct roles. Use the current project brand first. For a new unbranded diagram, use the Luminous Pastel palette below; for an existing diagram using the brighter legacy palette, retain its mapping unless a change is requested or required for readability. Do not silently combine “Thinking = Rose Quartz” with “Thinking = Teal” within the same set.

Use two or three semantic families plus neutral as a starting point. A single warning can legitimately have its own color. Additional categories may require additional families. Color is an aid to meaning, so retain labels and avoid color-only distinctions.

## Luminous Pastel — main skill palette

| Family and role | Header/accent | Card background | Dark text |
|---|---|---|---|
| Rose Quartz — thinking | `#D4789B` | `#FFF5F8` | `#8B3A5A` |
| Wisteria — judgment | `#9478B8` | `#F8F5FF` | `#5B3E7A` |
| Honey Amber — craft | `#D4A54A` | `#FFFCF5` | `#7A5A1E` |
| Celadon — evaluation | `#6BA898` | `#F2FAF6` | `#2E6B54` |
| Glacier — technical | `#5A9ABE` | `#F3F9FD` | `#2A5F7A` |
| Coral — agents or risk, as labeled | `#D47B64` | `#FFF7F4` | `#8B4434` |
| Moss — outcomes | `#7BA86C` | `#F5FAF2` | `#3A5E2E` |
| Neutral — structure | As needed | `#FFFFFF` | `#1B1B1F` |

For a small header on one of these saturated fills, `#1B1B1F` is a useful foreground candidate; calculate the actual pair. Do not automatically use white.

## Legacy brighter palette — existing diagram maintenance

The following values preserve the earlier companion. “Header fill” identifies a color role, not permission to place white text on it. Shade inventories vary by family; each does not have exactly six shades.

## Teal — Thinking, Foundation, Starting Points

| Role | Hex | Use |
|------|-----|-----|
| Header fill | `#14B8A6` | Card headers, section bars |
| Darker header | `#0D9488` | Second-tier headers |
| Card background | `#F0FDFA` | Card/section body |
| Chip background | `#CCFBF1` | Tags, labels, skill names |
| Chip border | `#5EEAD4` | Chip stroke |
| Dark text | `#0F766E` | Subtitles on light backgrounds |
| Medium text | `#0D9488` | Chip text, secondary labels |
| Header tint | `#F0FDFA` | Top banner for teal-themed diagrams |

## Purple — Judgment, Decisions, Analysis

| Role | Hex | Use |
|------|-----|-----|
| Header fill | `#8B5CF6` | Card headers |
| Darker header | `#7C3AED` | Second-tier |
| Card background | `#F5F3FF` | Body |
| Chip background | `#EDE9FE` | Tags |
| Chip border | `#C4B5FD` | Stroke |
| Dark text | `#6D28D9` | Subtitles |
| Medium text | `#7C3AED` | Labels |
| Header tint | `#F5F3FF` | Banner |

## Amber — Craft, Output, Production, Gold Standard

| Role | Hex | Use |
|------|-----|-----|
| Header fill | `#F59E0B` | Card headers |
| Darker header | `#D97706` | Second-tier |
| Card background | `#FFFBEB` | Body |
| Chip background | `#FEF3C7` | Tags |
| Chip border | `#FCD34D` | Stroke |
| Dark text | `#B45309` | Subtitles |
| Medium text | `#92400E` | Labels |
| Header tint | `#FFFBEB` | Banner |

## Cyan — Evaluation, Quality, Measurement

| Role | Hex | Use |
|------|-----|-----|
| Header fill | `#06B6D4` | Card headers |
| Card background | `#ECFEFF` | Body |
| Chip background | `#ECFEFF` | Tags |
| Chip border | `#67E8F9` | Stroke |
| Dark text | `#0E7490` | Subtitles |
| Medium text | `#0E7490` | Labels |

## Pink — Agents, Autonomy, Interaction

| Role | Hex | Use |
|------|-----|-----|
| Header fill | `#EC4899` | Card headers |
| Card background | `#FCE7F3` | Body |
| Chip background | `#FCE7F3` | Tags |
| Chip border | `#F9A8D4` | Stroke |
| Dark text | `#9D174D` | Subtitles |
| Medium text | `#9D174D` | Labels |

## Red — Danger, Incidents, Critical, Negative

| Role | Hex | Use |
|------|-----|-----|
| Header fill | `#EF4444` | Card headers |
| Card background | `#FEF2F2` | Body, bad-outcome panels |
| Chip background | `#FEF2F2` | Tags |
| Chip border | `#FCA5A5` | Stroke, bad-outcome border |
| Dark text | `#991B1B` | Subtitles |
| Medium text | `#DC2626` | Labels, warnings |

## Green — Success, Positive, Good Outcome

| Role | Hex | Use |
|------|-----|-----|
| Header fill | `#16A34A` | Rarely used as header |
| Card background | `#F0FDF4` | Good-outcome panels |
| Chip background | `#D1FAE5` | Success tags |
| Chip border | `#86EFAC` | Good-outcome border |
| Dark text | `#065F46` | Subtitles |
| Medium text | `#16A34A` | Labels |

## Neutral — Structure, Containers, Defaults

| Role | Hex | Use |
|------|-----|-----|
| Background | `#FAFAF8` | Default canvas; current project branding may differ |
| Card white | `#FFFFFF` | Default card body |
| Light grey bg | `#F9FAFB` | Subtle differentiation |
| Border | `#E5E7EB` | Structural containers |
| Body text | `#5F6B7A` | Primary body copy |
| Title text | `#1B1B1F` | Headlines, titles |
| Arrow/connector | `#9CA3AF` | Flow lines, arrows |
| Legacy footer tone | `#9CA3AF` | Decorative use only on the default canvas; use body text color for readable metadata |
| Muted text | `#78716C` | Callout body, secondary info |

---

## Contrast checks and use boundaries

Calculated using the WCAG sRGB relative-luminance method, with opaque colors and results rounded to three decimals:

| Pair | Ratio | Consequence |
|---|---|---|
| `#1B1B1F` on `#FAFAF8` | 16.428:1 | Strong text contrast |
| `#5F6B7A` on `#FAFAF8` | 5.191:1 | Meets the 4.5:1 normal-text threshold |
| `#9CA3AF` on `#FAFAF8` | 2.429:1 | Fails normal and large text; use a darker foreground for metadata |
| White on legacy Teal `#14B8A6` | 2.489:1 | Fails even the 3:1 large-text threshold |
| White on legacy Purple `#8B5CF6` | 4.234:1 | Below the normal-text threshold |
| White on legacy Amber `#F59E0B` | 2.148:1 | Fails even large text |
| White on Rose Quartz | 3.018:1 | Requires qualifying large text, not a small header |
| White on Wisteria | 3.725:1 | Requires qualifying large text |
| White on Honey Amber | 2.263:1 | Fails even large text |
| White on Celadon | 2.735:1 | Fails even large text |
| White on Glacier | 3.088:1 | Requires qualifying large text |
| White on Coral | 3.081:1 | Requires qualifying large text |
| White on Moss | 2.742:1 | Fails even large text |

These calculations correct the earlier claim that all palette combinations meet AA. They do not audit every possible pair, opacity, font, or rendering size. Bold weight alone does not turn 16-pixel text into qualifying large text. Check the final scaled size; retain at least 4.5:1 for ordinary text and 3:1 only where the large-text criterion applies.

Colored text on another colored background can be valid when the actual pair works. Likewise, `#86868B` and `#636366` are not universally forbidden colors: their suitability depends on background, purpose, and contrast. Do not rely on faint arrows where the connection itself carries essential information. Keep low-contrast shades for decoration or replace them with an appropriate darker token.

Use the current [W3C contrast guidance](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) for the criterion and [non-text contrast guidance](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html) for meaningful graphical elements.
