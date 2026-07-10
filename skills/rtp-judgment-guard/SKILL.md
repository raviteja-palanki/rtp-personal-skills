---
name: judgment-guard
description: >
  Prevent your team from losing the ability to think for themselves as they rely more on AI. Without designed friction, people accept AI outputs without engaging their own judgment. Over 6-18 months, expertise atrophies silently. This skill designs checkpoints that keep humans sharp — across five distinct erosion mechanisms: the fast clock (one person), the slow clock (the org stops making experts), the relay clock (quality decaying down a chain of handoffs), ownership offloading, and chosen blindness (people avoiding the AI's reasoning because looking costs them). Use when deploying high-stakes AI (medical, financial, hiring decisions), designing AI-augmented workflows, noticing that users aren't questioning AI outputs anymore, or after observing expertise degradation in teams using automation. Do NOT use for low-stakes decisions where acceptance is fine, or when human expertise is already gone (you can't rebuild judgment instantly). Pairs with: trust-ladder (calibrated trust), agent-risk (the override assumption), ai-prd (named owners), eval-framework (the quality tests can't reach).
imports: []
---

# Judgment Guard

## DEPTH DECISION

**Go deep if:** Designing a high-stakes workflow, noticing skill erosion, or rolling out AI to a team with deep domain expertise. **Skim to questions if:** Quick audit of whether checkpoints exist. **Skip if:** Low-stakes decisions where acceptance is intentional and beneficial.

## KEY TERMS (plain language)

- **Judgment atrophy** — the slow, silent loss of a person's ability to make a call on their own as they lean on AI.
- **The fast clock vs. the slow clock** — one person or role losing their edge (fast, 6–18 months) versus the whole organization ceasing to produce experts at all (slow, years).
- **Skill-keeping budget** — deliberately keeping people in some learning-by-doing loops even when automating would be cheaper, booked as an investment in future capability rather than waste.
- **The 3M conditions (Mindset / Meaning / Mechanisms)** — the three things that keep a person *choosing* to own an AI's output: believing they matter to it, having a reason worth the effort, and being judged on catching errors.
- **The 4 checkpoints** — rotation, calibration, override, and reasoning documentation; the deliberate friction that keeps a human sharp.
- **Controlled trial (RCT)** — an experiment with a comparison group, so a measured difference can be trusted as caused, not coincidental.
- **The third clock (relay clock)** — quality decaying as work passes through several people or AI steps in a row, each trusting the last one's output; distinct from the fast and slow clocks.
- **Motivated non-inquiry** — choosing not to look at the AI's reasoning because looking might cost you (money or exposure); distinct from passively offloading the check.
- **Provenance of record** — a tag marking the original human-verified source, so a later reader can return to the truth instead of a summary of a summary.

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../../../UNIVERSAL-SKILL-PROTOCOL.md):
1. Ask the Grounding Questions (Section 1) — at minimum: What expertise is at risk? What's the cost of that expertise degrading? How will users know they're losing judgment?
2. Route depth: Are you building a new system (Comprehensive) or auditing an existing one (Executive Summary)?
3. Identify output format: Word Document, Presentation, or Both?

Then proceed with the skill-specific analysis below.

## DELIVERABLE FORMAT

Before starting, ask for format: Word Document, Presentation, or Both.
Follow the [Universal Skill Protocol](../../../../UNIVERSAL-SKILL-PROTOCOL.md).

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

## THE SECOND CLOCK — WHEN THE ORGANIZATION STOPS MAKING EXPERTS

Everything above is the **fast clock**: one person or one role losing their edge over 6–18 months. There is a second, slower clock the checkpoints below don't catch.

**Clock two — the organization stops producing experts at all.** Junior staff never build their own judgment, because the AI does the work they would have learned from; senior expertise fades from disuse. This is worse than the per-person version because it's invisible until the day you need an expert and discover you stopped making them three years ago. The 4 checkpoints keep *this* reviewer sharp; they do nothing for the *pipeline* that produces the next one.

**The design rule — the skill-keeping budget.** On purpose, keep humans in selected skill-*building* loops even when automating would be cheaper, and record the efficiency you gave up as an investment in future capability, not waste. Name which loops (which tasks build the judgment you'll need to govern this system in three years), and write down the cost you're choosing to carry.

**Why it matters:** as the technology gets more capable, the need for human expertise goes *up*, not down — someone still has to be able to ask whether the system is reliable, lawful, and right for the situation, and if you skip this you're left with a machine that can't be held responsible. **When this is wrong:** where the expertise is genuinely being retired (a new process has replaced it), you don't need to keep making those experts — book the loss and move on.
*(Source: "Beyond Verification: What Responsible AI Really Demands of Human Experts," Renieris, Kiron, Mills & Kleppe, MIT Sloan Management Review, 12 May 2026 — panel poll, 84% ◆, in-panel opinion, not a population survey.)*

### Why the clocks run at all — the engine, and the one control that slows both

The reason expertise drains isn't laziness — it's an economics trap. AI cheapens the part of a job you can *measure* (code shipped, scans read) and by doing so raises the value of the part you *can't* (was it the right call, and who answers for it). A firm watching the metric sheds the unmeasurable half without noticing — booking two hidden liabilities as savings: **capability debt** (you cut the seniors who trained juniors, so the next experts never form — the slow clock as a balance-sheet item) and **judgment debt** (the experts you kept only *review*, so their calibration decays — the fast clock as a balance-sheet item). Software is worse than the classic case: a radiologist's error harms a named patient fast, but a coding error "looks fine at launch and only surfaces when the system is modified, integrated, secured, or scaled" — after the author has left — so the 6–18-month timeline above is the *optimistic* case.

**The paired control that slows both clocks:** a named senior stakes their name on each AI-generated production release *with a junior working under them* — one act that fixes accountability AND is the apprenticeship that keeps the pipeline alive. So the skill-keeping budget should default to senior+junior pairing on releases, not just rotating the lone reviewer. **Why "just educate the leader" won't fix the slow clock:** a trained expert can be *poached*, so training is a gift to a competitor — capability debt is a coordination failure, not ignorance. The fix changes the payoff: make repeated AI-related failures trigger heavier review and named sign-off, so negligence gets expensive enough that keeping humans is the cheap choice.
*(Source: "Big Tech's Looming Capability Crisis," Liu & Kovács, HBR, 2 Jun 2026. Complementarity per Agrawal, Gans & Goldfarb, *Prediction Machines*. Radiologist pay ~$570k/2025 ◆; Meta ~8,000 cut redirected to AI ⚠.)*

## THE THIRD CLOCK — WHEN QUALITY DECAYS DOWN A CHAIN OF HANDOFFS

The two clocks above track judgment fading *inside* one person (fast, 6–18 months) or *inside* one organization (slow, years). There is a third, and it runs sideways: quality decaying as a piece of work passes through several people — or several AI steps — in a row, where each actor trusts the last one's output and no one sees the whole chain.

The mechanism is a chain reaction. The moment one person stops checking the AI's output — reasoning "the next step is AI anyway, so why bother" — the next person rationally does the same, and fidelity to the original truth drops link by link (Holweg and Davenport call the accumulated result *knowledge decay*). Worked example: a hiring pipeline where AI writes the job description, AI screens CVs against it, AI runs the interview against that, and the candidate's AI answers the AI interviewer — four checks meant to catch errors instead multiply their misses (the same shape as an agent chain, 90% reliable × 10 steps ≈ 35% end-to-end), except what compounds is not "did the step succeed" but "does the content still mean what it originally meant."

**The check you can run:** map a real cross-team process end to end and count the AI-mediated handoffs. Three or more in a row with no human checkpoint on the *original* source between them is a knowledge-decay risk — flag it. The fix isn't to police AI use (you can't — most workers hide it). It's to tag the earliest ground-truth artifact (the real customer transcript, the real eval trace, the source document) as the *provenance of record*, and require every downstream AI-generated summary to carry a pointer back to it, so a later reader can always return to the truth instead of a summary of a summary.

**Why it matters:** checking is a cost each person pays and a benefit the *whole chain* receives — individually rational choices produce a collectively bad outcome, so quality erodes even though no one is dishonest. Naming a single owner of the ground-truth artifact restores one person's stake in the whole chain's fidelity, which is the only thing that stops the link-by-link drop. **When this is wrong:** a chain of many AI passes that each *re-anchor* to the same source document (a well-built retrieval pipeline) holds fidelity nearly flat — count re-anchored passes as low-risk, not as handoffs; and where content is low-stakes (an internal brainstorm), decay doesn't matter. The article states the decay as an architectural inevitability but cites no measured rate — treat it as a mechanism to watch for, not a constant.
*(Source: "Don't Let AI Slop Muck Up Your Company's Processes," Holweg & Davenport, HBR, 16 Jun 2026. Load-bearing incident: Deloitte Australia's ~AUD 440,000 government report with ~20 fabricated references, ◆.)*

## OWNERSHIP IS A CHOICE — THE CONDITIONS TO PROTECT

The 4 checkpoints below keep human *judgment* sharp. This module keeps human *ownership* alive — a different failure. Owning an outcome was never something you could hand off; it's a choice a person makes each day. So an AI in the chair doesn't take on ownership — it quietly removes the three conditions under which a human would have chosen it. Protect all three:

- **Mindset** — the owner has to believe "I matter to this outcome." Treating the AI as a colleague (naming it "Kevin," "ALEX-3") destroys this by making the human feel unnecessary. *Break signal:* the owner calls themselves a rubber stamp.
- **Meaning** — the owner needs a reason worth the effort of checking the AI's work. *Break signal:* nobody can say why carefully reviewing the AI matters.
- **Mechanisms** — reviews and recognition must reward *catching the AI's mistakes*, not just shipping its output fast. *Break signal:* your routines reward speed of shipping AI output, not quality of oversight.

**Why it matters:** a controlled trial (BCG, 1,261 people) found that treating the AI as an employee dropped personal accountability by about 9 percentage points and led reviewers to catch about 18% fewer errors (⚠/◆). A disclaimer won't fix that — it's a direct hit on whether a human still *chooses* to own the result, so you have to build the three conditions on purpose, the way you'd provision computing power. **When this is wrong:** where full hand-off is intended and human ownership isn't the goal, skip this — the conditions matter only when you're relying on a human to own the output.
*(Source: "Accountability Must Be Chosen, Not Mandated," Okposo, HBR, 29 Apr 2026. The naming effect is corroborated by the same BCG trial cited above.)*

## MOTIVATED NON-INQUIRY — WHEN PEOPLE CHOOSE NOT TO LOOK

The Ownership module above covers *offloading*: people catch fewer errors because a colleague-like framing makes them feel less responsible (the BCG "employee"-naming effect, ~18% fewer errors). This is a different failure, and it points the opposite way. Here people *know* it's their call and still choose not to see the AI's reasoning — because the reasoning is where the risk to *them* lives.

The evidence: in a controlled study of 2,512 participants acting as loan officers on real $10,000 decisions, 80% wanted the AI's risk score but only ~46% chose to view the reasoning behind it. Two things made people look *less*: tying their pay to the outcome made them ~20% more likely to skip the explanation, and warning them the explanation might reveal race or gender bias pushed avoidance up 10+ points. The tell that this is avoidance, not offloading: the skipping is *strongest* exactly where the person is most accountable (bonus on the line) and most exposed (bias warning present) — the opposite of what fatigue or diffused responsibility would predict.

**The fix is different from offloading's fix.** Offloading is repaired by reassigning ownership and rewarding error-catching (the 3M module above). Avoidance is not — the person already knows it's their job; they're choosing blindness because not-knowing pays. The only fix is to remove the payoff to not-knowing: make the "why" a *mandatory, logged review step* before the decision can be finalized, not an optional link. A dashboard that shows "explanation available" is not evidence anyone looked — log whether it was actually *opened*. And a sharp warning: a bias-disclosure prompt ("this explanation may reveal bias") can *backfire* — in the study it triggered avoidance of the very information it was meant to surface; pair any bias warning with mandatory engagement.

**Why it matters:** transparency features (explain buttons, audit trails) are not a judgment-erosion fix on their own — they can be quietly unused by the exact people whose incentives most need them used. So "we shipped an explain button" is not a control; "was it opened, by whom, on which decisions" is the thing to measure. **When this is wrong:** in low-stakes, low-bias-risk contexts (an internal dashboard where no one's pay or exposure is at stake) the cost that drives avoidance isn't present — don't force review where looking costs the viewer nothing; and forcing review everywhere raises overrides across the board — in the study, viewing the explanation made people ~6 points more likely to override the AI, which is the goal where the AI is wrong and a cost where it's right — so reserve the forcing function for decisions with real bias or compliance exposure.
*(Source: "Employees Aren't Questioning AI Advice Enough," Chan / Rand, HBR, 24 Jun 2026 — ◆ single study, n=2,512, pre-replication. Regulatory stakes ✅ CFPB circular 2023-03, GDPR / EU AI Act.)*

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

Follow the Conclusion Protocol from the [Universal Skill Protocol](../../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 6:
1. State the recommendation (which checkpoints to implement, in what order)
2. Name the key trade-off (efficiency loss vs judgment maintenance)
3. Acknowledge the biggest risk (organizational resistance, or checkpoint failure if not enforced)
4. Define the next action (owner of monitoring, first checkpoint launch date)

---

## VISUAL SUMMARY

After completing the primary output, invoke the **excalidraw-svg** skill to create a single Excalidraw SVG visual summary. This diagram should show the atrophy timeline (month 0-18), the 4 checkpoints positioned on that timeline, the baseline metrics and red flag thresholds, and an inset showing how monitored vs unmonitored judgment diverges over time. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.
