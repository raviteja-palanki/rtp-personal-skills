# Alignment Check — Concept Guide

## FIRST PRINCIPLES

93% of AI failures are organizational, not technical. This is the foundational insight that drives this skill.

The mechanism: A technology problem creates one failure mode (the model doesn't work). An organizational misalignment creates cascading failures. Teams succeed or fail based on whether five structural links hold together:

Purpose → Strategy → Capability → Architecture → Systems

If any link breaks, the deployment fails. The most insidious failures are the ones where the first four links are strong but the fifth (Systems) breaks — the team builds the right thing, manages adoption well, but then has no monitoring or feedback loops. The model degrades silently. Users lose trust without anyone knowing why. The investment compounds backward.

## DUAL DEFINITION

**Business definition:** Alignment-check is a diagnostic framework that identifies which of the five links (Purpose → Strategy → Capability → Architecture → Systems) is the constraint, preventing unnecessary technical spending when the constraint is organizational.

**Technical definition:** A cascading assessment that maps stakeholder understanding, strategic positioning, skill distribution, technical architecture decisions, and operational readiness — identifying the weakest link and the failure mode it would produce.

## THE 5-LINK CHAIN (Expanded)

### Why These Five?

Every successful AI deployment requires:
1. **Purpose:** A shared understanding of what problem the AI solves (executive clarity)
2. **Strategy:** A competitive and financial thesis for how AI fits into the business (business model clarity)
3. **Capability:** The right mix of technical and organizational skills to build and run the AI (human capital clarity)
4. **Architecture:** Technical design that's built for the actual business problem and includes failure handling (technical correctness)
5. **Systems:** Operational processes that keep the AI working over time (sustainability)

You could add more (governance, compliance, culture). But these five are irreducible — if any one breaks, the deployment fails.

### Why Organizational Misalignment Dominates

The data:
- Gartner: "90% of enterprise AI projects fail to progress past the pilot stage"
- McKinsey: "Most AI initiatives fail because of organizational, not technical, issues"
- BCG: "Only 8% of companies report running large-scale AI initiatives successfully"

The organizational factors cited: misalignment on strategy, lack of accountability, insufficient change management, unclear ROI thesis, competing priorities.

## THE TRAP (Expanded)

**Availability heuristic:** You can see the technology problem (need better models, more data, faster inference). You can't see the organizational problem because it's abstract (misalignment, unclear purpose, diffused accountability). So you solve the visible problem and miss the invisible constraint.

**Real example:** A financial services firm spent $2M on an AI model for credit underwriting. The model was technically brilliant — 94% accuracy, SOTA architecture, state-of-the-art monitoring. But adoption stalled because:
- The underwriters didn't trust it (Purpose broken — nobody had explained why the model was necessary)
- The compensation model hadn't changed, so underwriters saw it as a threat (Strategy broken — business model didn't work)
- The compliance team wasn't involved in design, so they blocked deployment mid-process (Architecture broken — compliance wasn't a design constraint)

The team's instinct: "We need a better model." Wrong diagnosis. The model was fine. The organization wasn't ready.

## INTELLECTUAL LINEAGE

- **Ronald Heifetz** — *Leadership Without Easy Answers.* The distinction between technical problems and adaptive challenges. Here applied to AI deployments.
- **Peter Senge** — *The Fifth Discipline.* Organizational systems thinking. Why individual excellence doesn't guarantee organizational success.
- **Jim Collins** — *Good to Great.* The importance of alignment on "what we're best at" before scaling.
- **Clayton Christensen** — *The Innovator's Dilemma.* How organizational incentives (not technology) determine whether innovations succeed or fail.
- **Donella Meadows** — *Thinking in Systems.* Why changing one variable in a system doesn't create expected outcomes if upstream variables are unaligned.

## REAL-WORLD EXAMPLES

**Example 1: The pilot that couldn't scale.** A healthcare company built an AI model to predict patient readmissions. Pilot results: 87% accuracy, doctors loved it. Scale attempt: adoption was 12% at month 3. Why? The pilot was in one department with a supportive leader. At scale, other departments saw it as a threat to their autonomy. Capability broken (no change management). Strategy broken (the business model didn't account for department-level incentives).

**Example 2: The beautiful architecture that nobody used.** A retail company invested in an agent system for inventory management. Technically exceptional. Monitoring was flawless. But operations teams kept overriding the AI and using manual processes instead. Why? The AI was designed by product people, not operations people. No one in operations felt ownership. Purpose broken (operations teams didn't understand why this AI existed or how it would help their lives).

**Example 3: The model that degraded and nobody noticed.** An e-commerce company deployed an AI recommendation engine. Month 1: 30% CTR improvement. Month 6: CTR back to baseline. Month 12: CTR 5% below baseline. Why? No retraining process. The model drifted with seasonal changes and user behavior shifts. Systems broken (no monitoring or feedback loops).

## PRODUCTION DISCIPLINE

**When to use this skill:**
- Pre-investment (before spending $1M+ on AI)
- Pre-implementation (when transitioning from pilot to production)
- Post-failure (when a deployed AI isn't delivering value)
- During hiring (when joining a company with AI initiatives)

**When NOT to use this skill:**
- Early-stage exploratory work (pilot phase doesn't need full alignment)
- Low-stakes decisions with reversible consequences
- When the organization is already aligned and executing well

**The timing question:** Diagnose early. A 1-week alignment check during problem definition can save 3 months of building in the wrong direction.

**Red flags that alignment is being skipped:**
- "Let's just build it and see what happens"
- Pilot succeeded but nobody's talking about how it scales
- Different stakeholders describe the AI's purpose differently
- Technology is approved but go-to-market strategy is unclear
- The AI is technically perfect but adoption is low

## FURTHER READING

- Ronald Heifetz, *Leadership Without Easy Answers* — On distinguishing technical problems from adaptive challenges
- Peter Senge, *The Fifth Discipline* — Systems thinking applied to organizations
- Jim Collins, *Good to Great* — Alignment on competitive positioning
- Donella Meadows, *Thinking in Systems* — Why changing one lever doesn't work if the whole system isn't aligned
- O'Reilly, *AI Engineering* (various authors) — Real-world case studies of AI deployments that failed and why
