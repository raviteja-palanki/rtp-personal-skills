---
name: opportunity-solution-tree
version: v1.1_latest
description: 'Teresa Torres'' Opportunity Solution Tree (outcome → opportunities → solutions → experiments) with the one cut the AI era demands: an AI-feasibility filter. OST expands the solution space, rightly, but for AI expansion alone produces a backlog of features the team can''t ship, because not every opportunity is probabilistically addressable. The filter sorts each into deterministic (rules), probabilistic-with-evals (spend AI bandwidth here), or probabilistic-but-unevaluable (the danger zone where projects die quietly). That makes the OST a roadmap with a ''no'' mechanism most teams lack. Use when planning a quarter or scoping a product area. Do NOT use for clearly-defined work (a bug, a regulatory deliverable) or a single committed direction. Pairs with: jtbd-analysis (the job becomes the outcome), determinism-compass (deterministic/probabilistic cut), problem-ai-fit (the fine feasibility cut), eval-framework (the eval surface). Triggers: ''what should we build'', ''map opportunities'', ''quarter planning''.'
imports:
  - problem-ai-fit
  - determinism-compass
  - jtbd-analysis
  - eval-framework
---

# Opportunity Solution Tree

**The objective:** map a desired outcome to opportunities, solutions, and experiments — then run every opportunity through an AI-feasibility filter *before* any of them get a roadmap slot — for the team planning a quarter with more ideas than bandwidth.

## The one idea

The team runs a beautiful Opportunity Solution Tree. Outcome at the top, five user struggles branching below, three solutions each, experiments at the leaves. Everyone nods. Then, six months later, half of it hasn't shipped — not because the team was slow, but because those opportunities were never *buildable* with AI in the first place.

Here is what happened. Teresa Torres' OST does one thing exceptionally well: it expands the solution space, so you generate many opportunities and many solutions instead of leaping from problem to the first idea. That expansion is the right move. But **for AI, expansion alone produces a backlog of features the team can't actually ship** — because not every opportunity is *probabilistically addressable.* Some should be solved with deterministic rules. Some genuinely need AI and can be measured. And some need AI but *can't be evaluated reliably yet* — and that third bucket is where projects go to die quietly, nine months after planning, when nobody can say whether they're working.

So the core idea adds one cut to the classic tree: the **AI-feasibility filter.** For each opportunity, ask — *deterministic, probabilistic-with-evals, or probabilistic-but-unevaluable?* That single cut turns the OST from a pretty diagram into a real roadmap, because it does the thing most teams have no mechanism for: **it says no.** Every other framework in the toolbox tells you what to build; the OST plus the feasibility filter tells you what *not* to put on the roadmap — the harder and more valuable call. A tree whose "no" list is empty is a backlog wearing a tree costume.

## How to use this skill

1. **Build the four layers** — outcome → opportunities (user struggles) → solutions → experiments. (THE 4 LAYERS.)
2. **Score and filter each opportunity** — impact × confidence × effort, then the AI-feasibility label. (SCORING + THE FILTER.)
3. **Produce the "no" list** — the opportunities you're deferring or killing, with reasons; that artifact is what makes the OST a planning tool.

## KEY TERMS (plain language)

- **OST (Opportunity Solution Tree)** — Torres' 4-layer map: one outcome → many opportunities → many solutions → experiments.
- **Opportunity** — a *user struggle in the user's voice* ("operators don't know which alerts to act on"), not a feature or a solution.
- **AI-feasibility label** — the added cut, one of three: **deterministic** (rules can solve it), **probabilistic-with-evals** (needs AI and can be measured), **probabilistic-but-unevaluable** (needs AI but can't be measured yet).
- **Eval surface** — the concrete way you'll measure whether the AI is doing the job (expert review of 100 outputs, user acceptance over 4 weeks, downstream task success).
- **Ship threshold** — the confidence bar at which the feature is shippable (80% expert agreement, 70% acceptance, <5% confident-wrong).
- **The "no" list** — the explicit set of opportunities you considered and rejected, with reasons; the artifact that makes the tree a roadmap, not a backlog.

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../../../UNIVERSAL-SKILL-PROTOCOL.md). At minimum: name the one measurable, time-bound outcome. **Go deep** when planning a quarter, scoping a new area, or choosing among 3+ candidate directions with limited bandwidth. **Skip** for clearly-defined work (a known bug, a regulatory deliverable, a contract obligation) or a single committed direction — that's execution, write the spec. Then route output format (tree doc, diagram, or both).

## THE 4 LAYERS

- **Layer 1 — Desired outcome.** One sentence, measurable, time-bound, tied to a real metric. *Bad:* "improve customer experience." *Good:* "reduce unplanned downtime on Tier-1 assets by 30% over 4 quarters." If it could apply to ten products, it's too vague; if the team can't argue with the number, it's not bold enough.
- **Layer 2 — Opportunities.** User struggles in the user's voice, sourced from evidence (interviews, tickets, behavior, JTBD). *Bad:* "predictive-maintenance dashboard." *Good:* "operators don't know which alerts to act on, so they ignore most of them." A healthy tree has 3–7 (more than 10 = outcome too broad; fewer than 3 = didn't push past the first idea). No evidence → mark it a hypothesis, not an opportunity.
- **Layer 3 — Solutions.** 2–4 *distinct* directions per opportunity (meaningfully different, not A/B of one idea). For alert fatigue: severity scoring (rules), AI confidence ranking (ML), an operator-collaboration view (hybrid), threshold tuning at source (rules). Notice the mix — that's the input to the feasibility filter.
- **Layer 4 — Experiments.** For each shortlisted solution, the *cheapest* test that could disprove it. This is where teams cheat by proposing "build the MVP" — that's a commitment, not an experiment. A real experiment disproves the hypothesis for <10% of the build cost (a one-week Wizard-of-Oz, a concierge test, a survey).

## SCORING + THE AI-FEASIBILITY FILTER

**Score each opportunity** on three axes (stage-calibrated): **Impact 1–5** (how much it moves the outcome), **Confidence 1–5** (5 = quantitative + qualitative + behavioral all align; 1 = "we think users want this"), **Effort 1–5** (inverted — 5 = <2 weeks, 1 = >6 months). **Don't multiply** — sort by impact × confidence descending, break ties by effort ascending (easier wins first), tag the top 3–5 as "next bets."

**Then apply the filter — every opportunity gets one label:**

- **Deterministic** — rules, lookup tables, decision trees, heuristics solve it. *Signals:* you can whiteboard the decision logic in 30 minutes; low input variability; no judgment required; stable expert mental models. **Action: build with rules, keep it off the AI roadmap.** *Why it matters:* AI engineering bandwidth is the constraint — spend an AI slot on a rules problem and a real AI opportunity gets deferred. Teams that skip this ship a lot of AI-flavored rule engines and call it innovation.
- **Probabilistic-with-evals** — needs AI's pattern-matching AND there's a way to measure whether it's working. *Signals:* output needs hard-to-encode judgment; high input variability; a measurable success criterion exists; a shippable confidence threshold exists. **Action: build with AI — and annotate the tree with the eval surface and the ship threshold.** This is the right place to spend AI bandwidth.
- **Probabilistic-but-unevaluable — the danger zone.** Needs AI, but there's no reliable way to measure success. *Signals:* the "right" answer is highly subjective; no measurable downstream action; expert review doesn't even agree with itself; noisy, lagged feedback. **Action: don't ship until you solve the eval problem** — find a validated proxy metric, reframe/narrow the scope until it's measurable, or park it. *The trap:* stakeholders push hardest here because it sounds the most exciting ("AI that understands customer sentiment"); shipping without evals is exactly how AI features earn "great demo, never delivered ROI."

The decision is a two-question funnel: *Can we whiteboard the logic in <30 min?* → yes = **deterministic**. If no: *Is there a measurable success criterion?* → yes = **probabilistic-with-evals**; no = **unevaluable** (park or narrow). (The VISUAL SUMMARY draws this.)

## WORKED EXAMPLE — reducing unplanned downtime 30% over 4 quarters

Five opportunities from interviews + ticket data: (1) alert fatigue — 78% of alerts ignored; (2) slow root-cause diagnosis — 4.2h mean; (3) PM schedules don't reflect asset health; (4) no defensible audit trail when a manager declines a recommendation; (5) spare parts not pre-staged. Scored: #1 (Impact 5 / Conf 5 / Effort 4) and #4 (3/5/4) are the fast, well-evidenced wins; #3 is big-if-true but mixed evidence.

**Filter applied:** #1 splits into severity scoring (**deterministic** — reliability engineers can whiteboard the rule) + AI confidence ranking (**probabilistic-with-evals** — eval surface: operator acceptance over 4 weeks + expert review of the bottom 50%; ship threshold: 70% acceptance, <5% confident-wrong on Tier-1). #4 (audit trail) is **deterministic** — a database and a form; *build it, keep it off the AI roadmap.* #5 (parts staging via prediction) is **unevaluable as scoped** — "did the right part arrive in time" is downstream of supply-chain decisions outside your control; narrow it ("predict failures for 5 asset classes where we control parts supply") before spending AI bandwidth, and ship the deterministic cross-customer pooling first.

**The roadmap that emerges** sequences deterministic wins (severity scoring, audit trail) in Q1 alongside an eval-driven-development AI pilot, then earns fleet-wide AI rollout in Q3 only if the pilot passes. **What got cut:** parts-staging-via-prediction is parked until the eval surface is real. That's the OST doing its job — saying no.

## THE PROTOTYPE CHANGED JOBS — build it to sharpen the problem, not to validate the answer

A cost change, and it moves the prototype from the bottom of this tree to the top.

**The old economics.** Prototypes were expensive, so you built them **late**, after you had decided what you wanted, to check whether the chosen solution worked. That put them under the solution layer, where most trees still place them.

**The new economics.** They are cheap and fast, so build them **early**, not to show the answer but *"to make the debate about direction more concrete."* A rough prototype at the opportunity stage is an instrument for interrogating the problem, and it belongs beside the opportunity, not under the solution.

**The acceptance test, and it is the operational half of this:** **evaluate the prototype on which questions it surfaced, not on how finished it looks.** A prototype that produced three arguments the team had not had yet did its job. A polished one that produced agreement did not, and the polish is what caused the agreement.

Three practical consequences for how you run the tree:

- **Rough and early beats polished and late.** Explicitly reward roughness, or the team will optimize the artifact instead of the debate.
- **A prototype can sit against more than one opportunity.** Its job at this stage is comparison, so building one against two competing opportunity framings is a better use than building two against one.
- **Log the questions it raised as tree nodes.** That is the output. If nothing new entered the tree, the prototype was a demo.

**Say this part out loud to the team, because it explains the pull better than any incentive story.** Problem definition **has no progress bar**. Building does. When production gets cheap, the activity with a visible completion signal outcompetes the one without it, regardless of which creates more value, so the pull toward "just build the thing" gets stronger exactly as prototyping gets cheaper. Give the framing work its own completion signal (a written problem statement, a named assumption, a falsifier) or it will keep losing. See `rtp-first-principles`.

*(Source: HBR, "AI Makes Building Easy. Choosing What to Build Is Harder," Aug 2026 — ⚠ and read carefully: the article concludes that problem definition beats execution **from a contest whose judging criteria explicitly prioritized problem definition over technical execution**, and reports no outcome number of any kind. That conclusion is circular. The prototype's changed function follows from the cost change rather than from the contest, and the progress-bar observation is the article's own honest reporting of behavior. Carry those two; leave the thesis.)*

## WHERE THIS SKILL MEETS THE REST OF YOUR STACK

The chain: **outcome → opportunities → solutions → AI-feasibility filter → experiments → eval design → the roadmap it hands to whoever builds the bet.** Trace both ends — where opportunities come from, and where a greenlit bet goes next.

**Feeds the tree (where opportunities come from):**
- **`rtp-jtbd-analysis`** *(import)* — a JTBD job statement becomes the desired outcome at the top of the tree; the hidden job filters which opportunities are worth pursuing.
- **`rtp-feedback-triage`** — its future-capability signals (the "I use a different tool for that" bucket) are pre-sourced, evidence-backed opportunities that drop straight into Layer 2. Triage catches them in the batch; the tree is where they become bets.

**Runs inside the filter (imports):**
- **`rtp-determinism-compass`** *(import)* — the deterministic-vs-probabilistic classification is *its* home; this skill applies it as a coarse feasibility label. Sharpen labels there.
- **`rtp-problem-ai-fit`** *(import)* — the feasibility filter here is the *coarse* cut; problem-ai-fit is the *fine* cut for every probabilistic solution before you commit.
- **`rtp-eval-framework`** *(import)* — every "probabilistic-with-evals" solution needs an eval design; that's where the eval surface gets built. A label without a 1-paragraph-specific eval design belongs in the "unevaluable" bucket until it's real.
- **`rtp-uncertainty-research`** — the experiments at the leaves use its research methods.

**Acts on the greenlit bet (the two-hop the tree usually drops):**
- **`rtp-ai-use-case-readiness`** — a "probabilistic-with-evals" label says the bet is *worth building*; it does not say *how autonomous* to build it. Hand each greenlit opportunity to readiness to right-size its autonomy level before it gets scoped. The tree picks *what*; readiness picks *how much agency*.
- **`rtp-ai-prd`** — the greenlit, autonomy-sized bet becomes a spec here. Skip this hop and the OST is a plan nobody writes down.
- **`rtp-ai-portfolio-management`** — the "no" list isn't only this tree's rejections; at portfolio scale it's the defer/kill ledger across competing bets. Feed the no's up so the same opportunity isn't re-litigated in three separate trees.

## RED TEAM — when the OST is ceremony

- **The work is clearly defined** — bug fixes, regulatory deliverables, tech debt; the opportunity is "ship the thing." Use a backlog.
- **0 or 1 viable opportunity** — OST earns its keep with 3+ directions to choose among; with one, you're executing, write the spec.
- **The outcome is unclear or non-measurable** — "improve UX" can't anchor a tree; refuse to start until it's one sentence with a number and a date.
- **The team treats it as a one-time artifact** — OST is alive (opportunities added as evidence emerges, killed as experiments fail); run-once-and-file gets planning overhead without planning compounding.

## WHEN WRONG

- **Every opportunity forced into the AI bucket** — an AI roadmap with no deterministic work is a smell; real ones are ~30–50% deterministic in support of the probabilistic core (⚠ heuristic).
- **"Probabilistic-with-evals" applied without a real eval design** — "we'll measure acceptance rate" is a placeholder, not an eval surface; if it's not 1-paragraph specific, it's unevaluable until it is.
- **The "no" list is empty** — every healthy tree has rejections; 8 opportunities all greenlit is a backlog in a tree costume. Force 2–3 explicit no's with reasons.

## QUALITY GATE

- [ ] Desired outcome is one sentence, with a number and a date
- [ ] ≥3 opportunities framed as user struggles in the user's voice, evidence-sourced
- [ ] Each opportunity has 2+ distinct solutions
- [ ] Every solution carries an AI-feasibility label
- [ ] Every probabilistic solution has an eval surface AND a ship threshold specified
- [ ] Scoring is explicit and sortable
- [ ] The "no" list names 2+ rejected opportunities with reasons
- [ ] The roadmap implication is named — what's built first, what waits, what's killed

## TRADE-OFF LEDGER

By adding the feasibility filter, you bet that the constraint on AI roadmaps is *what can actually be built and measured*, not idea generation — so a tree that says no is worth more than one that greenlights everything. You give up the comfort of a full-looking backlog and take on the discipline of eval-driven-development labeling. **Reversible?** Fully — it's planning, not a build. **The hidden trade:** the failure mode is *optimism laundering* — labeling an unevaluable opportunity "probabilistic-with-evals" to keep it alive, which just moves the quiet death from planning to month 9; the empty-"no"-list check and the 1-paragraph-eval test guard against it. **Confidence: High** — the "no" mechanism is the scarcest and most valuable part of AI planning. What would change it: a single-direction team in execution mode, where the tree is ceremony.

## CONCLUSION

Follow the Conclusion Protocol ([Universal Skill Protocol](../../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 5). Every OST ends with one paragraph: *"We're investing in [opportunities X and Y] this cycle. We're deferring [Z] until [condition]. We're saying no to [W] because [reason]. The riskiest assumption in our top opportunity is [assumption], which we'll test by [experiment] in [timeframe]."* If the team can't write that, the tree isn't done — loop back to the feasibility filter and the "no" list; that's where the work skipped.

## VISUAL SUMMARY

After the primary output, invoke the **excalidraw-svg** skill for one visual: the 4-layer tree (outcome → opportunities → solutions → experiments) with each solution color-coded by AI-feasibility label (green = deterministic, amber = probabilistic-with-evals, red = unevaluable), and the two-question filter funnel drawn beside it ("whiteboard in <30 min?" → "measurable success criterion?"). So a viewer sees both the expanded space and the cut that turns it into a roadmap. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.
