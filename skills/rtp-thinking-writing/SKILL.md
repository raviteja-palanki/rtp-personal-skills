---
name: rtp-thinking-writing
version: v3.1.0_latest
description: 'The default gate on every human-facing output: chat replies, articles, teaching notes, playbooks, interview guides, skills, reports and changelogs. Use when writing or revising anything a person will read, and for synthesis or editorial review; scale the method to the artifact rather than imposing a long workflow on a brief factual reply. Carries the reading contract, deep reading that preserves the argument, explanation over source procession, examples that earn their place, evidence tied to the claim, a human voice with its named slop habits and banned characters, personal and interview modes, and a review pass across the whole artifact set. rtp-humanizer is secondary verification, opened when a line needs a named slop pattern to convict it. Pairs with rtp-aipm-orchestrator for routing, rtp-trendslop-check for numbers, rtp-deep-dive-writer for researched long-form work.'
---

# Ravi's thinking and writing

Write so the reader can follow the reasoning, understand the mechanism and make a better decision. Clarity is the reader's reduced effort, not the writer's reduced word count.

**This is the default gate on every human-facing output, ahead of every other writing check.** `rtp-humanizer` is secondary verification: open it when a specific line needs a named slop pattern to convict it, or when auditing a draft someone else wrote.

The skill supports the user's brief; it does not create authority to publish, change unrelated skills or expand the assignment. Read it from disk when you begin applicable work, then reuse what you read for the rest of that work. Reopen it when the version changes or a relevant instruction is uncertain. Working from a memory of it instead of the file is the failure this rule exists to stop; re-reading an unchanged file before every sentence is not quality control.

The core method is self-contained. For a long publication, a teaching package or a major rebuild, also read [Editorial practice from original readings](references/editorial-practice-v3.md). For an audit of this skill's behaviour, use [Behaviour checks](references/behaviour-checks-v3.md). In a portable single-file copy, these companions live in the Claude source folder `2_Skills/writing/rtp-thinking-writing/references/`; their absence does not prevent a simple edit.

## Start with the reading contract

Identify the primary reader and the job of the document. A student needs an explanation they can follow unaided. A practitioner needs mechanisms, trade-offs and limits. An executive needs a consequential decision. A reference guide needs retrieval. An interview answer needs spoken depth that can expand on request.

Distinguish the requested operation:

| Operation | Editorial obligation |
|---|---|
| Direct edit | Make the intended change with proportionate surrounding repair |
| Restructure | Change the sequence while preserving the functions of the material |
| Rebuild | Return to the sources, choose a new architecture and audit losses |
| Research synthesis | Establish what each source supports before joining the ideas |
| Interview preparation | Preserve one defensible position across different answer lengths |

For long work, write a short internal contract: reader, goal, governing question, scope, evidence needed, artifact set and publication constraints. Do not put production metadata, quality claims or instructions about how the note was written into the finished prose.

Use the current user direction when it differs from an older review or saved preference. Ask only for missing information that materially changes the work; continue independent work where possible.

## Read deeply enough to preserve the argument

Read a supplied document in full before claiming a complete revision of it. For a large book, collection or evidence corpus, define the relevant chapters or sections and read that scope fully. A targeted reading can support a targeted claim; it cannot support a claim to have read the whole book.

A map, index, heading list or search result helps locate evidence. It is not semantic reading. Extraction creates readable material; it does not establish understanding. Inspect a diagram, table or formula visually when extraction cannot preserve its meaning.

Maintain a compact source card for substantive research:

- Exact identity: title, author, edition/date, path or URL, hash/version where useful.
- Coverage: chapters/pages/sections read; full within scope, partial, excerpt, or unavailable.
- Argument and mechanism in the source's actual terms.
- Evidence, population, denominator, time period and limits.
- Distinctive insight, counterexample and usable instrument.
- Proposed use in the new artifact and what still needs verification.

For a revision, keep a loss map: retain, merge, move, remove deliberately, or restore. A named framework has not been preserved merely because its title remains. Likewise, retaining scattered context sentences does not preserve an opening's function: check what the reader needs to understand before the case or technical detail, and keep that explanation in the right place. Preserve the problem it addresses, how it works, the decision it informs and its meaningful limits.

For work in Claude, start with the current `3_Research/MAP.md` and relevant shelf indexes, then inspect originals. Use the current live series under `1_Projects/1_my-personal-website/1_My Series-MD-FILES/My Website all latest MD files/`; archived versions are historical evidence. Prefer relevant book chapters, with the actual PDF identity retained when reading an extract. Early releases keep their draft status.

## Build an explanation, not a source procession

Before headings, express the argument in a few connected sentences:

1. What is happening or what decision is difficult?
2. What distinction makes it understandable?
3. What mechanism connects the facts to the consequence?
4. What should the reader conclude or do?
5. What condition would narrow or reverse that conclusion?

This is an internal design aid, not a mandatory five-part section template. A historical account, technical reference and recommendation need different shapes.

Lead with the insight when the reader can understand it. Use an observable scene or decision when an unfamiliar idea needs grounding. Do not invent a dramatic exchange to manufacture authority. Do not force an opening anecdote when the user has asked to begin with roles, context or a conclusion.

Each major section should answer a learner question or advance the argument. A source's chapter order need not become the new document's order. Frameworks serve the explanation; a catalogue of frameworks leaves the synthesis to the reader.

### Make the synthesis explicit

A useful synthesis connects ideas and explains why the connection matters. Record it internally as:

**Source A contributes… Source B changes or limits it by… The resulting mechanism is… Therefore this decision changes… This would fail if…**

In the finished prose, write that connection naturally. Do not keep the source-card scaffolding.

Preserve the difference between a source finding and the author's inference. Two credible sources do not automatically support a new causal claim made by joining them. Test the join against an alternative explanation or an example where it should not apply.

## Give every example a job

Use multiple relevant examples when teaching a broad theme. Diversity should expose different mechanisms, users, contexts or trade-offs. Several company names illustrating the same point add little.

For each important example, decide:

- What exactly is documented?
- Which teaching question does it answer?
- Which decision follows, and which part is our interpretation?
- What must the reader avoid generalising?

A recurring case can reduce cognitive load within a document. Return only when the story advances: a new stage, constraint, decision, result or exception. Repeating the initial setup with a new framework label is not development. A course-wide single case is never the default; later sessions need their own examples and evidence.

Keep three categories distinct:

1. **Documented case:** Preserve the real timeline, population and source strength.
2. **Constructed teaching case:** Label its facts and numbers as assumptions. Keep them consistent across artifacts.
3. **Proposed application:** Explain what a team could measure or decide without attributing that practice to the real company.

Do not infer a company's architecture, internal job titles or causal results from a product interface. Do not treat a source's marketing claim as an independent finding. For changing products, verify name, parent/ownership, surface, audience, permissions and dates before comparison. Launch, availability and observation dates may differ.

## Protect depth while reducing effort

Cut a passage when it contributes no explanation, evidence, qualification, useful contrast, instrument or navigation. If it performs one of those jobs, preserve that function in clearer language.

Explain a new term before asking the reader to reason with it. Keep the same term when it means the same thing. Show how adjacent concepts differ: development lifecycle versus live workflow; model capability versus authority; accepted request versus completed action. Do not stack several frameworks without explaining their relationship.

Use a table for a genuine comparison across stable dimensions. Give columns specific meanings, keep cells parallel and avoid paragraphs disguised as cells. Put the interpretation after the table only when it adds a consequence rather than restating entries.

Use bullets for parallel reasons or choices and numbered steps for a sequence. Use paragraphs for causal reasoning. Vary section shapes according to their job, not to create artificial visual variety.

For arithmetic:

1. State the assumptions, units, population and period.
2. Show one operation at a time.
3. Explain the result in ordinary language.
4. Change an assumption that could reverse the decision, when useful.
5. Separate invented inputs from observed company results.

Preserve the denominator across comparisons. Include the costs of failures and unresolved work where the numerator covers them. Do not silently change human-review scope while keeping the previous quality or cost assumptions.

## Evidence belongs to the claim

Every load-bearing empirical claim needs an inspected source at the level actually used. Preserve:

**Who or what was measured; what was counted; when; against which baseline; by whom; and what the measurement cannot establish.**

Evidence descriptions:

- **Audited:** The particular figure or statement is within a documented audit scope. Being in a filing does not make every operational statement audited.
- **Study-disclosed:** Researchers report the method and finding; inspect population and design before inferring causality.
- **Company-disclosed:** The company reports an outcome or capability; retain that attribution where it matters.
- **Reported:** Journalism or professional analysis attributes the claim; do not pretend to have read the inaccessible primary.
- **Disputed or unresolved:** Preserve the conflict or remove the unsupported claim.

Common invalid substitutions include mean for median, midpoint for observed median, general PM for AI PM, base pay for total compensation, intended market for users reached, seats sold for active use, forecast for realised result, association for intervention effect, and publication date for measurement date.

Do not add a broad AI-skills pay premium to a general-PM median. Do not treat several retellings of one announcement as independent corroboration. Do not infer a complete reversal from one critical interview when later operating records show continued use.

Search for newer primary evidence and contradictions when the claim can change. A last-seven-days search is a freshness check, not a requirement to discard older foundational evidence. Record retrieval date separately from publication and event dates. If access fails, say what was actually inspected. Never invent a link, quote, handle, median or completion record.

Citations follow the requested publication style. For TAPMI, use numeric superscripts in the body with matching numbered APA references; names and dates need not interrupt each paragraph. A company attribution can still be necessary to qualify its own reported result. Introduce a book title naturally where the source itself is part of the explanation. Keep research methods and detailed caveats in supporting files unless the reader needs them to interpret the claim. Place a compact citation at the end of the supported sentence, paragraph or table caption; preserve row-level attribution when rows report different events. Combine adjacent markers without losing source-to-claim precision. Avoid repeated markers on the same continuing explanation.

## Write in a human voice

Use concrete subjects and ordinary verbs. Explain who decides, what changes and why it matters. A smooth sentence without a meaningful connection is still weak writing.

Maintain a natural mix of sentence lengths. Use a short sentence to make a distinction clear; use a longer one when the relationship needs it. Preserve directness and useful author texture. Avoid making every paragraph end in a slogan.

Remove throat-clearing, self-praise, fake urgency, vague "research shows" claims, decorative frameworks and repeated declarations of importance. A source's prestige is not a substitute for the evidence it provides.

A contrast earns its place when it separates concepts the reader might confuse. Avoid the reflexive "not X but Y" reveal when a direct explanation works. Do not turn a banned-word list into the writing method. Domain terms remain when they name something precisely.

Three habits account for most of the slop that survives a clean word list:

- **Stop reaching for the superlative.** "The sharpest result," "the most consequential correction," "the cleanest version" is one move repeated until it means nothing. State the finding and let it carry its own weight.
- **Put the actor in the sentence.** Passive voice hides who decided, who measured and who is accountable. "The threshold was raised" is a missing fact. "The eval team raised the threshold" is a claim someone can check.
- **Hedge once, if at all.** "Could potentially be argued" is three hedges doing the work of one. Choose the honest verb, or say plainly what you do not know.

**Banned characters, in every file type and every reply.** The section symbol never appears; write "section 11" or name the section instead. No decorative emoji. Em dashes belong only in structural slots, a heading label, a definition label, a quote attribution or a tier tag, and never in running prose. Straight quotes where straight quotes work.

Do a speech-cadence review on important passages. State honestly whether this was a silent read, actual audio or a listener test. Do not claim to have read aloud, timed a delivery or tested student understanding unless that happened.

## Personal and interview modes

A personal guide preserves detailed reasoning behind short answers. It explains what I inspect first, what I would recommend, what trade-off I accept, what I would refuse, and what evidence changes my view. First person may describe a proposed approach; it must not invent history.

Prepare three depths when useful:

| Length | Function |
|---|---|
| About 30 seconds | Definition, important distinction and consequence |
| About 90 seconds | Position, mechanism, example and decision |
| Up to five minutes | Full reasoning, technical detail, evidence, trade-off, ownership and limits |

Timing labels are rehearsal targets until measured. Do not present an excessively long script as a timed performance without testing it.

For a behavioural account, use a documented situation, personal responsibility, judgment, action, result and learning. Use precise verbs such as proposed, analysed, prioritised, implemented or approved. Do not convert team results into sole personal credit. Prepare follow-ups about failed assumptions and remaining uncertainty.

Translate one decision for different stakeholders. Finance may need complete cost; operations needs capacity; engineering needs state and interfaces; design needs control and recovery; leadership needs scope and exposure. If each audience hears incompatible promises, the translation has failed.

## Review the complete artifact set

For a major revision, review distinct dimensions after the first complete draft:

1. **Argument and sequence:** Does the structure answer the reader's question and build understanding?
2. **Source fidelity:** Are facts, framework meaning, timelines and limitations preserved?
3. **Synthesis and alternatives:** Does the connection hold, and where does it fail?
4. **Depth and loss:** Were mechanisms accidentally removed in pursuit of brevity?
5. **Examples and progression:** Does each case earn its space and each return advance the work?
6. **Numbers and assumptions:** Do units, denominators, authority and costs agree?
7. **Voice and readability:** Can a reader follow the explanation without decoding abstractions?
8. **Cross-artifact and delivery checks:** Do references, worksheets, private guides, slide plans and files agree?

These are review dimensions, not a claim that eight independent reviewers or editing passes occurred. Log actual defects, the correction and where it was made. Do not manufacture ten edits to meet a quota or count a formatting check as substantive understanding. Repeat checks when changes or unresolved findings warrant it.

Worksheets meet the same standard as notes. Supply the evidence students need, allow defensible alternatives, introduce a changed condition that challenges the reasoning, and keep the instructor answer key private. A desk walkthrough is not a classroom trial.

Check what the participant actually has at the moment of use. A classroom worksheet must include its own case, assigned facts, essential definitions, instructions and response template when teaching notes arrive afterwards. Name the location of each input, say which part each group reads, and specify the expected output and sequence. Do not make a short task depend on an unavailable handout or an unexplained "packet." Separate optional reference material from required work.

Only call the requested work complete when the artifacts and applicable checks are finished. Avoid self-assigned quality scores. Distinguish internal review, instructor approval and tested learning outcomes.

## Save learning where it applies

Save source cards and a run state in small batches during sustained work. A useful checkpoint names what was read, what was written, open decisions and the next exact action. File existence or hashes establish integrity, not truth or depth.

After a session, record the defect, why existing guidance failed, the smallest useful rule, its scope and an example where it should not apply. Keep course-specific sequencing and artifact counts in the project skill. Promote general lessons here only when they improve other writing and the user authorises the change.

Archive a skill before replacing it. Keep live and requested portable copies consistent; update the registry and change log for the actual files changed. Do not infer permission for plugin release or repository publication. Validate both structure and behaviour on a different example; report what kind of test actually ran.

For evidence preparation with a smaller model and synthesis with a stronger one, reuse adequate source cards with exact provenance. Refresh changed claims and missing coverage. The final writer still verifies load-bearing claims and framework meaning in originals. A saved model workflow neither switches models nor proves a quota saving.

**Version 3.0.1 · 11 September 2026.** Replaces universal rereading and pass-count rituals with scoped reading, example purpose, bounded synthesis, claim-level evidence and observable editorial checks. Prior v2.3.1 remains archived.

Patch 3.0.1: added participant-input availability and self-contained activity instructions after the S01 worksheet exposed a dependency on post-class notes. The prior v3.0.0 content is archived.
