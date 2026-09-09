---
name: rtp-humanizer
version: v2.1_latest
description: 'Secondary verification pass for named AI-slop patterns. `rtp-thinking-writing` is the default gate and runs first; open this when a specific line needs a named pattern to convict it, or when auditing a draft someone else wrote. Two modes: edit (minimum effective change) and detect (name each pattern with the offending line, no rewrite). Carries the banned-character rules (no section symbol, no decorative emoji, em dashes in structural slots only, straight quotes), the cut-list, and 16 named patterns including fake-strong verbs, superlative reaching, faux-insight setups, negative listing and robotic rhythm, which a banned-word scan does not catch. Use when Ravi says humanizer, slop check, does this read as AI, or when a draft is clean at word level and still reads processed. Pairs with rtp-thinking-writing (the default gate), rtp-trendslop-check (numbers), rtp-deep-dive-writer (long-form).'
---
# rtp-humanizer

**The objective:** make every line read as though a sharp human wrote it on purpose, without sanding away the things that make it Ravi's.

## Where this skill sits, as of 10 SEP 2026

**`rtp-thinking-writing` is the default gate. This skill is secondary verification.**

The reason is a real failure, and it is the one a word list cannot catch. A session in Aug 2026 memorised the banned words, avoided every one of them for a full day, and still shipped prose Ravi could not read. The words were clean. The thinking underneath had no join, no position, and no reversal condition. **A slop dictionary audits the surface of a sentence. It has nothing to say about whether the sentence was worth writing.**

So the order is fixed:

1. **`rtp-thinking-writing`, read from disk, before the first sentence.** It governs the whole job: understand the source, decide what the reader must do, build the causal path, write in Ravi's spoken language, prove nothing was lost.
2. **This skill, second, when it earns its place.** A line reads wrong and you need the named pattern to convict it. A draft arrived from somewhere else and needs an audit. A detect pass is requested by name.

Reaching for this skill first produces the failure it was written to prevent: a clean draft that says nothing. The patterns below are still the sharpest named list in the system, and that is exactly what a second pass should be.

This still runs on **everything** it is invoked for, not just long prose. A CONTEXT.md written in slop is worse than one written plainly, because an agent will trust it and inherit the register.

Adapted from the `no-ai-slop` skill (Sam Rowe, MIT licence) with Ravi's own banned characters and evidence-discipline rules folded in.

## Three jobs

**Edit (default).** A draft arrives to fix. Make the minimum effective edit and return the edited draft plus a short **What changed** section.

**Detect.** The user asks whether something reads as AI, or asks for an audit without a rewrite. Name each pattern below that appears, quote the line, give the fix in a few words. Do not rewrite, do not score the draft, do not guess whether AI wrote it. **Detectors guess; named patterns are evidence the reader can check.** Offer to edit afterwards.

**Structure (v2.0).** The draft is clean and still does not read like business writing. Apply **How to structure it** below: headings that carry the argument, an Assumptions section, format that matches the content, and the interview-answer discipline on length. Cutting slop was never sufficient; a formless clean draft still loses a senior reader. **As of v2.1 the fuller version of this job lives in `rtp-thinking-writing`**, which owns the argument, the coverage ledger and the evidence discipline. Use this mode when that skill has already run and the structure still reads flat.

## The banned characters (absolute, no exceptions)

These are Ravi's, and they override any source style guide.

- **`§` the section symbol is banned outright.** It is slop. Write "section 11" or name the section: "the value question." Never "§11."
- **No decorative emoji.** Not in headings, not as bullets, not as tone softeners. Evidence-tier glyphs (✅ ◆ ⚠) are notation, not decoration, and are allowed where the tier discipline requires them.
- **Em dashes in structural slots only:** a heading label, a definition label, a quote attribution, a tier or flag tag. **Zero in running prose.** Use a comma, a period, a colon, or parentheses.
- **Straight quotes, not curly**, wherever a tool will render them literally.
- **Sentence case in headings.** Not Title Case, not ALL CAPS for emphasis.

## Editing principles

- **Preserve the writer's real voice first.** Before changing anything, notice the draft's vocabulary, cadence, bluntness, humour, uncertainty, and digressions. Keep what feels personal. Do not make every paragraph equally tidy.
- **Minimum effective edit.** Fix slop, errors, repetition, and genuinely unclear passages. Leave strong human sentences alone. A rough draft with a real voice should still sound like the same person afterwards.
- **Open it up, do not dumb it down.** Keep the substance, the nuance, the precision. Strip only what makes it hard to read: jargon, tangled structure, abstract nouns, sentences that lost their way.
- **Be concrete.** Abstraction is where writing dies. "The integration improved efficiency" becomes "The integration cut deploy time from 40 minutes to 4." Names, numbers, dates, mechanisms.
- **Protect the specific fact.** Never smooth a useful detail into generic importance. A figure with its population intact beats a rounded figure that reads better.
- **Active voice; make verbs work.** "Made a decision" becomes "decided." "Has the ability to" becomes "can." Never let an inanimate thing perform a human verb.
- **Keep useful edge.** Strong opinions, blunt language, humour, self-interruption, honest admission. Do not replace them with safer wording. Ravi's writing is supposed to have a point of view.
- **Vary the rhythm.** Clean is not enough. Voiceless writing reads as AI too. Vary sentence length, let one honest aside through, state an opinion somewhere.

## Words to cut

**Banned outright:** delve, foster, leverage (as a verb), utilize, facilitate, empower, streamline, robust, cutting-edge, paradigm shift, game changer, this changes everything, tapestry, realm, beacon, multifaceted, meticulous, intricate, paramount, transformative, elevate, embark, supercharge, harness, ever-evolving, underscore, showcase, testament, seamless, landscape (as a metaphor), pivotal, crucial, vital, additionally, garner, enhance.

**Often-empty adverbs:** just, literally, honestly, simply, actually, truly, fundamentally, importantly, crucially, inherently, inevitably. Cut when they add nothing; keep when they carry real emphasis, uncertainty, or Ravi's spoken rhythm.

**Banned because it is a house tic, not English:** "Monday move", "Monday morning", "what to do on Monday". Measured 01 SEP 2026: it appears in 3 of 221 real 2026 HBR and MIT Sloan articles, and in 259 files across this system. Write the heading that says what the section is: "Where to start", "First 30 days", "What to do differently", or a named action. If a piece needs to tell the reader what to do, name the action, not the weekday.

**Often-empty phrases:** it's worth noting, it's important to note, at the end of the day, when it comes to, at its core, in today's world, in the age of, the reality is, the truth is, in terms of, with regard to, in order to (use "to"), going forward, in this article, let's dive in, due to the fact that (use "because").

## Patterns to cut

**Binary contrasts.** "This is not X, it's Y." / "The question isn't X, it's Y." State Y directly.

**Throat-clearing openers.** "Here's the thing," "Let me be clear," "I'll be honest," "The uncomfortable truth is." Cut and state the point.

**Faux-insight setups.** "What most people get wrong," "Here's what nobody tells you," "The part everyone misses." These flatter the writer as lone expert. Make the claim stand alone.

**Colon reveals.** A noun phrase, a colon, a lowercase dramatic reveal. "The detail that makes it work: a separate agent grades it." Rewrite as a plain sentence. Colons are for lists, labels, and quotes, not drama.

**Superficial analysis.** Trailing `-ing` clauses pretending to explain: "highlighting," "underscoring," "reflecting," "showcasing." Cut or replace with a real point.

**Importance puffery.** "Marks a pivotal moment," "stands as a testament," "plays a vital role." State the fact; let the reader judge.

**Weasel attribution.** "Experts agree," "studies show," "industry reports suggest." Name the source and date, or cut the claim. Never invent one. This is also an evidence-discipline failure, not only a style one.

**Fake-strong verbs.** "Serves as," "stands as," "boasts," "features." Use "is" and "has."

**Synonym cycling.** Repeat the clearest word rather than rotating thesaurus entries.

**Negative listing.** "Not a X. Not a Y. A Z." Say Z.

**Dramatic fragmentation.** "X. And Y. And Z." / "That's it. That's the whole thing."

**Robotic rhythm.** Repeated sentence shapes, identical paragraph lengths, stacked punchy fragments.

**Rhetorical setups.** "What if I told you," "Think about it:", "Plot twist:", self-answered question-answer pairs.

**Fake-profound kickers.** The final "deep" line that turns a point into an aphorism. Delete it. Do not rewrite it into a better metaphor. End on the clearest concrete sentence already in the draft.

**Summary-recap endings.** "In conclusion," "Ultimately," "Overall," or a last paragraph restating the piece. The reader was just there. End on the last concrete point or the next action.

**Formatting slop.** Emoji in headings, bold sprinkled mid-sentence, bullets where two sentences of prose read better, headers over two-sentence sections. Format follows content; it does not decorate it.

**Forced rule of three.** Use the number of items the idea actually has.

## How to structure it

This half of the skill is the one that was missing. Cutting slop makes prose
clean. It does not make it read like business writing, and a clean draft with a
formless middle still loses a senior reader.

The reference set is 221 HBR and MIT Sloan articles from 2026, read on 01 SEP
2026. What follows is their grammar, not an invented style.

### Headings carry the argument

A heading is a claim, a question the reader is already asking, or a named thing.
It is never a label. "Overview", "Introduction", "Key considerations",
"Deep dive" and "Thoughts" tell a reader nothing and are the tell of a deck
built from a template.

Five heading shapes, all lifted from the reference set:

| Shape | Real examples | Use when |
|---|---|---|
| The reader's own question | "Is your tech foundation solid?" · "How will you govern your efforts?" · "Narrow or wide?" | The section resolves a decision they are stuck on |
| A named construct with its count | "The Four Modes of AI Collaboration" · "The Five Centers" · "Six Steps for AI-Supported Decision-Making" | You are introducing a framework worth remembering |
| The claim itself | "What Really Drives Data Transformation" · "What Sets Superteams Apart" · "Why This Matters" | The section has one finding and you want it read |
| The imperative | "Consider redesigning workflows" · "Shift assessment from answers to process" | The reader has to change something |
| The comparison | "Before and After Caterpillar's Data Transformation" | Two states, and the delta is the point |

Sentence case for prose headings. Title case only where the heading names a
formal construct.

### The high-signal section names

Use these words in headings when the section genuinely is that thing. They carry
more signal than any phrasing you could invent, because a business reader already
knows what each one promises.

- **Problem statement** — what is actually broken, stated without the solution in it
- **Value** — what it is worth, in the unit the reader is measured on
- **Hypothesis** — the claim you are testing, written so it could be wrong
- **Solution approach** — the mechanism, not the roadmap
- **Risks** — what breaks, with likelihood or impact where you have it
- **Assumptions** — see the rule below, this one is mandatory
- **Trade-off** — what you are giving up, named
- **Evidence** — figures with tier and population
- **Where it breaks** — the honest limit
- **Takeaways for {audience}** — when two audiences need different actions

Never stack all of them. Three or four earn their place in a normal piece.

### Assumptions get their own section. Always.

If the argument rests on anything unverified, it goes under its own
**Assumptions** heading, near the end, as a list. Not a parenthesis, not a hedge
folded into a sentence, not a footnote.

Two reasons, and the second is the one that matters. An assumption buried in
prose is invisible to a reader scanning for what to attack. And an assumption
you were willing to write down is one you can revisit when it turns out to be
wrong, which is the only way an argument improves.

Write each as a testable statement plus what would settle it:

> **Assumptions**
> - Usage is log-normal rather than flat. Settles by pulling P50, P90 and P99 cost per user from last quarter.
> - The 30% figure came from a controlled comparison, not a survey. Settles by asking for the method.

### Format follows content

Prose is the default. Reach for structure only where the content already has that
shape, and never to decorate.

- **A table** when there are two or more dimensions to compare. Options against criteria, before against after, tiers against evidence. If the table has one column, it was a list.
- **Bullets** for genuinely parallel items. Sub-bullets only for a real hierarchy, never for a second thought.
- **A quote** when the source's own words are more precise than a paraphrase, or when who said it is part of the evidence. Attribute it inline.
- **A comparison pair** when the reader is choosing. State both sides fairly, then say which and why.
- **A number** in a table, a story in prose. Do not narrate a table.

Vary it. Four sections with identical shape reads as machine-written even when
every word is clean, and the reference set almost never repeats a shape twice in
a row.

### Tight beats complete

The test is an interview answer, not a briefing document. A senior person asks
you something and you have ninety seconds. You lead with the answer, give the
mechanism, name the trade-off, and stop. You do not warm up, you do not cover
what they did not ask, and you do not summarise at the end.

Length follows the question. A definition is a paragraph. A decision is three.
If it runs past a page, the extra material is either a second piece or it is
padding.

### Think integratively, and from first principles

Clean prose with a borrowed argument is still a borrowed argument. Two habits
separate writing worth a senior reader's time from writing that merely reads well.

**Integrative.** The value is in the join, not the inventory. Three findings
listed is a summary. Two findings connected by a mechanism nobody stated is a
contribution. Before you write, ask what these sources say together that none of
them says alone, and lead with that.

**First principles.** Strip the framing before you answer. Most questions arrive
carrying an assumption that is doing the real work, and the useful answer often
rejects the premise. "Why did our AI pilot not move the P&L" is usually not a
question about AI.

## Be authentic, and never oversell

This is the half that protects everything else. Prose can pass every rule above
and still be untrustworthy.

### Never claim what you have not done

Write from what you have read and reasoned, and say so. The line is simple: a
claim the reader cannot check is a claim you should not make.

| Do not write | Write instead |
|---|---|
| "In my experience..." | "Across these three cases..." |
| "I have seen this a hundred times" | "This shows up in the Klarna and Salesforce reversals" |
| "Teams I have worked with..." | "The pattern in the corpus is..." |
| "As an expert, I would say" | Say it. The reasoning is the credential |
| "Trust me on this" | Give the mechanism and let them check it |

Ravi's own writing is allowed to draw on his actual work at Honeywell and
Perplexity. Anything written on his behalf is not, unless the source material
states it.

### Never overhype

No superlatives you cannot defend. Not "the most important shift", "a
fundamental rethink", "the single biggest lever", unless you can name the
comparison that makes it true. State the finding and let the reader judge its
size. A reader who feels sold to stops reading, and a senior one stops trusting.

The tell: if removing the adjective leaves the sentence just as informative, the
adjective was doing sales work.

### Be factually right, and show the receipts

- Every figure carries its **population** and its **tier**: audited, disclosed, or reported. Tiers never blend.
- A number you cannot source is either softened to a qualitative claim or cut. There is no third option.
- Never invent a source **type**. "According to earnings materials" when you do not know that is a fabrication, and it is worse than a wrong number because the provenance is what tells a reader to stop checking.
- Where the evidence is thin, say it is thin. That sentence buys more credibility than the paragraph it qualifies.

### Sources go at the end, where they can be checked

When the piece rests on data, close with a short **Sources** list. Not inline
footnote clutter, not a wall of links mid-argument. Each line names the article,
the author where it matters, and the date, so a reader can go and disagree with
you.

> **Sources**
> - HBR, "Managers Are Struggling to Keep Up with the AI Productivity Boom", May 2026
> - MIT SMR, "When Not to Use AI", Jun 2026

Naming the article is the citation. A description of the article is not, and it
makes the claim unauditable.

## Workflow

1. Read the whole draft before touching it.
2. Identify the core point and three to five voice signals to preserve. Keep this note internal. If the core point is unclear, ask.
3. For a detect request, return the findings and stop.
4. For an edit, make the minimum effective changes, then run the quality gate below.
5. Fix and re-run until it passes.
6. Return the edited draft plus **What changed**.

## Quality gate

- [ ] Zero `§`. Zero decorative emoji. Em dashes only in structural slots, none in running prose.
- [ ] No word from the banned list survives.
- [ ] Every number carries its population and, where the corpus requires it, its evidence tier.
- [ ] No weasel attribution. Every claim has a named source or is softened honestly.
- [ ] Paragraph lengths vary. At least one sentence carries a real opinion.
- [ ] **The read-aloud test.** Read a paragraph out loud. A stumble, a lost breath, or a sentence you would never say to a colleague means rewrite.
- [ ] The last line is a concrete fact or a move, not a flourish.
- [ ] **Every heading is a claim, a question, or a named thing.** Zero label headings ("Overview", "Key considerations", "Thoughts").
- [ ] **Every unverified thing the argument rests on is under its own Assumptions heading**, as a testable statement with what would settle it.
- [ ] Structure matches the content: tables where there are dimensions, bullets where items are parallel, prose everywhere else. No decoration.
- [ ] Section shapes vary. Nothing repeats the same skeleton twice in a row.
- [ ] Zero "Monday move" or "Monday morning". Name the action instead.
- [ ] **The piece makes a join, not a list.** If it only summarises sources, it has not earned a senior reader.
- [ ] **Zero claimed experience the author does not have.** No "in my experience" written on someone else's behalf.
- [ ] **Zero undefendable superlatives.** Remove each adjective and check the sentence still says the same thing.
- [ ] Every figure carries population and tier. Nothing is sourced to a type of document you did not verify.
- [ ] **Sources listed at the end** where the piece rests on data, each naming article, author and date.
- [ ] Ask directly: "what still makes this read like AI?" Name the remaining tells, then cut them.

## When wrong

- **Do not run this on quoted source material.** A verbatim quote keeps its author's slop; that is what makes it a quote.
- **Do not flatten a deliberate register.** A cinematic deck and a governance file have different voices, both legitimate.
- **Do not strip hedging that reflects genuine uncertainty.** "We think" is honest when the evidence is thin. False confidence is a worse failure than a hedge.

## Attribution

Pattern list adapted from `no-ai-slop` by Sam Rowe (MIT licence), extended with Ravi's banned-character rules, the evidence-discipline overlaps from `CLAUDE.md`, and the read-aloud gate.
