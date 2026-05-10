---
name: rtp-invisible-stack
description: 'Maps seven-layer CONTEXT: Constitution, Observations, kNowledge, Tracks, Equipment, eXecution, Template. Use when reviewing architecture, diagnosing demo-to-production gaps, or writing specs. Identifies weakest layer. Do NOT use for simple experiments. Prevents model fixation and infrastructure gaps.'
---
# Invisible Stack

## DEPTH DECISION

**Go deep if:** Architecting an AI feature with retrieval, tools, or conversation state, reviewing production failures, or diagnosing why demo works but production fails.

**Skim to Weakest Layer if:** You have a system already built and just need to identify which layer is causing problems.

**Skip if:** Simple single-turn prompt-response features with no retrieval or context dependencies.

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md):
1. Ask the Grounding Questions (Section 1) — at minimum: Who is the customer? What problem? What are we saying YES to and NO to?
2. Route depth: Executive Summary or Comprehensive Analysis?
3. Identify output format: Document, presentation, spreadsheet, or inline?

Then proceed with the skill-specific analysis below.

---

## Retrieval Quality as PM Decision (Not Just Engineering)

Retrieval is the silent killer. A perfect model receiving bad context produces hallucinations. **This is a PM responsibility.**

**Quality Hierarchy (impact on output quality):**

```
Retrieval Accuracy:          40% of output quality
  └─ Are the right docs found? Does search match user intent?

Information Density:         25% of output quality
  └─ Do retrieved docs contain the answer, or just tangential info?

Information Order:           20% of output quality
  └─ Is the most relevant doc first, or buried in position 5?

Clear Structure:             10% of output quality
  └─ Are docs well-formatted, making it easy for model to extract facts?

Instruction Clarity:         5% of output quality
  └─ Does the prompt tell the model how to use retrieved docs?
```

**What this means for you (the PM):**
- If retrieval accuracy is 60%, your output quality ceiling is 60% (model can't fix bad docs).
- Improving docs to clear, structured format (50→80% structure score) adds only 5% overall quality.
- But improving retrieval to find the right doc first (40→50% order) adds 2% quality.
- **Spend PM time on retrieval accuracy first. Everything else is smaller gains.**

**Embedding choice as PM decision:**
- Different embedding models produce different retrieval quality for different domains.
- Text-embedding-3-large for dense technical docs. OpenAI small for short customer queries.
- Test retrieval quality before committing to the model. This is not a "just implement it" decision.

**Chunking strategy as PM decision:**
- How you split documents affects retrieval. 256-token chunks vs. 2K chunks are different products.
- Chunking strategy determines whether you can surface facts or only general info.
- Again: test with real queries before committing to the technical implementation.

## THE TRAP

You will focus on the model. The bias is **spotlight effect** — attention goes to the visible, impressive part (the LLM generating responses) while ignoring the invisible infrastructure that determines whether those responses are any good. Users see the chat interface. They don't see retrieval, context assembly, guardrails, caching, routing, or observability. But those invisible layers are where production quality lives or dies.

The 10/90 rule: in a production AI system, the model is roughly 10% of the system. The other 90% — retrieval, context engineering, safety layers, caching, monitoring — is invisible to users and often invisible to product managers.

## THE PROCESS

1. **Map the full stack.** For any AI feature, identify every layer between "user input" and "user output." Use the CONTEXT framework as a checklist:
   - **C**onstitution — System instructions, behavioral constraints, safety rules
   - **O**bservations — Real-time data, user context, session state
   - **N**owledge — Retrieved documents, knowledge bases, structured data
   - **T**racks — Workflow state, multi-step routing, conversation history
   - **E**quipment — Tools, APIs, MCP connectors, function calls
   - **X**ecution — Orchestration logic, retry handling, timeout management
   - **T**emplate — Output formatting, response structure, prompt templates

2. **Assess each layer.** For each:
   - Does it exist? (Many production issues come from missing layers)
   - Who owns it?
   - How is it monitored?
   - What happens when it fails?

3. **Identify the weakest layer.** The system's production quality equals the quality of its weakest invisible layer. A perfect model with bad retrieval produces hallucinations. Perfect retrieval with no guardrails produces unsafe output.

4. **Design the invisible layers before the visible ones.** Reverse the natural order: instead of starting with the chat UI and working backward, start with the context architecture and work forward.

## REALITY CHECK

- Building the full invisible stack for every feature is over-engineering. Match stack depth to feature criticality.
- Each invisible layer adds latency. A 7-layer stack with 100ms per layer is 700ms before the model even starts generating.
- Invisible layers need their own monitoring — you can't monitor what you can't see.

## MEASURING EACH LAYER

Analysis without measurement is a guess. For every layer you identify in the stack, run this 3-question protocol:

**Coverage:** What percentage of queries does this layer handle?
- Example for a knowledge/RAG layer: "What % of user queries can be answered from our knowledge base vs. falling back to base model?"
- Why it matters: A layer that only activates 20% of the time contributes less than you think. A layer that activates 80% of the time is critical path.

**Accuracy:** When this layer fires, how often is it right?
- Example: "When our retrieval layer finds a relevant document, does the final answer use it correctly?"
- Why it matters: High coverage + low accuracy is worse than low coverage + high accuracy. You're wrong more often AND it's harder to debug.

**Latency:** How much time does this layer add to the total response time?
- Example: "Our safety filter adds 200ms P95. Our retrieval adds 800ms P95. Together: 1 full second before the model even starts."
- Why it matters: Users tolerate ~3–4 seconds for complex AI tasks. If your stack consumes 2 seconds before generation, you have 1–2 seconds left for the actual model call.

**Layer measurement template:**

| Layer | Coverage | Accuracy | Latency Added |
|---|---|---|---|
| Retrieval/RAG | __% of queries | __% precision | __ms P95 |
| Safety filter | __% of queries | __% true positive | __ms P95 |
| Knowledge cache | __% of queries | __% hit rate | __ms P95 |
| Post-processor | 100% of outputs | __% correct transformations | __ms P95 |

### Layer-Specific Measurement Protocol

| Layer | Coverage Metric | Accuracy Metric | Latency Metric | Acceptable Threshold | How to Collect |
|---|---|---|---|---|---|
| Constitution (system prompt, rules) | % of edge cases with explicit handling rules | Rule violation rate (outputs that break constraints) | N/A (static) | Coverage: >90% of known edge cases. Violations: <0.5% of outputs. | Log constraint violations. Run adversarial prompt suite monthly. |
| Retrieval (RAG, search, context) | % of queries that return ≥1 relevant document | Retrieval precision@5 (% of top-5 results that are relevant) | P95 retrieval latency | Precision@5: >70%. Latency: <500ms. Empty retrieval: <5% of queries. | Instrument retrieval pipeline. Sample 100 queries/week for manual relevance scoring. |
| Validation (guardrails, filters) | % of output categories with active guardrails | False positive rate (good outputs blocked) + false negative rate (bad outputs passed) | Guardrail evaluation latency | FP: <2%. FN: <1% for safety-critical. Latency: <200ms added to response. | Log every guardrail trigger with input/output pair. Weekly review of blocks and passes. |
| Orchestration (routing, tool calls) | % of tool calls with error handling | Tool call success rate. Fallback activation rate. | End-to-end orchestration P95 | Success: >95%. Fallback: <10% of requests. Latency: <2s for routing decision. | Instrument each tool call. Track retry counts, fallback triggers, timeout events. |
| Monitoring (observability, drift) | % of production features with active monitors | Drift detection accuracy (does the alert fire before users notice?) | Alert latency (time from drift to notification) | Drift detection: >80% caught before user report. Alert: <1 hour. | Deploy embedding-based drift detection. Track user-reported vs. system-detected issues. |

## AUDIT CASE STUDY

**Situation:** A B2B document analysis product had 65% user satisfaction scores after 6 months of operation. The team had been iterating on the generation model (trying different prompts, testing Claude vs GPT-4) with no meaningful improvement.

**The audit:** Using the measurement protocol above, the team found:
- Knowledge layer (retrieval): 50% precision. When it retrieved documents, half were irrelevant to the query.
- Generation model: Strong. Given correct context, it produced excellent answers.
- Safety layer: Working correctly.
- Post-processor: Working correctly.

**The finding:** The generation model wasn't the problem. The retrieval layer was polluting the context with irrelevant chunks, and the model was hallucinating to make sense of them.

**The fix:** Rebuilt the retrieval layer (re-chunking strategy + embedding model upgrade). Retrieval precision went from 50% → 81%.

**The result:** User satisfaction went from 65% → 82% — with no changes to the generation model.

**The lesson:** Never optimize the generation layer until you've audited the layers upstream of it. The invisible stack's weakest layer sets the ceiling for the whole system.

### How to Run an Invisible Stack Audit

**When to audit:** Before launch (mandatory), quarterly (recommended), after any model upgrade or architecture change (mandatory).

**The 6-Step Audit Protocol:**

1. **Map the stack.** List every layer between user input and user output. Include: system prompt, retrieval, pre-processing, model call, post-processing, guardrails, caching, logging. If you can't list them all, you have an invisible stack problem — by definition.

2. **Instrument each layer.** For each layer, verify you have: latency measurement, error rate, and at least one quality metric. If any layer has zero instrumentation, that's your first finding.

3. **Measure baseline.** Run 200+ representative queries through the full stack. Record per-layer metrics. This is your baseline before any changes.

4. **Stress test.** Run 50 adversarial or edge-case queries. For each: does the retrieval layer return garbage? Does the guardrail catch it? Does the monitoring layer alert?

5. **Compute layer contribution.** For each layer, measure: what % of end-to-end quality does this layer contribute? (Ablation test: remove the layer, measure accuracy drop.) Layers contributing <2% to accuracy are candidates for removal to reduce latency and cost.

6. **Document findings.** For each layer: current metric, threshold, gap, recommended fix, owner, timeline.

**Post-Audit Validation:**
- Re-run the same 200 queries after fixes. Compare before/after metrics.
- The audit is not done until the re-run confirms improvement.

---

## Vector DB Selection as PM Decision

Vector database choice is not an engineering-only decision. It's a strategic choice that affects unit economics, latency, and competitive positioning.

**Trade-offs to own:**
- **Hosted (Pinecone, Weaviate Cloud):** Lower operational burden, predictable costs at small scale, vendor lock-in risk, higher per-query pricing at scale
- **Self-hosted (Weaviate, Qdrant, Milvus):** Higher operational burden, lower cost at scale, escape hatch if pricing changes, requires infrastructure expertise
- **Hybrid:** Start hosted, migrate self-hosted when query volume justifies it

**PM decision points:**
- What's acceptable latency per query? (Hosted: 50-150ms, Self-hosted: 100-200ms)
- What's your long-term query volume forecast? (Hosted becomes expensive >1M queries/month)
- Is vendor lock-in acceptable? (If your competitive moat depends on retrieval quality, self-host)
- What's your cost per query budget? (Hosted: $0.001-0.01/query, Self-hosted: $0.0001-0.001/query at scale)

**Action:** Before finalizing vector DB choice, map unit economics across options. The "simplest" choice (hosted) may be the most expensive long-term.

---

## Re-ranking Strategies

First-pass retrieval returns 20 candidates. A re-ranker filters to top 3, improving quality but adding latency.

**Quality impact:**
- Retrieval only (top 20): 70% of queries find the right answer in the candidate list
- Retrieval + re-ranking (top 3): 85-90% of queries surface the best answer
- Improvement: 15-25% quality gain

**Latency cost:**
- Re-ranker adds 100-200ms per query
- Acceptable for chatbot features (users wait). Not acceptable for autocomplete (must be <50ms)

**PM trade-off:**
- High-latency features (research assistant, summarization): always use re-ranking
- Low-latency features (search results, autocomplete): skip re-ranking or use a lightweight re-ranker
- Medium-latency features (chat): A/B test re-ranking vs. no re-ranking to find acceptable latency threshold

---

## How Invisible Stack Shows Up in Evals

When eval failures happen, trace them to the invisible layer that caused them:

**Poor retrieval** → Hallucinations (model makes up facts because retrieved docs are irrelevant)
- Symptom: "The AI said X, but the docs never mentioned X"
- Owner: Retrieval engineer, embedding choice, chunk strategy
- Fix: Improve retrieval quality before fixing the prompt

**Poor guardrails** → Safety failures (no layer prevents harmful outputs)
- Symptom: "The AI said something unsafe/off-brand/wrong"
- Owner: Constitution layer, safety rules, output validation
- Fix: Add missing guardrails

**Poor caching** → Cost explosion (same queries run repeatedly, eating budget)
- Symptom: "We're hitting token limits on cheap queries"
- Owner: Execution layer, cache strategy
- Fix: Implement caching or change query patterns

**Poor context assembly** → Context confusion (the model receives conflicting or old information)
- Symptom: "The AI contradicted itself between messages"
- Owner: Tracks layer, session state management
- Fix: Implement state versioning or clear session boundaries

**Every eval failure has a root layer.** Before blaming the model, identify which invisible layer failed.

---

## OUTPUT FORMAT

Use this template when auditing a feature:

```
## Invisible Stack Audit: [Feature Name]

| Layer | Exists? | Owner | Monitoring | Failure Mode | Improvement Priority |
|-------|---------|-------|-----------|--------------|-------------------|
| Constitution | Yes/No | [name] | [metric] | [what breaks] | [1-5] |
| Observations | Yes/No | [name] | [metric] | [what breaks] | [1-5] |
| Knowledge | Yes/No | [name] | [metric] | [what breaks] | [1-5] |
| Tracks | Yes/No | [name] | [metric] | [what breaks] | [1-5] |
| Equipment | Yes/No | [name] | [metric] | [what breaks] | [1-5] |
| Execution | Yes/No | [name] | [metric] | [what breaks] | [1-5] |
| Template | Yes/No | [name] | [metric] | [what breaks] | [1-5] |

**Weakest layer:** [identified with evidence]
**Retrieval quality score:** [estimated %]
**Latency budget:** [total ms, with per-layer breakdown]
```

---

## QUALITY GATE

- [ ] Full stack mapped — every layer between input and output identified
- [ ] Each layer has an owner and a monitoring mechanism
- [ ] Weakest layer identified with specific improvement plan
- [ ] Latency budget allocated across layers
- [ ] Missing layers explicitly acknowledged (with justification for why they're missing)
- [ ] Vector DB choice justified with unit economics
- [ ] Re-ranking strategy selected (yes/no) with latency rationale

## GENERATE THE DELIVERABLE

Follow the Deliverable Protocol from the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md), Section 11:

Deliverables for this skill take one of three formats:
1. **Document:** Invisible Stack Audit report (PDF or markdown) with full layer mapping, measurement protocol, audit findings, and improvement roadmap
2. **Presentation:** Slide deck summarizing the stack, weakest layer, and executive recommendations
3. **Spreadsheet:** Layer inventory with coverage/accuracy/latency metrics and improvement priorities

Always include:
- Complete stack diagram (use the OUTPUT FORMAT template or create visual via excalidraw-svg)
- Per-layer measurement baseline with thresholds
- Identified gaps and improvement roadmap with owners and timelines

## WHEN WRONG

- Simple prompt-and-response features with no retrieval or context
- Prototypes where validating the model's capability is the priority
- When stack complexity has become the bottleneck and simplification is needed

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
