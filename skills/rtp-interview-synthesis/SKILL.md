---
name: interview-synthesis
description: "Open → axial → selective coding for customer-interview transcripts — the same discipline serious AI eval teams run on traces, applied to human conversations. Most PMs synthesize by skimming for quotes that confirm what they already believed; code every observation first and patterns emerge from the data instead of getting cherry-picked. The payoff most PMs miss: the codes that emerge from interviews become eval failure-mode candidates when the AI ships, so this is the bridge between qualitative discovery and AI evaluation. Use when a stack of 5–15 transcripts needs to become themes, persona signals, opportunity hypotheses, and eval-test candidates. Do NOT use under 3 interviews, for sales calls in disguise, or for summary (non-verbatim) transcripts. Pairs with: uncertainty-research (how to collect them), jtbd-analysis (switch interviews → four forces), eval-framework (codes → eval failure modes), failure-modes (anxiety codes → what to design for). Triggers: 'synthesize these interviews', 'what did we hear'."
imports:
  - jtbd-analysis
  - uncertainty-research
  - eval-framework
---

# Interview Synthesis

**The objective:** turn a stack of interview transcripts into structured, auditable insight — themes, persona signals, opportunity hypotheses, and eval-test candidates — for the PM shaping a problem space where different people keep pointing to different quotes.

## The one idea

Here is how most interview synthesis actually happens: the PM reads the transcripts, highlights the "good quotes," and writes a three-bullet summary. It's fast, and it's useless — because the quotes that get highlighted are the ones that confirm what the PM already believed walking in. The patterns nobody noticed never surface. The quiet contradictions get smoothed over.

The 0.1% move is one sentence: **run the same coding discipline on humans that eval teams run on machines.** Open coding → axial coding → selective coding — label every observation with a fresh code, cluster the codes into themes, then pick the themes that drive behavior — is the core technique serious AI eval teams (Hamel Husain, Shreya Shankar ◆) run on production traces, and the same workflow grounded-theory researchers have used on qualitative data for fifty years. When you label *every* observation before deciding what matters, the pattern surfaces *from* the data instead of being imposed on it, and your conclusions become auditable — every quote got a code, so stakeholders can check your work instead of trusting your judgment.

And there's a second payoff most PMs miss entirely, which is what makes this an *AI-PM* skill and not just a research one: **the codes that emerge from interviews become eval failure-mode candidates when the AI ships.** "User distrusts the prioritization" becomes an eval test ("ranking matches expert order ≥X% of the time"); "anxiety about audit-defensibility" becomes a system-property test. This skill is the **bridge between qualitative discovery and AI evaluation** — most teams treat interviews and evals as separate workstreams; the codes are the connection, and the audit trail runs from a specific interview to a specific eval.

## How to use this skill

1. **Run the three coding passes** — open (label everything, stay close to the data), axial (cluster into 8–15 themes), selective (pick the 3–5 that drive design). Don't skip passes; the rigor compounds. (THE METHOD.)
2. **Interview AI features differently** — users can't articulate what they want from probabilistic systems; probe workflow not magic, surface the failure cost they underweight, read trust as behavior not words. (AI-PRODUCT NUANCE.)
3. **Carry the codes downstream** — selective codes → opportunity hypotheses → eval test candidates handed to `eval-framework`. (THE EVAL BRIDGE.)

## KEY TERMS (plain language)

- **Open coding** — labeling every meaningful observation with a short, literal code (3–7 words) that describes what the user *said or did*, not what you think it means.
- **Axial coding** — clustering the open codes into 8–15 themes (categories that connect multiple codes).
- **Selective coding** — picking the 3–5 themes that drive the most behavior or design implication; the spine everything else hangs off.
- **The spine** — the selective codes; the test is "if I removed this category, would the design implications change?"
- **Eval failure-mode candidate** — a required system behavior derived from a code, ready to become an eval test when the AI ships (the discovery→evaluation bridge).
- **Coding close to the data** — staying descriptive in pass 1 ("user keeps a personal Excel"), saving interpretation ("user distrusts the tool") for pass 2. Abstraction earns its place later, not first.

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../../../UNIVERSAL-SKILL-PROTOCOL.md). At minimum: how many transcripts, are they verbatim (not summaries), and will this inform a roadmap or PRD. **Go deep** for 5–15 transcripts shaping a problem space. **Skip** under 3 interviews (no reliable pattern), or when the "interviews" are sales calls in disguise (see RED TEAM). Then route output format (synthesis doc, tagged transcripts + doc, or inline).

## THE METHOD — three coding passes

**Pass 1 — Open coding (line by line).** Read every transcript and label each meaningful observation with a short code. Don't organize, don't interpret — just label, staying close to the data. Code what the user *said* (literal), what they *did or stopped doing* (behavioral), emotional language, workarounds (what they built around the official workflow), contradictions, and **silences** (questions they deflected or pivoted away from — as much data as anything spoken). A 30-minute interview yields 50–150 open codes; overlap is fine, clustering comes next. *Discipline:* "user mentioned a spreadsheet workflow" is open coding; "user feels constrained by tools" is interpretation — save it for pass 2.

**Pass 2 — Axial coding (clustering).** You now have hundreds of open codes across all interviews. Sort them (sticky notes or spreadsheet rows), group by similarity, name each group, iterate as codes move between groups. A healthy synthesis has **8–15 axial codes** — fewer than 8 means you're under-clustering ("users want a better experience"); more than 15 means you didn't push past surface differences. *Frequency matters but isn't sufficient:* a code in 8 of 10 interviews is signal, but a code in 2 of 10 that's emotionally loaded ("I cried when I saw this") may be a deeper signal your sample under-showed.

**Pass 3 — Selective coding (the spine).** Pick the **3–5 codes** that drive the most behavior or design implication. *The test:* if you removed this category, would the design implications change? Yes → selective; no → it's an axial code supporting a selective one. The selective codes drive the design implications, persona signals, and eval candidates; everything else is supporting evidence. *If your synthesis ends at "users want a better product," the selective coding wasn't done — push past the obvious.*

## AI-PRODUCT INTERVIEW NUANCE

Interviewing about AI is harder than about traditional software, because users can't articulate what they want from probabilistic systems — their expectations come from movies, marketing, and a couple of viral demos, not experience. Three patterns:

- **Users describe magic, not workflow** ("I want it to just do my job"). Probe the actual flow: "walk me through the last time you did this without AI — where does AI fit, what does it replace vs. augment?" The gap between the magic and the workflow is where the design lives.
- **Users underweight failure cost.** "What if it's wrong?" → "I'd just correct it" (rarely true). Watch for a described workflow with no review step (they assume it's right), high-frequency use (they'll stop noticing errors), or high-stakes context (confident-wrong costs far more than they'll admit).
- **Users state trust as a feeling, not a behavior.** "Do you trust it?" → "I guess?" Useless. Reformulate to behavior: "when it gives you an answer, what do you *do* with it — do you check it, how?" "Has it been wrong — what changed after that?"

**The 5 hardest questions** (most PMs skip them; skip them and your synthesis is polite and wrong): (1) "Tell me about a time the AI was wrong — what did you do?" (2) "What would have to be true for you to stop using this entirely?" (fragility of adoption). (3) "If your manager asked why you trust its recommendation, what would you say?" (social/audit dimension — no answer means they tolerate it, don't trust it). (4) "What does this AI prevent you from getting better at?" (skill-atrophy anxiety, rarely volunteered). (5) "If we removed it tomorrow, what would change?" (is it load-bearing?).

**Listen in the silence** and code it in pass 1: a pause before "yes, I trust it" (trust is social, not actual); a topic-pivot on errors (they got burned — make it safe); deflection to "the team uses it differently" (telling you what you want to hear — return to their workflow); a nervous laugh about audit-defensibility (real concern, not a joke).

## THE EVAL BRIDGE — codes become failure-mode tests

The integration most PMs miss: the axial codes from synthesis become eval failure-mode candidates when the AI ships. Same machinery, different input.

| Axial code from interviews | Eval failure-mode candidate |
|---|---|
| Distrust of system prioritization | "Prioritization order matches expert ranking ≥X% of the time" |
| Anxiety about audit-defensibility | "Every recommendation has a timestamped, exportable audit log" |
| Confident-wrong fear | "When the system says 'high confidence,' actual accuracy ≥95%" (calibration) |
| Cognitive load during morning review | "Top-5 alerts include ≥90% of true high-priority issues" |
| Skill-atrophy concern | "User can disable AI suggestions and the feature still functions" (graceful degradation) |

**The chain:** open codes → axial codes → selective codes → user-need hypotheses → design implications → required system behaviors → **eval test candidates → `eval-framework`.** When the eval team asks "where did this failure mode come from?", the answer is "axial code 4 from the synthesis dated [X]" — the audit trail that makes evals defensible to leadership, grounded in real user expectation rather than internal speculation.

## WORKED EXAMPLE — 8 plant-operator interviews on a predictive-maintenance UI

6 operators across 3 plants + 2 reliability engineers, 30–45 min each, audio-transcribed. **Pass 1:** ~1,247 open codes ("morning review takes 20–40 min," "dashboard order seems random," "I keep a personal Excel," "real failure last quarter wasn't at the top"). **Pass 2:** 11 axial codes (distrust of prioritization — 47 codes / 7 interviews; workarounds — 38 / 8; audit-defensibility anxiety — 29 / 6; morning cognitive load — 52 / 8; false-alarm fatigue — 44 / 8; …). **Pass 3 — three selective codes:** (1) *operators re-prioritize from their own mental model, ignoring the system's ranking* — the binding constraint (until the ranking matches their mental model, accuracy doesn't matter); (2) *audit-defensibility is the unspoken use case* — the paper logs and notebooks are invisible to product; (3) *attention concentrates in the morning but failures don't* — the system optimizes the wrong window.

From those: a **persona signal** ("the mental-model-first operator," in 5 of 8 — acts only when system and mental ranking align); **opportunity hypotheses** ("if the system explained *why* it ranked an alert high, adoption rises" — codes 1,5; 7 of 8); **eval candidates** ("top-5 ranked alerts include ≥90% of operator-confirmed high-priority issues" — from selective code 1; "exportable audit log per recommendation with operator disposition" — from selective code 2); and **design moves** (a "why this rank?" tooltip; structured disposition logging that doubles as audit trail and training data; severity differentiated by attention window). Every finding is evidence-grounded, hypothesis-shaped, and flows downstream — that's what synthesis output should look like.

## WHERE THIS SKILL MEETS THE REST OF YOUR STACK

- **`rtp-eval-framework`** *(import, the signature bridge)* — selective codes become eval test candidates; this synthesizes *human conversations*, eval-framework synthesizes *AI traces* — same coding machinery, different input. The codes are the connection between discovery and evaluation.
- **`rtp-uncertainty-research`** *(import)* — describes *how* to collect interviews (sampling, study design); this describes how to *synthesize* them.
- **`rtp-jtbd-analysis`** *(import)* — switch interviews get coded here, then mapped to the four forces there; synthesis is one of JTBD's input methods.
- **`rtp-failure-modes`** — the anxiety codes name what scares users most; design and eval for exactly those.

## RED TEAM — when this produces noise

- **Under 3 interviews** — anything that looks like a pattern is anecdote dressed up; run more, or use a diary study / behavioral analytics.
- **Sales calls in disguise** — if the interviewer is the salesperson or the user has a commercial stake, the codes are polite and useless; re-interview with someone unaffiliated, or discard.
- **All one persona** — deep but narrow; run separate synthesis cycles per persona, don't mush them.
- **Confirming a pre-decided direction** — "research to support the launch" bends coding toward confirmation; have someone who didn't make the decision code it, or admit it's rationalization, not discovery.
- **Summary (non-verbatim) transcripts** — already filtered through someone's interpretation; the codes describe the summarizer's mind, not the user's. Use verbatim.

## WHEN WRONG

- **The PM codes alone** — single-coder synthesis has known reliability problems; for roadmap-shaping work, have a second person independently code ~30% and compare (disagreement is informative; never disagreeing means one coder dominates).
- **Codes too abstract from the start** — "user experiences friction" is interpretation, not an open code; stay literal in pass 1.
- **Selective codes that don't change the design** — if it ends at "users want a better product," push past the obvious.

## QUALITY GATE

- [ ] Every transcript read and coded (not skimmed)
- [ ] Open codes descriptive, not interpretive
- [ ] Axial codes number 8–15
- [ ] 3–5 selective codes named and rationalized
- [ ] Frequency counts present (how many interviews surface each theme)
- [ ] Quotes verbatim, not paraphrased
- [ ] At least one finding contradicts the team's prior beliefs (else it's confirmation)
- [ ] Flows downstream — opportunity hypotheses explicit, eval candidates listed

## TRADE-OFF LEDGER

By coding every observation instead of skimming for quotes, you bet that patterns hidden in the data are worth more than the fast three-bullet summary — and that the audit trail (codes → evals) is worth the hours. You give up speed (line-by-line coding of 8 transcripts is real work). **Reversible?** Yes — it's analysis, not a build. **The hidden trade:** the failure mode is *confirmation dressed as rigor* — a PM who already decided will code toward the decision, so the "one finding that contradicts our prior" gate and the second-coder check are load-bearing. **Confidence: High** — the discovery→eval bridge is unique to this skill and is what makes evals defensible. What would change it: too few interviews (under 3) for any pattern to be real.

## CONCLUSION

Follow the Conclusion Protocol ([Universal Skill Protocol](../../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 5). A complete synthesis ends with one paragraph: *"The pattern that surprised us is [selective code]. The most consequential for design is [selective code]. The next research move is [step]. The eval implications for the AI feature are [list]. We're refining our persona to add [signal]."* If you can write that confidently, it's done; if not, go back to selective coding — that's where the work usually skipped.

## VISUAL SUMMARY

After the primary output, invoke the **excalidraw-svg** skill for one visual: the coding funnel — hundreds of open codes narrowing to 8–15 axial codes narrowing to 3–5 selective codes — with an arrow continuing from the selective codes into an "eval test candidates" box, so a viewer sees both the synthesis narrowing *and* the bridge from interviews to evals. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.
