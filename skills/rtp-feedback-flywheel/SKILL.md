---
name: feedback-flywheel
version: v1.1_latest
description: 'Turn what users do with your AI''s output into the thing that improves the AI, automatically, on a cadence, with owners. Most products collect feedback (thumbs, edits, regenerations) that sits in a database and never reaches the model; this designs the closed loop from signal to labeling to a measured model gain. Collection is easy and feels like progress. Closure is rare and is the actual moat, but ONLY if the loop''s inputs are yours alone. Use when designing feedback capture, auditing why collected feedback changes nothing, or bootstrapping before you have users. Do NOT use for one-shot/batch systems, under ~500 active users, or when annotation velocity is permanently <5% of collection. Pairs with: eval-framework + eval-driven-development (the fix→regression cycle lives there), moat-finder (anti-moat check), ai-product-metrics (signals worth logging), gossip-mode (informal-signal sibling). Triggers: ''feedback loop'', ''why does our feedback change nothing'', ''data flywheel''.'
imports: [first-principles, stress-test]
---

# Feedback Flywheel — The Diagnostic

**The objective:** close the distance between "we collect feedback" and "the product got better because of it" — for the PM whose feedback database is full and whose model hasn't moved.

## The one idea

Open your feedback database. It's full — thumbs-downs, user edits, regenerations, escalations, months of it. Now ask the question that matters: how much of it ever reached the model as a measured improvement? For most products the honest answer is *almost none* — a small fraction (10–20%, a practitioner rule of thumb ⚠) becomes training or eval input, and the rest just accumulates, unlabeled.

That gap is the whole idea. **Collection is easy and feels like progress; closure is rare and is the actual work** — and the actual moat. Logging a thumbs-down costs nothing and produces a satisfying number on a dashboard. Getting that signal *labeled, into an eval set, through an experiment, and out as a measured model gain* is a pipeline with owners and a cadence, and it almost never exists by default. Until it does, your data is **inventory, not leverage** — a warehouse of signal nobody is converting.

And here is the sharp edge most teams miss: a mature flywheel is one of the strongest moats in AI, **but only if the loop's inputs are yours alone** — your users' corrections on your traffic. Run the same loop on public signals every rival also ingests and it compounds you toward the industry *average*, not ahead of it. Worse, a flywheel fed only by common, easy cases builds an advantage the next frontier model erases for free; the corrections worth the most are the hard, rare ones only your usage produces. So the diagnostic isn't just "is the loop closed?" — it's "is the loop closed *on signal only you have?*"

## How to use this skill

1. **Rank the signal, then capture it** — corrections > explicit feedback > implicit behavior > acceptance; ~80% of signal should be zero-friction implicit. (SIGNAL & CAPTURE.)
2. **Fix the bottleneck — annotation velocity** — measure the % of feedback reaching the model per week; if labeling can't keep up with collection, that's the broken link, not capture. (ANNOTATION.)
3. **Close the loop on a cadence with owners, and check the moat condition** — weekly→quarterly pipeline; then place yourself on the 1–5 maturity curve and confirm the inputs are yours alone. (THE CLOSED LOOP + MATURITY + MOAT.)

## KEY TERMS (plain language)

- **Flywheel** — a loop that feeds itself: usage produces signals, signals improve the product, the better product attracts more usage.
- **Signal-to-noise (SNR)** — how informative a feedback type is; a full rewrite says more than a thumbs-down.
- **Implicit vs. explicit feedback** — what users *do* (edit, regenerate, abandon) vs. what they *say* (thumbs, ratings); behavior is more abundant and often more honest.
- **Gold / silver / bronze labels** — expert-verified corrections (gold), AI-graded judgments checked against gold (silver), simple heuristics ("deleted everything = fail") (bronze).
- **Annotation velocity** — how fast collected feedback gets labeled into usable signal; the usual bottleneck.
- **Cold start** — bootstrapping the loop before real users exist, with synthetic corrections and simulated behavior.
- **Held-out test set** — cases kept outside the loop, so you can tell real improvement from overfitting to your own feedback.
- **Anti-moat loop** — a flywheel run on signals every competitor also has; it compounds you toward the average, not ahead.
- **Evidence tiers below** — the 10–20% reaching-the-model figure, the 15–20%/quarter improvement, the maturity-level percentages, and the loop-latency benchmarks are all ⚠ practitioner estimates; measure your own.

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../../../UNIVERSAL-SKILL-PROTOCOL.md). At minimum: what's the AI output, what do users *do* with it (edit? accept? escalate?), and do you have telemetry on that already. Then route depth and output format.

**Delivery-format gate (run this before optimizing loop speed or signal quality):** check whether feedback in this loop reaches a person as data (what happened, observable, specific) or as a verdict (good/bad, a judgment, a label). A meta-analysis of 600+ feedback studies (◆ peer-reviewed, not credited by name in the citing source) found feedback delivered as a verdict, rather than as data, produces worse subsequent performance than no feedback at all in over a third of studied cases. The mechanism: the same information delivered as judgment triggers a threat response that closes a person off; delivered as observation, it triggers curiosity that keeps them open. Adobe's Check-In system is a verified case of the fix (✅ independently verified): replacing ranked ratings with ongoing, data-style check-ins saved 80,000+ hours organization-wide, cut voluntary turnover by roughly 30-34%, and lifted "feedback helps me perform" by 8 points in employee surveys. A fast, clean loop delivered as verdict can still fail, because the person receiving it disengages before the data ever gets used. **Limit:** this applies to human-facing feedback loops specifically. A loop whose recipient is a system or model, not a person, may not carry this vulnerability, since a model has no threat response to trigger.

## SIGNAL & CAPTURE

**Rank by quality** (only signal above ~70% confidence should reach the model without human review): **gold** — user provides the right answer, expert-validated (95%+); **silver** — user edits with high edit distance (70–85%); **implicit** — regenerate / abandon / accept (30–60%); **absence** — no edits (~50%, ambiguous). Design for signal *purity*, not volume: a 1-word edit and an 80% rewrite tell completely different stories.

**Capture ~80% of signal implicitly** (explicit feedback asks cognitive load most users won't pay): edit distance and direction; regeneration attempts; copy-paste time lag (used immediately or hours later?); escalation to human (use the human resolution as a gold label). **Explicit, one-click, structured:** thumbs + optional error category (tone / accuracy / completeness / irrelevance), consent-gated in PII contexts.

## ANNOTATION — the usual bottleneck

Who labels what, how fast? **Gold** (humans) — corrections from experts or escalations, ~2–3% of volume; **silver** (LLM-as-judge) — judge flagged outputs weekly against a saved reference set of gold corrections; **bronze** (heuristics) — high-confidence patterns ("deleted all output = fail," "no edits = pass"). **The critical metric: % of feedback reaching the model per week.** If <5% of captured feedback becomes signal, your flywheel is static, not dynamic — and if the labeling backlog grows monotonically, the bottleneck is annotation, not collection. **Cold start** (pre-users): generate outputs and have annotators edit them to ground truth; simulate implicit signal ("regenerate" = fail, "accept" = pass) to train the LLM-as-judge; collect aggressively, label conservatively, ramp velocity as signal quality improves.

## THE CLOSED LOOP — a pipeline, not a wish

```
Weekly:     top user corrections → pattern analysis → "what failed?"
Monthly:    accumulated corrections → add to eval set → run evals on the current model
Quarterly:  new eval set → prompt experiment → A/B test → measure the delta
Continuous: LLM-as-judge on flagged production outputs, using corrections as the reference
```

**Most teams break here** — the cadence has no owner. Name them: who runs the weekly review, who owns the eval set, who commits to the experiments. If "nobody," the flywheel is broken. **Guard the pipeline** at each step — de-duplicate (20–30% of corrections are redundant), validate (an incorrect "correction" poisons the eval set), regression-test (a new signal can break edge cases), measure impact (A/B the change or you're optimizing blind). **PII is non-negotiable:** users must know their corrections improve the system (ToS/UI), opt-out available and logged separately, anonymize sensitive data before training, define a retention policy. Regulated domains compensate for consent friction with higher signal purity (corrections only, not implicit).

*(The eval side of this — writing the failing test before the fix, and the permanent fix→eval→regression cycle that keeps a fixed failure from silently returning — is `eval-driven-development`'s core discipline. This skill feeds corrections *into* that cycle; it doesn't re-teach it. Run them together.)*

## MATURITY & THE MOAT CONDITION

Place yourself on the curve (⚠ percentages illustrative): **L1** collecting, not using (signals sit in a DB); **L2** manual quarterly review (>2-month latency, weak moat — a competitor catches up in one cycle); **L3** semi-automated, monthly cycles (LLM-as-judge on flagged outputs, 2–4 wk latency, moderate moat); **L4** automated weekly loop (30–50% of feedback reaching the model, 1–2 wk latency, strong moat); **L5** self-improving daily with human guardrails (60–80% feeding the model, <1 wk latency, formidable). **Moving up:** 1→2 is one owner, 5 hrs/week; 2→3 is a basic LLM-as-judge + a 100–200 gold reference set; 3→4 is real infra (automated eval updates, CI/CD for model changes, A/B framework); 4→5 is online learning + strict quality gates (noisy annotations at L5 *degrade* the model — the risk rises with the autonomy).

**Loop latency is the multiplier:** best-in-class 1–2 weeks (Google Maps / Waze territory ⚠), average 2–3 months, worst never. A cycle that loops in 2 weeks produces ~26 compounding improvements a year vs. ~4 at quarterly — a 6.5× difference from speed alone. But improve *speed only after quality is real*: a fast loop without validation just ships silent regressions faster.

**The moat condition (don't skip):** a flywheel is a moat only if its inputs are yours alone, and only if it's fed the *hard, rare* cases (common-case corrections build an edge the next model erases). Run the full anti-moat check in `moat-finder`.

## WHERE THIS SKILL MEETS THE REST OF YOUR STACK

- **`rtp-eval-framework` / `rtp-eval-driven-development`** — corrections become eval cases here; the *fix → failing-test → regression-test* cycle that makes improvements permanent lives in eval-driven-development. This skill produces the signal; that discipline compounds it. Run together, don't merge.
- **`rtp-moat-finder`** — the anti-moat check: is the loop fed by signals only you have, and by the rare/hard cases? A flywheel on public signals is not a moat.
- **`rtp-ai-product-metrics`** — which signals are even worth logging (acceptance / correction / regeneration rates are the flywheel's raw material).
- **`rtp-gossip-mode`** *(sibling)* — catches the *informal* single signal sideways; this is the *structured, automated* loop at volume.
- **`rtp-fit-signal`** — the loop's health is visible two hops downstream in the trust curve: a genuinely *closing* loop (corrections compounding into model gains) shows up as a trust curve that keeps rising over quarters; a *collecting-only* loop shows a flat curve despite busy "engagement." fit-signal points back here when it needs to know whether corrections are actually closing or just accumulating — this skill is that diagnosis.
- **`rtp-stress-test`, `rtp-first-principles`** *(imports)* — stress the loop's cost/throughput at scale; strip "we collect feedback" to the one atomic question ("did signal reach the model as a measured gain?").

## DIAGNOSTIC QUESTIONS (weekly)

- **How long from user signal to model improvement?** >3 months = too slow; maturity-5 products iterate weekly.
- **What % of feedback reaches the model?** (corrections used ÷ collected). Target >15% at steady state; <5% = broken.
- **Is annotation velocity keeping up with volume?** A monotonically growing backlog = labeling is the bottleneck.
- **Can you show the causal chain?** corrections → eval-set expansion → model change → A/B delta. If not, you're guessing.
- **What signals are you throwing away, and why?** "Hard to interpret" is a labeling problem, not a collection problem.

## REALITY CHECK

- **Echo chambers are real** — optimizing only on what current users correct misses what non-users need; supplement with explicit research.
- **Implicit signals are noisy** — a user editing output might be personalizing, not correcting; classify before feeding the model.
- **Feedback loops can poison evals** — test only on user corrections and you'll miss adversarial inputs and distribution shift; keep a held-out set.
- **Privacy isn't optional** — in regulated domains, collection → annotation → training needs documented flow-through.

## QUALITY GATE

- [ ] Signal hierarchy defined (corrections ranked above implicit signals)
- [ ] Annotation bottleneck identified (labeling velocity ≥ collection rate)
- [ ] Closed loop documented (weekly/monthly/quarterly cadence with named owners)
- [ ] Cold-start plan exists (how to bootstrap before users)
- [ ] % of feedback reaching the model measured weekly (target >15% steady state)
- [ ] Moat condition checked (inputs yours alone; fed by hard/rare cases)
- [ ] Delivery-format gate checked (feedback reaching people in this loop lands as data, not verdict)

## WHEN WRONG

- Batch/one-shot systems with no interactive output (no loop possible).
- Under ~500 active users, or feedback too sparse for significance.
- Privacy prohibits training on corrections without consent you can't get.
- Annotation velocity permanently <5% of collection (you don't have a flywheel; don't pretend).
- Early-stage before PMF — a fast loop optimizing the wrong product is expensive thrash; get signal quality and a stable eval set first. (And in low-volume/high-privacy domains, a deliberately manual L2–3 loop can be the correct end state, not a failure.)

## TRADE-OFF LEDGER

By building the closed loop, you bet that compounding improvement from signal only you have beats the one-time model quality anyone can buy. You take on real cost — labeling capacity, eval infra, named owners — and the discipline of measuring the delta. **Reversible?** The infra is; the *compounding advantage* it builds is not easily copied (that's the point). **The hidden trade:** the failure mode is a *fast loop on public or common-case signal* — it feels like a moat and is actually the anti-moat, compounding you toward the average; the moat condition is the guard. **Confidence: High** that closure beats collection; **conditional** on the inputs being yours alone. What would change it: a domain where you can't ethically or legally close the loop, or a product too early for its own signal to be worth compounding.

## CONCLUSION

Follow the Conclusion Protocol ([Universal Skill Protocol](../../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 5): the recommendation (current maturity level + the one limiting factor to the next), the key trade-off (loop investment vs. one-time model quality), the biggest risk (an anti-moat loop, or annotation velocity that never catches collection), and the next action (owner + cadence for the weekly review, with the %-reaching-the-model metric as the scoreboard).

## VISUAL SUMMARY

After the primary output, invoke the **excalidraw-svg** skill for one visual: the flywheel loop (usage → signals → labeling → eval → model change → better product → more usage) with the **broken link highlighted** where most teams stall (the annotation/closure gap), and a side note marking the moat condition (inputs yours alone · fed by rare cases). So a viewer sees both the loop and exactly where it's usually broken. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.
