---
name: uncertainty-research
version: v1.5_latest
description: 'Research for non-deterministic AI, where two users asking the same question get different answers, which quietly breaks every standard research method. You can''t measure a moving target with a fixed ruler: a one-session usability study captures week-1 caution when real trust stabilizes at week 4, and averages hide terrible tail quality. Instead measure behavior over time (acceptance/edit/rejection rate), stratify by output quality, find the ''good enough'' acceptance threshold empirically, and build an expiry condition into every finding because the model moves. Use when planning trust studies, threshold studies, or validating an AI feature. Do NOT use for deterministic software, batch/offline AI, or under ~50 weekly active users. Pairs with: interview-synthesis (synthesize the interviews), jtbd-analysis (the switch-interview method), ai-product-taste (defines the bar; this measures the threshold), ai-use-case-readiness (downstream). Triggers: ''trust study'', ''threshold study'', ''how good is good enough''.'
imports:
  - first-principles
  - interview-synthesis
---

# Uncertainty Research

**The objective:** design research for AI whose output varies per query — trust studies, quality-threshold studies, feature validation — for the PM about to point a fixed-artifact method (one usability session, a single-metric A/B, an "is this helpful?" survey) at a moving target.

## The one idea

In traditional software, two users clicking the same button get the same result. In an AI product, two users asking the same question may get *different answers.* That one fact — non-determinism — quietly breaks almost every standard research method, and the breakage isn't visible until you're defending your findings to a skeptical stakeholder.

Here is the core: **you cannot measure a moving target with a fixed ruler.** Three concrete breakages: a one-session usability study captures *week-1* trust (cautious, realistic) — but real trust stabilizes at week 4, so you ship on the wrong number and get blindsided when users over-trust at month 3. A single-metric A/B reports a great *average* quality while the *tail* quality is terrible — and users hit exactly the tail and remember it. An "is this helpful?" survey averages across good and bad outputs without telling you whether users even *noticed* the bad one (most don't — a different and worse problem).

So research for probabilistic products does four things differently: **measure behavior over time** (acceptance / edit / rejection rate, not opinion ratings), **stratify by output quality** (so the average never hides the tail), **find the "good enough" threshold empirically** (users may accept 60–70% quality when the alternative is nothing — you're probably over-engineering toward 95%), and **build an expiry condition into every finding**, because a model improvement three months later can invalidate the study you shipped against. A trust number without a "valid while…" clause is a liability, not an asset.

## How to use this skill

1. **Calibrate expectations first** — interview 10–15 users on what they think the AI can/can't do; an expectation gap destroys trust regardless of feature quality, and it changes which method you need. (EXPECTATION CALIBRATION.)
2. **Match the method to the uncertainty** — longitudinal for trust, stratified sampling for quality, behavioral acceptance for the threshold. (THE METHODS + THRESHOLD RESEARCH + LONGITUDINAL DESIGN.)
3. **Attach an expiry condition** — every finding gets a "valid while [model accuracy / latency / segment / alternative] holds; re-validate if…" clause. (RESEARCH DECAY.)

## KEY TERMS (plain language)

- **Non-determinism** — the same input can produce different output; the property that breaks fixed-artifact research.
- **Behavioral vs. opinion measures** — what users *do* (accept, edit, reject, verify) vs. what they *say* ("helpful, 4/5"); behavior is the signal, opinion is noise.
- **Stratified sampling** — deliberately sampling outputs across quality levels and query types, so the average never hides the tail.
- **"Good enough" threshold** — the quality level users actually *accept* (not perfect); the point where more quality stops changing behavior.
- **The behavioral knee** — on an acceptance-rate-vs-quality plot, where acceptance stops rising as quality improves; above it, more quality is wasted investment.
- **Wizard-of-Oz (WoZ)** — humans generate responses users believe are AI; validates *demand*, not quality (humans set a too-high expectation bar).
- **Research decay / expiry condition** — AI findings go stale when the model moves; every finding carries the condition under which it stays valid.
- **Evidence tiers used below** — the WoZ 30–40% discount, the domain threshold examples, and the re-validation % bands are ⚠ practitioner heuristics; measure your own.

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../../../UNIVERSAL-SKILL-PROTOCOL.md). Answer four questions before designing anything: (1) what specific *behavior* are we measuring (not "trust" — "acceptance rate over 4 weeks")? (2) who's the user and their baseline tolerance for AI error? (3) what do we do differently if the threshold is 70% vs. 90% (if "nothing," don't run the study)? (4) when does this finding expire — what model or product change makes it stale? **Skip** for deterministic or batch/offline AI, or under ~50 weekly active users (too noisy).

## THE TRAP

You will apply traditional research methods unmodified — **methodological anchoring**. The three breakages, and the fix for each:

- **A/B tests** measure one metric against one output. AI needs *multi-metric* tests (quality + time-to-value + error rate), segmented by output-quality quartile — because great average quality can hide terrible tail quality.
- **Usability sessions** capture week-1 trust (cautious). Real trust stabilizes at week 4; ship on week-1 data and you'll be surprised by over-trust at month 3.
- **Surveys** ("is this helpful?") average across good and bad outputs. You need to know whether users even *noticed* the bad one — most don't.

## EXPECTATION CALIBRATION (the prerequisite)

Before any study, interview 10–15 active users — this determines which method you need. Ask: what do you think this AI can/can't do? if it makes a mistake, what would you expect? how confident are you (1–10)? what would make you stop using it? **Interpret:** if they expect 95% and the AI delivers 75%, the *expectation gap* destroys trust regardless of quality — fix the UX framing before researching trust. If they say "I don't know what it does," your UX isn't clear — fix that first. **Post-launch,** re-run at week 2 and week 8; *inflated* expectations are the dangerous ones — they precede sharp trust collapses.

## SIMULATED CUSTOMERS ANSWER A DIFFERENT QUESTION THAN YOU ASKED

**A model asked to role-play consumers reacting to a price change does not treat the price variation as an experiment. It treats it as a clue about context.** A higher price reads as "premium," not as "the same product costing more." So instead of the downward-sloping demand curve real shoppers produce, **you can get a flat or even upward-sloping one.**

That is not noise. It is a systematic misreading of what you were testing, and it will look like a clean result.

**Digital twins do better and still miss the thing that decides adoption.** Twins built from rich behavioral profiles of real people are a reasonable stand-in for some questions. But **real customers behave irrationally in ways that matter enormously for whether they adopt something new.** They cling to sunk costs. They overweight the pain of switching. **Simulated twins make the rational choice far more often than actual humans, so they systematically underestimate the exact frictions that kill new product launches.**

**Read that failure direction carefully, because it is the dangerous one.** Simulation does not add random error around the truth. **It biases optimistic on adoption**, and it biases most optimistic on the products that are most novel, because those are the ones whose fate turns on switching cost and framing.

**Where to use them and where not:**

| Question | Simulated customers |
|---|---|
| Rough comprehension of a message, early filter on a long list of concepts | **Reasonable.** Fast, cheap, directionally useful |
| Anything hinging on price sensitivity | **No.** The context-clue failure hits this directly |
| Anything hinging on sunk costs, switching costs, or how a choice is framed | **No.** Keep it with human research |
| Whether a genuinely new product will be adopted | **No.** This is where the optimism bias is largest |

**What to run instead for the excluded rows:** lead-user panels and ethnographic fieldwork that **watch how people actually behave rather than record what a model predicts they will choose.** The distinction is the same one this skill makes everywhere between stated and revealed preference, arriving now with a new way to get it wrong at scale.

**There is no clean fix for this yet**, and saying so is more useful than a workaround that restores confidence without restoring validity.

*(Source: De Freitas, Israeli, Nave, Timoshenko & Toubia, HBR, "Research: The Innovation Problems AI Can't Solve," Aug 2026, synthesizing linked empirical work — ⚠ as reported: the article carries the direction of each finding and not its magnitude, and the underlying studies' samples are not reproduced. Falsifier: a simulated-consumer study whose price-sensitivity estimates matched a real population's within the study's own confidence bounds.)*

## GET THE GRAIN RIGHT, OR YOU DETECT A PROBLEM YOU CANNOT LOCATE

**A broad engagement survey tells you something is wrong and cannot tell you what.** It asks the wrong questions at the wrong grain, so the fixes that follow are well-intended and aimed at nothing in particular. **People then see no change, and trust drops further than if nobody had asked at all.** Asking and not fixing is worse than not asking.

**The sequence that finds the mechanism instead:**

1. **Confidential long-form interviews with the people doing the work.** This is where the mechanism surfaces. Not the sentiment, the mechanism: which specific step, which handoff, which tool, which approval.
2. **A custom survey that quantifies it per task.** Built from what the interviews found, so the questions name real steps rather than abstractions. Now you have a magnitude attached to a located problem.
3. **Results go back to the same people, who design the fix.** Diagnosis and solution design both live with the people doing the work.

**The transferable rule for any research plan: match the grain of your instrument to the grain of the decision you need to make.** A five-point satisfaction scale on "how well do our tools support you" cannot produce a roadmap item. An interview that surfaces "I re-key the same order into three systems because the integration drops line items" produces one immediately.

**Why step 3 is not decoration.** Returning results to the people who gave them is what stops the trust erosion in the first place, and the people closest to a broken step usually know the fix. **Diagnosing down and solving up is the pattern that fails**, because a fix designed one level away from the work gets the mechanism approximately right and the details wrong.

**The check to run on your own study before fielding it:** for each question, write the specific action a particular answer would trigger. Any question with no action attached is measuring mood, and mood is not a finding.

*(Source: HBR, "Frontline Workers Know How to Solve Your Organization's Biggest Problems," Jul 2026 — ⚠ practitioner-tier, a method described with no comparative data against the broad-survey approach it replaces. The trust-erosion claim is asserted rather than measured. Falsifier: a broad engagement survey that located a specific mechanism precisely enough to design a fix from it.)*

## THE METHODS — match the method to the uncertainty

| What you're testing | Wrong method | Right method | Sample · Duration |
|---|---|---|---|
| Does the AI help users? | One 1-hour usability session | Longitudinal diary study (users log interactions) | 15–25 users · 2–4 wks |
| Is output quality good? | Expert review of 5 examples | Stratified random sample of 150+ outputs, scored by experts and users separately | 50+ outputs/use case · 1 wk |
| Do users trust it? | "Would you use this?" survey | Behavioral: acceptance / edit / rejection rate over time | 100+ users · 4–8 wks |
| Better than baseline? | A/B on one engagement metric | Multi-metric A/B (quality + time-to-value + error), segmented by quality quartile | 500+/arm · 2–4 wks |
| Does trust calibrate? | Post-session NPS | Confidence curves over 4 weeks — does confidence track actual accuracy? | 30+ users, 5+ interactions each · 4 wks |

**Design for variability:** larger samples than traditional research (model variation adds noise); stratify by query complexity, user expertise, and domain; measure trust *behaviors*, not satisfaction ratings; and **record the actual output each participant saw** (it varies — this matters). **Interpret with non-determinism in mind:** never average satisfaction across varied outputs; segment by output quality; treat trust as the leading indicator and satisfaction as lagging; and ask both "was it helpful?" *and* "would you rely on it?" — different questions.

**Wizard-of-Oz** (humans generate what users think is AI) validates *demand*, not quality — its critical limitation is that humans produce near-perfect, no-latency responses, so users calibrate to a human-quality baseline; when the real AI ships at 70–80%, the expectation gap destroys trust. Use WoZ for feature discovery and UX, **never** to forecast real-AI satisfaction; if you must estimate, discount WoZ results by ~30–40% (⚠ practitioner heuristic).

**Mutual-reinforcement detector** — when a framework or study claims its components "can't be adopted separately" or are "mutually necessary," check the underlying evidence before accepting the interdependence claim. If it rests on a single cross-sectional self-report survey, treat it as unverified. Dichotomizing a self-rated outcome at its ceiling (a "perfect score" cutoff, for instance) destroys the variance a real test of interdependence needs, so what looks like non-decomposability can be a measurement artifact rather than a property of the framework. The detector does not apply when the interdependence claim comes from a decomposition test (vary one component, hold the others fixed) or from objective outcome data instead of self-report. (Source: HBR podcast survey on "super teams," ⚠ tier: self-report, ceiling-cut on two items, method and n undisclosed.)

## DIVERGE ON RETRIEVAL, CONVERGE ON REVIEW

The single design rule for how a team gathers information before it frames a problem. It runs against what most teams are currently being sold, which is a shared workspace with a shared AI in it.

**The mechanism.** Search, discovery and chat systems run on exploitation logic: popular results, relevant results, results your history predicts. When several people research the same question on the same such tool, they are independently routed to the same material and independently arrive at similar conclusions. Everyone worked alone, so everyone believes the agreement is independent confirmation. It is a shared input path wearing the clothes of consensus.

**The evidence, and it is the only measurement of idea diversity in the corpus.** Ideas from a field experiment, semantically clustered:

| | standard search | exploration-based retrieval |
|---|---:|---:|
| Novices | 1 | 2 |
| **Experts** | 2 | **5** |

On standard search, **domain experts generated no more distinct solution territory than novices.** Change the retrieval to surface semantically distant material and only the experts broke into new space. Expertise pays through recombination, recombination needs unfamiliar input, and an exploitation-based tool withholds exactly that.

**The design rule, in three parts:**

1. **Never let one shared query path serve a group that is supposed to be generating options.** Give people different entry points, different corpora, different phrasings, and deliberately assign someone the unfamiliar sources.
2. **Separate the retrieval stage from the workspace stage.** The shared workspace is right for review and wrong for gathering. Diverge while you collect, converge when you compare. Most "collaborative AI research" setups collapse the two and lose the diversity before anyone sees it.
3. **Check for the failure directly.** Cluster the material each person came back with. **One or two clusters from a group of experts is the signal**, and it will feel like alignment.

**The prompting move for a generation setting, marked untested.** Ask explicitly for approaches from unrelated industries, and ask the model to challenge the dominant assumption in its own first answer. **The study behind this tested retrieval, not generation**, so treat the transfer as a reasonable hypothesis rather than a finding. See `rtp-prompt-craft`.

*(Source: MIT SMR Research Highlight, Aug 2026 — ◆ and thinly reported: written by the researchers rather than refereed, underlying paper unnamed, lab n=104 and field n=245 across at least four cells. **Roughly 60 per cell means the expert-versus-novice null on standard search is underpowered and consistent with a modest undetected effect.** The four cluster counts carry no dispersion, no interval and no test; clustering parameters and how expertise was classified are both unstated. Strong enough to change how you design a research sprint, not strong enough to quote as an effect. Ledger pattern O; see also `rtp-bias-spotter`, ideation bubbles, and `rtp-alignment-check`, the human twin of the same blindness.)*

## "GOOD ENOUGH" THRESHOLD RESEARCH — the most important question

Not "is it perfect?" but **"what quality level do users actually accept?"** Teams assume 90%+ is required; users may accept 60–70% when the alternative is no help. Over-assume and you over-engineer (months of quality gains that don't change behavior); under-invest and you ship a 40% feature users reject.

**The protocol:** (1) prepare stratified outputs at ~50/65/75/85/95% accuracy, shown in realistic context, *not* labeled by score. (2) Recruit N≥30, **segmented from the start** — experts (accept lower quality, they catch errors) vs. novices (need higher quality, they trust without verifying); if you serve both, analyze separately or a single combined number will mislead. (3) Measure *behavior*: acceptance rate (used without editing), edit rate, rejection rate, and whether they share the output externally (external use = real trust) — not "how helpful, 1–5?". (4) Plot acceptance vs. quality and find the **behavioral knee** — where acceptance stops rising as quality improves; above it, more quality is wasted. (5) Set validity conditions: "valid for [segment] under [use case] with [alternative]; re-run if segment, alternative, or error stakes change."

**Why thresholds vary so much** (⚠ illustrative): a coding assistant lands ~60% (alternative is a blank page; devs review and catch errors); a creative-writing tool ~40–50% (heavily edited, ideation only); customer-support drafts ~70% (agents review before sending); healthcare decision support ~90–95% (alternative is a clinician, errors are patient-safety and regulated). **The pattern: threshold = cost-of-being-wrong × how often users catch the error × what the alternative looks like.** Research it; don't assume it. (The *conceptual* bar — what "good" means in the domain — is `ai-product-taste`; this skill *measures* where the acceptance knee actually sits.)

## LONGITUDINAL TRUST DESIGN

Trust doesn't stabilize in one session — it develops or collapses over weeks: **week 1** cautious, verifies everything (low trust, realistic); **weeks 2–3** trust rising, verification dropping; **week 4** stabilizing as novelty wears off; **weeks 5–8** stabilizes *or* collapses (if the AI erred, trust can plummet). The short-study trap: a 1–2 session study captures week-1 caution and you mistake it for the real number. **Requirements:** ≥4 weeks, 5+ interactions/user/week, behavioral measures (acceptance/edit/rejection), track when users *stop verifying* (over-trust to flag) and when they *start rejecting* (broken trust), N≥30 (more if segmenting expert vs. novice). Return usage matters: churn in week 3–4 is trust collapse, not novelty fatigue. **Never ship on short-form (1–2 session) research** — treat it as directional only; plan the longitudinal study as a pre-launch quality gate.

## RESEARCH DECAY — every finding expires

You measure "users trust 75% accuracy"; three months later the model hits 82%; the finding is stale and you've built against it. So **define the condition, not just a date.** Re-validation sensitivity is stakes-dependent (⚠ heuristic): low-stakes (creative) >10–15% accuracy change; mid-stakes (productivity, support) >5%; high-stakes (healthcare, finance, legal) >2–3% (near-threshold products where a small change crosses into trust collapse). Write findings as conditions: *"valid while model accuracy is 75–85%; re-validate if it changes >5% — we're mid-stakes and users are near the acceptance knee."* Keep a findings database with expiry *conditions*; the re-validation trigger is a product change, not the calendar.

## PARTICIPANT STATE IS AN UNCONTROLLED VARIABLE IN YOUR STUDY

**If you run every session at the same time of day, you have baked one cognitive state into your findings and called it the user.**

Cognitive state moves on a daily rhythm with real edges. A short window just after waking favors loose, associative thinking. Roughly mid-morning to lunch is the sharpest window for sustained, accurate focus. The post-lunch stretch is a trough that suits neither. A second loose window opens in the evening.

**What that does to research data, concretely:**

- **A concept test run at 3pm gets more "sounds fine" than the same test at 10am.** Low-arousal agreement is not preference.
- **A generative session run at 10am gets tighter, more literal answers than one run in a loose window.** You will read that as a user with no unmet needs.
- **A usability session with a participant squeezed between two meetings measures a reactive state**, which is legitimate if that is the state your feature is used in, and a confound if it is not.

**Two rules that follow:**

1. **Match the session type to the window, or spread the schedule and record the time.** Divergent work, discovery interviews and concept generation, benefits from the loose windows. Convergent work, evaluative testing and comparison, benefits from the focus window. If you cannot control it, **at minimum record session time as a variable and check whether your findings cluster by it.** That check takes ten minutes and occasionally rewrites a conclusion.
2. **Match the state to the use context on purpose.** If the feature will be used by someone triaging alerts at the end of a long shift, testing it with a fresh participant at 10am overstates comprehension. **Design the session to reproduce the state the product actually lives in**, and say in the report which state you tested.

**The same rule applies to you and your synthesis.** Synthesis is convergent work that people habitually do late, after the sessions, when they are least able to hold nuance. Move it. A findings review written in a reactive state produces the confident, flattened summary that loses exactly the contradictions worth keeping.

*(Source: Mithu Storoni on the HBR IdeaCast, "Redefining What Efficiency Means in the Age of AI," May 2026 — ⚠ mechanism-tier; the daily-rhythm windows are described from neuroscience rather than measured in a research-operations setting, and the application to study design is a deduction. Falsifier: a study whose findings show no clustering by session time when time is deliberately varied.)*

## WHERE THIS SKILL MEETS THE REST OF YOUR STACK

- **`rtp-interview-synthesis`** *(import)* — this skill describes *how to collect* the interviews and studies; interview-synthesis describes how to *synthesize* them (open→axial→selective coding). Collect here, code there.
- **`rtp-jtbd-analysis`** *(boundary — de-duplicated)* — the **switch interview** (the moment a user started or stopped trusting the AI) is a JTBD method; its 6-question script + four-forces mapping live there, and its synthesis lives in interview-synthesis. Use those two together for switch interviews — this skill points to them rather than re-teaching the method. Its unique contribution to trust research: the switch interview's *trust-moment* framing ("I trusted it on day 3 when it caught a risk our last review missed" tells you exactly what converts skeptics; "I stopped on day 8 when it cited a regulation that didn't exist" tells you the irrecoverable failure mode).
- **`rtp-ai-product-taste`** — taste *defines* the quality bar (domain calibration, magic moment); this skill *measures* where the acceptance threshold empirically sits. Bar there, measurement here.
- **`rtp-ai-use-case-readiness`** *(downstream)* — the chain problem-ai-fit → uncertainty-research → ai-use-case-readiness; the measured threshold and trust curve feed the autonomy decision.
- **`rtp-fit-signal`** *(the lightweight cousin)* — its weekly trust-curve read is a fast, low-rigor version of this skill's longitudinal trust design. fit-signal points *here* when the stakes — a board, a contested CONFIRMED verdict, a sample too small to trust — demand real rigor; this is where that trust curve gets measured properly instead of eyeballed off a weekly average.
- **`rtp-eval-framework`** — benchmarks measure *capability*; users define *acceptability*. This skill produces the acceptability number the eval bar should be set against.

## OUTPUT FORMAT

```
## Uncertainty Research Plan: [Feature]
Research question: [specific, testable — "what accuracy do clinicians require to accept AI diagnosis summaries without verifying?"]
Method: [from the methods table]
Sample: N=[≥30 threshold / 100+ trust] · segments [types + why they differ] · source
Duration: [weeks — ≥4 for trust] · [interactions/user/week]
Metrics (behavioral): primary [acceptance/edit/rejection] · secondary [verification time, return usage]
Validity conditions: valid while [accuracy X%, latency Y ms, segment, alternative]; re-validate if [triggers]
```

## REALITY CHECK

- Longitudinal AI research is expensive — budget for it or accept incomplete trust data at launch.
- WoZ sets an upper-bound expectation the real AI may miss — discount 30–40% (⚠) for real-AI satisfaction.
- Findings decay — a model improvement can invalidate research in months; every finding needs an expiry *condition*, not a date.
- The right threshold comes from users, not benchmarks — benchmarks measure capability, users define acceptability.

## QUALITY GATE

- [ ] Sources of variation mapped before study design
- [ ] Method matched to uncertainty type (from the methods table)
- [ ] Sample size accounts for model variation (≥30 for threshold studies)
- [ ] Segmented by user expertise (expert vs. novice) before analyzing the threshold
- [ ] Actual AI outputs recorded per participant (they vary — this matters)
- [ ] Results segmented by output quality, not averaged
- [ ] "Good enough" threshold from behavioral data (acceptance rate), not opinion surveys
- [ ] Validity conditions set for every major finding (condition + re-validation trigger)
- [ ] Longitudinal study (≥4 weeks) planned before the launch decision
- [ ] WoZ results discounted 30–40% if used to estimate real-AI satisfaction

## WHEN WRONG

- Deterministic features inside the AI product — use standard research methods.
- You need directional signal fast — a short study is fine, just flag it as directional, not shippable.
- The model itself will change before the research concludes — the finding is stale on arrival.
- Under ~50 weekly active users — signals too noisy for any quantitative study.

## TRADE-OFF LEDGER

By running behavioral, longitudinal, quality-stratified research with expiry conditions, you bet that a moving target needs a moving ruler — that a real acceptance number and a real trust curve beat a fast survey that measures opinion. You give up speed and money (a 4-week longitudinal study is expensive) and the comfort of a single clean number. **Reversible?** Yes — it's research, not a build. **The hidden trade:** the failure mode is *findings that expire before the team acts on them* — which is why the expiry condition, not the study itself, is the load-bearing artifact. **Confidence: High** — non-determinism genuinely breaks fixed-artifact methods. What would change it: a deterministic feature, or a product too early for its own model to hold still.

## CONCLUSION

Follow the Conclusion Protocol ([Universal Skill Protocol](../../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 5): the recommendation (method, sample, duration), the hypothesis ("users accept X quality because Y; we're wrong if acceptance at X is below Z"), the key trade-off (rigor vs. speed; longitudinal vs. directional), the biggest risk (findings expire before the team acts — mitigate with expiry conditions), and the next action (step · owner · date). If it feeds a feature decision, hand off to `ai-use-case-readiness` with the measured threshold and trust curve.

## VISUAL SUMMARY

After the primary output, invoke the **excalidraw-svg** skill for one visual: three panels — the methods matrix (what you're testing × the right method), the "good enough" curve (acceptance rate vs. output quality with the behavioral knee marked), and the trust timeline (the week 1→8 calibration arc, stabilize-or-collapse). So a viewer sees the moving target and the moving rulers built to measure it. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.
