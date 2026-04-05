# Problem Type — Concept Guide

## FIRST PRINCIPLES

Not all problems are the same kind of problem. The framework for solving a technical problem (identify constraint, apply expertise, solve) doesn't work for adaptive challenges (where people must change their beliefs or behaviors).

The atomic insight: **Most AI failures happen because teams treat adaptive challenges like technical problems.** The team keeps building better solutions to a problem that isn't technical. Each solution fails. Frustration builds. The team concludes "this is hard" when the real issue is "we're solving the wrong problem."

The mechanism: A technical problem has a solution the team can discover. Build it. Deploy it. Works. An adaptive challenge requires people to change. You can't delegate that to engineers. You can only enable it.

When teams confuse technical and adaptive:
- They spend engineering effort on something that requires organizational change
- They build solutions that work technically but don't get adopted
- They keep iterating on the solution when the problem is actually in the environment
- The solution fails, trust erodes, and when the real (adaptive) problem is finally tackled, people are cynical

## DUAL DEFINITION

**Business definition:** Problem-type is a diagnostic framework that distinguishes technical problems (solvable by expertise) from adaptive challenges (solvable by learning and behavior change), and sequences the work accordingly.

**Technical definition:** A five-signal assessment (recurrence, cycling, barrier explicitness, authority effectiveness, solution obviousness) that classifies problems and produces a sequencing strategy for technical + adaptive work when both are present.

## THE HEIFETZ FRAMEWORK (Expanded)

Ron Heifetz's work at Harvard Kennedy School distinguishes:

### Technical Problem
- The problem is clear
- A solution exists (or can be designed)
- Implementation is straightforward
- Authority figures can solve it
- Once solved, it stays solved
- Examples: Database is slow. Algorithm has high error rate. Model latency is too high.

**The leadership move:** Identify the problem, bring in the expert, deploy the solution.

### Adaptive Challenge
- The problem is clear, but the solution is not known
- People must change their beliefs or behaviors
- Authority cannot solve it (cannot delegate to experts)
- Resistance is significant
- The work is political and emotional
- Examples: Sales reps don't trust AI. Hiring team can't let AI pick candidates. Customer support engineers see AI as a threat.

**The leadership move:** Identify the direction, create space for people to work through it, stay visible and accountable.

The confusion happens because both types of problems can feel urgent and both require resources. But the solution approach is fundamentally different.

## THE DANGEROUS MIDDLE: BOTH

Most real AI problems are BOTH technical and adaptive. The question isn't "which one is it?" but "what's the right sequencing?"

**Example: AI model is making biased recommendations**

Technical component: The model learns biased patterns from training data. Fix: better training data, fairness constraints, retrain.

Adaptive component: The organization hasn't agreed on what "fair" means in this context. Different stakeholders have different definitions. Fix: conversation, alignment, shared definition.

Wrong sequencing: Build a more fair model → deploy → discover stakeholders disagree → conflict → rollback

Right sequencing: Have the adaptive conversation → build a model that reflects shared understanding → deploy → fewer conflicts

## INTELLECTUAL LINEAGE

- **Ron Heifetz** — *Leadership Without Easy Answers.* The foundational framework for distinguishing technical and adaptive.
- **Donald Schon** — *The Reflective Practitioner.* On learning through uncertainty. Adaptive challenges require "reflection-in-action."
- **Peter Senge** — *The Fifth Discipline.* How organizations learn. Technical learning is product-focused; adaptive learning is process-focused.
- **Brene Brown** — *Dare to Lead.* On vulnerability in leadership. Adaptive challenges require admitting "we don't know" and learning together.
- **Amy Edmondson** — *The Fearless Organization.* Psychological safety is required for adaptive work.

## REAL-WORLD EXAMPLES

**Example 1: The recommendation engine that didn't get adopted.** A team built an e-commerce recommendation system. Metrics: 92% accuracy, 15% CTR improvement in tests. Real adoption: 8%. The team's response: build a better algorithm. Version 2: 95% accuracy, 18% CTR. Adoption: 10%. Why?

Technical issue: No. The system works.

Adaptive issue: Merchants didn't trust the AI. They believed the recommendations were cannibalizing their high-margin products. The merchants had incentives misaligned with the platform's goal. The team was solving the wrong problem.

Right answer: First, address the incentive structure. Show merchants how recommendations could increase their category sales. Start with opt-in pilots. Build trust. THEN deploy the technical system.

**Example 2: The data pipeline that kept breaking.** A team built a data infrastructure to support model training. Month 1: Works. Month 2: Data engineers are manually fixing pipeline failures every other day. Month 3: Still breaking regularly. The team's response: build a more robust pipeline.

Technical issue: Maybe. The pipeline architecture could be more resilient.

Adaptive issue: The organization doesn't have a shared understanding of data quality standards. The teams providing data aren't trained on why quality matters. There's no incentive for data providers to report issues. The team was solving infrastructure when the problem was organizational.

Right answer: First, establish shared data quality standards and incentives. Train teams on data responsibility. THEN build more robust infrastructure.

**Example 3: The AI hiring tool that created legal risk.** A company deployed an AI system to screen resumes. Metrics: 40% reduction in time-to-hire. Adoption: 100% (mandate from HR). Outcome: Legal team discovered systematic bias against candidates from non-target schools. The system had to be dismantled.

Technical issue: Yes, the model had bias.

Adaptive issue: The organization didn't involve legal, compliance, or D&I in the design. Nobody had conversation about what "fair" means before building. The mandate to use the system created fake adoption (people used it, but didn't believe in it, so they didn't scrutinize it).

Right answer: First, the adaptive work (involve stakeholders, define fair, build trust in the approach). THEN build the technical system with informed constraints. THEN deploy with actual adoption, not just compliance.

## PRODUCTION DISCIPLINE

**When to diagnose problem type:**
- Same problem keeps recurring despite multiple fixes
- A feature is technically perfect but adoption is failing
- Leadership says "just build it" but something feels off
- A project keeps stalling

**When NOT to diagnose:**
- Problem is clearly technical (database query timing)
- Problem is clearly adaptive (organizational structure doesn't make sense)
- Timing is compressed and analysis would delay action

**Red flags that a problem is adaptive, not technical:**
- The fix you tried didn't work, so you tried again
- Different stakeholders describe the problem differently
- People keep reverting to the old way
- Adoption metrics don't match technical capability metrics
- Mandate increases compliance but not belief

**The sequencing decision:** If both technical and adaptive, which comes first?
- Usually: Adaptive work first, because it defines the constraints for technical work
- Exception: If the adaptive work depends on seeing the technical solution first (e.g., "let me see what the AI can do before I decide if I trust it")
- Can they run in parallel? Sometimes, but make sure they're coordinated

## FURTHER READING

- Ronald Heifetz, *Leadership Without Easy Answers* — The foundational framework
- Donald Schon, *The Reflective Practitioner* — On learning through uncertainty
- Peter Senge, *The Fifth Discipline* — Organizational learning
- Brene Brown, *Dare to Lead* — On vulnerability in leadership
- Amy Edmondson, *The Fearless Organization* — Psychological safety and risk-taking
