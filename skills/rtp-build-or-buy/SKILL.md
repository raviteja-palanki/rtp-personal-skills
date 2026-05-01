---
name: rtp-build-or-buy
version: 2.0
description: "Build vs buy framework: prompt, in-context, RAG, fine-tune, vertical SaaS. 5 gates + in-context check: problem type, 200K context test, data, latency, cost, maintenance. Use when: scoping features, evaluating fine-tune ROI, comparing custom vs API costs. Triggers: 'build or buy', 'fine-tune vs prompt', 'RAG vs API', 'in-context vs fine-tune', 'should we train a model'"
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

Follow the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md).

---

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md), Section 1 — at minimum:

1. **Who is the customer?** Specific segment — not "our users."
2. **What problem?** In their words, not yours.
3. **What are we saying YES to — and NO to?** Name the opportunity cost of the engineering time this decision commits.

Then run the gates below.

---

## THE TRAP

You will choose based on **team expertise, not problem fit.** If you have a prompt engineer, everything is a prompt problem. If you have ML researchers, everything needs fine-tuning. This bias confirms itself — each approach works early, so the first wins feel like validation. Twelve months later you're maintaining infrastructure that shouldn't exist.

There's a second trap: **treating 2021-era fine-tuning logic as gospel in 2026.** Context windows are now 200K+ tokens. Many problems that required fine-tuning three years ago are now solved in-context in two days — not six weeks. Most teams skip the in-context check entirely.

This framework runs five gates plus the in-context check. Stop at the first "no." Pass all of them = BUILD (fine-tune). A "no" anywhere = stay in Prompt/In-Context/RAG/SaaS territory.

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

**Real practitioners made this call:**

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

**Real case — GitHub Copilot (2022–present):**
At $19/month × millions of developers, code completion API costs at scale reached hundreds of millions annually. Fine-tuning on a curated code corpus was justified — cost ratio exceeded 50%, payback closed in months, ML team was in place. This is the archetypal case where fine-tuning won.

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

Complete using the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md), Section 5.

---

## CONCLUSION

Follow the Conclusion Protocol from the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md), Section 6:

1. **State the path** — Which of the five options: Prompt, In-Context, RAG, Fine-Tune, or Vertical SaaS?
2. **Name the gate that decided it** — Which gate was the forcing function?
3. **Key trade-off** — What are we giving up by choosing this path?
4. **Biggest risk** — What's the most likely failure mode, and how would we catch it early?
5. **Next action** — Specific step, owner, date.

---

## GENERATE THE DELIVERABLE

Use the output generation prompt from the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md), Section 11.

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
