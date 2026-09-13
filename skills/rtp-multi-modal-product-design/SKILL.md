---
name: rtp-multi-modal-product-design
version: v1.0.1_latest
description: 'Choose text, voice/audio, image/vision, video, or a useful combination for an AI interaction. Use when scoping a multimodal feature, comparing input and output channels, designing a switch or fallback, setting latency and cost budgets, or reviewing an underused modality. Start with the task, user abilities and context, access needs, and consequences. Compare task success, input effort, verification effort, latency, cost per useful outcome, failure modes, and observed reliance. Test clean, typical, and degraded inputs against a fair baseline; specify behavior when a channel fails or outputs disagree. Produce a modality decision, review and correction paths, measurable operating limits, and revisit triggers. Verification cost is important but does not override accessibility or task fit. Pairs with cost-model, token-economics, ai-ux-patterns, confidence-tuner, eval-framework, and autonomy-spectrum. Triggers include multimodal, voice UI, add audio/video, and modality choice.'
imports:
  - cost-model
  - ai-ux-patterns
---

# Multi-Modal Product Design

Choose the channels that let the intended users complete their task and assess the result with acceptable effort and consequences. A **modality** is an input or output channel, such as text, audio, image, or video. Input and output choices may differ.

Begin with the task and the user's actual setting: sensory and motor access, language and literacy, device, environment, privacy, bandwidth, and whether their eyes or hands are occupied. Consider accessibility from the beginning. Text is a useful baseline when it fits; it is not a mandatory default every other channel must defeat.

Produce a modality decision with the user benefit, evidence, costs, review/correction path, failure behavior, and conditions for revisiting it. If only one channel is suitable and no consequential design choice remains, document the reason briefly and move on.

## 1. Find the input and output bottlenecks

**Input effort** is the work needed to express or capture the problem. **Verification effort** is the work needed to establish whether the result meets the user's need, including expertise, evidence, and corrections. Verification matters, but cannot alone decide the channel.

| User need or constraint | Candidate input | Candidate output or review path |
|---|---|---|
| Describe a visual condition or spatial layout | Photo, screenshot, diagram, or suitable description. | Annotated source image with a clear explanation and uncertainty where relevant. |
| Capture motion, timing, or a changing process | Video or a sequence of observations. | Relevant clips, time-linked explanation, or an accessible step sequence. |
| Express precise, revisable detail | Text or dictated text with correction. | Structured text, a document, or a usable alternative. |
| Work with eyes or hands occupied | Voice or other accessible controls. | Concise spoken response, confirmation where needed, and an available record. |
| Understand a spatial or procedural result | The source material needed for the task. | Diagram, demonstration, audio description, text, or a combination tested with users. |

Do not infer that a hands-busy setting permits distraction or action: check the specific context and consequences. A visual task may lose essential information when forced into text; complex reasoning may be easier to inspect in a diagram. Voice input with text output can be an intentional, useful choice rather than a broken conversation.

## 2. Compare the channels on the same task

Use the six dimensions from the original matrix—latency, cost, input friction, verification cost, failure modes, and trust/reliance—without assuming fixed rankings. Separate **understanding existing media** from **generating new media**; their costs and errors differ.

| Channel | Input and latency considerations | Verification and correction | Failures and reliance to test |
|---|---|---|---|
| **Text** | Typing, dictation, document preparation, generation or streaming time. | Searchable and editable, but long or specialized text may require substantial expertise. | Unsupported claims, omitted context, misleading certainty, or inappropriate action. Reading does not guarantee detection. |
| **Image / vision** | Capture/upload quality, image size, analysis or generation time. | Zoom, compare with the original, annotate, inspect a region, or revise/regenerate. | Misread detail, missing objects, spatial errors, misleading generated content, and unsupported conclusions. |
| **Audio / voice** | Recording conditions, turn-taking, transcription, response onset, playback duration. | Replay, seek, slow down, correct recognized words, or consult an accurate transcript where useful. | Speech recognition errors, wrong speaker or intent, pronunciation, omitted information, and fluent but inaccurate answers. |
| **Video** | Capture, length, frame/audio processing, generation, buffering, and playback. | Scrub, replay a segment, inspect key frames, compare time-linked evidence, or edit/regenerate supported parts. | Temporal or causal errors, inconsistent frames, unsynchronized audio/text, and important events missed between sampled frames. |

Price the real request, including retries, storage, transcoding, playback or delivery, and human effort. Report cost per **useful completed outcome** as well as per request. A faster first response can still mean a slower task if the user must repair it.

The original latency and relative-cost bands are retained as unverified historical planning examples in the [reference notes](references/planning-and-evidence-notes.md). They are not current price quotes or transferable budgets.

## 3. Make consequential results inspectable

Ask what the user needs to check, which evidence supports that check, and how they can correct an error. Text may help, but a text summary generated from the same mistaken interpretation is not independent verification. A confidence label is also not evidence of correctness unless its meaning and calibration are established.

Choose a review path suitable for the information and the user's access needs. Examples include a transcript, captions, audio description, original-image overlay, timestamps, a source excerpt, replay controls, a structured confirmation of key fields, or qualified review. Verify that important information survives the alternative representation.

For an action such as sending a message or making a purchase, distinguish recognizing the input, producing a proposal, and authorizing execution. Let a user correct a misheard recipient or amount before the consequential action where the contract requires it. Follow standing authorization for routine work; do not add repeated confirmations without a reason.

**Reliance can be miscalibrated in any modality.** Fluent prose, a confident voice, or a convincing image can mislead; the effect depends on task, presentation, user, and context. Test whether users detect and act on meaningful errors. Do not teach that text is inherently under-trusted or that video is always the most trusted.

Use `ai-ux-patterns` and `confidence-tuner` for interaction and uncertainty design, and `autonomy-spectrum` for the actual action/oversight contract. High verification effort is one consideration in autonomy; it is not an automatic prohibition or a reason to exclude an accessible channel.

## 4. Test representative and degraded inputs

Keep the three-quality test, with clear definitions:

1. **Clean:** favorable, supported conditions.
2. **Typical:** the range users are expected to supply, segmented where necessary.
3. **Degraded or boundary:** plausible poor conditions, missing channels, unsupported inputs, and failure cases that could matter.

Examples include blur, low light, compression, handwriting, background noise, overlapping speakers, interrupted recordings, frame loss, and conflicting audio/image/text. Evaluate supported accents and languages as normal user variation, not as defects in the speaker. Include users whose devices or access needs differ from the development team's.

Compare against a **fair alternative**. If the text baseline requires a person to describe an image or transcribe audio, count that labor and information loss. Avoid giving one condition an expert-cleaned input unavailable in the other. Hold the task and outcome criteria sufficiently comparable, and explain unavoidable differences.

Measure task completion, relevant error classes and severity, verification effort, accessibility, latency, and cost. For a new modality, its **noisy-input lift** is the measured improvement over the defined baseline under those conditions. Report uncertainty and segment differences; aggregate accuracy can hide a serious gap.

A modality need not beat text on every imaginable worst case to be useful. Specify the supported operating range and what happens outside it: request a clearer capture, use another channel, produce a qualified partial result, route for review, or stop the dependent action. Test that fallback. Neither a large clean-demo gain nor a passing average is enough to justify silent failure on a consequential input.

The historical claim that noise removes half to four-fifths of the gain is not an established general effect. Measure this configuration rather than applying that percentage.

## 5. Design transitions and disagreement between channels

**Cross-modal friction** is extra work or confusion created by a transition between channels. Some transitions add value: speaking can reduce entry effort while a written record supports review. Optimize the complete task, not the number of switches alone.

For each transition, specify:

- What information and state carry forward, including source identity and timing.
- Whether the output is a transcript, interpretation, generated example, or original evidence.
- How the user knows capture, processing, playback, and action status.
- How to edit, interrupt, cancel, retry, or change channel without losing valid work.
- What happens when two representations conflict or one becomes unavailable.

For example, if speech says one date and an attached document shows another, identify the conflict and use the task's source policy or obtain the needed clarification. Do not let the most fluent channel silently win. Keep corrections synchronized so an updated text value does not leave stale audio or a different execution parameter.

## 6. Set latency budgets from the interaction

Distinguish **response onset**, **time to useful content**, **completion time**, and **playback time**. Voice turn-taking, image generation, document analysis, and a long video render have different expectations. Measure both typical performance and tail latency, including P95 under relevant load and device/network conditions.

Choose budgets from user needs, testing, and consequences. The source's eight-second “broken” line and two-times production-versus-development multiplier are not universal facts. A responsive progress indicator does not make an unsuitable wait acceptable, and an asynchronous flow is not always the right solution for real-time work.

Use streaming, previews, progress, background execution, or a simpler response when they help. Make partial and unverified content recognizable. Preserve interruption and recovery behavior. For asynchronous work, explain how the result becomes available; use a notification only through a supported, authorized channel and the user's preferences.

## 7. Revisit the modality with evidence

Review early enough to catch important failures and later when users, costs, models, or workload change. A weekly review for the first 90 days can be a planning cadence, not a rule for every product.

| Signal | What to investigate | Possible response |
|---|---|---|
| **Activation and use** | Exposure, discoverability, eligible users, access barriers, task frequency, and value by segment. | Improve discovery, narrow the audience, change the flow, or retire an unhelpful option. Low overall use may hide essential accessibility value. |
| **Verification effort** | Time, expertise, error detection, and whether the review path itself is accurate and usable. | Add source-linked review, correction tools, a different representation, or expert review where justified. |
| **Cost per outcome** | Complete cost, outcome quality, willingness to pay, and any deliberate subsidy. | Optimize, package appropriately, change scope, or retire the option. A premium tier is not the automatic answer. |
| **Performance under degraded input** | Failure severity, supported range, segment effects, and fallback success. | Improve capture/validation, narrow support, add a fallback, or stop unsafe dependent behavior. |
| **Regeneration and correction** | Whether users are repairing defects, exploring creatively, or iterating by choice. | Fix the relevant problem; repeated generation does not always mean poor quality. |

Set thresholds with a denominator, timeframe, consequence, and owner. Preserve an exception for useful niche or accessibility needs when justified. Costs can be shared, fixed, or incurred only when the channel is used; a lightly used option does not necessarily charge every session its full per-use cost.

## Deliver the decision

State the chosen input and output channels, the user/task benefit, evidence and uncertainty, and the alternatives considered. Include the supported conditions, review and correction path, consequential-action contract, latency/cost budget, fallback, and revisit trigger.

Check that the recommendation works for the intended users, preserves important source information, and handles failure or disagreement without pretending a summary or confidence display proves correctness. Name the principal trade-off, largest remaining risk, and next useful check. Use the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md) proportionately.

Route evaluation to `eval-framework`, economics to `cost-model` / `token-economics`, UX and reliance to `ai-ux-patterns` / `confidence-tuner`, and execution rights to `autonomy-spectrum`. A channel comparison or transition diagram can clarify the decision; use `excalidraw-svg` when useful or requested. Plot measured or explicitly hypothetical values rather than an assumed universal inversion of trust and verifiability.
