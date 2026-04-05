---
name: rtp-ai-prd
description: "PRD for probabilistic systems: model as spec, dual metrics, prompts as artifacts, thresholds, failures, cost, drift. Use when: shipped AI feature, architecture, capability launches. Triggers: 'AI PRD', 'probabilistic spec'"
imports:
  - determinism-compass
  - bias-spotter
  - stress-test
  - prompt-as-spec
---

# AI-PRD: Probabilistic Product Specification

## DEPTH DECISION

**Go deep** if: you're writing a PRD for a shipped AI feature, speccing a new capability, or doing architecture review. Read all 5 phases.

**Skim to Phase 3 (Eval Criteria)** if: you already have a PRD and need to add AI-specific acceptance criteria. Phase 3 alone transforms a generic PRD into an AI-native one.

**Skip** if: you're in early exploration testing desirability, the AI component is <1% of critical path, or this is a purely deterministic feature.

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md):
1. Ask the Grounding Questions (Section 1) — at minimum: Who is the customer? What problem? What are we saying YES to and NO to?
2. Route depth: Executive Summary or Comprehensive Analysis?
3. Identify output format: Document, presentation, spreadsheet, or inline?

Then proceed with the skill-specific analysis below.

## THE TRAP

You write AI PRDs like traditional software: feature works or fails, success = happy path. You spec output format, latency, constraints. **But AI doesn't fail binary.** It confidently returns wrong answers users trust. You miss: what happens at 60% confidence? What's hallucination rate? How does drift trigger retraining? These are **product decisions**, not implementation.

Three failure modes: (1) Success bias—spec only happy path. (2) Black-box thinking—"model classifies intent" without accuracy/threshold spec. (3) Launch theater—you'll "monitor later" because eval is expensive. Result: feature ships fragile, breaks at scale, drift goes undetected for weeks.

## THE PROCESS

### Phase 1: Map Probabilism (Not Just Determinism)

1. **Operations breakdown:** input validation → retrieval → ranking → generation → safety-filter → delivery. For each AI operation, specify:
   - Input domain (structured/unstructured, token range)
   - Output distribution (is 60% confidence acceptable? 75%? 90%?)
   - Confidence thresholds: show if > X%, ask for clarification if Y-Z%, decline if < Y%
   - Cost per inference (tokens in/out, model choice, overhead)
   - Failure mode probability (estimated from similar deployed systems)

2. **Dual success metrics framework:**
   - **User outcome metrics:** task completion rate, time-to-decision, user satisfaction
   - **AI-specific metrics:** accuracy (by class), hallucination rate, false positive/negative rate, latency (P50/P95), confidence calibration (does 80% confidence = 80% accuracy?)

3. **Prompts as product artifacts:** Version-control prompt templates, test prompt changes like code, A/B test competing prompts on eval set before launch. Log prompt version with every request for drift analysis.

### Phase 2: Failure Modes with Detection & Recovery

4. **For each AI operation, enumerate:** false positives, false negatives, boundary cases, adversarial inputs, drift over time. For each, specify:
   - **Estimated probability:** from base rate (if exists), similar products, or expert judgment
   - **Consequence magnitude:** revenue, user time-cost, trust damage, cascading system failures
   - **Real-time detection:** can you identify failure as it happens (e.g., user thumbs-down, confidence drop, contradiction in follow-up)?
   - **Containment:** isolation strategy (feature off, fallback to rules, human escalation, partial output)
   - **Recovery path:** user action required, system rollback trigger, communication to user
   - **Learning loop:** does detection feed retraining, threshold recalibration, or knowledge base update?

5. **Drift monitoring (living spec):** Specify:
   - **Drift metric:** accuracy drop, confidence vs. accuracy divergence, class imbalance shift, latency creep
   - **Monitoring frequency:** daily, weekly (based on feature risk)
   - **Retraining trigger:** if accuracy drops > X% OR confidence-accuracy gap > Y%, automatically retrain or escalate
   - **Capability decay plan:** when next model generation ships, what assumptions change? What needs reverification?

### Phase 3: Evaluation Criteria as Acceptance Criteria

6. **Eval criteria = acceptance criteria (not just nice-to-have). Replace vague success statements with binary pass/fail evals.** Key principle: **Every acceptance criterion must be testable and measurable.** Instead of "model should be accurate," write "pass@5 ≥ 0.95 on held-out test set of 200 cases." Instead of "model will be fast," write "P95 latency ≤250ms on 99th percentile query complexity." Binary pass/fail is stronger than Likert scales for go/no-go decisions.

   **How to decompose complex quality into multiple binary checks:**
   - "Model should understand user intent" → Split into: (a) Intent classification accuracy ≥95% on 500 labeled queries; (b) Top-3 retrieved documents match intent ≥90% of the time; (c) User satisfaction on intent mismatch queries <5%.
   - "Hallucination rate must be low" → Split into: (a) Factual consistency with source documents ≥98%; (b) No contradictions within 3-turn conversation; (c) Confidence scores > 0.8 never pair with factually incorrect outputs.
   - "Latency should be reasonable" → Split into: (a) P50 ≤150ms; (b) P95 ≤500ms; (c) P99 ≤1000ms. Not a single number—specify the distribution.

   **Pre-launch gate structure:** Before shipping, all binary evals must pass. No exceptions. No "we'll improve it post-launch." This is your product definition.

   Define:

   - **Offline eval:** labeled test set with splits by class, edge cases, demographic groups. Metrics: accuracy, precision/recall per class, confidence calibration (does predicted ≥80% = actual ≥80% accuracy?)
   - **Online eval:** production sampler (1-10% of requests), live metrics, user feedback loop (thumbs up/down, explicit corrections)
   - **Regression test suite:** baseline failure modes must not resurface
   - **Adversarial eval:** known jailbreaks, prompt injection patterns, edge cases
   - **Segment performance:** accuracy on long-tail inputs, minority classes, out-of-distribution cases

7. **Probabilistic Specs: Thresholds, Ranges & Degradation (AI-specific, non-negotiable).** AI PRDs must specify confidence thresholds, accuracy ranges (not single numbers), and explicit failure behavior. This transforms vague specs into actionable product decisions.

   **Confidence thresholds as UI logic (not just model internals):**
   - "Only show result if confidence > 0.85" — This is a product decision, not research. It means: users see your best-guess answers. Below 0.85, you're betting users would rather see fallback behavior.
   - "Prompt for confirmation if 0.70 ≤ confidence ≤ 0.85" — Two-step confirmation on borderline answers. Cost: extra user friction. Benefit: flags uncertain territory. Measure user acceptance rate on these confirmations.
   - "Decline (show fallback) if confidence < 0.70" — You're saying the answer quality is worse than your fallback system (rule-based, human escalation, etc.). Only specify this if you actually have a fallback.

   **Accuracy ranges, not single numbers:**
   - BAD: "Achieve 92% accuracy." (Ignores variance. What if it's 87% in production?)
   - GOOD: "85-92% accuracy on primary use case; ≥90% on high-trust segments; ≥75% on rare edge cases."
   - This forces you to think about where the model is weak. It's an honest spec. Then you can decide: accept lower accuracy on rare cases, or retrain until all segments are ≥90%.

   **Degradation behavior (explicit fallback paths):**
   - "If confidence < 0.6, fall back to rules engine" → If model fails, execute deterministic alternative. Must be faster and less accurate, but safe.
   - "If response latency > 2s, return cached result from yesterday" — Graceful degradation under load.
   - "If hallucination score (from safety model) > 0.5, escalate to human review instead of direct delivery" — Detection + containment chain.
   - "If accuracy drops below 85% (detected via daily eval), automatically retrain or disable feature pending investigation" — Drift-triggered automation.

   **Cost calibration to confidence:**
   - High-confidence answers might use expensive model (Opus, retrieval-augmented).
   - Medium-confidence answers route to cheaper model (Haiku, cached results).
   - Low-confidence answers escalate (human, no AI output).
   - This is not a luxury—it's how you manage cost at scale without sacrificing quality.

   **Define:**

   - **Hallucination rate target:** e.g., "≤2% factually inaccurate statements in generated output"
   - **Confidence thresholds:** "show full answer if >85%, prompt for confirmation 70-85%, decline + suggest alternative if <70%"
   - **Refusal triggering:** specify exact conditions (low confidence, jailbreak pattern, out-of-domain, safety model flag)
   - **User experience:** what does refusal look like? Helpful fallback or hard stop?

8. **Dual Success Metrics: User Outcomes + AI-Specific (non-negotiable).** Most AI feature PRDs measure only one: accuracy. You'll ship, launch, then realize you optimized the wrong metric. You need TWO metrics running in parallel.

   **User outcome metrics (what the business cares about):**
   - Task completion rate (e.g., "customer resolves issue without escalation")
   - Time-to-decision (e.g., "analyst spends ≤3 min reviewing recommendation")
   - User satisfaction (e.g., "Net Promoter Score on feature ≥50")
   - Engagement rate (e.g., "45% of users apply AI suggestion without modification")
   - Cost to user (e.g., "support ticket handling cost drops 30%")
   - Retention (e.g., "users with feature enabled have 20% higher month-over-month retention")

   **AI-specific metrics (what your model is actually doing):**
   - Accuracy (by class, by segment, by complexity tier)
   - Precision & recall (if classification task; false positive rate is often more important than false negative)
   - Latency (P50, P95, P99; not averages)
   - Hallucination rate (% of outputs containing factually incorrect statements)
   - Confidence calibration (does 80% confidence = 80% actual accuracy? Or 92%? Overconfidence is a failure mode.)
   - Cost per query (tokens × model price; track daily)

   **Why you need both:**
   - You can have 95% accuracy and 30% task completion (model is right but users don't trust it → bad engagement).
   - You can have 75% accuracy and 80% task completion (model is wrong but users filter intelligently → good engagement).
   - You can have 90% accuracy and 45% task completion, but cost explodes to $0.50/query (model is right but unsustainable → wrong lever).

   **Measurement cadence:**
   - User outcome metrics: tracked weekly (lagging, need aggregation), reported monthly
   - AI-specific metrics: tracked daily (leading indicators), alarms set on regressions
   - Correlation check quarterly: are we moving both together? If not, something is wrong (feature, metric, user behavior changed).

   **Optimization focus:**
   - If AI metrics are high but user outcomes dropping → problem is not accuracy, it's UX (presentation, trust, explainability). Don't retrain; redesign.
   - If user outcomes flat but accuracy improving → model is not the lever. Product or market or pricing is. Pause AI investment.
   - If both dropping → immediate escalation. Feature is breaking. Rollback or retrain.

   Define:

9. **Prompt Specifications: Prompts as Versioned Product Artifacts (non-negotiable).** Your prompt is not research—it's product. Treat it like code: version control, regression testing, A/B testing before production.

   **Prompt version control:**
   - Store every prompt version in Git (or equivalent). Include date, author, intent, evals result.
   - Tag production versions (v1.2.3_prod). Don't allow ad-hoc prompt changes in production.
   - Log prompt version with every inference request. When debugging failures, you'll need to know which prompt generated that output.

   **Example version log:**
   ```
   v1.0_prod (2025-02-15): Base prompt. Accuracy 91%.
   v1.1_beta (2025-02-20): Added context window guidance. Accuracy 92%, latency +15ms.
   v1.2_prod (2025-02-25): Merged v1.1 feedback. Accuracy 92%, latency baseline.
   v2.0_beta (2025-03-01): Restructured reasoning chain (CoT). Accuracy 94%, latency +200ms.
   v2.0_prod (2025-03-15): Approved for general availability after A/B test on 10% users.
   ```

   **Prompt regression test suite:**
   - Before any prompt change ships, it must pass regression evals on:
     - 200 labeled examples from your test set (same split, no peeking at production)
     - Historical failure cases (adversarial examples, edge cases that previously broke)
     - 3-5 "golden" examples that define correctness for your use case
   - Regression failure = prompt does not ship. No exceptions.

   **A/B test plan for prompt changes:**
   - Never roll out a new prompt to 100% of traffic immediately.
   - Canary: Deploy to 5% for 24-48 hours. Monitor: accuracy, latency, user satisfaction.
   - If canary metrics match baseline, proceed to 25% for 1 week.
   - Roll back criteria: accuracy drop >2%, latency increase >100ms, user satisfaction decline >10%, hallucination spike.
   - Only 100% after 2 weeks of no regressions at 25%.

   **Prompt change governance:**
   - Changes require: (1) eval result, (2) regression test pass, (3) PM approval, (4) A/B test plan.
   - Owner: Single PM or engineer owns prompt evolution. Prevents drift.
   - Frequency: Monthly review cycle. Ad-hoc changes require emergency escalation.

   Define:

10. **Pre-launch eval gate (non-negotiable):**
   - ≥X% accuracy on primary use case
   - ≤Y% false positives (high-consequence-magnitude failures)
   - Confidence-accuracy calibration verified (no overconfident errors)
   - Hallucination rate ≤Z%
   - All failure modes have detection + recovery path tested
   - Prompt version locked in production with regression test suite passing

### Phase 4: Cost Boundaries & Scalability

11. **Cost model (baseline → stress test):**
   - Tokens/request: input tokens (context, user query) + output tokens (include variance)
   - Requests/user/day: from usage forecast
   - Daily cost = (avg_tokens × requests × users × token_price) / 1M
   - **Three scenarios:** baseline (current), 10x growth (elastic demand), 100x (inflection point)
   - **Overhead:** retries (error_rate × tokens), eval runs (sampling cost), retraining infra
   - **Price elasticity:** model survives if token cost 2x? 3x? 5x?

12. **Cost ceiling & feature pivot trigger:**
    - Max acceptable cost/user/day (COGS breakeven)
    - Cost ceiling (above this, feature deprecates or pivots)
    - Token price monitoring: automatic escalation if costs exceed threshold

13. **Bias & Fairness (living evaluation):**
    - **Segmentation:** performance by demographic group, geography, language. Accuracy must not vary >X% across segments.
    - **Bias audit:** quarterly check for stereotype reflection, false bias (model favors one class), representation issues
    - **Mitigation:** prompt engineering, data rebalancing, threshold adjustment per segment, or explicit disclosure of limitations
    - **Escalation:** if fairness metric breached, feature pauses until remediated

### Phase 5: PRD Blueprint & Living Spec

14. **PRD sections (be specific, not vague):**

**AI-Specific Requirements (non-negotiable):**
- Accuracy: X% on primary task (Y% on minority class)
- Hallucination rate: ≤Z%
- Confidence thresholds: show if >85%, clarify 70-85%, decline <70%
- Latency: P95 ≤Yms
- Cost: $Z/user/day baseline, $W/user/day at 10x
- Drift monitoring: retraining trigger if accuracy drops >X% in 7 days

**Failure Modes Table:**
| Mode | P(occur) | Consequence Magnitude | Detection Method | Recovery |
| False positive | X% | [revenue/trust] | [method] | [action] |
| Drift | [estimate] | [metric] | [monitoring] | [retrain/patch] |

**Prompts as Product:** Version all templates. A/B test on eval set. Log version with requests. Regression-test changes before production.

**Evaluation Plan:** Pre-launch gate (offline), canary phase (1% users), general availability. Ongoing: daily accuracy metrics, weekly segment analysis, quarterly bias audit.

15. **Post-launch monitoring (living spec = ongoing work):**
    - Daily: accuracy dashboard, hallucination rate, confidence calibration
    - Weekly: segment performance, class imbalance, latency trends
    - Monthly: cost/user tracking, token price elasticity analysis
    - Quarterly: bias audit, capability decay check (new model available?), prompt effectiveness review
    - Trigger: drift detected → escalation → decision (retrain, pivot, deprecate)

## REALITY CHECK

- **Specification depth = risk level.** Medical diagnostic? 40-page failure matrix. Content recommendation? 1-page. Match rigor to user impact, reversibility, consequence magnitude.
- **Eval staging:** Ship with 70% eval done if consequence magnitude is acceptable, complete 30% post-launch. But be explicit: "Hallucination monitoring kicks in week 2" vs. "we'll monitor." Pre-launch gate is non-negotiable: accuracy verified, confidence calibrated, regression test passed. Post-launch eval is continuous.
- **Confidence thresholds via simulation:** Don't guess. Run eval set, find threshold where false negatives + false positives are both acceptable. If 85% confidence → 90% refused, threshold is too high. If 60% confidence required, evaluate the real-world false positive rate first.
- **Cost is a living decision:** Token prices change, usage patterns shift, new models release. Quarterly: is cost/user still within ceiling? If trend shows 5x in 18 months, start deprecation planning now. Identify the inflection point where feature becomes uneconomic.
- **Bias audits mandatory:** "We'll audit later" is not acceptable. Quarterly segment performance checks are product, not research. Accuracy must not vary >X% across demographic groups. If it does, feature pauses.
- **Drift monitoring is not optional:** Specify detection frequency (daily? weekly?), retraining trigger (accuracy drop >5%?), and escalation path. Drift that goes undetected for 30 days is a product failure.

## QUALITY GATE (5-item binary checklist)

- [ ] Dual success metrics defined: user outcome + AI-specific (accuracy/hallucination/confidence calibration)
- [ ] All failure modes listed with: probability estimate, consequence magnitude, detection method, recovery path, and whether it feeds retraining
- [ ] Pre-launch eval gate specified: minimum accuracy/confidence calibration/hallucination rate, regression test suite
- [ ] Cost model complete: baseline/10x/100x with token pricing risk analysis + identified ceiling trigger
- [ ] Living spec post-launch: daily/weekly/monthly monitoring cadence, drift trigger + escalation path, quarterly bias audit, capability decay check
- [ ] Prompts version-controlled, A/B tested on eval set before deployment, regression tested on code changes
- [ ] PRD reviewed by someone outside core team for missing failure modes or unrealistic thresholds

## WHEN WRONG

- Purely deterministic features (rules-based matching, ranking on exact attributes)
- Early exploration phase (testing desirability, not shipping)
- AI component has <1% impact on user outcome (genuinely nice-to-have)
- When you're spec'ing to delay launch rather than de-risk launch (eval rigor tax exceeds risk reduction benefit)

---

---

## TRADE-OFF LEDGER

Complete the Trade-Off Ledger from the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 3.

## CONCLUSION

Follow the Conclusion Protocol from the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 5:
1. State the recommendation
2. Name the key trade-off
3. Acknowledge the biggest risk
4. Define the next action

---

## VISUAL SUMMARY

After completing the primary output, invoke the **excalidraw-svg** skill to create a single Excalidraw SVG visual summary. This diagram captures the essence of the analysis in one glanceable image — making the deliverable 10x more impactful. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.
