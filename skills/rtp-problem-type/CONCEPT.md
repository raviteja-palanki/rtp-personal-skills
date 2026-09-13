# Problem type: concept guide

Choose the work that matches the cause. Technical problems can be addressed through expertise and implementation. Adaptive challenges require learning and changes in behavior, values, incentives, roles, or relationships. An initiative may contain both, and the useful output is a plan for how those activities fit together.

The framework is associated with Ronald Heifetz's adaptive-leadership work. It does not establish that most AI failures are adaptive, that a technical fix can never recur, or that an organizational problem cannot have an explicit remedy.

## Two ways to explain the method

**For a business reader:** determine whether progress needs a better implementation, a change in how people work, or both. Then assign ownership and sequence the work.

**For an implementation team:** assess recurrence, cycling through solutions, clarity of the barrier, the effect of authority, and agreement on the remedy. Record technical, adaptive, mixed, or unclear evidence for each. The assessment is a heuristic supported by investigation, not a statistical classifier.

## What leadership contributes

For technical work, leaders establish the goal, provide expertise and resources, and verify the result. For adaptive work, they also create conditions for affected people to surface concerns, test changes, and take responsibility. They may need to model the behavior rather than simply authorize it.

Urgency, resistance, and uncertainty can occur in either type. An adaptive problem can have an unclear definition as well as an unknown remedy. A difficult implementation can remain technical even when experts need time to find the fault.

## Plan the mixed case

For disputed model recommendations, technical work may address data, objective functions, error measures, and constraints. Adaptive work may establish shared understanding of the intended outcome and its trade-offs. Appropriate legal and domain review remains a separate requirement where relevant.

Agree on consequential criteria before treating a technical design as settled. Use technical experiments to make the discussion concrete when they can be run safely. Coordinate parallel activities without pretending that a blocked dependency can be skipped.

## Conceptual influences

The original guide identifies these reading connections:

- Ronald Heifetz, *Leadership Without Easy Answers*: technical and adaptive challenges.
- Donald Schon, *The Reflective Practitioner*: reflection while acting under uncertainty.
- Peter Senge, *The Fifth Discipline*: organizational learning.
- Brene Brown, *Dare to Lead*: openness about uncertainty and difficult conversations.
- Amy Edmondson, *The Fearless Organization*: conditions in which people can raise concerns and learn.

These are conceptual influences. Inspect the appropriate source before using a precise quotation or empirical claim. Psychological safety can support adaptive work, but naming it does not establish that the organization has created it.

## Illustrative cases from the earlier guide

The source guide did not identify company records for these cases. Treat their numbers as constructed assumptions, not verified outcomes.

### Merchant recommendations and incentives

Assume a recommendation system reports 92% accuracy and a 15% click-through improvement in a test, with 8% adoption. A second version reports 95% accuracy, an 18% click-through improvement, and 10% adoption. These are separate measures; their movement alone does not prove that the system works well for merchants.

One possible explanation is that merchants believe recommendations reduce high-margin sales while the platform rewards a different outcome. Investigate that concern and the actual quality, exposure, and workflow. A response may combine revised incentives, transparent measurement of category sales, an opt-in pilot, and technical corrections.

The case illustrates why a model metric is insufficient to diagnose an adoption gap.

### A repeatedly failing data pipeline

Assume a pipeline initially works, then needs manual repair every other day during a later period. The architecture may need resilience. The contributing teams may also lack shared data definitions, reporting incentives, or ownership of quality.

Check logs and failure mechanisms alongside the organizational conditions. Establish the relevant standards and responsibilities while making known reliability repairs. Repeated failure is a reason to widen the diagnosis; it is not proof that infrastructure work is unnecessary.

### A hiring workflow with harmful screening behavior

Assume a hiring system reduces time-to-hire by 40% and reaches 100% mandated use, while a review identifies systematic disadvantage associated with applicants' schools. The percentages describe a hypothetical scenario, not a documented legal finding or a safe operating target.

The team needs to investigate the model and workflow, address immediate harmful behavior, and involve appropriate legal, compliance, and domain expertise. It may also need to change who defines success, who can challenge a result, and how decisions are reviewed. Mandated use does not establish belief in the system, and neither use nor skepticism alone explains whether reviewers scrutinized it.

The case illustrates the need for both technical examination and accountable organizational decisions. A discussion about fairness does not by itself establish that a hiring system meets applicable requirements.

## When to use the diagnosis

Use it when previous fixes have not produced the intended result, capability measures and completed-work measures diverge, stakeholder interpretations conflict, or an initiative repeatedly stalls.

Use a lighter check when the cause is already well understood. Contain an urgent failure first when needed. Neither resistance nor a mandate-induced change in usage should be treated as a conclusive diagnostic signal without more evidence.

The sequencing question is practical: which work provides the conditions another activity needs? Sometimes a shared decision must precede a build. Sometimes a prototype helps people assess what they would trust. Sometimes known repairs and organizational learning can proceed together. State the dependency and test whether the combined work improves the outcome.
