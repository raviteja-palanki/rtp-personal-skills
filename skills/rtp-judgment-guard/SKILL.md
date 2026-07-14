---
name: judgment-guard
description: >
  Decide, on purpose, where human judgment sits inside an AI system — because if you don't,
  adoption decides for you and the default removes the human. Two cases. ATROPHY: leaning on AI
  silently fades expert judgment over 6–18 months and stops an organization making new experts;
  design deliberate friction (rotation, calibration, state-first override, repair, reasoning
  capture) to keep humans sharp. COMPLEMENTARITY: in regulated, catastrophic-cost work (surgery,
  aviation, lending) the human stays permanently because human and AI together are more precise
  and more certain than either alone; design the labor split so each brings its best, the tail
  not the average setting the floor. Use when deploying high-stakes AI, users stop questioning AI
  outputs, designing human-in-the-loop for regulated work, or rolling AI into a team of experts.
  Do NOT use for low-stakes work where full automation is intended.
  Pairs with: determinism-compass, autonomy-spectrum, trust-ladder, agent-risk, safety-by-design.
imports: []
---

# Judgment Guard

**The objective:** decide, deliberately, which human judgment you keep inside an AI system, how you keep it sharp, and when you fuse human and machine into one permanent joint system — for the leader rolling AI into expert, high-stakes, or regulated work. It turns a decision that adoption otherwise makes for you, by default and always against the human, into one you make on purpose.

## The one idea

**AI doesn't just do the work. It changes what your people become — and if you don't decide the change, the default decides it, and the default removes the human.** There are two versions of this, and a serious system needs both.

**The atrophy case.** Every expert got good the same way: by doing the task, clumsily at first, over and over, until the judgment moved into their hands and became instinct. AI removes exactly that step — it does the reps for them. The work still ships, better and faster by every number on your dashboard, so it *looks* like pure gain. Underneath, the thing that made the expert an expert goes quiet from disuse, and no alarm rings. You find out the day the AI is finally wrong about something that matters, and no one in the room can still tell. The shape worth memorizing: **the cost of AI is paid twice — once, small and visible, when you keep a human sharp on purpose; or later, large and hidden, when you didn't.**

**The complementarity case.** Sometimes you keep the human not because they're fading, but because the human and the machine are each irreplaceable and *together* they are better than either could ever be alone. A surgical robot holds the instrument to a tenth of a millimeter with no tremor; the surgeon reads the bleed the scan never showed and owns the life on the table. Neither alone is tolerable. Together they operate more precisely *and* with more conviction — the surgeon acts decisively *because* the system confirms, and the system is safe *because* the surgeon governs it. Here the human is permanent **by design**, and where a wrong answer is catastrophic and irreversible, no amount of AI maturity changes that.

Same skill, one question underneath both: **which judgment stays human, and how do you engineer that on purpose** — before adoption answers it for you.

## How to use this skill — three questions

1. **Which judgment must stay human?** The stakes and the reversibility of a wrong call decide this. Everything downstream depends on it.
2. **How do you keep that judgment from fading?** → **Case 1 (Atrophy)** below: the five ways it drains, and the checkpoints that stop each.
3. **When must the human and AI be fused as one permanent system?** → **Case 2 (Complementarity)** below: the design for high-stakes, regulated work where the combination beats either alone.

Most systems live mostly in one case. Read the diagnosis to find yours; read the design to build it.

## KEY TERMS (plain language)

- **Judgment atrophy** — the slow, silent loss of a person's ability to make a call on their own as they lean on AI.
- **The cost paid twice** — you either pay a small, visible cost to keep a human sharp, or a large, hidden cost later when their judgment has quietly gone.
- **The three clocks** — judgment fades inside one *person* (fast, 6–18 months), inside one *organization* that stops making experts (slow, years), or *down a chain* of AI handoffs where each step trusts the last (sideways).
- **Skill-keeping budget** — deliberately keeping people in some learning-by-doing loops even when automating is cheaper, booked as an investment in future capability, not waste.
- **Offloading vs. chosen blindness** — catching fewer errors because a colleague-like AI made you feel less responsible (offloading), versus knowing it's your call and choosing not to look at the AI's reasoning because looking would cost you (chosen blindness).
- **The three-question diff** — after stating your own view, compare it to the AI's along three questions: what did it add, what did it get wrong, and what *looks right but isn't* (the costliest error — plausible, well-structured, wrong in a way only domain knowledge catches).
- **Complementarity** — a joint human-AI system deliberately designed so each does what it is irreducibly best at, and the combination beats either alone.
- **Tail risk** — the rare, worst-case outcome; in catastrophic-cost domains it sets the design, not the average performance.
- **Convergence / divergence** — two independent judgments agreeing (the source of the joint system's extra conviction) versus disagreeing (the signal to stop and resolve, never average).
- **Evidence tiers used below** — ✅ audited/peer-reviewed · ◆ company- or study-disclosed · ⚠ reported or practitioner estimate. Numbers marked *illustrative* are teaching devices, not measured facts.

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md). At minimum, answer: What expertise is at risk, and what does a wrong call cost — reversibly or not? How will anyone *know* judgment is fading? Then route depth (building a new system vs. auditing one) and output format (Document, Presentation, or Both).

---

## CASE 1 — ATROPHY: when leaning on AI quietly fades the human

### The trap

You will celebrate adoption. The bias is the **success illusion**: automation metrics feel like proof ("90% of tickets auto-routed!") while the real cost is invisible. Expertise doesn't erode visibly — it erodes in six-month increments, and the timeline is predictable:

- **Month 0–3 — Adoption.** People use the AI, catch its misses, learn the edge cases.
- **Month 4–6 — Complacency.** "The AI usually works." Exceptions start sliding through.
- **Month 7–12 — Delegation.** People manage exceptions instead of judging; "the AI said so" becomes authority.
- **Month 13–18 — Dependency.** They can't make the call without it. The expert is now a manager of exceptions, not a practitioner.

**Why it's expensive:** restoring judgment costs two to three times what it took to lose — if the expert hasn't already left, feeling their expertise was devalued. It *feels* like a technology problem (blame the AI) when it's a design problem (you built no checkpoints).

### The five drains (diagnosis)

Judgment doesn't drain one way. Look for each — they run on different clocks and need different fixes.

**1. The fast clock — one person dulls (6–18 months)**
- **Mechanism:** the timeline above. A tool that's 90% accurate teaches people to stop attending to the 10% where it fails; the mind stops working the problem, and the heuristics fade.

**2. The slow clock — the organization stops making experts (years)**
- **Mechanism:** junior staff never build judgment because the AI does the work they'd have learned from; senior expertise fades from disuse.
- **Why it's worse than the fast clock:** invisible until the day you need an expert and discover you stopped making them three years ago.
- **Why it happens — the economics trap:** AI cheapens the part of a job you can *measure* and raises the value of the part you can't, so a firm sheds the unmeasurable half without noticing, booking two liabilities as savings — **capability debt** (cut the seniors who trained juniors) and **judgment debt** (the experts you kept only *review*, so their calibration decays).
- **Why software is worse than the classic radiologist case:** a radiologist's miss is caught same-day; a coding error "looks fine at launch and only surfaces when the system is modified, scaled, or secured" — long after the author has left.
- **The one control that slows both:** a named senior stakes their name on each AI-generated production release *with a junior working under them* — one act that fixes accountability AND is the apprenticeship that keeps the pipeline alive.
- **When this is wrong:** the expertise is genuinely being retired — book the loss and move on.
*(Sources: MIT Sloan Management Review, Renieris et al., 12 May 2026 — 84% panel poll ◆, opinion not population survey. HBR, Liu & Kovács, "Big Tech's Looming Capability Crisis," 2 Jun 2026. Radiologist pay ~$570k/2025 ◆; Meta ~8,000 cut redirected to AI ⚠.)*

**3. The relay clock — quality decays down a chain of handoffs (sideways)**
- **Mechanism:** the moment one person stops checking ("the next step is AI anyway"), the next rationally does the same, and fidelity to the original truth drops link by link (Holweg & Davenport call it *knowledge decay*). A hiring pipeline where AI writes the JD, AI screens CVs against it, AI runs the interview against that — four checks meant to catch errors instead multiply their misses.
- **The check:** map a real cross-team process and count AI-mediated handoffs; three or more in a row with no human check on the *original* source is a decay risk.
- **The fix:** you can't police AI use (people hide it) — instead tag the earliest ground-truth artifact (the real transcript, the source doc) as the **provenance of record**, and require every downstream summary to point back to it, so a reader can always return to the truth instead of a summary of a summary.
- **When this is wrong:** a chain that each time *re-anchors* to the same source (a well-built retrieval pipeline) holds fidelity nearly flat — count re-anchored passes as low-risk.
*(Source: HBR, Holweg & Davenport, "Don't Let AI Slop Muck Up Your Company's Processes," 16 Jun 2026. Deloitte Australia's ~AUD 440,000 report with ~20 fabricated references ◆. No measured decay rate given — treat as a mechanism to watch, not a constant.)*

**4. Offloading ownership — the AI feels like a colleague, so the human feels off the hook**
- **Mechanism:** owning an outcome was never something you could hand off; it's a choice a person makes each day, and an AI in the chair quietly removes the three conditions under which they'd choose it.
- **Protect Mindset** ("I matter to this outcome" — naming the AI "Kevin" destroys it). *Break signal:* the owner calls themselves a rubber stamp.
- **Protect Meaning** (a reason worth the effort of checking). *Break signal:* no one can say why careful review matters.
- **Protect Mechanisms** (reviews reward *catching the AI's mistakes*, not just shipping fast). *Break signal:* your routines reward speed of shipping.
- **Why it matters:** a controlled trial (BCG, 1,261 people) found treating the AI as an employee dropped personal accountability ~9 points and led reviewers to catch ~18% fewer errors (⚠/◆) — a disclaimer won't fix a direct hit on whether a human still *chooses* to own the result.
- **When this is wrong:** full hand-off is intended and human ownership isn't the goal — skip it.
*(Source: HBR, Okposo, "Accountability Must Be Chosen, Not Mandated," 29 Apr 2026, corroborated by the same BCG trial.)*

**5. Chosen blindness — people know it's their call and still choose not to look**
- **How it's different from offloading:** here the reasoning is exactly where the risk to *them* lives, and the pointer runs the other way — not "I feel less responsible" but "looking would cost me."
- **The evidence:** in a study of 2,512 people making real $10,000 loan decisions, 80% wanted the AI's score but only ~46% viewed the reasoning behind it; tying pay to the outcome made them ~20% more likely to skip it; warning them the explanation might reveal bias pushed avoidance up 10+ points.
- **The tell it's avoidance, not fatigue:** skipping is *strongest* exactly where the person is most accountable and most exposed.
- **The fix is different from offloading's:** you can't reassign ownership (they already own it) — you remove the payoff to not-knowing by making the "why" a *mandatory, logged* review before the decision finalizes. "Explanation available" is not evidence anyone looked; log whether it was *opened*.
- **The sharp warning:** a bias-disclosure prompt can *backfire*, triggering avoidance of the very information it meant to surface — pair any bias warning with mandatory engagement.
- **When this is wrong:** in low-stakes, low-exposure contexts the cost that drives avoidance isn't present — don't force review where looking costs the viewer nothing.
*(Source: HBR, Chan / Rand, "Employees Aren't Questioning AI Advice Enough," 24 Jun 2026 — ◆ single study, n=2,512, pre-replication. Regulatory stakes ✅ CFPB circular 2023-03, GDPR / EU AI Act. Note: viewing the explanation raised overrides of both *right and wrong* AI calls, not only wrong ones.)*

### The five checkpoints (treatment)

Deliberate friction — not "slow the AI down," but "keep the human sharp." Choose what the stakes justify; two or three, enforced, beat five that aren't.

**1. Rotation — keep two decision pathways alive**
- **The practice:** no one uses the same AI tool for more than ~80% of their decisions for more than four weeks straight. A radiologist reads some scans unassisted, some with AI, some as peer reviewer of the AI's reads — rotate every four weeks, not daily (that's chaos).
- **Red flag:** "we can't rotate, they're too busy" — the AI has reached 100% dependency; fix that first.

**2. Calibration — measure the human against ground truth**
- **The practice:** monthly, give the team 10–20 cases where you already know the answer. Human judges blind (no AI answer first, to avoid anchoring), AI judges, reality shows who was right.
- **Red flag:** after six months, human accuracy is flat while AI accuracy improves — that gap is erosion.

**3. Override — its sharpest form is stating your call first**
- **The practice:** the strongest version of a human review is not "approve unless something looks off" — it's stating your own view *before* you see the AI's, so there is something real to compare against.
- **Mechanism:** gate the AI's output behind a required, timestamped "here's what I think and why" field — a stated position, not a click-through. A click without a prior stance is exactly the theater mandatory review decays into, and it defeats chosen blindness by removing the ability to stay uncommitted.
- **Then run the three-question diff:** what did the AI add that you missed; what did it get wrong; and — ranked highest, because it's the costliest — what *looks right but isn't* (plausible, well-structured output resting on a wrong assumption, the error only domain judgment catches).
- **Red flag:** override rate under ~1% — either the AI is perfect (unlikely) or no one is engaging.
*(State-first + the three-question diff and "looks right but isn't" as top severity: HBR, Duncan & Anderson, "Help Employees Get Better, Not Just Faster, with AI," 15 Jun 2026 — conceptual, built on the Dreyfus and Polanyi tradition; the "jagged frontier" calibration idea is ✅ Dell'Acqua/Mollick et al., HBS 24-013. The article's own 90%/10% and two-weeks-to-an-hour figures are ⚠ illustrative.)*

**4. Repair after a miss — before you re-engineer the process**
- **The practice:** when an AI-assisted call goes wrong, the reflex is to fix the process. Do the *social* repair first, or the fix lands structurally sound and socially inert.
- **Mechanism:** run an explicit reconciliation — both parties state what they could have done differently — opened with normalization ("there can be multiple good decisions; a call can be reasonable and still be beaten by how events unfold") so it doesn't collapse into blame. *Then* ask the process question — "*why* did this happen," not "what happened" — and change the system so the failure can't recur.
- **Why it matters:** this protects the Mindset condition from drain 4 — skip it, and the person you most need to keep owning the outcome quietly stops.
- **When this is wrong:** where psychological safety is genuinely absent, the "what could I have done differently" confession can be weaponized — fix the safety first, or the repair backfires.
*(Source: HBR, McCall, Wolfberg, Bilsborough, Pruna, "How Elite Sports Coaches Make High-Pressure Decisions," Jul–Aug 2026 — ⚠ anecdote-tier, 11 coaches, no numbers; cite the mechanic, not the quotes.)*

**5. Reasoning documentation — capture the why, not just the decision**
- **The practice:** "I decided [X] because [signals]; I ignored [Y] because [reason]; I'd change my mind if [condition]." Make capture automatic (a prompt after the decision, not extra work).
- **Cadence:** review monthly for patterns; quarterly, look for reasoning that has *disappeared* ("six months ago people flagged X; nobody mentions it now").
- **Red flag:** reasoning drops in complexity over time — "AI seems good" — that's the signal, in the person's own words.

---

## CASE 2 — COMPLEMENTARITY: when the human stays because human + AI together beat either alone

Case 1 keeps a human sharp against a fading default. Case 2 is the opposite starting point: in a regulated or catastrophic-cost domain, the human is *permanent by design*, and the goal is to fuse human and AI so the combination is more precise **and** more certain than either alone. The neurosurgeon-plus-robot is the clean picture — the robot's tremor-free precision, the surgeon's judgment on the bleed the scan never showed, and an outcome someone is accountable for. Here is how to design it.

### The Complementarity Design — four moves

**1. Split by irreducible strength**
- **The move:** list the task's sub-decisions and give each to whoever cannot lose it. *AI:* precision, consistency, recall across millions of cases, no fatigue. *Human:* the novel situation, the context no data held, the call someone must answer for. Give the robot the tremor-free motion; give the surgeon the bleed and the accountability.
- **Why:** a joint system is only as strong as the fit between the split and each party's true edge — mismatch the split and you get the weaknesses of both.

**2. Set the floor by the tail, not the average**
- **The move:** where the 0.1% is a dead patient or an unlawful denial, "the AI is more accurate on average" is the *wrong number* — you design for the worst plausible case.
- **Why this is precisely why mature AI does not remove the human here:** the tail, not the mean, sets the design, and the human is the tail's last defense.
- **When this is wrong:** where errors are cheap and reversible, designing for the tail is over-engineering — that's a Case 1 or a full-automation problem, not this one.

**3. Make convergence your conviction, divergence a full stop**
- **The move:** two independent judgments agreeing is *why* the joint call carries more conviction than either alone — the surgeon acts more decisively because the system confirms. When they disagree, that is the alarm: stop and resolve it, **never average it**.
- **Why:** averaging two judgments that disagree hides the very signal the joint system exists to surface, and manufactures false confidence in the middle.

**4. Keep the human's hands on the hard part, not just their eyes on the screen**
- **The move:** assign the permanent human the sub-decision that keeps their judgment live — not the rubber-stamp seat.
- **Why:** this is where the two cases fuse — a permanent human who only *watches* still atrophies (Case 1), so the atrophy checkpoints *serve* the complementarity design; oversight-by-watching decays into rubber-stamping within months, oversight-by-doing-the-hard-part stays calibrated.

**The regulated-domain rule, stated plainly:** where a wrong answer is catastrophic *and* irreversible *and* someone must be legally accountable, keep the human in the loop regardless of AI maturity — and still keep them few and elite, because scarcity is not the enemy here; a dull majority is. Complementarity is not a compromise between human and machine. It is a multiplier — done right, the pair is safer *and* more decisive than the sum.

---

## WHERE THIS MEETS YOUR STACK

Judgment-guard owns one seat: which judgment stays human, how you keep it sharp (Case 1), and how you fuse it with the machine when the stakes demand both (Case 2). It has no imports — every companion below is a hand-off, not an input.

**Hands off to, to build the rest of the joint system:**
- `determinism-compass` — which parts must be rule-bound and reproducible vs. which can tolerate the model's variance. Decide this *before* you split the labor in Case 2.
- `autonomy-spectrum` — who holds the decision at each step. In Case 2 the human keeps the final call by design; this skill sets where on the spectrum the rest of the system sits.
- `trust-ladder` — how far to trust the AI's half, calibrated, and how trust is repaired after a miss (the calibrated mirror of Checkpoint 4).
- `agent-risk` — proportionality and the kill-switch when the cost of a wrong call is catastrophic (Case 2's tail is agent-risk's home ground).
- `safety-by-design` — encode the constraints into the system so the joint pair can't be driven outside them.
- `stress-test` — its human gate ("will anyone say it fails?") is a worked instance of this skill's checkpoint pattern, applied to one specific moment: the pre-launch kill decision. Reuse the state-first-override and reward-the-honesty machinery there instead of re-deriving it from scratch.

**Acts on this skill's decision, one hop downstream:**
- `agent-spec` — takes "this judgment stays human" and encodes it as an actual autonomy level and confidence threshold in the technical spec; without that translation, the decision stays a slide, not a system.
- `stakeholder-communications` — carries the "why a human stays in the loop here" case to a board or regulator who will ask for the efficiency number this design deliberately doesn't optimize for.
- `needs-guard` — when the REALITY CHECK below's "some people resent checkpoints" risk materializes into real resistance, that's a need-violation to diagnose, not a training problem to push through.

**Arbitrates when this skill disagrees with a pure efficiency recommendation:**
- If `autonomy-spectrum` or `agent-spec` would otherwise push toward a higher autonomy level for speed or cost, and this skill's Case 2 test says the domain is regulated and catastrophic-cost, **judgment-guard's human-stays-in-the-loop call overrides the efficiency recommendation.** Run judgment-guard first in any domain where the two could conflict, not after.

## REALITY CHECK

- **The failure mode of this skill:** checkpoints without enforcement. "We require override documentation" that no one enforces is theater. Non-negotiable, or nothing.
- **The most expensive mistake:** waiting 12 months to check. Start monitoring at month 1 — by month 12 the judgment is already hard to restore.
- **The social cost:** some people resent checkpoints ("I know my job"). Frame as "we're protecting your expertise," not "we're watching you."
- **The honest inversion:** if the AI is genuinely better than the human on the *average* case and the tail is cheap, maintaining independent human judgment can create harm — then you're building oversight, not restoring judgment (and you may be in Case 2's opposite: full automation with a human only on the tail).

## QUALITY GATE

- [ ] Which judgment must stay human is decided, and *why* (stakes × reversibility), before anything else
- [ ] The case is named: atrophy (Case 1), complementarity (Case 2), or a mix — and the design matches
- [ ] Case 1: the specific drain(s) identified among the five, and checkpoints chosen to match (not a generic "add friction")
- [ ] Case 1: at least the state-first override (checkpoint 3) and the repair-after-a-miss step (checkpoint 4) are present for high-stakes work
- [ ] Case 2: the labor split is by irreducible strength, the floor is set by the tail, and divergence triggers a stop
- [ ] Every checkpoint has an owner, a cadence, and a red-flag threshold; enforcement is named
- [ ] Hand-offs to the companion skills (determinism-compass, autonomy-spectrum, trust-ladder, agent-risk, safety-by-design, agent-spec) are named where the design needs them

## DIAGNOSTIC QUESTIONS

1. **When did someone last override the AI?** "Can't remember / >6 months" → eroding. "This week" → still engaged.
2. **If the AI vanished tomorrow, could this person do the job at 70%?** "No, they'd be lost" is a red flag; "slower, but they know the fundamentals" is green.
3. **What's the most recent edge case this person caught that the AI missed?** A blank stare is the signal.
4. **Has their accuracy moved against the AI's over six months?** Diverging (human flat, AI rising) is erosion.
5. **(Case 2)** When human and AI disagree, does the system *stop* — or does it quietly average them into a confident middle?

## OUTPUT FORMAT

```
## Judgment Design: [Role / Decision Type]

**Which judgment stays human, and why:** [the sub-decisions, tied to stakes × reversibility]
**Case:** [Atrophy / Complementarity / mixed] — [one line on why]

**Case 1 — if atrophy applies**
- Drain(s) present: [which of the five]
- Timeline of concern: [erodes in X–Y months here]
- Checkpoints (owner · cadence · red flag):
  1. Rotation — … 2. Calibration — … 3. State-first override — … 4. Repair-after-a-miss — … 5. Reasoning capture — …

**Case 2 — if complementarity applies**
- Labor split (by irreducible strength): AI does […]; human does […]
- Tail the design must survive: [worst plausible case]
- Convergence/divergence rule: [what happens when they disagree]
- Which sub-decision keeps the human's hands (not just eyes) in it: […]

**Hand-offs to the stack:** [determinism-compass / autonomy-spectrum / trust-ladder / agent-risk / safety-by-design / agent-spec — where each is needed]

**Monitoring:**
| Metric | Baseline | Green | Red | Frequency |
|---|---|---|---|---|
| Override rate | | >Y% | <Z% | Weekly |
| Calibration accuracy | | stable | drops 5%+ | Monthly |
| Reasoning complexity | | stable | drops 30%+ | Monthly |
| (Case 2) divergence-resolved rate | | 100% stopped | any averaged | Per incident |
```

## WHEN WRONG

- Low-stakes, high-frequency decisions where efficiency is the goal and judgment isn't critical.
- The organization has deliberately chosen full delegation and the human isn't meant to own the output.
- The human's prior judgment is genuinely biased and the AI is better on a tail that's cheap — build oversight, not restored judgment.
- The timeline is so short (a six-week project) that judgment maintenance is premature.

---

## TRADE-OFF LEDGER

- **The bet:** by designing judgment on purpose, you're betting this expertise is valuable and — in Case 2 — irreplaceable.
- **What you give up:** ~10% of human time to checkpoints, and in Case 2 you refuse the cheaper fully-automated path.
- **Reversible?** Barely. Judgment lost over 18 months takes 9–15 to rebuild — a one-way door.
- **The hidden trade:** you're choosing sustained capability and decisive, accountable decisions over the next 24 months, not the fastest possible decision this month.
- **Confidence: High. What would change it:** the expertise is being retired (Case 1 moot), or the AI has proven itself on a tail that's cheap and reversible (build oversight differently).

## CONCLUSION

Follow the Conclusion Protocol (Universal Skill Protocol, Section 6): state the recommendation (which judgment stays human, which case, which checkpoints or which labor split), name the key trade-off (efficiency vs. sustained, accountable judgment), acknowledge the biggest risk (checkpoints unenforced, or a labor split that mismatches each party's real edge), and define the next action (owner of monitoring, first checkpoint or first convergence-review date).

---

## VISUAL SUMMARY

After the primary output, invoke the **excalidraw-svg** skill for one visual: the atrophy timeline (month 0–18) with the five checkpoints placed on it, beside the Case 2 panel — the labor split (AI precision × human judgment), the tail-set floor, and the convergence-or-stop rule — so a viewer sees both halves of the one idea at a glance. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.
