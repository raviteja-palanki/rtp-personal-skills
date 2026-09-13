# Planning and evidence notes

Review date: 13 September 2026.

## Historical numbers retained for traceability

The original skill supplied these practitioner-level estimates without an identified empirical dataset or comparable workload:

| Channel | Latency example | Cost relative to text |
|---|---|---|
| Text | 0.5–2 seconds | 1× |
| Image/vision | 2–5 seconds | 2–4× |
| Audio/voice | 1–3 seconds | 3–6× |
| Video | 5–15 seconds | 8–15× |

Analysis, generation, content length, resolution, caching, output duration, provider, and deployment can change each comparison. Re-price and measure the actual workflow. These ranges do not establish a general ranking.

Other historical starter thresholds were: synchronous P95 above eight seconds; text response under 500 ms and a progress cue after five seconds; production P95 twice development; activation below 10% after 60 days; verification above 30 seconds; cost above twice text; a premium-tier candidate if lift exceeds 30%; and regeneration above 1.5 times text. The source also proposed weekly review for 90 days and a 50–80% loss of clean-input lift under noise.

None is a validated universal gate. Use them only as examples of the **kind** of measure to specify, with local evidence, definitions, and an owner. In particular, activation among all sessions can misrepresent a channel designed for a small eligible population.

## Accessibility sources

The W3C's [audio/video planning guide](https://www.w3.org/WAI/media/av/planning/) distinguishes media types and their accessibility provisions. Its [transcript guide](https://www.w3.org/WAI/media/av/transcripts/) explains why a descriptive transcript may need visual information beyond spoken dialogue. [WCAG 2.2](https://www.w3.org/TR/WCAG22/) provides the relevant accessibility criteria; select requirements for the content, purpose, and conformance target rather than treating any text summary as sufficient.

These sources support planning accessible alternatives and accurate equivalents. They do not establish that text is always faster to understand, that a transcript independently verifies the source, or that voice is inappropriate for consequential work.

## What changed in the underlying reasoning

The original claim that audio and video cannot be edited is incorrect. Playback controls, text-linked editing, clip replacement, and regeneration can support correction, depending on the product. Full sequential playback is not always necessary for every verification task; timestamps, key frames, source links, and expertise affect the effort. Equally, quick scanning of text does not guarantee detecting an error.

Input quality matters, but “all modalities improve accuracy on clean input” and “production is mostly noisy” require a defined task and population. An accent is ordinary language variation; system support needs evaluation rather than framing the speaker as a degraded input.

The Novel Insights passage on verification substitution is relevant: persuasive explanation may substitute for checking evidence. Its particular research result should not be generalized into a hierarchy where text is safe and all other media invite over-trust. The practical lens is to test what users can actually inspect and how the representation changes their decisions. A summary, caption, or spoken explanation can improve access while still carrying an error.
