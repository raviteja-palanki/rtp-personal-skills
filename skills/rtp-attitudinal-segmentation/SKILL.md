---
name: rtp-attitudinal-segmentation
description: >
  Segment AI product users by stance toward AI itself — AI Embracer, AI Neutral,
  AI Skeptic — not just by role, company size, or behavior. Each segment needs
  different onboarding, different default autonomy levels, different evidence,
  different feedback prompts. Use when designing onboarding for an AI product,
  triaging churn that splits oddly across demographic cuts, planning a launch
  that crosses a mixed user base (e.g., new grads + 30-year veterans), or
  setting per-segment confidence thresholds. Triggers: "AI embracer vs skeptic",
  "users hate the AI", "skeptic operator", "split onboarding", "attitude
  segmentation", "psychographic", "trust by user type", "why are veterans
  churning", "grad vs veteran".
imports:
  - uncertainty-research
  - jtbd-analysis
  - feedback-triage
  - ai-product-metrics
---

# Attitudinal Segmentation

## DEPTH DECISION

**Go deep if:** You're shipping an AI product into a heterogeneous user base, watching churn split unpredictably across demographic cuts, designing onboarding from scratch, or planning launch into a population where some users picked up Copilot in school and others have done the job for 30 years.

**Skim to The Embracer / Neutral / Skeptic Table if:** You already have a segmentation, just need the per-segment shipping logic.

**Skip if:** Fewer than 20 active users (statistical segmentation isn't meaningful), commodity products where attitude doesn't predict behavior, or the product is mandated and users have no exit (but read the Red Team — even mandated tools have a compliance vs sabotage split).

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md):
1. Ask the Grounding Questions — at minimum: Who is the user? What's their alternative if they refuse the AI? What does "right answer" look like for each segment?
2. Route depth: Executive Summary or Comprehensive Analysis?
3. Identify output format: Document, presentation, or inline plan?

## THE STRUCTURAL INSIGHT

Most product teams segment by demographics (role, company size, industry) or behavior (active, churned, engaged). For traditional SaaS, that's enough. For AI products, it isn't.

The 0.1% angle: **segment by stance toward AI itself.** Embracers, Neutrals, and Skeptics each need different onboarding, messaging, default autonomy, feature surface, evidence format, and trust-building cadence. A team that ships the same UX to all three loses Skeptics first — who could have been your superusers — and over-onboards Embracers, who hated being slowed down by tutorials they didn't need.

This is what most AI PMs miss until churn hits. Their dashboard shows "PM tier churning" or "engineering tier churning," and they reorganize features around role. The actual cut is attitudinal — and it crosses every demographic you have. The 32-year-old engineer in your churn cohort is a Skeptic who got Embracer onboarding. The 58-year-old plant manager who's your top power user is an Embracer who finally found a tool good enough to trust.

The honest read: you can't see this without instrumenting for it. Attitudinal segmentation is invisible in standard analytics. You have to ask, or you have to infer from very specific behavioral signals (feature exploration depth, refusal acknowledgment rate, override frequency, support contact tone). Most teams do neither.

Hilary Gridley's framing in Lenny's Newsletter (2024) — Embracer / Neutral / Skeptic — is the cleanest version of this. It works because it's not psychographic vanity. It predicts shipping decisions.

A test for whether your current segmentation is doing real work: pick the next three features in your roadmap. For each, write down what changes about the design when the user is an Embracer vs a Skeptic. If the answer is "nothing changes," your segmentation is decoration. If the answer is three different defaults, three different copy variants, or three different onboarding flows, your segmentation is load-bearing. Most teams' segmentation is decoration.

## THE THREE DIMENSIONS OF ATTITUDE

Three stacked dimensions. Use them together — none alone is sufficient.

### Dimension 1 — Adoption Attitude (5 tiers)

How fast does this user adopt new tools, regardless of what the tool is?

- **Pioneer:** Seeks new tools actively. Tolerates rough edges. Tries the alpha.
- **Early adopter:** Picks up tools with a clear value prop. Wants less friction than a Pioneer.
- **Pragmatist:** Adopts when peers adopt. Needs social proof and clear ROI. The largest segment.
- **Conservative:** Adopts last. Needs extensive proof and low switching cost.
- **Skeptic:** Resists. Adopts only under external pressure or after seeing peers shift.

Source: Geoffrey Moore's chasm framework, updated for AI products by Hilary Gridley. The classic Moore curve assumed adoption was a function of risk tolerance. For AI specifically, that's only half the story — you also need the AI-specific axis below.

### Dimension 2 — AI-Specific Attitude (3 tiers)

How does this user feel about AI itself, separate from how they feel about new tools in general?

- **AI Embracer:** Excited by AI. Builds habits quickly. Tolerates setup friction. Forgiving of imperfect output. Will spend time training the system.
- **AI Neutral:** Pragmatic. Will use AI if it saves measurable time. Skeptical of hype but not hostile. Demands quick wins before investing.
- **AI Skeptic:** Trusts proven processes. Fears losing craft, voice, judgment, or job. Needs to see strong evidence before committing. NOT the same as Conservative on Dimension 1 — a Skeptic can be a Pioneer in every other domain.

This dimension comes from Hilary Gridley's framework (Lenny's Newsletter, 2024). The key insight: AI attitude is its own axis. Mixing it with adoption attitude (Dimension 1) collapses the signal.

### Dimension 3 — Craft Orientation (3 tiers)

Relevant for knowledge work tools and any product where the user has identity tied to their output.

- **Craft-protective:** Sees the product as a tool they control. Quality of output is identity-load-bearing. They will reject AI output that doesn't sound like them, even when it's technically better.
- **Output-focused:** Wants to ship. Good enough is fine. Speed over polish. Willing to send AI output as-is.
- **Collaborative:** Uses the tool to think alongside. Wants an interlocutor, not a generator. Values the conversation as much as the output.

Why this matters: Craft-protective users are often miscategorized as Skeptics, but they're not the same. A Craft-protective Embracer will use AI heavily — they just want it to disappear into their voice. A Craft-protective Skeptic won't use it at all. Different fix.

## THE EMBRACER / NEUTRAL / SKEPTIC TABLE

This table is the operating manual. It's load-bearing — every shipping decision in the next section flows from it.

| Lens | AI Embracer | AI Neutral | AI Skeptic |
|---|---|---|---|
| **Behavioral signals** | Explores advanced features in week 1. Light touch on instructions. High refusal-override rate. Tries beta flags. Raw feedback ("more autonomy please"). | Uses 2-3 specific features repeatedly. Doesn't explore. Asks support questions about specific tasks, not the product. Activity tied to specific workflow triggers. | Low feature adoption. High support contact about output quality. Explicit feedback about feeling replaced or distrusted. Verifies every output. May log in, never trigger AI features. |
| **Survey signals** | Self-rates AI familiarity 4-5/5. Has used Copilot/ChatGPT/Claude personally. Believes AI will "change my work." | Self-rates 2-3/5. Has tried AI but uses sparingly. Believes AI is "useful for some things." | Self-rates 1-2/5. Limited or no personal AI use. Believes AI is "overhyped" or "concerning." |
| **Onboarding strategy** | Skip the basics. Show the full surface area. Drop them into power-user mode by day 2. Tutorials feel insulting. | Show 1-2 concrete time-saved moments before any feature tour. "You did X in 4 minutes that used to take 20." Then offer the second feature. | Frame the AI as a draft assistant, not a decision maker. Show transparency-first views (sources, confidence, "here's why"). Never auto-execute on day 1. |
| **Messaging strategy** | Speed, capability, customization, unlocked potential. ("What if you could ship in half the time?") | Reliability, efficiency, ROI. ("Save 6 hours per week on routine tasks.") | Augmentation not replacement. Quality over speed. Familiar frameworks. Control. ("Your judgment, accelerated.") |
| **Feature exposure (what to show first)** | Multi-step automations, agent flows, tool integration, batch processing, advanced configuration. | A single anchor feature with measurable time savings. The most common workflow, automated. Nothing else. | Drafting tools where the user always has the final word. Source-cited outputs. Override paths that are visible, not buried. |
| **Trust-building tactics** | Embracers don't need trust building — they need challenge. Give them harder tasks. Surface the model's limits so they can route around them. | Show ROI math monthly. Surface time saved. Quiet but consistent reinforcement of value. | Long-form transparency. Show the data, the sources, the confidence interval, the override log. Personal examples from peers in their role. Slow ramp on autonomy — start at L1 and earn L2. |
| **Default autonomy level** | L3-L4 (act with notification, act independently). Embracers want the AI doing things, not asking. | L2-L3 (recommend, then act on confirm). Show the work, then execute. | L1-L2 (suggest, draft, never auto-execute). Skeptics need to feel the steering wheel. |
| **Feedback prompts** | "What should this do better?" — open-ended, generative. Embracers will write paragraphs. | Thumbs up/down with one-line reason field. Light-weight, transactional. | Explicit "the AI got this right" / "the AI got this wrong" buttons with reason taxonomy. Skeptics need a place to register the failure. The signal is gold — failure logs from Skeptics catch issues before they hit your other segments. |
| **What NOT to do** | Don't slow them with tutorials. Don't ask permission for obvious actions. Don't hide power features behind tier gates if they're motivated to use them. | Don't oversell. Don't add features they didn't ask for. Don't change the core flow they've memorized. | Don't auto-execute. Don't bury the override. Don't position the AI as smarter than them. Don't use language like "AI does this for you" — use "AI drafts this for you." |

The table is the contract. When you ship a feature, you ship three versions of the experience around it — not always three different UIs, but three different defaults, three different messages, three different onboarding paths.

A second layer of the table that most teams miss: **what each segment notices first.** When a new user lands on your homepage, what do their eyes go to?

| Element | Embracer notices | Neutral notices | Skeptic notices |
|---|---|---|---|
| Hero copy | The capability claim ("write 10x faster") | The outcome metric ("save 6 hours per week") | The hedge or the override path ("you stay in control") |
| Demo video | The fast cuts, the impressive output | The before/after comparison | Who narrates it, whether the narrator looks like them |
| Pricing page | The top tier and what's unlocked | The middle tier and the value | The free tier and the cancellation policy |
| Trust signals | Backed-by logos | ROI case studies | Named customer testimonials with full job titles, with override stories |

This is why one homepage rarely converts all three segments. The Embracer leaves thinking "this is exciting." The Skeptic leaves thinking "this isn't for me." The actual content is the same — they read it differently. The fix is segment-aware homepages (geo-IP-style routing if you can't survey, or post-survey routing if you can).

## SEGMENT-SPECIFIC SHIPPING DECISIONS

Six worked examples. In each, the right shipping decision differs by segment. A team that ships one default ships wrong for two of three.

**Decision 1 — Default autonomy level on a new agent feature**

- Embracer: L4 (autonomous, with audit log). Default is "act, log it, tell me weekly."
- Neutral: L3 (act on confirmation). Default is "show me what you'll do, then do it."
- Skeptic: L2 (recommend only). Default is "draft this, I'll execute."

Why this differs: A Skeptic who lands on L4 by default churns by week 2 — they feel the AI is acting without permission. An Embracer who lands on L2 churns by week 1 — they feel the AI is too slow. Same feature, three defaults, retention three times higher than a single-default ship.

**Decision 2 — Refusal threshold on uncertain inputs**

- Embracer: Bias toward attempting. They'll fix bad output faster than they'll wait for a refusal.
- Neutral: Match the average user's tolerance. Refuse when confidence is below 70%.
- Skeptic: Bias toward over-refusing. A Skeptic prefers "I don't know" to a wrong answer with confidence. The wrong answer destroys trust permanently; the refusal is annoying but recoverable.

Why this differs: Refusal is a trust signal, not a capability gap. Skeptics read over-refusal as "this AI is honest." Embracers read it as "this AI is broken."

**Decision 3 — Feedback prompt design**

- Embracer: Single open-text field. They'll write detailed feedback because they care about the product trajectory.
- Neutral: Thumbs + 3-tag taxonomy ("slow," "wrong," "unclear"). Low friction, light signal.
- Skeptic: Explicit binary correctness button — "got this right" vs "got this wrong" — with mandatory reason picker. The Skeptic's feedback is your highest-signal data because they're already verifying the output. Capture it.

**Decision 4 — Confidence display in the UI**

- Embracer: Hide it. They don't read it. It clutters the experience.
- Neutral: Show on hover. Optional surface, not in the main view.
- Skeptic: Show by default. Confidence score, sources, recency of training data, all visible. The transparency itself is the trust mechanism — most Skeptics won't read every confidence score, but they need to know it's there.

Cross-link: see `confidence-tuner` for per-segment confidence threshold tuning.

**Decision 5 — Onboarding path length**

- Embracer: 90 seconds. Show the power feature, let them go.
- Neutral: 4 minutes. Show one anchor feature with a measurable outcome, then exit.
- Skeptic: 12 minutes, broken into 3 sessions over the first week. Trust ramps with time, not with content density. Forcing all 12 minutes into day 1 is worse than spreading it.

**Decision 6 — Email cadence and tone in the first 30 days**

- Embracer: Weekly. "Here's what's new, here's a power tip." Capability-focused.
- Neutral: Twice a month. "Here's the time you saved, here's one feature you haven't tried." ROI-focused.
- Skeptic: Three emails total in 30 days, all from a named human (a PM, not a "team"). Each one acknowledges that AI is uncertain and shows a specific override or correction story. Empathy-focused.

**Decision 7 — Pricing trial length**

- Embracer: 7 days is enough. They'll know on day 2.
- Neutral: 14 days. Needs to see the workflow stick.
- Skeptic: 30 days minimum. Trust builds in week 4, not week 1. A 14-day trial for a Skeptic is a forced rejection.

The pattern across all seven: defaults that work for the median user fail at the tails. Attitudinal segmentation gives you the right tails.

### The Conversion Path

Segments aren't fixed. The product's job is to move users from Skeptic toward Embracer over time, without forcing it. The path:

- **Skeptic → Neutral.** The trigger is almost always a single output that exceeds the user's quality bar in a domain they care deeply about. Not a tour. Not a testimonial. One real moment where the AI got something right that the user expected it to get wrong. Design for that moment by week 3 — Skeptics who don't have it by week 4 typically churn.
- **Neutral → Embracer.** The trigger is the second or third use case. Neutrals adopt one workflow and stop. They become Embracers when they discover the product solves a problem they didn't initially hire it for. Surface adjacent use cases at week 6-8, not week 1.
- **Embracer → ??? .** Embracers don't convert further. They plateau as power users or churn to a more capable competitor. The retention play for Embracers is depth (advanced features, agent flows, customization), not conversion.

You don't need to push users along this path aggressively. You need to make sure the path exists and isn't blocked. The most common failure: shipping onboarding that lets Embracers fly but quietly buries the trust-building moments Skeptics need to make their first conversion.

## REAL-WORLD ENTERPRISE EXAMPLE — Fortune 100 / world-class AI-native startup scale

A predictive maintenance AI on a chemical plant floor. The model surfaces "high probability of bearing failure in pump P-102, recommend inspection within 14 days." Two operators use it. Same role title. Same job description. Wildly different outcomes.

**Sai, age 58, 40 years on the floor.** Watched three predictive systems fail before this one. Trusts his own ear — he can tell a bearing is going by the sound of the pump from 20 feet away. AI Skeptic. Craft-protective. He logs in once a day, checks if the AI agrees with what he already knows, and overrides it when it doesn't.

**Riya, age 25, two years on the floor.** Used Copilot in school. Built a side project with Claude over the summer. AI Embracer. Output-focused. She trusts the AI's confidence interval, schedules inspections off the recommendations, and is starting to skip her own walk-around because "the model would catch it."

A team that ships one UX to both loses both:

- **Sai churns or sabotages.** If the AI auto-creates work orders (L4 default), Sai feels the system is overriding his judgment. He stops trusting it. Worse, he stops sharing his ear-based catches with the system, which means the model never learns the floor sounds it can't hear from sensor data alone. The team's best knowledge source goes silent.
- **Riya over-trusts.** If the AI uses Skeptic-grade caution (L2 default with mandatory human review), Riya treats every recommendation as gospel because the UI told her to. She skips the walk-around. The model misses a failure mode that requires visual inspection. She gets blamed for the incident.

The right ship: **two configurations of the same product.**

- For Skeptic operators: AI is positioned as "second opinion." All recommendations show sensor data, model confidence, and historical override rate for similar predictions. L2 default — recommend, never auto-execute. Override path is one click. Override reasons feed back into the model. Sai feels respected. The system learns from his ear.
- For Embracer operators: AI is positioned as "first pass." Recommendations include automated work order drafts (still requiring sign-off). L3 default. Confidence display is collapsed by default. Walk-around reminders trigger weekly regardless of model state — because the embracer's blind spot is over-trust, and the product has to defend against it.

Same model. Same data. Different defaults. Both operators stay. Both contribute different value. The "single UX" team would call the Skeptic difficult and the Embracer the model user. The right team calls them both right and ships for both.

The wider a Fortune 100 enterprise pattern: every plant has both. The veteran operators with 30+ years and the recent grads who used AI in college. Most predictive systems fail because they ship one default — usually Embracer-leaning, because the PM team uses Copilot themselves. Skeptic operators (often the most knowledgeable on the floor) churn first. The team blames "change resistance." It's not change resistance. It's miscalibrated defaults.

The fix isn't a separate product. It's a "trust mode" toggle exposed during onboarding, with the segment-survey result selecting the default. Users can shift modes later. Most won't, and that's fine — the work is in getting the first 30 days right. After 30 days, both Sai and Riya are using the same product, contributing different signals, both retained, both producing value the other segment can't.

The same pattern shows up everywhere AI ships into mixed populations: clinical decision support (senior physicians vs residents), financial advisory tools (career advisors vs new hires), legal research AI (partners vs first-year associates), even consumer health apps (chronic-condition self-managers vs newly diagnosed users). The segment names are different. The shipping principle is identical.

## INSTRUMENTATION

You can't ship segment-specific defaults if you don't know which segment a user is in. Two paths to identify segment, used together.

**Path 1 — Behavioral signals from product analytics (no user input required):**

- **Feature exploration depth (week 1):** Embracers touch 5+ features. Neutrals touch 1-2. Skeptics touch 0-1 AI features (they may use non-AI parts of the product heavily).
- **Refusal acknowledgment rate:** When the AI refuses or expresses low confidence, do they retry, override, or abandon? Embracers retry or override. Skeptics often abandon — but in a healthy way (they go check the source).
- **Override frequency:** Skeptics override frequently and consistently. Neutrals override rarely. Embracers override aggressively but sporadically (they only override when wrong, not when uncertain).
- **Time-to-first-value:** Embracers hit first useful output in <10 minutes. Skeptics may take 2-4 weeks. Neutrals fall in between.
- **Support contact pattern:** Skeptics file tickets about output quality and trust. Neutrals file tickets about specific tasks. Embracers file feature requests, not bugs.
- **Verification behavior:** Does the user click through to sources? Do they re-prompt the same query in different ways? Skeptics verify. Embracers don't.

These signals get you 70% of segmentation accuracy without asking the user anything. Stand them up before you stand up the survey.

**Path 2 — Onboarding survey (5 questions, optional, 90 seconds):**

```
Welcome! Three quick questions help us tune your experience.

1. How often do you use AI tools (ChatGPT, Claude, Copilot, etc.) outside of work?
   ( ) Daily — I use them constantly
   ( ) Weekly — I use them for specific tasks
   ( ) Rarely — I've tried but don't use them often
   ( ) Never — I haven't used them

2. When you read about AI, what's your honest reaction?
   ( ) Excited — I want to try it
   ( ) Curious but cautious — I want to see what works
   ( ) Skeptical — I think a lot is overhyped
   ( ) Concerned — I worry about the impact

3. How much do you want this product to do for you automatically?
   ( ) Take action without asking — I'll review the log
   ( ) Show what it'll do, then do it on my OK
   ( ) Recommend, and I'll decide
   ( ) Suggest only — I'll execute everything myself

(Optional) 4. How long have you been doing this kind of work?
   ( ) Less than 2 years
   ( ) 2-10 years
   ( ) 10-25 years
   ( ) 25+ years

(Optional) 5. What worries you most about an AI helping with this?
   [open text]
```

Mapping to segments:
- Q1 "Daily" + Q2 "Excited" + Q3 "Take action" → **Embracer**
- Q1 "Weekly" + Q2 "Curious but cautious" + Q3 "Show, then do" → **Neutral**
- Q1 "Rarely" or "Never" + Q2 "Skeptical" or "Concerned" + Q3 "Recommend" or "Suggest only" → **Skeptic**

Mixed signals (e.g., Q1 "Daily" + Q3 "Suggest only") → flag as **Embracer with Craft-protective overlay** and use Skeptic-leaning autonomy defaults despite high familiarity. The mixed signal is information, not noise.

Question 4 is optional but valuable when the product crosses a generational gap (the a Fortune 100 enterprise case). Question 5 is the highest-signal question if you're starting fresh — the open text reveals the actual mental model.

**Combine both paths:** use behavioral signals to confirm or update the survey-based segment over the first 30 days. Users move between segments. A Skeptic who has a great month-1 experience may shift toward Neutral by month 3. Re-segment quarterly.

## CROSS-LINKS

- **`feedback-triage`** — the AI-failure axis (false positive vs false negative vs hallucination vs refusal-as-failure) hits each segment differently. Skeptics weight false confidence (a confidently wrong answer) far more heavily than Embracers do. Run feedback-triage segment-aware, not aggregated.
- **`ai-product-metrics`** — Skeptics generate more refusal events, more override events, more support contacts. Aggregated against your Embracer-heavy active user base, this looks like Skeptic users are "less successful." That's wrong. They're producing more signal. Segment your metrics dashboards or you'll kill the segment that's training your model.
- **`confidence-tuner`** — per-segment confidence threshold tuning. Skeptics want over-refusal (refuse below 80% confidence). Embracers want over-attempt (attempt above 50%). One global threshold averages both into a worse experience for both.
- **`uncertainty-research`** — when you run trust studies, segment the sample. A 30-person trust study with 25 Embracers and 5 Skeptics will tell you Embracer trust dynamics and miss Skeptic trust dynamics entirely. Stratify the recruit.
- **`jtbd-analysis`** — Embracers and Skeptics often have the same Job to Be Done but radically different anxieties about hiring your product to do it. Run JTBD segment-aware to surface the anxiety differential.

## DELIVERABLE FORMAT

Three artifacts. No more, no less.

**1. Segment Map**

For your specific user base, estimate the distribution:

```
Embracer:  [X]% (estimated from [signal source])
Neutral:   [Y]% (estimated from [signal source])
Skeptic:   [Z]% (estimated from [signal source])
Mixed:     [W]% (e.g., Embracer × Craft-protective)

Confidence: [low / medium / high based on data quality]
Re-validate: [trigger condition — e.g., "after 90 days of survey data" or
              "if churn pattern shifts"]
```

**2. Per-Segment Shipping Decisions**

For the next 3-5 features in your roadmap, fill out the decision grid:

```
Feature: [name]
- Embracer default: [config]
- Neutral default: [config]
- Skeptic default: [config]
- Why these differ: [one sentence]
- Failure mode if you ship a single default: [one sentence]
```

**3. Instrumentation Plan**

```
Behavioral signals (deploy in week 1):
  [ ] Feature exploration depth tracking
  [ ] Refusal acknowledgment rate
  [ ] Override frequency
  [ ] Support contact tone classifier (manual, then automated)
  [ ] Verification behavior (source-click rate)

Survey (deploy in week 2-3):
  [ ] 3-5 question segment survey at onboarding
  [ ] Quarterly re-survey to catch segment drift

Reporting:
  [ ] Segment dashboard with churn, retention, NPS by segment
  [ ] Alert on segment drift >10% quarter-over-quarter
```

## RED TEAM

When attitudinal segmentation is the wrong tool:

- **Very small user bases (<20 active users).** Statistical segmentation isn't meaningful. Use individual user research instead — name them, talk to them, build for the specific people you have.
- **Commodity products where attitude doesn't predict behavior.** A search box doesn't need attitudinal segmentation. The attitude lens fires when the product asks the user to extend trust — to delegate, to act on AI output, to change a workflow. If your product is just AI under the hood with no user-visible AI surface, skip this skill.
- **Products where users have no choice (mandated enterprise tools).** Attitude doesn't predict adoption — adoption is forced. But it does predict compliance vs sabotage. A Skeptic operator who's mandated to use the system will use it as little as possible, won't share knowledge with it, won't report failures, and may quietly route around it. That's still segmentation worth doing — just with different downstream actions (compliance support, not adoption support).
- **Pre-launch.** You can't segment users you don't have. Hold this skill for after first 100 users.
- **When the segment differential is small.** If your behavioral signals show three segments with 95% similar product behavior, you don't have three segments. You have one with weak attitudinal noise. Don't overfit.
- **When over-segmenting creates more variants than you can ship.** Three default configs is operationally feasible. Nine configs (3 attitude × 3 craft) usually isn't. Pick the dimension that drives the most behavioral variance and ship for that one.

## REALITY CHECK

- **Segment drift is real.** Users move between segments. A Skeptic who has a great month-1 experience may become a Neutral by month 3. Re-segment quarterly or you'll be shipping defaults for who they were, not who they are.
- **Embracers are not your superusers by default.** Skeptics, once converted, are often your stickiest users — they did the work of building trust, and they don't transfer that easily to a competitor. Don't ignore them on day 1 because they're "low engagement."
- **Onboarding designed for Embracers (the team's own profile) is the most common shipping mistake in AI products.** PM and engineering teams tend to be Embracers. They build for themselves. Then they wonder why the field hates the product.
- **The survey is biased.** Self-reported AI familiarity correlates with stated openness to AI. People who feel anxious about AI may answer "Curious but cautious" rather than "Concerned" because the question reads as a stance test. Validate survey-based segments against behavioral signals after 30 days.
- **The product team itself is not a representative sample.** If you have 20 PMs and engineers using the dogfood build, you have 20 Embracers giving you Embracer feedback. Recruit Skeptics into your dogfood pool deliberately. The signal you get from your first Skeptic dogfooder will be 5x more useful than your 20th Embracer dogfooder.
- **Sales and customer success teams sit on top of attitudinal data without realizing it.** Account notes ("this user is hesitant," "this team wants to see proof first," "this champion loves AI") are segment signals in disguise. Pipe these into the segment dashboard before you build the survey infrastructure — they're free and already labeled.

### Anti-Pattern Catalogue

Three failure patterns that show up repeatedly when teams try to add attitudinal segmentation late:

1. **The Persona Trap.** Team builds three personas ("Pioneer Pat," "Pragmatic Priya," "Skeptical Sam"), prints posters, and never changes a default. Personas without per-segment shipping calls are decoration. Skip the names; ship the defaults.
2. **The Survey-Only Trap.** Team runs the onboarding survey, segments users on day 1, never updates the segment afterward. Users move. The segment label decays. By month 3 the data is misleading. Behavioral signals must reconcile against survey data continuously.
3. **The Single-Variant Trap.** Team agrees attitudinal segmentation matters, then ships one default with the rationale "we'll get to per-segment configs later." "Later" never arrives. If you can only ship one default, ship it for the underserved segment (usually Skeptics) and accept Embracers will adapt — Embracers tolerate suboptimal defaults far better than Skeptics tolerate aggressive ones.

## QUALITY GATE

- [ ] Segment distribution estimated for the actual user base (not a generic AI product population)
- [ ] At least 3 product decisions in the next quarter mapped to per-segment shipping calls
- [ ] Behavioral instrumentation specified (which events, where logged, who owns the dashboard)
- [ ] Survey designed and approved (not just intent — actual question wording)
- [ ] Segment-aware metrics dashboards planned (churn, retention, NPS by segment, not aggregate)
- [ ] Re-validation cadence set (quarterly minimum, faster if churn pattern shifts)
- [ ] Failure mode named for ignoring this skill (which segment churns first if you ship a single default?)
- [ ] Cross-links to `feedback-triage`, `ai-product-metrics`, and `confidence-tuner` followed up

## WHEN WRONG

- Pre-launch products with no user data
- Products with <20 active users
- Mandated tools where exit isn't an option (use compliance lens instead)
- Commodity products where AI is invisible to the user
- When the team can only ship one default config — pick the underserved segment and serve them well, rather than averaging

---

## TRADE-OFF LEDGER

Complete the Trade-Off Ledger from the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 5.

## CONCLUSION

Follow the Conclusion Protocol from the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 6:
1. The recommendation — segment distribution + the 3 shipping decisions that will move first
2. The hypothesis — "We believe Skeptics make up [X]% of our users and churning at [Y]× the rate of Embracers because we ship Embracer-default onboarding. We'd know we're wrong if Skeptic-tuned onboarding doesn't move Skeptic month-2 retention by at least 30%."
3. The key trade-off — three defaults adds complexity vs single default loses the tails
4. The biggest risk — segments drift faster than you re-validate; mitigation is quarterly re-segmentation
5. The next action — instrument behavioral signals first, ship survey second, retune defaults after 60 days of data

---

## GENERATE THE DELIVERABLE

Use the output prompt from the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 11.

Generate the markdown handoff file when the next downstream skill is `confidence-tuner`, `feedback-triage`, or `adoption-launch`.

---

## VISUAL SUMMARY

After completing the primary output, invoke the **excalidraw-svg** skill to create a single Excalidraw SVG visual summary. The diagram should show:
- The three segments as three columns (Embracer, Neutral, Skeptic) with their default autonomy level, onboarding length, and feedback prompt style
- The mixed-signal cell (Embracer × Craft-protective) called out as a distinct overlay
- One arrow showing the conversion path (Skeptic → Neutral → Embracer over time, with the trigger event for each conversion)

Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.
