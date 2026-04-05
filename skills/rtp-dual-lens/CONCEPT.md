# Dual-Lens — Concept Guide

## FIRST PRINCIPLES

AI product management sits at the intersection of two vocabularies that rarely overlap. Business leaders speak in revenue, risk, competitive position, and customer trust. Engineers speak in latency, throughput, model accuracy, and system architecture. The PM who can only speak one language is, at best, a translator. The PM who thinks in both languages simultaneously is a bridge.

The atomic insight: **every AI product decision has a business meaning and a technical meaning. If you can only articulate one, you understand neither.**

## DUAL DEFINITION

**Business definition:** Dual-lens communication is the practice of expressing every AI product concept in two parallel forms — one that enables business leaders to make resource and strategy decisions, and one that enables engineers to make architecture and implementation decisions — connected by an explicit translation layer.

**Technical definition:** A structured communication protocol that maps business requirements to technical constraints and technical decisions to business implications, producing bi-directional traceability between stakeholder needs and system design.

## THE TRAP (Expanded)

**The Engineer's Trap: Precision Without Actionability.** An engineer describes the system with perfect technical accuracy. The business stakeholder nods, understands nothing, and approves whatever was proposed. Three months later, when the feature doesn't match expectations, both sides are surprised. The spec was precise. It just wasn't actionable for the person making the resource decision.

**The Executive's Trap: Ambition Without Constraint.** A VP declares "we need AI-powered personalization by Q3." The engineer hears no latency requirements, no cost ceiling, no accuracy threshold, no failure mode handling. They build what they think was meant. It's technically impressive and commercially useless.

**The PM's Trap: Translation Without Fidelity.** The PM tries to bridge the gap by simplifying. "The model is pretty accurate" becomes the translation of "87% F1 score with significant variance on long-tail queries." The simplification loses the information that would change the business decision.

## INTELLECTUAL LINEAGE

- **Anthropic's communication pattern** — Simultaneously publishing Constitutional AI research papers (technical) and enterprise trust documentation (business). The same concept, dual expression.
- **Shreyas Doshi** — On product sense requiring both "customer obsession" (business) and "technical depth" (engineering) — not as separate skills but as simultaneous lenses.
- **Marty Cagan** — "Deep enough to earn the respect of engineers." The PM earns cross-audience credibility by demonstrating fluency, not just familiarity.
- **Edward Tufte** — On the integrity of data presentation. Simplification that distorts is worse than complexity that's accurate.

## REAL-WORLD EXAMPLES

**Example 1: Explaining hallucination to a board.** Technical: "The model generates text that is syntactically correct but factually unsupported by the training data or retrieved context, with occurrence rates of 3-8% depending on query complexity." Business: "In 3-8% of responses, the AI will say something that sounds confident but is wrong. For a customer-facing product, that means 3-8 out of every 100 users get misinformation. Our mitigation strategy reduces this to under 1%, but eliminating it entirely is not possible with current technology."

**Example 2: Justifying RAG architecture.** Technical: "Retrieval-Augmented Generation embeds domain documents into vector representations, retrieves relevant chunks at query time via semantic similarity, and injects them into the model's context window, reducing hallucination on domain-specific queries by 60-80%." Business: "Instead of teaching the AI everything about our domain (expensive, slow to update, hard to control), we let it look up the answer in our own documents every time someone asks a question. It's like giving the AI an open-book exam instead of expecting it to memorize the textbook."

**Example 3: Explaining latency requirements.** Business: "We need responses in under 2 seconds. If it takes longer, users abandon the feature." Technical: "Sub-2-second SLA means we can't do full cross-document search, can't run expensive ranking algorithms, and can't use larger context windows. We need streaming output and token-level budget management." The translation: "The business constraint of 2-second latency has these specific architectural implications that trade against other desirable properties (depth of context, ranking sophistication)."

## PRODUCTION DISCIPLINE

**The alignment cost:** When business and engineering are misaligned on what's being built, the cost is catastrophic. Engineers ship a technically sound solution that doesn't match the business requirement. Three months of work delivers the wrong thing. Dual-lens communication catches this misalignment before work begins.

**The credibility multiplier:** A PM who can explain concepts in both languages gains credibility with both audiences. Engineers believe the PM understands their constraints. Business leaders believe the PM understands their goals. This credibility is the PM's most valuable asset in a conflict.

**The bridge-building skill:** Dual-lens is not about dumbing down technical concepts for executives. It's about finding the business meaning of every technical decision and the technical implication of every business requirement. This is hard work. It requires:
- Understanding the technical depth (or you'll oversimplify until you're wrong)
- Understanding the business context (or you'll miss what matters)
- The ability to translate between vocabularies (or the bridge won't hold)

**Red flags for broken dual-lens communication:**
- The business definition and technical definition don't describe the same thing
- One audience understands the concept and the other is confused
- Technical decisions are made without business stakeholders understanding the implications
- Business decisions are made without technical stakeholders understanding the constraints
- A PRD that works perfectly for business but is unactionable for engineering
- An engineering spec that engineers love but business leaders don't understand

**Common failure mode:** The PM writes a "translation" that's actually just a simplification. "The model is pretty good" is not a translation of "87% F1 with 12% variance on long-tail queries." It's a loss of information. Real translation preserves meaning while changing form.

## FURTHER READING

- Marty Cagan, *Inspired* — On PM credibility across business and engineering
- Anthropic, "Core Views on AI Safety" — Dual-audience communication in practice
- Edward Tufte, *The Visual Display of Quantitative Information* — On honest simplification
- Shreyas Doshi, "How to Develop Product Sense" — On simultaneous business + technical thinking
