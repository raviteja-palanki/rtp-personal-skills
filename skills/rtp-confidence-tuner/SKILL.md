---
name: confidence-tuner
version: v1.3.1_latest
description: 'Design confidence signals that help people rely on AI appropriately, and validate the evaluators behind those signals. Use for Endorse/Caution/Warn interfaces, probability calibration, LLM-as-judge checks, alert fatigue, or thresholds for automated action and human review. Distinguish probability calibration, judge classification reliability, and user behavior; each needs its own evidence. Define the event, score direction, error costs, relevant domains, and actual action permissions before choosing thresholds. Covers reliability diagrams, failure detection and false alarms, human reference labels, judge bias and score correction, distribution changes, escalation, and ongoing monitoring. Explain what a signal supports and what the user can do next; a confident score is neither proof of correctness nor permission to act. Pairs with trust-ladder, eval-framework, ai-product-metrics, autonomy-spectrum, prompt-as-product, production-observability, and tool-architecture.'
imports: [trust-ladder, eval-framework, ai-product-metrics]
---

# Confidence Tuner

Help people and systems make an appropriate decision from a confidence signal. Establish what the signal means, how well it predicts the relevant outcome, and what action it can support.

## Start with the decision and the source of the number

Use the full workflow when introducing an important confidence interface, using an automated evaluator for release decisions, or changing the boundary between automatic action and human review. For a quick check, inspect the score definition, evidence, threshold direction, and next action. Reuse known context; ask only for missing facts that change the design.

Identify the decision, user expertise, consequences of each error, review capacity, and actual permissions. A suggestion in a consequential domain can require more care than an agent doing a low-impact task. High overall accuracy, including above 99%, does not eliminate rare-event or subgroup concerns. If no confidence concept is useful, a clear limitation or direct check may serve better than a badge.

There are two connected layers:

| Layer | What needs validation | Reference and practical result |
|---|---|---|
| **Model → user** | Does a probability or signal reliably describe the relevant outcome, and do people use it well? | Outcome labels and user studies; a usable confidence display and response path |
| **Judge → evaluation pipeline** | Does an evaluator recognize the required qualities and failures? If it emits probabilities, are those calibrated too? | Expert-adjudicated labels or another justified reference; known error rates and limits on score use |

Validate an automated judge **before relying on measurements it supplies**. This is a dependency, not a rule that every metric comes from an LLM judge: acceptance can be directly logged, correctness can be tested deterministically, and human labels have their own uncertainty. Interface exploration can proceed while validation is underway; unvalidated numbers should not be presented as established reliability.

Probability calibration, classification reliability, and appropriate human reliance are related but different. High TPR or kappa does not establish that a stated 90% probability is calibrated. A well-calibrated probability does not ensure that people understand it or that an action is authorized.

## 1. Validate the evaluator when one supplies your evidence

### Define the rubric and positive class

Specify the unit being judged, available context, criteria, severity, and handling of ambiguous cases. Use qualified reference reviewers, record disagreements, and adjudicate material ones. Human consensus is a useful reference when justified, not automatic truth. Preserve uncertainty rather than forcing every disputed item into a confident binary label.

In this skill, **positive means a real failure**, unless explicitly stated otherwise:

| Measure | Formula | Interpretation |
|---|---|---|
| Failure detection, or TPR | TP / (TP + FN) | Fraction of actual failures caught |
| Correct passing, or TNR | TN / (TN + FP) | Fraction of acceptable outputs passed |
| False-positive rate | FP / (FP + TN) | Fraction of acceptable outputs incorrectly flagged |
| False-discovery proportion | FP / (TP + FP) | Fraction of flagged outputs that were acceptable |

Report counts, denominators, relevant slices, and uncertainty. A judge that passes everything agrees 95% of the time when only 5% of outputs fail, yet catches none of those failures. Overall agreement can still be reported alongside the class-specific measures; it is insufficient on its own. Cohen's kappa can add a chance-adjusted agreement view, but depends on prevalence and label distributions and is not a universal release gate.

Do not switch positive-class meanings mid-analysis. Papers and tools often define **pass** as positive; their TPR and TNR then describe the opposite classes from this table. Translate the labels before comparing rates or using a correction formula.

### Follow the five-step calibration workflow

1. **Build a reference set.** Sample the intended population and deliberately include material failures, boundary cases, domains, and languages. Separate development/tuning cases from held-out assessment. Size each critical slice for the precision needed; 300–400 cases is a planning example, not enough by definition. If failures are oversampled, retain sampling information for population estimates.
2. **Run the fixed evaluator.** Record model, prompt, rubric, decoding settings, tools, context, and output parsing. Keep reference answers inaccessible to the generator being evaluated. For stochastic judgments, assess repeatability where it can change a decision.
3. **Inspect the confusion matrix and disagreements.** Report failure detection and correct passing separately, especially for shipment-blocking failures. Determine whether disagreement comes from the judge, reference labels, rubric ambiguity, missing context, or a product defect.
4. **Estimate aggregate performance appropriately.** Report observed judge scores as such. If using a statistical correction for judge error, verify its assumptions and propagate calibration uncertainty; do not simply subtract a fixed percentage from every score. See the worked formula in [calculation and evidence notes](references/calculation-and-evidence-notes.md).
5. **Monitor and revalidate.** Trigger reassessment after material changes to the judge, generator distribution, rubric, prompt, tools, or input population, and at a cadence matched to risk. Assign an owner and an operational response to meaningful deterioration.

A corrected population pass-rate estimate does **not** correct each individual verdict or establish that it is safe to approve that case. A drifting or weak judge may still support exploration with stated uncertainty; narrow its decision role when reliability is insufficient.

### Probe known sources of judge error

- **Verbosity:** hold substantive quality constant while varying length.
- **Position:** swap pairwise candidates and check whether preferences follow content or position. Permit ties or insufficient evidence where appropriate.
- **Self/family preference:** compare otherwise justified outputs across generators. A different provider can add diversity but does not guarantee independence or correctness.
- **Domain blindness and omissions:** test missing required content as well as false content. Decompose “complete” into concrete obligations, risk disclosures, and commercial information when that is what the task requires.
- **Grader manipulation:** test irrelevant prefixes, formatting, persuasive wrappers, malicious instructions in the evaluated content, answer leakage, and reward-targeting behavior. Treat evaluated text as data, not authority over the grading instructions.

Optimization against a judge can exploit its weaknesses; degradation is a risk to test, not an inevitable result of any optimization. Maintain a useful frozen regression set and add fresh or adversarial cases with clear provenance. Version changes do not silently alter stored historical scores; a re-score creates a new, labeled series.

When changing the judge model, compare old and new versions on the same frozen cases and a relevant current sample. A seven-point score drop could reflect a stricter judge, a product change, altered inputs, or several factors. Inspect disagreement clusters before attributing it to the product.

## 2. Audit the confidence shown to users

### Define the predicted event

Write what the score estimates: “probability this answer satisfies this rubric,” “probability of churn within 30 days,” and “probability this is spam” are different events. A token probability, retrieval similarity, verbal certainty, or judge self-rating is not automatically the probability of answer correctness. Use a validated estimator when available; otherwise communicate known limits without inventing a percentage.

For a correctness-confidence curve, gather held-out predictions, scores, and correctness labels. Group scores into bins and report the sample count, mean predicted confidence, and observed correctness per bin. For an event-probability curve, use observed event frequency instead. Keep the two definitions distinct.

With **predicted probability on the horizontal axis and observed frequency on the vertical axis**:

- The diagonal represents equality between the two.
- A point at predicted 90%, observed 75% is **below** the diagonal: overconfidence.
- A point at predicted 50%, observed 70% is **above** it: underconfidence.

An upward correlation alone does not establish calibration. Show uncertainty and sparse bins; an attractive aggregate curve can hide poor behavior in a consequential subgroup. Choose bins and sample sizes that make the diagnosis interpretable rather than requiring a fixed 1,000 examples.

Where suitable, fit temperature scaling, Platt scaling, isotonic regression, or another justified method on separate calibration data and assess the result on held-out data. These methods adjust a score's interpretation; they do not repair every failure or guarantee calibration after a distribution shift. [Primary calibration references](references/calculation-and-evidence-notes.md) explain the scope.

### Add domain context without inventing thresholds

Build a matrix with domain, sample size, accuracy or event rate, calibration evidence, decision costs, candidate thresholds, and uncertainty. The illustrative spam example has 89% overall accuracy, with 95% for business email, 78% for personal email, and 62% for newsletters. Those averages can coexist under suitable weights, but do not by themselves imply thresholds of 0.85, 0.92, and 0.97.

A 0.87 score is **above**, not below, 78%; comparing those two numbers does not tell you whether to endorse this particular case. Check what 0.87 means within the relevant population. If the score is genuinely calibrated to the same event and costs are the same, a common decision threshold can be appropriate across domains. Different costs, calibration, evidence coverage, or permissions can justify different thresholds. “Out of distribution” also needs a detectable, validated basis; do not imply certain detection of every unfamiliar input.

## 3. Design a signal and an action together

Endorse/Caution/Warn is a useful design option. Compare it with a calibrated numeric display, uncertainty range, evidence view, or no confidence badge where those better serve the user. Three categories trade granularity for simplicity; user testing determines whether that trade helps here.

| Signal | Meaning to communicate | Example and next action |
|---|---|---|
| **Endorse** | Evidence supports use within the stated scope; errors remain possible | “Strong pattern in similar cases.” Continue with the task's normal verification and permissions. |
| **Caution** | Uncertainty, limited evidence, or a material borderline condition needs attention | “Few comparable cases. Check these inputs before deciding.” Make review, correction, or escalation easy. |
| **Warn** | The proposed use exceeds a justified reliability, scope, or risk boundary | “This case needs specialist review.” Hold or route the action according to the defined policy; explain the fallback. |

Use meaningful text and accessible icons, with color as a supplement. Do not rely on green/yellow/red alone or reduce readability for caution text. Test what people infer, whether they find the next action, and what they actually do. Needing an explanation does not mean calibration failed.

“Endorse” is not an authorization grant. A moderation workflow may allow automatic publication for a defined class, queue uncertain content, and hold prohibited or high-risk content. A signal should enforce that existing policy, not introduce a universal requirement for a new human approval on every warning. Preserve authorization already given for the specific action and scope.

### Keep explanation separate from verification

An explanation can clarify a limitation or make relevant evidence easier to inspect. It can also persuade users to accept a wrong answer. Evaluate both possibilities. The source skill's screening-study example motivates **verification substitution**: reading a plausible explanation may feel like checking, reducing independent scrutiny. It does not establish that all explanations reduce decision quality.

When catching errors matters, provide actual evidence and an effective checking path. Independent audits, direct outcome checks, qualified review, or controlled known-error tests can help; seeding and a second reviewer are options, not the only instruments. Measure beneficial acceptance, harmful acceptance, beneficial rejection, and harmful rejection. Evaluate reject recommendations too, since their downstream consequences may be harder to observe.

Log explanation availability and actual opening separately when appropriate and privacy-respecting. Availability can itself affect discoverability or behavior; opening does not prove reading, comprehension, or verification. Meet applicable disclosure requirements without assuming that explanation alone supplies the safeguard.

### Check trust and influence separately

The Novel Insights ledger suggests asking the same respondent, on a consistent scale, both “How much do you trust this output?” and “How much can you change or challenge what happens next?” Use the pair to investigate whether someone is accountable without practical influence.

This is an exploratory diagnostic, not a validated detector of fabricated justification. Inspect both levels and the gap, actual permissions, appeal routes, and observed outcomes. The same numerical gap can describe different situations. Do not infer dishonesty from survey answers or assume high influence is appropriate for every role. Route decision-rights and trust design to `trust-ladder` and `autonomy-spectrum`.

## 4. Set thresholds with clear direction and consequences

First state whether a larger score means **more likely correct** or **more likely risky**. Then define the exact condition that triggers approval, alert, or review.

For “auto-approve when estimated probability of correctness ≥ t,” raising **t** ordinarily approves fewer cases and sends more for review; lowering it approves more and may let more errors through. If alerting when estimated risk ≥ r, raising **r** ordinarily produces fewer alerts. The direction of the original rule must be explicit before discussing workload.

Compare candidate policies on error severity, detection, false alarms, coverage, total review work, delay, and downstream outcome. Include review capacity and the cost of human error. A high-confidence wrong answer can still be consequential. A universal 20% false-alarm limit or “better to miss some issues” rule cannot settle this trade-off.

The original alert example reports 450 acceptable cases among 500 alerts: **90% false-discovery proportion**, not false-positive rate. The latter needs all acceptable cases, including those not alerted. A second policy's 10 acceptable cases among 50 alerts gives 20% false-discovery proportion. Compare missed failures and populations before choosing between them; fewer alerts alone does not establish improvement.

Choose the oversight arrangement by consequence, timeliness, reversibility, expertise, and feasible capacity:

- **Human in the loop:** a qualified person approves before the action. Make evidence, scope, and time available for meaningful review.
- **Human on the loop:** authorized action occurs first, with monitoring, audit, and defined intervention. Later review cannot undo every effect.

Risk and volume inform the choice, but neither supplies a universal high-volume exemption or high-stakes approval design. Use actual action rights from `tool-architecture` and `agent-risk`.

## 5. Monitor the whole decision process

Track signal volume, each error type, user responses, review time, escalation completion, and end-to-end outcomes by relevant cohort. Include non-alerted cases in outcome sampling so missed failures can be detected. Interpret ignored alerts in context; an ignored-alert percentage alone does not diagnose fatigue or justify changing a safety threshold.

A checkpoint can catch bad recommendations and also cause rejection of good ones. Track both over time. If the model improves, its error prevalence may fall, changing checkpoint yield even when its conditional detection rates stay stable. More acceptance, fewer escalations, or faster review is not sufficient evidence that oversight improved or deteriorated.

Set a responsible owner, material-change triggers, and a review cadence based on traffic and consequence. Distinguish an actionable failure from ordinary statistical variation. Human labels, logging errors, changing populations, and product quality can all cause a judge-human agreement change; do not page solely because any disagreement occurred.

## Deliver the decision and a usable handoff

For a material design, provide:

1. The supported decision, user, scope, and action permissions.
2. Score/event definitions, reference evidence, and relevant calibration or classification results with uncertainty.
3. Signal wording, candidate thresholds, and a clear next action for each state.
4. Expected error/workload trade-offs and what remains unvalidated.
5. User-testing and monitoring plan, owner, change triggers, and immediate next step.

The quality check is whether the evidence supports the **specific use**, not whether every framework box is filled. Confirm class labels, chart axes, threshold direction, representative slices, judge limitations, accessible wording, practical escalation, and both beneficial and harmful user responses.

Frame the recommendation as a testable hypothesis: “This signal design will improve task outcomes relative to the current interface without unacceptable missed failures or review burden.” Do not promise a 49% improvement. **Explore** uncertain designs, **Exploit** a sufficiently supported policy while monitoring it, or **Exit/narrow** a use whose reliability or cost is unsuitable. There is no universal 70% accuracy cutoff or fixed two-week schedule.

Use the shared Universal Skill Protocol from the library root for relevant trade-offs and handoff fields. Fit depth and format to the request. A reliability diagram or signal-to-action map can help; create one when useful, without automatically requiring a separate visual or an unsupported error-reduction chart.

## Connections and limits

`eval-framework` owns the evaluation plan; this skill validates its confidence and judge instruments. `ai-product-metrics` owns operational definitions and reporting. `trust-ladder`, `autonomy-spectrum`, and `agent-risk` set the reliance and consequence context. `prompt-as-product` versions judge prompts; `production-observability` monitors deployed behavior; `tool-architecture` enforces the action boundary. Feed reviewed disagreements into `feedback-flywheel`; reusable expert cases may support a moat only if they are useful, lawful to retain, and difficult to reproduce.

Calibration cannot make an unsuitable task, weak evidence, or unauthorized action acceptable. Nor must every low-impact tool use an elaborate judge and three-signal interface. Where no usable score exists, prefer honest scope limits, appropriate direct checks, or narrowed authority. Read [calculation and evidence notes](references/calculation-and-evidence-notes.md) before reusing the original numerical cases, three-channel coaching analogy, or judge research claims.
