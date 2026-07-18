---
name: bias-spotter
version: v1.0_latest
description: "Names the cognitive bias making a flawed AI product decision feel obvious or inevitable — before the money is committed. The feeling of 'obviously right' is data, not truth: it has a named mechanism, and you can't introspect it away (finding no bias is itself the warning). Audit the decision, not your sense of being rational. The same pull attacks three stages: what you BUILD, how you MEASURE, and what the model itself CARRIES. Name it, price the risk in, mitigate — never block. Use when reviewing a PRD or feature proposal, before a resource commit, when a decision feels 'obvious' / 'the competitor did it', or after a senior person weighs in. Never to block a decision, or stall a team that needs to commit. Pairs with: falsification (what would prove this wrong), first-principles (strip the framing first), eval-framework (fixes Stage 2's red flags), trendslop-check (bias baked into AI-generated strategy). Triggers: 'that's just common sense', 'obviously we need to', 'this is our only option'."
imports: []
---

# Bias Spotter

**The objective:** name the cognitive bias making a flawed AI product decision feel obvious — before the money is committed — for anyone reviewing a recommendation, a PRD, or a resource bet. It never blocks a decision; it prices the risk into it.

## The one idea

Every expensive AI product mistake felt right at the time. The team that shipped the model that failed in production wasn't careless — the decision *felt* obvious, even rational, right up to the moment it broke. That feeling is the thing to distrust. It is not truth; it is data. And it has a mechanism, and the mechanism has a name.

Here is the trap that makes this hard, and it is the reason you can't just "be more objective." You cannot introspect your way out of a bias. Look inward for your own biases and you will find none — not because they're absent, but because the looking is done by the same biased machine. That is **meta-blindness**, and its cruelest feature is that *finding no bias is itself the warning sign.* Feeling rational is not evidence of being rational.

So the move is not "check my thinking." The move is: **audit the decision, not your feeling about it.** Name the mechanism pulling it toward "obvious," state the evidence, and force one mitigation. You are not trying to reach perfect rationality — that's a fantasy, and chasing it becomes analysis paralysis. You are trying to price a known risk into a decision you're going to make anyway.

And the pull shows up at three different stages, each needing a different fix:

- **What you BUILD** — decision biases. Which problem you pick, which solution you commit resources to. (Anchoring, sunk cost, bandwagon, novelty.)
- **How you MEASURE** — evaluation biases. Whether you can even tell if it's working. This is where bias does the most damage in AI, because evals *look* objective — they're numbers. (Demo bias, confirmation, benchmark anchoring.)
- **What the model CARRIES** — system biases. Baked into training data, propagating downstream whether you look or not. (Training-data bias, aggregation bias, automation bias.)

One mechanism, three stages. Find the stage you're in, and audit there.

## How to use this skill

1. **Run the audit** — name the decision, walk the checklist, find the one or two biases actually driving it. (THE PROCESS below.)
2. **Route to the stage** — is the risk in what you're building, how you're measuring, or what the model carries? Each of the three has its own bias set and its own fix. (THE THREE STAGES below.)
3. **Invert and price it in** — look for the evidence that would prove you wrong, then restate the decision with one named mitigation per bias.

## KEY TERMS (plain language)

- **Cognitive bias** — a systematic shortcut in human judgment that produces predictable errors; not stupidity, wiring.
- **Meta-blindness (bias blind spot)** — the inability to see your own biases while actively looking for them; finding none is a warning sign, not a clean bill of health.
- **Distribution shift / drift** — production data slowly stops resembling the data the model was tested on, so old accuracy numbers quietly expire.
- **LLM-as-judge** — using one AI model to grade another's output; useful, but the judge has tastes (verbosity, its own style) that skew scores.
- **BLEU / exact-match** — automated text-similarity scores; easy to measure, weakly related to whether users were actually helped.
- **Stratified sample** — an eval set deliberately built to include the rare and hard cases in proportion, not just the common easy ones.
- **Shadow deployment** — running the AI silently alongside the real process, comparing outputs without users seeing them; the honest dress rehearsal.
- **Inversion test** — asking "if the opposite were true, what evidence would I expect?" and then actually going to look for it.
- **Growth blindspot** — defaulting an AI feature to cost-cutting in a high-margin business, where it barely moves the P&L, while believing AI could grow the business several times more if aimed at revenue.
- **Evidence tiers used below** — ✅ audited/peer-reviewed · ◆ company- or study-disclosed · ⚠ practitioner/roundtable estimate. Numbers marked illustrative are teaching devices.

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../../../UNIVERSAL-SKILL-PROTOCOL.md). At minimum: state the decision in one sentence, and name what a wrong call costs. Then route depth (a full audit for a product decision under ambiguity — model selection, feature scope, rollout — vs. a quick check on a decision already made) and output format. Skip the deep pass when the decision is genuinely data-driven with a clean metric that self-corrects fast (a live A/B test).

## THE PROCESS

1. **Name the decision.** One sentence. If you can't, you don't understand it yet.
2. **Walk the checklist — answer honestly, don't just "check":**
   - **Anchoring** — what was the first number or solution I heard, and am I adjusting from it?
   - **Sunk cost** — is money or time already spent influencing this?
   - **Confirmation** — am I seeking evidence for what I already believe?
   - **Survivorship** — am I studying the successes and ignoring the failures?
   - **Optimism** — am I assuming best-case model performance and adoption?
   - **Authority** — am I deferring because a senior person or "expert" said so?
   - **Bandwagon** — am I doing this because competitors are?
   - **Present** — am I overweighting a fast win against a deferred cost?
3. **Name the dominant bias.** Usually one or two are driving the decision. Name them, with the specific evidence.
4. **Apply the inversion test.** "If the opposite of this recommendation were true, what evidence would I expect to see?" Then go look for it. (For a rigorous version, hand off to `falsification`.)
5. **Restate the decision with the bias priced in.** "We recommend X. The dominant bias risk is Y. We've mitigated it by Z." One mitigation per named bias.

---

# THE THREE STAGES — where the "obvious" feeling attacks

## Stage 1 — what you BUILD (decision biases)

These shape which problems you choose and which solutions you commit resources to.

- **Anchoring** — fixating on the first number you heard (a competitor's accuracy, a vendor's demo, a prior estimate).
- **Sunk cost** — continuing an AI initiative because you've spent six months on it, not because it's right.
- **Survivorship** — building for the customers you kept, not the ones you lost to a rival's better AI.
- **Bandwagon** — choosing a technology because everyone in your space uses it (LLMs, vector DBs).
- **Present bias** — shipping a fast MVP instead of eval infrastructure, then paying for it in production.
- **Novelty bias** — adopting a new architecture because it's exciting, not because it solves your problem better.
- **Growth blindspot** — the costly default in a high-margin business: pointing AI at cost-cutting, where it barely moves the P&L, instead of at revenue, where it has no ceiling.
  - **Why it bites:** costs can only fall to zero, so even a generous cost-cutting case moves firm value ~10% and stops. A lift to the organic *growth* rate is unbounded and gets multiplied by the valuation premium markets pay for growth. Executives believe AI can more than double firm value, yet almost all of them spend it on efficiency.
  - **When wrong:** in a thin-margin or survival-mode business, cost-cutting *is* the growth lever — don't force the revenue framing there. And a growth lift only counts if its source can't be copied, or the efficiency trap just reappears on the growth lever.
  - **Evidence:** the valuation arithmetic is conceptual/◆; the "2.35× / 135% premium in three years" is a ⚠ roundtable-of-execs belief, not an audited outcome — treat it as what leaders *think*, which is the point of naming the bias. (Source: Benartzi, Long & Puntoni, "Companies Are Using AI for Efficiency. They Should Use It to Grow," HBR, 1 Jun 2026. The deep P&L-placement lens lives in `moat-finder`.)

## Stage 2 — how you MEASURE (evaluation biases)

Bias does its most damage here, because evals *look* objective — they're numbers, metrics, test sets — and that is exactly where confirmation bias hides best.

- **Confirmation** — cherry-picking eval examples that confirm the model works; quietly dropping the ones where it fails.
- **Demo bias** — evaluating on a curated set easier than production; the impressive live demo that doesn't represent real usage.
- **Benchmark anchoring** — trusting a published accuracy number without testing on *your* user distribution.
- **Optimism** — assuming 92% in eval means 92% in production, ignoring drift and distribution shift.
- **Evaluation-gap bias** — measuring what's easy to track (benchmark scores) instead of what matters (user outcomes).

**The red flags that give it away:**
- You tested on the 100 *easiest* examples, not the hardest.
- You trained and eval'd on the same happy-path distribution, then met the 50% of production queries never in training.
- You eval'd English-only and shipped globally.
- You used an LLM-as-judge that prefers verbose answers, so your eval looks great while users get bloat.
- You only investigated failures users *reported*, missing the plausible-sounding wrong answers they never caught.

For turning these into a real measurement plan, hand off to `eval-framework`.

## Stage 3 — what the model CARRIES (system biases)

Embedded in the model's training and data; they propagate downstream whether or not you look.

- **Training-data bias** — the model learns majority patterns and fails on minorities and edge cases.
- **Representation bias** — some demographics, languages, or regions are underrepresented in training.
- **Measurement bias** — the metric you optimized doesn't align with what users need.
- **Aggregation bias** — works well on average, fails systematically for a specific segment.
- **Automation bias** — users and operators trust the output uncritically *because* it came from AI, with no human check.

**The compounding case — multi-agent systems.** When you chain agents, these biases don't just persist, they multiply:
- The first agent's training-data bias becomes the second's input bias.
- A confident-but-wrong upstream call gets *amplified* rather than corrected — confirmation bias between agents.
- A 5% error in agent 1 compounds to ~10% across a 2-agent chain, because agent 2 is working from 95%-good inputs.

Audit the chain, not just each agent.

## WORKED EXAMPLE — the AI support agent, four biases compounding

**The decision:** "We'll build an AI agent to handle 50% of inbound support tickets."

- **The demo** (demo + confirmation bias) — the team prototypes on questions the FAQ answers best; 92% accuracy; everyone feels confident. They looked, unconsciously, for examples where it would succeed.
- **The eval** (confirmation + training-data bias) — they eval on the support team's historical FAQ set, mostly common questions. "92% proves we're ready." But that's the exact distribution the model was trained on, and the FAQ is only ~40% of real production queries — the easy 40%.
- **Production** (survivorship bias) — the AI takes 40% of tickets; accuracy drops to 71%. The 60% of queries never in the FAQ — edge cases, multi-part questions, custom requests — were invisible during eval because they weren't in the data the team had ever successfully handled.
- **The cost** — a month of worse support; rolled back to 10% of traffic; two weeks rebuilding the eval process.

Each bias was small. Together they compounded into a **21-point** accuracy drop. **The prevention:** eval on a stratified sample that includes low-frequency queries; eval on production traffic, not the FAQ; have a neutral party curate the eval set; report accuracy *by query complexity*, not just the average; run a two-week shadow deployment before real rollout.

## WHERE THIS SKILL MEETS THE REST OF YOUR STACK

Bias-spotter names the pull and prices it in — it never makes the call itself. That means it always hands off: to a discipline that goes deeper on one stage, and in two cases to the skill that builds the structural fix rather than just naming the risk.

**Goes deeper on one stage:**
- **`rtp-falsification`** — the disciplined version of the inversion test (Stage 1): pre-commit the evidence that would prove the decision wrong, and go find it.
- **`rtp-problem-type`** — when Stage 1's action bias or optimism bias is driving a decision, check whether the real issue is a misdiagnosed adaptive challenge dressed up as a technical one. Bias-spotter names the pull; problem-type resolves that specific confusion.
- **`rtp-first-principles`** — strip the vendor framing and marketing language off a decision *before* you audit it, so you're auditing the real choice.
- **`rtp-eval-framework`** — Stage 2's red flags are symptoms; this is where you build the measurement plan that stops producing them (stratified samples, production-distribution eval sets, reporting by complexity, not just average).
- **`rtp-trendslop-check`** — when the bias isn't in your head but baked into the AI-generated strategy itself (the model defaulting to trendy advice).
- **`rtp-stress-test`** — where the most expensive AI bias (optimism on model accuracy) gets converted into measured evidence at scale.

**Where the diagnosis becomes a structural fix, not just an awareness exercise:**
- **`rtp-moat-finder`** — home of the P&L-placement lens behind the growth blindspot: which line of the P&L an AI investment touches, and that line's ceiling. The second-order risk: an uncorrected growth blindspot doesn't stay a one-decision problem — it skews an entire portfolio toward safe cost-cutting bets. If you're scoring multiple initiatives, run `rtp-ai-portfolio-management` and check whether growth blindspot is shaping the whole slate, not just the one in front of you.
- **`rtp-judgment-guard`** — Stage 3's automation bias ("users trust the output uncritically because it's AI") is a *name*, not a fix. Judgment-guard is where you design the checkpoint — state-first override, a forced second opinion — that actually breaks the uncritical-trust pattern instead of just flagging that it exists.

Run bias-spotter to name and price the bias; run the first group to prove, strip, and pressure-test the decision it's shaping; run the second group when naming the bias isn't enough and the fix has to be structural.

## REALITY CHECK

- **The meta-trap.** Using bias-spotting to *feel* rational while making the biased decision anyway. "We identified automation bias, so we're safe" — no, you named it and then shipped without mitigating it. **Bias awareness is not bias elimination**; the goal is to change the decision or add a safeguard.
- **Diminishing returns.** Beyond two or three dominant biases, more identification adds noise, not signal. Find the consequential ones.
- **Social cost.** Naming biases in a group can feel like a personal attack. Frame it as "the decision's bias risk," never "your bias."
- **The single most expensive AI bias is optimism on model accuracy.** It makes teams *underinvest* in fallbacks, escalation, and monitoring — a 90%-accurate model needs *more* guardrails than a 99% one, and teams often do the reverse.

## QUALITY GATE

- [ ] Decision stated in one sentence
- [ ] Full checklist answered (not just "checked")
- [ ] Dominant bias named with specific evidence
- [ ] The stage identified — build, measure, or carry — and that stage's biases audited
- [ ] Inversion test applied — counter-evidence actually sought
- [ ] Decision restated with bias risk acknowledged and one mitigation per named bias

## OUTPUT FORMAT

```
## Bias Audit: [Decision Name]

**Decision:** [one sentence]
**Stage:** [what you build / how you measure / what the model carries]
**Dominant biases:** [1–2 named biases with specific evidence]
**Inversion test result:** [what counter-evidence was sought, and what was found]
**Risk-adjusted recommendation:** [decision restated with named mitigation]
  e.g. "Proceed. Risk: automation bias from trusting the accuracy number.
        Mitigation: 2-week shadow deployment tracking accuracy by language,
        auto-rollback if multilingual accuracy drops below 80%."
```

## WHEN WRONG

- Low-stakes decisions where speed matters more than accuracy.
- Decisions with clear, measurable outcomes that will self-correct quickly.
- When used as a political tool to block decisions rather than improve them.
- When the team is already over-analyzing and needs to ship.
- With genuine domain experts whose base-rate accuracy is high (a radiologist's clinical read) — use it to sharpen their reasoning, not to second-guess signal.

## TRADE-OFF LEDGER

By running a bias audit, you bet that a few minutes of naming and inverting now is cheaper than committing resources to a decision that felt obvious and wasn't. You give up a little speed and some social comfort. **Reversible?** Fully — this changes no code, only the reasoning behind a choice. **The hidden trade:** the failure mode isn't over-caution, it's the *meta-trap* — naming the bias and feeling smarter while shipping it anyway. The audit is only worth its cost if it ends in a changed decision or an added safeguard. **Confidence: High.** What would change it: a decision already governed by a fast, clean metric, where the audit is ceremony.

## CONCLUSION

Follow the Conclusion Protocol from the [Universal Skill Protocol](../../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 5: state the recommendation (the decision, restated with the bias priced in), name the key trade-off (speed vs. pricing a known risk), acknowledge the biggest risk (the meta-trap — naming without mitigating), and define the next action (the one mitigation, with an owner).

## VISUAL SUMMARY

After the primary output, invoke the **excalidraw-svg** skill for one visual: the "obvious" feeling at the center, with three arrows to the three stages it attacks — BUILD (decision biases) · MEASURE (evaluation biases) · CARRY (system biases) — and the meta-blindness warning drawn as the trap around the whole thing ("finding no bias is the warning sign"). So a viewer sees one mechanism hitting three stages, and why you can't just look inward. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.
