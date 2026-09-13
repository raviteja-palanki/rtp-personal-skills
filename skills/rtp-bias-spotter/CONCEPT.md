# Bias Spotter — Concept Guide

## The central distinction

Human judgment uses shortcuts. Many are useful; some produce systematic errors under particular conditions. AI product work adds uncertainty about models, data, and user behavior, so a team can confuse a model's weakness with a weakness in how it evaluates that model.

Bias-spotting examines the evidence and process behind a decision. A choice feeling obvious is a cue to check its basis, not proof that it is wrong. Introspection alone can miss a bias, but a review must also allow the conclusion that no material bias is supported. Otherwise the audit cannot be disproved and becomes an accusation machine.

**Business definition:** a practical check for reasoning and measurement errors that could distort an AI investment, design, or rollout decision.

**Technical definition:** a structured examination of assumptions, sampling, metrics, comparisons, and human-system interactions, leading to supported risk findings and a proportionate response.

## Three common traps

**The demo effect: optimism and anchoring.** A curated demonstration scores 95%. The team places “95% accuracy” in the PRD without the demo's task and population limits. The remedy is an evaluation on the intended workload, not an argument that demos are always misleading.

**The competitor cascade: bandwagon and action bias.** A competitor launches an AI feature and a team rushes to match it. Check whether the feature solves a relevant user problem, is succeeding, and changes the competitive situation. A fast response may be justified; its basis should be explicit.

**Token blindness: present assumptions carried into scale.** In an illustrative model, 100,000 daily active users making 10 requests each produce 1,000,000 daily requests. At $0.002 per request, that is $2,000 a day. If context and retries add a genuine 3× cost not already included in the unit estimate, the total becomes $6,000. This is multiplicative arithmetic across assumptions, not evidence that cost always grows nonlinearly with traffic. Keep units clear and avoid counting overhead twice.

## Illustrative examples

**The chatbot that appeared successful.** Usage rises, but investigation finds repeat questions after poor answers. The activity metric did not establish successful completion. Check outcomes and rework before deciding whether higher usage is good or bad.

**The enterprise deal that shaped the roadmap.** A large customer requests a feature. Its value may justify priority, but the team should compare the broader market fit, opportunity cost, and contractual commitments. Customer size alone does not settle the decision.

**The model upgrade with mixed results.** A team spends two months moving to a newer model. Complex-query quality improves, simple-query latency worsens, and token cost triples in this hypothetical example. Testing only expected winners hid the trade-off. Compare the intended workload by segment before choosing a model or routing policy. The earlier GPT-3.5-to-GPT-4 framing was illustrative, not a current recommendation or a verified cost claim.

## Make the check usable in a team

Agree that consequential proposals can be questioned without attacking their authors. Review early enough to change the decision cheaply, and make room for relevant dissent. A signature or invitation to speak does not establish that someone has time, authority, or a safe route to act on a concern.

Notice recurring patterns across decisions, but do not turn them into permanent labels for people or teams. Pair a suspected pattern with an observable mechanism and a useful intervention. Missing feedback, rewards for visible activity, and a lack of review capacity may require organizational changes rather than an appeal to “be objective.”

“The senior person decided,” “the data speaks for itself,” and “there is no time to check” are reasons to inspect the process, not automatic findings of bias. Equally, a low-stakes choice may not justify a full audit. Scale the check to consequences and the quality of feedback.

## Intellectual lineage and further reading

- **Daniel Kahneman, *Thinking, Fast and Slow*:** accessible models of intuitive and deliberate thinking. Do not infer which mental process caused a specific decision from its confidence alone.
- **Amos Tversky and Daniel Kahneman:** prospect theory and judgment under uncertainty. Loss aversion is one possible explanation for choices involving losses, not a diagnosis of every decision to continue.
- **Charlie Munger, *Poor Charlie's Almanack*:** a practitioner synthesis of recurring judgment errors.
- **Gary Klein, “Performing a Project Premortem”:** imagining failure to surface prospective risks.
- **Philip Tetlock and Dan Gardner, *Superforecasting*:** calibration, updating, and probabilistic forecasting.

The [main skill](SKILL.md) provides the audit, three-stage diagnosis, output format, and handoffs. [Research notes](references/research-notes.md) retain the growth, label-test, and ideation examples with their evidence limits.
