# AI product requirements concept guide

An AI-PRD connects user value, permitted behavior, evidence, failure handling, economics, and operating decisions. Model performance and recovery both matter. Neither can compensate for every weakness in the other.

## Why model metrics need product context

A classifier with 90% accuracy made errors on 10% of the measured sample. Future frequency depends on the population and operating conditions, and the consequence depends on which cases failed. A high average can hide a harmful minority-class failure. A product with lower model accuracy might still help through effective correction, but acceptance alone cannot establish that users corrected the errors.

Traditional products also face bugs, uncertain inputs, and operational failures. AI adds particular questions about learned behavior, data/context changes, calibration, and open-ended results. A determinism map helps locate components; it does not make every failure obvious or make prompt instructions reliable enforcement.

## Five specification gaps

1. **Happy-path bias:** examples show success but omit ambiguity, refusal, unavailable evidence, and recovery.
2. **Metric mismatch:** model accuracy is treated as the user outcome, or engagement is treated as proof of correctness.
3. **Undefined boundaries:** “refuse unsafe requests” lacks the relevant policy, permission checks, UX, and verification. A confidence threshold alone is insufficient.
4. **Incomplete economics:** the estimate covers one successful inference while omitting unsuccessful attempts, review, tools, evaluation, and fixed costs.
5. **Unclear components:** a prompt rule is labeled deterministic, or learned retrieval/ranking is hidden inside a supposedly rule-based stage.

## Three illustrative cases

The following cases explain design choices. Their old numerical thresholds and cost estimates were not documented deployment evidence and should not be reused as benchmarks.

**Support routing.** Separate parsing, classification, routing permissions, and escalation. Define classes before using “false positive” or “false negative”; a billing/security confusion can be both, relative to different classes. Inspect ambiguous queries, class-specific errors, and new vocabulary. A confidence-distribution change may indicate drift but cannot establish the true error rate without appropriate labels. User reassignment is a signal to review, not an automatically correct training label.

With 200 tokens per query, five daily queries per customer, and 10,000 customers, the workload is **10 million tokens/day across 50,000 queries**. If a hypothetical blended price were $1 per million tokens, token cost would be $10/day or $0.0002/query, before other costs. Real input/output pricing and overhead must replace this illustration. The former $0.10/day claim had no supporting price basis.

**Code suggestions.** Syntactically valid code can be semantically wrong, insecure, or difficult to maintain. Use relevant execution, integration, security, and human-review evidence. BLEU measures token overlap, not semantic correctness; edit distance and acceptance are behavioral signals with several explanations. Declining a suggestion is not necessarily a silent failure. Continuing to type may avoid a bad suggestion but does not undo code already committed or deployed.

At 300 tokens per suggestion, ten suggestions/hour, 1,000 developers, and four active hours/day, workload is **12 million tokens/day**. A hypothetical $1-per-million blended price gives $12/day in tokens, not an evidence-free $0.10–$0.15/day. Whether any per-user cost is sustainable depends on price, value, adoption, and full costs.

**Clinical decision support.** Define the intended clinical role, applicable oversight, patient population, condition-specific sensitivity/specificity, calibration, harms, and evidence requirements with qualified experts. An anatomical variation or prior surgery is a distribution/coverage issue, not inherently an adversarial input. False positives can cause serious harm; follow-up is not the only possible detection route, and some effects may be irreversible.

Do not transplant generic 95% accuracy, 2% false-negative, 80% escalation, or 3% override gates into clinical use. Whether and how to show suggestions requires domain and human-factors validation. Override rates alone do not establish model error or justify automatic retraining. A token count for an image is not a price: 500 images/day across all facilities differs by a factor of thirty from 500 at each of thirty facilities, and actual modality billing matters.

## Cost and reliability checks

Define the period, usage, billing units, retry policy, tools, evaluation, infrastructure, staff work, and allocation. Divide attributable workflow cost, including failures, by verified successful outcomes. Compare baseline, growth, optimization, and adverse price/usage cases. Keep the calculation inspectable rather than forcing it into a single paragraph or filling pages without a decision.

For multi-step behavior, use the conditional reliability distinctions in `agent-spec`; multiplying marginal accuracies requires assumptions. For confidence, `confidence-tuner` separates a model score from a calibrated event probability. Human review can help but must be assessed as part of the actual workflow.

## Lineage and reading

Google's [Rules of Machine Learning](https://developers.google.com/machine-learning/guides/rules-of-ml) supports starting simply, maintaining a sound pipeline, measuring behavior, and planning to iterate. Rule 16 concerns launching and iterating; the earlier skill attributed a different sentence to it. Rule 36 concerns feedback loops from positional features.

Don Norman's *The Design of Everyday Things* offers broader context on understandable behavior and recovery. The CONTEXT framework is a context-organization lens, not a guarantee that its Constitution layer is deterministically enforced or its Equipment layer is mostly learned ranking. Constitutional AI refers to training and evaluation methods, not a claim that ordinary prompt rules enforce themselves.

The user-provided Gupta/Jaffer article provides practitioner guidance on decision-focused PRDs, examples, stages, and prototype feedback. This library adapts that guidance; its template, numerical scenarios, and story-health metric are local designs. See [evidence notes](references/prd-evidence.md).
