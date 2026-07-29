---
name: rtp-hbr-research
version: v1.1_latest
description: 'Monthly research-synthesis and apply engine for Harvard Business Review, MIT Sloan, and other top management research. Reads every PDF in full, writes one citation-disciplined note per article (numbers tagged by evidence strength, company claims backed by primary links, plain HBR-grade prose), finds patterns across articles, and checks each insight against what Ravi has already written — then ships those insights into the three places his thinking lives: the AI-PM skills, the website series, and the playbook. Everything versioned, tracked, git-synced. Use whenever Ravi adds research to 3_Research/hbr-and-journals/, says "HBR research", "research synthesis", "process the articles", "run the monthly cycle", "apply the cards", or asks what earlier research said. Pairs with humanizer (prose pass), rtp-deep-dive-writer (website articles), rtp-claude-admin (governance sync).'
---
# HBR research synthesis engine v3.1

> v3.1 (30 JUL 2026): corrected every path in this skill to match where the corpus actually lives, after two library reorgs this file's text never tracked. The corpus moved from `3_Research/1_hbr-ai-2026/` to `3_Research/hbr-and-journals/` (reshelved by topic); the engine home moved to `hbr-and-journals/_synthesis-engine/Q2_2026/`; and 125 of the June run's own notes and cards were found sitting in a disconnected project folder (`1_Projects/2_Playbook_AI/hbr-synthesis-output/`), never paired with their source PDFs, until this pass moved them next to their matched PDF (matched by each note's own title line against the corpus index, not by filename). A separate 104-file batch of the army's own progress markers had also been sitting inside `3_Research/` mislabeled as "articles" for at least one prior pass; it now lives at `1_Projects/2_Playbook_AI/hbr-synthesis-engine-state_Q2-2026/`, outside the research corpus entirely. The lesson this leaves for every future run: re-verify every path in this section against disk before trusting it, the same discipline this skill already demands of a citation. Full account in `5_Knowledge/hypotheses.md` H28-H31.
> v3.0 (10 JUL 2026): the apply loop, written from the June run's Stage-B experience and the Fable-5 QA pass over its output. The engine no longer stops at notes and maps: it now carries the full method for shipping each insight into the skills, the website, and the playbook, with the standing gates that a critical evaluation of 26 applied skills, 4 applied articles, and 4 playbook sections proved necessary (the WHY gate, plain-language legends, the business-clarity frontmatter bar, the primary-source gate, the container check, surface-appropriate notation, population scope on numbers, and the single-study concentration ledger). See "The apply loop" below. Also fixed a stale website path that would have failed the exact-target gate.

## What this does

It turns top management research into insight Ravi can act on, across three places where his work lives: the AI-PM skills (65 skills plus CLAUDE.md and the orchestrator), his own website writing (the four series in `1_My Series-MD-FILES/`), and the playbook (`2_Playbook_AI/AI_Playbook.md`).

This is not a summarizer. It reads the way a top AI product manager reads: to understand each idea well enough to teach it, to find new patterns by joining ideas across articles, and to write notes so clearly that an editor would not change a word. It runs once a month. Each run's notes and patterns stay on disk, and the next run builds on them.

> v2.3 (29 JUN 2026): hardened the army that runs the work, from a live failure. The June Q2 run fanned out all 66 articles at once (about 73 agents, 880k tokens in 5 minutes) and tripped the account's rolling session limit mid-flight, losing the whole window's reviews. Three fixes, now in `_army-deep-synthesis.js`: bounded batching (each run takes a deliberate slice and stops clean, the rest resume from disk), a citation gate in the reviewer (a striking named-company number with no primary link and no [VERIFY] tag fails review), and a comprehensive synthesis that reads the richest notes in full and writes a coverage ledger of all articles so nothing is silently dropped. The trigger was a near-miss: three deeply-analysed POC notes sat outside the run set and would have been excluded from the final synthesis. See "Running the army" below.
> v2.2 (27 JUN 2026): made the skill self-driving. Added exact input and output paths, a "read the trackers first" startup step, the humanizer pass as a required output step, an HBR-editor verification checklist, and put hidden-pattern analysis up front as the main job. v2.1: rewrote the skill to its own bar (no em dashes, plain words, dropped "canon," added the anti-patterns section). v2.0: the 13-part note, the writing standard, evidence tiers and the real-company citation rule, three-place routing, the two-tracker setup.

## The main job: hidden-pattern analysis

The reason this engine exists is part 8 of each note, and the running patterns file it feeds. Anyone can summarize an article. The value here is the pattern no single source states: the contradiction between two studies that resolves into a rule, the connection that turns two facts into one insight, the line from an HBR finding to something Ravi already wrote that neither saw on its own. Summary is table stakes. Pattern-finding is the product. If a run produces clean notes but no new patterns, it has failed at its main job. This is what makes the output worth a senior analyst's time, and it is the part the humanizer pass must never flatten.

## Where everything is (paths, relative to ~/Desktop/Claude)

**Corrected 30 JUL 2026 — verify these against disk at the start of every run rather than trusting this section by default; a corpus reorg is exactly the kind of change that goes stale here without anyone revisiting it (see H29 in `5_Knowledge/hypotheses.md`).**

Inputs, the PDFs to read, one topic-shelf folder per subject:
- `3_Research/hbr-and-journals/mit-sloan/` — MIT Sloan Management Review + "Ideas Made to Matter," with its own dated intake-batch subfolder (currently `Q3_2026/`)
- `3_Research/hbr-and-journals/hbr-articles/<topic>/` — HBR pieces sorted by subject (`leadership-and-workforce/`, `strategy/`, `ai-agents/`, `customer-and-market/`, `responsible-ai/`, `data-and-measurement/`, `innovation-and-rnd/`, `adoption-and-roi/`), each with its own dated intake-batch subfolder
- any later drop lands in `3_Research/00_NEW/` first; `rtp-research-librarian` sources, dates, and shelves it into one of the folders above before this skill ever reads it

Engine home and working files (the June 2026 run's own tracking; a new month's run gets its own dated subfolder alongside this one):
- home: `3_Research/hbr-and-journals/_synthesis-engine/Q2_2026/`
- what Ravi has already written: `_synthesis-engine/Q2_2026/EXISTING-WRITING-INDEX.md`
- year at a glance: `_synthesis-engine/Q2_2026/MASTER-TRACKER.md`
- shipped-edits ledger: `_synthesis-engine/Q2_2026/APPLICATION-TRACKER.md`
- running patterns: `_synthesis-engine/Q2_2026/RUNNING-PATTERNS.md`
- the note bar and the term glossary: `_synthesis-engine/Q2_2026/00-METHOD.md` and `GLOSSARY.md`
- the army's own tooling (progress markers, the run manifest, the orchestration script) lives OUTSIDE `3_Research/` entirely, at `1_Projects/2_Playbook_AI/hbr-synthesis-engine-state_Q2-2026/` — this is machinery, not reading material, and must never be re-filed into a research shelf (it was, once, for at least one full pass; see H28)
- the running coverage checklist of which source PDF has a note yet: `3_Research/hbr-and-journals/SYNTHESIS-COVERAGE-TRACKER.md`

Where a note and its card actually land (corrected — not a `runs/<month>/` subtree): directly beside the source PDF, in that same topic-shelf folder. A note is `<slug>.md`, its card is `<slug>-card.md`, its optional company-case companion is `<slug>-cases.md` — all three sit next to `<slug's-source>.pdf`. If a note's location is ever unclear, pair it back to its PDF by matching its own title line against the corpus index, never by guessing from filename (the method: H30 in `5_Knowledge/hypotheses.md`).

Outputs, the three places insights ship to:
1. Skills: edit the source at `2_Skills/ai-pm-skills/<cluster>/skills/<skill>/SKILL.md` (the `/skills/` segment is real and easy to drop by mistake), then sync to `.claude/skills/<skill>/SKILL.md` (folder name unprefixed) and `rtp-personal-skills-repo/skills/rtp-<skill>/SKILL.md` (folder name rtp- prefixed). Run `./scripts/skill-sync.sh` to confirm all three match.
2. Website writing: edit the article at `1_Projects/1_my-personal-website/1_My Series-MD-FILES/<NN-series>/<article>.md`.
3. Playbook: edit the section in `1_Projects/2_Playbook_AI/AI_Playbook.md`.

## Start every run by reading the trackers

Before opening a single PDF, read the state, so you pick the right inputs and write to the right place:
1. `MASTER-TRACKER.md`: which month is this, and what is its objective.
2. the run's `TRACKER.md`: which articles are already written up, and which are still pending. Read only the pending ones.
3. `APPLICATION-TRACKER.md`: which insights already shipped, so you do not propose them twice.
4. `EXISTING-WRITING-INDEX.md`: what Ravi has already written, so "new" is judged against fact.

Then inputs are the pending articles, and outputs are the routed targets named in each note's part 9. Update the trackers as you go, not at the end. A run that does not read the trackers first will re-read finished work and miss pending work.

## When to use it

- Ravi adds new PDFs to `3_Research/hbr-and-journals/` (a new quarter, say). Run the monthly cycle.
- "What did the research say about X?" Search the notes.
- "Which articles back this framework?" Check the running patterns file plus the notes.
- "Run the monthly cycle." Full pipeline.

## Principles that govern every run

1. Read every page. Nothing is skipped. A coverage check confirms each row in the tracker maps to a written note. "Do not miss a single page" is literal.
2. Do not trust earlier synthesis on faith, including this engine's own past output. Re-read the source. Use an earlier synthesis only to cross-check ("did we find what it claimed, and where did it miss or overreach?"), never as a base to copy. The April 2026 Q1 synthesis turned out unreliable on re-read, which is why this rule exists.
3. Know what Ravi has already written. Before calling anything new, check `EXISTING-WRITING-INDEX.md`. Most insights sharpen an article or playbook section he already has. Name which one, and what it adds. A genuinely new idea with no home is rare, and gets flagged on its own.
4. Every edit cites the article that prompted it. No source, no edit. Edits come from what the articles actually say, not from a hunch.
5. Sharpen, do not pad. Small, exact insertions, not rewrites. One well-aimed skill beats four that overlap. Confirm a new-skill idea across sibling articles before building it.

## The note: one per article (13 parts)

The bar is a senior AI practitioner reading for leverage. Each note has:

1. Header: title, author and affiliation, publication, date, read date.
2. Bottom line, one sentence: the single most useful thing.
3. Core claim: two to four sentences, plain language.
4. How the article argues it: the mechanism, understood well enough to teach. Comprehension shows here.
5. Named frameworks and models: capture these DILIGENTLY. Every named framework gets its exact name, its author and source, and its actual components or steps written out, not just a mention. A framework noted as "the author's 2x2" without its two axes and four quadrants is a failure. Frameworks are non-negotiable scaffolding: they must be complete and accurate even though the pattern analysis in part 8 is the deliverable. If the article names a model, a matrix, a set of stages, or a typology, reproduce it precisely enough that Ravi could redraw it from your note alone.
6. Key numbers: each tagged by how solid it is (see tiers below), each with its source.
7. Quotes worth keeping: exact wording, attributed, where a paraphrase would lose the edge.
8. Patterns and new thinking: the main job (see "The main job" above). Connections across articles, what this joins to in Ravi's existing writing, deductions no single article states, tensions between sources (note which one wins and why), patterns forming across the corpus. A note whose part 8 only restates the article is incomplete. This is the section an editor reads to learn something they did not already know.
9. Where it goes (three places): the exact skill plus the precise insertion; the exact website article to refine plus what to add; the playbook section plus the nuance.
10. New or already written: checked against `EXISTING-WRITING-INDEX.md`. Name the article or section it sharpens.
11. New-skill or new-article signal: only if nothing existing can hold it. Mark "watch" until sibling articles back it.
12. Where it breaks: the conditions under which the advice fails.
13. Monday move: what an operator does with it.

## Evidence tiers (tag every number, in prose and in visuals)

- audited: in a filing, regulator-grade. Mark it ✅.
- disclosed: a company's own number, or a single study's own finding. Mark it ◆ and note the method ("RCT, n=...").
- reported or unverified: press, an author's own analysis, single-source, or disputed. Mark it ⚠.

Never treat a number from one tier as equal to one from another. A run-rate is not booked revenue, which is not GAAP revenue. "AI revenue" is usually the wrong label: break it down to the real source and the real payer.

### Real-company claims get the strongest evidence (top priority)

Wherever a real company is named (Walmart, Klarna, Intercom, Cloudflare, Microsoft, Lenovo, Schneider, and the like):

- Capture the exact claim, not a paraphrase: what happened, the number, the date.
- Attach a primary source with an inline link (company filing or press release, the vendor's own page, a major outlet). Two independent sources for any number that carries weight.
- When in doubt, do the research. Run WebSearch or WebFetch before the claim ships. If a number is disputed or you cannot ground it, mark it [VERIFY] or soften it to a general pattern. Never pass it through as fact. (The "MIT 95%" miss is the lesson: a viral stat that contradicted Ravi's own writing.)
- Prefer the exact record over the article's wording. If HBR says "killed" and the primary source says "scaled back," cite the precise truth and note the gap. It usually sharpens the point.

## The writing standard

The test for every line: an editor reads it and finds nothing to change. This is what makes the orchestrator good not just at AI but at teaching AI, with authority.

The voice, named once so every card and every applied edit carries it: the world's best teacher explaining the way Feynman did (a smart outsider follows the mechanism on first read, because the writer actually understands it), with real technical and business depth underneath (the numbers, the architecture, the P&L line, never hand-waved), and a critical thinker's habit of connecting dots across divergent ideas (the insight two sources create together that neither states alone; that connection is the product, per "The main job" above). All three at once. Clarity without depth is a summary; depth without clarity is a paper; both without the connection is a book report.

- Explain, do not gesture. Write connected prose with varied rhythm, the way HBR does. Clipped fragments and arrows gesture at a thought instead of delivering it. Use bullets and tables only for lists that are genuinely lists.
- Plain words carry hard ideas. Pick the plainest word that holds the meaning. If a technical term is truly needed, explain the plain mechanism first, then name it, and only if the name earns its place.
- Examples that teach. Anchor every abstract claim to a concrete case the reader knows. Let the example carry the idea ("Kevin the AI employee" teaches better than a coined term).
- Nuance without hedging. "This holds when X. It breaks when Y."
- Authority comes from precision, not adjectives. Cut "extremely" and "massive." State the thing exactly.

## How not to write (anti-patterns)

The skill preaches clean prose, so it must follow it. These are the tells that mark writing as AI-generated. Strip them from the notes and from anything the notes feed. Full reference: the `humanizer` skill (24 patterns from Wikipedia's "Signs of AI writing").

- No em dashes. This is the most common tell. Use a comma, a period, a colon, or parentheses instead. (Same for the spaced-hyphen used as a dash.)
- No AI vocabulary: delve, underscore, intricate, robust, landscape (as a metaphor), testament, showcase, vibrant, tapestry, foster, garner, enhance, additionally, crucial, pivotal, vital, seamless. Plain words instead.
- No copula avoidance. Write "is" and "has," not "serves as," "stands as," "boasts," "features."
- No significance inflation. No "marks a pivotal moment," "a testament to," "underscores the importance of." State the fact.
- No fake-depth -ing tails: "highlighting...", "reflecting...", "showcasing...". Cut them or replace with a real point.
- No forced rule of three. Use the number of items the idea actually has.
- No "not just X, but Y" parallelisms. Say the point straight.
- No synonym cycling. Repeat the clearest word instead of rotating thesaurus entries.
- No vague attributions ("experts argue," "studies show"). Name the source and date.
- No inline-header lists where prose works. No title-case headings (use sentence case). No decorative emojis. Straight quotes, not curly.
- No chatbot artifacts ("I hope this helps," "Certainly!"), no training-cutoff disclaimers, no sycophancy.
- No filler: "in order to" becomes "to," "due to the fact that" becomes "because," "it is important to note that" becomes the point itself.
- No generic upbeat endings ("the future looks bright"). End on a specific fact, number, or move.
- Add a pulse. Clean is not enough. Have an opinion, vary sentence length, name the real feeling, let one honest aside through. Voiceless writing reads as AI too.

Final pass on every note: ask "what still makes this read like AI?" Name the remaining tells, then cut them.

## Three places every insight goes

Each note's part 9 routes the insight to all three. The application tracker then follows it to a real edit:

1. AI-PM skills: the 65 skills plus CLAUDE.md and the orchestrator, plus any new skill that survives confirmation.
2. Website writing: the specific article in `1_My Series-MD-FILES/`. Refine it in Ravi's voice. Sharpen, do not rewrite.
3. Playbook: the routed section of `AI_Playbook.md`, with numbers tagged by tier.

## Folder layout (corrected 30 JUL 2026 to match the current library structure)

```
3_Research/hbr-and-journals/
  mit-sloan/                        MIT SMR + "Ideas Made to Matter" PDFs, notes, and cards side by side
    Q3_2026/                        latest dated intake batch
  hbr-articles/
    leadership-and-workforce/       HBR PDFs, notes, and cards side by side
    strategy/
    ai-agents/
    customer-and-market/
    responsible-ai/
    data-and-measurement/
    innovation-and-rnd/
    adoption-and-roi/
    Q3_2026/                        latest dated intake batch
  _synthesis-engine/
    Q2_2026/                        the June run's own tracking (a new run gets its own dated subfolder)
      README.md                     what this is, plus the monthly cadence
      EXISTING-WRITING-INDEX.md     what Ravi has already written (shared across runs)
      MASTER-TRACKER.md             the year at a glance, one objective per month
      APPLICATION-TRACKER.md        the separate "what we picked, what shipped" ledger
      RUNNING-PATTERNS.md           patterns collected across the run
      GLOSSARY.md                   plain-language terms introduced by any card
      00-METHOD.md                  the note bar (points to this skill)
  SYNTHESIS-COVERAGE-TRACKER.md     checklist of every source PDF with or without a note yet

1_Projects/2_Playbook_AI/
  hbr-synthesis-engine-state_Q2-2026/   the army's own tooling: progress markers, MANIFEST.tsv, `_army-deep-synthesis.js` — not reading material, never lives inside 3_Research/
```

Retired: a `1_hbr-ai-2026/` tree with per-quarter folders and a nested `hbr-synthesis/runs/<month>/` structure. That layout stopped matching reality once the corpus was promoted to a top-level `hbr-and-journals/` folder and reshelved by topic; this section now describes what is actually on disk, not what an earlier version of this skill assumed.

### Two trackers, on purpose

- Coverage tracker (each run's `TRACKER.md`, plus `MASTER-TRACKER.md`): what got read and written up. Status moves pending, absorbed, note written, routed.
- Application tracker (`APPLICATION-TRACKER.md`): what actually shipped downstream, that is, each real edit to a skill, a website article, or the playbook, with its source article and a version note. Different question, different lifecycle ("did the insight ship?"). Kept separate so "we read it" is never mistaken for "we shipped it."

## The pipeline, per run

Stage 0, frame the run. Recount the corpus (folders drift, so count again instead of trusting an old listing). Group the articles into clusters of about seven to ten for the readers. Build or refresh `EXISTING-WRITING-INDEX.md`. Write the run's `TRACKER.md` with the month's objective stated plainly and every article as a row.

Stage 1, read and write up (in parallel, by cluster). One reader per cluster reads its PDFs in full and writes one 13-part note each, to the writing and citation bar. Patterns collect in `synthesis/RUNNING-PATTERNS.md` as they show up (three or more articles makes a rule candidate, two makes a hypothesis, one that is strong gets a "watch"). A coverage reader then checks that every tracker row has a note. For a large corpus, run the readers as bounded cluster jobs with a check after each, never one giant run.

Stage 1b, the humanizer pass (required, on the output). Run every note through the `humanizer` skill before it counts as done. The goal is writing that reads like a human analyst's notebook, not AI output. The rigor, the numbers, the citations, and above all the pattern analysis stay exactly as they are. Only the slop goes: em dashes, AI vocabulary, copula avoidance, inflated significance, forced threes. Quality is unchanged. Readability goes up.

Stage 2, synthesize. Lead with the one or two structural insights that reorganize the field. Reconcile contradictions and note which source wins and why. Produce the maps that drive Stage 3: a skills map, a website-refine map, a playbook map. Then write a coverage ledger, one row per article (id, title, one-line thesis, primary routing), as proof that no note was dropped from the synthesis. Read the richest notes in full, not only their compressed summary, so their analysis survives intact. Cross-reference earlier runs for patterns that strengthened, faded, or flipped. Run the synthesis through the humanizer pass too. Ravi reviews before any edit lands.

Stage 3, apply across the three places. This is now a full method of its own: see "The apply loop" below. The one-line version: build an Application Card per note, apply each batch's skill edits as soon as its cards land (apply-as-you-go, never a pile of synthesis waiting for a someday), run the website and playbook as consolidated passes, log every shipped edit in `APPLICATION-TRACKER.md`, and close with the git sync. No edit without a source.

## The apply loop (from card to shipped edit)

This is the engine's second half, and the reason it exists at all: research that never ships is overhead. The rhythm is monthly and simple from Ravi's side. He drops raw PDFs (HBR, MIT SMR, and any other high-quality source) into the quarter folder. The engine reads each in full and produces the note and its Application Card in one pass, as detailed as the card can usefully be. The cards then drive real edits to his local files: the AI-PM skills, the website series, and the playbook. The run closes with a git commit and push to `rtp-personal-skills-repo`. Nothing waits for a someday: each batch's skill edits ship as soon as its cards land (apply-as-you-go), and the website and playbook land as consolidated passes so multiple articles hitting one file arrive as distinct, non-colliding additions.

### The Application Card, one per article (the atomic unit)

Written beside its note, next to the source PDF (`<slug>-card.md` in the matching topic-shelf folder — see "Where everything is" above, not a `runs/<month>/` subtree), in extremely plain language, with a `## Legend` glossing every framework term (new terms also merge into `_synthesis-engine/Q2_2026/GLOSSARY.md`). Each card carries, per surface:

- The exact target: the skill's full path, the website article's verified `.md` path, the exact playbook section. Verify the path exists on disk before writing it into the card; never infer it from an index.
- The exact insertion prose, ready to paste, already written to the bar below (Why plus when-wrong included, tiers attached).
- The evidence line for every number: tier (✅ audited, ◆ disclosed, ⚠ reported), primary link or [VERIFY] flag, and the population the number was measured on ("wealth-management firms," "n=58, one lab task"). A card that generalizes a figure beyond its population is wrong even when the number is right.
- A "no edit" verdict where the insight is already covered. "No edit, covered by X" is a correct and common answer; restraint is part of the job.
- A `.applied-card` marker on disk once its edits ship.

### The standing gates (every edit, every surface)

1. The WHY gate, highest priority. Every rule or insert lands as: the rule, why it holds (the mechanism), and when it is wrong or over-warns. Prescriptive-only inserts fail review, because an AI using the skill must be able to judge in context, not follow blindly.
2. Plain language plus Legend. Lead with the plain mechanism, then name the term only if the name earns its place. Every touched skill carries a `## KEY TERMS (plain language)` legend covering the terms it actually uses.
3. Business-clarity on the front matter. Any skill touched gets its `description` raised to the bar: what it does and when to use it in words any business stakeholder reads on first pass, plus a `Pairs with:` line naming companion skills and why (this feeds the orchestrator's companion map). Skill IDs never change; renames break the registry, the git repo, and every cross-reference.
4. The primary-source gate. When any claim, number, or nuance is uncertain, read the original PDF, not the note. The note is secondary; the article is ground truth.
5. Version before edit, always: snapshot to `versions/skills/{DDMMMYYYY}/` or `versions/projects/{DDMMMYYYY}/` first. Then log the shipped row in `APPLICATION-TRACKER.md` with its source.
6. The container check, after every insert. Re-read the host section's heading and closing line: an insert that turns "three forces" into four must update both, or it reads as exactly what it is, a block dropped in by a machine.
7. Surface-appropriate notation. Tier glyphs, [VERIFY] tags, and editorial instructions ("note the conflict") are internal working notation. On the website they must land as reader-facing prose ("disclosure: the study's author holds equity in Bluon"). Cards carry website insertions already in reader-facing form.
8. The concentration ledger. When one study feeds three or more inserts across the canon, register it in `RUNNING-PATTERNS.md` as a named fragility, so a failed replication has a known blast radius.

### Surface 1: the AI-PM skills (raise to the gold standard with every touch)

Read the whole skill before editing it, not just the insertion point; the best enhancements of the June run came from reading skills in full. Place the insert where the skill's existing framework reaches for it, and make it cohere: a skill is a thought system, not a pile of research findings. With every touch, raise the whole file to the gold-standard bar: nuanced how-to-think direction in Ravi's thinking patterns, the authority of a senior world-class AI PM with technical and business depth and no hype, fully self-explanatory (plain mechanism first, legend for the terms, headings that say what is actually happening), Why plus when-wrong on every rule, tier and link on every number.

Watch for accretion, the biggest structural risk of a monthly loop. When a skill approaches five appended modules, or three bullets repeat the same underlying test, consolidate before adding: merge, name the shared spine, or split the skill (flag the split for Ravi first). One deeply coherent skill beats a sediment of true facts.

### Surface 2: the website series (strengthen, challenge, or write new)

Three moves, chosen by what the evidence actually does to what Ravi has published:

- Strengthen. New evidence supports a published view: append at the exact place the article already reaches for it, as a labeled section or callout in Ravi's voice. Enrich, never overwrite; the snapshot plus a pure-addition diff is the proof.
- Challenge. New evidence cuts against a published claim: never silently rewrite it. Add a dated, labeled correction section ("The evidence has moved, [Month Year]") that states the original view, the new evidence with its tier, and Ravi's updated position. A public record that updates itself honestly is worth more than one that was quietly always right. Flag every challenge move for Ravi's sign-off before it ships; these are his published words.
- Write new. Only when three or more sources converge on a theme no existing article holds (the part-11 signal, confirmed across siblings). Draft it with `rtp-deep-dive-writer` from the cards' evidence, and route it into the series index.

All website edits are voice-critical: reader-facing attribution, no internal notation, and the four-exemplar voice sign-off pattern (ship a small diverse batch, get Ravi's sign-off, then fan out).

### Surface 3: the playbook

Land insights as distinct paragraphs in the exact section the card names, and when several articles hit one section, synthesize them into one tight in-voice piece rather than queueing paragraphs (the June run folded roughly fifteen queued paragraphs into four additions; that ratio is the standard). Run the container check on every touched section. Rebuild the HTML and PDF (`build_playbook.py`) at close-out, or log the rebuild as pending.

### The QA pass (mandatory after every apply batch, before close-out)

Applied work is not done work. A separate critical pass, ideally a fresh session or agent that did not write the edits, verifies every batch the way the Fable-5 pass verified the June run (which found nine defects in work that had already passed its own review). The checklist:

1. Diff every changed file against its pre-edit snapshot. The diff must be pure addition on website articles and the playbook (zero deletions is the proof that "enrich, never overwrite" held), and coherent insertion on skills.
2. Trace every inserted number back to the primary PDF text, not to the note. Open the PDF, find the sentence, confirm the figure, the population, and the framing direction all match. A number the article frames as a win must not land as a cost, and a figure measured on one population must not ship generalized.
3. Never upgrade a tier. An analyst forecast is never ✅. A single study is ◆ at best. Anything press-only or disputed stays ⚠. When the run cannot ground a claim, it carries [VERIFY] or gets softened to a pattern; it never ships as fact. Web-verify (two independent sources) anything that ships to an external surface, and resolve every [VERIFY] flag before the website or playbook carries the claim.
4. Run the container check on every touched section, confirm every touched skill's legend covers the terms its inserts actually use, confirm the front matter still parses as YAML, and confirm no internal notation leaked into published prose.
5. Score the batch honestly: pass, needs-fix, or weak, per file, with the specific defect. Fix what can be fixed now (versioned), and put what needs Ravi's judgment on a named punch list. A QA pass that only praises is a failed QA pass.

Why this is non-negotiable: hallucination in this system is rarely an invented fact; it is a real fact that drifted, a tier that got rounded up, a scope that got dropped, a frame that got inverted. Every one of those passed a writer's self-review in June. Only the adversarial re-read against the primary caught them.

### The loop that improves the loop (the orchestrator learns from every run)

Each run must leave the system smarter, not just the canon bigger. At close-out: log any real waste in `5_Knowledge/session-anti-patterns.md`; add patterns seen once or twice to `5_Knowledge/hypotheses.md`; promote anything confirmed three times to `5_Knowledge/rules.md`; and when a run teaches a durable lesson about how to run (a new gate, a failure class, a review discipline), fold it into this skill AND into the orchestrator (`rtp-orchestrator/SKILL.md`), versioned, so every future session starts from it. The June run added six gates this way; the QA pass above added four more. That is the compounding: the same loop that updates Ravi's writing updates the machinery that updates Ravi's writing.

### Close-out: track, sync, push (a run is not done until this ships)

1. Trackers: `APPLICATION-TRACKER.md` (every shipped edit with source), the run's progress file, `SKILL-REGISTRY.md` and `2_Skills/CHANGE_LOG.md` (with the why).
2. Sync the three skill locations (`2_Skills/`, `.claude/skills/`, `rtp-personal-skills-repo/skills/rtp-*/`), via `./scripts/skill-sync.sh` on Ravi's machine or a manual copy in a sandbox (the script's paths are Mac-absolute and will not run in a mounted sandbox).
3. Git: `git add -A`, commit with a message naming the run and the surfaces touched, then push to `github.com/raviteja-palanki/rtp-personal-skills`. If the environment has no credentials, commit locally and log the pending push in the tracker and `ACTION-PLAN.md`; the push is Ravi's one manual step.

## Running the army (orchestration, learned the hard way)

The readers and reviewers run as a resumable army, one script: `1_Projects/2_Playbook_AI/hbr-synthesis-engine-state_Q2-2026/_army-deep-synthesis.js`, launched with the Workflow tool. Four rules keep it honest, each from a real failure:

1. Batch, never fan out the whole corpus at once. The June run launched all 66 articles together and tripped the account's rolling session limit in five minutes, losing every review that window. Each run now takes a bounded slice (default 12, set by `args {batch: N}`) and stops clean. This is the script form of the Stage 1 rule "bounded cluster jobs, never one giant run."

2. A note counts as done only when its review marker exists. Each article gets a `.pass` marker written only after a reviewer passes it on pattern depth, framework diligence, tiered citations, and clean prose. A window that dies after a note is written but before it is reviewed leaves no marker, so the next run re-reviews it. Finished, reviewed work is never redone or degraded. Resume touches only un-passed articles.

3. The reviewer holds a citation gate. The single most load-bearing named-company claim in a note must carry an inline primary link, a [VERIFY] tag, or a note that the article's wording was checked against the primary record. A striking number stated as fact with no source fails review. When in doubt the reviewer runs one search before passing.

4. Synthesis runs only when every article has passed, and it must be comprehensive. It reads every summary plus the richest notes in full, and writes a coverage ledger of all articles. The near-miss that forced this: three deeply-analysed POC notes sat outside the run set, with no summary file, and would have been excluded from the final synthesis even though one carried a candidate spine for the whole run. Lesson: any note that exists must be inside the run set, or it does not reach the synthesis.

## Verification: the HBR editor's checklist

Read each note the way an HBR editor reads a submission, and answer each question. Any "no" sends the note back before it ships.

Substance:
- Did I learn something from part 8 that I did not already know? (If part 8 only restates the article, reject. The pattern is the point.)
- Is the main claim clear in one read, and is the mechanism actually explained, not just named?
- Is every insight routed to a real place: a named skill, a named website article, a named playbook section? And does each edit cite the article behind it?
- Is "new" judged against `EXISTING-WRITING-INDEX.md`, or just assumed?

Evidence:
- Is every number tagged by tier (✅ audited, ◆ disclosed, ⚠ reported)? Is any run-rate being passed off as revenue?
- Does every named company carry the exact claim, the date, and a primary inline link? Were the claims that carry weight web-verified?
- Where the article's wording is looser than the record, did I cite the precise truth and note the gap?

Writing (the humanizer pass ran):
- Zero em dashes. None of the AI vocabulary. No copula avoidance, no inflated significance, no forced threes, no inline-header lists where prose works.
- Plain words. Real examples that carry the idea. Sentence-case headings, straight quotes, no decorative emojis.
- Does it read like a sharp human analyst wrote it, with a point of view, or like clean AI filler?

Coverage:
- Is every article in the run read in full, with its tracker row reconciled and nothing skipped?
- Are the trackers updated: coverage rows moved, and any shipped edit logged in the application tracker with its source?

## Updating this skill

After each run, refine the clusters, the note template, and the trackers from what the run taught. Version to `versions/skills/{DDMMMYYYY}/`, bump the version, update `SKILL-REGISTRY.md` and `2_Skills/CHANGE_LOG.md`, and run `skill-sync.sh` across all three locations.
