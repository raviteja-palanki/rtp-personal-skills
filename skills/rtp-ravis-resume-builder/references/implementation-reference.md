# Resume implementation reference

Read the main skill first. These helper names and examples match the existing script; they do not make it a portable or fully validated generator. The command requires local dependencies and verified font paths.

## URLs

All URLs are defined as constants near the top of the script. When updating a URL, edit the constant and keep the drawing code referring to it.

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
| `bullet_dot(c, x, y, r=1.2)` | Small teal filled circle | Established experience-bullet style |
| `tag(c, x, y, text, fs, bg, tc)` | Pill-shaped label | Returns width for flow layout |
| `badge(c, x, y, text, bg, fs)` | Colored badge; current helper uses white text | Returns width |
| `sec_hdr(c, x, y, text, line_w)` | Left column section header | Bold + underline |
| `rsec_hdr(c, x, y, text)` | Right column section header | Smaller variant |
| `wrap(c, text, font, fs, max_w)` | Word-wrap to max width | Returns list of lines |
| `draw_bullet(c, x, y, text, max_w, fs, ld, color)` | Bullet + wrapped text | Returns new y |
| `draw_link(c, x, y, text, url, fs)` | ↗-prefixed teal link | Returns text width |
| `links_row(c, x, y, links, fs, gap)` | Row of spaced links | Returns new y |


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


## Historical portfolio snapshot (April 2026)

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


The historical portfolio figures must be checked against the current registry before reuse. Personal project descriptions and career outcomes require Ravi’s current approved records; public company pages establish product information, not his individual contribution.
