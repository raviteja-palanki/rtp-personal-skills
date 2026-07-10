---
name: rtp-hbr-research
description: Monthly research-synthesis engine for Harvard Business Review, MIT Sloan, and other top management research. Reads every PDF in full to a senior-practitioner bar, writes one citation-disciplined note per article (each number tagged by how solid it is, real-company claims backed by primary links, written in plain HBR-grade prose), finds new patterns by joining ideas across articles, checks every insight against what Ravi has already written, and routes each finding to three places: the AI-PM skills, Ravi's website writing, and the playbook. Runs monthly (June to December 2026 and onward). Use whenever Ravi adds new research to 3_Research/1_hbr-ai-2026/, says "HBR research", "research synthesis", "process the articles", "run the monthly cycle", or asks what earlier research said.
---
# HBR research synthesis engine v2.3

## What this does

It turns top management research into insight Ravi can act on, across three places where his work lives: the AI-PM skills (65 skills plus CLAUDE.md and the orchestrator), his own website writing (the four series in `MAY2026-MD-FILES/`), and the playbook (`2_Playbook_AI/AI_Playbook.md`).

This is not a summarizer. It reads the way a top AI product manager reads: to understand each idea well enough to teach it, to find new patterns by joining ideas across articles, and to write notes so clearly that an editor would not change a word. It runs once a month. Each run's notes and patterns stay on disk, and the next run builds on them.

> v2.3 (29 JUN 2026): hardened the army that runs the work, from a live failure. The June Q2 run fanned out all 66 articles at once (about 73 agents, 880k tokens in 5 minutes) and tripped the account's rolling session limit mid-flight, losing the whole window's reviews. Three fixes, now in `_army-deep-synthesis.js`: bounded batching (each run takes a deliberate slice and stops clean, the rest resume from disk), a citation gate in the reviewer (a striking named-company number with no primary link and no [VERIFY] tag fails review), and a comprehensive synthesis that reads the richest notes in full and writes a coverage ledger of all articles so nothing is silently dropped. The trigger was a near-miss: three deeply-analysed POC notes sat outside the run set and would have been excluded from the final synthesis. See "Running the army" below.
> v2.2 (27 JUN 2026): made the skill self-driving. Added exact input and output paths, a "read the trackers first" startup step, the humanizer pass as a required output step, an HBR-editor verification checklist, and put hidden-pattern analysis up front as the main job. v2.1: rewrote the skill to its own bar (no em dashes, plain words, dropped "canon," added the anti-patterns section). v2.0: the 13-part note, the writing standard, evidence tiers and the real-company citation rule, three-place routing, the two-tracker setup.

## The main job: hidden-pattern analysis

The reason this engine exists is part 8 of each note, and the running patterns file it feeds. Anyone can summarize an article. The value here is the pattern no single source states: the contradiction between two studies that resolves into a rule, the connection that turns two facts into one insight, the line from an HBR finding to something Ravi already wrote that neither saw on its own. Summary is table stakes. Pattern-finding is the product. If a run produces clean notes but no new patterns, it has failed at its main job. This is what makes the output worth a senior analyst's time, and it is the part the humanizer pass must never flatten.

## Where everything is (paths, relative to ~/Desktop/Claude)

Inputs, the PDFs to read:
- `3_Research/1_hbr-ai-2026/Q1_2026/`
- `3_Research/1_hbr-ai-2026/Q2 2026/`
- any later drop folder, for example `3_Research/1_hbr-ai-2026/Q3_2026/`

Engine home and working files:
- home: `3_Research/1_hbr-ai-2026/hbr-synthesis/`
- what Ravi has already written: `hbr-synthesis/EXISTING-WRITING-INDEX.md`
- year at a glance: `hbr-synthesis/MASTER-TRACKER.md`
- shipped-edits ledger: `hbr-synthesis/APPLICATION-TRACKER.md`
- this month's run: `hbr-synthesis/runs/2026-06-june/` (holds `TRACKER.md`, `dossiers-q2/`, `dossiers-q1/`, `synthesis/RUNNING-PATTERNS.md`)

Outputs, the three places insights ship to:
1. Skills: edit the source at `2_Skills/ai-pm-skills/<cluster>/<skill>/SKILL.md`, then sync to `.claude/skills/<skill>/SKILL.md` and `rtp-personal-skills-repo/skills/rtp-<skill>/SKILL.md`. Run `./scripts/skill-sync.sh` to confirm all three match.
2. Website writing: edit the article at `1_Projects/1_my-personal-website/MAY2026-MD-FILES/<NN-series>/<article>.md`.
3. Playbook: edit the section in `1_Projects/2_Playbook_AI/AI_Playbook.md`.

## Start every run by reading the trackers

Before opening a single PDF, read the state, so you pick the right inputs and write to the right place:
1. `MASTER-TRACKER.md`: which month is this, and what is its objective.
2. the run's `TRACKER.md`: which articles are already written up, and which are still pending. Read only the pending ones.
3. `APPLICATION-TRACKER.md`: which insights already shipped, so you do not propose them twice.
4. `EXISTING-WRITING-INDEX.md`: what Ravi has already written, so "new" is judged against fact.

Then inputs are the pending articles, and outputs are the routed targets named in each note's part 9. Update the trackers as you go, not at the end. A run that does not read the trackers first will re-read finished work and miss pending work.

## When to use it

- Ravi adds new PDFs to `3_Research/1_hbr-ai-2026/` (a new quarter, say). Run the monthly cycle.
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
2. Website writing: the specific article in `MAY2026-MD-FILES/`. Refine it in Ravi's voice. Sharpen, do not rewrite.
3. Playbook: the routed section of `AI_Playbook.md`, with numbers tagged by tier.

## Folder layout (moved June 2026, so synthesis sits with its source PDFs)

```
3_Research/1_hbr-ai-2026/
  Q1_2026/                    source PDFs
  Q2 2026/                    source PDFs
  synthesis_Q1_2026/          April output (kept as a cross-check only, not trusted)
  hbr-synthesis/              the engine home
    README.md                 what this is, plus the monthly cadence
    EXISTING-WRITING-INDEX.md  what Ravi has already written (shared across runs)
    MASTER-TRACKER.md         the year at a glance, one objective per month
    APPLICATION-TRACKER.md    the separate "what we picked, what shipped" ledger
    00-METHOD.md              the note bar (points to this skill)
    runs/
      2026-06-june/           TRACKER.md, dossiers-q2/, dossiers-q1/, synthesis/
      2026-07-july/ ... 2026-12-december/
```

### Two trackers, on purpose

- Coverage tracker (each run's `TRACKER.md`, plus `MASTER-TRACKER.md`): what got read and written up. Status moves pending, absorbed, note written, routed.
- Application tracker (`APPLICATION-TRACKER.md`): what actually shipped downstream, that is, each real edit to a skill, a website article, or the playbook, with its source article and a version note. Different question, different lifecycle ("did the insight ship?"). Kept separate so "we read it" is never mistaken for "we shipped it."

## The pipeline, per run

Stage 0, frame the run. Recount the corpus (folders drift, so count again instead of trusting an old listing). Group the articles into clusters of about seven to ten for the readers. Build or refresh `EXISTING-WRITING-INDEX.md`. Write the run's `TRACKER.md` with the month's objective stated plainly and every article as a row.

Stage 1, read and write up (in parallel, by cluster). One reader per cluster reads its PDFs in full and writes one 13-part note each, to the writing and citation bar. Patterns collect in `synthesis/RUNNING-PATTERNS.md` as they show up (three or more articles makes a rule candidate, two makes a hypothesis, one that is strong gets a "watch"). A coverage reader then checks that every tracker row has a note. For a large corpus, run the readers as bounded cluster jobs with a check after each, never one giant run.

Stage 1b, the humanizer pass (required, on the output). Run every note through the `humanizer` skill before it counts as done. The goal is writing that reads like a human analyst's notebook, not AI output. The rigor, the numbers, the citations, and above all the pattern analysis stay exactly as they are. Only the slop goes: em dashes, AI vocabulary, copula avoidance, inflated significance, forced threes. Quality is unchanged. Readability goes up.

Stage 2, synthesize. Lead with the one or two structural insights that reorganize the field. Reconcile contradictions and note which source wins and why. Produce the maps that drive Stage 3: a skills map, a website-refine map, a playbook map. Then write a coverage ledger, one row per article (id, title, one-line thesis, primary routing), as proof that no note was dropped from the synthesis. Read the richest notes in full, not only their compressed summary, so their analysis survives intact. Cross-reference earlier runs for patterns that strengthened, faded, or flipped. Run the synthesis through the humanizer pass too. Ravi reviews before any edit lands.

Stage 3, apply across the three places (small, clustered, one pass at a time). Version, edit, update the registry and changelog, and for skills sync all three locations. Each cluster is its own small job with a check at the end. Log every shipped edit in `APPLICATION-TRACKER.md`. No edit without a source.

## Running the army (orchestration, learned the hard way)

The readers and reviewers run as a resumable army, one script: `hbr-synthesis/_army-deep-synthesis.js`, launched with the Workflow tool. Four rules keep it honest, each from a real failure:

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
