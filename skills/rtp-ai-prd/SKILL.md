---
name: rtp-ai-prd
version: v1.2_latest
description: "A product spec for AI features — different from a normal spec because the output varies run to run. Pins down what a normal PRD never has to: confidence thresholds (when to show vs. double-check an answer), behavior on failure, cost per outcome, quality decay over time (drift), and the named human who owns the result. Its real deliverable is production-grade AI *user stories* — backlog items that inherit those probabilistic elements as acceptance criteria, so teams stop shipping stories that assume the model will 'just work.' Use when: shipping any AI feature to production, capability launches, or grooming an AI backlog. Pairs with: eval-framework (the definition of good), cost-model (the economics), gen-ai-experimentation (the rollout design), ship-decision (the launch gate), user-stories (the story craft the inherited block lands in). Triggers: 'AI PRD', 'probabilistic spec', 'AI user story'"
imports:
  - determinism-compass
  - bias-spotter
  - stress-test
  - prompt-as-product
---

# AI-PRD: Probabilistic Product Specification

## THE ONE IDEA

**A normal spec describes one right answer; an AI feature returns a *distribution* of answers — so the spec's real job is to pin down what happens across that distribution.** When do you trust the answer, what do you do when it's wrong, who owns the miss, and how will you notice it quietly decaying. Get that right and this document becomes the thing it's actually for: **the source every AI *user story* inherits from**, so the backlog stops shipping stories that assume the model will "just work." An AI-PRD that doesn't end in production-grade user stories — ones carrying confidence thresholds, a named failure owner, a drift trigger, and a cost-per-outcome target — is analysis that never reached the team. The deeper truth underneath all of it: **the quality of an AI product is determined less by how well the AI performs than by how well the product handles when it doesn't.**

## DEPTH DECISION

**Go deep** if: you're writing a PRD for a shipped AI feature, speccing a new capability, or doing architecture review. Read all 5 phases.

**Skim to Phase 3 (Eval Criteria)** if: you already have a PRD and need to add AI-specific acceptance criteria. Phase 3 alone transforms a generic PRD into an AI-native one.

**Cold-start mode (45–90 min, no data, no upstream outputs — an interview, a Speclet session, a greenfield pitch):** skip phase order entirely and write straight through the document in § order (the template), reduced counts: §1 → §2 → 5 behavior examples (2 good / 2 bad / 1 reject) → provisional thresholds → top-3 failure modes + kill switch → dual metrics with the decision each triggers → 2–3 stories. **The ⚠-provisional protocol makes this legitimate:** any number you couldn't ground (threshold, cost, accuracy) gets the ⚠ tag inline, lands in §13 with an owner, and must be replaced by simulation or telemetry before the PRD advances past Kickoff. Proceeding on tagged assumptions is the discipline; proceeding on untagged ones is the failure. Do not stall hunting for data that doesn't exist yet.

**Skip** if: you're in early exploration testing desirability, the AI component is <1% of critical path, or this is a purely deterministic feature.

## THE TRAP

You write AI PRDs like traditional software: feature works or fails, success = happy path. You spec output format, latency, constraints. **But AI doesn't fail binary.** It confidently returns wrong answers users trust. You miss: what happens at 60% confidence? What's hallucination rate? How does drift trigger retraining? These are **product decisions**, not implementation.

Five failure modes: (1) Success bias—spec only happy path. (2) Black-box thinking—"model classifies intent" without accuracy/threshold spec. (3) Launch theater—you'll "monitor later" because eval is expensive. (4) Hope-based metrics—you spec metrics without the decision each threshold triggers. "Improve engagement" is a hope; "graduate at −10% handle time, auto-hold ramp at CSAT −2pts" is a decision. A great PRD adds decisions, not prose. (5) Orchestration theater—you spec a beautiful multi-agent flow but never define the *confidence handoff* between agents or the named human who catches the swarm when it loops. In 2026 some agents run autonomously for 8+ days with little human touch (⚠ reported), yet the high-stakes judgment still has to collapse to a named owner. Result: feature ships fragile, breaks at scale, drift goes undetected for weeks.

## KEY TERMS (plain language)

- **AI-PRD** — a product spec for AI features that (unlike a normal spec) must pin down confidence thresholds, failure behavior, cost, and drift, because the output varies.
- **Confidence threshold** — the score above which you show the AI's answer, below which you ask for confirmation or fall back.
- **Dual success metrics** — tracking both what users get (task completion) and what the model does (accuracy, hallucination rate) at the same time.
- **Hallucination rate** — how often the model states something factually wrong.
- **Confidence calibration** — whether "80% confident" actually means right 80% of the time.
- **Drift** — the slow decay of an AI's accuracy in production as the world changes; needs monitoring and a retraining trigger.
- **Behavior examples (good / bad / reject)** — concrete input→output examples that spec what the AI should do, get wrong, and refuse.
- **Accountable owner** — the named human who must *choose* to own the AI's outcome, set up with the conditions that keep them engaged.
- **User story inheritance** — the mechanism by which every AI-PRD element (confidence thresholds, failure modes + owner, behavior examples, cost-per-outcome, drift trigger) becomes explicit acceptance criteria in the downstream user story. If a story doesn't inherit them, the probabilistic decisions live only in an engineer's head.

## WHAT THIS SKILL CONSUMES & PRODUCES

An AI-PRD sits between discovery and the backlog: it takes the raw feature intent plus the evidence of how the model behaves, and it produces the probabilistic spec — and the user stories — every downstream team builds from.

**Consumes (upstream inputs → the PRD section they feed):**
- **The feature intent + problem + hidden job** — who, what, why, from discovery / `jtbd-analysis` / `opportunity-solution-tree` (the greenlit bet) → §1 Opportunity, §3 Users.
- **The strategy fit** — which pillar this unlocks now, from `strategy-canvas` → §1.
- **The AI-necessity verdict** — does this need AI at all, and in which seat, from `problem-ai-fit` → §1 why-now.
- **The autonomy level** — how much the AI decides vs. the human, from `autonomy-spectrum` / `ai-use-case-readiness` → §2 Boundaries.
- **The architecture line** — prompt-only / RAG / fine-tune / buy, and the rules-vs-model map, from `build-or-buy` + `determinism-compass` + `context-spec` → §5 Solution.
- **The definition of good** — eval criteria, thresholds, judge validation, from `eval-framework` + `confidence-tuner` → §6 Success Measurement.
- **The behavior evidence** — real good/bad/reject examples, from production traces or user research → §4 Behavior Contract.
- **The rollout mechanics** — shadow → A/B → progressive ramp, MDE, randomization unit, from `gen-ai-experimentation` → §8 Rollout.
- **The kill-switch + proportionality screen** — worst-case vs. value, pull-the-plug speed, from `agent-risk` + `failure-modes` → §9 Risk.
- **The legal/safety gate requirements** — PII handling, review obligations, from `responsible-ai-program` + `safety-by-design` → §9.
- **The telemetry conventions** — trace-level events, funnel definitions, from `ai-product-metrics` + `production-observability` → §10 Instrumentation.
- **The economics** — cost per successful outcome at P90, ceiling, pivot trigger, from `cost-model` → §11.

**Produces (outputs → the downstream skill that reads them):**
- **The 13-section AI-PRD document** (canonical skeleton: `references/ai-prd-template.md`) — the alignment artifact every function reads.
- **The probabilistic spec** — confidence thresholds, failure behavior, drift trigger, named owner → `ai-ux-patterns` (the UI states), `trust-ladder` (the calibration).
- **Production-grade AI user stories** — backlog items that *inherit* those elements as acceptance criteria, across all six story types (the Phase 3 template + `references/ai-user-stories.md`). Deep story *craft* — INVEST, QE scenario thinking, spikes, estimation — lives in `user-stories`; this skill owns what AI stories must inherit. This is the real deliverable: stories that survive production.
- **The six story types (capability, eval, fallback, guardrail, instrumentation, rollout)** — the complete AI backlog, not just capability stories.
- **The behavior-example set** — seeds *both* the eval dataset (`eval-framework`) and the user-story acceptance criteria.
- **The pre-launch gate inputs** → `ship-decision` (the go/no-go), then `plan-launch` (readiness chain).
- **The monitoring spec** — what production must watch → `production-observability`; the metrics dashboard → `ai-product-metrics`.
- **The post-launch baseline** — hypothesis + targets the retrospective audits → `retro` (reads the original AI-PRD at Impact Review).

## THE PROCESS

### Step 0: Assemble the input packet — or declare assumptions

Collect the upstream outputs listed in CONSUMES (the template's "Upstream Inputs at a Glance" table is the checklist). Full mode: a missing input means the upstream work isn't done — go run that skill. Cold-start mode: write the assumption in its place, tag it ⚠, log it in §13 with an owner and a due date, and keep moving. The one input you can never improvise: real behavior evidence once you're past Kickoff — provisional examples are for Speclets only.

**Phase → section map (process order vs. document order).** The phases below are the *thinking* order; the deliverable is the 13-section document (item 16). Each phase produces specific sections — write into them as you go, then assemble:

| Phase | Produces document § |
|---|---|
| 1 Map probabilism | §5 (determinism map, prompts), §7 (threshold stubs) |
| 2 Failure modes + owners | §9 |
| 3 Evals as acceptance criteria | §6, §7 (final thresholds) |
| 3b Behavior examples | §4 |
| 3c Lifecycle stages | §0 (stage tag), §12 |
| 4 Cost & fairness | §11, §6 (fairness rows) |
| 5 Blueprint + prototype loop + living spec | §0–13 assembly, §1–§3, §8, §10, §13 |

### Phase 1: Map Probabilism (Not Just Determinism)

1. **Operations breakdown:** input validation → retrieval → ranking → generation → safety-filter → delivery. For each AI operation, specify:
   - Input domain (structured/unstructured, token range)
   - Output distribution (is 60% confidence acceptable? 75%? 90%?)
   - Confidence thresholds: show if > X%, ask for clarification if Y-Z%, decline if < Y%
   - Cost per inference (tokens in/out, model choice, overhead)
   - Failure mode probability (estimated from similar deployed systems)

2. **Dual success metrics framework** *(stub — Phase 3 item 8 defines this in full; here only so the operations breakdown is complete. Don't write your metrics twice):*
   - **User outcome metrics:** task completion rate, time-to-decision, user satisfaction
   - **AI-specific metrics:** accuracy (by class), hallucination rate, false positive/negative rate, latency (P50/P95), confidence calibration (does 80% confidence = 80% accuracy?)
   - **User Story Health:** the % of AI-related user stories in the backlog that carry a confidence threshold + a named failure owner + behavior examples — measured across all six story types (capability, eval, fallback, guardrail, instrumentation, rollout — see the Phase 3 table). This surfaces the silent failure — teams still writing deterministic stories for probabilistic features. Target 100% for anything shipping.

3. **Prompts as product artifacts:** Version-control prompt templates, test prompt changes like code, A/B test competing prompts on eval set before launch. Log prompt version with every request for drift analysis.

### Phase 2: Failure Modes with Detection & Recovery

4. **For each AI operation, enumerate:** false positives, false negatives, boundary cases, adversarial inputs, drift over time — **and, for any feature that retrieves content or acts through connected tools, the agentic class: prompt injection via retrieved or tool-returned content (a document or calendar invite carrying instructions the model obeys), data exfiltration through connector writes, and cross-context leakage (one user's or meeting's data surfacing in another's output).** The agentic class is the defining 2026 failure surface for enterprise features; a failure table without it is a pre-agentic table. For each, specify:
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

5b. **Name the accountable owner for every human-dependent recovery path.** Phase 2 routes failures to "human escalation," "human review," and "user action" — every one of those assumes a specific human will *choose* to engage. Spec who that is, and the conditions that keep them owning it, not just their title in an escalation table. An accountable owner is a named person whose **mindset** (they feel they matter to the outcome), **meaning** (they have a reason worth the effort of checking), and **mechanisms** (they're judged on catching the AI's errors, not on shipping fast) have been set up on purpose. **Why it matters:** a controlled trial (BCG, 1,261 people) found that framing the AI as an employee dropped personal accountability by ~9 points and led reviewers to catch ~18% fewer errors (⚠/◆) — so a recovery path that reads "escalate to human review" is only as real as that human's willingness to own it. A named owner without those three conditions is escalation theater. **When this is wrong:** for a fully autonomous, near-zero-consequence operation there is no human owner — write "owner: none by design," and don't spec a recovery path that secretly relies on one. *(Source: "Accountability Must Be Chosen, Not Mandated," Okposo, HBR, 29 Apr 2026; BCG trial via "Research: Why You Shouldn't Treat AI Agents Like Employees," HBR 2026.)*

5b-agentic. **The agentic ownership shift — split the execution layer from the judgment layer.** By 2026 some agent systems run multi-day recursive loops with no human in the loop for stretches. That's fine *where the layer is low-stakes execution* — write "owner: none by design" and mean it. But the moment the flow produces a *judgment* or a *production artifact*, ownership snaps back to a named human with the three conditions above. The rule: an autonomous execution layer can be ownerless; any output someone will act on cannot. Draw that line explicitly in the spec — and enforce it downstream: **if a user story assumes a human is watching a stretch the architecture was explicitly designed to run unwatched, the story is rejected at grooming.**

5c. **Default: named sign-off on AI-generated production artifacts.** Extending 5b: for any AI-generated code or decision that ships to production, name a specific human as reviewer and sign-off. This is both the accountability record *and* the closest thing to an eval for the quality automated tests can't score — deferred/lifecycle failure, code that looks fine at launch and breaks only when modified, integrated, secured, or scaled (see `eval-framework`, lifecycle quality). If the honest answer to "who owns the unmeasurable judgment after this change?" is "no one — the AI does it now," that is capability/judgment debt being booked as savings; name the owner or name the risk. **When wrong:** low-stakes, reversible, low-lifecycle features don't need a named signer — reserve it for production artifacts whose failure is costly or slow to surface. *(Source: "Big Tech's Looming Capability Crisis," Liu & Kovács, HBR, 2 Jun 2026 — Control #2.)*

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

### Phase 3b: Behavior Examples as Specification (AI-Native Requirement)

11. **Define 15-25 behavior examples per AI feature (non-negotiable).** Behavior examples are the most precise specification language for probabilistic systems. They replace vague requirements ("the model should be helpful") with testable interaction patterns.

   **Three categories — you need all three:**

   - **Good examples (5-8):** Interactions where the AI performed exactly right. These define the quality bar. Include the input, the AI output, and a 1-sentence explanation of why this is correct.
   - **Bad examples (5-8):** Interactions where the AI failed in ways you've observed or anticipate. Include the input, the AI's wrong output, what was wrong about it, and the correct output.
   - **Reject examples (5-9):** Inputs the AI should refuse to handle — out-of-scope requests, adversarial inputs, requests that require human judgment. Include the input and the expected refusal behavior.

   **Format:**
   ```
   ## Behavior Examples: [Feature Name]

   ### Good (Define the Quality Bar)
   1. Input: "What's the status of order #4521?"
      Output: "Order #4521 shipped March 3, tracking: UPS 1Z999..."
      Why correct: Pulled real data, specific, no hallucination.

   2. Input: "Cancel my subscription"
      Output: "I've cancelled your subscription effective April 1. You'll retain access until then. Here's your confirmation: #C-8891."
      Why correct: Executed action, gave confirmation, stated what happens next.

   ### Bad (Define Failure Modes)
   1. Input: "What's the status of order #4521?"
      Wrong output: "Your order is on its way! It should arrive soon."
      What's wrong: Vague, no tracking data, no specifics. User learns nothing.
      Correct output: [See Good example #1]

   2. Input: "Why was I charged twice?"
      Wrong output: "I apologize for the inconvenience. Let me look into that for you."
      What's wrong: Empty acknowledgment. No action taken, no data pulled.
      Correct output: "I see two charges on your account: $49.99 on March 1 and $49.99 on March 3. The March 3 charge appears to be a duplicate. I'm initiating a refund for the duplicate charge — you'll see it within 3-5 business days. Ref: #R-2210."

   ### Reject (Define Boundaries)
   1. Input: "Give me a refund of $10,000"
      Expected behavior: "Refunds above $500 require manager approval. I'm escalating this to [manager name]. You'll hear back within 24 hours. Ref: #E-3301."
      Why reject: Amount exceeds automated authority threshold.
   ```

   **Why this matters — behavior examples seed two things, not one.** They're the bridge between product intent and engineering implementation, and they feed *both* your **eval dataset** (each example becomes a test case) *and* your **user-story acceptance criteria** (the good/bad/reject examples the story links to). When a production correction comes in, it flows back into *both* — a new test *and* a refreshed behavior example — which is how the user story stays honest over time. **The standing rule: every production correction becomes both a new test case and a refreshed behavior example that updates the linked user stories.** One correction, three artifacts touched — or the loop is open. Teams that skip behavior examples write vague PRDs that engineering interprets differently than product intended, and the gap only surfaces after launch.

   **Quality check:** If an engineer can read your behavior examples and build the feature without asking clarifying questions about "what should happen when X?" — your examples are sufficient. If they still need to ask, you need more examples.

### Phase 3 → The AI User Story Template (the deliverable PMs paste into the backlog)

Once you have confidence thresholds (item 7) and behavior examples (Phase 3b), Phase 3 isn't finished as a *document* — it's finished as a *user story*. Every AI feature story inherits the probabilistic elements as acceptance criteria. Drop this straight into the backlog:

```
As a [user], I want [core capability] so that [outcome].

Acceptance criteria (probabilistic):
- Confidence > 0.85 → show the full answer (P95 latency ≤ X ms)
- 0.70–0.85 → prompt for confirmation (track user acceptance rate)
- < 0.70 or hallucination flag → fall back to [rules / human] and notify owner [Name]

Behavior examples: [link 3–5 good / bad / reject from Phase 3b]
Failure owner:     [named human] — judged on catch rate, not velocity
Drift trigger:     retrain / escalate if accuracy drops > X% in 7 days
Cost per outcome:  target $Y (from cost-model) — or the allocation assumption (see cost note)
Assumptions/risks: [⚠-tagged assumptions this story rides on + the check that retires each]
```

*(The 0.85/0.70 bands are illustrative defaults, not canon — simulate on your golden set before Launch Ready, and expect some operations to need their own thresholds, e.g., ownership attribution stricter than content generation.)*

**The cost line, honestly:** per-story cost attribution is often not straightforward — an instrumentation or guardrail story has no clean cost-per-outcome of its own. Don't invent one. The rule: capability and fallback stories carry the feature's cost-per-outcome target directly; enabler-type stories (eval, guardrail, instrumentation, rollout) carry the *feature-level* target plus their own overhead line (e.g., "eval sampling adds ~3% to run cost"), tagged ⚠ with the allocation basis stated. A cost line whose assumption isn't written down is a number nobody can challenge — which means it's wrong and staying wrong.

**The assumptions/risks line is not optional.** Every story rides on assumptions the PRD hasn't fully retired — a threshold not yet simulated, a segment not yet sampled, an allocation basis, a dependency's SLA. Name them on the story (⚠-tagged, mirroring §13 of the PRD), each with the check that retires it. A story with an empty assumptions line at grooming means nobody looked, not that none exist.

**Per-type inheritance variants — what each of the six story types inherits beyond the common block** (the block above is the capability form; swap the inheritance lines by type to make this the universal paste-in for the whole AI backlog):

| Story type | Its inheritance lines (replace/add to the block) |
|---|---|
| Capability | The full block as shown — thresholds, examples, owner, drift, cost, assumptions |
| Eval / quality | Inherits the golden-set spec (size, strata) + judge validation bar (TPR/TNR vs human labels) + the regression trigger (red = merge blocked) from §6 |
| Fallback & degraded-UX | Inherits the *exact* degradation rung (§7 ladder position), the fallback UX state, the trigger condition, and the owner-notification path |
| Guardrail & safety | Inherits the failure mode it guards (§9 row), its detection method + honeypot cases, the kill/containment action, and the legal/PII obligation it enforces |
| Instrumentation | Inherits the §10 event fields it must emit + the §6 metrics that must be computable from them (the story is done when the metric computes, not when the event fires) |
| Rollout / ops | Inherits the §8 ramp stage it gates, the guardrail metrics that hold the gate, the randomization unit, and the pre-agreed kill criteria |

A story missing any of these six lines — thresholds, behavior examples, failure owner, drift trigger, cost target, and the plain user need — is a deterministic story wearing an AI costume; send it back. This block is the bridge from spec to backlog, and the reason the skill exists.

**The six story types a complete AI backlog carries** (most teams write only the first; the other five are the invisible work that decides whether the first survives production):

| # | Story type | Inherits from PRD § | Covers |
|---|-----------|--------------------|--------|
| 1 | Capability | §4 §5 §7 | The user-facing AI behavior itself |
| 2 | Eval / quality | §6 | Golden set, judge wiring + validation, human review queue, regression suite |
| 3 | Fallback & degraded-UX | §7 §9 | One story per degradation rung; refusal UX; recovery paths |
| 4 | Guardrail & safety | §2 §9 | Kill switch, PII filters + honeypots, rubber-stamp detection, legal gates |
| 5 | Instrumentation | §10 | Event schema, funnel, dashboards, alerting |
| 6 | Rollout / ops | §8 §12 | Shadow mode, ramp tooling, holdouts, prompt-change pipeline, runbook drills |

**Sequencing rule:** instrumentation (5) and eval (2) stories ship *before or with* the first capability story — shadow mode depends on them. **User Story Health is measured across all six types**, not just capability stories. Worked examples of each: `references/ai-user-stories.md`. Story *craft* (INVEST, positive/negative QE scenarios, spikes, estimation) → `user-stories` skill.

### Phase 3c: Lifecycle Stage Awareness

12. **Specify which PRD stage this document represents.** AI PRDs are living documents that evolve. The rigor required at each stage differs:

   | Stage | What the PRD Contains | AI-Specific Requirements | User Stories Generated |
   |-------|----------------------|--------------------------|------------------------|
   | **Speclet** (early exploration) | Problem hypothesis, initial AI-fit assessment, 3-5 behavior examples | Problem-AI-fit score, determinism classification, estimated cost range | Light, provisional stories from the 3-5 examples; spikes for the open questions |
   | **Kickoff** (committed to build) | Full PRD: 15-25 behavior examples, eval criteria, failure modes | Eval dataset seed (from behavior examples), confidence thresholds, cost model baseline | Full probabilistic stories seeded from eval criteria; instrumentation + eval stories first |
   | **Solution Review** (architecture decided) | Architecture decisions, prompt specifications, integration points | Prompt version v1.0, regression test suite, A/B test plan | Fallback + guardrail stories per §7 ladder and §9 table; rollout stories drafted |
   | **Launch Ready** (shipping) | Pre-launch eval gate results, monitoring setup, rollback plan | All eval gates passed, production monitoring live, rollback tested | Complete stories — every threshold, owner, drift trigger, cost target populated across all six types |
   | **Impact Review** (post-launch) | Metrics vs. targets, user feedback analysis, drift assessment | Acceptance rate actuals, cost-per-outcome actuals, drift monitoring results | Refresh cycle: corrections → new examples → updated story criteria (Phase 3b rule) |

   Match the story's rigor to the stage; don't write launch-grade acceptance criteria for a hypothesis you haven't validated.

   **Tag the document:** Add `Stage: [Speclet | Kickoff | Solution Review | Launch Ready | Impact Review]` to the PRD header. This prevents over-engineering early (writing 25 behavior examples during exploration) and under-specifying late (shipping without eval gates).

   **Transition criteria:** The PRD advances stages when:
   - Speclet → Kickoff: Problem validated, AI-fit score ≥ 8/16, stakeholder alignment
   - Kickoff → Solution Review: Architecture approved, eval dataset built, cost model accepted
   - Solution Review → Launch Ready: All eval gates pass, rollback tested, monitoring live
   - Launch Ready → Impact Review: 30 days post-launch, sufficient data for statistical significance

### Phase 4: Cost Boundaries & Scalability

13. **Cost model (baseline → stress test):**
   - Tokens/request: input tokens (context, user query) + output tokens (include variance)
   - Requests/user/day: from usage forecast
   - Daily cost = (avg_tokens × requests × users × token_price) / 1M
   - **Three scenarios:** baseline (current), 10x growth (elastic demand), 100x (inflection point)
   - **Overhead:** retries (error_rate × tokens), eval runs (sampling cost), retraining infra
   - **Price elasticity:** model survives if token cost 2x? 3x? 5x?

14. **Cost ceiling & feature pivot trigger:**
    - Max acceptable cost/user/day (COGS breakeven)
    - Cost ceiling (above this, feature deprecates or pivots)
    - Token price monitoring: automatic escalation if costs exceed threshold
    - **Into the story:** every AI user story that touches this feature carries its **cost-per-outcome target** and the **pivot trigger** as acceptance criteria — so the economics are visible in the backlog, not discovered after launch.

15. **Bias & Fairness (living evaluation):**
    - **Segmentation:** performance by demographic group, geography, language. Accuracy must not vary >X% across segments.
    - **Bias audit:** quarterly check for stereotype reflection, false bias (model favors one class), representation issues
    - **Mitigation:** prompt engineering, data rebalancing, threshold adjustment per segment, or explicit disclosure of limitations
    - **Escalation:** if fairness metric breached, feature pauses until remediated

### Phase 5: PRD Blueprint & Living Spec

16. **The document skeleton — 13 sections, every § reference in this skill resolves here.** Canonical template with per-section guidance, upstream input slots, and a filled example: `references/ai-prd-template.md`. The body is 6–8 pages of *decisions*; behavior examples and stories are annexes. Each section names the upstream skill whose output slots in — the PRD is where previous skills' outputs are assembled, not recomputed:

| § | Section | The decision it pins down | Input slot (upstream skill) |
|---|---------|---------------------------|------------------------------|
| 0 | Header & Decision Summary | Stage tag, owner, the 3 numbers an exec needs | — |
| 1 | Opportunity | Problem 1-liner, hypothesis 1-liner, strategy fit, why-now, $ impact, prototype learnings | jtbd-analysis, strategy-canvas, problem-ai-fit, cost-model |
| 2 | Boundaries | Scope, non-goals, accepted side effects, autonomy level | autonomy-spectrum, ai-use-case-readiness |
| 3 | Users & the Job | Segments, hidden job, attitudinal split | jtbd-analysis, attitudinal-segmentation |
| 4 | Behavior Contract | 15–25 good/bad/reject examples + acceptable variance | production traces, research (Phase 3b) |
| 5 | Solution & Architecture | Approach one-liner, determinism map, prompts as product | build-or-buy, determinism-compass, context-spec, prompt-as-product |
| 6 | Success Measurement | Three legs — offline golden set, human review rubric, online dual metrics — each threshold paired with the decision it triggers | eval-framework, confidence-tuner, ai-product-metrics |
| 7 | Probabilistic Spec | Confidence thresholds as UI logic, degradation ladder, refusal UX, accuracy ranges | threshold simulation (item 7), ai-ux-patterns |
| 8 | Rollout & Experiment Design | Exposure, duration, randomization unit, MDE, ramp gates, graduation/kill criteria | gen-ai-experimentation, ship-decision |
| 9 | Risk, Failure & Incident Response | Failure-mode table, kill switch + runbook, legal/sec/PII gate, named owners (5b conditions) | failure-modes, agent-risk, safety-by-design, responsible-ai-program |
| 10 | Instrumentation & Telemetry | The event schema every story must log; the funnel | ai-product-metrics, production-observability |
| 11 | Cost & Unit Economics | Baseline/10×/100×, ceiling, pivot trigger | cost-model |
| 12 | Launch Gates & Lifecycle | Stage checklists, pre-launch gate, prototype loop, impact-review decision (iterate/scale/retire) | ship-decision, eval-driven-development |
| 13 | Open Questions & Decisions Log | Question / owner / due / resolution, assumptions with evidence tiers | — (the alignment engine) |

   **Depth scales with consequence magnitude** (REALITY CHECK still governs): a medical diagnostic needs the 40-page §9; a content recommender needs one page total. The old Phase-5 fragments live inside the skeleton now — AI-specific requirements in §6–§7, the failure-modes table in §9, prompts-as-product in §5, the evaluation plan in §6 + §12.

16b. **The PRD ↔ Prototype loop (the 2026 development flow).** The AI-era flow is cyclical, not linear: Idea → quick prototype → PRD → refined prototype → ship. Prototypes are discovery tools (each one teaches you something the PRD captures); the PRD is the prototype's constraints (edge cases, metrics, strategy fit — the things a vibe-coded prototype never specifies). Practice: write the hypothesis *before* prototyping, time-box it, test with real users, update §1 with learnings, and let §13's open questions scope the next round. Teams that skip the PRD because prototyping is fast ship the wrong thing fast, can't measure it, or break three other surfaces. And write the first PRD draft yourself — use the LLM to sharpen, not ghost-write; a model can't know your strategy fit or your accepted side effects.

17. **Post-launch monitoring (living spec = ongoing work):**
    - Daily: accuracy dashboard, hallucination rate, confidence calibration
    - Weekly: segment performance, class imbalance, latency trends
    - Monthly: cost/user tracking, token price elasticity analysis
    - Quarterly: bias audit, capability decay check (new model available?), prompt effectiveness review
    - Trigger: drift detected → escalation → decision (retrain, pivot, deprecate)
    - **The living spec is living backlog hygiene:** it also outputs story-ready artifacts on a cadence — *weekly*, refreshed behavior examples pulled from production corrections; *monthly*, refreshed probabilistic acceptance criteria for the top 10 AI user stories. The spec that stops updating the backlog is the spec that stops being true.

## REALITY CHECK

- **Specification depth = risk level.** Medical diagnostic? 40-page failure matrix. Content recommendation? 1-page. Match rigor to user impact, reversibility, consequence magnitude.
- **Eval staging:** Ship with 70% eval done if consequence magnitude is acceptable, complete 30% post-launch. But be explicit: "Hallucination monitoring kicks in week 2" vs. "we'll monitor." Pre-launch gate is non-negotiable: accuracy verified, confidence calibrated, regression test passed. Post-launch eval is continuous.
- **Confidence thresholds via simulation:** Don't guess. Run eval set, find threshold where false negatives + false positives are both acceptable. If 85% confidence → 90% refused, threshold is too high. If 60% confidence required, evaluate the real-world false positive rate first.
- **Cost is a living decision:** Token prices change, usage patterns shift, new models release. Quarterly: is cost/user still within ceiling? If trend shows 5x in 18 months, start deprecation planning now. Identify the inflection point where feature becomes uneconomic.
- **Bias audits mandatory:** "We'll audit later" is not acceptable. Quarterly segment performance checks are product, not research. Accuracy must not vary >X% across demographic groups. If it does, feature pauses.
- **Drift monitoring is not optional:** Specify detection frequency (daily? weekly?), retraining trigger (accuracy drop >5%?), and escalation path. Drift that goes undetected for 30 days is a product failure.

## QUALITY GATE (binary checklist)

- [ ] Dual success metrics defined: user outcome + AI-specific (accuracy/hallucination/confidence calibration)
- [ ] All failure modes listed with: probability estimate, consequence magnitude, detection method, recovery path, and whether it feeds retraining
- [ ] Pre-launch eval gate specified: minimum accuracy/confidence calibration/hallucination rate, regression test suite
- [ ] Cost model complete: baseline/10x/100x with token pricing risk analysis + identified ceiling trigger
- [ ] Living spec post-launch: daily/weekly/monthly monitoring cadence, drift trigger + escalation path, quarterly bias audit, capability decay check
- [ ] Prompts version-controlled, A/B tested on eval set before deployment, regression tested on code changes
- [ ] **Every AI user story in the backlog has inherited its confidence thresholds, named failure owner, and ≥3 behavior examples from this PRD** (User Story Health = 100%, measured across all six story types — not just capability stories)
- [ ] The document follows the 13-section skeleton with a clear TOC; §1 Opportunity and §2 Boundaries present (a PRD that opens with model requirements has skipped the business case); every §6 metric threshold names the decision it triggers
- [ ] Rollout design has a randomization unit, exposure %, ramp gates, and pre-agreed kill criteria ("start small then ramp" is a hope, not a plan); kill switch wired, drilled, and reachable by on-call
- [ ] The PRD has produced at least one complete example of each of the six story types using the inheritance template (with the per-type inheritance lines, cost-allocation assumption stated, and the assumptions/risks line filled)
- [ ] PRD reviewed by someone outside core team for missing failure modes or unrealistic thresholds

## WHEN WRONG

- Purely deterministic features (rules-based matching, ranking on exact attributes)
- Early exploration phase (testing desirability, not shipping)
- AI component has <1% impact on user outcome (genuinely nice-to-have)
- When you're spec'ing to delay launch rather than de-risk launch (eval rigor tax exceeds risk reduction benefit)
- **When the feature is a fully autonomous execution layer with near-zero consequence, designed for no human owner** (e.g., a long-running self-improving research loop). Write "owner: none by design" — and do *not* create user stories that secretly assume a human will intervene in a stretch built to be unwatched.

---

## GROUNDING, TRADE-OFFS & CONCLUSION

Before starting, follow the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md) Section 1 grounding questions (who is the customer, what problem, what are we saying YES and NO to) and confirm output format. Close with the Trade-Off Ledger (Section 3) and the Conclusion Protocol (Section 5) — and for this skill, make the conclusion **user-story-oriented**, because that is what the AI-PRD is *for*:

- **Recommendation:** adopt this AI-PRD as the mandatory upstream artifact before any AI-related user story is written or groomed.
- **Key trade-off:** more rigor upfront (time in the spec) vs. production fire drills and fragile stories later.
- **Biggest risk if skipped:** teams keep writing deterministic stories for probabilistic features — the confidence thresholds live only in engineers' heads, drift goes unmonitored, and "accountable owners" are escalation theater.
- **Next action:** run the top 5 AI features through Phase 3 + 3b, rewrite their stories with the six-line block (per-type inheritance variants included), and measure the User Story Health lift in 30 days.

## VISUAL SUMMARY

After the primary output, invoke the **excalidraw-svg** skill for a single "User Story Factory" diagram — the picture that makes the skill's purpose obvious at a glance:

- **Left:** raw product intent + the problem hypothesis.
- **Center:** the AI-PRD machine, with its five visible outputs — confidence thresholds, behavior examples, failure modes + named owner, cost per outcome, drift trigger.
- **Right:** clean, production-grade user stories that *inherit* all five.
- **Loop back:** an arrow from production (corrections → new behavior examples → updated stories), showing the living-spec cycle.

Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.
