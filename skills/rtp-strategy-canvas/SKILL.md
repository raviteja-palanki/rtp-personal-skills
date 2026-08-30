---
name: rtp-strategy-canvas
version: v1.2_latest
description: 'The AI product strategy skill: what to solve, why only you can win it, and what you do when the model changes under you. Runs the 7-step framework (Objective → Users → Superpowers → Vision → Pillars → Impact → Roadmap) with the moves AI actually changes: separating stable anchors from volatile capability, writing capability-conditional bets (IF model X by date → Path A, ELSE Path B), reset triggers, and a strategy half-life measured in months. Anchors on the 2026 moat thesis: the durable edge is a compounding feedback loop wrapped in a workflow, not the model. Use to set or review an AI product strategy, run a quarterly reset, or push back on a static roadmap. Pairs with: moat-finder (Superpowers), vision-setting (Vision), ai-portfolio-management (Pillars), capability-tracking (what''s volatile), harness-operating-model (harness as moat), token-economics. Triggers: ''AI strategy'', ''product strategy for AI'', ''strategic direction'', ''quarterly strategy reset''.'
imports: [first-principles, moat-finder]
---

# Strategy Canvas — AI Product Strategy

**The objective:** produce a one-page AI product strategy your engineer can explain in thirty seconds and use to say no — one built on what won't change, hedged against what will, and defended by an advantage a competitor can't copy by switching models.

## THE ONE IDEA

**A strategy is a small set of hard choices about where to win and why. AI doesn't change that — it raises the stakes of getting it wrong and shortens the time you have to be right.** Three things follow, and they are the spine of everything below.

1. **Strategy matters more now, not less.** When engineers ship in hours what used to take weeks, the bottleneck stops being execution and becomes direction. A team that can't say what problem it's solving and why now is a team spending its speed on the wrong things. The test that cuts through every strategy doc: *can an engineer or designer explain it in thirty seconds, make a decision with it, and use it to say no?* If not, you have a document, not a strategy.
2. **The model is rented; the moat is what you wrap around it.** Foundation models are commodities every competitor can also license. The durable advantage in 2026 is not the model and not even raw data — it is a *compounding feedback loop wrapped in a workflow*: usage that makes the product better, sitting inside a process a customer would find painful to leave. The model is a brilliant temp worker anyone can hire; your product is the institution that knows the customer's business and would never be fired. (The depth of this lives in `moat-finder`; this skill only forces you to name yours.)
3. **The strategy has a half-life.** A static twelve-month plan against today's capability is obsolete the quarter a new model ships. AI strategy is written to *expire on purpose*: anchored to what's stable, hedged with conditional bets against what's volatile, and wired with triggers that force a re-check before the calendar does. A strategy with no expiration date is a plan.

And the discipline that protects all three: **AI is a thinking partner, not a strategist.** It will stress-test your objective, synthesize your research, and draft the doc. It will not do the original thinking — the judgment you earn sitting with your CEO each week, watching which features died and why, knowing which segment quietly churns. Use it to sharpen the strategy. Do not let it write your choices for you.

## KEY TERMS (plain language)

- **Objective** — the one measurable outcome the strategy exists to move, stated as *mission + measure* ("30-day retention from 18% to 22% by Q3"). Three or fewer, or you effectively have none.
- **Superpower** — an advantage you can actually win with, not "the same as competitors but better." (Named and scored in `moat-finder`.)
- **Stable vs volatile** — what holds for 12+ months (user problems, market structure, regulation) versus what turns in 3–6 (model capability, token cost, competitor parity). Anchor on stable; hedge on volatile.
- **Capability-conditional bet** — a plan written as a branch: *IF [measurable capability] by [date] → Path A, ELSE Path B.* Both paths shippable.
- **Reset trigger** — an event that forces a strategy re-check before the scheduled review (a model jump, a competitor move, a cost cliff).
- **Strategy half-life** — how long before capability change invalidates the strategy; in AI, months, not years.
- **The moat / the loop** — the compounding feedback loop wrapped in a workflow that a competitor can't replicate by switching models.

## THE SEVEN STEPS

The strategy is built in seven steps, sequential but iterative — you loop back constantly. At each step, this skill names the *AI-specific move* and hands the deep work to the skill that owns it.

1. **Objective — write a real one.** Mission plus measure, three or fewer. "Increase activation from 34% to 45% by Q3" is an objective; "build a product customers love" is a wish everyone nods at, which means no choice was made. Focus is saying no to a hundred good ideas. *AI move:* rank candidate objectives by where AI can actually move a metric — friction points, pattern-rich mistakes, data-dense decisions, creative bottlenecks, expertise gaps — and kill the technically fascinating ones that don't map to a user problem.
2. **Users — understand them better than they understand themselves.** Their *stage* and their *job* tell you far more than their demographics. Christensen's milkshake wasn't breakfast; it was "get me through a boring commute." *AI move:* map the trust curve — users don't adopt AI, they build trust with it in a loop. Name the trust thresholds, the collaboration zones, the learning curve, and the fallback when the AI is wrong. (Depth: `jtbd-analysis`, `adoption-launch` for the trust curve.)
3. **Superpowers — fight the battles you can win.** Bad strategy does what competitors do, better. Good strategy picks the fight you're structurally set up to win. *AI move:* find the advantage that survives a model swap — proprietary data that feeds a loop, workflow depth, encoded domain knowledge, switching cost. The one-line test: *if our competitor switches from one model to another tomorrow, does this advantage disappear?* If yes, it's a feature lead, not a moat. (Named and scored in `moat-finder`.)
4. **Vision — show it, don't describe it.** "We'll improve onboarding" tells no one what to build. A prototype is worth ten thousand words. *AI move:* build a "visiontype" — a working prototype (Bolt, Lovable, v0, Replit) that shows the before/after, the human-AI collaboration, and the flywheel getting smarter — in an afternoon, not a quarter. (Owned by `vision-setting`.)
5. **Pillars — choose 2–4 bets as a portfolio.** AI is overhyped short-term and underestimated long-term, so balance: quick wins (1–3 months, build credibility), strategic bets (3–12 months, build the moat), and option plays (cheap experiments on the future). Mark each offensive, defensive, or foundational, and hold explicit ratios. (Owned by `ai-portfolio-management`.)
6. **Impact — model the compounding, not a point estimate.** Traditional impact math breaks on AI because AI products improve with use: each good interaction makes the next one better. Size the learning curve, the network effects, and the second-order impact — that's how you justify a capability that looks expensive on day one. (Unit economics: `cost-model`, `token-economics`.)
7. **Roadmap — features are the output, not the start.** The single most common failure is jumping to "we need a chatbot." Roadmap items come from continuous discovery, not brainstorms or copying competitors. Do Vision → Strategy → Roadmap in that order; the process matters more than the doc. (Owned by the roadmap/discovery skills.)

**Step ∞ — keep updating.** Traditional strategy is refreshed yearly. AI capability moves monthly. Your first AI feature will be mediocre; that's normal. What matters is the learning loop that improves it fast.

## ANTI-PATTERN: THE URGENCY TRAP

Most AI strategies fail before they start, because the objective was scoped wrong, not because the technology underdelivered. The **urgency trap**: leaders pick AI use cases against whatever is easiest to see and measure right now (a dashboard, a cost line, a speed benchmark) instead of against the organization's actual purpose. Every initiative caps out at a faster version of the status quo, because the frame that chose the use case came entirely from the current state. There is no path from "faster" to a new value category, because nobody asked which new category was worth reaching. (HBR, on the urgency trap in AI strategy, Jul 2026.)

**The mechanism:** urgency compresses the time available to define why before jumping to what, and "what's measurable this quarter" is always faster to write down than "what matters in three years." So the rule is simple: never scope an AI initiative from the metric alone. Scope it from mission plus measure (Step 1 above), then check that the metric is a proxy for the mission, not a replacement for it.

The cost shows up in the people, not just the roadmap. Corroborating data, tier ◆ company-disclosed (Upwork / Workplace Intelligence study, population: regular AI users surveyed in 2026): AI-assisted output rose as much as 77% among these users, and burnout rose 88% in the same group. Users who saw no connection between their AI-assisted work and organizational strategy were twice as likely to say they'd consider quitting. The trap doesn't just cap the strategy's ceiling. It burns out the people executing it.

**Where this is wrong:** when the visible, measurable use case genuinely *is* the mission, not a stand-in for one. An AI-assisted runbook that cuts time-to-resolution during a live outage isn't the urgency trap, even though it's urgent and measurable, because the metric is the purpose, not a substitute for a purpose nobody stated.

**Diagnostic (nine questions, three per shift).** The source names three shifts a leader needs to make: prioritize clarity of purpose, resist urgency bias, and advance the vision by acting as a "visionary integrator" rather than a project manager. The nine questions below operationalize those three shift names. They are my own construction, written to make each shift checkable in a real planning meeting, not a verbatim quote from the source.

*Prioritize clarity of purpose*
1. If this initiative succeeds completely, what can the organization do in three years that it cannot do today, stated as a capability, not a metric?
2. Does the objective trace back to the mission statement, or only to this quarter's dashboard?
3. Could someone outside the team building this explain why it matters to the business, not just what it does?

*Resist urgency bias*
4. Would this still be the right use case with a year to decide instead of one quarter?
5. Is the deadline driving the scope, or is the scope driving the deadline?
6. What use case did we reject because it was harder to measure this quarter, and was it actually the more important one?

*Advance the vision as a visionary integrator*
7. Is one person holding the connection between this initiative and the organizational strategy, or has that connection been left implicit?
8. When engineering, design, and finance each ask "why this," does the same answer satisfy all three, or does the story change per audience?
9. Does the roadmap show a path to a new value category, or only a faster version of the current one?

## DESIGN FOR THE HARDEST CONSTRAINT, THEN RELAX UPWARD

**The common path is to build for the well-resourced case and water it down for everyone else. It reliably fails**, and the reverse order produces products that work in both places.

**Start where the constraints are toughest and solve them most efficiently there.** The resulting design travels upward cheaply. The reverse does not: a product built assuming abundant resources has that assumption distributed through every component, and removing it later is a rebuild rather than an adaptation.

**The objection is worth answering directly, because someone always raises it.** If you design for everyone you design for no one. The answer: a broadly attractive product rests on **finding the core value shared across markets**, then making relatively small modifications for price point or feature set. The core persists; the adaptations sit on top.

**The barrier is not engineering, and naming it correctly is what makes it addressable.** Product design has concentrated on well-resourced markets for two centuries, so **a dominant logic forms inside the organization**: the constrained customer becomes invisible rather than rejected. Market data does not dislodge it, because the data is read through the logic. **The intervention is exposure, not analysis.**

**The transfer to AI products, which is where this bites for us.** Your demo context is the wealthy market. The degraded case is the real one:

| The wealthy-market assumption | The constrained reality to design for first |
|---|---|
| A well-formed prompt from someone who knows the domain | A vague prompt from someone still learning it |
| A fresh reviewer with time to read carefully | Someone triaging at the end of a long shift |
| Clean, complete, well-labeled context | Partial context with two fields missing |
| Fast connection, large screen | Neither |

**Build for the bottom row and the top row is free. Build for the top row and the bottom row is a rewrite.**

*(Source: Amos Winter and Vijay Govindarajan on the HBR IdeaCast, "The Innovation Strategy Most Companies Miss," Aug 2026, drawing on their book *Global by Design* — ⚠ conversation-tier with no figures, populations or effect sizes. **The named examples are chosen because they worked**, which is survivor selection and should be flagged whenever the argument is repeated. The transfer to AI product contexts is this corpus's. Falsifier: a product line built for the well-resourced market that adapted downward as cheaply as a constraint-first design adapted upward.)*

## WHAT AI ACTUALLY CHANGES — the adaptive layer

Steps 1–7 are strategy. This is the part that is *specifically* AI, and it's where most teams go static.

**Separate stable from volatile, then hedge the volatile.** Put every assumption in one of two columns. *Stable (12+ months):* the user problem, market structure, regulation, your org's real capabilities. *Volatile (3–6 months):* model capability, token cost, competitor parity, context limits. **Anchor the strategy on the stable column; write the volatile column as conditional bets.** If more of your strategy rests on volatile assumptions than stable ones, the next major model release forces a rewrite.

**Write bets as branches, not hopes.** Each major bet: *IF [measurable capability] by [date] → build Path A, ELSE build Path B.* Example: "IF multi-step reliability clears 85% success with under two errors per ten steps on our eval by Q2 → ship the autonomous mode; ELSE → ship the co-pilot mode." Two rules keep this honest: the trigger is a *number someone can check quarterly* (not "when the team feels confident" — that's a decision you're deferring), and Path B is something you'd *ship and be proud of* (not "we'll reassess" — that's Plan A with a panic button).

**Wire reset triggers — the strategy re-checks itself.** Five events force a strategy conversation *before* the next quarterly review, not after:

| Trigger | Fires when | What it forces |
|---|---|---|
| **Capability jump** | a model ships >~15% better on *your* benchmark | re-check the bets — a feature you planned may now be in the base model |
| **Competitor parity** | a rival ships something in your 6-month plan | re-test the moat: does your edge hold if they have it? |
| **Cost cliff** | inference cost drops materially (~40%+) | use cases that were uneconomic are now viable — the build list changes |
| **Assumption broken** | 4+ weeks of your own data disprove a core "users want X" | revisit the *bet*, not just the feature |
| **Regulatory signal** | guidance/enforcement lands in your regulated vertical | the autonomy and safety bets change; don't wait |

If your triggers never fire across six months, they're too vague — sharpen the numbers.

**Name your strategy's half-life.** Roughly: frontier features (0–3 months) are triggers, never foundations — strategy built there is dead on arrival; competitive features (3–6 months) are conditional bets, expect to adjust twice a year; market structure (6–12) and user problems (12+) are your anchors. Build primarily on the 6–12 month layer.

## THE ONE-PAGE CANVAS (the deliverable)

```
STRATEGY CANVAS — [Product]
OBJECTIVE       | mission + measure, ≤3. "[X] from [a] to [b] by [date]."
STABLE ANCHORS  | user problem · market structure · regulation · org capability (12+ mo)
VOLATILE        | model capability · token cost · competitor parity (3–6 mo)
SUPERPOWER/MOAT | the loop-in-a-workflow a model swap can't copy (→ moat-finder)
BETS            | IF [measurable trigger] by [date] → Path A, ELSE Path B (both shippable) ×3
RESET TRIGGERS  | capability jump · competitor parity · cost cliff · assumption broken · regulatory
HALF-LIFE       | 3 / 6 / 12 months — because [reason]
NEXT REVIEW     | a specific date, ≤90 days out
```

One page. If it doesn't fit on one page, you haven't made the choices yet.

## WHAT THIS SKILL CONSUMES & PRODUCES

Strategy is the *conductor* — it takes the outputs of the discovery and analysis skills and turns them into one page of choices that the build skills execute against.

**Consumes (inputs):**
- **The objective/metric to move** — from `north-star-metric` or the business goal.
- **User understanding** — the job and the trust curve, from `jtbd-analysis` + `adoption-launch`.
- **The named, scored moat** — from `moat-finder` (the Superpowers step).
- **What's volatile / build-now-vs-wait** — from `capability-tracking`.
- **The unit economics behind a bet** — from `cost-model` / `token-economics`.
- **Competitor parity signals** — from `competitive-map` / `signal-scanner`.

**Produces (outputs):**
- **The one-page canvas** (objective · stable/volatile · moat · conditional bets · reset triggers · half-life) → the source of truth every downstream skill reads.
- **The portfolio pillars** → `ai-portfolio-management`; **the vision** → `vision-setting`; **the roadmap** → the discovery/roadmap skills.
- **The strategic frame for each feature** → `ai-prd` (a PRD that doesn't trace to a canvas bet is off-strategy).
- **The board/stakeholder narrative** → `stakeholder-communications`; **the quarterly reset** → the `strategy-review` command.

## WHERE THIS SKILL MEETS YOUR STACK

This skill is the *conductor* — it runs the seven steps and hands each one's depth to its owner. Route, don't re-teach:

- **The Superpowers/moat step → `moat-finder`** (Helmer's 7 Powers, the loop-is-the-moat thesis, scoring). This skill only forces you to *name* your moat and pass the model-swap test.
- **The Vision step → `vision-setting`** (show-don't-describe, visiontypes); **the Pillars step → `ai-portfolio-management`** (quick-wins/strategic-bets/option-plays, ratios); **the Users step → `jtbd-analysis` + `adoption-launch`** (the trust curve).
- **What's volatile, and build-now-vs-wait → `capability-tracking`**; **the harness as the model-agnostic asset on your canvas → `harness-operating-model`** (owns the economics/moat of the harness) and `agent-harness` (owns the architecture). Put "harness maturity" on the canvas; design it there.
- **Unit economics behind a bet → `cost-model` / `token-economics`**; **is this strategy real or is the model doing my thinking → `trendslop-check`** (guards against the AI-hype and the value-per-dollar traps).
- **Caution on strategic-center menus.** If a strategy conversation reaches for a menu of "where to center the strategy," such as McGrath's five strategic centers (technology, customer, ecosystem, and others), treat the options as ranked, not neutral, once AI commoditizes capability. Technology-centered strategy is the center a rented, falling-cost, commoditized capability kills fastest: a foundation model can close a technology-centered edge in one release cycle. Customer-centered and ecosystem-centered strategy are the two exclusivity plays that hold value under AI-driven commoditization, because they rest on relationship and network, not on a capability anyone can now license. This is wrong for a company whose actual moat is proprietary data or regulatory access, both centers outside this menu; check the Superpowers step before applying the ranking. (HBR management-tips compilation citing McGrath, Jul 2026.)

The spine: **this skill decides where to play and why you win; the stack does the deep work of each choice.**

## DIAGNOSTIC QUESTIONS

1. Can an engineer or designer explain this strategy in thirty seconds and use it to say no? If not, it's a document, not a strategy.
2. Is your objective *mission + measure*, and do you have three or fewer? (More than three = zero, because every team cherry-picks.)
3. For each bet: is it anchored to something stable, or to a volatile capability that needs a conditional trigger and a real Path B?
4. If a competitor switches models tomorrow, does your moat survive? If it evaporates, it was a feature lead — name the loop that wouldn't.
5. What fires a strategy reset before the next review — and would your team recognize it when it happens?
6. What's the strategy's half-life, and are you building on the 6–12 month layer, not the frontier?
7. Where are you letting AI do the thinking instead of the sharpening?

## QUALITY GATE

- [ ] Objective is mission + measure, ≤3, and would make someone in the room push back.
- [ ] Stable and volatile assumptions are in separate columns; the strategy anchors on stable.
- [ ] Every major bet is a branch — measurable trigger, dated, with a Path B you'd ship proudly.
- [ ] The moat passes the model-swap test and names a compounding loop, not a feature (→ `moat-finder`).
- [ ] The five reset triggers are documented with numbers, not feelings.
- [ ] The strategy is one page, with a named half-life and a next-review date ≤90 days out.
- [ ] The deep work of each step is routed to its owner skill, not re-decided here.

## WHEN WRONG

Don't reach for this skill pre-product-market-fit, where experimentation beats strategy and a formal canvas is procrastination in a suit; or when the market is so new there's no stable column to anchor on (then the whole strategy is one big option play — say so); or when the team needs to *execute* and "we should revisit the strategy" has become a way to avoid shipping. And keep the humility the frontier demands: **you will be wrong about capability timelines.** The point of the conditional bets and reset triggers isn't to predict the future — it's to make being wrong cheap and recoverable instead of a rewrite. A strategy that can't be invalidated isn't rigorous; it's just untestable.

---

## TRADE-OFF LEDGER

Complete the Trade-Off Ledger from the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 3.

## CONCLUSION

Follow the Conclusion Protocol from the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 5: state the recommendation (a direction, not "it depends"), the hypothesis ("we believe X moves Y because Z; we're wrong if [signal] by [date]"), the key trade-off, the biggest risk with its mitigation, and the next action by role and date.

---

## VISUAL SUMMARY

After completing the primary output, invoke the **excalidraw-svg** skill to create a single visual: the seven steps as a spine, the stable-vs-volatile split as two columns, the bets as IF→A/ELSE→B branches, and the moat plotted on a fragile (model-dependent) ↔ durable (loop-in-a-workflow) axis. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.
