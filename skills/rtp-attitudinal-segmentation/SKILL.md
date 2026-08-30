---
name: attitudinal-segmentation
version: v1.1_latest
description: 'Segment AI product users by their stance toward AI itself (AI Embracer, AI Neutral, AI Skeptic) rather than by role, company size, or behavior. The attitudinal cut crosses every demographic and predicts shipping decisions: each segment needs different onboarding, default autonomy, evidence, and feedback prompts, and a single-default ship loses two of three (Skeptics, who would have been your stickiest superusers, churn first). It''s invisible in standard analytics; you instrument for it or you miss it. Use when designing onboarding for an AI product, when churn splits oddly across demographic cuts, or when setting per-segment confidence thresholds. Do NOT use pre-launch, under ~20 users, or for commodity products where AI is invisible. Pairs with: feedback-triage, ai-product-metrics, confidence-tuner, uncertainty-research, jtbd-analysis (all run segment-aware). Triggers: ''users hate the AI'', ''skeptic operator'', ''split onboarding'', ''why are veterans churning'', ''grad vs veteran''.'
imports:
  - uncertainty-research
  - jtbd-analysis
  - feedback-triage
  - ai-product-metrics
---

# Attitudinal Segmentation

**The objective:** segment AI product users by their stance toward AI itself — and ship different defaults to each — for the team watching churn split in ways role and company-size can't explain. The alternative is one experience that fits the team's own profile and loses everyone else.

## The one idea

Two operators run the same predictive-maintenance AI on the same plant floor. Same role title, same job description.

**Sai, 58, forty years on the floor.** He's watched three predictive systems fail, and he can hear a bearing going from twenty feet away. He logs in once a day to check whether the AI agrees with what he already knows, and overrides it when it doesn't. An **AI Skeptic**.

**Riya, 25, two years in.** She used Copilot in school and built a side project with Claude over the summer. She trusts the confidence interval, schedules inspections off the recommendations, and is starting to skip her own walk-around because "the model would catch it." An **AI Embracer**.

Ship one experience to both and you lose both — Sai churns (or goes silent, and his ear-knowledge never reaches the model), Riya over-trusts (and gets blamed for the failure the model couldn't see). Here is the idea: **the cut that predicts their behavior isn't role, tenure, or company size — it's their stance toward AI itself,** and that cut crosses every demographic you have. The 32-year-old engineer in your churn cohort is a Skeptic who got Embracer onboarding. The 58-year-old plant manager who's your top power user is an Embracer who finally found a tool worth trusting.

Two things make this the thing most AI PMs miss. First, **it's invisible in standard analytics** — your dashboard says "PM tier churning," so you reorganize features around role, when the real cut is attitudinal; you have to instrument for it or infer it from specific signals, and most teams do neither. Second, **the default that fits the median fits neither tail** — and the tails are where retention is won or lost, because Skeptics (often your most knowledgeable users, and your stickiest once converted) churn first under an aggressive default.

The test for whether your segmentation is real: pick your next three features and write what changes in the design for an Embracer vs. a Skeptic. If the answer is "nothing," your segmentation is decoration. If it's three different defaults, it's load-bearing. (Hilary Gridley's Embracer / Neutral / Skeptic framing — Lenny's Newsletter, 2024 ◆ — is the cleanest version, because it predicts shipping decisions, not personas.)

## How to use this skill

1. **Identify the segment** — from behavioral signals (invisible instrumentation, ~70% accuracy ⚠) and a 90-second onboarding survey, used together. (INSTRUMENTATION.)
2. **Ship three defaults, not one** — onboarding length, default autonomy, evidence format, feedback prompt, trial length all shift per segment. (THE E/N/S TABLE + SHIPPING DECISIONS — the operating manual.)
3. **Design the conversion path** — move Skeptics toward Embracers over time without forcing it, and re-segment quarterly because users drift.

## KEY TERMS (plain language)

- **AI Embracer / Neutral / Skeptic** — a user's stance toward AI itself: excited and forgiving (Embracer); pragmatic, will use it if it saves measurable time (Neutral); trusts proven process, fears losing craft/judgment/job (Skeptic).
- **The attitudinal cut** — segmenting by stance toward AI rather than by demographics or behavior; it crosses every demographic.
- **Craft-protective** — a user whose identity is tied to their output; they reject AI that doesn't sound like them even when it's technically better. Distinct from Skeptic (a Craft-protective Embracer uses AI heavily — they just want it invisible).
- **Segment drift** — users move between segments over time (a Skeptic with a great month-1 can become a Neutral); re-segment quarterly.
- **Conversion path** — Skeptic → Neutral → Embracer, each move triggered by a specific moment (a Skeptic converts on one output that beats their quality bar in a domain they care about).
- **Trust mode** — a default configuration selected by segment at onboarding (the practical ship: one product, segment-selected defaults, not two products).
- **Evidence tiers used below** — ◆ named source · ⚠ practitioner estimate. Numbers like "~70% accuracy" and "3× retention" are ⚠ illustrative — measure your own.

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../../../UNIVERSAL-SKILL-PROTOCOL.md). At minimum: who is the user, what's their alternative if they refuse the AI, and what does "right answer" look like *for each segment*. **Go deep** when shipping into a heterogeneous base, when churn splits oddly across demographics, or when onboarding a population that spans "picked up Copilot in school" to "did this job for 30 years." **Skip** under ~20 active users (segment individually — name them, talk to them), for commodity products where AI is invisible, or pre-launch (you can't segment users you don't have) — but read the RED TEAM, because even mandated tools have a compliance-vs-sabotage split.

## THE THREE DIMENSIONS OF ATTITUDE

Three stacked dimensions — use together, none alone is sufficient.

1. **Adoption attitude** (how fast they adopt *any* tool): Pioneer → Early adopter → Pragmatist (the largest) → Conservative → Skeptic. (Geoffrey Moore's chasm, updated for AI.)
2. **AI-specific attitude** (how they feel about AI itself, separate from tools in general): Embracer / Neutral / Skeptic. **This is its own axis** — mixing it with adoption attitude collapses the signal. A person can be a Pioneer everywhere else and an AI Skeptic.
3. **Craft orientation** (for work where identity is tied to output): Craft-protective / Output-focused / Collaborative. Craft-protective users are often miscategorized as Skeptics — but a Craft-protective *Embracer* uses AI heavily and just wants it in their voice; a Craft-protective *Skeptic* won't touch it. Different fix.

## THE E/N/S TABLE — the operating manual

Every shipping decision flows from this. When you ship a feature, you ship three versions of the experience around it — not always three UIs, but three defaults, three messages, three onboarding paths.

| Lens | AI Embracer | AI Neutral | AI Skeptic |
|---|---|---|---|
| **Behavioral signals** | Explores advanced features week 1; high override rate; tries beta flags; raw feedback | Uses 2–3 features repeatedly; doesn't explore; asks task-specific questions | Low feature adoption; high support contact about output quality; verifies every output; may log in and never trigger AI |
| **Survey signals** | Rates AI familiarity 4–5/5; uses AI personally; "it'll change my work" | 2–3/5; tried AI, uses sparingly; "useful for some things" | 1–2/5; little personal AI use; "overhyped" or "concerning" |
| **Onboarding** | Skip basics; full surface area by day 2; tutorials feel insulting | 1–2 concrete time-saved moments *before* any feature tour | Frame as a draft assistant; transparency-first (sources, confidence, "here's why"); never auto-execute day 1 |
| **Messaging** | Speed, capability, unlocked potential | Reliability, ROI ("save 6 hrs/week") | Augmentation not replacement; control ("your judgment, accelerated") |
| **Default autonomy** | L3–L4 (act, notify) | L2–L3 (recommend, then act on confirm) | L1–L2 (suggest/draft, never auto-execute) |
| **Feedback prompt** | Open-ended ("what should this do better?") | Thumbs + one-line reason | Explicit "got this right / wrong" + reason taxonomy — **their failure logs are gold; they catch issues before your other segments do** |
| **What NOT to do** | Don't slow them with tutorials or permission prompts | Don't oversell or change the flow they memorized | Don't auto-execute, bury the override, or say "AI does this *for* you" — say "AI *drafts* this for you" |

## SHIPPING DECISIONS — same feature, three defaults

The pattern across every one: **defaults that work for the median user fail at the tails; attitudinal segmentation gives you the right tails.** Representative calls:

- **Default autonomy on a new agent feature** — Embracer L4 (act, log, tell me weekly); Neutral L3 (show, then do on OK); Skeptic L2 (draft, I'll execute). A Skeptic on L4 churns by week 2 (the AI acts without permission); an Embracer on L2 churns by week 1 (too slow). Same feature, three defaults, ~3× retention (⚠).
- **Refusal threshold** — Embracer bias to attempt (they fix bad output faster than they wait); Skeptic bias to over-refuse ("I don't know" beats a confident wrong answer — the wrong answer destroys trust permanently, the refusal is recoverable). Refusal is a trust signal, not a capability gap: Skeptics read over-refusal as honesty, Embracers as brokenness.
- **Confidence display** — Embracer hide it; Neutral on hover; Skeptic show by default (the transparency *is* the trust mechanism — most won't read every score, they need to know it's there). See `confidence-tuner` for the thresholds.
- **Onboarding length** — Embracer 90 seconds; Neutral 4 minutes on one anchor feature; Skeptic ~12 minutes broken into 3 sessions across week 1 (trust ramps with time, not content density).
- **Trial length** — Embracer 7 days (they know by day 2); Neutral 14; Skeptic 30 minimum (trust builds in week 4 — a 14-day trial for a Skeptic is a forced rejection).

**The conversion path** (segments aren't fixed; make the path exist, don't force it): *Skeptic → Neutral* on one real output that beats their quality bar in a domain they care about (design for that moment by week 3; Skeptics without it by week 4 typically churn). *Neutral → Embracer* on the second/third use case (surface adjacent jobs at week 6–8, not week 1). *Embracers don't convert further* — retain them with depth (advanced features), not conversion.

## WORKED EXAMPLE — Sai and Riya on the plant floor

Back to the two operators. The single-UX team loses both: if the AI auto-creates work orders (L4), **Sai** feels overridden, stops trusting it, and stops feeding his ear-based catches into the system — the model never learns the floor sounds sensors can't hear, and the team's best knowledge source goes silent. If the AI uses Skeptic-grade caution (L2, mandatory review), **Riya** treats every recommendation as gospel because the UI told her to, skips the walk-around, and misses a failure that needed a human eye.

The right ship is **two configurations of one product.** For Skeptic operators: AI as "second opinion" — every recommendation shows sensor data, model confidence, and the historical override rate; L2 default; one-click override whose reasons feed the model. Sai feels respected; the system learns from his ear. For Embracer operators: AI as "first pass" — recommendations include work-order drafts (still needing sign-off); L3 default; confidence collapsed; **walk-around reminders fire weekly regardless of model state, because the Embracer's blind spot is over-trust and the product must defend against it.** Same model, same data, different defaults — both stay, both contribute value the other can't.

This pattern recurs wherever AI ships into a mixed population — clinical decision support (senior physicians vs. residents), financial advisory (veteran advisors vs. new hires), legal research (partners vs. first-years). The segment names change; the shipping principle is identical. The practical mechanism is a **trust-mode toggle** exposed at onboarding, its default set by the segment survey. Most users never switch it, and that's fine — the work is getting the first 30 days right.

## INSTRUMENTATION — you can't ship segment defaults without knowing the segment

Use both paths together.

**Behavioral signals** (no user input; ~70% accuracy ⚠ — stand these up first): feature-exploration depth in week 1 (Embracers 5+, Skeptics 0–1 AI features); refusal-acknowledgment (Embracers retry/override, Skeptics abandon *to go check the source*); override frequency (Skeptics frequent + consistent, Embracers aggressive but sporadic); time-to-first-value (Embracers <10 min, Skeptics 2–4 weeks); support-contact pattern (Skeptics = output-quality/trust tickets, Embracers = feature requests); verification behavior (Skeptics click through to sources, Embracers don't).

**Onboarding survey** (5 questions, optional, ~90 sec): (1) how often you use AI tools outside work; (2) honest reaction when you read about AI; (3) how much you want the product to do automatically; (4, optional) years in this kind of work; (5, optional, highest-signal) what worries you most — open text, reveals the actual mental model. Map: Daily+Excited+"take action" → **Embracer**; Weekly+"curious but cautious"+"show then do" → **Neutral**; Rarely/Never+Skeptical/Concerned+"recommend/suggest only" → **Skeptic**. **Mixed signals are information, not noise** — Daily + "suggest only" → Embracer with a Craft-protective overlay; use Skeptic-leaning autonomy despite high familiarity.

Combine: use behavioral signals to confirm/update the survey segment over the first 30 days; re-segment quarterly.

## SEGMENT BY WHICH NEED IS THREATENED, NOT BY HOW LOUD THE RESISTANCE IS

The E/N/S table sorts people by attitude toward the technology. **This section sorts the resisters by cause**, which is what tells you what to actually do.

Three psychological needs sit under most workplace resistance. Each can be met or threatened by the very same rollout:

| Need | What it is | Met when | Threatened when |
|---|---|---|---|
| **Competence** | Feeling effective and capable | The tool extends what the person can already do | It redefines the skills that made them credible, or removes the entry-level work through which anyone becomes credible |
| **Autonomy** | Feeling in control of your own actions | Repetitive work goes away and attention is freed | Use is mandated, procedures are standardized into a cage, **or the person is held responsible for output the AI generated** |
| **Relatedness** | Having real connections at work | Freed time goes to the relational part of the job | Work that used to need collaboration is automated, access is unequal, or generational gaps widen |

**The autonomy row carries the sharpest item and it is a governance question, not an HR one.** Holding someone accountable for AI-generated output they could not meaningfully control frustrates autonomy directly. If your rollout pairs mandated use with personal accountability for the result, you have built the exact combination that produces resistance from people who otherwise like the tool.

**Which is the finding underneath all of this: resistance is not disbelief.** A person whose needs are threatened will resist a tool they privately think works well. The article's own evidence makes the point better than its argument does: **54% of respondents in one survey said they would use AI tools without formal approval, and 32% of at-work gen-AI users hide their use.** Those are not skeptics. Those are people routing around a system that threatens something, while still wanting the tool.

**So the diagnostic question changes.** Not "do they believe it works?" but **"which of the three does this rollout take from them, and what are we giving back on that same axis?"** Compensating on the wrong axis fails: more training does nothing for a threatened sense of autonomy, and more freedom does nothing for someone who has lost the path to credibility.

**Watch behavior, not stated attitude.** Coping shows up before opinion does. Adaptive coping looks like experimenting, asking for guardrails, and renegotiating scope. Maladaptive coping looks like hidden use, quiet disengagement, output passed on unread, and compliance without adoption. **Hidden use is the tell that matters most**, because it means the person has already decided the tool is useful and the organization is the problem.

*(Sources: two Apr 2026 pieces on worker response to gen AI, HBR's "Why Gen AI Feels So Threatening to Workers" and MIT Sloan Management Review's "The Human Side of AI Adoption: Lessons From the Field" — the three-needs frame and its AWARE sequence, ◆ synthesis over self-determination theory with two illustrative professions rather than a measured population; and a field-lessons piece on adoption. The 54% and 32% figures are ⚠ vendor surveys, BCG and Ivanti, cited secondhand. Falsifier: a rollout that frustrates all three needs and still gets voluntary, non-hidden adoption.)*

## WHERE THIS SKILL MEETS THE REST OF YOUR STACK

Run all of these **segment-aware, not aggregated** — that's the whole point:

- **`rtp-feedback-triage`** *(import)* — the AI-failure axis hits each segment differently; Skeptics weight a confidently-wrong answer far more than Embracers do.
- **`rtp-ai-product-metrics`** *(import)* — Skeptics generate more refusals, overrides, and support contacts; aggregated against an Embracer-heavy base, they *look* "less successful" when they're actually producing more signal. Segment the dashboards or you'll kill the segment training your model.
- **`rtp-fit-signal`** *(downstream verdict)* — the two-hop the dashboard hides: a *blended* trust curve can read CONFIRMED while Skeptics never inflected and are quietly churning under the aggregate. A CONFIRMED fit on an Embracer-heavy base isn't fit — it's a sampling artifact. The rule this skill hands forward: measure the trust curve per segment, or the PMF verdict is an average that describes no real user.
- **`rtp-confidence-tuner`** — per-segment confidence thresholds (Skeptics want over-refusal, Embracers over-attempt); one global threshold is worse for both.
- **`rtp-uncertainty-research`** *(import)* — stratify the recruit; a 25-Embracer / 5-Skeptic trust study misses Skeptic dynamics entirely.
- **`rtp-jtbd-analysis`** *(import)* — Embracers and Skeptics often share the *job* but have radically different *anxieties* about hiring the AI for it; run JTBD segment-aware to surface the anxiety differential.
- **`rtp-adoption-launch`** *(boundary)* — adoption-launch owns the *time-phased* rollout motion (surge → dip → rebound); this skill owns the *attitudinal cut* and per-segment defaults. The conversion path here feeds that motion; don't duplicate the phase logic.
- **`rtp-needs-guard`** *(boundary)* — a Skeptic's resistance is usually a psychological-need violation (competence, autonomy, belonging); needs-guard names and protects the need, this skill ships to the stance. Complementary: diagnose the need with needs-guard, ship the default here.

## RED TEAM — when this is the wrong tool

- **<20 active users** — statistical segmentation isn't meaningful; do individual user research.
- **Commodity products where AI is invisible** — the lens fires only when the product asks the user to *extend trust* (delegate, act on AI output, change a workflow). A search box doesn't need it.
- **Mandated tools with no exit** — attitude doesn't predict adoption (it's forced) but it *does* predict compliance vs. sabotage; a mandated Skeptic uses it minimally, won't share knowledge, won't report failures. Segment for compliance support, not adoption.
- **Pre-launch** — hold until the first 100 users.
- **When the differential is small** — three segments with 95% similar behavior isn't three segments; don't overfit.
- **When you can only ship one default** — ship it for the *underserved* segment (usually Skeptics) and accept that Embracers adapt — Embracers tolerate suboptimal defaults far better than Skeptics tolerate aggressive ones.

## REALITY CHECK & ANTI-PATTERNS

- **Onboarding built for Embracers (the team's own profile) is the most common AI-product shipping mistake.** PM and eng teams are Embracers; they build for themselves, then wonder why the field hates it. Recruit Skeptics into your dogfood pool deliberately — the first Skeptic dogfooder is worth 5× the twentieth Embracer (⚠).
- **Skeptics, once converted, are often your stickiest users** — they did the trust work and don't transfer it easily to a competitor. Don't ignore them on day 1 as "low engagement."
- **Sales/CS notes are attitudinal data in disguise** ("this user is hesitant," "this champion loves AI") — pipe them into the segment view before building survey infra; they're free and pre-labeled.
- **Three anti-patterns:** the **Persona Trap** (three named personas, posters, zero default changes — decoration); the **Survey-Only Trap** (segment on day 1, never update — users drift, labels decay by month 3); the **Single-Variant Trap** ("we'll do per-segment configs later" — later never arrives; if you can ship only one, ship for the underserved segment).

## QUALITY GATE

- [ ] Segment distribution estimated for the *actual* user base (not a generic AI population)
- [ ] ≥3 upcoming product decisions mapped to per-segment shipping calls
- [ ] Behavioral instrumentation specified (events, owner, dashboard)
- [ ] Survey wording drafted and approved (not just intent)
- [ ] Segment-aware dashboards planned (churn/retention/NPS by segment, not aggregate)
- [ ] Re-validation cadence set (quarterly minimum); segment-drift alert (>10% QoQ)
- [ ] Failure mode named: which segment churns first if you ship a single default?

## OUTPUT FORMAT

Three artifacts: **(1) Segment Map** (Embracer/Neutral/Skeptic/Mixed % with signal source, confidence, re-validate trigger); **(2) Per-Segment Shipping Decisions** for the next 3–5 features (Embracer/Neutral/Skeptic default · why they differ · single-default failure mode); **(3) Instrumentation Plan** (behavioral signals week 1, survey week 2–3, segment dashboards + drift alert). Generate a markdown handoff when the next skill is `confidence-tuner`, `feedback-triage`, or `adoption-launch`.

## TRADE-OFF LEDGER

By shipping three defaults instead of one, you bet that the tails (Skeptics and Embracers) matter more than the operational simplicity of a single config. You take on three onboarding paths, three default sets, and the instrumentation to route them. **Reversible?** Yes — it's configuration, not architecture. **The hidden trade:** the failure mode is *over-segmentation* — 3 attitude × 3 craft = 9 configs you can't ship; pick the dimension driving the most behavioral variance and ship for that one. **Confidence: High** for products that ask users to extend trust; **Low** for commodity/invisible-AI products (see RED TEAM). What would change it: three segments that behave 95% alike — then you have one segment with attitudinal noise.

## CONCLUSION

Follow the Conclusion Protocol ([Universal Skill Protocol](../../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 5): state the recommendation (segment distribution + the 3 shipping decisions moving first), frame the hypothesis ("Skeptics are ~X% and churning at ~Y× Embracers because we ship Embracer-default onboarding; we're wrong if Skeptic-tuned onboarding doesn't lift Skeptic month-2 retention by ≥30%"), name the key trade-off (three defaults' complexity vs. losing the tails), the biggest risk (segments drift faster than you re-validate → quarterly re-segmentation), and the next action (instrument behavioral signals first, ship the survey second, retune defaults after 60 days of data).

## VISUAL SUMMARY

After the primary output, invoke the **excalidraw-svg** skill for one visual: the three segments as three columns (Embracer / Neutral / Skeptic) with each column's default autonomy level, onboarding length, and feedback-prompt style; the mixed cell (Embracer × Craft-protective) called out as an overlay; and one arrow showing the conversion path (Skeptic → Neutral → Embracer) with the trigger event for each move. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.
