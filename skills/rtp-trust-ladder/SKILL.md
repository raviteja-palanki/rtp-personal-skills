---
name: rtp-trust-ladder
description: "Design autonomy levels that match CALIBRATED trust and failure severity. Use when: defining permission models, progressive autonomy, detecting over-reliance, repairing trust after errors. Do NOT use: to justify maximum trust, full autonomy without calibration, when mental models misalign."
imports: ["determinism-compass"]
version: "1.1"
---

# Trust Ladder

## DEPTH DECISION

**Go deep if:** Designing trust progression for a new AI feature, diagnosing trust issues in production, or deciding autonomy levels for multi-step agents.

**Skim to Diagnostic Questions if:** Quick trust audit — you just need to check whether users have calibrated expectations and whether rejection rate is healthy (not too high, not too low).

**Skip if:** Users already have established trust with the product, or you're tuning an existing autonomy level (use reality check instead).

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md):
1. Ask the Grounding Questions (Section 1) — at minimum: Who is the customer? What problem? What are we saying YES to and NO to?
2. Route depth: Executive Summary or Comprehensive Analysis?
3. Identify output format: Document, presentation, spreadsheet, or inline?

Then proceed with the skill-specific analysis below.

---

## THE TRAP

Binary choice: ask for everything (safe but creates decision theater) or full autonomy (fast but dangerous). The trap is confusing *maximum* trust with *appropriate* trust. Users who accept 100% of suggestions aren't more trusting — they've stopped checking. That's the failure mode.

Real cost: Over-asking wastes user attention and trains users to click yes without reading. Full autonomy breeds over-reliance. Both break catastrophically when the system fails. Calibrated trust means users still reject ~15–30% of suggestions — they're still thinking.

## THE PROCESS

**Step 1: Failure Mode Severity**
- What goes wrong if the AI acts alone?
  - **Trivial:** Typo, formatting error → Undo easily.
  - **Reversible:** Money transfer, file deletion → Undo with friction.
  - **Irreversible:** Publishing, legal commitment, medical decision → Cannot undo.
- **Trivial → Don't Ask.** **Reversible/Irreversible → Go to Step 2.**

**Step 2: Assess User Mental Model**
- Does the user's understanding of what the AI can/can't do match reality?
  - Test: Ask user, "What will happen if you press this button?" If their answer doesn't match what actually happens, their mental model is wrong.
  - Danger zone: Enterprise users often assume AI is deterministic ("It always does X"). When it doesn't, trust collapses.
- **If mental model is wrong:** Add transparency design *before* autonomy level discussion. Show reasoning traces, confidence scores, failure examples. Build accurate model first.
- **If mental model is right:** Proceed to Step 3.

**Step 3: Trust Calibration (Scale)**
- **Level 1 (Distrusts):** Burned before. Wants proof for every action.
- **Level 2 (Skeptical):** New or unsure. Wants safety rails.
- **Level 3 (Conditional):** Trusts AI on emails, not money. Domain-dependent.
- **Level 4 (Trusts):** Consistent good experiences. Willing to delegate.
- **Level 5 (Over-reliant):** Treats AI as ground truth. RED FLAG. User has stopped thinking.

Detection: **If user rejection rate < 5%, they're over-reliant.** Healthy products show 15–30% rejection rate.

**Step 4: Autonomy Assignment**

*For Trivial failures:*
- All levels → Autonomous. User can undo.

*For Reversible failures:*
- **Level 1–2:** Ask + show reasoning, alternatives, refusal option.
- **Level 3:** Ask with "trust this type of decision" checkbox.
- **Level 4:** Autonomous + 24hr undo visible. Include confidence score.
- **Level 5:** **Block autonomy intentionally.** Force permission even if annoying. This is calibration, not punishment.

*For Irreversible failures:*
- **All levels → Ask.** Show reasoning, cost of being wrong, alternatives, refusal. No exceptions.

**Step 5: Confidence Display (The Most Underrated Feature)**
- Always show confidence:
  - **95%+ confidence:** "I'm very confident in this."
  - **70–95% confidence:** "I'm fairly confident, but double-check."
  - **50–70% confidence:** "This is a guess. I could be wrong."
  - **Below 50%:** "I don't have enough information."
- Research: 63% of users are more likely to rely on AI that displays confidence levels. This builds *calibrated* trust, not blind trust.
- Show reasoning trace: Not just "transfer $5K." Say: "Transfer $5K because: (1) historical spend pattern suggests budget available, (2) vendor invoice matched, (3) approval authority confirmed."

## CALIBRATED TRUST

The goal is **calibrated trust**, not maximum trust. Over-trust is as dangerous as under-trust.

**The asymmetry:**
- Users who trust AI too much skip verification → **automation complacency.** They accept outputs without reading.
- Users who trust too little won't adopt → **adoption friction.** They reject the system as too slow.
- **Calibrated trust:** User's confidence matches actual system reliability. They still think. They verify 15–30% of recommendations.

**Why this matters:**
When a user reaches "maximum trust" (95%+ acceptance rate), they've stopped evaluating output. The system is *more* autonomous, but there's *zero visibility* into failures until catastrophe. Calibrated trust means the user is still in the loop — not clicking blindly.

**Design for calibration, not adoption metrics:**
- "We got acceptance rate to 94%" is a failure flag, not a win.
- "Users reject 22% of recommendations, and we know why each time" is healthy.
- Calibration = system trust ↔ user vigilance alignment.

## TRUST REPAIR MECHANISMS

After visible mistakes, trust drops **2–3x faster than it builds**. Unlike earning trust (slow, incremental), losing trust is catastrophic and immediate.

**The repair pattern (5 phases):**

1. **Immediate Acknowledgment**
   - Say it now: "I was wrong about this."
   - Don't hide. Don't say "that's surprising." Own it.
   - Timeline: Within 1 message, 1 interaction.

2. **Transparent Explanation**
   - Explain *what* happened: "I missed the currency mismatch."
   - Explain *why* it happened: "I didn't check the sender's location against the invoice currency code."
   - Explain *where you were uncertain*: "I was 67% confident the amounts matched without cross-checking currency."
   - Never blame the user ("you provided unclear data") or external systems.

3. **User Control Restoration**
   - Show manual alternative immediately: "You can review this transfer manually here."
   - Or: "I've flagged this for manual review before execution."
   - Communicate: "You're back in control."

4. **Compensation (Offer Manual Alternative)**
   - For reversible failures: "I'll process this, but with your explicit approval required."
   - For irreversible failures: "I won't process this autonomously again until you confirm the fix."
   - Friction is *appropriate* here. It rebuilds trust.

5. **Demonstrated Improvement**
   - Show the system learned: "I'm adding a currency-match check against sender geolocation."
   - Quantify: "This check will catch 94% of similar mismatches."
   - Timeline: Not "we'll fix it," but "here's what changed and when you'll see it."

**The 63% finding:** Users trust systems that explain their reasoning 63% more than black boxes. This applies *especially* after a failure. Explanation = trust repair fuel.

**Trust repair is product design, not support.** Build error acknowledgment and recovery into the product. If it's a support ticket, you've already lost users.

## CONFIDENCE DISPLAY PATTERNS

Users don't all want the same confidence format. Progressive disclosure by expertise level.

**Pattern 1: Binary (Novice Users)**
- Simple yes/no with confidence threshold.
- "Yes, safe to send" vs. "No, hold for review."
- Example: "Should I delete this file?" → "No, this looks like a template. Hold for review."
- Use case: Non-technical users who want clear recommendation without probability details.

**Pattern 2: Graded (Intermediate Users)**
- High / Medium / Low confidence labels.
- "I'm fairly confident this vendor is authorized. Medium confidence on pricing accuracy."
- Example: Email spam detection → "High: Spam" / "Medium: Review" / "Low: Unsure."
- Use case: Users who want nuance but not raw probabilities.

**Pattern 3: Numeric (Advanced Users)**
- Raw probabilities: "87% confidence this is spam."
- "Confidence: 82%. Risk of false positive: 18%."
- Show the inverse explicitly: confidence to accept *and* confidence to reject.
- Example: Fraud detection → "82% confident this is fraud. 18% chance of false positive."
- Use case: Data analysts, engineers, power users who want precision.

**Pattern 4: Explanation-Based (Learners)**
- Confidence shown through reasoning depth: "I found 3 matching sources confirming this. 1 source contradicts it."
- Example: "Is this a real person? Yes. I found: LinkedIn profile (2019+), GitHub history (5 years), Twitter presence (consistent handle)."
- No numeric score. Confidence is *implicit* in evidence count.
- Use case: Users building their own mental model of system reliability.

**Implement for progressive disclosure:**
- Novice users default to Pattern 1 (binary).
- Let users upgrade: "Would you like to see confidence scores?" → Pattern 3.
- Expert mode → Pattern 4 + raw probabilities + failure case analysis.
- Never force numeric confidence on novices. It creates false precision.

## TRUST-AUTONOMY CALIBRATION TABLE

Map autonomy levels against trust states. Each cell specifies: (1) what the system does, (2) what the user sees, (3) what data you collect.

### How to Navigate the Calibration Table

The table has multiple rows representing different trust stages. Don't try to read all rows — use this decision tree to find your starting point:

```
WHERE ARE YOU?
│
├── NEW USER (first 1–7 days of use)
│   └── Start at rows 1–3
│       Focus: Establishing baseline expectations. Show what the AI is good at
│             AND bad at before the user has formed strong opinions.
│
├── BUILDING TRUST (1–4 weeks, using regularly)
│   └── Start at rows 4–7
│       Focus: Consistent reinforcement. Users are forming mental models.
│             Every unexpected failure here costs 3x a failure in the expert stage.
│
├── CALIBRATED USER (1+ months, using confidently)
│   └── Start at rows 8–12
│       Focus: Maintaining calibration. Watch for over-reliance signals
│             (rejection rate drops below 5% = red flag).
│
└── POST-FAILURE RECOVERY (any stage, after a significant AI error)
    └── Go back 2 stages from current position.
        A calibrated user who sees a significant failure needs to rebuild trust
        from the "building trust" stage. Skipping this = over-reliance.
```

| Trust State | Autonomy Level | System Action | User Visibility | Data Collected |
|---|---|---|---|---|
| **New User** | Level 0 (Ask Everything) | Always ask. Show 3 alternatives. Request explicit permission. | "I need your approval. Here's why (reasoning). Here's what happens if I'm wrong (cost). Here are 2 alternatives." | Permission rate, reasoning clarity feedback, alternative selection. |
| **New User** | Level 1 (Recommend + Ask) | Recommend top option with confidence. Always ask for irreversible/reversible actions. Autonomous only for trivial. | Recommendation ranked. Confidence shown. Permission modal includes reasoning and cost. Undo visible (if reversible). | Recommendation acceptance rate, time to decide, which users choose alternatives. |
| **Building Trust** | Level 1 (Recommend + Ask) | Same as above. *Monitor:* Is rejection rate healthy (15–30%)? | Same as above. + Add: "I was wrong X times last week. Improving." | Rejection rate trend, error acknowledgments, user follow-up after repair. |
| **Building Trust** | Level 2 (Autonomous on Low Stakes) | Autonomous for trivial failures. Ask for reversible/irreversible. Show confidence on all actions. | Trivial actions: "I [did X] autonomously. Undo." For ask-decisions: full reasoning + cost + refusal. | Undo rate, permission time, confidence calibration (are users trusting high-confidence recommendations?). |
| **Calibrated** | Level 2 (Autonomous on Low Stakes) | Same as above. *Introduce "trust checks":* Occasional scenarios where AI is intentionally uncertain to see if user still evaluates. | All actions show confidence. Every 10th recommendation: "I'm uncertain here (45% confident). What's your call?" | Are users still evaluating? Trend in edit rate (should stay 15–30%). Do users accept high-uncertainty recommendations? |
| **Calibrated** | Level 3 (Autonomous on Reversible) | Autonomous for reversible. Ask for irreversible. 24-hour undo window visible. Confidence on all actions. | All decisions: Confidence + reasoning. Reversible actions: "I did this. You can undo until [time]." Irreversible: Ask. | Undo rate (should be < 5%). Permission acceptance for irreversible (should be high, ~80%+). Rejection rate trend. |
| **Over-Reliant** (RED FLAG) | Level 0 (Reset) | Block autonomy intentionally. Force permission even if annoying. Ask on *reversible* decisions (normally autonomous for Level 3). Introduce explicit uncertainty. | "I notice you're accepting most suggestions. I'm flagging uncertain recommendations so you stay in the loop." Permission modal for reversible. + Confidence always shown. | Rejection rate (should rise toward 20%+). Do users push back on new friction? Session data: are they still reading explanations? |
| **Over-Reliant** | Level 1 (Graduated Re-Trust) | Autonomous for trivial. Ask for reversible with "*trust this type*" checkbox to graduate back to Level 3. Use confidence to guide caution. | Reversible: Ask + confidence. Checkbox: "I understand the risk. Proceed autonomously next time." Reasoning always visible. | Do users re-enable autonomy? Time between failures and re-enablement? New failures post-re-enablement? |
| **Repairing (Post-Failure)** | Level 1 (Recommend + Ask) | Revert to Level 1. Ask on reversible (even if user was Level 4). Show *exact* reasoning for every action. Introduce manual alternative. | "I was wrong about [X]. Here's what changed. I'm asking permission going forward on [decision type]." Manual path visible. | Permission rate on previously-autonomous decisions (should jump). Do users accept manual alternative? Time to rebuild trust (measure as rate of permission acceptance dropping). |
| **Repairing** | Level 2 (Graduated Autonomy) | Conditional autonomous based on sub-category. E.g., "I'm autonomous on emails, but asking on all financial decisions." Confidence required. | "I'm rebuilding trust on [decision type]. Currently asking. When I reach [confidence threshold], I'll ask less." + Manual option always visible. | Do users re-enable autonomy by decision type? Rejection rate by category. Time to full autonomy recovery. |
| **Enterprise** | All Levels | All decisions (regardless of autonomy level) must generate audit trail: decision made, reasoning, confidence, who approved, when, what changed. Rollback must be visible. | Audit trail visible on demand. "Decision made by [user/system]. Reasoning: [trace]. Confidence: [%]. Approved by [user]. Rollback until [time]." | Compliance: can you recreate every decision? Rollback usage rate. Do users appeal autonomy decisions? |

**Key metrics by cell:**
- **Permission Rate:** % of decisions user approved vs. total shown.
- **Rejection Rate:** % user rejected. Healthy = 15–30%.
- **Edit Rate:** % of autonomous outputs user edited post-delivery. Healthy = 15–30%.
- **Undo Rate:** % of reversible decisions user undid. < 5% = healthy.
- **Confidence Calibration:** User accepts 85%+ when system shows 85% confident. User rejects 40%+ when system shows 50% confident.

### Navigation by Product Type

Different product categories have different starting points on the trust ladder and different safe maximum autonomy levels:

| Product Type | Starting Autonomy | Safe Maximum (6 months) | Key Constraint | Rejection Rate Benchmark |
|---|---|---|---|---|
| Consumer creative tools (writing, design) | Level 2 (suggest with preview) | Level 4 (act with undo) | Users expect speed over safety. False positives are worse than false negatives. | 5-15% — users tolerate some bad outputs if recovery is fast |
| Enterprise knowledge work (search, analysis) | Level 1 (show options) | Level 3 (act with approval) | Accuracy matters more than speed. Wrong answers erode trust permanently. | 10-20% — users prefer conservative over confident-and-wrong |
| Financial services (transactions, advice) | Level 0 (inform only) | Level 2 (suggest with confirmation) | Regulatory constraints. Every autonomous action needs audit trail. | 20-30% — high rejection is expected and healthy |
| Healthcare (diagnosis, triage) | Level 0 (inform only) | Level 1 (show options with evidence) | Liability. AI must never be the sole decision-maker for clinical decisions. | 25-40% — rejection signals appropriate caution |
| Legal (contract review, research) | Level 1 (show options) | Level 2 (suggest with citation) | Hallucination is catastrophic. Every output needs source attribution. | 15-25% — lawyers verify everything regardless |
| Customer support (routing, response) | Level 2 (suggest response) | Level 4 (auto-respond for simple) | Simple queries can be automated; complex ones need human. The boundary shifts over time. | 8-15% for simple queries; 30-40% for complex |

### Rejection Rate Benchmarks

The rejection rate — how often users override or dismiss AI suggestions — is your primary trust calibration signal. Target is 15–30% for most products. Here's how that breaks down by product type:

| Product Type | Healthy Range | Under-reliance | Over-reliance |
|---|---|---|---|
| Enterprise finance (audits, forecasting) | 20–35% | >50% | <10% |
| Legal review (contracts, compliance) | 25–40% | >60% | <15% |
| Consumer email / writing assistant | 3–8% | >20% | <1% |
| Internal developer tooling | 10–15% | >30% | <3% |
| Healthcare decision support | 30–50% | >70% | <20% |
| Customer support agent assist | 10–20% | >40% | <5% |
| Code review / suggestion | 15–25% | >45% | <5% |

**Why ranges differ:**
- High-stakes domains (finance, legal, healthcare): You *want* users to check the AI's work. Low rejection = users aren't thinking.
- Low-stakes, high-volume tasks (email writing, consumer features): Users don't need to scrutinize every suggestion. Low rejection is normal.

**How to measure:** Track the ratio of "AI suggestion used as-is" to "AI suggestion modified or dismissed" over a rolling 30-day window per user cohort.

### How to Measure Rejection Rate in Practice

**Event logging pattern:**
```
{
  "event": "ai_output_presented",
  "session_id": "...",
  "output_id": "...",
  "confidence": 0.87,
  "autonomy_level": 2,
  "timestamp": "..."
}
{
  "event": "user_action",
  "output_id": "...",
  "action": "accepted" | "edited" | "rejected" | "regenerated" | "ignored",
  "time_to_action_ms": 3200,
  "timestamp": "..."
}
```

**Computing the rate:**
- Rejection rate = (rejected + regenerated) ÷ total outputs presented
- Acceptance rate = accepted ÷ total outputs presented
- Edit rate = edited ÷ total outputs presented (partial acceptance — the output was useful but wrong)

**Trending:**
- Use 7-day rolling average (not daily — too noisy).
- Alert if rejection rate changes >5 percentage points week-over-week.
- Segment by: autonomy level, user tenure, query complexity, time of day.

### Mental Model Validation Protocol

Before a user depends on AI outputs for consequential decisions, they should understand what the AI gets wrong. This isn't a disclaimer — it's a calibration step.

**The protocol: Show 5 failures before you let users depend.**

Present 5 real examples of the AI being wrong *in the domain the user will use it for* during onboarding or during the first week of use. Not edge cases — representative failures.

**Why this works:**
- Users who see failures first are better calibrated than users who discover failures on their own.
- Seeing a failure in a safe environment (training, onboarding) is less damaging than discovering it in a live situation.
- It sets the right prior: "This AI is useful AND fallible." Both parts of that sentence matter.

**Implementation:**
1. During onboarding: "Here are 3 examples where this AI got it wrong. Notice what they have in common."
2. First week: Surface 2 low-stakes errors with annotations: "The AI said X, but the correct answer was Y. Here's why this happens."
3. Optional: Build a "known limitations" page that's easy to find (not buried in help docs).

**The test:** Before a user hits the high-autonomy stage of the trust ladder, can they answer: "What's the one type of question where I should double-check this AI's answer?" If they can't answer, they're not ready for high-autonomy use.

### Failure Presentation Template

For each of the 5 representative failures shown to users before they advance to higher autonomy:

**Failure Card Format:**
1. **The scenario** (1-2 sentences): What the user asked and what context the AI had.
2. **What the AI did** (1 sentence): The action or output the AI produced.
3. **What went wrong** (1 sentence): The specific error — hallucination, wrong context, outdated information, misunderstood intent.
4. **How to catch it** (1 sentence): The signal the user should look for to detect this class of error.
5. **What the user should do** (1 sentence): The correct recovery action.

**How to select the 5 representative failures:**
- 1 from the most common failure mode (highest frequency)
- 1 from the most dangerous failure mode (highest consequence)
- 1 that is subtle (AI output looks correct but isn't)
- 1 that is obvious (AI clearly wrong — builds calibration that AI does fail)
- 1 from the user's specific domain or use case

**Validation checklist — user passes when they can:**
- [ ] Identify what went wrong in 3 of 5 failure cards without hints
- [ ] Describe the correct recovery action for 4 of 5 failures
- [ ] Articulate one category of error they'd watch for in their own work

**Step 6: Over-Reliance Detection (Covered in Calibration Table)**
- This step is now integrated into the Trust-Autonomy Calibration Table above.
- Key metric: If user rejection rate < 5%, they're over-reliant. Intervene.

**Step 7: Enterprise Trust Equation**
- Enterprise buyers evaluate trust differently: **Trust = (Reliability × Transparency × Compliance) / (Risk of Embarrassment)**
- The denominator dominates. Enterprise doesn't care if your AI is 99.9% reliable if a 0.1% failure gets the CRO fired in front of the board.
- Design for: Audit trails (who approved what), rollback capability, compliance documentation, "I'm uncertain" displays, permission trails.
- Enterprise over-reliance is *worse* than consumer because the consequence magnitude is larger.

## REALITY CHECK

**Failure: Over-Asking**
Ask permission for everything. Users fatigue and click yes without reading. Now the AI is *more* autonomous (because users aren't paying attention), but you have no visibility.
- Prevention: Only ask for reversible/irreversible. Autonomous for trivial.

**Failure: Over-Reliance**
Users stop checking. AI fails on a reversible action. Users lose money because they'd learned to trust without verification.
- Prevention: Monitor rejection rate. Force permission on high-stakes even if user is Level 4. Show confidence scores. Introduce doubt.

**Failure: Mental Model Debt**
User thinks AI is deterministic. It's not. Trust breaks catastrophically when reality doesn't match expectation.
- Prevention: Show failure examples early. Document what the AI will/won't do. Test user understanding directly.

**Failure: Expectation Debt**
Marketing says "AI handles your entire approval workflow." Product only handles 60%. Enterprise buyer feels deceived.
- Prevention: Align marketing claims with actual capability boundaries. Be specific about what triggers the "ask human" path.

**Failure: No Trust Repair Path**
AI makes a mistake. You say "sorry" but don't change anything. User trust moves from 4 → 2 and stays there.
- Prevention: Design error acknowledgment and recovery into the product, not the support team.

## QUALITY GATE

Before shipping:

1. **Severity Mapped:** All failure modes identified and categorized?
2. **Mental Model Validated:** User's understanding of AI capability matches reality? (Test it.)
3. **Confidence Display:** Every recommendation shows confidence + reasoning?
4. **Permission UX Complete:** Action + reasoning + cost + alternatives + refusal?
5. **Over-Reliance Metrics:** Can you detect when rejection rate < 5% and respond?
6. **Trust Repair Designed:** What happens after a visible failure? Built in, not a support ticket?
7. **Enterprise Audit Trail:** Can you show the approval decision, the reasoning, who approved, when? (For enterprise, this is non-negotiable.)

## KEY PRACTITIONER QUESTIONS

- "What's the user rejection rate right now? If it's > 95% or < 5%, something's wrong." (Not a bug. A design signal.)
- "If the AI fails here, does the user's mental model predict that failure? Or does trust collapse because reality didn't match expectation?"
- "Are we designing for calibrated trust (users still thinking) or maximum trust (users stopped checking)?"
- "What's our trust repair story after a visible mistake?"
- "For enterprise: Can we audit every decision that was made autonomously vs. asked for permission?"

## WHEN WRONG

This skill gives bad advice if:
- Failure severity changes at runtime. (Rerun analysis.)
- You can't detect user trust level. (Ask directly. Don't guess.)
- Mental models are misaligned and you skip transparency design. (Build the model first.)
- Over-reliance fires but you have no autonomy-blocking mechanism. (Design for it upfront.)
- Regulatory requirements override the ladder. (HIPAA requires approval for all medical decisions. Accept.)
- Trust is domain-specific. (User trusts AI on emails, not money. Use separate ladders per domain.)
- You measure trust by "did the user accept this?" (Wrong metric. Measure by "is the user still thinking?")

---

## TRADE-OFF LEDGER

Complete the Trade-Off Ledger from the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md), Section 3.

## CONCLUSION

Follow the Conclusion Protocol from the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md), Section 5:
1. State the recommendation
2. Name the key trade-off
3. Acknowledge the biggest risk
4. Define the next action

---

## VISUAL SUMMARY

After completing the primary output, invoke the **excalidraw-svg** skill to create a single Excalidraw SVG visual summary. This diagram captures the essence of the analysis in one glanceable image — making the deliverable 10x more impactful. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.
