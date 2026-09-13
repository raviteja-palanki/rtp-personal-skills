---
name: ai-product-taste
version: v1.3.1_latest
description: 'Define what excellent AI output means for a specific user, task, domain, and price point. Use when strong benchmark scores do not translate into useful work, when a team cannot explain its quality bar, or when deciding whether to ship or improve a feature. Establish essential requirements, meaningful user outcomes, tolerable imperfections, and examples that evaluators can judge consistently. Examine acceptance by segment, the first useful experience, prompt framing, and whether users select among many outputs or depend on one finished artifact. Turn the result into a taste spec for eval-framework and eval-driven-development. Pairs with jtbd-analysis, confidence-tuner, prompt-craft, ai-product-metrics, and fit-signal.'
imports:
  - first-principles
  - dual-lens
---

# AI Product Taste

Use this skill to define the quality a particular AI feature must deliver and decide whether the current experience meets it. The result is a **taste spec**: observable standards, examples, failure boundaries, and evidence for a ship, improve, narrow, or test decision.

Product taste is informed judgment about what works for these users in this situation. A technically correct answer can still be unhelpful, poorly timed, hard to act on, or wrong for the audience. Those shortcomings can be investigated and measured; they do not require choosing between taste and evidence.

## Establish the task and essential requirements first

Name the user, job, domain, decision the output supports, current alternative, and price or service tier. Use existing context. Ask only for missing information that would materially change the quality bar. If the job itself is unclear, use `rtp-jtbd-analysis` before polishing an answer to it.

Separate three parts of the bar:

1. **Essential requirements:** correctness where required, safety, privacy, accessibility, valid permissions, and any obligations for the intended use. A lower price does not waive these requirements.
2. **Useful performance:** whether the output helps the user complete the job, with acceptable effort, timeliness, and recovery when it fails.
3. **Distinction:** the voice, insight, precision, or experience that makes this product preferable to a credible alternative.

Keep severity separate from frequency. A rare failure may still block release. Identify both false positives and false negatives in the actual task; neither is automatically the more costly error.

Apply the shared `UNIVERSAL-SKILL-PROTOCOL.md` where available: it lives at the AI-PM collection root in the source library and at the repository root in the plugin. Scale its grounding and handoff to the task. This skill does not require a separate workshop, document, or diagram for a simple quality judgment.

## Four distinctions that keep the bar honest

| Distinction | What to check |
|---|---|
| Accuracy and usefulness | A correct answer may omit the next step, bury the answer, or address the wrong question. Evaluate factual accuracy and task usefulness separately. |
| Fluency and trustworthiness | Smooth prose can conceal weak evidence. Check sources, uncertainty, and what the user can safely infer. |
| Speed and value | Speed matters when it improves the task. Measure useful completion, including verification and rework, rather than generation speed alone. |
| Comprehensiveness and signal | Include what changes the user's understanding or action. Offer depth when the task needs it; do not treat either brevity or length as inherently better. |

Benchmark scores can inform the assessment. They become misleading when their tasks, users, or failure costs differ from the product's own. A domain-specific rubric should complement relevant technical measures.

## Build the bar in five steps

### 1. Calibrate to the domain

Study how users accomplish the job today: specialist software, a human expert, a manual process, or another AI product. Observe real work and ask domain practitioners to compare concrete outputs. Their expertise matters, but investigate disagreements instead of treating one expert's preference as universal.

Describe excellence in terms someone can judge. “Accurate and helpful” is too broad. “Quotes the correct policy version, identifies the applicable exception, and gives the next action without inventing approval authority” is testable.

List the errors that matter, their consequences, who can detect them, and whether recovery is possible before harm occurs. Distinguish a preference from a requirement and record whose needs each represents.

### 2. Identify the first meaningful value

The **magic moment** is an experience that makes the product's value clear. It may be a useful surprise, a previously missed pattern, a completed task, or an ordinary step removed reliably. It need not produce a “wow.” Speed can be the value when timeliness is part of the job.

Examples: a coding assistant proposes a better pattern and demonstrates that it works; an analysis tool reveals a relevant driver with traceable evidence; a support tool resolves the issue without making the user repeat their story.

Specify what happened, what changed for the user, and how you would recognize it. Treat the proposed moment as a hypothesis until users experience that value. Express uncertainty honestly; do not invent a “60% confidence” label to make an answer sound calibrated. Use `rtp-confidence-tuner` for signals with a defensible interpretation.

### 3. Match the offer to the price

Determine what each tier promises and what it costs to deliver that promise. A free tier may offer fewer tasks, lower volume, slower service, or less customization. A premium tier may justify deeper analysis, specialist review, integrations, or stronger service commitments. The same consequential use still needs its essential requirements met at every tier.

The earlier free / $20 / $500 examples are illustrative positions, not universal quality thresholds. A $500 product is not automatically expert-equivalent, and a free product is not entitled to be misleading. If the required quality is unaffordable, narrow the supported job, change the service design, or reconsider the offer.

Include inference, retrieval, verification, human review, support, and rework in the relevant cost boundary. Avoid optimizing compute while shifting larger costs onto users.

### 4. Develop judgment through observation and comparison

Use the product for a real task. Watch new and experienced users, including people whose needs differ from those of the builders. Examine accepted, edited, regenerated, abandoned, and manually completed work. Ask why the user made that choice.

Test concrete alternatives in style, length, structure, uncertainty signals, and interaction. Preserve correctness and other essential requirements in every variant. Where practical, use comparable tasks, blinded assessment, and an appropriate sample. Report uncertainty and differences by segment rather than announcing a winner from a few preferences.

Acceptance is evidence of a choice, not proof of quality: people may accept a wrong answer, edit a good answer to fit house style, or reject it because integration is awkward. Pair behavior with outcome quality and the user's explanation.

### 5. Make the judgment reusable

Write the taste spec with examples of excellent, acceptable, and unacceptable output. Annotate why each example belongs in that category. Include common work, difficult cases, and severe failures even when rare. Five to ten corner cases can start a discussion; coverage depends on the task, not that count.

Turn the spec into an evaluation rubric with `rtp-eval-framework` and into release checks with `rtp-eval-driven-development`. Clarify how disagreement between evaluators is resolved. Keep some cases separate for checking whether an improvement generalizes. Update the bar when evidence warrants it, with a recorded reason and version, so learning is distinguishable from moving a target after seeing results.

## Domain examples: choose the specific use before choosing the bar

These examples illustrate judgment, not clinical, legal, or release standards.

| Domain | Useful qualities | Failure to investigate or block | Potentially tolerable imperfection |
|---|---|---|---|
| Legal research | Verifiable citations, correct jurisdiction and date, clear distinction between evidence and interpretation | Fabricated authority, omitted material limitations, or unsupported advice | An explanation longer than preferred, if it remains usable; the bar depends on research assistance versus a consequential legal decision |
| Healthcare | Evidence appropriate to the supported task, clear limits, and a suitable qualified review path | An error or omission that could materially affect care; rarity alone does not make a missed condition acceptable | Nonmaterial wording or administrative formatting, after confirming it does not alter clinical meaning |
| Creative writing | Suitable voice, originality, emotional effect, and fit to the brief | A generic result may miss the creative goal; deceptive, infringing, or harmful content raises different concerns | An awkward phrase that can be edited without undermining the work |
| Code assistance | Correct behavior, maintainable implementation, clear tradeoffs, and relevant security checks | A security flaw or incorrect behavior despite successful compilation | A minor style difference consistent with the project's constraints |
| Customer support | Correct resolution, empathy, appropriate escalation, and low user effort | Wrong policy, an unauthorized promise, or failure to escalate when needed | Slightly formal wording when it does not obstruct the interaction |
| Data analysis | Correct calculations, suitable data, traceable assumptions, and decision relevance | Confidently wrong numbers or a missing source that changes the conclusion | Omission of an immaterial source, with coverage and limits made clear |

“Fatal failure” in a taste spec means a failure that blocks this use or breaks a stated essential requirement. Do not use the term interchangeably for a security defect, a disappointing writing style, and a clinical hazard.

## Three additional lenses

### Prompt framing: express the desired quality, then test it

The language used to describe quality can influence the result. Anthropic's harness report describes particular visual convergence from a “museum quality” framing; it does not establish a universal quality improvement. Specific domain criteria and examples give evaluators more to work with than status words such as “expert-level.” [Anthropic's report](https://www.anthropic.com/engineering/harness-design-long-running-apps).

Use `rtp-prompt-craft` to develop prompt variants. Compare their outputs against the same bar, including factual and other essential requirements. An impressive-sounding instruction can change style without improving the job. The earlier +8% and +15% acceptance lifts were hypothetical examples; they are not expected effects or planning assumptions.

### Recall: investigate what users remember as valuable

After an interval suitable for the product, ask a user to describe the experience in their own words. A week is one possible interval. First collect unaided recall, then ask what changed in their work. Follow-ups require the normal authorization and scheduling mechanism; this instruction does not itself send a message or schedule one.

Separate descriptions of the presentation—speed, animation, volume of output—from descriptions of an outcome: a mistake caught, a task completed, an argument resolved. Both may be valuable. Entertainment can legitimately deliver spectacle, and routine automation may succeed by becoming unremarkable. If the job removes a step, ask about that absence without treating a blank memory as failure.

Treat recall as a diagnostic alongside actual outcomes, usage, and interviews. It does not establish that every user initially remembers spectacle, that only meaningful benefits survive a week, or that spectacle-only recall proves bad design. This is the library's unvalidated adaptation of an experience-design framework; see [research boundaries](references/research-boundaries.md).

The Novel Insights ledger's pattern X adds a useful question: **what does this AI experience replace, and for whom?** Compare an additional option with the removal of a valued existing service. The Duolingo Lily discussion records one co-author's preference for practicing with a chatbot because mistakes felt less embarrassing. It challenges the claim that an available human alternative necessarily reduces acceptance. It does not isolate provider displacement as the cause. Test availability, price, privacy, confidence, perceived loss, and outcome quality as competing explanations.

### Concentrate innovation while retaining a beginner's view

The **Proven–Better–New** heuristic asks you to name the dimension where novelty matters most and use suitable established patterns elsewhere. For example, a new analysis method may benefit from familiar navigation and onboarding. Adopt interaction principles responsibly and adapt them to the actual users; “use a proven pattern” does not mean copying proprietary assets or ignoring accessibility.

One focused bet can protect scarce design and engineering time. Some products require several connected innovations, so make those dependencies explicit instead of imposing a one-bet rule. Mark Pincus's account of social games harmed by neglected onboarding is an illustrative retrospective, not a controlled causal finding.

Keep a **first-time-user perspective**. Builders' familiarity can hide confusing prompts, labels, and steps. Observe newcomers at an appropriate cadence; there is no established one-quarter deadline for losing this perspective. A completed interaction can still produce an unusable answer. Investigate what the interface failed to elicit or explain rather than labeling the user or their prompt as the problem.

## Portfolio selection and depth of a finished artifact

Ask how the work is judged:

- **Portfolio selection:** users generate several candidates and select or test the best. Assess candidate diversity, useful yield, selection accuracy, and total cost. More draws can help, but correlated outputs and a weak judge can leave quality unchanged or select an appealing error.
- **Depth of the finished artifact:** a particular report, essay, investigation, or argument must stand on its own. Assess coherence, distinctive insight, evidence, and accountability for the complete artifact. It can still benefit from multiple drafts, research assistance, or critique.

Many workflows combine both. Do not infer that AI necessarily improves portfolios or inevitably homogenizes a single artifact. Test whether it improves the required quality in this workflow. The distinction from the Atlantic/OpenAI podcast discussion is a useful design lens; undisclosed deal terms and broad causal claims are outside what that source establishes.

## Diagnose a gap before prescribing polish

| Signal | Questions to investigate |
|---|---|
| “Good, but I would not pay” | Is the job important enough? Is value clear? Are alternatives, budget, purchasing friction, or the offer responsible? |
| High accuracy, low acceptance | Is the output relevant, usable, well integrated, and trusted for good reasons? Does the accuracy measure represent the user's task? |
| A specialist competitor wins | Which user need or quality dimension does it satisfy better? Compare actual work rather than reputation alone. |
| Flat NPS or churn | Which cohorts and alternatives changed? Is this a quality gap, acquisition mismatch, pricing issue, or something else? |
| The lowest-acceptance segment struggles | Inspect its tasks, constraints, and outcomes. Low acceptance identifies a question, not proof that the product's taste is worst there. |

Mature practice means the team can explain the bar, demonstrate outcomes, interpret disagreement, and maintain representative evaluation examples. There is no universal 80% acceptance threshold, required trust-curve shape, or NPS level that proves good taste.

When evidence supports a quality gap, inspect rejected and manual work, revise the relevant part of the bar, improve the output or experience, and retest. Style may be the problem; accuracy, missing functionality, or task selection may be the problem instead.

## Deliver the taste spec and hand it forward

Use a compact answer for a single judgment or this structure for a reusable spec:

```text
Taste Spec: [product / feature / version]
User, domain, job, and current alternative:
Decision: ship / improve / narrow scope / test further; evidence and limits
Essential requirements and release-blocking failures:
Useful outcome and proposed magic moment:
Quality dimensions, annotated examples, and acceptable imperfections:
Error asymmetry: false positives, false negatives, severity, and recovery
Work structure: candidate selection, finished-artifact depth, or both
Offer: tier | price | promised scope/service | cost boundary
Corner cases: case | required behavior | evidence | unresolved gap
Framing test: variants | sample | quality/outcome measures | uncertainty
Segment evidence: acceptance/editing | outcomes | reasons | remaining gaps
Evaluation handoff: rubric, cases, evaluator, version, next check
Next action, owner, and decision that the next evidence will change:
```

`rtp-first-principles` clarifies the job and assumptions; `rtp-dual-lens` translates the quality bar between business and engineering. Reuse that grounding when it already exists. `rtp-confidence-tuner` designs uncertainty signals, and `rtp-prompt-craft` implements the quality instruction. `rtp-ai-product-metrics` examines behavioral and outcome measures; `rtp-fit-signal` follows appropriate cohorts over time. Those measurements test the taste hypothesis rather than automatically confirming it.

Before handing off, check that the bar is domain-specific, essential requirements are explicit, failures reflect their consequences, pricing supports the promise, and examples can be judged consistently. Name the main tradeoff and what evidence would change the recommendation. A richer rubric costs more to maintain than one generic score, so use the detail the decision warrants.

If a visual would clarify a disputed gap, plot technical quality against user value and annotate the evidence. Both axes matter. Use an available visual skill when helpful; a diagram is not a required extra deliverable.
