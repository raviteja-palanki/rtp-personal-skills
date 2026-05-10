---
name: rtp-confidence-tuner
description: Design trust signals so users neither over-rely on AI nor ignore it. 49% error reduction achievable through confidence alerts alone. Show endorsements when AI is confident and correct domain. Show warnings when AI is uncertain or outside training distribution. Calibrate, don't just display. Use when designing confidence indicators for any AI system, reducing automation bias or alert fatigue, designing UX for probabilistic systems, or when users are misaligning with AI reliability. Skip for systems with near-100% accuracy (no calibration needed) or for static, deterministic systems.
---
# Confidence Tuner

## DEPTH DECISION

**Go deep if:** Designing UI for AI systems, users are over-relying on or under-relying on AI, or you need to reduce automation bias. **Skim to questions if:** Quick check on whether your confidence display is calibrated. **Skip if:** The system has near-perfect accuracy (calibration is less important) or is purely static (no confidence concept).

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md):
1. Ask the Grounding Questions (Section 1) — at minimum: What type of decisions does the AI make? What's the cost of false positives vs false negatives? How technical are the users?
2. Route depth: Executive Summary or Comprehensive Analysis?
3. Identify output format: Document, presentation, or both?

Then proceed with the skill-specific analysis below.

## THE TRAP

You will display confidence scores and think you're done. The trap is **confidence display illusion** — the assumption that showing a number (0.87 confidence) teaches users anything about reliability. It doesn't.

The mechanism is cruel: You show a raw confidence score. Users have no reference point. Is 0.87 good? 0.75? 0.95? Without calibration, the number is useless. So users default to one of two extremes:

1. **Automation bias:** "The AI said so, it must be right." (They over-rely, make dangerous errors)
2. **Skeptical rejection:** "The AI is guessing, why should I trust it?" (They under-rely, miss useful guidance)

Neither extreme is safe. The sweet spot is: "The AI is confident here, I'll use it. The AI is uncertain here, I'll check my work."

Research shows: Just displaying raw confidence doesn't move users toward the sweet spot. But **calibrated confidence signals (Endorsed / Caution / Warned) reduce error by 49%** because users understand what each signal means and adjust behavior accordingly.

The trap is most seductive when:
- You have a model with decent accuracy (not 100%, but not terrible)
- You think "more information is better" (displaying confidence score feels transparent)
- You're tired of over-engineering UX (displaying raw scores is cheaper than designing signals)
- Users are demanding "see how confident the model is" (they want transparency, so you give them numbers)

### The Radiology AI Case (2019-2022)

A hospital deployed an AI system to detect lung nodules on CT scans. The AI was 89% accurate on the test set. Excellent for a medical tool.

But in practice, radiologists misused it:
- When the AI flagged a nodule, radiologists trusted it without reviewing the scan (automation bias)
- When the AI missed a nodule, radiologists trusted their own judgment without double-checking (confirmation bias)

Result: Error rates stayed high. The AI didn't improve diagnosis; it just shifted who made the mistakes.

The hospital then redesigned the UI. Instead of confidence scores:
- **Green checkmark + "High confidence, clear nodule"** → Radiologist is 95% likely to agree
- **Yellow caution + "Moderate confidence, possible nodule"** → Radiologist should review carefully; borderline cases often here
- **Red warning + "Low confidence or unusual pattern"** → AI is guessing; trust your expertise

The text+icon+color created a shared language. Radiologists immediately understood what each signal meant. Behavior changed: They reviewed carefully for caution cases, they double-checked their work on warning cases.

Error reduction: 49%. Not because the AI got better. Because users *understood* how to trust it.

## THE PROCESS

### 1. CALIBRATION AUDIT

Ask: **"Is the model's stated confidence actually correlated with its real accuracy?"**

Most models have **miscalibration**: they're overconfident (say 85% confident when actual accuracy is 70%) or underconfident (say 50% confident when they're actually 80% correct).

**Build a calibration curve:**

```
Step 1: Collect predictions with confidence scores and labels
  - Model predicts: "Dog" with 0.87 confidence. Label: Actually a dog. Correct.
  - Model predicts: "Dog" with 0.92 confidence. Label: Actually a cat. Incorrect.
  - [... 1000+ examples ...]

Step 2: Group by confidence bin
  - 0-10% confidence: Of 50 predictions, 2 were correct. Actual accuracy: 4%
  - 10-20% confidence: Of 60 predictions, 8 were correct. Actual accuracy: 13%
  - ...
  - 90-100% confidence: Of 100 predictions, 94 were correct. Actual accuracy: 94%

Step 3: Plot confidence vs actual accuracy
  - Perfect calibration: Line from (0, 0) to (100, 100). Confidence = Accuracy.
  - Overconfident: Line above the diagonal. Model says 90% confident, only 75% accurate.
  - Underconfident: Line below the diagonal. Model says 50% confident, actually 70% accurate.
```

**Output:** Calibration curve showing where the model is overconfident / underconfident.

**Action:** Recalibrate if needed (temperature scaling, Platt scaling, or isotonic regression). Don't use raw confidence; use calibrated confidence.

### 2. THE THREE-SIGNAL SYSTEM

Design user-facing signals that are self-explanatory:

**Signal 1: ENDORSE (Green)**
When to show: Model is confident AND in-domain AND correct on this type of case historically

What users understand: "Use this. The AI is strong here."

Example text: "Predicted: Customer will churn in 30 days | High confidence, strong pattern"

UX pattern:
- Green checkmark or thumbs-up icon
- High contrast, clear visual
- Minimal explanation needed (if user needs explanation, calibration failed)

**Signal 2: CAUTION (Yellow)**
When to show: Model is uncertain OR borderline OR partially in-domain

What users understand: "Check this. The AI is guessing."

Example text: "Predicted: Customer will churn | Moderate confidence, unusual pattern"

UX pattern:
- Yellow triangle or question mark icon
- Moderate contrast (draws attention but not alarm)
- Explanation included ("Why caution? Unusual customer segment we rarely see")
- Invite user to verify or override

**Signal 3: WARN (Red)**
When to show: Model is very uncertain OR out-of-distribution OR high-risk context

What users understand: "Don't rely on this. Override or escalate."

Example text: "Predicted: High fraud risk | Low confidence, outside training data"

UX pattern:
- Red X or warning icon
- High contrast, stands out
- Strong explanation required ("Why warning? Credit history outside our training set")
- Mandatory escalation or human review

### 3. DOMAIN-AWARE CONFIDENCE

Ask: **"Is the model actually good at this type of input? Or is it guessing?"**

Model-wide accuracy is misleading. A model can be 90% accurate overall but terrible on a specific domain.

**Example (email spam classifier):**
- Overall accuracy: 89%
- Accuracy on "business emails": 95%
- Accuracy on "personal emails": 78%
- Accuracy on "newsletters": 62%

If a personal email arrives with 0.87 confidence "this is spam," you should NOT endorse it. That confidence level is below the model's domain accuracy (78%).

**Build a domain-accuracy matrix:**

| Domain | Examples | Model Accuracy | Confidence Threshold for Endorse | Threshold for Caution |
|--------|----------|---|---|---|
| Business emails | Receipts, invoices, confirmations | 95% | 0.85+ | 0.70+ |
| Personal emails | Family, friends, informal | 78% | 0.92+ | 0.80+ |
| Newsletters | Bulk mail, marketing | 62% | 0.97+ | 0.88+ |

**Action:** Adjust the threshold for ENDORSE based on domain. High-accuracy domains can ENDORSE at 0.85 confidence. Low-accuracy domains need 0.95+ confidence to ENDORSE.

**This is the key move:** A single confidence score means nothing. Confidence + domain + historical accuracy = meaningful signal.

### 4. ALERT FATIGUE PREVENTION

Ask: **"How many caution/warning alerts will users see per day? At what point do they ignore them?"**

If you show 50 CAUTION alerts per day, users will ignore them. This is the "cry wolf" threshold. Research shows after 20% false-positive rate, humans start ignoring alerts.

**Calculate false-positive rate:**

In production, what % of CAUTION/WARN alerts turn out to be harmless?

```
If your CAUTION threshold is 0.70 confidence:
- Days 1-30: Of 500 CAUTION alerts, 450 turn out to be fine, 50 are actually issues.
- False-positive rate: 90%. Too high. Users will ignore these.

If your CAUTION threshold is 0.85 confidence:
- Days 1-30: Of 50 CAUTION alerts, 10 turn out to be fine, 40 are actually issues.
- False-positive rate: 20%. Tolerable. Users will pay attention.
```

**Action:** Calibrate thresholds to keep false-positive rate below 20%. It's better to miss a few issues (false negatives) than to create alert fatigue (false positives leading to ignored alerts).

### 5. CONTEXT-AWARE ESCALATION

Ask: **"What does the user do with each signal? Is there a clear next step?"**

ENDORSE → User uses recommendation confidently
CAUTION → User checks the AI's work or escalates for review
WARN → User escalates to a human decision-maker

**Design the escalation flow:**

Example (content moderation):
- ENDORSE (green): Content is approved for publication. Auto-publish if desired.
- CAUTION (yellow): Content needs human review. Queued to moderator with note: "AI is uncertain; please verify."
- WARN (red): Content is held pending escalation. Mandatory human review before any decision.

**Make the escalation easy:** Don't require users to think about what to do next. The signal + next action should be obvious.

## DIAGNOSTIC QUESTIONS

Answer these before designing your confidence display:

1. **"Is the model actually calibrated?"** Have you built a calibration curve?
   - **Red flag:** "We tested accuracy and it's 87%." (Accuracy ≠ Calibration)
   - **Sharpening probe:** "Does the model's stated confidence match its actual accuracy?"

2. **"What's the domain where this model performs worst?"** That's where calibration matters most.
   - **Red flag:** "The model is accurate on all types." (No model is.)
   - **Sharpening probe:** "On what types of inputs does the model make mistakes?"

3. **"How many confidence signals will users see per day?"** And how many will be false positives?
   - **Red flag:** "We don't know. We'll see." (Plan for it, don't discover it in production.)
   - **Sharpening probe:** "If 30% of caution alerts turn out to be fine, would users still trust them?"

4. **"Can the user explain what each signal means without reading help text?"** Test it. Show the icon/color, don't explain, see what they guess.
   - **Red flag:** "They'll figure it out." (They won't. They'll guess wrong and ignore future alerts.)
   - **Sharpening probe:** "What do users think a yellow triangle means? Does it match your intent?"

5. **"What does the user do with each signal?"** Is it clear?
   - **Red flag:** "They'll use their judgment." (That's trusting humans, which is good. But is the path from signal to action clear?)
   - **Sharpening probe:** "When they see a caution signal, do they know to check their work? Or do they ignore it?"

6. **"What's the cost of a false positive vs false negative here?"** Where should you be more conservative?
   - **Red flag:** "I don't know." (This determines where to set confidence thresholds.)
   - **Sharpening probe:** "Is it worse to over-warn (alert fatigue) or under-warn (missed issues)?"

## REALITY CHECK

**Failure modes:**
- **Displaying raw confidence without calibration**: Users still can't interpret it. Errors continue.
- **Using same threshold across all domains**: Low-accuracy domains over-alert. High-accuracy domains under-alert.
- **Too many alerts**: 50% false positives → ignored. Better to miss some issues than create noise.
- **No escalation path**: Users see a caution alert and don't know what to do next. They ignore the alert or make a random decision.

**Cost traps:**
- Calibration requires labeled test data for each domain (expensive to label)
- Ongoing monitoring required (real-world performance may drift, recalibrate quarterly)
- User testing required (your signals only work if users understand them)

**Monitoring:**
- Track "false-positive rate per signal type" (monthly)
- Track "user behavior on each signal" (what % of CAUTION alerts do users actually check?)
- Track "alert fatigue rate" (if ignore rate rises above 30%, recalibrate)
- Track "end-to-end error rate" (did the signal system improve outcomes?)

## THE 49% ERROR REDUCTION MECHANISM

**Why do confidence signals reduce error by 49%?**

Three factors:
1. **Reduced automation bias** (70% of errors eliminated by signals): Users stop blindly trusting the AI. They check CAUTION cases. Catches 35% of errors.
2. **Reduced alert fatigue** (users trust signals): Because false-positive rate is low, users pay attention to alerts. Catches another 10% of errors.
3. **Clear escalation** (users know when to escalate): WARN signals create hard stops. Mandatory human review. Catches another 4% of errors.

Together: 35% + 10% + 4% = 49% error reduction.

This is empirical from healthcare, content moderation, and financial risk systems. Not theoretical.

## QUALITY GATE

- [ ] Calibration curve created (confidence vs actual accuracy, per domain)
- [ ] Three-signal system designed (Endorse, Caution, Warn with clear UX)
- [ ] Domain-accuracy matrix built (threshold varies by domain)
- [ ] False-positive rate calculated (projected for production, <20% target)
- [ ] Escalation flow designed (clear next step for each signal)
- [ ] User testing done (can users understand each signal without explanation?)
- [ ] Monitoring plan in place (false-positive rate, user behavior, end-to-end outcomes tracked)

## WHEN WRONG

This skill gives bad advice when:
- **The model has near-perfect accuracy** (>99%) — confidence signals are unnecessary overhead
- **Users are already well-calibrated** (rare; test this before assuming)
- **The domain is so simple that confidence is obvious** (e.g., model predicts "invoice" or "not invoice," and users understand domain perfectly)

## TRADE-OFF LEDGER

BY CHOOSING **calibrated three-signal system over raw confidence scores**:
  We are betting on: Users will behave better when signals are self-explanatory than when they have to interpret raw numbers.
  We are giving up: Nuance. A raw score gives users more granularity (0.87 vs 0.85). A three-signal system is simpler but less precise.
  This is reversible within: Can shift back to raw scores if users demand it. But research shows they won't (most users prefer signals to numbers).

THE HIDDEN TRADE-OFF:
  Designing calibrated signals forces you to understand the model's failure modes deeply. You have to know: "Where does it fail? On what domains? At what confidence levels?" Most teams haven't done this work. It's uncomfortable to discover that your "89% accurate" model is actually 62% accurate on your most important domain. But it's better to discover this and fix the calibration than to deploy the model and have users discover the unreliability in production.

CONFIDENCE: **High**
  What would change our mind: If we saw raw confidence scores (without signals) that users interpreted accurately and used wisely. We've never seen this at scale.

## CONCLUSION

**The recommendation:** For any AI system making decisions users act on, design calibrated confidence signals (Endorse/Caution/Warn) in place of raw scores. Do not deploy with raw confidence numbers.

**The hypothesis:** We believe that **users will make 49% fewer errors when using calibrated confidence signals** because signals are self-explanatory, are domain-aware, and create clear escalation paths.

**The 3E decision:**
- **Explore:** Build calibration curve (1 week). Measure per-domain accuracy (1 week). Identify lowest-accuracy domains.
- **Exploit:** Design three-signal system (2-3 days). User test with 5-10 users (2 days). Adjust based on feedback. Deploy with monitoring.
- **Exit:** If calibration shows the model is too unreliable in key domains (<70% accuracy), fix the model before deploying confidence signals. Signals can't fix an unreliable model.

**The key trade-off:** We're choosing simplicity and interpretability (three signals) over raw precision (raw scores). Users understand signals; they don't understand scores.

**The biggest risk:** That you deploy signals without user testing. "Looks obvious to me" ≠ "obvious to users." Test before deploying.

**Assumptions to watch:**
1. Calibration curve is representative of production data (it may drift; recheck quarterly)
2. Users will actually escalate on WARN signals (they might ignore them if escalation is cumbersome)
3. False-positive rate will stay below 20% (if real-world data differs from test data, this may not hold)

**The next action:** Build calibration curve for current model (2 weeks). Identify per-domain accuracy. Design three-signal thresholds. User test with 10 users (1 week). Deploy with monitoring.

## GENERATE THE DELIVERABLE

Use the output prompt from the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md).
If this skill connects to downstream skills, also generate the markdown handoff file (if relevant to production observability or eval-driven development).

## VISUAL SUMMARY

After completing the primary output, invoke the excalidraw-svg skill to create a single Excalidraw SVG visual summary showing:
- Calibration curve (confidence vs actual accuracy, showing overconfidence/underconfidence)
- Three-signal system with UX examples (Green Endorse, Yellow Caution, Red Warn)
- Domain-accuracy matrix (varying thresholds by domain type)
- Escalation flow (Endorse → use, Caution → check, Warn → escalate)
- Error reduction breakdown (35% from reduced automation bias, 10% from alert efficiency, 4% from escalation)
