# First Principles — Concept Guide

## FIRST PRINCIPLES

Every complex system is built from simple operations. The job of first-principles thinking is to find the ONE irreducible operation buried under layers of implementation, politics, and inherited assumptions.

In AI products, this matters more than in traditional software because AI introduces a seductive layer of complexity. Traditional software fails visibly — the button doesn't work. AI software fails invisibly — the button works, but the answer is wrong. First-principles thinking strips away the AI layer to ask: what is the user actually trying to accomplish, and does this accomplishment require probabilistic computation at all?

The atomic insight: **most AI product failures aren't AI failures. They're decomposition failures.** The team built an impressive AI system to solve a problem that didn't need AI, or that needed AI in a different place than where they applied it.

## DUAL DEFINITION

**Business definition:** First-principles thinking is the practice of identifying the single most important user outcome before deciding what technology to build. It prevents the most expensive mistake in AI product development: building sophisticated AI for the wrong problem.

**Technical definition:** First-principles decomposition maps a proposed system to its minimal viable computation graph — identifying which operations are deterministic (rules), which are probabilistic (AI), and which require human-in-the-loop oversight. It produces a determinism classification for every load-bearing component.

## THE TRAP (Expanded)

Three cognitive biases conspire against first-principles thinking in AI:

**Anchoring bias.** The first solution you encounter becomes the invisible frame. If a competitor launched an "AI-powered search," your team anchors on AI-powered search. Nobody asks whether search is the right metaphor, or whether users actually want search at all (maybe they want curation, or alerts, or a feed).

**Availability bias.** Whatever technology the team recently learned feels like the right tool. Team just completed a RAG proof-of-concept? Every problem looks like a retrieval problem. Team just experimented with agents? Every workflow needs an agent.

**Sunk cost fallacy.** Once a team has invested weeks building an AI component, first-principles questioning feels threatening. "Are you saying we wasted three sprints?" becomes the unspoken response, and the decomposition exercise gets short-circuited.

The common pattern: a team proposes "an AI feature that does X." The PM nods and writes the PRD. Nobody stops to ask whether X needs AI, whether the user even wants X, or whether X is the right decomposition of the user's actual problem.

## INTELLECTUAL LINEAGE

- **Kapil Gupta** — "Diagnosis before prescription." Gupta's insistence that prescriptions (solutions, how-tos, frameworks) are worthless without first seeing the problem clearly. Applied here: decompose the problem before reaching for AI.
- **Elon Musk / Physics thinking** — Reasoning from first principles rather than analogy. "We need AI because competitors have AI" is analogy. "We need probabilistic classification because this input is unstructured" is first principles.
- **Charlie Munger / Inversion** — "Tell me where I'm going to die, so I don't go there." Applied: before asking "where should we add AI?", ask "where would AI make this worse?"
- **Shreyas Doshi / Product Sense** — The distinction between the problem and the solution. Product sense starts with obsessing over the problem, not the technology.

## REAL-WORLD EXAMPLES

**Example 1: Enterprise document search.** A team proposed building an AI-powered semantic search for internal documents. First-principles decomposition revealed the atomic operation wasn't "search" — it was "find the current version of a specific policy." Rules-based metadata tagging with version control solved 80% of the problem. AI semantic search was needed for only the remaining 20% — natural language queries over unstructured content. The hybrid saved 60% of the original cost estimate.

**Example 2: Customer support AI.** A team proposed an "AI agent that handles customer support tickets." Decomposition revealed five distinct atomic operations: routing (rules), information retrieval (RAG), sentiment detection (classifier), response drafting (LLM), and escalation decisions (hybrid). Treating these as one "AI agent" meant the entire system had the reliability of its weakest link. Decomposing them allowed independent optimization and monitoring.

**Example 3: Pricing recommendation engine.** A team wanted to use AI for dynamic pricing. First-principles analysis showed the atomic operation was "adjust price based on demand signals." The demand signals were structured, quantitative, and followed predictable patterns. A statistical model outperformed the LLM-based approach at 1/100th the cost. AI was solving the wrong layer of the problem.

## PRODUCTION DISCIPLINE

In high-stakes AI product decisions, first-principles thinking becomes a forcing function that prevents expensive mistakes late in development:

**The decomposition gate:** Before estimating effort, assigning resources, or writing a PRD, decompose the problem. A team that skips this will spend 8 weeks building the wrong thing. A team that spends 4 hours decomposing will spend 4 weeks building the right thing. The math is brutal.

**The "atomic operation" discipline:** The ability to state what the user actually needs in one sentence, without technology words, is not a nice-to-have. It's the bare minimum of understanding the problem. If your team can't do this, you don't understand the problem yet. Stop.

**The hybrid architecture insight:** Most AI products don't fail because the AI is bad. They fail because someone built AI for the entire problem when AI was only needed for 20% of it. The decomposition that separates rules from AI from hybrid components is the difference between a cost-effective product and a cost-prohibitive one.

**Red flags that decomposition is being skipped:**
- "We'll figure it out during design" (you won't)
- "The demo shows it works" (demos are best-case scenarios)
- "This is how the competitor did it" (different decomposition, different users)
- "We have budget, so let's build the full feature" (decomposition should constrain scope, not budget)

## FURTHER READING

- Kapil Gupta, *A Master's Secret Whispers* — On seeing the problem before prescribing
- Daniel Kahneman, *Thinking, Fast and Slow* — On anchoring and the illusion of understanding
- Shreyas Doshi, "Product Sense" essays — On problem obsession vs solution obsession
- Shane Parrish, *The Great Mental Models* — On first-principles reasoning across domains
