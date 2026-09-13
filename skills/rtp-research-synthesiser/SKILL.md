---
name: rtp-research-synthesiser
version: v2.3.1_latest
description: 'Synthesize Ravi’s research signals into a clear, sourced digest that explains what changed and what it means. Use for a named intelligence dimension, a full sequential synthesis, emerging-pattern review, or cross-topic connections. The configured inputs are SuperGrok and Perplexity collections in Notion; verify actual access, dated entries, and prior coverage before treating them as current. Process one dimension at a time, continuing through all requested dimensions when a full pass is authorized. Check the underlying sources rather than treating agreement between two AI summaries as verification. Compare prior findings, preserve contradictions and source limits, and propose useful course, skill, interview, or knowledge updates. Includes all ten dimensions, saved page IDs, digest and run-log formats, and output routing. Do not manufacture novelty or automatically promote a pattern from its mention count.'
---
# Research synthesiser

Turn research inputs into an intelligible account of what changed, why it matters, and what Ravi can do with it. Connect findings across time and topics when the evidence supports the connection. A useful synthesis may establish a limitation, contradiction, or absence of meaningful change; it need not manufacture a new theory.

The configured collection pipeline is SuperGrok/Perplexity → n8n and source-metadata extraction → Notion → this synthesis → digest, categorized links, and proposed course/skill/knowledge applications. **These are stored design details, not proof that the services, schedules, integrations or archives are currently running.** Notion holds collected inputs; the underlying publication remains the authority for its claim.

## Choose the scope and establish access

Use Ravi's named dimension when given. For an unspecified synthesis, inspect available coverage and choose the highest-priority unprocessed dimension from current context; ask only if competing priorities would materially change the work. A full synthesis means all ten dimensions **sequentially**, with checkpoints between them. Do not require ten separate user prompts or stop after the first dimension when the full pass is authorized.

The [dimension and source registry](references/dimensions-and-sources.md) preserves all ten dimension mappings and twenty-five saved Notion page IDs. Page names and IDs are discovery aids; confirm the returned page identity and content. Use an available authorized connector or a supplied export. If access is unavailable, state the specific gap and continue with accessible material where useful. Do not claim to have read a remote page or that the corpus is complete.

No model switch, new automation, external message, or archive operation is implied by invoking this skill. Use the current capable model and the user's stated working preferences.

## Read the run state before repeating work

1. Locate the current run log and relevant prior digests. The legacy path is `3_Research/weekly-digests/SYNTHESIS-RUN-LOG.md`; it was absent during the September 13, 2026 wording pass. Check the map and project records before recreating an old structure.
2. Compare actual dated entries and source identifiers with prior coverage. A page's modification timestamp may reflect formatting rather than new research; an unchanged timestamp alone is not a full content comparison.
3. Process new or materially revised entries since the last completed boundary. If no prior log exists, establish the accessible date range and work through the requested backlog in manageable batches. Record missing archived periods.
4. If nothing relevant changed, report that briefly. Reanalysis is still appropriate when Ravi requests it, a new question changes the comparison, or a prior error needs correction.
5. Write the completed run boundary **after** saving and checking the digest. A partial run records the precise completed range, remaining work and output state; it must not mark the whole dimension covered.

Use page IDs, entry dates/IDs, and content fingerprints where available to avoid duplication. Repeated mentions of the same announcement can be one event with several links. Corrected or updated source versions should retain their relationship to the earlier record.

## Load context proportionately

Read the relevant current guidance in `CLAUDE.md`, `5_Knowledge/rules.md`, `5_Knowledge/hypotheses.md`, and `2_Skills/SKILL-REGISTRY.md`. Use the latest three or four relevant digests as a starting point, then search older material when a connection requires it. Standing rules can be challenged by better evidence; they are not scientific facts that new research must confirm.

Use the actual course context—`1_Projects/ai-fluent-course/CONTEXT.md` exists, and a separate `1_Projects/3_AI-Fluent-Course/` project also exists—according to the requested work. The prior `1_Projects/interview-prep/` path is stale; locate current context under `1_Projects/0_interview-prep/`. Do not silently substitute one project's state for another.

For research grounding, follow MAP → relevant folder context → index/graph → source. Read the current Novel Insights guide and relevant original claims, later challenges and scope corrections. Existing summaries help discovery; inspect the underlying evidence for consequential claims.

## Extract and verify the finding

For each relevant input, retain its date, collection page, original source, URL, claim, population/task, metric definition, and evidence status. A high-engagement post is an attention signal; a “production evidence” tag still needs a real deployment and outcome basis.

Compare Grok and Perplexity at the **underlying source level**:

| Collected pattern | What it establishes | Next step |
|---|---|---|
| Both collections mention it | Overlap in collection | Check whether they cite the same source and whether it supports the claim |
| Grok only | A signal found through that collection | Inspect the actual post, author, date, source and context |
| Perplexity only | A signal found through that collection | Inspect the cited research; the summary is not verification |
| Collections disagree | A discrepancy | Check versions, definitions, populations, dates and methods |
| Repeated across runs | Persistence in the feed | Deduplicate events and identify genuinely independent evidence |

Use evidence descriptions such as **primary result checked**, **practitioner report**, **secondary summary only**, **hypothesis**, or **unresolved**. Explain the reason where it changes the decision. Do not rank a source by which AI product collected it or attach a numerical confidence without a defensible basis.

One suitable primary source can establish a bounded claim. Multiple independent studies can support transfer or generalization, but three articles repeating one study do not provide three confirmations. Distinguish primary from audited, observed from forecast, causation from association, and vendor-wide outcomes from Ravi's own experience.

## Compare across time and dimensions

For a consequential finding, ask whether it supports, narrows, contradicts, or adds a different mechanism to an existing rule or hypothesis. Check whether a trend changed direction or whether the population, denominator, measurement, or reporting interval changed instead.

A connection record should include:

```text
Current finding and source/date:
Earlier finding and source/date:
Relationship: supports / extends / narrows / contradicts / unrelated
Deduction beyond either source, if supported:
Scope and alternative explanation:
Evidence that would change the deduction:
Practical or editorial use:
```

Cross-topic checking is part of the method; an original connection is not a required result. If the evidence does not support one, say so. Do not claim that nobody else has made the connection without checking the relevant literature.

Apply relevant tools from Ravi's library—CONTEXT, SHARP, 3X, moat analysis, strategy half-life, inner/outer conditions, PM cultures or thinking algorithms—using their **current definitions and source attribution**. Some are Ravi's synthesis and some derive from named practitioners. Do not label every framework proprietary or repeat obsolete algorithm counts or universal numerical half-lives.

## Write plainly without copying the source wholesale

Use `rtp-thinking-writing`. Learn from a source's clear explanation: identify its subject, concrete verb and mechanism, then explain the finding faithfully in your own words. Keep a technical term when it is the clearest term. A direct quotation can be useful when short, exact, attributed and within applicable quotation limits.

The August 6, 2026 lesson was a digest whose inflated language obscured fifteen edited articles. Its practical correction remains: favor “stop” over unnecessary “terminate,” and “is” over vague “serves as.” But a source is not always better written, a longer sentence is not necessarily worse, and paraphrasing does not always drift toward grandeur.

Check four things: **length serves the meaning; verbs describe actual action; wording preserves scope and causal strength; the paragraph sounds natural when read back.** Keep a useful sentence's mechanism without copying two or three sentences from every source or mechanically adopting an author's interpretation.

## Produce the digest and route the work

Use [the digest and reporting formats](references/digest-and-routing.md). Lead with the most consequential finding, then evidence, change from earlier understanding, limits, and a practical implication. A quiet period needs a short report, not empty template sections.

Preserve a categorized URL list with meaningful labels. “Must-read” can contain fewer than three sources; a top-five summary can contain fewer than five meaningful signals. Distinguish sources actually read from links collected for later review.

A thought-leadership seed is optional and should identify the proposed argument, evidence, competing explanation and best medium. An interview application is a sourced example or analytical perspective unless Ravi's records establish personal involvement.

Route **proposals and completed changes differently**. The digest can propose a course update, skill revision, prompt improvement or hypothesis. A registry version changes only after the skill is actually revised and synchronized. Do not mark a course, Notion page or knowledge rule updated because a proposal was written.

For authorized skill changes, follow exact-source backup → revision → version increase → validation/synchronization → registry/change log. Preserve the frontmatter structure and each description's 1,000-character limit. For shared rule changes, check current authority and preserve the supporting evidence and counterexamples.

**Pattern promotion is not automatic at three mentions.** `09_hbr-and-journals/_synthesis-engine/OPEN-ASSUMPTIONS.md`, O25, currently records that the promotion bar needs Ravi's judgment. Keep candidates and recommendations explicit; do not silently resolve that governance question by promoting a research hypothesis. A declared “promoted” state records an actual governance action, not scientific proof.

## Finish the requested scope

For a named dimension, save the digest and update its completed run boundary. For a full cycle, continue through all ten dimensions unless a required input blocks a specific dimension; complete independent ones and report the gap. The older priority order started with dimension 3, then 2, then the rest because interview work was urgent. Use that order only when the current priorities still support it.

After the requested dimensions are complete, produce a roll-up with top signals, connections, optional editorial seeds, links, interview/course implications, actual versus proposed skill/knowledge changes, and prompt refinements where useful. Label a partial roll-up with its coverage rather than calling it the completed weekly synthesis.

Historical cadence was daily Grok collection, weekly Saturday Perplexity collection and on-demand synthesis, often Sunday. The old footer's “Sunday 9 PM automated” claim conflicted with that design. Check the actual scheduler when asked about automation; this file does not create, enable or prove a scheduled run.

The earlier lifecycle expected about a month of raw Notion data followed by Ravi's Google Drive archive. Verify the actual retention and archive access before claiming coverage. Saved digests and knowledge files support later retrieval; they do not guarantee automatic host loading, permanent availability, or model memory.

Editorial revision: September 13, 2026. All ten dimensions, saved page identifiers, output families and temporal-comparison methods remain; evidence rules, scope, routing and historical configuration limits are now explicit.
