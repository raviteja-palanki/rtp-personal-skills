---
name: rtp-opportunity-solution-tree
description: >
  Teresa Torres OST with an AI-feasibility filter. Use when the team has a
  desired outcome and needs to map opportunities, solutions, and experiments —
  AND when not every opportunity is probabilistically addressable. Adds the
  determinism-compass cut that separates "needs deterministic rules" from
  "can tolerate AI variability." Without that filter, OST becomes a wish list.
imports:
  - problem-ai-fit
  - determinism-compass
  - jtbd-analysis
  - eval-framework
---

# Opportunity Solution Tree

Map outcomes → opportunities → solutions → experiments, then run each opportunity through an AI-feasibility filter before any of them get a roadmap slot.

> Teresa Torres got the structure right. The AI era requires one more cut: not every opportunity is probabilistically addressable. The OST that ignores this becomes a backlog of features the team can't ship.

---

## DEPTH DECISION

**Go deep if:** Planning a quarter, scoping a new product area, deciding what to build after a JTBD analysis, or trying to justify why some opportunities should be killed instead of explored. Use the full tree when the team has 3+ candidate directions and limited bandwidth.

**Skim to the AI-feasibility filter if:** You already have a tree and just need the cut between "build this with rules" and "build this with AI."

**Skip if:** The work is clearly defined (a known bug, a regulatory requirement, a contract deliverable), or the team is in execution mode on a single committed direction.

---

## DELIVERABLE FORMAT

Before starting, ask:

> **Format?**
> 1. **Tree document** — Markdown OST with all 4 layers + AI-feasibility annotations. Best for sharing with the team.
> 2. **Visual diagram** — Excalidraw SVG showing the tree structure. Best for stakeholder reviews.
> 3. **Both** — Tree doc + diagram.
>
> *Default: Tree document.*

---

## THE STRUCTURAL INSIGHT

Teresa Torres' OST is one of the cleanest tools in modern product management. It expands the solution space — instead of jumping from problem to one solution, you generate multiple opportunities and multiple solutions per opportunity, then experiment.

That expansion is the right move. But for AI features, expansion alone produces a backlog of opportunities the team can't actually ship.

**The 0.1% AI PM angle: AI capability narrows the tree.**

Some opportunities should be solved with deterministic rules. Some can tolerate AI variability. Some require AI but can't be evaluated reliably yet. Without separating these three buckets, the team commits to roadmap items it can't deliver — and the OST becomes a pretty diagram instead of a planning tool.

The AI-feasibility filter is the cut that turns the OST from a wish list into a roadmap. For each opportunity, ask: deterministic, probabilistic-with-evals, or probabilistic-but-unevaluable? The third bucket is where projects die quietly six months after planning.

**Why this matters:** every other framework in the AI PM toolbox tells you what to build. The OST plus feasibility filter tells you what NOT to put on the roadmap, which is the harder and more valuable call. Most teams don't have a "no" mechanism. This is one.

---

## THE 4-LAYER STRUCTURE

```
                        DESIRED OUTCOME
                  (one measurable, time-bound goal)
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
   OPPORTUNITY 1         OPPORTUNITY 2         OPPORTUNITY 3
   (user struggle)       (user struggle)       (user struggle)
        │                     │                     │
   ┌────┴────┐           ┌────┴────┐           ┌────┴────┐
   │         │           │         │           │         │
 SOL A     SOL B       SOL C     SOL D       SOL E     SOL F
   │         │           │         │           │         │
  EXP       EXP         EXP       EXP         EXP       EXP
  (a/b)   (proto)     (wizard)  (survey)   (concierge) (pilot)
```

### Layer 1 — Desired Outcome

One sentence. Measurable. Time-bound. Tied to a real metric, not a vanity number.

**Bad:** "Improve customer experience."
**Bad:** "Launch AI features."
**Good:** "Reduce unplanned downtime on Tier-1 industrial assets by 30% over the next 4 quarters."
**Good:** "Increase weekly active users in the maintenance planner from 2,400 to 4,000 by EOY."

If the desired outcome can apply to ten different products, it's not specific enough. If the team can't argue with the number, it's not bold enough.

### Layer 2 — Opportunities

User struggles, framed in the user's voice. Not features. Not solutions. Struggles.

**Bad:** "Predictive maintenance dashboard."
**Good:** "Operators don't know which alerts to act on, so they ignore most of them."

**Bad:** "AI-powered search."
**Good:** "Engineers can't find the document they need in under 5 minutes, so they recreate work that already exists."

Each opportunity should be sourced from real evidence — interviews, support tickets, behavioral data, JTBD analysis. If the only source is "we think users want this," mark it as a hypothesis, not an opportunity.

A healthy OST has 3-7 opportunities per outcome. More than 10 means the outcome is too broad. Fewer than 3 means the team didn't push past the first solution that came to mind.

### Layer 3 — Solutions

For each opportunity, brainstorm 2-4 distinct solution directions. Distinct means meaningfully different — not "version A and version B" of the same idea.

**Opportunity:** "Operators don't know which alerts to act on, so they ignore most of them."

**Solutions:**
- **Severity scoring** — Rules-based ranking that filters out alerts below a threshold.
- **AI confidence ranking** — ML model ranks alerts by predicted false-alarm probability.
- **Operator collaboration view** — Shows what other operators in similar situations did with similar alerts.
- **Reduce alert volume at source** — Tune the underlying detection thresholds based on plant history.

Notice that two are deterministic (severity scoring, threshold tuning), one is probabilistic (AI confidence), and one is hybrid (collaboration view uses both rules and ML for similar-case retrieval). This is the input to the AI-feasibility filter.

### Layer 4 — Experiments

For each shortlisted solution, design the cheapest test that would prove or disprove it.

**Hypothesis:** "If we rank alerts by severity score, operators will act on the top 20% and ignore the bottom 80%, reducing alert fatigue."

**Method:** Wizard-of-Oz. PM manually ranks one week of alerts using a draft scoring rule. Send the ranked list to 3 operators. Measure: do they act on the top-ranked alerts? Do they say the ranking matches their judgment?

**Bar:** If 2 of 3 operators say the ranking matches their judgment 80% of the time, build it. Otherwise, the rule needs work or the opportunity is mis-framed.

**Timeline:** 1 week of wizard-of-oz, 1 week of analysis. Total: 2 weeks.

The experiment layer is where most teams cheat — they propose "build the MVP" as the experiment. That's not an experiment, that's a commitment. A real experiment can disprove the hypothesis with less than 10% of the build cost.

---

## OPPORTUNITY SCORING

Before deciding which opportunities make the cut, score each on three axes. The scales are stage-calibrated — what counts as "high impact" for a Series A startup is different from a Fortune 100 enterprise.

### Impact (1-5)

How much would solving this move the desired outcome?

| Score | Enterprise (Fortune-100-scale) | Startup |
|---|---|---|
| 5 | Moves a top-line metric by >15% | Moves NSM by >25% |
| 4 | Moves a metric by 5-15%, or unblocks a strategic deal | Moves NSM by 10-25% |
| 3 | Improves a leading indicator by >20% | Improves leading indicator by >30% |
| 2 | Improves user experience without metric movement (yet) | Helps a single segment significantly |
| 1 | Nice-to-have, no clear metric path | Nice-to-have |

### Confidence (1-5)

How sure are we the opportunity is real?

| Score | Evidence |
|---|---|
| 5 | Quantitative data + qualitative interviews + behavioral signals all align |
| 4 | Two of three evidence types align |
| 3 | One strong evidence source (interviews OR data, not both) |
| 2 | Anecdotal — heard from a few users, no systematic source |
| 1 | "We think users want this" — no real evidence |

### Effort (1-5)

T-shirt size in engineering weeks. The 1-5 inverts: 5 = cheap.

| Score | Engineering weeks (calibrated to a 6-person team) |
|---|---|
| 5 | <2 weeks |
| 4 | 2-6 weeks |
| 3 | 6-12 weeks |
| 2 | 3-6 months |
| 1 | >6 months |

### Score formula

Don't just multiply. Use the priority ranking:
1. Sort by impact × confidence (descending)
2. Within each impact-confidence bucket, sort by effort (ascending — easier wins first)
3. Tag the top 3-5 as "next bets"

The reason for not multiplying everything: a 1-effort opportunity with 1-impact is not equivalent to a 5-effort opportunity with 5-impact, even though they have the same product. Lexicographic sorting forces the right ordering.

---

## THE AI-FEASIBILITY FILTER

This is the structural addition. Every opportunity gets one of three labels.

### Label 1 — Deterministic (DON'T spend an AI roadmap slot here)

The opportunity can be solved with rules, lookup tables, decision trees, regex, simple heuristics, or scripted workflows. The output is bounded, the input space is enumerable, and the rules don't change often.

**Signals:**
- The team can write the decision logic on a whiteboard in 30 minutes
- The input variability is low (Dimension A from problem-ai-fit ≤ 2)
- The output requires no judgment (Dimension B ≤ 1)
- Domain experts have stable mental models that haven't changed in 2+ years

**Action:** Build with rules. Don't add it to the AI roadmap. Track it in the regular product backlog.

**Why this matters for AI roadmaps:** AI engineering bandwidth is the constraint. Wasting an AI slot on a problem rules can solve means a real AI opportunity gets deferred. Teams that don't filter ship a lot of AI-flavored rule engines and call it innovation.

### Label 2 — Probabilistic with Evaluable Surface (the right place to spend AI bandwidth)

The opportunity needs AI's pattern-matching strengths AND there's a way to evaluate whether the AI is doing the job well.

**Signals:**
- The output requires judgment that's hard to encode as rules (Dimension B ≥ 3)
- The input variability is high (Dimension A ≥ 3)
- There's a measurable success criterion (the eval surface): user accepts/rejects, downstream action succeeds/fails, expert review confirms quality, etc.
- A confidence threshold exists at which the feature is shippable

**Action:** Build with AI. Specify the eval surface in the OST entry. Set a confidence threshold for shipping. Plan the experiment as a Wizard-of-Oz or constrained pilot.

**Required annotation in the tree:**
```
SOLUTION: [name]
  AI-Feasibility: Probabilistic-with-evals
  Eval surface: [how we measure quality — e.g., expert review of 100 outputs,
                  user acceptance rate over 4 weeks, downstream task success]
  Shipping threshold: [the confidence bar — e.g., 80% expert agreement,
                        70% acceptance rate, <5% confident-wrong rate]
```

### Label 3 — Probabilistic but Unevaluable (DANGER ZONE)

The opportunity needs AI but there's no reliable way to measure whether it's working. This is where projects go to die — they ship, nobody knows if they're succeeding, and they get killed quietly 9 months later.

**Signals:**
- The "right" answer is highly subjective (creative writing, "feels good," qualitative judgment)
- There's no downstream action whose success can be measured
- Expert review doesn't agree with itself (low inter-rater reliability)
- User feedback is noisy and lagged

**Action:** Don't ship until you've solved the eval problem. Either:
1. Find a proxy metric that correlates with the real outcome (and validate the correlation)
2. Reframe the opportunity to make it evaluable (narrow the scope until it has a measurable surface)
3. Park it. Move on. Don't burn an AI slot on something you can't measure.

**The trap:** stakeholders push hardest on Label 3 opportunities because they sound the most exciting ("AI that understands customer sentiment," "AI that drafts thought-leadership content"). The PM's job is to either narrow the scope until it's evaluable, or push back. Shipping without evals is how AI features earn the reputation of "great demos that never delivered ROI."

### The Filter as a Visual

```
       OPPORTUNITY
            │
            ▼
   ┌────────────────────┐
   │ Can we describe    │
   │ the decision logic │
   │ in <30 mins?       │
   └────────┬───────────┘
            │
       Yes ─┼─ No
            │
   ┌────────▼─────────┐    ┌──────────────────────┐
   │  DETERMINISTIC   │    │ Is there a measurable │
   │  Build with rules│    │ success criterion?    │
   │  Don't use AI    │    └────────┬─────────────┘
   │  bandwidth       │             │
   └──────────────────┘        Yes ─┼─ No
                                    │
                       ┌────────────▼──────────┐    ┌─────────────────────┐
                       │ PROBABILISTIC + EVALS │    │ UNEVALUABLE         │
                       │ Spec the eval surface │    │ Park or narrow scope│
                       │ Set ship threshold    │    │ Don't burn AI slot  │
                       │ Build with AI         │    │ on something you    │
                       └───────────────────────┘    │ can't measure       │
                                                    └─────────────────────┘
```

---

## REAL-WORLD ENTERPRISE EXAMPLE — Fortune 100 / world-class AI-native startup scale

### Desired outcome

> Reduce unplanned downtime on Tier-1 industrial assets by 30% over the next 4 quarters.

### Opportunities (from interviews + ticket data)

1. **Operators don't know which alerts to act on, so they ignore most of them.** (ignored alert rate: 78%)
2. **Engineers can't diagnose the root cause fast enough when an asset trips.** (mean time to diagnosis: 4.2 hours)
3. **Maintenance schedules don't reflect actual asset health, so we over-maintain healthy assets and under-maintain failing ones.** (PM compliance: 91%, but failure rate hasn't improved in 3 years)
4. **Plant managers don't have a defensible audit trail when they decide NOT to act on a recommendation.** (regulatory exposure)
5. **Spare parts aren't pre-staged for predicted failures.** (mean time to repair: 11 hours, of which 4 are parts logistics)

### Scoring

| Opportunity | Impact | Confidence | Effort | Notes |
|---|---|---|---|---|
| #1 (alert fatigue) | 5 | 5 | 4 | Top-line metric, well-evidenced, moderate build |
| #2 (root cause speed) | 4 | 4 | 2 | Big impact, but multi-quarter build |
| #3 (PM scheduling) | 5 | 3 | 2 | Big if true, but evidence is mixed |
| #4 (audit trail) | 3 | 5 | 4 | Strategic for regulated customers, well-evidenced, fast build |
| #5 (parts staging) | 3 | 4 | 3 | Adjacent, would need supply chain partnership |

### AI-feasibility filter applied

**Opportunity #1 — alert fatigue.**
- Solution A: Severity scoring (rules) → DETERMINISTIC. The plant's reliability engineers can write the rule on a whiteboard.
- Solution B: AI confidence ranking → PROBABILISTIC + EVALS. Eval surface: operator acceptance rate over 4 weeks, expert review of bottom-50% recommendations. Ship threshold: 70% acceptance, <5% confident-wrong on Tier-1 assets.
- **Recommended path:** Build A first (2 weeks, removes 60% of fatigue). Add B later when there's data to train on.

**Opportunity #2 — root cause speed.**
- Solution A: Searchable historical-incident library (deterministic + AI-assisted retrieval) → PROBABILISTIC + EVALS. Eval surface: time to find a relevant past incident, expert validation that retrieved cases are actually similar.
- Solution B: AI-generated diagnostic suggestions → PROBABILISTIC + EVALS. Eval surface: engineer acceptance rate, downstream root-cause confirmation rate.
- **Recommended path:** Build A first. B requires A to exist (you need the corpus).

**Opportunity #3 — PM scheduling.**
- Solution A: Health-index-based PM scheduling → PROBABILISTIC + EVALS. Eval surface: failure rate vs schedule rate. But: 6-month delay before signal emerges. Ship threshold: parity with current PM compliance, <2% increase in unexpected failures during pilot.
- **Recommended path:** Pilot on 50 assets first. Don't deploy fleet-wide without 6 months of evidence.

**Opportunity #4 — audit trail.**
- Solution A: Structured disposition log (rules + UI) → DETERMINISTIC. This is a database and a form.
- **Recommended path:** Build it. Don't put it on the AI roadmap. It's a 4-week feature for the regular product team.

**Opportunity #5 — parts staging.**
- Solution A: Failure-prediction-driven inventory pre-positioning → PROBABILISTIC + EVALS, but eval surface is shaky. The signal "did the right part arrive in time" is downstream of supply chain decisions outside a Fortune 100 enterprise's control.
- Solution B: Cross-customer parts pooling (deterministic rules + logistics) → DETERMINISTIC.
- **Recommended path:** B first. A is unevaluable as currently scoped — narrow it (e.g., "predict failures for 5 high-value asset classes where we control parts supply") before committing AI bandwidth.

### The roadmap that emerges

| Quarter | Build | Type | Owner |
|---|---|---|---|
| Q1 | Severity scoring (Opp #1A) + audit trail (Opp #4A) | Deterministic | Product team |
| Q1 | AI confidence ranking pilot (Opp #1B) — eval-first | Probabilistic | AI team |
| Q2 | Searchable incident library (Opp #2A) | Probabilistic | AI team |
| Q2 | Health-index PM pilot, 50 assets (Opp #3) | Probabilistic | AI team + reliability eng |
| Q3 | AI confidence ranking, fleet-wide (if pilot passes) | Probabilistic | AI team |
| Q3 | Diagnostic suggestions (Opp #2B) | Probabilistic | AI team |
| Q4 | PM rollout (if pilot passes) | Probabilistic | AI team + ops |

Note what got cut: Opportunity #5 (parts staging via prediction) is parked until the eval surface is real. That's the OST doing its job — saying no.

---

## DELIVERABLE FORMAT

Every OST produces five artifacts:

### 1. The tree (markdown)

```
# OST: [outcome]

## Desired outcome
[One sentence, measurable, time-bound]

## Opportunities

### Opportunity 1: [user struggle in user voice]
- Evidence: [interviews, data, tickets]
- Score: Impact [1-5] / Confidence [1-5] / Effort [1-5]

#### Solutions
1. [Solution name] — AI-Feasibility: [Deterministic / Probabilistic+Evals / Unevaluable]
   - Eval surface: [if probabilistic]
   - Ship threshold: [if probabilistic]
   - Experiment: [cheapest test]
2. [Solution name] — ...

### Opportunity 2: ...

## Scoring summary
[Table sorting opportunities by priority]

## Roadmap implication
[Which opportunities make the next 1-2 quarters, which are deferred, which are killed]

## What we said no to
[Explicit list of opportunities we considered and rejected, with reason]
```

### 2. Visual diagram (Excalidraw SVG)

The 4-layer tree with AI-feasibility labels color-coded:
- Deterministic (green)
- Probabilistic + Evals (amber)
- Unevaluable (red)

### 3. Scoring table

Sortable. Explicit on impact, confidence, effort. Ranked.

### 4. AI-feasibility annotations

For every probabilistic solution: eval surface, ship threshold, experiment plan.

### 5. The "no" list

Explicit list of opportunities the OST rejected, with the reason. This is the artifact that makes the OST a planning tool rather than a backlog.

---

## CROSS-LINK WITH ADJACENT SKILLS

- **`jtbd-analysis`** — A JTBD job statement becomes the desired outcome at the top of the tree. The hidden job filters which opportunities are worth pursuing.
- **`problem-ai-fit`** — For every probabilistic solution, run problem-ai-fit's 4-question test before committing. The AI-feasibility filter in this skill is a coarse cut; problem-ai-fit is the fine cut.
- **`determinism-compass`** — The deterministic vs probabilistic classification is sourced from determinism-compass. Use it to sharpen the AI-feasibility labels.
- **`eval-framework`** — Every "probabilistic + evals" solution needs an eval design. eval-framework is where that work happens.
- **`uncertainty-research`** — The experiments at the bottom of the tree use the research methods in uncertainty-research.

The chain: outcome → opportunities → solutions → AI-feasibility filter → experiments → eval design.

---

## RED TEAM

This skill produces wasted effort when:

**The work is clearly defined.** Bug fixes, regulatory deliverables, contract obligations, and tech debt don't need an OST. The opportunity is "ship the thing," and the OST adds ceremony without insight. Use a regular backlog instead.

**The team has 0 or 1 viable opportunity.** OST adds value when there are 3+ candidate directions and you need to choose. With 1 direction, you're not exploring — you're executing. Just write the spec.

**The desired outcome is unclear or non-measurable.** "Improve UX" or "support AI strategy" can't anchor an OST. Refuse to start the tree until the outcome is one sentence with a number and a date.

**The team treats the OST as a one-time artifact.** OST is alive — opportunities get added as evidence emerges, killed as experiments fail. Teams that run OST once, file it, and move on get the worst of both worlds (planning overhead without planning compounding).

**For an obvious tech debt fix or known bug.** "Users can't log in because of a CSRF token issue" doesn't need a tree. Fix it.

---

## WHEN WRONG

This skill misfires when:

- **The team forces every opportunity into the AI bucket.** AI roadmaps with no deterministic solutions are a smell. Either the work isn't truly AI-needed, or the filter wasn't applied honestly. Real AI roadmaps have 30-50% deterministic work in support of the probabilistic core.
- **The "Probabilistic + Evals" label is applied without a real eval design.** Saying "we'll measure user acceptance rate" is not an eval surface — it's a placeholder. If the eval design isn't 1-paragraph specific, the opportunity belongs in the "Unevaluable" bucket until the design is real.
- **The "no" list is empty.** Every healthy OST has rejections. An OST with 8 opportunities, all greenlit, is a backlog wearing a tree costume. Force the team to name 2-3 they're saying no to, and why.

---

## QUALITY GATE

Before shipping the OST:

- [ ] Desired outcome is one sentence, with a number and a date
- [ ] At least 3 opportunities are framed as user struggles in user voice
- [ ] Each opportunity has 2+ distinct solutions
- [ ] Every solution carries an AI-feasibility label
- [ ] Every probabilistic solution has an eval surface specified
- [ ] Scoring is explicit and sortable
- [ ] The "no" list names 2+ rejected opportunities with reasons
- [ ] The roadmap implication is named — what gets built first, what waits, what's killed

---

## CONCLUSION

Every OST ends with one paragraph:

> "We're investing in [opportunities X and Y] this cycle. We're deferring [opportunity Z] until [condition]. We're saying no to [opportunity W] because [reason]. The riskiest assumption in our top opportunity is [assumption], which we'll test by [experiment] in [timeframe]."

If the team can't write that paragraph, the tree isn't done. Loop back to the AI-feasibility filter and the "no" list — that's usually where the work skipped.
