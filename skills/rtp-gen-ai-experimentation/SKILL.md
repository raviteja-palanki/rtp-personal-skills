---
name: gen-ai-experimentation
version: v1.3.1_latest
description: 'Design gen-AI experiments at two connected levels: whether a capability improves organizational work, and whether a particular model, prompt, tool, or configuration change improves the product. Use for pilot design, causal-impact assessment, offline comparisons, shadow tests, online A/B tests, canaries, and rollout decisions. State the hypothesis, counterfactual, assignment and analysis units, outcomes, duration, uncertainty, and stopping rules before interpreting results. Covers learning versus adoption pilots, the productivity J-curve, segmentation, expert participation, four support structures, ecosystem studies, and conditions for scaling. Combine offline, live, qualitative, and operational evidence according to what each can establish; production data is not automatic causal proof. Pairs with eval-driven-development, eval-framework, production-observability, ai-product-metrics, confidence-tuner, adoption-launch, agent-risk, and ship-decision.'
imports: ["eval-driven-development", "eval-framework", "production-observability"]
---

# Gen AI Experimentation

Design a test that can change a decision. Identify what you want to learn, the evidence needed, and how much exposure and cost that learning justifies.

## Start with the decision and permitted exposure

Use the full skill for organizational adoption, a consequential product change, or a new experimentation program. For a familiar low-impact change, use the relevant comparison and rollout sections. Successful adoption does not end experimentation: changes in workflow, people, models, or economics may reopen the question.

There are two connected levels:

| Level | Main question | Design considerations |
|---|---|---|
| **Organizational / macro** | Does this capability improve work enough to expand its use? | People, teams, workflow, learning, coordination, participation, and full costs |
| **Product / micro** | Does this model, prompt, tool, retrieval, or configuration change improve the product? | Comparable task cases, trajectories, user exposure, quality, operational behavior, and business outcomes |

They can inform one another. Neither must be fully completed before the other begins. Their assignment and analysis units follow the mechanism: a product experiment may need user- or team-level assignment, while an organizational study may also measure individual tasks. Do not assume macro always takes months and micro only hours.

Reuse known context and the user's requested format. Before proposing live work, establish actual authorization, affected people/data, permissible actions, accountable owner, privacy/consent or notice requirements, and a practical harm-response path. An offline simulation is not inherently an intervention on real people, but still may process sensitive data. Fit controls to the experiment and applicable obligations using `responsible-ai-program`, `agent-risk`, and `tool-architecture`; a sandbox label does not establish compliance.

## 1. Choose the question and the kind of test

Pilot, A/B test, and organizational experiment are overlapping descriptions, not a hierarchy of rigor:

- A **pilot** is a limited trial of feasibility, delivery, adoption, or another question. It can have a hypothesis, comparison, and randomization.
- An **A/B test** compares assigned variants. It can study several outcomes and team-level effects if designed for them; random assignment is different from randomly sampling participants.
- An **organizational experiment** studies an intervention in work or coordination. It may use individual or cluster randomization, a randomized phased rollout, or another justified design. It still has scope and blind spots.

State what the proposed design can establish. Enthusiasm and feasibility evidence can inform a decision, but should not be presented as a causal estimate of productivity at scale.

### Clarify whether the pilot primarily seeks information or adoption readiness

An **information pilot** reduces a decision-relevant uncertainty. Choose cases by expected learning value, consequence, feasibility, and cost—not simply the highest uncertainty available. Uncertain outcomes need not be high stakes, and a failed test can cause damage if exposure was poorly controlled.

An **adoption-readiness pilot** helps people understand the capability, influence its design, and decide whether to try a next step. A low-stakes, useful workflow can support this purpose. Measure understanding, willingness, practical barriers, and honest feedback alongside task outcomes; do not manufacture consent or hide weak performance behind a trust-building label.

One pilot can serve both purposes if its measures and interpretation distinguish them. Use two stages when the objectives or risk limits conflict. The Warner Bros. Discovery case motivates this distinction; it does not prove information and adoption can never coexist.

## 2. Design the organizational comparison

Use the five structural questions below, with statistical support where the decision requires it.

### A. What is the hypothesis?

Specify intervention, population, outcome, direction or minimum worthwhile effect, proposed mechanism, and counter-signal. For example: “A coding assistant will reduce completion time on these tasks without unacceptable defects or review burden; effects may differ by experience.” A proposed 20–30% gain is a hypothesis or planning assumption, not an expected effect borrowed from another study.

Separate the effect of **offering access** from the effect of **using** the tool and from the effect of a larger package including training or workflow redesign. If several components change together, describe the package rather than attributing everything to the model.

### B. What is the counterfactual, and how will assignment support it?

Identify what would happen under the alternative: current workflow, no new tool, another tool, or a different implementation. Random assignment can help isolate effects when implemented and analyzed appropriately. Choose individual, team, site, or another unit to reduce contamination and capture the mechanism. Shared managers, artifacts, learning, or infrastructure can create spillovers between groups.

A staggered rollout is not automatically random or a valid natural control. Specify assignment timing, secular trends, anticipation, carryover, and comparison assumptions. Matched comparisons, interrupted time series, synthetic controls, or other quasi-experimental designs may be useful when their assumptions fit. A before/after result is evidence, but often weak evidence for a causal attribution.

Define eligibility, recruitment, assignment, sample size, minimum detectable or worthwhile effect, duration, and analysis unit. Preserve the assigned-group comparison where appropriate; reporting only enthusiastic adopters can introduce selection bias. Record uptake and attrition, and label any analysis of actual users separately with its assumptions. Cluster assignment requires analysis that respects clustering.

### C. What will be measured, before results are known?

Measure relevant outcomes at three levels:

| Level | Candidate measures |
|---|---|
| **Behavior** | Time on defined tasks, tool use, queries, review work, handoffs, and workflow changes |
| **Attitude** | Satisfaction, confidence, stress, practical influence, and perceived benefit |
| **Performance/value** | Output quantity and quality, customer outcomes, realized capacity or revenue, and full cost |

Choose primary outcomes and guardrails, define denominators/windows, and plan important subgroup analyses. Record exploratory measures as exploratory. Account for multiple comparisons, repeated looks, missing data, and changes to the analysis plan. Statistical significance does not by itself establish a worthwhile effect, and a non-significant result does not prove no effect.

Use privacy-respecting participation measures where voluntary expert work is essential. Track workload and reasons for withdrawal as well as usage; a participation fall is one possible early signal, not the only one and not evidence of low motivation by itself.

### D. How long is needed to answer this question?

Allow time for the relevant workflow cycle, learning, repeated use, delayed outcomes, and sufficient information. Short studies can validly measure immediate task effects; they cannot establish long-term adoption or durable skill transfer by duration alone. Four to twelve weeks, or the source's month-1-to-6 dip and month-9-to-18 gain diagram, are not universal timelines.

Set planned analysis and stopping rules. Stop or contain material harm promptly. For efficacy or futility decisions, use an appropriate fixed-horizon or sequential approach rather than repeatedly checking an ordinary significance test until a result looks favorable. Explain what an early stop permits you to conclude.

### E. Who benefits, and under which conditions?

Examine justified differences by experience, role, task, or workflow integration. Pre-specify consequential comparisons and report uncertainty; small subgroups can produce unstable apparent winners. A large effect in novices in one customer-service study is not a law about all junior/senior work.

For a skill-learning question, consider unaided practice, AI-assisted practice, and a no-practice comparison, plus a separate expert forecasting exercise if surprise is relevant. Randomization and comparable conditions determine what each contrast identifies. Test retention **and** transfer with suitable tasks. A one-week result is not necessarily pure recall or a lower bound on the long-term effect; skills can strengthen, fade, or fail to transfer. A forecast arm measures expectations, not treatment validity.

## 3. Treat the productivity J-curve as a hypothesis to investigate

Learning, workflow redesign, integration, and complementary investments can delay benefits or temporarily reduce measured output. The **productivity J-curve** also has an economic measurement mechanism: investment in poorly measured intangibles can affect measured productivity before benefits appear. Its established lineage includes Brynjolfsson, Rock, and Syverson's 2021 research; the 2026 HBR article applies related ideas to gen AI.

A dip does not prove failure, but neither proves an eventual payoff. Investigate weak task fit, ineffective implementation, real harm, changing demand, and measurement as alternatives. Review milestones, participation, leading evidence, costs, and expected benefit timing; revise or stop when the case no longer holds. Month three is not automatically too early to make any judgment.

The source's McKinsey “more than 80% report no material earnings contribution” is a dated self-report, not a longitudinal demonstration that those firms are all temporarily in a J-curve dip. Use [research and interpretation notes](references/research-and-interpretation-notes.md) to retain scope when drawing on prior experiments.

## 4. Support the people doing the experiment

A supported environment helps, but experimentation also consumes domain experts' time. The original two-site account describes three work modes: **trial and error**, **review and revision**, and **alignment and integration**. Budget for output inspection, documentation, technical help, meetings, rework, risk review, and production hardening.

Design four forms of support:

1. **Learning and technical help:** ongoing task-relevant training, usable documentation, and a triage route to competent technical support.
2. **Shared review:** clear evaluation criteria, cross-functional collaboration, and useful knowledge-sharing forums. Publish weights when aggregating dimensions; separate gates can work without weights.
3. **Integration and risk support:** consider technical, operational, compliance, and ROI risks, and provide the capacity to move a suitable prototype into the actual workflow.
4. **Recognized responsibility and time:** name an owner and allocate credible capacity. Align role expectations, evaluation, and rewards with the work where appropriate. Formal bonuses, raises, or a performance-review field are not the only ways to sustain participation; removing conflicting workload may matter more.

The reported 141-versus-3 deployments and over-80% dropout are two-site qualitative observations. They suggest mechanisms, not a controlled estimate that one support structure caused a 47-fold difference. Monitor actual local participation and effort rather than inferring causality from the ratio.

The five broader capabilities remain useful: **customer understanding**, **usable prototypes**, **learning-oriented teams**, **experimental expertise**, and **partnerships**. Fit investment to the decision's value. Simulations and demos can answer early questions; live use is needed for some workflow questions, not every question. Experimental expertise can be internal, external, or academic. Partnerships can improve access and perspective without automatically making a study rigorous.

For ecosystem studies with customers, partners, or suppliers, agree on the question, data and action permissions, assignment, incentives, analysis, and how findings may be shared. Choose population and sample for relevance and precision rather than merely large volume. The Grab and Siemens examples in the evidence notes are source-specific cases, not a requirement to run million-person studies or an authorization to contact partners.

## 5. Compare a product change through proportionate exposure

Offline, shadow, online, and progressive rollout provide different evidence. Select the stages needed for this change; they are not an inevitable four-step ceremony.

| Stage | What it can reveal | Important limit |
|---|---|---|
| **Offline evaluation** | Comparable behavior on known representative, critical, and challenge cases | Coverage, grader, environment, and distribution may differ from live use. It can still decisively establish a requirement violation. |
| **Shadow traffic** | Candidate behavior on copied live inputs without serving its answers | Shared data, load, caches, or tool side effects can create risk and distort results. It does not observe user reactions to the candidate. |
| **Online A/B test or canary** | Behavior under real exposure; a suitable randomized design can estimate an effect | A canary's operational detection objective may differ from a powered causal experiment. Selection, interference, logging, and limited duration can mislead. |
| **Progressive rollout** | Performance under broader exposure and operational conditions | Scaling changes the population, load, incentives, and sometimes the treatment itself. Reassess those changes. |

For shadow agents, isolate or suppress external side effects and protect privacy, permissions, capacity, and state. A duplicated request must not send a second email, charge a customer, or mutate production simply because the answer is hidden. Document what the shadow environment simulates and cannot reproduce.

For online comparisons, make assignment stable at a suitable unit, record actual exposure and all relevant versions, and avoid treating repeated turns from one user as independent participants. Validate logging and allocation before interpreting lift. Compare task and user outcomes with cost, latency, safety, and review guardrails. Investigate offline/online disagreement; live data does not automatically override valid evidence of a missing constraint or a biased experiment.

Increase exposure when the defined evidence and operating conditions support it. A low-impact change or urgent repair may have a justified direct-release path; “never 0→100%” is not a universal rule. Material risk calls for stronger containment and evidence. Existing authorization still governs the action.

### Prepare containment and recovery before live exposure

Define who can stop exposure, what conditions trigger it, how it is detected, and what happens to in-flight work and already-completed effects. An automated rollback rule can help when its metric, sample, window, and action are valid. Manual intervention may be appropriate; not every stop condition is computable by a gateway. The source's two-percent/ten-minute rule is an example, not a default.

Test the relevant stop or rollback path before depending on it. Turning off a candidate does not necessarily cancel an in-flight action or undo a completed one. Include reconciliation, compensation, and forward repair where needed, using `tool-architecture` and `ship-decision`.

### Evaluate agent transitions and the full outcome

Localize errors with the transition matrix from `eval-driven-development`, and test system-level behavior including recovery and authorized alternate paths. Do not equate per-step reliability with **pass^k**, which concerns repeated trials of a task.

For ten indispensable independent steps each succeeding with probability 0.95, all-step success is `0.95^10 ≈ 59.9%`; at 0.90 it is `34.9%`. These are illustrative assumptions, not estimates for every ten-step agent. Dependencies, branching, retries, shared causes, and recovery change the result. Measure cost and useful outcome at the workflow level as well as important transitions.

Use suitable isolated, stateful environments to test actions before risky live exposure. WebArena or other environment benchmarks can inspire a design; passing one cannot certify a different production system as safe. Record fidelity gaps and relevant real-world controls.

## 6. Decide whether to expand, revise, or stop

Apply the five scaling questions adapted from John A. List's *The Voltage Effect*:

1. **Is the effect credible and worthwhile?** Examine effect size, uncertainty, design validity, and all planned outcomes—not just the winning metric.
2. **Will it generalize?** Consider recruitment, uptake, attrition, task mix, timing, and populations not represented.
3. **Can the ingredients be reproduced?** Identify required expertise, manager support, workflow, data, configuration, and implementation effort.
4. **What changes at scale?** Assess infrastructure, dependencies, coordination, workload, and possible adverse effects.
5. **Do the economics hold?** Include tools, inference, integration, training, review, support, and opportunity cost. Model relevant scale scenarios rather than automatically multiplying everything by ten or one hundred.

Choose expansion, a targeted follow-up, a redesigned intervention, continued limited use, or exit. A result can be inconclusive. Lack of a randomized control does not make all evidence an anecdote; it limits the claims that evidence can support. A negative result should be visible and actionable without rewarding harm or treating participation as a loyalty test.

If tracking experiment velocity, define the unit, scope, completion, and decision produced. Even a stable definition within one team does not make counts a measure of learning: size and difficulty can change. Inspect what decisions improved and what uncertainty was resolved.

## Deliverable and handoff

Use this compact structure and expand only where the decision needs it:

```text
Gen AI Experiment Design: [capability or change]
Decision and primary purpose: [information, adoption readiness, product comparison]
Hypothesis: [intervention, population, outcome, mechanism, counter-signal]
Comparator and estimand: [alternative; effect of access, use, or intervention package]
Population, recruitment, assignment unit, analysis unit: [...]
Exposure and versioning: [eligibility, allocation, actual uptake, product/tool versions]
Sample, duration, analysis plan: [precision, clustering, missingness, repeated looks]
Outcomes: [primary, guardrails, behavior, attitude, performance, cost]
Subgroups: [planned comparisons and exploratory limits]
Permissions and participant/data protections: [applicable requirements and owner]
Support and effort: [capacity, technical help, shared review, integration]
Stop/recovery plan: [triggers, owner, in-flight work, rollback limits]
Result: [effect estimates, uncertainty, deviations, alternative explanations]
Scaling assessment: [credibility, generalization, ingredients, consequences, economics]
Decision, conditions, and next action: [...]
```

Use the shared Universal Skill Protocol for relevant trade-offs and handoff fields; follow the requested format. A comparison diagram or a clearly labeled J-curve hypothesis can help, but do not draw an assumed future payoff as measured fact.

`eval-framework` and `eval-driven-development` supply suitable tests; `confidence-tuner` validates judges. `production-observability` and `ai-product-metrics` define and monitor exposure/outcomes. `agent-risk`, `tool-architecture`, and `ship-decision` support the action boundary and rollout response. Organizational findings feed `adoption-launch` and `alignment-check`. Keep each result's population, intervention, counterfactual, and uncertainty attached when handing it on.

Read [research and interpretation notes](references/research-and-interpretation-notes.md) before using the historical effect sizes as planning inputs.
