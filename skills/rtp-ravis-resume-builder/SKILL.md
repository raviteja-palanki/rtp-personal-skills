---
name: rtp-ravis-resume-builder
version: v1.0.1_latest
description: 'Update or rebuild Ravi Teja Palanki’s professional resume using its existing ReportLab script, A4 two-column layout, Lato typography, and teal visual identity. Use for experience, portfolio, competencies, credentials, contact details, links, spacing, or a new resume PDF version; also use when Ravi asks to recreate or improve his uploaded resume. Read the current build script and latest approved content before editing. Preserve factual distinctions and the established design unless the request changes them. Check font availability, text fit, hyperlinks, and the rendered PDF; printed diagnostic output alone does not establish visual quality. The skill includes the layout, palette, helper functions, edit patterns, and historical content cautions. It is specific to Ravi’s resume, not a general resume-writing or document-formatting skill.'
---
# Ravi's resume builder

Produce or update Ravi Teja Palanki's resume with accurate content and a clean, readable PDF. The existing implementation is [scripts/build_resume.py](scripts/build_resume.py), which draws directly with ReportLab's canvas API. It is the source of the current layout and stored content; Ravi's latest approved facts and requested changes take precedence over an older script snapshot.

This resume intentionally uses **Lato and teal**, an established exception to the general four-font personal brand. Preserve that identity unless Ravi asks for a redesign. A new skill version is separate from the resume PDF's version number.

## Start with the requested change

Read the whole current script and the latest approved resume or supplied PDF. Identify the intended output version, content changes, and destination from context. For a simple URL correction, change its named constant and regenerate; do not rewrite unrelated career content.

Before a rebuild, distinguish employment, fellowship, advisory work, personal projects, and hypothetical examples. Preserve exact dates, ownership, scope, and supported outcomes. “Revenue opportunity” is not realized revenue; a team patent is not automatically Ravi's individual patent; all enterprise experience is not AI experience. Do not infer current credentials, subscriptions, job titles, or usage metrics from a stale snapshot.

The bundled script currently reflects April 2026 content, including **66 skills, three layers, and five plugins**. These are historical values, not current inventory. Read the current registry before revising that portfolio description; the September 2026 library pass has 90 active skills and a separate retired redirect. Preserve source-backed accomplishments and ask only about consequential facts that cannot be resolved from Ravi's records.

## Build and inspect

```bash
python3 "<skill-path>/scripts/build_resume.py" "<output-path>/Raviteja_Palanki_AI_PM_Resume_v<VERSION>.pdf"
```

Replace the placeholders with actual paths and the intended resume version. Keep the previous approved PDF and source available for recovery. The script accepts the output path as its first argument; without one it uses `RESUME_OUTPUT_PATH` or an unversioned default. Supply an explicit filename for a reviewed deliverable.

1. Confirm Python, ReportLab, and the actual Lato font files are available. The script's `/usr/share/fonts/truetype/lato/` path is a Linux assumption, not a portable default. Locate fonts on the current host and update the configuration deliberately if needed.
2. Make the requested content or layout change. Keep URLs in the `URL_*` constants and use the drawing helpers consistently.
3. Generate the PDF and read the boundary/proportion diagnostics. Fix overflow and inspect unexpected imbalance.
4. Render every page and inspect the real PDF at readable scale and intended A4 print size. Check clipping, overlaps, glyphs, column order, spacing, small text, badges, and footer.
5. Inspect text extraction and link annotations. Every displayed website link should target the intended URL and have a correctly placed clickable area. `draw_link()` creates its own annotation; do not duplicate it.
6. Deliver the versioned PDF with a brief description of the changes and the checks actually performed. Report any unresolved font, source-content, or rendering limitation accurately.

The script **prints diagnostics but does not fail the build when a boundary check fails**. Its second pass reports proportions without a pass/fail verdict, and “Saved” only means a PDF was written. Neither check establishes visual quality, accessible reading order, a live destination URL, or reliable applicant-tracking-system extraction. Do not promise “pixel-perfect,” universal Unicode support, or universal ATS compatibility.

## Preserve the established layout

| Element | Existing setting | How to use it |
|---|---|---|
| Paper | A4, approximately 595.28×841.89pt | Keep by default; a different page size requires a layout revision and new checks |
| Margins | Left/right 42pt; top 36pt; bottom 28pt | Preserve the content and footer clearance |
| Columns | Content about 511pt; left 312pt; gap 17pt; right about 182pt | Right column starts at x=371pt |
| Footer | y=32pt | Column text should end above footer+20pt, or y=52pt |
| Balance | Column end difference below 50pt | A design target, not a reason to pad or delete useful content mechanically |

**Header:** 24pt bold name; right-aligned 7.5pt contact; 10.5pt italic teal subtitle; tagline; three credential badges; LinkedIn and website links; rule.

**Profile:** three short bullets using 7.5pt text/10pt leading, the advisory-board line and TAPMI programme link, then a rule. Preserve the intended meaning without inventing evidence to fit three bullets.

**Left column:** Honeywell with four product/role blocks, Brillio, then Tata Motors, as represented in the approved chronology. Each block includes company/date, context, bold role/date, optional tag, italic organization, bullets, and a link row. The reference sizes are 9.5pt company, 8pt role, 7–7.5pt context/date, 6.5pt organization, 6.8pt bullets with 9.2pt leading, and 5.8pt links.

**Right column:** AI Portfolio → Tool Stack → Competencies → Certifications → Education. The stored layout contains three portfolio items, four tool rows, wrapping tags, certification list, TAPMI MBA/LADC, and NIT B.Tech. Add, remove, or reorder items when requested; these counts are a snapshot, not a content limit.

**Footer:** Ravi's name and a linked profile URL. Preserve the correct spelling and preferred public name from the approved resume.

The existing design is compact. Its 5.8–7.5pt content is not a general recommendation for readable resumes. When more content is needed, first edit for relevance or adjust layout; consider a second page or a requested alternative layout before shrinking essential text. A two-column visual layout requires checking extracted reading order.

## Fonts and visual elements

| Font file / registered name | Role |
|---|---|
| Lato Regular / `F`, `Lato` | Body, descriptions, links |
| Lato Bold / `FB`, `LatoB` | Name, titles, headers, badge text |
| Lato Italic / `FI`, `LatoI` | Subtitle and organization names |
| Lato Semibold / `FSB`, `LatoSB` | Available option |
| Lato Light / `FL`, `LatoL` | Registered but not currently used |

Check the actual font files for arrows, middle dots, registered/trademark marks, dashes, and any newly added characters. Lato does not cover every Unicode character. A font change may affect glyph coverage and wrapping; it does not inevitably break Unicode. Font substitution requires a deliberate design decision and a new render check.

Draw the established experience bullets with `bullet_dot()` and pill tags with `tag()`. The certifications intentionally use a middle-dot character; the old blanket prohibition on Unicode bullets did not describe that implementation. Both drawn and text bullets must render and extract sensibly.

## Palette and contrast

| Purpose | Color |
|---|---|
| Primary / links | Deep teal `#1B5E5E`; mid teal `#237878` |
| Text hierarchy | `#1A1A1A`, `#2D2D2D`, `#5A5A5A`; legacy footer `#999999` |
| Structure | Light teal `#ECF6F6`; rule `#D0D0D0` |
| Credential badges | Perplexity teal `#1B5E5E`; Lovable gold `#C9962A`; Salesforce blue `#0176D3` |
| PRO label | Background/text `#E4F0F0` / `#237878` |
| MAX label | Background/text `#FFF5E0` / `#8B6914` |

Keep the Salesforce badge blue rather than switching it to red. The original badge helper uses white text for all fills, but **white on the gold fill is about 2.67:1** and fails normal-text AA contrast. When producing a revised PDF, use a verified dark-text gold treatment or another approved accessible treatment. `#999999` on white is about 2.85:1 and is also unsuitable for essential small text. Brand fidelity includes readable use of the color, not preservation of an inaccessible pairing.

## Common edits

- **URL:** edit the named constant and check both the displayed label and annotation. A product page and a press release should not be presented as two distinct sources if both constants resolve to the same page.
- **Portfolio text:** locate the portfolio section by name, not an obsolete line number. Wrap to `RIGHT_W`; a long unbroken word can exceed the current helper's width despite wrapping.
- **New role:** follow title/date/tag → organization → `draw_bullet()` → `links_row()` → spacing. Recheck all following coordinates.
- **New portfolio item:** use title, wrapped description and link row; the examples in [the implementation reference](references/implementation-reference.md) preserve the existing calls.
- **Competency or certification:** update the appropriate list and inspect actual wrapping and length. The tag-flow width estimate is approximate; a long tag may still overrun.
- **Column balance:** adjust the right-column section gaps, historically around 24/12/24/12pt. Inspect the whole page rather than chasing equal bottoms at the cost of readability.

The [implementation reference](references/implementation-reference.md) retains all ten helper signatures, URL names, and portfolio edit examples. Its content snapshots are historical, not newly verified professional claims.

Editorial revision: September 13, 2026. The build script was read in full to make these instructions accurate; this wording pass does not itself revise or regenerate Ravi's professional resume.
