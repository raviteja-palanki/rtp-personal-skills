---
name: rtp-trust-under-fog
description: Communicate confidently when outcomes are genuinely uncertain — without over-promising or under-delivering. Boards want guarantees. Customers want certainty. AI outcomes are probabilistic. This skill helps you build stakeholder confidence through transparency, not false promises. Use when stakeholders demand guarantees you can't give, when communicating AI capabilities to non-technical audiences, when navigating probabilistic outcomes but deterministic business expectations, or when rebuilding trust after over-promise. Skip when outcomes are deterministic (no fog) or when stakeholders are already comfortable with uncertainty.
---
# Trust Under Fog

## DEPTH DECISION

**Go deep if:** You're communicating AI capabilities to boards, customers, or regulators; rebuilding trust after over-promise; or designing communication strategy for uncertain outcomes. **Skim to questions if:** Quick audit of whether your current communication strategy is over-promising. **Skip if:** Outcomes are deterministic (no uncertainty) or stakeholders are already comfortable with probabilistic results.

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md):
1. Ask the Grounding Questions (Section 1) — at minimum: Who is the stakeholder? What's their comfort with uncertainty? What's the worst consequence of being wrong?
2. Route depth: Executive Summary or Comprehensive Analysis?
3. Identify output format: Document, presentation, or both?

Then proceed with the skill-specific analysis below.

## THE TRAP

You will over-promise to close the deal, secure budget, or build excitement. The bias is **certainty bias in AI communication** — the assumption that stakeholders need guarantees to move forward, so you provide them (even when you don't have them).

The mechanism is seductive: You say "95% accuracy" instead of "95% accuracy on our test set, which may differ from production." You say "the AI will automate this workflow" instead of "the AI will automate 70-80% of this workflow, depending on real-world conditions we haven't tested yet." The first statement closes the deal. The second doesn't. So you use the first. Then reality hits.

The trap is most seductive when:
- Budget is competitive and you're pitching against competitors (who may also over-promise)
- The stakeholder is non-technical (they hear "95% accuracy" and believe "this will just work")
- The outcome you're promising is genuinely valuable (you want to believe it yourself)
- The consequence of not getting funding/approval is high (pressure to say "yes, we can do this")
- You've already built reputation on similar promises (now you're caught in a cycle)

### The Wells Fargo Fake Accounts Case (2016-2017, Reputation Angle)

Wells Fargo's fake accounts scandal is often cited as ethical failure. But there's a communication angle worth examining: the company promised "ambitious growth" to the board. Growth requires revenue. Sales team promised unrealistic targets to achieve the growth promise. Targets required opening new accounts, even when customers didn't want them. Fake accounts followed.

The core failure: Over-promise at the top cascades down. Sales team over-promises to sales managers. Sales managers put impossible quotas on frontline staff. Staff cuts corners. Fraud.

What if Wells Fargo had communicated differently? "We'll grow revenue by 5% annually, from existing customer relationships deepening, plus new acquisitions. This is lower than competitors who promise 10%, but sustainable." No fake accounts needed.

The trust repair required *exact the opposite of over-promise*. After scandal broke, new leadership had to say: "We over-promised. We're now under-delivering on growth to build back trust." It took 5 years.

**The AI parallel:** You over-promise on model accuracy or automation capability. Deployment happens. Reality doesn't match. Stakeholders feel betrayed. Trust erodes. Recovery is slow.

## THE PROCESS

### 1. THE CERTAINTY AUDIT

Ask: **"Which parts of this outcome can I guarantee? Which parts are genuinely uncertain?"**

Be forensically honest.

**Example (AI customer support triage):**

| Component | Guaranteed | Uncertain | Confidence | Why |
|-----------|-----------|-----------|-----------|-----|
| **Model classifies tickets into 10 categories** | Yes | N/A | 99% | Tested on 10k+ examples. Accuracy is consistent. |
| **Classification works on NEW categories (not in training)** | No | Yes | 20% | We haven't seen these tickets. Model will guess. |
| **Humans accept the classification as useful** | No | Yes | 60% | Depends on how clear the categories are, how well trained they are, workflow friction. |
| **Support team velocity increases 20%** | No | Yes | 40% | Depends on alert accuracy, adoption, motivation to use the tool. |
| **Cost per ticket drops 15%** | No | Yes | 30% | Depends on velocity improvement + wage inflation + system maintenance costs. |

**Output:** A certainty map showing what you're confident in, what's uncertain, and where the uncertainty lives.

### 2. MAP THE UNCERTAINTY SPECTRUM

Ask: **"On a spectrum from deterministic to probabilistic, where does this outcome live?"**

Use the [determinism-compass skill](https://example.com/determinism-compass) framework. Outcomes exist on a spectrum:

**Deterministic end:**
- Outcome is rule-based. If X, then Y.
- Repeatability is 100%.
- Example: "If ticket contains keyword 'billing,' route to billing team." Always works.

**Probabilistic end:**
- Outcome requires judgment or pattern recognition on ambiguous inputs.
- Repeatability is <99%.
- Example: "AI decides if customer complaint is valid or frivolous." Same complaint might get different judgment depending on context.

**Most AI outcomes live on the probabilistic side.** Acknowledge this. Don't pretend they're rule-based.

### 3. THE THREE COMMUNICATION STYLES

Design communication for each stakeholder using style appropriate to their tolerance and need-to-know.

**Style 1: Confident Uncertainty**
*Use for:* Customers, frontline teams, anyone implementing the system

Format: "We're [X]% confident, and here's what we'll do about the other [100-X]%."

Example: "The AI is 85% confident in its recommendations. When it's less confident, it flags the recommendation for you to review. This way, you benefit from AI speed on the easy cases, and stay in control on the hard cases."

**Why this works:** You're not pretending certainty. You're showing competence by naming uncertainty AND having a plan for it. People trust this more than false certainty.

**Style 2: Bounded Promises**
*Use for:* Boards, investors, contracts where you need to commit to something

Format: "Under these conditions, expect X. If conditions change, reset."

Example: "Under current market conditions (competitor pricing stable, customer mix consistent), we expect 15% cost reduction in support operations. If competitors undercut pricing by >20%, or customer mix shifts to higher-support segments, we'll reevaluate."

**Why this works:** You're making a promise, but you're also making the boundary conditions explicit. If boundary conditions change, you're not suddenly wrong — you're just resetting. This is contracts language, not marketing language.

**Style 3: Transparent Ranges**
*Use for:* Technical teams, detailed planning, resource allocation

Format: "Between X and Y, depending on Z."

Example: "Automation will handle between 60-85% of tickets, depending on how well the model learns your specific ticket distribution. We'll know the actual number after 2 weeks of live data."

**Why this works:** You're giving decision-makers a range to plan for. They can resource for the worst case (85% automated = 15% remaining) and upside if the best case hits (60% automated = 40% remaining). This is planning language.

### 4. THE UNCERTAINTY BUDGET

Ask: **"How much uncertainty can each stakeholder absorb?"**

Different stakeholders have different tolerance.

**Board:** Can handle 10-20% uncertainty in outcome. They care about predictability for financial planning.

**Customer:** Can handle 30-40% uncertainty in experience quality. They care about value and whether it's predictable enough to rely on.

**Frontline team:** Can handle 50%+ uncertainty in workflow. They care about tools that help, even if imperfect.

**Regulator:** Can handle 5-10% uncertainty in critical metrics (accuracy, bias, safety). Anything above is approval-blocking.

**Design:** Communicate style that matches their uncertainty budget.

**Example (insurance claim automation):**
- **Board:** "Claims automation will improve processing speed by 20-30%, reducing cost per claim by $50-75. This assumes our model generalizes to new claim types (our biggest unknown)."
- **Claims team:** "The AI will process 60-70% of claims without human review, on a probationary basis. We'll expand if accuracy stays above 98%."
- **Regulator:** "The model has 98.5% accuracy on test set. Real-world accuracy may vary. We audit 100% of automated decisions for the first 90 days."

### 5. SIGNAL-BASED RESETTING

Ask: **"How will I know if my prediction was wrong? And what do I do then?"**

Uncertainty is only manageable if you have a plan for being wrong.

**Define leading indicators** (signal that emerges in days/weeks):
- "If the model accuracy on live data is <95% after week 1, we pause full rollout and investigate."
- "If customer satisfaction with recommendations drops >5%, we retreat to hybrid mode (AI suggests, human approves)."

**Define lagging indicators** (signal that emerges in months):
- "If cost per ticket doesn't improve by 10% after 3 months, we reevaluate the model."
- "If adoption stays below 60% after 6 months, we solicit feedback on why and adapt."

**Most importantly: Say what you'll do.**
Not: "We'll monitor and adapt." (Vague. Non-committal.)
But: "If accuracy drops below 95%, we will pause rollout and spend 1 week investigating. We'll communicate findings to leadership by Friday."

## DIAGNOSTIC QUESTIONS

Answer these before designing your communication strategy:

1. **"Can I list five ways this prediction could be wrong?"** If you can't, you're overconfident.
   - **Red flag:** "It can't be wrong. We tested it."
   - **Sharpening probe:** "What's the most surprising way this could fail?"

2. **"What's the worst realistic outcome if this goes wrong?"** Not catastrophic. Realistic.
   - **Red flag:** "Nothing really bad. Maybe slight delay." (That's probably under-estimating.)
   - **Sharpening probe:** "What would the news headline be if this failed publicly?"

3. **"What does the stakeholder actually care about?"** Your accuracy metric? Or their business outcome?
   - **Red flag:** "They want 99% accuracy." (Do they, or do they want their workflow to work smoothly?)
   - **Sharpening probe:** "If accuracy was 92% but the workflow improvement was 25%, would they still want this?"

4. **"Have I told them the worst-case scenario?"** Or are they assuming best case?
   - **Red flag:** "I mentioned it was probabilistic." (Did they hear it or did they decide it doesn't apply to them?)
   - **Sharpening probe:** "If I asked them to repeat back the range of outcomes, what would they say?"

5. **"How will I know I was wrong?"** Specific signal, not abstract.
   - **Red flag:** "We'll evaluate after launch and adjust." (Too vague. When? By what metric?)
   - **Sharpening probe:** "What number would make you say, 'This isn't working as promised'?"

6. **"Am I comfortable defending this communication to a skeptical audience?"** Board? Regulator? Customer who got bad result?
   - **Red flag:** "I'm a little nervous about how this lands." (That's your signal that you've over-promised.)
   - **Sharpening probe:** "If they pushed back and asked 'why did you say it would do X when it only did Y?', what's my answer?"

## REALITY CHECK

**Failure modes:**
- **Communicating certainty, then being wrong**: You say "85% accuracy," it's 72%. Stakeholder feels lied to, even if 72% is still useful.
- **Communicating uncertainty, then underdelivering on what you DID promise**: You say "between 60-85% automation," it's 50%. Even though 50% is in the uncertain range, if you promised "we'll know after 2 weeks," and after 2 weeks you still don't know, trust erodes.
- **Communicating ranges, then not telling people which end of the range happened**: "60-85% automation" rolls out. You discover it's 62%. You don't communicate this. People assume 85% and are disappointed when they notice the actual number later.

**Cost traps:**
- Transparent communication feels slower (longer sentences, more caveats).
- Stakeholders may demand proof of your uncertainties (which is reasonable and requires data you may not have).
- Recovery from over-promise is expensive (years of under-deliver to rebuild trust).

**Monitoring:**
- Track "stakeholder satisfaction with accuracy of prediction vs reality" (quarterly)
- Track "leading indicator signals detected and acted on" (did you catch signals early?)
- Track "trust signals" (return rates, contract renewals, team satisfaction, regulatory compliance)

## THE OVER-PROMISE RECOVERY PROTOCOL

If you've already over-promised, here's how to repair:

**Phase 1: Admit (Week 1)**
- Name the over-promise. "We said X, but we're learning it's more like Y."
- Explain why (technology limits, real-world conditions different from test, etc.)
- No excuses. No blame-shifting.

**Phase 2: Reset (Week 2)**
- Communicate the new, more realistic expectation.
- Use Bounded Promises or Transparent Ranges (not Confident Uncertainty — you've lost that)
- Offer choices: "Do you want to (A) continue with revised expectations, (B) pause and reassess, or (C) exit?"

**Phase 3: Deliver (Weeks 3+)**
- Under-promise, over-deliver. If you say "60-70%," aim for 75%.
- Report frequently. Monthly updates on progress.
- Celebrate small wins. "We hit 72% this week, on our way to the upper range."

**Phase 4: Rebuild (Months 2-6)**
- Restore trust through consistency. Do what you say, every time.
- Involve stakeholders in monitoring. "Here's the leading indicator dashboard. You're seeing exactly what we're seeing."
- Acknowledge what was learned. "We were wrong about X. Here's what we know now."

## QUALITY GATE

- [ ] Certainty map created (what's guaranteed vs uncertain)
- [ ] Uncertainty spectrum mapped (deterministic end vs probabilistic end)
- [ ] Communication style selected per stakeholder (Confident Uncertainty vs Bounded Promises vs Transparent Ranges)
- [ ] Uncertainty budget defined for each stakeholder (how much variance can they absorb?)
- [ ] Leading indicators defined (what signal will tell us we're off course?)
- [ ] Resetting protocol in place (what do we do if the prediction is wrong?)
- [ ] Communication tested with skeptical stakeholder (can they poke holes in it?)

## WHEN WRONG

This skill gives bad advice when:
- **Outcomes are actually deterministic** (not probabilistic) — don't apply uncertainty communication if it's rule-based
- **Stakeholders are sophisticated and already comfortable with uncertainty** (they may find transparent ranges patronizing; accelerate to Bounded Promises)
- **You're dealing with a situation where transparency will *increase* distrust** (rare, but if the outcome is so uncertain that even being transparent makes them uncomfortable, you may need to first prove capability with smaller bets)

## TRADE-OFF LEDGER

BY CHOOSING **transparent, bounded communication over false certainty**:
  We are betting on: Stakeholders will trust us more if we're honest about uncertainty than if we pretend certainty.
  We are giving up: The initial excitement and easy approval that comes with over-promising.
  This is reversible within: If transparency causes you to lose a deal, you can adjust messaging. But recovery from broken trust takes months.

THE HIDDEN TRADE-OFF:
  Transparent communication forces you to name what you don't know. This is uncomfortable. It also means stakeholders see the gap between what's promised and what's guaranteed. Some will flee. That's actually good — they're not a good fit anyway. You're attracting stakeholders who are okay with the uncertainty, which is the right kind of stakeholder.

CONFIDENCE: **High**
  What would change our mind: If we saw teams that over-promise consistently win more contracts and maintain more trust than teams that communicate transparently. We've never seen this.

## CONCLUSION

**The recommendation:** Use transparent, bounded communication for all AI outcomes. Do not promise certainty you don't have.

**The hypothesis:** We believe that **stakeholders will develop stronger, more durable trust in teams that communicate uncertainty honestly than in teams that over-promise**, because over-promises inevitably break and break trust when they do.

**The 3E decision:**
- **Explore:** Audit current communication strategy (1 day). Are you over-promising? What signals suggest this?
- **Exploit:** If over-promising detected, reset communication with stakeholders using one of the three styles (Confident Uncertainty, Bounded Promises, Transparent Ranges). Establish leading indicators for course-correction.
- **Exit:** If stakeholders refuse to accept any uncertainty and demand guarantees, this is a fit problem. Either (A) find a different stakeholder, or (B) reduce scope until you can guarantee it.

**The key trade-off:** We're choosing durable trust over initial enthusiasm. Transparent communication is slower to close, but stronger once it lands.

**The biggest risk:** That you reset communication with stakeholders and they decide the risk is too high. This is better than discovering it later after you've over-delivered.

**Assumptions to watch:**
1. Stakeholders can tolerate the level of uncertainty you're naming (test this with questions, not assumptions)
2. Leading indicators you've defined will actually emerge in real-time (false — some won't, meaning you've misunderstood the system)
3. You can actually deliver the worst-case scenario you've promised (if you can't, you've set the bound too loosely)

**The next action:** Conduct communication audit (1 day). Identify places where you're over-promising. Rewrite communication using one of the three styles. Get stakeholder feedback before rolling out.

## GENERATE THE DELIVERABLE

Use the output prompt from the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md).
If this skill connects to downstream skills, also generate the markdown handoff file (if relevant to governance or stakeholder management strategy).

## VISUAL SUMMARY

After completing the primary output, invoke the excalidraw-svg skill to create a single Excalidraw SVG visual summary showing:
- The Certainty Audit matrix (what's guaranteed vs uncertain vs unknown)
- The Uncertainty Budget by stakeholder (Board: 10% tolerance, Customer: 40% tolerance, etc.)
- The Three Communication Styles with examples for each
- Over-promise recovery timeline (Admit → Reset → Deliver → Rebuild)
