---
name: ai-portfolio-management
version: v1.6.1_latest
description: "Choose, sequence, fund, review, and stop AI initiatives as an interconnected portfolio. Use when initiatives compete for resources, share dependencies, lack clear funding decisions, or need governance across discovery and production. Combine project stage gates with a portfolio view of value, risk, time, capacity, and shared foundations. Classify five value mechanisms, use transparent scoring where helpful, and record Buy/Hold/Sell allocation decisions alongside Ravi’s Explore/Exploit/Exit hypothesis decisions. Match evidence and controls to the next commitment; protect bounded learning without allowing perpetual pilots. Pairs with strategy-canvas, moat-finder, build-or-buy, cost-model, gen-ai-experimentation, adoption-launch, and responsible-ai-program. Triggers: AI portfolio, initiative prioritization, investment review, stage gates, OPEN framework, AI Centre of Excellence."
imports: [strategy-canvas, moat-finder, build-or-buy]
---

# AI Portfolio Management

Make explicit choices about which AI work deserves the next commitment of money, people, data, and attention. Evaluate each initiative on its evidence and evaluate the portfolio on its combined value, dependencies, risk, and capacity.

**A high score cannot compensate for a critical control gap or unavailable capacity.** Early exploration should earn funding through a useful learning question and a bounded plan; scaling needs evidence appropriate to the actual scope. An initiative does not need to demonstrate production ROI before it can investigate whether the idea works.

## Establish scope and decision rights

Reuse context and follow the Universal Skill Protocol at the source library root or packaged plugin root. Identify strategic priorities, current and proposed initiatives, budget and people constraints, existing commitments, material risks, and who can allocate resources or authorize a stage transition.

Use a light version for a small team or a single initiative with competing alternatives. Three concurrent initiatives is a useful trigger, not an eligibility threshold. A pre-product team can use an opportunity list, experiment budget, and stop criteria without creating a governance board.

Keep two views connected:

- **Project pipeline:** where each initiative is, what it has learned, and what evidence or control is required for its next commitment.
- **Portfolio dashboard:** whether the mix makes sense across value mechanisms, time horizons, risks, capabilities, shared dependencies, and available resources.

The pipeline-and-dashboard approach draws on Hoque, Nelson, Davenport, and Scade’s portfolio framework. OPEN—Outline, Partner, Experiment, Navigate—is one way to name the stages; existing organizational terminology can serve the same purpose. The [evidence reference](references/evidence-and-calculations.md) records attribution and case limits.

## 1. Inventory initiatives and classify how they create value

For each initiative, record the problem and intended users, sponsor and operating owner, stage, next decision, expected benefit, primary outcome, costs, dependencies, risks, evidence, and current commitment. Include shared data, evaluation, governance, and workforce capabilities when other initiatives depend on them.

Use the five-type classification before choosing measures. Assign a primary type and secondary types where useful; revisit them as the initiative changes. The types describe value mechanisms, not a maturity ladder or an automatic sourcing decision.

| Type | Value mechanism | Useful measures and questions |
|---|---|---|
| **1. Competitive parity** | Maintains a needed capability or avoids losing customers, efficiency, or position | Cost and consequence of inaction, service outcomes, retention, cost to provide the capability |
| **2. Option value** | Creates a credible ability to pursue future opportunities | Named opportunities enabled, evidence gained, cost and time to exercise the option, conditions for doing so |
| **3. Unique integration** | Improves a process through a useful combination of data, workflow, and technology | End-to-end cycle time, errors, throughput, service or business outcomes, and integration/operating cost |
| **4. Data flywheels and lock-in ecosystems** | Repeated use may improve the product or strengthen a valued ecosystem | Verified learning-loop improvement, data rights and quality, customer value, retention and switching considerations |
| **5. Organizational capability building** | Develops skills and operating capability that support later change | Demonstrated capability, time and cost to adopt a relevant change, reuse and sustained operating outcomes |

Parity can produce a financial return without a durable competitive advantage. Strategic categories can produce near-term value, and their labels do not prove defensibility. A data flywheel needs an actual, permitted learning mechanism; collecting logs alone does not establish one. Option and capability investments need bounded commitments and evidence of useful progress, not an indefinite exemption from review.

Use both a measure specific to the value mechanism and an appropriate economic case. Where an initiative spans types, separate benefits and assumptions without double-counting the same outcome. It is acceptable to report a benefit qualitatively when monetizing it would create false precision.

## 2. Map dependencies and capacity before ranking

Identify the data, systems, models, suppliers, domain experts, decision-makers, and operating teams each initiative requires. Show shared bottlenecks and correlated risks. A shared dependency does not make all projects identical; assess each project and the combined exposure.

For every proposed commitment, answer:

1. **Who will do the work, and is the required participation available?** Check named expert involvement, time allocated, continuity, and reasons for changes in participation. Falling attendance may reflect a planned phase change, overload, or withdrawal. An unavailable critical capability blocks work that depends on it; a falling percentage alone is not an automatic stop rule.
2. **Where will the capacity come from?** Record what is postponed, stopped, simplified, reassigned, hired, sourced, or drawn from genuinely available capacity. If nothing is displaced, show why the work still fits. “We will absorb it” is not a capacity calculation.

Use `rtp-adoption-launch` for participation and manager-workload design, and `rtp-gen-ai-experimentation` for the support an experiment requires. Resources becoming available are a reason to reconsider the queue, not a reason to fund the highest score automatically. Moving a project into production may consume more operating capacity rather than release it.

### Treat foundations as investments with beneficiaries

Shared foundations may reduce duplication and risk. Define the users, required domains, ownership, service levels, rights, interoperability, and incremental delivery plan before funding a broad platform. Sequence the minimum useful foundation with dependent work. Neither a multi-year cleanup of all enterprise data nor a separate silo for every pilot is a universal starting point.

Five useful design checks, adapted from the Caterpillar case, are:

- Set an outcome target that identifies which data domains matter; revenue is one option alongside cost, quality, service, and risk.
- Give named business and technical owners clear responsibilities and decision rights.
- Fund the necessary lifecycle with milestones and reviewable commitments, including maintenance.
- Include relevant internal and external stakeholders in the design.
- Connect dependent AI initiatives to the capability where it is appropriate, with explicit exceptions and interfaces.

Measure three tiers: **enablement** through fitness of the asset for its intended use; **use and delivery** through meaningful adoption and process results; and **realized value** through attributable business or mission outcomes. Counts of accurate records and usage frequency can help, but neither alone establishes value. A named executive does not prevent duplication without workable governance.

AI-assisted data cleanup can itself be a bounded use case. Compare it with simpler methods, evaluate false corrections and missed anomalies, preserve provenance, and obtain domain review where needed. Do not assume it is cheaper or safe simply because it builds a foundation for other AI.

## 3. Use four stages with evidence for the next commitment

Define gate criteria before the relevant work where feasible. Make each criterion testable, give it an owner, and record met, unmet, unknown, or justified not-applicable status. Required controls must be in place for the approved exposure. A narrow experiment can need different evidence from broad production.

| Stage | Work and output | Decision criteria |
|---|---|---|
| **1. Opportunity — Outline** | Frame the need, alternatives, strategic connection, initial value/risk hypothesis, and dependencies. Produce an opportunity entry, not a disguised project commitment. | **Gate 1:** a worthwhile question, plausible approach, strategic or necessary operating rationale, initial impact/risk classification, and a bounded next step |
| **2. Design and Partnership — Partner** | Develop a proportionate business case, data and capability plan, experiment design, and governance. Consider internal, vendor, partner, and hybrid approaches through `rtp-build-or-buy`. Map changes to roles and work. | **Gate 2:** suitable and permitted data for the experiment; required skills and participation; scope-appropriate risk assessment, ethics and security controls; named accountable owner; credible budget and experiment plan |
| **3. Experiment — Experiment** | Test technical performance, integration viability, human usefulness, and cost through appropriate prototypes or trials. Seek findings that can change the decision. | **Gate 3:** evidence for the proposed scale, representative testing and relevant adversarial scrutiny, verified oversight/recovery, operating and integration costs, useful adoption evidence, and readiness for the actual deployment scope |
| **4. Scale and Operate — Navigate** | Deploy within the authorized scope; manage reliability, misuse controls, cost, service, workforce changes, knowledge, and actual outcomes. | **Operating review:** performance and controls remain adequate, value still justifies continued commitment, capacity exists, and material changes trigger renewed assessment |

Responsible AI belongs throughout this sequence. Use `rtp-responsible-ai-program` for the assessment and controls, including bias, misuse, unintended consequences, and accountable ownership. Record the result at every gate rather than attaching a generic policy. Red-team work and review depth should fit the threat and consequence; a completed exercise alone is not evidence that all risks are controlled.

Run experiments against meaningful alternatives and preserve contrary evidence. Multiple experiments can be useful when the team has capacity, but this skill does not require parallel agents. Production also involves learning; the shift to operating discipline does not mean discovery ends.

## 4. Compare initiatives with transparent judgment and economics

Assess four dimensions: **strategic alignment**, **technical and organizational feasibility**, **risk and reward**, and **resource requirements**. State the evidence and uncertainty behind each. Scoring makes judgments visible; it does not turn them into objective facts.

If the organization has a useful rubric, reuse it. Otherwise compare the dimensions descriptively first. For an optional numerical view, define 0–4 anchors for each dimension and weights that sum to one. Make higher always mean more favorable, including **resource fit** rather than raw resource quantity. Calculate `score /100 = 25 × Σ(weight × rating)`. Label it a decision aid, record unknowns separately, and withhold an aggregate when critical inputs are missing. Explain sensitivity to weights and close rankings.

Compare eligible choices with capacity, dependencies, mandatory obligations, and the value of additional learning in view. Avoid gaming through unexplained optimistic ratings. Review the rubric when evidence shows it is misleading; preserve comparable historical scores or mark changes rather than silently rewriting the criteria every quarter.

### Economic measures answer different questions

Use conservative, base, and optimistic cases with stated assumptions for adoption, quality, demand, implementation, ongoing operations, training, verification, support, and timing. Separate incremental cash flows, released capacity, and nonfinancial outcomes. Use `rtp-cost-model` for the detailed model and reconcile with the finance owner’s conventions.

| Measure | Defined calculation | Appropriate interpretation |
|---|---|---|
| **Simple ROI** | One explicit convention is `(cumulative incremental benefits − all incremental costs) / all incremental costs × 100` over a stated period | A compact undiscounted comparison; disclose the period and included costs. Different ROI conventions are not directly comparable |
| **Payback** | Time until cumulative net cash flows recover the initial outlay; `initial outlay / constant annual net cash inflow` is a shortcut only for that simple pattern | Indicates recovery time; ordinary payback omits discounting and benefits after recovery |
| **NPV** | `Σ from t=0 to T of incremental net cash flow_t / (1+r)^t` | Estimates value at the chosen discount rate and horizon; includes initial and later costs, not gross benefits alone |
| **IRR** | A rate at which the project’s NPV equals zero | A supplementary yield measure; it can be absent, multiple, or misleading for rankings across different cash-flow patterns and scales |

For mutually exclusive alternatives, assess incremental value and constraints rather than selecting the highest IRR. These distinctions follow standard [investment-appraisal guidance](https://www.accaglobal.com/hk/en/student/exam-support-resources/prodipsust-study-resources/technical-articles/investment-appraisal.html) and [ACCA’s discussion of NPV/IRR comparisons](https://www.accaglobal.com/content/dam/acca/global/PDF-students/acca/f9/exampapers/fm-2018-sepdec-sample-a.pdf).

For example, 1,875 released analyst-hours at $125/hour represents $234,375 of valued capacity under that rate assumption. It is not automatically an annual cash saving: specify the measurement period, whether time is actually released, its alternative use, and any costs required to realize the benefit. Shared platform benefits should be allocated or reported at portfolio level without being claimed in full by every dependent project.

## 5. Record an allocation decision and a hypothesis decision

The two labels answer different questions. Keep them consistent and state the actual budget, scope, and action so the labels do not obscure the decision.

### Buy, Hold, or Sell: what happens to the commitment?

- **Buy:** add an initiative or increase its commitment when the next scope is justified and capacity is available. This portfolio label does not mean buying software from a vendor.
- **Hold:** maintain a defined commitment for a stated reason and review point. It can support bounded exploration or continued operation; it is not an automatic extension.
- **Sell:** stop, reduce, or sunset a commitment and handle its dependencies, people, data, contractual obligations, and transition responsibly. It does not imply a literal asset sale.

### Explore, Exploit, or Exit: what does the evidence support?

**3E is Ravi Teja Palanki’s hypothesis-decision framework, introduced April 5, 2026.** Record one current decision at each material review:

| Decision | Meaning | Required next commitment |
|---|---|---|
| **Explore** | A useful uncertainty remains, and more learning is worth its cost | Name the hypothesis, experiment or evidence needed, budget, owner, decision date, and stop conditions |
| **Exploit** | Evidence supports delivery or operation within a defined scope | Specify that scope, resources, outcome and control measures, and conditions for review or expansion |
| **Exit** | Continuing this scope is no longer justified | State why, what stops, how obligations are handled, and whether any reusable asset or learning merits a separate opportunity |

Explore can be appropriate after an inconclusive Stage 3 experiment or for a new question discovered in production. It must earn another bounded commitment. Exploit does not require full-scale rollout or end all learning. Exit can be justified by one decisive constraint; it need not wait for many negative signals.

On exit, perform a proportionate **pivot check**: could a data asset, model, process, capability, or learning help a distinct adjacent problem? Reuse only what is transferable and permitted. Create a new opportunity with its own customer problem and assumptions; earlier evidence can reduce repeated work where it still applies, not waive the new gate. A valid answer is no. Avoid manufacturing a pivot merely to keep sunk work alive.

## 6. Rebalance and sequence the portfolio

Review the whole portfolio, not just status reports from its projects. A useful starting cadence is a monthly dashboard review and quarterly deeper rebalancing, adjusted for pace and stakes. Incidents, critical dependency failures, pricing changes, new evidence, or major strategy changes may require an earlier decision. Set responsible-AI and ethics review timing through the applicable program and record the next date.

Use a separate horizon/capability lens alongside the five value mechanisms:

- **Confidence builders:** relatively bounded initiatives intended to demonstrate useful results and build experience.
- **Capability builders:** work that develops reusable operating, technical, or human capability.
- **Transformation bets:** uncertain initiatives with potential to change a business or mission substantially.

The original three-to-six, six-to-eighteen, and eighteen-plus-month horizons are examples; estimate the real horizon and risk independently. A short project can be high risk. A “capability builder” in this lens is not identical to value type 5. There is no universal 50/30/20 allocation: specify whether a mix is measured by spend, people, or initiative count and why it fits the strategy.

At review, ask:

1. Does the mix support current obligations, near-term outcomes, and worthwhile future options?
2. Are shared foundations, operating support, and critical experts funded and available?
3. Are costs, schedule, quality, participation, adoption, or controls signaling a need to change scope?
4. Which addition, reduction, continuation, or exit would improve the combined portfolio under its constraints?
5. Has every reviewed initiative received a clear 3E decision, commitment, owner, and next review point?

Sequence by dependencies, learning value, readiness, consequences, reversibility, and capacity. Organizational scope alone is not a readiness ladder: a customer-facing draft and an internal autonomous payment action can have very different consequences. Estimate error costs before deployment where possible and use bounded experiments for unresolved questions. Neither the pace of organizational learning nor the best deployment surface is universally predictable.

## Deliver a review people can act on

Lead with the funding and sequencing decisions, then show their evidence and trade-offs. Keep the dashboard concise and link detailed cases where needed.

```text
Portfolio purpose, period, and resource constraints:
Snapshot: initiative | value type(s) | stage | horizon | evidence/rating |
          Buy/Hold/Sell | 3E | next commitment | owner
Shared dependencies, bottlenecks, operating obligations, and capacity:
Gate review: criteria met/unmet/unknown | controls | decision | action/date
Economic case and value-specific measures, with uncertainty:
Rebalancing: what changes, what it displaces, and why:
3E log: hypothesis | decision | rationale | budget/time bound | pivot check
Portfolio measures, trigger conditions, and next review date:
```

Check that decision labels agree, assumptions and denominators are clear, no score overrides a required control, shared value is not counted twice, and exits include real transitions. Explain the trade-off between governance effort and the cost of weak decisions. For a small decision, a short record may be enough; a substantial commitment warrants deeper evidence.

Use a pipeline, dependency map, or balance chart if it clarifies a decision. Label scenarios and uncertain estimates. Connect strategy to `rtp-strategy-canvas`, defensibility to `rtp-moat-finder`, sourcing to `rtp-build-or-buy`, and operating adoption to `rtp-adoption-launch` through focused handoffs.

Historical ROI studies and the Lloyds control-tower case are retained in the [reference](references/evidence-and-calculations.md). Use them to frame questions, not to assign an initiative a universal failure probability or claim governance alone causes success. Consult relevant Novel Insights entries with their later qualifications when updating a portfolio thesis.
