# AI PRD evidence and revision notes

Reviewed 13 September 2026. Separate source guidance from local product requirements and illustrative examples.

## Practitioner source

The complete extracted text of the user-provided **Aakash Gupta, “AI PRDs: Everything You Need to Know,” 16 August 2025**, developed with Miqdad Jaffer, was read. Embedded screenshots and externally linked tear-down documents were not fully transcribed or independently reviewed.

The article supports problem/strategy/scope decisions, explicit outcome thresholds, behavior examples, rollout choices, ownership, lifecycle stages, and iteration between a prototype and its spec. It suggests 15–25 examples at Solution Review and advises against using an LLM for the first draft. Those are practitioner recommendations, not universal empirical requirements. This revision preserves accountable authorship while allowing AI drafting with adequate context and review. It does not infer that the article proves every prototype-first team fails or that a particular template caused product adoption.

The section 0–13 arrangement, Athena examples, six story coverage areas, and User Story Health measure are this library's synthesis. The old template's “SKILL.md v416” source label was not a valid current version.

## Primary checks

- Google's official [Rules of Machine Learning](https://developers.google.com/machine-learning/guides/rules-of-ml): relevant simple-pipeline, iteration, measurement, and feedback-loop passages checked. Rule 16 was previously misquoted.
- [AI-employee framing study, authors' manuscript](https://emmawiles.github.io/storage/ai_employee.pdf): 1,261 managers; reported nine-percentage-point accountability shift and 18% fewer errors detected concern the subgroup with institutionalized AI agents on organizational charts. These are not the average effect for every manager, and they do not validate an error-catching quota or eliminate the value of formal ownership.
- The probability, unit-cost, and percentage-direction corrections are explicit calculations. Hypothetical prices and thresholds are labeled; none is a current vendor quote or deployment recommendation.

## Novel Insights cross-check

Revisited the August scarcity/prototype discussion and the invoice approval/exception-rate passages. The useful pattern is to measure what a fast, completed artifact or a low exception rate can conceal: unresolved problem value, incomplete evaluation, and accepted-but-wrong outcomes.

The ledger's stronger claim that speed with a rising approval rate proves a dissolving gate is not supported by that rate alone. Quality, case mix, and detection coverage can change. Pair behavioral signals with independent outcome review. A visible build can crowd out problem definition, but neither a prototype nor a written PRD is inherently the correct first artifact for every task.

## Not retained as general rules

No fixed 8/16 fit gate, 70%-complete eval permission, thirty-day significance promise, universal 0.85/0.70 score bands, ownerless production process, mandatory error-catching incentive, or “one metric always lies” claim. No assertion that every fallback is faster/safer, all high-confidence errors disappear with calibration, or every production correction requires three immediate artifact edits. The revised skill names the applicable decision, evidence, and exception instead.
