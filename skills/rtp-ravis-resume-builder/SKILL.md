---
name: ravis-resume-builder
description: >
  Pixel-perfect PDF resume generator for Raviteja Palanki (Ravi). Produces an Apple-quality,
  A4, two-column resume using ReportLab with Lato font and full Unicode support.
  Use this skill whenever the user asks to update, rebuild, regenerate, or modify Ravi's resume
  — including content edits, URL changes, adding/removing experience roles, updating portfolio
  items, changing competencies, or tweaking layout spacing. Triggers on "update my resume",
  "rebuild resume", "generate resume PDF", "change resume content", "new resume version",
  "fix resume link", "add to my resume", "resume v17", "update portfolio on resume", or
  any reference to modifying Ravi's professional resume. Also triggers when the user uploads
  a resume PDF and asks to recreate or improve it. Do NOT use for creating resumes for other
  people or for general document formatting unrelated to Ravi's resume.
---

# Ravi's Resume Skill Builder

You are generating Ravi Teja Palanki's professional resume as a pixel-perfect PDF. The resume
is built programmatically with ReportLab's canvas API — there is no template file. The Python
script `scripts/build_resume.py` in this skill's directory IS the single source of truth.

## Quick Start

To regenerate the resume with no changes:

```bash
python3 <skill-path>/scripts/build_resume.py <output-path>
```

To make changes, edit the script, then run it. The script includes a built-in design review
that prints boundary checks and proportion metrics — both passes must show checkmarks before
you ship.

## Design System — The Rules That Matter

These design decisions were arrived at through many iterations of feedback. They exist for
specific reasons and should not be changed casually.

### Paper & Font

**A4 (595.28 x 841.89 pt)** — Indian standard. The extra height over US Letter gives the
layout breathing room that prevents the footer from colliding with content. Switching to
Letter will break the layout.

**Lato** — A Google Font with full Unicode coverage. The resume uses arrows (↗ →), middle
dots (·), registered marks (® ™), em dashes (—), and more. Previous attempts with Helvetica
and DejaVu Sans either broke Unicode rendering or looked unprofessional. Lato is the only
font that passed both the visual quality and Unicode reliability tests.

Font files live at `/usr/share/fonts/truetype/lato/`. The script registers five weights:

| Weight | Variable | Usage |
|---|---|---|
| Regular | `F` / `"Lato"` | Body text, descriptions, links |
| Bold | `FB` / `"LatoB"` | Names, titles, section headers, badge text |
| Italic | `FI` / `"LatoI"` | "AI Product Leader" subtitle, org names |
| Semibold | `FSB` / `"LatoSB"` | Available but rarely used |
| Light | `FL` / `"LatoL"` | Available but not currently used |

### Colour Palette

The palette was matched from the original v15 brand identity. The teal tones are the
primary accent; gold and blue are badge-specific.

```
Primary accents:
  Deep Teal   #1B5E5E   Section headers, underlines
  Mid Teal    #237878   Links, subtitle, bullet dots

Text hierarchy:
  Black       #1A1A1A   Name, company names, role titles
  Dark Gray   #2D2D2D   Body text, bullet content
  Mid Gray    #5A5A5A   Dates, secondary descriptors, right-column descriptions
  Light Gray  #999999   Footer name text

Structural:
  Light Teal  #ECF6F6   Tag/pill backgrounds
  Rule Color  #D0D0D0   Horizontal divider lines

Badge fills (white text on coloured background):
  Teal        #1B5E5E   Perplexity AI Business Fellow
  Gold        #C9962A   Lovable L4 Platinum Builder
  Blue        #0176D3   Salesforce Agentforce Specialist (brand blue — NOT red)

Tool labels:
  PRO bg/text  #E4F0F0 / #237878
  MAX bg/text  #FFF5E0 / #8B6914
```

### Layout Grid

```
Margins:    42pt left, 42pt right, 36pt top, 28pt bottom
Content:    ~511pt wide
Left col:   312pt (Experience)
Gap:        17pt
Right col:  ~182pt (Portfolio, Tools, Competencies, Certs, Education)
Right X:    ML + LEFT_W + GAP = ~371pt
Footer Y:   32pt from bottom
```

### Visual Elements

**Bullets**: Small filled teal circles drawn with `canvas.circle()`. Do NOT use Unicode
bullet characters — they render inconsistently across PDF viewers.

**Tags/Pills**: Rounded rectangles (`roundRect`) with light teal background and teal text.
Used for competencies and tech labels (e.g., "Salesforce", "Azure AI Foundry", "React + .NET").

**Badges**: Rounded rectangles with coloured fills and white bold text. Used in the header
for credentials.

**Links**: Teal text prefixed with the ↗ arrow character, with a thin teal underline.
Clickable via `linkURL()`. Every visible link must also be a clickable hyperlink.

## Page Structure

The resume flows top to bottom in this exact order:

### 1. Header (full width)
- Name: 24pt Bold, left-aligned
- Contact: 7.5pt Regular, right-aligned (phone, email, city)
- Subtitle: "AI Product Leader" in 10.5pt Italic teal
- Tagline: "Ships Reliable, Human-Centered AI Products at Scale · 0-to-1 Builder · 12+ Years Enterprise B2B"
- Three credential badges in a row (Perplexity, Lovable, Salesforce)
- LinkedIn + Website links
- Thin horizontal rule

### 2. Profile (full width)
- Three bullet points summarizing career (7.5pt, 10pt leading)
- "Advisory Board Member" line with inline TAPMI Programme link
- Thin horizontal rule

### 3. Two-Column Layout

**Left Column — EXPERIENCE**

Each company block follows this pattern:
```
COMPANY NAME  year–year          (9.5pt Bold + 7.5pt date)
Role description                  (7pt Regular)
  Role Title — Context  year      (8pt Bold + 7pt date + optional tag)
  Org Name (italic)               (6.5pt Italic gray)
  · Bullet point                  (6.8pt, 9.2pt leading)
  · Bullet point
  ↗ Link  ↗ Link                  (5.8pt teal)
```

Companies in order: Honeywell (4 sub-roles), Brillio, Tata Motors.

**Right Column** (sections separated by 12-24pt gaps)

1. **AI Portfolio** — Three items, each with bold title, gray description, and teal link(s)
2. **Tool Stack** — Four rows of tool names with optional PRO/MAX micro-labels
3. **Competencies** — Pill tags that wrap naturally within column width
4. **Certifications** — Simple bullet list with middle-dot prefix
5. **Education** — TAPMI (MBA) with LADC achievement link, NIT (B.Tech)

### 4. Footer
- "Ravi Teja Palanki" left-aligned in light gray
- "ravitejapalanki.com/profile" right-aligned in teal, linked

## URLs

All URLs are defined as constants near the top of the script. When updating a URL, change
ONLY the constant — never hardcode URLs inline in the drawing code.

```python
# Personal
URL_LINKEDIN    = "https://www.linkedin.com/in/ravipalanki/"
URL_WEBSITE     = "https://ravitejapalanki.com"
URL_PROFILE     = "https://ravitejapalanki.com/profile"

# Portfolio
URL_GITHUB      = "https://github.com/raviteja-palanki/rtp-personal-skills"
URL_PP          = "https://productpatterns.in"
URL_PP_GITHUB   = "https://github.com/raviteja-palanki/Patterns"
URL_LEARN       = "https://learn.ravitejapalanki.com"
URL_SUBSTACK    = "https://ravitejapalanki.substack.com"

# Education
URL_TAPMI_AI    = "https://www.tapmi.edu.in/mba-ai/"
URL_LADC        = "https://www.tapmi.edu.in/ladc/"

# Honeywell products
URL_TRACKWISE, URL_DMS, URL_TMS, URL_EU_MIR    (Sparta Systems)
URL_BAT_PROD                                     (Battery MXP)
URL_PI_PROD                                      (Production Intelligence)
URL_WA_PROD, URL_WA_APP                          (Worker Assist)

# Brillio
URL_BRILLIO, URL_BRILLIO_PE
```

## Helper Functions Reference

| Function | What it draws | Key params |
|---|---|---|
| `rrect(c, x, y, w, h, r, fill, stroke)` | Rounded rectangle | r = corner radius |
| `bullet_dot(c, x, y, r=1.2)` | Small teal filled circle | Always use instead of Unicode |
| `tag(c, x, y, text, fs, bg, tc)` | Pill-shaped label | Returns width for flow layout |
| `badge(c, x, y, text, bg, fs)` | Coloured badge, white text | Returns width |
| `sec_hdr(c, x, y, text, line_w)` | Left column section header | Bold + underline |
| `rsec_hdr(c, x, y, text)` | Right column section header | Smaller variant |
| `wrap(c, text, font, fs, max_w)` | Word-wrap to max width | Returns list of lines |
| `draw_bullet(c, x, y, text, max_w, fs, ld, color)` | Bullet + wrapped text | Returns new y |
| `draw_link(c, x, y, text, url, fs)` | ↗-prefixed teal link | Returns text width |
| `links_row(c, x, y, links, fs, gap)` | Row of spaced links | Returns new y |

## How to Make Common Changes

### Update a URL
Find the `URL_` constant at the top. Change the string. Regenerate.

### Update portfolio description
Find the portfolio section (~line 493). Edit the description text. If using multiple lines
for the right column's narrow width, verify each line fits within ~182pt at 6.2pt font size.
You can test widths:
```python
pdfmetrics.stringWidth("your line", "Lato", 6.2)  # must be < 182
```

### Add a new experience role
Follow the existing pattern under the Honeywell section. Each role needs:
1. Bold title + date + optional tech tag
2. Italic org name
3. Bullet points via `draw_bullet()`
4. Links row via `links_row()`
5. Spacing gap (`ly -= 8` typically)

### Add a new portfolio item
In the right column's AI Portfolio section:
```python
c.setFont(FB, 7)
c.setFillColor(BLACK)
c.drawString(RIGHT_X, ry, "Project Name")
ry -= 9.5
for line in wrap(c, "Description here", F, 6.2, RIGHT_W):
    c.setFont(F, 6.2)
    c.setFillColor(MID_GRAY)
    c.drawString(RIGHT_X, ry, line)
    ry -= 8
draw_link(c, RIGHT_X, ry, "Link Text", URL_VAR, fs=5.8)
ry -= 16
```

For two links side-by-side:
```python
lx = RIGHT_X
tw = draw_link(c, lx, ry, "First", URL_1, fs=5.8)
lx += tw + 5
draw_link(c, lx, ry, "Second", URL_2, fs=5.8)
ry -= 16
```

### Add a competency tag
Add the string to the `comps` list. The flow layout handles wrapping automatically.

### Add a certification
Add the string to the certifications list. Each cert gets a middle-dot prefix.

### Adjust column balance
If one column grows significantly longer, tune the `ry -= N` gaps between right-column
sections. The key tuning points (in order):
- After AI Portfolio → Tool Stack (currently ~24pt gap)
- After Tool Stack → Competencies (currently ~12pt gap)
- After Competencies → Certifications (currently ~24pt gap)
- After Certifications → Education (currently ~12pt gap)

Target: both columns ending within 50pt of each other.

## Design Review

The script includes two automatic review passes that print after every build:

**Pass 1 — Boundaries**: Checks both columns end above the safe zone (footer + 20pt).
Checks column height difference < 50pt.

**Pass 2 — Proportions**: Reports column utilization percentages, breathing room, font,
paper size, and badge colour.

Both passes must show checkmarks. If boundaries fail, content is too long — trim text or
reduce spacing. If proportions are unbalanced, adjust the inter-section gaps in the right
column.

## Critical Rules

1. **Never change the font from Lato.** Unicode will break.
2. **Never change paper size from A4.** Layout will overflow.
3. **Never use Unicode bullets.** Always use `bullet_dot()`.
4. **Always run the design review** after any change.
5. **Always keep URLs as constants** — never hardcode inline.
6. **Badge colours are brand-specific** — Salesforce = Blue #0176D3, not red.
7. **Every link must be clickable** — pair every `draw_link()` with a `linkURL()` call
   (draw_link does this automatically; if adding manual links, don't forget).
8. **Output filename**: `Raviteja_Palanki_AI_PM_Resume_v{VERSION}.pdf`

## Current Content Snapshot (April 2026)

### Claude Cowork Skills (Portfolio Item 1)
```
66 custom skills for AI PM workflows — a composable operating system with 3
layers (Thinking -> Judgment -> Craft), 5 plugins, and a self-correcting
orchestrator. Built as an installable Claude plugin.
```
Link: https://github.com/raviteja-palanki/rtp-personal-skills

### Product Patterns (Portfolio Item 2)
```
RAG + knowledge graph product with LLM evals built in
```
Links: productpatterns.in + https://github.com/raviteja-palanki/Patterns

### AI Learning (Portfolio Item 3)
```
Sharing AI knowledge publicly — frameworks, lessons, and insights
```
Links: learn.ravitejapalanki.com + Substack
