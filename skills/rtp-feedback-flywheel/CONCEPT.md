# Feedback Flywheel — Concept Guide

## FIRST PRINCIPLES

The best evaluation data for an AI product comes from the people using it. Not from synthetic benchmarks, not from internal testing, not from offline eval sets — from real users correcting real mistakes on real tasks. Every edit a user makes to AI output is a labeled training example. Every abandonment is a signal. Every escalation to a human produces a gold-standard reference.

The atomic insight: **the product interface is the evaluation system.** They're not separate concerns. The way you design the interaction determines the quality and volume of feedback you can capture, which determines how fast the AI improves, which determines the product's competitive trajectory.

## DUAL DEFINITION

**Business definition:** The feedback flywheel turns every user interaction with AI output into data that makes the AI better — creating a compounding improvement cycle where the product gets smarter the more people use it. This is the mechanism behind data-driven competitive moats in AI products.

**Technical definition:** An instrumented interaction layer that captures implicit and explicit user feedback signals (acceptances, edits, rejections, escalations) and routes them into evaluation pipelines, prompt optimization workflows, and retrieval quality assessments through defined cadences.

## THE TRAP (Expanded)

**The Eval-in-a-Vacuum Problem.** Teams build evaluation sets from synthetic data or internal examples. These evals pass. The product launches. Users encounter queries and contexts the eval never anticipated. The offline eval says 92% accuracy. Users experience 75%. The gap exists because the eval doesn't reflect real distribution.

**The Feedback Graveyard.** Many products collect thumbs-up/thumbs-down signals but never process them. The data sits in a logging table that nobody queries. The PM says "we collect feedback." The ML engineer says "I've never seen the feedback data." This is cargo-cult feedback collection.

**The Edit Goldmine.** When a user edits AI-generated text, the before/after pair is an incredibly rich signal. It tells you not just that the AI was wrong, but exactly how it was wrong and what the correct output should have been. Most products don't capture edits as structured data.

## INTELLECTUAL LINEAGE

- **Eugene Yan** — On LLM-as-judge evaluation and using user corrections as reference labels for automated eval.
- **Aman Khan** — On production ML observability and the difference between offline and online metrics.
- **RLHF as product design** — Reinforcement Learning from Human Feedback isn't just a training technique. It's a product design philosophy: the interface generates the feedback that improves the model.
- **Amazon's flywheel** — Bezos's virtuous cycle applied to AI: more users → more feedback → better AI → more users.

## REAL-WORLD EXAMPLES

**The editing flywheel (Amazon-scale loop).** A document AI tool captured every user edit to AI-generated drafts as structured data (before/after pairs + user ID + timestamp + document type). After 3 months: 50,000 before/after pairs. Quality analysis revealed three dominant patterns: (1) model over-used jargon (technical language in executive summaries), (2) paragraphs were too dense (model generated 400-word blocks where users preferred 100-150 words), (3) missed company-specific terminology (proprietary product names, internal nomenclature). Monthly: prompt improvements targeting these patterns. Quarterly: fine-tuned retrieval for terminology. Result: user acceptance rate 40% → 68% over 6 months. Competitive advantage: every day more users edit → more signal → better model → fewer edits → less user work. This is compounding advantage.

**The escalation signal (customer support).** A support AI tracked escalations to human agents as an implicit negative signal. Data: when users requested human handoff, what was the query? Analysis of 10,000 escalations revealed 60% came from three query categories: billing edge cases, feature request routing, and technical troubleshooting for specific products. Root cause: retrieval system lacked specialized knowledge for these categories (general knowledge base wasn't fine-grained enough). Intervention: built three specialized retrieval clusters for these query types. Result: escalation rate dropped 45% (10% → 5.5% overall, but 35% → 8% for those three categories). Measurement: tracked escalation rate weekly; escalation curve was smooth, predicting business impact in real time.

## FURTHER READING

- Eugene Yan, "LLM-as-Judge: Evaluating LLM Outputs" — Automated eval using human references
- Chris Olah & Anthropic, interpretability research — Understanding what models learn from feedback
- Jeff Bezos, "The Flywheel" — Compounding improvement cycles as competitive strategy
