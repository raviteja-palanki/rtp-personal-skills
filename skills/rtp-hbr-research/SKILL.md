---
name: rtp-hbr-research
version: v3.7.1_latest
description: 'Read, synthesize, and apply management research from HBR, MIT Sloan, and related sources in Ravi’s library. Use for "HBR research", "process the articles", a monthly research cycle, application cards, or questions about earlier findings. For a full cycle, read each selected source completely, produce a fifteen-part note and the framework, case, and application records, reconcile cross-source insights and open assumptions, and apply useful findings within the authorized scope. Preserve exact article keys, source meanings, quotations, populations, and evidence limits; track reading separately from downstream edits and publication. Use rtp-thinking-writing for clear explanation, rtp-humanizer for specific wording problems, rtp-deep-dive-writer for website revisions, and rtp-claude-admin for versioning and synchronization. A retrieval question can be answered directly without starting a new corpus-wide run.'
---

# HBR Research — Understand the evidence and put useful findings to work

Turn research into clear notes, defensible connections, and appropriate improvements to Ravi's work. The main analytical task is to explain mechanisms and test relationships across sources and existing writing. An accurate summary supports that work; it is also a legitimate result when the material does not support a new deduction.

Do not manufacture novelty, a contradiction, a failure condition, or an edit to satisfy a template. Preserve the difference between what a source observed, what its authors concluded, what the synthesis infers, and what Ravi may choose to do.

## 1. Set the scope and read the current state

Distinguish **retrieval**, **a full synthesis cycle**, **application of existing cards**, and **wording retrofit**. A question about one earlier finding needs a bounded search and appropriate source checks, not a monthly pipeline. New intake should follow the research librarian's intake and classification workflow; an authorized direct reading can proceed without waiting for unrelated shelf maintenance.

For a cycle, use the workspace root `~/Desktop/Claude` and verify the paths in the [workspace and workflow reference](references/workspace-and-workflow.md). Read the live `_synthesis-engine/START-HERE-NEXT-SESSION.md` first. Then inspect the generated article graph and queue, the relevant coverage and application trackers, and the existing-writing index. Read the Novel Insights guide and relevant claims with their later challenges, plus applicable open assumptions. Older run files provide history; their counts and pending lists are not automatically current.

Define the selected sources, objective, order, output requirements, and authorized destinations. Track partial work accurately. A `.pass` or `.applied-card` marker is evidence of a recorded action only when it matches the current file versions and covered outputs.

Read `rtp-thinking-writing` in full once when beginning a writing session, using the current file rather than an old memorized version. Use `rtp-humanizer` when a particular passage needs its pattern guidance. Record source and skill reads honestly in the run log; user updates should emphasize progress and findings, not recite a repeated timestamp ritual before every article.

Work sequentially when Ravi requests it. Delegation is optional and must follow the current request and available tools. Cross-source reconciliation remains the lead's responsibility. This skill does not require agents, an “army,” or a particular model to do good research.

## 2. Read each selected source fully

For a full note, read the entire source, including figures, tables, captions, methods, notes, and relevant qualifications. Inspect page images when extraction loses a framework or chart. If pages are missing or unreadable, identify the gap and keep the work partial; do not claim a complete reading from a summary, search snippet, or incomplete extraction.

Capture the exact title, authors and affiliations, publication, publication date, source location, and read date. Distinguish a publication date from a browser's print or download timestamp. HBR articles, podcast transcripts, MIT Sloan Management Review, and MIT Sloan's Ideas Made to Matter are different publication forms; name the actual one. Check an official episode or article page when local metadata is unclear, and mark a bounded inference or unresolved date explicitly.

Use earlier synthesis to find relevant material and compare interpretations. Verify consequential claims against the source before carrying them into new work. A source article is authoritative for what its authors wrote; it is not automatically authoritative for every company result it repeats. Read underlying records when attribution, numbers, or methods require it.

Apply the [evidence and wording guide](references/evidence-and-wording.md). A correct digit with a changed denominator or population is still a wrong claim. Preserve the scope of measured outcomes, modeled estimates, forecasts, and reported anecdotes.

## 3. Write the complete fifteen-part note

Keep these parts in a predictable order. Use `none identified`, `not applicable`, or a specific unresolved finding where appropriate, rather than filling a section with speculation.

| Part | Content |
|---:|---|
| **1. Source** | Exact title, author and affiliation, publication, date, source location, and read date |
| **2. Main takeaway** | The most useful supported point in one sentence |
| **3. Core claim** | Two to four clear sentences describing the argument |
| **4. Mechanism** | How the argument works, with enough detail to teach it |
| **5. Frameworks and models** | Exact names, origins, components, axes, stages, or categories; identify anything the source only mentions |
| **6. Key numbers** | Values, units, populations, dates, methods, sources, and evidence labels |
| **7. Quotations and plain lines** | Accurate attributed quotations worth retaining, plus a `### Plain lines` block illustrating clear source language within applicable quotation limits |
| **8. Cross-source patterns** | Connections, tensions, boundary conditions, and relationships to Ravi's writing; label deductions and distinguish shared sources from independent support |
| **9. Application routes** | Assess skills, website, and playbook separately; name a verified target and proposed change, or explain why no edit is useful |
| **10. New or already covered** | What the current writing already says and the specific addition, correction, or unresolved difference |
| **11. New artifact signal** | A possible new skill or article only when existing homes cannot serve it; explain the evidence and scope |
| **12. Limits** | Where the authors' advice applies, where it breaks, and any analyst-proposed boundary clearly marked as such |
| **13. Practical next step** | A useful action, test, decision, or reason to defer action |
| **14. Novel deductions** | New claims enabled by the analysis, with a test that could contradict each; `None beyond Part 8` is valid |
| **15. Open assumptions** | Facts or judgments still needed, why they matter, and what would settle them; `None identified` is valid |

Parts 8 and 14 have different jobs: the former maps and evaluates connections; the latter states any new deduction those connections support. They can reference each other instead of repeating the same paragraph. A run that finds a well-supported correction, a useful boundary, or no additional pattern can still have done valuable work.

For frameworks, capture enough structure to redraw or apply the framework faithfully: matrix axes and cells, stage order and transitions, category distinctions, checklist items, or spectrum positions. Do not invent missing details. Preserve meaning in your own clear explanation and quote exact wording where it matters and is permitted. A published framework's completeness does not authorize unrestricted reproduction of copyrighted expression.

## 4. Maintain the four article records

For the full pipeline, use the **source filename stem**, copied from disk with only its extension removed. Preserve spaces, punctuation, case, and Unicode characters. Compare names after NFC normalization; do not rename files merely to normalize them. Check for stem collisions across shelves before writing centralized outputs.

| Record | Location and purpose |
|---|---|
| `<stem>_Note.md` | Beside the source: the fifteen-part analysis |
| `<stem>.frameworks.md` | `_frameworks/`: complete framework structure, glossary, limits, and routing |
| `<stem>.cases.md` | `_case-in-point/`: cases with context, approach, result, evidence, interests, and use |
| `<stem>-card.md` | Beside the source: proposed applications or explicit no-edit decisions |

Read `3_Research/09_hbr-and-journals/_frameworks/EXTRACTION-SPEC.md` before producing framework or case records. The same key joins files and index rows; `<slug>.md` and `<slug>-cases.md` in older instructions are historical conventions, not new output names. Resolve legacy records through their titles, graph entries, and source content rather than guessing from a similar filename.

An article with no named framework or company case still gets a short, explicit empty record in a full extraction cycle. Log survey results separately from company cases. An employer named in an author biography is not a case. If a current run deliberately defers cards, record that stage as pending; three files do not establish completion of a four-record contract.

## 5. Reconcile insights and assumptions

Read the relevant entries in `NOVEL-INSIGHTS.md`, including later refinements and counterexamples. Name articles and stable keys, not “article 1” or a position within a batch. For each proposed contribution, state whether it supports, extends, narrows, contradicts, or merely resembles an existing claim. An extension is not an additional confirmation.

A useful falsifier tests the **current claim** in a named setting, with an observable result and a consequence for that claim. After changing scope, check the falsifier again. The successful application of a proposed remedy does not necessarily refute the problem the remedy addresses. When sources disagree, compare the actual questions, settings, methods, and outcomes; they may both be valid within different boundaries.

Historical status labels use `watch`, `hypothesis`, `rule candidate`, `promoted`, and `retired`. Counts of one, two, or three articles were organizing conventions, not a statistical confidence scale or automatic promotion rule. Repeated reports of one study remain one underlying source. Preserve shared-source links so a correction can be traced across dependent claims.

Keep the dated evidence history when a claim changes. Promotion into `5_Knowledge/rules.md` is a governance decision under the current policy; O25 in `OPEN-ASSUMPTIONS.md` records an unresolved request for Ravi's ruling. Do not silently settle that policy by counting articles. Similarly, distinguish a contradicted clause from retirement of an entire broader claim.

Use `OPEN-ASSUMPTIONS.md` for consequential unknowns and recurring unresolved questions. Name what would settle each entry and use the applicable status: `open`, `answered`, `retired`, or `escalate`. A load-bearing unknown can support explicitly conditional reasoning; it cannot be presented as fact or used to justify a dependent action that requires an answer.

Reconcile the selected batch before starting another. If work was interrupted, inspect the saved files and review state. A missing report does not mean no work was written; a written file does not mean its claims were verified.

## 6. Apply useful findings within the agreed scope

An application card assesses three possible destinations; it does not force every insight into all three. Include the exact target and location, proposed wording, mechanism, conditions, source and evidence scope, unfamiliar-term explanations, and a no-edit decision where appropriate. Confirm that targets exist. Use the website's verified URL index for published links; file stems and public slugs are not interchangeable.

Read the whole target skill or article before revising it. Follow `rtp-deep-dive-writer/references/article-revision-standard.md` for website work. A substantive insight should connect evidence, mechanism, product implication, action, and limitation. A factual correction, clearer definition, or source repair can also be worth making without inventing a new product decision.

Preserve previous versions, protected frontmatter, identifiers, and intentional deployment aliases. Increase the revised version and keep each description within Ravi's **1,000-character limit**. Explain technical terms where readers need them; a fixed `KEY TERMS` heading or a `Pairs with:` line in every description is not required when the document already handles them clearly.

Keep each file coherent. Update headings, counts, transitions, examples, and conclusions when an insertion changes their meaning. Prefer one strong home for an idea, with useful cross-links, over repeated additions across related files. Consider consolidation when modules accumulate; five modules or three similar bullets are prompts for judgment, not automatic split thresholds.

For website work, distinguish strengthening an argument, correcting or challenging a published claim, and drafting a new article. Preserve a visible correction history when the changed claim warrants it. Draft a concrete result before seeking any still-needed decision about Ravi's public position; do not ask again when the current request already authorizes the change. Local editing, publication, and deployment are separate states.

For the playbook, integrate related findings into the relevant explanation rather than appending a paragraph per source. Rebuild and inspect its HTML or PDF when that delivery is in scope; otherwise mark the rebuild pending. A historical fifteen-to-four paragraph consolidation is an example, not a compression ratio to enforce.

If one study supports several consequential edits, record the dependent destinations in the application or concentration ledger. Three destinations is a useful review trigger; even one important dependency may deserve tracking. The point is to find affected claims later, not to penalize a good source for being useful.

## 7. Review, track, and close the run

Use the [review and application protocol](references/review-and-application.md) for wording retrofits, quotation protection, and batch QA. Review every selected article against its actual completion requirements. For a full synthesis, maintain a coverage row for every in-scope source so a rich note cannot disappear because it lacked a short summary or an old progress marker.

Verify changed claims against their sources, compare edits with the saved versions, inspect the surrounding structure, and check links, headers, versions, and output locations. A careful self-review is valid when the work is sequential; do not claim independent review unless it occurred. A review that finds no defects can pass. Manufactured criticism is no more useful than uncritical approval.

Keep reading/extraction status separate from application status. Update each record as work becomes verifiably complete. Rebuild generated indexes through their actual tools when the run changes indexed files; inspect their outputs rather than manually altering counts. Update the live continuation note with completed work, remaining work, uncertainties, and exact paths.

Synchronize canonical skills, the repository mirror, and only the appropriate existing deployments, including supporting resources. Run the relevant governance checks. Record the difference between a local edit, synchronized files, a commit, a pushed repository, a packaged plugin, and an installed plugin. Use scoped staging and the reviewed release workflow when publication or plugin release is authorized; an unrelated retrieval or research note does not require `git add -A` or a push.

Log useful process lessons with supporting examples and limitations. Update this skill or the orchestrator when a durable improvement is justified and in scope. A run need not invent a new rule to count as complete.

Revision 3.7.1 — wording, structure, evidence, routing, and governance reviewed 13 September 2026. Earlier monthly-run incidents inform the protocols in the references; they are historical observations, not current corpus counts or performance guarantees.
