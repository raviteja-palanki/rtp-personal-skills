# AI-PRD — Concept Guide

## FIRST PRINCIPLES

A traditional PRD specifies: what the user does, what the system does, what happens on success. It assumes that "the system does X" means "the system reliably does X." This assumption breaks for AI products.

In an AI product, the PRD must answer a question that traditional PRDs don't have to ask: **What does the product do when the AI is wrong, and how does the product behave at the boundary of the AI's competence?**

This is not an edge case. A classifier with 90% accuracy will be wrong on 1 in 10 requests. A language model with "good quality" will occasionally hallucinate information, misunderstand intent, or refuse to answer. These aren't rare bugs. They're design parameters. The PM's job is to acknowledge them in the spec and make them part of the product, not part of the "we'll fix this later" category.

The atomic insight: **The quality of an AI product is not determined by how well the AI performs. It's determined by how well the product handles when the AI doesn't perform.**

## DUAL DEFINITION

**Business definition:** An AI-PRD is a product specification that treats probabilistic outputs (model inference) as a product-level design parameter, not an implementation detail. It specifies not just what the AI does when right, but what the product does when the AI is uncertain or wrong — including failure detection, user recovery paths, cost boundaries, and the safety guardrails that prevent failures from cascading.

**Technical definition:** A specification document for AI features that includes: a determinism boundary map (which parts are rules vs AI vs hybrid), failure mode specifications (false positives, false negatives, boundary cases, adversarial inputs, drift), evaluation criteria (offline accuracy, online drift, user feedback loops), a cost model (tokens per request, user unit economics, cost ceilings), a safety and refusal policy (confidence thresholds, escalation triggers, PII handling), and production monitoring strategy (detection latency, recovery mechanisms).

## THE TRAP (Expanded)

### Success Bias in AI Specs

The demo shows the model getting it right. The user story describes the happy path. The engineering team specifies the inference latency and model serving infrastructure. But nobody answers: "What happens when the model is wrong?"

This is catastrophic for AI products. Unlike traditional software where bugs are rare, model uncertainty is guaranteed. The product that pretends this isn't true will ship brittle, will erode user trust quickly, and will scramble for damage control once the failures start accumulating.

### The Missing Bridge Between Model Metrics and Product Metrics

ML engineers optimize for accuracy. "90% top-1 accuracy on the test set" sounds good. But the product person doesn't care about top-1 accuracy. They care about: Does the user trust this? Can the user fix it quickly if it's wrong? Does the wrong answer cost money? Does it damage our reputation?

The gap between model metrics and product metrics is where many AI products fail. The model is 90% accurate, but the product is useless because the 10% of failures happen in the high-stakes scenarios, or because the failure mode is silent (user acts on wrong information without realizing it).

### Refusal Theater

Some teams specify that "the AI will refuse unsafe requests." But then there's no threshold specified. No measurement of refusal rate. No user experience designed for refusal. The result: the AI refuses too often (product is useless), or the team removes the refusal entirely (product is dangerous).

Refusal isn't a binary. It's a calibrated response that depends on: How confident is the model? What's the cost of a wrong answer? Is there an alternative path? The PM must specify the refusal policy as a product decision, not a vague guideline.

### Cost Model Blindness

Many AI product launches succeed in the pilot but fail at scale because the cost model wasn't understood. A feature that costs $0.01 per user per day is sustainable. A feature that costs $0.50 per user per day might be death on the balance sheet.

Teams often run the cost calculation wrong. They count tokens for a single successful inference, not including retries. They don't include context padding. They don't model the eval overhead (running the model on thousands of test cases to detect drift). The cost model is deferred to "we'll optimize it later," and then the feature either gets deprecated or becomes unprofitable.

### Determinism Boundary Neglect

Many AI PRDs fail to specify which parts of the system are deterministic and which are probabilistic. The result: nobody knows what to test, nobody knows where failures will happen, nobody knows which components need guardrails.

A good determinism map is worth more than a 100-page failure-mode analysis. Once you know which parts are rules and which are AI, the failure modes become obvious.

## INTELLECTUAL LINEAGE

**Ravi's AI Product Stack** — The CONTEXT framework (Constitution → Observations → kNowledge → Tracks → Equipment → eXecution → Template) is itself a determinism map. The Constitution layer is entirely deterministic (rules). The Equipment layer is mostly AI (learned ranking). The eXecution layer is hybrid (AI with safety guardrails). An AI-PRD applies the same thinking at the feature level.

**Anthropic's Failure Design Philosophy** — Claude doesn't just optimize for accuracy. It optimizes for accuracy, refusal appropriateness, and transparency when uncertain. These are product-level decisions that show up in the spec and the user experience.

**Amazon's Six-Pager Culture** — A PRD should be short and decisive. The AI-PRD adds specific sections for probabilistic behavior, but follows the same principle: be specific, not vague. "High accuracy" is vague. "90% accuracy on the non-null class, 70% on edge cases, with automatic escalation below 75% confidence" is specific.

**Google's Rules of Machine Learning** — Specifically, rule #1: "Don't be afraid to launch a product without machine learning." And rule #16: "The best way to make progress on machine learning is often to reduce the problem to a simpler one." The AI-PRD embeds this thinking: it forces you to specify where AI actually adds value, not where it's just a hammer looking for a nail.

**Don Norman on Error Design** — In *The Design of Everyday Things*, Norman argues that well-designed systems make errors visible and recovery easy. Applied to AI products: the PRD must design for AI errors as explicitly as for user errors.

## REAL-WORLD EXAMPLES

### Example 1: Intent Classifier in Customer Support Routing

**The Happy-Path PRD:** "Classify customer queries into categories. Route to appropriate team. Latency <500ms. Success."

**The AI-PRD:**
- Determinism: Input parsing (rules) → Intent classification (AI) → Routing rules (rules) → Human escalation (hybrid)
- Failure modes:
  - False negative: Low-confidence classification routed anyway → Customer waits, wrong team tries to help → Detection: escalation time > threshold → Recovery: auto-escalate to human
  - False positive: Misclassified as "billing question" when actually "account security" → Sensitive info discussed with wrong team → Consequence magnitude: high. Detection: user feedback button → Recovery: admin can reassign, plus security audit
  - Boundary case: Ambiguous query matching two categories equally → Random classification → Detection: confidence score near 50% → Recovery: route to senior agent instead
  - Drift over time: New query types (AI-powered chatbots trying to abuse the system) → Model accuracy drops from 88% to 81% → Detection: monitoring on live classification distribution → Recovery: trigger retraining workflow
- Eval criteria:
  - Offline: 88% accuracy on held-out test set
  - Online: monitoring P(confident classification) should stay above 75%, P(misclassification | escalated) should stay below 8%
  - User feedback: weekly review of thumbs-down classifications
- Cost model: ~200 tokens per query, 5 queries per customer per day, 10k active customers = 10M tokens/day = ~$0.10/day total, or $0.00001 per query
- Refusal policy: If confidence <70%, escalate to human. If ambiguity score (top-2 gap) <5%, escalate to senior agent.
- When wrong: User can immediately request reassignment. System learns from the reassignment (feedback signal). Monthly audit on reassignment patterns to catch drift.

**The difference:** The happy-path PRD would ship with no escalation logic, no monitoring, and a confusing failure when the AI got it wrong. The AI-PRD requires you to think through failure in advance, build the infrastructure for it, and measure it in production.

### Example 2: Code Generation in IDE Extension

**The Happy-Path PRD:** "Generate code completions based on context. Show in autocomplete. Acceptance rate >60%. Done."

**The AI-PRD:**
- Determinism: Context gathering (rules) → Ranking candidates (AI) → Display (rules) → User acceptance (user action)
- Failure modes:
  - False positive: Suggestion is syntactically valid but semantically wrong (uses wrong variable name, applies wrong algorithm) → User accepts and ships broken code → Consequence magnitude: high (code in production). Detection: hard to catch before commit. Recovery: depends on user testing, not product recovery
  - Silent failure: User sees suggestion, types something else, doesn't realize the suggestion was better → No feedback, no learning → Detection: nearly impossible. Recovery: only via user feedback or A/B testing
  - Boundary case: Suggestion is 50% correct (predicts 50% of the lines right) → User starts typing and refines it → Medium consequence magnitude. Detection: via keystroke patterns (user immediately overwrites). Recovery: don't show low-confidence suggestions
- Eval criteria:
  - Offline: BLEU score on held-out code snippets (semantic similarity)
  - Online: suggestion acceptance rate (should stay >60%), keystroke-after-suggestion latency (if user immediately overwrites, suggestion was bad), edit distance (how many characters does user change)
- Cost model: 300 tokens per suggestion, user might request 10 suggestions per hour of active coding, 1000 developers, 4 hours/day active coding = 12M tokens/day = ~$0.10-$0.15/day
- Refusal/filtering policy: If confidence <40%, don't show suggestion (better to show nothing than wrong). If suggestion requires user to change existing code, require >80% confidence.
- When wrong: User just keeps typing (low-friction recovery). Keystroke pattern indicates the suggestion was bad (learning signal). Weekly analysis of keystroke-after-suggestion patterns to detect drift.

**The difference:** The happy-path PRD treats acceptance rate as success. The AI-PRD recognizes that 60% acceptance could mean "users trust it" or "users accept it without realizing it's wrong." It builds in monitoring to detect silent failures.

### Example 3: Medical AI Diagnostic Assist (High Stakes)

**The Happy-Path PRD:** "Classify images for potential conditions. Show confidence score. Radiologist reviews. 95% accuracy."

**The AI-PRD:**
- Determinism: Image ingestion (rules) → Feature extraction (AI) → Classification (AI) → Confidence scoring (AI) → Display + recommendation (hybrid: AI output + human review requirement)
- Failure modes:
  - False negative: Image shows condition, model says it's clear → Radiologist trusts the AI and approves without looking carefully → Patient misses diagnosis → Consequence magnitude: catastrophic (patient harm). Probability: 2% (100% accuracy is 98% per-condition accuracy × multiple conditions). Detection: clinical follow-up (can't catch before). Recovery: none at point of error, only at clinical follow-up.
  - False positive: Image is normal, model says potential condition exists → Radiologist is prompted to look for something → May lead to unnecessary procedures → Consequence magnitude: medium (unnecessary cost, patient anxiety). Probability: 3%.
  - Boundary case: Borderline image (could go either way) → Model confidence 52% vs 48% for alternate → Flip a coin at the boundary → Radiologist can't tell if the AI saw something real or just got lucky.
  - Adversarial: Model trained on typical anatomy fails on anatomical variation (patient has relevant prior surgery) → Misclassification rate jumps to 15% for that subpopulation.
- Eval criteria:
  - Per-condition accuracy (not aggregate accuracy): must be >95% per condition
  - False negative rate <2% (because cost of misdiagnosis is high)
  - False positive rate <5% (because unnecessary procedures have cost)
  - Confidence calibration: if model says 90% confident, it should be right 90% of the time, not 70%
  - Drift detection on per-radiologist accuracy (different radiologists have different baselines; if drift changes this, model may have changed)
  - Subpopulation analysis: accuracy on diverse anatomies, ages, imaging equipment
- Cost model: 2000 tokens per image analysis, 500 images/day across all customers, 30 facilities = $0.15-0.20/day
- Safety policy:
  - Confidence threshold: <80% → auto-escalate to senior radiologist
  - Never suppress the AI's suggestion (radiologist should always see it)
  - Confidence must be well-calibrated (no false confidence)
  - Log every classification + radiologist decision for long-term monitoring
- When wrong: Radiologist has the authority to override (and does, frequently). Every override is logged. Monthly analysis of override patterns. Retraining triggers if a subpopulation shows >3% override rate.

**The difference:** The happy-path PRD focuses on accuracy metric. The AI-PRD recognizes that some errors are catastrophic. It requires per-condition accuracy (not aggregate). It specifies confidence thresholds that trigger escalation to human. It builds in subpopulation monitoring. It acknowledges that 95% accuracy means 5% error rate, and in high-stakes scenarios, that might not be acceptable — so the escalation policy is designed to catch the hard cases.

## THE COST MODEL SECTION (Critical, Often Skipped)

A cost model is not optional. A feature that's $0.01/user/day is sustainable. $0.10/user/day might break the balance sheet at scale. Yet teams spec features without doing the math.

**The math:**
- Tokens per request: (context window × fill% + output tokens)
- Requests per user per day: typical usage pattern
- Total daily tokens: (tokens per request) × (requests per user) × (users)
- Daily cost: (total tokens) ÷ 1M × (price per million)
- Model at 3x scale, 10x scale, 100x scale. Find the breakpoint.

**The scenarios to model:**
- Baseline: current capacity, current token price, current model
- Growth: 10x users, same per-user behavior. Does latency/cost scale linearly or worse?
- Optimization: reductions you could make (shorter context, shorter output, fewer requests per user)
- Failure: what if token price triples? Does the feature still make sense?

The cost section of an AI-PRD should be 1 paragraph of calculation, not 10 pages of justification. Math, not prose.

## FURTHER READING

- Ravi Teja Palanki, "The CONTEXT Framework" — Seven-layer AI product architecture
- Ravi Teja Palanki, "The Determinism Compass" — Mapping where AI belongs
- Anthropic, "Constitutional AI" — Hybrid design of AI systems with explicit guardrails
- Google, "Rules of Machine Learning" (especially rules 1, 16, 36) — When ML adds value
- Shreya Shankar et al., "No Code Changes, Lots of Headaches" — Production AI failure modes
- Barocas & Selbst, "Big Data's Disparate Impact" — How ML failures concentrate in subpopulations
- Martin Fowler, "Microservice Tradeoffs" — How to think about failure domains
