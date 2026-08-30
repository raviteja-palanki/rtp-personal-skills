---
name: invisible-stack
version: v2.2_latest
description: 'Every AI feature has a visible part (the model writing the answer) and a stack of hidden parts (retrieval, safety, memory, tools) that decide whether that answer is any good. This maps those hidden layers (the seven CONTEXT layers), measures each, and finds the single weakest layer capping quality, because a perfect model fed bad context still ships a bad product. Use when reviewing an AI architecture or diagnosing why a demo works but production doesn''t. Do NOT use for simple single-turn features with no retrieval, memory, or tools. Pairs with: context-spec (this finds the weak layer, that writes the build spec for all seven), eval-framework (every eval failure traces to one broken layer here), production-observability (instruments each layer), failure-modes (each layer''s break maps to a named failure), moat-finder (skipping the stack is now a negative-flywheel survival risk). Triggers: ''demo works, production doesn''t'', ''AI architecture review'', ''why is quality capped'', ''RAG quality''.'
imports: [determinism-compass, stress-test]
---

# Invisible Stack — The Production-Quality Diagnostic

**The objective:** find the one hidden layer capping your AI feature's quality, before you waste weeks tuning the wrong thing — for the PM whose demo dazzles and whose production system disappoints.

## The one idea

A B2B document-analysis product is stuck at 65% satisfaction after six months. The team has spent those months on the model — new prompts, frontier model A vs. B — and nothing moves. Then someone measures the layer nobody was watching: retrieval was finding the right document only *half* the time. The model was never the problem; it was hallucinating to reconcile the irrelevant chunks retrieval kept handing it. Fix the retrieval, and satisfaction jumps to 82% — with no change to the model at all.

That is the whole idea. **The model is the part everyone watches, and it is rarely the part that's broken.** Users see the chat box; they don't see retrieval, context assembly, guardrails, memory, tool calls, or monitoring — and *those* invisible layers are where production quality lives or dies. A useful frame is the **10/90 split** (⚠ illustrative, the ordering not the number): the model is maybe 10% of what determines quality, and the other 90% is the stack around it. It draws attention it doesn't deserve precisely because it's the one component you didn't build and can't easily change, while the layers you *can* control go unexamined — the **spotlight effect**.

And the mechanism that makes this decisive is the **weakest-layer ceiling:** the layers run in sequence, and a later one cannot rebuild information an earlier one destroyed. The model cannot cite a document retrieval never found; perfect generation on top of 50%-accurate retrieval is still 50% right. So a system's quality is capped by its worst layer — which means the highest-leverage fix is almost never where attention naturally goes. This skill makes the invisible infrastructure visible enough to *measure*, so you can point at the specific layer setting the ceiling and fix that, instead of swapping models and hoping.

## How to use this skill

1. **Map the full stack** with the CONTEXT checklist — the layers you forget are the ones with no owner and no monitor, which is why they break in production. (THE PROCESS, step 1.)
2. **Measure each layer** on coverage × accuracy × latency, and find the weakest one with a *number*, not a hunch. (MEASURING EACH LAYER.)
3. **Fix upstream first** — design the invisible layers before the visible UI, and never optimize the model until you've audited the layers above it.

## KEY TERMS (plain language)

- **The invisible stack** — every processing step between a user's request and the answer they see; the chat box is visible, retrieval/safety/memory/tools are not.
- **CONTEXT (the seven layers)** — the mapping checklist: **C**onstitution (rules), **O**bservations (live session data), k**N**owledge (retrieved docs), **T**racks (memory/history), **E**quipment (tools/APIs), e**X**ecution (orchestration, retries), **T**emplate (output format). Its whole job is to leave no layer unnamed.
- **Weakest-layer ceiling** — quality is capped by the worst layer, because a later layer can't rebuild what an earlier one lost.
- **Retrieval / RAG** — the step that searches your documents and hands the best ones to the model; RAG = retrieval-augmented generation.
- **Precision@5** — of the top 5 documents retrieval returns, how many are actually relevant.
- **Embedding / chunking / re-ranker** — the model that turns text into comparable numbers; how you cut docs into searchable pieces (small = precise facts, large = context); a second-pass filter that reorders candidates to the best few.
- **Ablation test** — remove a layer, measure the quality drop; that drop is the layer's real contribution.
- **Spotlight effect** — over-weighting the one visible thing (the model), under-weighting everything you can't see.
- **Evidence tiers used below** — ✅ audited · ◆ disclosed · ⚠ practitioner estimate. Numbers marked *illustrative* are teaching devices, not data.

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../../../UNIVERSAL-SKILL-PROTOCOL.md). At minimum: name the feature and whether it has retrieval, memory, or tools (if not, skip — there's no invisible stack). **Go deep** when architecting a feature with retrieval/tools/state, reviewing production failures, or diagnosing a demo-vs-production gap. Then route depth and output format.

## THE TRAP

You will focus on the model (the **spotlight effect**). The **10/90 split** is the corrective: the model is a small share of what determines quality; retrieval, context engineering, safety, caching, and monitoring are the rest (⚠ illustrative proportion — the ordering is the point). **When it over-warns:** a thin single-turn feature with no retrieval or memory really is mostly model — don't manufacture layers that aren't there.

**Retrieval is the quiet failure point, and a PM decision — not "engineering will handle it."** A perfect model fed bad context produces confident hallucinations no prompt tweak fixes. Where output quality comes from, ordered by leverage (the claim is *ordinal*, not cardinal — don't cite percentages): retrieval accuracy (did we find the right docs at all?) ≫ information density ≫ order (best doc first, or buried?) ≫ structure ≫ prompt clarity. So if retrieval finds the right document 60% of the time, ~60% is your quality ceiling — spend your first hour there, not on formatting. **Embedding choice and chunking are PM decisions** because each silently sets that ceiling, and the trade-offs (precision vs. context, cost vs. accuracy) are product trade-offs wearing technical clothing; hand them off unexamined and you've outsourced your ceiling.

## THE PROCESS

1. **Map the full stack** — name every layer between input and output using the CONTEXT checklist (C/O/N/T/E/X/T above). Why a checklist and not free recall: the layers you forget are exactly the unowned, unmonitored ones that break in production. If you can't list all seven, the missing ones are your first finding.
2. **Assess each layer** — does it exist? who owns it? how is it monitored? what happens when it fails? A layer with no owner and no monitor is a production incident waiting for a date.
3. **Identify the weakest layer** — it sets the ceiling. *When this frame misleads:* sometimes the fault is two adequate layers interacting badly (a decent retriever and a decent formatter that disagree on structure) — if fixing the "weakest" layer doesn't move quality, look at the *seams*, not the layers.
4. **Design invisible before visible, and re-architect before you automate.**

   Start from the context architecture and work forward to the UI. The interface inherits whatever ceiling the invisible layers set.

   **The stakes are higher than build quality: automating a broken workflow is negative-flywheel, not merely wasted effort.** Drop an agent on a messy process and it reproduces the mess at scale, *and the feedback loop reinforces the bad pattern faster*. Bad data in, bad pattern learned and compounded.

   So "re-architect before you automate" is now a survival variable rather than a nicety. A rushed agent pilot on a messy process actively degrades your own long-tail data relative to a rival running it clean. (Hammer's 1990 "obliterate, don't automate," sharpened by Christensen's disruption logic. Conceptual, 30-year pedigree ◆.)

   That is the exclusive-data economics: your own customer data, kept private, is the moat. A second and opposite kind of data, meaning identity, reputation and trust records meant to be checked across an ecosystem of agents and vendors, runs the other way. See the split under `rtp-moat-finder` below.

   *When wrong:* a genuinely clean, well-instrumented workflow has little to re-architect. Don't manufacture a reengineering project to gate a simple automation. *(Full moat framing in `moat-finder`; secondary insight from HBR q2-21, Lee/Mantia/McNeill, forthcoming Jul-Aug 2026.)*

## MEASURING EACH LAYER

Analysis without measurement is a guess. For each layer, run three questions: **Coverage** (what share of queries does it touch? — a layer on 20% of traffic matters less than it feels; a layer on 80% is critical path), **Accuracy** (when it fires, how often is it right? — high coverage + low accuracy is the worst combination, wrong more often and harder to trace), **Latency** (how much time does it add? — users tolerate ~3–4s for a complex task ⚠; if the stack eats 2s before generation, 1–2s is all that's left).

The thresholds below are **⚠ practitioner starting points, not laws** — tune to your domain (a safety-critical medical feature and an internal drafting tool have different tolerances for the same false-negative rate):

| Layer | Coverage | Accuracy | Latency | Suggested start (⚠ tune) |
|---|---|---|---|---|
| Constitution (rules) | % edge cases with an explicit rule | rule-violation rate | N/A | coverage >90%; violations <0.5% |
| Retrieval (RAG) | % queries returning ≥1 relevant doc | Precision@5 | P95 retrieval | Precision@5 >70%; <500ms; empty <5% |
| Validation (guardrails) | % output categories with a guardrail | false-positive + false-negative rate | added latency | FP <2%; FN <1% where safety-critical; +<200ms |
| Orchestration (routing/tools) | % tool calls with error handling | success + fallback rate | end-to-end P95 | success >95%; fallback <10%; <2s |
| Monitoring (observability) | % features with a live monitor | drift caught before users report | drift→alert time | >80% caught first; alert <1hr |

**Run the audit** before launch (mandatory), quarterly, and after any model upgrade (a swap silently reshuffles which layer is weakest): map → instrument each (any layer with zero instrumentation is your first finding) → baseline on a few hundred representative queries → stress-test with adversarial/edge cases → **ablate** (remove a layer, measure the drop — that's its real contribution; near-zero = a candidate to cut for latency/cost) → document per-layer gap/fix/owner/timeline, and re-run to confirm the improvement.

## AUDIT CASE STUDY (illustrative ⚠)

The document-analysis product from "the one idea": stuck at ~65% satisfaction, months spent on the model with no movement. The audit found retrieval at ~50% precision (half the surfaced docs irrelevant), a strong model, and working safety/post-processing. **The model was never the problem** — retrieval was polluting the context and the model hallucinated to reconcile it. The fix was upstream (re-chunking + a better embedding model), lifting precision ~50%→81% and satisfaction ~65%→82%, no model change. **The durable lesson (not the numbers): never optimize the generation layer until you've audited the layers upstream of it.**

## HOW THE STACK SHOWS UP IN EVALS

When an eval fails, trace it to the layer that caused it instead of blaming the model. This is the same object `eval-framework` works on from the other end (error analysis *groups* failures; this skill *names the layer* each group belongs to), and each maps to a named entry in `failure-modes`: poor retrieval → **hallucination** (owner: retrieval/embedding/chunking — fix retrieval before the prompt); poor guardrails → **safety failure** (Constitution/validation — add the guardrail); poor caching → **cost blowup** (eXecution — cache/reshape); poor context assembly → **self-contradiction** (Tracks/session state — version or clear boundaries); works in test, degrades at production scale → **the classification gap** (owner: eXecution/Equipment — a scale-dependent infrastructure dependency such as a connection pool, a cache, or a rate limit that holds up in test and buckles under production concurrency). **Every eval failure has a root layer.** Naming it turns "the model is bad" into an assignable fix with an owner.

**The classification gap, named.** Three anonymized AI-vs-IT advisory engagements found the same misdiagnosis each time. AI teams classify failures by output quality (wrong answer, hallucination); IT teams classify by system health (uptime, error rate). Neither taxonomy has a slot for an infrastructure dependency that only breaks under production load, so the defect falls between the two classification systems and gets logged as a model problem by default, because that is the only taxonomy anyone reaches for. **When this is wrong:** if the same failure reproduces at test volume after a real model or prompt change, that is a regression, not a classification gap; don't use "it's probably infra" as a reflex excuse to skip checking the model. (Source: three anonymized AI-vs-IT advisory engagements, Jul 2026. ⚠ mechanism only, no outcome measures; cite the pattern, not a success rate.)

## WHERE THIS SKILL MEETS THE REST OF YOUR STACK

- **`rtp-context-spec`** — this skill *diagnoses* the weak layer; context-spec *writes the build spec* for all seven. One finds, one designs — run in sequence.
- **`rtp-eval-framework`** — every eval failure traces to one broken layer here; run them together to route a failure group to its owning layer.
- **`rtp-production-observability`** — you can't fix a layer you can't see; it instruments each layer (the monitoring row above is its home).
- **`rtp-failure-modes`** — each layer's break maps to a named failure (bad retrieval → hallucination, missing guardrail → unsafe output).
- **`rtp-cost-model` / `rtp-token-economics`** — the vector-DB and re-ranker choices are unit-economics decisions (hosted vs. self-hosted, latency vs. relevance); those skills do the cost math.
- **`rtp-moat-finder`.** The negative-flywheel point from step 4: skipping the stack before automating is not merely wasteful, it degrades the data moat. Moat-finder carries the full competitive framing.

  **The data moat is not one thing, and treating it as one is a common mistake.**
  - **Customer data** (a specific user's documents, conversations, behavior) is worth more kept exclusive. Competitors cannot see it, and that exclusivity is the moat.
  - **Network or registry data** (identity, reputation and trust records meant to be checked across an ecosystem of agents and vendors) works the opposite way. Its value comes from how many participants can verify against the same record. Hoarding it behind a private wall shrinks the network to your own users and destroys the trust signal that made it worth building.

  **When this split is wrong:** a field that looks like "reputation" but is really an internal ranking score you never intend to federate still follows the customer-data rule. Don't apply the keep-it-universal logic just because a field is named "trust" or "identity." *(Source: MIT Sloan, "Who will own the AI agent economy?," Jul 2026 — ⚠ single researcher's position, disclosed conflict of interest; carry the structural distinction only, not the forecast.)*
- **`rtp-ai-use-case-readiness`** *(upstream)* — the skill that usually hands you the feature to architect. It sets the autonomy level; that level constrains which layers even exist — a level-2 use case has no Equipment (tools) or heavy eXecution layer to audit, a level-5 agent has both and they dominate the stack. Take the level as the input; don't design a seven-layer stack for a feature that only needed two. (The chain: opportunity-solution-tree greenlights → use-case-readiness sizes autonomy → this skill designs the stack to fit.)

## VECTOR DB & RE-RANKING (PM decisions, not engineering-only)

**Vector DB** choice sets unit economics, latency, and lock-in (⚠ ranges, [VERIFY] current pricing): hosted (Pinecone/Weaviate Cloud — low ops, ~50–150ms, painful economics north of ~1M queries/mo, ~$0.001–0.01/query) vs. self-hosted (Weaviate/Qdrant/Milvus — higher ops, ~$0.0001–0.001/query at scale, an escape hatch if a vendor changes pricing) vs. hybrid (start hosted, migrate when volume justifies). If retrieval quality is your moat, lean self-hosted for control. **Re-ranking** filters ~20 first-pass candidates to the best few, adding ~100–200ms (⚠): almost always worth it for research/summarization (users wait), skip or go lightweight for autocomplete (needs sub-50ms), A/B for chat. Own these as a PM because the "simplest" choice (hosted) is often the most expensive long-term, and the person who owns the unit economics must see that before the migration cost is locked in.

## QUALITY GATE

- [ ] Full stack mapped — every layer between input and output named (missing layers are findings)
- [ ] Each layer has an owner and a monitoring mechanism
- [ ] Weakest layer identified with a measured number — and the seams checked if fixing it doesn't move quality
- [ ] Latency budget allocated across layers
- [ ] Vector-DB choice justified with unit economics; re-ranking decision made against the latency budget

## WHEN WRONG

- Simple prompt-and-response features with no retrieval or context — there's no invisible stack.
- Prototypes where the open question is still "can the model even do this?" — validate capability first.
- When stack complexity has itself become the bottleneck — the right move is to *remove* layers, not map more.

## OUTPUT FORMAT

```
## Invisible Stack Audit: [Feature]
| Layer | Exists? | Owner | Monitoring | Failure mode | Priority (1–5) |
| C/O/N/T/E/X/T … |
Weakest layer: [with a measured number]   Retrieval quality: [measured %, method]   Latency budget: [total, per-layer]
```
Deliver as a document (full audit + roadmap with owners/timelines), a deck (stack + weakest layer + exec rec), or a spreadsheet (layer inventory). Always include a stack diagram (via `excalidraw-svg`), the per-layer baseline vs. thresholds, and the gap-to-fix roadmap.

## TRADE-OFF LEDGER

By auditing the invisible layers before touching the model, you bet that the ceiling is set upstream of where attention naturally goes — that a measured weak layer beats another model swap. You give up the satisfying, visible work of prompt-and-model tuning for the unglamorous work of instrumenting retrieval and guardrails. **Reversible?** Fully — it's diagnosis, not a rebuild. **The hidden trade:** the failure mode is *mapping as procrastination* — a seven-layer audit on a thin feature that needed none; match stack depth to how much a wrong answer can hurt. **Confidence: High** — the weakest-layer ceiling is arithmetic, not opinion. What would change it: a genuinely single-turn feature where the model really is the system.

## CONCLUSION

Follow the Conclusion Protocol ([Universal Skill Protocol](../../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 5): the recommendation (the weakest layer, named with a number, and the upstream fix), the key trade-off (fixing the invisible layer vs. the visible model), the biggest risk (a seam problem masquerading as a weak-layer problem, or a model swap that reshuffles the weakest layer), and the next action (owner + date for the fix, and the re-run that confirms it).

## VISUAL SUMMARY

After the primary output, invoke the **excalidraw-svg** skill for one visual: the seven CONTEXT layers stacked between "user input" and "user output," each with its coverage/accuracy/latency, and the **weakest layer highlighted** as the ceiling — so a viewer sees at a glance that the visible model sits on top of an invisible stack that decides its quality. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.
