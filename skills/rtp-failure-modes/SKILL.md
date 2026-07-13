---
name: failure-modes
description: "What will go wrong with this AI feature, what does each failure cost, and what happens to the user when it does? Maps the full failure surface (six kinds of hallucination, injection, cascade, silent decay), prices each by cost and how long it stays invisible, then designs the response: honest uncertainty language, correction paths, when the AI should refuse, and the fallback chain when it breaks. Use when speccing an AI feature, designing production monitoring, running a pre-launch failure audit, or writing failure acceptance criteria. Do NOT use to decide whether to use AI at all (that's problem-ai-fit), or for purely deterministic systems. Pairs with: stress-test (the load/cost/latency surface), feedback-triage (routes live failures to their fix team using this taxonomy), ai-ux-patterns (how failure looks to the user), trust-ladder (repairing trust after a visible miss), agent-risk (kill-switch when failure cascades). Triggers: 'what could go wrong', 'failure audit', 'how should it fail'."
imports: [stress-test]
---

# Failure Modes — Diagnostic & Design Framework

**The objective:** know what will go wrong before users find out, and design the product's behavior for those moments on purpose — for the PM speccing an AI feature or auditing one before launch.

## The one idea

Every demo shows success. Every design review walks the ideal flow. Every user story describes winning. So the PM writes one line about failure — "show error message" — and moves on. That is designing a car with no seatbelts because you plan to only drive in good weather.

Here is why that's a category error for AI specifically: **in a probabilistic product, how you fail IS the product experience for a meaningful slice of every single day.** A model that's right 92% of the time is *wrong, in front of a user, thousands of times a day.* The happy path is not the product; the product is the happy path *plus* what happens the other 8% of the time — and that second half is usually left undesigned. This skill makes the failure surface a first-class design object: map what will go wrong, price each failure by its cost *and* how long it stays invisible, then design the response.

And the single most important thing to internalize is which failure to fear. It is not errors — it's **confident wrong.** When the model is wrong and *says* "I'm not sure," the user verifies and you're fine. When the model is wrong and says it with full confidence, the user acts on it — because nothing in the experience prompted a check. In a chain of agents, one confidently-wrong step poisons every step downstream. Prioritize by **failure cost × how long it stays invisible**, never by frequency alone: a rare catastrophic confident-wrong outweighs a flood of harmless refusals.

## How to use this skill

1. **Identify** the failure taxonomy for this feature (the six hallucination subtypes, injection, cascade, silent decay). (Phase 1.)
2. **Quantify** each by detection latency and annual cost, and prioritize by cost × invisibility. (Phase 2.)
3. **Design the response** — failure UX, the refusal boundary, the graceful-degradation fallback chain, and (for multi-agent) verification gates against cascades. (Phases 3–5.)
Then write failure *acceptance criteria* into every user story — "when the AI is wrong, the user can X; when uncertain, the system does Y."

## KEY TERMS (plain language)

- **Failure mode** — one specific way the system gets things wrong (invents a fact, returns stale data, refuses a fair request); named so it can be detected and designed for.
- **Hallucination** — the model states something false as if true; split below into six subtypes because each is caught differently.
- **Confident wrong** — false output delivered with full certainty; the most dangerous mode, because nothing prompts the user to check.
- **Detection latency** — how long a failure stays invisible: immediate (user sees it), delayed (days), silent (months, or never without an audit).
- **Cost asymmetry** — failures aren't equal; a rare catastrophic miss outweighs frequent harmless ones, so budget by annual cost, not frequency.
- **Cascade** — in a chain of agents, one step's bad output becomes the next step's trusted input, and errors compound instead of cancel.
- **Graceful degradation** — the fallback ladder when AI fails: cached answer → simpler model → fixed rules → human → honest error; each step trades capability for reliability.
- **Refusal boundary** — the confidence line below which the AI says "I don't know" instead of guessing; a product decision tuned empirically, not a technical constant.
- **Circuit breaker** — an automatic trip that stops a failing step from dragging down the whole pipeline.

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../../../UNIVERSAL-SKILL-PROTOCOL.md). Answer three questions first: (1) who's the user and what stakes do they face (a doctor acting on output ≠ a knowledge worker drafting an email — this changes which failures matter and how much UX they deserve)? (2) what does the output feed into next (a final recommendation, an input to another system, or raw material the user edits — each has a different cascade and recovery profile)? (3) do you have telemetry (if yes, read the error rates before theorizing; if no, the monitoring design is this session's most urgent deliverable). Then pick depth: **quick audit** (top-5 failure modes + annual risk budget + failure UX, ~20 min) or **full registry** (complete taxonomy, latency map, cascade paths, mitigation budget, monitoring, failure UX, degradation hierarchy, acceptance criteria, 2–4 hrs). *If the real question is "should we use AI at all?", that's `problem-ai-fit` — this skill assumes the decision is made.*

## THE TRAP

- **Accuracy mono-focus** — obsessing over accuracy while ignoring latency, cost, drift. A 95%-accurate model at 4s loses users faster than an 88%-accurate one at 500ms. Accuracy is one of six dimensions.
- **Happy-path monopoly** — the seatbelt problem above.
- **Confident wrong** — the deadliest mode; when it's wrong *and* certain, the user acts on it.
- **Blame-shift** — "try rephrasing your question" puts the failure on the user; trust erodes because the AI dodged responsibility. Compare: "I'm not confident here — verify before acting." Same failure, opposite trust impact.
- **Confidence theater** — "87% confidence" is noise unless it maps to an action: "confident — no check needed" vs. "review this" vs. "too uncertain — ask a human." Actionable language beats false precision.

## PHASE 1 — IDENTIFY: the failure taxonomy

| Failure type | Manifestation | Detectability | Cost asymmetry |
|---|---|---|---|
| Hallucination: **fabrication** | pure invention (facts never existed) | medium (needs external check) | high (user trusts false info) |
| Hallucination: **conflation** | correct facts, wrong attribution/context | hard (needs domain knowledge) | critical (undetectable) |
| Hallucination: **extrapolation** | extends a true pattern past the data | hard (sounds plausible) | high (false confidence) |
| Hallucination: **temporal confusion** | reports 2023 data as current | medium | high in fast-moving domains |
| Hallucination: **over-generalization** | applies a specific fact broadly | medium | medium-high |
| Hallucination: **misattribution** | real quote/fact, wrong source | hard (needs citation check) | critical in legal/academic |
| **Confident wrong** | high certainty + false | critical (no uncertainty signal) | extreme (highest user harm) |
| **Prompt injection** | external input hijacks behavior | hard (zero-day potential) | extreme (jailbreak, data theft) |
| **Retrieval failure** | wrong doc; bad synthesis | medium (verify vs. source) | high in confidential/legal |
| **Refusal** | legitimate request declined | immediate | low per instance, high if systematic |
| **Latency / cost explosion** | too slow / token budget blown | immediate / delayed (billing) | low / high (feature disabled) |
| **Cascade: sub-agent failure** | one agent's bad output propagates | hard (buried in the chain) | extreme (compounding) |
| **Silent degradation** | quality drifts down, no error signal | critical (invisible) | extreme (months of bad output) |

## PHASE 2 — QUANTIFY: detection latency × cost

**Detection latency** — how long until a silent failure is noticed: **immediate** (seconds), **delayed** (days/weeks — drift, cost creep), **silent** (months or never without an audit), **discovered externally** (a complaint, a lawsuit, a news article — reputational). Every *silent* failure needs an owned monitoring mechanism before launch.

**Prioritize by annual risk, not frequency** (numbers below are illustrative — a worked *shape*, not research; build your own from telemetry): a 0.5% confident-wrong at $5K/incident ($250K/yr) outranks a 3% fabrication at $500 ($150K/yr) which outranks a 0.01% injection at $50K ($50K/yr). The structure is the point: `frequency × cost per incident × annual volume`, compared against prevention cost — invest when prevention is <10% of annual risk, reassess when it's >50%.

## PHASE 3 — DESIGN: failure UX & response modes

For each output, answer *"what happens when this is wrong?"* — wrong-and-noticed-now → correction path; wrong-and-noticed-later → recovery + trust repair; wrong-and-never-noticed → verification mechanism; wrong-and-causes-a-downstream-action → undo/reversal.

**Pick a response mode per failure type:** **graceful degradation** (partial result + explicit uncertainty — best for non-critical, early-stage); **explicit failure** (refuse, explain, offer alternatives — best for high-stakes, where silence is worse than refusal); **silent failure** (output with a confidence signal but no verification path — acceptable only for low-stakes experimentation where users know they're testing). **Never ship confident-wrong** — if you can't detect or prevent it, you've *chosen* silent failure; own that choice.

**Failure UX patterns:** progressive confidence *inline* ("fairly confident, but verify the date" beats a generic disclaimer); inline correction (edit in place, train on the fix); explanation on failure ("no recent pricing — our KB was last updated in January" beats "no results"); one-click undo (≥30s); dead-easy feedback (route bad outputs to the improvement queue); a visible degraded-mode indicator.

**Refusal boundary:** what confidence triggers "I don't know"? what does refusal look like? is refusal better than a low-confidence answer (usually yes for high-stakes)? *The refusal paradox:* too many refusals = useless, too few = dangerous — it's a product decision, tuned empirically. (Design the confidence *signals* themselves with `confidence-tuner`.)

## PHASE 4 — GRACEFUL DEGRADATION HIERARCHY

The fallback chain when AI fails, each step trading capability for reliability: **cache** (last known good — fast, stale) → **simpler model** (cheaper, less capable) → **rules** (deterministic, no surprises) → **human escalation** (slow, high trust) → **error state** (last resort). *Worked example — AI support agent:* cache (exact match on 50+ historical, 50ms, "from our knowledge base") → simpler model (low complexity, 200ms) → rules (confidence <60%, includes escalation link) → human ("creating a support ticket") → error ("here's how to reach us directly"). Show the user when they're in a fallback — transparency builds trust even in failure.

## PHASE 5 — CASCADES IN MULTI-AGENT SYSTEMS

When agents chain, failures compound in ways single-agent systems never see. *The math:* Agent A at 95% hands Agent B 5% garbage; B can't tell garbage from valid text, treats it as ground truth, and its accuracy on garbage input collapses to ~20% — so ~1% of end-to-end paths are *confident-wrong*, your worst mode. **Patterns → mitigations:** upstream hallucination propagation → a verification gate between agents; coordination drift → shared-state monitoring; tool-call cascade → a circuit breaker per tool; context saturation → compaction at each handoff; evaluator hallucination → hybrid eval (LLM + code-based graders). **Design:** circuit breaker (3 fails/10 min → fallback), isolation (a handoff contract with fallback input types), checkpoint/rollback before each handoff, per-step timeouts, and error attribution logging (agent → operation → latency → failure type → recovery).

**Recovery cost spectrum** — not all failures cost the same to fix: **seconds** (wrong autocomplete → undo) · **minutes-hours** (bad email/code → correction + apology) · **days-weeks** (bulk records wrong → audit trail + escalation) · **permanent** (PII leaked, safety-critical, trust destroyed → *prevention only, no recovery exists*). Design by user type: power users tolerate errors and recover fast (design for speed); casual users don't know when the AI is wrong (design for safety — prefer "I'm not sure"); enterprise admins affect thousands (design for confirmation + audit + reversibility).

## PRODUCTION CASE — the cascade no one saw coming

*Anonymized, B2B SaaS, 2024.* A 3-agent pipeline (Analyst pulls data → Summarizer synthesizes → Reporter formats an exec brief). The Analyst's warehouse partition stopped refreshing but returned data *with no error signal.* The Summarizer summarized stale data with full confidence; the Reporter formatted a polished brief. **Undetected for 19 days; 34 enterprise customers got briefs; 3 made budget decisions on stale metrics.** Fixes: a freshness hard-stop (data >6h old), a cross-check (flag if data deviates >20% from prior period), a freshness timestamp on every output, and an end-to-end pipeline acceptance metric checked daily. **The lesson: structurally-valid output with no error code is invisible to agent-level monitoring — you need pipeline-level quality and freshness checks at every handoff.**

## DIAGNOSTIC QUESTIONS (design review)

- **Worst-case failure and its cost?** Not most likely — worst *plausible*. "A user takes [action] on [failure] and suffers [harm], [frequency], [$/incident]."
- **How long until we notice a silent failure?** Band each type immediate/delayed/silent; every silent one needs an owned monitor before launch.
- **Recoverable vs. permanent?** For the top 3: fastest path to making the user whole, and its cost. No answer = permanent = invest in prevention.
- **False-confidence vector?** Run accuracy against confidence scores; if accuracy <60% in the high-confidence bucket, that's your confident-wrong zone — fix before launch.
- **Cascade check?** Draw the agent chain; at each handoff, "could garbage pass through undetected?" If yes, add a verification gate.

## WHERE THIS SKILL MEETS THE REST OF YOUR STACK

Failure-modes is the **taxonomy home** — how AI breaks, and how to design for it. It composes with:

- **`rtp-stress-test`** *(import)* — the load/cost/latency/adversarial surface (the *technical* pre-mortem); this skill is the *failure-behavior* half.
- **`rtp-feedback-triage`** — routes *live* production failures to their fix team *using this taxonomy* (its sub-types are this skill's failure modes); triage routes, this designs.
- **`rtp-ai-ux-patterns`** — how each failure *looks* to the user (uncertainty ladder, error states); this decides the response, that renders it.
- **`rtp-confidence-tuner`** — designs the calibrated trust signals that make the refusal boundary and progressive-confidence UX actually work.
- **`rtp-trust-ladder`** — repairing trust after a visible miss (the recovery half of a failure).
- **`rtp-agent-risk`** — the kill-switch and proportionality when a cascade turns catastrophic.
- **`rtp-problem-ai-fit`** *(upstream)* — decides whether to use AI at all; this assumes yes.

## REALITY CHECK

- Not every failure needs mitigation — accept low-cost ones, but *document* the choice.
- The worst failures are the ones you don't know you have — invest in detection, not just prevention.
- Mitigations compound into a latency tax (guardrails + retrieval + post-hoc checks) — measure total cost.
- Over-warning creates fatigue — if every output has a disclaimer, users stop reading them; calibrate transparency to risk.
- Cascades are exponential (95% × 95% = 90.25%) — map yours.
- Hamel Husain: spend 60–80% of your time on error analysis and evaluation. Anthropic's eval-saturation point: when your eval catches 99%, the last 1% is where the catastrophic ones hide — refresh eval sets quarterly.

## QUALITY GATE

- [ ] Top-5 failure modes ranked by cost × (1/detectability)
- [ ] All six hallucination subtypes explicitly mapped
- [ ] Detection latency assigned to each (immediate/delayed/silent)
- [ ] Response mode chosen per mode, with justification
- [ ] Failure UX designed for each high-stakes output (confidence, correction, escalation)
- [ ] Refusal boundary defined with a specific threshold and reasoning
- [ ] Failure acceptance criteria written for every user story
- [ ] Graceful-degradation hierarchy mapped with triggers
- [ ] Cascade paths documented with verification gates (multi-agent)
- [ ] Monitoring designed for any failure with detection latency >1 hour
- [ ] Annual risk budget calculated for the top failures; escape hatch documented

## WHEN WRONG

- Truly sandboxed features that never touch external-facing output.
- Research prototypes with explicit "beta" messaging.
- Ship-to-learn is the priority AND detection/rollback is fast (<1 hr).
- When failure analysis becomes a delay tactic instead of a path to safer shipping.
- Deterministic components (rules-based error handling is a different discipline).
- When the real question is "use AI at all?" — that's `problem-ai-fit`.

## TRADE-OFF LEDGER

By making the failure surface a first-class design object, you bet that in a probabilistic product the cost of undesigned failure (confident-wrong acted on, silent decay shipped for months) dwarfs the design time. You give up velocity — a full registry is 2–4 hours, and mitigations add a latency tax. **Reversible?** The analysis is; a permanent failure (leaked PII, a safety incident) is a one-way door, which is exactly why you spend here. **The hidden trade:** the failure mode of *this* skill is over-mitigation — a disclaimer on everything, a refusal at every turn, until the product is useless; calibrate transparency and the refusal boundary to risk, don't max them. **Confidence: High** — how you fail is the product for a slice of every day. What would change it: a sandboxed, fast-rollback, low-stakes feature where shipping to learn wins.

## CONCLUSION

Follow the Conclusion Protocol ([Universal Skill Protocol](../../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 5): the recommendation ("the top unmitigated risk is [X], annual risk $[Y], prevention $[Z] → invest/accept/monitor"), the key trade-off (which response mode, accepting what to avoid what), the biggest risk (the failure mode you know least about + how you'll baseline it), and the next action (specific, owner, deadline). Frame it as a hypothesis: "we believe [monitoring] will catch [failure] because [mechanism]; we're wrong if [signal] within [timeframe]."

## VISUAL SUMMARY

After the primary output, invoke the **excalidraw-svg** skill for one visual: the failure taxonomy plotted on two axes — cost per incident (up) × detection latency (right) — so the top-right quadrant (expensive AND invisible: confident-wrong, silent degradation, cascade) is visibly the priority zone, with the graceful-degradation ladder drawn alongside as the response. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.
