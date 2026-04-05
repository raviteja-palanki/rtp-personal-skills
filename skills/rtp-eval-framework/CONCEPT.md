# Evaluation Framework — Concept Guide

## FIRST PRINCIPLES

Measurement reveals what you actually value. If you measure helpfulness scores, you get helpful outputs — but they might be unhelpful for users with different needs. If you measure user clicks, you get clickable outputs — but click-baiting is a form of helpfulness that degrades trust. If you measure speed, you get fast outputs — but fast hallucinations are worse than slow correct answers.

The atomic insight: **the evals you choose to run determine the behavior of your system. If you don't measure it, it doesn't improve. If you measure it wrong, the system optimizes toward gaming that metric instead of serving users.**

## DUAL DEFINITION

**Business definition:** An evaluation framework is a structured approach to measuring whether an AI system is performing at the quality level required for its use case, using a mix of automated metrics, human judgment, and production user signals to detect regression and guide improvements.

**Technical definition:** A tiered evaluation infrastructure consisting of unit evals (fast, cheap, for gating commits), integration evals (semantic quality on curated sets), human evals (ground truth measurement, for calibration), LLM-as-judge systems (automated semantic scoring at scale), and production monitoring (real user signals, for drift detection).

## THE TRAP (Expanded)

**Vibe Check Masquerading as Rigor.** You read through 10 outputs and say "looks good." This is not an evaluation. It's an availability heuristic — your brain remembers the impressions it notices and forgets the patterns. A good output catches your attention. A mediocre output doesn't. You're measuring salience, not quality. The trap is subtle: reading 10 outputs FEELS like evaluation, so you feel confident. Meanwhile, the 11th output you didn't read is a catastrophic failure for a user segment you didn't think to test.

**Metric Gaming.** You optimize for BLEU score. The model learns to output text similar to the reference output, even when the reference is incorrect. You optimize for LLM-as-judge score. The model learns to output text that impresses LLMs — verbose, hedging language that sounds "thoughtful." You optimize for user clicks. The model learns click-baiting. Every metric you measure becomes a target to hack.

**Eval Set Brittleness.** Your eval set has 100 examples. They all represent users like you — formal, patient, trying common use cases. A new user type arrives and hits a blind spot in your training data. The eval set never warned you. Not because you measured wrong, but because you didn't measure the right thing. Eval set representativeness is the blind spot that blindsides you.

**Human Annotation Quality Collapse.** You hire annotators. They label 1000 outputs. You get inter-annotator agreement of 73%. This means your "ground truth" is fuzzy — 27% of labels are noise. You then compare your model against fuzzy ground truth and conclude the model is 82% accurate. But is it? You don't know if the disagreement is noise or if the 82% is measured against contradictory labels. Annotation quality assessment is skipped, confidence is false.

**The Producer Fallacy.** You measure on examples produced BY your system in development (cherry-picked outputs). You don't measure on examples USED by real users (unfiltered distribution). You measure on outputs you know are good. Real production hits adversarial inputs, edge cases, and inputs outside your distribution. Your evals are not predictive of production quality.

## INTELLECTUAL LINEAGE

- **Eugene Yan on ML evaluation:** Beyond metrics; measuring what users actually care about. Applied to AI: the metric is not the goal; user value is the goal; the metric is just a proxy.
- **Aman Khan on evaluating AI:** Multi-tiered evaluation with LLM-as-judge for semantic quality. The insight: you can't hand-annotate everything, so build an evaluation system that's efficient at scale.
- **Katherine Lee on model evals:** The eval set composition matters as much as the metric. A biased eval set will produce biased models.
- **John Schulman on human feedback:** Humans disagree because the task is genuinely ambiguous, not because annotators are bad. Embrace disagreement as a signal, not a bug.

## REAL-WORLD EXAMPLES

**Example 1: Customer support classification (SaaS).** Built eval set with 100 support tickets. Classified them by humans. Got 92% accuracy on eval set. Shipped. In production, specific user segment (enterprise customers using non-English product names) hit 60% accuracy. Why? The eval set was entirely English support tickets from mid-market customers. The model was solving a different problem. The eval was rigorous but not representative.

**Example 2: Content generation (media).** Measured correctness using LLM-as-judge. Got 87% "correct" scores. Shipped. Users complained outputs were verbose, hedging, and evasive. Turns out the LLM-judge favored cautious language (hedging = looks well-reasoned to other LLMs). The eval metric optimized for a style users didn't want. Added human evaluation with explicit guidance: "clarity and directness matter more than hedging." Human eval score was 73%. But user satisfaction went up because the outputs matched user expectations, not judge expectations.

**Example 3: Recommendation system (e-commerce).** Measured using conversion rate from recommendations. 15% CTR on recommendations. But time-to-purchase went up (users were clicking the recommendations but taking longer to decide). Deep dive: recommendations were accurate but not diverse. Users were clicking accurate recommendations they didn't want, wasting time. Changed the metric to "diverse recommendations that convert within 30 seconds" (including measuring abandonment). CTR went down to 11%, but revenue went up. The old metric was gaming the system (high CTR but low revenue).

**Example 4: Fact-checking system (news).** Built eval set with fact-checkers labeling statements as true/false. Got consensus (inter-annotator agreement) of 68% — very low. Dug into disagreement. Found that fact-checkers disagreed on interpretation: Was a statement "mostly true" (checkers said true) or "misleading without context" (checkers said false)? The eval was measuring disagreement between judges, not system quality. Restructured evals to ask checkers to justify disagreements. Found real failures (hallucinations, misreadings) vs semantic disagreements (interpretation differences). Quality went from "confusion" to "actionable signals."

## THE EVAL-BUSINESS CORRELATION (Most Important, Most Skipped)

An eval framework is theater if it doesn't predict user value. You measure "LLM-as-judge score 4.2/5" and assume users will be happy. But what if higher judge scores correlate with lower user retention?

This happens when:
- Your eval metric (judge score) optimizes for something users don't care about (verbosity, hedging)
- Your business metric (user clicks) is gamed by the system (clickbait outputs rank high but erode trust)
- Your eval captures narrow competence but misses real-world requirements (answers are factually correct but slow to read)

**The solution:** Quarterly correlation analysis.
- Run a cohort analysis: users who got high-quality outputs (eval score > 4/5) vs low-quality (eval score < 3/5)
- Measure their retention, engagement, support tickets, revenue
- If high eval score doesn't correlate with positive business metrics, your eval is broken

This is the only way to catch metric divergence before it becomes a strategic problem.

## FURTHER READING

- Eugene Yan, "What you should know about ML evaluation" — On the gap between metrics and user value
- Aman Khan, "On Evaluating and Comparing Open Domain Dialog Systems" — On multi-tiered evaluation
- Katherine Lee, "Can Models Explain Themselves?" — On eval set composition and bias
- John Schulman, "Fine-Tuning Language Models from Human Preferences" — On handling disagreement
- Pearl & Mackenzie, *The Book of Why* — On correlation, causation, and measurement

## THE EVAL SET COMPOSITION DEEP DIVE

Most teams skip this and regret it. Here's what rigorous composition looks like:

```
EVAL SET COMPOSITION MATRIX

DIMENSION 1: USER TYPE
- Beginner (new to domain) — 20%
- Intermediate (familiar) — 50%
- Expert (power user) — 20%
- Adversarial (trying to break it) — 10%

DIMENSION 2: REQUEST COMPLEXITY
- Simple (single fact lookup) — 30%
- Moderate (multi-step reasoning) — 40%
- Complex (ambiguous, conflicting sources) — 20%
- Edge case (outside normal distribution) — 10%

DIMENSION 3: REQUEST DOMAIN
- Common use cases from our top 5 — 60%
- Long-tail use cases we've seen once — 20%
- Use cases we haven't seen but similar products support — 15%
- Adversarial attacks designed to break the system — 5%

DIMENSION 4: TEMPORAL
- Requests from month 1 after launch — 25%
- Requests from month 3 — 25%
- Requests from month 6 — 25%
- Requests from month 12 (latest) — 25%

This ensures you're measuring across user types, across complexity levels, across domains,
and across time. If quality degrades for experts or complex cases, you'll see it.
```

## THE LLM-AS-JUDGE CALIBRATION PROCESS

Don't just build an LLM judge and trust it. Calibrate first.

```
STEP 1: Build a test set of 50 examples
- Get 5 human expert judges to label each example (on a 1-5 scale)
- Calculate inter-annotator agreement (Fleiss' kappa)
- If agreement < 0.70, the task is too subjective to measure or the rubric is too vague
- If agreement > 0.80, proceed

STEP 2: Get the LLM judge to label the same 50 examples
- Run the LLM on all 50 examples
- Calculate agreement between LLM judge and human judges
- Should be > 80%

STEP 3: Analyze disagreement
- Where does the LLM judge diverge from humans?
- Is it systematic? (Always too generous, too harsh, biased toward certain styles?)
- Or random? (Just noise)

STEP 4: Refine the prompt
- If systematic, adjust the rubric and examples in the prompt
- If random, the LLM judge might not be suitable for this task

STEP 5: Re-test
- Re-run on the 50 examples
- Verify agreement > 80%
- Only then deploy at scale

This takes 2-4 hours but saves you from deploying a judge that's systematically wrong.
```

## THE REGRESSION DETECTION THRESHOLD

This is where most teams make a mistake. They set the threshold too low or too high.

```
SCENARIO A: Threshold too high (alert only if metric drops 20%)
- Few false alarms
- But real regressions miss the alert until they're big
- You discover the problem weeks later when users complain
- Too much damage

SCENARIO B: Threshold too low (alert if metric drops 2%)
- Few regressions are missed
- But you get hundreds of false alarms from noise
- Team ignores the alerts ("the alerts are always going off")
- Alerts become useless (alarm fatigue)

OPTIMAL: Calibrate based on noise
- Measure your metric on the same eval set 10 times over a week
- Calculate the standard deviation
- Set threshold to 3x the standard deviation
- This catches real regressions while filtering noise
```
