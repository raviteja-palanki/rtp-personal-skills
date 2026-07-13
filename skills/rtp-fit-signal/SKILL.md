---
name: fit-signal
description: >
  Tell whether an AI product has earned real user dependence, or just survived a lucky stretch.
  Standard PMF metrics — NPS, retention, DAU — get inflated by AI's own variance, so a team can
  "confirm PMF" on users who are stress-testing the product, not depending on it. The one signal
  immune to that variance is the trust curve: rising, plateauing confidence in AI output over
  weeks, which luck can't fake because it takes many good experiences in a row. Builds a
  fidelity-based trust score, the magic moment that predicts who reaches it, correction-rate
  decay (and the resignation trap that fakes it), switching cost, and a four-verdict scorecard:
  confirmed, emerging, uncertain, no fit. Use when you have 8+ weeks of active users and must
  decide scale, iterate, or pivot — or when NPS looks fine but something feels off. Do NOT use
  pre-launch, on deterministic products, or under 100 weekly active users.
  Pairs with: falsification, feedback-flywheel, stress-test, uncertainty-research, ai-product-metrics.
imports:
  - falsification
  - feedback-flywheel
  - stress-test
---

# Fit Signal

**The objective:** decide, with evidence instead of vibes, whether an AI product has earned real user dependence — for the team staring at "healthy" retention and NPS and still not sure whether to scale, keep iterating, or pivot.

## The one idea

A user opens your AI feature on Monday. It works — clean output, nothing to fix. Tuesday, same feature, a slightly different question, and it hallucinates. Wednesday, it works again. Averaged over a month, your NPS reads a healthy 42. Retention looks fine. The dashboard is green.

The user still doesn't trust you. They just haven't left yet.

That gap is the whole problem. **Every metric a PM defaults to for product-market fit — NPS, retention, DAU — assumes the product is the same experience every time it's used.** That assumption is what makes those metrics work: a stable product a user keeps returning to is one they've decided to depend on. AI breaks the assumption. The product is a different experience every time, so the metrics stop measuring fit and start measuring variance. Retention looks healthy because it's a cohort average, and averages smooth a bad Tuesday into a good Wednesday. NPS looks healthy because the person who had two good sessions this week answers the survey today, not on the day it failed them. You can clear every "PMF confirmed" threshold on a spreadsheet built from users who are stress-testing your product, not depending on it — checking back to see if it's gotten reliable yet, not because they've decided it has.

The one signal that survives contact with variance is the **trust curve**: does a user's confidence in your output rise over weeks and hold high, or stay flat, or bounce around? That question is hard to fake, because holding high for eight straight weeks takes many individually good experiences in a row — no amount of lucky timing on one NPS survey can manufacture that. Everything else in this skill — the magic moment, correction-rate decay, switching cost — exists to explain what moves the trust curve, and to catch the one trap that fakes it: users who look calmer because they've stopped checking, not because they've started trusting.

## How to use this skill — four questions

1. **Is trust actually accumulating, or are you reading NPS and retention instead?** → Signal 1, the trust curve — the core measurement below.
2. **What's the one interaction that turns a user trying you out into a user who comes back?** → Signal 2, the magic moment.
3. **Are users correcting your output less because they trust it, or because they gave up checking?** → Signal 3, correction-rate decay and the resignation trap.
4. **What's the actual verdict — scale, iterate, or pivot?** → The PMF scorecard, at the end.

Read Signal 1 first regardless of which question brought you here — it's the spine the other three attach to.

## KEY TERMS (plain language)

- **Trust curve** — a user's (or cohort's) weekly trust score, plotted over 8+ weeks; the one PMF signal that isolates dependence from lucky timing.
- **Fidelity score** — one number per AI output, on a single 0–1 scale: used as-is (1.0), minor edit (0.6), major rewrite (0.2), rejected or regenerated (0.0). The building block both the trust score and the correction rate are computed from.
- **Trust score** — the average fidelity score across a week's outputs; a magnitude-weighted read of "how much did this user actually rely on what you gave them."
- **The engagement mirage** — DAU, session length, and NPS all rising while users are actually stress-testing your reliability, not depending on it; it looks exactly like early PMF and isn't.
- **Magic moment** — the specific interaction (completing N tasks, a successful edit-then-use cycle, sharing output) that precedes a user's trust curve inflecting upward; differs per cohort.
- **Correction-rate decay** — the drop in how often outputs need a major edit or a regeneration as weeks pass; a real trust signal, unless it's the resignation trap.
- **The resignation trap** — correction rate falls not because quality improved but because the user stopped checking; the tell is a flat or rising complaint rate alongside a falling correction rate.
- **Switching cost** — how much friction it would take a trusting user to leave for a competitor; the indirect confirmation that fit is real, not just measured wrong.
- **Evidence tiers used below** — ✅ audited/peer-reviewed · ◆ company- or study-disclosed · ⚠ illustrative teaching anchor. Every number, formula output, and threshold in this skill is ⚠: there is no published trust-curve benchmark literature yet. Run the formulas on your own cohort and set your own thresholds — the numbers here show the shape of a healthy curve, not someone else's cutoff.

## GROUNDING (Before Starting)

Go deep if you have 8+ weeks of active-user data and need to decide whether to scale, keep iterating, or pivot. Skim straight to Signal 1 if you already have trust data and just need the interpretation. Skip this skill entirely if you have under 100 weekly active users (the signal is too noisy to read), your product is deterministic (classic PMF frameworks already work), or it's batch/offline AI with no real-time feedback loop (there's no session for trust to build within).

Then follow the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md): name the customer and the problem, decide Executive Summary vs. full analysis, and pick the output format.

---

## THE FALSIFICATION HANDOFF — what would prove you don't have fit

Before you measure anything, write down what would prove you wrong. This is `falsification`'s discipline — import it for the full pre-registration method. Here are the four questions specific to AI-PMF:

- If you removed the AI component entirely, would users still use the product? (Yes → you have workflow-PMF, not AI-PMF.)
- If you swapped in a competitor's model, would anyone notice? (No → the AI is commoditized, not a moat.)
- If you doubled the price, would usage collapse? (Yes → they're here for the price, not the preference.)
- If you went dark for a week, would users go find an alternative? (No → they don't depend on you yet.)

Pre-commit to what you're measuring before you look: the trust curve's shape, the magic moment's hit rate, correction-rate decay, and switching cost. Deciding the bar after seeing the data is how teams talk themselves into PMF that isn't there.

## SIGNAL 1 — THE TRUST CURVE (the core signal)

Classify every AI output into one of four categories, and use the same classification for both this signal and Signal 3 below — they're two different aggregations of the same event log, not two separate systems:

| Category | Fidelity score | Counts as a "correction"? |
|---|---|---|
| Used as-is | 1.0 | No |
| Minor edit (small fix, <30% changed) | 0.6 | No |
| Major edit (rewrite, >50% changed) | 0.2 | Yes |
| Rejected / regenerated | 0.0 | Yes |

**Trust score** (this signal) = the average fidelity score across a week's outputs — magnitude-weighted, so a run of minor edits drags it down gently. **Correction rate** (Signal 3) = the % that were major-edit-or-regenerated — a hard failure rate that a pile of minor edits doesn't touch. Track both: if trust score rises while correction rate stays flat, outputs are getting slightly better on average but not more reliable — a different problem than the reverse.

```
Worked example — 10 outputs this week:
6 used as-is (1.0) + 2 minor edits (0.6) + 1 major edit (0.2) + 1 rejected (0.0)
Trust score = (6×1.0 + 2×0.6 + 1×0.2 + 1×0.0) ÷ 10 = 7.4 ÷ 10 = 0.74
Correction rate, same week = (1 major + 1 rejected) ÷ 10 = 20%
```

A stricter version also weights by downstream use — did the user act on the output, or just read it. Add that once the basic pipeline is trustworthy; it isn't needed to start.

Plot the trust score for 8+ weeks (⚠ illustrative shape of a healthy curve):
```
Wk 1: 0.42   Wk 2: 0.45   Wk 3: 0.48   Wk 4: 0.51
Wk 5: 0.58 (inflection)   Wk 6: 0.62   Wk 7: 0.65   Wk 8: 0.67 (plateau)
```

Read the shape, not any single week:
- **Flat or declining** — no PMF. Something is systematically unreliable; more engagement won't fix it.
- **Inflecting upward, plateauing above ~0.60 (⚠ illustrative bar — calibrate to your domain)** — the PMF signal. Users are learning to depend on you.
- **Volatile, swinging 0.3–0.7** — variance is too high to trust. A more consistent competitor can take these users even at lower raw accuracy.

Segment before you conclude anything: an overall trust score of 0.55 can hide 0.72 on use case A and 0.38 on use case B. That's not "PMF, needs work" — it's PMF for A and not for B, and the action is double down on A, then fix or kill B.

One companion threshold worth tracking alongside the curve: **the confidence level at which users switch from doing it manually to trusting your output.** If they need >90% confidence before using what you gave them, you've built a verification tool, not a dependency — useful, but a much smaller market. If they confidently use output at 70% confidence, that's a real trust signal, independent of the curve's shape.

## SIGNAL 2 — THE MAGIC MOMENT (the conversion trigger)

The magic moment is the specific interaction that precedes a user's trust curve turning upward — the thing that flips "trying this out" into "I use this weekly." It's usually one of: completing N outputs (trust through repetition), a successful edit-then-use cycle (overcomes first distrust), sharing output with a colleague (external validation), or returning on 3+ separate days (habit forming).

Find it by looking at the users whose trust curve actually inflected — what did they do in the two weeks before the turn that the flat-curve users didn't? Then measure it per cohort, because the moment isn't universal (⚠ illustrative):

```
Power users (5+ queries/day):  70% hit the moment → 78% 8-wk retention
                                30% miss it        → 32% 8-wk retention
Skeptics (1-2 queries/day):    45% hit the moment → 65% 8-wk retention
                                55% miss it        → 28% 8-wk retention
Occasional (<1/day):           20% hit the moment → 55% 8-wk retention
                                80% miss it        → 18% 8-wk retention
```

The occasional cohort's 20% hit rate is the tell: this segment isn't reaching fit, so more marketing to them won't help — the fix is either redesigning their path to the moment or deprioritizing them for the cohort that already gets there. Once you know the moment, design toward it: a guided tour toward N completed outputs, a more discoverable edit flow, lower-friction sharing. Track the hit rate itself over time — a rising hit rate should precede a rising retention number by a few weeks; if it doesn't, the moment you found isn't the real one.

## SIGNAL 3 — CORRECTION-RATE DECAY (and the resignation trap)

Using the same four-category classification from Signal 1, correction rate = (major edits + regenerations) ÷ total outputs, tracked week over week.

```
Healthy pattern (⚠ illustrative): Wk 1: 60% → Wk 2: 45% → Wk 4: 25% → Wk 8: 15%
Concerning pattern:                Wk 1: 70% → Wk 4: 65% → Wk 8: 60%
```

Target a 50–60% reduction from week 1 to week 8 (⚠ illustrative bar — set your own from your first cohort). Flat or rising correction rate means the product isn't getting more reliable in the user's hands, full stop.

**The trap:** falling correction rate can mean the user learned to trust you, or it can mean they gave up checking. Both look identical in the correction-rate number alone. Distinguish them with a second signal — complaint rate and downstream use. If corrections fall *and* complaints stay flat *and* users keep acting on the output, that's trust. If corrections fall while complaints rise or downstream use quietly drops, that's resignation: users accepting worse output because checking isn't worth their time anymore — a leading indicator of churn, not fit.

Expect different baselines by use case — code generation should sit above 90% used-as-is-or-minor-edit, open-ended creative work closer to 60–70% (⚠ illustrative). A use case running 80% correction when you expected 40% means either the use case is wrong for AI or the product is failing it specifically.

## SWITCHING COST — the indirect confirmation

If trust is real, leaving should be costly. Four behavioral proxies, roughly in order of how much they tell you (⚠ illustrative targets):

| Proxy | What it tells you | Illustrative target |
|---|---|---|
| Deleted account in first 2 weeks | No stickiness at all | <15% |
| Tried a competitor, came back | Prefers you even after testing the alternative | >20% |
| Paid for a premium tier | Financial plus workflow lock-in — the strongest signal | >5–10% |
| 50+ interactions logged | Workflow is built around you | >40% of retained users |

For a direct read rather than a proxy: give 20–30 trusting users (trust score >0.60, active 4+ weeks) a free trial of a competitor, and watch whether they come back. Above ~70% return is real switching cost; below ~50% is a danger signal regardless of what the dashboard says. The same logic works as a pricing test: estimate what fraction would leave at a 20% price increase — under 5% leaving means the switching cost can support a premium; over 10% means it can't yet.

## THE FEEDBACK LOOP CHECK — import feedback-flywheel

Correction-rate decay is only a trust signal if the corrections users give you are actually closing a loop — reaching someone, changing the prompt or retrieval or model, and showing up as fewer of the same corrections for the next cohort. If they're landing in a database nobody reads, "users correct less" may just be the resignation trap above, dressed up as good news.

The full design of that loop — signal capture, annotation velocity, the weekly-to-quarterly cadence, when it's a real moat versus overhead — is `feedback-flywheel`'s job; import it. The one check to run here: pick last month's ten most common correction patterns and ask whether any of them changed the product. If the answer is no, don't credit a falling correction rate to trust — credit it to resignation until proven otherwise.

## THE VERDICT — THE PMF SCORECARD

Bring the signals together into one read. Fill ACTUAL from your own data; the TARGET column is ⚠ illustrative — replace it with the thresholds you pre-committed to in the falsification handoff.

```
SIGNAL                       TARGET        ACTUAL      STATUS
Trust score (week 8)         >0.60         ___
Inflection point             by week 4-5   ___
Magic-moment hit rate        >60%          ___
Correction-rate decay        >50%          ___
Feedback loop                closing       ___
Switching cost                real         ___
```

Four verdicts, four actions:

- **PMF CONFIRMED** — trust >0.60 and inflecting, magic moment >60%, feedback loop closing, switching cost real. **Scale with confidence; ship adjacent features.** Before scaling, run `stress-test` (import) — a confirmed trust signal on 200 users says nothing about whether the system holds at 20,000.
- **PMF EMERGING** — trust trending up but not plateaued, magic moment 40–60%, loop just starting to close. **Invest in the magic moment's UX; re-measure in 4 weeks.**
- **PMF UNCERTAIN** — trust flat, magic moment <40%, loop not closing, switching cost weak. **Investigate the root cause — quality, wrong problem, or bad UX — before choosing fix or pivot.**
- **NO FIT** — trust crashing, churn climbing, magic moment <20%. **Kill or fundamentally pivot the feature.** More engagement will not fix a fit problem — that's the mistake this skill exists to prevent.

## WHERE THIS MEETS YOUR STACK

Fit-signal owns the *diagnosis*: is this AI product actually earning dependence. It hands the surrounding work to:

- **`ai-product-metrics`** — the raw acceptance, correction, and regeneration events this skill aggregates into a trust curve; that skill defines what to instrument, this skill tells you what the numbers mean for fit.
- **`feedback-flywheel`** (import) — whether user corrections are actually closing into product improvement; without it, "correction rate fell" can't be trusted as a signal.
- **`uncertainty-research`** — when the simple weekly-average trust score isn't rigorous enough (small samples, contested findings, a board that wants a defensible number), that skill's stratified and longitudinal methods measure trust properly.
- **`falsification`** (import) — the pre-registration discipline behind the four kill-condition questions above; run it in full before measuring, not after you like what you see.
- **`stress-test`** (import) — once the scorecard says CONFIRMED, this is the technical half: does the system hold at 10x the users, not just earn their trust at the current scale.

## REALITY CHECK

- **Trust curve is noisy under 100 weekly active users.** Measure bi-weekly or monthly instead of weekly until volume catches up — a weekly read at that size is mostly noise.
- **A 20–30% week-to-week swing is normal**, not a framework failure, if there's been a quality regression or a latency spike. Investigate the cause; don't discard the method.
- **Different use cases have different baseline curves.** Support triage and creative writing will never converge to the same numbers — don't force them to.
- **PMF is not revenue.** You can have real trust and weak monetization (freemium), or real revenue with no trust (a captive market that would leave the moment it could). They're different problems; don't let one masquerade as evidence for the other.
- **You can't call the feedback loop "broken" until you've funded it.** Capturing feedback without processing it is a resourcing gap, not proof the flywheel doesn't work.

## QUALITY GATE

- [ ] 8+ weeks of data, 100+ weekly active users — enough volume for the signal to mean something
- [ ] Kill conditions and success thresholds written down *before* looking at the data (the falsification handoff)
- [ ] Trust curve calculated and its shape read — flat / inflecting-then-plateau / volatile — not just its latest value
- [ ] Trust segmented by use case, not read as one blended number
- [ ] Magic moment identified per cohort, with a hit rate, not assumed to be universal
- [ ] Correction-rate decay checked against complaint rate and downstream use — the resignation trap ruled out, not ignored
- [ ] Last month's correction patterns checked for whether any actually changed the product
- [ ] Switching cost tested with at least one behavioral proxy or the competitor-trial test
- [ ] Scorecard filled with real numbers, one of the four verdicts written down, next action named

## DIAGNOSTIC QUESTIONS

1. **Has anyone plotted trust week-over-week, or only checked NPS and retention?** Only NPS/retention means you don't have a PMF read yet — you have an engagement mirage until proven otherwise.
2. **When correction rate fell, did complaint rate fall with it?** Corrections down but complaints flat or up is resignation, not trust.
3. **What's last month's magic-moment hit rate, by cohort?** A blank stare here means no one has looked — that's the diagnosis by itself.
4. **If you went dark for a week, would users go find an alternative?** "No" means dependence hasn't happened yet, whatever the dashboard says.
5. **Is trust uniform across use cases, or is a strong one hiding a weak one?** A single blended number can hide a kill-this/scale-that split that changes the whole roadmap.

## WHEN WRONG

- Pre-launch, with no users yet to measure.
- Deterministic products with low output variance — the classic PMF playbook (Sean Ellis, retention cohorts) already works; don't add this overhead.
- Batch or offline AI with no real-time feedback loop — there's no session for trust to build within.
- Under 100 weekly active users — the math above is just noise at that volume.
- When "let's measure PMF properly" has become the reason nothing ships. This skill informs a decision; it isn't a substitute for making one.

---

## TRADE-OFF LEDGER

**By trusting the curve over NPS and retention, you bet** that dependence, not sentiment, is what actually predicts whether this product survives contact with a more reliable competitor. **You give up** the comfort of the simpler metrics — trust measurement takes real instrumentation (fidelity scoring, per-cohort tracking) that an NPS survey doesn't require, and it will sometimes hand you an uncomfortable UNCERTAIN verdict when the dashboard says CONFIRMED. **Reversible?** Yes — this is a measurement choice, not a product commitment; you can adopt or drop the trust curve without touching the product itself. **The hidden trade:** you're choosing to find out now, from eight weeks of real behavior, whether users depend on you — instead of finding out in six months, from a churn spike, that they never did. **Confidence: High. What would change it:** a deterministic product, where the classic metrics already work, or a userbase too small for the curve to mean anything — in either case, use standard cohort retention or `stress-test` instead.

## CONCLUSION

Follow the Conclusion Protocol (Universal Skill Protocol, Section 6): state the recommendation (scale, iterate, fix-or-pivot, or kill, tied to the scorecard's verdict), name the key trade-off (measurement rigor now vs. the comfort of metrics that lie), acknowledge the biggest risk (the resignation trap read as trust, or a kill condition abandoned once the team likes what early data shows), and define the next action (who owns the weekly trust-curve update, and the date of the next scorecard read).

---

## VISUAL SUMMARY

After the primary output, invoke the **excalidraw-svg** skill for one visual: the trust curve (weeks 1–8, the inflection marked) beside the magic-moment cohort bars and the four-verdict scorecard, so a viewer sees in one glance where the curve sits, what's driving it, and what to do next. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.
