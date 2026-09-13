---
name: rtp-build-or-buy
version: v2.6.1_latest
description: 'Choose how to obtain an AI capability and which parts to own. Compare prompting, examples in context, retrieval-augmented generation, fine-tuning, and a finished vendor product; these can be combined. Use six checks for task fit, simpler baselines, data, latency, economics, and ongoing ownership. Reject an option that fails a critical requirement without assuming every other option fails too. Assess data rights and provider reuse before testing sensitive work, and include orchestration, review, support, and switching costs. Use for feature scoping, vendor renewals, custom-versus-API decisions, or model-tuning proposals. Pairs with moat-finder, cost-model, agent-harness, invisible-stack, determinism-compass, and ai-portfolio-management. Triggers: build or buy, fine-tune versus prompt, RAG versus API, should we train a model, vendor replacement.'
imports: [determinism-compass, stress-test, agent-harness]
---

# Build or Buy

Choose the combination of capability, ownership, and supplier that meets the task’s requirements at an acceptable lifecycle cost. Separate what creates distinctive value from what simply needs to work well.

**Building an application, fine-tuning a model, hosting a model, and training a model from scratch are different commitments.** A custom application can use a purchased API; a vendor can host a fine-tuned model; RAG and fine-tuning can work together. The five approaches below are useful design choices, not mutually exclusive rungs on a ladder.

## Frame the decision and its constraints

Reuse known context and follow the Universal Skill Protocol at the source library root or packaged plugin root. Establish the customer, task, current alternative, required outcome, consequences of error, data restrictions, expected volume, response-time needs, available capacity, and decision horizon. Name the work this commitment would displace.

Use a short comparison for early exploration. Go deeper for a consequential deployment, renewal, difficult migration, or substantial ongoing commitment. Cost and data rights can matter before product–market fit or at a single customer; ten thousand users is not a threshold for taking them seriously. In research, learning may itself be the benefit, but it still needs a bounded budget and appropriate controls.

Before sending data or buying anything, establish the authorized scope of the task and the applicable data/contract constraints. The output of this skill is a reviewable decision and next step, not automatic permission to procure, upload restricted material, or deploy.

## 1. Decide what to own and what can be sourced

Identify the asset: customer relationship, workflow, data and rights, evaluation knowledge, operating capability, model customization, or another contribution. Test whether owning a particular component improves outcomes, control, resilience, economics, or defensibility. Team expertise is a resource to consider, not proof that its preferred architecture fits.

Use these companion lenses where relevant. Their full case connections and limits are in the [ownership reference](references/ownership-and-provider-boundaries.md).

| Lens | Decision to examine |
|---|---|
| **0. Capability versus advantage** | Does buying or building the capability create an advantage, preserve parity, or merely provide a tool? Acquisition alone does not settle this |
| **1. Task-level sourcing** | Which routine, knowledge-sensitive, occasional specialist, or consequential judgment tasks need different sourcing and oversight? Keep workflow handoffs in view |
| **2. Vendor replaceability** | Does the product retrieve stored information or estimate something uncertain, and does its value depend on one organization’s data or a shared corpus? Inspect actual rights, reliability, integration, and replacement cost |
| **3. Operational history** | Which relevant history is difficult to reconstruct, and can a purchased tool use it while the organization retains appropriate rights and control? Owning data does not require owning the model |
| **4. Bargaining position and hold-up** | What credible alternatives remain after the purchase, and which investments would be useful only with this supplier or channel? Price transition and retained capability |
| **5. Jurisdiction and availability** | Which providers and deployment routes are actually permissible and available for the workload, including failover? Validate specific restrictions rather than inferring them from a provider category |
| **6. Stock and flow** | Does value come from an archive, continuing new information, or both? Examine relevance, exclusivity, rights, refresh needs, and reuse instead of treating either form as a guaranteed moat |
| **7. Partnership capacity** | Can a partner supply missing delivery capability, and what integration, governance, IP, data, and coordination work remains with us? |
| **8. Organizational level** | Does the relevant asset or economy of scale exist within one team, across the company, or across a portfolio? Place shared work where it can be supported and governed |

### Check what each provider can receive and reuse

For any proposed service, identify the product, account type, deployment route, settings, contract version, and data flow. Review inputs, outputs, retained logs, feedback, ratings, corrections, support submissions, third-party tools, and any synthetic-data use separately where their terms differ. Distinguish access, retention, permitted reuse, actual reuse, and demonstrated competitive effects.

A statement that content is not used for general model training can be a meaningful protection. It does not answer every question about storage, feedback, support access, or confidentiality. Conversely, a feedback clause is not proof that all customer interactions train a shared model. Verify current primary terms and obtain the relevant contractual interpretation for material uncertainties.

Compare sanctioned commercial services, private or dedicated routes, self-hosting, and decomposition according to the actual requirements. “Private cloud,” “on-premises,” and “sandbox” are not guarantees by label: inspect telemetry, network egress, access, updates, and operational controls. A routine task may still contain sensitive information, while a differentiating workflow may be usable with an appropriately governed service.

Reducing friction in an approved route can help avoid unauthorized workarounds; do not assume restrictions inevitably cause them or treat personal accounts as outside all rules. Investigate actual behavior. The provider-learning claim in Novel Insights is a hypothesis with explicit limits, not an established consequence of every API call.

## 2. Compare the five approaches and a simpler baseline

| Approach | What it does | When it is worth testing | What remains to manage |
|---|---|---|---|
| **Prompt + model/API** | Supplies instructions to an existing model | General capability may already meet the task | Evaluation, prompts, service changes, permissions, cost, and integration |
| **Examples in context** | Demonstrates desired behavior in the request without updating model weights | Examples may resolve a behavior or format gap | Example quality and selection, context limits, privacy, latency, and recurring token cost |
| **RAG + prompt** | Retrieves relevant permitted material and supplies it at inference time | Current or proprietary information needs to be available to the answer | Retrieval quality, freshness, access enforcement, citations, and answer evaluation |
| **Fine-tuning** | Further trains a base model for a defined behavior or objective | A measured quality, consistency, efficiency, or other requirement justifies adaptation | Training/evaluation data, regressions, hosting route, versions, monitoring, and ongoing ownership |
| **Vertical SaaS** | Provides a more complete product for a particular workflow | A vendor meets enough of the actual requirement at a worthwhile total cost | Procurement, configuration, integrations, oversight, user support, data, and exit planning |

Also compare the current process, ordinary code or rules, search, a smaller model, and a hybrid where appropriate. An exact lookup or calculation may need no generative model. RAG supplies context but does not guarantee a correct answer. A finished product reduces some work rather than eliminating all maintenance.

Avoid generic price, accuracy-gain, or shipping-time ranges. Record dated estimates or measurements for the selected configuration and workload. The reference retains the earlier ranges as illustrations, not selection criteria.

## 3. Run six checks on the candidate approach

Keep the familiar gate identifiers—1, 1.5, and 2–5—for existing handoffs. There are six checks. A failed hard requirement rules out the **current candidate or scope** until resolved. It does not automatically select another option. Passing every check makes an option eligible; compare eligible alternatives before committing.

### Gate 1 — Task and evaluation fit

Define what a useful result must accomplish and how it will be evaluated. Separate **correctness**, **repeatability**, and **acceptable variation**, using `rtp-determinism-compass` where needed. Classification, extraction, and ranking can involve uncertain labels or probabilistic models; generation can have meaningful, verifiable quality requirements even when several answers are acceptable.

Create a small, representative evaluation slice and important difficult cases. Agree on the rubric, reference evidence, severity of errors, and handling of ambiguity. Disagreement can reveal a missing specification or legitimate uncertainty; it does not by itself rule out fine-tuning. A twenty-case slice can expose a problem but cannot establish broad performance by itself.

Fine-tuning can improve style, format, domain behavior, tool use, or other open-ended output. It can also teach poor habits. Evaluate the actual gain and regressions rather than assuming pretraining contains all useful behavior or that a rubric-based gain is unreal. Coding, medical coding, and support drafting need task-specific evaluation; neither one clinical note nor one support question necessarily has exactly one acceptable answer.

### Gate 1.5 — Simpler baseline and examples in context

Test a credible prompted baseline, then useful improvements such as clearer instructions, selected examples, retrieval, output constraints, a different model, or a smaller scoped task. Choose examples and configurations on development data. Keep final evaluation cases and answers separate from the prompt and training process; supply test inputs without their target answers.

Few-shot learning predates 2023. Larger context can make more examples possible, but capacity, effective use of context, latency, and price depend on the actual model and request. Fifty examples are an option to test, not a required experiment. More examples may help, do nothing, or hurt.

Compare quality, total cost, and latency on the same workload. A baseline meeting the quality floor may still warrant tuning to reduce cost or delay; a small shortfall may be critical in a consequential task. There is no universal 15% gap that justifies tuning. Distinguish percentage points from relative percentages, and change an acceptance threshold only for a defensible product reason, not to declare a convenient pass.

Use a short, bounded experiment where it can cheaply resolve the choice. If a known constraint rules out a candidate, record it rather than running an irrelevant trial. If a simpler solution already meets the full requirement at acceptable cost, explain what additional benefit would justify customization.

### Gate 2 — Suitable data and permission to use it

For supervised tuning, inspect the task examples, target outputs, provenance, rights, label process, coverage, freshness, and held-out evaluation. Logs are not automatically validated labels. Some tuning methods use other training signals; define the objective and data it requires rather than applying a supervised-label rule to every method.

Quantity is only one factor. There is no general thousand-example minimum, no guarantee at ten thousand, and no automatic overfitting result at four hundred. Use learning curves, held-out results, error analysis, and meaningful subgroup checks. Small datasets or synthetic examples can help when relevant and validated; their construction costs, artifacts, and missing cases still matter.

Audit a useful sample with appropriate reviewers. Distinguish raw agreement, chance-adjusted agreement where relevant, adjudicated correctness, and downstream consequences. A universal 85% agreement cutoff is not a substitute for examining disagreements. Separate train, development, and test sets at the level needed to prevent leakage between near-duplicate cases, customers, or time periods.

Sensitive data can narrow hosting choices without requiring a custom-trained model. A purchased or open-weight model deployed in an acceptable environment may meet the need. Check availability, licensing, and actual protections before recommending it.

### Gate 3 — Latency and throughput in the real workflow

Define the relevant measure: time to first useful response, complete result, tool completion, or deadline. State load, concurrency, task mix, response length, region, and warm/cold conditions. Measure distributions and consequential tails, including P95 where useful. P95 is a percentile of the measured observations, not a guaranteed maximum or a statement about 95% of unique users.

Test end-to-end behavior for each plausible route, including retrieval, model calls, validation, retries, queues, and network time. A sub-100 ms requirement may favor local execution, cached results, or simple code, but does not by itself mean “buy” or make all remote processing impossible. Async work still has deadlines, queue capacity, and completion-cost constraints.

Choose performance targets from the task rather than generic autocomplete or support-response limits. Before production, prototypes, load tests, and component estimates can identify a real constraint. When using estimates, name what remains unmeasured and how it will be checked. Cache only where relevance, freshness, permissions, and equivalence support reuse.

### Gate 4 — Lifecycle economics and opportunity cost

Compare alternatives that meet the required outcome and controls. Include:

- Upfront engineering, data preparation and validation, training, integration, migration, evaluation, and procurement.
- Recurring input/output and cached-token charges, model serving, retrieval, tools, storage, observability, retries, and support.
- Human review, correction, fallback, maintenance, incident response, learning, and user adoption.
- Transition and exit costs, commitments, price or volume uncertainty, and engineering capacity displaced.

Use current primary prices and measured token mixes for the actual product, tier, region, and service terms. A difference in price per thousand tokens is not a saving per call until tokens per call and all other charges are accounted for. Compare cost per attempted task and per successful useful outcome, with quality and consequence alongside both.

Ratios to labor cost or gross margin can provide context. They are not universal buy thresholds: a small ratio at enormous volume can still matter, and a large ratio does not prove fine-tuning is cheaper. Define whether margin is measured before or after the AI cost to avoid a circular denominator. Budget impact, value, and alternative uses of capacity all matter.

Model the chosen horizon under conservative, base, and optimistic assumptions, including current and plausible higher volume where useful. Calculate incremental net savings, payback where meaningful, and discounted value for a material multi-period decision. Use `rtp-cost-model`, `rtp-token-economics`, and `rtp-ai-portfolio-management` for detailed treatment. Avoid adding both a full labor charge and the same foregone output as separate cash costs; show opportunity cost distinctly.

The [calculation reference](references/evidence-and-calculations.md) corrects the original payback and retry examples. No eighteen- or twenty-four-month payback rule applies to every organization. If the candidate costs more, it may still be justified by additional outcomes or necessary controls; state and evaluate that reason explicitly.

### Gate 5 — Ongoing ownership, recovery, and exit

Name the operating owner, required capabilities, funded capacity, backups, service commitments, and escalation path for the expected lifecycle. Confirm access to evaluation, monitoring, incident response, data refresh, and a viable hosting or vendor route. Enthusiasm is not a staffing plan, but a motivated proposer is not disqualified from becoming the owner.

Use managed services, shared specialists, or a dedicated team as the workload requires. Neither a dedicated ML engineer nor 40% of one person’s time for twenty-four months is a universal threshold. Conversely, an unfilled future hire does not cover a current critical responsibility.

Define triggers for reassessment or retraining from performance, drift, task change, data, provider support, cost, and risk. Quarterly retraining is an option, not a requirement; unnecessary retraining can introduce regressions. Test new versions before release and maintain an appropriate rollback or replacement path. A base-model update does not automatically update a tuned derivative.

Keep enough internal competence to evaluate the supplier and execute a credible transition where its value exceeds the cost. Model replacement, vendor migration, retained human practice, and operational fallback are distinct options. Record how long each would take and what would be lost.

## 4. Include orchestration in the same comparison

Prompting, RAG, fine-tuning, and vendor products can all contain orchestration. Compare a simple workflow with more complex designs on quality, latency, reliability, successful outcomes, and total cost. Multiple calls may be sequential, parallel, or conditional; independent subtasks are not the only valid reason to orchestrate.

Use `rtp-agent-harness` for the architecture decision. This skill does not authorize or require spawning agents. A universal 30% quality lift or 10–22× cost multiplier cannot choose the design. Measure call counts, token sizes, tools, evaluation, retry behavior, and human effort; complexity can be worthwhile at a small lift if the outcomes justify it, or wasteful at a large lift if the base task has little value.

Recalculate the economics when the actual workflow changes. Cost per successful outcome is not the same as cost per request. A twenty-percent retry rate adds twenty percent to full-attempt cost when at most one same-cost retry occurs on twenty percent of requests; an unlimited independent geometric retry process has a different expectation. Use the actual stopping and retry policy.

## 5. Make switching practical without overbuilding an abstraction

Separate application logic from provider-specific requests where this reduces expected migration and operating cost. A thin adapter can handle request/response formats, capability checks, routing, error handling, telemetry, and allowed fallbacks. Preserve model-specific capabilities where they matter; a conditional inside an adapter is not automatically a design failure.

Models differ in semantics, tool behavior, context, safety behavior, output format, and supported deployment routes. An API wrapper does not make them equivalent. Validate a candidate replacement on the task, its controls, and data permissions. A fallback provider needs to be permissible and technically suitable before it is used.

Estimate the cost of portability against likely switching needs. The original two-to-four-week abstraction effort, eight-to-twelve-week unabstracted migration, and under-two-week swap are examples without a general basis. Avoid a large compatibility layer for a small experiment unless a real requirement justifies it.

## Deliver and review the decision

Lead with the recommended combination and the component boundaries: what is built, purchased, hosted, customized, and retained. Include:

```text
Customer, task, baseline, requirements, and decision horizon:
Options compared, including a simpler or non-AI alternative:
Ownership thesis and applicable companion lenses:
Data flow, rights, provider reuse, and deployment constraints:
Six checks: evidence, pass/fail/unknown, and material limitations:
Quality, latency, lifecycle cost, and successful-outcome comparison:
Operating owner, capacity, recovery, and exit/switching plan:
Chosen scope, key trade-offs, assumptions, and contrary evidence:
Next action, owner, date, and revalidation triggers:
```

Check that the conclusion follows from measured or clearly labeled evidence; no numerical heuristic is treated as a law; training and evaluation data are separated; required controls apply to every eligible option; and the recommendation includes remaining work on the buy side. A privacy constraint, generation task, small dataset, or favorable score does not decide the architecture alone.

State what the choice gives up, the largest practical risk, reversibility and its cost, and what would change the decision. Revisit when a material assumption changes, not only at tenfold volume or a scheduled model release. A decision flow or cost chart is useful when it exposes a real trade-off; use actual results or labeled scenarios rather than generic accuracy gains.

Hand detailed architecture to `rtp-agent-harness` or `rtp-invisible-stack`, economics to `rtp-cost-model`, and competitive assumptions to `rtp-moat-finder`. Consult relevant research and Novel Insights with later qualifications for a consequential strategic claim; keep dated evidence separate from reusable principles.
