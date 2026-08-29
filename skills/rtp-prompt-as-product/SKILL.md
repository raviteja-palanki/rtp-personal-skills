---
name: prompt-as-product
version: v1.0_latest
description: 'Treat prompts as versioned product artifacts with the rigor of code deployments: version control, regression testing, A/B testing, rollback, pinned versions. The prompt is the new product surface: a five-word reorder in a system prompt can shift the output distribution across your entire user base, and you can''t eyeball it, because small changes compound non-linearly. So a prompt change gets the same release process as code: version, regression-test every category, A/B on 1–5%, release with a tested rollback. Use when shipping a prompt change to production, debugging ''the AI started behaving differently'', or designing a prompt deployment process. Distinct from prompt-craft (how to write it) and eval-driven-development (the measurement discipline). Pairs with: prompt-craft (writes the prompt), eval-framework (measures it), determinism-compass, production-observability (live monitoring), ship-decision (the gate). Triggers: ''prompt change'', ''system prompt update'', ''prompt versioning'', ''prompt rollback''.'
imports:
  - eval-framework
  - determinism-compass
---

# Prompt as Product

**The objective:** ship a prompt change without silently breaking production — for the PM who's about to hear "we just tweaked the system prompt."

## The one idea

You reorder five words in a system prompt. It's just text — the change feels local, additive, harmless — so you ship it. A day later hallucinations spike across the user base, acceptance rate creeps down, and here's the part that stings: **your evals passed and production still degraded.**

That's the whole idea in one scene: **the prompt is a product surface with the blast radius of a code deploy, disguised as a text edit.** Prompts don't behave linearly — a small change compounds, shifting which examples the model attends to, its confidence calibration, its reasoning-chain depth, its hallucination tendency, its token cost, all at once. You cannot eyeball the effect of a wording change any more than you can eyeball the effect of a database migration. It *feels* harmless precisely because it's text, and that feeling is the trap.

So the discipline is simple and non-negotiable: **a prompt change gets the same release process as code.** Version it, regression-test every category (not just the metric you meant to improve), A/B on a small cohort, ship with a *tested* rollback, and monitor by version. The red flag is "we just tweaked the system prompt" — no version, no test, no rollback plan. The green flag is a prompt change you can name, diff, roll back in under five minutes, and tie to a metric. Same discipline you'd never skip for code; the only reason teams skip it here is that a prompt looks like writing, not engineering.

## How to use this skill

1. **Run the change through the release process** — baseline → propose with intent → regression-test → A/B → release with rollback. (THE PROCESS.)
2. **Make the prompt's logic auditable** — decision tables turn "be helpful" into testable rows, each a regression case. (Step 6.)
3. **Monitor by version and practice rollback** — you should be able to name the version every user is on, and revert in <5 minutes because you've drilled it.

## KEY TERMS (plain language)

- **Prompt as product surface** — a change to the prompt changes the product for every user, like a code deploy — so it earns the same rigor.
- **Regression suite (tiered)** — smoke (10–20 canonical queries, every change), regression (100–200 known failure modes, every release), stress (1,000+ incl. adversarial, weekly), golden set (20–50 expert-curated, for *taste* not just accuracy).
- **Golden set** — hand-curated examples where a domain expert defined the "perfect" output; catches taste failures automated evals miss.
- **Decision table** — input condition → prompt behavior → expected output → test case; makes prompt logic auditable and each row a regression case.
- **A/B cohort** — a small % of traffic (1–5%) that gets the new prompt, monitored on acceptance/regeneration/edit-distance/corrections.
- **Pinned version + rollback drill** — historical prompt versions kept accessible; reverting practiced like a fire drill so it takes 5 minutes, not 3 hours.
- **Evidence tiers below** — the A/B cost figures are ⚠ illustrative (rates move); measure your own.

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../../../UNIVERSAL-SKILL-PROTOCOL.md). The diagnostic that routes everything: *can you roll back to the prompt from two weeks ago, without friction?* If no, that gap is the work. **Go deep** for a production prompt change or designing a deployment process. Then route depth and output format.

## THE PROCESS — a prompt change is a release

1. **Establish the baseline.** Version the current prompt, run the eval suite, log the metrics. Without a baseline you're comparing against vague memories of "how it used to work" and you'll ship regressions no one notices until users complain.
2. **Propose the change with intent.** Write the new version and the *why* ("reduce hallucination on factual questions"). Undocumented changes become debt — six months on, no one knows why the prompt says what it says, and you iterate blindly.
3. **Regression-test every category, not just your target.** Run the full suite; measure cost-per-output (did it get verbose?) and determinism impact. Improving one metric while breaking another is worse than no change.
4. **A/B on 1–5% of traffic** for at least 3–5 days (weekly seasonality matters). Watch acceptance, regeneration, edit distance, corrections, and silent failures (users abandoning tasks). Evals don't capture production reality; real users find the edge cases your test set missed.
5. **Release with a tested rollback.** Tag the version, keep the old one instantly accessible, monitor the first 24h aggressively, auto-rollback if key metrics degrade past threshold. Rollback is 5 minutes in theory and 3 hours in practice if you're unprepared.
6. **Use decision tables for complex prompts** — map input conditions to behavior ("factual question → cite sources, be concise"; "confidence <60% → express uncertainty"; "input contains PII → redact + log sanitized"). Each row is auditable and becomes a regression test; this replaces "be helpful" with testable logic.
7. **Structure the regression testing** into the tiered suite (smoke / regression / stress / golden) from KEY TERMS — the golden set is what catches the technically-correct-but-off-brand outputs metrics miss.

**Estimate A/B cost before running:** `daily users × cohort% × avg tokens/session × $/token × days`. *(⚠ illustrative: 10K DAU × 5% × 2K tokens × $0.002/1K × 7 days ≈ $14.)* At that price the bottleneck isn't cost, it's your ability to write and evaluate variants — so test weekly, not monthly. Cost only becomes the constraint at high volume (1M+ sessions → $1,000+/test; batch variants) or long-context tasks (shrink the cohort, extend duration). The minimum viable test: 5% cohort, 7 days, one binary outcome metric — don't build a factorial experiment when a simple A/B answers the question.

## WHERE THIS SKILL MEETS THE REST OF YOUR STACK

Three "craft" skills touch the prompt; the cuts are deliberate:

- **`rtp-prompt-craft`** — *writes* the prompt (the writing craft); this skill *manages its changes over time* (the lifecycle). "Why is the output bad?" → prompt-craft. "Why did quality drop after last week's change?" → here.
- **`rtp-context-spec`** — the third leg of the craft triad: it *designs* the context architecture (what information reaches the window, the token budget). A prompt change is often also a context change — reorder the layers or alter what the system prompt pulls in and you changed the architecture, which earns this same versioned release. Diff both, regress both; a "prompt tweak" that quietly re-plumbed the context is the change most likely to pass evals and break production.
- **`rtp-eval-driven-development` / `rtp-eval-framework`** *(import)* — EDD *defines what "good" means* and owns the eval-improvement discipline; prompt-as-product *governs how you change the prompt* in response. The anti-pattern is running this without an eval framework — managing changes without knowing if they're improvements. (EDD runs first; this runs throughout development.)
- **`rtp-production-observability`** — the by-version acceptance/correction/cost monitoring and the <1-hour detection SLA live there; this skill is what those alerts protect.
- **`rtp-determinism-compass`** *(import)* — how much output stability the change must preserve.
- **`rtp-ship-decision`** — the go/no-go gate a prompt change passes through; this skill supplies the regression + A/B evidence it needs.
- *Demand-side note:* "the prompt is the product" has a demand-side twin — influencing an external AI *buyer* is context engineering, not marketing — flagged as the `marketing-to-ai-agents` new-skill candidate and noted in `context-spec` (HBR q2-23; not duplicated here).

## DIAGNOSTIC QUESTIONS

- **Can you roll back to the prompt from two weeks ago in <5 minutes, without a deploy?** If rollback is a multi-hour redeploy, that's the first thing to fix.
- **Do you have a diff of what changed between releases — and could someone new understand *why*?** If changes live in Slack, prompt evolution is invisible.
- **Do you regression-test outside your primary metric?** Name 5 things that could break that your current evals don't check (cost-per-output that doubled is the classic).
- **Can you tie an acceptance-rate drop to a specific prompt version?** If corrections spiked 10%, could you name the change that caused it?
- **Do you *practice* rollback, like a fire drill?** The first time you roll back shouldn't be in a production incident.

## REALITY CHECK

- **Production looks like:** change → automated dashboard flag → regression evals (15 min) → automated A/B → ship/iterate/rollback (all <24h) → users see no degradation because you caught it early.
- **It does NOT look like:** "we tweaked the prompt" with no version control; evals up but production down; a 3-hour redeploy to roll back; not knowing which version users are on; a hallucination spike you can't connect to the change.

## QUALITY GATE

- [ ] Version control (git-like tracking of prompt history)
- [ ] Regression testing across all prior test sets — no degradation in any category
- [ ] A/B plan (target metrics, cohort size, duration, rollback threshold)
- [ ] Rollback procedure documented AND tested (<5 min)
- [ ] Production monitoring by version (acceptance, corrections, cost-per-output, latency)
- **Blocks shipping if:** no baseline · a regression in any category · A/B shows cost/token up >15% (usually wordy defensive prompting) · rollback untested.

## WHEN WRONG

- **You'll see** acceptance drop + corrections spike post-launch; latency up (prompt too long, model overthinking); cost-per-output up (defensive language → verbose); new hallucinations; regeneration rate up.
- **Recovery:** roll back immediately (<5 min), then read the diff — it's usually too much instruction (model confused), a removed critical example (lost signal), or a tone/framing change (shifted the reasoning path). Iterate against the eval suite first, then re-A/B.
- **Not the tool** when you need to *write* a better prompt (that's prompt-craft) or define what to measure (that's eval-driven-development).

## TRADE-OFF LEDGER

By putting a release process around every prompt change, you bet that the blast radius of a five-word edit justifies code-deploy rigor — that a caught regression is cheaper than a silent production decline users route around until acceptance quietly craters. You give up the speed of "just tweak it" for versioning, regression tests, and an A/B window. **Reversible?** That's the entire point — the discipline exists to make every change reversible in minutes. **The hidden trade:** the failure mode is *process theater* — regression suites nobody runs, rollbacks nobody drills; the ledger's rigor is only real if it's exercised. **Confidence: High** — prompt non-linearity and the "evals-pass-production-fails" gap are well-established. What would change it: a pre-launch prototype with no users, where there's nothing to regress.

## CONCLUSION

Follow the Conclusion Protocol ([Universal Skill Protocol](../../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 5): the recommendation (ship / iterate / rollback, with the regression + A/B evidence), the key trade-off (release rigor vs. tweak-and-ship speed), the biggest risk (an untested rollback, or a regression outside the target metric), and the next action (the versioned change + its A/B plan + the rollback trigger, with an owner). Hand off to `ship-decision` for the go/no-go.

## VISUAL SUMMARY

After the primary output, invoke the **excalidraw-svg** skill for one visual: the prompt-release pipeline (baseline → propose → regression → A/B on 1–5% → release → monitor by version) drawn as a code-deploy pipeline, with the rollback path looping back from "monitor" to "previous version" and a blast-radius icon on the prompt showing the five-word edit reaching the whole user base. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.
