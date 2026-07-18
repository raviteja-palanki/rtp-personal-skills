---
name: rtp-multi-modal-product-design
version: v1.0_latest
description: "Choose the right modality (text, voice, image, video) for an AI feature by the one variable that actually decides it — how expensive it is for the user to VERIFY the output — not by what's technically possible or what looks impressive in a demo. Covers the modality trade-off matrix (latency, cost, input friction, verification cost, failure mode, trust asymmetry), the noisy-input test (the accuracy lift that survives production, not the clean-demo lift), cross-modal friction, latency budgets, and modality-pivot triggers. Use when scoping a multimodal feature, deciding voice vs text, pricing a modality against its cost/latency, designing a modality switch, or pushing back on 'let's add video'. Pairs with: cost-model (modality unit economics), ai-ux-patterns + confidence-tuner (the over-trust visuals/audio create), autonomy-spectrum (verification cost sets the safe autonomy level). Triggers: 'should this be voice', 'multimodal', 'add audio/video', 'modality choice', 'voice UI'."
imports:
  - cost-model
  - ai-ux-patterns
---

# Multi-Modal Product Design — Modality Is a Product Decision

**The objective:** pick the modality (and the switches between modalities) that a feature actually needs — decided by user friction, cost, latency, and above all *verification cost* — instead of by novelty or what the model can technically do. The default is text; every step away from it must earn its keep.

## THE ONE IDEA

**Modality is not a technology choice; it's a product choice — and the variable that decides it is how expensive it is for the user to *check whether the AI was right*.** Text you scan in seconds and edit in place; video you must watch start-to-finish and can't edit at all. Three consequences:

1. **Verification cost, not impressiveness, sets the modality.** The more expensive an output is to verify, the higher the stakes at which it fails — because a user who can't cheaply check it will either not check it (and act on a wrong output) or abandon it. Text keeps a healthy default skepticism; a video's temporal continuity *feels* like certainty, so users over-trust exactly the modality that's hardest to verify. Match the modality's verification cost to the consequence of being wrong.
2. **The lift that matters is on *noisy* input, not clean demos.** Every modality shows a big accuracy lift on clean input (high-res images, clear audio, structured docs) and a much smaller one — sometimes *negative* — on the messy input production actually sends. If the modality doesn't beat text-only at *worst-case* input quality, it's a liability, not an asset. Design for the noisy case.
3. **Start at text; add the minimum modality set, not the maximum impressive one.** Each modality adds cost, latency, and a transition point where users get confused about what to trust. The right question is never "what can we support?" but "what's the smallest set that closes the gap for this user at this task?"

The spine: **default to text, add a modality only when its noisy-input lift justifies its cost *and* its verification cost fits the stakes, and minimize the switches between modalities.**

## KEY TERMS (plain language)

- **Modality** — the channel an AI feature uses to take input or give output: text, voice/audio, image/vision, video.
- **Verification cost** — how much time and attention a user must spend to confirm the output is correct. Text: seconds; audio: a full listen; video: a full watch. The deciding variable.
- **Trust asymmetry** — users under-trust text (healthy) and over-trust visuals, audio, and video (dangerous), *inversely* to how easy each is to verify.
- **Noisy-input lift** — the accuracy gain a modality gives on real, messy production input — not the clean-demo number.
- **Cross-modal friction** — the confusion added each time a flow switches modality (voice-in → text-out, text → image+text).
- **Modality pivot** — the structured decision to add friction to, gate, or remove a modality that isn't earning its cost.

## THE MODALITY TRADE-OFF MATRIX

For every modality, six dimensions decide the fit. *(All figures below are 2026 order-of-magnitude ⚠ — directional, not quotes; they move with model pricing. The **pattern** is the durable content.)*

| Modality | Latency | Cost/request | Input friction | **Verification cost** | Failure mode | Trust asymmetry |
|---|---|---|---|---|---|---|
| **Text** | fastest (~0.5–2s) | cheapest (1×) | must type (medium) | **seconds — scan + edit in place** | hallucination; user catches before acting | under-trusted (healthy) |
| **Image / vision** | ~2–5s | ~2–4× | take/upload (med-high) | **look — quick, but subtle errors invisible** | visual artifacts, composition | over-trusted ("I can see it") |
| **Audio / voice** | ~1–3s | ~3–6× | speak (low, if mic) | **a full listen — high; can't edit** | mispronunciation, wrong context | over-trusted (authority) |
| **Video** | slowest (~5–15s) | most (~8–15×) | record (very high) | **a full watch — highest; no edit path** | temporal-coherence errors, hardest to spot | over-trusted (narrative = certainty) |

**Read the verification column as the spine:** it runs *opposite* to the trust column. The modality users trust most (video) is the one they can least afford to verify — which is exactly why high-stakes outputs belong in the most-verifiable modality (text), and why any less-verifiable modality carrying consequential content needs a **text summary alongside it** so the user has a cheap way to check.

## THE NOISY-INPUT TEST — the one test that kills bad modality bets

Before committing to a modality, run your eval set at **three input-quality levels: clean, typical, worst-case.** The rule: *if accuracy at worst-case input is worse than text-only, the modality is a liability.* Clean input gives the optimistic lift from the matrix; noisy input (blurry photos, accented speech, handwritten forms) drops that lift by roughly half to four-fifths ⚠ — and sometimes turns it negative, because the model over-indexes on a bad signal. Production is mostly noisy. Design for the noisy case, price the modality at its noisy-input accuracy, and if it doesn't clear text-only there, don't ship it.

## CHOOSING THE MODALITY — input vs output bottleneck

Ask what the user is actually trying to do, and where the constraint is:

- **Input is the bottleneck** (they struggle to express the problem): visual problem → image input; spatial/temporal → video input; complex/nuanced → *text* (easiest to edit); real-time/hands-busy → voice.
- **Output is the bottleneck** (they struggle to understand the result): spatial result → image; procedural/step-by-step → video; anything the user must *verify or act on* → **text** (cheapest to check); real-time interaction → voice.
- **Neither — speed and cost dominate** → text. Fastest, cheapest, most verifiable.

Then **minimize modality switches.** Each transition (voice-in → text-out, text → image+text) adds latency and a moment where the user doesn't know which output to trust. Voice-in/text-out is fine for transcription but jarring for a conversational assistant — if you add a modality to the input, ask whether users expect the same modality back.

## LATENCY BUDGETS — when "slow" becomes "broken"

User patience is modality-specific, but one line holds across all of them: **for a synchronous interaction, P95 latency past ~8 seconds is perceived as *broken*, not slow.** Text feels instant under ~500ms and needs a progress indicator past ~5s; image is expected to take a couple seconds with a "rendering…" cue; audio/video past their budgets need to go **async with a "ready for you" notification** rather than making the user wait. Load-test at realistic volume — production P95 is often ~2× the dev-environment number — and design the interaction model (streaming, progressive disclosure, async) *before* adding a modality that pushes you past the threshold.

## THE MODALITY PIVOT — when a modality isn't earning its cost

Modality choice isn't one-and-done; check weekly for the first 90 days and pivot on structured triggers, not vibes:

| Signal | Threshold ⚠ | Action |
|---|---|---|
| Activation rate | <10% of sessions after 60 days | Discovery problem (fix onboarding) *or* value problem (remove it) — a user interview tells you which |
| Verification friction | >30s to verify an output | Add a text summary alongside the modality output |
| Cost per outcome | >2× the text-only equivalent | Gate behind a premium tier if lift >30%; else remove |
| Accuracy vs text-only (noisy input) | below text-only baseline | Add input validation, or remove — text-only is better |
| Regeneration rate | >1.5× the text-only rate | The modality is hurting quality, not helping |

The through-line: a modality that's impressive but under-activated, unverifiable, or negative-margin is a cost you're paying in 100% of sessions for a benefit in a few. Track each modality's activation and cost-per-outcome, and be willing to remove.

## WHERE THIS SKILL MEETS YOUR STACK

- **The unit economics of a modality at your volume → `cost-model` / `token-economics`.** This skill flags that video is ~8–15× text; that skill models whether it survives at scale and what pricing covers it.
- **The over-trust problem visuals/audio/video create → `confidence-tuner` + `ai-ux-patterns`.** Trust asymmetry is a calibration problem — a less-verifiable modality needs a confidence signal and an uncertainty UI, not just a prettier output.
- **The noisy-input eval → `eval-framework`** (run the three input-quality levels there); **the modality's verification cost sets the safe autonomy level → `autonomy-spectrum`** (an output no one can cheaply verify can't be trusted at a high leash).

The spine: **this skill picks the channel by verification cost and noisy-input lift; the stack prices it, calibrates the trust it earns, and sets how autonomously it can run.**

## DIAGNOSTIC QUESTIONS

1. Why does this modality beat text for *this* user at *this* task — in one sentence, for real user reasons, not "it's impressive"? What % of your segment actually benefits?
2. What's the accuracy lift on **worst-case** input, not clean input? Is it still above text-only?
3. What's the cost per request at your volume, and does monetization cover it — or is the loss acceptable and bounded?
4. What's P95 latency **under load**? Does it stay under the ~8s "broken" line for a synchronous flow, or is it designed async?
5. How long must the user spend to verify the output — and what do they lose if they *don't* verify (the failure-mode stakes)?
6. If the flow switches modalities, where are the transition points, and is it clear which output the user should trust?

## QUALITY GATE

- [ ] The modality choice is justified by a real user reason (friction/verification/task), not novelty; benefit measured by segment.
- [ ] The noisy-input test passed: worst-case-input accuracy beats text-only (or the modality is cut).
- [ ] Cost per request is known and covered by monetization (or the loss is bounded and deliberate).
- [ ] P95 latency under load meets the modality's budget, or the interaction is async with notification.
- [ ] For any less-verifiable modality carrying consequential content, a text summary / confidence signal gives a cheap check.
- [ ] Cross-modal transitions are minimized and the trust mapping (what to trust when) is consistent.
- [ ] Modality-pivot triggers are instrumented (activation, verification time, cost-per-outcome, regeneration rate).

## WHEN WRONG

Exit this skill early when only one modality is clearly dominant — a text classifier doesn't have a modality question; this skill is for products where *the modality choice IS the design question*. And two honest caveats: (1) every number here (accuracy lifts, cost multiples, latency bands, the noisy-input drop) is a 2026 directional pattern (⚠), not an audited constant — run your own eval at your own input distribution before quoting any of it. (2) The rule "high-stakes → most-verifiable modality" has real exceptions — accessibility-first and hands-busy contexts (field work, driving, low-vision users) may *require* voice even at high stakes; there, the answer isn't "use text," it's "keep the less-verifiable modality but add a cheap verification path and a confidence signal." Match the modality to the *user's real constraint*, not to a rule applied blindly.

---

## TRADE-OFF LEDGER

Complete the Trade-Off Ledger from the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 3.

## CONCLUSION

Follow the Conclusion Protocol from the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 5: state the recommendation, name the key trade-off, acknowledge the biggest risk, define the next action.

---

## VISUAL SUMMARY

After completing the primary output, invoke the **excalidraw-svg** skill to create a single Excalidraw SVG visual summary — ideally the four modalities plotted with *verification cost* rising against *trust* (showing the dangerous inversion: users trust most what they can verify least). Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.
