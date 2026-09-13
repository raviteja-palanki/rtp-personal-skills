# Examples, calculations, and source limits

## Accuracy and exposure

At 92% correctness, the remaining 8% are incorrect under that evaluation's definition. The count depends on exposure: at 1,000 outputs it is 80 expected errors; at 25,000 outputs it is 2,000. The rate does not establish that each mistake is visible to a user, harmful, independent, or equally consequential. The earlier “thousands every day” statement omitted the required volume.

For annual expected loss, the main skill's $250,000 / $150,000 / $50,000 comparison assumes 10,000 annual exposures per row. The rows may refer to overlapping events; calculate scenario loss without counting the same consequence twice. Attack probability can also change with adversarial behavior, so a historical rate is not necessarily a stable future estimate.

Detection delay is one factor affecting loss and response. Multiplying cost by delay or dividing by an undefined detectability score produces a ranking whose units and meaning may be unclear. Preserve those dimensions explicitly unless a defensible model connects them. High-severity constraints can dominate an expected-dollar estimate.

## Cascade arithmetic

For two required stages with 0.95 success at each stage, a product of 0.95 × 0.95 = **0.9025** is appropriate if their success probabilities are independent, or if the second 0.95 is the conditional probability of succeeding given the first stage's success. The final error rate is not generally obtained by multiplying two standalone benchmark accuracies: input distribution, recovery, correlation, and the definition of success matter.

For the bad-input example:

```text
P(A supplies bad input) = 0.05
P(B corrects it | bad input) = 0.20
P(bad input then correction) = 0.05 × 0.20 = 0.01
P(bad input remains wrong) = 0.05 × 0.80 = 0.04
```

The previous version called the 1% branch confidently wrong; under the stated success definition, it is the corrected branch. No confidence measure was provided. B's behavior on valid inputs is also needed for overall final quality. If B's 20% refers to a different outcome, define that outcome before calculating anything.

## Document-tail cost

If ordinary documents cost $0.08 each and 5% of documents cost ten times that amount:

```text
ordinary contribution per incoming document = 0.95 × $0.08 = $0.076
long-document contribution = 0.05 × $0.80 = $0.040
overall mean = $0.116
long-document share = $0.040 / $0.116 ≈ 34.5%
```

If the tail is defined as ten times the **overall average**, its share is 0.05 × 10 = 50%. The old 40% figure follows from neither stated interpretation. These are illustrative workload assumptions; measure tokens, retrieval, retries, processing, human review, and other relevant cost components.

The old five-to-twenty-page typical document, two-hundred-plus-page tail, fifty-page fallback, 35% saving, and 95% retained utility are scenario values. Do not silently truncate a document or present a partial analysis as complete to meet a cost target.

## A documented error becoming precedent

The laundering-path idea is this library's synthesis from the August 2026 middle-office discussion, not an incident reported by the source. The local source is consultant/vendor-authored and refers to unnamed clients and unpublished analysis.

The useful question is whether uncertain resolved cases are promoted into reusable rules without adequate validation. Provenance can help detect and retract an error; it does not make every recorded answer permanent or prove correctness. A system can sometimes detect that it is uncertain before an expert resolves the case, so the fact that expert input was needed does not prove it could never recognize the boundary.

Test boundary cases, changes in escalation behavior, the correctness of generated rules, and the ability to find and correct dependent outputs. An ordinary representative sample remains useful alongside targeted cases. Controls should be matched to the job they actually perform: a valid schema is not verified content, and a signature is not evidence of effective review.

## Incident and threshold examples

The earlier three-agent stale-data story—19 days, 34 customers, three budget decisions—has no independently verifiable source in the provided material. Preserve it as a hypothetical cascade scenario. Six-hour freshness, 20% period-over-period deviation, and daily end-to-end checks are candidate settings to calibrate, not production requirements.

Likewise, these older values remain illustrative: thirty-second undo; three failures per ten minutes for a circuit breaker; a one-hour monitoring or recovery cutoff; 60% accuracy within a high-confidence bucket; cache coverage of fifty historical examples; 50-ms and 200-ms fallback targets; and 10%/50% mitigation-cost ratios. Set actual conditions from consequence, exposure, observed behavior, detection, and recovery.

There is no universal trust-recovery duration or rule that power users can safely absorb errors while casual users cannot. Test capability for the task. Irreversible harm may prevent full restoration while still requiring containment, correction, notification, and support.

## Evaluation-maintenance references

The old attribution to Hamel Husain of spending 60–80% of time on error analysis/evaluation was not independently verified in this pass. Treat it as a practitioner emphasis to source before quoting, not a required allocation.

Anthropic describes **eval saturation** as a suite reaching the point where it offers little signal for further capability improvement; a high-scoring suite can still detect regressions. It does not establish that the last 1% at a 99% score necessarily contains catastrophic failures. Review suites after relevant changes and newly observed failures, with a cadence suited to the system. [Primary evaluation guidance](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents).
