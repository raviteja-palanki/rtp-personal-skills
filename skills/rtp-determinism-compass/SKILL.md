---
name: determinism-compass
version: v1.3.1_latest
description: 'Decide what must remain consistent in an AI workflow, where variation is useful, and how to verify both. Map each component to an execution pattern, acceptable variation, reproducibility needs, tests, and failure handling. Keep correctness, repeatability, and permission to act separate. Use for architecture, specifications, QA, model changes, or recurring reliability problems. Include end-to-end evaluation and the reversibility of consequential actions. Pairs with autonomy-spectrum, problem-ai-fit, eval-framework, and stress-test.'
imports: []
---

# Decide where variation is acceptable

Map the workflow before choosing sampling settings or tests. For each component, state what must stay correct, what may vary, how failure affects users, and how the result will be checked. Then choose deterministic code, model inference, or a combination that meets those requirements.

**Keep three decisions separate:**

- **Correctness:** Does the result satisfy the requirement? Identical wrong answers still fail.
- **Repeatability:** Under the same relevant inputs and conditions, how closely must results match? A model can produce different valid answers, or need to reach the same substantive decision in different words.
- **Authority:** What may the system do with the result? Reliable or deterministic behavior does not itself authorize an action.

Use a full component map for architecture and specification work. Use a focused check for a model change, test mismatch, or recurring failure. Revisit an existing architecture when evidence shows the boundary is wrong; this skill is not limited to initial design. Even creative or exploratory work can have fixed constraints such as permissions, format, or factual grounding.

## Start with the requirement, not the temperature

Name the user outcome, relevant inputs and system state, consequence of error, and decision being made. Use the supplied context and requested format. Ask only for missing information that changes the classification.

For each component, answer these seven questions:

1. **Input:** Is it structured or unstructured? Which changing state, source version, time, permissions, or tool result affects it?
2. **Output:** Is there one required value, one required substantive decision, or a range of acceptable outputs?
3. **Variation tolerance:** Which differences are acceptable, and how will they be measured? Separate wording changes from changed facts, decisions, or actions.
4. **Risk:** Where does variation create harm, inconsistency, unfair treatment, or downstream failure? Where does it create useful choice?
5. **Reproducibility:** What must be recorded or held fixed for debugging and audit? What degree of replay is actually supported?
6. **Dependencies:** How can errors propagate, be detected, or be recovered from? What counts as completed-work success?
7. **Reversibility:** Can a wrong result or action be undone, by whom, within what time, and at what cost? Identify residual harm even if the software change can be rolled back.

The useful classification is about the actual component. Routing can use rules or a model. Classification can use a deterministic algorithm or sampled generation. A fixed output format does not make its contents correct. Avoid treating input structure or domain name as a complete architecture decision.

## Build the component map

| Requirement | Candidate pattern | What to verify |
|---|---|---|
| Exact calculation, lookup, permission check, or well-defined transformation | Deterministic code or authoritative lookup where feasible | Correctness against the requirement, boundary cases, state, dependencies, and failure behavior |
| Unstructured input mapped to a required class or value | Model or parser with validated boundaries; rules where adequate | Semantic correctness, extraction quality, rare cases, consistency, and abstention or fallback |
| Several acceptable text or creative outputs | Generation within explicit constraints | Meaning, usefulness, grounding, constraints, and unacceptable outliers |
| A workflow combining these requirements | Hybrid components with explicit handoff contracts | Each component, each boundary, and the completed task |

A common pattern is input validation → model-assisted interpretation or generation → output validation and controlled execution. It is a useful starting point, not a rule that every router is deterministic or every core must use a model.

At each handoff, define the input and output schema, semantic expectations, authority, error signal, fallback, and owner. A schema can enforce fields or types; it cannot guarantee that the model selected the right customer, amount, or clause.

### Calibrate variation to consequences

Do not assign a percentage until "variation" has an operational definition. Ranking overlap, class disagreement, factual contradiction, and writing style are different measures.

- Recommendations, grammar suggestions, and code completions may allow several useful answers when users can inspect them. They can still carry serious risk in particular contexts; user review is a design assumption to test.
- Support wording may vary while the policy, facts, and promised action remain consistent.
- Calculations, binding transactions, and safety-critical instructions need verified substantive correctness. Legal or clinical judgment may still involve uncertainty; forcing identical text does not resolve it.
- A changed answer tomorrow may be appropriate if the evidence, policy, or user circumstances changed. Define what "same input" includes before calling this inconsistency.

An effective prompt is: "Which difference would cause a user or downstream system to make a materially different decision?" Specify that tolerance first. Repeated runs help reveal instability, but five, ten, fifty, or one hundred trials are not universal proof of reliability. Choose coverage and repetitions from the failure frequency and consequence you need to detect.

## Select controls that match the requirement

1. **Sampling and execution settings.** Check what the actual model and service support. Lower temperature may reduce sampling variation; zero temperature and a fixed seed do not guarantee correctness or identical execution across environments. Evaluate settings on the task instead of assigning them by domain.
2. **Versions and replay.** Record model identifier, prompt, tools, configuration, relevant source versions, and observed outputs. Pin versions where supported and useful. A replay claim should state which environmental conditions can be reproduced. [PyTorch's reproducibility guidance](https://docs.pytorch.org/docs/stable/notes/randomness.html) illustrates why seeds alone do not establish reproducibility across releases or platforms.
3. **Caching.** A valid cache entry can return the same stored result for the same key. Check freshness, identity and permissions, key completeness, invalidation, and fallback. Caching can repeatedly serve a wrong or stale answer; cache misses still follow their own execution path.
4. **Validation and fallback.** Use exact assertions for exact requirements, semantic evaluation for meaning, and controlled recovery for failures. A confidence threshold needs a defined, evaluated score and a cost-aware policy.
5. **Repeated sampling or voting.** Use only where candidates can be compared meaningfully and the measured benefit justifies cost and latency. Shared errors can defeat voting. Agreement is not truth, and neither voting nor caching is an evaluation metric.

Read [calibration and research notes](references/calibration-and-research.md) when considering the numerical examples or external governance cases. The operational rules above take precedence over illustrative settings.

## Choose the success measure deliberately

**pass@k** asks whether at least one of k trials succeeds. **pass^k** asks whether all k trials succeed. At k = 1 they coincide. Neither requires identical outputs: different valid answers can all pass. [Anthropic's agent-evaluation guide](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) explains their distinct uses.

For a task with independent trials and constant success probability p:

```text
pass@k = 1 − (1 − p)^k
pass^k = p^k
```

At p = 0.90, pass^3 = 0.729. Under those assumptions, at least one of three trials fails with probability 0.271. In real evaluations, estimate performance across representative tasks and repeated trials; do not raise an aggregate pass rate to a power and present it as a measured result when tasks differ or failures are correlated.

| Product situation | Useful measure | Important limitation |
|---|---|---|
| User expects one dependable completion | pass@1, repeated-trial consistency, segment and severity results | A high aggregate can hide failures in consequential cases |
| Several candidates are genuinely allowed | pass@k plus the selector's success, cost, and latency | A correct candidate helps only if the workflow can identify and use it |
| Batch classification | Per-item and per-class measures, plus workflow quality | One accuracy threshold rarely captures unequal error costs |
| Safety filter or protective control | Misses and false alarms by category and severity, with uncertainty | Finite tests cannot prove that it always catches every harmful case |

Choose targets from the use case. Being customer-facing, internal, or creative does not by itself choose a metric or acceptable threshold.

## Evaluate components and the completed workflow

Use several kinds of checks where they answer different questions:

- **Exact checks:** required values, schemas, arithmetic, deterministic formatting, permissions, and expected state changes. Exact checks can apply to a model's answer when the task really has an exact answer.
- **Property checks:** required fields, length, allowed content, invariants, and relationships among values. Passing these checks does not establish factual or semantic correctness.
- **Semantic evaluation:** task-specific correctness, groundedness, usefulness, and error severity, with a suitable grader and representative examples.
- **Repeated trials:** disagreement, unacceptable outliers, and the distribution of results under relevant conditions.
- **Regression evaluation:** a stable comparison set plus refreshed coverage for new failures and changed production conditions. Review before consequential model, prompt, tool, or data changes.

Specify sample size, coverage, repetitions, grading method, uncertainty, and a justified regression threshold. A set of 200 examples or a two-percentage-point alert can be a starting experiment; neither is a sufficient universal gate. Compare serious failures and important segments as well as aggregate scores.

### Calculate compounding only with stated assumptions

If every step must succeed and each step has the same independent success rate r, an n-step chain succeeds with probability r^n. More generally, multiply each step's success probability **conditional on the preceding steps having succeeded**. Marginal step accuracies cannot automatically be multiplied.

Under the equal-rate independent illustration:

| Per-step success | Five-step success |
|---:|---:|
| 99% | 95.1% |
| 95% | 77.4% |
| 90% | 59.0% |
| 85% | 44.4% |
| 80% | 32.8% |

At 95% per step, three steps yield 85.7% and four yield 81.5%. At 98% per step, five yield 90.4%. These are calculations for the stated model, not measured forecasts for an agent. Real systems can have correlated failures, conditional branches, retries, correction, or redundant paths. Measure the final outcome directly.

A single visible model response can also depend on retrieval and other hidden steps. Conversely, an intermediate error may be corrected before the final outcome. Avoid claiming that completed-work accuracy is always lower than every component's score.

### Keep majority voting distinct from pass^k

With three independent binary candidates, each correct with probability p, the chance of at least two being correct is:

```text
P(at least 2 correct) = 3p²(1 − p) + p³
```

At p = 0.77 this is about 86.6%; all three being correct is about 45.7%. A majority needs two votes, not unanimous agreement. For free-form tasks, several correct answers may differ and wrong answers may cluster. Define the equivalence and selection rule, then test the actual voting system before claiming this gain.

If the estimated or observed chain falls short, consider reducing unnecessary steps, improving weak components, adding useful verification, narrowing the task, or using human review where it adds sufficient value. A new checkpoint can have its own errors and cost; verify the completed workflow again.

## Cross predictability with reversibility before expanding autonomy

Predictability is how well the outcome can be anticipated. Reversibility is whether its consequences can be undone. They are separate from literal output determinism. Also consider severity, authority, exposure, and the speed of detection and intervention.

| | More predictable outcome | Less predictable outcome |
|---|---|---|
| **Readily reversible** | Proceed with proportionate checks and a clear recovery path | Run a bounded experiment when potential harm and cost are acceptable |
| **Hard to reverse** | Verify the commitment and critical assumptions before acting | Seek relevant dissent and evidence, reduce exposure, or redesign the commitment before proceeding |

This is a decision aid, not permission to bypass required review. A supposedly reversible pilot can still expose data, affect people, or incur sunk cost. If uncertainty cannot yet be reduced, look for ways to reduce the consequence of being wrong: smaller scope, staged commitments, or a credible exit.

The **verifiability cut line** asks how far the team can justify autonomous operation through checked goals, constraints, evaluations, escalation, and accountable oversight. Setup review alone is insufficient. Where per-output review is necessary, include its quality, capacity, and cost in the design; it may still be worthwhile. If the required review is unavailable, narrow or pause the autonomous action rather than pretending setup checks replace it.

A routine task can have high liability. Human accountability and operational performance targets serve different purposes and can both be necessary. See `autonomy-spectrum` for the fuller autonomy decision and `judgment-guard` for maintaining the expertise that oversight depends on.

Monitoring is especially useful where detection and intervention can limit consequences. For harmful actions that cannot be undone in time, establish preventive controls as well. Gates and monitoring can complement each other; reversibility alone does not prove that either is sufficient.

## Worked component map: contract-clause assistance

This example describes a candidate design, not validated legal performance. Domain reviewers must set acceptable uses and error consequences.

| Component | Requirement and candidate pattern | Evaluation | Reproducibility and recovery |
|---|---|---|---|
| PDF extraction | Faithfully recover text and layout; parser, OCR, or hybrid | Representative documents, missing text and order checks | Record parser/OCR version; flag unreadable or incomplete files |
| Clause classification | Required substantive labels from unstructured input | Class correctness, rare cases, disagreement, appropriate abstention | Record model/configuration; test any voting or fallback rather than assuming improvement |
| Risk scoring | A defined score with consistent decision meaning | Domain rubric, calibration if probabilistic, segment and outlier analysis | Track rubric and model versions; route unsupported cases |
| Summary generation | Wording may vary; facts, scope, and required caveats must hold | Grounding, completeness, usefulness, and authorized data handling | Preserve relevant inputs and output; review by agreed criteria |
| Output formatting | Exact schema or template requirements | Unit and snapshot tests where exactness matters | Version formatter; handle invalid content without silently changing meaning |

A risk-score variance threshold such as 0.2 has no meaning until the score scale and statistic are defined. A "no PII" check is appropriate only if the product actually prohibits that data in the output. The success criterion is the completed review-assistance task, including what the human must inspect or correct.

## Deliver the decision in a usable form

For a full review, use this matrix in the requested document, spreadsheet, presentation, or inline response:

```text
Determinism classification: [feature and user outcome]
Component | Required invariants and allowed variation | Execution pattern
          | Settings, if relevant | Tests and justified targets
          | Version/replay strategy | Failure and recovery owner

Completed-work evaluation: [measured results or explicitly modeled estimates]
Variation budget: [dimension, tolerance, population, consequence]
Reproducibility: [what can be replayed and what cannot]
Regression plan: [coverage, repetitions, change triggers, decision rule]
Autonomy: [authority, reversibility, preventive controls, monitoring]
Trade-off: [quality, cost, latency, flexibility, review workload]
Next action: [specific test or decision, known owner, decision point]
```

The shared `UNIVERSAL-SKILL-PROTOCOL.md` is at the AI-PM source root or plugin root. Apply its handoff guidance when another skill needs the result. [CONCEPT.md](CONCEPT.md) explains the boundary idea and additional examples.

## Final quality check

1. Every relevant component has an execution pattern and a clear boundary contract.
2. Correctness requirements and allowed variation are explicit and distinct.
3. Sampling settings are supported and evaluated; they are not promises of determinism.
4. Tests examine meaning and completed work as well as format.
5. Versioning, seeds, caching, voting, and confidence policies have stated limits.
6. Metrics match the actual attempt and selection process; pass^k is not called majority voting.
7. Compounding calculations state their assumptions and are distinguished from measured outcomes.
8. Autonomy reflects authority, severity, reversibility, and effective oversight.

Conclude with the chosen boundary, its principal trade-off and residual uncertainty, and the next action. Use a component-flow visual when it clarifies where checks and consequential actions sit; an already clear table may be enough.

**Version 1.3.1, 13 SEP 2026.** Puts consequential distinctions first; retains the component method, repeated-trial metrics, hybrid design, reversibility framework, cases, and research provenance. Corrects determinism, autonomy, sampling, and compounding claims.
