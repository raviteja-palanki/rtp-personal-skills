---
name: "gen-ai-experimentation"
version: v1.3_latest
description: 'Run gen-AI experiments at BOTH altitudes: the macro/organizational question (should we scale this AI capability into the workforce?): Productivity J-Curve, pilots vs experiments vs A/B tests, control groups) AND the micro/product question (is this model/prompt/config change actually better?): offline evals -> shadow -> online A/B -> progressive rollout, with kill switches). The unifying rule: production evidence is the ultimate arbiter at both altitudes: it overrides benchmarks, offline evals, and team opinion. Use when validating a gen-AI capability before scaling, or testing whether a change is really better. Pairs with: eval-driven-development (the offline gate), production-observability (where online tests are measured), ai-product-metrics (the business metrics), confidence-tuner (the judge), ship-decision. Triggers: "gen AI experiment", "AI pilot design", "productivity J-curve", "shadow deployment", "A/B test the model", "is the new prompt better".'
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

They nest: the macro experiment validates that a capability is worth having; the micro loop runs continuously *inside* that validated capability to improve it safely. The existing content below is the macro altitude (the HBR organizational-experiment framework). The new section **"Product Experimentation"** is the micro altitude (from the AI Evals series).

**The rule that unifies both: production evidence is the ultimate arbiter.** Offline evals say a change is *probably* better; a benchmark says a model *looks* better; the team *believes* it's better. Only online, on real traffic, tells you it *definitely* is — and it overrides all three. Every experiment, at either altitude, is a machine for replacing opinion with production evidence.

---

## THE TRAP

Most organisations call something an "experiment" when it is actually a pilot. That distinction is not semantic — it determines whether you learn anything you can act on.

A pilot answers the question: "Can our best users make this tool work?" An organizational experiment answers the question: "Will this tool improve performance for our actual workforce, under real conditions, at scale?"

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

## THE FIRST QUESTION: IS THIS PILOT'S JOB INFORMATION OR PERMISSION

Before you pick a pilot's use case, answer one question first: what is this pilot actually for? There are two distinct jobs, and the selection rule for each is the opposite of the other.

**INFORMATION.** The pilot exists to reduce uncertainty about whether the capability works at all. Run it on the *highest*-uncertainty use case, the one where you genuinely don't know the answer, because that is where the pilot has something real to tell you. A visible failure here is fine. It is data, not damage.

**PERMISSION.** The pilot exists to manufacture organizational trust and consent to try more. Run it on the *lowest*-stakes, most noncontroversial use case you can find. A media company running gen AI pilots did exactly this on purpose, picking projects for being unremarkable: "if we screwed it up, nobody would care." That is the reverse of standard pilot advice, which says pick the safest bet to de-risk delivery. That advice is correct for an information pilot and wrong for a permission pilot, because a permission pilot is not trying to de-risk delivery. It is trying to earn the org's willingness to try a second one.

**Why conflating the two breaks the program:** a permission pilot judged on operational KPIs (cost saved, tasks automated, cycle time cut) looks unimpressive by design, because it was never meant to move those numbers. Teams then read the flat metric as failure and kill the pilot at the exact moment it succeeded at its actual job, which was making the next, riskier pilot politically possible.

**Where this breaks down:** a single pilot cannot cleanly serve both jobs. A noncontroversial use case rarely has enough uncertainty to produce real information, and a high-uncertainty use case is, by definition, higher-stakes than a permission pilot can afford. If you need both outcomes, run two pilots in sequence rather than asking one to do both jobs at once.

*(Source: HBR, "Warner Bros. Discovery: Seeking Growth With Generative AI," Jul 2026, a media-company case on pilot selection. Single-company account, ⚠ tier, unverified for generalizability. The transferable part is the mechanism, not a number to replicate. Add this as the required first question before designing any pilot in this skill's checklist.)*

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

A rigorous organizational experiment has five structural requirements:

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

**Name the counterfactual, don't assume it.** A control group only works if you can state, in one sentence, what would have happened without the AI-assisted intervention, and then actually test or approximate that, rather than crediting the AI for a change that would have happened anyway. eBay's incrementality-testing practice is the model: before attributing a lift to an intervention, run the counterfactual (a held-out group, a synthetic baseline, or a matched pre-period) rather than assuming the correlation is the causal story. Skip this and every "AI improved X by Y%" claim is really "X changed by Y% while AI was present," which is a weaker and sometimes wrong claim. This breaks down when a true counterfactual is not obtainable, for example a one-time organization-wide rollout with no comparable group. In that case, say so explicitly rather than quietly treating the before/after difference as causal.

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

**A design template worth copying: three arms plus a forecast.** When the question is whether AI-assisted practice actually builds a skill (not just improves one output), a clean structure is unaided practice, AI-assisted practice, and a no-practice holdout, run alongside a separate forecasting arm that asks domain experts to predict the result before it's known. The holdout isolates the pure practice effect from the AI-assisted effect; the forecasting arm tells you whether the finding was surprising or something experts already expected, which calibrates how much anyone should update on it. Its stated limit: a one-week retention window tests recall, not the months-long skill transfer that actually justifies a training investment. Treat a short retention window as a lower bound, not a final answer, and extend the window before using the result to size a rollout.

*(Source: a randomized experiment, unpublished and unrefereed as of Jul 2026, tier ◆ at best, no sample size reported. Flag as design pattern, not as a benchmark result to cite in a business case.)*

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

## THE SANDBOX IS NECESSARY AND NOT SUFFICIENT — four scaffolds around an experimentation program

The standard move is to give domain experts a supported sandbox: an isolated, secure environment with legally-compliant models and setting-specific data for retrieval. Then wait for solutions.

**Two organizations did exactly that, in the same season, and one ended with 141 organization-wide solutions in use and the other with three.** They were matched at the start on the dimensions prior research says drive engagement: problem fit, operational readiness, compliance posture. **The sandbox was the control condition, present at both sites, and it did not decide the outcome.** What decided it was the scaffolding around it.

**The hidden cost this scaffolding pays for**, which is the thing nobody budgets: collective experimentation is real work on top of an already-full job, and it arrives in three modes.

| Mode | Why it happens | What it costs |
|---|---|---|
| **Collective trial-and-error** | the model is remarkable at some tasks and unreliable at adjacent ones, with no discernible pattern, so nobody can assume what it can do | painstaking comparison of outputs, documentation, chasing technical help |
| **Collective review and revision** | the tool is easy enough that many groups use it, so experts must justify their approach to colleagues with different quality criteria | preparation before every meeting, and **each meeting triggers downstream waves of rework** |
| **Collective alignment and integration** | models change often, so you cannot pick one approach and settle into execution | continual re-comparison against priorities, revisiting metrics, swapping models, revalidating prompts, adapting to real workflows |

**The four scaffolds. Three match the modes; the fourth runs across all of them and is the one that gets cut.**

1. **For trial-and-error:** three things. *Ongoing* training rather than a one-time session. A lightweight documentation method experts can fit into routines they already have. And a triage process that assigns a dedicated technical expert to priority projects, so domain experts "were not alone with hallucinations and edge cases." The failing site had initial-only training, a vaguer documentation method, and intermittent rather than assigned technical help.
2. **For review and revision:** cross-functional product work, a **shared evaluation rubric with explicit weights**, and knowledge-sharing forums. **Both sites ran cross-functional forums. The forum is not the scaffold; the rubric is.** See `rtp-eval-framework`.
3. **For alignment and integration:** a standing risk screen (the working site used four categories: technical, operational, compliance, ROI) and real integration support to harden prototypes into production systems. Without it, experts build manual workarounds and, in the researchers' words, waste enormous amounts of time.
4. **Roles and rewards, and this is the one that decides whether the other three matter.** Job descriptions have to name the innovation work. Performance reviews have to credit it. Raises, bonuses and promotions have to follow. The sentence to put in front of anyone planning a voluntary program: *"My annual review is still based on the same criteria as before gen AI existed. All that work is invisible at review time."*

**The failure mode is silence, and it defeats every status report you have.** At the failing site, more than **80% of domain experts gradually dropped out.** Nobody refused, nobody resisted, nobody lobbied against AI, and nothing was escalated. **The program did not fail a gate. It ran out of participants.** So instrument **participation rate** from week one, beside usage. It is the only number that moves early.

*(Source: HBR, "AI Experiments Need Domain Experts. Here's How to Support Them," Aug 2026 — ◆ two-year qualitative field study, semi-structured interviews and observation, two pseudonymized US sites. **Read the mechanism, not the ratio: 141-to-3 is a between-organization comparison with n=2 across two different industries, so industry alone could produce much of a 47-to-1 gap, and the 80% figure has no stated denominator.** The article names a hidden cost as its central subject and never prices it: no hours, no meeting counts, no rework volume. That absence is the standing gap on the cost side of adoption. Ledger pattern B; see `rtp-adoption-launch` Gate Zero questions 3 and 4.)*

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
- **The macro altitude connects to → `adoption-launch` / `alignment-check`.** The organizational experiment's "should we scale" verdict feeds the adoption plan and the readiness check.

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
- **Counting experiments without defining one:** An "experiment count" that spans everything from a single A/B test to a full product launch is not a comparable unit, and a rising count can mean more real learning or just more small, easy tests. Define what counts as one experiment before you track velocity on it. A self-reported survey of "super teams" that used this exact rollup (⚠ self-report, ceiling-cut sample, no denominator given) is not evidence a team is actually accelerating; check what got counted before trusting the trend line. This caution does not apply once you are comparing counts within one team using one fixed definition over time. The risk is cross-team or cross-period comparison where the definition silently shifted.

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
*Version 1.2, 29 AUG 2026: added the information-vs-permission pilot question, counterfactual discipline in control-group design, a three-arm-plus-forecast design template, and an experiment-count caution*
*Framework Source: Harvard Business Review, Berndt, Englmaier, Sadun, Tamayo & von Hesler, "A Systematic Approach to Experimenting with Gen AI", January–February 2026*
*Part of: AI PM Skills / eval-and-quality layer*
