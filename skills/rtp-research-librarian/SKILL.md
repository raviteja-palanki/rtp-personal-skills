---
name: rtp-research-librarian
version: v1.0_latest
description: >
  File new third-party material into 3_Research correctly, and keep the library's map honest. Triggers whenever
  anything lands in 3_Research/00_NEW/, when Ravi says "file this", "organize this", "I've added resources", or when
  a session notices unfiled material. Carries the full folder map, the naming conventions, a content-hash dedup
  protocol, an image-identification protocol (images are opened and viewed, never named from their filename), and
  a quality gate built from real filing failures. Its first principle: a wrong file is worse than an unfiled file —
  when the right shelf is not obvious, ask Ravi rather than guess.
  Pairs with: rtp-claude-admin (folder governance), rtp-hbr-research (consumes 05_playbook-intel),
  rtp-deep-dive-writer (consumes the series shelves), rtp-skill-refresh (consumes research for skill passes).
imports: []
---

# Research Librarian

**The objective:** put every new third-party resource on the one shelf where a human or agent will actually look for it, with a filename that says what it is — for Ravi, who has collected these resources over years and cannot afford them being silently mis-shelved or mis-named.

The library is `3_Research/`. It is the **only** home for third-party material. Ravi's own outputs live in `1_Projects/`. That boundary is the first thing to check and the easiest thing to get wrong.

## VOICE — the prose this skill produces

Everything written here gets read by a human or reasoned over by an agent: `CONTEXT.md` files, `MAP.md`, filing-run reports, the OPEN questions you send Ravi. **Run `humanizer` before any of it ships.**

Write descriptions that say what a thing *is*, not what it gestures at. "Eval methods, LLM-as-judge, observability — mostly 2025–2026, heaviest on Hamel Husain and Shreya Shankar" beats "a comprehensive collection of valuable evaluation resources." The first tells an agent whether to open the folder; the second tells it nothing.

No hype, no AI vocabulary, no bullets where a sentence works. Say what you verified and what you didn't. A `CONTEXT.md` that reads like marketing copy is worse than none, because an agent will trust it.

## WHEN THIS RUNS

- Anything appears in `3_Research/00_NEW/` — that folder being non-empty *is* the trigger.
- Ravi says "file this", "organize this", "I dropped some resources", "add this to research".
- A session notices third-party material sitting in `1_Projects/`, `2_Skills/`, or `5_Knowledge/` — it does not belong there.
- Do **not** run this to reorganize the whole library on a whim. Structural change is a Ravi decision (see WHEN TO ASK).

## THE MAP — where things go

Ten folders, named after Ravi's own outputs so there is no translation step. Eight map to a website series or the Playbook; two are material types that span everything.

| Folder | Holds | Feeds |
|---|---|---|
| `00_NEW/` | Landing zone only. Should be empty after every filing run | — |
| `01_agentic-stack/` | Agents, protocols, MCP & integrations, agent-native products, agent memory | website series 01 · skill domain `agent-design` |
| `02_harness-engineering/` | Harness design, context engineering, RAG, prompting | website series 02 |
| `03_ai-evals/` | Eval methods, observability, LLM-as-judge, testing & A/B, metrics & analytics, tooling | website series 03 · `eval-and-quality` |
| `04_ai-pm-os/` | Strategy (+pricing, GTM, growth), discovery, PRDs & specs, prototyping, frameworks & templates, foundations, leadership, responsible-AI | website series 04 · `ai-strategy` / `product-sense` / `craft` |
| `05_playbook-intel/` | HBR, MIT Sloan, industry reports, executive surveys, frontier-company and ecosystem intelligence | the AI Playbook |
| `06_podcast-transcripts/` | Full timestamped transcripts, named by guest | all |
| `07_courses-webinars/` | Courses, masterclasses, webinar decks — grouped by provider | all |
| `08_career/` | Interview prep, resume & ATS, career growth | — |
| `_images-to-identify/` | Staging only. Images awaiting a viewing pass. Never a permanent home | — |

**Each theme folder holds everything on that theme** — articles, books, and visuals together. Books live *inside* their series (`03_ai-evals/books/Evals for AI Engineers by Shreya Shankar, Hamel Husain_2025/`), not in a separate books silo.

## THE FILING PROCEDURE

Run this per file. Do not batch-guess.

1. **Is it third-party?** If Ravi wrote it — a dossier, a draft, a synthesis, a config — it goes to `1_Projects/`, not here. HBR *articles* are research; HBR *dossiers Ravi wrote* are output.
2. **Is it already in the library?** Check by **content hash**, never by filename. See DEDUP.
3. **What is it about?** Read enough to know. For a PDF, extract the title and first page. For an image, **open and view it**. For a transcript, check the header.
4. **Which single shelf would someone look on?** Use the map. If two shelves are equally plausible, pick the one matching the *series* Ravi writes, and note it — don't copy to both.
5. **Does the filename say what it is?** If not, rename it. See NAMING.
6. **Update the map.** Regenerate `MAP.md` and `INDEX.csv` from the tree.

## NAMING CONVENTIONS

- **Articles:** keep the real title; keep the author if present (`Advanced Techniques: Continuous Discovery - by Aakash Gupta.pdf`). Provenance lives in the filename, which is what makes topic-filing safe.
- **Books:** one folder per book, named **`Title by Author_Year`** (e.g. `Evals for AI Engineers by Shreya Shankar, Hamel Husain_2025`). Every chapter, index, appendix and the whole-book PDF live inside that folder. Never split a book across shelves; never flatten chapters to the parent.
- **PDFs with URL/garbage names** (`news.aakashg.com_api_v1_post_pdf_postId=188188669.pdf`): extract the real title from the PDF's own first page with `pdftotext -f 1 -l 1`. Reject candidate lines containing a domain, `http`, `api`, `postid`, or pure digits — those are page furniture, not titles.
- **Images:** never named from the old filename. See IMAGES.
- **Transcripts:** guest name as filename; leave them flat and greppable.
- **Forbidden names:** `_misc`, `_general`, `_essays`, `general-*`, `untitled`, `articles`. If a bucket needs one of these, the classification failed — split it or ask.

## DEPTH — separating PM-level from technical material

The same theme carries two very different kinds of reading, and mixing them makes both harder to use:

- **PM-level** — what it is, why it matters, the trade-off, the decision. What Ravi writes *from*.
- **Technical** — how it's actually built: code, architecture internals, benchmarks, tokenization, chunking strategies, latency and throughput numbers, API and SDK detail. The byte-by-byte Substack deep dives.

**Convention: a technical shelf is the topic shelf plus `_technical`.**
```
01_agentic-stack/agent-design/              PM-level: when to use agents, autonomy, risk
01_agentic-stack/agent-design_technical/    implementation: tool-calling loops, schemas, traces
02_harness-engineering/context-and-rag/
02_harness-engineering/context-and-rag_technical/   chunking, embeddings, retrieval eval code
03_ai-evals/eval-methods_technical/         judge prompts, scoring harnesses, statistical detail
```

**Rules:**
- Create the `_technical` shelf **only when there are enough items to justify it** (the ≥8 rule). Below that, leave the material on the main shelf — a two-file `_technical` folder helps nobody.
- **Classify by content, never by filename.** A title like "A Guide to Context Engineering" tells you nothing about depth. Read the file: code blocks, API signatures, benchmark tables, model-internals vocabulary (tokenizer, attention, quantization, embedding dimensions, batch size, throughput) mark it technical. Roadmaps, stakeholders, prioritisation, positioning mark it PM-level.
- **When a piece is genuinely both** — a deep dive that opens with the product argument and then goes into implementation — file it on the **PM-level** shelf, because that's the reading Ravi does most, and note the technical depth in the filename if it isn't obvious.
- The `_technical` shelf follows every other rule unchanged: dating, versioning, books inside, nothing loose.

## DATING — every resource carries its date when one is knowable

**Rule: every filename ends with its publication month and year in `Mon_YYYY` form, for any file type where a date can be established.**

```
The Art of Asking Smarter Questions_Mar_2026.pdf
A Guide to Context Engineering for PMs - by Aakash Gupta_Nov_2025.pdf
2026 AI & Data Leadership Executive Benchmark Survey_Jan_2026.pdf
```

**Why this matters more than tidiness.** AI moves fast enough that a 2024 article and a 2026 article on the same topic can say opposite things. Without a date in the name, a future session — or Ravi — cannot tell which is the current data point, and a skill refresh may cite superseded material as though it were live. The date in the filename is what makes recency *queryable* without opening anything: `ls | grep 2026`, or sort the `INDEX.csv` date column.

**How to find the date — in this order, stopping at the first that is certain:**
1. **The PDF's own first page.** HBR, MIT Sloan, and most publications print the date near the title or in the header/footer. `pdftotext -f 1 -l 1 file.pdf -` then look for `Month YYYY`, `DD Month YYYY`, or an ISO date.
2. **The PDF metadata** — `pdfinfo file.pdf` (`CreationDate` / `ModDate`). Treat as *weaker* evidence: it records when the file was made, which for a saved-to-PDF web article is often the download date, not the publication date. Use it only if it agrees with the content or nothing better exists.
3. **The existing filename**, if it already carries a date (`..._oct23.pdf` → `Oct_2023`).
4. **The folder it came from**, if that folder is date-scoped (`Q1_2026/`) — gives quarter-level confidence only.

**Never invent a date.** If none of the above yields one, append `_undated` and list the file in the run's OPEN table so Ravi can supply it. `_undated` is an honest flag; a guessed date is a fabrication that will silently corrupt every future recency judgement.

**Other file types — same rule, different evidence:**

| Type | Where the date comes from |
|---|---|
| `.docx` / `.pptx` | Title slide or header first; document properties (`core.xml` created/modified) second |
| **Images / screenshots** | What's *visible in the image* first — an article dateline, a post timestamp, a chat date separator. Then EXIF `DateTimeOriginal`; then the macOS screenshot filename (`Screenshot 2025-01-20 at …` → `Jan_2025`), which is the *capture* date — usually close enough for a screenshot, and it is honest evidence rather than a guess |
| **Transcripts** | The episode publication date if stated in the header; otherwise leave `_undated` — a guest's name gives no date |
| **Books** | Publication year already lives in the folder name (`…by Author_Year`); individual chapters inside need no separate date |
| `.md` / `.txt` | A date in the frontmatter or first heading; otherwise `_undated` |
| **Web-saved articles** | The dateline in the page body — not the file's creation timestamp, which is when it was saved |

For an image *set* (a paged article, a chat thread), the date goes on the **set's folder**, not on each image inside it.

**Ambiguity rules:**
- Two-digit years resolve to the 2000s (`oct23` → `Oct_2023`).
- A revised or second edition takes the **revision** date, with the original noted in the filename only if Ravi asks.
- Undated evergreen material (a framework poster, a template) may stay undated — but mark it `_undated`, don't leave the field silently absent.

## VERSIONS — when the same document exists more than once

Two files can be near-identical yet not duplicates: a v1 and a v2, a draft and a final, a first and second edition. **Content-hash dedup will correctly refuse to merge them** — they differ — so they must be *labelled*, or the library quietly holds two competing truths with no way to tell which is current.

**Detect a version set** when several files share a title but differ by: an explicit marker (`v1`, `v2`, `Rev B`, `Second Edition`, `Draft`, `Final`, `Updated`), different publication dates on the same title, or near-identical content at different sizes.

**Name them so the latest is unmistakable:**
```
AI Strategy Guide_v1_Apr_2025.pdf
AI Strategy Guide_v2_Jan_2026.pdf          ← newest by date and version
Enterprise AI ROI Measurement_Draft_Nov_2025.pdf
Enterprise AI ROI Measurement_Final_Feb_2026.pdf
```
- Version marker goes **before** the date: `<Title>_<version>_<Mon_YYYY>`.
- If there's no explicit version marker but the dates differ, the date alone carries it — don't invent `v1`/`v2` numbering that the publisher never used.
- If it's genuinely unclear which is newer, say so in the run's OPEN table rather than picking.

**All versions of one document live together in a single folder — never scattered across shelves.** Two versions sitting in different folders is the worst outcome: an agent finds one, has no idea a newer one exists, and cites stale material with full confidence.

```
04_ai-pm-os/strategy/AI Strategy Guide_versions/
├── AI Strategy Guide_v2_Jan_2026_CURRENT.pdf     ← newest, explicitly tagged
├── AI Strategy Guide_v1_Apr_2025.pdf
└── _VERSIONS.md                                   ← one line per version + what changed
```

- The folder is named `<Title>_versions/` and sits on the shelf the document belongs to.
- **The newest carries `_CURRENT` in its filename.** That single token means no agent has to compare dates or parse version numbers to know what to read. When a new version arrives, move `_CURRENT` to it — the tag is always on exactly one file.
- `_VERSIONS.md` lists each version with its date and, where knowable, what changed. If the change is unknown, say "change not documented" rather than inventing one.
- **Superseded versions are kept, never archived as duplicates** — an older edition shows how thinking moved, which is evidence Ravi writes from. Only *byte-identical* copies get archived.
- A version set counts as **one resource** in the map, not N.

**Books:** editions are part of the folder name (`AI Agents in Action, Second Edition by Micheal Lanham_2025`), and each edition is its own folder — never merged.

**Recency in practice.** When any skill consumes this library — a skill refresh, an article draft, a Playbook update — it reads newest-first and treats older material as background unless the topic is genuinely stable. On a fast-moving topic (models, pricing, agent tooling, evals) anything older than ~18 months is a *historical* data point and must be labelled as such if cited. On slow-moving topics (discovery craft, interviewing, org design) age matters far less. State which regime applies when it affects the conclusion.

## IMAGES — the strictest rule

`Screenshot 2025-01-20 at 12.54.25 AM.png` and `09029304-9c2e-4864-b536-611d8f1ee647_1602x980.jpg` carry **zero** information. Naming them from context is fabrication.

1. **Open and view every image.** No exceptions, no inference from the folder it arrived in.
2. **Name it for what it shows**, in plain words: `Uber-Lyft — why-now market timing (tech, consumer, regulatory).png`.
3. **Group related image sets into their own subfolder.** Screenshots usually arrive as *series* — a WhatsApp thread, a paged article, a slide deck photographed screen by screen. Detect a set by: near-identical timestamps, sequential numbering, the same visual layout, or narrative continuity when viewed in order. Then create one clearly-named subfolder, e.g.:
   - `04_ai-pm-os/strategy/MINT — <article title>_<date>/` for a paged newspaper article
   - `08_career/interview-prep/WhatsApp — <topic> thread_<date>/` for a chat series
   - `03_ai-evals/observability/<Talk title> — slide captures/` for a photographed deck
   A 12-image article shot page-by-page is **one resource**, not 12 files. Filing them individually destroys it.
4. **Multi-page sets get an ordering prefix** — `01-`, `02-` — so reading order survives.
5. If the image is unreadable, low-value, or you cannot tell what it is, **leave it in `_images-to-identify/` and ask**. Do not invent a name.

## DEDUP — content only

- Compare by **MD5 of file contents**. Never by `(filename, size)`.
- Why: filename+size produced errors in *both* directions. It archived unique files whose generic names collided (`Brief Table of Contents (Not Yet Final)` recurs across different books), and it missed true duplicates whose filenames differed only in punctuation (`AI Coding Tools…: What Executives…` vs `AI Coding Tools…_ What Executives…`).
- Keep the copy with the better filename; move the other to `_ARCHIVE_duplicates_<DATE>/01_duplicate-copies/<theme>/`.
- **Never delete anything.** Redundant material is archived, with a README explaining what it is and how to restore.

## QUALITY GATE — every item must pass

Each line below exists because it was actually broken once. Verify, don't assume.

- [ ] **Third-party check** — nothing of Ravi's own authorship landed in `3_Research/`
- [ ] **Content-hash dedup** — no `(name,size)` shortcuts anywhere
- [ ] **Topic beats source** — nothing filed under a publisher/author folder because that's where it came from; provenance is in the filename instead
- [ ] **One shelf per theme** — no parallel `articles/` hierarchy sitting beside the real theme folders
- [ ] **No shelf under ~8 items** — thin shelves merge up into their parent
- [ ] **No bucket holding >40% of its parent** — that's a pile, not a shelf; split it or ask
- [ ] **No forbidden bucket names** (`_misc`, `_general`, `general-*`, `_essays`)
- [ ] **Destination names come from this skill's controlled vocabulary** — never from the source path's basename (that produced `07_courses-webinars/prompting/`)
- [ ] **Books whole** — one folder per book, `Title by Author_Year`, chapters inside, no book split across two folders
- [ ] **Every image was actually viewed** before being named or filed
- [ ] **Related image sets grouped** into one named subfolder with ordering prefixes
- [ ] **Every file carries `_Mon_YYYY`** where a date was establishable, and `_undated` where it wasn't — no date was ever guessed
- [ ] **Dates came from content, not file timestamps** (a save date is not a publication date)
- [ ] **Version sets live in one `<Title>_versions/` folder**, with exactly one file tagged `_CURRENT` and a `_VERSIONS.md` present
- [ ] **No superseded version was archived as a duplicate** — only byte-identical copies are archived
- [ ] **Ambiguous keywords disambiguated** — "cohort" is user-cohort analytics, not a course cohort; "tools" is not "tooling"; check the sense before matching
- [ ] **`MAP.md` and `INDEX.csv` regenerated from the tree**, never hand-edited
- [ ] **`00_NEW/` is empty** at the end of the run
- [ ] **Nothing deleted** — redundant material archived

## THE RETRIEVAL-FIRST PRINCIPLE (read this before optimising folders)

**The library exists to be retrieved from, not to look tidy.** Its failure modes are not untidiness — they are:

1. **Silent miss** — relevant material exists but isn't found, so the output is thin, or an agent hallucinates a fact that was sitting on the shelf unread. The worst failure, because nothing signals it happened.
2. **Stale hit** — 2024 material cited as current on a topic that moved. This is the trendslop failure at library scale.
3. **Version ambiguity** — three copies found, none marked current.

**Now the non-obvious part: agents don't browse folders the way people do.** Given a task, an agent either reads `MAP.md` and lists one folder, or greps `INDEX.csv`. Both are **name-based** retrieval. So the **filename carries most of the retrieval weight, and the folder carries far less than intuition suggests.**

Consequences that should drive effort allocation:
- A 300-file shelf whose filenames are descriptive and dated is **highly** retrievable.
- A 20-file shelf full of `Screenshot 2025-01-20 at 12.54.25 AM.png` is **unretrievable at any cost**, no matter how elegant the folder tree.
- Therefore: **filename quality > index quality > folder arrangement.** Fix them in that order. Rearranging folders while files are badly named is motion, not progress.

**Retracted rule — "no shelf over 40% of its parent."** That optimises folder *balance*, which nobody retrieves by. If a theme genuinely holds a third of the library because it's the broadest thing Ravi writes about, splitting it for symmetry adds a hop and helps nobody. Goodhart: the metric replaced the goal. **Split a shelf only when its contents are genuinely different kinds of thing, never to even out counts.**

**The findability test — the only one that matters.** For any file, ask: *if an agent needed exactly this in six months, what would it search for, and would this file surface?* If the answer needs the agent to already know the folder, the filename has failed.

## WHEN IN DOUBT, RESEARCH IT — don't guess, don't leave it blank

Uncertainty is not a reason to guess **or** to give up. Before flagging something OPEN, use the tools:

- **WebSearch / web_fetch** for anything externally knowable: a book's publication year and author, whether two documents are different editions, what an acronym on a screenshot refers to, who a podcast guest is and what they're known for, whether an article has a newer version. A book's year is a *fact on the internet* — look it up rather than writing `_undated`.
- **The file's own content** first — `pdftotext` the first page, view the image, read the transcript's cold open. Internal evidence beats external.
- **Cross-check before committing** when the answer is load-bearing: two independent sources that converge, exactly as the evidence discipline requires elsewhere in this library.

**The order:** file content → web research → ask Ravi. Escalate to Ravi only for judgements that are *his*, not for facts that are merely unknown to you. Record where a fact came from when it isn't obvious, so a later session can re-verify.

**Never** let research become invention. If a search is inconclusive, `_undated` and an OPEN flag are the honest outcome — a plausible-looking year that no source supports is exactly the fabrication this library is meant to prevent.

## WHEN TO ASK RAVI

A wrong file is worse than an unfiled file. These are his resources, collected over years.

**Ask, don't guess, when:**
- A resource fits two series equally well and the choice affects where he'll look for it.
- A new material type arrives that the map has no shelf for (ask before inventing a folder).
- An image is unreadable or its subject is genuinely unclear.
- A change would restructure existing folders, rename a shelf, or move more than a handful of already-filed files.
- Something looks like Ravi's own work but sits among third-party material.

**Decide without asking when:** the topic is unambiguous, the filename is clearly wrong and the real title is extractable, or the file is a byte-identical duplicate.

**How to ask:** name the file, say what it appears to be, give the two or three candidate shelves with your recommendation and reasoning. One message, batched across all doubtful items — don't interrupt per file.

## WHEN WRONG

- **Bulk reorganizations** — this skill files *incoming* material. Restructuring the library is a Ravi decision.
- **Ravi's own drafts and outputs** — those route to `1_Projects/`.
- **Material for a specific live project** that only serves that project (course assets, website build files) — leave it with the project.

## ENVIRONMENT CONSTRAINTS (known, not bugs)

- **Directories cannot be deleted from the agent sandbox** — host permission blocks `rmdir`; files are fine. Empty shells persist until cleared in Terminal: `find ~/Desktop/Claude -type d -empty -delete` (run 2–3× for nested).
- **Bash calls cap at 45s.** Hashing and large moves run resumably in chunks with state in `3_Research/.verify/`.
- `.DS_Store` files may resist deletion; ignore them in all counts.

## OUTPUT OF A FILING RUN

```markdown
# Filing run — <date>
**Filed:** <n> items    **Archived as duplicates:** <n>    **Left for Ravi:** <n>

## Filed
| File (final name) | Shelf | Why |
|---|---|---|

## Renamed
| Was | Now | Source of the new name (PDF title / viewed image) |
|---|---|---|

## Image sets grouped
| Set | Images | Shelf |
|---|---|---|

## OPEN — need Ravi's call
| File | What it appears to be | Candidate shelves | My recommendation |
|---|---|---|---|

**Quality gate:** all boxes ticked / the following failed: …
**MAP.md + INDEX.csv regenerated:** yes
```
