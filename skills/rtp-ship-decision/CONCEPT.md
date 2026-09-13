# Ship Decision — Concept Guide

## The central distinction

A system can run successfully and still produce a wrong, harmful, or economically unsustainable result. This is true of conventional software too; AI adds task-dependent uncertainty and failure modes that ordinary execution checks may miss.

The release question is therefore broader than “does it run?” It is whether the proposed use has enough evidence, controls, operational support, and value to justify exposure. Review these throughout development instead of adding safety and business concerns only after engineering is finished.

**Business view:** an accountable choice among launching, limiting scope, holding, and stopping, with consequences for customers, employees, resources, and future options.

**Technical and operational view:** seven readiness areas—safety/authority, reliability, economics, observability, user understanding, graceful degradation, and release accountability—supported by appropriate tests and monitored exposure.

## Four traps to recognize

**Staging becomes the whole world.** A controlled environment makes comparison easier but can omit real variation, misuse, permissions, dependency behavior, and user workflows. Production is not inherently “biased toward failure”; it can differ from the test distribution. Make the important differences visible and include realistic cases.

**Familiarity becomes assurance.** A team that knows the intended use may unconsciously compensate for gaps. Examine what unfamiliar users actually understand and do. With a true 99% success rate over one million comparable attempts, the expected failure count is 10,000. A million users making a million attempts each is a different volume. Failure count alone does not describe severity, distinct people harmed, or legal outcome.

**No complaints becomes no problem.** Users can abandon silently or accept incorrect output. Combine operational events, user feedback, and independent quality checks. Monitoring improves detection when coverage and response work; a dashboard cannot guarantee every issue will be caught.

**Disclosure becomes a transfer of responsibility.** A label helps users understand the feature but does not establish permission for harmful behavior or settle liability. Applicable duties depend on facts, use, contracts, and jurisdiction. Design useful recourse and seek the required specialist review for the actual case.

## Four illustrative scenarios

These are fictional teaching cases. They are not claims about identified companies or lawsuits, and their controls reduce risk rather than guarantee prevention.

### 1. An unsupported legal citation

A legal research assistant produces an apparently valid citation that does not exist. A reviewer may catch it before filing, or an unchecked citation may enter a brief and create serious professional and legal consequences. The original guide's unnamed $2 million settlement and product closure were not substantiated and should not be treated as historical evidence.

Before exposure, test citation existence and whether the cited material supports the claim, define the intended professional review, and make unresolved evidence clear. Test refusal and escalation when the system lacks a source. Monitor representative outcomes and offer a correction path. Recovery can be possible but becomes harder after downstream reliance; it is not uniformly “impossible.”

**Decision:** hold unsupported source-dependent answers or narrow the feature until validation and review are adequate. An AI label alone does not resolve the gap.

### 2. A provider update hides a subgroup regression

A provider version improves aggregate performance while a support assistant gets worse at certain complaint types. If all quality reporting is aggregated, the affected workflow can remain hidden.

Track effective versions and relevant task segments, test the changed configuration, inspect failures, and define a compatible recovery path. A fixed 5% category threshold is only an example; choose a meaningful threshold with sample context. Model drift is one possible cause alongside retrieval, routing, tools, and traffic changes.

**Decision:** limit the affected scope, investigate, and restore an acceptable compatible configuration or apply another containment path. Do not assume a provider lets you restore every past model.

### 3. Longer work changes the cost model

Assume one million outputs per month at $0.02 each: modeled cost is $20,000. If per-output cost triples because outputs become longer, the corresponding cost is $60,000 at unchanged volume, not $150,000. Reaching $150,000 would require a 7.5-fold overall cost factor or additional explained volume and cost categories.

Stress both volume and task mix. Track token usage, retries, tools, human work, quality, and verified outcomes. Use a response that fits the user contract and consequence—better routing, usage limits, controlled queues, budget expansion, or a scoped pause.

**Decision:** expand only within a defensible capacity and funding plan. A good unit margin does not eliminate aggregate cash or dependency limits.

### 4. A thirty-minute provider outage

A critical workflow relies on one provider and lacks a useful fallback. A thirty-minute outage disrupts customers. In a 30-day time-based window, 99.9% availability permits 43.2 minutes of unavailability; this incident alone does not necessarily breach that target. At 99.99%, the allowance is 4.32 minutes. Other downtime and the contract's measurement rules matter.

Define the actual workflow tolerance and service indicator, then test dependency failure, queueing, communications, and the capacity of alternatives. Staging evidence cannot guarantee future uptime.

**Decision:** choose a release scope and fallback consistent with the promised service, and retain incident response for failures that still occur.

## What makes the gate useful

A gate is useful when evidence can change the decision and the responsible people can enforce its conditions. That can mean approval, a design correction, reduced scope, delay, or stopping. Count outcomes in context; a zero-stop history is not proof of absent authority.

The same discipline applies to postponement. Compare the cost of a narrower launch, additional testing, delay, and the current process. Recognition for well-supported stopping decisions can reduce social pressure, but a cancellation quota would distort the goal.

Use the [main skill](SKILL.md), [day-one template](references/day-one-review.md), and [evidence notes](references/ship-evidence.md) to make a concrete, reviewable decision. A completed review is evidence for a scoped choice, not a promise of error-free operation.
