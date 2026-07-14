---
name: feedback-triage
description: "Score user feedback by frequency × severity × strategic fit — plus the AI-failure axis that frequency-only triage misses. AI-feature feedback is bimodal (users love it, or the AI hallucinated at them), and averaging it into 'mostly positive' hides the structural problem. The fix: flag AI failures separately, because they route to a different team entirely — a hallucination goes to the eval/ML team, not design (design can't fix hallucinations). Classifies every item into 6 categories, sub-types each AI failure to its fix team, and ranks by a 4-axis score. Use when triaging support tickets, NPS comments, in-product feedback, or complaints at volume. Do NOT use for non-AI products, under ~20 items, or a clear single bug. Pairs with: failure-modes (the deep taxonomy), eval-framework (failures become regression tests), ai-product-metrics (AI-failure rate is a metric), interview-synthesis, opportunity-solution-tree. Triggers: 'triage feedback', 'rank these tickets', 'what should we fix first'."
imports:
  - failure-modes
  - ai-product-metrics
  - eval-framework
---

# Feedback Triage

**The objective:** turn an unstructured pile of user feedback into a ranked, *routed* report — with the AI-failure axis that frequency-only triage misses — for the PM setting the next sprint's priorities from a mix of tickets, NPS comments, and complaints.

## The one idea

Your dashboard says "mostly positive, some complaints." That sentence is a lie the math told you, and here is how.

Standard triage ranks by frequency × severity × strategic fit — clean, and correct for a decade of traditional features. But **AI-feature feedback is bimodal:** users either love it ("magic, saved me hours") or hate it ("it hallucinated a number and I repeated it to my client"). The middle is thin. Average across that distribution and you get "mostly positive" — which quietly buries the slice of users watching the AI fail at them.

And the complaints in that slice aren't UX issues. This is the core: **an AI failure and a UX issue land on the same screen but route to completely different fix teams.** A confusing button routes to design. A hallucinated output routes to the AI eval team — and maybe to model retraining, prompt engineering, or the grounding pipeline. *Design cannot fix a hallucination; the eval team cannot fix button placement.* So triage that doesn't separate "AI failure" from "generic UX issue" hands the fix to the wrong team, and the roadmap waits a quarter while the design team's UX research fails to move the AI complaint count.

The structural addition is one axis: a yes/no **AI-failure flag**. Add it and the routing becomes obvious. Skip it and the bimodal feedback averages into a number that tells you nothing and sends the work to the wrong place.

## How to use this skill

1. **Classify first** — every item into one of 6 categories; the category decides the fix team. (CLASSIFICATION.)
2. **Score on 4 axes** — frequency × severity × strategic fit + the AI-failure flag; the flag isn't a tiebreaker, it changes the routing path. (THE 4-AXIS SCORE.)
3. **Sub-type every AI failure and route it** — hallucination, over/under-confidence, wrong refusal, wrong routing, latency — each to a different team with a different cycle time. (THE AI-FAILURE BREAKDOWN.)

## KEY TERMS (plain language)

- **Bimodal feedback** — AI feedback clusters at "love it" and "hate it" with a thin middle; averaging it hides the failing slice.
- **AI-failure flag** — the yes/no 4th axis: did the *AI* produce a wrong/refused/failed output (1), or is this a generic UX/perf/scope issue (0)? A "1" routes to a different team entirely.
- **The 6 categories** — every item is one of: UX issue · performance · AI failure · edge case · out-of-scope request · future-capability signal.
- **AI-failure sub-type** — within an AI failure: hallucination, over-confidence, under-confidence, wrong refusal, wrong tool/routing, latency — each with its own fix team and cycle time.
- **Future-capability signal** — feedback that isn't a bug but an unmet need ("I use a different tool for that"); the most valuable and easiest-to-miss category — it feeds discovery, not a fix team.
- **Evidence tiers used below** — the frequency % bands and the ">25% AI-failure rate = structural" cutoff are ⚠ practitioner heuristics; calibrate to your product.

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../../../UNIVERSAL-SKILL-PROTOCOL.md). At minimum: where did this feedback come from, and does routing actually trigger work (if the backlog is unread, triage is theater — fix that first). **Go deep** for 50+ items, or when the product has both AI and non-AI features and routing sets the sprint. **Skip** for non-AI features with simple bugs (frequency-only is fine), under ~20 items (read each and respond individually), or a clear single bug. Then route output format.

## THE 4-AXIS SCORE

Each theme (after clustering) gets four scores; total is an 11-point scale.

- **Frequency (0–5)** — share of the corpus: 5 = >20% · 4 = 10–20% · 3 = 5–10% · 2 = 2–5% · 1 = <2% but recurring (3+) · 0 = one-off. *(Under 50 items, use counts: 5 = 10+, 4 = 5–9, 3 = 3–4, 2 = 2, 1 = 1.)*
- **Severity (0–3)** — 3 = blocking (can't complete the core task) · 2 = major friction (completes it, but must manually correct a wrong answer) · 1 = minor annoyance · 0 = cosmetic. *Score by what happens to the user, not by who's complaining.*
- **Strategic fit (0–2)** — 2 = serves a current OKR/roadmap bet · 1 = adjacent · 0 = about something being deprioritized. *Judged by what's planned, not what's exciting.*
- **AI-failure flag (0–1)** — 1 = the AI produced the wrong/refused/failed output · 0 = UX, perf, scope, content. Carries disproportionate routing weight.

**Thresholds:** 8–11 critical (this sprint) · 5–7 high (next sprint or experiment first) · 3–4 medium (backlog, watch the trend) · 0–2 low.

## CLASSIFICATION — the first cut decides the fix team

| Category | Signals | Routes to | AI-flag |
|---|---|---|---|
| **UX issue** | "couldn't find it," "the flow was confusing," "expected X got Y" | Design + UX research | 0 |
| **Performance** | "took 30s," "timed out," "froze" | Engineering (infra/perf) | 0 (1 if it's *AI inference* latency) |
| **AI failure** | "it made up a fact," "confidently told me the wrong number," "refused for no reason" | AI eval team + ML eng | 1 |
| **Edge case** | "works in English not French," "fails on special characters" | Engineering (fast fix once scoped) | 0 (1 if the AI fails on a specific input class) |
| **Out-of-scope request** | "could you add X?," "would be nice if…" | Product (acknowledge, decline/defer) | 0 |
| **Future-capability signal** | repeated unmet need, "I work around it by…," "I use a different tool for that" | Discovery / strategy | 0 |

Apply scores *within* each category — don't compare an AI-failure score directly to a UX-issue score; they're different axes of fix.

## THE AI-FAILURE BREAKDOWN — sub-type routes to the fix team

When the flag is 1, assign a sub-type — each has a different owner and a different cycle time (lumping them all as "AI complaints" delays everything):

| Sub-type | What it is | Routes to | Fix protocol (and typical cycle) |
|---|---|---|---|
| **Hallucination** | fabricated fact, invented citation | AI eval team + grounding-pipeline owner | add to eval set; audit RAG retrieval; tighten grounding (~weeks) |
| **Over-confidence** | wrong output stated with certainty | AI eval + UX (confidence display) | calibrate confidence; surface uncertainty below threshold (~1 week) |
| **Under-confidence** | hedged/refused when it shouldn't | AI eval + prompt eng | audit over-tuned refusal triggers; allow confident answers on well-supported cases |
| **Wrong refusal** | declined a legitimate request on compliance grounds that don't apply | Safety + prompt eng | audit refusal taxonomy; separate "must refuse" from "answer carefully" |
| **Wrong tool / routing** | multi-agent picked the wrong tool/agent/source | Agent design / orchestration | fix routing logic; improve tool descriptions; add ambiguous-query evals |
| **Latency failure** | so slow the user gave up (cause is the *inference* path) | AI infra + model selection | profile inference; smaller/distilled model; streaming UX |

The deep taxonomy of *how* each of these breaks lives in `failure-modes` — this skill routes them; that skill designs the fix.

## WORKED EXAMPLE — 200 feedback items on a predictive-maintenance feature

Collected over 6 weeks across in-app feedback, support tickets, and CS notes.

**Step 1 — classify:** UX 64 (32%) · Performance 18 (9%) · **AI failure 71 (36%)** · Edge case 22 (11%) · Out-of-scope 14 (7%) · Future-capability 11 (6%). *The 36% AI-failure rate is the diagnostic — above ~25% (⚠) in a mature feature means structural issues UX iteration won't solve.*

**Step 2 — score the AI-failure bucket (all axis-4 = 1), top themes:**

| Theme | F | S | Fit | Total | Sub-type |
|---|---|---|---|---|---|
| Alert ranking confusing vs operator judgment | 5 | 2 | 2 | 10 | over-confidence (false ranking, stated confidently) |
| Flagged a failure 4 hrs after the operator saw it on the floor | 4 | 3 | 2 | 10 | latency / under-detection — investigate |
| "High confidence: failure imminent" on a healthy asset | 4 | 3 | 2 | 10 | over-confidence |
| Refused to predict a Tier-2 asset ("insufficient data") | 3 | 2 | 2 | 8 | wrong refusal |
| Recommended replacing a part swapped 2 weeks ago | 3 | 2 | 2 | 8 | hallucination (context-blind) |

**Step 3 — route:** confident-wrong predictions → AI eval (calibration audit, lower Tier-1 thresholds); context-blind recommendation → grounding pipeline (add maintenance history to retrieval); wrong refusal → prompt + safety (audit refusal triggers by asset tier); latency → AI infra.

**Step 4 — score the UX bucket separately** (64 items → design/eng): can't filter alerts by plant (9), mobile truncation (7), no snooze (6).

**Step 5 — future-capability signals** (11 items → discovery, not a fix team): "share alerts with reliability engineers" (7 mentions, adjacent collaboration product); "tell me what *you* would do alongside the prediction" (4 — taps JTBD's audit-defensibility hidden job). These feed the next OST cycle.

**What the synthesis says:** the 36% AI-failure rate is structural — fix the failure modes *before* adding new AI capability, or adoption collapses; over-confidence is the most dangerous sub-type (it drives operator action on wrong data — calibrate first); the two future-capability signals point at adjacent products. The real question the triage answers isn't just "this sprint" — it's whether the AI feature stays in market or gets walked back to draft mode until the failure modes are fixed.

## WHERE THIS SKILL MEETS THE REST OF YOUR STACK

Feedback-triage produces two different outputs that travel to two different places: individual items route to fix teams; the AI-failure *rate* routes to a feature-viability decision. Trace both.

**Where the fix gets designed and held (boundary):**
- **`rtp-failure-modes`** *(import, boundary)* — this skill *routes* incoming feedback by sub-type; failure-modes carries the *deep taxonomy* of how AI breaks and designs the fix. Route here, design there — don't re-teach the taxonomy.
- **`rtp-eval-framework`** *(import)* — every recurring AI failure becomes a regression test; the triage report is the input to eval expansion. When the fix is a prompt change, that regression test is what `prompt-as-product` runs before the change ships — so a routed failure becomes a permanent guardrail, not a one-time patch.
- **`rtp-ai-product-metrics`** *(import)* — the AI-failure rate is itself a metric; track it over time, set a threshold.

**Where a theme goes for depth or discovery:**
- **`rtp-interview-synthesis`** — when a theme needs depth, run synthesis on a sample of users who reported it.
- **`rtp-opportunity-solution-tree`** — future-capability signals become opportunities in the next OST cycle.

**Where the AI-failure RATE escalates (the two-hop most triage misses):**
- **`rtp-ship-decision`** — the worked example asks the real question — "does the feature stay in market, or get walked back to draft mode?" A structural AI-failure rate (>~25%) isn't a sprint of fixes, it's a re-opened go/no-go. Triage produces the rate as evidence; ship-decision is where the walk-back call actually gets made and owned. Routing individual items without escalating a structural rate is the trap — you fix ten tickets while the feature quietly loses the market.

**Siblings and segment-aware operation:**
- **`rtp-gossip-mode`** / **`rtp-attitudinal-segmentation`** *(siblings)* — gossip catches the *informal single* signal; this processes the *structured batch*; and run this **segment-aware** (Skeptics weight a confidently-wrong answer far more than Embracers) rather than aggregated.

## RED TEAM — when this is overhead, not insight

- **No AI features** — frequency × severity × strategic fit is enough; the AI axis adds nothing.
- **Under ~20 items** — noise dominates; read each and respond individually.
- **A clear single bug** — "login broken" doesn't need a 4-axis score; fix it.
- **Internal stakeholder complaints, not user feedback** — execs/sales follow a different routing protocol; use stakeholder-mapping.
- **A backlog nobody reads** — if routing doesn't trigger work, the triage is theater; fix the upstream authority gap or stop.

## WHEN WRONG

- **The AI-failure flag applied too loosely** — "I don't like that the AI replaces my workflow" is out-of-scope or a future-capability signal, not a failure; the flag is for outputs the AI got *wrong*, not design choices users dislike.
- **Severity conflated with stakeholder volume** — a loud customer doesn't raise severity; score by user impact (note "vocal customer" separately for political routing).
- **Strategic fit judged by what's exciting** — a fascinating off-strategy theme is correctly a 0; triage routes to strategy, it doesn't set it.
- **The roadmap doesn't update from the triage** — then it produced a document, not a decision.

## QUALITY GATE

- [ ] Every item classified into one of the 6 categories
- [ ] Every AI-failure item has a sub-type assigned
- [ ] Each high-priority theme has a fix team and fix protocol (unambiguous — no "team X or Y")
- [ ] Future-capability signals tagged for discovery
- [ ] The AI-failure rate calculated and reported (tracked over time)
- [ ] Themes sourced — quotes verbatim, not paraphrased
- [ ] The "what to ignore" list is explicit

## TRADE-OFF LEDGER

By adding the AI-failure axis and sub-type routing, you bet that *where the fix goes* matters as much as *how often it's reported* — that a correctly-routed rare hallucination beats a mis-routed frequent one. You take on the classification overhead and the discipline of verbatim sourcing. **Reversible?** Fully — it's a scoring method, not a build. **The hidden trade:** the failure mode is over-flagging (calling every AI-mentioning complaint a failure), which floods the eval team with design gripes; the WHEN-WRONG guard exists to hold that line. **Confidence: High** for products with real AI surface area; the AI axis is dead weight without it (RED TEAM). What would change it: a product where AI is invisible to the user.

## CONCLUSION

Follow the Conclusion Protocol ([Universal Skill Protocol](../../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 5). A complete report ends with one paragraph: *"Of the [N] items this period, [%] were AI failures, [%] UX issues, [%] future-capability signals. The top three themes drive [Y%] of complaints. We're routing [A] to AI eval, [B] to design, [C] to discovery. The AI-failure rate is [trending up/stable/down] vs. last period — [implication for the AI roadmap]."* If it instead ends with "lots of feedback, mixed sentiment, will keep monitoring," the triage isn't done.

## VISUAL SUMMARY

After the primary output, invoke the **excalidraw-svg** skill for one visual: the bimodal feedback curve (a "loved" peak and a "hated" peak with a thin middle) above a router that splits the hated slice into two paths — UX issues → design, AI failures → eval/ML (with the sub-types fanning out to their fix teams) — so a viewer sees why averaging hides the problem and why the AI-failure axis is what routes the fix. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.
