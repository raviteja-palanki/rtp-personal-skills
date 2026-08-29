---
name: problem-type
version: v1.0_latest
description: 'Decide what class of problem you''re holding before you solve it: a technical problem (a better build closes it) or an adaptive challenge (only people changing how they work closes it). The most expensive AI mistakes solve the wrong class: teams ship better models at a problem no model can fix; recurrence after every fix is the tell. A different axis from ''does it need AI'' (that''s problem-ai-fit). Use when the same problem recurs despite fixes, leadership says ''just build it'' but the barrier is organizational, or a feature is technically perfect and adoption still fails. Never to justify inaction, since often the answer is both, sequenced. Pairs with: problem-ai-fit (whether it needs AI at all), falsification (pre-commit the timeline), alignment-check (which org link is broken), adoption-launch (the adaptive work run as a launch), needs-guard (the psychological need the change threatens). Triggers: ''why isn''t this being adopted'', ''we tried everything'', ''just build it''.'
imports: []
---

# Problem Type

**The objective:** before you solve anything, decide what class of problem you're holding — one a better build closes (technical), or one that only closes when people change how they work (adaptive) — for the PM or leader watching a fix fail to stick. Misclassify, and you ship better and better solutions to a problem no solution can reach.

## The one idea

The sales team isn't using the AI recommendation engine. So the team does the obvious thing: builds a better model. Accuracy goes from 80% to 96% to 99%. Adoption stays at 15%. They try a sidebar, then a chatbot, then email summaries — all technically good, all ignored.

Here is what everyone missed. The real reason a rep won't use it is that the AI recommended something once that embarrassed them in front of a customer, and now they don't trust it. No amount of accuracy fixes a trust wound. The team was solving a *technical* problem. The problem was *adaptive.*

That is the one idea: **the most expensive mistake in AI is almost never a bad solution — it's solving the wrong class of problem.** There are two classes, and they close in completely different ways:

- **Technical** — the solution can be found and built. Experts diagnose it, ship it, done. (A slow query, a missing feature, a high error rate.)
- **Adaptive** — the solution requires people to change behavior or beliefs. No build closes it; you can only *enable* the change, and it takes months. (A team that won't trust the AI, a hiring org that can't let AI recommend candidates.)

And here is the tell that you've misclassified, the single most useful signal in this whole skill: **a technical fix, when it's the right class, stays fixed. If you keep fixing it and it keeps coming back, the problem isn't what you think it is.** Recurrence-after-fix is the canary. The instinct when a technical fix fails is to build a *better* technical fix — which is exactly the trap, because building feels productive (action bias) while organizational change feels slow and messy, so teams skip the actual cure.

One more thing this is *not*: it is not the question "does this even need AI?" — that's a different axis (`problem-ai-fit`). A problem can be perfectly AI-suitable and still fail, because the barrier was never technical at all.

## How to use this skill

1. **Run the five signals** — each pulls toward technical or adaptive. Count the votes. (THE FIVE SIGNALS below.)
2. **If it's both — and most real AI problems are — sequence the work.** The adaptive conversation usually has to unlock the technical build, not follow it. (THE DANGEROUS MIDDLE below.)
3. **Act to the class:** technical → define the solution and ship; adaptive → name the belief that must change and the leadership that must model it, and run it as a launch (`adoption-launch`).

## KEY TERMS (plain language)

- **Technical problem** — the solution is discoverable and buildable; expertise and effort close it.
- **Adaptive challenge** — the solution requires people to change behavior or beliefs; no build closes it, only enabled change (Ron Heifetz's distinction, Harvard Kennedy School).
- **Action bias** — building feels productive, so teams build; organizational change feels slow, so it gets skipped even when it's the actual fix.
- **Compliance vs. change** — people doing the new thing when watched, versus believing in it; the ambiguity that makes adaptive progress hard to measure.
- **The dangerous middle** — a problem that is genuinely both, where success depends entirely on sequencing the two kinds of work correctly.

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../../../UNIVERSAL-SKILL-PROTOCOL.md). At minimum, state the problem (not the solution) in one sentence, name who's affected, and list what you've already tried. Then route depth (a full diagnosis of a stuck initiative vs. a quick classification of a new problem) and output format (Document, Presentation, or Both).

## THE TWO CLASSES (Heifetz)

| | **Technical problem** | **Adaptive challenge** |
|---|---|---|
| **Definition** | The solution exists or can be designed by experts. Resistance is minimal — people want the fix. Authority can solve it directly. | The solution isn't known in advance; it's discovered through learning. Resistance is significant — people must give up old ways. It can't be delegated to experts: leadership must *model* the change, not just authorize it. |
| **Pattern** | problem → expert diagnoses → solution deployed → solved | problem → no obvious solution → leadership names the direction → people work through it together over time → new behavior emerges |
| **Examples** | Slow database → optimize the query. High error rate → better training data. Latency too high → add a caching layer. | A sales team that won't trust the AI → build credibility through transparency. Support engineers who see AI as a threat → show how it amplifies their expertise. |

## THE FIVE SIGNALS

Each signal pulls toward technical or adaptive. Read all five, then count.

1. **Has the same problem recurred despite fixes?** Technical fixes, when right, stay fixed. *Adaptive tell:* "We built 95%, then 97%, then 99% accuracy — adoption is still low." Every fix works and the problem persists, so the problem isn't what you think.
2. **Are you building the same solution twice — or cycling through solutions?** *Adaptive tell:* "Recommendation engine → low adoption. Chatbot → low adoption. Email → low adoption." Every *technique* is failing, so it's not the technique.
3. **Is the barrier explicit or implicit?** Technical barriers are measurable ("query takes 5s, SLA is 2s"). *Adaptive tell:* "They have access, they just don't use it, and we don't know why." Invisible barrier = adaptive territory.
4. **Does authority solve it, or only enable it?** A CEO can order a database optimized. A CEO *cannot* order trust. *Adaptive tell:* "Leadership mandated it; adoption went 10%→40% and plateaued — compliance, not belief."
5. **Is the solution obvious-but-unbuilt, or genuinely unclear?** Technical: everyone agrees what to do once they understand it. *Adaptive tell:* "Smart people have argued for six months about whether we should even use AI for hiring — we disagree on fundamentals, not implementation."

**Count the votes:** 3+ technical → technical; 3+ adaptive → adaptive; split → both (see below).

## THE DANGEROUS MIDDLE — when it's both

Most real AI problems are both. The question isn't "which one?" but "what's the sequence?" Get the sequence wrong and even correct work fails.

**Example — "the model makes biased recommendations."** Technical component: it learned from biased data → collect better data, add fairness constraints, retrain (solvable). Adaptive component: the org hasn't agreed on what "fair" *means* here, and stakeholders define it differently (requires conversation).

- **Wrong sequence (fails):** build a fairer model → deploy → conflict erupts because no one agreed on the definition → model gets reverted.
- **Right sequence (works):** hold the adaptive conversation first ("what does fairness mean to us?" — six weeks, hard, ending in shared understanding, not perfect agreement) → build a model reflecting it → deploy → conflict is muted because people co-created the definition.

The rule: **the adaptive work usually unlocks the technical work.** Define the goal with people before you build the solution for them. If the two can run in parallel, start the one with the longer lead time first — and that's almost always the adaptive one.

## THE PROCESS

1. **State the problem in one sentence, without the word "solve."** ("Sales reps adopt the AI engine at 15% vs. a 60% target.")
2. **Score each of the five signals** as technical or adaptive.
3. **Count.** 3+ one way decides it; split means both.
4. **If both, sequence:** does the adaptive work unlock the technical? (usually yes) Can they run in parallel? If so, start the longer-lead one first.
5. **Act to the class:** technical → define the solution and estimate effort; adaptive → name the belief/behavior that must change and the leadership approach to enable it.

## DIAGNOSTIC QUESTIONS

- **When did this first appear, and what have you tried?** Same fix 3+ times with no success, or many *different* technical fixes all failing → adaptive. Fix deployed and it worked → technical.
- **If you replaced the whole team but kept the process and tech, would the problem vanish?** Yes → the problem was structural (technical). No → it's people/belief-dependent (adaptive).
- **What's the most honest answer to "why isn't this solved yet?"** "We can't agree on what to do" → adaptive. "It needs three weeks of engineering / more data" → technical.
- **Could the smartest person in the company, with unlimited budget and six weeks, solve it?** Yes → technical. No, because of organizational barriers → adaptive. No even with unlimited resources → probably both.
- **Can you define what success looks like?** If you *can't* — because the org hasn't agreed on the values — that inability is itself the signal it's adaptive.

## WORKED EXAMPLE — "the AI feature isn't getting adopted"

**Problem:** sales reps adopt the AI recommendation engine at 15% vs. a 60% target.

- **S1 recurrence** — three model versions, 80%→96% accuracy, adoption flat → adaptive.
- **S2 cycling** — sidebar, then chat, then email; all technically good, all low → adaptive.
- **S3 barrier** — implicit; "they don't use it" and no one knows why → adaptive.
- **S4 authority** — VP mandated it; 5%→15% then plateaued → adaptive (compliance, not belief).
- **S5 solution** — engineers say UI, sales say trust, product says workflow → adaptive (disagreement on fundamentals).

**Diagnosis: 5/5 adaptive.** The real problem: reps fear the AI picks people they wouldn't, threatening their commission and their sense of competence — or one bad past recommendation killed trust.

**What won't work:** a better model, a mandate, a nicer UI — all technical fixes to an adaptive problem.

**What will:**
- Understand the real fear (six weeks of listening).
- Reposition AI as amplifying the rep's judgment, not replacing it.
- Create an opt-in fast-track where early adopters prove it works.
- Celebrate reps who *override* the AI and are right — the signal that human judgment still counts.

After that groundwork, the technical improvements land differently.

## WHERE THIS SKILL MEETS THE REST OF YOUR STACK

Problem-type answers *what class of problem* you hold. It hands off to a different-axis check, three skills that act on an adaptive verdict, and one skill that guards against the diagnosis being misused.

**A different axis (run both, don't substitute one for the other):**
- **`rtp-problem-ai-fit`** — whether the problem needs AI at all, and if so, which seat AI takes — a decision *engine* for narrow, well-bounded decisions vs. a *helper* for wide, judgment-heavy ones. Problem-type is the technical-vs-adaptive cut; problem-ai-fit is the needs-AI and role cut. *(Cross-ref sanctioned by q2-11 card, MIT SMR, Amorim/Saleh/Sundling, 6 May 2026 — its substance lives in problem-ai-fit, not here.)*

**Acts on an adaptive verdict:**
- **`rtp-alignment-check`** — locates *which* organizational link (purpose → strategy → capability → architecture → systems) is actually broken.
- **`rtp-adoption-launch`** — runs the adaptive work as a product launch with personas and phases, not a one-time training.
- **`rtp-needs-guard`** — names the psychological need (competence, autonomy, belonging) the change threatens, which is usually the real engine of "resistance."

**Guards the diagnosis itself:**
- **`rtp-bias-spotter`** — the action bias named in KEY TERMS above is the exact mechanism bias-spotter's Stage 1 audits. If you're not sure whether you genuinely diagnosed adaptive or just found a comfortable reason to avoid the harder technical build, run its checklist on your own call.
- **`rtp-falsification`** — the REALITY CHECK below names the failure mode of this skill: "it's adaptive, so we wait," used to justify indefinite delay. Falsification is the fix — pre-commit to what evidence, by what date, would prove "we need six more weeks of listening" wrong instead of just true forever.

Run problem-type to classify; run the second and third groups to act on and stress-test that classification.

## REALITY CHECK

- **The failure mode of this skill:** using it to *avoid* action. "It's adaptive, so we wait." No — you work both; often the answer is adaptive and technical in parallel, sequenced so adaptive unlocks technical.
- **The common misread:** treating all resistance as adaptive. Sometimes it's just poor communication or bad change management — you did the change right and told people badly. That's technical.
- **The cost of getting it wrong:** treat adaptive as technical and you burn engineering on solutions no one uses (and each failure erodes trust further); treat technical as adaptive and you hold alignment meetings while the database is on fire.

## QUALITY GATE

- [ ] Problem stated as a problem, not a solution
- [ ] All five signals scored (not all need to be conclusive)
- [ ] Primary classification made — technical, adaptive, or both
- [ ] If both: the sequence is explicit (which unlocks which; what runs in parallel)
- [ ] Technical → solution and effort estimate defined; Adaptive → the belief/behavior change and the leadership approach are named
- [ ] Next action specified (start the build, start the adaptive conversation, or both)

## TRADE-OFF LEDGER

By diagnosing the class before acting, you bet that misclassifying the problem is more expensive than the one to two weeks of diagnosis. You give up the immediate comfort of shipping a technical "solution" now. **Reversible?** Within a week — if the diagnosis is wrong, course-correct fast. **The hidden trade:** if it's adaptive and you treat it as technical, the engineering effort doesn't compound *and* each failed fix teaches the org to trust the AI less — "we tried better algorithms and nothing worked" is a worse position than where you started. **Confidence: High.** What would change it: a problem already clearly one class (a slow query, or a pure org-structure dispute) — skip the diagnosis and act.

## CONCLUSION

Follow the Conclusion Protocol from the [Universal Skill Protocol](../../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 5: state the classification (technical, adaptive, or both with the sequence), name the key trade-off (speed of a technical fix vs. correctness of the diagnosis), acknowledge the biggest risk (misdiagnosis — or over-analyzing when action is needed), and define the next action (technical owner, adaptive sponsor, and the decision point).

## VISUAL SUMMARY

After the primary output, invoke the **excalidraw-svg** skill for one visual: the five signals drawn as a spectrum from TECHNICAL to ADAPTIVE with the problem plotted on it, and — if both — a small timeline underneath showing the adaptive work unlocking the technical build (sequence, not simultaneity). So a viewer sees the class and the sequence at a glance. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.
