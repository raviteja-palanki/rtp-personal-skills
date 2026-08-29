---
name: falsification
version: v1.0_latest
description: 'Turns ''this will work'' into a claim that can lose: named numbers, pre-agreed kill conditions, and stakeholders signed up to act before launch momentum makes honesty expensive. In a probabilistic system you can always find an example where the model got it right, so the only defense is deciding in advance what evidence would prove you wrong, then genuinely looking for it. Use when reviewing a strategy, before committing resources or launching, or when someone is sure it ''will work'' without saying what failure looks like. Never to block action (de-risk with it) or on cheap, reversible decisions. Pairs with: bias-spotter (the bias making the claim feel safe), problem-type (its antidote to ''we''ll wait''), stress-test (the technical pre-mortem sibling), eval-driven-development (pre-registered criteria, daily), ship-decision (the gate the kill conditions arm). Triggers: ''this will improve X'', ''we should launch this'', ''we need this to compete''.'
imports: []
---

# Falsification

**The objective:** turn "this will work" into a claim that can lose — with named numbers, pre-agreed kill conditions, and stakeholders signed up to act on them *before* launch momentum makes honesty expensive. For anyone about to commit resources to an AI feature on a claim no one has tested against failure.

## The one idea

A team ships the launch deck with the five best model outputs on the slide. They're real — the model genuinely produced them. What's not on the slide is the 500 other generations where it hallucinated or failed quietly. Everyone leaves the room believing the feature works.

That deck is the whole problem in miniature, and here is the core: **a claim that can't lose is a wish, not a claim.** "AI search will improve the experience" cannot be wrong — there's no result that would falsify it — so it tells you nothing. And AI makes this trap far worse than ordinary product work, because non-determinism *weaponizes* it: in a probabilistic system you can always find an example where the model got it right. Cherry-picking a win is trivially easy and devastatingly misleading. Your intuition, running an unfalsifiable claim on a system that always offers a success to point at, will fool you every time.

So the only defense against fooling yourself is to decide, in advance and in writing, **what evidence would prove you wrong** — then genuinely go look for it. And you are fighting two enemies, which is why the discipline has two halves:

- **Confirmation bias, in you.** You'll run a user test, find three people who loved it, and call it validation — never noticing the seven who were confused. The fix is *pre-registration*: write the pass/fail number down before you see the results, so the results can't quietly redefine success.
- **Launch momentum, in the org.** Once everyone has championed the feature, invoking a kill condition looks like sabotage. The fix is *pre-commitment*: get stakeholders to sign up to the kill conditions *before* launch, while honesty is still cheap.

Make the claim able to lose. Name what losing looks like. Get people to agree to act on it — before the momentum arrives.

## How to use this skill

1. **Make the claim able to lose** — restate the recommendation as a falsifiable hypothesis with numbers and a timeframe. (THE PROCESS, step 1.)
2. **Name and pre-register the kill conditions** — 3–5 measurable outcomes that would prove it wrong, written down *before* results, each with a detection method. (Steps 2–4.)
3. **Get pre-commitment to act** — stakeholders sign up to the kill decisions before launch, not after.
4. **Always measure the failure mode directly**, not just the success rate — the AI-specific patterns below turn vague claims into tests that can actually fail.

## KEY TERMS (plain language)

- **Falsifiable hypothesis** — a claim specific enough that evidence could prove it wrong ("under 90 seconds for 80% of queries"), versus one that can't lose ("improve the experience").
- **Kill condition** — a measurable outcome, agreed before launch, that triggers a pre-committed action (pause, pivot, sunset). Not a vibe; a number with an owner.
- **Pre-registration** — writing the pass/fail criteria down before seeing results, so results can't redefine success.
- **Criteria drift** — deciding what "passing" means *after* looking at the output; confirmation bias wearing an eval's clothes (Shreya Shankar's term).
- **Frozen / held-out test set** — a fixed set of cases the model never trains on, kept stable so month-over-month scores are comparable.
- **Distribution mismatch** — your test data doesn't resemble real production input (typos, slang, edge cases), so the score flatters.
- **Precision / recall** — of the things flagged, how many were right (precision); of the things that should have been flagged, how many were caught (recall). "Accuracy" alone hides which is broken.

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../../../UNIVERSAL-SKILL-PROTOCOL.md). At minimum: state the claim being made and who's about to commit to it. Then route depth (a full falsification brief for a significant AI investment vs. a quick check that success criteria are even measurable) and output format. Skip it when the decision is genuinely cheap to reverse — just ship and learn.

## THE TRAP — success theater

You will look for evidence that you're right (**confirmation bias**), and in AI that instinct is armed with an endless supply of cherry-pickable wins. Teams systematically hide failure in five ways — learn to see them:

- **Demo bias** — the best 5 outputs go on the slide; the 500 failures don't.
- **Average masking** — "90% accuracy" hides that the worst 10% of queries (edge cases, ambiguous, adversarial) run at 40% — and users hit exactly those and remember them.
- **Metric gaming** — the team optimizes the metric, not the outcome: "cut tickets 20%" → the AI deflects tickets into a new category that doesn't count as a ticket. Metric hits, problem unsolved.
- **Distribution mismatch** — the eval set is curated or synthetic; production is typos and off-label requests. 85% in eval becomes 65% live.
- **Silent failure** — models don't crash, they return confident garbage; by the time complaints surface, you've trained on contaminated feedback.

## THE PROCESS

1. **State the recommendation as a falsifiable hypothesis.** Bad: "AI search improves the experience." Good: "AI search reduces average time-to-answer from 4 minutes to under 90 seconds for 80% of queries, without increasing support escalations."
2. **Name 3–5 kill conditions** — measurable outcomes that would prove it wrong: which metric declining invalidates it? which user behavior signals failure? which cost threshold makes it unviable? which competitor move makes it irrelevant?
3. **Design the counter-test for each** — what data, over what period, past what threshold counts as "failed."
4. **Pre-commit the kill decision.** In writing, before launch: "If [condition] holds after [period], we will [pause / pivot / sunset]." Get stakeholder sign-off *now*, not after.
5. **Run the red team.** "If I were trying to make this fail, what would I do?" Then check whether those conditions already exist in the wild.
6. **For AI claims, pin the thresholds.** "This model detects fraud" → at what accuracy, on what distribution (train/prod/adversarial), below what number does it fail the business? Accuracy without context is false precision.

## THE PRE-MORTEM — five ways AI features die

Imagine it's six months out and the feature failed. Force the story for each mode below, then set a kill condition. *(Sibling note: `stress-test` carries the pre-mortem aimed at the **technical** surface — load, cost, latency. This one is aimed at the **hypothesis** — which claim breaks. Run whichever matches what you're protecting; don't run both out of ritual.)*

| Failure mode | The story | Detect it | Example kill condition |
|---|---|---|---|
| Model degradation | 87% at launch, 79% by month 3 — distribution shift, drift, or contaminated feedback | Monthly eval on a frozen test set (not "user satisfaction") | Accuracy drops >5% after 60 days → pause to new users; unresolved in 2 weeks → sunset |
| Cost explosion | Viable at 10K queries/day, hemorrhaging at 100K — GPU serving, human-in-loop that doesn't scale | Cost-per-query visible daily | Cost/query > $0.08 at 50K/day → switch to cheaper model; if quality < 80% → sunset |
| Trust collapse | "Amazing" week 1 → "wasted my hour" week 3 → avoided week 8; one bad answer erases five good | DAU decline + escalation spikes (not just positive reviews) | >20% report incorrect info in surveys → require human verification; if usage drops >40% → kill |
| Data drift (prod ≠ train) | Trained on clean queries; production is typos, slang, edge cases never seen | Compare eval vs. production accuracy monthly, stratified | Production accuracy >10% below eval within 30 days → manual-review layer before serving |
| Competitive leapfrog | You gain 12% growth; a rival ships better AI search in 4 weeks and takes it | Weekly competitive monitoring | Rival ships equivalent in 90 days → strategic reassessment; no differentiated use case in 30 days → sunset |

## PRE-REGISTER THE EVAL — where falsification actually bites

Evals are where you test the hypothesis, but only if the eval maps to a claim and the bar was set *before* you looked.

- **Map every claim to an eval.** "If this claim is true, [specific eval] passes at [threshold]." *"AI summaries reduce reading time" → 200 documents, binary pass/fail "did the user finish the task faster with the summary?", threshold 80%.*
- **Binary pass/fail beats Likert.** "Rate clarity 1–5" is negotiable (one person's 3 is another's 5). "Could a user with no domain knowledge complete the task using only the AI's explanation?" is falsifiable.
- **Pre-register the bar (fights criteria drift).** "We commit now: the eval passes at 80% task completion. We run it. We report the result, whatever it is." Not: "let's run it and see how it looks" — you'll pass whatever you see.
- **Track evals over time.** A passing eval isn't proof; *an eval that used to fail and now passes* is proof — and an eval that dropped from passing to failing is the signal to act.

| Eval | Hypothesis | Threshold | Launch | M1 | M3 | M6 | Read |
|---|---|---|---|---|---|---|---|
| Sarcasm detection | catches sarcasm at 85%+ | 85% | 87% ✓ | 84% ✗ | 82% ✗ | 78% ✗ | degrading on data drift → act |
| Task completion | users finish with AI help | 70% | 72% ✓ | 71% ✓ | 68% ✗ | 65% ✗ | requests growing more complex |

## AI-SPECIFIC FALSIFICATION PATTERNS — measure the failure mode, not the success rate

Every row is a claim that sounds good in a meeting and fails in production. The through-line: **measure the failure mode directly.**

| Claim | Falsification test | Example kill threshold |
|---|---|---|
| "AI will reduce support tickets" | Track deflection AND new tickets caused by AI errors ("your AI gave me wrong info") separately | Kill if AI-caused tickets > 15% of deflected |
| "Users prefer AI summaries" | A/B with the original visible; track reverts and edit distance vs. human baseline | Kill if >40% edit or revert to original |
| "This model is accurate enough" | Test on production distribution, stratified by segment/complexity/language; compare worst segment to best | Kill if worst-segment accuracy < 70% |
| "Hallucination rate is <2%" | Blind eval on 1000+ generations incl. adversarial prompts; separate confident hallucinations from uncertainty | Kill if hallucination > 5% on production distribution |
| "Users trust this feature" | Behavioral trust: do they act without verifying? do they override? "would you trust it with a high-stakes decision?" | Kill if <60% would use it for important decisions |

## WORKED EXAMPLE — AI-powered document search

**Hypothesis:** "AI document search reduces average research time from 45 min to under 15 min for 80% of knowledge workers on a 10,000-doc repository, within 30 days, without raising task error rate above 3%."

**Three of the pre-committed kill conditions (5 total in the real brief):**
- *Insufficient value* — average research time still > 25 min after 30 days → pivot to hybrid (AI re-rank on top of manual search). Detect: UI instrumentation, query→completion time.
- *Trust damage* — hallucinated citations > 5% of results (cited doc doesn't match the claim) → add a citation-verification layer. Detect: monthly human review of 100+ sampled queries.
- *Cost* — cost/query > $0.08 at 10K/day → switch to a cheaper embedding model or cache. Detect: real-time cost tracking.

**Pre-committed action (the part that matters):** *"If any two conditions trigger by day 14, we sunset and reallocate the team."* Signed before launch by PM, Eng, Data, and Leadership — the sign-off *is* the deliverable, because it's what survives launch momentum. Eval mapping: primary binary "correct doc in top 3?" at 80%; secondary "any hallucinated citation?" under 5%; behavioral A/B (50 AI vs. 50 manual) for task time, AI must be 20%+ faster with no error increase.

## WHERE THIS SKILL MEETS THE REST OF YOUR STACK

Falsification makes a claim able to lose. It works next to:

- **`rtp-bias-spotter`** — names the *bias* making the claim feel safe (optimism, confirmation, demo bias); falsification then builds the test that would catch it.
- **`rtp-problem-type`** — its REALITY CHECK names its own worst failure mode: "it's adaptive, so we wait," indefinitely. Falsification is the direct antidote — pre-commit what evidence, by what date, would prove the wait isn't just stalling dressed as patience.
- **`rtp-judgment-guard`** — the same defense mechanism at a different scale. Judgment-guard's state-first override commits an individual to a call *before* seeing the AI's answer, so the answer can't bias the judgment; falsification's pre-commitment does the identical thing for an organization, committing stakeholders to kill conditions before launch momentum can bias the will to act on them.
- **`rtp-stress-test`** — the technical pre-mortem sibling: it protects against load/cost/latency breaking; this protects against the *hypothesis* being wrong. Same discipline, different failure surface.
- **`rtp-eval-driven-development`** — where the pre-registered criteria live day to day; falsification sets the bar, EDD runs the loop against it.
- **`rtp-ship-decision`** — the gate the kill conditions arm. Falsification writes the no-go triggers; ship-decision is where they're honored (and where the incentive to *voice* a kill lives).

Run falsification to make the claim losable; run these to name the bias, resolve a misdiagnosis, borrow the commitment mechanism, price the technical risk, operate the evals, and arm the gate.

## DIAGNOSTIC QUESTIONS

- **What specific metric would make me stop this?** If you can't name one with a number, you're not being honest with yourself.
- **Am I testing on the distribution that matters (production) or the one that flatters (eval set, synthetic, cherry-picked)?**
- **Have I pre-registered success, or am I defining it after seeing results?** Post-hoc criteria are confirmation bias.
- **Do stakeholders know the kill conditions — or will they be shocked when I invoke them?** Surprise kills become political fights.
- **What's the cheapest experiment that would disprove this, and have I run it?** If you haven't run the cheapest test, you're not actually confident.
- **Can everyone on the team name the kill conditions from memory?** If they're fuzzy, they won't execute them.

## OUTPUT FORMAT

```
## Falsification Brief: [Feature / Hypothesis]

**Hypothesis:** [specific numbers, timeframe, success + a guardrail metric]
**Kill Conditions:**
  1. [metric] past [threshold] after [timeframe] → [action]
  2. [cost metric] past [threshold] at [scale] → [action]
  3. [user-behavior signal] → [action]
**Eval Mapping:** [eval → which claim it tests → pass/kill threshold] ×N
**Pre-Mortem Top Risks:** [risk · probability · detection speed · recovery time] ×3
**Pre-Commitment (sign-off before launch):**
  [ ] PM  [ ] Engineering  [ ] Data  [ ] Leadership will execute the actions above
```

## QUALITY GATE

- [ ] Recommendation stated as a falsifiable hypothesis with numbers
- [ ] 3–5 kill conditions with specific thresholds and pre-committed actions
- [ ] A counter-test designed for each kill condition
- [ ] Eval criteria pre-registered *before* running the eval
- [ ] Pre-mortem completed for 3+ failure modes
- [ ] Stakeholders have explicitly agreed to the kill conditions before launch
- [ ] Red team done — the skeptic's strongest counter-argument is written down

## REALITY CHECK

- **Falsification becoming nihilism.** Everything can be falsified; the goal is the *most likely* failure modes, not proving nothing works.
- **The political cost is the point.** Stakeholders who championed the feature resist pre-mortems — which is exactly why pre-commitment has to happen before the momentum, not after.
- **It costs 2–4 hours of real thinking.** Budget it; it's cheaper than a committed-then-broken launch.

## WHEN WRONG

- Very early exploration where the hypothesis isn't worth formalizing yet.
- Cheaply reversible decisions — just ship and learn.
- When the team has already falsified rigorously and now needs to commit.
- When falsification is being used as a political tool to avoid deciding.

## TRADE-OFF LEDGER

By making the claim losable and pre-committing to kill conditions, you bet that 2–4 hours of honest thinking now is cheaper than six months and stakeholder credibility spent on a claim that was never able to fail. You give up the comfort of an unfalsifiable pitch and take on political friction. **Reversible?** The brief is; the credibility spent defending a wish that broke in public is not. **The hidden trade:** the failure mode is *nihilism* (falsify everything, commit to nothing) — so cap it at the most likely failure modes and act. **Confidence: High.** What would change it: a genuinely cheap-to-reverse decision, where shipping and learning beats the ceremony of a brief.

## CONCLUSION

Follow the Conclusion Protocol from the [Universal Skill Protocol](../../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 5: state the recommendation (the hypothesis, made falsifiable), name the key trade-off (upfront honesty and friction vs. a public failure later), acknowledge the biggest risk (criteria drift, or stakeholders who won't honor the kill), and define the next action (the pre-registered kill conditions, signed, with owners).

## VISUAL SUMMARY

After the primary output, invoke the **excalidraw-svg** skill for one visual: a claim in the center split into "can't lose (a wish)" vs. "can lose (a hypothesis)", with the two enemies drawn on either side — confirmation bias (cherry-picked wins) and launch momentum (the kill nobody will invoke) — and the two fixes (pre-register the bar · pre-commit the stakeholders) as the bridges across them. So a viewer sees why a losable claim plus signed kill conditions is the whole defense. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.
