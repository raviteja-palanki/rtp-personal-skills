# Review, wording retrofit, and application protocol

Reference revision 3.7.1 — reviewed 13 September 2026.

## Wording retrofit: preserve meaning while making it clearer

Work one file at a time with its source open. Save a recoverable pre-edit copy and record the source and output versions. A broad search can locate candidate problems; it cannot decide whether a phrase, quote, or claim should change.

For a wording-only assignment, preserve numbers, populations, dates, tiers, unresolved flags, quotations, article keys, paths, and routing decisions. Make sentences clearer without changing their assertions. If a factual error appears, log the source discrepancy and handle it under the authorized correction scope. In Ravi's broader revision work, factual corrections are allowed when researched and tracked; they should not be disguised as cosmetic edits.

Use the current thinking-and-writing skill, then compare the note with the source paragraph by paragraph. Replace ornate or empty phrasing with a clear explanation. Borrow brief, properly attributed source wording where useful and permitted. Do not flatten useful reasoning to match an author's sentence length or replace every technical term with an imprecise synonym.

The retrofit tracker is generated from disk by `_synthesis-engine/tools/build-retrofit-tracker.py`; its status source is `tools/retrofit-state.json`. Verify current paths and schema before using them. Update the actual state store as a file is completed, then regenerate the view. Record whether the source was opened and what kind of review occurred.

## The quotation and digit checks

Historical retrofit batches changed punctuation inside quotations while splitting surrounding sentences. Preserve source quotations exactly, including punctuation and capitalization, unless an explicitly tracked quote correction is in scope. Change the host sentence rather than silently changing the quote to fit it.

Distinguish three uses of quotation marks:

1. **Source quotations:** compare with the pre-edit snapshot during wording work and with the source during a fidelity review.
2. **The note's own labels or scare quotes:** these can be rewritten after confirming that they are not attributed quotations.
3. **Proposed website copy:** quotation marks may delimit an insertion rather than identify borrowed wording; review the content according to its actual purpose.

Compare protected spans and numerical claims before and after editing. A changed stream is a review signal. Resolve it through the actual source and edit intent, then record any authorized correction. For a strictly wording-only pass, revert unintended differences. For an authorized evidence correction, retain the documented before/after instead of reverting a known error merely to make a diff empty.

The earlier shell examples matched only straight double-quoted, single-line spans and a narrow digit pattern. They could miss curly quotes, block quotations, nested quotes, spelled-out numbers, signs, units, and changed associations. They could also flag unrelated quoted labels or harmless reordering. Do not treat those expressions as a complete quote or meaning audit.

Use a protected-span inventory suited to the file, an exact diff, and a source-aware read. Check that each unchanged figure still refers to the same population and comparison. A byte-identical digit sequence can sit in a sentence whose meaning has reversed. Source excerpts may contain unusual punctuation, symbols, or stylistic “banned words”; a style pass must not rewrite them.

When source wording differs from the existing note, record the file, location, old quote, correct source span and location, correction reason, and applied status. An excerpt with an ellipsis must preserve the intended meaning and indicate omission clearly. Keep quotation lengths within applicable rights and limits. The historical estimate of roughly thirty quote discrepancies across ten notes is a dated backlog observation, not the current unresolved count.

## Application cards

Each card assesses the three destinations separately. Include:

- Exact verified file or named section, and the specific point of insertion or revision.
- Ready-to-review wording that explains the proposed change, mechanism, and conditions.
- Source, method, evidence label, population, and date for consequential claims; an unresolved item is a research task, not publication-ready copy.
- A plain explanation of unfamiliar terms, inline or in a legend where that improves use.
- A no-edit decision when already covered, unsupported, outside scope, or better housed elsewhere.
- The application state per destination, with relevant version or diff references.

Do not set `.applied-card` merely because one of several proposed destinations was edited. Record partial and no-edit outcomes accurately. The marker convention should follow the actual tooling schema; use the tracker to preserve detail that a marker cannot represent.

## Eight checks for a coherent application

1. **Meaning and limits:** a new prescription explains why it helps and when it may mislead. A simple factual correction need not grow into a formulaic rule/mechanism/exception paragraph.
2. **Language:** explain the mechanism in plain words and define terms where needed. Preserve functional identifiers and source terminology.
3. **Skill interface:** preserve the identifier and existing frontmatter structure, update the version, and keep the description within 1,000 characters. Companion routing can live where it is clearest; do not add new frontmatter fields without a separate reason.
4. **Source fidelity:** trace consequential claims to the underlying record, and distinguish source statements from analysis. A note is a useful index, not independent verification of itself.
5. **Recoverability:** preserve the pre-edit version and record what changed and why. Use the current governance backup conventions.
6. **Surrounding structure:** reread the heading, introduction, related examples, count references, and conclusion. An added fourth condition must not leave a “three conditions” promise behind.
7. **Audience notation:** internal tiers and `[VERIFY]` flags can support working notes. Public prose needs clear attribution and resolved or plainly stated uncertainty; stripping a flag does not resolve it.
8. **Source concentration:** track consequential claims and destinations that share one study or dataset. A later correction should have a discoverable scope.

## Review the resulting batch

Compare each changed file with its snapshot. Preserve content required by the task, but do not use “zero deletions” as a universal quality test. Adding around an error can leave two contradictory statements in place. Authorized corrections and structural improvements may need replacement, with visible history where appropriate.

Trace numbers, quotations, population, direction, and evidence labels to sources. Record disputed or unresolved findings accurately; a forecast does not become observed because a company published it. Correct a mistaken prior tier with an explicit reason rather than preserving a known error or silently upgrading it.

Check YAML, links, naming, file joins, legends or inline definitions, sibling dependencies, and reader-facing notation. Review the actual generated HTML or PDF when that output is part of the task. Repeated templates should organize information without flattening every conclusion into the same rhetorical pattern.

Record a per-file result such as `pass`, `needs fix`, or `limited by unresolved evidence`, with the specific reason. A clean review can pass without invented defects. A fresh reviewer can add value when available and allowed, but the current sequential request takes precedence; identify a self-review honestly.

For a full note, check all fifteen parts, complete source coverage, accurate framework extraction, useful source comparison, current routing targets, and a clear explanation. Novelty is not a quota. A well-supported no-new-pattern finding or no-edit verdict can pass.

## Track and release the work that was authorized

Update coverage state separately from application state. Update the registry, change log, and other governance records when skills change. Preserve the source, mirror, and intended deployed subset, including new references and assets. A generic source-to-all-deployments copy can create unintended installations or overwrite aliases.

Inspect repository changes before staging. Stage the reviewed files for this task rather than every unrelated change. Keep commits, pushes, plugin packaging, and local installation separately recorded; a local edit is not a remote release. Follow the current reviewed release process when the user has authorized publication or plugin refresh. If a later step cannot run, record the exact pending action without claiming completion.

The previous “four exemplars before fan-out,” “pure additions only,” and “automatic rule after three confirmations” were historical workflow choices. They do not override the user's present authorization, a sequential working preference, or unresolved governance decisions. Preserve the useful purpose: early voice calibration when needed, recoverable changes, and evidence-based review of durable rules.
