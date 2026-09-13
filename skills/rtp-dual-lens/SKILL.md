---
name: dual-lens
version: v1.0.1_latest
description: 'Explain one AI product concept accurately to business and technical readers, then check that both descriptions lead to the same decision. Use for shared PRDs, strategy documents, roadmap commitments, and presentations where audiences may interpret the same words differently. Connect outcomes to measurable constraints, expose unresolved assumptions, and assign failure ownership. Use a brief check when the meaning is already shared. Pairs with problem-ai-fit, first-principles, stakeholder-communications, trust-under-fog, and stress-test.'
imports: []
---

# Make the business and technical meaning agree

Write the concept in two forms: one that helps a business reader decide what is worth doing, and one that lets an engineer assess how it could work. Then explain the connection between them. **The deliverable is shared meaning: both descriptions must preserve the same scope, promises, constraints, and uncertainty.**

Use this skill before a consequential cross-functional commitment, or when a specification leads different readers to picture different products. Name the concept, the decision, and the audiences first. Use existing context; ask only for missing information that could change the result. A brief check is enough for a small clarification. A second definition adds little when the decision has no meaningful cross-domain implication.

Do not hide a feasibility gap with reassuring language. If feasibility or the value of AI is unresolved, mark the claim as a hypothesis and use `problem-ai-fit` or `first-principles` to investigate it. Alignment can reveal a need to revisit that decision; it does not prove that the feature should be built.

## Write both definitions, then test their connection

1. **Business definition.** Explain the customer or business outcome, who benefits, the main cost or risk, and the decision required. Use ordinary language without removing a constraint that affects the decision.
2. **Technical definition.** Describe the relevant system behavior, architecture, latency, cost per unit, failure modes, and verification. Include only details needed to assess this concept, and label untested assumptions.
3. **Bridge.** Explain how the technical behavior produces the intended outcome and where that connection could fail. Check scope, units, populations, time periods, and success criteria across both definitions.
4. **Translation layer.** Map each consequential business requirement to a testable technical constraint, and each consequential technical choice to its business implication. Distinguish a possible implementation from a necessary one.
5. **Audience validation.** When representatives are available within the authorized task, ask a business reader what decision follows and an engineer what they would build and test. Compare their interpretations. Otherwise, record that the brief has had a desk review and still needs audience validation; do not claim that stakeholders approved it.

A useful mapping is: "Knowledge must be updated daily" → "The source ingestion, index refresh, and retrieval path must meet the agreed freshness target." Choosing retrieval-augmented generation can support this, but does not create a daily refresh process by itself.

Another is: "A useful response within two seconds" → "Define what counts as useful, measure that point in the interaction, and budget retrieval, model, and interface time." Streaming is one option for showing partial output; it does not guarantee a complete answer within that budget.

## Why the connection can fail

A business leader and a technical lead can read the same sentence and infer different scope. The **curse of knowledge** is one possible contributor: familiarity makes it harder to notice what another reader lacks. Genuine disagreement, ambiguous incentives, and missing evidence can also cause the gap. Diagnose which applies before polishing the wording.

AI concepts often need particular care because internal operations are hard to picture, behavior varies across cases, and usage-dependent costs need explicit units. For example, "95% accuracy" leaves unanswered which task, population, test set, failure severity, and operating conditions it describes. A clear explanation retains the distinctions that affect the decision.

**Translation loss** is the decision-relevant meaning lost while changing vocabulary. Both directions matter: a business definition can hide a technical limitation, and a technical definition can omit why the limitation matters to users.

## Choose the framework that addresses the gap

### Model empathy: describe capability in the actual task

Treat the following as questions to investigate with the selected system and representative inputs, not a permanent ranking of what all models find easy or hard.

| Task | Conditions that may make it more tractable | Conditions needing particular evaluation | Product implication |
|---|---|---|---|
| Classification | Clear categories and representative examples | Ambiguous boundaries, rare classes, overlapping labels | Define the taxonomy and examine disagreements and errors by class |
| Generation | Clear output requirements and grounded source material | Factual precision, novelty, conflicting evidence | Check content separately from format; valid JSON can still be wrong |
| Reasoning | Bounded steps with checkable intermediate results | Long dependencies, temporal constraints, uncertain premises | Test the completed task and consequential intermediate steps |
| Retrieval | Relevant, accessible, well-indexed material | Negation, ordering, exact counts, permissions, missing evidence | Use structured filters or queries where appropriate and test retrieval coverage |
| Tool use | Clear interfaces and bounded actions | Multi-tool coordination, partial failures, recovery | Provide a harness with validation, permissions, retry limits, and recovery paths |

For contract work, extracting clause text, classifying risk, and comparing conflicting clauses are different tasks. Test each instead of calling the entire job "easy classification." Estimate review workload from observed errors and risk; a 15% review allowance is an illustrative planning assumption, not a model capability fact.

### Translation patterns: turn vague phrases into questions and measures

All numbers in the following examples are hypothetical. They illustrate how to specify a problem, not targets to reuse automatically.

| Business phrase | A more precise statement to investigate | Next move |
|---|---|---|
| "The AI is slow" | P95 time to a complete answer exceeds an assumed three-second requirement | Measure retrieval, queueing, model, network, and rendering time; do not assume context length is the cause |
| "Users don't trust it" | Acceptance is 34% against a 60% target, with frequent overrides | Investigate quality, usefulness, explanation, incentives, and whether overrides are appropriate |
| "Make it smarter" | Reduce a defined unsupported-answer rate in one category from 8% to 3%, while protecting other criteria | Name the failure, evaluation population, measure, and trade-offs |
| "It costs too much" | An assumed $0.04 per query exceeds a $0.02 unit-cost ceiling at the expected volume | Inspect token use, retrieval, retries, review, prices, and volume assumptions |
| "We need more AI features" | A user outcome is blocked by a specific capability gap | Compare AI with rules, search, workflow changes, or another suitable approach |

### Audience patterns: change the lead, preserve the facts

| Audience | Lead with | Example of an appropriate emphasis |
|---|---|---|
| Board or senior leadership | Business impact, material risk, decision | An assumed 5% relative churn reduction could be worth $2 million annually; state the baseline and calculation. An assumed 5% review rate needs a workload model before claiming one additional employee is enough. |
| Engineering leads | Behavior, architecture options, constraints, verification | Explain why retrieval or fine-tuning fits, what freshness is required, and how precision, recall, and P95 latency will be tested on the specified document set. A three-week training cycle is an assumption to verify. |
| Data scientists | Evaluation method, data, segment performance | "Macro-F1 is 0.94, while minority-class recall is 68%" identifies a gap hidden by an aggregate. Do not call F1 accuracy. |
| Designers | User decisions, uncertainty, failure and recovery | Explain when the system should clarify, show evidence, or offer refinement. A 70% confidence threshold is usable only if the score is meaningful and the policy has been evaluated. |
| Customer success | Observable behavior, limits, escalation | State supported contract types and how uncertain or unsupported cases reach review. An 80% threshold or 24-hour turnaround must be an agreed, resourced policy. |

## Four questions that expose a weak bridge

1. **Would both readers take compatible next steps?** If one approves a feature the other considers infeasible, identify whether they differ on meaning, evidence, scope, or the decision itself.
2. **Does the business definition hide a technical risk?** "Real-time personalization" needs a measured latency requirement and a freshness trade-off. "Hallucination-free" needs a bounded claim and evidence; it cannot be established by adding a verification component or choosing reassuring words.
3. **Does the technical definition hide a business constraint?** "RAG pipeline" may exist to meet knowledge freshness. "Three-second latency" may come from measured abandonment—or may only be an assumption. Say which.
4. **Is failure ownership actionable?** Name the accountable owner, operational responder, escalation path, and relevant trigger. Assign responsibility by the actual failure and operating agreement. A 5% hallucination rate does not determine whether product or engineering owns an incident.

For a production commitment, unresolved monitoring or rollback responsibility belongs in the finding. Do not invent a named person, on-call service, or threshold. Carry the agreed ownership into `stress-test` and `production-observability`.

## Worked example: contract-review assistance

This is a constructed planning case, not legal guidance or verified performance. Qualified reviewers retain responsibility for legal judgments. The purpose is to check that the two descriptions make compatible claims.

**Business definition:** "Help lawyers find potentially high-risk clauses before their review. Test a goal of reducing review time by 60%, with a possible $2 million annual benefit under the stated workload assumptions. Missing an important clause creates risk; unnecessary flags consume review time. For this hypothetical pilot, the proposed target is to flag at least 95% of known high-risk issues, with no more than 10% of flags being false alarms. These proposed targets require domain review and do not themselves establish acceptable risk."

**Technical definition:** "One candidate pipeline extracts PDF text, segments clauses, retrieves relevant policy or examples, and classifies or ranks potential issues with supporting evidence. Evaluate the complete pipeline, including extraction and retrieval failures. The proposed targets translate to high-risk recall of at least 95% and precision of at least 90%, using the same labeled population. Test an assumed P95 completion time of 30 seconds for 50-page documents and an assumed variable processing cost of $0.15 per document."

**Metric check:** Recall measures detected real issues divided by all real issues; precision measures real issues divided by all flags. Here, 10% false flags means the fraction of flags that are wrong, not the false-positive rate among all negative cases. A candidate with 95% precision and 80% recall would miss the proposed 95% recall target. [Google's classification metric definitions](https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall) support these distinctions.

**Bridge:** The expected time saving depends on the real review workflow, missed issues, unnecessary flags, and handling time. A precision change from 95% to 90% does not, by itself, prove that savings fall from $2 million to $1.2 million; that comparison needs a workload model. Thirty seconds may be acceptable for batch review if user evidence supports it. At $0.15 each, 200 documents cost $30; $30,000 requires 200,000 documents. Annualize only after stating annual volume, and include other operating costs before calling the result profitable.

**Translation layer:**

- "Find high-risk issues" → define issue categories, recall requirements, review ownership, and representative evaluation.
- "Reduce review time by 60%" → measure completed review time and quality, including verification and correction work.
- "Batch review is acceptable" → test the completion-time requirement; streaming may add little value here.
- "Use current policies and precedent" → evaluate retrieval coverage, permissions, freshness, and source reliability; do not assume one architecture is mandatory.

**Model empathy:** Ambiguous or conflicting clauses can require comparison and domain judgment. Route uncertain cases according to tested criteria and reviewer capacity; a label such as "medium" is meaningful only after the team defines it.

## A reusable brief

Use this shape when a standalone brief helps; an inline explanation can use the same logic more compactly.

```text
Dual-Lens Brief: [concept and decision]
Business definition: [outcome, scope, cost or risk, evidence status]
Technical definition: [behavior, constraints, verification, evidence status]
Bridge: [how the constraints support the outcome; unresolved gaps]
Translation layer: [consequential requirement ↔ constraint mappings]
Model empathy: [task, likely difficulty, evaluation, product implication]
Failure ownership: [accountable owner, responder, escalation, trigger]
Validation: [who reviewed what; what remains unconfirmed]
Next action: [decision or test, owner if known, decision point]
```

## Use the rest of the library where it adds value

- `problem-ai-fit`: investigate whether the use case needs AI and whether the required capability is supported.
- `first-principles`: identify the underlying operations when the two definitions keep drifting.
- `trust-under-fog`: communicate uncertainty when a business promise exceeds the evidence.
- `stress-test`: examine hidden technical, operational, and economic risks at the relevant scale.
- `stakeholder-communications`: tailor the delivery after the meaning is established.
- `production-observability`: turn agreed failure ownership and triggers into operational practice.

The shared `UNIVERSAL-SKILL-PROTOCOL.md` is at the AI-PM source root or plugin root. Apply its handoff guidance when this brief feeds another skill. Read [CONCEPT.md](CONCEPT.md) for the conceptual background and additional teaching cases.

## Check before using the brief

Both definitions should be accurate and actionable; each material promise should connect to a measurable constraint or an explicit uncertainty. Verify calculations, denominators, units, and time periods. State whether real audience validation occurred. Surface unresolved disagreement rather than reporting alignment from a polished document alone.

The trade-off is communication effort now versus possible rework later. Use evidence from the actual task to judge whether a full brief is worthwhile; do not assign high confidence automatically. Organizational norms may make cross-domain explanation difficult, so agree on what each audience needs without dropping consequential facts.

If a visual clarifies the relationship, show one concept with business and technical panels connected by a concrete mapping. Use an available diagram skill when useful. Conclude with the shared interpretation, its most consequential unresolved risk or trade-off, and the next validation or implementation decision.

## Terms used in this skill

- **RAG:** retrieval-augmented generation; supplying retrieved material to a model. Freshness depends on the source and retrieval process.
- **Context window:** the amount of input and generated context a model can consider within its supported limits. Actual content, model, caching, and implementation affect cost and speed.
- **Streaming:** delivering output incrementally. Distinguish time to first useful output from time to a complete answer. See [Claude's streaming documentation](https://platform.claude.com/docs/en/build-with-claude/streaming).
- **Inference:** running a model to produce an output; its cost depends on the service and usage.
- **P95 latency:** the latency at or below which 95% of measured requests fall; report the population and measurement point. It complements averages rather than replacing all other latency measures.

**Version 1.0.1, 13 SEP 2026.** Reorders the skill around the decision and bridge test, retains all three frameworks and the brief, and corrects metric, cost, capability, and ownership ambiguities.
