---
name: rtp-research-librarian
version: v1.2.1_latest
description: 'Identify, name, deduplicate, and file incoming research in Ravi’s 3_Research library, then keep its indexes accurate. Use when Ravi asks to file resources, material arrives in 00_NEW, or a task encounters a clear filing problem. Inspect content before naming it, view images before identifying them, distinguish publication dates from capture dates, and preserve editions and format variants. Use the current MAP and folder context rather than an old hardcoded shelf list. Archive verified duplicates with recovery records; retain unresolved items with explicit reasons. Prefer useful names and retrievable metadata over cosmetic folder balance. This skill also guides focused library research and source checking. Pair with rtp-claude-admin for workspace governance, rtp-hbr-research and rtp-research-synthesiser for journal analysis, rtp-deep-dive-writer for series writing, and rtp-skill-refresh for skill updates.'
imports: []
---
# Research librarian

Make Ravi's research easy to find, identify, and cite accurately. File incoming material on the most useful shelf, preserve its provenance and reading order, and leave a recoverable record of changes. An unresolved item with a clear reason is preferable to a confident wrong label.

Use `rtp-thinking-writing` for descriptions and reports. Say what the material contains, what you inspected, and what remains uncertain. For example: “Eval methods, LLM-as-judge, and observability; mostly 2025–2026, with substantial Hamel Husain and Shreya Shankar material.” Avoid promotional language or vague descriptions; use technical terms when they help retrieval.

## Scope and current authority

The main source library is `3_Research/`. Ravi's live drafts, deliverables, and project-only assets normally belong in `1_Projects/`. **There are intentional research-library exceptions:** `12_ravi-published/` holds a managed copy of his published work; journal synthesis notes, frameworks, and cases live beside their sources; `_book-text/` contains derived reading extracts. Do not move these out merely because Ravi or an agent authored them.

Run when Ravi requests filing or organization, when authorized work encounters incoming material in `00_NEW/`, or when a specific misplaced resource needs attention. A nonempty inbox identifies available work; it does not authorize interrupting an unrelated task or restructuring the whole library. Preserve a project's assets when they serve that project.

Read `MAP.md`, the relevant `CONTEXT.md`, and `INDEX.csv` before selecting a shelf. Use the actual tree and governance if the map disagrees. The map's generated block is maintained by `_tools/rebuild-map.py`; `INDEX.csv` has `parent,shelf,title,author,date,year,kind,file`. Its rows count files, while an article graph or filing report may count logical resources. Name the counting unit.

## Current library map

This table was checked against the local tree on September 13, 2026. Use it for orientation, then check the current map rather than treating the list as immutable.

| Location | Main purpose |
|---|---|
| `00_NEW/` | Incoming material awaiting identification or filing |
| `01_agentic-stack/` | Agents, protocols, integrations, memory, agent-native products |
| `02_harness-engineering/` | Harnesses, context engineering, RAG, prompting |
| `03_ai-evals/` | Evaluation, observability, experiments, metrics and tooling |
| `04_ai-pm-os/` | Strategy, discovery, product craft, leadership and responsible AI |
| `05_industry-reports/` | Industry reports and executive surveys outside the journal collection |
| `06_ai-trends/` | Frontier companies, market changes and ecosystem intelligence |
| `07_courses-webinars/` | Courses, masterclasses and webinars, with established provider groupings |
| `08_career/` | Interviews, resumes, career development |
| `09_hbr-and-journals/` | HBR, MIT Sloan and related source/synthesis material |
| `10_tech-foundations/` | Established technical foundations shelf |
| `11_ai-tech-essentials/` | Established technical essentials shelf |
| `12_ravi-published/` | Managed published-work mirror; follow its sync process |
| `_book-text/` | Derived book/chapter text with source-PDF references |
| `_images-to-identify/` | Images whose identity or filing remains unresolved |
| `_tools/`, `.verify/` | Library tooling and resumable verification state |
| `_archive/`, dated duplicate archive | Recovery/history; excluded from live counts as specified |

The old `05_playbook-intel/` and flat `06_podcast-transcripts/` routing are superseded. Transcripts now occur on topic shelves, including AI PM OS, agentic stack, evals, trends and career, plus an existing provider collection. Do not recreate the old root folders. Books remain whole within their topic shelf; each edition can have its own book folder.

## File one resource at a time

1. **Establish identity and ownership.** Inspect the title and substance. For a PDF, read the title page and enough body text to confirm the actual article; render pages if the extraction or visual content is unclear. For a transcript, read the header and relevant opening. For an image, open and view it. Record inspection limits.
2. **Check for existing copies and versions.** Search the index and compare content. Use the deduplication procedure below; a similar filename or file size is not proof of duplication.
3. **Choose the primary shelf.** Classify by subject and intended retrieval. When a resource spans topics, choose the dominant use and record the secondary topic in metadata or a context note rather than copying it to several shelves.
4. **Set a supported name and date.** Preserve a real title and author where known; distinguish publication, revision and capture. Keep a set or book together.
5. **Prepare a reversible move.** Check the destination for collisions, record old and new paths, and preserve source bytes. Do not overwrite a different file because its desired name matches.
6. **Move and verify.** Confirm the destination bytes and intended location before removing the old live path. Update affected path references and set/version manifests.
7. **Update indexes and report.** Use the existing tooling and metadata policy, verify forward and reverse integrity, and regenerate the map. Report completed, archived and unresolved resources separately.

Read enough to classify the resource accurately; filing does not establish that the entire resource was deeply analyzed. If the intended title in a web page's header differs from its transcript body, inspect the mismatch. A file may contain a mislabeled article or several sources. Name the identified substance, preserve the mismatch in a note, and record a missing intended article for recapture. Do not call it corrupt or silently merge two sources without evidence.

## Names, depth, dates, and editions

Use a descriptive title, supported author, and known publication date. Preserve meaningful source wording, but adapt characters that the filesystem cannot safely represent. Do not reject a legitimate title just because it includes “API,” a domain, or a number; distinguish a real title from page furniture by reading the page.

Articles usually follow `Title - by Author_Mon_YYYY.ext`. Books use `Title by Author_Year/`, containing the complete book, chapters, index, and appendices. Transcripts should identify the guest and, when needed to prevent collisions, the episode/topic and date. Image sets use a descriptive dated folder and ordered member names.

Keep PM-level and implementation material discoverable. Existing `_technical` siblings distinguish code, schemas, internals, benchmarks and detailed engineering from product decisions. Mixed pieces normally stay on the main topic shelf, with technical depth noted in metadata. The original eight-item threshold is a **guideline for creating new topic subdivisions**, not a reason to dismantle a useful small existing shelf, split a book, or separate an image set.

Do not add vague new buckets such as `_misc`, `_general`, `general-*`, `_essays`, `untitled`, or `articles`. Existing historical names are not an instruction to rename them during an incoming filing task. Courses can retain their provider organization. Topic and purpose guide new shelves; no rule requires every directory to have the same shape or size.

Detailed examples and the full date/version procedure are in [identity, dates, and versions](references/identity-dates-versions.md). The essential distinctions are:

- Publication is not capture. A browser print timestamp, EXIF time, filesystem modification time, or document-created property establishes only its own event unless corroborated.
- Use a publisher's dateline or edition record where available. Keep original publication and later update separately when they affect interpretation.
- Unknown dates stay unknown. Use `_undated` where the naming convention calls for it; record quarter/year-only precision without inventing a month.
- Keep byte-distinct editions and format variants. A cleaner capture may be the preferred reading copy only after checking completeness; it is not necessarily a newer edition.
- Use one `_CURRENT` reading-copy marker only when a preferred/current artifact can be established. If unresolved, record the ambiguity rather than assigning a false winner.

## Images and related sets

Open each image before naming or classifying it. A filename, neighboring file, OCR extract, or inherited description can suggest an identity but cannot replace viewing. If the image is inaccessible or unreadable, keep it in staging with a precise note. Low relevance is a different judgment from unknown identity; do not discard a resource merely because it seems unimportant.

Look for sets through page sequence, timestamps, layout, narrative continuity, **or a shared task**. A twelve-image article is one logical reading resource with twelve files. Three different interfaces can be a comparison of the same experiment. Preserve `01-`, `02-` order where sequence exists; for a comparison without natural sequence, use descriptive member names and a manifest rather than implying chronology.

The prior `arize.png`, `braintrust.png`, and `langsmith-clean.png` example showed the same apartment-leasing trace-audit task across three platforms, including matching `nb-000NN` identifiers. Its lesson is to inspect what was captured, not to assume that every product-named image is a bake-off or that it is rarely a logo.

## Deduplicate without losing evidence

Normalize filenames to **NFC when comparing or joining paths**, while retaining the actual path for filesystem operations. Unicode-normalization differences can cause false misses on macOS and elsewhere. NFC does not make all punctuation variants equivalent, and filename normalization is separate from hashing file contents.

Use a strong content hash such as SHA-256, followed by byte comparison before treating files as exact duplicates. Size can narrow candidates, but name and size cannot decide identity. Legacy MD5 records may help locate candidates; they do not override a fresh verification.

For verified identical bytes, keep the copy with the clearest name and correct references, then move the redundant copy into the existing dated duplicate archive with a restoration note. Preserve a collision-safe destination and a manifest of both paths and verification method. Do not delete it.

Different bytes may represent the same text in another capture, a revised edition, omitted figures, or changed metadata. Text equality alone does not establish equal visual content, links, annotations, completeness, or provenance. Keep both by default as format variants; any content-level consolidation requires a documented comparison and recoverable disposition. Do not archive a superseded edition as an exact duplicate.

The historic failure cases remain instructive: generic “Brief Table of Contents” names collided across books, while punctuation differences hid actual duplicates. Inspect identity and preserve context rather than choosing a filename shortcut.

## Keep retrieval and indexes honest

Prioritize the most consequential retrieval failures: **silent misses**, **stale hits**, and **version ambiguity**. Descriptive names and metadata often help more than cosmetic folder rearrangement, but filenames are not the only retrieval surface. Search indexed titles, authors, topic context and extracted content as appropriate.

The old “no shelf over 40% of its parent” rule is **retired**. Split only when different material needs different retrieval paths. A large coherent shelf can work; a small poorly labeled shelf can fail. Test with realistic queries: would someone seeking this method, author, company or evidence find it without already knowing its folder?

Use `_tools/index-check.py` for current index policy and forward/reverse checks; inspect its invocation before running a repair. `_tools/rebuild-map.py` rebuilds the generated map from the index. Do not invent an index-regeneration command or hand-edit generated map counts. Preserve curated author, date and kind fields when reconciling rows. Journal `ARTICLE-GRAPH.csv` and its queue have their own generators and source-versus-format counting rules.

Exclude `.DS_Store`, tooling, staging and archives according to actual policy. Do not claim a file count is a logical-resource count. Run only the affected checks after a small filing change; a library-wide audit is a separate scope.

## Research and escalation

For a research task, use MAP → relevant folder context → index/graph → the actual material. Read relevant book chapters thoroughly, preferring `_book-text/` extracts while citing the source PDF from their header. Consult current five-series files under `1_Projects/1_my-personal-website/1_My Series-MD-FILES/My Website all latest MD files/`; do not substitute `version1/` when current files exist.

Check current primary sources when a consequential fact, version, price, date or interpretation may have changed. X can provide primary posts; verify the exact post, author and date when used. An empty search or blocked page is an access limit, not evidence that no post exists. Other primary sources may resolve the question; do not force an X search for every filing task. Grok, X and Cursor Grok are relevant to Ravi's actual use cases, not a universal test of every AI interface.

Source suitability matters more than a fixed count: one direct publisher record can establish an edition; repeated reports of one study are not independent confirmation. For adoption, retain population, date and behavior—tried, active weekly, paid seat and deployment differ. Use a source chart or a clearly labeled reconstruction when a visual helps; do not silently present reconstructed data as the original chart.

Read the current Novel Insights guide and relevant pattern/challenge passages when applying research to skill revision. Treat patterns as hypotheses with source limits. Record a useful new lesson when supported; routine filing does not require inventing a tenet or revising a skill on every invocation.

Resolve straightforward naming, duplicates and shelf choices within the user's authorization. Ask Ravi when an unresolved choice changes his intended organization, ownership is uncertain, or a proposed structural change exceeds the task. Present the affected files, candidate choices and recommendation together. Continue independent filing while those items remain pending; an empty `00_NEW/` is not a completion requirement when uncertainty remains.

## Completion and report

Verify identity, image viewing, date precision, shelf fit, duplicate/variant treatment, set integrity, collision protection, updated references, index integrity and recovery records. Report untested items honestly. Avoid a universal claim that the sandbox cannot remove directories or commands stop at 45 seconds: inspect current permissions and work resumably when needed. Never run a broad empty-directory deletion as a filing cleanup.

```text
Filing run — date
Filed: N logical resources / N files
Archived duplicates: N files, verification method and recovery location
Unresolved: N resources, reasons and next action

Filed: final path, identity evidence, shelf rationale
Renamed/moved: original path, final path, reason
Sets/versions: members, ordering, preferred-copy basis
Open decisions: resource, uncertainty, candidate choices, recommendation
Checks: performed results, failures, and untested conditions
Index/map: actual updates and integrity-check results
```

Use only relevant sections for a small run. When a skill or governance rule needs an authorized correction, follow the exact-source backup and version process in `rtp-claude-admin`, update the registry/change log, and preserve the reason. This skill's September 13, 2026 revision reconciles the live map, date precision, duplicate evidence and its earlier contradictory folder rules.
