# AI PM interview question bank

Use this bank to choose a relevant question and a meaningful follow-up. **E** means mechanism emphasis; **P** means product-decision emphasis. Difficulty **1–3** is a local practice estimate, not an employer rating. Section references point to the numbered topics in [the concept guide](concepts.md). Selected examples appear in [the model answers](model-answers.md); not every question has a corresponding answer.

## Part A — Company preparation groups

These groups combine historical reports with realistic practice extensions. The source is Aakash Gupta and Prasad Reddy’s [July 22, 2026 article](https://www.news.aakashg.com/p/ai-pm-technical-interview). The short note for each company identifies the reported seed topics. Treat the full lists as practice questions, not verified transcripts or current hiring rubrics. Confirm the actual role and rounds with current company or recruiter information. No company is restricted to one interviewer lens.

### OpenAI

The July 2026 report mentions hallucination definitions and a capability/cost strategy question. The remaining questions extend those topics for practice.

1. Define hallucinations in LLMs. [§2] — tests mechanism understanding. Diff 2. E.
2. You have a model with 10× the capability at 10× the cost. What do you do with it? — tests product strategy under a capability/cost trade-off. Diff 3. P.
3. How would you reduce hallucination in a deployed assistant? [§2] Diff 2. E→P.
4. Walk me through what happens between a user's prompt and the response. [§1] Diff 2. E.
5. How would you measure whether a new model is actually better for our users? [§8] Diff 3. P.

### Anthropic

The report mentions hallucination handling and capability redlines. The remaining questions extend those topics for practice.

1. How would you handle hallucinations in a generative AI model deployed to users? [§2, §13] Diff 2. E→P.
2. How would you define a "redline" for a model capability? [§13] Diff 3. P/E.
3. How do you evaluate whether a safety mitigation is working without killing usefulness? [§8, §13] Diff 3. P.
4. When is human-in-the-loop worth the cost, and where do you put the human? [§13] Diff 2. P.
5. How would you think about the trade-off between helpfulness and harmlessness in a product? [§13] Diff 3. P.

### Google DeepMind / Gemini

The report mentions agent-building experience and a high-level Gemini response design. The remaining questions extend those topics for practice.

1. Propose a high-level design for a Gemini-like assistant responding to a user query; distinguish your proposal from its actual architecture. [§1, §2, §7] Diff 3. E.
2. What AI agents have you built to make yourself more productive? [§5] — tests hands-on experience; be specific and real. Diff 2. P.
3. Users say Gemini is confident but wrong. How would you fix it? [§2] Diff 2. E→P.
4. How would you design multimodal query handling (text + image)? [§14] Diff 3. E.
5. How would you decide what to cache vs. recompute in a high-QPS assistant? [§9] Diff 3. E.

### Nvidia

The report mentions GPU use and RAG system design. The remaining questions extend those topics for practice.

1. Explain how GPUs are used in deep learning applications. [§10] Diff 3. E.
2. Design a RAG system on Nvidia infrastructure with latency, relevance, and cost trade-offs. [§7, §9, §10] Diff 3. E.
3. Your inference costs are too high. Walk me through the levers. [§9, §10] Diff 3. E.
4. Training vs. inference — where does the cost live in a deployed product, and why? [§10] Diff 2. E.
5. How do transformers work? [§12] Diff 3. E.
6. Why is long context expensive? [§10, §12] Diff 3. E.

### Perplexity

The report mentions explaining RAG. The remaining questions extend those topics for practice.

1. Explain how RAG works. [§7] Diff 2. E.
2. Answers are citing the wrong sources. Retrieval or generation problem? [§7, §8] Diff 3. E.
3. How would you improve retrieval quality? [§7] Diff 3. E.
4. How do you keep an answer engine fresh when the world changes hourly? [§2, §7] Diff 2. P.
5. Semantic vs. keyword search — when each? [§14] Diff 2. E.

### Glean

The report mentions end-to-end agentic systems. The remaining questions extend those topics for practice.

1. Have you built any end-to-end agentic systems? Walk me through one. [§5] Diff 3. E/P.
2. How do transformers work? [§12] Diff 3. E.
3. Design enterprise search that respects per-user document permissions. [§7] Diff 3. E/P. Check authorization before evidence reaches the model, including caches.
4. Workflow or agent for [a given enterprise task]? [§5] Diff 3. P.
5. How would you evaluate an enterprise AI assistant where every customer's data is different? [§8] Diff 3. P.

### Microsoft

The report mentions model-selection trade-offs and AI experience design. The remaining questions extend those topics for practice.

1. Explain the trade-offs in model selection. [§6, §11] Diff 2. P.
2. Walk me through the system design of an AI-powered experience. [§1–§9] Diff 3. P/E.
3. Walk me through the unit economics of an LLM feature. [§9] Diff 3. P.
4. When would you fine-tune vs. RAG vs. prompt? [§11] Diff 2. P/E.
5. How do you decide which model to ship on for a new feature? [§6, §9] Diff 2. P.

### Amazon

The report mentions a behavioral example of going deep into an ML system. The remaining questions extend those topics for practice.

1. Tell me about a time you had to go several layers deep into an ML system or AI infrastructure to diagnose and solve a problem. [§2–§10] Diff 3. P/E. Use a real story with precise ownership and mechanism.
2. Walk me through the unit economics of an LLM feature. [§9] Diff 3. P.
3. A model in production silently degraded. How did you catch it / how would you? [§8] Diff 3. P.
4. How do you decide what's a good task for an LLM vs. not? [§3] Diff 2. P/E.

### Meta

The report mentions evaluation, human feedback, and prompt prototyping. The remaining questions extend those topics for practice.

1. Whiteboard an evaluation framework for an AI feature, including human-in-the-loop feedback. [§8] Diff 3. P.
2. You ship an assistant and the north-star metric goes up. How would you know the model is quietly getting worse anyway? [§8] Diff 3. P.
3. Design a prompt-chain prototype for [a task] and tell me how you'd test it. [§5, §8] Diff 2. P/E.
4. What metrics tell you an AI feature is actually working (vs. vanity)? [§8] Diff 2. P.

## Part B — By topic

Each question has a suggested follow-up. Select the part that tests the candidate’s actual reasoning gap; the notes are discussion guidance, not a single required answer.

### Topic 1 — How LLMs work [§1]

1. Walk me through what happens from prompt to response. Diff 2. E.
   - Follow-up: What information conditions the next token? Then explain variation from sampling, request context, retrieval, or serving changes. What consistency can you test, and what does temperature zero fail to guarantee?
2. What is temperature and when would you change it? Diff 1. E.
   - Follow-up: For a document extractor, choose supported sampling settings and test schema compliance and correctness. Lower sampling variation is not proof of accuracy.
3. What's a token and why does it matter for cost and latency? Diff 1. E→P.
   - Follow-up: How would unnecessary prompt or output tokens affect this product? Use its actual pricing and workload; preserve instructions and evidence needed for quality.

### Topic 2 — Hallucination & grounding [§2]

1. Why do models hallucinate, and as a PM what's your move? Diff 2. E→P.
   - Follow-up: What can prompting improve, and what needs source, retrieval, or system changes? Measure support and correctness separately. Define the fallback and release conditions for the task’s consequences.
2. Users complain the assistant is confident but wrong. Fix it. Diff 2. E→P.
   - Follow-up: Suppose 30% of retrieved chunks are judged wrong in a defined sample. Check the labels, source coverage, parsing, permissions, query interpretation, retrieval, and ranking before choosing a fix.
3. What's the difference between the context window and the model's knowledge? Diff 2. E.
   - Follow-up: A 500-page document does not fit: compare selective retrieval, a larger supported context, staged processing, and traceable summaries. Evaluate relevant omissions and cost.

### Topic 3 — ML vs LLM [§3]

1. You're building churn prediction. LLM or another predictive ML method? Diff 2. E→P.
   - Follow-up: When would the data or task favor another approach? Evaluate prediction with suitable discrimination and calibration measures, language processing with task-specific checks, and the complete intervention with user outcomes.
2. How do you decide what's a good task for an LLM vs. not? Diff 2. E→P.
   - Follow-up: Give one suitable and one unsuitable task from a product you understand. Distinguish direct experience from an observed or hypothetical example.
3. Fraud detection — LLM or another predictive ML method? Diff 2. E.
   - Follow-up: Compare structured fraud prediction with reading unstructured evidence or drafting an analyst summary. What evaluation and action controls does each need?

### Topic 4 — Tools, function calling, MCP [§4]

1. Your AI feature calls a tool. Walk me through what actually happens under the hood. Diff 2. E.
   - Follow-up: Where are arguments validated and actions authorized? How would you inspect overlapping tools or an ambiguous write outcome? Coordination can occur even for one call; there is no terminology trap or universal selection accuracy.
2. What is MCP and why does it exist? Diff 2. P/E.
   - Follow-up: Would an existing connector meet the task and control requirements? Explain when a custom MCP server is worth building and which compatibility, permission, and maintenance questions remain.
3. Your agent keeps calling the wrong tool. Diagnose. Diff 3. E.
   - Follow-up: Inspect examples of wrong selections, descriptions, capability overlap, argument schemas, authorization, and runtime errors. Consider tool retrieval if evaluation supports it, not at a fixed tool-count threshold.

### Topic 5 — Agents & orchestration [§5]

1. What's an agent? / Have you built an end-to-end agentic system? Diff 2–3. E/P.
   - Follow-up: When would a fixed workflow suffice? If one in ten test runs fails, classify failures and consequences before choosing verification, recovery, restrictions, or review. Retries alone may repeat the error.
2. Workflow vs. agent — how do you decide? Diff 2. P.
   - Follow-up: Choose a concrete task and explain which decisions are predetermined, which can be dynamic, and what bounds the system. A workflow can still contain variable model outputs.
3. Would you use LangChain here? Diff 2. E.
   - Follow-up: For a single call and then a multi-step stateful task, compare a raw SDK with available framework features. Explain the concrete benefit and dependency cost rather than imposing a call-count rule.
4. Explain the instructions, tools, and skills shorthand for an agent, and what else a working system needs. Diff 2. E.
   - Follow-up: Explain instructions, tools, and reusable skills as a teaching shorthand. Then identify the runtime, state, permissions, evaluation, and budgets needed for a working system.

### Topic 6 — Routing & model selection [§6, §11]

1. How would you cut LLM costs without gutting quality? Diff 2. P.
   - Follow-up: Set routing rules from representative evaluation and a quality requirement. Measure misroutes, routing overhead, escalation cost, and unrecovered failures; do not assume confidence is calibrated.
2. Explain the trade-offs in model selection. Diff 2. P.
   - Follow-up: Weight quality, total cost, latency, context, tools, modalities, privacy, hosting, and support for the specific product. What constraint eliminates an otherwise strong model?
3. When would you fine-tune instead of prompt or RAG? Diff 2. P/E.
   - Follow-up: For internal documents, compare freshness, provenance, update cost, and behavior needs. Retrieval is often useful for changing facts; fine-tuning can encode information and may complement it.

### Topic 7 — RAG & context engineering [§7]

1. Explain how RAG works. Diff 2. E.
   - Follow-up: Separate retrieval quality, source truth and freshness, answer faithfulness, citation support, and end-task correctness. Diagnose before choosing parsing, hybrid search, ranking, prompt, or training changes.
2. Design a RAG system with latency, relevance, cost trade-offs. Diff 3. E.
   - Follow-up: Explain the latency, relevance, and cost effects of each stage. What could be cached, how would it expire, and how would permission changes be enforced?
3. When does adding more context HURT? Diff 3. E.
   - Follow-up: Test relevance, conflicting material, context placement, and model limits on the actual task. More context is not always harmful or always helpful; avoid universal context-rot thresholds.

### Topic 8 — Evals & metrics [§8]

1. Whiteboard an eval framework with human-in-the-loop. Diff 3. P.
   - Follow-up: Define representative offline cases and a held-out set. Validate judge agreement and bias, then inspect important cohorts and guardrails alongside production outcomes.
2. North-star metric went up — how do you know the model is quietly getting worse? Diff 3. P.
   - Follow-up: Inspect correction, repetition, escalation, faithfulness, and completion by cohort. Explain alternative interpretations: regeneration can mean exploration and escalation can be the intended safe result.
3. What's the difference between input metrics and success metrics for an AI feature? Diff 2. P.
   - Follow-up: Choose a meaningful outcome and diagnostic measures for the actual task. Verified resolution, accuracy, or satisfaction may matter; volume alone does not prove value.

### Topic 9 — Unit economics & latency [§9]

1. Walk me through the unit economics of an LLM feature. Diff 3. P.
   - Follow-up: Calculate the largest cost drivers before prioritizing levers. Explain relevant latency percentiles, interactive response needs, and batch deadlines rather than assuming one universal order or p95 target.
2. Cost per inference — what drives it? Diff 2. P.
   - Follow-up: Use actual input, output, cache, and tool prices with their units. Include retries and infrastructure where relevant; output-price ratios and cache discounts vary.
3. Design for a hard latency budget (voice assistant). Diff 3. E/P.
   - Follow-up: Measure the complete voice path, including initial wait, ongoing generation, and tools. Streaming shows partial output after it begins; it does not itself eliminate TTFT. Test quality effects of model, retrieval, or output changes.

### Topic 10 — GPUs & inference [§10]

1. Explain how GPUs are used in deep learning. Diff 3. E.
   - Follow-up: Compare lifetime training and serving workloads. Diagnose compute, bandwidth, memory capacity, and utilization before considering quantization, batching, model choice, or context changes.
2. Why is inference often memory-bandwidth-bound? Diff 3. E.
   - Follow-up: Explain when weight and KV-cache movement can limit decoding. Why might prompt processing or a different batch and hardware configuration have a different bottleneck?

### Topic 11 — Transformers [§12]

1. How do transformers work? Diff 3. E.
   - Follow-up: Explain parallel training with causal masking, sequential autoregressive generation, and the relevant attention and cache costs. Distinguish dense-attention scaling from every operation in every architecture.
2. What is attention, in one breath? Diff 2. E.
   - Follow-up: Use a pronoun example to illustrate contextual relationships. Do not claim that a single attention weight proves why the model answered as it did.

### Topic 12 — Safety & redlines [§13]

1. Define a redline for a model capability. Diff 3. P/E.
   - Follow-up: Define the risk, measurement, deployment conditions, decision owner, and required response. Verify current policy before assigning a company-specific threshold or action.
2. Users over-trust the model (automation bias). What do you do? Diff 2. P.
   - Follow-up: Combine appropriate evidence, uncertainty, action controls, and review. Test whether users make better decisions; disclaimers and friction alone do not establish reduced over-reliance.

---

## Part C — Balanced mock sets

Pre-built 5-question sequences spanning the core areas. The sets sample different kinds of reasoning; adjust their order and difficulty to the candidate and role. Use for a default mock when no company is specified.

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
4. Your inference costs are too high — diagnose the drivers and prioritize levers. [§9, §10]
5. LLM or another predictive ML method for churn — and how do you evaluate each half? [§3, §8]

**Set 3 — Applied product (Product-Layer, metrics-forward)**
1. Explain how RAG works. [§7]
2. Whiteboard an eval framework with human-in-the-loop. [§8]
3. How would you cut LLM cost without gutting quality? [§6]
4. Fine-tune, RAG, or prompt for our internal knowledge? [§11]
5. What's an agent, and when would you NOT build one? [§5]

**Set 4 — Safety-focused practice**
1. Why do models hallucinate — and your move as PM? [§2]
2. How would you define a redline for a model capability? [§13]
3. When is human-in-the-loop worth the cost, and where does the human sit? [§13]
4. How do you measure a safety mitigation without killing usefulness? [§8, §13]
5. Design a deployed assistant's fallback path for when it's confidently wrong. [§2, §13]

Use the [shared rubric](grading-rubric.md) after the agreed practice interval. Ask one question at a time. Five questions is a default, not a mandatory session length. The bank retains 44 company-group questions, 34 topic questions with follow-ups, and four five-question mock sets.
