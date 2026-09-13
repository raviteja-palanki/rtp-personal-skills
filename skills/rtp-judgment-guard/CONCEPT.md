# Judgment Guard — Concept Guide

## The design question

AI can change both the output of work and the experiences through which people develop and exercise judgment. The useful question is which capabilities the workflow still needs, who must hold them, and how the design will maintain or build them.

**Business definition:** choose and support the human role in an AI workflow so it contributes to the intended outcome, preserves needed capability, and satisfies the actual responsibility and risk constraints.

**Technical definition:** diagnose the mechanism affecting judgment, choose and evaluate appropriate checkpoints, and compare the performance and consequences of the resulting human–AI process.

The main skill covers two cases: capability and judgment, and tested human–AI complementarity. It uses six checkpoint IDs: rotation/practice, calibration, independent view and override, repair after a miss, decision rationale, and disclosure safety. The sixth is considered first because honest records and an effective challenge route can be prerequisites for interpreting the others.

## What the evidence must distinguish

- **Atrophy:** a previously demonstrated, still-needed capability declines.
- **Non-formation:** the workflow fails to provide sufficient learning opportunities.
- **Misapplication:** existing skill does not transfer effectively to directing or reviewing AI.
- **Behavior and authority:** people may defer, avoid information, lack capacity, or be unable to get a concern acted on even when they have relevant skill.
- **Pre-emption:** an early answer shapes the frame before an independent view is exercised.

A falling override rate is compatible with several of these mechanisms, as well as with improved AI. An unchanged human score alongside a rising AI score does not establish atrophy. A fixed number of months cannot diagnose skill loss.

## Illustrative cases, with the inference kept separate

**A radiology outage.** In a hypothetical system, AI-only accuracy is 94%, assisted accuracy is 96%, and unaided performance during a forty-eight-hour outage two years later is 72%. A later supervised assessment records 89%. These numbers do not establish the original radiologists' unassisted baseline or isolate atrophy from workload, case mix, measurement, or outage conditions. The original two-week recovery story was not an observed clinical program. Assess competence and design appropriate training under qualified supervision; do not infer a recovery timetable from this example.

**Fraud investigation.** A hypothetical override rate falls from 15% to 3% to below 1% over twelve months, and 40% of the later overrides are judged incorrect. This warrants examining both missed errors and unnecessary overrides. It does not prove that the investigators' ability declined: compare task mix, AI performance, reviewer workload, incentives, and independently assessed outcomes. An outage also needs a defined contingency plan.

**Hiring review.** A team initially changes 50% of AI recommendations, later checks fewer candidate records, and discovers a problematic school-based pattern. Investigate whether the system, review criteria, access, or incentives allowed the issue to persist. An earlier claim that three months of human-only hiring restores calibration was illustrative and unsupported. Human-only decisions are not automatically fairer or more accurate; assess the actual process and requirements.

The separate “30 cases per day, 90% AI accuracy, two minutes of review” radiology narrative in the original guide was also hypothetical. It cannot establish universal neural atrophy or a month-twelve inability to read an image.

## What useful checkpoints do

Practice provides appropriate opportunities to learn. Calibration compares performance with a suitable standard. Independent assessment can expose anchoring. A meaningful override can change an outcome. Repair addresses the causes and consequences of a miss. Rationale records support review. Disclosure safety helps concerns reach a fair decision process.

None works merely because a form exists. Each needs a purpose, competent participation, capacity, evidence, and an action when the result warrants it. Cost the work explicitly; the original time and staffing arithmetic is corrected in the [calibration notes](references/calibration-and-evidence.md).

## Intellectual lineage

- **Kahneman and Klein, “Conditions for Intuitive Expertise” (2009):** conditions under which expertise and reliable intuition can develop; not a universal AI-atrophy timetable.
- **Etienne Wenger, *Communities of Practice*:** learning through participation and relationships.
- **Hubert and Stuart Dreyfus, *Mind over Machine*:** distinctions in skill acquisition; the familiar conscious/unconscious-competence ladder should not be treated as the Dreyfus model itself.
- **Malcolm Gladwell, *Outliers*:** a popular account of expertise. Ten thousand hours is not a universal necessary or sufficient dose of practice.
- **Barbara Fredrickson's broaden-and-build work:** a perspective on positive emotion and resources, not direct proof that automation causes neural atrophy.
- **Alicia Juarrero, *Context Changes Everything*:** a conceptual lens on context and constraints, rather than measured evidence for these checkpoints.

Use the [main skill](SKILL.md) to design the workflow. [Mechanisms and design notes](references/mechanisms-and-design.md) preserve the richer cases and distinctions; [calibration and evidence notes](references/calibration-and-evidence.md) retain research scope, quantities, and open questions.
