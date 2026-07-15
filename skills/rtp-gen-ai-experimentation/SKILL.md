---
name: "gen-ai-experimentation"
description: 'Run gen-AI experiments at BOTH altitudes: the macro/organisational question (should we scale this AI capability into the workforce? — Productivity J-Curve, pilots vs experiments vs A/B tests, control groups) AND the micro/product question (is this model/prompt/config change actually better? — offline evals -> shadow -> online A/B -> progressive rollout, with kill switches). The unifying rule: production evidence is the ultimate arbiter at both altitudes — it overrides benchmarks, offline evals, and team opinion. Use when validating a gen-AI capability before scaling, or testing whether a change is really better. Pairs with: eval-driven-development (the offline gate), production-observability (where online tests are measured), ai-product-metrics (the business metrics), confidence-tuner (the judge), ship-decision. Triggers: "gen AI experiment", "AI pilot design", "productivity J-curve", "shadow deployment", "A/B test the model", "is the new prompt better".'
imports: ["eval-driven-development", "eval-framework", "production-observability"]
---

# Gen AI Experimentation

## DEPTH DECISION

**Go deep if:** You are deciding whether to scale a gen AI tool, designing a structured test to validate AI impact before a broad rollout, or building your organisation's internal experimentation capability.

**Skim to the experiment design checklist if:** You have a clear hypothesis and just need to structure the test correctly.

**Skip if:** You've already validated the use case with rigorous data and are in scale-up mode — switch to eval-driven-development for ongoing quality.

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md).

---

## THE ONE IDEA

**"Experimentation" for gen AI happens at two altitudes, and confusing them wastes money at both.** Teams run a rigorous macro study to decide whether to adopt a tool, then change the prompt weekly with zero micro discipline — or they A/B-test prompts obsessively while never asking whether the capability was worth having. You need both loops, and they answer different questions:

| | **Macro — Organisational** | **Micro — Product/Technical** |
|---|---|---|
| The question | Should we *scale this AI capability* into the workforce/ecosystem? | Is *this model/prompt/config change* actually better? |
| Unit of analysis | A person / team | An output / trajectory |
| The arbiter | Causal impact study with a control group | Offline evals → shadow → online A/B → progressive rollout |
| Timescale | Weeks–months | Hours–days |
| The trap it kills | Mistaking a pilot's enthusiasm for evidence | Shipping a change because the offline number went up |

They nest: the macro experiment validates that a capability is worth having; the micro loop runs continuously *inside* that validated capability to improve it safely. The existing content below is the macro altitude (the HBR organisational-experiment framework). The new section **"Product Experimentation"** is the micro altitude (from the AI Evals series).

**The rule that unifies both: production evidence is the ultimate arbiter.** Offline evals say a change is *probably* better; a benchmark says a model *looks* better; the team *believes* it's better. Only online, on real traffic, tells you it *definitely* is — and it overrides all three. Every experiment, at either altitude, is a machine for replacing opinion with production evidence.

---

## THE TRAP

Most organisations call something an "experiment" when it is actually a pilot. That distinction is not semantic — it determines whether you learn anything you can act on.

A pilot answers the question: "Can our best users make this tool work?" An organisational experiment answers the question: "Will this tool improve performance for our actual workforce, under real conditions, at scale?"

The gap between those two questions is where AI rollouts die. A successful pilot creates enthusiasm. A successful experiment creates evidence. Enthusiasm is not enough to justify a £2M deployment.

| | Pilot | A/B Test | Organisational Experiment |
|---|---|---|---|
| Participants | Handpicked enthusiasts | Random sample from digital channel | Random assignment or staggered rollout across the organisation |
| Hypothesis | Absent ("let's try it") | Narrow feature variant | Explicit and testable, covering workflow and human impact |
| Control group | None | Yes, for the feature variant | Yes — essential |
| What you learn | "Our best users liked it" | Which variant performs better on one metric | Causal impact on real-world performance, adoption, and satisfaction |
| Scaling decision basis | Enthusiasm and anecdotes | Statistical lift on one metric | Effect sizes, segment breakdowns, cost at scale |
| What it misses | Almost everything | Coordination, workflow, culture effects | Nothing designed to be missed |

A/B tests are a step forward from pilots but still fall short for gen AI — they capture feature-level signal, not the broader effects on how teams coordinate, how workflows shift, and how different employee segments experience the change.

---

## The Productivity J-Curve

> **Attribution:** This concept was developed by the research team (Berndt, Englmaier, Sadun, Tamayo, von Hesler) in their HBR analysis of gen AI adoption, drawing on economic history research by Paul David on electricity adoption. Published HBR, January–February 2026.

Organisations adopting gen AI almost always experience an **initial dip in productivity before sustained gains**. This is the Productivity J-Curve — and it is not a failure signal. It is a structural consequence of how general-purpose technologies get absorbed.

```
Performance
    │
    │                                          ╱╱╱ Sustained gains
    │                                       ╱╱╱
    │                                    ╱╱╱
    │         ───────────────────────╱╱╱
    │         ↑ Adoption             ↑ Inflection point
    │      ╲╱  J-Curve dip
    │
    └──────────────────────────────────────────── Time
         Months 1-6           Months 9-18+
```

**Why the dip happens:**
- Learning curves: people are slower while adjusting to a new tool
- Workflow disruption: existing processes don't fit the new capability
- Integration costs: connecting AI to existing systems takes time and energy
- Complementary investments needed: training, process redesign, data infrastructure

**What the dip is NOT:**
- Evidence the technology doesn't work
- A reason to abandon the initiative
- A management failure

**The McKinsey 2025 data point:** Despite rapid gen AI adoption, more than 80% of firms reported gen AI had no significant impact on earnings yet. This is the J-Curve at scale — most organisations are in the dip, not yet through it.

**The strategic implication:** Don't judge gen AI ROI at month 3. Build the complementary investments (training, workflow redesign, process integration) in parallel with technology adoption, not after.

---

## What Makes a Good Organisational Experiment

A rigorous organisational experiment has five structural requirements:

### 1. A Clear, Testable Hypothesis

Not: "We want to see if Copilot helps our team."

Yes: "We believe gen AI coding assistants will reduce task completion time for junior engineers by 20-30%, with smaller effects for senior engineers, because the tool provides the most value where knowledge gaps are largest."

The hypothesis forces you to define: What changes? For whom? By how much? Why?

### 2. A Control Group (Essential)

Without a control group, you cannot distinguish the effect of the tool from the effect of time, the effect of the early adopters being more motivated, or a market trend that affected everyone.

**Methods:**
- **Random assignment:** Half the team gets the tool, half doesn't. Gold standard.
- **Staggered rollout:** Roll out to different groups over time, creating natural control groups. Works when randomisation is impractical.
- **Lab in the field:** A controlled environment where interactions with the new technology can be observed (P&G's hackathon model is an example).

### 3. Metrics Defined Before the Experiment Starts

Define metrics before you see results, or you'll find the metric that makes the tool look good.

Measure at three levels:
- **Behavior changes:** Time to complete specific tasks, frequency of tool use, types of queries
- **Attitude changes:** Job satisfaction, confidence, reported stress levels
- **Productivity outcomes:** Output quantity, quality scores, customer metrics

### 4. Duration Long Enough to Capture Real Effects

Short experiments capture the novelty effect, not the genuine productivity change. Gen AI adoption often requires 4-12 weeks of integration before the full effect shows. Run experiments for long enough to capture both the initial disruption and the stabilisation.

### 5. Granular Analysis by User Segment

Gen AI's effectiveness is highly context-dependent. What works brilliantly for one group may fail for another. Always segment results by:
- Experience level (junior vs senior)
- Role type (generalist vs specialist)
- Task type (creative vs analytical)
- Workflow integration (solo vs collaborative)

**Why this matters:** Evidence from customer service AI shows large benefits for less-experienced workers but nearly undetectable effects for experienced workers. If you only measure the average, you'll miss both the groups where it's transformative and the groups where it's a distraction.

---

## Proven Results from Gen AI Experiments (Attribution Reference)

Use these as benchmarks when setting hypotheses and evaluating your own results.

| Experiment | Conducted By | Finding |
|---|---|---|
| AI coding assistant (GitHub Copilot, Google) | GitHub & Google (controlled trials) | 21–55% faster task completion; higher completion rates; improved job satisfaction |
| Customer service AI (Fortune 500) | Fortune 500 company (staggered rollout, 5,000+ agents) | 14% overall productivity gain; 34% for less-experienced agents; higher customer sentiment; improved retention |
| P&G Innovation Hackathon | P&G + Raffaella Sadun (Harvard) | AI solo users performed as well as non-AI teams; both AI groups better at blending technical and commercial ideas |
| Microsoft Copilot across 7,000 employees | Microsoft + academics (66 firms) | 1.3–3.6 fewer hours/week on email; faster document drafting; no change in meeting behavior; training + change management critical to adoption |
| Siemens shop floor AI assistant | Siemens (Erlangen factory, 2024) | Reduced time to find information; workers felt more secure in jobs (not less); enabled workers to handle more-complex problems independently |

---

## Ecosystem Experimentation

The most sophisticated organisations run experiments not just internally but across their ecosystems — testing with customers, partners, and suppliers to generate insights at scale.

**Why this matters for product companies:** If your product includes gen AI features, ecosystem experimentation tells you which use cases genuinely matter for your customers, what implementation challenges they face, and how to design for adoption — not just capability.

**The Grab example:** Collaborating with academic researchers to study gen AI impact on 1 million+ entrepreneurs across 6 countries, with precision on which tasks AI helps most and how different business types actually use it.

**How to design ecosystem experiments:**
1. Partner with customers who have enough volume to generate statistically meaningful results
2. Bring in academic researchers to ensure experimental rigour (access to experimental expertise without hiring it full-time)
3. Design the experiment to answer product questions, not just validate the technology
4. Share findings with partner customers — the relationship creates mutual value

---

## The Five Capabilities You Need to Experiment Well

1. **Customer understanding:** Every experiment must start from a specific, high-impact customer problem — not a technology looking for a use case. Distinguish between strategic differentiators and "nice to haves." Channel resources into high-impact experiments only.

2. **Usable prototypes:** Early prototypes people can actually use in real conditions. Not demos. Not simulations. Tools users put into their actual workflow.

3. **Learning mindset:** Cross-functional teams working in short sprints, bringing customers in from the start, treating results — including failures — as learning inputs to the next iteration.

4. **Experimental expertise:** The ability to design clean experiments, determine appropriate sample sizes, analyse results correctly, and communicate findings in plain language. Some companies hire this capability; others partner with academic researchers.

5. **Partnership capabilities:** Active relationships with suppliers, customers, industry experts, and academics who can provide domain expertise, distribution at scale, and experimental credibility.

---

## Responsible AI Checkpoint

> **This step is mandatory.** Any gen AI experiment involves deploying AI on real people — employees or customers. Before running an experiment:
>
> - Has the AI Use Case Risk Assessment been completed? (From `responsible-ai-program` skill)
> - Who is accountable at the project level if the AI causes harm during the experiment?
> - Has informed consent been addressed for participants?
> - Are the experiment's data collection practices compliant with privacy requirements?
> - If the experiment reveals bias or harm, who stops it and how fast?
>
> Experiments are not exempt from responsible AI requirements. Running an unethical experiment "in the name of learning" is not a defence.

---

## The Ship/Don't Scale Decision

A successful experiment does not automatically mean you should scale. Before scaling, evaluate:

| Question | What you're assessing |
|---|---|
| Is the effect real or a false positive? | Was the result a fluke in a small sample? Do you have enough statistical power? |
| Will it generalise? | Did you test on motivated early adopters? Will results hold for a broader, more diverse group? |
| Are the success ingredients replicable? | Is the success dependent on one exceptional manager, one specific workflow, or one tool configuration? Can you replicate those conditions? |
| What are the unintended consequences at scale? | What happens when 10x more people use this? Does it strain infrastructure, create new dependencies, or change team dynamics in unexpected ways? |
| Is the cost sustainable at scale? | Gen AI adoption requires non-trivial investments. Does the cost model work at 100x? |

*Framework derived from John A. List's "The Voltage Effect," applied to gen AI by the HBR research team.*

---

## PRODUCT EXPERIMENTATION — offline → shadow → online → progressive (the micro altitude)

Everything above answers "should we scale this capability into the org?" This section answers the question you'll ask a hundred times more often: **"is this specific change — new model, new prompt, new retrieval config — actually better?"** The discipline is a promotion pipeline where each stage buys more certainty at more risk.

**The certainty ladder:**

1. **Offline evals (pre-deploy).** Run the change against your golden dataset and challenge tier (`eval-driven-development`). Fast, cheap, safe — but it only says *probably* better. Offline evals are a gate, not a verdict. They catch regressions before real users ever see them; they do not prove real-world lift.
2. **Shadow deployment.** Duplicate live production traffic to the candidate version *without serving its output to users*. Both the current model (serving users) and the candidate (silent) process the same real requests; you log and compare. The safest way to test on real traffic — zero user risk — and the first time you see the change on the *actual* input distribution rather than your curated eval set.
3. **Online A/B / canary.** Route a fraction of real traffic to the candidate and compare on *both* automated quality scores *and* business metrics (acceptance, task completion, support tickets). This is the arbiter. It overrides the offline number — a change can win offline and lose online because the eval set never matched reality.
4. **Progressive rollout.** Widen exposure through gates — a common sequencing is shadow → canary → progressive % → full, with each step gated on the same metrics holding. Never flip 0→100%.

**Wire the kill switch before you flip any traffic.** The rollback condition must be a rule the gateway evaluates on a rolling window (e.g., "safety-eval below floor OR error-rate +2% over 10 min → auto-revert"), configured *before* the change goes live. A kill switch you have to build during the incident is not a kill switch. Canary now extends beyond models to prompts, retrieval pipelines, and agents — version and gate each the same way (`prompt-as-product`).

**Gate agents per-step, not just end-to-end (Pass^k).** A 10-step agent with 95% per-step reliability succeeds end-to-end only ~60% of the time; at 90% per-step it's ~35%. An end-to-end online metric hides *which* step is bleeding reliability. Gate the reliability of each transition (the Transition Failure Matrix from `eval-driven-development`), and price/scale by chain length. Before any prod deploy of an agent, run it in a **stateful eval sandbox** (WebArena-, GAIA2-style environments that simulate the full task) — the online test tells you if it's better; the sandbox tells you if it's *safe to let touch production at all*.

*(Sources: [Shadow/canary/A-B for LLMs, 2026](https://tianpan.co/blog/2026-04-09-llm-gradual-rollout-shadow-canary-ab-testing); [Four controlled deployment strategies, MarkTechPost 2026](https://www.marktechpost.com/2026/03/21/safely-deploying-ml-models-to-production-four-controlled-strategies-a-b-canary-interleaved-shadow-testing/). Grounded in AI Evals L3-T23 / L3-T25.)*

## WHERE THIS MEETS YOUR STACK

- **Offline gate → `eval-driven-development` / `eval-framework`.** The offline stage of the certainty ladder *is* the eval suite. The online test only earns its cost if the offline gate already passed.
- **Online measurement → `production-observability` / `ai-product-metrics`.** Shadow and A/B results are read through traces (per-version spans) and the metrics dashboard. The experiment is only as trustworthy as the observability measuring it.
- **The judge scoring both altitudes → `confidence-tuner`.** Whether offline or online, if an AI judge scores the outputs, its TPR/TNR must be validated or the "winner" may be an artifact of judge bias.
- **The kill switch and per-step autonomy gates → `agent-risk` / `tool-architecture` / `ship-decision`.** The rollback rule and the sandbox-before-prod discipline are the same controls those skills design; the experiment is where you exercise them.
- **The macro altitude connects to → `adoption-launch` / `alignment-check`.** The organisational experiment's "should we scale" verdict feeds the adoption plan and the readiness check.

The spine: **the macro experiment decides whether the capability is worth having; the micro pipeline decides whether each change to it is real — and production evidence is the judge at both altitudes.**

---

## OUTPUT FORMAT

```
## Gen AI Experiment Design: [Tool/Feature]

Hypothesis:
"We believe [gen AI capability] will [measurable outcome] for [specific user segment]
because [mechanism]. We'd know we're wrong if [counter-signal] within [timeframe]."

Experiment Design:
- Control group: [how selected]
- Treatment group: [who gets the tool]
- Duration: [X weeks]
- Metrics: [behavior / attitude / productivity]
- Segmentation plan: [how results broken down]

Responsible AI Pre-Check:
- Risk assessment completed: [YES/NO]
- Project-level accountability assigned: [name/role]
- Privacy/consent addressed: [YES/NO]
- Harm stop protocol: [who, how fast]

Success Criteria:
- Minimum effect to justify scaling: [specific threshold]
- What would make us stop the experiment early: [criteria]

Scaling Decision Framework:
| Question | Assessment |
|----------|-----------|
| Real effect (not false positive)? | |
| Generalisable beyond early adopters? | |
| Success ingredients replicable? | |
| Unintended consequences checked? | |
| Cost sustainable at 10x? | |
```

---

## WHEN WRONG

- **Use case lacks genuine ROI:** Experimenting with AI when the problem doesn't justify the investment. Experimentation has cost. Focus on high-impact use cases.
- **Organisation not ready for honest results:** If negative results will be ignored or buried, experiments are pointless. They only work in organisations that will act on what they learn, including stopping.
- **Experiment runs too short:** Results from a 2-week experiment capture novelty effects, not real productivity change. Extend the timeline.
- **No control group:** Without a control group, you have an expensive anecdote, not evidence.

**Micro / product altitude:**
- **Shipping on the offline number.** The eval improved, so you shipped — and users saw no change (or worse). Offline is a gate, not a verdict; let online traffic be the arbiter.
- **0→100% flip with no kill switch.** You promoted the change everywhere at once, and when it regressed you had no rolling-window rollback rule wired in. Progressive rollout + pre-configured kill switch, always.
- **End-to-end agent metric hiding a bleeding step.** The overall success rate looked fine while one transition quietly failed 30% of the time. Gate per-step (Pass^k), not just end-to-end.
- **Confusing the altitudes.** Running a rigorous org study to adopt a tool, then changing its prompt weekly with zero micro discipline — or A/B-testing prompts obsessively on a capability the org never validated. Run both loops.

---

## TRADE-OFF LEDGER

Complete the Trade-Off Ledger from the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 5.

## CONCLUSION

Follow the Conclusion Protocol from the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 6.

---

## VISUAL SUMMARY

After completing the primary output, invoke the **excalidraw-svg** skill to create a single Excalidraw SVG visual summary — ideally visualising the Productivity J-Curve and the experiment design structure. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.

---

*Version 1.0 — 5 APR 2026*
*Framework Source: Harvard Business Review, Berndt, Englmaier, Sadun, Tamayo & von Hesler, "A Systematic Approach to Experimenting with Gen AI", January–February 2026*
*Part of: AI PM Skills / eval-and-quality layer*
