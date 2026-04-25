# Workflows — Two Categories

The `workflows/` folder holds two distinct kinds of orchestrated work. They serve different needs and live side by side without overlap.

## 1. Sprint Templates (multi-day project plans)

Run when: kicking off a new initiative, running a quarterly cadence, executing an incident response, or any work that spans days and orchestrates 30+ skills end-to-end. These are project blueprints, not single prompts.

| File | Timeline | Purpose |
|---|---|---|
| `new-ai-feature.md` | 12 days | Concept → launch full cycle. Chains 39 skills across discovery, strategy, spec, launch. |
| `ai-discovery-sprint.md` | 5 days | High-intensity discovery sprint. Validate problem-solution fit, map failure landscape, architecture clarity, research roadmap. |
| `quarterly-strategy-review.md` | 5 days | Quarterly strategy refresh. Capability check, moat erosion, build-or-buy reassessment, roadmap adjustment. |
| `ai-incident-response.md` | hours-days | Active AI incident response. Triage, communicate, contain, retro. |
| `eval-ops-setup.md` | days | Stand up an eval pipeline from scratch. Open coding, axial coding, eval suite, regression tests, drift watch. |
| `agent-launch-checklist.md` | days | Pre-launch readiness for an agentic system. Autonomy spec, safety review, kill-switch, observability, comms. |

## 2. Slash Commands (single-prompt skill chains)

Run when: a single-shot decision or output is needed that pulls multiple skills together in one motion. Triggered by typing `/{name}` — execute end-to-end in one session.

| Command | Chains | Purpose |
|---|---|---|
| `/brief-me` | memory + recent activity | 60-second morning briefing — what's pending, overdue, at risk, where to start. |
| `/stakeholder-update` | stakeholder-communications + memory + activity | Audience-tailored update (exec / eng / customer) with AI-native confidence framing. |
| `/weekly-digest` | week's CHANGE_LOG + git activity + ACTION-PLAN deltas | Stakeholder-facing weekly digest, ready to paste. |
| `/design-ai-feature` | 10-skill gauntlet (problem-ai-fit → ai-prd) | Pre-build validation gates with STOP signals. The single most valuable workflow before any AI feature build. |
| `/ai-prd-flow` | problem-ai-fit + use-case-readiness + jtbd-analysis + ai-prd + ship-decision | Lighter PRD-writing motion when context is established. |
| `/discover` | problem-ai-fit + jtbd-analysis + opportunity-solution-tree + uncertainty-research | Single-prompt discovery cycle. |
| `/triage-feedback` | feedback-triage + failure-modes | Score and route a batch of feedback in one motion. |
| `/strategy-review` | strategy-canvas + moat-finder + competitive-map + cost-model + signal-scanner | On-demand strategic check (the lighter cousin of the 5-day sprint). |
| `/plan-launch` | adoption-launch + ship-decision + cost-model + breach-ready + production-observability | Pre-launch readiness with kill-switch design. |
| `/retro` | ai-prd lookup + ai-product-metrics + stress-test + feedback-flywheel | Post-ship retrospective with assumption audit. |

## Picking which one

- **Need a multi-day project plan?** → Sprint template.
- **Need a single output now (PRD, update, briefing, decision)?** → Slash command.
- **Need both at once?** → Run the slash command first to validate, then the sprint template to execute.

The slash commands are NOT replacements for the sprint templates — they're the daily-cadence layer that supports execution between sprint cycles.
