# Bias Spotter — Concept Guide

## FIRST PRINCIPLES

Human cognition runs on heuristics. Heuristics are fast but systematically wrong in predictable directions. In AI product management, these systematic errors are amplified because AI products themselves are probabilistic — making it harder to distinguish between "the model is wrong" and "my judgment about the model is wrong."

The atomic insight: **the most dangerous AI product decisions are the ones that feel obviously right.** When something feels obvious, it means your System 1 (fast, intuitive) has already decided and your System 2 (slow, analytical) is rationalizing. Bias-spotting forces System 2 to actually check the work.

## DUAL DEFINITION

**Business definition:** Bias-spotting is a structured check that prevents the most common and expensive reasoning errors in AI product decisions — especially the tendency to overestimate AI capabilities, underestimate AI costs, and chase competitors rather than user needs.

**Technical definition:** A systematic audit of the decision-making process that identifies which cognitive heuristics are active, assesses their impact on the specific decision being made, and produces a bias-adjusted recommendation with explicit residual risk.

## THE TRAP (Expanded)

AI products create a unique bias cocktail:

**The Demo Effect (Optimism + Anchoring).** Teams see a demo where the model performs brilliantly on curated examples. This anchors expectations. The 95% accuracy on the demo set becomes the mental model, even when production data is messier, more diverse, and adversarial. The PM writes "95% accuracy" in the PRD without qualifying it.

**The Competitor Cascade (Bandwagon + Action).** A competitor launches an AI feature. The board asks "where's our AI feature?" The team scrambles to build one. Nobody asks whether the competitor's feature is actually working, whether users want it, or whether the competitive threat is real. The bias compound: bandwagon ("everyone's doing it") plus action bias ("we must respond").

**The Token Blindness (Present + Normalcy).** Per-token costs look trivial at prototype scale. A team calculates "$0.002 per request — negligible!" They don't model 100,000 daily active users, each making 10 requests, with 3x token overhead for context and retries. Present bias makes the current cost feel like the future cost. Normalcy bias makes cost growth feel linear when it's actually multiplicative.

## INTELLECTUAL LINEAGE

- **Daniel Kahneman** — *Thinking, Fast and Slow.* The System 1/System 2 framework. Most AI product decisions are System 1 dressed in System 2 language.
- **Charlie Munger** — The psychology of human misjudgment. 25 cognitive biases mapped to investment decisions. Applied here to product decisions.
- **Amos Tversky** — Prospect theory. Loss aversion explains why teams double down on failing AI features rather than cutting losses.
- **Gary Klein** — Pre-mortem technique. "Imagine this project has failed. Why?" Forces prospective rather than retrospective bias checking.
- **Philip Tetlock** — *Superforecasting.* On calibration — the practice of assigning honest probabilities to outcomes rather than binary predictions.

## REAL-WORLD EXAMPLES

**Example 1: The chatbot that "worked."** A team launched an internal chatbot and measured success by usage volume. High usage felt like validation (confirmation bias). A deeper analysis revealed users were asking the same question multiple times because the first answer was wrong. High usage was a failure signal, not a success signal. The bias: measuring what confirmed the narrative instead of what revealed the truth.

**Example 2: The enterprise deal that drove the roadmap.** A large customer requested a specific AI feature. The sales team anchored the entire roadmap around it. Nobody asked whether this feature served the broader market or just this one customer's idiosyncratic workflow. The bias: authority (the customer is always right) compounded with anchoring (the first request frames the roadmap).

**Example 3: The model upgrade that wasn't.** A team invested two months upgrading from GPT-3.5 to GPT-4 for their product, assuming the upgrade would improve all metrics. It improved accuracy on complex queries but increased latency on simple ones, and the token cost tripled. The bias: optimism (newer = better) combined with survivorship (they only tested on the hard cases where improvement was expected).

## PRODUCTION DISCIPLINE

The hardest part of bias-spotting isn't identifying biases—it's having the organizational permission to name them without being accused of "being difficult" or "killing momentum."

**Cultural setup:** Bias-spotting works best in teams that have agreed in advance: "We're going to check for biases on consequential decisions. This is not an attack on the person who proposed the idea. It's a check on the reasoning." Without this setup, speaking up about biases feels like political risk.

**The timing question:** The best time to spot biases is before momentum builds. The worst time is after a team has already invested weeks. Run the bias checklist on decisions early, when course-correction is still cheap.

**The dominant bias pattern:** Most AI product teams have one or two dominant biases that repeat across decisions. (e.g., "we always optimize for short-term metrics at the expense of long-term sustainability," or "we always chase competitors rather than users"). Identifying the team's bias pattern is more valuable than doing one-off checks.

**Red flags that bias-checking is being skipped:**
- "We don't have time for this process"
- "This is too low-stakes for analysis" (but if it's low-stakes, the analysis takes 15 minutes)
- "Let the data speak for itself" (the data will be interpreted through biases)
- "The senior person has decided, so we don't need to check" (especially important to check then)

## FURTHER READING

- Daniel Kahneman, *Thinking, Fast and Slow* — The foundational text on cognitive biases
- Charlie Munger, *Poor Charlie's Almanack* — 25 cognitive biases applied to decision-making
- Philip Tetlock, *Superforecasting* — On calibration and honest probability assessment
- Gary Klein, "Performing a Project Premortem" (HBR) — Prospective bias checking
