---
name: uncertainty-research
version: v1.5.1_latest
description: 'Design research that accounts for variation in AI outputs, user context, and behavior over time. Use for task validation, trust and reliance studies, quality trade-offs, or changing product conditions. Match the method and sample to the decision; combine behavioral outcomes with people’s accounts, examine consequential failures and relevant segments, and record the system each participant experienced. Distinguish user acceptance from correctness and acceptable risk. State where a finding applies and what change warrants revalidation. Standard research methods remain useful when designed for the relevant variation. Pairs with interview-synthesis, jtbd-analysis, ai-product-taste, eval-framework, ai-use-case-readiness, and fit-signal. Triggers: trust study, threshold study, how good is good enough, research for AI.'
imports:
  - first-principles
  - interview-synthesis
---

# Uncertainty Research

Choose a study that can answer the decision-relevant question despite variation in outputs, tasks, people, and time. Record what participants actually experienced and distinguish the quality of the system from their expectations, feelings, and reliance on it.

AI does not invalidate standard interviews, usability studies, surveys, or experiments. Those methods already address variation when designed appropriately. This skill helps identify which sources of uncertainty matter and adapt the study without mistaking a narrow observation for a general product finding.

## Frame the question and protect the meaningful outcome

Establish the user and task, current alternative, proposed decision, available evidence, and consequence of being wrong. Reuse context and follow the Universal Skill Protocol at the source library root or packaged plugin root, with proportionate depth and format.

Answer four planning questions:

1. **What do we need to learn?** Define the construct: usability, quality, expected reliability, actual reliance, satisfaction, demand, workload, or task outcome. These are related but different.
2. **Whose experience and which conditions matter?** Name the relevant populations, tasks, expertise, setting, and available alternatives.
3. **What decision can the evidence change?** Specify a product, scope, control, or further-research choice. Exploratory questions may help frame a later decision rather than trigger an immediate feature change.
4. **What limits transfer of the finding?** Record the system configuration, task population, context, and assumptions that may change.

For “good enough,” separate three questions: whether users accept the output, whether it accomplishes the task, and whether the residual consequences are acceptable. Willingness to use a flawed answer does not establish a safe quality threshold. In consequential work, meaningful error control remains necessary even if additional quality does not increase acceptance.

Use the method for low-volume, batch, offline, and deterministic systems when the uncertainty warrants it. A product with fewer than fifty weekly users can still yield useful evidence. The method and scope of claims should fit the data, not an arbitrary eligibility cutoff.

## 1. Map what can vary

Distinguish model sampling from other sources of change: prompt and tool versions, retrieved data, memory, user permissions, task difficulty, latency, interfaces, and the participant’s situation. Two people asking similar questions may see different answers because their context differs, not only because generation is stochastic.

For each study condition, record the actual output or interaction trace with appropriate permission and data minimization. Preserve relevant inputs, version/configuration, latency, task, participant context, and important interventions. For a fixed-stimulus study, store the stimulus and explain what live behavior it does not represent. For live use, capture enough to reconstruct consequential differences.

Choose the unit of analysis and assignment: person, task, team, session, or another meaningful unit. Repeated outputs from one person or repeated runs of one task are not automatically independent observations. Plan how the analysis will account for that dependence.

## 2. Understand expectations without replacing experience with a score

Use existing research or proportionate interviews to learn what participants think the system can do, where they expect errors, how they would respond, and what would make them restrict or stop use. A confidence rating can add context if the question is clear; it is not a calibrated probability merely because it uses a numeric scale.

Compare expectations with demonstrated behavior. A gap may call for clearer interaction design, better quality, training, or a narrower scope. Do not assume a 95%-expected versus 75%-delivered gap always destroys trust or must be fixed by messaging alone. If the study concerns current expectations, changing the framing first changes the question being studied.

Ten to fifteen interviews, or checks at weeks two and eight, are example plans. Choose timing and coverage for the uncertainty. Record both under-reliance and over-reliance where relevant; greater trust is not always the goal.

## 3. Match the method to the question

| Question | Useful method | What it can establish and what to add |
|---|---|---|
| Can people understand and use this interaction? | Task-based usability sessions with relevant outputs and errors | Locates interaction problems; repeated use may be needed for learning or habit claims |
| Does it help in real work? | Field observation, diary study, task comparison, or a suitable experiment | Captures context and outcome; distinguish reports from observed performance |
| How good is the output? | Representative evaluation plus targeted difficult cases, using a stated rubric | Measures quality in scope; compare expert judgment, user experience, and objective outcomes as appropriate |
| Is it better than the current approach? | Randomized or otherwise credible comparison with a primary outcome and relevant guardrails | Supports a comparative claim; check confounders, assignment, sample size, and exposure |
| Does reliance match system capability? | Task studies and, where needed, repeated observation of correct and incorrect outputs | Measures appropriate acceptance, rejection, verification, and correction rather than uptake alone |
| How does experience change over time? | Longitudinal observation across relevant task cycles and changes | Tests learning, reliance, workload, return use, and recovery; investigate attrition instead of assuming its cause |
| Which quality differences matter? | Controlled variation of relevant output properties, combined with outcome and preference measures | Estimates trade-offs within the tested range, not a universal minimum quality |

Combine behavior and self-report. Acceptance, edits, rejection, verification, and return use show actions; interviews and surveys help explain needs, expectations, satisfaction, and perceived cost. Neither is automatically truth or noise. Copying or sharing an output is not proof of informed trust, and an edit can be personalization rather than error correction.

Choose quantitative sample size from the target precision or detectable effect, baseline rate, variation, repeated measurements, grouping, attrition, and planned subgroup comparisons. Qualitative adequacy depends on scope and information quality. The old table’s fixed values—thirty participants, one hundred users, or five hundred per arm—were examples, not general minimums.

### Preserve the overall result while inspecting the tail

Include representative traffic and deliberately inspect important failure classes, query types, user groups, and rare consequential situations. Define strata and quality judgments independently where feasible. When difficult cases are oversampled, use the sampling design and appropriate weights to estimate population rates. Report sample composition and relevant uncertainty.

A mean can be useful alongside the distribution, tail consequences, and segment results. Do not ban averages or equate the lowest quality quartile with the full risk picture. Rare serious errors may be hidden even within a quartile summary.

For experiments, preserve the randomized comparison. Classifying users after treatment by output quality can select different populations in each arm and distort a causal interpretation. Use pre-treatment task strata for planned comparisons where possible, and label post-treatment quality breakdowns as descriptive unless the analysis addresses that selection.

## 4. Study quality trade-offs without making acceptance the safety standard

Start with `rtp-ai-product-taste` to define relevant quality dimensions. Then identify the uncertainty the study should resolve—for example, whether a more complete draft reduces total rework enough to justify delay.

1. **Create defensible conditions.** Use realistic tasks and outputs whose quality differences can be described and checked. “75% quality” is meaningless without a rubric, unit, and denominator. Keep irrelevant presentation differences controlled when testing content quality.
2. **Recruit for the question.** Include relevant expertise and contexts. Experts may detect some errors better, but do not presume they always accept lower quality or novices always trust without checking.
3. **Choose safe exposure.** When studying incorrect outputs, use appropriate research authorization, safeguards, and debriefing where needed. Do not put participants or downstream recipients at risk merely to observe whether they notice an error.
4. **Measure the whole response.** Record task success, harmful or missed errors, appropriate reliance, edit and verification effort, satisfaction, and meaningful user choices. Show what is being traded off.
5. **Estimate the relationship.** Plot outcomes and acceptance against the defined quality variation with uncertainty. A knee or plateau may be absent, uncertain, or differ by segment.
6. **Interpret within scope.** A plateau in acceptance can reflect a ceiling, insensitivity, hidden costs, or inability to detect improvement. It does not prove additional accuracy, fairness, accessibility, or error reduction has no value.

The prior coding, creative-writing, support, and healthcare percentage thresholds are not validated standards. In particular, a clinical acceptance study cannot set acceptable patient risk simply by finding when people stop checking. Hand findings to `rtp-eval-framework` and `rtp-ai-use-case-readiness` with their scope and remaining safety or control questions.

## 5. Observe change over an appropriate period

Use longitudinal research when the claim involves learning, habit, sustained reliance, repeated failures, or recovery. Choose duration by task cycles and exposure, not an automatic four-week minimum. A rare monthly task and a daily drafting task accumulate different evidence in four weeks.

Track baseline experience, actual use opportunities, correct and incorrect outputs, reliance, workload, significant incidents, and reasons for reduced or discontinued use. Retain participants who withdraw in the account of the study, even when their later measures are missing; attrition can bias a stable-looking survivor group.

Trust may rise, fall, fluctuate, or remain stable. Lower verification can reflect appropriate familiarity, fatigue, pressure, or over-reliance. More rejection can reflect better discrimination. Week-three churn can reflect task completion, novelty, access, quality, workload, or trust; investigate the explanation.

A short study can establish important usability or performance facts and may be adequate for a bounded decision. It does not establish long-term behavior. State the unresolved time-dependent question and the monitoring or follow-up plan rather than requiring every product to wait for the same study duration.

### Include relevant participant state

Record setting, interruptions, workload, shift position, and time-related context when they may affect the task. Match important use conditions or sample across them deliberately. A fresh morning session may not represent end-of-shift alert triage, but the size and direction of any difference must be measured.

Do not assume everyone is creative after waking, focused at ten, or agreeable at three. Chronotype, sleep, schedules, health, and context vary; clock time is not a direct measure of cognitive state. Avoid collecting sensitive information without need. Plan analysis and review with enough time and attention to preserve ambiguity, without claiming one hour of day guarantees sound synthesis.

## 6. Use simulations and prototypes for the questions they can support

**Wizard-of-Oz** uses a person to perform some functions of a proposed system. It can investigate demand, interaction, workflow, or reactions to controlled output. Define what the human is simulating, including latency, errors, capabilities, and consistency. Follow appropriate consent and disclosure/debriefing practices for the research design.

Humans do not always produce perfect or instant responses. Results transfer only to the tested conditions. Do not forecast a real AI product’s satisfaction by applying a blanket 30–40% discount to a human-assisted prototype. Compare the actual system or construct an explicitly justified model of the expected differences.

**Simulated customers or digital twins** can help generate hypotheses, explore a large option set, or test a research process. Validity for population estimates requires comparison with real participants on the relevant task and outcomes. Rich profiles or fluent answers alone do not establish that validity.

Be especially careful with price, switching cost, novel products, and framing. A model can interpret a manipulated price as information about quality rather than respond as the intended shopper would. Bias can be systematic, but neither its existence nor an always-optimistic direction should be assumed for every simulation. A validated result on one survey does not validate every purchase or adoption prediction.

Use actual-customer research, fieldwork, or appropriate experiments when the claim requires it. Lead users offer useful perspectives but are not automatically representative of a broader market. Keep simulated and human evidence separate and labeled. The [research reference](references/research-and-examples.md) records both the original cautions and primary counterevidence to a blanket dismissal of simulation.

## 7. Match the detail of the instrument to the decision

A broad survey can locate a broad concern; it may need follow-up to identify a specific step or cause. One useful sequence is confidential interviews, a task-specific survey where quantification matters, and collaborative interpretation with the people doing the work. Use the sequence when it fits rather than requiring all three stages for every study.

Ask how each question informs the research purpose. Mood, belonging, satisfaction, and other experiences can be valid outcomes even when one answer does not immediately produce a roadmap item. Return useful findings to participants where appropriate, explain next steps and limits, and avoid implying that every requested fix will be implemented. Lack of a particular fix does not universally make asking worse than silence.

### Check claims about combined interventions

When a framework claims its components are mutually necessary, distinguish a proposed mechanism from a tested interaction or dependency. A single cross-sectional self-report survey may not establish causality, direction, or necessity. Dichotomizing a rating at its ceiling can discard information and change the observed relationships; inspect the underlying distribution and analysis.

Objective outcomes alone do not prove interdependence either. Compare component combinations or other suitable designs, considering confounding, power, and scope. A justified cutoff can be useful for a particular decision; it is not universally invalid just because it uses a top rating.

### Vary information sources when independent exploration matters

For a research or discovery team, inspect whether apparent agreement comes from independent evidence or the same underlying sources. Different search terms, starting points, corpora, and perspectives can widen coverage. A shared workspace can support both collection and review if provenance and diversity are maintained.

Compare source overlap and substantive alternatives, not a mandatory number of semantic clusters. Shared tools do not always return identical material, and independent tools can repeat the same source. The earlier retrieval example reports novice/expert clusters of 1/2 under standard search and 2/5 under exploratory retrieval: two is not equal to one, and these counts alone establish neither significance nor statistical power. Treat cross-domain generation prompts as hypotheses extending a retrieval result, not as a measured effect.

## 8. State validity and revalidation conditions

For each major finding, record when and where it was observed, the tested system, population, task, alternative, and uncertainty. A historical finding remains a record of that study; what may expire is its applicability to a changed product or decision.

Name changes that could affect transfer: output distribution, failure type, model or prompt, retrieval, interface, latency, user population, workflow, stakes, or alternatives. Decide whether a focused check, partial update, or full study is needed. A higher average accuracy does not automatically invalidate every result, and a stable average can hide a changed tail.

Use both change-based triggers and an appropriate periodic review where silent change is possible. Replace the old 2–3%, 5%, and 10–15% revalidation bands with task-specific reasons and clear units. Distinguish a relative percentage change from percentage points. If a system changes during a study, version and analyze the exposure; do not silently pool it or automatically discard everything learned.

## Deliver and check the plan or findings

Lead with the research question, method, decision it supports, and the main limitation. Include:

```text
Task and population:
Baseline and system conditions:
Question, hypothesis, and decision:
Method and why it fits:
Sample, recruitment, assignment, and analysis unit:
Duration and relevant exposure:
Primary outcome and consequential guardrails:
Behavioral and reported measures:
Variation, segments, missing data, and analysis plan:
Research safeguards and data handling:
Validity scope, revalidation triggers, owner, and next action:
```

Check that the method can answer the claim, samples are not treated as independent without reason, quality measures and denominators are clear, and user acceptance does not stand in for correctness. Show actual output exposure, uncertainty, meaningful tails, and limitations of simulation or short duration.

Use `rtp-interview-synthesis` for qualitative analysis and `rtp-jtbd-analysis` for switching interviews. `rtp-ai-product-taste` informs relevant quality dimensions; `rtp-eval-framework` integrates capability and task checks; `rtp-ai-use-case-readiness` uses the evidence to assess a proposed scope. `rtp-fit-signal` may surface a question needing deeper research, but a weekly measure is not inherently invalid simply because it is lightweight. `rtp-first-principles` keeps the claim and outcome aligned.

A method matrix, quality-response plot, or longitudinal chart can clarify a substantial result. Label hypothetical curves as hypothetical, include uncertainty where available, and never draw a universal acceptance knee or week-one-to-eight trust arc as if it were observed data.
