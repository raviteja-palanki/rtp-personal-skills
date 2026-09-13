# Problem–AI Fit: optional profile and examples

Use with the four-question assessment, not as a substitute for it. Reviewed 13 September 2026.

## Four dimensions for a deeper comparison

The old sixteen-point score combined four useful questions with unsupported approval bands. Keep the dimensions visible. If numbers help compare similar candidates, use 0–4 within each dimension, explain the anchor chosen, and leave unknowns unscored rather than turning missing information into zero.

| Dimension | Lower end | Middle | Higher end | Interpretation limit |
|---|---|---|---|---|
| **A. Input variability** | Fixed or tightly constrained inputs | Bounded variation | Open-ended or hard-to-enumerate variation | Variation may favor learned methods, but volume of distinct inputs does not prove the rules are complex |
| **B. Judgment or inference demand** | Direct lookup or specified transformation | Some inference or context-sensitive selection | Ambiguous evidence, substantial inference, or competing considerations | More judgment can make the task harder to automate; it is not an automatic AI advantage |
| **C. Evidence and data readiness** | Little usable task evidence | Partial coverage with known gaps | Suitable accessible data, references, and demonstrated task evidence | Training, retrieval, and evaluation data have different roles; quantity alone is not readiness |
| **D. Bounded consequences** | Serious exposure with ineffective or unproven controls | Some credible prevention, detection, or recovery with residual concerns | Evidence of acceptable exposure and effective controls for the proposed scope | High scores elsewhere cannot compensate for an unresolved consequential failure |

Intermediate ratings need written reasons. Record the least certain rating and whether changing it would alter the recommendation. A one-point change in an ordinal estimate does not automatically justify a different architecture.

If a continuing workflow asks for 0–16, an optional sum preserves compatibility, but label it **descriptive profile total, not a validated fit or readiness score**. Include the four components and hard constraints. The prior bands—13–16 “AI-native,” 9–12 “strong,” 5–8 “weak,” and 0–4 “not AI”—are historical and should no longer decide the recommendation. Similarly, the old four-YES/three-YES/two-YES grading was not validated and could conceal a failed safety condition.

## Numerical cutoffs removed as decision rules

The previous version used an 80% lookup baseline, a remaining 20% requiring AI, and a ten-times-cost condition. Those are examples, not laws. It also used 20–100 patterns, fewer than 100 versus 100–1,000 versus 1,000–10,000 versus 10,000-plus labels, and 80/90/99% accuracy requirements. Appropriate data and performance depend on the task, method, base rates, consequences, and controls.

Other unverified heuristics included 60–70% of enterprise proposals not needing AI, low-score teams almost always underperforming, maintenance costing three to five times the build, rules changing twice a year, and a task stable for two years being a lookup problem. Stability may make learning easier; binary output, a finite category set, or an afternoon rule draft does not rule out useful ML.

Example support hypotheses—forty-percent faster resolution, 70% patterned tickets, fifty thousand historic pairs, sixty-percent overrides, $200,000 and six months invested, a 25% foregone portal benefit, or a one-week reversal—must be replaced by the actual project’s evidence and assumptions. Old GPT-4o-based $0.02/ticket estimates do not establish current total costs.

## Three overengineering illustrations, corrected

**Ticket routing:** the prior story compared a six-month, $200,000 ML effort at 87% accuracy with a 200-line rules script at 92%, claiming zero cost and a disbanded ML team. These are not verified company results. The useful test is whether a rules baseline handles the actual routing distribution, including ambiguous language, changing categories, and consequential misroutes. It still has operating and maintenance cost.

**Lead scoring:** the example named four months of ML work, AUC 0.74, a two-week heuristic, and changes three times a year. It also claimed three variables explained 80% of variance and that the heuristic worked better without a comparable measure. Those conclusions are not supported. Compare ranking or classification on a suitable held-out population and assess business outcomes, selection effects, and actual workflow. AUC, explained variance, and conversion lift are not interchangeable.

**Fraud detection:** the old comparison used a nine-month model, 15% false positives, $500,000 annual infrastructure, and a $5,000 rules solution with “99% accuracy,” then described that as catching 99% of fraud. Accuracy and fraud recall are different; in an imbalanced task a system can be highly accurate while missing nearly all fraud. Compare relevant false positives, false negatives, loss, latency, and changing behavior. An amount/location/velocity rule is a candidate baseline, not established coverage or a guarantee that the task is non-adversarial.

These cases teach comparison with simple alternatives. They do not establish that model-based routing, lead scoring, or fraud detection is generally unnecessary.
