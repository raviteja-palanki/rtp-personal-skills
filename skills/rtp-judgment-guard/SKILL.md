---
name: rtp-judgment-guard
description: >
  Prevent your team from losing the ability to think for themselves as they rely more on AI. Without designed friction, people accept AI outputs without engaging their own judgment. Over 6-18 months, expertise atrophies silently. This skill designs checkpoints that keep humans sharp. Use when deploying high-stakes AI (medical, financial, hiring decisions), designing AI-augmented workflows, noticing that users aren't questioning AI outputs anymore, or after observing expertise degradation in teams using automation. Do NOT use for low-stakes decisions where acceptance is fine, or when human expertise is already gone (you can't rebuild judgment instantly).
imports: []
---

# Judgment Guard

## DEPTH DECISION

**Go deep if:** Designing a high-stakes workflow, noticing skill erosion, or rolling out AI to a team with deep domain expertise. **Skim to questions if:** Quick audit of whether checkpoints exist. **Skip if:** Low-stakes decisions where acceptance is intentional and beneficial.

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md):
1. Ask the Grounding Questions (Section 1) — at minimum: What expertise is at risk? What's the cost of that expertise degrading? How will users know they're losing judgment?
2. Route depth: Are you building a new system (Comprehensive) or auditing an existing one (Executive Summary)?
3. Identify output format: Word Document, Presentation, or Both?

Then proceed with the skill-specific analysis below.

## DELIVERABLE FORMAT

Before starting, ask for format: Word Document, Presentation, or Both.
Follow the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md).

## THE TRAP

You will celebrate adoption. The bias is **sunk cost + success illusion** — teams feel good about automation metrics ("90% of tickets routed by AI!") while missing the invisible cost. Expertise doesn't atrophy visibly. It erodes in 6-month increments. By the time you notice, the expert radiologist can't read an X-ray without the AI's assistance. The veteran underwriter has forgotten how to spot fraud patterns. The customer success manager doesn't trust their own judgment anymore.

The trap is most seductive because:
- Adoption metrics feel like success (they're not)
- The atrophy is silent (no alarm bells)
- Restoring judgment takes 2-3x longer than it took to lose it
- It feels like a technology problem (blame the AI) when it's a design problem (you didn't build checkpoints)

Here's the mechanism: Humans are adaptive. When a tool is 90% accurate, people stop paying attention to the 10% of cases where it fails. Their mind stops working through the problem. At month 6, they don't notice they've stopped thinking. At month 12, the AI breaks and they can't work without it. At month 18, they can't restore judgment because the neural pathways have atrophied — they've forgotten the heuristics, the edge cases, the intuitions.

The timeline is predictable:
- **Month 0-3:** Adoption. People use the AI, catch the 10% of failures, learn edge cases
- **Month 4-6:** Complacency. People stop catching failures. "The AI usually works." Exceptions start sliding through
- **Month 7-12:** Delegation. People are managing exceptions, not judging whether the AI is right. "The AI said so" becomes authority
- **Month 13-18:** Dependency. People can't make the judgment without the AI. The expert is now a manager of exceptions, not a practitioner

### The Cost

If this expertise matters (medical diagnosis, underwriting, hiring decisions), re-building judgment after 18 months of atrophy requires:
- Expensive retraining (3-6 months)
- Supervised practice (another 3 months)
- Confidence restoration (another 3 months)
- Total: 9-15 months to get back to pre-AI capability

And that's if the person hasn't left (many do, when they feel their expertise was devalued).

## THE 4 CHECKPOINTS

To prevent judgment atrophy, design deliberate friction. These aren't "slow down the AI" — they're "keep the human sharp."

### Checkpoint 1: ROTATION

**The principle:** No one should use the same AI tool for more than 80% of their decisions for more than 4 weeks straight.

**How it works:** Rotate specialists in and out of AI-augmented tasks. A radiologist reads 30% of scans unassisted, 30% with AI assistance, 40% as a peer reviewer of the AI's previous reads. Every 4 weeks, rotate the roles.

**Why it works:** Rotation maintains two decision pathways. The human mind stays engaged in the unassisted work. The peer review catches when the AI is drifting.

**Implementation:**
- Map the decision tasks (this AI handles 70% of triage, human handles 30%)
- Rotate every 4 weeks (not every day — rotating too fast creates chaos and people resent it)
- Make sure each person has at least 20% of their time in "unassisted" work
- Track accuracy of rotated personnel: if someone falls behind during their "human only" month, that's a signal judgment has eroded

**Red flag:** "We can't rotate. Someone is too busy." This means the AI has reached 100% adoption and created permanent dependency. Fix this first.

### Checkpoint 2: CALIBRATION EXERCISES

**The principle:** Regularly assess whether the human's judgment matches the AI's and reality. If they diverge, there's atrophy.

**How it works:** Monthly or quarterly, give the team 10-20 test cases where you already know the ground truth. Human makes a judgment. AI makes a judgment. Reality shows which was right. Compare.

**Why it works:** Calibration exercises are the canary in the coal mine. If the human's accuracy is dropping while the AI's stays stable, expertise is atrophying.

**Implementation:**
- Create a test set of 20 cases covering easy, medium, hard, and edge cases
- Ground truth is determined in advance (by an independent expert, or historical outcome data)
- Humans judge blind (don't see AI's answer first, to avoid anchoring)
- AI judges
- Compare both to ground truth
- Monthly review: track each person's calibration score

**Scoring example (medical context):**
- "The human said yes, AI said no, ground truth is yes" → human +1, AI +1, both right
- "The human said yes, AI said yes, ground truth is no" → human 0, AI 0, both wrong
- "The human said yes, AI said no, ground truth is no" → human 0, AI +1, AI right, human wrong (signal: atrophy)

**Red flag:** After 6 months, human accuracy is flat while AI accuracy is improving. That's judgment erosion.

### Checkpoint 3: OVERRIDE REQUIREMENTS

**The principle:** Some decisions must require human override/reasoning, not just human review.

Difference:
- **Review:** "The AI decided yes, I will review it for 10 seconds and click approve unless I spot an obvious error"
- **Override:** "The AI decided yes, I need to state my reasoning for whether I agree, and those two reasonings are logged and compared"

**How it works:** For high-stakes decisions, require the human to either:
1. State their own judgment independently (then compare to AI)
2. Explicitly reason about why they're overriding the AI
3. Flag cases where they disagree with the AI so the model can be audited

**Why it works:** Override requirements force active engagement. You can't rubber-stamp if you have to explain why.

**Implementation:**
- Identify decisions where a human override is possible (not all decisions are — some are too fast)
- Create a decision tree: if human disagrees with AI, document the reasoning
- Make override reasons searchable and analyzable (quarterly: "what override patterns are we seeing?")
- If an override gets overridden later (human was wrong, AI was right), log it and review with the human

**Red flag:** Override rate is <1%. Either the AI is perfect (unlikely) or humans aren't engaging. If someone has been working with the AI for 6 months and has never overridden it, check their judgment.

### Checkpoint 4: REASONING DOCUMENTATION

**The principle:** Capture the human's reasoning, not just the decision.

**How it works:** When a human makes a judgment, capture why. What signals did they use? What edge cases did they consider? What would they need to see to change their mind?

**Why it works:** Documentation codifies tacit knowledge before it atrophies. When you reread your reasoning from 12 months ago, you can spot where your thinking has shifted (usually toward AI-dependency).

**Implementation:**
- Create a simple template for reasoning capture: "I decided [yes/no] because [signal 1], [signal 2], and [signal 3]. I ignored [signal 4] because [reasoning]. I would change my mind if [condition]."
- Make this capture automatic (prompt after decision, not extra work)
- Monthly review: aggregate reasoning to find patterns
- Quarterly: find reasoning that's disappeared (e.g., "6 months ago, humans were flagging [X] as a concern, but nobody mentions it now")

**Red flag:** Reasoning documentation drops in complexity over time. At month 0, reasoning is detailed. At month 12, reasoning becomes "AI seems good" or "I agree with the AI." That's the signal judgment is eroding.

## REALITY CHECK

- **Failure mode of this skill:** Designing checkpoints without enforcement. "We require override documentation" but nobody enforces it. Checkpoints only work if they're non-negotiable.
- **Most expensive mistake:** Waiting 12 months to check. By then, judgment is hard to restore. Start monitoring at month 1.
- **The social cost:** Some people will resent checkpoints ("I know my job, don't patronize me"). Frame as "we're protecting expertise" not "we're watching you."
- **Cost of checkpoints:** ~10% of human time. This is cheap insurance against expertise erosion.
- **When checkpoints backfire:** If the AI is genuinely better than the human (e.g., AI radiologist is more accurate than average radiologist), maintaining the human's independent judgment creates harm. In this case, the question is different: does the human need to be sharp, or do we need oversight? If oversight only, reduce judgment maintenance and build AI verification instead.

## QUALITY GATE

- [ ] The stakes of expertise loss are clear (what happens if this person can't judge anymore?)
- [ ] Timeline of atrophy is mapped (6-18 months in this context)
- [ ] All 4 checkpoints evaluated for relevance (rotation, calibration, override, documentation)
- [ ] At least 2-3 checkpoints selected based on context
- [ ] Implementation plan includes: who runs the checkpoint, how often, success metric
- [ ] Monitoring plan specified: how will you know if judgment is eroding anyway?

## DIAGNOSTIC QUESTIONS

1. **When was the last time someone on the team overrode the AI's recommendation? If you can't remember, you have a problem.**
   - If answer is "never" or ">6 months ago", judgment is probably eroding
   - If answer is "this week", humans are still engaged
   - Spectrum anchor: "Can't remember" → "Multiple times per week"

2. **If we removed the AI tomorrow, could this person do their job at 70% efficiency?**
   - Red flag: "No, they'd be completely lost"
   - Green flag: "They'd be slower, but they know the fundamentals"
   - Spectrum anchor: "Fully dependent (0% without AI)" → "Slightly faster with AI (90% without it)"

3. **What's the most recent edge case this person caught that the AI missed?**
   - Red flag: "Um... I'm not sure" or "A few months ago"
   - Green flag: "Last week, the AI recommended [X] but I knew [situation] makes that wrong"
   - Spectrum anchor: "Can't think of one" → "Multiple per week"

4. **Has this person's accuracy changed in the last 6 months, compared to the AI?**
   - Red flag: "Human accuracy flat or declining while AI accuracy improves"
   - Green flag: "Human and AI accuracy both stable (or human is improving from feedback)"
   - Spectrum anchor: "Diverging" → "Aligned"

5. **If a new version of the AI makes a different decision than the previous version, does this person notice?**
   - Red flag: "They just follow whatever AI says"
   - Green flag: "They'd catch that and ask why the change"
   - Spectrum anchor: "No (rubber-stamping)" → "Yes (paying attention)"

## OUTPUT FORMAT

Structure your output around the 4 checkpoints:

```
## Judgment Maintenance Plan: [Role/Decision Type]

**Expertise at risk:** [What judgment is at risk of atrophying, why it matters, cost of loss]

**Timeline of concern:** In this context, judgment erodes in [X-Y months] if unchecked.

**Current state (diagnostic):**
- When was the last override? [answer + assessment]
- If AI was removed tomorrow, capability would be? [% + gap]
- Edge cases caught recently? [examples or gap]
- Human vs AI accuracy trend? [diverging/aligned/improving]

**Checkpoints to implement:**

1. **Rotation:** [Specific schedule — % time in each mode, rotation frequency]
2. **Calibration:** [Frequency, test set size, scoring method, red flag thresholds]
3. **Override:** [Decision types requiring override reasoning, template, logging mechanism]
4. **Documentation:** [Reasoning capture format, review frequency, degradation signal]

**Monitoring dashboard:**
| Metric | Baseline | Green flag | Red flag | Frequency |
|--------|----------|-----------|----------|-----------|
| Override rate | [X%] | [>Y%] | [<Z%] | Weekly |
| Calibration accuracy | [X%] | [stays stable] | [drops 5%+] | Monthly |
| Reasoning complexity | [average words] | [stays stable] | [drops 30%+] | Monthly |
| Time to decision (unassisted) | [X sec] | [stays stable] | [increases 50%+] | Quarterly |

**Success metric:** At 12 months, human judgment on rotation/calibration tasks has not degraded. At 18 months, human could restore to 80% efficiency within 2 weeks of removing AI.
```

## WHEN WRONG

- Low-stakes, high-frequency decisions where efficiency is primary goal and judgment isn't critical
- Organization has already accepted full delegation (e.g., purely automating routine work, not AI-assisting expertise)
- The human's prior judgment is biased and the AI is genuinely better (in this case, you're building oversight, not restoring judgment)
- Timeline is so compressed (6-week project) that judgment maintenance is premature
- The human has explicitly opted in to delegation and understands the trade-off

---

## TRADE-OFF LEDGER

BY CHOOSING to design judgment maintenance:
  We are betting on: that this expertise is valuable and irreplaceable
  We are giving up: 10% of human time to checkpoints (rotation, calibration, override reasoning, documentation)
  This is reversible within: Not really — if judgment erodes for 18 months, restoring it takes 9-15 months. This is a one-way door.

THE HIDDEN TRADE-OFF:
  Checkpoints slow down the AI. A human reviewing the AI's decision takes longer than just accepting it. You're choosing speed in absolute terms for speed in sustained capability — you want faster, better decisions over 24 months, not just this month.

CONFIDENCE: High
  What would change our mind: An organization where the expertise is no longer strategically important (e.g., a new process has replaced the old expertise) or where the AI has proven it's more accurate than humans and humans should trust it (in which case, you're building oversight differently)

---

## CONCLUSION

Follow the Conclusion Protocol from the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md), Section 6:
1. State the recommendation (which checkpoints to implement, in what order)
2. Name the key trade-off (efficiency loss vs judgment maintenance)
3. Acknowledge the biggest risk (organizational resistance, or checkpoint failure if not enforced)
4. Define the next action (owner of monitoring, first checkpoint launch date)

---

## VISUAL SUMMARY

After completing the primary output, invoke the **excalidraw-svg** skill to create a single Excalidraw SVG visual summary. This diagram should show the atrophy timeline (month 0-18), the 4 checkpoints positioned on that timeline, the baseline metrics and red flag thresholds, and an inset showing how monitored vs unmonitored judgment diverges over time. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.
