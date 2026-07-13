---
name: needs-guard
description: "Ensure AI deployment doesn't threaten what workers actually care about — autonomy, competence, belonging. When workers resist AI, it's usually not fear of change or a skill gap: the AI removed something they depend on to feel like a professional. Resistance is a need-violation problem, which makes it a product problem, not a change-management one — you diagnose which psychological need is broken (Self-Determination Theory: autonomy, competence, relatedness) with the AWARE diagnostic, then redesign the deployment to protect it. Use when workers resist AI, adoption plateaus at months 3–4, or people use unauthorized 'shadow AI' tools. Do NOT use before tools are selected (ai-use-case-readiness first), or when resistance is really a UX or AI-quality problem. Pairs with: attitudinal-segmentation (stance vs. need), adoption-launch (the phased motion), problem-type (need violation = adaptive challenge), eval-framework (rule out quality issues). Triggers: 'workers resist the AI', 'adoption is dropping', 'shadow AI'."
imports: [first-principles, bias-spotter]
---

# Needs Guard

**The objective:** make sure an AI deployment doesn't quietly strip the things workers depend on to feel like professionals — autonomy, competence, belonging — for the PM or leader watching adoption stall and hearing "our people just resist change."

## The one idea

You roll out the AI. Month 1, adoption surges — novelty. Month 3, it collapses. The team concludes: "workers don't understand the technology," or "we didn't train them enough," or "this generation resists change."

None of that is true, and here is what's actually happening: **the AI removed something the worker depends on to feel like a professional.** The support agent who can no longer explain *why* a ticket was routed the way it was can't defend her decision to a customer — so she feels exposed and stops trusting the tool. That's not fear of change. It's a need being violated.

The core idea reframes the whole problem: **resistance is not a change-management problem, it's a need-violation problem — which makes it a *product* problem.** You're shipping a tool that violates a psychological need, and no amount of training, propaganda, or executive mandate fixes a need violation (a worker who understands the AI perfectly but feels replaced will still resist it). Self-Determination Theory names the three needs every professional requires: **autonomy** (control over how I work), **competence** (feeling skillful, able to learn and defend my answers), and **relatedness** (belonging, being valued, not disposable). Diagnose which one the deployment breaks, redesign the workflow to protect it, and adoption happens *naturally* — because the tool stops threatening the person.

The bias that hides this is **fundamental attribution error**: blaming the person's character ("they resist change") instead of the system ("this violates their competence need"). The signals are usually already there — most sharply when workers bypass your official tool for an unauthorized "shadow AI" one. That workaround isn't disobedience; it's them restoring a need your system took away. Ask what the unauthorized tool lets them do that yours doesn't, and they'll name the violated need for you.

## How to use this skill

1. **Map the touch points** — every moment a worker interacts with the AI: what they see, where they can intervene, what happens to their input.
2. **Run the AWARE diagnostic** — score each touch point Green/Yellow/Red on the five need dimensions. (THE AWARE DIAGNOSTIC.)
3. **Name the dominant violation and redesign the deployment to protect it** — not the model, the *workflow and framing* around it — then measure *voluntary* adoption, not forced compliance.

## KEY TERMS (plain language)

- **Self-Determination Theory (SDT)** — Deci & Ryan's finding that people need three things to feel motivated and professional: autonomy, competence, relatedness.
- **The three needs** — *autonomy* (control over how I work), *competence* (feeling skillful, able to learn and defend my answers), *relatedness* (belonging, being valued).
- **AWARE** — the five-dimension diagnostic that maps onto the three needs: **A**utonomy, **W**ork-identity + **A**ffiliation (≈ relatedness), **R**outine/expertise + **E**xpertise-recognition (≈ competence).
- **Shadow AI** — workers bypassing the official tool for unauthorized consumer ones; the clearest signal your system violates a need, and a map to which.
- **Fundamental attribution error** — blaming the worker's character ("they resist change") for a problem the system caused ("this violates their competence need").
- **Voluntary vs. deployment adoption** — % who use the tool *when they could choose not to* vs. % who merely have access; only the first is real adoption.
- **Evidence tiers used below** — the resistance stats (~31% actively resist, ~54% use unauthorized tools) and the Green-count→adoption bands are ⚠ practitioner/survey figures cited without a primary link here — treat as directional [VERIFY], not audited. SDT itself is ✅ established psychology.

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../../../UNIVERSAL-SKILL-PROTOCOL.md). At minimum: who are the workers, what AI is being deployed, and what's the resistance pattern (a month 3–4 dip? active workarounds? shadow AI? complaints to HR?). Listen to *how* they resist — "I can't see what it's doing" (autonomy), "I don't trust it with my reputation" (competence), "this makes me replaceable" (relatedness). **Skip** if you haven't selected the AI tools yet (run `ai-use-case-readiness` first). Then route depth and output format.

## SELF-DETERMINATION THEORY, APPLIED TO AI

Three needs, and what breaks each:

- **Autonomy** — control over your work. AI strips it when the worker *must* accept the AI's decision; they feel the system owns their work.
- **Competence** — feeling skillful and able to meet challenges. AI strips it when it hides *how* it reached a decision; the worker can't learn, can't defend the answer, can't improve.
- **Relatedness** — belonging and being valued. AI strips it when it's positioned as a replacement ("this will replace 30% of support staff"); the worker feels disposable.

Systems that protect all three see high sustained adoption; systems that violate even one see it decay by month 6 (⚠ directional). AI *can* protect all three — most don't, because teams build for capability, not for need protection.

## THE AWARE DIAGNOSTIC

For each touch point, score five dimensions Green (protected) / Yellow (at risk) / Red (violated):

| Dim | Question | Red flag | Green flag |
|---|---|---|---|
| **A — Autonomy** | Does the worker control how they work, or does the AI dictate it? | "The AI decides, the worker executes" | "Worker can override, modify, or choose the output" |
| **W — Work identity** | Is the AI positioned as replacing or assisting? | "This AI will handle 70% of tickets" | "The AI handles routine cases; you handle complex ones" |
| **A — Affiliation** | Does the worker belong to a team, or compete with the AI? | "We measure how many tickets the AI handles *without* a human" | "We measure how well worker + AI solve tickets together" |
| **R — Routine/expertise** | Can the worker learn, or is the reasoning a black box? | "The AI's decision is a black box" | "The worker can see how the AI reasons and learn its patterns" |
| **E — Expertise recognition** | Is the worker's judgment still valued, or is the AI the authority? | "The AI's score is the decision; the worker implements it" | "The worker's judgment is the decision; the AI's score is input" |

**The pattern (⚠ directional):** 5 Green → high sustained adoption · 3–4 Green → mid adoption with friction · 2 Green → low adoption, workers turn to shadow AI · 0–1 Green → active resistance.

**Then name the dominant violation** — usually one or two needs drive it. *"I can't explain the AI's output to the customer"* → **competence**. *"I'm just clicking approve; I have no choice"* → **autonomy**. *"This is going to replace me"* (even if untrue) → **relatedness**. And if workers use shadow AI, interview them: "what does the unauthorized tool let you do that ours doesn't?" — the answer names the violated need.

## REDESIGN TO PROTECT THE NEED

Don't redesign the model yet — redesign the *deployment and workflow*. Each fix has a one-question test:

- **Autonomy violated** → add explicit decision gates (override/modify/reject), and let the system learn from the worker's choice. *Test: "Can I change the AI's decision?"* Example: "AI routes, worker implements" → "AI recommends with reasoning, worker confirms or changes, system learns."
- **Competence violated** → make the reasoning visible and learnable. *Test: "Can I explain this decision to a colleague?"* Example: bare decision → decision + top-3 reasoning factors + links to similar past cases.
- **Relatedness violated** → position it as "worker + AI team," and measure that way. *Test: "Do I feel my job is secure?"* Example: "AI handles 50% of tickets" → "This frees you from routine triage for complex work and mentoring; we measure 'solved by worker + AI,' not 'by AI alone.'"
- **Routine/expertise violated** → build a feedback loop the worker improves from. *Test: "Am I learning something new each week?"* Example: "AI decision is final" → "weekly digest of the error patterns the AI catches, so you can spot them before it does."

## WHERE THIS SKILL MEETS THE REST OF YOUR STACK

- **`rtp-attitudinal-segmentation`** — segmentation ships to the *stance* (Embracer/Neutral/Skeptic); this diagnoses the *need* under a Skeptic's resistance. Diagnose the need here, ship the default there.
- **`rtp-adoption-launch`** *(owns the curve)* — the surge→dip→rebound adoption *motion* and its phase-by-phase support live in adoption-launch; needs-guard supplies the *why* behind the dip (which need broke). Hand off to it for the phased plan — don't re-teach the curve here.
- **`rtp-ai-use-case-readiness`** *(upstream)* — select and right-size the AI tools before diagnosing need violations; a badly-scoped tool violates needs by construction.
- **`rtp-problem-type`** — a need violation is textbook *adaptive challenge* (requires people to change, not a better build); problem-type classifies it, needs-guard names the specific need.
- **`rtp-eval-framework`** — rule out the honest case first: if workers resist because the AI genuinely produces bad results they'll be blamed for, that's a quality problem, not a need violation — validate performance before redesigning the deployment.
- **`rtp-first-principles`, `rtp-bias-spotter`** *(imports)* — strip the "they resist change" story to the atomic need at stake, and catch the fundamental attribution error driving it.

## REALITY CHECK

- **Diagnosing without worker input.** You run AWARE yourself, conclude "autonomy," redesign — and they still resist, because you diagnosed the symptom, not the lived experience. Interview 10–15 resisters or shadow-AI users; their answers beat your inference.
- **Assuming all workers share a need.** Senior staff may prioritize autonomy (they want to mentor); juniors may prioritize competence (they want to learn). Segment the diagnostic by persona.
- **Confusing adoption with forced compliance.** Month-1 adoption is deceptive; what matters is month-6 use *when no one's watching*. Measure voluntary adoption, not access.
- **One-time training won't fix a need violation.** Training solves "they don't understand the AI"; it fails on "the AI violates a need." Distinguish capability problems (train) from need problems (redesign).

## QUALITY GATE

- [ ] AWARE diagnostic completed for each major touch point
- [ ] Dominant need violation(s) named
- [ ] Specific redesigns proposed to protect the need (not "communicate better")
- [ ] A feedback loop for continuous worker improvement is included
- [ ] Worker personas considered (not one-size-fits-all)
- [ ] Success metric is voluntary use, not deployment access

## WHEN WRONG

- **Resistance isn't about needs** — sometimes it's poor training, missing digital skills, or genuine usability problems. Run user testing alongside; if they can't figure out the UI, that's UX, not needs.
- **The AI is genuinely unsafe and workers are right to resist** — the issue is AI quality; validate with `eval-framework` before touching the deployment.
- **Leadership has actually decided to cut headcount 30%** — redesigning to "protect autonomy" won't move adoption; workers sense when the story ("focus on complex work") doesn't match reality. Fix the strategy first.

## TRADE-OFF LEDGER

By redesigning the deployment to protect psychological needs, you bet that sustained adoption and discretionary effort rise when workers' needs are protected. You give up speed (add ~2–3 weeks for interviews, redesign, persona validation) and *absolute* automation — "AI handles 50%" becomes "AI handles 70% but the worker has override," which lowers throughput metrics and raises quality-and-learning metrics. **Reversible?** Yes, at the deployment layer — revert and re-diagnose if it doesn't land. **The hidden trade:** protecting needs *keeps humans in the loop*, so if your only metric is AI throughput, this will look like a regression; if your metric is worker+AI quality, it's a gain. **Confidence: High** (SDT is well-validated ✅; the AI-specific stats are ⚠). What would change it: a deployment that violates every AWARE dimension and still hits 60%+ voluntary adoption.

## CONCLUSION

Follow the Conclusion Protocol ([Universal Skill Protocol](../../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 5): state the recommendation (run AWARE before blaming workers; name the violated need; redesign to protect it), the hypothesis (workers voluntarily adopt when the three needs are protected; we're wrong if a 4–5-Green deployment still dips by month 3), the biggest risk (a wrong diagnosis, or a need so fundamental — "this automates my job away" — that redesign can't fix it, meaning the problem is strategy), and the next action: **interview 10–15 resisters or shadow-AI users, ask "what's missing for you in the official system?", map answers to AWARE, redesign from that evidence.** Hand off to `adoption-launch` for the phase-specific support plan.

## VISUAL SUMMARY

After the primary output, invoke the **excalidraw-svg** skill for one visual: the AWARE diagnostic as a five-spoke radar (each spoke Green/Yellow/Red) with the three underlying SDT needs (autonomy / competence / relatedness) labeled beneath the spokes they map to, and a small before→after workflow strip showing one need being protected (e.g., black-box decision → decision + reasoning + similar cases). So a viewer sees which need is broken and what protecting it looks like. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.
