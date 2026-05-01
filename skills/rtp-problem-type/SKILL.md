---
name: rtp-problem-type
description: >
  Figure out if you're facing a technical problem (clear solution, known path) or an adaptive challenge (unclear solution, requires people to change). Most AI failures happen because teams treat adaptive challenges like technical problems — they keep "solving" something that requires organizational change, not a better algorithm. Use when the same problem recurs despite fixes, leadership says "just build it" but the barrier is organizational, a feature is technically perfect but adoption is failing, or when you notice the pattern "we tried everything and it didn't work." Do NOT use to avoid difficult decisions or to justify doing nothing — often the right move is both technical AND adaptive work, sequenced carefully.
imports: []
---

# Problem Type

## DEPTH DECISION

**Go deep if:** Same problem recurring despite multiple "solutions", adoption failures despite technical correctness, or diagnosing why a project keeps stalling. **Skim to questions if:** Quick classification during problem definition. **Skip if:** Problem is clearly technical (database query is slow) or clearly adaptive (organizational structure doesn't make sense).

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md):
1. Ask the Grounding Questions (Section 1) — at minimum: What's the actual problem statement? Who's affected? What have we already tried?
2. Route depth: Are you diagnosing a stuck initiative (Comprehensive) or classifying a new problem (Executive Summary)?
3. Identify output format: Word Document, Presentation, or Both?

Then proceed with the skill-specific analysis below.

## DELIVERABLE FORMAT

Before starting, ask for format: Word Document, Presentation, or Both.
Follow the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md).

## THE TRAP

You will default to technical solutions. The bias is **sunk cost + action bias** — building something feels productive while organizational change feels slow. When a technical solution fails, the instinct is to build a better technical solution, not to ask "is this a technical problem at all?"

The trap is most seductive because:
- Technical problems feel solvable (hire better engineers, better algorithms, more data)
- Adaptive challenges feel messy (change how people think, organizational resistance, political)
- Measuring technical progress is clean (better metrics, faster inference, higher accuracy)
- Measuring adaptive change is ambiguous (did hearts and minds actually change, or did people just comply?)
- Adaptive work is slower — it takes 6-12 months to change how people approach a problem

Here's the mechanism: A technical problem has a solution the team can discover. Build it. Deploy it. Done. An adaptive challenge requires people to change their behavior or beliefs. You can't delegate that to engineers. You can only enable it.

**Classic example:** Sales reps aren't using the AI recommendation engine. The technical team builds a better model (higher accuracy). Adoption doesn't improve. The team builds more features. Still nothing. What if the real problem is that reps don't trust the AI because it once made a recommendation that embarrassed them in front of a customer? That's adaptive — it requires rebuilding trust, not rebuilding the model.

## THE HEIFETZ FRAMEWORK

Ron Heifetz (Harvard Kennedy School) distinguishes technical problems from adaptive challenges:

### Technical Problem
- The solution exists or can be designed by experts
- Implementation is straightforward (once the solution is known)
- Resistance is minimal (people generally want the solution)
- Can be solved by the people currently in charge
- Authority figures solve it
- Examples: Database is slow → optimize the query. Algorithm has high error rate → better training data. API latency is too high → caching layer.

**Pattern:** Problem → Expert diagnoses → Solution deployed → Problem solved

### Adaptive Challenge
- The solution is not known in advance; it must be discovered through learning
- Implementation requires people to change behavior or beliefs
- Resistance is significant (people must give up old ways, even if better ones exist)
- Can only be solved by people working through it together (not delegated to experts)
- Requires leadership to model the change, not just authorize it
- Examples: Sales team doesn't trust AI → requires building credibility through transparency. Hiring team can't let AI recommend candidates → requires changing hiring beliefs. Support engineers see AI as a threat → requires showing how AI amplifies their expertise, not replaces it.

**Pattern:** Problem → No obvious solution → Leadership articulates the direction → People work through it together over time → New behavior emerges

## THE 5 DIAGNOSTIC SIGNALS

To distinguish technical from adaptive, look for these signals:

### Signal 1: HAS THE SAME PROBLEM RECURRED DESPITE FIXES?

**Technical problem:** When you fix it, it stays fixed. You optimize the database query, and it's fast forever (until data volume changes and you optimize again).

**Adaptive challenge:** The problem recurs even after technical fixes. This is the canary in the coal mine.

**Red flag example:** "We built an AI model with 95% accuracy. Adoption was still low. We built a better model with 97% accuracy. Adoption is still low. We improved to 99% accuracy. Adoption is still low."

This is not a technical problem. Every technical fix works and solves the problem. If you keep fixing it and the problem keeps coming back, the problem isn't what you think it is.

### Signal 2: ARE YOU BUILDING THE SAME SOLUTION TWICE?

**Technical problem:** Once solved, you don't rebuild it. You might optimize it, but you don't start from scratch.

**Adaptive challenge:** You're cycling through solutions. "Let's try a different algorithm. Let's try a different deployment approach. Let's try different features. Let's try a different UI."

**Red flag example:** "We tried a recommendation engine. Low adoption. We switched to a chatbot interface. Low adoption. We switched to email recommendations. Low adoption."

This is not a technical problem. Every technical approach is failing. The problem isn't the technique — it's something about how people relate to the solution.

### Signal 3: IS THE BARRIER EXPLICIT OR IMPLICIT?

**Technical problem:** Barrier is explicit. "The query takes 5 seconds and our SLA is 2 seconds." Clear, measurable, objective.

**Adaptive challenge:** Barrier is implicit. "We're not sure why people aren't adopting it. They have access to it, but they don't use it." Or: "The CFO says no to the investment, but won't say why." Or: "The team knows they should do this differently, but keep reverting to the old way."

**Red flag example:** "The AI recommendations are better than what sales reps choose. Usage is still low. We don't know why."

When the barrier is invisible, you're in adaptive territory.

### Signal 4: DOES AUTHORITY SOLVE IT, OR ONLY ENABLE IT?

**Technical problem:** Authority can solve it. "CEO says: optimize the database." Done. Engineers work on it, problem is solved.

**Adaptive challenge:** Authority can only enable it. "CEO says: we need to trust the AI recommendations." If people don't internalize this, mandating it creates compliance, not belief. Sales reps use the AI tool because they're told to, but they still don't trust it. The mandate doesn't solve the adaptive challenge.

**Red flag example:** "Leadership said we have to use the AI. Adoption increased from 10% to 40%, but it plateaued. People are complying, not believing."

### Signal 5: IS THE SOLUTION OBVIOUS BUT NOT IMPLEMENTED, OR IS THE SOLUTION UNCLEAR?

**Technical problem:** Once you understand it, the solution is clear. "We need to index this column." "We need more training data." Everyone agrees on what to do.

**Adaptive challenge:** The solution is not obvious. Even smart people disagree. "Should we trust AI recommendations?" has no technical answer. People have different risk appetites, different experiences with AI, different incentive structures.

**Red flag example:** "We've talked about whether to use AI for hiring decisions for 6 months. Smart people on the team still disagree on whether it's even a good idea. We're not disagreeing on implementation — we're disagreeing on the fundamentals."

## WHEN PROBLEMS ARE BOTH (THE DANGEROUS MIDDLE)

Most real AI problems are BOTH technical and adaptive. The framework isn't "which one is it?" but "what's the sequencing?"

**Example: "AI model is making biased recommendations"**

- **Technical component:** The model learns from biased training data. Solution: collect better data, add fairness constraints, retrain. This is solvable.
- **Adaptive component:** The organization hasn't agreed on what "fair" means for this context. Different stakeholders have different definitions. This requires conversation.

**Wrong sequencing (fails):**
1. Build a more fair model
2. Deploy it
3. Conflict erupts because stakeholders didn't agree on the definition of fairness
4. Model gets reverted

**Right sequencing (works):**
1. Have the adaptive conversation: what does fairness mean to us? (6 weeks, hard conversation, no final agreement but shared understanding)
2. Build a model that reflects that shared understanding
3. Deploy it
4. Conflicts are reduced because people co-created the definition

## THE PROCESS

1. **State the problem in one sentence, without saying "solve".**
   Example: "Sales reps have low adoption of the AI recommendation engine"

2. **For each of the 5 signals, mark as technical or adaptive.**
   - Signal 1 (recurrence): Has this problem come back despite fixes? → This signal pulls toward [adaptive or technical]
   - Signal 2 (cycling): Are we trying different solutions repeatedly? → [adaptive or technical]
   - Signal 3 (barrier): Is the barrier explicit or implicit? → [adaptive or technical]
   - Signal 4 (authority): Does the CEO ordering it solve it? → [adaptive or technical]
   - Signal 5 (solution): Is the solution obvious or debated? → [adaptive or technical]

3. **Count the votes.** If 3+ signals point to adaptive, it's adaptive. If 3+ point to technical, it's technical. If split, it's both.

4. **If both, sequence the work.**
   - Does the adaptive work unlock the technical work? (usually yes — define the goal before building the solution)
   - Can they happen in parallel? (sometimes)
   - If parallel, which has longer lead time? (start that one first)

5. **For technical problems, define the solution and estimate effort.**
   For adaptive challenges, define the change and the leadership approach.

## DIAGNOSTIC QUESTIONS

1. **When did this problem first appear, and what have we tried to fix it?**
   - If: Same fix tried 3+ times with 0 success → Adaptive
   - If: Different fixes, all technical, none working → Adaptive
   - If: Fix deployed and worked → Technical
   - Spectrum anchor: "Tried once, worked" → "Tried 5+ times, keeps recurring"

2. **If we removed the people (replaced team) and kept the process/tech, would the problem disappear?**
   - If: Yes, problem was people-dependent → Adaptive
   - If: No, problem is structural → Technical
   - Spectrum anchor: "Process is the constraint" → "People/beliefs are the constraint"

3. **What's the most honest answer to 'why isn't this solved yet?'**
   - If: "We don't know how" or "We can't agree on what to do" → Adaptive
   - If: "It requires 3 weeks of engineering" or "We need more data" → Technical
   - Spectrum anchor: "Political/belief disagreement" → "Clear technical barrier"

4. **If you gave the smartest person in your company unlimited budget and 6 weeks, could they solve it?**
   - If: Yes → Technical. If no because of organizational barriers → Adaptive.
   - If: No, even with unlimited resources → Likely both, but check if you're missing something
   - Spectrum anchor: "Yes, just throw resources at it" → "No, it's not a resource problem"

5. **What would success look like if the problem is adaptive vs technical?**
   - Adaptive success: "People have changed how they think about [X]" or "People choose [Y] because they believe it"
   - Technical success: "The metric moved from [X] to [Y]" or "The constraint was removed"
   - If you can't define adaptive success (because the organization hasn't agreed on values), that's a sign it's adaptive
   - Spectrum anchor: "Measured by metrics" → "Measured by beliefs/behavior change"

6. **When was the last time someone questioned whether this problem should exist at all?**
   - If: Recently, and people had different answers → Adaptive (lack of shared purpose)
   - If: Nobody questions it, just the solution → Technical (purpose is clear)
   - If: People keep questioning it and it's slowing you down → Adaptive, needs resolution
   - Spectrum anchor: "Shared purpose" → "Disputed purpose"

## REALITY CHECK

- **Failure mode of this skill:** Using it to avoid hard decisions. "This is an adaptive challenge, so we need to wait." No — you need to work both. Often the answer is "do the adaptive work and the technical work in parallel, but sequence them so adaptive unlocks technical."
- **Most common mistake:** Treating all organizational resistance as adaptive. Sometimes the barrier is just poor communication (technical) or bad change management (you did the change right, but told people badly).
- **Hidden cost of getting it wrong:** If you treat adaptive as technical, you'll build better and better solutions that don't get used. Waste of engineering. If you treat technical as adaptive, you'll have alignment meetings while the database is on fire.
- **When to act fast:** If it's technical, solve it immediately. If it's adaptive, start the work immediately but recognize it takes longer. The worst case is treating it as technical and discovering 6 weeks in that it's adaptive.

## QUALITY GATE

- [ ] Problem stated clearly (not the solution, the problem)
- [ ] All 5 signals analyzed (not all have to be conclusive)
- [ ] Primary classification made (technical, adaptive, or both)
- [ ] If both: sequencing is clear (which comes first, can they be parallel?)
- [ ] For technical: solution and effort estimate defined
- [ ] For adaptive: the belief/behavior change is articulated, and the leadership approach is sketched
- [ ] Next action is specified (start technical work, start adaptive conversation, or both)

## WORKED EXAMPLE: "AI FEATURE ISN'T GETTING ADOPTED"

**Problem:** "Sales reps have adopted the AI recommendation engine at 15% when we expected 60%."

**Signal 1 (recurrence):** We've built 3 versions of the model. Accuracy improved from 80% to 96%. Adoption is still 15%. → Adaptive signal

**Signal 2 (cycling):** We tried a sidebar widget, then a chat interface, then email summaries. All technically good. All low adoption. → Adaptive signal

**Signal 3 (barrier):** Barrier is implicit. "People don't use it" but why? Unclear. → Adaptive signal

**Signal 4 (authority):** Sales VP said "use the AI." Adoption went from 5% to 15%. But it plateaued. → Adaptive signal (mandate increased compliance, not belief)

**Signal 5 (solution):** We disagree on what the solution is. Engineers think it's a UI problem. Sales thinks it's that reps don't trust the AI. Product thinks it's a workflow problem. → Adaptive signal

**Diagnosis:** 5/5 signals → Adaptive challenge.

**The real problem:** Sales reps think the AI will pick candidates they wouldn't pick, and they'll lose commission if the rep doesn't build relationships. Or: "The AI picked a candidate once who turned out to be a bad hire, so now I don't trust it." Or: "Using AI feels like admitting I don't know my job."

**What won't work:**
- Better model (technical fix to adaptive problem)
- Mandate ("you have to use it")
- Better UI (technical fix to adaptive problem)

**What will work:**
- Understand the real fear (6-week listening + research)
- Show how AI amplifies the rep's job, not replaces it (positioning change)
- Create a "fast track" where early adopters opt in and prove the AI works (builds credibility)
- Celebrate reps who override the AI and are right (show that human judgment is still valued)
- After 6 months of this work, the technical improvements (better model, better UI) will land differently because the adaptive groundwork has been done

---

## TRADE-OFF LEDGER

BY CHOOSING to diagnose technical vs adaptive:
  We are betting on: that misclassifying the problem type is more expensive than taking time to diagnose
  We are giving up: 1-2 weeks of immediate technical "solutions" that will likely fail
  This is reversible within: 1 week (if diagnosis is wrong, course-correct quickly)

THE HIDDEN TRADE-OFF:
  If it's adaptive and you treat it as technical, you'll spend engineering effort that won't compound. Worse, failed technical solutions erode trust. "We tried better algorithms and nothing worked" means people trust the AI even less. Better to diagnose early.

CONFIDENCE: High
  What would change our mind: If the problem is already clearly technical (database query timing) or clearly adaptive (organizational structure disagreement), skip the diagnosis and act

---

## CONCLUSION

Follow the Conclusion Protocol from the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md), Section 6:
1. State the classification (technical, adaptive, or both with sequencing)
2. Name the key trade-off (speed of technical solutions vs correctness of diagnosis)
3. Acknowledge the biggest risk (misdiagnosis, or over-analyzing when action is needed)
4. Define the next action (technical work owner, adaptive work sponsor, decision point)

---

## VISUAL SUMMARY

After completing the primary output, invoke the **excalidraw-svg** skill to create a single Excalidraw SVG visual summary. This diagram should show the 5 signals (recurrence, cycling, barrier, authority, solution) as a spectrum from technical to adaptive, the problem plotted on that spectrum, and if both, the sequencing/timeline showing which work happens when. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.
