---
name: ai-use-case-readiness
version: v2.0_latest
description: "Right-size the autonomy for a use case — the minimum that captures the value, not the maximum you could build. The question is never 'can we make this autonomous?' but 'what's the least autonomy that still works?' — because autonomy is a governance question, not a capability one: you CAN build a level-5 agent; cost-of-error, verifiability, and policy decide whether you SHOULD. Runs a 5-phase diagnostic — 12 questions, the 0–7 spectrum, two matrices, a floor/ceiling gap, a phased roadmap — output framed as a testable hypothesis, not a rubber stamp. Use when a team says 'let's build an agent', or when 'can it be autonomous?' is asked before 'should it be?'. Do NOT use for a monolithic undecomposed use case (first-principles first) or a pure tech-stack choice. Pairs with: problem-ai-fit (whether AI at all), autonomy-spectrum (quick level reference), determinism-compass (what stays deterministic), cost-model (control-burden economics). Triggers: 'let's build an agent', 'how autonomous', 'can this be an agent'."
imports:
  - first-principles
  - determinism-compass
  - autonomy-spectrum
---

# AI Use Case Readiness

**The objective:** determine the right-sized autonomy for a use case — the minimum that captures the value, not the maximum you could build — for the PM or team about to say "let's build an agent."

> "Almost any feature has some positive return. The only question that matters is: is this the *absolute best* use of our finite resources?" — Shreyas Doshi

## The one idea

A team builds a level-5 autonomous agent for a workflow that is 80% stable rules and 20% exceptions. It works. It demos beautifully. And it costs ten times more to build, control, and maintain than the level-2 system that would have done the same job. Impressive, and wrong.

That is **autonomy theater**, and it comes from asking the wrong question. The instinct, when agents are novel and well-funded, is to look at a use case and ask *"can we make this autonomous?"* The right question — the whole skill — is *"what's the minimum autonomy that captures the value?"*

Here's the mechanism that makes the wrong question so seductive and so expensive: **autonomy is a governance question, not a capability one.** You CAN build a level-5 agent — the model can write the SQL, call the API, take the action. Whether you SHOULD is decided by three other things entirely: what a wrong action costs, whether you can verify correctness before the damage lands, and what policy allows. "The system can act" and "the system should act" are different sentences, and the gap between them is months of engineering and a completely different trust model.

So this skill sizes autonomy from the bottom up. It starts at "no AI" and moves up only as far as the value genuinely requires and the controls genuinely allow — because harder problems (high tacitness, high cost-of-error) usually need *more* human judgment, not less. The output is never a rubber stamp; it's a testable hypothesis: "level X is right-sized because [reasons]; we're wrong if [counter-signal]."

## How to use this skill

Five phases — enter at whichever point matches what you already know. It is a **parameter-driven diagnostic, not a linear checklist**: activate the questions and matrices that actually drive *this* decision.

1. **GROUND** — anchor in the customer's reality (skip if carried from problem-ai-fit).
2. **DIAGNOSE** — decompose the use case into sub-tasks; run the diagnostic questions.
3. **ASSESS** — place it on the autonomy spectrum and the two matrices.
4. **DECIDE** — set the autonomy floor and ceiling; state the recommendation as a hypothesis.
5. **PLAN** — phased roadmap, controls, operating model.

A quick assessment is Ground + Risk questions + one matrix. A comprehensive one runs all of it.

## KEY TERMS (plain language)

- **Autonomy level (0–7)** — how much the system does on its own, from deterministic rules (0) to fully autonomous across domains (7); each step up costs more to build, control, and trust.
- **Autonomy floor** — the minimum sophistication needed for the task to work at all.
- **Autonomy ceiling** — the maximum autonomy that's *safe* given current controls. When the floor is above the ceiling, you have a real problem to resolve, not a design to ship.
- **Need for agency** — how much dynamic planning, judgment, and exception-handling the work genuinely requires. High agency need ≠ high autonomy allowed.
- **Control burden** — how hard it is to let the system act *safely* (driven by cost of error, verifiability, reversibility, consequence breadth).
- **Explicit vs. tacit knowledge** — codifiable rules vs. expert judgment that resists capture. High tacitness usually means *more* human review.
- **Verifiability** — whether you can check correctness before action, right after, only later, or not at all. Your primary control lever: if you can't verify, you can't control.
- **Autonomy theater** — building a high-autonomy agent for work a low-autonomy system would do better; the central failure this skill prevents.

## GROUNDING (Before Starting) — Phase 1: GROUND

Follow the [Universal Skill Protocol](../../../../UNIVERSAL-SKILL-PROTOCOL.md). Anchor in the human truth before assessing autonomy — an elegant autonomy matrix for a workflow nobody cares about is waste with extra steps. If you came from problem-ai-fit, carry these forward; otherwise answer them:

1. **Who exactly is the user?** Name the person ("Tier-2 support agents handling billing disputes"), not "the business."
2. **What's the actual job, in their words?** What they'd say at lunch, not "leverage AI for process optimization."
3. **How do they do it today, and what breaks?** The current solution is the baseline you have to beat.
4. **How painful is this — top-5 problem or a nice-to-have?** A perfect agent for their #4 pain won't get adopted.
5. **What happens when the current process fails, and who gets hurt?** This grounds cost-of-error in reality.
6. **What are we saying YES to — and NO to?** If you can't fill in the NO, you haven't made a decision.

Then route output format: **Word** (stakeholder report, default for comprehensive), **Presentation** (review), or **Inline** (quick answer).

## THE TRAP

You will optimize for *maximum* autonomy instead of *right-sized* autonomy. The bias is **agentic hype** — agents are novel, well-funded, and feel like the future. Three variants:

- **Autonomy theater** — a level-5 agent for 80%-stable-rules work; it runs, but costs 10× a level-2 system to maintain.
- **Novelty bias on action rights** — the LLM *can* write SQL or invoke APIs, so you assume it *should*. Execution rights are a governance question, not a capability one.
- **Cost-of-error amnesia** — you run twelve diagnostics on tacitness and variability and forget Q3: "what happens if it's wrong?" High-tacit, high-error domains need human-in-the-loop, not autonomy.

## PHASE 2: DIAGNOSE

**First, decompose.** Restate the job in operational terms (trigger, inputs/outputs, actors, systems, permissions, success metric, consequence-if-wrong), then break it into sub-tasks and rate each on: explicit vs. tacit · advisory vs. executional · cost of error · verifiability · best-fit level. **Critical rule:** if one sub-task is much riskier than the rest, do not let the average hide it — most good architectures are **hybrids** (level 3 for stable parts, level 1 for risky parts).

**Then run the 12 diagnostic questions.** Answer what you can; mark the rest as assumptions (an honest "I don't know" beats a confident guess).

1. **What exact decision or action is being delegated?** ("The system [recommends/decides/executes] X; the human [reviews/approves/overrides].") *Red flag:* "the system decides" but a human reviews every output — that's advisement with friction.
2. **Advise, decide, execute, or execute-with-approval?** Strictly ordered; advising costs nothing if wrong, execution costs a lot. *Red flag:* "approval required" but it defaults to yes after 2 hours — that's execution.
3. **What happens if the output is wrong, late, or fails silently?** Three separate failure modes. *Red flag:* "low cost, we'll fix it later" — when is later? Weeks isn't low cost.
4. **Can correctness be checked before action, right after, only later, or never?** Verifiability is the control lever. *Red flag:* "we'll monitor dashboards" — monitoring isn't verification if the damage already landed.
5. **Which parts are explicit rules vs. tacit judgment?** *Red flag:* "mostly rules" but examples keep needing override — that's tacit masquerading as explicit.
6. **How often do novel cases appear?** Exceptions = cases needing human judgment, and they grow with scale. *Red flag:* "rare now" — how many per month at 10× volume?
7. **Does the environment stay stable mid-execution?** *Red flag:* "stable in the happy path" — errors live in the unhappy path.
8. **Can a bad action be rolled back quickly and cheaply?** *Red flag:* "rollback not possible" → autonomy on that action must be zero.
9. **What permissions and decision rights are required?** The ceiling is what policy allows PLUS what's safe. *Red flag:* "technically possible but policy says no" — governance is the bottleneck.
10. **What's the smallest bounded slice that still creates value?** That's your pilot. *Red flag:* "we need to scale to everything now" — you're piloting, not launching.
11. **What telemetry exists to measure outcomes?** Can't measure it → can't improve or defend it.
12. **Does the economic upside justify the control burden?** *Red flag:* "upside undefined; we're building because we can."

**Then surface your assumptions.** Rate each: **Validated** (measured), **Informed** (expert judgment), **Assumed** (reasonable, untested), **Unknown** (guessing). The test: *if this assumption is wrong, does the autonomy recommendation change?* If yes, it's critical — test it before committing. **Name the assumption that scares you most; test that first.**

## PHASE 3: ASSESS

**The autonomy spectrum (0–7)** — use the *lowest* level that captures the value. (For the full per-level teaching, see the imported `autonomy-spectrum`.)

| Level | Name | The system… | The human… |
|---|---|---|---|
| 0 | No AI | follows deterministic if/then rules | writes the rules, monitors |
| 1 | Rules engine | applies decision trees / business logic | maintains the rules |
| 2 | AI for one task | classifies, extracts, ranks, or generates from one prompt | integrates the output |
| 3 | Copilot | drafts (emails, reports, code); value = speed | reviews, edits, approves before anything ships |
| 4 | Supervised agent | takes multiple actions, escalates ambiguity | reviews outcomes async/batch |
| 5 | Bounded agent | acts within scoped permissions; can't override policy | audits exceptions |
| 6 | Semi-autonomous | acts independently in a narrow, reversible domain | spot-checks; intervenes on anomalies |
| 7 | Fully autonomous | decides and acts across domains, minimal oversight | monitors; handles incidents (rare — only after 0–6 are battle-tested) |

**Default: start at 0–3.** Move to 4+ only if the case genuinely needs dynamic planning, multi-step tool use, or open-ended exception handling.

**The two matrices — always use both.**

*Matrix A — Knowledge × Cost of Error ("how much can we safely automate?"):* explicit + low cost → **automate** (0–1); explicit + high cost → **controlled automation** (1–2, verify before acting); tacit + low cost → **assistive** (2–3, AI recommends); tacit + high cost → **human judgment zone** (level 3 max — AI assists, human decides, do NOT automate). *Key insight: high tacitness implies stronger human review, not higher autonomy.*

*Matrix B — Need for Agency × Control Burden ("how much autonomy can we responsibly give?"):* low agency + low burden → **deterministic automation** (1–2); low agency + high burden → **deterministic + checkpoints** (high burden ≠ needs an agent); high agency + low burden → **bounded/semi-autonomous** (5–6, if narrow + reversible + low consequence); high agency + high burden → **copilot/supervised** (3–4, human stays in the loop).

**Score the operating conditions 1–5** on the dimensions that matter here (numbers structure judgment, they don't imply false precision — "3–4 on tacitness" is useful; "3.72 → autonomy 4.91" is theater): knowledge tacitness · cost of error · verification difficulty · irreversibility · process variability · coordination complexity · environment dynamism · consequence magnitude · decision-rights sensitivity.

**State the four meta-judgments** (don't collapse to one number): **Need for agency** (Low/Med/High), **Control burden** (Low/Med/High), **Implementation effort** (weeks/months/quarters), **Economic leverage** (<$50K / $50K–500K / >$500K or strategic).

## PHASE 4: DECIDE

**Set the floor and ceiling.** Floor = minimum needed to work; ceiling = maximum safe given current controls. If the **floor is above the ceiling**, resolve it four ways: narrow the scope (lowers the floor), strengthen controls (raises the ceiling), delay until controls exist, or accept human-in-the-loop as Phase 1 (level 4 now, level 6 later). The gap is often the most important insight in the whole assessment.

**Watch for agentic false positives** — signs a lower-autonomy design is better: the value is really extraction/routing/templated generation (level 2 is enough); the hard part is bad data or poor integration, not reasoning (fix upstream first); the workflow is too low-frequency to justify the control burden (human labor is cheaper); it "passes internal eval" but can't be verified in production; execution is blocked by policy (solve governance first); the work involves negotiation, relationships, or accountability (humans must own these — agency destroys accountability).

**State the recommendation as a hypothesis** — this is what separates a readiness assessment from a rubber stamp:

```
HYPOTHESIS: autonomy level [X] is right-sized for [use case] because [reasoning].
IF TRUE:  leading indicator [e.g., acceptance >40% in 2 wks] · lagging [e.g., 50% time cut in 2 mo] · control [zero rollback-critical errors]
IF FALSE: counter-signal [e.g., escalation >20%, or users bypass it in 3 wks] · damage [cost/time/trust] · reversibility [timeframe]
DAMAGE IF WRONG: too high [agent takes bad actions; 6-mo trust recovery] · too low [advisory system nobody uses]
PIVOT: raise to [Y] if [positive signals + mature controls]; lower to [Z] if [negative signals or control gaps]
LOAD-BEARING ASSUMPTIONS: 1. [most fragile — evidence level — test by] 2. … 3. …
THE ASSUMPTION THAT SCARES ME MOST: [name it; test first]
```

## PHASE 5: PLAN

**Recommend the operating model** — state solution class now, autonomy level now, ceiling later, readiness band (**Ready now** / **Ready with controls** [name them] / **Assist-only now** / **Not a fit** — rules are better), why-not-one-level-lower, why-not-one-level-higher, human checkpoints, telemetry.

**Recommend level 5+ ONLY when ALL five hold:** (1) genuinely needs dynamic planning/multi-step orchestration; (2) action rights can be scoped safely; (3) outcomes are verifiable or reversible; (4) consequence is bounded enough for learning (errors <$100K or <100 users); (5) economics justify the control burden (>$500K/yr or strategic). If any one is shaky, recommend 3–4.

**Phase the rollout — smallest valuable wedge first.** Phase 1 (level 2–3 assistive, ~20% savings, basic eval, exit at >30% acceptance + zero critical failures) → Phase 2 (level 4 bounded, ~50%, tool design + fallback + audit logs, exit at <2% escalation + <0.5% critical errors) → Phase 3 (level 5–6, ~70%, governance + monitoring + incident response, exit at zero critical errors over 4 weeks + policy approval). Each phase is its own hypothesis. **Controls to specify at every phase:** approvals, policy constraints, eval plan, monitoring, rollback/recovery, auditability, kill switches.

## HARD RULES

1. Recommend the lowest-autonomy design that captures the value.
2. Decompose before scoring — good architectures are hybrids.
3. "Needs reasoning" ≠ "can safely act." Intelligence and autonomy are separate questions.
4. Current readiness ≠ future potential — say *when* it becomes ready, not just that it isn't.
5. Don't reward novelty — if rules or workflow design solve it better, say so.
6. High error cost + low verifiability = human-led, not autonomy.
7. High tacitness ≠ high autonomy — often the opposite.
8. Action rights matter as much as reasoning quality — solve both.
9. Name what must change for the recommendation to change — specifically ("if we build X and measure Y past Z"), not "if policy changes."
10. When evidence is thin, say so — name the critical assumptions and what to test first.

## WHERE THIS SKILL MEETS THE REST OF YOUR STACK

This skill outputs one thing — a right-sized autonomy level, stated as a hypothesis. Trace where that level travels, because "level X is right" is a decision three other skills then have to build, encode, and defend.

**Upstream (settled before you size the level):**
- **`rtp-opportunity-solution-tree`** — usually the skill that *hands you the use case*: a "probabilistic-with-evals" opportunity the tree greenlit arrives here to have its autonomy right-sized. The tree decided *what's worth building*; this decides *how much agency* it gets.
- **`rtp-problem-ai-fit`** — confirms AI is the right approach at all; this skill then sizes the *level*. Carry its customer grounding forward. Sizing autonomy for a use case AI shouldn't own is motion without progress.
- **The substrate question sits even further upstream:** this skill scores individual *use cases* and assumes the data foundation exists. Whether the *substrate* is ready — data vintage, liquidity, reuse, ownership — is a separate question whose pieces live in `build-or-buy`'s data-recency lens and `moat-finder`'s data-liquidity score (both sourced to the Caterpillar/Lenovo "years of data before any model" cases). A dedicated data-foundation-readiness diagnostic is a watch-tier candidate. *(Cross-ref per q2-14 / q2-27, MIT SMR & HBR, May 2026 — substance lands there, not here.)*

**Imports (run inside the diagnostic):**
- **`rtp-autonomy-spectrum`** *(import)* — the quick 0–7 level reference for fast checks; this skill is the thorough diagnostic behind it. (Confirm on autonomy-spectrum's own pass that it carries the full per-level teaching, so this skill's pointer stays honest.)
- **`rtp-determinism-compass`** *(import)* — for the deterministic portions of a hybrid design, and when governance questions dominate the call.

**The downstream chain — who acts on the level, two hops out:**
- **`rtp-invisible-stack`** — the first stop: once the level is set, design the seven-layer architecture to fit it. Autonomy constrains architecture, not the reverse — a level-2 use case doesn't need an agent harness, and building one is the autonomy theater this skill exists to prevent.
- **`rtp-agent-spec`** — the second hop the level actually lands in: "level X, human reviews Y" becomes an encoded autonomy level, confidence threshold, and handoff/recovery spec. Without that translation the readiness verdict stays a slide, not a system; the floor/ceiling gap becomes agent-spec's escalation design.
- **`rtp-cost-model`** — prices the control burden the level implies; a level-4+ recommendation is only real if its unit economics survive the human-in-the-loop review cost.

**Arbitrates the level against a downstream push for more autonomy:**
- **`rtp-agent-risk`** — when the value case argues for higher autonomy than the cost-of-error and verifiability answers allow, agent-risk's proportionality-and-kill-switch test is where the ceiling holds. Where a wrong action is catastrophic and irreversible, this skill's ceiling overrides the autonomy the demo could justify — and that verdict then arms `rtp-ship-decision`'s go/no-go gate.

## REALITY CHECK

- **Autonomy is a governance question, not a technology question** — you CAN build level 5; policy determines whether you SHOULD.
- **Cost of error compounds** — 0.1% error × 10K tasks/month = 10 errors/month. Acceptable?
- **Verification IS the product** — if you can't verify output, you can't scale the system.
- **"Agent" ≠ "autonomous"** — an agent can be supervised (level 4) or advisory (level 2).
- **Hybrid designs are underrated** — level 1 for 70% + level 3 for 25% + level 0 for 5% often beats a pure level 4.
- **ROI must be real** — saving 1 hour/month for 2 months of control-building doesn't work.

## QUALITY GATE

- [ ] Customer reality established — who, what problem, how painful, what we're saying NO to
- [ ] Use case decomposed into sub-tasks, not one blob
- [ ] The 12 diagnostic questions answered (or gaps named with evidence level)
- [ ] Load-bearing assumptions surfaced, rated, and flagged
- [ ] Both matrices completed (Knowledge × Cost; Agency × Control)
- [ ] Four meta-judgments stated; autonomy floor and ceiling identified and the gap explained
- [ ] Recommendation stated as a hypothesis (IF TRUE / IF FALSE / PIVOT), with why-not-lower and why-not-higher
- [ ] Phased path with exit criteria, each framed as a hypothesis; controls named

## WHEN WRONG

- **The use case wasn't decomposed** — run first-principles first; a monolithic input yields a monolithic (wrong) recommendation.
- **You need a tech-stack recommendation, not an autonomy one** — use system-design.
- **The decision is organizational/political** — if the VP already decided "full autonomy," no diagnostic score changes that; have a different conversation.
- **Evidence is too thin** — when the critical assumptions are all "Assumed/Unknown," the framework produces false precision; name the 3 that matter, test them, defer the decision.
- **You're using it as a recipe, not a diagnostic** — if the questions don't help you decide, you need more information, not more framework.

## TRADE-OFF LEDGER

By sizing autonomy from the bottom up, you bet that the least-autonomy design that captures the value beats the most-capable one you could build. You give up the novelty and the demo dazzle of a full agent, and you take on the discipline of decomposition. **Reversible?** The assessment is; a shipped level-5 agent that took bad actions and burned customer trust is a ~6-month one-way door. **The hidden trade:** requiring human review caps throughput — if volume outgrows it, you'll raise autonomy under pressure instead of thoughtfully, so plan the phase gates now. **Confidence: High** that right-sizing beats maximizing; the per-level call is only as strong as the evidence behind the critical assumptions. What would change it: a genuinely low-cost, fully-reversible, high-agency domain where a bounded agent is simply correct.

## CONCLUSION

Follow the Conclusion Protocol ([Universal Skill Protocol](../../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 5): state the recommendation (the autonomy level and readiness band), name the key trade-off (right-sized value capture vs. capability/novelty), acknowledge the biggest risk (the assumption that scares you most), and define the next action (the pilot slice, its owner, and what to measure). When this feeds a downstream skill, carry forward the customer grounding, the recommended level and its hypothesis, and the critical assumptions.

## VISUAL SUMMARY

After the primary output, invoke the **excalidraw-svg** skill for the visuals that carry the story at a glance — a senior stakeholder should follow the recommendation from these alone: the **Autonomy Staircase** (0–7 with the recommended level highlighted, green→amber→red by governance burden), **Matrix A** (Knowledge × Cost) and **Matrix B** (Agency × Control) with the use case plotted, and — when floor and ceiling differ by 2+ levels — the **Floor/Ceiling Gap** bar, plus the **Phased Roadmap** if a phased rollout is recommended. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.
