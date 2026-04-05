# Stress Test — Concept Guide

## FIRST PRINCIPLES

Traditional software has binary failure modes — it works or it doesn't. The server responds or it times out. The function returns the right answer or it throws an error.

AI products fail differently. They degrade. The model gets slightly less accurate after a provider update, and nobody notices for three weeks. Latency creeps up as context windows grow, and the PM attributes declining engagement to "seasonal patterns." Costs increase gradually as usage grows, and finance doesn't flag it until the quarterly review.

The atomic insight: **AI products require stress testing not because they might fail catastrophically, but because they will fail gradually — and gradual failure is invisible until it's expensive.**

## DUAL DEFINITION

**Business definition:** Stress testing is the practice of verifying that an AI feature will remain economically viable, performant, and reliable at production scale — before committing the resources to launch it. It prevents the most common AI product failure: a feature that works beautifully in pilot and bankrupts you at scale.

**Technical definition:** A four-dimensional evaluation of system behavior under production conditions: fault tolerance at scale, unit economics at volume, tail-latency under load, and observability coverage for non-deterministic components.

## THE TRAP (Expanded)

**The Demo-to-Production Gap.** The most dangerous moment in AI product development is the successful demo. Stakeholders see it work and extrapolate linearly: "If it works for 10 users, it'll work for 10,000." But AI systems don't scale linearly. Context windows grow (slowing retrieval), token costs multiply as users ask more complex questions (not constant per request), the distribution of inputs at scale includes adversarial cases that never appeared in the pilot, and model provider behavior changes under load. The gap between "works" and "survives" is where most AI products die.

**Gradual Failure is Invisible.** This is THE critical insight. Traditional systems fail noisily — the server goes down, requests error out, something is clearly broken. AI systems fail quietly. A model provider pushes an update and accuracy drops 3% — nobody notices for three weeks. Context window grows by 20% and latency creeps from 600ms to 900ms — attributed to "seasonal variation." Token costs increase 40% and the feature becomes unprofitable — discovered in the quarterly review. Gradual failure is invisible until it's expensive. Stress testing exists to find gradual failure before production users do.

**The Average Lie.** "Average latency: 800ms." This number is useless for predicting user experience. If 5% of users experience 4-second latency, and those 5% are disproportionately power users with complex queries, your average is hiding your biggest pain point. P95 is not a vanity metric — it's the experience of your most engaged users.

**The Cost Blindness.** Token costs are abstract. "$0.003 per 1K tokens" doesn't trigger an alarm. "$45,000/month" does. But one is the other at scale. Teams that don't model cost at volume discover their AI feature is economically doomed only after they've built user dependency on it and committed the roadmap.

## INTELLECTUAL LINEAGE

- **Google SRE** — Error budgets, SLOs, and the philosophy that reliability is a feature. Applied to AI: model quality is a reliability metric.
- **Eugene Yan** — Production ML systems writing. On the gap between ML research metrics and production metrics.
- **Netflix Chaos Engineering** — The principle that you should test failure before it tests you. Applied to AI: simulate model degradation, not just model outage.
- **Nassim Taleb** — Antifragile. Systems that benefit from stress vs systems that break under it. AI products should be designed to improve from production stress (via feedback loops), not just survive it.

## REAL-WORLD EXAMPLES

**Example 1: The cost surprise.** A team launched an AI writing assistant. At pilot (500 users), token costs were $2,000/month. At GA (15,000 users), costs hit $89,000/month — not 30x (linear) but 44x, because average tokens per request increased as users learned to ask more complex questions. A stress test modeling user behavior evolution would have caught this.

**Example 2: The latency cliff.** An AI search feature performed at 600ms average in testing. In production, P95 was 3.2 seconds because the retrieval step was O(n) on document count, and the production corpus was 8x larger than the test corpus. The average was fine. The tail was catastrophic.

**Example 3: The silent degradation.** A model provider pushed a minor update. Average accuracy dropped from 91% to 87%. Without automated quality monitoring, the team discovered this four weeks later through a spike in customer complaints. A monitoring system that tracked accuracy on a reference test set daily would have caught it in 24 hours.

## FURTHER READING

- Google SRE Team, *Site Reliability Engineering* — Error budgets and SLO design
- Eugene Yan, "What I've Learned Working with AI Products" — Production ML realities
- Nassim Taleb, *Antifragile* — Designing systems that benefit from stress
- Will Larson, "Sizing and Costing AI Features" — Unit economics for AI products
