# Stress Test — Concept Guide

## Why a working demo is not enough

A demo answers whether a feature can work in the demonstrated setting. A production commitment asks whether it can meet defined expectations across the intended workload, including unusual inputs, congestion, dependency failures, abuse, and changing usage.

Both conventional software and AI systems can fail abruptly or degrade quietly. AI adds particular challenges when a response is fluent and technically successful but substantively wrong. Uptime alone will not reveal that failure, and an average can hide a consequential tail or subgroup.

Stress testing brings likely failure conditions into a controlled examination before the exposed commitment. It improves the evidence available for a decision; it cannot promise that every future failure will be found.

**Business definition:** assess whether a proposed AI release can meet its user, operating, cost, and reliability commitments, and identify the changes or limits needed before proceeding.

**Technical definition:** evaluate six areas—failure at scale, cost at volume, tail latency, monitoring, adversarial inputs, and applicable agent resilience—under specified conditions and criteria. Combine those tests with a pre-mortem for outcome failures the current metrics may miss.

## Four gaps worth examining

**Demo to production.** More users may change arrival rates, request mix, context length, and exposure to rare cases. Costs can scale approximately linearly under fixed per-request assumptions, but those assumptions may not hold. Test the mechanism rather than simply assert that AI never scales linearly.

**Successful response to useful response.** A provider update might reduce quality while requests still succeed. In an illustrative case, a 3-percentage-point accuracy decline, a latency change from 600ms to 900ms, or a 40% cost rise could escape an incomplete dashboard. These outcomes have different causes and require different measures.

**Average to distribution.** An 800ms average does not describe every user's experience. If a material group faces four-second waits, examine the tail and its workload. P95 is a percentile threshold, not automatically the experience of power users or the worst-case request. Keep the average where useful, alongside percentiles, timeouts, and segmentation.

**Unit price to complete operating cost.** At an illustrative $0.003 per 1K tokens, $45,000 in monthly inference requires 15 billion billed tokens at that blended rate. The price alone does not imply the volume. Real estimates need separate billing categories, context, retries, tools, evaluation, infrastructure, and relevant human work.

## Illustrative scenarios

These examples teach mechanisms; they are not verified company cases.

**A writing assistant's cost surprise.** Five hundred users cost $2,000/month in a pilot. Fifteen thousand users cost $89,000/month after a broader launch. Users increased 30x while cost increased **44.5x**. That could reflect more requests, longer contexts, different models, or overhead; it does not prove that longer requests caused the gap. A useful test measures those drivers and models plausible changes before committing.

**A search feature's latency cliff.** A test records 600ms average latency; production records 3.2-second P95 with an eight-times-larger corpus. Average and P95 are different measures, so that comparison alone does not establish a regression or its cause. An O(n) retrieval step is a candidate bottleneck only if the implementation and measurements support it. Compare consistent measures under controlled workload changes.

**A provider update and delayed quality detection.** Accuracy on a defined evaluation falls from 91% to 87%, a four-percentage-point decline. The team hears about problems four weeks later. A suitable daily reference check might detect the change earlier; it cannot guarantee detection within 24 hours without sufficient coverage, sample size, sensitivity, and functioning response. Production segments may reveal failures the reference set misses.

## People are part of the test

Set decision rights and stopping conditions before results arrive. Give testers and reviewers access, time, and a way to challenge an unsafe or unsupported conclusion. The person who finds a failure should not be penalized for contradicting the hoped-for outcome.

Personal exposure can reveal an incentive or conflict; it is not the measure of a reviewer's value. Independent evidence may be especially useful when the proposal owner faces strong pressure to proceed. Reward well-supported judgment, including correction, cancellation, or continuation as appropriate.

## Intellectual lineage and further reading

- **Google SRE:** service-level indicators and objectives, error budgets, and user-centered reliability. [Service Level Objectives](https://sre.google/sre-book/service-level-objectives/) provides a primary reference.
- **Chaos engineering practice, including Netflix:** controlled experiments on failure and recovery. The test itself needs a bounded blast radius and stop conditions.
- **Eugene Yan's production-ML writing:** connecting model measures with operating systems and user outcomes. Verify the exact article before citing a particular claim.
- **Nassim Nicholas Taleb, *Antifragile*:** distinguishes surviving stress from improving through it. A feedback loop must demonstrate improvement before a system is described as benefiting from stress.
- **Will Larson's engineering-management writing:** a practitioner reading lead for operating and costing systems. The earlier guide's “Sizing and Costing AI Features” title was not verified in this pass and should not be treated as a checked citation.

Use the [main skill](SKILL.md) for the process and report. [Calibration and examples](references/calibration-and-examples.md) retain the detailed worksheets, historical quantities, and source limits.
