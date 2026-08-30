---
name: build-or-buy
version: v2.5_latest
description: 'Should you build this AI capability yourself or buy it? Six stop-at-the-first-''no'' checks (problem type, whether examples-in-the-prompt already do it, data, speed, cost, upkeep) across the four ways to get AI: prompt a general model, ground it in your own documents (RAG), train your own (fine-tune), or buy a finished product. Companion lenses decide which work is even worth owning. Use when: scoping features, vendor renewals, ''should we train a model'' debates, comparing custom vs. API costs. Pairs with: moat-finder (is what you''d build defensible, and which value-chain layer a vendor sits in), cost-model (what it costs at scale), agent-harness (orchestration cost multiplier once you''ve decided to build). Triggers: ''build or buy'', ''fine-tune vs prompt'', ''RAG vs API'', ''in-context vs fine-tune'', ''should we train a model'
imports: [determinism-compass, stress-test, agent-harness]
---

# Build or Buy

## DEPTH DECISION

**Go deep if:** You're evaluating fine-tuning ROI, designing model abstraction layers, planning to commit engineering resources for 12+ months, or making a decision that's hard to reverse.

**Skim to diagnostic questions if:** You want a quick routing decision for a specific feature — which of the five options fits?

**Skip if:** Pre-PMF stage where you just need to ship something and prove the product works. Revisit at 10K users when cost becomes real.

---

## DELIVERABLE FORMAT

Before starting, ask:

> **What format would you like this in?**
> 1. **Word Document** (.docx) — Decision report with gate analysis, cost math, and trade-off ledger. Best for sharing with engineering or leadership.
> 2. **Presentation** (.pptx) — Slide deck with gate findings and recommendation. Best for architecture reviews or exec alignment.
> 3. **Both** — Full report + summary deck.
>
> *Default: Word Document.*

Follow the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md).

---

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 1 — at minimum:

1. **Who is the customer?** Specific segment — not "our users."
2. **What problem?** In their words, not yours.
3. **What are we saying YES to — and NO to?** Name the opportunity cost of the engineering time this decision commits.

Then run the gates below.

---

## THE TRAP

You will choose based on **team expertise, not problem fit.** If you have a prompt engineer, everything is a prompt problem. If you have ML researchers, everything needs fine-tuning. This bias confirms itself — each approach works early, so the first wins feel like validation. Twelve months later you're maintaining infrastructure that shouldn't exist.

There's a second trap: **treating 2021-era fine-tuning logic as gospel in 2026.** Context windows are now 200K+ tokens. Many problems that required fine-tuning three years ago are now solved in-context in two days — not six weeks. Most teams skip the in-context check entirely.

This framework runs five gates plus the in-context check. Stop at the first "no." Pass all of them = BUILD (fine-tune). A "no" anywhere = stay in Prompt/In-Context/RAG/SaaS territory.

**Why gates, not a weighted score:** a scoring model lets a strong result on one axis paper over a real failure on another — a team that scores well on "we have labeled data" (Gate 2) will talk itself past a genuine "no" on maintenance ownership (Gate 5), because the good Gate 2 score feels like validation. Gates force a clean stop the moment any one requirement fails, instead of averaging it away.

## KEY TERMS (plain language)

Read these once; the rest of the skill uses them.

- **Build vs. buy** — make it yourself (custom model work) versus use an existing API or a vendor's product.
- **Prompt + API** — just ask a general model with instructions; no training involved.
- **In-context learning** — paste examples into the prompt so the model picks up the pattern on the spot, without any training.
- **RAG (retrieval-augmented generation)** — fetch your own documents and hand them to the model so its answer is grounded in your data.
- **Fine-tune** — train a base model further on your own labeled examples so it specializes.
- **Vertical SaaS** — a ready-made product from a vendor that already solves this exact problem.
- **Deterministic vs. probabilistic task** — one where a single "correct" answer exists and people agree (a look-up) versus one with many good answers (generation).
- **P95 latency** — the response time 95% of users stay under; more honest than the average because it catches the slow tail.
- **The five gates (plus the in-context check)** — problem type → in-context check → data → latency → cost → maintenance; six steps in all, stop at the first "no."

---

## THE PROCESS

---

### Gate 1: Problem Type — Deterministic Output?

**Ask:** Can you write a precise output spec where multiple people would agree on what "correct" means?

- **Deterministic:** Classification (spam/not), extraction (dates, entities, structured fields), ranking (relevance scores) → **Continue**
- **Probabilistic:** Generation (write, summarize, explain, debug) → **BUY** (API with prompting only)

**Why this gate is first:** Fine-tuning on open-ended output almost never beats a general model. GPT-4 and Claude were trained on the full distribution of human writing — your 5,000 labeled examples won't teach the model anything the pre-training didn't already cover. The accuracy gain is real (maybe 2-3%) but the overhead is enormous.

> **Think through:** Write down three examples of "correct" output for this task. Ask two other people to evaluate them. Do they agree? If three smart colleagues disagree on whether example #2 is correct — the output is probabilistic.
>
> **Low end:** Email spam filter. Binary label, ground truth exists, humans agree 99%+ of the time. Deterministic — continue.
>
> **Mid range:** Medical ICD-10 code extraction. One right answer per clinical note, but edge cases require clinical judgment. Treat as deterministic with human-in-the-loop for ambiguous cases.
>
> **High end:** Customer support response drafting. No single correct answer — twenty good responses exist. Fine-tuning here makes your model sound like your *average* support rep, not your best one. Stop here.
>
> **Red flag:** You're designing a fine-tuning pipeline for a summarization or generation task. You'd be training on a task with no ground truth. Any accuracy gain you measure reflects your eval rubric, not real quality improvement.
>
> **Sharpen it:** Build a 20-row evaluation set with ground truth labels. If you can't label all 20 rows without debate, the task is probabilistic. Stop here and use a prompted API.

---

### Gate 1.5: In-Context Learning Check — Can 200K Context Solve This Without Training?

> **This gate didn't exist before 2023. In 2026, it eliminates the majority of fine-tuning candidates.**

**Ask:** Can you inject enough labeled examples directly into the prompt to reach your accuracy threshold — without training a model at all?

- **<100 labeled examples needed:** → **BUY + In-Context** (50-100 shot prompting at 200K context costs pennies and ships today — no training pipeline needed)
- **100–500 examples:** → **Test in-context first.** Spend 2 days running 50-shot experiments. Only proceed if accuracy is more than 15% below your threshold.
- **500+ examples AND in-context falls short by >15%:** → **Continue to Gate 2**

**Why this gate changed the math:**

In 2021, the cost equation favored fine-tuning:
- API: $0.06/1K tokens (GPT-3), context window 4K tokens
- Fine-tune: Train once, then $0.006/1K tokens inference — 10× cheaper per call

In 2026, the equation has shifted:
- API token costs are 10–20× cheaper than 2021
- Context windows are 200K+ (Claude), not 4K
- 50-shot prompting accuracy for classification tasks has largely closed the gap with fine-tuning
- **The narrow case for fine-tuning is now: deterministic task + >1K labeled examples + in-context doesn't close the accuracy gap + high enough volume for cost math to work**

**Real practitioners made this call** (⚠ reported pattern — directionally reliable, illustrative rather than independently audited figures):

*Intercom Fin (2023-2024):* Fine-tuned on 50K+ support transcripts. Justified — deterministic routing decisions, massive labeled volume, dedicated ML team, latency tolerance. Gate 1.5 couldn't close the gap at that scale. Fine-tuning won.

*Notion AI (2023-present):* In-context prompting + RAG. No fine-tuning. Ships features in weeks. Writing assistance is probabilistic (fails Gate 1), so they never got to this gate — but even their structured features use in-context approaches.

> **Think through:** Before spending 4–6 weeks on a training pipeline, spend 2 days running 50-shot experiments. What accuracy do you get? What's the gap to your threshold?
>
> **Low end:** 10–20 examples in prompt → 85%+ accuracy. You're done. Ship the prompting solution.
>
> **Mid range:** 50-shot prompting → 72% accuracy, threshold is 85%. Gap is 13%. Consider: improving labeled data quality, adjusting threshold, or testing 100-shot before declaring fine-tuning necessary.
>
> **High end:** 200 examples (approaching context limit), 62% accuracy, threshold is 90%. Gap is 28%. Fine-tuning is warranted — proceed if you pass Gates 2-5.
>
> **Red flag:** You're designing a fine-tuning pipeline and haven't run a single in-context experiment. This is 2026's version of premature optimization.
>
> **Sharpen it:** Paste 50 labeled examples + 20 test cases into a single Claude or GPT-4o prompt. Measure accuracy. This takes 2 hours. Do this before writing one line of training pipeline code.

---

### Gate 2: Data Availability — 1,000+ Quality-Labeled Examples in Production?

**Ask:** Do you have labeled examples that reflect actual production traffic — not just logs, not just synthetic data?

- **10K+ labeled examples:** Continue (strong signal — proceed)
- **1K–10K labeled examples:** Continue with risk flag (validate label quality before training)
- **<1K examples:** **BUY** — fine-tuning below 1K increases overfitting risk significantly; a strong prompted baseline usually outperforms
- **None, but can generate synthetic:** **BUY** — cost of generation + validation usually exceeds API savings for most use cases; synthetic data also underrepresents edge cases
- **Proprietary/sensitive data, can't use API:** Continue (privacy constraint justifies building even with lower volume)

> **Think through:** "We have the data" usually means "we have logs." Logs are not labeled examples. How many of those logs have verified correct outputs attached? Who labeled them? When?
>
> **Low end:** 400 labeled examples from a 6-week pilot. Stop here. Too small, too recent. Fine-tuning will overfit. Use prompted baseline and collect more data over 3-6 months.
>
> **Mid range:** 4,000 examples from 9 months of production, labeled by QA team, covering 75% of traffic distribution. Proceed with caution — run eval against prompted baseline before committing to training.
>
> **High end:** 40,000+ examples from 18 months, human-labeled with >90% inter-annotator agreement, reviewed for distribution coverage. Strong fine-tuning candidate.
>
> **Red flag:** Your training data came from one customer segment, one time period, or one product version. Fine-tuning on non-representative data creates models that regress exactly on the edge cases that matter most.
>
> **Sharpen it:** Randomly sample 50 examples from your dataset. Have two people independently label them. What's your inter-annotator agreement rate? Below 85% agreement — fix the labeling guidelines before training anything.

---

### Gate 3: Latency Budget — P95 Target Achievable?

**Ask:** What's your maximum acceptable response time, measured at the 95th percentile — not average?

- **<100ms required:** **BUY (on-device or cached only)** — API round-trip overhead alone is 80–200ms. Remote API calls cannot hit <100ms reliably.
- **100–500ms:** Continue (possible with optimized API + caching; plan this explicitly)
- **>500ms:** Continue (RAG and fine-tuning both viable)

> **Think through:** P95 is the right metric, not average. Average response time of 300ms looks fine. But if 5% of users experience 2,000ms — and those users are your enterprise clients or power users — the average is hiding your actual problem.
>
> **Low end:** Code autocomplete in an IDE. User types, expects suggestion in <80ms or it feels broken. Standard API calls are impossible here without local model inference.
>
> **Mid range:** Support agent draft response. Agent clicks "suggest reply," waits 1–2 seconds. 500ms P95 is acceptable. Fine-tuning viable if other gates pass.
>
> **High end:** Async document analysis. User uploads a report, result arrives in 30 seconds. Latency is irrelevant. Optimize for accuracy and cost.
>
> **Red flag:** "We'll optimize latency later." Fine-tuning infrastructure does not make you faster than a well-cached API call for most tasks. If you're at the latency boundary today, building won't solve it without dedicated inference infrastructure — which is a separate, expensive commitment.
>
> **Sharpen it:** Measure your actual P95 latency in production. If you don't have this measurement, you don't have a latency problem yet — you have a measurement problem. Fix that first.

---

### Gate 4: Cost Economics — Does Building Beat Buying?

> **Absolute cost thresholds ($0.50/user/year, $5/user/year) are wrong for 2026. The right benchmark is relative: API cost as a percentage of your labor cost per task, or as a percentage of gross margin per user.**

**Ask:** What does API cost represent relative to the value it delivers — not just its absolute dollar amount?

**Benchmark 1 — vs. Labor Cost:**

```
API cost per task ÷ labor cost per same task = cost ratio

Ratio < 0.1  (API costs <10% of what human labor costs): BUY — building to save 90% of pennies
Ratio 0.1–0.5: BUY (economics rarely close after you add build + maintenance cost)
Ratio > 0.5  (API costs 50%+ of labor): Run the full ROI calculation below
```

**Benchmark 2 — API Cost as % of Gross Margin Per User:**

```
Annual API cost per active user ÷ annual gross margin per active user

< 2%: BUY — cost impact is negligible; fine-tuning won't change the business
2–10%: Run ROI calculation — fine-tuning may close, but only if volume is large
> 10%: Fine-tuning ROI often closes — worth serious analysis
```

**The Full ROI Calculation (when above benchmarks flag it as worth investigating):**

| Item | Formula | Example |
|------|---------|---------|
| Current annual API cost | Tokens/request × requests/user/year × token price × users | $1.8M/year |
| Fine-tune savings per call | API token price − fine-tune inference price | $0.08 → $0.006/1K tokens |
| Annual API savings | Savings/call × volume | $1.5M/year |
| Fine-tune upfront cost | Engineering (4–12 weeks) + compute + tooling + eval infra | $350K |
| Annual maintenance cost | ML engineer time + quarterly retraining + monitoring | $180K/year |
| Net annual savings | API savings − maintenance cost | $1.32M/year |
| Payback period | Upfront cost ÷ net annual savings | $350K ÷ $1.32M = ~3 months |

**Real case — GitHub Copilot (2022–present):** ⚠ reported/illustrative — pricing tiers ($19+/month) are public; the "hundreds of millions annually" figure is this skill's own back-of-envelope estimate at millions of developers, not a disclosed GitHub number.
At $19/month × millions of developers, code completion API costs at scale plausibly reach hundreds of millions annually. Fine-tuning on a curated code corpus was justified — cost ratio exceeded 50%, payback closed in months, ML team was in place. This is the archetypal case where fine-tuning won.

**Counter-case — Most B2B SaaS features (2024–2026):**
500 users × 2,000 API calls/user/year × $0.001/call = $1,000/year in API costs. Fine-tuning upfront cost: $200–400K. Payback: never. This describes the majority of actual build-or-buy decisions — and almost all of them should be "buy."

> **Think through:** Calculate your current (or projected) annual API cost. Now add up the full cost of building: engineering time at burdened salary, ML infra, quarterly retraining, monitoring tooling. Does it close in under 18 months?
>
> **Low end:** Annual API cost is $8K. Fine-tuning saves $7K/year. Build cost $250K. Payback 35 years. Stop immediately.
>
> **Mid range:** Annual API cost is $80K. Fine-tuning saves $65K/year. Build cost $300K, maintenance $120K/year. Net savings $-55K/year. Negative ROI. Still no.
>
> **High end:** Annual API cost is $2M. Fine-tuning saves $1.7M/year. Build cost $400K, maintenance $200K/year. Net savings $1.5M/year. Payback 3 months. Build it.
>
> **Red flag:** Your ROI calculation includes token savings but excludes: (1) engineering time to build the pipeline, (2) ML engineer salary to maintain it, (3) compute for retraining cycles, (4) evaluation infrastructure, (5) 4–6 months of engineering not shipping product features. Add all five before declaring the math closed.
>
> **Sharpen it:** Build the actual spreadsheet with all five cost components. If payback period is >24 months, the economics do not close for most companies. Show this to your CFO before committing.

---

### Gate 5: Maintenance Commitment — Named Owner for 24 Months?

**Ask:** Can you maintain custom models for two years? This means: re-fine-tune quarterly, monitor for accuracy drift, update pipelines when base models change, debug production failures.

- **Dedicated ML engineer (not shared) + inference infrastructure + monitoring:** BUILD if Gates 1–4 passed
- **Part-time ML engineer (shared with other projects):** **BUY** — maintenance will degrade. Part-time ML ownership creates compounding technical debt that takes 3–4× as long to fix as it took to build.
- **No ML engineer, plan to hire later:** **BUY** — hiring for specialized ML takes 3–6 months. Your model will drift in the meantime. "We'll hire someone" is not a maintenance plan.

> **Think through:** Most teams that build fine-tuned models are good at the initial build. They fail at maintenance 18 months later — after the person who built it has moved on or shifted focus. Who specifically will own this? Is that commitment real?
>
> **Red flag:** The owner is the person who proposed the fine-tuning idea and is excited about it now. Excitement at proposal time is not a proxy for sustained ownership 18 months from now. Ask: who will own this when it's no longer new and interesting?
>
> **Sharpen it:** Name one specific person who will own this. Confirm they have 40%+ of their time available for this work for the next 24 months. If you can't complete both statements, don't build.

---

## Reference: Five Approaches Compared

| Approach | Time to Ship | Cost per Call | Accuracy Gain | Data Needed | Maintenance |
|----------|-------------|---------------|---------------|-------------|-------------|
| **Prompt + API** | Hours | $0.001–0.05 | +5–15% | None (few-shot in prompt) | Minimal |
| **In-Context (50–200 shot)** | 1–3 days | $0.01–0.30 | +10–25% | 50–200 labeled examples | Minimal |
| **RAG + Prompt** | 2–4 weeks | $0.10–2 + infra | +15–35% | Proprietary documents | Moderate |
| **Fine-Tune** | 4–12 weeks | $200K–500K upfront + $0.001–0.01/call | +20–45% | 1K–50K labeled examples | High |
| **Vertical SaaS** | 1–2 weeks | $100–10K/month | Domain-optimized | None | None |

**The 2026 insight:** In-context learning sits between Prompt and RAG as an often-missed option. For deterministic tasks with 50–200 examples, it delivers fine-tuning-level accuracy at prompt-engineering cost and timeline. Run this experiment before committing to anything downstream.

---

## Choosing Your Path: Routing Guide

**Prompt + API:** Cost/user < 2% of gross margin. Latency > 200ms acceptable. Domain is well-covered by general models. Output is probabilistic (generation, summarization). → Ships in hours.

**In-Context (50–200 shot):** Task is deterministic. You have 50–200 labeled examples. 0-shot prompting accuracy is insufficient. Gate 1.5 not yet tested. → Test this before anything else.

**RAG + Prompt:** You have proprietary documents not in model training. Latency budget 500–5,000ms. Per-user cost 2–10% of gross margin. Domain-specific factual accuracy matters. → Real case: Intercom knowledge base lookup, Notion AI document grounding.

**Fine-Tune:** All five gates pass. Rare in practice — approximately 10% of real build-or-buy decisions. → Real cases: GitHub Copilot (code at scale), Intercom Fin (support routing at 50K+ labeled examples).

**Vertical SaaS:** A purpose-built vendor already solved this exact problem. Vendor lock-in is acceptable. You want zero maintenance overhead. → Real cases: Harvey for legal contract review, Glean for enterprise search.

---

## Companion Lenses: Which Work to Own, and Which Bought Software to Keep (2025-2026)

The five gates answer "how should we build this AI capability: prompt, RAG, fine-tune, or buy?" Nine findings, mostly from 2026, sit one level *up*: they help you decide which work is even worth owning, and which purchased software is safe to keep vs. worth replacing. Use them before the gates, then run the gates on whatever you decide to own. *(These are companion lenses, not new gates — they don't change the five-gate logic above.)*

### Lens 0 — Buying a capability is not building an advantage (frame the asset first)

Before choosing build vs. buy on a specific model, ask what kind of asset this is. Acquiring technology — buying the tool, the team, or the company — does not, on its own, create a durable advantage: a large study of ~17,000 corporate transactions found that buying technology doesn't produce innovation (◆).

**Why it matters:** the advantage is what you *compound after* you own the capability (your data, your workflow, your feedback loop), not the purchase itself. So "we can just acquire it" answers a cost question, not a moat question — don't let it end the strategy conversation.

**When this is wrong:** for pure speed-to-parity — where you just need the capability to exist and aren't expecting an edge from it — buying is exactly right and the moat question is beside the point.
*(Source: "3 Ways to Rethink Your Build-or-Buy Strategy," Srivastava, HBR, 9 Jun 2026.)*

### Lens 1 — Decide task by task, not function by function (the four task types)

For any AI-enabled workflow, sort each *task* (not each whole department) into one of four types, each with its own sourcing answer:

- **Routine, digital, high-volume** (case triage, tier-one IT support, claims intake) → automate in-house, or keep with a vendor at sharply lower cost.
- **Knowledge-heavy, data-sensitive** (pricing, retention, procurement strategy) → keep in-house, because AI makes your own data and context more valuable.
- **Specialized but occasional** (tax structuring, incident response, ERP migration) → stays outside, with smaller, higher-skill teams.
- **Regulated, high-liability, judgment-heavy** (claims denials, legal sign-offs, lending decisions) → hybrid: AI-supported work, a named human accountable inside, outside expert review, governed through risk forums rather than contract targets.

**Why it matters:** "outsource the whole function" is now the wrong unit. AI follows the work, not the org chart, so the right grain of the decision is the task — a single function can hold tasks that belong in all four boxes.

**When this is wrong:** bringing routine work back in-house assumes you've kept the talent to manage both AI and vendors; a firm without it may do better with an AI-enabled vendor, and in regulated work the cost of a human owner plus outside review can exceed the old savings.
*(Source: "AI Is Rewriting the Economics of Outsourcing," Agrawal, HBR, 5 Jun 2026.)*

### Lens 2 — Which bought software is safe to keep vs. worth replacing (Stanton's survival grid)

For any purchased SaaS tool, place it on two plain questions:
- **Does it look up a stored answer, or estimate an unknown one?** (Look up last month's invoice = stored. Guess which supplier will miss a delivery = estimate.)
- **Does it run on just your company's data, or on data pooled from many companies?**

| | Your data only | Pooled across many companies |
|---|---|---|
| **Looks up a stored answer** | *Most at risk* — a workflow over a database; AI + a non-technical builder can rebuild it. Consolidate or build in-house. | Ask whether your own team could recreate a good-enough copy of the data. |
| **Estimates an unknown answer** | *Exposed* — general models are catching up on single-company guesswork. Keep only if building it yourself would be costly. | *Stickiest* — the advantage is the rare, hard cases pooled from many customers that a general model hasn't seen enough of. |

**Why it matters:** AI makes *easily-copied* software replaceable, not all software; this grid tells you which box a vendor sits in. For the stickiest box, compare the price to the *cost of replacing what it does* (the expert time and mistakes avoided), not to other software — that's a far higher ceiling.

**When this is wrong:** where mistakes are cheap, a general model plus your own logs is "good enough" on the hard cases and the premium isn't worth paying; and the grid over-credits "pooled" data that's actually scrape-able or buyable.
*(Source: "AI's Impact on SaaS Will Be Uneven," Stanton, HBR, 27 May 2026.)*

### Lens 3 — Own what your operational history makes irreplaceable (the data-vintage question)

For an AI system, add one build-vs-buy question the five gates and the traditional cost math both miss: **does this system's value depend on operational history only you possess — supplier behavior, years of failure data, customer order dynamics — and if so, how many years would a competitor need to reproduce that history, even with a better model than yours?**

If the value rides on time-indexed behavioral history, build and own it. A vendor selling a generic "[domain] AI" is selling a *model*; it can't ship with *your* history pre-loaded, and it can't backfill it by signing a new customer — time can't be bought back. If the value is just the model's general capability, buy it; the history isn't the moat.

**Why it matters:** the usual build-cost-vs-license-cost math prices the software and ignores the data vintage. Two independent cross-industry cases now make the same point — Caterpillar and Lenovo — and Lenovo states it most sharply: five years of patience bought a proprietary training-and-grounding corpus (two decades of manufacturing-failure data, supplier under-commitment patterns) no off-the-shelf platform replicates. The moat is the accumulated data, not the model wrapped around it. **When this is wrong:** for a capability where you just need parity fast and expect no edge from it, buy — the vintage question is beside the point. And "we have years of data" is a moat only if that data covers the *rare, hard cases* and isn't cheaply scrape-able (cross-check Lens 2); high-volume commodity history is not a moat.
*(Sources: "How Lenovo Built an AI-Powered Supply Chain," Handfield, HBR, 27 May 2026 [◆; author has no financial tie to Lenovo]; "Data Transformation Is the CEO's Business," MIT SMR, 21 May 2026 — Caterpillar [◆].)*

---

### Lens 4 — Two ways a buy decision quietly transfers your pricing power

Both of these are invisible in a Gate 4 cost comparison, because neither is a cost at the moment you decide.

**Transfer one: you retire the only substitute you had.** Your own competent in-house practitioners are what keeps a supplier honest, because they are the credible alternative. Buy the tool, let the practice atrophy, and the substitute is gone. **The supplier's maximum-leverage moment is the first renewal after your last capable practitioner has left**, and that is usually two or three renewals after the decision, long past the point anyone reviews it. **The move:** keep a small number of people *capable* of executing the core function even when they are not doing it daily, and book that capability explicitly as a negotiating position rather than as slack. Name them in the Gate 5 ownership commitment.

**Transfer two: the hold-up structure, and the standard advice gets the sequence backwards.** The shape recurs wherever a platform intermediates your customer. You are told to build a large, ongoing, **non-redeployable** asset whose only consumer is the intermediary: complete machine-readable product data, every attribute an agent might query, third-party certified, behind a low-latency API. A human buyer never reads it. Then the same advice tells you the platforms will control the agents and charge for placement.

Hold those two together. **Every increment of quality in that asset raises your value inside the platform's channel, which strengthens the platform's bargaining position, which raises the toll it can charge.** That is textbook hold-up, and it is usually visible in the advice's own text without the author joining it up.

The hedge on offer is a direct channel, and it is the right hedge. The trouble is the sequencing: the standard prescription funds the specific asset first and the hedge later, **which is exactly the order that maximizes your exposure during the window when the standards are being written.**

Three rules that follow:

1. **Build the specific asset anyway.** Not building it means not being selected at all, and exclusion is worse than a toll.
2. **Fund the hedge in parallel, not after.** Your direct channel is your switching capability, and **switching capability is the only stop authority you hold** over a platform. A hedge that arrives after the dependency is not a hedge.
3. **Write the investment case honestly: this asset is a defense against exclusion, not a source of margin.** Approving it on a margin story it cannot deliver is how it gets cut in year two, at the worst possible moment. Route the margin question to `rtp-moat-finder`, fake-moat loop #4, which separates universality assets from exclusive ones, and `rtp-marketing-to-ai-agents` for what the asset has to contain to work at all.

*(Sources: the expertise-retirement mechanism, HBR, Garr, "How to Respond to the Coming AI Cost Shock," Aug 2026 — ◆, and see `rtp-token-economics` for the dated subsidy facts. The hold-up structure, HBR, "Algorithmic Shopping Is Here," Aug 2026 — ⚠ framework-tier; the article names both halves in separate pillars and never joins them, so the hold-up reading is this corpus's. The platform-move timeline in that article is its verifiable part and its Gartner projection is not.)*

### Lens 5 — Provider choice is bounded by jurisdiction, not engineering merit (the sovereign-AI check)

**Rule:** Before treating "we can always switch providers" as your resilience argument in a build-or-buy case touching regulated or cross-border data, check whether jurisdiction, not capability, decides which providers are actually usable.

**The taxonomy:** AI infrastructure and model providers now split into four archetypes: hyperscalers, country-endorsed national champions, AI-native specialists, and federated consortia. A survey of 1,928 executives across 28 countries maps how providers split across these four types (◆ single-vendor-commissioned survey). Flag the authorship plainly: all four named authors are Accenture employees, and one case cited in the source names Accenture as an undisclosed deal partner on that account. Read every claim in it as vendor-interested.

**The mechanism:** Data residency law and export-control regimes bind specific workloads to specific legal jurisdictions, and inside a given jurisdiction only a subset of the four archetypes is legally usable. AstraZeneca runs one provider inside China for regulated work and a separate provider outside China for R&D, split by legal requirement rather than preference. Where that kind of split applies, failing over to a different provider is not automatically a safety net. It can itself be the compliance violation, because the failover provider may not be licensed to handle that data in that jurisdiction. Multi-provider optionality can collapse to a single legally usable option even while several technically capable providers exist.

**When this is wrong:** for a workload with no cross-border data movement and no regulated-data component, this check does not apply, and the four-archetype taxonomy is just a map of the field, useful for comparing capability and price with no jurisdictional wrinkle. Don't run the compliance check on a single-country internal tool with no sensitive data. Run it whenever a Gate 4 or Gate 5 case leans on vendor flexibility as part of the resilience or negotiating argument, and the workload touches regulated or cross-border data.
*(Source: the Accenture/MIT Sloan Management Review survey in HBR, "What CEOs Need to Know About Sovereign AI," Jul 2026 — ◆ single-vendor-commissioned; n=1,928 executives, 28 countries. Case cited: AstraZeneca's dual-jurisdiction infrastructure split.)*

### Lens 6 — Stock or flow decides how strong your "we have the data" case really is

**Rule:** When a build case rests on "we have proprietary data," ask whether that data is a stock (a fixed archive, valuable once) or a flow (continuously refreshed, valuable because it keeps arriving) before treating it as a reason to build.

**The mechanism:** A buyer of that data, for example an AI lab licensing content, pays fundamentally differently for the two. A static archive supports a one-time sale: once licensed, copied, or trained on, there is nothing more to buy, and a competitor who assembles a similarly sized archive catches up in one effort. A continuously refreshed corpus supports a recurring subscription, because the buyer needs ongoing access to what keeps arriving, not just what already exists. That difference is the entire source of ongoing leverage: a stock seller negotiates once, a flow seller negotiates every renewal. HBR's Cold Call discussion of the Atlantic-OpenAI content licensing deal names this distinction directly, without disclosing the deal's actual terms (⚠ podcast transcript, terms undisclosed; cite the mechanism only, not any dollar figure).

**What it changes:** a stock-type data asset is a weaker moat to build around than a flow-type one. Treat "we have five years of archived data" and "we generate fresh data every day" as two different build cases, not one. The flow case supports paying for durable infrastructure around it. The stock case usually does not, because the value depreciates to zero the moment it is copied.

**When this is wrong:** this question does not apply when you are not building around a proprietary-data moat at all, for instance when you are the buyer in a vertical SaaS purchase with no data-ownership stake, or when the "proprietary" claim doesn't survive Lens 2's scrape-able-data test in the first place. Run this check only after Lens 2 and Lens 3 confirm the data claim is real.
*(Source: HBR Cold Call podcast, Caroline Elkins on the Atlantic/OpenAI licensing deal, Jul 2026 — ⚠ tier; no disclosed terms, mechanism only.)*

---

### Lens 7 — When the capability is real but the institution cannot carry it alone

A pattern from research-heavy institutions that generalizes to any organization whose core capability is discovery rather than delivery.

**The five moves, and the third is the build-or-buy decision proper:**

1. **Adopt portfolio management for the pipeline**, industry-style, rather than funding projects one at a time.
2. **Integrate the emerging technology into the process itself**, not alongside it. Generative models for structure prediction and de novo design, self-driving labs pairing AI with robotic automation, and **a human retained in the loop for defining the research question and judging risk.**
3. **Use strategic partnerships instead of a full in-house build**, and accept that this creates dependence. **The governance frameworks for managing that dependence, the data privacy exposure and the IP risk are the cost of the partnership**, not an afterthought to it.
4. **Extend investment beyond the early stage.** Venture-style financing to bridge discovery and commercialization, because grant funding, philanthropy and operating margin do not reach across that gap.
5. **Keep the global collaborations**, for trial design, manufacturing, real-world evidence and regulatory harmonization.

**The transferable rule for move 3.** When you partner rather than build, **the governance work is the build.** You have not avoided the engineering cost; you have converted it into a contract, a data-exposure surface and an IP question. Price all three, or the partnership looks cheaper than it is.

**A limit the source states about itself, which is worth respecting.** The authors note that **no institution has fully implemented all five elements.** It is a synthesis across observed practice, not one organization's proven playbook, and it carries no acronym or outcome data.

*(Source: Offodile, Kadakia, Dash, Snider, Wu & Vickers, HBR, "U.S. Medical Centers Need a New Model for Drug Discovery and Development," Apr 2026 — ⚠ synthesis-tier, explicitly incomplete by the authors' own statement.)*

### Lens 8 — Assess the industry before the company, and name who leaves self-sufficient

A private-equity firm's repeatable process for installing AI capability in the companies it buys. **The order is the transferable part**, and it inverts what most acquirers and most internal build-or-buy reviews do.

**Four steps, in order:**

1. **Assess AI's effect on the target's whole industry, before investing.** Not the company's AI readiness. The industry's. A well-run company in a sector AI is about to reprice is a different asset from the same company in a stable one.
2. **Run company-level diligence on products and projects.** Only now does the individual company's position matter.
3. **Identify use cases and an implementation plan for after close**, before the deal completes. The plan is diligence output, not a first-hundred-days exercise.
4. **Secure senior buy-in on both tools and talent.** Both, because a tool agreed to without the hires is a licence nobody operates.

**The central-team design, and the stated exit condition is the useful part.** A central data, digital and AI team supplies tools, vendors, senior hires and consultants, **and aims to leave each company self-sufficient.** A central team with no stated exit condition becomes a permanent dependency, which is the same pricing-power transfer Lens 4 describes, run internally instead of against a supplier.

**One more move worth noting: the firm runs its own cross-portfolio AI system reading purchasing contracts and invoices across all its companies.** That is an asset no single portfolio company could build, because it exists only at the level that sees all of them. **When you are the parent, ask what you can see that none of your units can**, because that is the only thing you can build that they could not have bought.

**How to run this as a build-or-buy lens:** before scoping a capability, ask whether the question is being asked at the right altitude. Some capabilities are only defensible one level up.

*(Source: HBR, "Building AI Capabilities Into Portfolio Companies at Apollo," Jun 2025 — ◆ single firm, self-described, no outcome data attached to the process. **Over a year old and from private equity rather than product**, so treat the sequence as a structure to borrow rather than as current practice. Falsifier: an acquirer whose company-first diligence produced AI outcomes as good as an industry-first assessment did.)*

## Multi-Agent Harness: When Orchestration Kills Your ROI

If you've decided to BUILD (fine-tune or RAG), you face one more question: single model call or multi-agent orchestration?

**The decision rule:** Use a single model call unless all three conditions are met:
1. Quality gap between single-agent and multi-agent is >30% on your eval set
2. The task decomposes cleanly into independent steps (not sequential chain)
3. Each correct output has enough downstream value to cover the 10–22× cost multiplier

**Cost impact on your build-or-buy decision:**

| Harness Complexity | Cost Multiplier | Monthly cost at 100K requests ($0.01/base call) | Break-even value per outcome |
|---|---|---|---|
| Single call | 1× | $1,000 | $0.01 |
| Planner + Generator | 3–5× | $3,000–$5,000 | $0.03–$0.05 |
| P + G + Evaluator (1 retry) | 5–10× | $5,000–$10,000 | $0.05–$0.10 |
| Full multi-agent (3+ agents, retries) | 15–22× | $15,000–$22,000 | $0.15–$0.22 |

**The hidden killer:** Harness cost can flip a "build" decision back to "buy." If your Gate 4 cost analysis showed fine-tuning was viable at single-call pricing, re-run it with the harness multiplier. Many products that pass Gate 4 fail when you add orchestration overhead.

**When harness cost kills fine-tuning ROI:**
- Your fine-tuning advantage is <15% accuracy lift over prompted. The harness cost eats the margin.
- Your output value per outcome is <$0.10. Multi-agent orchestration is for high-value outcomes (legal analysis, medical triage) not commodity tasks (classification, routing).
- Your retry rate exceeds 20%. Each retry is a full cycle. A 20% retry rate adds ~25% to your effective multiplier.

**Re-run Gate 4 with harness costs:** Take your per-outcome value and divide by the harness multiplier. If the result is below your base model call cost, the harness isn't justified — simplify the architecture or buy a vertical SaaS solution.

For the full harness architecture decision (Planner/Generator/Evaluator patterns, sprint contracts, context management): see the `agent-harness` skill.

---

## Model-Agnostic Abstraction Layer

If you BUILD (any option), abstract the model layer on day one. Models change every 6–12 months. Without abstraction, each model upgrade is 8–12 weeks of work. With abstraction, it's 1–2 weeks.

**Pattern:**
```
Application → Abstraction Layer → Model (Claude, GPT-4o, Llama, etc.)
```

The layer handles: prompt formatting per model, context window normalization, retry/fallback logic, cost tracking per model, A/B routing between models.

**Test:** If your application code contains any `if model == "gpt-4"` conditional, the abstraction is leaky.

**Cost:** 2–4 weeks of engineering upfront. **Value:** Model swap in <2 weeks when a better or cheaper option ships — and it will.

---

## TRADE-OFF LEDGER

```
BY CHOOSING [Prompt / In-Context / RAG / Fine-Tune / Vertical SaaS]:

  We are betting on:
  [What must be true for this to work — be specific]

  We are giving up:
  [What we cannot do because of this commitment — name it]

  This is reversible within: [timeframe]
  OR
  This is a one-way door because: [reason — usually: training pipeline, data labeling investment, vendor contract]

THE HIDDEN TRADE-OFF:
  [The non-obvious second-order consequence most people miss]
  Example for fine-tune: "We are betting that this model won't be obsoleted by a better general model in 18 months — but Claude and GPT update every 6–9 months."

CONFIDENCE: [High / Medium / Low]
  What would change our mind: [specific signal or data point]
```

Complete using the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 5.

---

## CONCLUSION

Follow the Conclusion Protocol from the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 6:

1. **State the path** — Which of the five options: Prompt, In-Context, RAG, Fine-Tune, or Vertical SaaS?
2. **Name the gate that decided it** — Which gate was the forcing function?
3. **Key trade-off** — What are we giving up by choosing this path?
4. **Biggest risk** — What's the most likely failure mode, and how would we catch it early?
5. **Next action** — Specific step, owner, date.

---

## GENERATE THE DELIVERABLE

Use the output generation prompt from the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 11.

**Visuals to generate for this skill:**
1. **Gate decision flow** — Which gates passed, which one stopped the analysis, and why
2. **Cost comparison chart** — Current API cost vs. fine-tune total cost (upfront + maintenance) at current and 3× projected volume
3. **Five-option positioning map** — Where this use case sits across the Prompt / In-Context / RAG / Fine-Tune / Vertical SaaS spectrum

If this analysis connects to downstream skills (agent-harness, invisible-stack, cost-model), generate the markdown handoff file per Universal Skill Protocol, Section 9.

---

## QUALITY GATE

- [ ] Problem type classified (deterministic vs. probabilistic — Gate 1)
- [ ] In-context experiment run before fine-tuning considered (Gate 1.5) — 50-shot test, not just assumed
- [ ] Data availability assessed with actual labeled count and inter-annotator agreement (Gate 2)
- [ ] Latency P95 defined — not average latency (Gate 3)
- [ ] Cost economics calculated as % of gross margin or labor cost — not absolute thresholds (Gate 4)
- [ ] Fine-tuning ROI spreadsheet completed if cost gates flagged it as worth analyzing
- [ ] Maintenance owner named by name, not "we'll hire someone" (Gate 5)
- [ ] Decision stated with the specific gate that forced it
- [ ] If BUILD: model-agnostic abstraction layer design included
- [ ] Model switching plan exists — can you swap in <2 weeks?

---

## WHEN WRONG

- **Very early exploration** — just ship, don't optimize. Revisit at 10K users when real cost data exists.
- **Single-customer, high-touch deployment** — cost/user math breaks down when you have one customer paying a flat fee; relationship and SLA drive the decision.
- **R&D context** — if building is the learning goal, the gates don't apply. This framework is for product decisions, not research.
- **Gate assumption changed materially** — re-run from Gate 1 when: volume grows 10×, a new model ships that changes the cost equation, or your accuracy threshold shifts due to product requirements.
- **Pre-2023 decision being re-evaluated** — run Gate 1.5 before anything else. Many fine-tuning decisions made in 2021-2022 should be revisited now that 200K context exists.
