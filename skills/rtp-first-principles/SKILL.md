---
name: first-principles
version: v1.2.1_latest
description: 'Clarify an AI product problem before choosing a solution. Identify the user outcome, break the work into essential operations, and decide which need rules, learned patterns, or accountable human judgment. Use for new feature proposals, technology changes, competitive responses, and diagnoses where the framing is uncertain. Keep the check brief when decomposition is already sound or the decision is easily reversible. Pairs with problem-ai-fit, determinism-compass, and bias-spotter.'
imports: []
---

# First principles

Identify what the user needs to accomplish before deciding what technology to build. Decompose the work far enough to choose and test the right components, while keeping the surrounding workflow visible.

Use a full pass for a consequential feature proposal, a disputed framing, or competing technical approaches. Use a brief check when the team has already decomposed the problem. When the problem is well understood and execution is the main uncertainty, proceed with the work rather than reopening the framing without cause.

**Pairs with:** `problem-ai-fit` to assess whether the underlying bottleneck needs AI; `determinism-compass` to choose rules, learned patterns, and judgment; `bias-spotter` to examine why a particular framing felt persuasive. Read [CONCEPT.md](CONCEPT.md) for the conceptual background and illustrative cases.

## Establish the context already available

Identify the user, their current workflow, the problem, and the trade-off under consideration. Use the request and existing evidence before asking questions. Ask only about a missing detail that would materially change the analysis.

Follow the user's requested depth and format. An inline answer is suitable for a quick check. A consequential architecture decision may need a fuller document, component table, and supporting evidence. The library's `UNIVERSAL-SKILL-PROTOCOL.md` supplies shared workflow guidance at the AI-PM source root or packaged plugin root; the essential method is self-contained below.

## Recognize a solution chosen too early

**Anchoring** occurs when an early solution becomes the frame for the whole problem. A competitor's launch, a senior stakeholder's preference, an appealing demo, or a tight deadline can make decomposition feel unnecessary.

For solution anchoring, ask: **Would we have identified this problem without first seeing this solution?** Finding a problem through a demo is a reason to seek independent evidence, not proof that the problem is imaginary. Look for user research, support records, observed friction, or another defensible signal of need.

**Complexity bias** treats a sophisticated solution as inherently more suitable. Establish a simple baseline before assuming that a language model is necessary. Depending on the task, that baseline might be a lookup table, string matcher, sorting rule, or explicit decision tree. Check its coverage, failure cost, maintainability, and exceptions against the actual traffic.

The earlier "80% lookup table" and "70% simple rules" tests are prompts to investigate coverage, not universal thresholds. Likewise, an assumed "95% handled by regex" needs measurement before it justifies a design. The point is to compare credible alternatives on the same task, not to prefer rules regardless of their performance.

## Terms used in this skill

| Term | Meaning |
|---|---|
| Atomic operation | The smallest useful operation needed for the user outcome; a workflow may contain several |
| Essential component | A component whose removal prevents the required outcome, including reliability, safety, or accessibility requirements |
| Optional component | A component that can be removed without violating the agreed outcome or requirements |
| Determinism spectrum | A way to distinguish explicit rules, learned patterns, and decisions that require judgment |
| Lookup table test | A comparison with a simpler implementation before adding model complexity |
| Capability and need | What a component can do versus what the situation requires it to do |

Earlier versions call essential components "load-bearing" and optional components "decoration." Treat these as functional distinctions, not judgments about the people or disciplines proposing them.

## Decompose the problem in six steps

### 1. State the user problem

Write one sentence in the user's language before naming the proposed technology. For example, "Find the current policy that applies to this case" is more informative than "Build an AI search feature."

Technology may be part of the user's actual task, such as administering a model platform. The test is whether the sentence explains the need rather than merely naming the solution.

### 2. Identify the essential operation and workflow

Ask what completion means to the user. Separate that outcome from its interface and implementation. Then identify the operations needed to achieve it, including dependencies, handoffs, and the final state. Do not compress several consequential operations into one vague label merely to produce a single "atom."

### 3. Test each component for necessity

For each proposed component, ask what happens if it is removed. Can the required outcome still be achieved at the agreed quality, reliability, accessibility, and risk level? If yes, consider simplifying or deferring it. If no, explain the requirement it serves.

### 4. Choose an approach for each essential component

| Situation | Candidate approach | What to check |
|---|---|---|
| Finite, enumerable inputs and outputs | Lookup table or template | Coverage, updates, and exceptions |
| Clear policy or if/then logic | Rules or conventional code | Correctness, conflicting rules, and maintenance |
| Patterns in unstructured or variable input | A learned model or hybrid | Representative performance, error costs, and drift |
| Genuine ambiguity or consequential judgment | Explicitly designed decision support, automation, or human review | Authority, evidence, accountability, reversibility, and failure response |
| Several of these within one workflow | Hybrid | The boundary and contract between components |

An input being unstructured makes AI worth considering; it does not establish that an LLM is the best choice. Human review also needs a purpose, capacity, relevant evidence, and authority. Use `determinism-compass` and the autonomy skills for the detailed decision.

### 5. State the resulting principle

Explain the operation, selected approach, and reason in one or a few sentences:

"The essential operation is [operation]. Use [approach] because [requirement and evidence]. Reconsider it if [condition]."

The result should help the team choose a design, not merely rename the proposal.

### 6. Compare component capability with product requirements

Describe what the component actually produces: a ranking, classification, extracted field, generated response, or proposed action. Compare this with the outcome the product promises, such as finding the right record, completing an authorized action, or giving a supported answer.

Record the measured capability, task population, product requirement, and remaining gap. Consider options such as a better prompt, retrieval, fine-tuning, validation, review, narrower scope, or a different product design. Choose based on evidence from the task. A general benchmark is not a substitute for the product's own evaluation.

## Revisit the framing when its conditions change

Before a substantial PRD or defensibility assessment, use the existing "Question Zero" check:

1. Separate observed behavior from assumptions about what is happening.
2. Write the current problem framing and the date it was last seriously challenged.
3. Consider alternative framings, using AI to propose useful questions as well as possible solutions.

The corpus uses twelve months without a meaningful review as a prompt to treat a frame as provisional. This is an operational heuristic, not an empirically established expiry date. Material changes in users, incentives, regulation, technology, or workflow can justify an earlier review. A settled problem in a stable setting does not need ceremonial reframing every cycle.

Connect this check to Question Zero in `rtp-moat-finder`: a defensible asset may still serve a problem that has changed.

**Source and limit:** Schonthal, MIT Sloan Management Review, "The Innovation Advantage GenAI Can't Give You," May 2026. The earlier source record attributes the three-step protocol to the article and characterizes its claim about cheaper ideation as an argument without measured value data. The twelve-month trigger is this corpus's interpretation. Do not repeat "ideation value is zero" as a measured result.

## Make problem definition visibly productive

Building a prototype has an obvious completion signal. Understanding a problem may involve unresolved questions and repeated discussion, making progress harder to see. The earlier corpus calls this the "progress-bar problem."

Give the reasoning a useful completion signal: a written problem statement, a short assumption record, and a test that could challenge the framing. Use rough prototypes to reveal missing questions and constraints, not only to demonstrate a preferred answer. Explain when revisiting a question is improving the problem definition, while placing a reasonable boundary on discussion that produces no new evidence.

If the problem is already clear and execution is the actual risk, visible implementation progress is appropriate. The check is whether the team agrees on the need, outcome, and relevant constraints without silently meaning different things.

**Source and limit:** HBR, "AI Makes Building Easy. Choosing What to Build Is Harder," August 2026. The prior source record notes that the contest described in the article favored problem definition and solution design in its judging criteria and reported no outcome effect size. That design cannot establish a general superiority of framing over execution. The observations about visible progress remain a useful mechanism to examine.

## Separate available strengths from present needs

Capability describes what a system or person can supply. Need describes what the situation calls for. Applying a strength to the wrong need is one way a capable system can fail.

- A model may supply fluent text when the task needs a verified fact.
- A leader may offer vision when a team needs fairness or reliable support.
- An agent may be capable of taking control while the task requires a checkpoint.

Ask what is needed before supplying the strongest available capability. This connects the lookup table test to the autonomy distinction between capability and permission, and to Ravi's Bridger approach of understanding a stakeholder before proposing an answer. The needs in an agent workflow belong to the people and task around it; avoid treating the agent as having human needs.

**Source connection:** van Vugt, Sheng, and Andrews, HBR, "Are You Meeting the Needs of the People You Lead?", 13 May 2026, supplies the leadership side of the earlier comparison. The machine side comes from the library's autonomy guidance. The connection is a corpus interpretation, not a universal explanation for every failure.

## Inspect the model as one component

The useful product question is what the current system can reliably do under the intended conditions. Inspect its documented capabilities, connected tools, memory, configuration, and actual task performance. Do not assume that all deployed assistants lack memory or current information, or that a model must fail on every unfamiliar problem.

Keep the distinctions that matter to the design:

- Fluent generation does not establish factual correctness.
- Current information requires an appropriate supplied or retrieved source.
- Session continuity depends on the surrounding memory and state design.
- Consistency depends on the complete system, not only a sampling setting.
- Longer workflows create more opportunities for errors, missing state, and failed handoffs; evaluate them at both component and workflow levels.

The surrounding engineering may include retrieval, APIs, state storage, validation, post-processing, review, and recovery. Retrieval-augmented generation is one option for supplying information, not the only way to obtain current data. Add complexity only when it improves the actual outcome.

This bounded architecture guidance is consistent with Anthropic, ["Building effective agents," 19 December 2024](https://www.anthropic.com/engineering/building-effective-agents), which distinguishes predefined workflows from model-directed agents and emphasizes task-specific tools, retrieval, memory, and evaluation. Its older tooling examples should not be treated as a current product inventory.

## Apply the lookup table test with real evidence

Compare the simplest credible baseline with a model or hybrid on representative cases. Consider the cost and consequences of both false positives and false negatives, exception-handling capacity, maintenance, and recovery.

An illustrative hybrid may use rules for 80% of cases and escalation for the remaining 20%. An alternative model may have 95% aggregate accuracy. Those figures alone do not establish which system is preferable: they use different measures, and the consequence and distribution of the remaining errors matter.

For a constructed fraud-screening example, rules might flag unusual location changes or transaction size, while a learned component investigates less explicit patterns. The earlier examples of transactions in two countries six hours apart or at 100 times a customer's average are candidate signals, not validated detection thresholds. Measure their usefulness and false positives in the actual setting.

An explicit escalation boundary can make limitations understandable, but its value depends on whether the escalation produces a timely, competent result. Do not assume that users always prefer a hybrid or always distrust a particular error rate.

## Decompose an agent's workflow and its evaluation

For the illustrative task "Research a company and write a two-minute brief," separate the work into finding information, filtering results, extracting facts, synthesizing the answer, and formatting it. The time label is a presentation target until the brief is rehearsed or timed.

| Operation | Possible implementation | Appropriate checks |
|---|---|---|
| Retrieve information | A defined API call, with query construction handled separately | Tool contract, authentication, errors, source freshness, and retrieval coverage |
| Filter results | Explicit rules, semantic ranking, or a hybrid | Rule tests and representative relevance judgments |
| Extract facts | Structured parsing or model-based extraction | Schema checks and field precision/recall on labeled examples |
| Synthesize | Model-supported composition and review | Factual support, completeness, coherence, and task-specific quality |
| Format | A template or other predictable transformation | Output structure, rendering, and preservation of content |

Unit tests suit deterministic behavior. Learned judgments need representative evaluations, and the complete workflow needs integration and outcome checks. An API call may be deterministic in its interface while the information it retrieves changes; do not equate an API test with proof that the research succeeded.

The earlier file attributes the component-decomposition teaching to Mahesh without a complete source citation. Preserve that attribution as an incomplete provenance note, not an independent empirical authority. Anthropic's ["Demystifying evals for AI agents," 9 January 2026](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents), provides an inspected engineering reference for evaluating agent behavior across actions and outcomes.

## Work through a capability gap without inventing a safety threshold

The earlier medical-information example used an assumed benchmark score of 95% and an assumed product requirement of 99.5%, a difference of 4.5 percentage points. Retain this as arithmetic in a constructed example. Neither figure is a verified MedQA result, a clinical safety standard, or a deployment recommendation.

The useful exercise is to ask whether capability and requirement measure the same task and population, which errors remain, how serious they are, and whether a proposed control addresses those errors. Do not assert that prompting cannot close a particular gap, that review defeats the goal, or that a disclaimer makes deployment acceptable without supporting evidence. Consider narrowing the task or changing the product when the requirement cannot be supported, and identify the qualified review needed for the actual domain.

## Deliver a usable decomposition

For a full analysis, include:

```text
User problem: [the outcome in the user's language]
Essential operation and completion state: [what must actually happen]

Components:
Component | Essential? | Rule/pattern/judgment | Approach | Evaluation

Capability gap, where relevant:
Measured capability and population: [...]
Product requirement and its basis: [...]
Comparable gap or remaining uncertainty: [...]
Options and recommended approach: [...]

First principle: [operation, approach, and reason]
Trade-off: [what this choice gives up]
Reconsider when: [observable condition]
Next action: [step, owner, and date when established]
```

Do not invent missing values. Mark an assumption or propose a clearly labeled test. A short reply can express the same reasoning without displaying the template.

Before delivering, check that the problem and completion state are clear, essential components retain their purpose, the implementation choices have reasons, and the evaluations cover both components and the end-to-end outcome. Explain the main trade-off, remaining risk, and appropriate next step. A diagram is useful when it clarifies the decomposition; use `rtp-excalidraw-svg` when appropriate and available, or another suitable host workflow. A visual is not mandatory for an already clear answer.

Use a lighter approach for early exploration and reversible decisions. Novel problems may need discovery before decomposition. If incentives, politics, or authority are the central issue, route to the appropriate problem and stakeholder skills rather than treating a technical component map as the complete answer. Revising no components can be a legitimate result when the original design survives scrutiny; do not force changes to prove the exercise occurred.

**Version 1.2.1, 13 SEP 2026.** Preserves the six-step decomposition, lookup baseline, framing review, capability-versus-need distinction, agent component map, gap analysis, diagnostics, and output structure. Clarifies illustrative percentages and source limits, replaces blanket model-capability claims with task-specific checks, and removes mandatory format questions and decorative visual requirements. The concept companion carries the original case distinctions with explicit evidence status.
