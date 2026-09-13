# Problem–AI Fit — Concept Guide

Choose AI because it improves the relevant outcome enough to justify its cost and consequences. Compare it with a credible baseline: rules, search, ordinary software, a human workflow, an existing product, or doing nothing. Neither novelty nor simplicity is sufficient evidence on its own.

## Two definitions

**Business:** deciding whether an AI-enabled approach is a worthwhile use of resources for a defined customer problem, with a clear alternative and evidence of value.

**Technical:** assessing the task, suitable capabilities, data and evaluation requirements, failure controls, and operating costs before committing to an architecture or level of authority.

A lookup on clean structured data often suits ordinary code. Finding the right source from ambiguous language may benefit from learned retrieval. A transformation may be a fixed-format conversion or a difficult recognition task. Classification may use rules or ML, and generation may use a template or a model. The operation name helps decomposition; it does not decide the implementation.

## The trap

A team may adopt AI to satisfy a technology agenda, imitate a competitor, or justify a past platform purchase without establishing a useful outcome. This is a hypothesis about the decision process, not an assumption about every executive’s motives. Ask what evidence supports the choice and what would change it.

The opposite error is dismissing AI because a crude rule can produce an answer. Compare complete task outcomes and ongoing costs. An existing model may outperform costly rule maintenance; a well-designed rule may outperform an unnecessarily complex model. The assessment should reveal which is true in this scope.

## Illustrative cases

**Invoices:** fixed layouts may support template extraction and validation; variable layouts or poor scans may need recognition models and careful exception handling. The earlier $0.002 versus $0.15 per invoice and 97% accuracy figures were hypothetical, not verified results. A TRANSFORM label alone cannot establish that AI is unnecessary.

**Content moderation:** a classifier with escalation may be useful, but a review queue does not make all harms reversible. Check missed harmful content, unjustified removal, reviewer capacity, and appropriate authority. Four favorable checklist answers cannot settle those issues.

**Scheduling:** calendar access and constraint logic can handle many scheduling tasks. Natural-language requests, preferences, coordination, or exceptions may add other components. Separate understanding a request from checking availability and from authority to send an invitation. These are illustrative design comparisons, not documented startup outcomes.

## Intellectual connections

Google’s Rules of ML supports testing useful non-ML baselines and implementing measurement. Product judgment and opportunity-cost ideas associated with Shreyas Doshi motivate comparing this investment with the work it displaces. Aman Khan’s evaluation practice is relevant background; the earlier exact talk-title and broad “most failures” attribution were not verified here. A particular provider’s current feature list is not a durable proof of the boundaries of AI.

Use the [skill](SKILL.md) for the decision process, the [profile and examples](references/assessment-profile-and-examples.md) for optional detail, and the [research notes](references/research-boundaries.md) for source limits. The practical test is whether the proposed approach earns its role on the actual task under actual constraints.
