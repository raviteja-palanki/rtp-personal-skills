---
name: rtp-confidence-tuner
description: 'Calibrate confidence at both layers of the AI stack — the model''s confidence shown to the USER (trust calibration: Endorse/Caution/Warn so users neither over-rely nor ignore the AI), and the JUDGE''s confidence behind an eval score (TPR/TNR/kappa, so an automated evaluator can be trusted). Same discipline — does a stated confidence track truth? — at two layers, and the judge layer sits upstream: you can''t honestly calibrate a user''s trust on top of an unvalidated scoreboard. Use when designing confidence signals, reducing automation bias, validating an LLM-as-judge before relying on it, setting auto-approve vs send-to-human thresholds, or debugging why a green dashboard ships red product. Pairs with: eval-framework, ai-product-metrics, trust-ladder, production-observability, prompt-as-product. Triggers: "confidence signal", "trust calibration", "LLM as judge", "TPR TNR", "automation bias", "auto-approve threshold".'
imports: [trust-ladder, eval-framework, ai-product-metrics]
---

# Confidence Tuner

## DEPTH DECISION

**Go deep if:** Designing UI for AI systems, users are over-relying on or under-relying on AI, or you need to reduce automation bias. **Skim to questions if:** Quick check on whether your confidence display is calibrated. **Skip if:** The system has near-perfect accuracy (calibration is less important) or is purely static (no confidence concept).

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md):
1. Ask the Grounding Questions (Section 1) — at minimum: What type of decisions does the AI make? What's the cost of false positives vs false negatives? How technical are the users?
2. Route depth: Executive Summary or Comprehensive Analysis?
3. Identify output format: Document, presentation, or both?

Then proceed with the skill-specific analysis below.

## THE ONE IDEA

**Calibration is a single discipline — *does a stated confidence signal actually track truth?* — and it runs at two layers of the AI stack. Get the layers backwards and everything downstream is theater.**

| | **Layer 1 — Model → User** | **Layer 2 — Judge → Eval pipeline** |
|---|---|---|
| Whose confidence? | The model's, shown to the user | The AI judge's verdict behind an eval score |
| Checked against what "truth"? | Real outcomes / labeled data | Human-expert labels |
| Who gets hurt when it's wrong? | The human (automation bias, or skeptical rejection) | The whole team — you optimize toward a lying scoreboard and ship green-dashboard/red-reality |
| The instrument | Calibration curve → Endorse/Caution/Warn | TPR / TNR / Cohen's kappa → bias-corrected scores |

**The non-obvious part — Layer 2 is upstream of Layer 1.** The acceptance rate, accuracy, and quality numbers you'd use to *build* a user-facing confidence signal are themselves produced by the judge. If the judge is uncalibrated, those numbers are fiction — and a beautifully designed Endorse/Caution/Warn badge just paints fiction green. **Order of operations: validate the judge (Layer 2) before you design the user's trust signal (Layer 1).** Most teams do the opposite — they ship pretty confidence UI resting on a scoreboard nobody ever checked against a known weight.

This skill's original content (below) is the mature, worked treatment of **Layer 1**. The section **"Layer 2 — Calibrating the Judge"** adds the layer that has to come first. Read Layer 2 first if you have an automated evaluator; read Layer 1 first if a human sees every output.

**Calibrate proportionally.** The bar is not uniform — it scales with autonomy and consequence. A Level 1–3 suggestion tool (a human reviews every output) tolerates a looser judge and simpler signals. A Level 5–7 agent that *acts before anyone looks* needs fail-case TPR above 0.90 on safety-critical failures. Don't over-engineer calibration for a low-stakes autocomplete; don't under-engineer it for an autonomous agent. (This is the `trust-ladder` / `autonomy-spectrum` link, made concrete.)

---

# LAYER 1 — CALIBRATING THE USER'S TRUST (Model → User)

*The model emits a confidence; the user has to know how much to trust it. This is the layer most teams reach for first — and it only works if the numbers underneath it have already been validated at Layer 2.*

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

---

# LAYER 2 — CALIBRATING THE JUDGE (before you calibrate the user)

*If any number on your dashboard — accuracy, acceptance rate, pass rate — is produced by an AI judge rather than by a human or a deterministic check, then that judge is the instrument every Layer 1 signal rests on. An uncalibrated judge means every confidence badge above it is confidently wrong.*

### The judge is a measurement instrument, not a truth source

An LLM judge that produces a score is a bathroom scale you have never checked against a known weight. You don't trust a scale because it shows a number; you trust it because you've verified it against a known weight and you know its bias. Same with a judge: the question is never *"does the judge work?"* — it's *"do I know **how** it fails?"* A scale that reads three pounds light on every measurement is usable (correct for the bias). A scale that drifts randomly is worthless. A scale you never check is dangerous precisely because it *usually seems about right*.

### Measure TPR and TNR separately — never "agreement %"

The single most common judge mistake is reporting one number: *"our judge agrees with humans 88% of the time."* That number is a vanity metric whenever failures are rare. If 5% of outputs are bad, a judge that rubber-stamps *everything* scores 95% agreement while catching zero real failures.

Split it into two rates — the smoke-detector test:

- **True Positive Rate (TPR)** — when there *is* a real failure, how often does the judge catch it? *Does the alarm beep when there's actual fire?* **This is the metric that protects users.**
- **True Negative Rate (TNR)** — when the output is actually good, how often does the judge correctly pass it? *Does the alarm stay quiet when you're just cooking?* Low TNR = false alarms = engineers investigate non-issues and eventually rip the batteries out (stop trusting the dashboard).

The failure mode is documented and systematic: recent research finds LLM judges can identify *valid* outputs at **TPR > 96% while catching *invalid* ones at TNR < 25%** — an "agreeableness bias" that inflates apparent reliability in exactly the class-imbalanced setting real products live in. An 88%-agreement judge with fail-case TPR of 0.65 is missing a third of the failures that could become a compliance incident. *The dashboard says green; the product leaks risk.*

Add **Cohen's kappa** — chance-corrected agreement — as the headline. Human-human kappa on hard rubrics averages ~0.80; a judge above ~0.75 is trustworthy for release decisions on a narrow workflow, below ~0.40 is noise dressed as signal. *(Tier: TPR>96%/TNR<25% and kappa benchmarks are ⚠ research-reported, not universal constants — measure your own; the asymmetry is the durable lesson.)*

### Correct the raw scores by the judge's known error

Once you know the judge's TPR and TNR from a labeled test set, you can *correct* the pass rate it reports on unlabeled production traffic. If the judge is systematically 10% too lenient on safety, the corrected estimate accounts for that. The `judgy`-style bias correction is the operational move: you don't need a perfect judge, you need a judge whose bias you've *measured* — then you subtract it. This is the scale that reads three pounds light: usable, because you know by how much.

### The five-step calibration workflow

None of this needs ML expertise — it needs domain knowledge, labeled examples, and discipline:

1. **Build a calibration set** — 300–400 production examples across the full quality spectrum, *including the ambiguous cases near the pass/fail boundary* (that's where judges break). Domain experts label each. This is the golden dataset for your *judge*. Split: ~200 train / 100 test / 100 held back for periodic re-checks.
2. **Run the judge against the test split** — now you have two parallel labels per case: human and judge.
3. **Compute the confusion matrix** — TP/TN/FP/FN → TPR and TNR, sliced by the failure types that would block shipment.
4. **Correct for judge error** on unlabeled traffic (the bias correction above).
5. **Monitor and recalibrate** — track judge-human agreement over time; recalibrate when the product changes, the rubric changes, or **the judge model changes**.

### New judge model = new instrument

The trap that makes teams debug the wrong thing: you upgrade the judge model (cheaper, faster) and the pass rate drops seven points. You assume the *product* regressed. It didn't — the *judge* got stricter on tone and more lenient on missing caveats. This is non-determinism applied to the evaluator itself. **Rule: new judge model, new calibration.** Dual-run old and new judges on a frozen calibration set, review the disagreement clusters, and only cut over when the new judge clears your TPR/TNR bar on the slices that matter.

### The judge's own biases — probe for them by name

A judge carries systematic biases that raw agreement hides. Probe each explicitly:

- **Verbosity bias** — longer answers score higher regardless of quality.
- **Position / swap bias** — in pairwise comparisons the first (or second) option is favored; check *swap consistency* (reverse the order — does the verdict flip?).
- **Self-preference / family bias** — the judge favors outputs from its own model family. This nearly makes teams pick the wrong generator model. Not measuring it is now sloppy.
- **Domain blindness** — the legal-tech judge that scored contract summaries "complete" while every one silently omitted the indemnification clause. It could spot *wrong* information but not *missing* information. The fix was decomposing "complete" into commercial / risk-disclosure / obligation completeness — recall on omitted liability clauses jumped 0.41 → 0.89.

### Grader-hacking is the calibration killer — assume it

A calibrated judge is calibrated *as of the last check, against a static distribution*. The moment the judge's verdict becomes a target — the generator is optimized to please it — calibration decays. This isn't hypothetical: research shows a bare *"Thought process:"* prefix or even punctuation-only responses can push judges to **35–90% false-positive rates**, and benign wrappers that leave harmful text untouched flip judges 57–100% of the time. Goodhart's law, live: *when the measure becomes the target it stops being a good measure.* Consequence: calibration is a maintained instrument, not a one-time gate. Re-validate on a fresh, adversarially-seeded set on a schedule — and treat the judge prompt as a versioned artifact (`prompt-as-product`), because a five-word change to it silently re-scores your entire history.

### Threshold calibration: auto-approve vs. send-to-human (HITL vs. HOTL)

The judge's confidence also sets *where the human enters*. This is a product decision on two axes — **risk × volume**:

- **Human-in-the-loop (HITL)** — synchronous; a human approves before the action lands. For low-volume, high-consequence work (a $2M contract clause, a clinical flag). The judge routes; the human decides.
- **Human-on-the-loop (HOTL)** — asynchronous audit; the system acts, humans sample and correct after. For high-volume, lower-consequence work (tagging support tickets). The judge auto-approves above a threshold; humans audit a sample and feed corrections back into recalibration.

Set the auto-approve threshold too low and you drown the humans (alert fatigue, Layer-1 problem); too high and failures ship. The threshold is not a constant — it moves with the judge's measured TNR and the consequence of the miss.

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

**Layer 2 (the judge behind your numbers):**

7. **"Is any number on your dashboard produced by an AI judge — and have you checked its fail-case TPR?"**
   - **Red flag:** "Our judge agrees with humans 88% of the time." (Agreement % is a vanity metric when failures are rare. Ask for TPR and TNR separately.)
   - **Sharpening probe:** "When there's a *real* failure, what fraction does the judge catch? What's your kappa?"

8. **"When did you last recalibrate — and did the judge model change since?"**
   - **Red flag:** "We upgraded the judge model last month; pass rate dropped, so the product must have regressed." (New judge = new instrument. You may be debugging the product for the judge's drift.)
   - **Sharpening probe:** "Have you dual-run old vs. new judge on a frozen calibration set?"

9. **"Have you probed the judge for verbosity, position, self-preference, and grader-hacking?"**
   - **Red flag:** "The judge is an LLM, it's objective." (It carries systematic biases; a bare 'Thought process:' prefix can spike its false-positive rate.)
   - **Sharpening probe:** "Does the verdict flip when you swap candidate order? Does it favor its own model family?"

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

*(Evidence tier: the 49% headline and its 35/10/4 decomposition are ⚠ practitioner/illustrative — a directional pattern drawn from calibrated-alert studies in healthcare, content moderation, and financial risk, not a single audited number you can cite. Use it to motivate the design, not as a promised outcome. Measure your own error-reduction against your own baseline.)*

## QUALITY GATE

**Layer 1 — user trust:**
- [ ] Calibration curve created (confidence vs actual accuracy, per domain)
- [ ] Three-signal system designed (Endorse, Caution, Warn with clear UX)
- [ ] Domain-accuracy matrix built (threshold varies by domain)
- [ ] False-positive rate calculated (projected for production, <20% target)
- [ ] Escalation flow designed (clear next step for each signal)
- [ ] User testing done (can users understand each signal without explanation?)
- [ ] Monitoring plan in place (false-positive rate, user behavior, end-to-end outcomes tracked)

**Layer 2 — judge trust (do these FIRST if any dashboard number comes from an AI judge):**
- [ ] Judge validated on a labeled calibration set (300–400 cases incl. boundary cases)
- [ ] TPR and TNR reported *separately* on the failure slices that block shipment (not just "agreement %")
- [ ] Cohen's kappa computed (>0.75 for release decisions on a narrow workflow)
- [ ] Judge bias probed (verbosity, position/swap-consistency, self-preference/family)
- [ ] Raw scores bias-corrected by the judge's known TPR/TNR (judgy-style)
- [ ] Recalibration cadence set + judge prompt version-controlled; dual-run on any judge-model change

## WHEN WRONG

This skill gives bad advice when:
- **The model has near-perfect accuracy** (>99%) — confidence signals are unnecessary overhead
- **Users are already well-calibrated** (rare; test this before assuming)
- **The domain is so simple that confidence is obvious** (e.g., model predicts "invoice" or "not invoice," and users understand domain perfectly)

**Where the two-layer framing itself breaks (be honest about the edges):**
- **No AI judge in the loop.** If your evals are pure human review or deterministic checks, Layer 2 collapses to inter-rater reliability / test correctness — the *judge-bias* content (verbosity, self-preference, grader-hacking) doesn't apply, though the calibration discipline still does.
- **The model exposes no usable confidence signal.** Many models don't, or their logprobs are meaningless for the task. Then Layer 1 needs a *proxy* confidence (an auxiliary estimator, or the judge's own confidence) — which makes Layer 1 depend on Layer 2 even more directly. Don't fake a calibration curve from numbers that don't mean anything.
- **Treating calibration as a one-time gate.** The most expensive error: calibrate once, ship, and assume the number holds. Grader-hacking and distribution drift decay it silently. If you can't commit to a recalibration cadence, don't build decisions on the judge that require high calibration — lower the autonomy instead.

## WHERE THIS MEETS YOUR STACK

Calibration is a diagnosis-and-trust layer; it hands off in both directions. The routing:

- **An uncalibrated judge makes every downstream number suspect → `ai-product-metrics` and `eval-framework`.** The acceptance rate, pass rate, and quality scores those skills report are only as honest as the judge behind them. Calibrate the judge here *first*; then those dashboards mean something. This is the upstream dependency the one-idea spine names.
- **The calibration bar is set by autonomy and consequence → `trust-ladder` / `autonomy-spectrum` / `agent-risk`.** How much TPR you need, and whether a human sits in-the-loop or on-the-loop, is a function of how much the system can do before anyone looks. Don't set the bar here in isolation.
- **The judge prompt is a versioned artifact → `prompt-as-product`.** A five-word change to the judge silently re-scores your entire history. Version it, diff it, and re-run calibration on any change — the same discipline you'd apply to a production prompt.
- **Calibration decays; catch the decay in production → `production-observability`.** Monitor judge-human agreement over time as a first-class metric (not just latency/cost). A drop in agreement is drift or grader-hacking; it should page someone.
- **The calibration set is a moat → `moat-finder` / `feedback-flywheel`.** Competitors install the same eval framework in an afternoon; they can't replicate the 300–400 expert-argued edge cases you labeled. Route production disagreements back into the set (the flywheel) so the moat compounds.
- **Threshold → who acts → `tool-architecture`.** Where the auto-approve line sits is also a permissions decision: what the system is allowed to do unsupervised above that confidence is a consequence-gating question, not just a UX one.

The spine: **Layer 2 makes the numbers trustworthy; Layer 1 makes the user trust them correctly; the rest of the stack decides how much to bet on that trust.** Never let a confidence signal — user-facing or judge — go unvalidated and then get treated as truth.

---

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

**The recommendation:** For any AI system making decisions users act on, design calibrated confidence signals (Endorse/Caution/Warn) in place of raw scores. Do not deploy with raw confidence numbers. And if any number feeding those signals comes from an AI judge, calibrate the judge (Layer 2: TPR/TNR/kappa) *before* you design the user signal — a confidence badge resting on an unvalidated scoreboard is worse than no badge, because it manufactures false trust.

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

Use the output prompt from the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md).
If this skill connects to downstream skills, also generate the markdown handoff file (if relevant to production observability or eval-driven development).

## VISUAL SUMMARY

After completing the primary output, invoke the excalidraw-svg skill to create a single Excalidraw SVG visual summary showing:
- Calibration curve (confidence vs actual accuracy, showing overconfidence/underconfidence)
- Three-signal system with UX examples (Green Endorse, Yellow Caution, Red Warn)
- Domain-accuracy matrix (varying thresholds by domain type)
- Escalation flow (Endorse → use, Caution → check, Warn → escalate)
- Error reduction breakdown (35% from reduced automation bias, 10% from alert efficiency, 4% from escalation)
