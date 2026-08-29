---
name: rtp-hbr-research
version: v3.7_latest
description: 'Monthly research-synthesis and apply engine for Harvard Business Review, MIT Sloan, and other top management research. Reads every PDF in full, writes one citation-disciplined note per article (numbers tagged by evidence strength, company claims backed by primary links, plain HBR-grade prose), finds patterns across articles, and checks each insight against what Ravi has already written, then ships those insights into the three places his thinking lives: the AI-PM skills, the website series, and the playbook. Everything versioned, tracked, git-synced. Use whenever Ravi adds research to 3_Research/09_hbr-and-journals/, says "HBR research", "research synthesis", "process the articles", "run the monthly cycle", "apply the cards", or asks what earlier research said. Pairs with rtp-humanizer (the mandatory language gate, opened and read before the first note), rtp-deep-dive-writer (website articles), rtp-claude-admin (governance sync).'
---
# HBR research synthesis engine v3.6

> v3.6 (07 AUG 2026): the quote gate. Six of six retrofit batches broke the quote rule while believing they had followed it, and the only check that caught it was a byte-diff of every quoted span against the pre-edit copy. That diff is now mandatory, along with a digit-stream diff. Also separated quote drift against the source PDFs into its own workstream: roughly thirty quotations across ten notes do not match their article, some introduced by mechanical sweeps reaching inside quote marks. See "The quote gate" and "Quote drift is its own workstream".

> v3.5 (07 AUG 2026): reuse became the default. Ravi's ruling: "I'm ok if you re-use HBR words as is as possible." Paraphrase was the norm and borrowing the rescue; it is now the other way round, because paraphrase drifts one direction only, toward the grander word, and ten paraphrases produce a note nobody can read. Added the understandability test, which outranks the anti-pattern checklist: a note can pass every word list and still be unreadable, and one did. Also added the retrofit protocol for repairing notes already written. See "Reuse is the default", "The understandability test", and "The retrofit pass".

> v3.4 (06 AUG 2026): the language gate. `rtp-humanizer` is now opened and read in full before the first note of a run, and the run's opening report to Ravi names which files were opened and when. The skill had pointed at the generic `humanizer` plugin skill; it now points at Ravi's own, which supersedes it. Added the five shapes that survive a word-list pass (fake-strong verbs, superlative reaching, faux-insight setups, negative listing, robotic rhythm), because a session on 06 AUG shipped all five with zero banned words present. The editor's checklist now checks those five by name, plus the length test, the direction test and a read-aloud against the article. See "The language gate" and "Borrow the article's language".

> v3.3 (05 AUG 2026): corrected the note's own part count. The skill said 13 parts in its header while requiring Parts 14 and 15 in a later section, so an agent reading the top built a note missing the two parts that feed the accumulating ledgers. It is 15 parts everywhere now. Also repointed the engine home from the June run's `Q2_2026/` subfolder to the live `_synthesis-engine/`, and named `START-HERE-NEXT-SESSION.md`, `ARTICLE-GRAPH.csv`, `queue_2026.csv` and `PROMPT-FOR-NEW-ACCOUNT.md` as the four files a cold session actually needs. No count lives in this skill's prose; derive every number from the graph.

> v3.2 (30 JUL 2026): four outputs per article instead of one. A note traps its own best material, so every article now also produces a `.frameworks.md` (every named framework reproduced completely, with a plain-language legend) and a `.cases.md` (every named-company case with problem, before-state, approach, results, learnings, tier, and source link), both centralized on their own shelves so they can be browsed and compared across the corpus instead of hunted note by note. Added the two accumulating files that outlive every run, `NOVEL-INSIGHTS.md` and `OPEN-ASSUMPTIONS.md`, plus Parts 14 and 15 of the note that feed them. Added the parallel-agent rules, and five standing checks that each came from a real near-miss. Naming is now `<stem>_Note.md` on the source PDF's exact filename stem, so all four files and both index CSVs join without fuzzy matching. See "Four outputs per article", "Two accumulating files", and "Running this with parallel agents" below.

> v3.1 (30 JUL 2026): corrected every path in this skill to match where the corpus actually lives, after two library reorgs this file's text never tracked. The corpus moved from `3_Research/1_hbr-ai-2026/` to `3_Research/09_hbr-and-journals/` (reshelved by topic); the engine home moved to `09_hbr-and-journals/_synthesis-engine/Q2_2026/`; and 125 of the June run's own notes and cards were found sitting in a disconnected project folder (`1_Projects/2_Playbook_AI/hbr-synthesis-output/`), never paired with their source PDFs, until this pass moved them next to their matched PDF (matched by each note's own title line against the corpus index, not by filename). A separate 104-file batch of the army's own progress markers had also been sitting inside `3_Research/` mislabeled as "articles" for at least one prior pass; it now lives at `1_Projects/2_Playbook_AI/hbr-synthesis-engine-state_Q2-2026/`, outside the research corpus entirely. The lesson this leaves for every future run: re-verify every path in this section against disk before trusting it, the same discipline this skill already demands of a citation. Full account in `5_Knowledge/hypotheses.md` H28-H31.
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
- `3_Research/09_hbr-and-journals/mit-sloan/` — MIT Sloan Management Review + "Ideas Made to Matter," with its own dated intake-batch subfolder (currently `Q3_2026/`)
- `3_Research/09_hbr-and-journals/hbr-articles/<topic>/` — HBR pieces sorted by subject (`leadership-and-workforce/`, `strategy/`, `ai-agents/`, `customer-and-market/`, `responsible-ai/`, `data-and-measurement/`, `innovation-and-rnd/`, `adoption-and-roi/`), each with its own dated intake-batch subfolder
- any later drop lands in `3_Research/00_NEW/` first; `rtp-research-librarian` sources, dates, and shelves it into one of the folders above before this skill ever reads it

Engine home and working files (the June 2026 run's own tracking; a new month's run gets its own dated subfolder alongside this one):
- home: `3_Research/09_hbr-and-journals/_synthesis-engine/` — the live run's state. **Read `START-HERE-NEXT-SESSION.md` there first; it is the one file that describes the current state of the run.** The `Q2_2026/` subfolder beside it is the June run's historical record, not current state
- the machine-readable truth on what has been synthesised: `09_hbr-and-journals/ARTICLE-GRAPH.csv`, rebuilt from the tree and never hand-edited. **No count lives in prose. Derive every number from this file, normalising filenames to NFC on both sides**
- the work queue, regenerated newest-first from the graph: `_synthesis-engine/queue_2026.csv`
- the handoff for a fresh account: `_synthesis-engine/PROMPT-FOR-NEW-ACCOUNT.md`, rewritten at every session end
- what Ravi has already written: `_synthesis-engine/Q2_2026/EXISTING-WRITING-INDEX.md`
- year at a glance: `_synthesis-engine/Q2_2026/MASTER-TRACKER.md`
- shipped-edits ledger: `_synthesis-engine/Q2_2026/APPLICATION-TRACKER.md`
- running patterns: `_synthesis-engine/Q2_2026/RUNNING-PATTERNS.md`
- the note bar and the term glossary: `_synthesis-engine/Q2_2026/00-METHOD.md` and `GLOSSARY.md`
- the army's own tooling (progress markers, the run manifest, the orchestration script) lives OUTSIDE `3_Research/` entirely, at `1_Projects/2_Playbook_AI/hbr-synthesis-engine-state_Q2-2026/` — this is machinery, not reading material, and must never be re-filed into a research shelf (it was, once, for at least one full pass; see H28)
- the running coverage checklist of which source PDF has a note yet: `3_Research/09_hbr-and-journals/SYNTHESIS-COVERAGE-TRACKER.md`

Where a note and its card actually land (corrected — not a `runs/<month>/` subtree): directly beside the source PDF, in that same topic-shelf folder. A note is `<slug>.md`, its card is `<slug>-card.md`, its optional company-case companion is `<slug>-cases.md` — all three sit next to `<slug's-source>.pdf`. If a note's location is ever unclear, pair it back to its PDF by matching its own title line against the corpus index, never by guessing from filename (the method: H30 in `5_Knowledge/hypotheses.md`).

Outputs, the three places insights ship to:
1. Skills: edit the source at `2_Skills/ai-pm-skills/<cluster>/skills/<skill>/SKILL.md` (the `/skills/` segment is real and easy to drop by mistake), then sync to `.claude/skills/<skill>/SKILL.md` (folder name unprefixed) and `rtp-personal-skills-repo/skills/rtp-<skill>/SKILL.md` (folder name rtp- prefixed). Run `./scripts/skill-sync.sh` to confirm all three match.
2. Website writing: edit the article at `1_Projects/1_my-personal-website/1_My Series-MD-FILES/My Website all latest MD files/<series>-md/<article>.md`. **Corrected 02 AUG 2026.** The live series folders are `agentic-stack-md`, `harness-engineering-md`, `environment-series-md`, `evals-series-md`, `ai-pm-os-md`, plus `site-pages-md` and `frontier-companies-md`. The sibling `version1/` folder holds the old `<NN-series>/` names and is Ravi's personal archive: never read it for current state, never route into it. Filenames are lowercase and were renumbered in that pass (`L2-T02-compounding-moats.md` became `l2-t12-building-compounding-moats.md`), so **match on the slug body, never on the `tNN` digits, and confirm the file exists on disk before writing the path into a note or card.**
3. Playbook: edit the section in `1_Projects/2_Playbook_AI/AI_Playbook.md`.

## Start every run by reading the trackers

Before opening a single PDF, read the state, so you pick the right inputs and write to the right place:
1. `MASTER-TRACKER.md`: which month is this, and what is its objective.
2. the run's `TRACKER.md`: which articles are already written up, and which are still pending. Read only the pending ones.
3. `APPLICATION-TRACKER.md`: which insights already shipped, so you do not propose them twice.
4. `EXISTING-WRITING-INDEX.md`: what Ravi has already written, so "new" is judged against fact.

Then inputs are the pending articles, and outputs are the routed targets named in each note's part 9. Update the trackers as you go, not at the end. A run that does not read the trackers first will re-read finished work and miss pending work.

## When to use it

- Ravi adds new PDFs to `3_Research/09_hbr-and-journals/` (a new quarter, say). Run the monthly cycle.
- "What did the research say about X?" Search the notes.
- "Which articles back this framework?" Check the running patterns file plus the notes.
- "Run the monthly cycle." Full pipeline.

## Principles that govern every run

1. Read every page. Nothing is skipped. A coverage check confirms each row in the tracker maps to a written note. "Do not miss a single page" is literal.
2. Do not trust earlier synthesis on faith, including this engine's own past output. Re-read the source. Use an earlier synthesis only to cross-check ("did we find what it claimed, and where did it miss or overreach?"), never as a base to copy. The April 2026 Q1 synthesis turned out unreliable on re-read, which is why this rule exists.
3. Know what Ravi has already written. Before calling anything new, check `EXISTING-WRITING-INDEX.md`. Most insights sharpen an article or playbook section he already has. Name which one, and what it adds. A genuinely new idea with no home is rare, and gets flagged on its own.
4. Every edit cites the article that prompted it. No source, no edit. Edits come from what the articles actually say, not from a hunch.
5. Sharpen, do not pad. Small, exact insertions, not rewrites. One well-aimed skill beats four that overlap. Confirm a new-skill idea across sibling articles before building it.

## The note: one per article (15 parts)

**It is 15 parts, not 13.** Parts 1 to 13 are below. Parts 14 and 15 were added in v3.2 and are defined in their own section further down, because they are what feed the two accumulating files. A note missing 14 and 15 is incomplete.

The bar is a senior AI practitioner reading for leverage. Each note has:

1. Header: title, author and affiliation, publication, date, read date.
2. Bottom line, one sentence: the single most useful thing.
3. Core claim: two to four sentences, plain language.
4. How the article argues it: the mechanism, understood well enough to teach. Comprehension shows here.
5. Named frameworks and models: capture these DILIGENTLY. Every named framework gets its exact name, its author and source, and its actual components or steps written out, not just a mention. A framework noted as "the author's 2x2" without its two axes and four quadrants is a failure. Frameworks are non-negotiable scaffolding: they must be complete and accurate even though the pattern analysis in part 8 is the deliverable. If the article names a model, a matrix, a set of stages, or a typology, reproduce it precisely enough that Ravi could redraw it from your note alone.
6. Key numbers: each tagged by how solid it is (see tiers below), each with its source.
7. Quotes worth keeping: exact wording, attributed, where a paraphrase would lose the edge. **Plus a `### Plain lines` block holding the two or three sentences where the author explains the mechanism in the fewest words.** Those set the register for Parts 8 and 14. See "Borrow the article's language" below.
8. Patterns and new thinking: the main job (see "The main job" above). Connections across articles, what this joins to in Ravi's existing writing, deductions no single article states, tensions between sources (note which one wins and why), patterns forming across the corpus. A note whose part 8 only restates the article is incomplete. This is the section an editor reads to learn something they did not already know.
9. Where it goes (three places): the exact skill plus the precise insertion; the exact website article to refine plus what to add; the playbook section plus the nuance.
10. New or already written: checked against `EXISTING-WRITING-INDEX.md`. Name the article or section it sharpens.
11. New-skill or new-article signal: only if nothing existing can hold it. Mark "watch" until sibling articles back it.
12. Where it breaks: the conditions under which the advice fails.
13. Monday move: what an operator does with it.

## Four outputs per article, not one (added v3.2, 30 JUL 2026)

A note alone traps its own best material. The framework sits in Part 5 where nobody browsing frameworks will find it; the company case sits in Part 6 where nobody hunting for a citable example will find it. So every article now produces four files, and the run is not done until all four exist.

| file | location | what it is for |
|---|---|---|
| `<stem>_Note.md` | beside the source PDF, in its topic shelf | the 15-part note: interpretation, mechanism, patterns, routing, novel insights, open assumptions |
| `<stem>.frameworks.md` | `09_hbr-and-journals/_frameworks/` | every named framework, reproduced completely, each with a plain-language legend |
| `<stem>.cases.md` | `09_hbr-and-journals/_case-in-point/` | every named-company case, with problem, before-state, approach, results, learnings, tier, and source link |
| `<stem>-card.md` | beside the note | the Application Card (see "The apply loop") |

**`<stem>` is the source PDF's filename with `.pdf` removed, character for character** — spaces, punctuation, curly apostrophes, and the trailing `_Mon_YYYY` tag included. Do not slugify, shorten, or invent an ID. The stem is the join key across four files and two index CSVs, and an approximation forces someone to fuzzy-match it back later. That has already happened once in this system, to 79 files.

The full contract for the two extraction files, including per-type completeness rules and the tier discipline, is `09_hbr-and-journals/_frameworks/EXTRACTION-SPEC.md`. Read it before writing either file.

## Two accumulating files that outlive every run (added v3.2)

These are the highest-value artifacts the engine produces, because they are the only ones whose worth is purely cumulative. A note is bounded by its article. These are bounded by the corpus.

**`_synthesis-engine/NOVEL-INSIGHTS.md`** — the cross-corpus pattern ledger. Every insight carries the articles supporting it, a count, a named falsifier, and a status on the ladder `watch` (1 article) → `hypothesis` (2) → `rule candidate` (3+) → `promoted` (to `5_Knowledge/rules.md`) → `retired` (falsified, kept with the reason). Nothing is ever deleted: a falsified insight tells the next session what has already been tried. **An insight with no falsifier is an opinion wearing evidence costume.** Append to this file on every run, and reconcile: an insight that gains a third confirming article gets promoted, one that meets a counterexample gets refined or retired in writing.

**`_synthesis-engine/OPEN-ASSUMPTIONS.md`** — what the synthesis needed to know and could not settle. Two kinds of entry. First, **load-bearing assumptions**: when a synthesis needs a fact it does not have, name the assumption and proceed, because the alternative is a sentence that reads as if the fact were known. Second, **recurring unanswerable questions**, so the fifth encounter is recognized as the fifth rather than rediscovered. Every entry names the specific thing that would settle it; "more research needed" is not an entry. Statuses: `open` → `answered` (with source) → `retired` (unanswerable, with why) → `escalate` (needs Ravi's judgment, not more research).

Why this matters more than it looks: a person reading 200 files holds about seven in working memory and finds the patterns they already expected. These two files are the defense against that limit, and they are the reason the corpus produces insight a single reading cannot.

## Part 14 and Part 15 of every note (added v3.2)

Parts 1 to 13 stay. Two more are required, making 15 in total, and they are what feed the accumulating files:

**14. Novel insights, reasoned from first principles.** Not a restatement of the article and not a restatement of Part 8's patterns. This is the deduction the article makes possible but does not make: the connection to a second article, the claim that follows from joining two facts, the reframe that changes what the reader would build. Each one gets a falsifier. If the article genuinely supports no novel deduction, write "None beyond Part 8" and mean it, rather than manufacturing one.

**15. Open assumptions and what I would want to know.** What did this note assume in order to finish? What question did the article raise that it cannot answer? What would change the reading if you learned it? Each entry names what would settle it. These append to `OPEN-ASSUMPTIONS.md`.

Both parts append upward to the accumulating files at the end of every run. A note that produces neither a novel insight nor a named assumption across a whole batch has almost certainly been read shallowly.

## Running this with parallel agents (added v3.2)

Reading is parallelizable. Cross-article pattern-finding is not. Split accordingly.

**Fan out for:** reading an article and writing its four files; extracting frameworks and cases from existing notes; retrofitting shelves. Bounded, verifiable, independent per article.

**Keep central:** Part 8's cross-article patterns, and all reconciliation into `NOVEL-INSIGHTS.md`. An agent that has read three articles cannot find a pattern that needs forty. This is the difference between parallelism and fragmentation.

**The rule that makes fan-out work:** an agent cannot find batch-level patterns, so **hand it the patterns already established and ask it to confirm, extend, contradict, or add.** Pass the current `NOVEL-INSIGHTS.md` entries by letter into every agent prompt, and require the agent to cite letters in its report so the lead can reconcile. The June 2025 finance-trio agent falsified half of one pattern and supplied two better replacements precisely because it was given the pattern to test rather than asked to find patterns from scratch.

**Every agent prompt must carry, without exception:** the `EXTRACTION-SPEC.md` path, one exemplar note and one exemplar cases file to read first, the exact output paths, the evidence-tier rules, the established insight letters, the voice anti-pattern list, and an instruction to flag uncertainty rather than smooth it. Then **review every returned file against the source.** Draft quality is never final quality, and an agent's confident report is not verification.

**Standing checks, each from a real near-miss:**

1. **"In its first year" requires the year to have elapsed.** Barnes Group was acquired January 2025; a June 2025 article claimed a five-times first-year return.
2. **Provisioning is not usage.** "Students will have access to" is not "1 million users." Same class of error as seats-sold versus software-used.
3. **A claim of measurability with no measurement is tiered ⚠ and never softened into usability.** A chief AI officer calling improvements "measurable" while supplying no measurement is the worst evidence failure available, because it sounds like data.
4. **A `[VERIFY]` flag has two meanings that need separating:** "nobody looked hard enough" versus "no such document exists" (a client-owned company files no management report). Conflating them makes diligence look like laziness.
5. **A scopeless productivity number needs its denominator asked for.** Expect roughly half when the scope moves from the task to the organization: Vanguard's own figures are ~25% for coding alone, 10-15% across the development life cycle.

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

## Borrow the article's language (added 06 AUG 2026, from Ravi's instruction)

**HBR and MIT Sloan copy is professionally edited. The article almost always says the thing more plainly than the note does.** So stop inventing phrasing. Take the author's.

This rule exists because of a real failure. A session on 06 AUG 2026 wrote thirty batch sections and Ravi could not read them. The words were not on any banned list: "bears on", "carries", "arrives", "yields", "worth naming", plus a superlative in almost every section. Fake-strong verbs and puffery. The agent had invented its own register instead of borrowing the one sitting in front of it, in fifteen professionally edited articles.

**Part 7 captures quotes worth keeping, meaning the memorable ones. Add a second job: capture the article's PLAINEST sentences.** Not the quotable line. The sentence where the author explains the mechanism in the fewest, shortest words. Log two or three per article under a `### Plain lines` sub-heading in Part 7.

Real examples, all from the Jul-2026 batch, all better than anything a synthesis would have produced unaided:

> "Trust is not a feature. It is the foundation."
> "Skip discovery, and you automate the wrong experience."
> "Green still means go, red still means stop."
> "A security problem dressed as a design problem."
> "Trust is built less by impressive outputs and more by honest boundaries."
> "The more capable they are, the more they absorb, until the best of them leave."

**Then use that register when you write Parts 8 and 14.** Short verbs. Concrete nouns. One clause where three would fit.

### The four tests

1. **Length test.** If your sentence about a thing is longer than the article's sentence about the same thing, use the article's.
2. **Verb test.** Keep the author's verb. If they wrote "stop", do not write "terminate". If they wrote "is", do not write "serves as" or "carries".
3. **Direction test.** Paraphrase always drifts toward the fancier word, never the plainer one. So when you paraphrase, check which direction you moved. If it got grander, you got it wrong.
4. **Read-aloud test.** Read your Part 8 out loud against a paragraph of the article. If the article sounds like a person and your note sounds like a report, rewrite the note.

**One thing this rule does not license.** Do not smuggle the author's *claim* in while borrowing their *words*. A plain sentence is still a claim that needs its tier, its population and its source. Borrow the phrasing, keep the evidence discipline.

**And do not flatten a genuine finding into the article's frame.** The whole point of Part 8 is the deduction the article does not make. Say that in the article's plain register, not in the article's argument.

### Reuse is the default, not the fallback (Ravi's ruling, 07 AUG 2026)

His words: "I'm ok if you re-use HBR words as is as possible."

That settles a question the earlier version left open. Paraphrasing was treated as the norm and borrowing as a rescue. It is the other way round. **When the article has already said it well, use its sentence.** Quote it if it is distinctive, lift the phrasing if it is plain. Invent wording only where you are saying something the article does not say, which is Parts 8 and 14.

The reason is mechanical, not stylistic. Every paraphrase is a chance to drift, and paraphrase drifts one direction only, toward the grander word. Ten paraphrases produce ten small upgrades in register and a note nobody can read. Reuse has no drift.

**What still needs your own words:** the deduction in Part 8, the novel insight in Part 14, the routing in Part 9, the break conditions in Part 12. Those are yours because the article does not contain them. Everything describing what the article says can be the article's own language.

**What reuse does not license:** borrowing the author's *claim* along with their words. A plain sentence is still a claim that needs its tier, its population and its source.

### The understandability test, which outranks the checklist

The bar is not "passes the anti-pattern list." A note can pass every list and still be unreadable, and one did: on 06 AUG 2026 thirty batch sections cleared every banned word and Ravi could not read them.

**So the test is a person, not a list.** Hand the paragraph to a smart operator who has not read the article. Do they understand it on first read? If they have to go back to the start of the sentence, rewrite it. Length, clause count and abstraction are what break comprehension, and none of them appear on a word list.

Three questions per paragraph, in this order:

1. **Would I say this out loud to a colleague?** If not, it is not written yet.
2. **Is any sentence of mine longer than the article's sentence about the same thing?** Then use the article's.
3. **Can I cut a clause with no loss?** Then it was not carrying anything.

## The retrofit pass (repairing notes already written)

A retrofit is a re-read of finished synthesis files against their source articles, to fix language, tone and wording. It is not a slop-word sweep, and running it as one is the mistake that made it necessary.

**Tracker:** `_synthesis-engine/RETROFIT-TRACKER.md`, generated from disk by `tools/build-retrofit-tracker.py`. The file list is never hand-edited. Status lives in `tools/retrofit-state.json` so a rebuild cannot lose completion state. Mark each file done as you finish it, not at the end of a batch, because agents die mid-flight and an unmarked finished file gets redone.

**Never mass-edit a retrofit.** A regex across 400 files cannot tell a paraphrase that drifted from the author's own sentence, and it cannot read. The unit of work is one file with its article open beside it. Mechanical sweeps are legitimate only for a banned character with a deterministic replacement, and even then every distinct transformation gets previewed before anything is written.

**Per file, in order:**

1. Open `rtp-humanizer` in full, once per session.
2. Open the synthesis file and its source article. The article is beside the note, same filename stem, `.pdf` or `.txt`.
3. Read the note against the article, paragraph by paragraph. You are looking for two things: sentences that are harder than the article's sentence about the same thing, and sentences that say less than they appear to.
4. Replace invented phrasing with the article's, per "Reuse is the default".
5. Apply the understandability test to every paragraph you touched.
6. Log the file in the tracker with whether you opened the source.

**What a retrofit must never change:** a number, a population, an evidence tier, a `[VERIFY]` tag, a quotation, an article key, a path, a routing target, or any claim. If an edit would change what a sentence asserts, stop and leave it. Prose only.

**A note on self-review blocks.** Several notes carry a line listing the banned words they checked for. Those are mentions, not uses, and editing them changes what the check claims. Leave them and whitelist them in the detector instead.

### The quote gate, the most repeated failure on this job

**Six of six retrofit batches broke the quote rule while believing they had followed it.** Two caught eight and four of their own only because they ran a diff. Without it, every breach ships.

**The mechanism is always the same.** You split a long sentence. A quotation that sat mid-sentence now ends the new one. The comma inside the quote marks looks wrong, so you make it a period. You have edited the author's words. The same pull capitalises a lowercase opening, drops a question mark, and swaps a colon for a period.

**So copy the file before editing and diff both streams before reporting:**

```bash
cp "<note>" /tmp/pre_<name>
# ...edit...
diff <(grep -o '"[^"]*"' /tmp/pre_<name>) <(grep -o '"[^"]*"' "<note>")     # quotes
diff <(grep -o '[0-9][0-9.,%]*' /tmp/pre_<name>) <(grep -o '[0-9][0-9.,%]*' "<note>")   # digits
```

Both must return nothing. Revert a breach by restructuring the host sentence, never by adjusting the quote. **Revert even when your version matches the PDF better than the note does**, because a quote correction is a claim correction and hiding one inside a wording pass makes it invisible to review.

**Three things wear quote marks and only the first is protected:**

- **A source quotation.** Absolute, punctuation included.
- **The note's own scare-quoted shorthand.** Not from any article. May be rewritten away with its sentence. Check the PDF before deciding.
- **Ready-to-paste website copy in a Part 9 insertion block.** The marks are functional. Keep them, split inside them.

### Quote drift is its own workstream, not retrofit work

Roughly thirty quotations across ten notes do not match their source article: a comma for a period, a capitalised opening, a dropped question mark, an ellipsis hiding a cut clause. Some were introduced by mechanical sweeps that reached inside quote marks, which is the strongest argument in this file against mass edits.

**Never repair these during a retrofit.** They need a pass with the PDF authoritative and every change logged, because each one is a claim correction. Log what you find with file, line, the note's version and the PDF's version.

## The writing standard

The test for every line: an editor reads it and finds nothing to change. This is what makes the orchestrator good not just at AI but at teaching AI, with authority.

The voice, named once so every card and every applied edit carries it: the world's best teacher explaining the way Feynman did (a smart outsider follows the mechanism on first read, because the writer actually understands it), with real technical and business depth underneath (the numbers, the architecture, the P&L line, never hand-waved), and a critical thinker's habit of connecting dots across divergent ideas (the insight two sources create together that neither states alone; that connection is the product, per "The main job" above). All three at once. Clarity without depth is a summary; depth without clarity is a paper; both without the connection is a book report.

- Explain, do not gesture. Write connected prose with varied rhythm, the way HBR does. Clipped fragments and arrows gesture at a thought instead of delivering it. Use bullets and tables only for lists that are genuinely lists.
- Plain words carry hard ideas. Pick the plainest word that holds the meaning. If a technical term is truly needed, explain the plain mechanism first, then name it, and only if the name earns its place.
- Examples that teach. Anchor every abstract claim to a concrete case the reader knows. Let the example carry the idea ("Kevin the AI employee" teaches better than a coined term).
- Nuance without hedging. "This holds when X. It breaks when Y."
- Authority comes from precision, not adjectives. Cut "extremely" and "massive." State the thing exactly.

## The language gate, run before you write (added v3.4, 06 AUG 2026)

**Two files get opened and read in full before the first note of a run is written. Not recalled, opened.**

1. `2_Skills/writing/rtp-humanizer/SKILL.md` — Ravi's version, which supersedes the generic `humanizer` plugin skill. It carries the banned characters, the cut-list and 16 named patterns.
2. The article itself, for its plain lines, per "Borrow the article's language" above.

**Why this is a gate and not advice.** It was advice twice in this file and it still failed. The 06 AUG 2026 session worked from a memorised word list, avoided every banned word, and shipped thirty unreadable batch sections: "bears on", "carries", "arrives", "yields", "worth naming", a superlative per section, and the same three-beat skeleton thirty times. **A word list catches words. The patterns that break a note are shapes.** Only the skill lists the shapes.

**Order matters.** Read the skill first, then read the article's plain lines, then write. Reversing this produces a note that gets cleaned afterwards, and cleaning afterwards is what produced the 06 AUG failure: the surface was scrubbed and the register underneath was still invented.

**Two lines belong in every run's opening report to Ravi:** which two files were opened, and the timestamp. "Ran the humanizer" without that is the exact claim the failed session made all day.

## How not to write (anti-patterns)

The skill preaches clean prose, so it must follow it. These are the tells that mark writing as AI-generated. Strip them from the notes and from anything the notes feed. **Full reference: `2_Skills/writing/rtp-humanizer/SKILL.md`, which is Ravi's own and supersedes the generic `humanizer` plugin skill.** The list below is the floor. The skill is the gate.

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

**The five shapes that survive a word-list pass** (all five shipped on 06 AUG 2026 with zero banned words present):

- **Fake-strong verbs.** "Bears on", "carries", "arrives", "yields", "speaks to". Write "affects", "has", "comes from", "means". If "is" works, use "is".
- **Superlative reaching.** "The sharpest result", "the most consequential correction", "the cleanest specimen". One move repeated until it means nothing. State the finding and stop.
- **Faux-insight setups.** "Worth naming rather than filing quietly", "the part everyone misses", "what this actually shows". Make the claim stand alone.
- **Negative listing and dramatic fragmentation.** "Not flagged, not escalated. Stopped." Say what happened.
- **Robotic rhythm.** Thirty sections built as claim, then "Why this matters", then a falsifier. Identical skeletons read as AI even when every word is clean. Vary the section shape across a batch.

Final pass on every note: ask "what still makes this read like AI?" Name the remaining tells, then cut them.

## Three places every insight goes

Each note's part 9 routes the insight to all three. The application tracker then follows it to a real edit:

1. AI-PM skills: the 65 skills plus CLAUDE.md and the orchestrator, plus any new skill that survives confirmation.
2. Website writing: the specific article in `1_My Series-MD-FILES/`. Refine it in Ravi's voice. Sharpen, do not rewrite.
3. Playbook: the routed section of `AI_Playbook.md`, with numbers tagged by tier.

## Folder layout (corrected 30 JUL 2026 to match the current library structure)

```
3_Research/09_hbr-and-journals/
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

Retired: a `1_hbr-ai-2026/` tree with per-quarter folders and a nested `hbr-synthesis/runs/<month>/` structure. That layout stopped matching reality once the corpus was promoted to a top-level `09_hbr-and-journals/` folder and reshelved by topic; this section now describes what is actually on disk, not what an earlier version of this skill assumed.

### Two trackers, on purpose

- Coverage tracker (each run's `TRACKER.md`, plus `MASTER-TRACKER.md`): what got read and written up. Status moves pending, absorbed, note written, routed.
- Application tracker (`APPLICATION-TRACKER.md`): what actually shipped downstream, that is, each real edit to a skill, a website article, or the playbook, with its source article and a version note. Different question, different lifecycle ("did the insight ship?"). Kept separate so "we read it" is never mistaken for "we shipped it."

## The pipeline, per run

Stage 0, frame the run. Recount the corpus (folders drift, so count again instead of trusting an old listing). Group the articles into clusters of about seven to ten for the readers. Build or refresh `EXISTING-WRITING-INDEX.md`. Write the run's `TRACKER.md` with the month's objective stated plainly and every article as a row.

Stage 1, read and write up (in parallel, by cluster). One reader per cluster reads its PDFs in full and writes one 15-part note each, to the writing and citation bar. Patterns collect in `synthesis/RUNNING-PATTERNS.md` as they show up (three or more articles makes a rule candidate, two makes a hypothesis, one that is strong gets a "watch"). A coverage reader then checks that every tracker row has a note. For a large corpus, run the readers as bounded cluster jobs with a check after each, never one giant run.

Stage 1b, the humanizer pass (required, on the output). Run every note through the `humanizer` skill before it counts as done. The goal is writing that reads like a human analyst's notebook, not AI output. The rigor, the numbers, the citations, and above all the pattern analysis stay exactly as they are. Only the slop goes: em dashes, AI vocabulary, copula avoidance, inflated significance, forced threes. Quality is unchanged. Readability goes up.

Stage 2, synthesize. Lead with the one or two structural insights that reorganize the field. Reconcile contradictions and note which source wins and why. Produce the maps that drive Stage 3: a skills map, a website-refine map, a playbook map. Then write a coverage ledger, one row per article (id, title, one-line thesis, primary routing), as proof that no note was dropped from the synthesis. Read the richest notes in full, not only their compressed summary, so their analysis survives intact. Cross-reference earlier runs for patterns that strengthened, faded, or flipped. Run the synthesis through the humanizer pass too. Ravi reviews before any edit lands.

Stage 3, apply across the three places. This is now a full method of its own: see "The apply loop" below. The one-line version: build an Application Card per note, apply each batch's skill edits as soon as its cards land (apply-as-you-go, never a pile of synthesis waiting for a someday), run the website and playbook as consolidated passes, log every shipped edit in `APPLICATION-TRACKER.md`, and close with the git sync. No edit without a source.

## The apply loop

**Before any of this touches a website article, read the revision standard.** It lives at `2_Skills/writing/rtp-deep-dive-writer/references/article-revision-standard.md` and it governs every revision to an existing article in any series. This skill produces the research; that standard decides whether a finding is allowed into published writing and in what shape.

**The three gates it imposes on this loop, stated so they cannot be skipped:**

- **A finding must complete the chain: evidence, mechanism, product decision, practical action, limitation.** A note that stops at evidence is a news update and does not go into an article.
- **If the signal does not change the job, the architecture, the meter, the proof, the risk, or the trust boundary, it is news.** Interesting is not the bar.
- **One idea, one home.** Before adding a finding to an article, check whether another article in the series already owns it. If it does, link causally rather than restating.

**When cross-linking, take the URL from `1_Projects/1_my-personal-website/WEBSITE-URL-INDEX.md`.** The live pattern is `https://ravitejapalanki.com/writing/{series}/{slug}`. Never build a link from a filename; the file stems and the published slugs are not the same thing, and every URL in the retrieval corpus was wrong for exactly that reason until 30 AUG 2026.

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

Writing (the language gate ran):
- Was `rtp-humanizer` opened and read this session, before the first note was written? Name when. A remembered word list is not the gate.
- Does Part 7 carry a `### Plain lines` block with two or three of the author's plainest sentences, and do Parts 8 and 14 use that register?
- Zero em dashes in running prose. Zero section symbols. None of the AI vocabulary. No copula avoidance, no inflated significance, no forced threes, no inline-header lists where prose works.
- **The five shapes checked by name:** fake-strong verbs, superlative reaching, faux-insight setups, negative listing, robotic rhythm. Checking for banned words does not check for these.
- Length test against the article: is any sentence of mine longer than the article's sentence about the same thing?
- Direction test: where I paraphrased, did the wording get plainer or grander? Grander means rewrite.
- Plain words. Real examples that carry the idea. Sentence-case headings, straight quotes, no decorative emojis.
- Read one paragraph of the note aloud against a paragraph of the article. If the article sounds like a person and the note sounds like a report, rewrite the note.
- Does it read like a sharp human analyst wrote it, with a point of view, or like clean AI filler?

Coverage:
- Is every article in the run read in full, with its tracker row reconciled and nothing skipped?
- Are the trackers updated: coverage rows moved, and any shipped edit logged in the application tracker with its source?

## Updating this skill

After each run, refine the clusters, the note template, and the trackers from what the run taught. Version to `versions/skills/{DDMMMYYYY}/`, bump the version, update `SKILL-REGISTRY.md` and `2_Skills/CHANGE_LOG.md`, and run `skill-sync.sh` across all three locations.
