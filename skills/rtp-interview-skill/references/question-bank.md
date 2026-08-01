# AI PM Technical Interview Question Bank

Real and realistic questions for the AI PM technical round, organized two ways: **by company** (with each company's style and archetype) and **by topic** (with follow-up ladders). Every question is tagged: what it **tests**, **difficulty** (1 = warm-up, 3 = deep), and the **archetype** it favors (E = Engineer in the Room wants mechanism; P = Product-Layer PM wants what-you-do-with-it).

Use this to select questions in a mock, to hand practice sets to the user, and to generate the *right* follow-up (the follow-up ladder is the point of this round).

Concept references in brackets like [§4] point to `concepts.md`. Model answers for the starred (★) questions are in `model-answers.md`.

---

## PART A — By Company

Match the archetype to the company. Depth-lab and infra companies run "Engineer in the Room." Applied-AI product companies lean "Product-Layer PM." Most run a blend; when in doubt, open Product-Layer and drop a level when the candidate handles it.

### OpenAI — archetype: Engineer in the Room (with product judgment)
Style: probes mechanism and definitions, then jumps to product strategy on capability. Expect a crisp definitional question followed by a "what would you do with it" strategy question.
1. ★ Define hallucinations in LLMs. [§2] — tests mechanism understanding. Diff 2. E.
2. ★ You have a model with 10× the capability at 10× the cost. What do you do with it? — tests product strategy under a capability/cost trade-off. Diff 3. P. (Where does 10× capability create 10×+ value: complex agentic workflows, high-stakes reasoning, coding, research — not "what's 2+2." Segment by willingness-to-pay and task value; route.)
3. How would you reduce hallucination in a deployed assistant? [§2] Diff 2. E→P.
4. Walk me through what happens between a user's prompt and the response. [§1] Diff 2. E.
5. How would you measure whether a new model is actually better for our users? [§8] Diff 3. P.

### Anthropic — archetype: Engineer in the Room + Safety
Style: mechanism plus safety/alignment framing. They want to see you design for the model being wrong, and reason about capability thresholds.
1. ★ How would you handle hallucinations in a generative AI model deployed to users? [§2, §13] Diff 2. E→P.
2. ★ How would you define a "redline" for a model capability? [§13] Diff 3. P/E.
3. How do you evaluate whether a safety mitigation is working without killing usefulness? [§8, §13] Diff 3. P.
4. When is human-in-the-loop worth the cost, and where do you put the human? [§13] Diff 2. P.
5. How would you think about the trade-off between helpfulness and harmlessness in a product? [§13] Diff 3. P.

### Google DeepMind / Gemini — archetype: Engineer in the Room
Style: system design of the model's response path, plus "what have you actually built."
1. ★ Design a high-level system for how Gemini responds to a user query. [§1, §2, §7] Diff 3. E.
2. What AI agents have you built to make yourself more productive? [§5] — tests hands-on experience; be specific and real. Diff 2. P.
3. Users say Gemini is confident but wrong. How would you fix it? [§2] Diff 2. E→P.
4. How would you design multimodal query handling (text + image)? [§14] Diff 3. E.
5. How would you decide what to cache vs. recompute in a high-QPS assistant? [§9] Diff 3. E.

### Nvidia — archetype: Engineer in the Room (infra-heavy)
Style: hardware and infrastructure depth. This is the most technical of the set. If you can't talk GPUs and inference cost, you're in trouble.
1. ★ Explain how GPUs are used in deep learning applications. [§10] Diff 3. E.
2. ★ Design a RAG system on Nvidia infrastructure with latency, relevance, and cost trade-offs. [§7, §9, §10] Diff 3. E.
3. Your inference costs are too high. Walk me through the levers. [§9, §10] Diff 3. E.
4. Training vs. inference — where does the cost live in a deployed product, and why? [§10] Diff 2. E.
5. How do transformers work? [§12] Diff 3. E.
6. Why is long context expensive? [§10, §12] Diff 3. E.

### Perplexity — archetype: Engineer in the Room (retrieval-focused)
Style: RAG, retrieval quality, grounding, citations. It's an answer engine, so retrieval is the whole game.
1. ★ Explain how RAG works. [§7] Diff 2. E.
2. Answers are citing the wrong sources. Retrieval or generation problem? [§7, §8] Diff 3. E.
3. How would you improve retrieval quality? [§7] Diff 3. E.
4. How do you keep an answer engine fresh when the world changes hourly? [§2, §7] Diff 2. P.
5. Semantic vs. keyword search — when each? [§14] Diff 2. E.

### Glean — archetype: Engineer in the Room (agentic + enterprise RAG)
Style: end-to-end agentic systems, enterprise search, permissions.
1. ★ Have you built any end-to-end agentic systems? Walk me through one. [§5] Diff 3. E/P.
2. How do transformers work? [§12] Diff 3. E.
3. Design enterprise search that respects per-user document permissions. [§7] Diff 3. E/P. (Retrieval must filter by ACL *before* the model sees content — a security-in-RAG depth signal.)
4. Workflow or agent for [a given enterprise task]? [§5] Diff 3. P.
5. How would you evaluate an enterprise AI assistant where every customer's data is different? [§8] Diff 3. P.

### Microsoft — archetype: Product-Layer PM
Style: model selection trade-offs and system design of an AI experience, framed around product decisions.
1. ★ Explain the trade-offs in model selection. [§6, §11] Diff 2. P.
2. Walk me through the system design of an AI-powered experience. [§1–§9] Diff 3. P/E.
3. ★ Walk me through the unit economics of an LLM feature. [§9] Diff 3. P.
4. When would you fine-tune vs. RAG vs. prompt? [§11] Diff 2. P/E.
5. How do you decide which model to ship on for a new feature? [§6, §9] Diff 2. P.

### Amazon — archetype: Product-Layer PM + Dive Deep
Style: behavioral-technical hybrid. "Tell me about a time you went deep into an ML system." Ties technical depth to their Leadership Principles (Dive Deep, Ownership).
1. ★ Tell me about a time you had to go several layers deep into an ML system or AI infrastructure to diagnose and solve a problem. [§2–§10] Diff 3. P/E. (STAR structure + real mechanism. This is where technical depth meets behavioral.)
2. Walk me through the unit economics of an LLM feature. [§9] Diff 3. P.
3. A model in production silently degraded. How did you catch it / how would you? [§8] Diff 3. P.
4. How do you decide what's a good task for an LLM vs. not? [§3] Diff 2. P/E.

### Meta — archetype: Product-Layer PM (metrics-forward)
Style: evaluation frameworks, human-in-the-loop feedback, prototyping.
1. ★ Whiteboard an evaluation framework for an AI feature, including human-in-the-loop feedback. [§8] Diff 3. P.
2. You ship an assistant and the north-star metric goes up. How would you know the model is quietly getting worse anyway? [§8] Diff 3. P.
3. Design a prompt-chain prototype for [a task] and tell me how you'd test it. [§5, §8] Diff 2. P/E.
4. What metrics tell you an AI feature is actually working (vs. vanity)? [§8] Diff 2. P.

---

## PART B — By Topic

Each topic lists questions with follow-up ladders. The ladder is how a real interviewer pushes "one level deeper on the weakest part." Use it in mocks.

### Topic 1 — How LLMs work [§1]
1. ★ Walk me through what happens from prompt to response. Diff 2. E.
   - Ladder: "You said 'it predicts the next token' — predicts from what?" → training distribution, not a lookup. → "A user gets a different answer every time. Why?" → temperature. → "How would you make it deterministic and what do you lose?" → temp→0, lose diversity/recovery.
2. What is temperature and when would you change it? Diff 1. E.
   - Ladder: "You're building a legal-doc extractor. What temperature and why?" → low/0 for consistency.
3. What's a token and why does it matter for cost and latency? Diff 1. E→P.
   - Ladder: "So how does that change how you'd write a system prompt?" → shorter prompts = lower COGS [§9].

### Topic 2 — Hallucination & grounding [§2]
1. ★ Why do models hallucinate, and as a PM what's your move? Diff 2. E→P.
   - Ladder: "So just write a better prompt?" (trap) → no, grounding is structural. → "How do you measure grounding?" → faithfulness + retrieval quality [§8]. → "Grounded and it still occasionally lies. Ship?" → fallback path, stakes-based.
2. ★ Users complain the assistant is confident but wrong. Fix it. Diff 2. E→P.
   - Ladder: as above; then "retrieval returns wrong chunks 30% of the time — where do you look?" → chunking, embeddings, reranker, top-k.
3. What's the difference between the context window and the model's knowledge? Diff 2. E.
   - Ladder: "Your 500-page doc doesn't fit. Options?" → chunk + RAG, or a long-context model; trade-offs of each.

### Topic 3 — ML vs LLM [§3]
1. ★ You're building churn prediction. LLM or ML? Diff 2. E→P. (The canonical question.)
   - Ladder: "When would you NOT use trees here?" → sparse labels, value is in language, unstructured features. → "How do you evaluate each half of the hybrid?" → AUC/PR + drift for the tree; faithfulness/quality for the LLM.
2. How do you decide what's a good task for an LLM vs. not? Diff 2. E→P.
   - Ladder: "Give me one of each from a product you know." → forces real experience.
3. Fraud detection — LLM or ML? Diff 2. E.
   - Ladder: same tabular logic; then "where does the LLM help fraud at all?" → reading unstructured evidence, drafting analyst summaries.

### Topic 4 — Tools, function calling, MCP [§4]
1. ★ Your AI feature calls a tool. Walk me through what actually happens under the hood. Diff 2. E.
   - Ladder: "Where's the intelligence and where's your code?" → deciding = model; executing/validating = your code. → "Two tools do the same thing. What happens?" → selection accuracy craters (13.62%). → "Does orchestration come into this?" (trap) → no, single call.
2. What is MCP and why does it exist? Diff 2. P/E.
   - Ladder: "Would you build your own MCP server?" → honest: real eng lift; configure/eval existing connectors first.
3. Your agent keeps calling the wrong tool. Diagnose. Diff 3. E.
   - Ladder: tool descriptions, count (>30–50 → retrieval), argument schemas, validation layer.

### Topic 5 — Agents & orchestration [§5]
1. ★ What's an agent? / Have you built an end-to-end agentic system? Diff 2–3. E/P.
   - Ladder: "When would you NOT build an agent?" → workflow suffices; autonomy costs predictability/eval/tokens. → "It fails 1 in 10 runs. What do you add?" → verifier loop, retries, guardrails, HITL for high-stakes.
2. Workflow vs. agent — how do you decide? Diff 2. P.
   - Ladder: give a concrete task; make them classify and justify.
3. Would you use LangChain here? Diff 2. E.
   - Ladder: "Single call — yes or no?" → no, raw SDK; "now it's 6 steps with memory and tools?" → yes / LangGraph for agents.
4. Explain the three layers of an agent. Diff 2. E.
   - Ladder: "Where does a 'skill' live and what's in it?" → reusable know-how: routing + context check + structure rules.

### Topic 6 — Routing & model selection [§6, §11]
1. ★ How would you cut LLM costs without gutting quality? Diff 2. P.
   - Ladder: "How do you set the routing threshold?" → precision/cost trade-off on a labeled set, tied to a quality floor. → "A hard query gets misrouted to the weak model. Now what?" → confidence threshold + escalation.
2. Explain the trade-offs in model selection. Diff 2. P.
   - Ladder: cost, latency, quality, context length, tool-use ability, privacy/hosting; make them weight for a specific product.
3. When would you fine-tune instead of prompt or RAG? Diff 2. P/E.
   - Ladder: "We want it to know our internal docs — fine-tune?" (trap) → no, RAG; fine-tuning ≠ fresh facts.

### Topic 7 — RAG & context engineering [§7]
1. ★ Explain how RAG works. Diff 2. E.
   - Ladder: "Answers are wrong — retrieval or generation?" → faithfulness vs. retrieval quality. → "Improve retrieval." → chunking, hybrid search, reranker, query rewrite. → "Why not fine-tune on the docs?" → facts vs. behavior.
2. ★ Design a RAG system with latency, relevance, cost trade-offs. Diff 3. E.
   - Ladder: push on each axis; then "what do you cache?" → embeddings, frequent queries [§9].
3. When does adding more context HURT? Diff 3. E.
   - Ladder: context rot / lost-in-the-middle; relevance beats volume.

### Topic 8 — Evals & metrics [§8]
1. ★ Whiteboard an eval framework with human-in-the-loop. Diff 3. P.
   - Ladder: "Offline set — what's in it?" → golden set, graded criteria. → "How do you trust an LLM-judge?" → calibrate vs. human, watch verbosity/position/self bias. → "North-star's up but is it worse?" → guardrail signals, segment.
2. ★ North-star metric went up — how do you know the model is quietly getting worse? Diff 3. P.
   - Ladder: correction/regeneration rate, escalation rate, rolling faithfulness, cohort segmentation.
3. What's the difference between input metrics and success metrics for an AI feature? Diff 2. P. (Mistake 3 territory.)
   - Ladder: sessions/prompts served = input; task resolution = success. "Which would you put on the dashboard the CEO sees?"

### Topic 9 — Unit economics & latency [§9]
1. ★ Walk me through the unit economics of an LLM feature. Diff 3. P.
   - Ladder: "It's losing money per user — levers in order?" → cut context/output, cache, route, small fine-tuned model, pricing. → "How does p95 latency change the build?" → real-time vs. batch design.
2. Cost per inference — what drives it? Diff 2. P.
   - Ladder: input+output tokens, output priced 3–5× input, context size, caching.
3. Design for a hard latency budget (voice assistant). Diff 3. E/P.
   - Ladder: TTFT, streaming, smaller model, drop reranker, cap output.

### Topic 10 — GPUs & inference [§10]
1. ★ Explain how GPUs are used in deep learning. Diff 3. E.
   - Ladder: "Training vs. inference cost — which dominates a live product?" → inference (recurring). → "Inference is too expensive — what do you do?" → quantize, batch, route, cap context/KV cache.
2. Why is inference often memory-bandwidth-bound? Diff 3. E.
   - Ladder: weights + KV cache movement; quantization and batching as fixes.

### Topic 11 — Transformers [§12]
1. ★ How do transformers work? Diff 3. E.
   - Ladder: "Why did they beat RNNs?" → parallel attention, long-range deps, GPU-scalable. → "Why is long context expensive?" → O(n²) attention + KV cache.
2. What is attention, in one breath? Diff 2. E.
   - Ladder: "Give me a sentence where attention matters." → coreference ("it" → "animal").

### Topic 12 — Safety & redlines [§13]
1. ★ Define a redline for a model capability. Diff 3. P/E.
   - Ladder: "How would you measure the model approaching it?" → evals/red-teaming. → "It's close — what do you do?" → don't ship / mitigate / gate.
2. Users over-trust the model (automation bias). What do you do? Diff 2. P.
   - Ladder: surface uncertainty + sources, friction for high-stakes, measure over-reliance.

---

## PART C — Balanced Mock Sets (ready to run)

Pre-built 5-question sequences spanning the core areas. Each opens easy, escalates, and ends on a synthesis question. Use for a default mock when no company is specified.

**Set 1 — Generalist AI PM (Product-Layer archetype)**
1. How do you decide what's a good task for an LLM vs. not? [§3]
2. Users say the assistant is confident but wrong. Fix it. [§2]
3. Your feature calls a tool — what actually happens under the hood? [§4]
4. Walk me through the unit economics, and how p95 latency changes the build. [§9]
5. North-star's up — how do you know the model is quietly getting worse? [§8]

**Set 2 — Deep technical / infra (Engineer in the Room)**
1. How do transformers work? [§12]
2. Explain how GPUs are used in deep learning. [§10]
3. Design a RAG system with latency, relevance, cost trade-offs. [§7, §9]
4. Your inference costs are too high — levers, in order. [§9, §10]
5. LLM or ML for churn — and how do you evaluate each half? [§3, §8]

**Set 3 — Applied product (Product-Layer, metrics-forward)**
1. Explain how RAG works. [§7]
2. Whiteboard an eval framework with human-in-the-loop. [§8]
3. How would you cut LLM cost without gutting quality? [§6]
4. Fine-tune, RAG, or prompt for our internal knowledge? [§11]
5. What's an agent, and when would you NOT build one? [§5]

**Set 4 — Safety-forward (Anthropic-style)**
1. Why do models hallucinate — and your move as PM? [§2]
2. How would you define a redline for a model capability? [§13]
3. When is human-in-the-loop worth the cost, and where does the human sit? [§13]
4. How do you measure a safety mitigation without killing usefulness? [§8, §13]
5. Design a deployed assistant's fallback path for when it's confidently wrong. [§2, §13]
