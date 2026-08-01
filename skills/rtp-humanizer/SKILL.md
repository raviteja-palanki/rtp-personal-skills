---
name: rtp-humanizer
version: v1.0_latest
description: 'Strip AI-slop patterns from any written output while preserving the writer''s actual voice. Runs as a mandatory final pass on everything Ravi ships: articles, skills, CONTEXT.md files, changelog entries, commit messages, emails, synthesis notes, the session TL;DR. Two modes: edit (fix the draft, minimum effective change) and detect (name each pattern with the offending line, no rewrite). Carries the banned-character rules (no section symbol, no decorative emoji, em dashes in structural slots only), the cut-list of AI vocabulary and empty phrases, and 16 named slop patterns with a rewrite for each. Use on every output before it ships, not only when asked. Pairs with rtp-thinking-skills (runs alongside on every deliverable), rtp-deep-dive-writer, rtp-hbr-research.'
---
# rtp-humanizer

**The objective:** make every line read as though a sharp human wrote it on purpose, without sanding away the things that make it Ravi's.

This runs on **everything**, not just long prose. A CONTEXT.md written in slop is worse than one written plainly, because an agent will trust it and inherit the register. `CLAUDE.md` names this as a mandatory pass, and this skill is what that pass executes.

Adapted from the `no-ai-slop` skill (Sam Rowe, MIT licence) with Ravi's own banned characters and evidence-discipline rules folded in.

## Two jobs

**Edit (default).** A draft arrives to fix. Make the minimum effective edit and return the edited draft plus a short **What changed** section.

**Detect.** The user asks whether something reads as AI, or asks for an audit without a rewrite. Name each pattern below that appears, quote the line, give the fix in a few words. Do not rewrite, do not score the draft, do not guess whether AI wrote it. **Detectors guess; named patterns are evidence the reader can check.** Offer to edit afterwards.

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
- [ ] Ask directly: "what still makes this read like AI?" Name the remaining tells, then cut them.

## When wrong

- **Do not run this on quoted source material.** A verbatim quote keeps its author's slop; that is what makes it a quote.
- **Do not flatten a deliberate register.** A cinematic deck and a governance file have different voices, both legitimate.
- **Do not strip hedging that reflects genuine uncertainty.** "We think" is honest when the evidence is thin. False confidence is a worse failure than a hedge.

## Attribution

Pattern list adapted from `no-ai-slop` by Sam Rowe (MIT licence), extended with Ravi's banned-character rules, the evidence-discipline overlaps from `CLAUDE.md`, and the read-aloud gate.
