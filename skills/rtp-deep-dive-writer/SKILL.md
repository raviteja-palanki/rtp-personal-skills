---
name: rtp-deep-dive-writer
version: v1.1.1_latest
description: 'Write or revise Ravi''s substantial practitioner articles on AI products, evaluation, context, agents, and related technical subjects. Help a senior product manager understand a mechanism, make a better decision, and use a practical artifact. Preserve Ravi''s curious, candid voice, useful existing material, verified evidence, and connections across his series. Use rtp-thinking-writing for the shared writing standard; this skill adds research, article structure, series navigation, two-visual guidance, and a focused revision process. Read the article-revision reference before revising an existing article and the series-publishing reference for website-bound work. Keep examples, source findings, interpretation, and recommendations distinct. Preserve the current project''s publishing contract and report incomplete checks honestly.'
---

# Ravi's Deep Dive Writer

Write so the reader understands the idea, can examine the evidence, and knows how to apply it. Ravi's voice is a practitioner learning through teaching: curious, concrete, candid about uncertainty, and willing to take a defensible position.

Use `rtp-thinking-writing` for the shared reasoning and voice standard. This skill adds the depth and publishing requirements of researched articles. Apply the user's requested scope: a correction needs a careful correction; a full rewrite needs a full preservation and structure review.

Before revising an existing article, read [Article revision standard](references/article-revision-standard.md). For a series article, also read [Series publishing](references/series-publishing.md). These references distinguish editorial preferences from requirements needed by the site's renderer.

## 1. Establish the article and the decision

Read the complete article and its relevant topic specification before claiming a complete revision. Identify the reader, the decision or concept, the main argument, the strongest existing material, and gaps that affect understanding. Locate the active series map and tracker; old status tables and archived maps are historical context.

Keep a short preservation record for a substantial revision: what stays, moves, combines, changes for accuracy, or is deliberately removed. Retain strong source-backed openings, useful analogies, definitions, framework functions, worked examples, exercises, and memorable takeaways. Preserve good wording when it remains accurate. A familiar sentence does not become exempt from correction.

The original skill mentions Ravi's Honeywell role and his 2025 Perplexity AI Fellowship. Use the current supplied profile when a bio is needed; do not assume an old title is current. Never invent a customer encounter, personal experience, responsibility, or endorsement to make the voice more convincing.

Consider four planning questions before drafting. Brief working notes are enough; no fixed time allocation or private reasoning transcript is required.

1. **Tension:** What is difficult to understand or decide? Which belief should the reader reconsider, and why?
2. **Audience:** What should the reader remember, use, or explain to a colleague? Which artifact would help?
3. **Voice:** Are the stakes recognizable, the images concrete, the verbs active, the words familiar, the terms explained, and the rhythm natural?
4. **Connections:** What insight does this article owe the reader before referring them elsewhere?

## 2. Research the claims that carry the argument

Use relevant material in `3_Research`, the topic map, and any supplied research. For a substantive update, reread the relevant Novel Insights entries with their later qualifications. Treat a ledger connection as a hypothesis or synthesis until its sources support the intended claim. Repeated mentions of the same study are not independent corroboration.

Verify changing product details, research, prices, regulations, and incidents against current primary sources. Keep strong foundational work when it remains relevant. Read methods and counterevidence for consequential claims. A source opening successfully does not establish that it supports the sentence.

Connect **evidence, mechanism, decision, action, and limitation** when adding practitioner guidance. If the mechanism is uncertain, describe plausible explanations rather than inventing a cause. A wording repair, corrected date, or clearer definition can be valuable without introducing a new decision or research story.

Keep four layers clear in prose:

- What the source observed or reported.
- How you interpret the result.
- What you recommend for this reader.
- Where the evidence stops or the advice may change.

Use real cases within their documented scope. Signal constructed or composite examples near their introduction, for example, "Consider an illustrative support workflow." Mark assumed numbers. Naming a real company does not make a scenario factual. An unavailable source may remain an explicitly attributed, limited report when useful; do not imply direct verification.

### For articles with many sources or numbers

1. Put the central insight early. A short scene, arresting fact, direct explanation, or decision can open the piece. Choose the form that makes the point clear fastest.
2. Give each section a distinct job. Combine repetition while retaining qualifications that change the conclusion.
3. Use tables or charts when they make comparisons easier. Explain what to notice and why it matters. A paragraph with several numbers is a cue to review the form, not an automatic chart requirement.
4. Label evidence accurately: audited within a documented audit scope, study-disclosed, company-disclosed, reported, or disputed. A filing can contain unaudited metrics. A revenue run-rate is not realized annual revenue. Keep units, periods, populations, and denominators consistent.
5. Reconcile sources by comparing what they actually measured. Explain a defensible synthesis; preserve unresolved disagreement when the evidence does not settle it. A requested source-by-source summary is also a valid output.
6. Put citations close to the claims they support and collect necessary method notes unobtrusively. Seek independent corroboration where consequences warrant it; two reports repeating one announcement remain one evidence source.
7. Correct an established article or playbook when stronger evidence warrants it. Record the correction and check connected articles; consistency must not preserve an error.
8. Close with a useful consequence or action. Do not force a calendar slogan, a dramatic revelation, or a new numerical claim into the ending.
9. For web delivery, provide concise authoring notes for the hero visual, rendering, and pull quotes. Use the project's supported author-only location and check that these notes do not appear as reader-facing instructions.

## 3. Teach through a clear sequence

The following is the default deep-dive template. Preserve required site fields and established section contracts. Adapt section length and, where the project permits, headings or order to the lesson. One-off articles need not inherit a website's navigation metadata.

| Part | What the reader receives |
|---|---|
| Title and opening promise | A specific subject and usually three or four things they will understand or do |
| The story | A brief documented case or clearly labeled scenario that establishes the stakes; a few paragraphs usually suffice |
| The core idea | A plain definition, a helpful analogy, its limits, and the concept visual at the point of need |
| Where this hits in production | Concrete patterns, their consequences, and the conditions that distinguish them; three is a useful starting shape |
| Connecting the dots | An original, defensible connection that changes how the reader sees or uses the concept |
| The trap | The bias or mistaken belief, the behavior it causes, the consequence, and a workable correction |
| Remember this | Usually three complete, memorable claims that retain necessary conditions |
| In practice | A usable table, trace, dashboard, scoring rubric, checklist, exercise, or decision template; place the practice visual here |
| Up next | When a next article exists, explain the question it answers and why it follows; include the verified cross-reference |
| Authoring material and references | Two SVG briefs, verified citations, and the required Builds on / Leads to navigation, in their supported locations |

### Make the language inviting and precise

Use the clarity and concrete stakes Ravi values in advertising without turning every paragraph into persuasion. Emotion should follow the situation; technical explanations can be calm. Keep useful abstract concepts and explain them through examples rather than replacing every abstract noun mechanically.

Use familiar words, active verbs, and named actors where they help. Introduce necessary jargon on first use in each standalone article, including terms such as inference, tokens, latency, embeddings, retrieval, JSON, MCP, P95, or a named regulation when the intended reader may not know them. A short definition should support the lesson rather than interrupt every sentence. Preserve technically necessary distinctions.

Vary sentence length with the thought. Read for natural speech rhythm; a silent review is valid and should be described honestly. Remove empty claims of importance, stacked hedges, filler, generic conclusions, sales language, and chatbot greetings. Use `rtp-humanizer` to diagnose specific patterns. Its guidance concerns writing habits, not a list of words that must disappear from quotations or all legitimate uses.

Length follows the lesson and the user's requested format. Compress repetition and routine definitions; expand mechanisms, worked examples, and consequences that need explanation. Do not impose a word minimum, a fixed percentage cut, or deliberate messiness to simulate a human voice.

### Make Connecting the dots earn its place

This signature section should explain a connection the reader can assess. Consider:

- **Autonomy:** How does the importance of the concept change with the system's actual permissions and ability to act?
- **Advantage:** Which resource or operating habit could compound, under what conditions, and who else could reproduce it?
- **Cross-domain reasoning:** Which idea from product strategy, safety, evaluation, economics, or system design explains the mechanism?
- **Practice:** What constraint or failure would an implementation reveal that a definition alone misses?

A compact 150–300 words often works, but completeness determines length. State the argument and its limits here. A cross-reference supplies depth; it cannot substitute for the insight. Do not claim that every article reveals a moat or a causal relationship.

## 4. Preserve the series and visual contracts

For website series, retain the bracketed cross-reference format:

```text
[<Post Title> (<Series Name> <Post ID>)]
```

Resolve the actual title, series, ID, and destination from the active project. Do not construct a live URL from a filename. The current website URL index is `1_Projects/1_my-personal-website/WEBSITE-URL-INDEX.md`; verify that the intended destination still matches. The [series publishing reference](references/series-publishing.md) contains the spine schema, navigation rules, visual briefs, framework vocabulary, and project locations.

Maintain two visual roles for the standard series: a **concept visual** that makes the central idea easier to remember and a **practice visual** that explains a mechanism, contrast, or usable artifact. For a prose-only revision, keep existing SVG assets and provide redesign notes. Create or edit the assets when that is within the requested scope, using `rtp-excalidraw-svg` and the current series design system.

Visual copy should use short, self-explanatory labels. State the intended quick-scan message, main visual element, exact display text, and improvement needed. A practice table can be appropriate when it makes the decision clearer. Do not force data into a decorative diagram. Check label accuracy, reading order, and whether the visual teaches the intended point.

## 5. Revise with nine focused checks

After reading the full original and applying the revision standard, use these checks. Combine passes for a small correction; repeat only those affected by new edits or unresolved issues.

1. **Opening:** Does the opening establish the point or stakes honestly? Keep a strong illustrative opener when a real case would be weaker or poorly evidenced.
2. **Thesis:** Can the main idea be expressed clearly in one sentence without hiding a material condition?
3. **Practice:** Can the reader use the artifact with the inputs provided? Are criteria, assumptions, and ownership clear where needed?
4. **Connections:** Does each idea have a natural primary home? Retain enough explanation for this article to stand alone.
5. **Navigation:** Check exact references, spine relationships, destinations, and the current publishing schema.
6. **Language:** Remove the specific habits that weaken clarity; preserve voice, useful nuance, and exact source wording.
7. **Length:** Cut repetition and unnecessary structure. Restore missing reasoning instead of chasing a reduction target.
8. **Memorability:** Does one sentence or visual communicate a useful, defensible insight when seen alone?
9. **Ending:** Does the article complete its promise and, where appropriate, connect naturally to the next question?

For substantial rewrites, also score truth, usefulness, clarity, distinctiveness, and durability using the reference rubric. Scores are editorial judgments with reasons, not measured guarantees of reader response. Fix factual defects regardless of the average score.

Four practical checks preserve the original Screenshot, Monday morning, Standalone, and Naval aspirations:

- A memorable sentence or visual is accurate outside its immediate paragraph.
- The reader can apply the practice artifact to a real decision.
- A newcomer has the explanation and definitions needed to follow the argument.
- The ending is clear, specific, and worth remembering.

Do not invent endorsement from Naval Ravikant, an executive, or a colleague. Reader testing can help when authorized and available; the skill does not authorize sending anyone a message. Mark a self-review as a self-review.

## 6. Save and report the actual result

Save the revision to the established project folder and filename, with a recoverable earlier version. Update the active tracker, affected links, and required article metadata. Report what changed, where the file is, which checks were completed, and any material uncertainty or unfinished asset work. Editing an article does not by itself authorize publishing it.

Use companion skills when they improve the article: `rtp-autonomy-spectrum` and `rtp-ai-use-case-readiness` for capability and permissions; `rtp-moat-finder` and `rtp-safety-as-moat` for competitive claims; `rtp-eval-framework` for evaluation; `rtp-strategy-canvas` for strategic choices; `rtp-trust-ladder` for appropriate reliance; `rtp-excalidraw-svg` for visuals; and `rtp-thinking-writing`, `rtp-thinking-skills`, and `rtp-humanizer` for reasoning and expression. Verify the installed name when source and plugin names differ.

**Revision 1.1.1, 13 Sep 2026.** Preserves the original teaching template, four planning areas, nine revision checks, research standard, two-visual workflow, series navigation, and practitioner voice. Reconciles conflicting version labels and replaces mechanical style rules with clear, evidence-aware editorial checks.
