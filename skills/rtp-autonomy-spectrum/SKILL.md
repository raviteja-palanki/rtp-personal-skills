---
name: autonomy-spectrum
version: v1.7_latest
description: 'Place every AI interaction at the level it deserves, not the highest the model can reach, by asking one question: who decides what happens next, the code or the model? Gives the 7-level spectrum (Feature → Chatbot → Assistant → Copilot ‖ Agent → Autonomous Agent → Multi-Agent), with plain-language ''what the AI does against what the human does'' for each. Also covers the structural shift at Level 4→5 where the model takes over the workflow, consequence-based leveling, leash length and progressive trust, and the effective-against-designed level (the rubber-stamping trap). Use when someone says ''let''s build an agent'', when designing any AI feature, evaluating a competitor, or deciding how much control to hand the model. Pairs with: ai-use-case-readiness (deep governance diagnostic; this is the quick reference), trust-ladder, agent-spec, agent-risk, tool-architecture, agent-harness, judgment-guard. Triggers: ''autonomy level'', ''agent spectrum'', ''how autonomous'', ''let''s build an agent''.'
imports:
  - determinism-compass
  - tool-architecture
  - agent-risk
  - judgment-guard
---

# Autonomy Spectrum

**The objective:** decide, for each interaction in your product, how much the model gets to control — set by the *consequence of it being wrong*, not by what the model *can* do. Autonomy is a design decision, not a capability decision. Target the right level, never the highest.

## THE ONE IDEA

**The only question that sets autonomy is: *who decides what happens next — the code, or the model?*** Everything else follows from where that line falls, and three consequences reorganize how you design:

1. **Set the level from consequence, not capability.** The trap is reverse-engineering autonomy from what the model *can* do ("it CAN check out a cart, so let it"). Start from failure: if it does this wrong, what's the damage, who absorbs it, can we undo it? The right level is the *lowest* one that still delivers the value — because flexibility, cost, and unpredictability all rise together as you climb.
2. **There's a structural shift, not a smooth ramp, at Level 4→5.** Below it, **code controls the workflow** (the model suggests, a human or a rule decides the action). Above it, **the model controls the workflow** (you set a goal and guardrails; it decides what to do, in what order, with which tools). Crossing that line isn't a feature upgrade — it's an architecture change: cost jumps, failure shifts from "wrong suggestion a human catches" to "wrong action that cascades before anyone notices," and monitoring shifts from checking outputs to watching decisions.
3. **Autonomy is per-interaction, never per-product.** GitHub Copilot isn't "a Level 6 product" — it's Level 1 (Tab autocomplete), Level 3 (chat), and Level 6 (issue→PR) at once. The PM question is never "what level is our product?" It's "what level is *this interaction*, given what breaks if the AI fails here?" Every winning product is a deliberate *mix*.

## KEY TERMS (plain language)

- **Autonomy level** — how much the AI decides on its own, from autocomplete (you decide) to a multi-agent system (the model decides what happens next).
- **The structural shift (1–4 vs 5–7)** — below the line code controls the workflow; above it the model does, and cost, failure modes, and monitoring all change.
- **Consequence magnitude** — how bad it is if an action is wrong, and whether it can be undone; the right basis for setting autonomy.
- **Leash length** — how much the agent does without a human stepping in: supervised → spot-check → exception-based → autonomous.
- **Verifiability cut line** — autonomy may rise as far as you can still verify the *setup* (goals, limits, thresholds), and must stop where it would need a human verifying every *output* — which doesn't scale.
- **Progressive trust escalation** — earn leash length through a demonstrated track record; never grant it up front.
- **Kill switch** — a built-in, tested way to stop or reverse the agent fast.

## THE SEVEN LEVELS

The dividing line is the structural shift: below it, code controls the workflow; above it, the model does.

| Level | Type | Who decides? | Example | Cost/interaction ⚠ | Governance |
|:--:|:--|:--|:--|:--:|:--:|
| 1 | **AI Feature** | Code, always | Gmail Smart Compose | <$0.01 | Minimal |
| 2 | **Chatbot** | Code, via decision trees | Scoped support/FAQ bot | ~$0.01–0.03 | Low |
| 3 | **AI Assistant** | Human directs, AI responds | ChatGPT chat, Perplexity search | ~$0.01–0.05 | Moderate |
| 4 | **Copilot** | Human decides, AI *suggests* | GitHub Copilot autocomplete, Cursor Tab | ~$0.01–0.10 | Moderate |
| — | **⚡ STRUCTURAL SHIFT** | **code controls ↑ / model controls ↓** | | | |
| 5 | **Agent** | AI decides *within boundaries* | Deep-research mode, a scoped task agent | ~$0.10–0.50 | High |
| 6 | **Autonomous Agent** | AI decides, humans *monitor* | Claude Code issue→PR, Devin | ~$0.50–$50+ | Very high |
| 7 | **Multi-Agent System** | Distributed AI decisions | Parallel coding agents, cross-domain agent orchestration | $1–$thousands | Maximum |

*(Cost bands are 2026 practitioner order-of-magnitude ⚠, not quotes — they move with model pricing; the point is the ~10× jump at each structural boundary, not the digits. Named products are illustrative and will drift; the level is what's durable.)*

*Why seven and not five: the field converged on 5–6 level scales (the Cloud Security Alliance's Jan-2026 six-level model, most vendor ladders), all adapted from the SAE J3016 driving-automation levels that gave the car industry a shared vocabulary. This spectrum splits their bottom tier into Feature vs Chatbot and their top into Autonomous vs Multi-Agent, because those boundaries carry different governance. Treat the levels as **buckets on a continuum**, not a ladder with clean rungs — real autonomy varies continuously across generalization, collaboration, and oversight, which is exactly why products land on "5–6" and why the same product spans several levels. The convergence of independent authors on nearly the same boundaries is the signal the taxonomy is real; the digit is not the point.*

**The reactive/proactive tells:** a *chatbot* says "I can help with A, B, or C"; an *assistant* says "tell me what you need" and waits; a *copilot* offers help unasked but only *suggests* — it never acts without approval. The word that defines Level 4 is *suggests*. The moment the system takes a consequential action on its own, you've crossed into Level 5.

### What each level actually means — who does what

Read each level as a division of labor between the machine and the person. The line "what the AI does / what you do" is the whole point.

**Level 1 — AI Feature.** A small, fixed prediction baked into a tool you already use.
- *The AI does:* one narrow thing at a set moment — finishes your sentence, flags a likely typo, ranks a playlist.
- *You do:* everything else. You're driving; you accept the prediction or ignore it.
- *Everyday example:* Gmail completing your sentence as you type.
- *If it's wrong:* you just don't press Tab. Harmless.

**Level 2 — Chatbot.** Answers inside a script you wrote.
- *The AI does:* matches your question to a pre-built path or a known answer. It may use a model to understand your words, but the *flow* is coded, not decided.
- *You do:* ask; when you go off-script, you're handed to a human.
- *Everyday example:* a support bot — "I can help with orders, returns, or shipping. Which one?"
- *If it's wrong:* it says "I didn't get that — let me connect you." Low stakes.

**Level 3 — AI Assistant.** Does what you ask, then stops and waits.
- *The AI does:* understands a free-form request and produces an answer or a draft — but only when asked, and it does nothing until you ask again.
- *You do:* decide what to ask, when, and what to do with the answer. Close the tab and nothing happens.
- *Everyday example:* asking ChatGPT to draft an email or summarize a report.
- *If it's wrong:* it can be confidently wrong (a made-up "fact"), but you're reading every answer, so you catch it.

**Level 4 — Copilot.** Suggests while you work; you stay in command.
- *The AI does:* watches your work and offers help unasked — but it only *suggests*. It never takes the action itself.
- *You do:* accept, edit, or reject each suggestion. Your hands stay on the wheel.
- *Everyday example:* GitHub Copilot proposing the next few lines of code as you type.
- *If it's wrong:* the danger is subtle — the suggestion *looks* right, so you may wave it through without checking. This is exactly where rubber-stamping (and the effective-level trap below) begins.

**⚡ — the structural shift. Below: you or the code decide the action. Above: the model decides and acts. —**

**Level 5 — Agent.** You set the goal; it plans and acts within the fences you set.
- *The AI does:* takes a goal, decides the steps and which tools to use, and carries them out — inside boundaries you defined.
- *You do:* set the goal and the guardrails, then review the *result* — not each step.
- *Everyday example:* "research this topic and write me a briefing" — it plans a search, reads sources, and drafts the document.
- *If it's wrong:* it can misread the goal or take an odd step, and because it acted on its own, you may not notice until later.

**Level 6 — Autonomous Agent.** It runs the whole job; you monitor outcomes, not steps.
- *The AI does:* owns an end-to-end task over minutes to hours — plans, acts, checks its own work, retries when it fails — without asking permission along the way. This is delegation, not collaboration.
- *You do:* set it up and watch the outcomes; you don't approve individual actions.
- *Everyday example:* hand it a coding ticket; it reads the codebase, writes code across files, runs the tests, and opens a pull request you review at the end.
- *If it's wrong:* errors compound *quietly* — a 20-step job at 95%-per-step is only ~36% fully correct — and it can mark work "done" that isn't. The failure is silent, not loud, which is why monitoring must watch *decisions*, not just outputs.

**Level 7 — Multi-Agent System.** Several specialists coordinate; no single one owns the whole job.
- *The AI does:* multiple agents split the work, hand off to each other, and coordinate — a supervisor may orchestrate, but each makes its own decisions in its lane.
- *You do:* oversee the *system* and the handoffs between agents, not any single agent's steps.
- *Everyday example:* a claims pipeline — one agent reads the documents, another checks policy, another decides, another drafts the reply.
- *If it's wrong:* everything that breaks with one agent, multiplied — plus new failures where one agent's mistake becomes another's input, and two agents disagree with no rule to settle it.

## THE STRUCTURAL SHIFT — everything changes at 4→5

| | **Levels 1–4: code controls** | **Levels 5–7: model controls** |
|---|---|---|
| What happens | Rules say "when X, do Y"; the model predicts/suggests | You set a goal; the model decides steps, order, tools |
| Who approves actions | Humans — every real consequence needs a human decision | The model, subject to guardrails you set in advance |
| If it fails | You see it immediately; a wrong suggestion looks wrong | You may not know for hours; errors compound and cascade |
| Governance | Check outputs (sampled review) | Watch decisions (real-time alerting, kill switches) |
| Cost | Bounded | Jumps ~10–100× (24/7 monitoring, rollback, kill switches) |

**Analogy:** below the line is a co-pilot who suggests while the pilot's hands stay on the wheel; above the line is a new hire with a job description and authority limits who then works independently — you don't approve each email they send. Most teams underestimate this line and try to cross it as a "feature," then discover it needed different infrastructure, monitoring, and org structure.

## THE VERIFIABILITY CUT LINE — how far autonomy can go

Checking every output by hand cancels the efficiency that justified the AI. So move human judgment *up front*, to the setup — goals, limits, escalation paths, thresholds. The rule:

> **Autonomy may rise as far as you can still verify the *design*, and must stop where it would require verifying every *output*.** You can hand off as far as you can check the setup, and no further.

This predicts *before* you ship why over-reaching rollouts get pulled back — a shopping agent that auto-checked-out was pulled to a human-present mode within months because it had been pushed past the point the setup alone could guarantee the outcome. The leash (below) is *how much* you let the agent do; the cut line is *the ceiling the leash can never cross* — no track record earns autonomy past the point you can no longer check the design. *(When wrong: "can I verify the design?" is itself a judgment call — a team can convince itself it verified a setup it didn't understand. The cut line sets the ceiling, not the guarantee; pair it with consequence magnitude. Source: "Beyond Verification," Renieris, Kiron, Mills & Kleppe, MIT Sloan Management Review, 12 May 2026.)*

## AUTONOMY IS A LEVER, NOT A GOAL

**Do not treat autonomy as a binary switch, and do not treat moving up this spectrum as progress in itself.**

**Design for a deliberate progression** from advisory, to human-in-the-loop decision-making, to full execution rights under oversight. **And expect the progression to be non-uniform across tasks inside the same function.** In structured, low-risk areas such as repetitive analysis or contract validation, an agent moves quickly along the curve. In high-stakes activities such as negotiation, **the agent may stay in a coaching role indefinitely, and that is a finished design rather than an unfinished one.**

**Read that against the cliff finding above and the two fit together.** The optimal arrangement jumps rather than slides, so you cannot plan a smooth migration. **But the jumps happen per task, not per function.** Which means the practical unit of this spectrum is a task, and a function-level autonomy level is an average that describes nothing you can operate.

**The failure this prevents, and it is the most common one in regulated functions.** Where decisions carry contractual or financial consequences, organizations limit autonomy and preserve human approval **so strongly that they neutralize the benefit of the agentic system entirely.** They then conclude the technology underdelivered. The honest read is that they bought a Level 5 system and operate it at Level 2, which is the effective-versus-designed gap this skill already names, arriving through caution rather than through rubber-stamping.

**What to specify before the first agent runs**, rather than negotiating it after a compliance question forces the issue: approval rights, audit trails, escalation paths, and override mechanisms. **Governance is a design parameter here, not a review gate.** A working pilot that cannot scale because the governance layer was bolted on late is the most common failure in agentic deployment.

*(Source: Himmelreich, Oshri, Scala & Zaidani, HBR, "Why Agentic AI Could Transform Procurement," Aug 2026 — ⚠ practitioner-tier for the graduated-autonomy prescription, drawn from interviews with no comparative data against binary-switch deployments. The phrase "autonomy is a lever, not a goal" is the authors' own. Falsifier: a deployment that reached durable value by treating autonomy as a single function-level setting.)*

## AUTOMATION CLIFFS: THE OPTIMAL LEVEL JUMPS, IT DOES NOT SLIDE

**Organizations plan for a smooth trade: slightly better model, slightly more automation.** A formal model of the routing decision says the shape is a step, not a slope.

**The setup.** A coordinator routes a stream of tasks between AI-only, human-only, and AI-assisted review, under a hard constraint on how much human attention is available, and the reviewer chooses how much effort to spend. The reviewer's effort is not fixed, which is the part most models omit and the part that produces the result.

**The finding.** While the model sits below human performance, **many arrangements can be optimal, including human-only.** Once it crosses key performance thresholds, the equilibrium shifts abruptly toward AI-only. **Small technical improvements trigger large reallocations of work.**

**What that means for anyone running this spectrum.** Your current level is not a point you will slide along. It is a plateau you will sit on until a threshold is crossed, and then the right answer moves several levels at once. **Two consequences:**

1. **Do not plan a level-by-level migration.** A roadmap that moves Level 3 to Level 4 next quarter and Level 4 to Level 5 the quarter after is modelling a slope that does not exist. Plan the plateau you are on and the jump you would make.
2. **Know your thresholds in advance.** The jump is triggered by a measurable crossing, so the useful preparation is naming which metric at which value would move you, before a release forces the question.

**And the conclusion the authors draw, which cuts against the default:** adding human-in-the-loop steps feels safer and is not always better. Stretch people across too many AI-assisted decisions and the expected gains do not materialize. **The right strategy is sometimes full automation, and sometimes no AI at all.** Collaboration is a design choice, not a responsible default.

*(Source: Gu, Li & Zhu, reported as "Out of the Loop?," Jul 2026 — ◆ a formal model, and the authors state plainly that future work should include empirical validation using data from real workflows. **Nothing in it has been tested against a running system.** Carry the structural insight, not a prediction about your own thresholds. Falsifier: a real deployment whose optimal human-AI arrangement shifted smoothly as model quality improved.)*

## THE JUMP FROM ASSISTANT TO AGENT IS NOT A STEP ALONG THIS SPECTRUM

**Two dimensions separate an assistant from an agent, and both have to move.** Autonomy is how long the product runs unattended. Context integration is how many digital environments it can read from and write to. Assistants sit low on both, agents high on both. **That combination is what turns "answer my question" into "do the job."**

**What measurement shows when a team crosses it, and the third number is the one nobody plans for:**

| What changes | Observed shift |
|---|---|
| **Machine work per session** | Roughly 40 to 48 times as much. The agent pauses far more often and is stopped no more often. |
| **Task time and cost** | Roughly 87% less time and 94% less cost, modelled against an assistant-plus-human workflow. |
| **The work people attempt** | More cognitively demanding, spanning more knowledge domains, crossing occupational boundaries. **A large block is work nobody attempted with the assistant at all.** |

**The user's posture changes from operating to supervising**, and the pause-versus-stop split is the evidence: the agent asks far more often and gets halted no more often, which means the human is answering rather than steering.

**The management consequence, and it is the reason this belongs in a leveling skill.** A dashboard tracking time saved will faithfully report the efficiency gain and be completely blind to the scope change. **The efficiency number is real and it is the least interesting of the three.** The one that changes your roadmap is that people started attempting work they previously did not attempt at all, because that is new demand, not a cheaper version of old demand.

**What to do with it when you level a product:** if you are moving a feature from Level 3 or 4 up to Level 5, instrument the scope change before you ship, not after. Log what tasks users bring, not only how long they take. Otherwise your first read on the upgrade will be an efficiency figure and your second read, six months later, will be a surprise about what the product is now used for.

*(Source: HBR, "Research: How AI Agents Broaden the Scope of Knowledge Work," Jul 2026 — ◆ study-disclosed. The time and cost reductions are modelled against a counterfactual workflow rather than measured against a running one, so treat 87% and 94% as directional. The 40-to-48x machine-work range and the pause-versus-stop split are the more solid observations. Falsifier: an assistant-to-agent upgrade where the mix of tasks users attempt stayed the same and only throughput moved.)*

## THE EFFECTIVE LEVEL — what you operate at, not what you designed

**The most dangerous gap in this whole framework: the level you designed is not the level you are running if people rubber-stamp.** A product built as a Level 4 copilot (the AI *suggests*, a human *approves*) quietly becomes a Level 5 agent the first time operators approve without reading. You wrote a Level 4 safety case and are now operating at Level 5 without one. Automation bias makes this drift the default, not the exception: when the AI is usually right, the human stops being a checkpoint and becomes a click. Five things follow:

- **Measure the effective level, not the designed one.** A high acceptance rate with near-zero edit or override rate on consequential actions is the tell that your "Level 4" is really a Level 5. Over-trust is a failure mode, not a success signal (`ai-product-metrics` treats acceptance-with-zero-edits as an anti-metric for exactly this reason).
- **A human checkpoint is not automatically a control.** "Keep a human in the loop" and "train people to be skeptical" fail two ways — under volume they rubber-stamp, and when the model argues back they get talked out of the correction (active persuasion, not just passive bias). What actually holds is *structural*: independent human analysis *before* the AI's answer is shown, a parallel check, or a clean split between AI-drafting and final human judgment. Design the friction; don't exhort people to resist. (This is `judgment-guard` and `trust-under-fog`.)
- **"Humans monitor" at Level 6 decays — the supervision paradox.** The longer an agent runs on its own, the more the overseer's own skill fades, so when the rare edge-case failure finally arrives, the monitor has the *least* context to catch it. "Humans monitor" is not a stable control unless you design the monitor's engagement on purpose — rotation, spot-checks that require real work, state-first review — or it becomes "humans watch a dashboard they no longer understand" (`judgment-guard`).
- **A cheap three-answer self-test surfaces rubber-stamping before you measure it.** Ask whoever signs off on a consequential action who decided it: "the code decided," "I decided and the model only drafted," or **"the model is the default and I am only the ratifier."** The third answer is the tell. It describes ratification, not judgment, and it means a "Level 4 copilot" is running as an unacknowledged Level 5 agent. *(Source: HBR, "Our Favorite Management Tips on Decision-Making," Jun 2026, n=10, ⚠ weak evidence, a diagnostic prompt rather than a validated instrument. When wrong: a ratifier with real rejection power and a demonstrated track record of using it is still exercising judgment; use the acceptance/edit-rate metric above as the tiebreaker, not the self-report alone.)*
- **The slack test: widen a hard-coded threshold and watch the distribution, not the mean.**

  Telemetry alone cannot tell you whether a number reflects a judgment the system is making or a rule it is merely obeying. This test separates them.

  **How to run it.** Take a designed threshold: a refill-reminder window, a discount cap, an escalation delay. Widen it. Then watch two things:
  - Does behavior move toward the new boundary?
  - Does the guardrail still hold?

  **How to read it.** If both are true, the original threshold was constraining judgment rather than matching it, and **your effective level is lower than your designed one**. If behavior does not move, the threshold was already loose enough.

  **The case.** A pharma team widened a medication refill-reminder window from 7 to 14 days and saw exactly this shift (◆ company-reported, single case, roughly 65 frontline-worker survey respondents). The mechanism generalizes past pharma. The specific 7-to-14 number does not.

  *(When wrong: never run this on a hard compliance or safety ceiling. Widening a dosage limit or an irreversible-action cap to "test" it turns a measurement instrument into the incident it was meant to prevent.)*

And a capability caveat that compounds all of it: **you cannot read the model's competence off a task's apparent difficulty.** The frontier is *jagged* — models are superhuman on some tasks and surprisingly poor on others that look just as easy. So "this seems simple, raise the autonomy" is exactly as wrong as "the model is smart, raise the autonomy." Set the level from *measured* performance on *that* task, never from how hard the task looks or how capable the model seems. *(Sources: 2026 human–AI reliance research on the deployed-tier-vs-procured-tier gap and active over-reliance; the jagged frontier, Mollick, 2023–2026.)*

## DOES THE SPECTRUM MATURE? — the map is stable; your position moves

As long-running harnesses and stronger models improve (Claude 4.8, Fable 5, GPT-5.x), the natural question is: do the levels themselves change? **No — the map is stable, because "who decides what happens next" is a permanent question. What matures is (1) how *reliably* you can operate at a level and (2) how *far up* the spectrum is safe to reach.** Three moving parts, none of which move the map:

1. **Reliability-at-a-level climbs fast.** Anthropic's Claude Code nearly *doubled* its unattended run time in one quarter (under 25 min → over 45 min, Oct 2025 → Jan 2026 ⚠); Fable 5 now runs *for days*, and Stripe reported it migrating a ~50M-line codebase in a day, a task quoted at ~2 months for humans (◆ vendor-reported, single case). A Level-6 coding agent that needed constant babysitting in early 2026 runs hours-to-days on its own now. The *level* (you monitor, it acts) is unchanged; the *cost and friction* of sitting there dropped.
2. **The safe ceiling rises — unevenly.** The frontier of what's safe to run autonomously moves up (robust days-long L6, dependable parallel L7 subagents). But maturation is *jagged and domain-specific*: coding autonomy matured dramatically while a regulated-finance L5 may not have budged, because the ceiling is set by **consequence + verifiability, not model capability** (the verifiability cut line doesn't move just because the model got smarter). Don't let a benchmark win in one domain justify raising autonomy in another.
3. **Governance flips from tax to enabler.** The 2026 pattern is *adaptive governance* — agents get *promoted* to higher autonomy only when their performance logs prove stable precision (this skill's progressive-trust escalation, now the industry default). Mature governance is what *earns* the climb; it's the thing that lets you raise the ceiling safely, not the toll for doing so.

**The trap this predicts:** the gap between marketing and reality persists — most *production* deployments in 2026 still sit at Level 1–2 while vendor marketing implies Level 3–4. So "the models matured, so we're at Level 6 now" is a capability claim masquerading as a deployment fact. Track your *effective* level (above), not the frontier's.

**The strategic read (connect to `capability-tracking` + `harness-operating-model`):** because reliability-at-a-level keeps improving, the *governance scaffolding* you build to make a level safe today is partly scaffolding a maturing harness will absorb — build it cheaply, expecting to simplify it. But the *judgment of where to sit on the spectrum* (consequence, verifiability, effective-level discipline) is permanent — that's the part worth investing in. The levels don't dissolve; the babysitting does.

## SETTING THE LEVEL — consequence magnitude & the leash

**First, decompose the decision.** Split it into its narrow subdecisions and its wide wrapper (see `problem-ai-fit`, engine-vs-helper): the narrow cores can take an engine-grade level; the wide wrapper stays human-led however capable the model looks. Then map each action:

| Action class | Consequence | Control requirement |
|---|---|---|
| Reversible, low | undone easily; <$1; noticed immediately | Agent acts freely; logging optional |
| Reversible, medium | undoable; $1–100; noticed within hours | Agent acts with mandatory logging; human audits within 24h |
| Reversible, high | undoable but costly; $100–10k; harm cascades | Explicit human approval *before* the action |
| Irreversible, medium+ | cannot undo; >$10k; permanent | **Agent cannot access. Period.** |

*(This is the leash-setting view; the per-tool contract that enforces it — reversibility class, permission scope, kill switch — is designed in `tool-architecture`. Set the level here; enforce it there.)*

**Leash length** = how much the agent does without a human: **Supervised** (approve every decision — learning phase / high magnitude) → **Spot-check** (audit a random sample post-hoc — reversible, calibrated confidence) → **Exception-based** (act within domain, escalate on low confidence/anomaly — high-accuracy domain, predictable failure) → **Autonomous** (monitor dashboards only — proven track record AND low magnitude AND explicit user consent).

**Progressive trust escalation — earn the leash, don't grant it:** start Supervised → after a clean streak move to Spot-check → then Exception-based → consider Autonomous only if consequence magnitude is low. Any error resets the streak (regress one mode, not to zero); never auto-raise past the domain boundary; re-certify on a schedule; and expose the record to the user ("246/247 correct; last error [date]; recommending exception-based for 30 days") so autonomy never escalates by surprise. *(Track-record thresholds are design choices, not universal constants — calibrate to your error cost.)*

**Context anxiety** — decision quality degrades *nonlinearly* as the context window fills, well before 100%. Drop autonomy by a level around 40–60% utilization, go advisor-only by 60–80%, read-only past 80%, and alert automatically at the threshold. *(Anthropic finding ⚠; measure your own knee.)* And design **rollback before you deploy**: if you can't undo an action within its window, the agent doesn't get access to it.

## ALLOCATING *YOUR OWN* WORK — the four-mode table, and a usable entry gate

The seven levels set the machine's autonomy on a task. This is the same decision pointed at a person's own week, and it is the version an operator can act on tomorrow. Four modes, each naming what is at stake if you get it wrong:

| Mode | What's at stake | Use it for |
|---|---|---|
| **1. Leader-owned** | your judgment | high-stakes decisions where diagnosis, trade-offs, accountability or trust are central |
| **2. Leader-shaped, AI-assisted** | your voice | communications where AI helps with structure and you author the meaning |
| **3. AI-enabled, human review** | your presence | repeatable work where AI handles volume and you stay close to the original signals |
| **4. AI-handled, bounded** | your capacity for deeper thinking | lower-risk, specific work, including agentic workflows, where errors can be identified and corrected without substantial cost |

**The point of deciding in advance is that the transfer becomes a choice instead of a drift.** Work migrates upward through this table one small, reasonable-looking increment at a time, and nobody ever decides to hand over their judgment.

**A concrete entry gate for mode 4**, from a practising COO, in order:

1. Is the work specific enough to define clearly?
2. Can the team tell what a good result looks like?
3. Will an error be easy to spot and inexpensive to correct?
4. Is this internal, routine work, or work where AI will publicly represent the company?

Worked boundary from the same source: routing inbound requests and drafting first-pass answers to common product questions sit **inside** mode 4. Writing a key customer an apology after a service outage sits **outside** it, because the tone of that message affects the whole relationship.

**Read the gate critically, because it has a hole.** All four questions are **error-cost** questions. **None of them is a reversibility question**, and none asks who is accountable when the bounded work goes wrong. A cheap-to-correct error in an irreversible action is still irreversible: sending is cheap to detect and impossible to undo. Add the two missing questions before you use this gate on anything outward-facing:

5. **If this is wrong, can the action be undone, or only apologized for?**
6. **Who is answerable, and can they actually alter the outcome?** (See `rtp-responsible-ai-program` on alterability.)

**Two named risks that arrive with mode 3, and they are why "human review" is not a safety guarantee.** **Over-reliance**: "When these distillations arrive continuously and usually look right, review becomes routine. Leaders skim where they once read and approve where they once interrogated." **Distance**: "A synthesis can make you feel like you understand a situation when, in reality, you've lost touch with it." Mode 3's stated stake is your presence, and those two mechanisms are how it is lost while the review box stays ticked. Route to `rtp-judgment-guard`, drain 7 and checkpoint 3.

*(Source: HBR, Lancefield, "Don't Let AI Flatten Your Leadership Style," Aug 2026 — ⚠ anecdote-tier throughout. The four-mode table is the author's own, presented with no evidence of any kind; the COO's four questions are attributed to a single unnamed practitioner. Carry both as a **useful external taxonomy the corpus does not otherwise have**, and do not cite them as findings. The two added questions and the error-cost critique are this corpus's.)*

## THE EXERCISE-FED EXCEPTION — when the default inverts

Every level above assumes the same direction: shed execution, keep judgment. Climbing from Level 4 to Level 5 hands the model the doing and leaves you the goal and the review; the four-mode table above does the same to a person's own week. That default inverts when a capability is **exercise-fed**: built and maintained by a human actually doing the work, not by reviewing someone else's or something else's output. There, automate the decision and keep the human doing the execution, because the execution is the mechanism that maintains the skill, not overhead the decision could be extracted from.

**Condition for when this applies:** the capability compounds through repeated hands-on doing (reading the film, drafting the reply, running the diagnosis), not through repeatedly being handed a decision to ratify. A decision-fed capability, where judgment sharpens from making the call rather than from doing the manual steps, still follows the standard default: automate the execution, keep the human deciding.

*(Source: Dan Wang on the HBR IdeaCast, on process knowledge, 2026, framing-tier evidence. Treat this as a named exception to test against one specific capability, not a reversal of the spectrum's general direction. When wrong: most execution in most workflows is decision-fed, not exercise-fed, so inverting the default there just re-imports the toil this whole framework exists to remove.)*

**A second, independent case, with no AI system present.** School of Rock's Method App centralized the input layer of music instruction (a legally cleared song and show library) and left the execution layer (actual teaching) untouched and local. Teaching musicianship is an exercise-fed capability: instructors form judgment by doing the work repeatedly, not by reviewing someone else's decision about it. The company's design choice, standardize the ingredients, never the recipe's execution, is this exception's own prescription, reached without any model involved. This strengthens the exercise-fed exception by showing it is not an AI-era discovery but a general design principle AI happens to make more visible; it would be wrong to cite as proof the exception applies broadly, since it remains a named exception to test against one specific capability. *(Source: HBR Cold Call, "How School of Rock Created Structure in Order to Scale with Agility and Creativity," Jun 2026.)*

## THE LAUNCH GATE FOR ANY SYSTEM THAT CAN CONTRADICT A HUMAN

The levels above answer *how much the machine decides*. This answers a question they skip: **when the machine disagrees with the person, who wins, and what gets written down.**

**Why "copilot, not autopilot" does not settle it.** One asset manager states that objective plainly, then describes an agentic analyst that can "independently analyze nuanced topics, fact-check humans, and offer contrarian viewpoints." **A system with standing to fact-check a portfolio manager and argue the other side is not a copilot in the sense the phrase implies.** It is a second analyst with dissent rights.

**"Copilot, not autopilot" has become the enterprise phrase for "we have not settled the autonomy question,"** and it is load-bearing in exactly the places a decision is needed.

**Two things to name before launch, not after:**

1. **The resolution rule.** When the model dissents and the human proceeds anyway, is that allowed, allowed-with-sign-off, or blocked? Name it per decision class.
2. **The log record.** What is written when a human overrides a model's contrary read?

**Why the log is not optional.** If the model flags a contrarian view, the human proceeds, and the position loses money, **that disagreement record is either a governance asset or a litigation exhibit.** Somebody should decide which in advance, and by default nobody does.

**The inverse of the usual question, and worth stating plainly.** Most governance work asks who can stop the model. This asks **who overrules the human when the model disagrees.** Both need an answer, and only the first one usually gets one.

**When this is wrong:** a system with no standing to dissent, one that only ranks or drafts, does not need a resolution rule. The gate applies the moment the output can be read as a contrary judgment rather than a suggestion.

*(Source: HBR, "Transforming Investing With AI at Franklin Templeton," Jun 2026 — ◆ single company, self-described, and the article does not notice the tension. Both the observation and the gate are this corpus's. Pairs with `rtp-trust-ladder`.)*

## PRODUCTS ARE MULTI-LEVEL BY DESIGN — three patterns

The Copilot blueprint: one product, three autonomy contracts made explicit in the UI — Tab (L1, passive) · Chat (L3, reactive) · issue→PR (L6, delegated). Users understand the boundaries because the interface makes each mode distinct. Three patterns recur across the products that win:

1. **Progressive disclosure of autonomy** — start users at L3, let them succeed, offer L4 as a natural step, surface L5+ only to users who've shown they understand the tool. Nobody starts at L6; products that *demanded* L5–6 trust from users with zero L3 experience (the standalone-hardware attempts) failed. Don't change the workflow AND raise autonomy AND introduce a new tool at once — change one thing at a time.
2. **Model-agnostic architecture** — build for the *task*, not a specific model's quirks. A model-agnostic layer means the product improves automatically when the next model ships, and survives a vendor outage by swapping providers; a model-locked product needs a rewrite. (The evaluation infrastructure that lets you compare models across your real workflow is the harder-to-copy moat — see `harness-operating-model`.)
3. **AI-as-core vs AI-as-add-on** — bolting AI onto an existing UI caps your autonomy ceiling (an add-on can't reach the full data model); rebuilding with AI in the data model unlocks higher autonomy but costs more and is harder to reverse. Both are valid — but they lead to very different ceilings, so choose deliberately.

## OUTPUT — WHERE YOU ARE ON THE SPECTRUM

The deliverable is not a single number for the product. It is a **"you are here" map** that states, for each meaningful interaction, the level it operates at *today* (with evidence), the level you *recommend* (with the reason), and the honest unknowns. Three parts:

**1. The per-interaction table** — the backbone:

| Interaction | Designed level | **Effective level today** (evidence) | Recommended level (why) | Consequence if wrong | The move / open question |
|---|:--:|:--:|:--:|---|---|
| e.g. Returns triage | 4 | **~5** — 96% accept, <2% edit → operators rubber-stamp | 5, *with* a structural check | wrong refund, reversible ≤$X | Add pre-action gate on >$X; else it's an un-cased L5 |
| e.g. Billing disputes | 3 | 3 | 3 (needs human judgment) | legal/─reputational | Hold at 3 |
| e.g. Doc drafting | 5 | 5 | 5→6 *candidate* | low, reversible | **Open:** can we verify the setup? decision needed |

Always show **designed vs effective** side by side — the gap is the finding.

**2. The "you are here" marker on the spectrum.** Place the product's interactions on the 1–7 line as dots, and mark two things: where each sits *now* and where it's *recommended* to go (an arrow). Use a **range**, not a point, wherever the honest answer is a band — "operating at 4, drifting toward an effective 5," or "5–6, depending on task complexity." A single confident dot where reality is a range is a false precision that hides the risk.

**3. Flag what's still undecided.** Not every interaction resolves to a clean level. Where it doesn't — a candidate L5 whose *setup verifiability* is unresolved, or a case where legal/compliance hasn't signed off on the effective level — mark it **OPEN: decision needed**, name who owns the decision, and say what evidence would settle it. A map that hides its open questions is worse than one that names them.

**Multiple diagrams are appropriate** and often clearer than one: (a) the spectrum line with current-vs-target markers and ranges; (b) the per-interaction table as a heatmap; (c) a designed-vs-effective delta chart that makes rubber-stamping visible. Draw whichever the audience needs — a board wants the spectrum marker and the recommendation; an engineering lead wants the per-interaction table.

The discipline: the target is never "make everything an agent." It's a deliberate *mix* — FAQ stays L2 (cheap, reliable), high-volume bounded-consequence returns move to L5, high-stakes disputes stay L3 — and the output makes the *current position, the recommended position, and the unresolved questions* all legible on one page.

## WHERE THIS SKILL MEETS YOUR STACK

- **The thorough governance diagnostic → `ai-use-case-readiness`.** This skill is the *quick per-interaction reference* for placing a level; that skill is the *deep readiness/governance scoring* for a use case. This one carries the full 7-level teaching; readiness points here for it.
- **Calibrated trust + repair after an error → `trust-ladder`** (autonomy matched to *calibrated* trust, and how to walk it back). **Per-step design of a chosen Level 5+ agent → `agent-spec`.**
- **Keeping the human overseer sharp (the supervision paradox) → `judgment-guard`**; **communicating probabilistic autonomy to stakeholders who want guarantees → `trust-under-fog`**; **detecting rubber-stamping (over-trust as an anti-metric) → `ai-product-metrics`.**
- **The per-tool reversibility gate that enforces the level → `tool-architecture`**; **worst-case + can-you-kill-it-fast-enough → `agent-risk`**; **what must stay deterministic → `determinism-compass`.**
- **The machine that actually runs a Level 5+ agent → `agent-harness`** (MHTE, the loop); **the cost/org of running it as a program → `harness-operating-model`.**
- **Whether to build governance scaffolding now or wait for the maturing harness to absorb it → `capability-tracking`** (the "does the spectrum mature?" strategic call).

The spine: **this skill sets *how much* the model decides; the stack decides *how to enforce, run, and roll back* that decision.**

## QUALITY GATE

- [ ] Every interaction is classified by level — not the whole product as one number.
- [ ] Levels are set from consequence magnitude, not from what the model can do.
- [ ] Leash length matches a demonstrated track record; escalation is Supervised→Spot-check→Exception-based→Autonomous.
- [ ] The chosen level respects the verifiability cut line (you can still verify the *setup*).
- [ ] Any irreversible / >$10k action is walled off from the agent entirely.
- [ ] The **effective** level is measured, not assumed — you track edit/override rate on consequential actions, so rubber-stamping can't silently escalate a designed L4 into an operating L5.
- [ ] At Level 6, the overseer's engagement is designed (rotation / real-work spot-checks), not just "someone watches the dashboard."
- [ ] Kill switch accessible, tested, documented; rollback designed per action class before deploy.
- [ ] Context-utilization thresholds set (autonomy drops as the window fills).
- [ ] Users can see and understand the autonomy level and how it was earned.
- [ ] The output shows a "you are here" map: current (effective) vs recommended level per interaction, ranges where the honest answer is a band, and every unresolved case flagged **OPEN: decision needed** with an owner.

## WHEN WRONG

Skip or soften this skill when: the domain is pure-read with zero consequence (let the agent analyze, drop the governance overhead); confidence doesn't predict accuracy (non-stationary error distribution — run `eval-framework` first, don't tie the leash to confidence); users are intolerant of wait time (async approval breaks UX — *reduce consequence magnitude* instead of adding gates); or a regulator mandates specific controls (design compliance-first via `safety-by-design`). And the deepest misuse is conflating "we *want* Level 6" with "we *need* it" — most products are best served by Level 3–4 with excellent UX, and reaching for L5+ to match a competitor's demo is how programs ship the architecture change without the infrastructure it demands. Named products and cost bands here are illustrative 2026 snapshots (⚠) — the levels and the structural shift are the durable content; re-verify any specific example before quoting it.

---

## VOCABULARY BRIDGE

Engineer says *"deterministic workflow or agentic loop?"* → Level 2–4 or Level 5+. Designer says *"what happens when the AI does something unexpected?"* → the L4→5 UX challenge. Board member asks *"where are we on agents?"* → not "we're building agents" but "we're at L2–3 today; moving returns to L5 this quarter; here's the investment and the governance."

---

## TRADE-OFF LEDGER

Complete the Trade-Off Ledger from the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 3.

## CONCLUSION

Follow the Conclusion Protocol from the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 5: state the recommendation, name the key trade-off, acknowledge the biggest risk, define the next action.

---

## VISUAL SUMMARY

After completing the primary output, invoke the **excalidraw-svg** skill. More than one diagram is usually right here: (1) the **Agent Spectrum with "you are here" markers** — all 7 levels, the structural-shift line at 4→5, and the product's interactions plotted as *current-position dots and recommended-position arrows*, using ranges (a bar, not a dot) wherever the honest answer is a band; (2) a per-interaction **designed-vs-effective** delta that makes rubber-stamping visible; (3) the cost-vs-governance tradeoff rising with the level. Mark any **OPEN: decision needed** case visibly. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.
