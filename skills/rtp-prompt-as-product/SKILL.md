---
name: prompt-as-product
version: v1.0.1_latest
description: 'Manage prompts as versioned product artifacts so changes can be understood, evaluated, released, monitored, and recovered safely. Use when shipping a production prompt change, investigating changed AI behavior, or designing a prompt release process. Record the prompt and its dependencies, define intended behavior and decision criteria, test relevant regressions, choose proportionate live exposure, and prepare a tested recovery path. Includes decision tables, four evaluation tiers, experiment cost estimates, release gates, and monitoring by version. Scale the process to the change: a prototype edit, routine low-impact update, major behavior change, and urgent fix need different evidence. Prompt-craft writes the prompt; context-spec designs its information environment; eval-driven-development and eval-framework define and measure quality. Pairs with determinism-compass, production-observability, cost-model, and ship-decision.'
imports:
  - eval-framework
  - determinism-compass
---

# Prompt as Product

Make a prompt change traceable from its purpose to its observed effect. The useful release record answers: **what changed, what should improve, what must remain acceptable, who was exposed, and how will we recover?**

A short edit can change behavior across many tasks. Its visual size does not tell you its impact. Conversely, every wording edit does not require a large experiment. Choose the release discipline from the users, actions, dependencies, and consequences affected.

Use this skill for the prompt lifecycle. Use `prompt-craft` to improve the instructions themselves and `context-spec` to design what information reaches the model. If production behavior changes without a prompt edit, investigate model, retrieval, tools, routing, data, and traffic changes too.

## Start with the change and its exposure

Identify the current version, proposed change, intended outcome, affected users and tasks, and whether the system only produces drafts or can act externally. Use existing context; request missing facts only when they change the release decision.

| Situation | Proportionate approach |
|---|---|
| Personal draft or early prototype with no production users | Save the useful baseline and check representative examples; keep iteration light |
| Low-impact production change with well-understood behavior | Version it, run relevant regression checks, confirm recovery, and monitor an appropriately scoped release |
| Meaningful behavior change with uncertain user benefit | Add a controlled comparison when traffic, measurement, and user protection support it |
| Change affecting consequential actions or sensitive workflows | Strengthen offline evidence, boundary tests, scoped exposure, and independent checks before expanding |
| Urgent correction of known harm | Use the incident process and existing authority; contain exposure and run the checks feasible before release, then complete follow-up validation |

A **canary** limits exposure while checking release health. A product **A/B experiment** estimates a defined treatment effect. Both can compare candidate and control populations, and one rollout can serve both purposes, but a brief canary is not automatically a sufficiently powered product experiment. Offline replay and shadow testing answer other questions; shadow runs must not duplicate external actions.

## The release process

### 1. Establish an identifiable baseline

Save the current prompt, its owner, and the effective configuration: model identifier and resolved version where available, template variables, retrieval sources, tool contracts, routing, safety controls, and relevant evaluation versions. Record which dependencies are pinned and which can change independently.

Run the appropriate baseline evaluations and capture production metrics for a comparable scope. A versioned artifact improves traceability; it does not guarantee identical model outputs or preserve a provider version forever. Keep a migration path for retired dependencies.

### 2. Propose the change with a reason

Save the candidate and a readable diff. State the observed problem, intended behavior, plausible mechanism, and evidence that would count against the change. Separate unrelated changes when that makes effects easier to interpret; document a necessary bundle as a bundle.

Example: “For factual support questions, require an approved policy source before stating eligibility. Expected benefit: fewer unsupported eligibility claims. Watch for unnecessary refusals, added latency, and unresolved cases.” This is a testable hypothesis, not a promised improvement.

### 3. Define behavior and decision criteria before testing

For complex instructions, use a decision table. Include boundaries, exceptions, and cases where a behavior should **not** occur.

| Input condition | Intended behavior | Observable check |
|---|---|---|
| Approved source answers the factual question | Give a concise answer with a traceable source | Answer is supported and citation resolves |
| Evidence is missing or contradictory | State the uncertainty; retrieve, clarify, or escalate as appropriate | No invented fact or unsupported certainty |
| Personal information is necessary for an authorized task | Use only the permitted information and protect logs and outputs | Access, disclosure, and retention follow the task policy |
| Personal information is unnecessary or disclosure is unauthorized | Omit or redact it using the approved handling rule | No prohibited disclosure, including in diagnostic logs |

A model's self-reported “60% confidence” is not a calibrated decision threshold. Use validated signals and task-specific rules where thresholds matter.

Choose the primary outcome, hard constraints, acceptable trade-offs, subgroup checks, and ship/iterate/stop criteria before inspecting candidate results. Improvement in one dimension can justify a bounded decline in another; violating a hard constraint cannot be hidden by an average gain. A 15% cost increase is neither universally acceptable nor an automatic failure.

### 4. Run the appropriate evaluation tiers

| Tier | Purpose | Illustrative starting scope |
|---|---|---|
| Smoke | Catch obvious breakage quickly | 10–20 canonical tasks after a change |
| Regression | Preserve known capabilities and prevent recurrence | 100–200 representative tasks and known failure cases before release |
| Stress | Probe boundaries, adversarial inputs, long contexts, and load | 1,000+ cases when breadth is needed; schedule by risk and change frequency |
| Golden set | Assess expert judgment, usefulness, tone, and taste | 20–50 curated examples with rubrics and acceptable response ranges |

These counts and schedules are examples, not evidence thresholds. Small, well-chosen sets can catch large defects; rare harms and subtle effects may require much more evidence. A golden example demonstrates quality without making one wording the only correct answer.

Cover the target behavior and plausible collateral effects: factuality, task completion, unnecessary refusal, access boundaries, output format, appropriate variation, latency, and cost. Include both positive and negative cases. Keep evaluation environments and comparison conditions controlled, and protect independent holdouts from repeated prompt tuning.

Review meaningful failures and grader disagreements. Use repeated trials where variability matters. Distinguish task failure from a broken test, unavailable dependency, or overly rigid grader. Record residual gaps instead of describing a passing suite as proof of production safety.

### 5. Choose and evaluate live exposure

Use live comparison when it answers an unresolved question that can be investigated responsibly. Specify assignment unit, cohort eligibility, exposure fraction, observation window, minimum useful evidence, and stop conditions. Keep assignment consistent at the user, account, session, or job level appropriate to the task; inspect shared-state contamination and concurrent experiments.

An initial 1–5% cohort can limit exposure in some services. It is not a universal minimum or sufficient sample. Duration depends on traffic, outcome delay, task diversity, relevant cycles, and detectable effect size. Three to five days does not cover a full weekly cycle; seven days does not automatically establish an effect.

Track verified outcomes and guardrails alongside acceptance, regeneration, edit distance, corrections, and abandonment. Those behavioral signals have multiple explanations: an accepted answer can still be wrong, and a regeneration can be creative exploration. Report sample sizes, denominators, uncertainty, and affected segments. Low-volume or rare-risk decisions may need expert review, targeted offline evidence, or a narrower release instead of a misleading A/B result.

### 6. Release with a tested recovery path

Tag the release, record who or what is receiving it, and confirm an owner can contain problems. Test restoration to a compatible, known acceptable configuration, including relevant dependencies and handling of in-flight tasks. Pin a task's effective configuration where changing it halfway would make behavior incoherent.

Set detection and recovery targets from the consequences and operating architecture. A five-minute rollback may be a useful local target; it is not a universal rule or a guarantee that no user will be harmed. Restoration can use routing, configuration, or deployment mechanisms as appropriate.

**Restoring the prompt does not undo completed external actions.** Reconcile uncertain writes, preserve evidence and authorization state, and use approved correction or compensation paths. If the old configuration is unsafe or incompatible, disable the affected capability, restrict exposure, or apply a reviewed fix instead of restoring it blindly. Automated rollback is useful when its triggers and effects are understood; some situations need human incident judgment.

### 7. Monitor, explain, and retain learning

Monitor by effective version and cohort, using both comparative and absolute service thresholds. Watch the initial release closely, then continue long enough to observe delayed outcomes and drift. Keep the deployment record linked to metrics, evaluation results, incidents, and subsequent decisions.

A drop associated with a version is an investigation lead, not proof of cause. Compare traffic mix, provider changes, retrieval freshness, routing, tools, caches, and other releases. Read failed examples before assuming the prompt became too long or a removed example caused the problem. Turn confirmed failures into regression cases and document why the chosen recovery worked.

## Estimate the experiment cost

For a simple illustrative treatment budget:

`daily eligible users × treatment share × sessions/user/day × tokens/session × blended price/token × days`

With 10,000 users, 5% treatment, one session each day, 2,000 tokens per session, a hypothetical blended $0.002 per 1,000 tokens, and seven days, treatment inference costs **$14**. This is not necessarily the incremental cost of the experiment: those users might otherwise have generated control costs.

For the actual budget, price input/output and cache categories separately when required; add extra replay or shadow calls, retries, tools, storage, evaluation, and human review. Compare treatment against the displaced baseline. Use `cost-model` for cost per verified outcome and scale effects. Test cadence should follow useful learning and operational capacity, not this example's low price.

## Five diagnostic questions

1. Can we identify and restore an acceptable prior configuration within the required recovery time, including compatible dependencies?
2. Can someone new understand both the diff and the reason for it?
3. Which important behaviors could regress outside the target metric, and what checks cover them?
4. Can we connect observed behavior to versions and cohorts while considering alternative causes?
5. Has the recovery path been exercised, including in-flight and completed actions where relevant?

## Release gate and decision

- [ ] Identifiable baseline, candidate, dependencies, owner, and reason for change.
- [ ] Relevant regression evidence reviewed against stated constraints and trade-offs.
- [ ] Exposure plan justified; any live experiment has a defined outcome, assignment, evidence requirement, and stopping rule.
- [ ] Recovery path tested at the required scope and speed; remaining limitations explicit.
- [ ] Monitoring by version and cohort, with action thresholds and an accountable response owner.

**Ship** when the evidence supports the stated scope and constraints. **Iterate or limit exposure** when benefit is unclear or evidence is insufficient. **Contain or recover** when a stop condition or known harm requires action. An urgent fix may need an explicitly documented, shortened route; it should not wait for an arbitrary experiment window to expire.

The trade-off is faster iteration versus the cost of discovering regressions after exposure. Keep enough discipline to make the decision reliable without turning a low-impact edit into process for its own sake. Version records, dashboards, and rollback documents help only when people can use them under real operating conditions.

Deliver a concise release note: version and intent; evidence and limitations; decision and scope; accepted trade-off; recovery trigger; next action and owner. For a formal gate, hand this to `ship-decision`. Use `eval-driven-development` and `eval-framework` for measurement, `determinism-compass` for acceptable variation, and `production-observability` for ongoing detection and response. `marketing-to-ai-agents` covers influencing external AI buyers; it is a separate demand-side application of product information and context.

If a diagram would clarify ownership or recovery, show the seven stages and the recovery branches with `excalidraw-svg`. A visual is optional. For source notes and reusable release fields, see [Release evidence and record](references/release-evidence.md). The shared Universal Skill Protocol supplies cross-skill handoff conventions; scale its use to the task.
