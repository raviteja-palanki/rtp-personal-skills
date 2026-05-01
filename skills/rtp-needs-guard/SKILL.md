---
name: rtp-needs-guard
description: >
  Ensure AI deployment doesn't threaten what workers actually care about: feeling competent,
  having autonomy, and belonging. 31% of workers actively resist AI. 54% use unauthorized
  tools. These aren't skill gaps — they're signals that psychological needs are being violated.
  The AWARE framework diagnoses which need is broken. Use when designing AI change management,
  assessing worker resistance, or pre-deployment impact assessment.
imports: [first-principles, bias-spotter]
---

# Needs Guard

When AI gets implemented, workers resist. Not because they're afraid of change. Because something they depend on professionally is being removed.

> "You don't have an adoption problem. You have a need violation problem." — From 15 years of change management research applied to AI.

---

## Quick Reference: The Resistance Statistics

- **31% of workers actively resist AI** — Not because they lack training or skill. Because something that mattered to them professionally is being taken away.
- **54% use unauthorized AI tools** — They bypass your official deployment to use consumer tools. This is worker-driven shadow AI. It tells you your official system is not meeting their needs.
- **The 70/20/10 failure pattern** — 70% adoption in Month 1 → 50% by Month 3 (the dip) → 40-45% stable if nothing changes → 60%+ if you address the underlying need violation.

**What this means:** Resistance is not a change management problem. It's a product problem. You're shipping an AI tool that violates psychological needs. Your job is to diagnose which needs, then redesign to protect them.

---

## DEPTH DECISION

**Go deep if:** Workers are resisting AI, adoption is plateauing at Months 3-4, people are using unauthorized tools, or you're designing change management for AI adoption.

**Skim to diagnostic questions if:** You need a quick assessment of which psychological need is broken.

**Skip if:** You haven't yet selected which AI tools to deploy (use `ai-use-case-readiness` first).

---

## DELIVERABLE FORMAT

Before starting, ask:

> **What format would you like this assessment in?**
> 1. **Word Document** — Formatted report with embedded visuals. Best for sharing with stakeholders.
> 2. **Presentation** — Slide deck with key findings. Best for meetings and reviews.
> 3. **Both** — Full report + summary deck.
>
> *Default if no preference: Word Document.*

Follow the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md).

---

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md):
1. Ask the Grounding Questions — at minimum: Who are the workers? What AI system is being deployed? What's the resistance pattern you're seeing?
2. Route depth: Executive Summary or Comprehensive Analysis?
3. Identify output format: Document, presentation, or inline?

**Additional grounding for this skill:**

> **1. What's the resistance pattern?** Early adoption dip (Month 3-4)? Active workarounds? Refusing to use official tools? Complaining to HR?
>
> **2. What was the communication around this AI?** "This will make you more productive" vs "This will automate your job" vs "This is required by leadership"?
>
> **3. What happens when a worker uses the AI tool?** Does it help them do their job, or does it take something away (autonomy, expertise recognition, connection to the work)?
>
> **4. What do workers say when they resist?** Listen for: "I can't use this — I can't see what it's doing" (autonomy), "I don't trust it with my reputation" (competence), "This makes me feel replaceable" (belonging).

---

## THE TRAP

The mistake you're about to make: **Blaming the worker for resisting, when the AI system violates their psychological needs.**

Here's how it plays out. You roll out AI. Month 1: adoption surges (novelty). Month 3: adoption collapses (reality). You conclude: "Workers don't understand the technology" or "We didn't train them enough" or "This generation resists change."

None of that is true. What's actually happening: **The AI system is removing something the worker depends on to feel like a professional.**

The bias that drives this mistake is **fundamental attribution error** — attributing the problem to the person's character ("they resist change") instead of the system ("this system violates their competence need").

**The fix:** Run the AWARE diagnostic below. Diagnose which psychological need is being violated. Then redesign the AI deployment to protect that need. Adoption won't require propaganda or coercion — it will happen naturally because the tool stops threatening the worker.

---

## Self-Determination Theory Applied to AI

Before you run the diagnostic, understand what workers actually need. Self-Determination Theory says humans require three psychological needs to feel like professionals:

1. **Autonomy** — Control over your work and how you do it. When AI strips autonomy, workers feel like the system owns their work.
2. **Competence** — Feeling skillful and able to meet challenges. When AI hides how it reaches decisions, workers can't learn, can't defend their answers, can't improve.
3. **Relatedness** — Belonging to a team and being valued. When AI is positioned as a replacement ("this will replace 30% of support staff"), workers feel disposable.

**The research finding:** Systems that protect all three needs see 65%+ sustained adoption. Systems that violate even one need see 30-40% adoption by Month 6.

AI systems *can* protect all three. Most don't — because teams build for capability, not for need protection.

---

## THE PROCESS

### Step 1: Map the AI System's Touch Points

What does your AI system do? List every moment a worker interacts with it:

```
Example: Support ticket routing AI
- Worker sees: AI flagged this ticket as "return request" with 72% confidence
- Worker action: Review and route to Returns team
- System output: Worker's choice is logged; AI learns from it

Touch point 1: "I can see the AI's reasoning (72% confidence) but I can override it"
Touch point 2: "My override is valued — the system learns from my corrections"
Touch point 3: "I'm partnering with the AI, not replaced by it"
```

**What to document:**
- What information is visible to the worker?
- Where can the worker intervene or make a choice?
- What happens with the worker's input — is it ignored, logged, valued?

---

### Step 2: Run the AWARE Diagnostic

For each touch point, ask these five questions:

```
A — AUTONOMY: Does the worker control how they work, or does the AI dictate it?
     ✗ Red flag: "The AI decides, the worker executes" or "The worker must accept the AI's decision"
     ✓ Green flag: "Worker can override, modify, or choose the AI's output"

W — WORK IDENTITY: Is the AI positioned as replacing the worker, or assisting?
     ✗ Red flag: "This AI will handle 70% of tickets" or "This replaces manual review"
     ✓ Green flag: "This AI handles the routine cases; you focus on complex ones"

A — AFFILIATION: Does the worker belong to a team, or are they competing with the AI?
     ✗ Red flag: "We're measuring how many tickets the AI can handle without human review"
     ✓ Green flag: "We're measuring how well the worker + AI team solve tickets"

R — ROUTINE & EXPERTISE: Can the worker improve and learn, or does the AI hide its reasoning?
     ✗ Red flag: "The AI's decision is a black box" or "Workers can't explain the AI's output"
     ✓ Green flag: "Workers can see how the AI reasons and learn from its patterns"

E — EXPERTISE RECOGNITION: Is the worker's judgment still valued, or is the AI the authority?
     ✗ Red flag: "The AI's score is the decision; the worker just implements it"
     ✓ Green flag: "The worker's expertise is the decision; the AI's score is input"
```

**Score the diagnostic:**

For each dimension, mark it as:
- **Green** (need is protected)
- **Yellow** (need is at risk)
- **Red** (need is violated)

**The pattern that predicts adoption:**
- 5 Green → 65%+ sustained adoption
- 3-4 Green + 1-2 Yellow → 45-55% adoption with ongoing friction
- 2 Green + 2-3 Yellow → 30-40% adoption; workers use unauthorized tools
- 0-1 Green + 4+ Red → 10-20% adoption; active resistance

---

### Step 3: Identify the Dominant Need Violation

Usually one or two needs are driving the resistance. Here's how to spot which:

**If workers say:** "I don't understand why the AI flagged this" or "I can't explain the AI's output to the customer"
→ **Broken need: Competence.** Workers can't defend their decisions. They feel exposed.

**If workers say:** "The AI handles everything; I'm just clicking approve" or "I have no choice anymore"
→ **Broken need: Autonomy.** Workers feel like operators, not professionals.

**If workers say:** "This is going to replace me" or "My job is changing" (even if untrue)
→ **Broken need: Relatedness.** Workers feel disposable.

**If workers bypass the official AI and use unauthorized tools:**
→ **The official AI violates a need.** The unauthorized tool is their workaround to restore that need. This is critical data. Interview the workers using unauthorized tools. Ask: "What does the unauthorized tool let you do that the official one doesn't?" Their answer names the violated need.

---

### Step 4: Redesign to Protect the Need

Don't redesign the AI itself (yet). Redesign the *deployment and workflow* to protect the violated need:

**If Autonomy is violated:**
- Redesign: Give the worker explicit decision gates where they can override, modify, or reject the AI's output
- Test: "Can I change the AI's decision?" If no → autonomy is still violated
- Example: Instead of "AI routes ticket, worker implements" → "AI recommends route with reasoning, worker confirms or changes route, system learns from worker's choice"

**If Competence is violated:**
- Redesign: Make the AI's reasoning visible and learnable
- Test: "Can I explain why the AI made this decision to a colleague?" If no → competence is still violated
- Example: Instead of "AI returns a decision" → "AI returns decision + top 3 reasoning factors + links to similar past cases so worker can learn the pattern"

**If Relatedness is violated:**
- Redesign: Position the system as "worker + AI team," not "AI that replaces workers"
- Test: "Do I feel like my job is secure?" If no → relatedness is still violated
- Example: Instead of "We deployed AI to handle 50% of tickets" → "This frees your team from routine triage so you can focus on complex cases and mentoring. We're measuring success by 'cases solved with worker + AI' not 'cases solved by AI alone.'"

**If Routine/Expertise is violated:**
- Redesign: Ensure the system provides feedback loops where the worker can improve based on AI patterns
- Test: "Am I learning something new each week from using this system?" If no → improvement loop is broken
- Example: Instead of "AI decision is final" → "Weekly digest: Here are the most common error patterns the AI is catching. Here's how you can spot them before the AI does."

---

## DIAGNOSTIC QUESTIONS WITH ANSWER NUDGES

**Use these to assess your specific AI deployment:**

1. **Override power:** Can the worker override the AI's decision?
   - Red flag: "No, the AI's decision is final"
   - Yellow: "Yes, but it triggers an escalation and creates extra work"
   - Green: "Yes, easily, and the system learns from their override"

2. **Reasoning transparency:** Can a worker explain the AI's decision to someone else?
   - Red flag: "No, it's a black box"
   - Yellow: "Sort of — there's a confidence score but no reasoning"
   - Green: "Yes — the system shows reasoning factors and similar past cases"

3. **Position of expertise:** Who makes the final decision — the AI or the worker?
   - Red flag: "The AI. The worker just implements."
   - Yellow: "Both, but the AI's score is weighted higher"
   - Green: "The worker. The AI is input to their judgment."

4. **Feedback loop:** Do workers learn from the AI, or does the AI just operate?
   - Red flag: "Workers don't see feedback"
   - Yellow: "Workers see end-of-month statistics"
   - Green: "Workers get weekly feedback on their patterns and the AI's patterns"

5. **Job security framing:** What's the narrative about this AI's impact on jobs?
   - Red flag: "This will automate these tasks" or "This replaces manual work"
   - Yellow: "This will change some jobs" (true but scary)
   - Green: "This handles the routine work. You focus on complexity and judgment."

---

## REALITY CHECK

**Failure modes:**

- **Designing the deployment without worker input.** You run the AWARE diagnostic yourself, conclude "Autonomy is violated," redesign the workflow, then roll it out. Workers still resist because you diagnosed the *symptom*, not the actual lived experience. **Fix:** Interview 10-15 workers who are resisting or using unauthorized tools. Ask: "What's missing for you in the official system?" Their answers are more accurate than your diagnosis.

- **Assuming all workers have the same needs.** Senior staff might prioritize autonomy (they want to mentor and improve). Junior staff might prioritize competence (they want to learn and develop expertise). **Fix:** Segment your assessment. Do the AWARE diagnostic for different worker personas separately.

- **Mixing up "adoption" with "using the tool because we forced them to."** Month 1 adoption is deceptive. What matters is Month 6 adoption *when no one's watching*. If workers revert to manual processes when possible, adoption never happened — you just created compliance. **Fix:** Measure "voluntary adoption" (% of workers using the tool when they could choose not to) not just "deployment adoption" (% who have access).

- **One-time training won't fix a need violation.** Training helps when the problem is "workers don't understand the AI." Training fails when the problem is "the AI violates a need." **Fix:** Distinguish between capability problems (solved with training) and need problems (solved with redesign). A worker who understands the AI perfectly but feels replaced will still resist it.

---

## QUALITY GATE

- [ ] AWARE diagnostic completed for each major touch point
- [ ] Dominant need violation(s) identified by name
- [ ] Specific redesigns proposed to protect that need (not just "communicate better")
- [ ] Feedback loop for continuous improvement included
- [ ] Worker personas considered (not one-size-fits-all)
- [ ] Measurement metric aligned with adoption quality (voluntary use, not just access)

---

## WHEN WRONG

This skill gives bad advice if:

- **The resistance is not about violated needs.** Sometimes workers resist because they lack basic digital skills, the training was poor, or the system has genuine usability problems. Run the diagnostic, but also do user testing. If workers can't figure out how to use the system, that's a UX problem, not a needs problem.

- **The AI system is genuinely unsafe, and workers are right to resist.** If workers are resisting because the AI produces bad results and they'll face consequences, the issue is AI quality, not need protection. Use `eval-framework` to validate the AI's performance before redesigning the deployment.

- **The organization has already decided to automate away jobs.** If leadership's actual plan is "use AI to reduce headcount by 30%," then redesigning the deployment to "protect autonomy" is not going to move adoption. Workers can sense when the story ("You'll focus on complex work") doesn't match the reality ("We're sizing teams down 30%"). Fix the strategy first, then redesign the deployment.

---

## TRADE-OFF LEDGER

### Choosing to redesign the AI deployment to protect psychological needs:

**We are betting on:** That sustained adoption and discretionary effort from workers will increase when their psychological needs are protected.

**We are giving up:** Speed. Redesigning for need protection takes longer than "just roll it out and train people." You'll need to run worker interviews, redesign workflows, test multiple iterations, and validate with different personas. Add 2-3 weeks to your timeline.

**This is reversible within:** Deployment. If the redesigned deployment still doesn't drive adoption, you can revert to the original and run the diagnostic again to find which need is still violated.

**The hidden trade-off:** **Protecting psychological needs forces you to keep workers in the loop.** This means lower absolute automation ("AI handles 50% of cases" becomes "AI handles 70% but workers have override") but higher quality ("Worker + AI collaborate" beats "AI alone"). Your metrics will change. If you're measuring "AI case throughput," protecting needs will reduce that number. If you're measuring "case quality and worker learning," it will increase.

**Confidence: High**
- Evidence: 15+ years of change management research, Self-Determination Theory validation, organizational psychology studies
- What would change our mind: A well-executed AI deployment that violates all AWARE dimensions but achieves 60%+ voluntary adoption anyway

---

## CONCLUSION

**The recommendation:** Before you measure adoption or blame workers for resistance, run the AWARE diagnostic. Diagnose which psychological need (Autonomy, Work identity, Affiliation, Routine/expertise, Expertise recognition) is being violated. Then redesign the deployment to protect that need — not because it's nice, but because adoption that's not sustained is not adoption.

**The hypothesis:** We believe workers will voluntarily adopt and discretionally engage with AI systems when those systems protect their psychological needs for autonomy, competence, and belonging. We'd know we're wrong if a well-designed deployment (AWARE: 4-5 Green) still sees adoption dip by Month 3, suggesting other factors are at play.

**The biggest risk:** You run the diagnostic, identify the violated need, redesign the deployment, and adoption still doesn't improve. This signals one of two things: (1) Your diagnosis was wrong — dig deeper with worker interviews; (2) The violated need is so fundamental (e.g., "this genuinely automates my job away") that redesign can't fix it. In that case, the problem is strategy, not deployment.

**Assumptions to watch:**
- Workers can articulate what they need (often they can't — you need to infer from behavior)
- The violated need is the same across all worker segments (usually it's not)
- Redesigning deployment is sufficient without addressing model quality and reliability (it's not)

**The next action:** Interview 10-15 workers who are resisting or using unauthorized tools. Ask: "What's missing for you in the official system?" Map their answers to AWARE dimensions. Then redesign the deployment based on that evidence.

---

## GENERATE THE DELIVERABLE

Use the output prompt from the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md).

If workers are experiencing need violations that stem from broader job-change dynamics, generate a markdown handoff file for the `adoption-launch` skill so it can design phase-specific support that protects needs across the adoption curve.

---

## VISUAL SUMMARY

After completing this analysis, invoke the `excalidraw-svg` skill to create:
1. **AWARE Framework Visualization** — 5 dimensions as radar chart showing Green/Yellow/Red for your deployment
2. **Psychological Needs Model** — How Autonomy, Competence, Relatedness connect to adoption patterns
3. **Redesign Pathway** — Workflow before/after showing need protection
