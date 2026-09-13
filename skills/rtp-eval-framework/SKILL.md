---
name: rtp-eval-framework
version: v1.5.1_latest
description: "Design an evaluation approach for an AI product: define useful behavior, inspect real failures, choose representative and risk-focused cases, validate scorers, and set a justified quality bar. Use for a launch, quality complaint, evaluation redesign, or production-monitoring plan. Covers open/axial/selective coding, code and human checks, LLM judges, component and trajectory tests, pass@k/pass^k, rubric validity, source and tool context, normative benchmarks, adversarial probes, differentiation, and review of the conclusions drawn from results. Preserve useful regression coverage while testing relevant new capabilities. Separate correctness, constraints, user experience, cost, and uncertainty; a completed action or high score does not establish success by itself. Pairs with eval-driven-development, confidence-tuner, ai-product-metrics, production-observability, feedback-flywheel, failure-modes, and judgment-guard."
imports: [feedback-flywheel, first-principles, stress-test]
---

# Evaluation Framework

Define whether this product works for its intended users and decisions, then build evidence that can reveal where it does not. Deliver a failure taxonomy, an evaluation suite, and a justified quality bar.

## Begin with the claim the evaluation must support

Identify the customer outcome, supported task and scope, consequences of failure, actual permissions, and decision the results will inform. Reuse known context. A quick assessment can inspect coverage, scorer validity, and release criteria; a consequential launch or unexplained quality problem needs deeper analysis. Early prototypes and deterministic components can benefit from evaluation too—use lightweight observation or assertions when appropriate.

Three evaluation views complement one another:

| View | Useful question | Limit |
|---|---|---|
| **Benchmark/model** | What relevant capabilities and limits does a model show under specified conditions? | Transfer to this product is a hypothesis to test. A benchmark is one kind of evaluation. |
| **Product** | Does the complete product deliver the intended outcome on representative and critical cases? | Aggregate results may hide component, subgroup, or interaction failures. |
| **Trajectory** | Did the system reach the outcome through acceptable actions, state changes, and resource use? | A trace is evidence to inspect, not proof of the external outcome. |

These are complementary scopes, not a universal three-era maturity ladder. A product with strong benchmark results and dissatisfied users may have several causes, including workflow, measurement, distribution, or model limitations. Do not assume one cause or that every team occupies the same stage.

Keep four misleading-success patterns visible from the start:

- **Completion fallacy:** an email was sent, but to the wrong person or with the wrong content.
- **Corrupt success:** the desired result was achieved by violating a required constraint.
- **Unsupported execution claim** (called “agent gaslighting” in the source): the agent says it booked a flight without reliable evidence that the booking exists. The label does not establish intent to deceive.
- **Saturation blindness:** a high score is mistaken for complete coverage. A perfect regression result can be healthy; it does not establish perfection outside that suite.

## 1. Map the system, its context, and the evaluation boundary

Tailor coverage to the workflow rather than treating product labels as exclusive:

| System | Coverage to consider |
|---|---|
| Chatbot | Factuality, relevance, safety, interaction and conversation context; multi-turn behavior when supported |
| Copilot | Task quality, workflow fit, edits, acceptance and rejection outcomes; acceptance alone is not correctness |
| Agent | End-to-end outcome, tool selection, permissions, state, recovery, intermediate constraints, and resource use |
| Search/RAG | Retrieval relevance and coverage, answer grounding, citation support, freshness, and access rights |

Decompose the actual system into components and transitions; do not create subagents merely to evaluate it. A contract analyzer may include PDF extraction, term extraction, rule comparison, risk classification, and safeguards. Extraction can include probabilistic OCR, so choose tests by implementation rather than assuming it is deterministic. Component tests help localize failures; integration and end-to-end checks reveal interactions they miss.

For each material component, ask whether ML is needed, what data and evidence exist, which quality and legal/policy constraints apply, and whether a suitable reference judgment is available. A missing answer is a risk or investigation need, not automatically a reason to reject the component.

Use the **three gulfs** as diagnostic hypotheses:

1. **Comprehension/context:** missing or unsuitable retrieval, state, input interpretation, or tool information.
2. **Specification:** unclear goals, conflicting instructions, undefined scope, or an inadequate success criterion.
3. **Generalization/capability:** behavior the configured system cannot yet perform reliably on the relevant distribution.

Also inspect tools, infrastructure, reference labels, and graders. Several causes can coexist; their prevalence is not established by this framework. Compare plausible repairs, including a model change, rather than always blaming context first. Route context/instruction issues to `invisible-stack` and `context-spec` when the evidence points there.

Define the evaluation boundary: inputs supplied, information the agent must gather, environment, tools, starting state, human assistance, time, and costs. A supplied-input test measures a different workload from collecting those inputs in practice. It is not automatically a mathematical upper bound on end-to-end performance. State what was excluded and test the full workflow when making full-workflow claims.

## 2. Inspect cases and build a useful failure taxonomy

Start with representative traces and a deliberate sample of consequential or unusual cases. Include passes as well as reported failures so silent errors and grader mistakes can surface. Inspect the actual evidence available: user request, supplied context, retrieved material, tool calls/results, observable actions, and outcome. Do not invent or require unavailable private reasoning traces.

The open → axial → selective coding sequence helps turn observations into a taxonomy:

### Open coding: describe before forcing a category

Read each case closely and record what failed, surprised you, or needs clarification. Examples include an unwarranted refusal, an invented regulation, a missing second request, excess confirmation, or an inaccurate execution claim. Note the first visible failure and its effects, but also record independent later failures or successful recovery.

Use domain expertise appropriate to the task. Qualified external reviewers can contribute; outsourcing does not inherently invalidate the work. Keep the product team connected to evidence and decisions. Existing requirements and known risk categories can guide sampling while leaving room for new findings. Purely schema-free coding is one approach, not a ban on structured or mixed methods.

Fifty to one hundred traces can be an initial planning range, not a threshold for rigor. Sample size and time depend on task diversity, consequence, and trace length. A small review can be useful exploratory evaluation; describe its limits instead of claiming population assurance.

### Axial coding: group related observations

Cluster observations into specific categories such as fabricated regulatory citations or unnecessary refusal of routine requests. Retain the supporting examples and ambiguous items. Split categories that hide distinct mechanisms; combine duplicates without losing important differences. Frequency counts are observations in the sampled set, not automatically production prevalence.

One or two examples may justify a category or a test if the consequence warrants it. Do not park a severe rare failure merely because it lacks three repetitions. A taxonomy of five to twelve categories is illustrative; choose a useful level of detail.

### Selective coding: choose what to address and measure

Prioritize by severity, exposure/frequency, affected users, detectability, feasibility, and decision value. Hidden harm can deserve priority over visible irritation. Difficulty of scoring neither makes a failure unimportant nor automatically makes it the top priority. Select a manageable set of initial evaluators and name important gaps that remain.

The real-estate CRM example reports failed transfers (8), unsuitable tour rescheduling (7), excessive confirmations (4), misunderstood inquiry types (4), and claimed unavailable access (3). Treat these as source-reported illustrative counts without a population denominator. The useful result is a product-specific taxonomy that a broad helpfulness score might miss.

When production data is unavailable, construct cases across relevant dimensions such as persona, task complexity, topic, language, and state. Generating structured combinations before natural wording can improve diversity. A direct request for test queries can also be a starting point; inspect and revise the result rather than assuming either method guarantees coverage. Label synthetic cases and audit their distance from real use.

Revisit the taxonomy after material changes or emerging evidence, at a sustainable cadence. No surprise in four weeks does not prove that reviewers stopped looking. This qualitative method also helps `interview-synthesis`, but its social-science lineage predates its use in AI evaluation; it is one useful method, not the only rigorous approach to unstructured data.

## 3. Define the rubric and test its validity

Make criteria concrete enough that reviewers can explain a disagreement. Use binary checks for clear obligations, anchored ratings for meaningful degrees, and explicit unresolved states when evidence is insufficient. Binary labels do not remove subjectivity or guarantee agreement.

Check these six ways a rubric can mislead:

1. **Unclear priorities or aggregation.** State which dimensions are mandatory, separate, or combined. If using a weighted score, publish its weights and rationale; a rubric with separate gates need not invent weights. A review forum needs a shared standard and a decision process, not just more meetings.
2. **Circular validation.** If you add a dimension because it distinguishes people or systems, that difference does not itself prove the dimension matters. State the hypothesis and seek an appropriate external outcome or other independent evidence. Preserve a bridge to the old measure when useful; do not require an arbitrary one-cycle overlap in every case.
3. **Tool/configuration confounding.** Record the tools, retrieval/ranking configuration, inputs, and assistance. Hold them fixed when estimating another component's effect, or deliberately vary them in a design that can estimate their effects. Do not hold them fixed when the tool itself is the intervention. A null expert-novice difference may reflect task, instrument, power, or context; it is not proof of equal expertise.
4. **Supplied-input and comparator mismatch.** State what the evaluator assembled and which human/current-workflow comparison supports the claim. Human acceptance of a model output does not by itself establish workforce substitution. Use the comparison and costs appropriate to the decision; a new randomized human arm is not the only possible evidence source.
5. **Self-report, ceiling cuts, and common-method bias.** A maximum-score category can support a defined descriptive measure, but it loses information and may reflect rater style as well as substance. Retain original ratings and rater IDs when appropriate, report the definition, and examine independent outcomes or calibrated anchors. A cut below the ceiling is still a cut and does not by itself remove common-method bias. Do not infer a causal “superteam” recipe from same-rater correlations.
6. **Checks that only repeat the system's assumptions.** A system or author may propose a valid falsifier, test, or failure hypothesis. Its origin does not make it decorative. The check gains force from a genuinely discriminating condition and trustworthy evidence; independent review can expose blind spots. An internally written test with an external observable result can be valid. Incentives for reporting bad news also matter.

The source's numerical research examples and corrections are in [evidence and validity notes](references/evidence-and-validity-notes.md). Keep reported findings, methodological critiques, and proposed transfers distinct.

### Check conversation purpose where it matters

Duhigg's practical, emotional, and social conversation types offer a hypothesis for assessing whether a response fits the moment. A factually accurate answer can still ignore distress or a need to be heard. Label the user's expressed need when supported by the conversation; turns can mix purposes and should not require speculative psychological diagnosis. Even a single-turn factual request may carry emotional context.

Test whether task accuracy, acknowledgment, helpful next action, and interaction quality are appropriate together. Emotional fit does not excuse inaccurate consequential guidance. Pilot this lens rather than treating it as a validated universal scoring taxonomy.

## 4. Choose and validate scorers

| Requirement | Suitable starting approach | What still needs checking |
|---|---|---|
| Exact format, required field, calculable condition | Code assertions, parsers, or tests | Test correctness, coverage, environment, and meaningful semantics |
| Ambiguous specification | Clarify the requirement with its owner and retain a case that tests it | Repairing a prompt does not make an evaluator unnecessary or free |
| Semantic judgment with a usable rubric | Qualified human review, an LLM judge, or a combination | Reference quality, task fit, bias, repeatability, and cost |
| Unresolved definition of good | Exploratory review, user/domain research, and explicit uncertainty | Do not automate a confident verdict before the criterion supports it |

For LLM judges, define the positive class before reporting TPR/TNR. If **pass is positive**, TPR is the fraction of truly acceptable outputs passed and TNR the fraction of truly unacceptable outputs failed. The `confidence-tuner` alarm-oriented table uses **failure as positive**; translate labels before comparing rates. Report both rates and counts. Overall agreement or kappa can add information but cannot replace class-specific error analysis.

Separate rubric/prompt development examples from held-out assessment. Inspect human disagreements; 73% agreement does **not** mean 27% of labels are noise. Clarify ambiguity, preserve legitimate differences, and adjudicate consequential disputes. Reusing the same 50 examples to tune and certify the judge overstates generalization. For ordered scores, choose a reliability statistic suited to the scale and design; unweighted categorical kappa does not capture ordinal distance.

Probe verbosity, candidate order, self/family preference, omissions, irrelevant wrappers, prompt injection, and evaluator leakage. Assess uncertainty and relevant slices. No fixed 80% TPR, 70% TNR, 80% agreement, or 0.70 kappa authorizes deployment by itself. Use `confidence-tuner` for calibration, bias correction, and threshold design.

## 5. Evaluate the agent and its environment together

The **evaluation harness** runs trials, graders, state setup, and results collection. The **agent harness** supplies the model's tools, context, state, recovery, and execution rules. Record and test their versions along with the model; the same model can behave differently under different harnesses.

Use a known starting state and isolate independent trials to prevent unintended carryover. A deliberately stateful sequence, cache, or memory can be part of the product being tested; define it explicitly rather than wiping away the behavior under evaluation. Simulations and replay have fidelity limits. Agent text, a screenshot, or a successful tool call may not alone establish the final external outcome.

| Agent task | Evidence to combine |
|---|---|
| Coding | Unit/integration tests, relevant execution results, requirement coverage, maintainability and security review |
| Conversation | Task outcome, interaction quality, appropriate refusals/escalations, unnecessary turns and bounded recovery |
| Research/reasoning | Correct claims, supporting sources, coverage, source quality and relevant freshness; citations must support the associated claims |
| Computer use | Before/after state, operation results, and appropriate backend checks; verify intended outcome and unintended changes |

Assess acceptable trajectories as well as outcomes. Different valid tool sequences can succeed; do not grade one expected path as the only correct path unless the process itself is required. Check authorization, duplicate actions, partial completion, timeouts, recovery, and resource budgets. No fixed claim that final-output tests miss 80% of failures or that state corruption is universally the leading failure is supported here.

**pass@k** asks whether at least one of k trials succeeds; **pass^k** asks whether all k do. They serve different deployment needs and neither is a universal shipping criterion. If trials have identical independent success probability p, these probabilities are `1 − (1 − p)^k` and `p^k`; actual dependencies and heterogeneous task difficulty need appropriate estimation. Multiple candidates are only useful if a user or system can choose a good one within cost and time limits. See `ai-product-metrics` for reporting.

### Preserve regression coverage and test what remains uncertain

Keep representative common cases and targeted rare/consequential cases, with clear weights or separate reporting. An enriched hard-case set diagnoses risk; its raw failure rate is not automatically the population rate. Common cases can require reasoning, and unusual cases can be memorized. Freshness does not prove a test was held out, and a public benchmark is not necessarily leaked to a particular model.

When relevant challenge cases become well supported, retain them as regression coverage. Add new capability cases where they test a meaningful need. Do not force a 60–75% baseline score, replace 20–30% monthly, or call every score above 85% useless. Version the dataset and document legitimate retirements so changes remain interpretable. `eval-driven-development` owns this maintenance loop.

### Include lifecycle quality where artifacts persist

Test foreseeable integration, modification, security, load, and maintenance demands. Some future failures can be represented with scenarios, fault injection, or change tasks before launch; others require longitudinal observation. A golden dataset is not inherently blind to every deferred failure.

Record relevant artifact provenance, tool/model versions, reviews, and release decisions. Provenance helps investigation and accountability; it is not a quality score or a substitute for tests. The SLSA standard concerns verifiable source/build history, not certification that someone exercised good judgment. Low-lifecycle work may need lighter records, but a one-off analysis can still have a lasting consequential use.

## 6. Add focused tests for the decision

### A normative reference when outcomes have no simple label

Where a defensible professional model, guideline, or standard exists, use it as an explicit **reference under stated assumptions**. It is not unquestionable ground truth, and a transparent task-specific rubric remains valid when appropriate.

The four-part method is: choose and justify the reference; decompose it into diagnostic tests; use realistic inputs while adding justified stress cases; and keep versioned comparisons across model generations. Test both relatively **invariant principles** and **state-dependent decisions** when the distinction helps. Many domains contain mixed cases; this is a useful slice, not the mandatory first cut for every evaluation.

The financial-advice case uses life-cycle modeling with consumption smoothing, diversification, and rebalancing diagnostics. It illustrates that broad alignment can coexist with systematic weaknesses. It does not make equity participation universally correct for every person, nor establish an individual financial recommendation. See the version-specific paper and comparison limits in the evidence notes.

### Adversarial probes

Test plausible attempts to manipulate instructions, access restricted data, misuse tools, bypass policy, or exploit encoded inputs. Prioritize by the threat model and use authorized isolated environments. Forty attacks can reveal defects; surviving them does not establish general safety. Dedicated expertise may be needed for consequential threat surfaces. Route findings to `stress-test`, `failure-modes`, and the relevant control owner.

### Differentiation, when different decisions matter

For a competitive pricing, ranking, bidding, or timing product, consider decision overlap with observable rivals, timing overlap, and reliance on distinctive inputs. Assign an owner and specify what competitor data are actually available and lawfully usable. Similar decisions may reflect good fundamentals, commodity economics, or common information; they do not prove strategic failure. Distinctive inputs do not guarantee better outcomes. Test customer and business value rather than rewarding novelty for its own sake.

### Audit the lesson drawn from the results

Before an important scale-up decision, have an appropriate accountable reviewer inspect the conclusion: comparator, sample, uncertainty, excluded work, alternative explanations, and what the result actually permits. This **learning audit** reviews the inference as well as outputs; keep it proportionate rather than adding a new approval to every small task.

Record unresolved questions, their owner, and a route to evidence. “No unresolved items” can be a legitimate result; do not manufacture uncertainty or assume reviewers were silenced. The question is whether uncertainty could be expressed and was handled honestly.

## 7. Set quality bars, cadence, and business interpretation

Derive the bar from consequence, customer needs, actual commitments, legal/policy requirements, the current workflow, alternatives, and feasible resources. Customer willingness to tolerate errors does not override other obligations. Leadership commitments usually impose requirements, not a quality ceiling. Competition can inform a comparator but does not define the only acceptable floor.

Progressive release limits exposure and supports learning; it does not justify a knowingly inadequate safety bar for the first 1% of users. State hard constraints, task thresholds, cost/latency budgets, uncertainty, and the response to failure separately. Calibrate alerting for severity, variability, sample size, repeated monitoring, and response capacity. Three times a standard deviation is not a universal regression detector.

A practical rhythm may combine fast checks on relevant changes, sampled production evaluation, and periodic expert review. Match it to traffic and risk; there is no universal weekly/monthly quota or full-suite requirement on every edit. Track labeling, model/tool execution, storage, review, and maintenance costs. At an illustrative $0.01 per case, 10,000 cases cost $100/run, $700 for seven runs, or $3,000 for thirty runs, before other costs.

Connect fixes to expected user outcomes and test the relationship with compatible measures. A flat satisfaction score may reflect low exposure, an insensitive measure, changed users, or a real disconnect; it does not automatically invalidate a safety or correctness improvement. Correlation alone does not establish causation. Report useful stories **and** measurements: failure, exposure, consequence, intervention, result, uncertainty.

Keep usage verbs precise—tried, active, paid, deployed—and distinguish a snapshot from a trend. Use local research and fresh primary sources when they materially improve the evaluation design; preserve source version and scope. Do not require reading the entire research library for every invocation, invent social posts, or automatically rewrite this skill because a test failed.

## Deliver the evaluation and its limits

Provide the supported decision and claim; system/evaluation boundary; prioritized taxonomy; dataset and sampling plan; scorer validation; baseline/current results; separate quality criteria; coverage gaps; and owners for maintenance and response. Include the key trade-off, material uncertainty, and next action. Fit the requested format and use the shared Universal Skill Protocol's relevant handoff fields. A coverage matrix or system-to-evaluator diagram may help when it clarifies the decision.

Before relying on the result, check that important successes and failures are represented, class labels and denominators are explicit, cases and graders are valid, state and versions are controlled, scores are comparable, and uncertainty is proportionate to the claim. Knowing five failure names from memory is not a substitute for evidence. A tool or suite can support quality, but neither guarantees a moat or a safe product.

Route execution of the ongoing development loop to `eval-driven-development`, scoring confidence to `confidence-tuner`, operational monitoring to `production-observability`, and reporting to `ai-product-metrics`. Use `feedback-flywheel` for reviewed feedback. A cluster may reveal a bug, an unmet need, or instrumentation noise; investigate before sending a discovery opportunity to `feedback-triage` and `opportunity-solution-tree`. There is no automatic 15% feature threshold or fixed conversion from a four-point recall drop to twelve-percent ticket growth. Use `judgment-guard` when the competence of human reviewers is itself part of the system's reliability.

See [the concept guide](CONCEPT.md) for worked examples and [evidence and validity notes](references/evidence-and-validity-notes.md) before reusing historical research figures.
