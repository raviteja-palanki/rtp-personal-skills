# Calculation and Evidence Notes

Reviewed 13 September 2026. These notes preserve useful examples and source leads while making their limits explicit.

## Correct an aggregate estimate without changing class meanings

The [judgy project](https://github.com/ai-evals-course/judgy) documents a Rogan–Gladen correction with **pass as positive**. Define sensitivity `s = P(judge passes | truly acceptable)`, specificity `c = P(judge fails | truly unacceptable)`, and observed judge pass rate `q`. Then:

`estimated true pass rate = (q + c − 1) / (s + c − 1)`

This is not “subtract the judge's bias.” For an illustrative `s = 0.90`, `c = 0.80`, and `q = 0.76`, the estimate is `0.56 / 0.70 = 0.80`. The package assumes `s + c > 1`. With a denominator near zero, estimates become unstable. An impossible estimate outside [0,1] warrants checking assumptions and estimation uncertainty; silently clipping it does not fix the measurement problem.

The primary paper [How to Correctly Report LLM-as-a-Judge Evaluations](https://arxiv.org/abs/2511.21140), v1, 26 November 2025, treats uncertainty from both evaluation and calibration samples. The correction requires conditional error rates that apply to the target population; it cannot repair arbitrary distribution shift or invalid reference labels. Sample design, changing mixtures within classes, and subgroup differences therefore matter. This is an aggregate estimator, not a case-level clearance mechanism.

The main skill uses **failure as positive** for its alarm-oriented confusion matrix. Translate that convention before using pass-positive software. The original research claim “TPR >96% on valid outputs, TNR <25% on invalid ones” used pass-positive labels; presenting it inside a failure-positive explanation reversed the meanings.

## Probability calibration

[Guo et al., ICML 2017](https://proceedings.mlr.press/v70/guo17a) studies calibration on image and document classifiers and reports that temperature scaling works well on many tested datasets. It does not validate any particular LLM's verbal confidence, every task, or an Endorse/Caution/Warn interface.

The current [scikit-learn calibration documentation](https://scikit-learn.org/stable/modules/calibration.html) defines reliability diagrams using mean predicted probability horizontally and observed positive frequency vertically. In that convention, overconfidence lies below the diagonal. The source skill had the labels reversed. For confidence in the predicted label being correct, define correctness as the event; for a binary event probability, use the event's occurrence. These plots answer different questions unless the event is the same.

The original sample bins—2 correct out of 50 predictions (4%), 8 out of 60 (13.3%), and 94 out of 100 (94%)—are illustrative arithmetic. Exact calibration also requires each bin's mean predicted score, not just the bin endpoints. A fixed 1,000-example minimum or ten equal-width bins is not a universal statistical design.

## The radiology and 49% stories

The source describes a hospital nodule-detection system at 89% accuracy, a redesigned signal interface, and 49% error reduction. It later labels the headline and 35/10/4 decomposition practitioner/illustrative rather than one audited study. Retain it only as an **illustrative interaction-design case**; do not present a named hospital deployment, clinical effectiveness result, or guaranteed improvement without a retrievable study.

Overall accuracy does not establish clinical adequacy, and radiologist agreement does not equal diagnostic correctness. The statement that 70% of errors were eliminated but that this caught 35% of errors has no consistent denominator as written. Adding 35 + 10 + 4 gives 49, but summing overlapping mechanisms does not establish a causal decomposition. There is no basis here for drawing a measured 49% breakdown chart.

The useful hypothesis survives: interpretable signals, relevant verification, and a practical escalation path may improve decisions. Compare against a suitable baseline and measure missed errors, unnecessary rejection, and final outcomes. Calibrated numeric displays may work for some users; the source does not establish that users universally prefer categories.

## Explanation, checkpoints, and real-time convergence

The original cites Sudakov and Furr, HBR, August 2026, describing a Lane/Boussioux screening working paper: unexplained recommendations reportedly improved decision quality by 4.3 points, explained recommendations did not show that improvement, bad-output detection fell 11.9 points, and compliance increased by about 10 points for acceptance and 26.9 for rejection. These remain source-reported, task-specific results, not newly independently verified here. A null improvement is not proof of no effect in every setting. Nor does an explanation of a recommendation have exactly the same mechanism as a warning that identifies uncertainty.

The MIT SMR checkpoint account cites an ongoing, largely unpublished practitioner study with no disclosed model, prompt, or rate. It motivates distinguishing caught bad advice from unnecessary rejection of good advice. It does not prove every checkpoint has an inevitable expiration date or that false rejection remains constant as users and models change.

The July 2026 sports-coaching podcast proposes convergence among a data signal, one's own direct observation, and an independent second observer, with a repeated inspection. Preserve this as a **practitioner decision heuristic**, not a validated gate for clinical, financial, or other high-stakes action. Consider independence, common-source bias, delay cost, available expertise, and the task's existing procedure. Agreement can be jointly wrong; a second look can repeat the same bias. The source does not specify degraded staffing arrangements. That absence does not establish that every two-channel arrangement is unsafe or that action must always wait for three-way agreement.

## Judge cases and historical thresholds

The original judge research figures—valid-output detection above 96%, invalid-output detection below 25%, human kappa around 0.80, grader attacks producing 35–90% false positives, and wrappers flipping 57–100% of verdicts—lack a precise primary citation in this skill. Keep them as research leads until their model, dataset, label convention, attack setup, and denominator are checked. They motivate concrete tests; they are not present-day prevalence estimates.

The legal-tech completeness example reports omission recall improving 0.41→0.89 after decomposing the rubric into commercial, risk-disclosure, and obligation completeness. Treat that numerical result as illustrative/source-reported rather than an audited product outcome. The useful method is testing omissions explicitly, then verifying whether the narrower rubric improves valid detection without excessive false alarms.

The following original defaults are planning illustrations, not release rules: 300–400 calibration examples with 200/100/100 splits; kappa >0.75 or <0.40; safety-critical detection >0.90; 20% false alarms; 30% ignored alerts; 50 warnings per day; quarterly recalibration; 5–10 user participants; a two-week calibration schedule; and model accuracy below 70% as an exit. Notice that a 200/100/100 split totals **400**, not 300. Choose sample sizes, precision, cadence, and operational limits for the specific decision.

## Novel Insights: trust and influence

The ledger passage on cross-cultural collaboration proposes two matched questions about trust and influence and interprets high trust/low influence as a possible accountability mismatch. This is a transfer from human-team research to AI use, not an independently validated AI instrument. The questions can uncover lack of challenge or appeal routes. They do not prove that the respondent fabricates reasons, and a difference score alone discards useful level information.

The same ledger cautions about explanation substituting for independent verification. Carry that as a testable mechanism with boundary conditions; it should not become a universal ban on explanation or a claim that only seeded errors can test review quality.
