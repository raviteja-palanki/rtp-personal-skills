# Red Team — Concept Guide

## FIRST PRINCIPLES

Karl Popper's foundational insight: a theory that can't be proven wrong isn't a theory — it's a belief. Applied to products: a feature hypothesis that has no defined failure conditions isn't a hypothesis — it's a wish.

AI products are uniquely vulnerable to unfalsifiable reasoning because non-deterministic outputs make it easy to find confirming examples. "The model works great!" can always be supported by cherry-picked examples. Falsification forces the question: "Under what specific, measurable conditions would we admit this doesn't work?"

## DUAL DEFINITION

**Business definition:** Falsification is the practice of defining what failure looks like before you launch, so you can recognize it when it happens — instead of rationalizing it away after the fact.

**Technical definition:** The construction of testable null hypotheses for AI product features, with pre-committed decision thresholds on specific metrics (accuracy, latency, cost, user behavior), measured over defined time windows.

## THE TRAP (Expanded)

AI products create three falsification-resistant patterns:

**The anecdote shield.** Non-deterministic systems always produce good outputs sometimes. A PM under pressure to justify an AI feature will find the perfect example. "Look, it handled this complex query perfectly!" The five mediocre responses and two terrible ones don't make the slide deck.

**The moving goalpost.** When initial metrics disappoint, the definition of success shifts. "Well, accuracy is only 70%, but user satisfaction is up." When satisfaction disappoints: "But engagement increased." The goalpost moves until a metric is found that confirms the narrative.

**The premature scaling defense.** "It doesn't work yet because we need more data/better prompts/a larger model." This is sometimes true and sometimes a rationalization. Without pre-committed kill conditions, you can't distinguish between "needs more time" and "fundamentally flawed."

## INTELLECTUAL LINEAGE

- **Karl Popper** — The Logic of Scientific Discovery. Falsifiability as the demarcation between science and pseudoscience.
- **Anthropic's red-teaming practice** — Systematic adversarial testing of AI systems before deployment. Applied here to product decisions.
- **Teresa Torres** — Assumption mapping. Identifying the riskiest assumptions and testing them first.
- **Nassim Taleb** — The Black Swan. On the asymmetry of evidence: a thousand white swans don't prove "all swans are white," but one black swan disproves it.

## REAL-WORLD EXAMPLES

**Example 1: The summarization feature.** A team launched AI document summarization without kill conditions. Usage was "growing." Six months later, a user study revealed people were re-reading the original documents after the summary because they didn't trust the output. Usage was high because the feature was creating extra work, not reducing it. With pre-committed kill conditions on "time saved per document," this would have been caught in month two.

**Example 2: The recommendation engine.** A team defined clear falsification criteria: "If click-through rate on AI recommendations drops below 15% for two consecutive weeks, we investigate. Below 10%, we revert to rules-based." CTR hit 12% in week three. Because the kill condition was pre-committed, the team investigated immediately instead of waiting and hoping. They found a data freshness issue, fixed it, and CTR recovered to 22%.

**Example 3: The cost trap.** A team launched an AI feature with "cost efficiency" as a success metric but no kill threshold. The per-token cost was $0.002 per request. At prototype scale, this felt negligible. At production scale with 10M daily tokens, it became $20k/day. The kill condition "if cost exceeds $5k/day for 30 days, we pivot" would have caught this in month one. Without pre-commitment, the team rationalized the expense for six months until the CFO demanded an explanation.

## PRODUCTION DISCIPLINE

**Pre-commitment is political.** The team that championed a feature will resist formalizing failure conditions. It feels like saying "I might be wrong," which feels weak. But pre-commitment is actually strength—it means you're confident enough to specify what success looks like. The team that won't define failure conditions isn't confident; it's avoiding accountability.

**The metric selection problem:** The easiest kill condition to define is the one that will almost certainly not trigger. Teams often choose vanity metrics (engagement, usage) over hard metrics (revenue, cost, retention). Falsification forces honest metric selection. If the only success metric is "teams are using it," that's not falsification—that's a wish.

**The time window matters:** Most AI products look like failures at week two and successes at month three (or vice versa). Falsification requires specifying time windows. "If accuracy is below 70% after two weeks of production data, we investigate" is different from "after two months." The time window should match the natural pace of the system and your ability to gather signal.

**Red flags for failed falsification:**
- Metrics chosen after launch instead of before
- Kill conditions that are vague ("if it doesn't feel right")
- Kill conditions that are impossible to measure
- No pre-commitment—just a promise to "check metrics after launch"
- Different stakeholders with different definitions of success

## FURTHER READING

- Karl Popper, *The Logic of Scientific Discovery* — The origin of falsifiability
- Nassim Taleb, *The Black Swan* — On the asymmetry of evidence
- Teresa Torres, *Continuous Discovery Habits* — Assumption testing in product
- Anthropic, "Red Teaming Language Models" — Adversarial testing methodology
