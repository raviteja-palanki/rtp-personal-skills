# Determinism Compass — Concept Guide

## FIRST PRINCIPLES

Every software system is a composition of operations. Each operation sits somewhere on a spectrum from fully deterministic (given input X, always produce output Y) to fully probabilistic (given input X, produce an output from a distribution of acceptable responses). Traditional software lives at the deterministic end. LLMs live at the probabilistic end. Production AI products live in the messy middle — and the PM's job is to draw the map.

The atomic insight: **the single most important architectural decision in an AI product is where the boundary sits between deterministic and probabilistic components.** Get this wrong and you'll have an unreliable product (too much AI) or a brittle product (too many rules). Get it right and you'll have a system where each component uses the right tool for its job.

## DUAL DEFINITION

**Business definition:** The determinism compass tells you which parts of your product need AI and which parts should be traditional software — so you don't pay AI costs for problems that have simpler solutions, and you don't build brittle rules for problems that require AI judgment.

**Technical definition:** A component-level classification system that maps each operation in a feature to one of three execution modes — deterministic (rules engine), probabilistic (model inference), or hybrid (model inference with deterministic guardrails) — based on input structure, output variability, and judgment requirements.

## THE TRAP (Expanded)

**The "AI-First" Fallacy.** Teams adopt an "AI-first" philosophy that sounds innovative but produces absurd results. An AI-first team might use an LLM to validate whether an email address contains an "@" symbol. This is a regex problem. The LLM is slower, more expensive, and occasionally wrong. But "AI-first" doesn't have a carve-out for regex, so nobody questions it.

**The "Rules-Only" Fortress.** The opposite trap. Teams burned by AI unreliability retreat to rules for everything. They build elaborate decision trees to handle customer intent classification — hundreds of if/else branches that become unmaintainable, miss edge cases, and produce a robotic user experience. The problem genuinely requires pattern recognition on unstructured input, but the team's bad experience with AI has made rules the default.

**The Missing Boundary Contract.** Even teams that classify correctly often fail at the handoff. The rules engine passes a request to the AI component — but what format? What happens if the AI returns an unexpected response? Who validates the AI output before it reaches the user? The boundary between deterministic and probabilistic zones is where most production failures occur.

## INTELLECTUAL LINEAGE

- **Ravi's CONTEXT Framework** — The seven-layer production AI architecture where each layer has different determinism requirements. The Constitution layer is mostly rules; the Execution layer is mostly AI; the Equipment layer is hybrid.
- **Anthropic's Constitutional AI** — A masterclass in hybrid design. The model (probabilistic) is guided by constitutional principles (deterministic rules) that constrain its output space. The boundary is explicit and engineered.
- **Martin Fowler / Domain-Driven Design** — Bounded contexts applied to AI systems. Each bounded context has its own determinism classification.

## REAL-WORLD EXAMPLES

**Example 1: Banking transaction monitoring.**
- Rules (deterministic): Flag transactions over $10,000 (regulatory mandate — no judgment needed).
- AI (probabilistic): Classify whether a pattern of small transactions constitutes structuring (requires pattern recognition on complex temporal sequences).
- Hybrid: AI flags suspicious patterns with a confidence score. Below 90% → human analyst review. Above 90% → auto-freeze account with instant customer notification. The boundary is explicit, and each zone has a clear responsibility.

**Example 2: Content moderation pipeline.**
- Rules: Block known prohibited URLs and phone numbers (deterministic blocklist, zero false negatives required).
- AI: Classify whether novel user-generated content violates community guidelines (judgment call on subjective policy).
- Hybrid: AI assigns severity score (1-10). Scores 1-3 → no action. Scores 4-7 → queued for human review. Scores 8-10 → auto-remove with transparent appeals path. The confidence threshold is tunable based on false-positive cost.

**Example 3: Customer support routing.**
- Rules: Password reset requests → automated flow (structured category, keyword match, zero judgment needed).
- AI: Ambiguous requests that don't match any category → intent classification and urgency assessment.
- Hybrid: AI classifies intent. But if customer has been escalated 3+ times in 30 days OR account value > $100K, route to human regardless of AI confidence. Business rules override probabilistic judgment.

## FURTHER READING

- Ravi Teja Palanki, "The CONTEXT Framework" — Seven-layer production AI architecture
- Anthropic, "Constitutional AI: Harmlessness from AI Feedback" — Hybrid deterministic/probabilistic design
- Martin Fowler, "Bounded Contexts" — Domain boundaries applied to system design
- Google, "Rules of Machine Learning" — When to use ML and when not to
