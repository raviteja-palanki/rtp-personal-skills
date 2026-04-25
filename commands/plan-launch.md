---
name: plan-launch
description: Pre-launch readiness for AI features. Chains adoption-launch + ship-decision + cost-model + breach-ready + production-observability. Outputs a launch checklist with rollback criteria, kill-switch design, monitoring dashboard list, and comms plan. Triggers on "plan a launch," "ready to ship [AI feature]," "GA checklist."
version: 1.0.0
author: RTP (Ravi Teja Palanki)
chains:
  - adoption-launch
  - ship-decision
  - cost-model
  - breach-ready
  - production-observability
---

# /plan-launch
**Pre-launch readiness for AI features. The kill-switch design separates this from a normal launch plan.**

> "Every L4+ AI feature needs a trip-wire and a named owner who can pull it. If you can't name both, you're not ready." — RTP

---

## WHEN THIS RUNS

Trigger phrases: "plan a launch," "ready to ship [AI feature]," "GA checklist," "production rollout for AI."

Use this when:
- The AI-PRD is approved and engineering is implementing
- You're 2-4 weeks from launch
- The autonomy level is L3+ (L1-L2 features can use a normal launch plan; L3+ need this one)

Do NOT use this for:
- Internal-only experiments (use a lighter checklist)
- Pure deterministic features (use `pm-go-to-market:gtm-strategy` or similar)
- Re-launching after a rollback (use `/retro` first to learn, then this to relaunch)

---

## INPUT

The user invokes this with the feature name. If empty, ask:

1. "What AI feature is launching and what's the autonomy level?"
2. "What's the target launch date?"
3. "What's the rollback strategy if something breaks — feature flag, code revert, or no rollback path?"

If the answer to (3) is "no rollback path," stop. That's the first thing to fix.

---

## STEP 1 — ADOPTION-LAUNCH

**Skill: `adoption-launch`**

Plan the rollout pattern. Three options:

| Pattern | When to use | Risk |
|---|---|---|
| Full launch | Low-stakes, well-tested, evals all green | Low |
| Staged rollout (1% → 10% → 50% → 100%) | Most AI features at L3+ | Medium — controlled |
| Beta program (named users, opt-in) | High-stakes, novel autonomy level, regulated domain | Low — bounded |

For staged rollout, define:
- **Cohort 1** — internal users only, 1-3 days
- **Cohort 2** — friendly external users, 3-7 days
- **Cohort 3** — broader external rollout, 7-14 days
- **Cohort 4** — GA

Between cohorts: hold gates. If any acceptance metric drops below floor, hold rollout. Don't advance on optimism.

---

## STEP 2 — SHIP-DECISION

**Skill: `ship-decision`**

The four ship questions, run before launch (not before GA — before each cohort gate):

1. **Are we solving the right problem?** (Has the JTBD changed since the PRD?)
2. **Can we measure success?** (Acceptance criteria still testable, golden set still relevant?)
3. **Can we afford this at GA?** (Cost ceiling holds at projected volume?)
4. **Can we recover when it breaks?** (Failure recovery designed AND tested?)

If any answer is "no" or "we'll find out," the gate doesn't open.

---

## STEP 3 — COST-MODEL (Launch Pass)

**Skill: `cost-model`**

The launch-time cost check is different from the strategic cost check. Here you verify:

- **Pilot cost / call** — what was actual unit cost in the staged rollout?
- **Volume multiplier** — what's the realistic GA volume vs. pilot?
- **Daily ceiling** — what's the dollar amount that triggers an alert?
- **Cost-runaway scenarios** — verbose output, prompt injection driving long completions, retry storms. What does each cost in the worst hour?
- **Caching status** — is caching live in production at launch, or planned for "later"?

The structural risk: **cost ceilings without alerts are wishes**. Every ceiling needs a paged alert before launch.

---

## STEP 4 — BREACH-READY

**Skill: `breach-ready`**

The incident plan for AI failures. AI features fail differently from deterministic ones — they don't crash, they confidently return wrong answers.

Required outputs:

| Failure mode | Detection signal | Containment | Recovery |
|---|---|---|---|
| Hallucination spike | User correction rate >X% | Drop AI output, fall back to deterministic | Re-train or revert prompt |
| Refusal regression | Model refusing legitimate inputs >X% | Adjust safety threshold | Audit refusal logs, tune |
| Latency spike | P95 >X ms | Route to faster model, cache previous answers | Investigate retrieval / context bloat |
| Cost spike | Hourly cost >X | Throttle, route to cheaper model | Investigate output length / volume |
| Prompt injection | Anomalous outputs detected by judge | Isolate the input class, alert security | Patch input filter |
| Bias / unfairness | User reports or audit detection | Pause feature for affected segments | Re-eval with bias-focused golden set |

Each row needs an owner. "Engineering" is not an owner. A name is an owner.

---

## STEP 5 — PRODUCTION-OBSERVABILITY

**Skill: `production-observability`**

The monitoring dashboard list. Without this, the breach-ready plan is fiction — you can't react to failures you can't see.

Required dashboards (each linked, not just listed):

1. **AI quality dashboard** — eval pass rate over time, regression alerts, golden set delta
2. **Cost dashboard** — per-call cost, daily total, projection to month-end, ceiling utilization
3. **Latency dashboard** — P50/P95/P99 by model, by user segment, by prompt version
4. **User behavior dashboard** — adoption rate, correction rate, abandonment rate, satisfaction signal
5. **Safety dashboard** — refusals, suspicious inputs flagged, bias signals
6. **System health** — model availability, retrieval latency, error rates

Each dashboard has:
- A primary owner (named person who looks at it daily for the first 30 days)
- Alert thresholds wired to paging
- A weekly review cadence after the first 30 days

---

## STEP 6 — KILL-SWITCH DESIGN (THE L4+ REQUIREMENT)

**This is what makes AI launches different.** A kill-switch is the deliberate, designed mechanism to disable the AI feature in production without a code deploy.

For L4+ features, the kill-switch is not optional. It's the difference between "we noticed a problem and shipped a fix in 4 days" and "we noticed a problem and turned it off in 90 seconds."

**Required components:**

| Component | Definition |
|---|---|
| Trip-wire signal | The specific metric or alert that justifies pulling the switch |
| Threshold | The numeric level at which the trip-wire fires |
| Owner | One named person authorized to pull the switch (NOT a committee) |
| Backup owner | One additional named person if primary is unavailable |
| Mechanism | Feature flag / config toggle / API kill / model fallback (not a code deploy) |
| Time-to-disable | How long from decision to disabled (target: <2 minutes) |
| User experience when disabled | What the user sees — "feature temporarily unavailable" with helpful fallback |
| Re-enable criteria | What conditions must be met to turn it back on |

**The honest question:** If the AI feature started returning unsafe outputs at 3 AM on a Saturday, who pulls the switch and how long does it take? If the answer involves calling someone or filing a ticket, the kill-switch isn't real.

**Kill-switch design also needs a periodic test.** Once a quarter, run the kill-switch in a staging environment to confirm it actually works. Untested kill-switches are theater.

---

## STEP 7 — COMMS PLAN

Calls into the orchestrator's `/stakeholder-update` motion (or the `product-management:stakeholder-update` skill). Required comms:

| Audience | Channel | Cadence | Owner |
|---|---|---|---|
| Internal team | Slack channel | Daily for first week, then weekly | PM |
| Engineering / SRE | Incident channel | Real-time for any threshold breach | Eng lead |
| Leadership | Email digest | Weekly, then monthly | PM |
| Customers | In-app + email | At each cohort gate that affects them | PM + CS |
| Sales / CS | Briefing doc | Before each cohort | PM |
| Compliance / Legal (if applicable) | Memo | Before launch, after first 30 days | PM + Legal |

For each: what's said, who says it, when it's sent, what triggers an unscheduled comms (e.g., kill-switch pull → customer email within 4 hours).

---

## STEP 8 — LAUNCH TIMELINE

| T- | Action | Owner | Status |
|---|---|---|---|
| T-21 | All evals green on full golden set | Eng + PM | |
| T-14 | Cost-model verified at projected GA volume | PM | |
| T-10 | Kill-switch designed, owner named, mechanism live in staging | Eng + PM | |
| T-7 | Monitoring dashboards live; alert thresholds set | Eng + PM | |
| T-7 | Breach-ready playbook reviewed with on-call | PM + Eng lead | |
| T-5 | Comms plan approved; all draft messages reviewed | PM | |
| T-3 | Final ship-decision check; cohort 1 list confirmed | PM | |
| T-1 | Kill-switch tested in staging; rollback drill complete | Eng | |
| T-0 | Cohort 1 enabled (internal); monitoring active | Eng + PM | |
| T+3 | Cohort 1 review; gate decision for cohort 2 | PM | |
| T+10 | Cohort 2 review; gate decision for cohort 3 | PM | |
| T+24 | Cohort 3 review; gate decision for GA | PM |
| T+30 | First post-launch retrospective | PM |

---

## OUTPUT FORMAT

A single launch readiness document with:

1. **Executive summary** (1 paragraph) — what's launching, autonomy level, rollout pattern, kill-switch owner
2. **Cohort plan** (the staged rollout)
3. **Ship-decision results** (pass/hold/fail per question)
4. **Cost ceiling and alert thresholds**
5. **Breach-ready playbook** (the failure mode → owner table)
6. **Monitoring dashboards** (with links and owners)
7. **Kill-switch design** (the 8-component table, completed)
8. **Comms plan** (the audience table)
9. **Launch timeline** (T- table)
10. **Open risks** (anything not yet resolved, with owner and target date)

---

## QUALITY BAR

A real `/plan-launch` document for an L4+ AI feature has:

- A staged rollout with hold gates between cohorts, not "ship to everyone Friday"
- A kill-switch with a NAMED owner (not "engineering"), a tested mechanism, and a time-to-disable target
- Cost alerts wired to paging, not just dashboards
- Failure-mode owners specified by name for each failure mode
- A monitoring dashboard list where every dashboard has a daily-review owner for the first 30 days
- Comms drafted before launch, not improvised after

**The test:** Hand the document to the on-call engineer for the launch weekend. They should know exactly what to do if any threshold breaches. If they have questions, the document isn't done.

---

## CROSS-REFERENCES

- **Run before:** the actual launch, ideally 2-4 weeks out
- **Run after launch:** `/retro` at T+30 to extract lessons
- **Related workflows:** `/design-ai-feature` (run earlier in the cycle), `/ai-prd-flow` (the spec this is launching)
- **Skill files used:** `adoption-launch`, `ship-decision`, `cost-model`, `breach-ready`, `production-observability`
- **Stakeholder comms:** `product-management:stakeholder-update`
