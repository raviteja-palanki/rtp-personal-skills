---
name: ai-use-case-readiness
version: v2.6_latest
description: 'Right-size the autonomy for a use case: the minimum that captures the value, not the maximum you could build. The question is never ''can we make this autonomous?'' but ''what''s the least autonomy that still works?'' Autonomy is a governance question, not a capability one: you CAN build a level-5 agent; cost-of-error, verifiability, and policy decide whether you SHOULD. Runs a 5-phase diagnostic: 12 questions, the 0-7 spectrum, two matrices, a floor/ceiling gap and a phased roadmap. The output is framed as a testable hypothesis, not a rubber stamp. Use when a team says ''let''s build an agent'', or when ''can it be autonomous?'' is asked before ''should it be?''. Do NOT use for a monolithic undecomposed use case (first-principles first) or a pure tech-stack choice. Pairs with: problem-ai-fit (whether AI at all), autonomy-spectrum (quick level reference), determinism-compass (what stays deterministic), cost-model (control-burden economics). Triggers: ''let''s build an agent'', ''how autonomous'', ''can this be an agent''.'
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
- **Foundation dependency** — whether the use case works standalone (low-foundation), needs a specific data pipeline to function (data-dependent), or breaks if the underlying infrastructure changes (foundation-critical). Classify this before scoring any other readiness dimension.

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

You will optimize for *maximum* autonomy instead of *right-sized* autonomy. The bias is **agentic hype**: agents are novel, well-funded, and feel like the future. Five variants:

- **Autonomy theater** — a level-5 agent for 80%-stable-rules work; it runs, but costs 10× a level-2 system to maintain.
- **Novelty bias on action rights** — the LLM *can* write SQL or invoke APIs, so you assume it *should*. Execution rights are a governance question, not a capability one.
- **Cost-of-error amnesia** — you run twelve diagnostics on tacitness and variability and forget Q3: "what happens if it's wrong?" High-tacit, high-error domains need human-in-the-loop, not autonomy.
- **Values-veto laundering.** A common four-criteria prioritization checklist scores risk, feasibility, business impact and human-vs-AI appropriateness, then averages all four.

  **The mechanism:** averaging lets high scores on the other three outvote a hard values line, so a use case that should never have entered scoring comes out "green" anyway.

  **Fix:** human-vs-AI appropriateness is a gate, not a criterion. Decide it pass/fail first, before the other three are scored at all.

  **Wrong when:** the appropriateness line is itself contested or actively moving, such as a new regulatory allowance or a shifted internal policy. Then treat it as a gate to revisit on a cadence rather than a permanent veto. *(Source: an AI use-case prioritization webinar recap, Jul 2026 — prescriptive checklist with zero supporting evidence; carried as a common practice pattern, not a validated finding.)*
- **New-task-creation mislabeling.** A proposal claims the deployment "creates new kinds of work," and nobody checks whether the actual task list changed.

  **Why the underlying taxonomy cannot settle it.** The five-category model of how AI reshapes labor (Acemoglu, Autor and Johnson: labor-augmenting, capital-augmenting, automating, expertise-leveling, new-task-creating) can only be scored correctly *after* the labor market has repriced the work. That makes it useless as an ex-ante screen on its own.

  **The test it does yield:** compare the task list required for the role or workflow before and after the deployment. **If the list is unchanged, the deployment cannot be new-task-creating**, because that category requires the task set itself to expand.

  **Necessary, not sufficient.** A deployment with an unchanged task list can still raise measured demand for the underlying expertise by deepening a task it already had. This test will not catch that case.

  **Name the distractor out loud.** A deployment that clearly helps people answers a different question than whether it is ready for its claimed autonomy level. A strong helpfulness case is not a readiness assessment and should never substitute for one. *(Source: Acemoglu, Autor and Johnson, a publicly available economics paper — ⚠ reported in this pass, not independently verified against the primary source.)*

## PHASE 2: DIAGNOSE

**Zero, classify foundation dependency (required before any other dimension).** Every use case falls into one of three classes. **Low-foundation** works standalone, with no upstream dependency. **Data-dependent** needs a specific pipeline or data source to function, so breaking the pipeline breaks the use case. **Foundation-critical** breaks if the underlying infrastructure changes: a platform migration, a model swap, or a schema change takes it down too. The mechanism this guards against: without classifying first, a team can score a foundation-critical use case "ready" on every autonomy dimension and still ship something that dies the next time the data team touches a schema, because the readiness score was measuring the wrong risk entirely. **Wrong when:** the classes blur within one use case, with some sub-tasks data-dependent and others low-foundation. Classify per sub-task once you decompose, not once for the whole use case. *(Source: HBR, "AI and IT Teams Often Clash. But They Don't Have To.," Jul 2026, three anonymized advisory cases — ◆ company-disclosed pattern, no public citation available given anonymization; carried as a practitioner pattern, not a measured statistic.)*

**Then decompose.** Restate the job in operational terms (trigger, inputs/outputs, actors, systems, permissions, success metric, consequence-if-wrong), then break it into sub-tasks and rate each on: foundation dependency · explicit vs. tacit · advisory vs. executional · cost of error · verifiability · best-fit level. **Critical rule:** if one sub-task is much riskier than the rest, do not let the average hide it. Most good architectures are **hybrids** (level 3 for stable parts, level 1 for risky parts).

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

## A LIGHTWEIGHT QUALIFICATION FRAME FOR PRE-PMF WORK

The five phases above are built for an organization deciding how autonomous a use case should be. **When the company is pre-PMF and the founder is the primary seller, that is too heavy.** Six behaviors do most of the work:

| | Creates | The test |
|---|---|---|
| **Speed** | attention | did this person just describe my situation better than I could? |
| **Problem** | urgency | what has changed to make solving this *now* essential? |
| **Results** | belief | can the buyer describe the outcome to their own board without you present? |
| **Implementation** | safety | did you answer the risk question before they raised it? |
| **Niche** | repeatability | one buyer type, one problem, one motion that repeats |
| **Trust** | permission | is your credibility transferable, or does it live only in you? |

**Use Problem as the qualifying gate.** The named failure it catches: a founder pitching generically, unable to state the buyer's tension precisely. One worked case reframed around "revenue at risk" rather than a generic service pitch, which **disqualified deals that had been consuming the pipeline** and promoted earlier-stage conversations previously dismissed.

**Implementation is the one that explains silence.** Buyers who seemed enthusiastic go quiet **not because they stopped believing**, but because someone upstream raised a risk nobody answered.

**Where this sits relative to the phases above.** This qualifies the *opportunity*. The five phases size the *autonomy*. Run this first when the question is whether anyone wants it, and the phases when the question is how much the system should decide. See `rtp-fit-signal` for the demand-side signals.

*(Source: Rubinstein & Onyemah, HBR, 24 Jun 2026 — ⚠ inductive from an interview set of founders, no effect sizes, and the worked case is a single German manufacturer. Use it as a conversation frame, not as a validated model.)*

## READ YOUR READINESS SCORE AS A MOAT AUDIT

A reframe that changes what you do with the output, and it is the most useful thing in this skill for a strategy conversation.

**A readiness checklist looks like a hygiene exercise. It is a moat audit wearing a checklist's clothes.**

Here is why. The things a readiness assessment measures are, almost without exception, the inputs that **cannot be bought from a vendor and are not falling in price**: whether people will actually change how they work, whether the data is clean enough to use, whether decisions have owners, whether the workforce trusts what is being deployed. Model capability is rented, commoditizing, and available to every competitor on the same terms. **Organizational change capacity is none of those things.**

So a low readiness score is not only a delivery risk. It is a statement about where your competitive position actually comes from, and a high one is an asset most competitors cannot purchase.

**A serviceable external diagnostic, six questions, if you want one that a board will recognize:**

1. **Shared ambition.** Have you decided how you want to do business differently, and why that is better for customers and employees, before deploying anything?
2. **Governance.** Does your review process shape the work early, and can it stop something? (Ask the twelve-month question in `rtp-responsible-ai-program`.)
3. **Scaling past the pilot.** What are you doing to get executive support *before* you start, and to keep those leaders interested as you make progress?
4. **Technical foundation.** Clean data, working tools, integrated systems. Every organization has some data cleanup to do; the failure modes are ignoring it and trying to fix all of it at once.
5. **Culture.** Can the organization experiment readily, decide from data rather than history, and accept speed over perfection?
6. **Skills and reassurance.** Have you told people how their roles will change and what support they get? *"We're going to change your job, but we're going to help you make that transition."* And the reason to say it: *"if you're not telling them, people are thinking the very worst."*

**Two ways to use the score, and the second is the one people miss:**

- **As a gate**, the usual way. Low score, fix the condition before funding the use case.
- **As a portfolio input.** If your readiness on a capability is genuinely high and rivals' is low, that gap is durable, because it takes years to close and no vendor sells it. Weight toward use cases that *consume* that advantage. Route to `rtp-moat-finder` and `rtp-ai-portfolio-management`.

**Where this reframe is wrong:** readiness that is high because the use case is trivial is not a moat. The asset is change capacity demonstrated on hard work, not an easy deployment that went smoothly.

*(Source: MIT SMR, Westerman, "6 questions to guide your AI strategy," 3 Aug 2026 — the six questions are his, ◆ reported company examples with **no measurement anywhere in the article** and no adoption figures of any kind. The moat reframe is this corpus's: he names organizational change capacity as the constraint and calls it a strategy question rather than a scarce complementary input. Note that this article's only statistic is broken in an instructive way; it is carried as a teaching case in `rtp-trendslop-check`, and its governance framing is refuted in `rtp-responsible-ai-program`. Ledger patterns A and N.)*

## WHICH FUNCTION SHOULD GO FIRST: A THREE-CHARACTERISTIC SCREEN

Most companies pick the function that is loudest about AI. **Three characteristics predict agentic fit, and a function that has all three is better positioned than one that has any two.**

1. **Economic visibility.** Does activity in this function translate directly into financial outcomes, **measurable in the same currency the CFO uses?** If the value has to be argued rather than counted, every scaling conversation will be a negotiation.
2. **Process structure at scale.** Are the workflows repeatable and multi-step? That is where agents that reason, act and adapt across tasks deliver disproportionate value, as opposed to a single-call assistant.
3. **Persistent judgment-heavy friction.** Is there manual intervention at specific points that **resisted traditional automation precisely because it needs judgment rather than rule-following?**

**The third is the discriminating one and it is the one most screens omit.** It separates work that rules-based automation already solved from work that stayed manual because it needed a person to weigh something. **Friction that RPA could have removed and did not is an RPA project. Friction that RPA could not remove is the agent-shaped opportunity.**

**The worked ranking that makes the point.** In a survey of 385 organizations, agentic adoption ran software development 35%, IT operations 31%, marketing 26%, and **procurement 9%** — despite procurement scoring highest on all three characteristics. The lag was organizational, not technological.

**Three organizational barriers to check before you name a first function**, because scoring well on the three characteristics does not mean the function can carry the work:

- **Accountability and control.** Where decisions carry contractual or financial consequences, organizations respond by **limiting autonomy and preserving human approval so strongly that they neutralize the benefit.** A function with heavy approval structures needs the autonomy design solved before the pilot, not after.
- **Fragmented ownership.** Is the function the *owner* of the initiative or its *beneficiary*? Solutions designed by IT with limited operational input succeed in controlled conditions and stall against exception-rich reality. **The trade-offs should be made by the people who will live with the consequences.**
- **Data as an afterthought.** Inconsistent master data and incomplete categorization mean the agent never had a chance, and the conclusion drawn will be that the technology failed.

**Then the failure mode to name out loud before anyone starts, because it has a name and it is common.** Practitioners call it **the belief stage**: pilots launched, adoption celebrated, accountability for value left unclear, initiative stalls there indefinitely. **The antidote is a requirement, not a warning. Every agent carries an investment case from the outset, mapped to a specific process phase, a defined value lever, and measurable financial KPIs.** A pilot that cannot name its value lever is already in the belief stage on day one.

*(Source: Himmelreich, Oshri, Scala & Zaidani, HBR, "Why Agentic AI Could Transform Procurement," Aug 2026 — drawing on the authors' decade of research through ERP, RPA and intelligent automation plus practitioner interviews. The adoption percentages are ◆ from a survey of 385 organizations cited without its sampling frame or its definition of adoption, so **the ordering is usable and the levels are not.** The three characteristics are presented as a description of procurement; treating them as a general screen is this corpus's move. Falsifier: a function scoring low on all three that captured durable agentic value ahead of one scoring high.)*

## CAN THE REVIEWER JUDGE WITHOUT PRODUCING?

**Before you approve a use case on the theory that AI lets a wider group do this work, run one test: can a person judge whether the output is good without being able to produce it themselves?**

Two tasks, same subject, opposite answers:

- **Come up with article topics.** You can tell a good topic from a weak one without being able to write the article. Judgment here needs less expertise than production.
- **Write the article.** You cannot tell whether the language lands without knowing how to make language land. Judgment here *is* production.

A controlled experiment at a UK fintech put 78 employees through both tasks in three groups: writers who did the work daily, marketing specialists from the same department who shared the vocabulary but had never written an article, and developers and data scientists from neither world.

**On topic generation, AI collapsed the gap.** The spread between best and worst group fell from 0.80 to 0.13 on a five-point rating. AI-assisted marketers slightly beat AI-assisted writers, and every AI-assisted group beat the unassisted writers.

**On writing, the gap held, and for the furthest group AI added nothing at all.** With AI: writers 3.96, marketers 3.92, technologists 3.38. The technologists' score *without* AI was 3.42. **They were no better with the tool than without it.**

**The mechanism, and it is not what the headline suggests.** Every group got comparable output from the model. Only some could act on it. The marketers had enough shared language to refine what the model produced; the technologists "could not effectively use or improve the AI's suggestions," and many simply pasted the output straight in. **The limit is not on what the model can generate. It is on who can edit.** Editing capacity is exactly the thing the tool does not supply.

**Turn it into a readiness screen, run before the effort estimate:**

| Ask | If yes | If no |
|---|---|---|
| Can the intended user state the acceptance standard without producing the artifact? | The use case widens. Score it accordingly. | The use case does not widen. Score it as an assist for people who already do this work. |
| Is the intended user inside the domain's vocabulary, even without production experience? | Adjacent. Expect near-expert results with review. | Distant. Expect no gain, and expect paste-through. |
| Can you detect paste-through in production? | Proceed. | Build that detection first. It is the only signal that tells you the widening failed. |

**The rule this replaces.** "AI lets anyone do this now" is not a readiness finding. **The honest version is that AI redistributes capability inside a neighborhood and does nothing across the fence.** Widening a task from writer to marketer is a real plan. Widening it from writer to data scientist is a staffing decision dressed as a capability one, and it will show up as output nobody edited.

*(Source: Vendraminelli et al., HBR, "Gen AI Won't Make Your Employees Experts," Apr 2026 — ◆ controlled experiment, n=78, single UK fintech, executive raters on a 1-5 scale, one task pair. Small n and one company; the design is unusually clean and the grouping variable, distance from the domain rather than seniority, is the right one. Falsifier: a task where a group with no domain vocabulary matches experts on the production half, not only the judgment half.)*

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
- [ ] Foundation dependency classified (low-foundation / data-dependent / foundation-critical) before scoring any other dimension
- [ ] Use case decomposed into sub-tasks, not one blob
- [ ] The 12 diagnostic questions answered (or gaps named with evidence level)
- [ ] Load-bearing assumptions surfaced, rated, and flagged
- [ ] Both matrices completed (Knowledge × Cost; Agency × Control)
- [ ] Four meta-judgments stated; autonomy floor and ceiling identified and the gap explained
- [ ] Recommendation stated as a hypothesis (IF TRUE / IF FALSE / PIVOT), with why-not-lower and why-not-higher
- [ ] Phased path with exit criteria, each framed as a hypothesis; controls named
- [ ] Any "creates new kinds of work" claim checked against the task list before and after, not asserted from a helpfulness case

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
