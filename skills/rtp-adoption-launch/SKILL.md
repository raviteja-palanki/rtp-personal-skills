---
name: adoption-launch
version: v1.8_latest
description: 'Treat AI adoption as a product launch, with personas, phases and phase-specific support, rather than as a training program. Adoption curves are predictable: Surge → Dip → Rebound, and the shape repeats across unrelated companies and tool types (Novo Nordisk, Microsoft). One-time training doesn''t prevent the dip; the dip is a product and organizational-design problem, not a training problem. Use when planning AI rollout, adoption is stalling, or designing change management. Pairs with: needs-guard (which psychological need the rollout threatens), attitudinal-segmentation (embracers vs. skeptics), agent-risk (when someone has a rational reason to want it to fail), purpose-dialogue (connecting the rollout to what people believe in), judgment-guard (the multi-year capability-debt question: apprenticeship pipelines thinning as AI absorbs junior tasks, which is distinct from this skill''s single-rollout competency trap, below).'
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
- **Surplus disposition** — who keeps the time or money the tool saves, stated before the rollout. Unstated, the people producing the saving assume the organization is coming for it.
- **Participation budget** — the experimentation work written into named people's job descriptions and reviews. Without it you are running on volunteered effort, which has a shelf life.
- **The withdrawal signal** — a program dying because people stop showing up rather than because anyone objects. It passes every review on the way down, so participation rate is the only early number.
- **The authorship deadline** — input has to be solicited before the plan is fully formed. Consultation after the announcement can do useful things; building ownership is not one of them.
- **Currency translation** — stating the benefit in the metric the adopter already cares about (safety, not efficiency) rather than the one the buyer cares about. The claim has to be true, or it is a slogan they can test.
- **Psychological safety** — feeling safe enough to experiment with a new tool without fear of blame or job loss.
- **Adversarial-user risk** — when someone has a rational incentive to make the rollout fail (a real headcount threat); route to `rtp-agent-risk`, not to more training.
- **The abstention list** — the places you name up front where AI cannot be used *even with disclosure*, because disclosure itself is what destroys the value there. Different from a disclosure policy, which assumes disclosure is always the safe default.
- **Status repair** — whether a rollout raises or erases the standing of the function whose expertise it's meant to scale. A self-service tool can quietly delete the role that used to generate demand for that function's work.
- **Contestability** — the ability of an individual adopter who personally absorbs the error to push back on the AI's output. Strongest, and most necessary, precisely where one person bears the cost of being wrong.
- **The whether-channel** — the part of an observed act that signals *permission* ("this is safe to attempt here") rather than *process knowledge*. It needs no observer competence and can move a whole organization from one act, but only when the observer sees the demonstrator absorb a real, personally costly consequence.
- **Accountability vs. ownership decay** — accountability (who answers for the outcome) sits on the org chart long after ownership (who actually feels responsible day to day) has quietly drifted back to the old habit.
- **Forking** — whether a team has locally modified a rolled-out program to fit its own context. A cheap, observable signal of whether the program will survive its sponsor leaving.
- **Noncontroversial pilot** — a first AI pilot chosen because a failure would cost little visibility, not because it carries the highest information value. Optimizes for organizational permission and trust, not for what you'd learn from it.
- **The false-alignment test and the take-up plan** — a pair of pre-launch gates. The first checks whether the launch team's verbal agreement is real: each leader writes down independently what the change is before any group discussion, and divergent answers mean the room performed consensus rather than reached it. The second checks whether the plan is actually executable: name who has to change what behavior, and whether that's credible given their workload and incentives.

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

**A sequencing version of the same trap, one step earlier: mandating usage before you've found your power users.** A common three-part playbook says: set a usage OKR to force adoption, watch the resulting usage data to find your power users, then build around them. The order is the bug. Once usage is a measured target, Goodhart's Law is already live: the telemetry now records compliance, not behavior, and a genuine power user becomes indistinguishable from someone gaming the metric to hit the OKR. **The fix:** find and study your power users from usage data collected *before* any usage target exists, then set the OKR. Reversing the order corrupts the exact signal you need. **When this is wrong:** if you have no pre-mandate usage data at all (a brand-new tool, no prior soft rollout), there's nothing to sequence, and a usage OKR from day one is the only option; just don't trust what it tells you about who your power users are. *(Source: MIT Sloan "Strategy Summit 2026: Who's Going to Succeed with AI?", podcast interview with Andrew McAfee, Jul 2026 — ⚠. Flag: McAfee runs Workhelix, a consultancy whose client data is the piece's only proprietary evidence for the broader playbook; the sequencing contradiction is a logical one, independent of that conflict, but the surrounding numbers are his firm's own and uncorroborated.)*

---

## GATE ZERO — WAS THIS CO-CREATED OR ANNOUNCED? (run before you design the phases)

The three phases below tell you *what* the adoption curve does. This gate tells you whether your Surge numbers can be trusted at all. Ask six questions before finalizing any rollout plan. The first two ask whether people were brought in. Questions three and four ask whether anyone worked out what the rollout costs the people doing it, and both are routinely skipped. The fifth asks whether the people actually using the tool can push back on it when it's wrong. The sixth checks whether the room's agreement was ever real, and whether the plan names who has to act on it:

1. **Was the AI strategy co-created with the people who will use it, or announced to them?**

   If announced, treat the Surge-phase adoption numbers as unreliable however strong they look. Leaders systematically believe adoption is happening before employees have even started.

   Two independent 2026 studies, two methodologies, two populations, one story:
   - **76% of executives believed employees were enthusiastic about AI. Only 31% actually were** (◆).
   - IBM's Institute for Business Value surveyed 2,000 CEOs and equivalent senior leaders across 33 geographies and 21 industries (Feb-Apr 2026): **85% of employees have AI access, but only 25% use it regularly. A 61-point gap.** (◆ [IBM, "Only 25% of workers are using AI. Here's how tech leaders are changing that," ibm.com/think, 2026](https://www.ibm.com/think/news/workers-using-ai-2026-ceo-study))

   What leaders believe about usage and what is actually happening are two different numbers, and the gap is now CEOs' top AI concern, ahead of cost or accuracy.
2. **Does the frontline-manager layer have safety and empathy support, or only the senior leaders?**

   People experience a rollout through their immediate manager, not the C-suite. If only senior leaders are bought in, the layer that decides whether someone feels safe to experiment is missing. That layer also has its own distinct failure mode.

   **Role elevation against role burial.** AI adoption typically moves work *up* for juniors, who take on strategy work once reserved for seniors, and *up* for executives, who expand scope and ambition. Managers sit between them and get new duties instead: validating AI output, coaching teams through it, and translating vague "make this AI-enhanced" mandates from above. Those duties land **on top of unchanged delivery pressure, with no formal change to their role, their metrics, or their incentives.**

   Managers don't get elevated. They get buried.

   **The tell:** if your rollout plan supports end users and executives but changes nothing about what is asked of managers or how they are measured, you have built Gate Zero's failure mode into the plan. *(Shin & Sucher, HBR, 26 Jun 2026, "AI Adoption Is Overloading Your Middle Managers" — ⚠ 18 interviews at two large firms, small-N, treat directionally.)*

**The same mechanism shows up one layer over, in functions rather than people: call it status repair.** An MIT Sloan Management Review study looked at retrieval-augmented generation (RAG) rollouts across eight consumer-goods companies. What separated the successes (Novartis, PepsiCo) from a failing one wasn't how well the benefit was explained. It was whether the rollout raised or erased the standing of the insights function whose expertise it was meant to scale. Self-service search deleted the "librarian" role that used to generate demand by showing requesters the archive went deeper than their question assumed. Once that role was gone, self-service didn't increase demand for the underlying research corpus, the researchers' budget got cut, and the tool that was supposed to make the function more valuable made it look less necessary instead. **The move:** before rollout, ask whether the tool raises or erases the standing of the function it is built on top of, and design a role for that function inside the new workflow, not only around it. **When this is wrong:** the study covers eight companies with no stated sampling frame, so treat this as a real pattern worth checking for, not a base rate; and it doesn't apply where there's no expert function to protect in the first place, only a manual task being automated.
3. **Who keeps the time or money this saves, and has anyone said so out loud?**

   A saving with no stated owner is read by the people producing it as a saving the organization is about to claim. They are often right to read it that way.

   **The case.** Mass General Brigham gave clinicians an ambient AI scribe: free to the clinician, voluntary throughout, aimed squarely at burnout, with a per-seat license the organization paid for. Among primary care clinicians, the group with the most to gain, a significant number took the license and never used it. They said why, directly: **"You are now giving me back time. What are you going to ask me to do with that time?"**

   The precedent that made the question rational sat in the same organization's memory. A physician given a *human* scribe "had to produce more, so see more patients, in order to pay for the human scribe to be assigned to them."

   **The move:** state the surplus disposition before the rollout, in writing. Then check whether this population has previously watched a saving in that same currency get repossessed. If they have, say what is different this time, or expect the license to sit unused.
4. **Whose job description and performance review contains this work?**

   If the answer is nobody's, you are running on volunteered effort, and it has a shelf life.

   **The case.** Two organizations started gen AI innovation in the same season with the same supported sandboxes and the same access to setting-specific data, matched on the things prior research says drive engagement: problem fit, operational readiness, compliance posture.
   - One put the experimentation work into job descriptions and performance reviews. It ended with **141 organization-wide solutions in use.**
   - The other treated it as a stretch assignment that motivated people would absorb in their spare time. It ended with **three**, after **more than 80% of its domain experts gradually dropped out.**

   The sentence that explains it: *"My annual review is still based on the same criteria as before gen AI existed. All that work is invisible at review time."*

   **The move:** name the domain experts, put the experimentation work in their objectives before the rollout starts, and track participation rate as a metric beside usage.
5. **Can the person using this push back when it's wrong, and does that depend on a skill they still have?**

   **The case.** An early AI sepsis-flagging tool shipped with no explanation for its alerts, and clinicians ignored it. Adding an explanation for each flag fixed uptake. Clinicians who got the explanation went on to independently catch roughly **10% of the cases the model missed on its own.**

   **The correction this forces: explanation is an uptake feature, not a safety feature.** It works only where the reviewer still has, and keeps exercising, independent judgment about the underlying case.
   - **Where that competence is intact**, an explanation turns justified doubt into justified action. The clinician can check the model's reasoning against their own and catch what it missed.
   - **Where that competence has eroded**, the identical explanation turns doubt into *unjustified* action, because a fluent explanation reads as confirmation whether or not it is correct. This gets worse, not better, as explanations get more polished.

   **The move:** treat contestability, meaning the reviewer's standing ability to independently catch an error, as a resource that has to be actively maintained rather than assumed to survive the rollout. It matters most exactly where one person, not the organization, absorbs the cost of a miss.

   **When this is wrong:** where no individual bears the error cost personally, in a low-stakes and easily reversible use, spending effort to preserve independent competence is wasted. The tool can be trusted, or checked in bulk after the fact.
6. **Did the launch team actually agree, and does the plan name who has to act on it?**

   **The optimism gap, again.** BCG survey data across roughly 6,000 people in a dozen countries (✅ audited) found the same gap this skill documents for AI in question 1: roughly **70% of executives feel positive about a change they haven't detailed yet, against roughly 45% of employees.** The cause is information asymmetry, not resistance. Employees are reacting rationally to less information, not digging in.

   **Why co-authorship works.** The source connects this to the IKEA effect (people pay **63% more** for furniture they assembled themselves, ✅ peer-reviewed) to make a mechanism claim: people do not sabotage what they personally helped build. That is a stronger claim than "involving people is good practice."

   That mechanism produces two gates. Both run *before* you design the Surge/Dip/Rebound phases below, not during them.

   - **The false-alignment test.** Before any group discussion, every leader on the launch team writes down, independently, what the change is and how it will work. If the written answers do not converge, the agreement you heard in the room was performed consensus. Launching on performed consensus is a known failure mode.
   - **The take-up plan.** Name specifically who has to change what behavior for this to land, then state plainly whether that is credible given their current incentives and workload. Treat "no" or "unclear" as a blocking gate, not a risk you note and proceed past.

   **When this is wrong:** the false-alignment test breaks under low psychological safety, because people write down the answer they think is sanctioned rather than what they believe. The test needs its own safety precondition to be trustworthy (see `needs-guard`). The source also does not say how co-authorship holds up at a 50,000-person rollout against a small team, so treat it as strongest at the leadership-team scale where it was demonstrated.

   *(Source: an HBR piece on transformation leadership, 2026. The BCG optimism-gap figures are ✅ audited survey data. The IKEA effect is ✅ peer-reviewed [Norton, Mochon & Ariely, "The IKEA Effect," Journal of Consumer Psychology, 2012]. The co-authorship-at-scale claim is the piece's own extrapolation, not something either underlying study measured directly.)*

**Two ways these gates fail quietly, and both defeat your status report.**

**The failure mode is withdrawal, not objection.** At the site that lost its experts, nobody sent a memo, nothing was escalated, and no gate was failed. In the researchers' words: *"They did not refuse or resist AI. They did not lobby against it. Instead, they simply withdrew."* The initiative ran out of participants. **A program dying this way passes every review on the way down**, because every instrument you have reads objections and none of them reads absence. Participation rate is the one number that moves early, which is why question 4 asks you to instrument it.

**Consultation after the decision cannot build ownership, and calling it co-creation makes it worse.** The distinction that matters: consensus shows up in the room, appetite shows up months later when priorities collide and people decide what to protect. Appetite is built by authorship, and **authorship has a deadline**: soliciting input and genuinely listening *before the plan is fully formed*, rather than after it has been announced. So a rollout plan written after the decision was made can still do useful things, and building ownership is not one of them. Stop the Surge phase from promising it. A related correction on the capacity side: bandwidth is created by **removing work**, not by adding people. Of the four standard moves for creating capacity (postpone a competing initiative, clarify who owns decisions, shift resources to what matters most, protect uninterrupted thinking time), three take work away. If your readiness plan adds headcount and postpones nothing, it has not created capacity.

**The first lever that makes all six gates easier: state the benefit in the adopter's currency, not the buyer's.**

Rio Tinto's leaders talked to employees about mining automation as **safety**: *"a mine where no miner will ever get hurt again."* Not efficiency.

Here is why that works. For a miner, the live metric is not cost per tonne. It is whether you go home. Efficiency is management's currency, and it is exactly the currency in which automation reads as a threat, because efficiency in a labor-intensive operation means fewer people. Same technology, same rollout. The framing is the difference between resistance and participation. **The precondition, and it is what separates this from spin:** the translated claim has to be true and checkable. A safety framing on a deployment that does not improve safety is a slogan the workforce can test within a quarter, and failing that test costs more than the efficiency framing would have.

**A scoping note on when this lever applies:** growth or threat-removal framing is not a universal substitute for currency translation. It is a gating precondition ahead of it, and it only works where the adopter is plausibly replaceable by the tool. Warner Bros. Discovery ran its first AI pilots deliberately on **noncontroversial** work, chosen because "if we screwed it up, nobody would care" rather than for the highest information value, on the reasoning that an early pilot's real deliverable is organizational permission and trust, not what you learn from it. That is the opposite of standard risk-reducing pilot advice, which optimizes for learning. Currency-translated safety framing (Rio Tinto) works once the threat is credible and the adopter is the one who could be replaced; if nobody's job is plausibly at stake, growth framing has nothing to neutralize, and the more useful first move is a noncontroversial pilot that buys trust before you ever need to translate a benefit. **When this is wrong:** don't pick a pilot so trivial it produces no learning at all. The choice is a trade-off between trust and information, not a reason to abandon information value entirely.

**A second lever, distinct from currency translation: build an abstention list, not a disclosure policy.** A museum ran a public AI-avatar marketing campaign loudly, and banned AI outright, with no exceptions, from donor emails. The variable that separates the two isn't domain risk (marketing versus donor relations). It's whether the AI's output *is* the value (no prior non-AI version existed, so the audience judges the output on its own terms) or whether it's evidence a person spent attention on the recipient (a prior version existed, and a hand-written donor email was valuable specifically as proof someone spent twenty minutes thinking about them). Disclosure destroys that kind of value outright; it does not make it safer. **The move:** before rollout, name the specific places where AI cannot be used *even with disclosure*, because disclosure is exactly what breaks them. Don't rely on a general disclosure policy to cover this case. **When this is wrong (the falsifier):** a deployment that clearly replaced a well-liked, human-produced artifact and was still received well on its own terms. If that shows up, the substitution test above is missing a variable. *(Source: HBR, "How a Museum Marketing Team Used AI to Bring People Closer to Art," Jul 2026 - weak evidence, no outcome numbers attached — ⚠. Carry the mechanism, not the case as proof it works.)*

*(Sources for questions 3 and 4 and the block above. MGB scribe: HBR Cold Call, Gallani, Aug 2026 — ⚠ interview format, and note what is missing: the abandonment rate is never quantified, burnout "dropped significantly" with no figure, instrument or comparison group, and the license fee amount is never stated. The human-scribe precedent is one physician's recollection relayed twice, the weakest provenance in the episode and the most load-bearing fact in it; cite the mechanism, not the case. Participation budget: HBR, "AI Experiments Need Domain Experts," Aug 2026 — ◆ two-year qualitative field study, two pseudonymized US sites. **The 141-to-3 comparison is n=2 across two different industries, so industry alone could produce a good part of a 47-to-1 ratio, and the 80% figure has no stated denominator.** Carry the mechanism and the review-criteria quote; do not carry the ratio as an effect size. Appetite deadline and capacity moves: HBR, Morris, "Before Rolling Out a New Strategy, Assess Your Team's Readiness," 12 Aug 2026 — ⚠ weakest evidence rung, a consultant selling the remedy, three of five illustrations unnamed composite clients. The underlying distinctions borrow Deci and Ryan on motivation and hold up independently. Rio Tinto: MIT SMR, Westerman, Aug 2026 — ◆ reported example, no adoption figures attached. Status repair (RAG/librarian role): MIT Sloan Management Review, Jul 2026, eight consumer-goods companies — ⚠ no stated sampling frame; carry the mechanism, not a base rate. Contestability (sepsis-flagging tool): an HBR interview, 2026 — ⚠. The interview's flagship 41%-mortality-reduction claim does not survive checking against the hospital's own public disclosures and is not carried here in any form; only the ~10%-of-missed-cases finding and the explanation-conditional mechanism are cited. Warner Bros. Discovery noncontroversial-pilot sequencing: MIT Sloan Management Review case interview, 2026 — ◆ company-disclosed account, no adoption or outcome figures attached. Ledger pattern D.)*

**A distinct risk to screen for, separate from adoption friction:** ask "does anyone on this team have a rational incentive to want this rollout to fail?" If a rollout genuinely threatens headcount, that fear is *accurate*, not a perception gap — and co-creation is not a fix for an honest conflict of interest. Route that to `rtp-agent-risk` (adversarial-user risk), not to more training.

**Why it matters:** adoption is gated by whether people feel *safe enough to experiment*, and experimenting with a tool that might replace you is a risk nobody takes when they don't feel safe ("why would anyone be enthusiastic about training their replacement?"). An announced rollout skips the step that builds that safety, so it enters the Surge phase already fragile — the Month-3 dip below isn't only novelty wearing off, it's fear that was present from day one. This is the causal variable the dip-causes list doesn't yet name. **When this is wrong:** where use is genuinely non-negotiable and universal (a tool everyone must use to do the core job), the safety dynamic is weaker and the curve is driven more by workflow fit than by fear; and where the fear is *accurate* (the AI really is eliminating the role), empathy and co-creation are the wrong lever — the honest move is a straight answer about the conflict, not a co-creation workshop.

*(Sources: "Empathetic Leadership Can Make or Break AI Adoption," Zaki, HBR, 30 Apr 2026. The 76%-vs-31% gap is ◆ [BCG 2026](https://www.bcg.com/publications/2026/ai-at-work-why-strategy-matters-more-than-tools); the "~60% plan to lay off non-adopters" companion finding is ⚠ reported. The 85%/25%/61-point IBM figure is ◆ company-disclosed (IBM Institute for Business Value 2026 Global CEO Study, 2,000 CEOs, 33 geographies, 21 industries). "AI Adoption Is Overloading Your Middle Managers," Shin & Sucher, HBR, 26 Jun 2026 — the role-elevation/burial framework and its three breakdowns are ⚠ reported (18 semi-structured interviews at two unnamed consulting firms; treat the mechanism as directional, not a measured population rate). **Decay clock:** re-verify the IBM and BCG figures before citing past mid-2027 — adoption-gap numbers move fast as tooling and organizational practice mature.)*

## THREE LEVERS SHAPE THE DIP, AND THEY ARE INDEPENDENT

The Surge-Dip-Rebound curve below describes *what* happens. **These three decide how deep the dip goes and how fast you climb out**, and confusing them is why rollouts get the wrong intervention.

| Lever | What it controls | If you get it wrong |
|---|---|---|
| **Product** | **the ceiling.** How much better can anyone get with this tool, at the limit | you optimize training against a tool that cannot deliver |
| **Process** | **the speed of recovery.** Training and playbooks that determine how fast someone climbs back to par | the dip lasts longer than the patience budget |
| **People** | **whether the curve happens at all.** Effort is unevenly distributed | you read a flat line as success |

**The People lever is the one that gets misread.** Low-effort adopters produce **a flat line: no dip and no gain.** High-effort adopters produce **a deep dip followed by a real payoff.** So a rollout dashboard showing no dip is not evidence of a smooth launch. **It is often evidence that nobody is really trying**, and the gain will not arrive either.

**The competency trap this predicts.** Your most expert incumbents have every shortcut in the old system memorized. **On a new general-purpose tool they can come out worse off during the transition**, because expertise in the old system does not transfer and can actively interfere. Expect your best people to have the deepest dip, and do not read that as resistance.

## BUILD WITH THE WORKERS, NOT FOR THEM

**Three practices from manufacturing that transfer to any deployment where the people affected hold tacit knowledge.**

**Map tasks and judgment calls separately, with worker input.** Break the role into component tasks, then **separately identify the judgment calls the person makes while performing it.** The second list is the one that never appears in a process document, and it is where the workarounds, shortcuts and "common sense" live. Surfacing it gives you a forward view of how the role shifts toward delegation, oversight, orchestration and exception handling.

**Train in the flow of work, not in concepts.** Training content should match the tool-mediated tasks the person is doing that day. Pair it with real-time analytics so a supervisor sees where work stalls, errors rise, or confidence drops. **The two-way version is the point: the worker gets better at the tool, and the worker's questions push the tool to support more advanced work.**

**Measure capability, not exposure.** Courses completed and training hours logged measure exposure. These measure capability:

- Speed and accuracy of human-AI handoffs
- Time to resolve exceptions
- Frequency and quality of successful interventions when the system flags an issue

*(Sources: the three J-curve levers, Iavor Bojinov in HBR, "Microsoft's Path to Adopting and Scaling AI Across its Sales Organization," May 2026, building on Brynjolfsson's productivity J-curve — ◆ single company, and the levers are the author's decomposition rather than a measured model. The build-with-workers practices, a consulting-authored HBR piece on manufacturing, May 2026 — ⚠ practitioner-tier with no outcome data. Both carry the mechanism, not a claimed effect.)*

## STRATEGY MOVES FAST, CULTURE MOVES SLOWLY, TALENT DECISIONS ARE THE BRIDGE

**A strategy can change in a quarter. The culture it lands on cannot.** So the work of pushing a technology shift through an established company is the work of pushing it through every talent decision until it compounds. **Announcements do not move culture. Hiring, promotion, and pay do.**

**The rollout sequence, in order, from a 150-year-old company moving from an engineering-led culture to one where customer use and pain points set direction:**

1. **Communicate aggressively and consistently, starting with the rationale.** Not the plan. **The reason, stated so employees find it believable.** A rationale people do not believe makes every subsequent step read as theater.
2. **Lay out the objectives on that rationale, and how progress will be evaluated.** What are we trying to achieve, and how will we know.
3. **Build incentives consistent with it.** Pay is one and not the only one. Anything that signals who gets ahead here.

**Note the ceiling the practitioner himself puts on it**, because it is more honest than most accounts of the same sequence: the claimed result is that the organization will "at least" say it knows what the strategy is and is behind it. **That is awareness and stated support. It is not adoption**, and treating it as the finish line is how a rollout stalls at high survey scores.

**The transferable rule for anything in this skill.** If your rollout plan contains no change to a talent decision, you are relying on communication to move culture. **Check three things before launch: does anyone get promoted differently, does anyone get hired differently, does anyone get paid differently?** If all three are no, the change is reversible the moment attention moves.

*(Source: John Stankey at the HBR Leadership Summit 2026, Jul 2026 — ⚠ single-company practitioner account from the CEO of the company in question, with no outcome data attached to the sequence and an obvious interest in how the transformation is characterized. The three steps are conventional; **the useful part is the ceiling he puts on their result.** Falsifier: a culture change that held after attention moved on, with no accompanying change to hiring, promotion or pay.)*

## SAFETY IS THE ADOPTION VARIABLE, AND SABOTAGE IS A PREDICTABLE RESPONSE

Gate Zero asks whether the rollout was co-created or announced. **This section says what goes wrong when it was announced, and why the damage is worse than slow uptake.**

**The chain, and each link is testable:**

1. **Leaders do not know how their people feel about the rollout.** They report an informed, enthusiastic workforce already saving hours a week. The workforce reports confusion, small time savings, and no clear strategy. **This gap is not a communications problem.** It persists because nobody is doing the perspective-taking that would close it.
2. **Safety is what produces experimentation.** People who feel protected will take the risk of trying a new tool. People who do not are being asked a question they will not say out loud: why would anyone be enthusiastic about training their replacement? **Fear of becoming obsolete shuts down the exploring that adoption is made of.**
3. **Unsafe rollouts produce worse output, not just less of it.** Under surveillance without care, people perform effort rather than doing work, and AI makes the performance faster and harder to spot. The result looks sensible, lacks substance, is cheap to produce, and is expensive for colleagues to unwind.
4. **The severe end of the same spectrum is active resistance.** Feeding sensitive data to unauthorized tools, tampering with output. **Treat it as a structurally predictable response to an unmanaged threat rather than as a discipline problem**, because the discipline response makes it worse and the structural response fixes it.

**Two things are missing at the root, and each fix restores one.** Leaders lack a feedback loop. Employees lack a safety net.

| Fix | Which one it restores | The failure it prevents |
|---|---|---|
| Co-create the strategy instead of announcing it | The feedback loop. Asking replaces telling. | The perception gap that started the chain |
| Train frontline managers, not only senior leaders | The safety net, at the layer where people actually experience management | Safety that exists in the town hall and nowhere else |
| Build AI that deepens connection, not only AI that substitutes | Both, by changing what the technology is for | The zero-sum frame that makes self-protection rational |

**The third one is the one that gets skipped, and it is a product decision, not an HR one.** Every automation choice carries an implicit answer to whether this tool replaces people or connects them. **That answer is a choice you are making whether or not you notice making it**, and the workforce reads it correctly long before anyone announces it.

**The measurable version, so this does not stay a values conversation:** ask people what they would need to feel safe experimenting, before the rollout. Then ask again at 60 days. If the second answer is thinner than the first, the rollout is producing performance rather than adoption, and your usage numbers are measuring the wrong thing.

*(Source: Jamil Zaki, HBR, "Empathetic Leadership Can Make or Break AI Adoption," Apr 2026 — ⚠ argument-tier, drawing on the author's own empathy research applied to AI rather than on an AI-specific study. The adoption-gap figures are secondhand survey citations. "Workslop" is borrowed vocabulary, not the article's coinage. Falsifier: an announced, non-co-created rollout in a low-safety environment that produced durable voluntary adoption and no hidden use.)*

## TWO LEVERS DRIVE ADOPTION, AND ONLY ONE OF THEM CARES ABOUT QUALITY

Gate Zero's currency translation is one lever. **There is a second, and this skill has been folding them together.**

| Lever | The mechanism | Cost to run | The catch |
|---|---|---|---|
| **Currency translation** | denominate the benefit in a metric the adopter is already measured on | high: you have to do the metric work | slow, and it needs a credible claim |
| **Audience exposure** | make the tool's use **visible to an external audience the employee cares about** | low: no metric work at all | **it drives use, not skilled use** |

**The exposure case.** One asset manager reported rapid adoption of virtually every AI tool it released. The stated mechanism was not that anyone showed employees a metric. It was that **the tools were visible to clients and partners.** A salesperson uses the tool because the adviser across the table can see whether they did.

**The failure mode, and it is specific and checkable.** Someone who opens a tool because a client will notice has every incentive to open it and **none to use it well.** So exposure predicts a distinctive signature: **high adoption, flat output quality, and nobody measuring the second one.** That same company reported rapid adoption of everything and not one quality metric.

**The rule: if you pull the exposure lever, you must instrument quality**, because the lever you pulled does not care about it. Currency translation at least points at an outcome. Exposure points at a behavior.

**When exposure is unavailable:** it only exists where the tool touches an external audience the employee cares about. For purely internal tooling there is no exposure lever, and currency translation is the only one you have.

## FIVE CONDITIONS FOR AN ONBOARDING THAT PEOPLE ACTUALLY LIKE

The phase model below is about **timing**. This is about **content**, and the two are independent.

The conditions are **sequential**: a later one cannot activate until the earlier ones are met. Not every good experience needs all five, but the ones that change behavior tend to have them.

1. **Control.** "What is this, and how should I engage with it?" Orientation and a clear choice, given before anything else is asked.
2. **Harmony.** "Do you know what I am feeling, and do you care?" Meet people where they are emotionally before asking them to move.
3. **Significance.** "Do you know my story, and do you care?" Personalization that signals this specific person matters.
4. **Warmth.** "Who is with me, and how can they help?" Visible, reachable support.
5. **Growth.** "How will I be more capable tomorrow?" **This one collapses entirely if 1 through 4 are unmet**, which is why a training-first rollout with no orientation fails.

**Use it as a checklist against your Surge-phase materials.** Most rollouts jump to condition 5, because training is the thing that looks like adoption support. See `rtp-feedback-flywheel` for how to source these from your own top-decile users rather than assuming.

*(Sources: the two-lever split, HBR, "Transforming Investing With AI at Franklin Templeton," Jun 2026 — ◆ single company, self-reported, and the quality-signature prediction is this corpus's inference from the absence of quality metrics rather than a measured finding. The five conditions, Marcus Buckingham in HBR, Jun 2026 — ⚠ framework-tier, one company's worked examples, no outcome data.)*

## THE ADOPTION CURVE: Three Phases, Three Different User Needs

### Phase 1: Surge (Week 1 - Week 4)

**What's happening:** Novelty. Users try the tool because it's new and leadership said to. Productivity hasn't improved yet — they're running both the manual process AND the AI tool in parallel. (Novo Nordisk's own numbers for this phase: 23% frequent users, 74% moderate users — see Quick Reference.)

**User mindset:** "This might be useful. I'll experiment."

**Who you deliberately launch to first:** don't default to "everyone at once" or even "your broadest ideal customer profile." Choose an **Early Customer Profile** — the narrow slice with the highest pain and highest tolerance for rough edges, not necessarily your eventual mainstream user — and aim for a genuine **beachhead**: 60-70% real penetration of that narrow slice within 3-18 months, before expanding. A wide, unfocused Week 1 rollout produces a wide, unfocused Month 3 dip with no concentrated pocket of proof to rebound from; a narrow, well-chosen Surge cohort gives you real reference users by the time you need them for Phase 3.

**A real exception to "highest pain first":** highest-pain slices are the right choice when what you need from the pilot is information about whether the tool works. Sometimes what you need first is organizational permission, and that calls for the opposite choice. Warner Bros. Discovery deliberately ran its first pilots on **noncontroversial** work ("if we screwed it up, nobody would care") rather than its highest-value use cases (see the growth-framing scoping note in GATE ZERO). Pick the noncontroversial pilot when trust, not information, is your actual constraint; pick the highest-pain slice when it isn't.

**Support needed:**
- Quick wins — show the easiest use cases first (not the hardest)
- Slack channel for peer support (not just help desk)
- Weekly "tip of the week" showing one new feature
- **Champions program, chosen deliberately** — not just "the most enthusiastic person per team." Microsoft's own internal Copilot rollout (HBS Case 626065) found that the single highest-leverage move was pairing its *most skeptical, most tenured, highest-credibility veteran* with its *most experimental, most tech-savvy junior employee* — not exposing the org to an early adopter's success from a distance. The mechanism is credibility transfer, not exposure: a demo convinces no one because it's disconnected from a skeptic's actual workflow and risk tolerance, but watching a 20-year veteran the team already trusts visibly switch over is unfakeable proof. Recruit your Champions for who they can convert, not just for who converts easiest.

  **Why a veteran's switch works and a workshop doesn't: the whether-channel.** An observed act carries two separate signals. A how-channel is process knowledge, what to actually do, and it needs the observer to already have some competence to absorb it. A whether-channel is permission, meaning this is safe to attempt here, and it needs no observer competence at all: it can move a whole team from a single act. The whether-channel only fires when the observer sees the demonstrator personally bear a real, costly consequence. A workshop or a simulated demo asks nothing real of the person demonstrating, so it transmits no permission no matter how polished it looks, which is exactly why a scripted leadership demo convinces nobody and an unscripted veteran switching over does. **Three tests for whether a "demonstration" actually qualifies:** the calendar test (did the demonstrator's own schedule visibly change), the uncertainty test (did they visibly not know the answer and say so rather than perform confidence), and the cancellation test (was something real called off or delayed to make room for this). A Champion, or a leader, who passes none of the three is only announcing, not demonstrating. Treat their Surge-phase involvement as decoration, not as the credibility-transfer mechanic this section relies on. *(Source: HBR, "Model the Transformation You Expect Employees to Deliver," Jul 2026 — ⚠. The author is a consultant citing his own unnamed clients with a book to sell; the how/whether distinction and the three tests are worth carrying, the specific baseline percentages behind them are not.)*

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

**A trap specific to this phase: accountability and ownership decay at different rates.** Accountability (who answers for the outcome on paper) persists long after ownership (who actually feels responsible for it day to day) has quietly drifted back to the old habit. A status report that only checks "who owns this" will read as healthy for months after the real work has reverted, because the org chart hasn't caught up with what people are actually doing. **The move:** in Rebound, check ownership directly (what people actually do without being asked) rather than accountability (whose name is on the initiative). **When this is wrong:** for a genuinely simple, low-discretion tool with no habit to form or lapse, this distinction doesn't add much, since there isn't a meaningful gap between the two to watch for. *(Source: HBR, "New Skills to Navigate Continuous Change," Jul 2026 — ⚠ reported, mechanism-level claim, no population or figures attached.)*

**A related caution on what "success" should not be measured by: training hours.** A KPMG study of 523 organizations (◆ company-disclosed survey data) found training hours delivered are an exposure metric, not a quality one. The constraint on adoption quality is sequencing and evaluation discipline, not how much training people sat through (see `rtp-judgment-guard` for the full finding). Don't let "hours of training delivered" stand in for "adoption is working" anywhere in a Rebound-phase report.

**A cheap, observable signal of whether this phase will hold: forking.** Has any team locally modified the rolled-out program to fit its own context, rather than running the identical, unmodified version everyone else got? An unmodified program predicts it lapses the moment its executive sponsor moves on; a locally forked one predicts it survives, because someone besides the sponsor now has a stake in it working. **The move:** ask this as a post-launch health check, not just at launch. **When this is wrong:** in a genuinely standardized, compliance-driven rollout (the same steps must run identically everywhere for audit or safety reasons), forking is the wrong outcome to hope for. There, an unmodified program is the correct one. *(Source: HBR, "Design AI Systems That Actually Strengthen Human Reasoning," Jul 2026 — ⚠ reported, single piece, no quantification given.)*

**Support needed:**
- **Continuous improvement loops** — Weekly feedback: "Here's what you're using, here's where similar users struggle, here's a shortcut you might like."
- **Advanced features for power users** — The users who love the tool will want more sophisticated features. Build for them. They drive adoption within their teams.
- **Outcomes measurement, and lead with quality, not hours saved** — Shift from "% of users using" to "what improved because of this." Novo Nordisk's own data found employee satisfaction correlated three times more strongly with *perceived work-quality improvement* than with time saved, and that people who saved time reinvested it into strategic and relationship work, not leisure. "This saved you 2 hours a week" is a weaker message than "this catches errors before your manager sees them." Report both, but lead with quality.
- **Ownership check, not just accountability check** — confirm who still actually does the new workflow day to day, not just whose name is attached to the initiative on paper.
- **Forking check** — ask whether any team has adapted the rollout to its own context. If every instance is identical months in, that is a warning sign, not proof of consistency.

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

6. **By Rebound, has anything been forked, and does ownership still match accountability?** (post-launch durability check)
   - Red flag: "Every team runs the identical, unmodified version, and we haven't checked who actually does the new workflow versus whose name is on it"
   - Yellow: "One or two teams have adapted it locally; we haven't formally checked ownership drift"
   - Green: "Multiple teams have forked it to their own context, and a recent check confirmed the people using it day to day, not just the named owner"

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

- **Relying on a general disclosure policy instead of an abstention list.** Some places where AI is used, disclosure itself destroys the value (a hand-written-looking donor email, for instance). Name those places up front; don't assume "we'll disclose it" covers every case.

- **Letting a self-service tool erase the function it was built on top of.** If the rollout deletes the "librarian" role that used to generate demand for a team's expertise, don't be surprised when usage of the underlying work drops and that team's budget gets questioned next.

- **Treating training hours delivered as evidence adoption is working.** Hours of training are an exposure metric. They say nothing about sequencing or evaluation discipline, which is what actually predicts adoption quality.

- **Mistaking an identical, unmodified rollout across every team for a sign of consistency.** It is more often a sign that nobody has made it their own, and it tends to lapse the moment the executive sponsor moves on.

- **Trusting verbal agreement in the launch-team room without checking it in writing.** A room that nodded along can still hold five different mental models of what's being launched. Run the false-alignment test before you build phases on top of that agreement, not after.

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
- [ ] Places where AI can't be used even with disclosure are named up front (an abstention list), not left to a general disclosure policy
- [ ] The function whose expertise this rollout is meant to scale has been checked for status repair, not just given a benefit explanation
- [ ] Contestability (whether the person using this can independently catch an error) is treated as a resource to maintain, not assumed to survive on its own
- [ ] Any leadership or Champion "demonstration" you're relying on passes at least one of the calendar, uncertainty, or cancellation tests
- [ ] Every leader on the launch team has independently written down what the change is and how it works (false-alignment test), and a named take-up plan states who must change what behavior and whether that's credible
- [ ] Rebound-phase reporting checks ownership (who actually does the new workflow) and forking (has anyone adapted it locally), not just usage and a named owner
- [ ] Resource allocation and ownership clear for each phase

---

## WHEN WRONG

This skill gives bad advice if:

- **The underlying AI tool doesn't actually work.** If the AI has quality/reliability problems, no adoption strategy will fix it. Use `eval-framework` to validate performance before investing in adoption.

- **The user's real problem has nothing to do with adoption support.** Sometimes resistance is because the tool is too slow, requires too much context, or gives inconsistent answers. No amount of Champions or peer support fixes that. Fix the product.

- **The organization has no plan to sustain adoption support beyond 6 months.** If adoption lead role disappears after Month 3, adoption will revert. Champions will burn out. Make sure the organization has committed to long-term support before designing a phase-based plan.

- **There's no stable, tenured workforce with a legible internal credibility hierarchy.** The skeptic-experimenter Champion pairing assumes you have an identifiable, respected "20-year veteran" figure to recruit. In high-turnover, distributed, or gig workforces, or flat orgs without that figure, this specific tactic won't transfer — fall back to broader peer-network champions instead.

- **Nobody's role is plausibly threatened by the tool.** Growth or threat-removal framing (Gate Zero's currency-translation lever) has nothing to neutralize when the adopter isn't plausibly replaceable by what you're rolling out. Defaulting to a noncontroversial first pilot in that setting trades away real learning for permission you didn't need to buy.

- **Psychological safety on the launch team is low.** The false-alignment test only surfaces real disagreement if people write down what they actually believe. Where speaking against the sanctioned answer carries a visible cost, everyone's written answer converges anyway, and the test reports false confidence instead of catching none.

---

## TRADE-OFF LEDGER

### Choosing to treat adoption as a product launch with phase-specific support:

**We are betting on:** That active, phase-specific support — including deliberate Champion selection and a manager-layer check, not just end-user support — will prevent adoption collapse at Month 3 and produce a durable rebound by Month 5.

**We are giving up:** Speed and simplicity. A "just roll it out and train people" approach is faster. A phase-based adoption program requires ongoing coordination, resource allocation, and continuous adaptation for 5+ months.

**This is reversible within:** Not really. Once you launch, adoption curve is playing out. But you can course-correct. If Month 3 dip is worse than expected, you can intensify support in Month 4.

**The hidden trade-off:** **Adoption support consumes resources.** The Champions program, the adoption lead, the weekly communications, the help desk triage — this costs people and time. You're trading engineering velocity (product team is responsive to adoption feedback) for adoption sustainability. If your product is mature and feature parity is your goal, this trade-off makes sense. If you're early-stage and innovation velocity is paramount, this trade-off is harder.

**Confidence: High on the curve shape; Medium on the specific tactics.**
- **Evidence.** The Surge-Dip-Rebound shape rests on Everett Rogers' adoption research, plus two rollouts that reproduce it independently at very different scale and tool type: Novo Nordisk (◆, MIT Sloan, Jul 2025) and Microsoft (⚠, HBS Case 626065, May 2026). The access-against-use gap is confirmed independently by the IBM 2026 CEO Study (◆) and a McKinsey 2025 survey (✅).

  Weaker ground, and worth naming as such. The competency-trap and role-elevation mechanisms each rest on a single well-documented case or a small-N interview study, not yet replicated. The same is true of the seven 2026 additions: status repair, contestability, the sequencing correction on power users, the whether-channel and its three tests, the abstention list, forking as a durability signal, and the false-alignment test with its take-up plan. Each is grounded in one case, a small-N or unsampled study, or a source with a disclosed conflict of interest.

  **Carry the mechanisms. Treat the specific numbers behind them as unverified.**
- What would change our mind: A team that gets sustained, outcome-linked adoption with zero structured adoption support beyond one-time training; a second and third independent case showing the competency trap or role-elevation mechanism *doesn't* hold, which would demote those two from "apply by default" to "watch for it"; or a rollout that erases a function's status, ships explanation without preserved competence, or runs an unmodified program indefinitely and still produces durable, high-quality adoption.

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
- Status repair, contestability, the power-user sequencing correction, the whether-channel tests, the abstention list, forking, and the false-alignment test/take-up plan pair each hold in your context (each is currently grounded in one case, a small or unsampled study, or a source with a disclosed commercial interest; treat all seven as directional, not as base rates, until they replicate)

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
3. **Critical Intervention Points** — Timeline showing when to deploy Champions, edge case triage, the manager-layer check, outcomes measurement, and the Rebound-phase ownership and forking check
