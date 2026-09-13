---
name: harness-operating-model
version: v1.3.1_latest
description: 'Plan how to fund, staff, operate, and maintain the system around an AI agent. Use for harness budgets, ROI reviews, ownership decisions, deployment and vendor choices, or capability-retirement plans. Compare the reliability dividend and other benefits against full costs; assess review capacity, five maturity stages, four organization models, the AI-spine and Assembler patterns, and four deployment shapes. Separate capabilities that may move into models or managed platforms from responsibilities the organization must continue to govern. Produce a proportionate operating plan with a baseline, budget, owners, evidence, next investment, and stopping conditions. Treat cost ratios, timelines, staffing counts, and moat claims as hypotheses to test. Agent-harness covers the machine and diagnosis; this skill covers the program. Pairs with cost-model, token-economics, build-or-buy, adoption-launch, alignment-check, capability-tracking, and moat-finder.'
imports: [agent-harness, cost-model, capability-tracking]
---

# The Harness Operating Model

Decide what operating capability the workflow needs, who will own it, how it will be funded, and when to expand, change, or stop investing. Use `agent-harness` to diagnose the machine; use this skill to make the surrounding program viable.

Start with the workflow, customer or employee outcome, current alternative, expected scale, consequential actions, and constraints. A small managed workflow may need a short plan and an existing owner. A shared agent platform may need a larger program. Neither requires a new team merely to satisfy a maturity label.

Produce an operating plan with a supported value case, complete costs, ownership and authority, deployment boundaries, review capacity, change policy, and the next decision. Separate observed results from forecasts and illustrative planning numbers.

## 1. Establish the value case

The **reliability dividend** is value gained by preventing failures, detecting them earlier, reducing their impact, or recovering more effectively. It can make useful delegation feasible. A harness can also change the quality of model decisions by supplying better context, tools, routing, and verification; it does more than reduce the cost of an unchanged wrong answer.

Include all relevant benefit channels:

- Better completed work, quality, or customer outcomes.
- Less rework, interruption, loss, and remediation.
- Faster delivery or reduced effort where those gains matter.
- Greater capacity or new kinds of useful work.
- Evidence and controls needed to operate within the organization's obligations.

Do not dismiss productivity as a weak pitch or promise that every error becomes recoverable. Authority is not granted in exact proportion to cheap failure; consequence, demonstrated performance, control quality, user expectations, and policy also matter.

For an economic comparison, use the same workload, timeframe, completion standard, and scope on both sides. Estimate baseline and proposed failure exposure by incident class, with uncertainty. Avoid double-counting saved effort as both cash savings and extra revenue. Capacity becomes financial value only through an explicit use or cost change.

```text
Incremental net benefit for a period
= incremental value of completed work
+ realized savings and avoided losses
− incremental operating costs
− investment costs allocated or incurred for that comparison
```

Use the appropriate cash-flow treatment for payback or investment appraisal. Keep important non-financial outcomes visible rather than forcing unreliable monetary values onto them. `cost-model` and `token-economics` provide the detailed analysis.

The historical $9/20-minute unusable attempt versus $200/six-hour deliverable is a practitioner anecdote. It illustrates why cost per valid outcome may matter more than cost per attempt. It does not isolate the effect of a harness or establish what a similar program should cost.

## 2. Budget the full program

Keep the five often-missed cost centers explicit, then add execution costs without hiding them under maintenance.

| Cost center | Include |
|---|---|
| **1. Evaluation and reference outcomes** | Domain-expert time, case design, labeling, rubric development, test execution, judge calibration, and maintenance. |
| **2. Engineering and product capacity** | Implementation, integration, reliability work, product decisions, and the opportunity cost of diverted staff. |
| **3. Observability and records** | Instrumentation, storage, access, retention, analysis, privacy handling, and incident investigation. |
| **4. Human review and escalation** | Review effort, queue management, reviewer training, specialist availability, and support tooling. |
| **5. Maintenance and migration** | Version changes, dependency testing, repair, policy updates, deprecation response, and exit preparation. |

Also account for **inference, tools, retrieval, runtime, sandbox compute, network, licenses, and vendor support**, where applicable. Shared costs may be allocated across workflows; avoid counting the same platform cost twice. Cost ranking depends on the deployment. Tokens are not inherently the fifth-largest expense, and evaluation data is not automatically training data or available for training.

### Make the human-review line concrete

Illustrative load: `10,000 sessions/day × 3% routed to review × 5 minutes = 1,500 minutes = 25 review-hours/day`. That is workload, not sufficient staffing. Allow for peaks, shift coverage, utilization, breaks, training, complex cases, rework, and urgent response. Measure completion latency and backlog as well as average handling time.

A review queue can be a designed part of the system without reducing the human to a passive component. Give reviewers evidence, competence, workload limits, and real authority. Synchronous review can work at high volume with adequate resources; exception-based review can fail if it misses important errors. Choose the design by task and consequence, not a universal 10/100/1,000-actions rule. See `judgment-guard` and `adoption-launch`.

### Treat the cost shape as a scenario

**Front-load → plateau → compounding benefit** is one possible trajectory:

1. Initial work creates contracts, controls, integration, and evaluation.
2. Stabilization may deliver less visible improvement while reducing incidents.
3. Reuse and learning may lower onboarding effort or improve later outcomes.

These stages need not take one year each or occur in that order. A vendor-based deployment can start cheaply; growth can increase costs; a platform may never justify expansion. Show actuals, scenarios, assumptions, and the conditions under which reuse would pay. A “Year 2 plateau” is not an explanation that excuses missing value, and CFO enthusiasm is not break-even evidence.

## 3. Compare investment, dependencies, and alternatives

### Lock-in and runtime exposure

The **lock-in wedge** is future dependence created by today's interface, memory, workflow, data, or commercial choice. Estimate migration effort, service interruption, data export, retraining, and lost capabilities. Open source can also create coupling; a managed platform can provide portable interfaces and exports. Do not assign 60% of workflows to closed platforms and 40% to open ones without examining them.

The **runtime wedge** is the cost and responsibility of durable execution, scheduling, checkpoints, tenancy, and isolation that may be overlooked in a model-only budget. Account for it where incurred; do not add an automatic 30–40% surcharge.

Cost, quality, and speed often trade off, but a better design can improve all three. State which constraints bind and test each outcome rather than invoking a fixed “pick two” rule.

### Stop, hold, or redirect effort using evidence

Review the next investment against:

- Its expected marginal benefit, uncertainty, cost, and operational obligation.
- Remaining important failure modes and the ability to measure progress.
- Alternatives: a smaller change, a different model, a purchased capability, narrower scope, another workflow, or stopping the use case.
- Vendor roadmap confidence, timing, access, and the cost of waiting.

A flat aggregate score can hide an important rare-error improvement; less than one percentage point after three edits is not a universal stopping rule. A workflow at 95% can still need substantial work. A roadmap announcement is not a shipped substitute. Expanding coverage may be better than deeper work, or may spread an inadequate control to more users.

Fewer recurring prompt repairs, earlier regression detection, and requests to expand are useful operating signals. Calculate break-even from the relevant benefits and costs; these signals do not establish it alone.

## 4. Assign ownership and choose an organization model

Name an accountable program owner and the people authorized to change policies, permissions, workflows, evaluations, and production configuration. Shared responsibility can work when the division and escalation path are explicit. Do not assume model, tools, and environment already have owners while only the harness lacks one.

| Model | Arrangement | Useful when | Watch for |
|---|---|---|---|
| **Harness-as-Platform** | A central team supplies shared orchestration, evaluation, registry, and controls. | Workflows share enough needs to justify a common service. | Queues, weak fit, and product teams building ungoverned alternatives. |
| **Harness-as-Feature** | Product teams own their workflow's harness. | Needs differ or a small local implementation is sufficient. | Duplicate infrastructure, divergent controls, and learning that does not travel. |
| **Harness-as-Operating-Model** | Harness design and evaluation are central to how the product organization delivers work. | Agent execution is integral to the product and operating process. | Overstandardization, unclear business ownership, and expensive change. |
| **Harness-as-Deployment** | A forward-deployed team adapts and supports a customer-specific system. | Customer integration or domain work needs sustained close involvement. | Dependence on individuals, weak knowledge transfer, and unclear customer authority. |

These can coexist. The source's 12+ teams, 2–8 teams, fewer than 500 staff, and 30% maintenance-time threshold are planning examples, not selection rules. Incumbents can adopt relevant practices without copying an AI-native organization wholesale.

Distinguish **internal deployment governance** from **customer delivery**. The source uses the unexplained acronym “MDASH” for the former; use plain language unless the team has defined it. Buyers may use embedded or forward-deployed teams, and sellers still need internal governance. Set responsibilities and incentives from the work, not from the buying/selling label alone. Staff continuity, succession, and customer knowledge transfer matter more than treating engineer retention as an anti-poaching tactic.

### The Harness PM responsibility

This role coordinates the product's failure modes, evaluation priorities, cost envelope, tool scope, escalation experience, and proposed changes in autonomy. It may be an existing PM or a dedicated role. It is not automatically the highest-value hire, and model/platform PM roles can also own reliability and domain outcomes.

Give the owner enough technical understanding and decision authority to connect product value with operational evidence. They should know key uncovered risks, recent improvements, limits of the evals, and current cost and service performance. “Eval coverage percentage” needs a defined denominator; an arbitrary top-three/last-five recital is not a competence test. Permission expansion may require business, technical, security, or other authorized owners beyond the PM.

### Two additional patterns

**The AI spine:** a cross-functional structure brings technical and business-process knowledge together. The source proposes a technology/platform owner, AI engineers, and embedded risk/compliance, connected to a business owner, knowledge owner, and end users, under executive sponsorship. Business ownership includes deciding whether an underperforming use case continues. Knowledge ownership includes curating reference material and judging domain adequacy within agreed authority. It does not override required safety or policy constraints.

Biweekly internal meetings and monthly user sessions are possible cadences. A model in which the spine retains a share of verified revenue or savings may support reinvestment. It can also create inflated attribution, reluctance to fund controls, and short-term incentives. Define benefit measurement, independent review, allocation, and funding for obligations without direct revenue. Funding design does not eliminate political disagreement.

**The Assembler:** a small team maintains reusable identity, memory, orchestration, interception, and observability/evaluation components, while workflow teams own their composition and outcomes. The source's one PM plus one engineer and approximately ten-workflow trigger are illustrative. Staff for demand, shared complexity, and support needs. Keep common primitives useful without silently taking over all business logic.

## 5. Choose deployment boundaries and vendor responsibilities

Assess four separable layers: **model service**, **runtime**, **execution environment**, and **business systems and authority**. Decide where data, files, processes, credentials, tool results, session state, and logs may exist. Then compare configurations against those requirements.

| Deployment shape | Typical split | What to establish |
|---|---|---|
| **A. Vendor-managed** | Provider operates model, runtime, and sandbox. | Actual isolation, access, retention, service limits, control interfaces, and shared duties. |
| **B. Hybrid** | Provider supplies some model/runtime services; customer hosts selected tools or execution. | What data still crosses the boundary, including prompts, arguments, results, metadata, and logs. |
| **C. Composed** | Runtime, model, and execution services come from multiple providers or components. | End-to-end identity, policy, tracing, recovery, support, and ownership across interfaces. |
| **D. Customer-managed** | Customer operates the selected stack. | Engineering and security capability, isolation, dependencies, updates, and actual control over every relevant service. |

No shape is inherently fastest, most flexible, or compliant. Sensitive or regulated work can sometimes use appropriate managed services; local execution alone does not make all data private or satisfy every requirement. Verify the exact deployment and applicable rules through the relevant specialists and `safety-by-design`.

Write a shared-responsibility matrix for operations, business permissions, data handling, validation, response, and recovery. A vendor may carry meaningful contractual and operational responsibility; selecting that vendor does not by itself settle what consequences the organization permits.

Orchestration is not isolation. Isolation is not proof of safety. A container with broad network access and inherited credentials may have a wider effect than its label suggests. A durable runtime can repeat a side effect unless the action and recovery contract prevent it. Route action contracts to `tool-architecture` and incident exposure to `agent-risk`.

### Build, buy, and retain control deliberately

Separate **source availability**, **customization**, **operational control**, **portability**, and **commercial dependence**. “Open” and “closed” alone are insufficient. A rented harness still needs domain evaluation, workflow ownership, adoption work, and vendor review; the team is not reduced to filing feature requests.

Domain rubrics, workflow policies, and authority decisions commonly need strong internal ownership. Implementation of tracing, retrieval, runtime, dashboards, and tool libraries can often be purchased. These are candidates, not mandatory boundaries. A short specification does not make outsourcing appropriate, and domain complexity does not prohibit competent outside support. Use `build-or-buy` for the comparison.

## 6. Assess maturity and choose the next useful improvement

The five-stage ladder is a diagnostic aid. Teams can have different maturity by responsibility.

1. **Prompt:** an initial model call and task instruction.
2. **Retry:** basic parsing and recovery behavior.
3. **Eval suite:** explicit outcomes and representative checks.
4. **Harness:** coordinated context, actions, verification, and operational controls.
5. **Harness discipline:** ownership, versioning, incident learning, migration, and continuing review.

Do not infer that 60–70% of teams sit at stage 2, that every stage-3 transition removes most pain, or that only stage-5 teams renew. Identify the actual gap affecting this workflow.

### A nine-part audit, schedulable as a nine-day starter kit

1. Map actual components against `agent-harness`: Model, Harness, Tools, Environment; the five clusters; and governance. Do not invent an unexplained eleven-component checklist.
2. Inspect a representative and risk-relevant sample of traces, including successes and failures. Fifty is a planning example.
3. Interview the engineer and operational responder about recurring workarounds and hidden work.
4. Catalog tools, MCP servers where used, agent identities, permissions, and external dependencies.
5. Compare important production failures with current evaluation coverage.
6. Write the evidence-based maturity diagnosis, including strengths and unknowns.
7. Create prioritized changes with owners and acceptance criteria. Four tickets is optional.
8. Establish or improve the trace-to-eval loop. Five cases and one CI integration can be a starter; validate any model judge against representative expert decisions, including severe disagreements.
9. Assess each important cluster as portable, partially portable, or coupled, with an exit cost and test. Three coupled clusters are not an automatic failure.

The work may take less or more than nine days. The source's >90% judge agreement on 50 cases is not a universal standard: agreement can be inflated by common easy cases. Use metrics and uncertainty appropriate to the error cost.

Track **recovery rate** as `eligible errored sessions reaching the defined valid outcome without human intervention / eligible errored sessions`. Define error, eligibility, valid outcome, and observation window. Report cost, harm, timeout, and escalations alongside it. A system with more unnecessary retries can improve this rate while worsening the service. The historical 30–50% before and 70–80% after ranges are not validated targets.

## 7. Plan what changes and what remains accountable

The **dissolving ladder** distinguishes two possible migrations:

- **Into a model capability:** better output structure, tool use, long-context handling, reasoning, or safety behavior may reduce particular workarounds.
- **Into a vendor's harness or platform:** orchestration, persistence, and other services may become purchased capabilities, with a different cost and dependency profile.

Neither is guaranteed. Long context does not eliminate retrieval freshness or access controls; structured generation does not eliminate semantic validation; model safety does not replace action policy. Before retiring a component, identify every job it performed and ensure the replacement covers each necessary one. A generic JSON schema also never proved factual meaning by itself.

Keep five continuing responsibilities visible, whether implemented internally or through a provider:

1. **Domain evaluation and reference outcomes:** what counts as a good result and how that standard is maintained.
2. **Organizational workflow and authority:** how work connects to real decisions, systems, and obligations.
3. **Observability and records:** what evidence is needed, who may access it, and how its integrity and retention work.
4. **Cost and capacity controls:** what the organization can spend and how it handles variable demand.
5. **User context and memory:** authorized, relevant, current state with appropriate privacy controls.

These are continuing responsibilities, not five implementations that no model or vendor could ever supply. A model is not a revenue-seeking actor adversarial to the customer; supplier incentives and billing terms are the relevant economic issue. Add **availability and degraded operation** when continuity requires it, with tested alternatives rather than assumed instant provider switching.

For each capability, ask whether it is generic or specific, benefits from scale, is attractive for a provider to supply, and can be improved through a validated automated evaluation loop. Use these as scenario inputs, not a three-yes forecast of absorption by 2027. Automated improvement still needs controlled objectives, held-out checks, authority boundaries, and monitoring for metric gaming.

## 8. Test the advantage and explain the plan

A harness, proprietary model, dataset, or other asset can contribute to advantage. None is automatically a moat. Ask whether the improvement matters to users, whether the organization captures its value, how competitors could reproduce it, and what must keep working. `moat-finder` owns the deeper assessment.

A trace→eval→change loop can improve the system, but it can also overfit observed cases or reinforce a weak rubric. Keep held-out cases and independent calibration where useful. A 50–100-item sanitized subset is a possible starting point, not enough by definition; public benchmarks may measure a different task and are not mandatory if sharing would violate data rights.

Translate the same evidence for different stakeholders:

- **Engineering:** which failure classes and maintenance work the investment should reduce.
- **Design and users:** how behavior, recoverability, and review experience should improve.
- **Executives and budget owners:** expected outcomes, cost, uncertainty, and the next expansion or stopping decision.
- **Security and other control owners:** which boundaries and records the design supplies and what still needs review.

Avoid promising that every trace is a compliance artifact or every dollar buys future autonomy. User adoption and buyer value are different questions; explain both without inventing a second benefit. `stakeholder-communications` supports the wording.

## Final operating-plan check

Confirm a comparable baseline, complete budget and scenarios, named owners with usable authority, sufficient review/response capacity, deployment responsibilities, and a justified next investment. Include important dependency risks, retirement or re-evaluation triggers, and evidence that could change the decision.

Use the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md) for proportionate trade-off and handoff records. A cost scenario, organization map, or responsibility diagram can help; use `excalidraw-svg` when useful. Do not draw an inevitable Year-3 break-even curve as if it were a measured forecast.

For the machine use `agent-harness`; for economics use `cost-model` / `token-economics`; for adoption and readiness use `adoption-launch` / `alignment-check`; for changing capabilities use `capability-tracking`; and for defensibility use `moat-finder` / `safety-as-moat`. See [evidence and worked examples](references/evidence-and-worked-examples.md) for the source cases and numerical limits.
