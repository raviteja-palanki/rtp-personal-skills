---
name: rtp-adoption-launch
version: v1.1_latest
description: >
  Treat AI adoption as a product launch — with personas, phases, and phase-specific support — not as a training program.
  Adoption curves are predictable: Surge → Dip → Rebound, and the shape repeats across unrelated companies and tool
  types (Novo Nordisk, Microsoft). One-time training doesn't prevent the dip; the dip is a product and
  organizational-design problem, not a training problem. Use when planning AI rollout, adoption is stalling, or
  designing change management. Pairs with: needs-guard (which psychological need the rollout threatens),
  attitudinal-segmentation (embracers vs. skeptics), agent-risk (when someone has a rational reason to want it to
  fail), purpose-dialogue (connecting the rollout to what people believe in), judgment-guard (the multi-year
  capability-debt question — apprenticeship pipelines thinning as AI absorbs junior tasks — distinct from this
  skill's single-rollout competency trap, below).
imports: [first-principles, needs-guard]
---

# Adoption Launch

Adoption curves for enterprise software are predictable. Yours will follow the same pattern. The question is not whether your team will hit the Month 3 dip — they will. The question is whether you've planned for it.

> "Adoption is not 'once and done.' It's a product launch with phases, personas, and repeated value realization." — Everett Rogers, adapted for AI

---

## Quick Reference: The Adoption Curve You're About to Experience

```
Week 1-4 (Surge):      Fast initial uptake — most of the target population tries it at least once
Month 2:               Novelty fades; usage starts to soften
Month 3-4 (The Dip):   The collapse — a meaningful share of early adopters go quiet
Month 5+ (Rebound):    Stabilizes higher than the dip — only if you've intervened
```

**The shape repeats across unrelated companies and tool types.** Two independently-run, named studies show the same curve, at very different scale:

- ◆ **Novo Nordisk** — a 20,000-employee Copilot rollout, 3,000+ employees surveyed (Wade, Trantopoulos, Navas, Romare, *MIT Sloan Management Review*, 8 Jul 2025, "How to Scale GenAI in the Workplace"). Month 1: 23% frequent users + 74% moderate users. Months 3-4: 15% of early adopters go inactive; average time saved per person drops from 2.29 to 2.14 hours/week as the easy wins exhaust. Past the dip, gains compound — and satisfaction correlates 3x more strongly with *perceived work-quality improvement* than with time saved.
- ⚠ **Microsoft** — its own Customer & Partner Solutions sales org, ~62,000 people (HBS Case 626065/68357, discussed by co-authors Iavor Bojinov and Shunyuan Zhang on HBR's *Cold Call* podcast, 12 May 2026). Daily active Copilot usage collapsed from 22% to 5% within about a month of launch — inside the company that built the tool, selling it to their own sales force. **[VERIFY]** — the exact figures come directly from the case researchers describing their own primary data on-air; the underlying HBS case document is paywalled and not independently re-audited here. Usage eventually reached 80-90% daily active after a redesigned approach, roughly two years in.

**What causes the dip?** Not user error. Not skill gaps. The dip happens because:
1. **Novelty wears off** — the excitement of new technology fades.
2. **No canonical use case** — prior enterprise tools (SAP-style) came bundled with an implied task list; the tool's affordances matched the job. General-purpose AI has no such match: "it can do lots of things, but no one tells you what you should do with it" (Bojinov, HBS). That absence — not resistance — is what surfaces to you as "edge cases."
3. **Workarounds compete** — workers find faster manual processes or unauthorized tools.
4. **Support fatigue** — help desk traffic spikes at Weeks 3-4; response times increase; workers abandon the tool.

Organizations that survive the dip are not smarter about training. They proactively redesign support for each phase — and they watch a different segment than the one they'd expect (see THE TRAP and Phase 2, below).

---

## DEPTH DECISION

**Go deep if:** You're designing an adoption strategy for AI rollout, adoption is stalling at Month 2-3, or you need to redesign current rollout plan to prevent the dip.

**Skim to diagnostic questions if:** You need to quickly assess your current adoption phase and what support is needed.

**Skip if:** You haven't yet designed which AI tool to deploy (use `ai-use-case-readiness` first) or you don't have a cohort of users to validate adoption patterns with.

---

## DELIVERABLE FORMAT

Before starting, ask:

> **What format would you like this adoption plan in?**
> 1. **Word Document** — Formatted report with embedded visuals, timelines, and support playbooks. Best for sharing with leadership.
> 2. **Presentation** — Slide deck with phases, personas, and key decisions. Best for meetings and stakeholder alignment.
> 3. **Both** — Full report + summary deck.
>
> *Default if no preference: Word Document.*

Follow the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md).

---

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md):
1. Ask the Grounding Questions — at minimum: Who are the users? What AI system? What's the deployment scope?
2. Route depth: Executive Summary or Comprehensive Analysis?
3. Identify output format: Document, presentation, or inline?

**Additional grounding for this skill:**

> **1. What's your current adoption state?** Pre-launch, Surge phase, in the Dip, or planning from scratch?
>
> **2. Who are the users?** Segment by role, seniority, and AI comfort level. "Knowledge workers" is too broad. Distinguish: executives, individual contributors, team leads, and — separately — the manager layer between them (see GATE ZERO, point 2).
>
> **3. What's the current user support model?** One-time training, ongoing help desk, peer champions, documentation? List what you have.
>
> **4. What's your adoption success metric?** Is it "% of users with access," "% using weekly," "% using daily," or "measured improvement in user outcomes"? (The answer should be the third or fourth, not the first two — see THE TRAP, second panel, on why the first two can actively mislead you.)

---

## KEY TERMS (plain language)

- **The adoption curve (Surge → Dip → Rebound)** — the predictable path: fast initial uptake, a Month 3-4 dip, then recovery from Month 5 if you intervene.
- **Gate Zero** — the pre-check on whether the rollout was *co-created* with users or merely *announced* to them; an announced rollout starts fragile.
- **Perception gap** — the distance between how enthusiastic leaders *think* people are and how they actually are (76% vs. 31%).
- **Adoption personas** — Enthusiast / Pragmatist / Skeptic / Resister; archetypes by stance toward the tool, not by job title.
- **Activation theater** — usage metrics (logins, seat activation) that look healthy while the underlying work hasn't actually changed; the dashboard equivalent of showing up to a meeting without contributing.
- **The competency trap** — your most expert, most tenured users can have the *deepest* dip, not the shallowest, because their old shortcuts don't transfer to a general-purpose tool.
- **Role elevation vs. role burial** — whether an org layer's job moved *up* (new higher-value scope) under AI, or just got *heavier* (new oversight duties stacked on unchanged work, unrewarded). Juniors and executives usually get elevated; middle managers usually get buried, by default, not by design.
- **Psychological safety** — feeling safe enough to experiment with a new tool without fear of blame or job loss.
- **Adversarial-user risk** — when someone has a rational incentive to make the rollout fail (a real headcount threat); route to `rtp-agent-risk`, not to more training.

## THE TRAP

The mistake you're about to make: **Treating adoption as a training problem when it's a product problem.**

Here's how it plays out. You roll out AI. You provide comprehensive training: documentation, videos, workshops. Month 1: adoption surges (they're trained). Month 3: adoption collapses (training didn't stick). You conclude: "We need more training" or "Users didn't absorb the material."

So you add more training. More videos. More workshops. Adoption still doesn't improve.

The actual problem: **Your AI tool doesn't solve the user's real problem in a way that's faster, easier, or better than their current process.** Or it solves the problem but creates new friction (takes too long, is hard to trust, requires constant context-switching). Compounding this: general-purpose AI has no canonical use case the way prior enterprise tools did (see Quick Reference, above) — so the friction users hit often isn't a bug, it's the absence of a built-in task list nobody designed around.

Training can't fix a product problem. The user isn't resisting because they don't understand the AI. They're abandoning it because it doesn't fit their workflow.

**The bias that drives this mistake:** **Fundamental attribution error.** Attributing low adoption to user incompetence ("they need more training") instead of product misfit ("the tool doesn't solve their problem efficiently").

**When this over-warns:** not every dip is curve-normal. Sometimes it really is a broken product or the wrong use case — and "it's just the curve, wait it out" becomes an excuse not to look at real failure data. Before you conclude "this is the predictable dip," cross-check against `eval-framework` or `ai-product-taste`: is the AI actually reliable and useful, or does it just look that way in the demo?

**The fix:** Treat adoption like a product launch, not a training rollout. Identify your adoption personas (not just job titles — adoption personas). For each persona, design phase-specific value propositions and support. Month 1 support is different from Month 3 support. Most teams skip this and wonder why adoption collapses.

### A second, easy-to-miss trap: activation theater

There's a subtler version of the same mistake, and it hides behind a dashboard that looks fine. McKinsey's most recent global AI survey found 88% of organizations report regular AI use in at least one business function (✅ up from 78% a year earlier) — but only 39% report *any* enterprise-level EBIT impact from that use, and most of that 39% report less than 5% of EBIT attributable to AI (✅ [McKinsey, "The State of AI in 2025," 5 Nov 2025](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai)). Usage is real. Value, at the enterprise level, mostly isn't yet. That gap is exactly what a Surge-phase login dashboard hides.

**The bias that drives this mistake: Goodhart's Law** — when a measure becomes the target, it stops being a good measure. If your adoption metric is "% with access" or "% who logged in this week," people (and teams reporting up) will optimize for the number, not the underlying work. This isn't necessarily dishonest: a worker who opens the tool once to avoid looking like a holdout, without changing how they actually do the work, satisfies the metric without producing the value the metric was supposed to proxy for.

**When this over-warns:** don't apply this suspicion before you have any usage data at all — you can't accuse a metric of being gamed with zero data yet. And don't apply it reflexively to simple, low-complexity tools where "opened it and got the answer" legitimately *is* the whole job (a lookup or search assistant, for instance). Reserve this lens for complex, workflow-embedded tools where usage and value plausibly diverge — which is most enterprise AI rollouts, but not all of them.

**The fix:** measure outcome-linked adoption (Phase 3, below), not access. And when you see high login numbers with no quality or outcome movement, don't declare victory — go find out what's actually happening in those sessions.

---

## GATE ZERO — WAS THIS CO-CREATED OR ANNOUNCED? (run before you design the phases)

The three phases below tell you *what* the adoption curve does. This gate tells you whether your Surge numbers can be trusted at all. Ask two questions before finalizing any rollout plan:

1. **Was the AI strategy co-created with the people who will use it, or announced to them?** If announced, treat the Surge-phase adoption numbers as unreliable no matter how strong they look — leaders systematically believe adoption is happening before employees have even started. In one 2026 survey, **76% of executives believed employees were enthusiastic about AI; only 31% actually were** (◆). A second, independent 2026 study puts a number on the same gap from the other direction: IBM's Institute for Business Value surveyed 2,000 CEOs and equivalent senior leaders across 33 geographies and 21 industries (Feb-Apr 2026) and found **85% of employees have AI access, but only 25% use it regularly — a 61-point gap** (◆ [IBM, "Only 25% of workers are using AI. Here's how tech leaders are changing that," ibm.com/think, 2026](https://www.ibm.com/think/news/workers-using-ai-2026-ceo-study)). Two different methodologies, two different populations, the same story: what leaders believe about usage and what's actually happening are two different numbers, and the gap is large enough that it's now CEOs' top AI concern, ahead of cost or accuracy.
2. **Does the frontline-manager layer have safety/empathy support, or only the senior leaders?** People experience a rollout through their immediate manager, not the C-suite. If only senior leaders are bought in, the layer that actually decides whether someone feels safe to experiment is missing — and that layer has its own, distinct failure mode. A June 2026 HBR analysis of AI rollouts inside two large firms (18 interviews; ⚠ small-N, treat directionally) names it "role elevation vs. role burial": AI adoption typically moves work *up* for juniors (they take on strategy work once reserved for seniors) and *up* for executives (who expand scope and ambition), but for managers stuck between them, the new duties — validating AI output, coaching teams through it, translating vague "make this AI-enhanced" mandates from above — get **added on top of unchanged delivery pressure, with no formal change to their role, their metrics, or their incentives.** Managers don't get elevated. They get buried. If your rollout plan has support for end users and executives but nothing that changes what's asked of managers or how they're measured, you've built Gate Zero's failure mode directly into the plan (Shin & Sucher, HBR, 26 Jun 2026, "AI Adoption Is Overloading Your Middle Managers").

**A distinct risk to screen for, separate from adoption friction:** ask "does anyone on this team have a rational incentive to want this rollout to fail?" If a rollout genuinely threatens headcount, that fear is *accurate*, not a perception gap — and co-creation is not a fix for an honest conflict of interest. Route that to `rtp-agent-risk` (adversarial-user risk), not to more training.

**Why it matters:** adoption is gated by whether people feel *safe enough to experiment*, and experimenting with a tool that might replace you is a risk nobody takes when they don't feel safe ("why would anyone be enthusiastic about training their replacement?"). An announced rollout skips the step that builds that safety, so it enters the Surge phase already fragile — the Month-3 dip below isn't only novelty wearing off, it's fear that was present from day one. This is the causal variable the dip-causes list doesn't yet name. **When this is wrong:** where use is genuinely non-negotiable and universal (a tool everyone must use to do the core job), the safety dynamic is weaker and the curve is driven more by workflow fit than by fear; and where the fear is *accurate* (the AI really is eliminating the role), empathy and co-creation are the wrong lever — the honest move is a straight answer about the conflict, not a co-creation workshop.

*(Sources: "Empathetic Leadership Can Make or Break AI Adoption," Zaki, HBR, 30 Apr 2026. The 76%-vs-31% gap is ◆ [BCG 2026](https://www.bcg.com/publications/2026/ai-at-work-why-strategy-matters-more-than-tools); the "~60% plan to lay off non-adopters" companion finding is ⚠ reported. The 85%/25%/61-point IBM figure is ◆ company-disclosed (IBM Institute for Business Value 2026 Global CEO Study, 2,000 CEOs, 33 geographies, 21 industries). "AI Adoption Is Overloading Your Middle Managers," Shin & Sucher, HBR, 26 Jun 2026 — the role-elevation/burial framework and its three breakdowns are ⚠ reported (18 semi-structured interviews at two unnamed consulting firms; treat the mechanism as directional, not a measured population rate). **Decay clock:** re-verify the IBM and BCG figures before citing past mid-2027 — adoption-gap numbers move fast as tooling and organizational practice mature.)*

## THE ADOPTION CURVE: Three Phases, Three Different User Needs

### Phase 1: Surge (Week 1 - Week 4)

**What's happening:** Novelty. Users try the tool because it's new and leadership said to. Productivity hasn't improved yet — they're running both the manual process AND the AI tool in parallel. (Novo Nordisk's own numbers for this phase: 23% frequent users, 74% moderate users — see Quick Reference.)

**User mindset:** "This might be useful. I'll experiment."

**Who you deliberately launch to first:** don't default to "everyone at once" or even "your broadest ideal customer profile." Choose an **Early Customer Profile** — the narrow slice with the highest pain and highest tolerance for rough edges, not necessarily your eventual mainstream user — and aim for a genuine **beachhead**: 60-70% real penetration of that narrow slice within 3-18 months, before expanding. A wide, unfocused Week 1 rollout produces a wide, unfocused Month 3 dip with no concentrated pocket of proof to rebound from; a narrow, well-chosen Surge cohort gives you real reference users by the time you need them for Phase 3.

**Support needed:**
- Quick wins — show the easiest use cases first (not the hardest)
- Slack channel for peer support (not just help desk)
- Weekly "tip of the week" showing one new feature
- **Champions program, chosen deliberately** — not just "the most enthusiastic person per team." Microsoft's own internal Copilot rollout (HBS Case 626065) found that the single highest-leverage move was pairing its *most skeptical, most tenured, highest-credibility veteran* with its *most experimental, most tech-savvy junior employee* — not exposing the org to an early adopter's success from a distance. The mechanism is credibility transfer, not exposure: a demo convinces no one because it's disconnected from a skeptic's actual workflow and risk tolerance, but watching a 20-year veteran the team already trusts visibly switch over is unfakeable proof. Recruit your Champions for who they can convert, not just for who converts easiest.

**Common failure:** Too much training, too much complexity. Overwhelm kills adoption. Teach one workflow. Master that first.

### Phase 2: The Dip (Month 2 - Month 4)

**What's happening:** Reality. Users hit edge cases. The AI tool works for 80% of their use cases. The remaining 20% breaks their workflow. They revert to manual processes or unauthorized tools. (Novo Nordisk's own numbers: 15% of early adopters go inactive; time saved per person drops from 2.29 to 2.14 hours/week. Microsoft's, at much larger scale and with no canonical use case to anchor a general-purpose tool: daily active usage collapsed from 22% to 5% within about a month — see Quick Reference.)

**User mindset:** "This doesn't work for my situation. I'm going back to what I know."

**Why training doesn't help:** The user understands the tool. The problem is the tool doesn't fit their workflow. Training can't fix that.

**The segment you're least likely to be watching is often the one at greatest risk: your most tenured, most expert people.** Call this the **competency trap.** The people who've mastered the *old* system have every shortcut memorized — and that mastery doesn't transfer to a general-purpose AI tool, and can actively interfere with it. Your most experienced performers can have the deepest, most invisible dip of anyone, precisely because they have the most to unlearn and the least patience for unstructured experimentation (Bojinov & Zhang, HBS Cold Call, 12 May 2026). The fix isn't to assume your best people will adapt fastest — it's the opposite: route extra experimentation slack and explicit permission to be temporarily slower toward your most tenured high performers, not your newest hires, because that's the segment with the deepest, least visible risk.

**A second segment to check, distinct from any individual user: your managers, as a layer.** Before you declare the Dip "handled" based on end-user metrics, run the role-elevation check from Gate Zero on the manager layer specifically: has their role gained new, higher-value scope (elevation), or has it just absorbed new AI-validation and coaching duties on top of an unchanged workload, unrewarded and unmeasured (burial)? If it's burial, that predicts a manager-specific version of the dip your general adoption numbers won't show you, because managers who are quietly drowning don't show up as "low adoption" — they show up as slower everything else. Two concrete fixes from the research: reward coaching and knowledge-sharing explicitly in performance criteria, not just delivery and utilization; and put senior leaders in working sessions with managers (not just managers reporting up), so leadership's expectations get calibrated against what's actually happening operationally.

**Support needed:**
- **Edge case triage** — Help desk tickets shift from "how do I use this" to "the AI doesn't work when X." Listen to these tickets. They reveal design gaps.
- **Rapid feature iterations** — Some edge cases are real gaps. Fix the top 3 by Month 4. Users won't have patience for "we'll fix it in Q3."
- **Workflow redesign** — Some edge cases require users to change their process slightly. Redesign the workflow, not the training.
- **Peer mentoring, weighted toward the competency-trap segment** — The Champions program becomes critical. Peer advice works better than help desk advice at this phase, and your most tenured users need it most, even though they'll be the least likely to ask for it.
- **Usage monitoring and intervention** — Identify users who've gone quiet (haven't used the tool in 2 weeks). Reach out with: "How can we help?" not "You should be using this." Watch for activation theater here too (THE TRAP, second panel): a user logging in without any change to their actual output isn't the same as a user who's gone quiet, and both need a different intervention than a simple usage nudge.

**The critical mistake:** Assuming the dip is temporary and waiting it out. The dip is not temporary. Without intervention, adoption will crater and stay there. You have roughly 4 weeks to intervene — Weeks 6-10 post-launch.

### Phase 3: Rebound (Month 5+)

**What's happening:** Habit formation or abandonment. Users who made it through the dip are now using the tool as a regular part of their workflow. Users who dropped out have moved on.

**User mindset:** "This is part of how I work now" OR "I tried this; it's not for me."

**Support needed:**
- **Continuous improvement loops** — Weekly feedback: "Here's what you're using, here's where similar users struggle, here's a shortcut you might like."
- **Advanced features for power users** — The users who love the tool will want more sophisticated features. Build for them. They drive adoption within their teams.
- **Outcomes measurement, and lead with quality, not hours saved** — Shift from "% of users using" to "what improved because of this." Novo Nordisk's own data found employee satisfaction correlated three times more strongly with *perceived work-quality improvement* than with time saved, and that people who saved time reinvested it into strategic and relationship work, not leisure. "This saved you 2 hours a week" is a weaker message than "this catches errors before your manager sees them." Report both, but lead with quality.

---

## ADOPTION PERSONAS: Not Job Titles, Adoption Archetypes

Your org chart has: Support Manager, Senior Support, Associate Support. Your adoption personas are different. Here are the archetypes:

### 1. The Enthusiast (5-10% of any population)
**Profile:** Early adopter. Loves new tools. Will experiment and find uses you didn't anticipate.

**What they need:**
- Early access (let them in Week 1)
- Autonomy to experiment
- Recognition (showcase their success)

**Risk:** Enthusiasts are not representative. Their success doesn't predict broader adoption. If adoption metrics are based only on enthusiast feedback, you'll miss problems the other 90% are experiencing.

**How to use them:** Turn them into Champions — but see Phase 1 above: the highest-leverage Champion pairing pairs an Enthusiast-type experimenter with a converted *Skeptic*, not two Enthusiasts. Also listen to Enthusiast feedback about what's *not* working, not just what is.

### 2. The Pragmatist (30-40% of any population)
**Profile:** Will use the tool if it clearly saves time or improves outcomes. Resistant to change, but not hostile to it.

**What they need:**
- Clear ROI — "This saves you X hours per week" (show the data)
- Low friction — if adoption requires changing their workflow, they'll resist
- Integration — the tool should fit into their existing workflow, not replace it

**Risk:** Pragmatists abandon fast if the tool doesn't deliver on the ROI promise. If you tell them "This saves 30 minutes per week" but it actually takes 15 minutes extra setup time before saving time, they'll churn by Week 4.

**How to use them:** They represent the mainstream market. If they're adopting, you're on track. If they're not, you have a product problem.

### 3. The Skeptic (30-40% of any population)
**Profile:** Needs proof. Will wait and see if others succeed. Not hostile — just unconvinced.

**What they need:**
- Social proof — "I see Sarah from my team using this successfully"
- Time — let them watch others succeed for a month before asking them to try
- Low pressure — forcing adoption pushes them into the next category

**Risk:** Trying to convert skeptics too fast creates resistance. Wait until Month 3. By then, you'll have real data from pragmatists about what works and what doesn't.

**How to use them:** Don't target most Skeptics in Surge phase — with one deliberate exception: your single highest-credibility, most tenured Skeptic is exactly who you want inside your Phase 1 Champion pairing (see above), because converting that person first is worth more than converting ten easier ones later. For the rest of this persona, wait for Rebound phase: skeptics will convert if adoption among peers is real.

### 4. The Resister (10-20% of any population)
**Profile:** Won't use the tool unless forced. Often for good reasons: the tool doesn't fit their workflow, or it threatens something they value professionally.

**What they need:**
- Use `needs-guard` skill to diagnose why they're resisting
- If resistance is about violated psychological needs, redesign won't be solved by adoption strategy
- If resistance is about AI quality or reliability, fix the product first

**Risk:** Treating all resistance as "lack of training" and doubling down on communications. This creates resentment, not adoption.

**How to use them:** Don't try to convert them in Surge or Dip phases. In Rebound phase, after you've fixed the tool based on Pragmatist feedback, revisit them with a honest conversation: "We've fixed X and Y. Does this now work for your use case?"

---

## THE PROCESS: Design Phase-Specific Adoption Support

### Step 1: Map your adoption personas to your population

```
Enthusiasts:        5-10%
Pragmatists:       30-40%
Skeptics:          30-40%
Resisters:         10-20%
```

Adjust these percentages based on your org. Some teams skew more pragmatic. Some have more enthusiasts. The key: you'll have all four types.

### Step 2: For each Phase, design support specifically for the active personas

**Surge Phase support (focus: a deliberately-chosen Early Customer Profile cohort — see Phase 1)**

- **Champions Program:** Pair one converted Skeptic (highest tenure, highest credibility, highest AI skepticism — not highest enthusiasm) with one Enthusiast-type experimenter per team. Give them early access, training, and recognition.
- **Quick Win Workflows:** Pick the 1-2 easiest use cases. Master those first. Don't try to cover all uses.
- **Weekly Tips:** Every Friday, share one new feature or shortcut. Keep it focused.
- **Slack Channel:** Real-time peer support. Champions will answer questions better than help desk.
- **Success Celebration:** Share wins weekly. "This week, Sarah saved 2 hours using the AI for X." Make it real — but pair the time-saved number with a quality/outcome number (Phase 3 lesson, pulled forward).

**Dip Phase support (focus: at-risk Pragmatists, the competency-trap segment, and the manager layer)**

- **Edge Case Triage:** Categorize help desk tickets by problem type. The top 3 problems reveal design gaps.
- **Rapid Iteration:** Fix the top 3 design gaps within 4 weeks. Announce the fixes. Show you're listening.
- **Workflow Redesign:** Some use cases require the user to change their process. Work with users to design the new workflow together.
- **Peer Mentoring, weighted toward tenure:** Shift from "help desk solves problems" to "power user in your team helps you" — and proactively check in with your most tenured, most expert users, since the competency trap means they're at higher risk than they look.
- **Manager-layer check:** Run the role-elevation-vs-burial diagnostic (Gate Zero) on managers specifically. If they're absorbing new AI-validation and coaching duties with no change to how they're measured, fix the incentive and support structure now, not after they burn out.
- **Check-ins with Silent Users:** If someone used the tool in Week 2 but not Week 6, reach out. "How can we help?" not "You should use this." Distinguish this from activation theater (THE TRAP): a user who logs in weekly but hasn't changed their output needs a different conversation than a user who's gone fully quiet.
- **Reframe the Narrative:** Don't say "adoption is low." Say "we're learning what works and what needs improvement." This is true and less discouraging.

**Rebound Phase support (focus: all personas, differentiated)**

- **For Enthusiasts:** Advanced features. Let them explore deeper.
- **For Pragmatists:** Outcomes measurement. Show them the impact: time saved, quality improved, stress reduced — lead with quality.
- **For Skeptics:** Case studies from peers. "Here's how Marcus in Accounting uses this now."
- **For Resisters:** Honest conversation. "What would need to be true for you to use this?" Listen. Don't argue.
- **Continuous feedback loops:** Weekly usage metrics + quarterly deep interviews. What's working? What's not? What's changed?

### Step 3: Build the adoption support team

You'll need:
- **1 adoption lead** (owns the whole program)
- **Team champions** (skeptic-experimenter pairs, focused on peer support and credibility transfer)
- **Help desk triage** (routes questions, not just answers them)
- **Product liaison** (feeds help desk insights back to product team for rapid iteration)

The Champions program is not optional. It's not nice-to-have. It's the difference between adoption that rebounds and adoption that craters.

---

## DIAGNOSTIC QUESTIONS WITH ANSWER NUDGES

**Use these to assess where you are and what to do next:**

1. **What phase are you in?** (Week 2, Month 2, Month 4, Month 5+)
   - Red flag: "We don't know"
   - Green flag: "We're tracking weekly adoption metrics"

2. **What's your adoption metric?** (% with access, % using weekly, % seeing improved outcomes)
   - Red flag: "% of people with access" — that's not adoption, that's deployment, and it's exactly the metric Goodhart's Law eats first
   - Yellow: "% using weekly"
   - Green: "% using regularly + measured improvement in outcomes"

3. **Do you have a Champions program?** (a converted Skeptic paired with an experimenter, per team)
   - Red flag: "No, we have help desk documentation"
   - Yellow: "Yes, but they're our most enthusiastic people, not our most credible skeptics"
   - Green: "Yes, built on skeptic-experimenter pairs, recognized and supported, and adoption metrics improve when they engage"

4. **What are help desk tickets about?** (Skills, edge cases, integration issues)
   - Red flag: "How do I use this" (Surge phase questions in Month 3)
   - Yellow: "Edge cases, design gaps, integration friction"
   - Green: "Design gaps are being triaged and fixed weekly"

5. **Are you ready for the Month 3 dip?** (Planned support, resource allocation)
   - Red flag: "We haven't thought about it"
   - Yellow: "We have a plan but no resources allocated"
   - Green: "Adoption lead is focused full-time on preventing churn. Champions are actively engaged. The manager layer has its own support plan, not just end users."

---

## REALITY CHECK

**Failure modes:**

- **Assuming adoption is binary (adopted/not adopted).** Adoption is a spectrum. A user who uses the tool once per week is not the same as a user who uses it 10x per day. Measure the depth, not just the breadth.

- **Measuring adoption before Month 3.** If you're celebrating high adoption in Week 2, you're celebrating novelty, not adoption. Wait until Month 4-5 to assess whether adoption is real or temporary.

- **Mistaking activation for adoption.** McKinsey's own 2025 survey found 88% of organizations report regular AI use in at least one function, but only 39% report any enterprise EBIT impact, and most of that 39% is under 5%. A green usage dashboard is not evidence that the work has actually changed — go check.

- **Assuming your most tenured people are your safest segment.** They're often your riskiest, per the competency trap: mastery of the old system doesn't transfer, and can interfere.

- **Not listening to resisters.** 10-20% of users will resist. Before you assume they're "change-averse," use `needs-guard` to diagnose why. Sometimes they're right — the tool violates their needs or doesn't fit their use case.

- **Treating adoption as "someone else's problem."** If adoption is owned by HR/Change Management/Help Desk but not by the product team, adoption will fail. Product team needs to hear from users daily about what's working and what's not.

- **Designing support for end users and executives, but not for managers.** The manager layer has its own distinct failure mode (role burial) that end-user adoption metrics won't surface.

- **One-time communication blitz.** If your "adoption campaign" is three emails in Week 1, adoption will not be sustained. You need weekly engagement for 3+ months.

---

## QUALITY GATE

- [ ] Adoption curve phases are explicitly planned with timeline and resource allocation
- [ ] Adoption personas defined for your specific population (not generic)
- [ ] Phase-specific support playbooks created for each phase and persona
- [ ] Champions program designed around skeptic-experimenter pairs, with incentives and recognition
- [ ] Help desk triage process set up to feed insights back to product
- [ ] Adoption metrics are outcome-based, not just access-based — and you've checked whether your current metric is vulnerable to Goodhart's Law
- [ ] The competency-trap segment (your most tenured, most expert users) has a specific support plan, not just general Dip-phase support
- [ ] The manager layer has been checked for role elevation vs. role burial, separate from end-user adoption metrics
- [ ] Resource allocation and ownership clear for each phase

---

## WHEN WRONG

This skill gives bad advice if:

- **The underlying AI tool doesn't actually work.** If the AI has quality/reliability problems, no adoption strategy will fix it. Use `eval-framework` to validate performance before investing in adoption.

- **The user's real problem has nothing to do with adoption support.** Sometimes resistance is because the tool is too slow, requires too much context, or gives inconsistent answers. No amount of Champions or peer support fixes that. Fix the product.

- **The organization has no plan to sustain adoption support beyond 6 months.** If adoption lead role disappears after Month 3, adoption will revert. Champions will burn out. Make sure the organization has committed to long-term support before designing a phase-based plan.

- **There's no stable, tenured workforce with a legible internal credibility hierarchy.** The skeptic-experimenter Champion pairing assumes you have an identifiable, respected "20-year veteran" figure to recruit. In high-turnover, distributed, or gig workforces, or flat orgs without that figure, this specific tactic won't transfer — fall back to broader peer-network champions instead.

---

## TRADE-OFF LEDGER

### Choosing to treat adoption as a product launch with phase-specific support:

**We are betting on:** That active, phase-specific support — including deliberate Champion selection and a manager-layer check, not just end-user support — will prevent adoption collapse at Month 3 and produce a durable rebound by Month 5.

**We are giving up:** Speed and simplicity. A "just roll it out and train people" approach is faster. A phase-based adoption program requires ongoing coordination, resource allocation, and continuous adaptation for 5+ months.

**This is reversible within:** Not really. Once you launch, adoption curve is playing out. But you can course-correct. If Month 3 dip is worse than expected, you can intensify support in Month 4.

**The hidden trade-off:** **Adoption support consumes resources.** The Champions program, the adoption lead, the weekly communications, the help desk triage — this costs people and time. You're trading engineering velocity (product team is responsive to adoption feedback) for adoption sustainability. If your product is mature and feature parity is your goal, this trade-off makes sense. If you're early-stage and innovation velocity is paramount, this trade-off is harder.

**Confidence: High on the curve shape; Medium on the specific tactics.**
- Evidence: Everett Rogers' adoption research; the Novo Nordisk (◆, MIT Sloan, Jul 2025) and Microsoft (⚠, HBS Case 626065, May 2026) rollouts independently reproduce the same Surge-Dip-Rebound shape at very different scale and tool type; the IBM 2026 CEO Study (◆) and McKinsey 2025 survey (✅) independently confirm the access-vs-use gap; the competency-trap and role-elevation mechanisms are each currently grounded in a single well-documented case or small-N interview study, not yet replicated across multiple independent sources.
- What would change our mind: A team that gets sustained, outcome-linked adoption with zero structured adoption support beyond one-time training; or a second and third independent case showing the competency trap or role-elevation mechanism *doesn't* hold, which would demote those two from "apply by default" to "watch for it."

---

## CONCLUSION

**The recommendation:** Adopt adoption as a product launch. Design for three phases with distinct user support needs, including a distinct check on your manager layer. Build a Champions program around converted skeptics, not just enthusiasts. Treat the Month 3 dip as inevitable and plan for it, with specific attention to your most tenured users. Measure adoption by sustained, outcome-linked use, not deployment access.

**The hypothesis:** We believe that organizations that treat adoption as a structured product launch with phase-specific personas, a deliberately-selected Champion pairing, and a manager-layer check will achieve durable adoption by Month 5, while organizations that provide one-time training and measure only access will see adoption crater and stay there. We'd know we're wrong if a team achieves durable adoption with no structured support beyond initial training, or if the competency-trap and role-elevation mechanisms fail to replicate in a second independent setting.

**The biggest risk:** You execute the adoption plan perfectly, but the underlying AI tool has quality issues. No adoption strategy survives product failure. Before investing in adoption, ensure the tool is reliable and actually solves the user's problem better than their current approach.

**Assumptions to watch:**
- Adoption personas accurately represent your population (they won't be perfect; refine based on Month 2 data)
- Champions program will sustain itself with peer energy (it won't; you need formal recognition and support)
- Month 3 dip is universal (it is for most organizations; exception: if every user has a non-negotiable need to use the tool)
- The competency trap and role-elevation mechanisms hold in your context (currently grounded in one well-documented case each; watch for whether they replicate, and treat them as directional until they do)

**The next action:**
1. Define your adoption personas for your population, and choose a deliberate Early Customer Profile for Surge, not "everyone at once"
2. Design support playbooks for Surge, Dip, and Rebound phases — including a specific plan for your competency-trap segment and your manager layer
3. Identify and empower your Champions program, built on skeptic-experimenter pairs
4. Set up help desk triage to feed insights to product team
5. Allocate resources and assign ownership for each phase

---

## GENERATE THE DELIVERABLE

Use the output prompt from the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md).

If adoption plans reveal need violations (e.g., "workers can't override AI decisions"), generate a markdown handoff to the `needs-guard` skill for deployment redesign.

---

## VISUAL SUMMARY

After completing this analysis, invoke the `excalidraw-svg` skill to create:
1. **Adoption Curve by Persona** — 4 lines showing Enthusiast, Pragmatist, Skeptic, Resister adoption trajectories
2. **Phase-Support Matrix** — Phases (rows) vs Personas (columns) showing what support is needed when
3. **Critical Intervention Points** — Timeline showing when to deploy Champions, edge case triage, the manager-layer check, and outcomes measurement
