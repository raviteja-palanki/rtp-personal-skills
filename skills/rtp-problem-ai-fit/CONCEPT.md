# Problem-AI Fit — The Concept

*The most important question in AI product management is the one teams skip.*

---

## The Atomic Insight

The default state of any product problem is "doesn't need AI." AI is the intervention that must be justified, not the starting assumption. This inversion — treating AI as the exception rather than the rule — prevents the most expensive category of AI product failure: building sophisticated infrastructure for simple problems.

---

## Dual Definition

**For the CEO:** "Before we invest in AI infrastructure, we need to verify that this problem actually requires machine judgment — not just faster data processing. Most of what looks like an AI problem is actually a search, rules, or workflow problem wearing an AI costume."

**For the CTO:** "The four-question test distinguishes problems that need probabilistic reasoning from problems that need deterministic logic. LOOKUP and TRANSFORM operations don't benefit from LLMs — they benefit from good indexing and clean data pipelines. Save the AI budget for CLASSIFY and GENERATE problems where human judgment actually needs to be scaled."

---

## The Trap — Expanded

AI-washing is the enterprise version of cargo cult programming.

The cargo cult built runways out of bamboo because they saw that real runways attracted planes full of supplies. Enterprise teams build AI features because they see that AI companies attract funding, press, and executive attention. The bamboo runway doesn't attract planes. The AI feature doesn't attract users.

The mechanism is organizational, not technical. The decision to use AI is rarely made by the person who understands the problem best. It's made by the person who needs to tell a story to the board, or who needs to justify a platform investment, or who read a competitor's press release. By the time the engineers start building, the "should we use AI?" question has been answered by default.

The four-question test is designed to interrupt this pattern. It forces the conversation back to first principles before architecture decisions are made. And critically, it gives the team a structured way to say "no" to AI without looking unambitious.

---

## Intellectual Lineage

**Aman Khan (Arize AI)** — The observation that most ML products fail not because of model quality, but because the problem was wrong for ML in the first place.

**Shreyas Doshi** — "The most impactful thing a PM can do is decide what NOT to build." Applied to AI: deciding NOT to use AI is often the highest-leverage product decision.

**Anthropic's own product philosophy** — Claude doesn't try to be everything. It's a language model that excels at reasoning, writing, and analysis. The features it doesn't have are as revealing as the features it does. Knowing where AI adds value — and where it doesn't — is product judgment at work.

---

## Real-World Examples

**Invoice processing.** A fintech company proposed "AI-powered invoice extraction." Decomposition: the atomic operation was TRANSFORM (extract structured fields from a known document format). The AI-necessity test scored 1/4 — the output didn't require judgment, just pattern matching. Solution: template-based extraction with regex fallbacks. Cost: $0.002/invoice instead of $0.15/invoice. Accuracy: 97% (higher than the LLM prototype, which hallucinated amounts on poorly scanned documents).

**Content moderation.** A social platform proposed "AI content moderation." Decomposition: the atomic operation was CLASSIFY (assign content to policy-violation categories). Score: 4/4 — judgment required, learnable from examples, errors recoverable (human review queue), high volume. This was a genuine AI problem. The right architecture was a fast classifier for clear cases with LLM escalation for ambiguous ones.

**Meeting scheduling.** A productivity startup proposed "AI meeting scheduler." Decomposition: the atomic operation was LOOKUP (find overlapping free time across calendars). Score: 0/4. The problem needed calendar API integration, not language understanding. The LLM prototype was slower, more expensive, and less accurate than a simple constraint-satisfaction algorithm.

---

## Further Reading

- Aman Khan, "When Not to Use ML" (talk, Arize AI)
- Shreyas Doshi, "The Most Important PM Decisions Are What Not to Build"
- Google's Rules of ML: Rule #1 — "Don't be afraid to launch a product without machine learning"
