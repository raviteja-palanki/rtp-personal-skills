---
name: ai-product-metrics
version: v1.0_latest
description: 'Pick the leading indicators that actually predict AI product health — acceptance, correction, regeneration, conversational burden, cost-per-successful-outcome, and the 5-stage AI funnel (Surfaced -> Invoked -> Completed -> Accepted -> Retained) — because DAU and retention are lagging indicators that miss model regressions. Also carries the two moves most metrics decks skip: reading the dashboard as a demand-signal aggregator (evals as discovery), and the executive-translation layer that turns an eval-score move into the business number a CFO/GC/COO/CHRO acts on. Use when designing an AI metrics dashboard, debugging why DAU is stable but users complain, mapping North Star + AARRR for AI, or translating eval scores for a board. Pairs with: eval-framework, feedback-flywheel, confidence-tuner (is the judge trusted), cost-model/token-economics, stakeholder-communications, fit-signal. Triggers: "AI metrics", "North Star metric", "acceptance rate", "AI funnel", "cost per successful outcome".'
imports:
  - eval-framework
  - feedback-flywheel
  - confidence-tuner
---

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md):
1. Ask the Grounding Questions (Section 1) — at minimum: Who is the customer? What problem? What are we saying YES to and NO to?
2. Route depth: Executive Summary or Comprehensive Analysis?
3. Identify output format: Document, presentation, spreadsheet, or inline?

Then proceed with the skill-specific analysis below.

---

## THE ONE IDEA

**A metric earns its place on an AI dashboard only if it moves when the product genuinely succeeds or fails for a real user. Everything else is a lagging proxy (DAU, retention) or a gameable one (accuracy %, session count).** That single test reorganizes the whole dashboard, and three consequences fall out of it:

1. **Measure cost per *successful outcome*, not per token or per call.** The denominator is "a user actually got a useful result," never "the model emitted something." This is now where the market is heading — 2026 pricing repriced from seats to outcomes (see the cost section).
2. **Read the dashboard as a demand-signal aggregator, not just a health monitor.** Correction clusters and the review queue are a live stream of unmet needs — offense, not just defense. Most decks use metrics only to catch regressions; the sharp move is using them to find the roadmap.
3. **Ship the executive-translation layer, or the evidence stays invisible.** An eval-score move ("context recall −4%") means nothing to a CFO until it's translated to the number they act on ("support tickets +12%, ~$X margin"). The metric and its translation are one artifact, not two.

**Where are you on the maturity ladder?** (the series' *Three Eras of Evaluation*, applied to metrics)

- **Era 1 — Benchmark metrics.** MMLU, leaderboard scores. Say nothing about *your* product. If your dashboard is model benchmarks, you're not measuring your product yet.
- **Era 2 — Product metrics.** Acceptance rate, cost-per-successful-outcome, the AI funnel, pass^k. Where most "advanced" teams live. Most of this skill lives here.
- **Era 3 — Trajectory metrics.** For agents: was the 10-step *path* safe, efficient, faithful — not just the final answer. Conversational burden and per-step pass^k are the entry points.

Each era layers on; it doesn't replace the prior one. Name where your dashboard actually is before adding metrics.

**Red flag**: "Our DAU is up, retention is up." But users are regenerating outputs constantly, correcting AI mistakes, or doing manual work despite having AI.

**Green flag**: You track acceptance rate, correction patterns, conversational burden, and cost-per-successful-outcome — and every top-line number has a translated business equivalent next to it. You catch degradation before DAU drops, and you mine corrections for the next feature.

---

## KEY TERMS (plain language)

- **Leading vs. lagging indicator** — a signal that moves early (acceptance rate, correction rate) versus one that moves late (DAU, retention, revenue).
- **Acceptance / correction / regeneration rate** — how often users accept, fix, or re-run AI output; the core leading signals of AI quality.
- **Cost per successful outcome** — the cost of a user actually getting a useful result, not the cost per API call.
- **Conversational burden** — how much effort the user spends getting the AI to do its job (turns-to-success, rephrases, corrections). 15 turns of re-prompting can "succeed" while the product fails; a trajectory-era metric that bridges evals and UX.
- **Evals as discovery** — using the metrics dashboard and correction/review queue as a demand-signal aggregator: a cluster of failures on one intent is a roadmap blind spot, not just a bug.
- **Executive translation** — the layer that maps an eval-score or leading-indicator move into the number each stakeholder acts on (CFO margin, GC compliance posture, COO escalation, CHRO skill-mix).
- **North Star + AARRR** — the one company-level metric, plus the Acquisition / Activation / Retention / Revenue / Referral funnel.
- **The AI funnel** — Surfaced → Invoked → Completed → Accepted → Retained; where AI-quality drop-offs happen.
- **Value chain (enablement → creation → realization)** — asset quality (before use) → usage → revenue; the causal spine a dashboard should be ordered on.
- **Goodhart's law / anti-metric** — when a measure becomes a target it stops being a good measure; build metrics that resist being gamed.
- **Instrument blindness** — when the measure you already collect (e.g. satisfaction) is the one least able to detect the problem you care about.

## THE TRAP

**The "Vanity Metrics" Trap**

DAU goes up. Retention looks good. But your AI is producing garbage that users fix manually. You don't notice because:

- DAU measures usage, not value
- Retention measures habit, not satisfaction
- Time spent could mean "struggling" not "succeeding"
- Revenue could be from frustration (users buying more credits to re-run failed outputs)

Traditional metrics lag. By the time DAU drops, you've already lost users' trust.

**The "Accuracy Theater" Trap**

You measure eval accuracy at 94%. Users say the product is broken. Why?
- Accuracy is unweighted (wrong answer to important question == wrong answer to trivial question)
- Doesn't measure "trust calibration" (does the model know when it's wrong?)
- Ignores the distribution of errors (10 errors on 1000 simple questions, or 1 error on 10 hard questions?)

**The "Satisfaction Blindness" Trap**

A satisfaction/CSAT score cannot detect persona-driven harm — and for an AI-as-teammate surface (a writing critic, a code-review bot, an automated feedback tool) it is, in a controlled study, the *least sensitive* channel to that harm. High adoption and high friction routinely coexist: people keep using a tool they *have* to use while quietly working around it, and report neutral satisfaction the whole time. So pair any satisfaction number with a **friction proxy** as a required check, not a nice-to-have: turn-length ratio, rephrase rate, and override/argue-attempt rate. If friction rises while satisfaction stays flat, believe the friction. *(When wrong: these log proxies are once-removed from the underlying evidence and aren't validated to correlate at equal strength — a directional check, not proof. Source: "Does Your AI Have a Personality Problem?", HBR, 24 Jun 2026; self-report null + friction signals ◆.)*

---

## THE PROCESS

**1. Define Your Leading Indicators**

These predict product health before revenue metrics move:

- **Acceptance Rate**: What % of AI outputs do users accept as-is? (Target: 70%+)
- **Regeneration Rate**: How often do users re-run the same prompt? (Target: < 10%)
- **Correction Rate**: What % of outputs do users edit before using? (Target varies by domain)
- **Conversational Burden**: Turns-to-success — how many exchanges (re-prompts, corrections, clarifications) before the user gets a usable result? (Target: as few as the task honestly needs; watch the *trend*, not an absolute.) A task that "succeeds" in 15 turns is a failure the acceptance rate alone will miss. This is the trajectory-era metric — it measures the *path*, not just the endpoint.
- **Abandonment Rate**: Tasks users start but never complete with the AI
- **Cost-per-Successful-Outcome**: Actual money spent per task the user marks "done"

**2. Measure Hallucination + Trust Calibration**

- Track: False positive rate (AI says X with high confidence, but X is wrong)
- Track: Confidence gap (does AI confidence correlate with accuracy?)
- Monitor: User corrections to AI claims (high correction rate = low trust)

**3. Layer in Efficiency Metrics**

- Latency (p50, p95, p99 — tail matters)
- Token efficiency (are prompts getting bloated?)
- Cost per output (includes model cost + infrastructure)
- Cost per successful outcome (adjusted for acceptance rate)

**The market is repricing around this exact denominator.** Cost-per-successful-outcome stopped being a purely internal metric in 2026 — it became the *price*. Hybrid/outcome-based pricing rose from 27% to 41% of AI vendors between 2025 and 2026 ⚠, with published per-outcome prices: HubSpot's Customer Agent at $0.50 per resolved conversation (halved from $1.00), Intercom at $0.99 per resolution, Help Scout at $0.75 ◆. The implication for your dashboard: if a competitor can name their price per successful outcome and you can't name your *cost* per successful outcome, you can't defend your margin or your pricing. This metric is now a strategic instrument, not just an ops number. *(When wrong: outcome pricing is the hardest model to operationalize — you have to define "success" unambiguously and handle partial success/disputes; if "success" is fuzzy, the metric is fuzzy too. Tier: vendor-published prices ◆, market-share shift ⚠.)*
*(Sources: [Bessemer — AI Pricing & Monetization Playbook](https://www.bvp.com/atlas/the-ai-pricing-and-monetization-playbook); [Flexprice — 7 Pricing Metrics That Capture AI Value, 2026](https://flexprice.io/blog/7-pricing-metrics-capture-ai-product-value).)*

**4. Build Cohort Dashboards**

Slice by:
- User segment (power users vs. casual)
- Task complexity (simple vs. reasoning-heavy)
- Model version
- Prompt version

Catch degradation in specific segments before it hits company metrics.

**5. Set Regression Thresholds**

- Acceptance rate drops > 3%? Investigate.
- Regeneration rate jumps > 20%? Alert.
- Cost per output increases > 10%? Check prompt version.
- Hallucination rate spikes > 2%? Pause releases.

**6. Track pass@k and pass^k Metrics (Anthropic Framework)**

These consistency metrics measure whether your system is capability-limited or consistency-limited:

- **pass@k**: Probability of at least one correct solution in k attempts. Answers: "Can the system succeed if given multiple tries?" Use for: development, capability benchmarking, research, understanding raw capability.
- **pass^k**: Probability that ALL k trials succeed consistently. Answers: "Will every interaction work reliably?" Use for: production readiness, SLA commitments, customer-facing agents where every interaction must work.

**Decision table:**
| Scenario | pass@k | pass^k | Diagnosis | Action |
|----------|--------|--------|-----------|--------|
| High pass@k, low pass^k | 0.80+ | 0.33- | Capable but inconsistent | Improve determinism: few-shot examples, temperature tuning, structured outputs |
| Both low | 0.50- | 0.20- | Capability problem | Retrain, change model, redesign prompts |
| Both high | 0.90+ | 0.85+ | Production ready | Scale confidently, monitor drift |

**Real example**: A coding agent with pass@1 = 0.8 (80% success rate) has pass^5 = 0.33 (33% chance all 5 solutions work). That's a 67% failure rate for multi-step tasks. Customers see failure, even though the system is 80% capable.

For customer-facing agents, track pass^k not pass@k. A single failure in a sequence damages trust more than raw capability metrics suggest.

**7. Define Anti-Metrics (What Going UP Would Be Bad)**

Most metric frameworks define what success looks like. Anti-metrics define what a dangerous signal looks like — a metric that's increasing but shouldn't be.

**The pattern:** For every primary metric, ask: "What metric going UP would actually signal a problem?"

| Primary Metric | Anti-Metric | Why It's Dangerous |
|----------------|-------------|-------------------|
| DAU (Daily Active Users) | Session count with no task completion | Users are coming back because the AI keeps failing — they're retrying, not succeeding |
| Acceptance rate | Acceptance rate + zero edits on complex tasks | Users may be blindly accepting AI output without reviewing. Over-trust is a failure mode, not a success signal |
| Feature adoption | Adoption + increased support tickets | Users are adopting but can't figure it out — adoption without competence |
| Time in product | Time in product + low task completion | User is stuck, not engaged. High time-on-task in a productivity tool means friction, not value |
| Cost reduction | Cost reduction + declining quality scores | You cut cost by degrading quality. The savings are temporary — churn follows |

**Process:**
1. For each primary metric and guardrail metric, define its anti-metric
2. Monitor anti-metrics alongside primaries on the same dashboard — never in isolation
3. If a primary metric is trending up AND its anti-metric is also trending up, investigate before celebrating. The growth may be masking a deeper problem.

**The check that catches perverse incentives:** Anti-metrics are the systematic defense against Goodhart's Law — "when a measure becomes a target, it ceases to be a good measure." By defining what going UP would mean going WRONG, you force the team to think about gaming, over-optimization, and unintended consequences.

**8. Detect Eval Saturation**

When your eval suite stops moving despite meaningful improvements in production, your metrics have plateaued. Signs include:

- All metrics are green, but users still complain or support tickets spike
- Scores haven't moved in 3+ months despite launches and iterations
- New model versions show no improvement on evals, but users perceive them as better (or vice versa)

**Root cause**: Your eval set is stale. It measures what you've already solved, not what breaks in production.

**Fix**: Refresh eval sets monthly. Replace 20-30% of eval dataset with real production traces — actual user inputs that failed, edge cases you didn't anticipate, novel task types. Track eval "difficulty score" — if average difficulty drops over time, your suite is getting too easy.

**Process:**
1. Monthly: Pull top 20-30 errors from production logs
2. Add to eval set, removing lowest-signal existing examples
3. Measure: Does this new eval version show measurable gaps in your system?
4. Iterate: If new evals don't expose problems, you're not testing hard enough

---

## NORTH STAR + AARRR FOR AI PRODUCTS

The metrics above (acceptance rate, regeneration rate, hallucination rate, pass^k) are AI-specific leading indicators. They tell you whether the model is doing its job. They do not tell you whether the *product* is doing its job.

For that, you need the foundational metric framework — North Star + AARRR — adapted for AI features. Lenny Rachitsky's North Star guide is the canonical reference. AARRR (Acquisition / Activation / Retention / Revenue / Referral) is the canonical funnel. Both are PM table stakes. The AI twist is what they look like when the product is non-deterministic.

### The North Star for AI Products

**The Lenny criteria for a North Star metric:**
1. Represents value delivered to users (not value extracted from them)
2. Predicts long-term revenue
3. Measurable
4. Actionable (the team can move it)
5. Understandable (everyone in the company can explain it)

**The AI-specific failure mode:** Most AI products pick a North Star that ignores AI quality. "Daily active users." "Queries per day." "Sessions per week." These are activity metrics — they go up when users come back, regardless of whether the AI did its job.

**The 0.1% angle: AI features need a "successful AI interaction rate" North Star that pure DAU/retention misses.**

The pattern: pick the North Star metric AT the moment of AI-driven value delivery. Not "users who logged in" — "users who completed a successful AI-assisted task." Not "queries per session" — "queries that produced a user-accepted output."

**The canonical AI-feature funnel (the five-stage model):**

| Stage | Definition | What "Good" Looks Like |
|---|---|---|
| **Surfaced** | The AI feature was visible to the user (in their UI, in their workflow) | High — the feature is discoverable |
| **Invoked** | The user actually used the feature (typed a prompt, clicked the button) | Conversion from surface depends on UX clarity |
| **Completed** | The AI finished generating an output (no timeout, no refusal, no error) | High — model and infra reliability |
| **Accepted** | The user kept the output (used it, copied it, sent it, saved it) | The acceptance rate metric — the truth about quality |
| **Retained** | The user came back and used the feature again within 7 days | The trust metric — did the experience earn repeat use? |

Each stage has a drop-off. Each drop-off has a different optimization. **The North Star sits at "Accepted" or "Retained" — never at "Invoked."** Invocation is activity. Acceptance is value.

**Worked example:**

For an AI contract review tool, candidate North Stars:

- **Bad:** "Daily active users" — measures coming back, not value
- **Bad:** "Queries per day" — measures activity, not success
- **Bad:** "Reviews completed" — measures throughput, not whether the review was useful
- **Better:** "Reviews accepted by user without edit" — measures whether the AI's output was good enough as-is
- **Best:** "Weekly active users who accept at least 3 reviews per week" — combines retention, activity, and quality into one metric

The "best" version satisfies all five Lenny criteria. It moves only when the product is genuinely working. It can't be gamed by adding more users or running more queries.

### AARRR Adapted for AI Features

The AARRR funnel applies to AI products, but each stage gets an AI-specific layer.

#### Acquisition

The user discovers the feature exists. Same as any product — marketing, search, word of mouth, in-product placement.

**The AI-specific twist:** Unlike traditional features, AI features benefit from social proof signals that signal "this AI doesn't suck." Demo videos showing real outputs. Customer logos. Eval transparency. Hallucination rates published openly. Trust signals at acquisition time reduce the "is this just AI hype?" friction.

**Metric:** Trial conversion rate from acquisition channel. Watch for big variation by channel — power-user channels (developer communities, expert forums) often convert at 3-5x the rate of generic channels because the audience already trusts AI and knows how to use it.

#### Activation

The user experiences first value. For AI features, this is the first successful interaction.

**The AI-specific twist:** Activation is about whether the user's *first prompt produces a useful output*. If the first prompt fails or feels wrong, churn risk in the first week is 3-5x higher than for users whose first prompt succeeded. The first impression is load-bearing.

**Metric:** First-prompt acceptance rate. Measures: of users who tried the feature once, what % accepted the AI's output without editing or regenerating?

**Optimization:** First-time user experience matters more in AI products than traditional ones. Show example prompts. Suggest queries. Pre-populate the input with a high-confidence template. Get the user to a "yes, this worked" moment in their first 60 seconds.

#### Retention

The user comes back and uses the feature again.

**The AI-specific twist:** Trust takes 4 weeks to stabilize (per the `uncertainty-research` skill). A user who uses the feature 3 times in week 1 and never returns has been quietly disappointed. A user who uses it 1 time per week for 8 weeks has built durable trust. Track retention curves by week, not just by month.

**Metric:** Weekly active acceptance rate — % of weekly actives who accepted at least one AI output that week. Catches users who keep coming back but stop accepting outputs (a sign of declining trust before churn).

**Optimization:** The biggest retention lever in AI products is fixing the failure modes that surface in week 2-3. Users tolerate week-1 errors as "I'm still learning." They don't tolerate week-3 errors. The eval-and-quality work compounds at retention.

#### Revenue

The user pays. For AI products, this often shows up as: free tier users converting to paid, paid users upgrading to higher tiers, expanding seat count.

**The AI-specific twist:** AI features have unit cost. Revenue without unit economics modeling produces "we have $1M ARR and burn $1.2M on inference" surprises. Track revenue PER unit of AI capacity consumed. Track revenue versus cost-per-successful-outcome (the metric from the Process section above).

**Metric:** Net revenue per user, after AI cost. Not gross. The AI cost is the real margin compression.

**Optimization:** The pricing model should align with the cost structure. Per-seat pricing (flat fee per user) is a margin trap if power users consume 10x the AI capacity of casual users. Usage-based pricing aligns better but requires the user to understand and accept variable bills. The right answer depends on segment — enterprise often prefers flat, prosumer often prefers usage-based.

#### Referral

The user invites others.

**The AI-specific twist:** AI products have a unique referral mechanism — *output sharing*. When a user copies an AI output and pastes it into Slack, email, or a doc, the recipient sees the output AND the implicit endorsement. Track output-shared rate as a leading indicator of organic growth.

**Metric:** % of accepted outputs that were shared externally. Higher = organic referral surface area.

**Optimization:** Make sharing easy. Watermark outputs subtly with the product name (without compromising the user's intent). Offer "share this answer" affordances. Track which outputs get shared most — they reveal which use cases produce shareable artifacts and which produce private ones.

### Mapping the AI Funnel to AARRR

The five-stage AI funnel (Surfaced → Invoked → Completed → Accepted → Retained) maps onto AARRR but isn't identical. Use both:

| AARRR | Maps to AI Funnel | Why Both Matter |
|---|---|---|
| Acquisition | Pre-Surfaced | User has to find the product before the AI funnel begins |
| Activation | Surfaced + Invoked + Completed (first time) | Activation in AI = first successful interaction |
| Retention | Repeated Acceptance + Retention | Coming back AND accepting outputs |
| Revenue | (Conversion event, separate) | Often gated by retention |
| Referral | Output Sharing | Distinct from formal referral programs |

**The discipline:** Build dashboards that show both. AARRR for the business view (where executives think). The five-stage AI funnel for the product view (where PMs and engineers diagnose). They tell the same story at different altitudes.

### The Combined Dashboard Structure

Add this to the dashboard template in the section above. The North Star + AARRR sit *above* the AI-specific metrics — they're the company-level view that the AI quality metrics support.

```
NORTH STAR METRIC: [e.g., Weekly active users who accept ≥3 AI outputs per week]
Current: [Value]    Target: [Value]    Trend (4w): [↑/↓]

AARRR FUNNEL
| Stage | Metric | Current | Target | Trend |
|---|---|---|---|---|
| Acquisition | Trial conversion rate | — | — | — |
| Activation | First-prompt acceptance rate | — | — | — |
| Retention | WAU with ≥1 acceptance | — | — | — |
| Revenue | Net revenue per user (post-AI cost) | — | — | — |
| Referral | % outputs shared externally | — | — | — |

AI FUNNEL (per primary feature)
| Stage | Conversion | Drop-off Reason | Action |
|---|---|---|---|
| Surfaced → Invoked | — | — | — |
| Invoked → Completed | — | — | — |
| Completed → Accepted | — | — | — |
| Accepted → Retained (7d) | — | — | — |
```

The discipline: every drop-off in the AI funnel ladders up to a drop-off in AARRR. If first-prompt acceptance is low, AARRR Activation is low. If accepted-to-retained conversion is low, AARRR Retention is low. The funnels aren't separate diagnoses — they're the same diagnosis at different altitudes.

### The Value Chain Your Dashboard Should Be Ordered On: Enablement → Creation → Realization

The funnels above measure *creation* (usage) and *realization* (revenue) well, but they don't name the tier *underneath* both: the quality of the AI asset itself, before anyone uses it. A board-legible AI dashboard has three tiers in causal order:

- **Value enablement** — the quality of the asset *before* anyone uses it: eval pass rates, golden-dataset coverage, data freshness. (Caterpillar's version: the count of accurate "trifecta" records on the platform.)
- **Value created** — usage and its trajectory: acceptance rate, invocations, how fast usage is growing (the AARRR + AI-funnel view above).
- **Value realization** — revenue attributable to the AI solution (the income-statement line).

The point is the *causal chain*: realization is downstream of creation, which is downstream of enablement. Reporting all three together is what lets leadership trace a multi-year platform investment to the P&L — and it's exactly the report that sustained a six-year program at Caterpillar when revenue alone would have looked flat for years. Enablement is the tier that survives long timelines because it moves first; most AI dashboards jump from leading indicators straight to business outcomes with no named asset-quality tier.

**Why it matters:** without the enablement tier, a slow-to-realize platform investment looks like failure on the dashboard for years and gets killed before the revenue line turns. **When this is wrong:** this is one access-privileged case (the authors ran the program; internal figures are self-calculated). Cite the *triad structure* at full confidence as a reporting lens; treat Caterpillar's outcome numbers as directional. For a fast product cycle the tiers still apply, but the multi-year patience they enabled does not transfer.
*(Source: "Data Transformation Is the CEO's Business," MIT Sloan Management Review, 21 May 2026 — CISR value-monitoring triad; anchor: Caterpillar services revenue $14B (2016) → $24B (2024) ◆, [Caterpillar 2024 Annual Report](https://www.caterpillar.com/en/investors/reports/annual-report/ceo-message.html).)*

---

## THE DASHBOARD IS A DEMAND-SIGNAL AGGREGATOR (Evals as Discovery)

Every section above uses metrics *defensively* — to catch regressions before DAU drops. That's half the value. The sharper, more contrarian half: **a metrics dashboard is a live map of unmet needs. Read it offensively and it becomes your roadmap.**

The mechanism is simple. When users correct, regenerate, or abandon, they are telling you exactly where the product fails to do the job. Aggregate those failures and they *cluster* — and a cluster is not a bug, it's a demand signal.

- **The correction stream is user research that already happened.** Every edit is a user showing you the gap between what the AI produced and what they needed. You don't have to schedule interviews; the edit distance already logged it.
- **The review queue is a stream of unmet needs.** The traces a human had to step in on are the exact tasks the product can't yet do alone. That queue *is* the "what should we build next" list.
- **A cluster is a roadmap item, not a defect.** When ~15% of failures pile onto one intent or task type, that's not a QA ticket — it's a product blind spot big enough to be a feature. The team that treats it as "fix the bug" patches a symptom; the team that treats it as "we've discovered an unmet need" ships the thing users were straining to get.

**The move:** add a *failure-clustering* view to the dashboard — group corrections/regenerations/abandonments by intent, task type, and persona, ranked by volume × severity. Review it in the same cadence as the health metrics, but ask a different question: not "what regressed?" but "what are users repeatedly failing to get, and is that a feature?" This is where the metrics work feeds `feedback-flywheel`, `jtbd-analysis`, and `opportunity-solution-tree` — the dashboard stops being a rear-view mirror and becomes a discovery instrument.

*(When wrong: a cluster can be a genuine defect, not a demand signal — a retrieval bug that mangles one intent looks identical to unmet demand for that intent until you read the traces. Cluster detection routes you to the traces; it doesn't diagnose for you. See `production-observability` for trace-level root-causing before you promote a cluster to the roadmap.)*

---

## THE EXECUTIVE-TRANSLATION LAYER (the metrics execs actually read)

Here is the failure that kills objectively-successful AI initiatives: the metrics are healthy, the eval scores climb, cost-per-outcome drops 65% — and the initiative still loses executive support, because none of that was ever translated into the language the executive makes decisions in. **An eval-score move is invisible until it becomes a business number.** The metric and its translation are one artifact, not two.

### Eval score → business outcome

The first translation is the most-skipped: connect a leading indicator to the lagging business outcome it predicts, with the mechanism named.

- "Context recall −4% this week" → "support tickets +12% next week, ≈ $X in deflection lost." *(This is "evals are the new PRD" applied to the dashboard: the score is only worth reporting if you can state what business number it moves.)*
- "Acceptance rate −3% on complex tasks" → "power-user churn risk up; those cohorts drive Y% of expansion revenue."
- "Cost-per-successful-outcome +15%" → "gross margin −Z points at current volume."

Build this mapping once, keep it on the dashboard, and every metric review becomes a business review.

### The four stakeholder translations

Each executive speaks a different language and holds a different decision framework. The PM is the only role holding all of them at once — the Bridger archetype, operationalized on the dashboard. Pair every technical metric with its translated equivalent:

| Stakeholder | They care about | Translate your metric into |
|---|---|---|
| **CFO** | gross margin, unit economics | cost-per-successful-outcome trend → "margin protection: −65% cost/outcome = $X/mo recovery, $Y NPV over 24mo" |
| **GC** | regulatory exposure, evidence | eval pass rates on safety/HHH-Harmless → "compliance posture: 99.2% with audit trail, the evidence base if a regulator asks" |
| **COO** | cycle time, escalation, capacity | intervention/acceptance rate → "escalation pattern: 18%→9% intervention = 50% fewer human escalations = N hours/week freed" |
| **CHRO** | skill-mix, role transitions | automation-by-tier → "workforce shift: tier-1 73% AI-resolved, high-judgment work stays human, ramp time −60%" |

**Translation is bidirectional.** The round-trip is the discipline: the CFO's margin concern becomes a cost-model workstream; the GC's compliance concern becomes an eval-coverage workstream. Stakeholder concerns become technical roadmap items, not just questions to survive.

**Translation is honest, not spin.** The cautionary case: Klarna's 2024 "AI replaced 700+ agents" headline was a CHRO-pleasing translation that didn't survive contact with reality — by 2025 they were re-hiring for nuance. Spin works once; translation compounds trust. If a translation only lands because it's flattering, it's spin. *(Source: [Klarna rehiring humans, CNBC, Mar 2025](https://www.cnbc.com/2025/03/14/klarna-rehiring-humans-cs.html).)*

### Make the dashboard bilingual

The practical artifact: every metric tile carries two labels — the technical name and its translated meaning. "Intervention Rate: 9% — *escalation pattern; predicts human-capacity load*." "Cost/successful outcome: $0.42 — *unit-economics floor; the number your price must clear*." A bilingual dashboard trains the whole team in translation by surface design, and it means any executive who glances at it reads it in their own language. This is the layer `stakeholder-communications` picks up for board-grade narrative.

### Human-review cost is a line item — model it

The executive question that catches teams flat-footed: "what does quality *cost* us to maintain?" Model it explicitly — **expert hourly rate × traces reviewed × review frequency.** That number is the denominator the eval flywheel is paid to shrink: the ROI of an automated LLM judge is real only when it cuts human-review volume substantially *at equal quality* (which is a `confidence-tuner` question — the judge's TPR/TNR has to be proven before you trust it to replace a reviewer). Report human-review cost and its trend next to cost-per-outcome; a flat or rising review cost while volume grows is the signal your judges aren't yet trustworthy enough to lean on.

---

## KEY DIAGNOSTIC QUESTIONS

**On Leading Indicators:**
- Can you tell me the acceptance rate for your product right now? (Be honest: can you?)
- How do you know if a prompt change made things better or worse?
- What's your cost per successful user outcome, not per API call?

**On Hallucination Awareness:**
- Do you track false positives separately from false negatives?
- Can you measure how often users correct AI outputs after using them?
- Do you know which domains/tasks have highest hallucination risk?

**On Segment Visibility:**
- Are your metrics the same for all users, or split by segment?
- Do power users have different acceptance rates than casual users?
- Where is degradation happening first? (Usually in the edge cases.)

**On Causality:**
- If acceptance rate drops, can you trace it to a specific change? (Prompt, model, feature)
- Do you monitor metrics BEFORE and AFTER every release?
- Can you explain why a metric changed, or are you just reacting?

**On Translation & Discovery:**
- For each top-line metric, can you state the business number it moves? (If not, execs can't act on it.)
- When users correct or abandon, do those failures cluster — and do you review the clusters as roadmap candidates, not just bugs?
- What does maintaining quality cost you? (Expert rate × traces reviewed × frequency — the number your judges are paid to shrink.)

---

## REALITY CHECK

**What mature AI product telemetry looks like:**
- Real-time dashboard: acceptance rate, regeneration rate, cost per output, latency
- Per-cohort breakdowns: power users vs. casual, by task type
- Automated alerts: acceptance rate down > 3%, cost per output up > 10%
- Regression testing: new prompt version must not degrade any metric
- User feedback loop: corrections flagged, investigated, fed back to evals

**What it doesn't look like:**
- "Our DAU is up" (but users are frustrated)
- Accuracy metrics only (ignoring cost, latency, hallucination rate)
- No visibility into cost per successful outcome
- Monthly reviews of metrics (by then, damage is done)
- Metrics that only go up (if you never see degradation alerts, you're not measuring hard things)

---

## QUALITY GATE

**Metrics infrastructure must include:**
1. ✓ Acceptance rate tracking (per user, per task type, per model version)
2. ✓ Correction/edit distance tracking (how much do users change AI output?)
3. ✓ Cost-per-successful-outcome (not just API cost)
4. ✓ Hallucination/false positive monitoring (calibrated by domain)
5. ✓ Latency tracking (p50, p95, p99)
6. ✓ Cohort analysis (power users vs. casual, task type, geography)
7. ✓ Automated regression testing (new releases checked against baseline)
8. ✓ Regression thresholds (with automated alerts)

**Blocks shipping if:**
- No acceptance rate baseline to compare against
- Cost-per-outcome increases without explanation
- Hallucination rate increases > 2%
- Latency degradation > 20% (p95)

---

## WHEN WRONG

**You'll see:**
- DAU up, but support tickets spike (users struggling silently at first, then complaining)
- Acceptance rate drops without explanation (didn't correlate with any release)
- Cost per output climbs (prompts got verbose, model overthinking)
- Certain segments have degraded acceptance (you missed it because you only looked at aggregate)
- Users switch to competitors but you don't know why (you never asked about correction rate)

**Recovery:**
- Pull the metrics for the past 30 days, split by segment
- Correlate drops with releases/changes
- Investigate: was it a prompt change, model change, or user behavior shift?
- Measure the actual impact: how many users affected, what's the revenue impact?
- Fix the root cause, then re-verify with your metrics
- Adjust your alert thresholds based on what you learned

---

## AI PRODUCT METRICS DASHBOARD TEMPLATE

Use this structure to build your product metrics dashboard. Adapt the metric names to your domain, but keep the structure: leading indicators first, then consistency, then cost, then cohort breakdowns.

### Dashboard: [Product Name]

**Last Updated:** [Date]
**Report Period:** [Week/Month]

#### Leading Indicators

| Metric | Current | Target | Trend (7d) | Alert Threshold |
|--------|---------|--------|------------|-----------------|
| Acceptance Rate | — | 70%+ | — | Drop > 3% |
| Regeneration Rate | — | < 10% | — | Rise > 20% |
| Correction Rate | — | [Domain-specific] | — | TBD |
| Conversational Burden (turns-to-success) | — | [Task-specific] | — | Rise > 15% |
| Abandonment Rate | — | < 5% | — | Rise > 2% |
| Cost per Output | — | [Budget] | — | Rise > 10% |
| Cost per Successful Outcome | — | [Budget] | — | Rise > 15% |

Each leading-indicator row should carry a **translated label** (the bilingual-dashboard discipline) — e.g. "Cost per Successful Outcome — *unit-economics floor; the number your price must clear*." And pair the health view with a **failure-clustering view** (corrections/regens/abandonments grouped by intent × persona, ranked by volume × severity) so the same dashboard does discovery, not just monitoring.

#### Consistency Metrics

| Metric | pass@1 | pass@3 | pass@5 | pass^5 | Target (pass^5) |
|--------|--------|--------|--------|--------|-----------------|
| Overall | — | — | — | — | 0.85+ |
| Simple Tasks | — | — | — | — | 0.90+ |
| Complex Tasks | — | — | — | — | 0.75+ |
| [Segment] | — | — | — | — | TBD |

**Interpretation**: If pass^5 is low while pass@5 is high, your system is capable but inconsistent. Focus on determinism improvements.

#### Cost Metrics

| Metric | Per-Query | Per-Success | Monthly Spend | vs Budget | vs Prior Month |
|--------|-----------|-------------|---------------|-----------|----------------|
| Compute Cost | $— | $— | $— | — | — |
| Token Efficiency | — tokens | — | — | — | — |
| Model Cost | $— | $— | $— | — | — |
| Infrastructure | $— | $— | $— | — | — |
| Total Cost | $— | $— | $— | — | — |

**Cost-per-Success calculation**: Total monthly spend ÷ (successful outcomes / month)

#### Quality Metrics

| Metric | Current | Target | Status | Notes |
|--------|---------|--------|--------|-------|
| Hallucination Rate | —% | < 2% | — | False positive rate |
| False Negative Rate | —% | < 3% | — | Missed cases |
| Confidence Calibration | — | High | — | Does AI know when it's wrong? |
| User Correction Rate | —% | TBD | — | % outputs edited before use |

#### Latency Metrics

| Percentile | Current | Target | vs Prior Week | Status |
|------------|---------|--------|----------------|--------|
| p50 | — ms | — ms | — | Median |
| p95 | — ms | — ms | — | Tail matters for UX |
| p99 | — ms | — ms | — | Outliers |

#### Cohort Breakdowns

| Segment | Acceptance Rate | Correction Rate | Cost/Success | pass^5 | Trend |
|---------|-----------------|-----------------|--------------|--------|-------|
| Power Users | —% | —% | $— | — | — |
| Casual Users | —% | —% | $— | — | — |
| [Task Type A] | —% | —% | $— | — | — |
| [Task Type B] | —% | —% | $— | — | — |
| [Geography/Region] | —% | —% | $— | — | — |
| [Model Version A] | —% | —% | $— | — | — |
| [Model Version B] | —% | —% | $— | — | — |

**Why slice by segment**: Degradation usually hits edge cases first. Aggregate metrics hide problems.

#### Health Status Summary

| Category | Status | Notes |
|----------|--------|-------|
| Leading Indicators | 🟢 | Acceptance rate stable, regen rate low |
| Consistency | 🟢 | pass^5 = 0.82, above target |
| Cost Efficiency | 🟡 | Cost/success up 8%, investigate |
| Quality | 🟢 | Hallucination rate within bounds |
| Latency | 🟢 | p95 within SLA |

**Alerts Triggered:**
- [List any metrics that crossed thresholds]

**Actions for Next Period:**
- [List decisions: prompt changes, model updates, eval refreshes, etc.]

---

## BUILDING YOUR DASHBOARD

**Start here (Month 1):**
- Acceptance rate + regeneration rate (easiest to instrument)
- Cost per output (from your inference platform logs)
- Basic cohort: power users vs. casual

**Expand (Month 2-3):**
- Correction rate (track edit distance on outputs)
- Hallucination monitoring (user feedback loop)
- Latency tracking (p50, p95, p99)

**Mature (Month 4+):**
- pass@k and pass^k metrics
- Eval saturation detection
- Automated regression testing
- Real-time alerts on all thresholds
- Monthly eval refresh with production traces

**Common pitfall**: Building a dashboard is not enough. You need to *act* on it. Set specific owners for each alert threshold. Weekly metric reviews. Monthly asks: "What changed this week? Why? What do we do about it?"

---

## WHERE THIS MEETS YOUR STACK

Metrics are a diagnosis layer, not a fix layer. A number tells you *something is wrong*; where you go next is what separates a dashboard-watcher from a PM. The two-hop routing:

- **A leading indicator drops and won't recover with a model swap → it's usually a context failure, not a model failure.** The series' hardest-won lesson: most eval/metric regressions trace to the *context* (retrieval, instructions, prompt), not the model's raw capability. Falling acceptance rate → route to `invisible-stack` / `context-spec` to audit the kNowledge and Constitution layers *before* anyone proposes a bigger model. First hop: the metric. Second hop: the context stack that actually produces it.
- **A metric won't move because the score behind it isn't trustworthy → `confidence-tuner`.** If acceptance is measured by an LLM judge, "90% agreement" can be a vanity number when failures are rare. Validate the judge's TPR/TNR separately before you believe *any* trend built on it. A metric is only as honest as the judge underneath.
- **Cost-per-successful-outcome is the denominator two other skills own the numerator of.** Route the cost side to `cost-model` (unit economics at 10×) and `token-economics` (how the pricing model has to align with the cost structure). This skill defines the metric; those two make it defensible at scale.
- **Conversational burden rising → `ai-ux-patterns`.** High turns-to-success is a UX-and-trust problem (uncertainty communication, progressive disclosure), not just a model-quality problem. The metric surfaces it; the UX patterns fix it.
- **A failure cluster on the dashboard → `feedback-flywheel`, `jtbd-analysis`, `opportunity-solution-tree`.** Once "evals as discovery" flags a cluster, these are where a demand signal becomes a roadmap item.
- **Translating scores for a board → `stakeholder-communications`.** This skill builds the bilingual dashboard and the four translations; that skill turns them into the narrative arc a board review needs.
- **Metric passes but production still degrades silently → `production-observability`.** Dashboards aggregate; traces diagnose. Root-cause a cluster at the trace level there before promoting it to the roadmap (or blaming the model when the *harness* failed it).

The spine: **this skill decides *what* to measure; the stack decides *what to do* when a measurement moves.** Never let a red number end at "investigate" — route it.

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
