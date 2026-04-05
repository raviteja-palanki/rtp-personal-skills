# Strategy Canvas — Concept Guide

## FIRST PRINCIPLES

Traditional product strategy assumes a stable capability frontier. You know what technology can do. You compete on how well you apply it to user problems. The strategic question is "where to play and how to win" within known boundaries.

AI product strategy operates on a shifting capability frontier. What the technology can do changes quarterly. A feature that required 6 months of custom ML last year is a prompt away today. A competitive moat built on data advantage can be undermined by a new model that needs less data.

The atomic insight: **AI strategy is not about predicting the future of AI. It's about designing a strategy that remains valid across multiple possible futures of AI.**

## DUAL DEFINITION

**Business definition:** The AI strategy canvas is a living strategic document that separates stable market realities from volatile technology capabilities, defines strategic bets that adapt to capability changes, and identifies the unique advantages that make the strategy defensible regardless of which models or tools emerge.

**Technical definition:** A capability-conditional strategic framework that maps product direction to model capability thresholds, defines trigger conditions for strategic pivots, and maintains an inventory of durable technical advantages (proprietary data, workflow integration, domain models) independent of any specific model provider.

## THE TRAP (Expanded)

**The Roadmap Trap.** A PM creates a 12-month AI roadmap. Month 3: a new model launches that can do in zero-shot what the team planned to fine-tune for. The roadmap is obsolete, but sunk cost and organizational momentum keep it alive. The team spends 9 months building something that's now commodity.

**The Model-Dependent Strategy.** "Our advantage is that we use Claude/GPT-4/Gemini." This is a vendor relationship, not a strategy. When the competitor switches to the same model (trivially easy), the advantage evaporates. Strategy must be independent of model choice.

**The Data Moat Illusion.** "We have more data." Historically true as a moat. But foundation models are increasingly data-efficient. A model that needs 1,000 examples to learn your domain makes your 10,000-example dataset 10x less valuable as a moat. Data is a moat only if it's proprietary, growing, and hard to replicate — not just large.

## INTELLECTUAL LINEAGE

- **Roger Martin** — *Playing to Win.* "Where to play" and "how to win" adapted for AI's volatile capability frontier.
- **Gibson Biddle** — DHM (Delight, Hard-to-copy, Margin) model. Applied to AI: hard-to-copy in AI is workflow depth and trust, not model access.
- **Hamilton Helmer** — *7 Powers.* Which of the 7 powers (scale, network effects, switching costs, etc.) actually apply in AI products?
- **Shreyas Doshi** — On the distinction between strategy (where to invest) and planning (how to execute). AI collapses the timeline between them.

## REAL-WORLD EXAMPLES

**Capability-conditional bet.** A legal tech company defined two strategic paths: Path A (if model reasoning improves to handle multi-step legal analysis by Q3) = AI-first legal research. Path B (if not) = AI-assisted human research with smart retrieval. When model capability hit the threshold in Q2, they triggered Path A with an already-designed architecture. Competitors who bet on a single path either over-built or under-built.

**Unique context advantage.** An enterprise AI company's moat wasn't the model — it was 200+ pre-built connectors to enterprise systems (SAP, Salesforce, ServiceNow). Any competitor could match their model quality. None could replicate three years of integration engineering, customer-specific configurations, and compliance certifications.

## FURTHER READING

- Roger Martin, *Playing to Win* — Strategic choice-making adapted for volatile environments
- Hamilton Helmer, *7 Powers* — Durable competitive advantage analysis
- Gibson Biddle, "DHM Framework" — Delight/Hard-to-copy/Margin for AI products
- Ben Thompson, *Stratechery* — Platform strategy in AI era
