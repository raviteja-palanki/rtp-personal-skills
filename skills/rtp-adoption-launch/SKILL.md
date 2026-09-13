---
name: rtp-adoption-launch
version: v1.10.2_latest
description: 'Plan and improve AI adoption as an ongoing product launch: choose a useful starting cohort, involve the people doing the work, fund support, and measure sustained task outcomes. Use before rollout, when use stalls, or when access and activity look healthy but value is unclear. Diagnose product fit, skills, workflow, incentives, trust, and capacity before choosing an intervention. Use Surge, Dip, and Rebound as planning scenarios rather than a universal calendar. Include managers, expert users, meaningful participation, the destination of savings, and safe agent permissions. Pairs with needs-guard, attitudinal-segmentation, agent-risk, purpose-dialogue, judgment-guard, autonomy-spectrum, uncertainty-research, and feedback-triage. Triggers: AI rollout, adoption plan, stalled usage, change management, champions program.'
imports: [first-principles, needs-guard]
---

# Adoption Launch

Help the intended people use a worthwhile system effectively in their real work. Plan the product, workflow, learning, support, and incentives together, then adapt to the evidence after launch.

**Surge → Dip → Rebound is a planning scenario, not an adoption law.** Some rollouts show early enthusiasm, a decline, and recovery; others grow steadily, start slowly, plateau, or fail. A usage curve also differs from a productivity J-curve. Diagnose what is happening before assigning a phase or predicting recovery.

## Establish the decision and current state

Reuse known context. Follow the Universal Skill Protocol at the source library root or packaged plugin root, with depth and format appropriate to the request. A quick diagnostic can be inline; a substantial rollout may need a document, presentation, or both. Ask only for missing information that changes the work.

Establish:

- **People and task:** intended users, roles, expertise, managers, current workflow, and meaningful benefit.
- **System and scope:** what is being introduced, where, available quality evidence, action permissions, and whether use is voluntary or required.
- **Current state:** pre-launch or observed use over time, relevant cohorts, use opportunities, known difficulties, and support already available.
- **Decision and success:** launch, narrow, improve, expand, pause, or stop; the task outcomes, costs, and constraints that should guide that choice.

Use `rtp-ai-use-case-readiness`, `rtp-eval-framework`, and `rtp-ai-product-taste` to resolve material suitability or quality gaps. Adoption work can begin during discovery, before a cohort exists; broad deployment still needs evidence and controls proportionate to its consequences. More persuasion cannot compensate for unacceptable performance.

## 1. Resolve six pre-launch questions

These checks establish whether people can credibly do the proposed work. Prioritize unresolved conditions that affect safety, feasibility, or honest communication; not every uncertainty requires delaying a bounded pilot.

### 1. Can affected people influence the decisions that remain open?

Include the people doing the work while the workflow and rollout can still change. Map tasks and, separately, the judgment calls, exceptions, and workarounds that formal process documents miss. Explain which decisions are fixed, which are open, and how feedback will be used.

Co-creation can improve fit and ownership; it does not guarantee adoption or remove an actual conflict of interest. Consultation after an announcement can still improve implementation and build ownership where choices genuinely remain open. Choosing to use a finished tool is not the same as authoring it, and authoring the tool does not settle who receives its savings.

Compare leaders’ expectations with employees’ accounts and observed work. An announced rollout does not make its telemetry false; it makes the meaning of participation worth checking. Use `rtp-needs-guard` and `rtp-purpose-dialogue` where needs or purpose are material.

### 2. What changes for managers and expert functions?

Check managers separately from end users and executives. AI validation, coaching, incident handling, and interpretation of new mandates may add work without removing old obligations. **Role elevation** means a useful change in scope with the capacity and authority to perform it; **role burial** means additional duties piled onto an unchanged job. Neither follows automatically from seniority.

Name what is removed, delegated, rescheduled, or resourced. Recognize necessary coaching and knowledge sharing in objectives and reviews. Bring senior leaders into real working sessions to align expectations with operational constraints. Hiring can add capacity when skills, coordination, and time allow; removing or simplifying work can also create it. Adding people alone does not prove the bottleneck is resolved.

Check the expert function behind a self-service tool. Search may replace request handling while leaving interpretation, curation, and discovery of a better question essential. Preserve and fund the useful contribution in the new workflow. This **status-repair check** protects needed expertise and appropriate recognition, not every existing task or hierarchy.

### 3. Who receives the savings, and who bears new costs?

State how saved time or money will be used: lower workload, better quality, additional demand, learning, service improvement, or another agreed purpose. Identify who decides and what remains uncertain. Include review effort, coordination, emotional burden, and support work alongside license and technical costs.

Ask whether earlier changes in this organization made a similar promise and then increased expectations. Make current commitments credible and checkable. A free or voluntary tool can still impose costs. Concern about headcount can be accurate; explain actual plans honestly rather than promising security the team cannot guarantee.

Translate the benefit into the adopter’s meaningful outcome, such as rework, safety, client service, or time with patients. Where the buyer is different, also explain value in the buyer’s terms, including total cost and budget predictability. Use evidence for both. Benefit framing is useful even when nobody’s job is threatened, and it does not replace resolving a real threat.

### 4. Is participation supported by real capacity?

Name the people needed for experimentation, domain review, champion work, support, and product fixes. Allocate time and recognize those contributions appropriately in objectives or reviews. Use a proportionate support model; a small team may combine roles, while a larger rollout may need dedicated capacity.

Track participation and reasons for withdrawal as well as objections. Silence can reflect overload, changed priorities, absence of a relevant task, or dissatisfaction. It is a signal to investigate, not proof of resistance. Participation rate is one useful indicator alongside missed work, queues, quality, and unresolved decisions.

### 5. Can people challenge and recover from consequential errors?

Give the responsible person a usable route to inspect evidence, question an output, escalate, correct, and recover within their authority. **Contestability** includes that right and process as well as the competence and time to exercise it. An explanation may help or harm reliance; a plausible explanation is not proof of correct reasoning.

Maintain the review capability the control depends on, using `rtp-judgment-guard` where appropriate. The cost of error can fall on customers, colleagues, the organization, or the public, even when the operator bears no personal penalty. Scale review to the consequence and reversibility; neither individual review of everything nor unexamined trust is the default.

For agents, resolve permissions and recovery before expanding scope. The agent-specific checks below make this concrete.

### 6. Does the team share an executable understanding?

Use a **false-alignment test** when ambiguity is consequential: ask key participants to independently describe the intended change, scope, success, and responsibilities before discussing differences. Divergence identifies something to resolve; convergence is not proof of understanding if people fear giving an unsanctioned answer. A confidential route or a concrete scenario may help.

Write a **take-up plan**: who must change which behavior, when, with what capacity, support, and incentive. Resolve a critical dependency that is not credible, or narrow the launch so it no longer depends on it. Clarify rationale, objectives, and evaluation. Check whether work allocation, recognition, promotion, hiring, or pay conflict with the change; every small rollout does not require changing all these systems.

## 2. Choose the cohort and support by evidence

Choose an **Early Customer Profile**: a specific group with a relevant need, workable conditions, and enough tolerance for the bounded experiment. Balance learning value, potential benefit, consequences, organizational permission, and representativeness of the next cohort. A low-consequence pilot can build experience and confidence while still answering a useful question. High pain alone does not make a high-risk use an appropriate first pilot.

A concentrated **beachhead** can produce evidence and reference users before expansion. Set local expansion criteria for outcomes, quality, control, and support capacity. The historical 60–70% penetration within three-to-eighteen months is not a universal requirement.

### Four working personas

Use these as changeable stances toward this tool and task, not personality labels or fixed shares of a population. People may be mixed, unknown, or in different categories for different uses. Align detailed segmentation with `rtp-attitudinal-segmentation`.

| Working stance | Useful support | What to learn |
|---|---|---|
| **Enthusiast:** willing to explore | Bounded early access, experimentation time, support, recognition, and a route to advanced work | Where the tool succeeds and fails; enthusiastic users may not represent others |
| **Pragmatist:** wants worthwhile results at acceptable effort | Credible task outcomes, integration, clear setup and review costs | Whether total effort and outcomes improve; a workflow change can be worthwhile when supported |
| **Skeptic:** needs convincing evidence | Relevant peer examples, direct testing, time and space to question | Which concern remains unresolved and what evidence would address it |
| **Resister or current non-adopter:** does not want to use it under current conditions | An honest discussion of fit, quality, needs, incentives, access, and consequences | Whether the right response is a fix, different scope, support, or a decision not to use it |

Listen to all groups early. Do not wait until a prescribed month to hear a skeptic or non-adopter, assume every group exists, or assign the old 5–10%, 30–40%, 30–40%, and 10–20% bands as population facts. Required use also needs appropriate support and outcome measurement.

### Champions and credible demonstrations

Where peer learning is useful, recruit champions for relevant competence, credibility, availability, and willingness to help. One option is to pair a trusted, experienced skeptic with an experimenter. Give both support and time; do not require a converted veteran in every team or infer competence from age. Distributed or high-turnover teams may need different peer networks or direct support.

A demonstration can teach **how** to act and signal **whether** experimentation is supported. Make real leadership commitments visible: time protected on the calendar, uncertainty acknowledged honestly, and competing work adjusted where necessary. These are useful checks, not three mandatory tests or proof that a staged demo cannot help. Do not manufacture risk, cancel valuable work, or pressure a colleague to perform enthusiasm for credibility.

Consider five onboarding needs: **control** through orientation and clear choices; **harmony** through attention to current concerns; **significance** through relevant context; **warmth** through reachable support; and **growth** through useful practice and feedback. This is a design checklist, not a demonstrated sequence in which learning becomes impossible unless every earlier condition is fully met.

## 3. Plan support for three possible states

Use observed task cycles and cohort behavior to decide which support is needed. A cohort may skip a state, remain stable, or return to an earlier one after a major product change. The old calendar—weeks one-to-four, months two-to-four, and month five onward—is an illustration, not a deadline.

### Surge: support exploration and a first useful workflow

Help people understand what the tool can do and try one or two relevant workflows without overwhelming them. Offer realistic examples, in-workflow practice, clear limitations, accessible documentation, and an appropriate peer or help channel. An optional tip or demonstration cadence can keep learning focused. Choose the cadence from need rather than requiring a Friday message.

Support may include champions, office hours, guided practice, or direct assistance. Use channels already appropriate to the team. Draft outreach when requested; sending messages requires the user’s authorization.

Measure access, attempts, successful task completion, quality, setup and review effort, and actual use opportunities from the start. People may gain value immediately or spend time learning and running old and new methods together. Early outcomes are evidence; their durability remains a separate question.

### Dip or stall: identify the cause before prescribing the fix

Compare cohorts, tasks, versions, use opportunities, quality, support demand, and changes in workload. Speak with people whose use declined and those who continue. Possible causes include novelty fading, an unclear use case, missing skills, workflow friction, unreliable output, latency, pricing or limits, competing tools, overloaded support, incentives, or fear. Several may coexist.

| What the evidence shows | A useful response |
|---|---|
| People do not know how to perform a relevant task | Targeted practice, examples, coaching, and clearer interaction design |
| The system fails on important work | Triage with `rtp-feedback-triage`; fix, narrow, pause, or provide a reliable fallback |
| The tool works but adds coordination or context-switching cost | Redesign the actual workflow with its users and test total effort |
| Expert users lose efficiency during transition | Examine which shortcuts or judgment calls changed; offer relevant experimentation time and peer support |
| Managers accumulate validation and coaching work | Rebalance obligations, authority, recognition, and support |
| People fear consequences or see conflicting incentives | Investigate the concern and change the actual conditions where warranted |
| Logins remain high while useful outcomes do not improve | Inspect real tasks and reasons for use; activity alone cannot explain value |
| Use stops because the relevant task disappeared or was completed | Adjust the denominator and interpretation; a reminder may be unnecessary |

Expertise can help adaptation or create transition costs; the most experienced people are not automatically the riskiest segment. A flat curve can reflect stability, effective integration, low effort, or a poor measure. Neither a deep dip nor its absence proves commitment.

Prioritize fixes by consequence, recurrence, task importance, and feasibility. Assign owners and credible dates, communicate what changed, and check whether the fix helped. “Top three within four weeks” and “intervene in weeks six-to-ten” are example plans, not universal deadlines. Serious defects may require immediate restriction. Some declines recover without an intervention, so avoid claiming causation from a rebound alone.

### Rebound or sustained use: verify value and durability

Track whether the workflow remains useful across relevant cycles, cohorts, and changes. Support advanced needs where they serve the product’s goals; continue learning from mainstream users and non-adopters. Use `rtp-feedback-flywheel` to connect signals to reviewed improvements and `rtp-uncertainty-research` for deeper questions.

Check both **accountability**, the formal responsibility, and **operating ownership**, the people actually maintaining and using the workflow. A named owner does not prove the work still happens. Monitor support capacity and renewal or funding needs as well as habits.

Local adaptation, sometimes called **forking**, can show engagement and reveal useful context. It does not prove durability, and an unchanged workflow does not prove indifference. Maintain required controls and versioned changes; standardized or compliance-sensitive processes may appropriately remain identical. Test whether the work survives routine personnel or sponsor changes through actual operating evidence.

Report quality, task outcomes, net effort, user experience, and cost in the order the decision requires. Time saved is a legitimate benefit when measured credibly; perceived quality is not a substitute for actual quality. Explain what happened to the savings and any new workload elsewhere.

## 4. Add the controls the context requires

### Agent permissions and calibrated reliance

Describe permissions by action and scope: draft versus send, recommend versus execute, which data, which recipients, limits, and duration. A person can then make an informed choice and understand the consequence of withholding a permission. Route the autonomy design to `rtp-autonomy-spectrum`.

Provide task-specific failure guidance grounded in evaluation, visible activity, enforceable guardrails, appropriate escalation, and tested stop or recovery paths. A monitoring “control tower” is useful only if someone has the information, authority, and capacity to act. Some actions cannot be undone; design controls before they occur.

Permission friction is one possible cause of stalled agent use. Training and better explanations can help understanding, but neither justifies unnecessary access. A higher autonomous-workflow percentage is not inherently better than well-designed assisted work. Describe actual power truthfully; making an agent sound less capable while leaving its permissions intact misleads the user.

As valuable work moves through a provider, recheck the actual data, retention, reuse, and contractual boundaries with the relevant owners. Greater adoption does not by itself prove provider training or competitive leakage. Keep observed exposure, permitted reuse, and demonstrated reuse separate.

### Visibility, attention, and appropriate abstention

Visibility to clients, partners, or internal peers may influence use. Measure task quality and effects as well as visible activity. Audience exposure can motivate skilled work or mere compliance; the absence of a reported quality metric is not evidence that quality stayed flat. Meaningful benefits, usability, norms, requirements, learning, and incentives can all influence adoption.

Identify uses where personal attention, authorship, privacy, or another essential value could be lost. Set a clear **abstention list** where AI use is inappropriate under the relevant policy or relationship. Consider the specific contribution AI would make, recipients’ expectations, and truthful disclosure. Disclosure may not repair a loss of personal attention, but that does not make concealment the solution or every AI-assisted personal message unacceptable.

### Psychological safety and actual misconduct

Ask what people need to experiment responsibly, then check after meaningful exposure whether conditions improved. Protect constructive feedback and recognize honest learning. A fixed sixty-day survey is optional; an answer becoming shorter is not proof of performative adoption.

Distinguish concern, non-use, unauthorized workarounds, mistakes, and deliberate misconduct. A threat to someone’s interests does not prove sabotage. Address actual security incidents and harmful conduct through the appropriate process while investigating contributing workload, incentives, and access problems. Use `rtp-agent-risk` for evidenced adversarial risk; use `rtp-needs-guard` for needs and work-design questions. Co-creation and disciplinary action are not universally effective or ineffective across these different cases.

## 5. Measure adoption without confusing it with value

Define each measure’s verb, numerator, denominator, population, period, and data source. Distinguish seats purchased, access, activation, attempts, daily or weekly use, successful task use, paid use, deployment, renewal, and realized outcomes. Choose frequency for the task: daily use is not a better goal for monthly planning.

Collect an appropriate baseline before targets or mandates where feasible. A usage target can change behavior and make interpretation harder; it does not make all subsequent evidence useless. If no baseline exists, a mandate is not the only option. A bounded pilot, voluntary observation, task study, or comparison may help. Identify skilled users from quality and context as well as frequency.

Combine:

- **Reach and depth:** eligible people and use opportunities, successful tasks, sustained use by cohort, and reasons for stopping or declining.
- **Quality and outcomes:** task success, consequential errors, handoff accuracy, exceptions resolved, effective interventions, service results, or other relevant outcomes.
- **Net burden and value:** setup, training, verification, support, downstream rework, time and money saved, where those savings went, and buyer value when applicable.
- **Operating health:** participation, manager workload, support queues, ownership, control effectiveness, and maintainable local adaptations.

Training hours and course completion measure exposure; they can inform planning but do not establish capability. Usage measures are useful leading or operational indicators without proving impact. A lack of reported enterprise profit does not prove that every local use produced no value.

For a named product’s adoption claim, build a historical series when the question concerns a trend. Keep population, tier, measure, and definition comparable; mark breaks. Distinguish internal Microsoft use from GitHub customers, and completions from metered chat or agents. Check current primary pricing and usage rules when they matter. Cite social posts accurately and distinguish anecdote from population evidence. Two articles repeating one underlying source are not independent confirmation.

## Deliver the plan and review the decision

Lead with the recommended scope, the problem it addresses, and the evidence supporting the next step. Include:

```text
Users, task, baseline, system, and deployment scope:
Launch or improvement decision and critical constraints:
Six pre-launch checks: resolved decisions and material gaps:
Starting cohort, stances, and expansion criteria:
Support for exploration, stalls, and sustained use:
Owners, allocated capacity, costs, and credible dates:
Measures, denominators, review cadence, and trigger actions:
Agent permissions, recovery, and abstention boundaries where relevant:
Assumptions, alternatives, and evidence that would change the plan:
Next action and handoff:
```

Check that support matches a diagnosed need; important quality or authority gaps appear before launch recommendations; experts and managers receive context-appropriate attention; claims about savings and roles are honest; and resources match the proposed work. Include pause, stop, narrow, and expand criteria. A champion program and a multi-month campaign are options to justify, not mandatory fixtures.

State the trade-off: support consumes capacity and can delay other work, while a weak launch can waste licenses, attention, and trust. Some decisions are reversible through a staged rollout; others create commitments, exposure, or habits that cost more to unwind. Write a local hypothesis with a measurable outcome and review period rather than promising a month-five rebound.

Use a phase–support matrix or a timeline when it clarifies ownership and decisions. Plot observed cohort curves, or clearly label scenarios; do not fabricate persona trajectories. Connect to adjacent skills with a focused handoff rather than repeating their full procedures.

The [evidence and examples reference](references/evidence-and-examples.md) preserves the original cases, corrections, and planning heuristics. For a research-intensive use, start with relevant `3_Research` indexes and source notes, check the Novel Insights entry and later boundaries, then verify consequential or changing claims with primary sources. Record durable new learning through library governance with its evidence and scope.
