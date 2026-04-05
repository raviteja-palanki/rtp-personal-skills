# Fit Signal — Concept Guide

## FIRST PRINCIPLES

In deterministic products, product-market fit is measurable and stable. If you build a task management app and 65% of users return weekly, that's a real signal. If you build a note-taking app and NPS is 45, that's predictive of growth.

In AI products, deterministic metrics become unreliable because the product itself is non-deterministic. Same input, different outputs. User experience on Monday differs from Tuesday. One hallucination can destroy a week of trust, and one exceptional output can restore it.

The atomic insight: **In non-deterministic systems, metrics that assume stable product quality become measures of variance, not product-market fit.**

Here's the inversion:
- High NPS in a deterministic system = user loves the product = PMF likely
- High NPS in an AI system = user had good experiences recently = could mean PMF or could mean they got lucky this week = no inference

Similarly:
- 60% retention in a deterministic system = product is sticky = PMF
- 60% retention in an AI system = on average 60% of users came back = tells you nothing about whether they trust the system or are just testing it repeatedly hoping for consistent quality

The products that succeed in AI don't rely on traditional PMF metrics. They measure **trust accumulation**: Does the user's confidence in the AI increase over time? Can they depend on it? Would they switch if they could?

This is why classical PMF frameworks (Sean Ellis' "Would be very disappointed if couldn't use?" test, Rahul Vohra's AARRR metrics) fail for AI. These frameworks assume the product experience is deterministic and stable. They're measuring "is the user dependent on the product?" When the product delivers inconsistent output, dependency doesn't indicate fit — it indicates desperation.

## DUAL DEFINITION

**Business definition:** Product-market fit for AI products is the state where users can reliably depend on the AI output for a specific task, their confidence in that output increases over repeated use, and the switching cost to a competitor is high enough that they wouldn't leave even with a price increase or feature gap.

**Technical definition:** Measurable evidence that (1) user trust curve is inflecting upward and plateauing at high confidence (>0.60), (2) error correction rate is decaying as users learn the system's boundaries, (3) the system is capturing and absorbing user corrections to improve future outputs, and (4) estimated switching costs exceed the cost to acquire replacement customers, such that LTV:CAC ratio is sustainable.

## THE TRAP (Expanded)

### Trap 1: The Engagement Mirage

You launch an AI feature. Users engage heavily. You measure:
- DAU: 500 → 1,200 (150% growth)
- Session length: 2min → 8min (4x increase)
- Features used per session: 1.2 → 3.5 (3x increase)
- NPS: 48 (healthy)

You declare PMF and start scaling investment.

Six months later, churn accelerates. You investigate and find: users were engaging *with the variance*, not with the product. They kept coming back because they were testing whether the AI would be reliable. After six months of inconsistent quality, they gave up and left.

The engagement was real, but it was fragile. It looked like fit but was actually stress-testing.

### Trap 2: The Variance Bounce

User A tries your AI coding assistant on Monday. The code it generates is excellent. User A starts a new session on Tuesday and gets mediocre code. On Wednesday, excellent code again.

User A's trust curve looks like a sine wave oscillating between 0.3 and 0.8. Your cohort-level metric (averaging across users and time) shows trust = 0.55, which looks healthy.

But User A is leaving. They can't depend on your product. They're looking for a competitor.

Aggregated metrics hide the variance problem. You need to measure variance explicitly, not just mean quality.

### Trap 3: The Correction Loop Trap

You track: "Users are correcting outputs less over time." You celebrate: "PMF signal! Quality is so high users trust the output more."

Alternate explanation: Users have learned that correction is futile. They gave up. They're not editing because they've accepted the AI will be wrong sometimes and they'll work around it.

True PMF means users are correcting less *and* the output quality is actually improving*. You can't tell the difference between "acceptance" and "resignation" without measuring downstream — does the user come back, or do they just accept a worse outcome?

### Trap 4: The Benchmark Illusion

You measure: "Our AI gets the task right 82% of the time. Competitor's AI gets it right 79%. We win."

But your users are leaving to the competitor. Why?

They don't care about 82% vs 79%. They care about consistency. Your AI is right 82% of the time but unpredictable about *which* 82%. The competitor's AI is right 79% of the time but *predictably* right on the most important use cases and *predictably* wrong on edge cases. Users know what they're getting.

PMF is not about winning a benchmark. It's about reliability enabling dependence.

### Trap 5: The Implicit Trust Assumption

You assume: "If NPS is 45+, users trust the product."

NPS measures "would you recommend this?" Not "do you depend on this?"

A user can say "yes, recommend this" (high NPS) while also thinking "but I use it with skepticism and always double-check the output." That's low trust, high NPS.

Conversely, a user can have NPS 35 ("don't recommend, too many edge cases") while having high trust ("but I've learned the edge cases and work around them").

NPS and trust are orthogonal in AI products. Don't confuse them.

## INTELLECTUAL LINEAGE

- **Sean Ellis' "Would be very disappointed?" test** — The origin of PMF measurement. Ellis asked: If you could no longer use this product, how disappointed would you be? The premise: users dependent on a product would be very disappointed. For deterministic products, this is reliable. For non-deterministic products, it's insufficient. A user could be very disappointed but still not depend on the system if the system is unreliable.

- **Rahul Vohra's segmentation approach** — Vohra moved beyond "would be disappointed" to segment users by how delighted they were. This helps, but it still assumes stable product quality. In AI, user delight swings with output variance.

- **Elaine May's work on trust decay** — In safety-critical systems (aviation, healthcare), trust isn't built by perfect performance. It's built by consistent performance, even when that performance is "good, not perfect." Pilots trust systems that are predictably good on normal cases and predictably warn on edge cases. They don't trust systems that are sometimes excellent and sometimes fail without warning.

- **Nassim Taleb on tail risk and dependence** — You don't depend on a system because it's good on average. You depend on it because you know its failure modes and can work around them, or because failures are so rare they don't threaten your plan. This applies to AI: users trust AI not when it's 85% accurate, but when they understand the 15% it gets wrong.

- **Anthropic's trust framework** — Trust in AI systems comes from (1) transparency about limitations, (2) consistent behavior within known boundaries, (3) honest communication of failure modes, and (4) predictable refusal rather than silent failures.

## REAL-WORLD EXAMPLES

### Example 1: The Coding Assistant Case (Predictability > Accuracy)

Two coding AI assistants, 2023.

**Competitor A:**
- Accuracy: 81% (code compiles, does what you ask)
- Variance: ±25% (sometimes excellent, sometimes terrible on same task types)
- Engagement: 4 sessions/week, 12 min/session
- NPS: 44
- Retention at 8 weeks: 62%

**Competitor B:**
- Accuracy: 73% (code compiles, does what you ask)
- Variance: ±8% (consistently good on common patterns, predictably fails on edge cases)
- Engagement: 2.5 sessions/week, 8 min/session
- NPS: 51
- Retention at 8 weeks: 71%

**Surface metrics:** Competitor A should win (higher accuracy, higher engagement).

**Reality:** Competitor B captured the market. Why?

Developers don't care about 81% vs 73%. They care about **predictability**. Competitor B's low variance meant developers learned: "This AI is great for [pattern X], bad for [pattern Y]." They could work around it.

Competitor A's high variance meant: "Is this good code? I have to re-read everything." Developers never trusted it, even on average "good" weeks.

**PMF signals diverged:**

| Metric | Competitor A | Competitor B | Winner |
|--------|--------------|--------------|--------|
| Trust curve (week 8) | 0.52 (volatile) | 0.65 (inflecting) | B |
| Correction rate decay | +5% (worsening) | -50% (improving) | B |
| Engagement trend | Down (give up on AI) | Up (learned dependency) | B |

**Lesson:** Consistency > accuracy on raw metrics. Trust curve catches what NPS/engagement hide.

### Example 2: The Customer Support Escalation Case

AI vendor launched customer support AI for SaaS companies.

**Early metrics looked great:**
- Deflection rate: 35% (AI answered and customer didn't escalate)
- User satisfaction on deflected issues: 4.2/5
- NPS: 42
- Retention: 58%

**But after 3 months, logos started churning.**

Investigation found: Deflection rate was *misleading*. Customers weren't satisfied with the AI response; they were satisfied that *someone* responded quickly. Many were still escalating to human support because they didn't trust the AI.

True metric: Trust curve showed plateau at 0.48 (below the 0.60 threshold). Customers would use the AI but didn't depend on it.

The product was solving a different problem than intended: "quick response" not "reliable resolution." Once customers realized the AI responses weren't reliable, engagement dropped.

PMF signal: The magic moment never happened. Users never reached the inflection point on the trust curve.

### Example 3: The Privacy Policy Pivot (Trust Curve Detects Hidden Blockers)

Research assistant AI, 2022. Privacy policy: "We use your queries to improve our model (with anonymization)."

Traditional metrics:
- NPS: 38 (okay)
- Retention at 8 weeks: 45% (concerning)
- Engagement: Soft, unprompted

They pivoted privacy policy: "We never retain your data. All queries are deleted after processing."

New traditional metrics:
- NPS: 41 (+3, marginal)
- Retention: 52% (+7, slight improvement)
- Engagement: Slightly better

**But trust curve revealed the real story:**

| Week | Old Policy (Data Retained) | New Policy (Data Deleted) |
|------|---------------------------|--------------------------|
| 1 | 0.42 | 0.48 |
| 2 | 0.45 | 0.56 |
| 3 | 0.44 | 0.62 |
| 4 | 0.43 | 0.68 |

Old policy: **Flat trust curve** — users never gained confidence. They suspected data retention was a risk; trust ceiling was low.

New policy: **Clear inflection upward** — users felt safe depending on the system once privacy was explicit.

**Lesson:** Users had a hidden PMF blocker (privacy risk) that NPS couldn't detect. Trust curve caught it because it measures dependence, not just satisfaction. The pivot worked because it removed the blocker.

### Example 4: The Magic Moment Discovery

Legal research AI platform launched with three use cases:
1. Case law search
2. Contract analysis
3. Regulatory compliance checking

Engagement metrics were flat across all three. Retention was 40%.

They measured magic moment per use case:
- Case law search: 15% of users hit "5 successful searches" (the magic moment). Of those, 75% returned.
- Contract analysis: 40% of users uploaded a contract and successfully analyzed it. Of those, 82% returned.
- Regulatory checking: 8% of users completed a full compliance check. Of those, 70% returned.

The winning use case wasn't the most popular — it was the one with highest magic moment conversion (40%) and strongest retention from magic moment users (82%).

They deprioritized case law search and regulatory checking. They focused 80% of product investment on making contract analysis easier to reach the magic moment.

Result: 6 months later, retention at 8 weeks was 71% (vs. 40%). Trust curve showed clear inflection at week 3 (when users completed their first contract analysis).

Lesson: PMF isn't always about doing everything well. It's about finding the use case where the magic moment converts users to trust curve inflection.

## FRAMEWORK LIMITATIONS

This framework assumes:

1. **Interactive AI products.** Batch inference or offline AI don't have real-time user feedback loops. Magic moment and trust curve don't apply.

2. **Sufficient user volume.** With <50 weekly active users, noise is too high. Minimum 100 WAU for meaningful trust curve measurement.

3. **Measurable output quality.** If output quality can't be evaluated (e.g., creative writing, open-ended generation), correction rate is noisy. Rely more on engagement and switching cost signals.

4. **Coherent user cohorts.** If your user base is highly heterogeneous (power users, casual users, enterprise, individual), measure magic moment and trust per cohort separately.

5. **Clear success definition per use case.** "Code generation" has clear correctness; "brainstorming" doesn't. PMF signals are weaker for subjective use cases.

## FURTHER READING

- Sean Ellis, "Find Product-Market Fit" — The foundational PMF definition
- Rahul Vohra, "Segment Your Users by Delight" — Advanced user segmentation for PMF
- Elaine May, *Trust in Automation* — On how humans build trust in non-deterministic systems
- Nassim Taleb, *Antifragile* — On dependence and tail risk in complex systems
- Anthropic blog, "Constitutional AI as Trust Infrastructure" — On trust as a measurable property of AI systems
- Andrew Ng, "AI for everyone" — On AI capability and reliability distinctions in product
