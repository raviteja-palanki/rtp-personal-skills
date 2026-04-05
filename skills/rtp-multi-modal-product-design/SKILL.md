---
title: "Multi-Modal Product Design"
plugin: "agent-design"
version: "2.0"
imports: ["cost-model", "ai-ux-patterns"]
tags: ["multimodal", "modality-choice", "product-design", "cost-latency"]
status: "production"
---

# Multi-Modal Product Design: Modality Is a Product Decision

## DEPTH DECISION

You have a product idea. The model can handle text, image, audio, and video. The question: Which modality should you use, and when should you switch between them?

The trap: Treating modality as a technology choice. "We'll use video because it's fancy." But modality is a product choice. Voice is faster but harder to verify. Images are engaging but expensive. Video is powerful but has the highest latency and cost. Each modality has different failure modes and trust dynamics.

**Who uses this:** Product managers scoping multimodal features. Designers choosing interaction patterns. Engineers estimating cost and latency.

## DELIVERABLE FORMAT

Before starting, ask:

> **What format would you like this in?**
> 1. **Word Document** (.docx) — Formatted report with embedded visuals. Best for sharing.
> 2. **Presentation** (.pptx) — Slide deck with key findings. Best for meetings.
> 3. **Both** — Full report + summary deck.
>
> *Default: Word Document.*

If the user specifies format in their request, skip the question.

Follow the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md).

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md):
1. Ask the Grounding Questions (Section 1) — at minimum: Who is the customer? What problem? What are we saying YES to and NO to?
2. Route depth: Executive Summary or Comprehensive Analysis?
3. Identify output format: Document, presentation, spreadsheet, or inline?

Then proceed with the skill-specific analysis below.

## THE TRAP

**Trap 1: Assuming one modality can do everything.** You build a text-first product. Users ask for voice. You layer voice on top without understanding what voice changes about the user experience.

**Trap 2: Picking modality for engagement, not effectiveness.** Video looks impressive. Video output gets more engagement. You build video features. Cost is 10x higher. Users churn.

**Trap 3: Modality mismatch at critical moments.** You use text for low-stakes suggestions. Voice for high-stakes confirmations. User gets confused about when to trust what.

**Trap 4: Ignoring failure modes.** Text hallucination: fixable, user reads before acting. Audio hallucination: user listens, acts, realizes it's wrong. Different stakes.

**Trap 5: Building cross-modal workflows without friction points.** Audio → text summary → image. User doesn't know what happens between steps. Experience feels fragmented.

## THE PROCESS

### 1. Modality Trade-off Matrix

For each modality, define 6 dimensions. Build a matrix.

**Latency:**
- Text: 0.5–2 seconds (fast). Streaming helps.
- Image: 2–5 seconds (moderate). Depends on image size and model.
- Audio: 1–3 seconds (fast, once input is done). But input duration is variable.
- Video: 5–15 seconds (slow). Depends on video length and fps sampling.

**Cost per request:**
- Text: $0.001–$0.01 (cheapest).
- Image: $0.01–$0.05 (10x text).
- Audio: $0.02–$0.10 (varies by duration).
- Video: $0.10–$1.00 (expensive; usually charged by minute).

**User input friction:**
- Text: Must type. Medium friction.
- Image: Must take/upload. Medium-high friction.
- Audio: Record or paste. Low friction (if microphone available).
- Video: Must record. Very high friction.

**Output verification:**
- Text: User reads, quickly validates.
- Image: User looks, quickly validates. But composition errors hard to explain.
- Audio: User listens, must allocate attention. High verification cost.
- Video: User watches (must be sequential). Highest attention cost.

**Failure modes:**
- Text: Hallucination, wrong reasoning. User catches before acting.
- Image: Visual artifacts, composition errors. Users might miss subtle errors.
- Audio: Mispronunciation, wrong context. User acts on wrong assumption.
- Video: Temporal coherence errors. Hardest to spot while watching.

**Trust asymmetry:**
- Text: Users skeptical by default. "The AI might be wrong." Good baseline.
- Image: Users trust visuals too much. "I can see it, so it's real."
- Audio: Users trust authority too much. "The AI said it."
- Video: Users trust narrative too much. Temporal continuity feels like certainty.

## MODALITY TRADEOFF MATRIX

Every modality adds cost, latency, and (sometimes) accuracy. Before combining modalities, map the actual tradeoffs.

| Modality Combination | Relative Cost | P95 Latency | Accuracy Lift (typical) | When justified |
|---|---|---|---|---|
| Text only | 1× baseline | 0.5–3s | Baseline | Always the default |
| Text + vision (image understanding) | 2–4× | 1–5s | +15–40% on visual tasks | Product contains screenshots, diagrams, documents |
| Text + voice (STT → LLM → TTS) | 3–6× | 2–8s | +20–30% for hands-free UX | Mobile, field workers, accessibility |
| Text + structured data (tool calls) | 1.5–3× | 1–4s (sync) | +30–60% on data-grounded tasks | Finance, analytics, CRM queries |
| Vision + structured data | 4–8× | 3–8s | +40–70% on document-data tasks | Invoices, forms, receipts |
| Full multimodal (text + vision + voice + data) | 8–15× | 5–15s | Depends heavily on task | Enterprise automation, accessibility-first products |

**How to use this table:**
1. Start with Text only. Does it solve the problem at acceptable accuracy?
2. If not, identify which modality combination closes the gap.
3. Price-check: Can the accuracy lift justify the cost/latency multiplier at your volume?
4. Build the minimum viable modality set — not the maximum impressive one.

**The latency test:** If P95 latency exceeds 8 seconds for a synchronous interaction, users perceive it as broken, not slow. Design the interaction model (async, streaming, progressive disclosure) before adding modalities that push you past this threshold.

### Cost-Latency-Accuracy Matrix by Task Type

The tradeoff table above gives averages. In practice, accuracy degradation varies dramatically by task type and input quality. Use this matrix to make modality decisions for specific features:

| Task Type | Text Only (baseline) | + Vision (clean input) | + Vision (noisy input) | + Voice | + Structured Data |
|---|---|---|---|---|---|
| **Document understanding** | 70% accuracy | 92% (+22%) | 75% (+5%) — OCR errors on scans | N/A | 95% (+25%) with metadata |
| **Customer support** | 85% resolution | 88% (+3%) — screenshots help | 82% (−3%) — blurry photos hurt | 87% (+2%) — tone detection | 90% (+5%) with CRM context |
| **Data extraction** | 60% accuracy | 88% (+28%) — tables/forms | 65% (+5%) — handwritten/damaged | N/A | 92% (+32%) with schema |
| **Creative generation** | Baseline quality | +40% engagement (visual output) | N/A | +15% engagement (audio output) | N/A |
| **Code assistance** | 80% correctness | 85% (+5%) — UI screenshots | 78% (−2%) — low-res screenshots | N/A | 90% (+10%) with repo context |
| **Meeting assistance** | 75% action accuracy | N/A | N/A | 88% (+13%) — real-time transcription | 92% (+17%) with calendar/CRM |

**How input quality changes the equation:**
- **Clean input** (high-res images, clear audio, structured documents): Accuracy lift matches the optimistic end of the tradeoff table.
- **Noisy input** (blurry photos, accented speech, handwritten documents): Accuracy lift drops 50–80%. In some cases, adding the modality makes accuracy worse than text-only because the model over-indexes on bad signal.
- **Mixed input** (production reality): Expect accuracy somewhere between clean and noisy. Design for the noisy case. If the modality doesn't justify its cost at noisy-input accuracy, don't ship it.

**The accuracy degradation test:** Before committing to a modality, run your eval set at three input quality levels (clean, typical, worst-case). If accuracy at worst-case input quality is worse than text-only, the modality is a liability, not an asset.

### 2. Modality Selection Decision Tree

For a feature you're building:

**START: What is the user trying to accomplish?**

A) **Input is the bottleneck.**
User is struggling to express the problem.
- If: Problem is inherently visual → Image input.
- If: Problem involves spatial relationships → Video input.
- If: Problem is complex/nuanced → Text input (easier to edit).
- If: Problem is real-time → Audio input (fast capture).

B) **Output is the bottleneck.**
User needs to understand the result.
- If: Result requires spatial understanding → Image output.
- If: Result requires real-time interaction → Audio output.
- If: Result requires verification → Text output (easiest to check).
- If: Result is procedural → Video output (can show steps).

C) **Neither. Speed and cost matter most.**
- Choose text. Fastest, cheapest.

### 3. Cross-Modal Workflow Design

When you transition between modalities, friction increases.

**Example workflow 1: Audio → Text**
- User: [speaks request]
- System: Transcribes (0.5s), summarizes (1s).
- System outputs text summary.
- User reads, verifies.
- Total: 1.5s latency. User must do two things (listen, read).

**Example workflow 2: Image → Text**
- User: [uploads image]
- System: Analyzes image (2s), generates description (1s).
- System outputs text.
- User reads.
- Total: 3s latency. One output modality (good).

**Example workflow 3: Text → Image + Text**
- User: [types description]
- System: Analyzes (0.5s), generates image (3s) + description (0.5s).
- System outputs image + text.
- User sees both. Which do they trust? Image or text?
- If different → confusion.

**Design rule:** Minimize transitions between modalities. Each transition adds friction and confusion.

### 4. Latency Budgets by Modality

Different modalities have different user expectations for latency.

**Text to text:**
- < 500ms: Feels instant.
- 500ms–2s: Feels fast.
- 2–5s: Feels slow but acceptable.
- > 5s: User switches context. Needs progress bar.

**Image to image:**
- < 2s: Good.
- 2–5s: Expected. Show progress ("rendering...").
- 5–10s: Acceptable for complex requests.
- > 10s: User leaves. Too expensive.

**Audio to audio:**
- < 2s: Expected (user still listening).
- 2–5s: Acceptable.
- > 5s: User has moved on. Needs notification ("ready for you").

**Video to video:**
- < 5s: Expected (processing indicator).
- 5–15s: Acceptable for complex video.
- > 15s: Needs strong async behavior. "I'll send you a notification when ready."

### 5. Quality Evaluation by Modality

How do you measure quality? Depends on modality.

**Text quality:**
- Measurable: BLEU score, ROUGE, embedding similarity.
- Verifiable: User reads and checks in seconds.
- Recovery: User corrects via follow-up. Simple feedback loop.

**Image quality:**
- Measurable: Visual similarity (LPIPS), composition metrics (hard).
- Verifiable: User looks at output. But subtle errors are invisible.
- Recovery: User asks for regeneration or edits manually.

**Audio quality:**
- Measurable: WER (word error rate), naturalness (subjective).
- Verifiable: User must listen completely. High verification cost.
- Recovery: User asks for re-generation. Cannot edit.

**Video quality:**
- Measurable: Frame consistency, temporal coherence (proprietary metrics).
- Verifiable: User watches entire video. Very high verification cost.
- Recovery: Re-generation is expensive. No edit path.

**Design insight:** Text is the most verifiable and correctable. Video is the least.

## KEY DIAGNOSTIC QUESTIONS

**Q1: Modality Fit**

For your feature, is the chosen modality the bottleneck or the solution?

*Think through:* Whether this modality directly removes the user's constraint or adds a new layer of interface.

*Low end:* "We chose voice because it's impressive. Users don't actually dictate much. Most requests are text."

*Mid range:* "Image input helps 40% of users who have visual references. But text still works for 60%. We're optimizing for one segment."

*High end:* "Modality choice IS the product. Removing typing friction (voice input) is the core value prop. Users test voice first, not last."

*Red flag:* You can't articulate why this modality beats alternatives for your specific user at your specific task.

*Sharpen it:* Of your user segment, what % actually benefit from this modality? Have you measured adoption by modality?

- If audio input is slow because users can't dictate their problem → Text might be better.
- If image output looks great but users can't verify accuracy → Add text description.
- Ask: What does the user actually need to accomplish? Does this modality help?

**Q2: Cost Alignment**

Is the cost-per-request aligned with your monetization?

*Think through:* The economics of the modality vs. how users are charged.

*Low end:* "Video output costs $0.50 per request. We offer it on a free tier."

*Mid range:* "Image generation costs $0.03 per request. We charge users $5/month. At 10 requests/user/month, we break even."

*High end:* "We only offer voice for premium customers ($50/month). Volume is low. Cost per user is justified."

*Red flag:* You don't know the cost per request. You haven't modeled unit economics for this modality at your scale.

*Sharpen it:* At your volume (requests per month), what's the cost per request? What's the customer LTV needed to justify it?

- If you're offering a free tier with video output → You'll lose money per request.
- If you're charging per use and using video → Price must cover video inference cost.
- Do you know the cost per request in each modality? Have you costed your product?

**Q3: Latency Expectations**

Are you meeting user expectations for latency in each modality?

*Think through:* What feels instant, slow, or broken for THIS modality.

*Low end:* "Text to text takes 10 seconds. Users think it's broken. No loading indicator."

*Mid range:* "Image generation takes 4 seconds. User sees a progress bar. Feels acceptable."

*High end:* "Video output takes 12 seconds. It's fully async. User gets a notification when ready. No UX friction."

*Red flag:* Real latency under load is 2x higher than your development environment. You haven't load-tested.

*Sharpen it:* What's P95 latency under realistic load? Does it match user expectations for this modality?

- Text taking 8 seconds → Unacceptable. Add progress bar or switch to async.
- Audio output taking 5 seconds → Users expect this. No indicator needed.
- Video output taking 20 seconds → Unacceptable unless heavily emphasized as async.
- Have you tested latency with real users? Do they perceive it as acceptable?

**Q4: Verification Friction**

How much work must the user do to verify output is correct?

*Think through:* The time and cognitive load required to confirm the AI was right.

*Low end:* "Users must listen to 2 minutes of audio to verify a transcription. They never do. Errors go unnoticed."

*Mid range:* "Image outputs are visually clear. Users spot errors in 15 seconds. 70% of users verify before using."

*High end:* "Text output is scannable. Users verify in 5 seconds. 90%+ catch obvious errors before acting."

*Red flag:* Verification friction exceeds the value of the output. Cost to check > benefit of using it.

*Sharpen it:* For your use case, can users afford the verification cost? What happens if they don't verify?

- Text: 10 seconds to read and check.
- Image: 20 seconds to visually inspect and understand.
- Audio: 60+ seconds to listen and evaluate.
- Video: 300+ seconds to watch and understand.
- Is this friction acceptable for your use case? Can you reduce it?

**Q5: Failure Mode Tolerance**

If the AI makes a mistake, can users detect it before acting?

*Think through:* The consequences of using a wrong output. How much does the user lose if they don't catch the error?

*Low end:* "Audio suggests a stock trade. User acts on wrong information. $10K loss. Unrecoverable."

*Mid range:* "Text writes an email draft with a small error. User edits before sending. Recoverable with 1 minute of work."

*High end:* "Image thumbnail looks wrong. User re-generates before publishing. No risk to accuracy."

*Red flag:* You're using modalities with low verification in high-stakes scenarios (medical advice, financial decisions, legal docs).

*Sharpen it:* For mistakes in this modality, what's the user's recovery cost? Is it acceptable?

- Text hallucination in a code suggestion → User reads and rejects.
- Image hallucination in a design tool → User sees and corrects.
- Audio hallucination in a voice assistant → User acts on wrong information. Too late to recover.
- Video hallucination in a tutorial → User follows wrong steps.
- For high-stakes features, avoid modalities where errors are hard to spot pre-action.

## REALITY CHECK

Before you commit to a modality choice:
- Have you tested it with users? Not designers, not you. Actual users.
- Have you costed it? Do you know your cost per request?
- Have you measured latency? With real models, real sizes, under load.
- Have you stress-tested the failure mode? What happens when the AI is wrong? Can users recover?
- Have you compared to the simplest modality (text)? Is the added complexity worth the benefit?

## QUALITY GATE

Before you ship a multimodal feature:
- [ ] You've articulated why this modality is the right choice. Not "it's cool." For real user reasons.
- [ ] You've measured latency and it meets user expectations for that modality.
- [ ] You've budgeted cost. You know cost-per-request. Monetization covers it or loss is acceptable.
- [ ] You've tested failure modes. Users can detect AI mistakes before acting (for high-stakes).
- [ ] You've designed the transition points. If multiple modalities, friction points are minimized.
- [ ] You have a quality metric for this modality. It's measurable and verifiable.

## WHEN WRONG

### The Modality Pivot Decision Framework

Before listing failure scenarios, establish the systematic approach to modality pivots. When a modality isn't working, you need a structured re-evaluation — not a knee-jerk removal.

**Pivot triggers (check weekly for first 90 days):**

| Signal | Threshold | Action |
|---|---|---|
| Modality activation rate | <10% of sessions after 60 days | Evaluate: is it a discovery problem or a value problem? |
| Verification friction | >30 seconds to verify output | Add text summary alongside the modality output |
| Cost per outcome | >2× the text-only equivalent | Add friction (usage limits) or switch to async |
| User-reported errors | >5% of outputs flagged | Run accuracy audit at noisy input quality |
| Regeneration rate for modality | >1.5× the text-only regeneration rate | The modality is hurting quality, not helping |

**The pivot decision tree:**

```
Modality underperforming
├── Activation <10%?
│   ├── Users don't know it exists → Fix discovery (UI, onboarding)
│   └── Users tried it and stopped → The modality doesn't add enough value. Remove.
├── Accuracy worse than text-only at noisy input?
│   ├── Can you improve input quality? → Add input validation (min resolution, noise check)
│   └── Input quality is what it is → Remove modality. Text-only is better.
├── Cost >2× text-only per outcome?
│   ├── Accuracy lift >30%? → Keep, but gate behind premium tier
│   └── Accuracy lift <30%? → Remove. Cost doesn't justify the improvement.
└── Latency >8s P95?
    ├── Can you make it async? → Move to async with notification
    └── Must be synchronous? → Switch to faster modality or remove
```

**Recovery procedures by failure mode:**

| Failure | Specific Recovery Steps | Success Metric |
|---|---|---|
| Low adoption (<10%) | 1. Check if feature is discoverable. 2. Run 5 user interviews. 3. If value problem: deprecate within 30 days. If discovery problem: redesign entry point. | Activation reaches 20% within 30 days of fix |
| Accuracy degradation | 1. Segment accuracy by input quality. 2. Add input validation (reject below threshold). 3. If still below text-only: deprecate. | Accuracy at P25 input quality exceeds text-only baseline |
| Cost spiral | 1. Calculate true cost per outcome including regenerations. 2. Add usage caps per tier. 3. If margin still negative: move to outcome-based pricing for that feature. | Feature-level margin turns positive within 60 days |
| Verification friction >30s | 1. Add text summary alongside non-text output. 2. Add confidence indicators. 3. If still >30s: the modality is wrong for this use case. | Verification time drops below 15s |

### Scenario Catalog

**Adding modalities for sophistication, not user value.**
The product demo includes voice, vision, and real-time data because it's impressive. Product teams add modalities to signal capability to investors and enterprise buyers. Track each modality's activation rate — if voice is used in 3% of sessions but you're paying for it in 100% of sessions, remove it.

**Using this skill on a single-modality problem.**
You're building a text classification tool. Nothing fires — no vision, no voice, no tool calls. If only one modality is clearly dominant, exit the skill early. Multi-modal product design is for products where the modality choice IS the design question.

**Ignoring the fallback design.**
Vision works on clean inputs. Production has messy inputs. For every modality, design an explicit fallback: "If vision confidence is below threshold X, ask the user to re-upload or switch to text input."

**The modality mismatch (input ≠ output expectation).**
Voice-in / text-out is fine for transcription but jarring for conversational assistants. If you add a modality to the input, consider whether users expect the same modality in the output.

**Engagement without utility.** Video has high completion rate but doesn't help users accomplish their goal. Trigger: users engage but churn anyway. Switch to a simpler modality.

**Latency became intolerable.** Video takes 12 seconds per request. Users perceive >8s as broken. Move to async or switch modality.

**Cost spiraled.** Image feature costs more than expected. Add friction to reduce request rate, switch to cheaper modality, or increase pricing.

**Users can't verify output.** Audio hallucination rate is high. Users act on wrong information. Add text summary alongside audio.

**Failure modes are invisible.** Video tutorial contains errors that are hard to spot while watching. Add chapters, text summaries, and scrub-to-verify UX.

**Modality mismatch creates confusion.** Text for low-stakes, image for high-stakes — but users don't know which to trust. Establish a clear modality-trust mapping and be consistent.

---

## GENERATE THE DELIVERABLE

Use the output generation prompt from the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 11.

If this skill connects to downstream skills (e.g., build-or-buy, cost-model), generate the markdown handoff file as well.

---

## TRADE-OFF LEDGER

Complete the Trade-Off Ledger from the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 3.

## CONCLUSION

Follow the Conclusion Protocol from the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 5:
1. State the recommendation
2. Name the key trade-off
3. Acknowledge the biggest risk
4. Define the next action

---

## VISUAL SUMMARY

After completing the primary output, invoke the **excalidraw-svg** skill to create a single Excalidraw SVG visual summary. This diagram captures the essence of the analysis in one glanceable image — making the deliverable 10x more impactful. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.
