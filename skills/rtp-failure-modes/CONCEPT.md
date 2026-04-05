# Failure Modes — Concept Guide

## FIRST PRINCIPLES

Traditional software has a small, well-understood failure space: crashes, bugs, timeout, data corruption. AI products have an expansive, poorly understood failure space because the system can produce outputs that are syntactically correct but semantically wrong, contextually inappropriate, or subtly biased — without any error signal.

The atomic insight: **AI failure is not an event. It's a spectrum.** The model doesn't crash — it produces an output that's somewhere between perfect and harmful, and the product's job is to handle every point on that spectrum.

## DUAL DEFINITION

**Business definition:** Failure mode analysis for AI features identifies every way the feature can fail users, quantifies the business impact of each failure type, and ensures mitigation investment is proportional to risk — preventing both under-investment in dangerous failure modes and over-investment in trivial ones.

**Technical definition:** A systematic taxonomy of non-deterministic system failures — hallucination, refusal, drift, latency degradation, cost overrun, and output bias — with probability estimates, consequence magnitude calculations, detection mechanisms, and mitigation architectures for each.

## THE TRAP (Expanded)

**The Accuracy Mono-focus.** Teams obsess over model accuracy while ignoring latency, cost, and drift. A model that's 95% accurate but takes 4 seconds to respond loses users faster than a model that's 88% accurate at 500ms. Accuracy is one of six failure dimensions, not the only one.

**The Silent Drift.** Model providers update models without announcement. Behavior changes subtly. The team doesn't have automated regression tests against a reference set. Weeks later, support tickets spike. Nobody connects the dots because the model "didn't change" — but it did.

**The Bias Blindspot.** Teams test with representative data and conclude "no bias." But the test data itself reflects existing biases. The model performs well on majority cases and poorly on minority cases, and the aggregate accuracy metric hides the disparity.

## INTELLECTUAL LINEAGE

- **Aman Khan (Arize AI)** — Production ML observability. On the difference between offline metrics and production behavior.
- **Anthropic's 4D Framework** — Evaluating AI systems across multiple dimensions, not just accuracy.
- **FMEA (Failure Mode and Effects Analysis)** — Industrial engineering methodology adapted for AI products.
- **Eugene Yan** — On the gap between model metrics and product metrics in production systems.

## REAL-WORLD EXAMPLES

**Hallucination in legal tech (catastrophic consequence magnitude).** An AI legal research tool hallucinated case citations — LLM-generated names like "United States v. Margenthau (2019)" that sounded plausible but didn't exist. Consequence magnitude: catastrophic — lawyers cited fake cases in briefs, creating legal liability for the company and malpractice exposure for law firms. Detectability: near-zero (fake citations matched the format of real ones perfectly). Mitigation cost: high (every citation verified against a deterministic case database via deterministic API call before display, adding 200ms latency). Business impact: the mitigation cost was justified because the cost of not mitigating (lawsuits, destroyed trust, regulatory scrutiny) was orders of magnitude higher.

**Drift in customer support (silent failure).** Claude 2 to Claude 3 transition: a support team updated their AI backend. Model performance on accuracy metrics remained flat. But tone shifted from formal/professional to conversational/casual. Enterprise customers (Fortune 500 financial institutions) escalated, saying "your AI sounds like a teenager." No accuracy drop. No error signals. No monitoring caught it. Detectability: zero with standard LLM benchmarks; tone regression wasn't in their eval suite. Root cause: different system prompts between versions, never formally tested. Mitigation: integrated tone/voice regression testing into the eval pipeline (daily runs on reference customer support queries).

**Cost explosion in document processing (tail risk).** A document analysis feature that worked well for typical 5-20 page contracts. Context window scaled linearly with document length. Average cost per document: $0.08. Median: acceptable. But 5% of documents were 200+ pages (massive contracts, regulatory filings). These 5% documents consumed 10x average tokens, driving 40% of total costs. This tail-risk cost model wasn't visible in average-case metrics. Mitigation: hard limits on document length with graceful degradation (first 50 pages analyzed, user offered options for selective analysis or chunked processing). Business impact: reduced costs by 35% while maintaining 95% feature utility (most users didn't need all 200 pages analyzed).

**Bias in hiring.** An AI screening tool used to rank candidates was trained on historical hiring data. It systematically downranked women for senior engineering roles (27% lower callback rate, statistically significant). Consequence magnitude: catastrophic (discrimination liability, reputation damage, regulatory risk). Detectability: missed during development (accuracy metrics looked fine; no fairness metrics were in the eval). Root cause: training data reflected existing hiring bias; aggregate accuracy masked disparate impact. Mitigation: added stratified evaluation (separately measure performance by gender/race), hired fairness auditors, changed training data curation, added explicit diversity constraints to the model.

## FURTHER READING

- Aman Khan, "Observability for ML in Production" — Production failure detection
- FMEA methodology — ISO 60812 standard adapted for software
- Eugene Yan, "Evaluation Metrics for LLMs" — Beyond accuracy
- Anthropic, "Challenges in Evaluating AI Systems" — Multi-dimensional assessment
