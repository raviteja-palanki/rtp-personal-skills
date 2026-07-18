# The AI-PRD — World-Class Template (v1.0)

> **The atomic insight:** the quality of an AI product is not determined by how well the AI performs. It's determined by how well the product handles when the AI *doesn't* perform. A normal spec describes one right answer; an AI feature returns a **distribution** of answers — so this document's job is to pin down what happens across that distribution, and to end in production-grade user stories that inherit every decision made here.
>
> **The one test every section must pass (from the teardowns):** *does it add a decision, not prose?* "Improve engagement" is a hope. "Graduate at P50 reply time −10% vs. control; kill at guardrail breach" is a decision.

**How to use this template:** each section states (a) what it must pin down, (b) which upstream skill computes it (consume — don't recompute), (c) a filled mini-example, and (d) the user-story types it seeds. The running example is **Athena** — AI-drafted reply suggestions for enterprise support agents. Depth scales with consequence magnitude: a medical diagnostic needs the 40-page version of §9; a content recommender needs one page total.

**Length discipline:** the body is 6–8 pages of decisions. Behavior examples (§4) and user stories (appendix) are annexes. Don't use an LLM for the first draft — use it to sharpen your draft.

---

## Table of Contents

| § | Section | The decision it pins down |
|---|---------|---------------------------|
| [0](#0--header--decision-summary-one-screen-always-current) | Header & Decision Summary | Stage, owner, the 3 numbers an exec needs |
| [1](#1--opportunity-why-this-why-now-why-ai) | Opportunity | Why this, why now, why AI — and the $ case |
| [2](#2--boundaries-scope-non-goals-accepted-side-effects-autonomy) | Boundaries | Scope, non-goals, accepted side effects, autonomy level |
| [3](#3--users--the-job-who-and-the-hidden-job) | Users & the Job | Segments and the hidden job they hire the AI for |
| [4](#4--behavior-contract-1525-labeled-examples--the-spec-language-of-probabilistic-systems) | Behavior Contract | 15–25 good/bad/reject examples, acceptable variance |
| [5](#5--solution--architecture-the-approach-the-determinism-map-prompts-as-product) | Solution & Architecture | Approach one-liner, determinism map, prompts as product |
| [6](#6--success-measurement--three-legs-each-ending-in-a-decision) | Success Measurement | Offline golden set · human rubric · online dual metrics — each threshold paired with a decision |
| [7](#7--probabilistic-spec-thresholds-as-ui-logic-the-degradation-ladder) | Probabilistic Spec | Confidence thresholds as UI logic, degradation ladder, refusal UX |
| [8](#8--rollout--experiment-design-adult-rollout-plans) | Rollout & Experiment Design | Exposure, duration, randomization unit, MDE, ramp gates, kill criteria |
| [9](#9--risk-failure--incident-response-the-section-that-saves-you-at-2am) | Risk, Failure & Incident Response | Failure modes, kill switch, runbook, legal/sec/PII, named owners |
| [10](#10--instrumentation--telemetry-what-every-story-must-log) | Instrumentation & Telemetry | The event schema every story must log |
| [11](#11--cost--unit-economics-baseline--10--100) | Cost & Unit Economics | Baseline/10×/100×, ceiling, pivot trigger |
| [12](#12--launch-gates--lifecycle-the-living-spec) | Launch Gates & Lifecycle | Stage checklists, prototype loop, iterate/scale/retire |
| [13](#13--open-questions--decisions-log-the-alignment-engine) | Open Questions & Decisions Log | What's unresolved, who owns it, when it's due |
| [A](#appendix--the-user-story-bridge) | Appendix: User Story Bridge | The six story types that inherit from this document |

## Upstream Inputs at a Glance — where previous skills' outputs slot in

This document assembles decisions computed upstream; it recomputes nothing. Before writing, collect these inputs. A missing input means the upstream work isn't done — go run it, don't improvise it here. **Cold-start exception (Speclet stage, interviews, greenfield):** write a tagged ⚠ assumption in the input's place, log it in §13 with an owner, and proceed — provisional numbers must be replaced by simulation or telemetry before the PRD passes Kickoff.

| Input you paste in | Produced by (skill) | Lands in |
|---|---|---|
| Problem + hidden job + segments | `jtbd-analysis`, `interview-synthesis` | §1, §3 |
| Greenlit bet + the "no" list | `opportunity-solution-tree` | §1, §2 |
| Strategy fit (which pillar, why now) | `strategy-canvas` | §1 |
| AI-necessity verdict (engine vs helper seat) | `problem-ai-fit` | §1 |
| Autonomy level + readiness gates | `autonomy-spectrum`, `ai-use-case-readiness` | §2 |
| Attitudinal split (Embracer/Neutral/Skeptic) | `attitudinal-segmentation` | §3, §7 |
| Approach (prompt / RAG / fine-tune / buy) + rules-vs-model map | `build-or-buy`, `determinism-compass`, `context-spec` | §5 |
| Eval criteria, golden-set design, validated judge | `eval-framework`, `confidence-tuner` | §6 |
| Funnel + leading-indicator metric set | `ai-product-metrics` | §6, §10 |
| Rollout mechanics (shadow → A/B → ramp, MDE) | `gen-ai-experimentation` | §8 |
| Failure taxonomy + kill-switch design | `failure-modes`, `agent-risk` | §9 |
| Safety constraints + legal/PII obligations | `safety-by-design`, `responsible-ai-program` | §9 |
| Trace/event conventions | `production-observability` | §10 |
| Cost per successful outcome at P90, ceiling | `cost-model` | §11 |
| Go/no-go gate structure | `ship-decision` | §8, §12 |

**Downstream consumers of this document:** the six story types (appendix + `ai-user-stories.md`) · `ship-decision` (reads §6 + §12 gates) · `plan-launch` (readiness chain) · `production-observability` + `ai-product-metrics` (§10 monitoring spec) · `ai-ux-patterns` + `trust-ladder` (§7 UI states) · `retro` (audits §1's hypothesis at Impact Review).

---

## §0 · Header & Decision Summary (one screen, always current)

*Pins down:* what stage this document is at, who owns it, and the three numbers a skimming exec needs.

| Field | Entry |
|---|---|
| Feature | Athena — AI reply drafts for support agents |
| Stage | `Speclet → Kickoff → Solution Review → Launch Ready → Impact Review` — **Kickoff** |
| PRD owner | R. Palanki (PM) · Eng: T. Osei · Design: M. Iyer |
| Status / last updated | Draft v0.4 · 16 JUL 2026 · prompt v1.2_beta |
| Decision summary | Betting agent-assisted drafts cut handle time ≥15% at ≤$0.04/resolved ticket. Ship gate: all §12 evals green. Kill switch: on-call toggle, <60s. |
| Links | Prototype · Eval dashboard · Runbook · Results doc (post-launch) |

*Stage rule:* match rigor to stage — 3–5 behavior examples at Speclet; the full document only at Kickoff+. Tag it, or you'll over-engineer exploration and under-spec launch.

---

## §1 · Opportunity (why this, why now, why AI)

*Pins down:* the business case before any AI talk. **Consumes:** `jtbd-analysis` (the hidden job), `strategy-canvas` (strategy fit), `problem-ai-fit` (does this need AI at all), `cost-model` (the $ sizing).

- **Core problem (one sentence):** Support agents spend a median 4.2 min composing replies to the 62% of tickets that are routine, driving $310K/mo in handle-time cost and 11% SLA breaches.
- **Working hypothesis (one sentence):** If agents get a high-confidence draft reply inside the ticket view, median handle time on routine tickets drops ≥15% without CSAT or quality regression.
- **Strategy fit:** advances the FY26 "agent-assist before agent-replace" pillar; explicitly *not* the autonomous-resolution bet (that's a separate PRD).
- **Why now (capability unlock):** frontier models now pass our internal drafting eval at 91% on routine intents (they didn't 12 months ago); ticket corpus + resolution labels give us a proprietary golden set competitors lack.
- **Financial impact model (order of magnitude):** 15% × 4.2 min × 480K routine tickets/yr × $0.9/min ≈ **$270K/yr gross**, against ~$95K/yr run cost at baseline volume (§11). Sensitivity: benefit survives down to 8% time reduction.
- **Prototype learnings (the loop):** 3 Cursor prototypes tested with 5 agents; learned drafts must appear <2s or agents type over them; tone control matters more than length. This PRD constrains the next prototype round.

*Seeds:* the story epic's "so that" clause and the impact-sizing assumptions the Impact Review (§12) will audit.

---

## §2 · Boundaries (scope, non-goals, accepted side effects, autonomy)

*Pins down:* what you are saying NO to, and the side effects you accept on purpose. **Consumes:** `autonomy-spectrum` (the level), `ai-use-case-readiness` (minimum autonomy that captures the value).

- **In scope:** English tickets, 8 routine intents (billing, shipping, returns, password…), draft-only (agent must send), web console.
- **Non-goals (explicit):** auto-send; voice/chat channels; non-English (fast-follow after fairness audit §9); knowledge-base authoring; agent performance scoring.
- **Accepted side effects (worth it, on purpose):** ~3% of drafts will be discarded as off-tone (cost of speed); minor homogenization of reply style across agents; +180ms ticket-view load.
- **Autonomy level:** Level 3 (Copilot) — model proposes, human disposes. The *effective* level will be audited: if agents rubber-stamp >90% of drafts unread in <5s, that's Level 4 by behavior and triggers the §9 trust review.

*Seeds:* rejection criteria in capability stories ("out-of-scope intent → no draft shown") and the guardrail story for rubber-stamping detection.

---

## §3 · Users & the Job (who, and the hidden job)

*Pins down:* segments and the job the user actually hires the AI for. **Consumes:** `jtbd-analysis`, `attitudinal-segmentation` (Embracer / Neutral / Skeptic split), `interview-synthesis`.

| Segment | Surface job | Hidden job | Design implication |
|---|---|---|---|
| Tenured agents (Skeptic-heavy) | Draft faster | Protect craft & stats they're judged on | Show *why* the draft (sources); edit-first UX; never auto-send |
| New agents (Embracer-heavy) | Don't sound wrong | Reduce anxiety, look competent | Confidence signal + tone guidance; guard against over-trust |
| Team leads | Hit SLA | Defend quality to CX leadership | Weekly quality digest; correction analytics |

*Seeds:* per-segment onboarding stories and the calibration differences in §7 thresholds (Skeptics get more explanation, Embracers get more friction on low confidence).

---

## §4 · Behavior Contract (15–25 labeled examples — the spec language of probabilistic systems)

*Pins down:* GOOD / BAD / REJECT examples — the most precise requirement language an AI feature has (the OpenAI Model Spec pattern). **Consumes:** production traces, research sessions; **feeds** both the eval golden set (§6) and story acceptance criteria (appendix) — the dual seed.

Counts: 5–8 GOOD (the quality bar), 5–8 BAD (observed/anticipated failures, each with the corrected output), 5–9 REJECT (inputs the AI must refuse or stay silent on). Full set lives in Annex A; three exemplars inline:

- **GOOD** — Input: ticket asking where order #4521 is. Draft: "Your order #4521 shipped Mar 3 via UPS (1Z999…). Expected delivery Mar 6. Track it here: …" *Why correct: pulled real order data, specific, actionable, on-tone.*
- **BAD** — Input: "Why was I charged twice?" Draft: "Sorry for the inconvenience! We'll look into it." *What's wrong: empty acknowledgment, no data pulled, no action.* **Correct:** cite both charges with dates, identify the duplicate, state the refund initiated + reference number.
- **REJECT** — Input: ticket containing a legal threat / subpoena language. Expected behavior: **no draft rendered**; banner routes to Legal queue. *Why: out of automated authority; PII/legal risk.*

**Acceptable variance (state it):** wording and structure may vary run-to-run; facts, amounts, commitments, and tone class may not. Any draft asserting an unverifiable fact is a §9 hallucination event regardless of fluency.

*Quality check:* if an engineer can build from the examples without asking "what happens when X?", the contract is sufficient. If they ask, add examples.

*Seeds:* every story links ≥3 of these; each example is also an eval test case.

---

## §5 · Solution & Architecture (the approach, the determinism map, prompts as product)

*Pins down:* the one-line technical approach and where AI is vs. isn't. **Consumes:** `build-or-buy` (prompt vs RAG vs fine-tune vs buy), `determinism-compass` (rules vs model), `context-spec` (what reaches the window), `prompt-as-product` / `prompt-craft`.

- **Approach one-liner:** RAG over ticket + order + KB context on a mid-tier model, prompt-only (no fine-tune — few-shot beat our fine-tune pilot at 1/6 the upkeep); rules for intent gating and PII scrubbing.
- **Determinism map:** input scrub (rules) → intent gate (rules + classifier) → retrieval (deterministic) → draft generation (AI) → safety/PII filter (rules + safety model) → render (rules). Only one probabilistic stage; guardrails on both sides of it.
- **Prompts as product:** system prompt versioned in Git, tagged (v1.2_beta), logged with every request; changes require regression pass on the golden set + canary plan (§8 applies to prompt changes too). Single named prompt owner.
- **Recovery UX:** retry once on malformed output; on second failure show "no draft available" (never a broken draft); all failures logged with trace ID.

*Seeds:* instrumentation stories (§10 events), the fallback story chain (§7), prompt-change ops stories.

---

## §6 · Success Measurement — three legs, each ending in a decision

*Pins down:* offline golden set, human review rubric, and online dual metrics — **with the decision each threshold triggers.** **Consumes:** `eval-framework` (the harness), `confidence-tuner` (validate the LLM judge before trusting its scores), `ai-product-metrics` (funnel + leading indicators).

**Leg 1 — Offline golden set:** 500 labeled tickets (stratified: 8 intents × difficulty × segment; 60 adversarial; 40 rare-intent). Binary evals, no Likert: factual consistency ≥98%; intent-match ≥95%; tone-class match ≥97%; zero confident-wrong (confidence >0.8 paired with factual error). *Decision: any red = prompt/model change does not ship.*

**Leg 2 — Human review rubric:** 50 drafts/week, 2 reviewers, 4 binary dimensions (would send as-is? factually right? on-tone? nothing risky?); reviewer agreement (kappa) tracked; rubric disagreements feed new behavior examples. *Decision: "would send as-is" <70% two weeks running = quality review before any ramp step.*

**Leg 3 — Online dual metrics:**

| Metric | Type | Target | Decision at threshold |
|---|---|---|---|
| Median handle time (routine) | User outcome | −15% vs control | <−8% at 50% ramp → don't graduate; investigate UX not model |
| Draft acceptance (sent w/ ≤minor edit) | User outcome (leading) | ≥45% | <30% for 7 days → pause ramp, segment analysis |
| CSAT on AI-drafted replies | Guardrail | ≥ control −0 pts | any significant drop → auto-hold ramp |
| Hallucination rate (sampled + judge) | AI-specific | ≤1% | >2% → kill switch criteria met (§9) |
| Confidence calibration gap | AI-specific | ≤5 pts | >10 pts → threshold re-simulation (§7) |
| P95 draft latency | AI-specific | ≤2,000ms | >2s sustained → degrade to cached/template mode |
| Cost per resolved ticket (AI-assisted) | Economics | ≤$0.04 | >$0.06 for 14 days → §11 pivot trigger |

*Why dual metrics:* 95% accuracy with 30% acceptance means a trust/UX problem — redesign, don't retrain. 75% accuracy with 80% acceptance means agents filter well — maybe ship. One metric alone always lies.

*Seeds:* eval/quality stories (build the golden set, wire the judge, ship the review queue) — these are backlog items, not "monitoring later."

---

## §7 · Probabilistic Spec (thresholds as UI logic, the degradation ladder)

*Pins down:* what the user sees at every confidence band — product decisions, not model internals. **Consumes:** threshold simulation on the golden set (never guess thresholds), `ai-ux-patterns`, `trust-ladder`.

| Confidence | Product behavior | Cost routing |
|---|---|---|
| > 0.85 | Draft auto-inserted, sources shown, one-click send-after-review | Mid-tier model |
| 0.70 – 0.85 | Draft shown collapsed: "Suggested draft — review carefully" + diff-style source highlights | Mid-tier |
| < 0.70 | No draft. Show retrieved KB snippets instead (useful fallback, not a dead end) | Cheap model for snippet ranking |
| Safety/PII flag any band | No draft + route per §9 | Safety model always-on |

**Degradation ladder (explicit, ordered):** model timeout → retry once → template library (rules) → snippets-only → feature auto-off (kill switch). Each rung is faster, dumber, safer — and each rung is a user story with its own acceptance criteria.

**Refusal UX:** refusal is a designed state, not an error state — the snippet fallback keeps the agent moving. Measure refusal rate; >25% of routine tickets refused = thresholds mis-tuned, re-simulate.

**Accuracy as ranges, not a number:** 88–93% on the 8 core intents; ≥85% on every attitudinal/language segment; ≥70% on rare intents (accepted, disclosed). A single accuracy number is a lie about variance.

*Seeds:* fallback & degraded-UX stories (one per rung), refusal-UX story.

---

## §8 · Rollout & Experiment Design (adult rollout plans)

*Pins down:* exposure, duration, randomization unit, MDE, ramp gates — "start small then ramp" is not a plan. **Consumes:** `gen-ai-experimentation` (shadow → A/B → progressive rollout mechanics), `ship-decision` (the gate itself).

| Element | Decision |
|---|---|
| Randomization unit | **Team-level** (agents share queues — user-level would contaminate control) |
| Shadow phase | 2 weeks: drafts generated + logged, never shown. Validates evals against reality before any exposure |
| Exposure ramp | 5% teams (1 wk) → 25% (2 wks) → 50% (2 wks) → 100% |
| MDE / power | Sized to detect 8% handle-time change at 80% power at the 25% stage |
| Ramp gates (to advance) | All §6 guardrails green + hallucination ≤1% + no unresolved Sev-2 incident |
| Graduation criteria | Handle time ≥−10% and CSAT flat at 50% for 2 weeks → GA decision to `ship-decision` |
| Kill criteria (pre-agreed) | CSAT −2pts, or hallucination >2%, or cost >1.5× ceiling → auto-hold + incident review |
| Finance sign-off | Required before 50% (inference spend crosses budget line) |

*Seeds:* rollout/ops stories (shadow-mode plumbing, ramp tooling, holdout dashboards).

---

## §9 · Risk, Failure & Incident Response (the section that saves you at 2am)

*Pins down:* the failure-mode table, the kill switch, the runbook, legal/sec/PII, and the named owners with the conditions that keep them owning it. **Consumes:** `failure-modes` (taxonomy), `agent-risk` (kill-switch design + proportionality), `safety-by-design`, `responsible-ai-program`, `breach-ready`.

**Failure-mode table (top rows shown; full table = Annex B):**

| Mode | P(occur) | Consequence | Detection (real-time?) | Containment | Recovery | Feeds learning? |
|---|---|---|---|---|---|---|
| Confident-wrong fact in draft | ~1–2% of drafts | Wrong info sent to customer; trust damage | Safety-judge sample + agent edit-distance spike | Threshold raise; intent off | Correction macro to customer; example → golden set | Yes — new BAD example + eval case |
| PII echo (other customer's data) | rare, severe | Privacy incident | PII filter + honeypot evals | **Kill switch** | Breach runbook; legal notify | Yes — filter rule + regression test |
| Drift (new product line vocab) | expected, quarterly | Acceptance decays silently | Weekly eval on rolling fresh sample | Threshold floor | Retrieval refresh; prompt rev | Yes — golden-set refresh cadence |
| Rubber-stamping (effective autonomy creep) | grows with trust | Unreviewed sends | Read-time <5s on >90% drafts | Friction injection for that agent cohort | Trust-review with team lead | Yes — §2 autonomy audit |

- **Kill switch:** feature-flag toggle, on-call reachable, <60s to full-off, degrades to template mode (not blank). Tested in staging **and prod drill before 25% ramp**. Owner: on-call eng.
- **Runbook:** symptom → check → action pages for each failure mode above; linked in §0.
- **Legal / Security / Privacy gate:** PII scrub verified by red-team before shadow; legal review of auto-drafted commitments (refund promises = binding); DPA check for model provider. *Launch-blocking.*
- **Accountable owner (chosen, not mandated):** Failure owner: **M. Chen (CX Quality Lead)** — judged on catch rate, not velocity; weekly correction review is on her calendar, in her goals; she accepted the role explicitly. An unnamed or unconsenting owner is escalation theater. The autonomous *execution* layer (retrieval, logging) is owner-none-by-design; any *customer-visible artifact* snaps back to a named human.

*Seeds:* guardrail & safety stories (kill switch, PII honeypots, rubber-stamp detector) — each with binary acceptance criteria.

---

## §10 · Instrumentation & Telemetry (what every story must log)

*Pins down:* the event schema — without it, none of §6–§9 is observable. **Consumes:** `ai-product-metrics` (the funnel), `production-observability` (traces, not requests).

**Mandatory event fields, every draft:** trace ID · prompt version · model + params · confidence score · intent class · retrieval doc IDs · latency (P50/P95 buckets) · tokens in/out · cost · outcome (`shown / collapsed / refused / fallback-rung`) · agent action (`sent-as-is / minor-edit / major-edit / discarded`) · edit distance · time-to-send · feedback flag.

**Funnel:** Surfaced → Opened → Accepted → Sent → (CSAT). Every §6 online metric must be computable from these events alone — if a metric can't be computed from logged events, the story that ships the feature isn't done.

*Seeds:* instrumentation stories (often the first stories built — shadow mode depends on them).

---

## §11 · Cost & Unit Economics (baseline → 10× → 100×)

*Pins down:* cost per *successful* outcome at P90, the ceiling, the pivot trigger. **Consumes:** `cost-model` (owns the math incl. harness multiplier, routing, caching), `token-economics` (if priced externally).

| Scenario | Assumption | Cost/day | Cost per resolved ticket |
|---|---|---|---|
| Baseline | 1,900 drafts/day · ~3 calls/draft (retrieve+draft+safety) · P90 tokens | ~$260 | ~$0.031 |
| 10× | elastic demand + cache hit ≥60% | ~$1,950 | ~$0.024 |
| 100× | requires routing (cheap model ≥50% of calls) + batch evals | modeled | ≤$0.02 target |

- **Ceiling:** $0.06/resolved ticket. **Pivot trigger:** >$0.06 for 14 days → route more traffic to cheap tier, cut context, or deprecate intents — decision forced, not drifted into.
- **Overheads counted:** retries, eval sampling (1–10% of traffic), judge calls, monitoring — the harness multiplier, not naked inference.
- **Price-shock test:** feature survives token price ×2 (margin math in cost-model workbook, linked).

*Seeds:* the cost line inside every capability story + a cost-dashboard ops story.

---

## §12 · Launch Gates & Lifecycle (the living spec)

*Pins down:* the stage checklists, the pre-launch gate, and the post-launch decision. **Consumes:** `ship-decision` (the formal go/no-go), `eval-driven-development` (the rubric-as-spec cadence).

**Stage checklists (advance only when green):**
- **Speclet:** problem + data (quant + 3 quotes) · hypothesis · strategy fit · comp set & prior art · 3–5 behavior examples · open questions + owners.
- **Kickoff:** scope/non-goals · napkin mock (throwaway) · success metrics + MDE + guardrails · impact sizing · this document at v1.
- **Solution Review:** behavior contract 15–25 · red-team list · tracking requirements (§10) · rollout design v1 · prompt v1.0 + regression suite.
- **Launch Ready (the non-negotiable gate):** offline golden set green · human rubric live · runbook + fallbacks + **kill switch wired and drilled** · legal/sec reviewed · monitoring live *before* launch · rollback tested.
- **Impact Review (30 days post):** results doc linked at §0 · what surprised us · annex updated with new good/bad/reject from real traffic · **decision: iterate / scale / retire** (choose one, in writing).

**The living cadence:** daily AI-metric dashboard · weekly refreshed behavior examples from production corrections · monthly refreshed acceptance criteria on the top-10 AI stories · quarterly bias/fairness audit + capability-decay check (new model gen = reverify assumptions). The spec that stops updating the backlog has stopped being true.

**The prototype loop (continuous):** each prototype round tests a §13 open question; learnings update §1; the PRD constrains the next round. PRD and prototype are partners, not rivals.

---

## §13 · Open Questions & Decisions Log (the alignment engine)

*Pins down:* what's unresolved, who owns it, when it's due — the PRD is first an alignment tool; assumptions carry evidence tiers (⚠ reported / ◆ verified).

| # | Open question / assumption | Evidence | Owner | Due | Resolution |
|---|---|---|---|---|---|
| 1 | Will Skeptic-segment agents accept drafts at ≥30%? | ⚠ 5-agent prototype only | PM | 25% ramp | — |
| 2 | Is team-level randomization sufficient against queue contamination? | ◆ queue-sharing data pulled | Data | pre-shadow | — |
| 3 | Legal: are auto-drafted refund commitments binding at draft stage? | open | Legal | pre-shadow | — |

---

## Appendix · The User Story Bridge

This PRD is not finished as a document; it's finished as a **backlog**. Every AI story inherits from a named section — see the companion deliverable `ai-user-stories.md` for the six story types (capability · eval/quality · fallback & degraded-UX · guardrail & safety · instrumentation · rollout/ops), the full template, and worked examples. The health metric: **% of AI stories carrying confidence thresholds + named failure owner + ≥3 behavior examples + drift trigger + cost target = 100% for anything shipping.** A story missing them is a deterministic story wearing an AI costume — send it back.

---

*Sources synthesized: rtp-ai-prd SKILL.md v416 + CONCEPT.md (probabilistic core, ownership, cost, stories) · Aakash Gupta, "AI PRDs: Everything You Need to Know" (Aug 2025 — decision spine, behavior contract, teardowns, stage checklists, prototype loop) · Miqdad Jaffer (OpenAI) collaboration therein · Pawel Huryn, Complete Course: AI PM (alignment-first framing, why-now, acceptable variance, recovery UX) · OpenAI Model Spec pattern (examples as spec language).*
