# AI User Stories — The Production-Grade Story Deliverable (v1.0)

> Companion to `ai-prd-template.md`. The AI-PRD is finished as a **backlog**, not a document. This file defines the six AI story types, the inheritance map back to the PRD, the full story template, worked examples (running example: **Athena** — AI reply drafts for support agents), and the grooming checklist that keeps deterministic stories in AI costumes out of your sprint.

---

## 1 · Why AI stories are different

A normal story assumes the system reliably does X. An AI story can't — the model returns a distribution. So every AI story must carry, as **acceptance criteria**, the probabilistic decisions the PRD made: confidence thresholds, behavior examples, a named failure owner, a drift trigger, and a cost target. If those live only in the PRD (or worse, an engineer's head), the backlog ships stories that assume the model will "just work" — and production proves otherwise.

**User Story Health (the metric):** % of AI stories in the backlog carrying all five inherited elements. Target: **100% for anything shipping.** Measure it monthly; it surfaces the silent failure of teams writing deterministic stories for probabilistic features.

---

## 2 · The six story types (a world-class AI backlog has all six)

Most teams only write type 1. The other five are the invisible work that decides whether type 1 survives production.

| # | Story type | Inherits from PRD § | What it covers | Typical count per feature |
|---|---|---|---|---|
| 1 | **Capability** | §4 §5 §7 | The user-facing AI behavior itself | 3–8 |
| 2 | **Eval / quality** | §6 | Golden set, judge wiring + validation, human review queue, regression suite | 2–4 |
| 3 | **Fallback & degraded-UX** | §7 §9 | One story per degradation rung; refusal UX; recovery paths | 2–4 |
| 4 | **Guardrail & safety** | §2 §9 | Kill switch, PII filters + honeypots, rubber-stamp detection, legal gates | 2–4 |
| 5 | **Instrumentation** | §10 | Event schema, funnel, dashboards, alerting | 1–3 |
| 6 | **Rollout / ops** | §8 §12 | Shadow mode, ramp tooling, holdouts, prompt-change pipeline, runbook drills | 2–3 |

**Sequencing rule:** instrumentation (5) and eval (2) stories ship *before or with* the first capability story — shadow mode depends on them. "Monitoring later" is launch theater.

---

## 3 · The AI story template (paste into the backlog)

```
As a [user], I want [core capability] so that [outcome tied to PRD §1 hypothesis].

Acceptance criteria (probabilistic):
- Confidence > [X] → [full behavior] (P95 latency ≤ [N] ms)
- [Y]–[X] → [hedged behavior] (track user acceptance rate)
- < [Y] or safety flag → [fallback rung / route] and notify owner [Name]
- Instrumentation: events [list from §10] logged and computable in the funnel

Behavior examples:  [link ≥3 good / bad / reject from PRD §4 / Annex A]
Failure owner:      [named human, consented] — judged on catch rate, not velocity
Drift trigger:      [retrain / escalate if metric moves > X in N days, from §6]
Cost per outcome:   target $[Y] at P90 (from §11) — or the allocation assumption, ⚠-tagged
Assumptions/risks:  [⚠-tagged assumptions this story rides on + the check that retires each]
Rollout gate:       [which §8 ramp stage this story must be green for]
Out of scope:       [the §2 non-goals this story must NOT drift into]
```

**Cost, honestly:** per-story cost attribution is often not clean. Capability and fallback stories carry the feature's cost-per-outcome target directly. Enabler-type stories (eval, guardrail, instrumentation, rollout) carry the feature-level target plus their own overhead line ("eval sampling adds ~3% to run cost"), with the allocation basis written down and ⚠-tagged. A cost number without its assumption is a number nobody can challenge.

**Assumptions/risks is not decoration:** every story rides on something unretired — an unsimulated threshold, an unsampled segment, a dependency SLA. Name each on the story with the check that retires it (mirrors PRD §13). An empty line at grooming means nobody looked.

**The send-it-back rule:** a story missing thresholds, behavior examples, failure owner, drift trigger, or cost target is not ready for sprint. Exception (write it explicitly): fully autonomous, near-zero-consequence execution layers may carry `Failure owner: none by design` — but any story producing a judgment or customer-visible artifact cannot.

---

## 4 · Worked examples — one per type (Athena)

### Story A1 · Capability — high-confidence draft
As a support agent, I want a ready-to-review reply draft on routine tickets so that I resolve them in under half the current handle time.

- **AC:** confidence >0.85 → draft auto-inserted with source citations, P95 ≤2,000ms; 0.70–0.85 → collapsed "review carefully" draft with source highlights (acceptance tracked); <0.70 or safety flag → no draft, KB snippets shown, event logged.
- **AC:** facts, amounts, and commitments in the draft must match retrieved records (wording may vary — acceptable variance per §4); any unverifiable factual claim = hallucination event.
- **AC:** out-of-scope intents (§2 non-goals) render no draft — verified by the 9 REJECT examples.
- Behavior examples: GOOD #1–3, BAD #2, REJECT #1 (Annex A) · Failure owner: M. Chen · Drift: acceptance −20% w/w or eval accuracy −5% in 7 days → escalate · Cost: ≤$0.031/resolved at P90 · Rollout gate: shadow-exit · Out of scope: auto-send, non-English.

### Story A2 · Eval/quality — the golden set is a deliverable
As the AI quality owner, I want a 500-case stratified golden set with binary evals wired into CI so that no prompt or model change ships on vibes.

- **AC:** 500 cases stratified by 8 intents × difficulty × segment, incl. 60 adversarial + 40 rare-intent; every §4 behavior example present as a test case.
- **AC:** binary checks (factual ≥98%, intent ≥95%, tone ≥97%, zero confident-wrong) run on every prompt PR; red = merge blocked.
- **AC:** LLM judge validated against 200 human-labeled cases (TPR/TNR reported) before its scores gate anything.
- Failure owner: eval eng (named) · Drift: golden set refreshed monthly from production corrections · Cost: eval run ≤$15/full pass.

### Story A3 · Fallback & degraded-UX — the snippets rung
As a support agent, I want useful KB snippets when no draft qualifies so that a refusal never becomes a dead end.

- **AC:** confidence <0.70 → top-3 KB snippets ranked (cheap model) render in ≤800ms; empty-state copy tested; refusal event logged with reason code.
- **AC:** refusal rate >25% on routine intents for 7 days → alert to PM (threshold mis-tuning, §7 re-simulation).
- Behavior examples: REJECT #2–4 · Failure owner: M. Chen · Cost: snippet path ≤$0.004/request.

### Story A4 · Guardrail & safety — the kill switch is a story
As the on-call engineer, I want a one-action kill switch that degrades Athena to template mode in under 60 seconds so that a Sev-1 never waits on a deploy.

- **AC:** flag toggle reachable from on-call console; full-off ≤60s; degrades to template library, not blank UI; customer-visible drafts stop immediately.
- **AC:** drill executed in prod before 25% ramp; runbook page linked; auto-trigger wired to hallucination >2% or CSAT breach (§8 kill criteria).
- Failure owner: on-call rotation (mechanism: drill pass is a ramp gate) · Drift: n/a · Cost: n/a.

### Story A5 · Instrumentation — the funnel before the feature
As the product analyst, I want every draft to emit the §10 event schema so that all §6 metrics are computable from logs alone.

- **AC:** every draft logs trace ID, prompt version, confidence, intent, retrieval IDs, latency, tokens/cost, outcome, agent action, edit distance; Surfaced→Sent funnel renders in the dashboard.
- **AC (definition of done for the feature, not just this story):** any §6 metric not computable from logged events blocks shadow-mode start.
- Failure owner: data eng (named) · Cost: logging overhead ≤2% of request cost.

### Story A6 · Rollout/ops — shadow mode
As the PM, I want a 2-week shadow phase where drafts are generated and scored but never shown so that offline evals are validated against reality before any agent sees a draft.

- **AC:** shadow drafts scored daily against golden-set metrics; divergence >5pts between offline and shadow accuracy → Kickoff assumptions reviewed before ramp.
- **AC:** team-level randomization assignments locked and audited pre-ramp (contamination check, §8).
- Failure owner: PM · Rollout gate: this story IS the gate to 5%.

---

## 5 · Grooming checklist (run every backlog review)

- [ ] Every AI story carries all five inherited elements (thresholds, examples, owner, drift, cost) — or an explicit `none by design`.
- [ ] All six story types present for any feature past Kickoff — no capability stories sprinting ahead of instrumentation/eval stories.
- [ ] Behavior-example links resolve to the current Annex (stale links = stale spec).
- [ ] Named failure owners have *consented* and their catch-rate review is calendared — a name without the conditions is escalation theater.
- [ ] Thresholds trace to a golden-set simulation, not a guess.
- [ ] Weekly: new production corrections became new behavior examples AND new eval cases (the dual seed) — top-10 story criteria refreshed monthly.
- [ ] User Story Health computed and reported: __% (target 100%).

---

*Inheritance is the whole game: the PRD decides once; every story carries the decision. When a story and the PRD disagree, one of them is stale — fix it the same day.*
