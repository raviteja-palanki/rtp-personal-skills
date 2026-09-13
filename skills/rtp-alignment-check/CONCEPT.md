# Alignment Check — Concept Guide

## What this skill helps you see

An AI initiative can have a capable model and still struggle because its purpose, incentives, ownership, workflow, or operating practice do not fit together. It can also have strong organizational support and a technical limitation that genuinely prevents success. Alignment Check examines both possibilities.

The five-link lens connects:

1. **Purpose:** the problem and intended outcome.
2. **Strategy:** the approach to creating and sustaining value.
3. **Capability:** skills, resources, authority, and capacity to execute.
4. **Architecture:** the design and dependencies that support the task.
5. **Systems:** the operating practices that keep the service useful.

These categories organize the diagnosis. They are not an empirically validated set of five irreducible conditions, and a weakness does not always mean total failure. Find the gap that matters for the actual commitment.

**Business definition:** diagnose what must change for an AI initiative to deliver its intended outcome, so investment addresses the real constraint.

**Technical definition:** assess stakeholder expectations, strategic choices, capability, design, and operations, tracing how an evidenced gap affects execution and identifying a proportionate repair.

## Avoid the convenient diagnosis

Technology is often visible and tractable: a team can buy a model, add data, or improve latency. Organizational problems can be harder to discuss. That can encourage a premature technical fix. The reverse is possible too: “culture” can become an explanation that avoids investigating real technical weaknesses.

The earlier claim that “93% of AI failures are organizational” was unsupported as stated. A related primary survey asks leaders about their greatest adoption obstacle; it does not measure the causes of failed projects. The [research notes](references/research-and-limits.md) explain the distinction and preserve the other original statistical leads without treating them as verified facts.

## Illustrative cases

**An underwriting investment with blocked adoption.** A firm spends $2M and reports 94% model accuracy, but underwriters distrust the workflow, incentives conflict, and a required review arrives late. These facts suggest purpose, strategy, and design questions. They do not establish that the model is “fine”: the accuracy measure, error costs, fairness, and task coverage still need examination. A better model alone may not resolve the operating barriers.

**A pilot that does not transfer.** A readmission-prediction pilot reports 87% accuracy and positive clinician feedback. Broader use is 12% at month three. A supportive pilot leader and differing departmental incentives are possible explanations. Check workflow, suitability, data, resources, and alternatives before attributing the result solely to resistance or autonomy concerns.

**An inventory agent people override.** A retail team repeatedly bypasses recommendations. Missing operational participation may matter, but overrides can also reflect legitimate local constraints or poor recommendations. Investigate the reasons and outcomes, then decide whether to improve the model, change the workflow, or involve operators differently.

**A recommendation feature loses its lift.** Click-through rate is 30% above a defined baseline in month one, back to baseline in month six, and 5% below by month twelve in this hypothetical example. The figures alone do not prove drift or missing retraining caused the decline. Check seasonality, user mix, experiment design, product changes, and the relevance of CTR to the intended outcome. Use valid findings to choose the fix.

These are teaching scenarios, not verified company cases or domain-specific deployment recommendations.

## Use agreement as an input to action

Independent, concrete descriptions can reveal differences hidden by broad assent. Compare the problem, future workflow, trade-offs, and responsibilities before a consequential group decision. Then resolve meaningful differences under clear decision rights and record the resulting commitment.

Do not require identical views or unanimous agreement. An authorized decision may proceed with a recorded objection and explicit conditions for review. Conversely, a signature without resources, understanding, or ability to act may not establish readiness.

Use the check before a major commitment, during pilot-to-production planning, after a failure, or when joining an unfamiliar initiative. The original $1M investment threshold and one-week diagnosis budget were examples, not requirements. Scale the work to consequence and uncertainty; early exploration needs enough alignment for a safe, useful experiment rather than a complete transformation plan.

## Intellectual lineage

- **Ronald Heifetz, *Leadership Without Easy Answers*:** technical problems and adaptive challenges.
- **Peter Senge, *The Fifth Discipline*:** interactions and feedback across an organization.
- **Jim Collins, *Good to Great*:** practitioner ideas about focus and organizational capability.
- **Clayton Christensen, *The Innovator's Dilemma*:** incentives and established business processes that can shape innovation choices.
- **Donella Meadows, *Thinking in Systems*:** examining relationships, feedback, and consequences beyond a single intervention.

These works inform the lens; they do not validate this exact five-link diagnostic. The earlier “AI Engineering, various authors” reference was underspecified; verify the intended work before using it to support a particular case or claim.

The [main skill](SKILL.md) contains the workflow and report. The [15-question guide](references/diagnostic-questions.md) provides warning signs, stronger evidence, and concrete spectrum anchors.
