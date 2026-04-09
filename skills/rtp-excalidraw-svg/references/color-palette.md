# Color Palette Reference

## The Excalidraw-Inspired Pastel System

Eight semantic color families. Each has 6 shades for different roles.

### Selection Rule

Pick 2-3 primary families per diagram. Use neutral for structure. One family gets emphasis (saturated header bars), others get supporting roles (card backgrounds, chips).

---

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
| Background | `#FAFAF8` | ALWAYS the SVG background |
| Card white | `#FFFFFF` | Default card body |
| Light grey bg | `#F9FAFB` | Subtle differentiation |
| Border | `#E5E7EB` | Structural containers |
| Body text | `#5F6B7A` | Primary body copy |
| Title text | `#1B1B1F` | Headlines, titles |
| Arrow/connector | `#9CA3AF` | Flow lines, arrows |
| Footer text | `#9CA3AF` | Attribution, meta |
| Muted text | `#78716C` | Callout body, secondary info |

---

## Accessibility Notes

All color combinations meet WCAG AA contrast ratio:
- `#1B1B1F` on `#FAFAF8` = 15.8:1 (AAA)
- `#5F6B7A` on `#FAFAF8` = 5.2:1 (AA)
- `#FFFFFF` on `#14B8A6` = 3.2:1 (AA Large Text — headers only)
- `#FFFFFF` on `#8B5CF6` = 4.6:1 (AA)
- `#FFFFFF` on `#F59E0B` = 2.5:1 (AA Large Text — use 700+ weight)

For white-on-color headers, always use font-weight 700+ and size 16px+ to qualify as "large text" under WCAG.

---

## Anti-Patterns

- Never use `#86868B` (medium grey) as text on dark backgrounds — this is the old unreadable pattern
- Never use `#636366` for anything the user needs to read
- Never put colored text on colored backgrounds (e.g., purple text on teal bg)
- Never use more than 3 color families + neutral in one diagram
- Never use a color family for just one element — if it appears, it should appear at least 2-3 times
