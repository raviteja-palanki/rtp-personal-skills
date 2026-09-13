# Uncertainty Research: the concept

Research findings are useful when the study captures the variation that matters to the decision. For an AI product, that can include output quality, task difficulty, context, system changes, expectations, and experience over time. Standard research methods remain useful; the design and the claim must fit these conditions.

## Two useful definitions

**For product decisions:** choose research that shows whether the system helps the intended people with their work, under realistic conditions and acceptable consequences.

**For research design:** define the construct, population, conditions, assignment and analysis units, exposure, measures, and limits of inference. Account for repeated observations and meaningful output variation. Use qualitative accounts, behavior, and task outcomes for the different questions each can answer.

## Three distinctions to keep clear

**A good session is evidence about that session.** It can reveal important usability or task-performance facts. Broader quality and sustained-use claims need coverage of the relevant tasks, outputs, people, and time. Random sampling is only one source of variation; retrieval, permissions, context, and versions can also change the experience.

**Satisfaction, trust, reliance, and correctness are different.** A person may like a response, expect future reliability, accept an answer without checking, or complete a task correctly. Measure the construct the decision requires. Trust can be studied at a point in time; a claim about how it develops requires evidence across relevant exposure. More trust or less verification is not automatically better calibration.

**A prototype establishes evidence about its tested conditions.** In Wizard-of-Oz research, record what the human supplied and how its speed, errors, and capabilities compare with the intended product. Neither perfect human performance nor an inevitable satisfaction penalty can be assumed.

## Illustrative cases

These are teaching scenarios retained from the earlier concept file. They are not verified field studies.

### Writing assistant: declining verification

Twenty people use a writing assistant for four weeks. Verification rates are 100%, 60%, 25%, and 20%; later checks concentrate on complex sections. This suggests a change in reliance worth investigating. To call it appropriate calibration, compare checking and acceptance with actual errors, task outcomes, difficulty, workload, and participant explanations. Fatigue or pressure can also reduce checking.

The sequence does not establish a universal four-week trust curve, a linear decline, or a two-to-three-week delay before value appears. A single session would miss later behavior, but could still establish useful interaction findings.

### Search: an overall result conceals different experiences

A 200-query evaluation reports 72% overall satisfaction and 94%, 67%, and 41% for simple, multi-step, and ambiguous tasks. Report the number and mix of queries in each group to interpret the overall result. Investigate whether the lower-scoring tasks are frequent or consequential for the intended users and why people were dissatisfied.

Satisfaction is not a failure rate. Even if non-satisfaction were used as a clearly labeled proxy, the ratio for the lowest group is 59% / 28% ≈ 2.11, not the earlier 2.3. Prioritize improvements using task importance, outcome evidence, coverage, and cost rather than that ratio alone.

### Email prototype: a difference needs an explanation

A human-assisted prototype takes two minutes per email and receives 95% satisfaction. A later AI version receives 45%, with output quality described as 78% against an anticipated 80%. The quality percentage needs a rubric and denominator before it is interpretable. The satisfaction gap alone does not establish that expectations caused it; compare participants, tasks, errors, speed, framing, and other changes.

Test the intended system and communicate its demonstrated capabilities and review needs honestly. A blanket discount for Wizard-of-Oz results or a generic “70–80% correct” promise cannot replace that evidence.

## Intellectual foundations

- Teresa Torres’s continuous discovery work connects research to product decisions and ongoing learning.
- Don Norman’s mental-model work helps distinguish what people expect from how a system behaves.
- [Lee and See, *Trust in Automation* (2004)](https://journals.sagepub.com/doi/10.1518/hfes.46.1.50_30392) connects trust and appropriate reliance in context; it does not prescribe one trust timeline.
- [Google’s People + AI Guidebook](https://pair.withgoogle.com/guidebook-v2/chapters) offers design guidance for human–AI interaction.

Use the [skill](SKILL.md) for the procedure and the [research reference](references/research-and-examples.md) for evidence boundaries and the numerical examples.
