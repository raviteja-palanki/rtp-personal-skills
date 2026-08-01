# AI PM Technical Concept Library

The technical depth a PM needs to pass the AI PM technical round. Every concept here is written to one bar: **enough to be a credible partner to research and engineering, not enough to be mistaken for one.** For each concept you get the mechanism (what actually happens), the trade-off (what it costs), the number (a stat that proves you've been close to it), the interview framing (weak vs. strong answer), and the follow-up the interviewer will drop.

Use this file to (a) answer concept questions accurately, (b) generate correct follow-ups in a mock, and (c) fact-check a user's answer. Do not read it to the user in full — hand them the 90-second version.

> Numbers are current as of early 2026. Pricing, adoption, and benchmarks move fast — flag if stale.

**Table of contents**
1. How LLMs work: prediction, tokens, temperature
2. Why LLMs get things wrong: context window, hallucination, grounding
3. ML vs. LLM: choosing the model class
4. Tools, function calling, and MCP
5. Agents, workflows, orchestration, and skills
6. Routing and model selection
7. RAG and context engineering
8. Evals and grounding metrics
9. Unit economics and latency
10. GPUs, inference, and why Nvidia asks about them
11. Fine-tuning vs. RAG vs. prompting
12. Transformers and attention (the "how do transformers work" question)
13. Safety, redlines, and human-in-the-loop
14. Multimodality and embeddings
15. The 30-second glossary

---

## 1. How LLMs Work: Prediction, Tokens, Temperature

### The mechanism
An LLM never looks anything up. It scores the next **token** against a **probability distribution** and picks one — guess after guess, left to right. A token is a chunk of text, roughly ¾ of a word on average in English (common words are one token; rare words split into several). "Unbelievable" might be `un` + `believ` + `able`.

Ask it "the capital of France is" and it ranks every possible next token against everything it saw in training. "Paris" scores around 0.92 because that pairing appears constantly across the text it learned from — atlases, Wikipedia, trivia. It appends the chosen token to the sequence and repeats: the output it just produced becomes part of the input for the next guess. This is **autoregressive generation**.

Two consequences a PM must internalize:
- The model has no notion of "true," only "likely given training." Truth and likelihood usually coincide; when they diverge, you get a confident wrong answer (see §2).
- Generation is inherently sequential — each token depends on all prior tokens. That's why output latency scales with output length, and why streaming exists (§9).

### Temperature (and top-p)
One setting decides which ranked token actually gets picked: **temperature**.
- **Low temperature (→0):** plays it safe. Takes the top-ranked token almost every time. Same prompt → same answer. Use for extraction, classification, code, anything where you want determinism.
- **High temperature (→1+):** reaches for lower-ranked tokens more often. Output turns varied and surprising. Use for brainstorming, creative copy, diversity.
- **top-p (nucleus sampling):** a sibling knob — sample only from the smallest set of tokens whose probabilities sum to p (e.g., 0.9). Often tuned alongside temperature.

PM-relevant: temperature is a product lever, not just a research one. A "regenerate for a different answer" feature is temperature. A support bot that must be consistent runs low temperature. Non-determinism in your eval harness usually traces to temperature > 0.

### The number
Claude Opus 4.8 holds ~1M tokens of context — roughly 69% of the entire Harry Potter series in working memory at once. (Context window ≠ knowledge; see §2.)

### Interview framing
**Q (Google DeepMind / Gemini):** "Design a high-level system for how Gemini responds to a user query."
- **Weak:** "It processes the query and generates the best response."
- **Strong:** "Tokenize the input, run it through the model to get a probability distribution over next tokens, sample one based on temperature, append, repeat until a stop token. Around that core loop: retrieval to ground it in real documents, tool access for live data, and a safety filter on the way out. The interesting product decisions are in that 'around' layer — what you retrieve, which tools you expose, where the guardrails sit."

### The follow-up
"You said 'sample based on temperature.' A user complains your assistant gives a different answer every time they ask the same thing. What's happening and what do you change?" → temperature is too high; drop it toward 0 for consistency, or cache. Bonus: note the trade-off — lower temperature also makes it more repetitive and less able to recover from a bad opening token.

---

## 2. Why LLMs Get Things Wrong: Context Window, Hallucination, Grounding

Three linked ideas. Interviewers push hardest on hallucination.

### Context window
The model's built-in knowledge is **frozen at the end of training** (its "knowledge cutoff"). The **context window** is how much text it can hold in front of it during a single conversation — its working memory for that chat. Everything the model "knows" in a session is either baked into weights at training time or sitting in the context window right now.

Go past the window and the model can no longer hold all the text — early content falls out of view. Practical failure modes: the model "forgets" instructions from the top of a long chat, or performance sags in the middle of a very long context (the "lost in the middle" effect — models attend most reliably to the beginning and end).

### Hallucination — the one they push on
Because the model is only ever guessing the next likely token, it can guess wrong **with total confidence**. Ask for a fact it doesn't hold and it still hands you a clean, confident, wrong answer — producing the next likely word is the only move it has. It has no "I don't know" reflex unless training gave it one.

OpenAI's research frames this as **statistically inevitable**: hallucination is a byproduct of next-token training that better data alone cannot fully remove. Part of the cause is incentive — standard training and benchmarks reward a confident guess over an abstention, so models learn to always answer. Ungrounded factual recall runs **above a 50% error rate** on benchmarks like SimpleQA (hard, obscure facts).

The PM reframe that scores points: **this is the model working as designed, not a bug to prompt away.** A longer or sterner prompt does not fix it. You fix it structurally — with grounding.

### Grounding — the fix
Give the model real information to work from, instead of relying on frozen weights:
1. **Prompt** — put the facts directly in the context. (Cheapest. Works when the facts are few and known.)
2. **Retrieval (RAG)** — pull relevant documents into the prompt at query time. (For a corpus too big to paste; see §7.)
3. **Tools** — hand it a function that fetches live data. (When the answer must be current — prices, inventory, weather.)

This is the **grounding ladder**: ground only as much as the task requires. Start with a prompt, add retrieval if you need facts from a corpus, add a live tool if the answer must be up to date. Over-grounding costs latency and money; under-grounding costs correctness.

The craft of assembling that context well is **context engineering** (§7) — a lot of real AI product quality lives here.

### The numbers
- Ungrounded factual recall: **>50% error** on SimpleQA-style benchmarks.
- Well-grounded systems: hallucination can drop **below 1%** on grounded benchmarks.

### Interview framing
**Q (Anthropic / OpenAI / Gemini):** "Users complain the assistant is confident but wrong. How would you fix it?"
- **Strong:** "It's working as designed — it predicts the next likely token, it doesn't look anything up, so with nothing real to work from it produces something false with full confidence. Ungrounded recall is above 50% error on SimpleQA. So I ground it: retrieval for real documents, or a tool for live data — that drops hallucination below 1% on grounded benchmarks. Then I measure it two ways: **faithfulness** offline against a golden set (does the answer trace back to what I retrieved), and **escalation/correction rates** online. A sterner prompt does not fix this."

### The follow-up ladder
1. "How would you measure whether grounding is actually working?" → faithfulness (answer traces to retrieved text) AND retrieval quality (did we fetch the right snippet) — two different failures, don't chase one when it's the other. See §8.
2. "Retrieval is returning the wrong chunks 30% of the time. Where do you look?" → chunking strategy, embedding model, the query rewriting step, and the top-k. Retrieval quality, not the LLM.
3. "You've grounded it and it still hallucinates occasionally. Ship or not?" → depends on stakes; design a fallback path (abstain, cite sources, human-in-the-loop for high-risk answers). Never a deterministic PRD (§5, §13).

---

## 3. ML vs. LLM: Choosing the Model Class

The single most common AI PM technical question ("You're building churn prediction. LLM or ML model?"). It tests whether you reach for the frontier model reflexively or match the tool to the task.

### The mechanism / decision rule
- **Tabular prediction** (churn, fraud, credit risk, demand forecasting) — structured features, a clean label — belongs on **classical ML**, specifically **gradient boosted trees** (XGBoost, LightGBM). They're cheaper, faster, and **interpretable**: a tree can tell you *why* an account got flagged (feature importances, SHAP values). An LLM cannot answer "why wasn't this account flagged" in a way you'd stake a business on.
- **Language and generation** — turning a messy support ticket into a structured feature, drafting the save email, summarizing, classifying free text — is where the **LLM earns its seat**.
- **The real system is usually hybrid.** Trees predict; the LLM reads and writes. Don't force either-or.

### Why trees for tabular (the depth move)
Churn data is tabular: rows of accounts, columns of features (usage, tenure, tickets, plan), a binary label (churned / didn't). Gradient boosted trees are built for exactly this shape. They're cheaper to train and serve than an LLM, faster at inference, and — critically for a business — interpretable and easy to monitor and retrain. An LLM on tabular data is slower, pricier, non-deterministic, and opaque.

### The number
An LLM inference can cost 100–1000× a tree inference for the same tabular prediction, and the tree answers "why" out of the box. That interpretability is often a regulatory or trust requirement (lending, insurance), not a nice-to-have.

### Interview framing (the canonical A+ answer)
**Q:** "You're building churn prediction. LLM or ML?"
- **A+:** "ML model, but let me explain. Churn is tabular — structured features, a clean yes/no label. I'd put gradient boosted trees on it, XGBoost, because they're cheaper, faster, and more interpretable. The first question after I ship is *why didn't an account get flagged* — trees answer that well, an LLM does not. Where an LLM earns a seat is the language layer — turning messy support tickets into a feature, or drafting the save email once an account trips the threshold. So the real system is hybrid. Trees predict, the LLM reads and writes."
- Why it lands: commits (ML), shows depth ("tabular," "clean label"), shows experience ("I'd put… the first question after I ship…"), shows nuance (hybrid), stays short.

### The follow-up
1. "When would you NOT use trees here?" → if you have almost no labeled churn data but rich text signals, or if the value is entirely in explaining/acting in language. Also if features are unstructured (raw text, images) and you can't engineer good tabular features.
2. "How do you evaluate the tree vs. how do you evaluate the LLM part?" → tree: AUC/precision-recall on a holdout, calibration, drift monitoring. LLM: faithfulness/quality evals on the generated text (§8). Two different eval regimes in one system.

---

## 4. Tools, Function Calling, and MCP

### The mechanism — three steps, every time
Feature answers "what's the weather in Austin?" Three steps:
1. **The model decides.** It's shown a `get_weather` tool with a name, a description, and a JSON **schema** for its arguments (e.g., `location`). It matches the question to that description and outputs a **structured request**: `get_weather(location="Austin")`. Crucially, **the model does not run anything** — it emits an intent.
2. **Your code executes.** Your application makes the actual API call and gets back `"68°F, cloudy."` This runs in your infrastructure, not the model's.
3. **You validate, then the model writes.** The model can call the wrong tool or pass a bad argument (wrong city). Your code checks the result before passing it back for the model to write the final sentence using that real data.

The one-line version that scores: **the intelligence is in deciding to call and with what; execution and validation live in your code.** Most people get this backwards and think the model runs the API.

### The failure mode: tool confusion
If one tool is `get_customer_profile` and another is `lookup_customer`, both described as "retrieving customer details," the model has a much harder time picking — it starts guessing. Tool selection accuracy can **drop to 13.62%** with a large, undifferentiated tool list, then **more than triple to 43.13%** once retrieval narrows the options to the relevant few (arXiv 2505.03275). Claude Code's own docs confirm the drop-off past **30–50 tools** loaded at once. PM takeaways: clear, differentiated tool descriptions are a real product surface; and past a few dozen tools you need **tool retrieval** (fetch only the relevant tools into context per query), not one giant list.

### Why MCP exists
Before **MCP (Model Context Protocol)**, every tool needed a custom integration with every model — an N×M mess of adapters. MCP, Anthropic's open standard (Nov 2024), replaced that with one interface: closer to a USB-C port than a pile of adapters. A tool built as an MCP server works with any MCP-compatible model.

Adoption tells the story: from ~**100,000 monthly SDK downloads** at launch (Nov 2024) to ~**97 million by March 2026**. By December 2025, OpenAI, Google, Microsoft, and AWS had joined Anthropic in governing it through the Linux Foundation.

**The honest PM take:** standing up your own MCP server is real engineering lift without a platform team. For most PMs the higher-leverage skill is learning to **configure and evaluate existing connectors well**, not to claim you built infrastructure.

### Interview framing
**Q (common everywhere):** "Your AI feature calls a tool. Walk me through what actually happens under the hood."
- **Weak:** "The model calls the API and returns the result."
- **Strong:** "The model never runs the tool — that's the part most people get backwards. I give it a list of tools, each with a name, a description, and a JSON schema for arguments. The description is what it uses to decide when to reach for one, so a vague description is a real bug. When it decides, its output is a structured request — function name plus arguments. My code runs that, validates the result, and passes it back for the model to write the final answer. The intelligence is in deciding to call and with what. Execution and validation live in my code — which is where I check it, because it can absolutely pass the wrong argument."

### The follow-up
1. "Two tools do almost the same thing. What happens?" → selection accuracy craters (13.62% figure); fix with differentiated descriptions and tool retrieval past ~30–50 tools.
2. "Does orchestration come into this?" (a trap — see §5) → No, for a single `get_weather` call: request → your code runs it → response. Orchestration shows up only when the loop stops being a single step (multiple tools to sequence, retries, state across turns, multiple agents to route between). Reaching for the sophisticated answer here fails the question.

---

## 5. Agents, Workflows, Orchestration, and Skills

"If you think agents are just advanced prompts, this section is for you."

### The definition that matters (Anthropic's line on determinism)
- A **workflow** follows predefined, deterministic paths — prompt chains, routing, verifier loops. You wrote the control flow.
- An **agent** dynamically directs its own process, with no fixed path — it decides what to do next, in a loop, until it judges the task done.

Anthropic's engineering guidance is blunt: **find the simplest solution possible, and only increase complexity when needed.** Most "agent" problems are better served by a deterministic workflow. Autonomy is a cost (unpredictability, harder eval, higher token spend), not a feature you add for its own sake.

### The three layers of an agent
Take a Slack digest agent that summarizes unread channels every morning:
1. **Instruction** — the system prompt that persists across the session ("group by channel, flag anything urgent first").
2. **Tools** — the APIs/MCPs it's allowed to call (here, the Slack API to read messages).
3. **Skill** — packaged know-how for the whole task, reusable across sessions: what counts as urgent, how to format the digest, when to ask a clarifying question instead of guessing.

A **skill**, in practice, holds: routing logic (which prior context matters), a context health check (confirm what's already known), and structure rules (format, tone, what to ask first). It's the reusable expertise layer that survives across sessions — the thing this very file is an example of.

### Common orchestration patterns (know the names)
- **Prompt chaining** — output of step 1 feeds step 2 (draft → critique → revise). Deterministic.
- **Routing** — classify the input, send it down a specialized path (§6).
- **Parallelization** — fan out subtasks, gather results (map-reduce, or voting for reliability).
- **Orchestrator-workers** — a lead model decomposes a task and dispatches sub-agents.
- **Evaluator-optimizer / verifier loop** — one model generates, another checks against criteria, loop until it passes.

### LangChain / LangGraph — when to reach for it
LangChain is the glue around the model: prompt templates, output parsers, memory, retrievers, piped together. For a **single call, prompt in / model out**, it adds nothing but debugging overhead — every extra abstraction layer hides where an error actually happened; a raw SDK call is simpler and easier to debug. It earns its place once you have **many steps, swappable pieces, memory, and tool use to coordinate.** Note the split: LangChain (chains) vs. **LangGraph** (stateful, graph-based agent orchestration) — for agents, reach for LangGraph. n8n covers no-code workflow automation; it tops out when logic gets genuinely dynamic.

### Interview framing
**Q (Glean, DeepMind):** "What's an agent? / Have you built any end-to-end agentic systems?"
- **Weak:** "It's an AI that uses a really good prompt to figure out what to do."
- **Strong:** "Three layers — the system prompt for standing instructions, the tools it's allowed to call, and a skill layer for packaged know-how that survives across sessions. And I'd start with a deterministic workflow, then only add autonomy where a fixed path genuinely fails. Anthropic's own guidance is find the simplest solution and only add complexity when needed — most 'agent' problems are really workflow problems."

### The follow-up
1. "When would you NOT build an agent?" → whenever a deterministic workflow does the job; autonomy costs predictability, eval difficulty, and tokens.
2. "You chain three model calls. Would you use LangChain?" → depends on step count and reuse; for three static steps a raw SDK is more debuggable; adopt the framework when you have memory/tools/swappable components; use LangGraph for stateful agents.

---

## 6. Routing and Model Selection

### The mechanism
A **router** is a function: query comes in, a decision comes out, the right chain runs. Route "what's my order status" to a cheap small model; route "why was I charged twice and I need this fixed now" to a model that can actually reason through an angry, multi-part complaint.

Two patterns dominate:
- **Model routing** — small/cheap models for easy work, large models for hard work. The router can be a classifier, a small LLM, or even rules.
- **Intent routing** — classify what the user wants, send it down a separate path, so billing never touches technical support.

### The number that justifies the whole exercise
- A trained router (RouteLLM) can **cut costs by over 85%** on MT-Bench while holding most of a stronger model's quality.
- **GPT-4o** costs **$2.50 / 1M input tokens** and **$10.00 / 1M output**; **GPT-4o mini** is **$0.15 / $0.60** — roughly **17× cheaper both ways.** Route "what is 2+2" to the frontier model and you pay a 17× premium for capability the question never needed. Multiply by millions of queries/month and it stops being a rounding error.
- Brian Armstrong (Coinbase CEO): they route prompts to cheaper models where appropriate and have kept costs "roughly flat" while token usage grows exponentially.

### The PM angle
For price-sensitive markets (India, APAC — anywhere token cost is a bigger share of unit economics), routing is closer to a **shipping requirement** than a nice-to-have. The trade-off to name: an aggressive router occasionally misroutes a hard query to a weak model and produces a bad answer — so you need a **confidence threshold and a fallback/escalation path** (send to the strong model if the cheap one is uncertain), and you monitor misroute rate.

### Interview framing
**Q:** "How would you cut the cost of an LLM feature without gutting quality?"
- **Strong:** "Routing. Most queries are easy — I'd classify intent and difficulty up front and send the easy majority to a small model, reserving the frontier model for genuinely hard queries. RouteLLM-style routing cuts cost 85%+ on MT-Bench while holding most of the quality, and GPT-4o vs. 4o-mini is a 17× spread, so this is real money at scale. The risk is misrouting a hard query to a weak model, so I'd set a confidence threshold with escalation to the strong model, and monitor misroute rate as a guardrail metric."

### The follow-up
"How do you decide the routing threshold?" → it's a precision/cost trade-off you tune empirically on a labeled set: too aggressive saves money but raises bad-answer rate; too conservative wastes the savings. Tie the threshold to a quality floor (e.g., don't let task-resolution drop below X).

---

## 7. RAG and Context Engineering

### The mechanism
**RAG (Retrieval-Augmented Generation)** grounds the model in a corpus too big to fit in context. The pipeline:
1. **Ingest / index (offline):** chunk your documents, embed each chunk into a vector (a list of numbers capturing meaning) with an embedding model, store vectors in a **vector database** (Pinecone, Weaviate, pgvector).
2. **Retrieve (at query time):** embed the user's query, find the nearest chunks by vector similarity (semantic search), often combined with keyword search (**hybrid search**) and a **reranker** that reorders the top candidates for relevance.
3. **Augment:** stuff the retrieved chunks into the prompt as context.
4. **Generate:** the model answers using those chunks, ideally citing them.

### Where RAG actually breaks (the depth move)
Naming these separates people who've built RAG from people who've read about it:
- **Chunking** — too big and you dilute relevance and blow context; too small and you fragment meaning across chunks. Chunk strategy (fixed size, semantic, by section) is a real tuning surface.
- **Embedding/retrieval quality** — the wrong chunks retrieved is the #1 RAG failure. Fixes: better embedding model, hybrid (keyword + semantic) search, query rewriting, and a reranker.
- **The reranker** — cheap retrieval casts a wide net (high recall); a reranker (a cross-encoder) reorders for precision. Retrieve 50, rerank to the best 5.
- **Context assembly** — order matters ("lost in the middle"); dedupe; leave room for the answer.

### Context engineering
The broader craft of assembling everything in the model's context window well — system prompt, retrieved docs, tool results, conversation history, output format — so the model has exactly what it needs and no more. Related failure the interviewer may probe: **context rot / distraction**, where stuffing too much marginally-relevant text *degrades* answers. More context is not always better.

### RAG vs. fine-tuning vs. prompting (see also §11)
- **Prompting** — cheapest, for behavior/format and small known facts.
- **RAG** — for knowledge: facts that change, are too large for context, or need citations. Update the corpus, not the model.
- **Fine-tuning** — for *behavior/style/format* the model can't be prompted into, or to bake in a narrow skill. Does NOT reliably add fresh factual knowledge and can't cite sources — a common misconception the interviewer will test.

### The number
Grounding via retrieval takes ungrounded recall from **>50% error** down toward **<1%** on grounded benchmarks — the same numbers as §2, because RAG *is* grounding at corpus scale.

### Interview framing
**Q (Perplexity):** "Explain how RAG works." **Q (Nvidia):** "Design a RAG system on Nvidia infrastructure with latency, relevance, and cost trade-offs."
- **Strong (Perplexity):** "The model can't hold the whole corpus and its knowledge is frozen at training, so I retrieve. Offline I chunk and embed documents into a vector store. At query time I embed the query, pull the nearest chunks — usually hybrid keyword-plus-semantic search with a reranker on top — stuff them into the prompt, and have the model answer with citations. The thing that makes or breaks it isn't the LLM, it's retrieval quality: chunking and the reranker. If the answers are wrong, I look there before I touch the prompt."
- **Nvidia add-on:** "The trade-offs are the three axes you named. Latency: retrieval + a reranker adds hops, so I'd cache embeddings, keep the vector index in GPU memory for ANN search, and cap top-k. Relevance: hybrid search + reranking buys accuracy at the cost of that latency. Cost: bigger retrieval and bigger generation models cost more per query, so I'd route — small model for simple lookups, large model only when the query needs synthesis."

### The follow-up ladder
1. "Answers are wrong. Is it retrieval or generation?" → check faithfulness (does the answer trace to retrieved text) vs. retrieval quality (did we fetch the right chunk) — §8. Different fixes.
2. "How do you improve retrieval?" → chunking, embedding model, hybrid search, query rewriting, reranker, top-k tuning.
3. "Why not just fine-tune on the docs?" → fine-tuning doesn't reliably inject fresh facts or cite; RAG lets you update the corpus and attribute sources.

---

## 8. Evals and Grounding Metrics

The day-two playbook. This is where AI PMs separate from traditional PMs, and where "confident but vague" answers die.

### Offline vs. online
- **Offline evals** run against a fixed **golden set** (a curated set of inputs with known-good outputs or graded criteria) before you ship and on every change. They catch regressions.
- **Online evals** run in production on real traffic. They catch drift and real-world failure the golden set never imagined.

### Core metrics a PM should name
- **Faithfulness / groundedness** — does the answer trace back to the retrieved/provided source? (Catches hallucination in RAG.)
- **Retrieval quality** — precision/recall of the retrieved chunks (did we fetch the right context at all?). Faithfulness and retrieval quality are **different failures** — a faithful answer to the wrong chunk is still wrong. Don't chase one when it's the other.
- **Answer relevance / correctness** — did it actually answer the question, correctly?
- **Task resolution / task success** — did the user get what they came for? The north-star output metric for most assistants (contrast with input metrics — see mistakes).
- **Online signals:** escalation rate (to human/strong model), correction/regeneration rate, thumbs up/down, deflection rate, containment rate.

### LLM-as-judge
You can't human-grade every output at scale, so you use an **LLM-as-judge**: a model scores outputs against a rubric. Cheap and scalable, but it has known biases (verbosity bias — prefers longer answers; position bias — prefers the first option; self-preference — prefers its own style). You **calibrate the judge against human labels** on a sample before trusting it, and you keep humans in the loop for high-stakes grading. Naming these biases is a strong depth signal.

### The right instinct under pressure (this scores higher than a confident guess)
"Honestly, I'd confirm the exact metric with the team before locking one in. My instinct is two separate checks — faithfulness (does the answer trace to the retrieved text) and retrieval quality (did we pull the right snippet). Those are different failures and I wouldn't want to chase one when it's the other." Naming the edge of your knowledge and what you'd check beats a confident wrong metric every time.

### Interview framing
**Q (Meta):** "Whiteboard an evaluation framework for [an AI feature], including human-in-the-loop feedback."
- **Strong:** "Two layers. Offline: a golden set of representative inputs with graded criteria — faithfulness, correctness, format — run on every model or prompt change to catch regressions, scored by an LLM-judge that I've first calibrated against human labels so I trust it. Online: task-resolution as the north star plus guardrail signals — escalation rate, correction rate, thumbs-down — sampled for human review, and those human labels flow back to expand the golden set. Human-in-the-loop sits at two points: calibrating the judge, and reviewing the online sample."

### The follow-up
1. "Your north-star metric is up. How do you know the model is quietly getting worse?" → north-star can rise while quality drops (e.g., users retry more, or a cohort shifts). Watch the guardrails: correction/regeneration rate, escalation rate, faithfulness on a rolling sample, and segment the metric. Silent degradation is the AI PM's nightmare — design for it.
2. "How do you trust an LLM-judge?" → calibrate against human labels, measure judge-human agreement, watch for verbosity/position/self-preference bias.

---

## 9. Unit Economics and Latency

The business layer. Increasingly asked directly ("Walk me through the unit economics of an LLM feature").

### Cost mechanics
You pay per **token**, split into **input** (prompt, including retrieved context and tool results) and **output** (generation), with **output typically 3–5× the input price.** So:
- **Cost per inference ≈ (input tokens × input price) + (output tokens × output price).**
- Long system prompts, big RAG contexts, and verbose outputs all show up directly in COGS. A bloated prompt is a margin problem.
- **Prompt caching** cuts cost dramatically when a large prefix (system prompt, few-shot examples, a big document) repeats across calls — cached input tokens are far cheaper (often ~10× cheaper) than fresh ones. A major lever for chat and RAG.
- **Reference prices (early 2026):** GPT-4o ≈ $2.50/$10.00 per 1M in/out; GPT-4o mini ≈ $0.15/$0.60 (~17× cheaper). This gap is why routing (§6) is real money.

### Latency mechanics
- **TTFT (time to first token)** — how long until the first token appears. Dominated by prompt processing (prefill) and retrieval hops. Streaming exists to hide this: show tokens as they generate so perceived latency ≈ TTFT, not total time.
- **TPOT / tokens-per-second** — generation speed after the first token. Output length × per-token time = the bulk of total latency.
- **p50 vs. p95/p99** — always design to the tail. p95 latency is what your angriest users feel; a great p50 with an ugly p95 is a bad product.
- Latency levers: smaller/faster model (routing), shorter outputs (max tokens, terser prompts), streaming, caching, parallel retrieval, speculative decoding.

### How cost + latency change what you build
- A real-time UX (autocomplete, voice) has a hard latency budget → smaller models, tight outputs, aggressive caching, maybe no reranker.
- A batch/back-office task (nightly summarization) can use a big model and long context because latency doesn't matter and you optimize purely for cost/quality.
- High-volume consumer at thin margins → routing and caching are survival, not polish.

### Interview framing
**Q (Microsoft, Amazon):** "Walk me through the unit economics of an LLM feature. How do cost per inference and p95 latency change what you build?"
- **Strong:** "Cost per inference is input tokens times input price plus output tokens times output price, and output runs 3–5× the input price — so my system prompt, my RAG context, and how verbose I let the model be all land straight in COGS. At volume I'd cache the repeating prefix — often ~10× cheaper on those tokens — and route the easy majority to a small model; GPT-4o to 4o-mini is a 17× spread. On latency I design to p95, not p50, and I stream to hide time-to-first-token. If it's a real-time surface I'll trade some quality for speed — smaller model, shorter outputs, maybe drop the reranker; if it's batch I'll spend latency for quality and optimize purely on cost."

### The follow-up
"Your feature is losing money per user. What levers do you pull, in order?" → (1) cut prompt/context bloat and output length, (2) prompt caching, (3) routing to cheaper models, (4) smaller fine-tuned model for the narrow task, (5) rate limits / usage-based pricing if the value supports it. Order matters: kill waste before you re-architect.

---

## 10. GPUs, Inference, and Why Nvidia Asks

Nvidia (and infra-heavy roles) probe hardware. You don't need to be an ML systems engineer — you need to know why GPUs matter and where the bottlenecks are.

### The mechanism
Neural networks are enormous stacks of **matrix multiplications**. **GPUs** do thousands of these in parallel (vs. a CPU's handful of fast serial cores), which is why deep learning runs on them. Training and inference are both matmul-bound.

- **Training** — one giant, parallel job across many GPUs for weeks/months; the expensive one-time (per model) cost.
- **Inference** — running the trained model to serve users; the recurring cost that dominates a deployed product's bill. Inference is often **memory-bandwidth-bound**, not compute-bound: the bottleneck is moving weights and the **KV cache** (the stored attention state for the tokens so far) in and out of GPU memory.

### Levers PMs should recognize
- **Quantization** — store weights in lower precision (FP16 → INT8/INT4) to cut memory and speed inference, at a small accuracy cost. A key cost lever.
- **Batching** — serve many requests together to keep the GPU busy (throughput vs. latency trade-off; continuous batching is the modern approach).
- **KV cache** — memory grows with context length and concurrency; it's why long contexts and many concurrent users are expensive.
- **VRAM is the constraint** — a model must fit in GPU memory; bigger models need more/bigger GPUs (H100/H200/Blackwell), which is the supply story behind Nvidia's ~$5T market cap.

### Interview framing
**Q (Nvidia):** "Explain how GPUs are used in deep learning."
- **Strong:** "Neural nets are billions of matrix multiplications, and GPUs do those massively in parallel — thousands of cores versus a CPU's few — which is the whole reason deep learning is practical. Two regimes: training is one huge parallel job across many GPUs, the big one-time cost; inference is the recurring cost of serving users, and it's usually memory-bandwidth-bound, not compute-bound — the bottleneck is shuttling weights and the KV cache through GPU memory. So the product levers are quantization to shrink the memory footprint, batching to keep the GPUs saturated, and watching VRAM, because the model has to fit."

### The follow-up
"Your inference costs are too high. What do you do?" → quantize, batch better (continuous batching), route to smaller models, cap context/output length (shrinks the KV cache), and consider distillation. Note the latency/throughput trade-off in batching.

---

## 11. Fine-tuning vs. RAG vs. Prompting

A frequent trade-off question; people conflate the three.

| | What it changes | Best for | Cost / effort | Can add fresh facts? | Cites sources? |
|---|---|---|---|---|---|
| **Prompting** | Nothing (runtime instruction) | Behavior, format, small known facts, fast iteration | Lowest | Only what you paste | If you provide them |
| **RAG** | The context (runtime) | Knowledge that's large, changing, or needs citations | Medium (build/maintain a pipeline) | **Yes** — update the corpus | **Yes** |
| **Fine-tuning** | The weights (offline training) | Style, tone, format, a narrow specialized skill, latency (smaller model matches a bigger one on the narrow task) | Highest (data + training + eval + redeploy) | **No** (not reliably) | **No** |

### The rule
Start at the bottom of the ladder. Prompt first. Add RAG when you need knowledge. Fine-tune only when prompting + RAG can't get the behavior/format/skill you need, or when you want a small cheap model to match a big one on a narrow task. **The #1 misconception (and interview trap): "we'll fine-tune it on our docs so it knows our data."** Fine-tuning teaches *behavior*, not *facts* — for facts that update and need attribution, RAG is the tool. You can combine: fine-tune for format/skill AND RAG for knowledge.

### Interview framing
**Q:** "The model doesn't know our internal product. Fine-tune or RAG?"
- **Strong:** "RAG, almost certainly. Fine-tuning bakes in behavior and style, not fresh facts — and it can't cite, which internal-knowledge answers usually need. Our docs also change, so I'd rather update a corpus than retrain a model every week. I'd reach for fine-tuning only if the problem were tone or format, or if I wanted a small cheap model to match a big one on one narrow task — and even then I'd RAG the knowledge on top."

### The follow-up
"When IS fine-tuning worth it?" → narrow, stable task where prompting is too unreliable or too expensive at scale (a small fine-tuned classifier beating few-shot on a huge frontier model), a specific output format/style, or latency/cost from serving a much smaller model. Never for volatile facts.

---

## 12. Transformers and Attention (the "how do transformers work" question)

Nvidia and Glean both ask this. You do NOT derive it — you explain it at the level that proves you understand what you build on.

### The mechanism at PM depth
A **transformer** is the neural network architecture behind modern LLMs (the "T" in GPT). The one idea that matters: **attention.** When processing a token, the model computes how much every other token in the context should influence it — it "attends" to the relevant ones. In "the animal didn't cross the street because *it* was too tired," attention is what lets the model resolve "it" to "animal." **Self-attention** does this across the whole sequence in parallel — which is exactly what makes transformers GPU-friendly and scalable, unlike the older sequential RNNs.

Layers you can name:
- **Embeddings** — tokens become vectors.
- **Positional encoding** — since attention is order-agnostic by default, position info is added so the model knows word order.
- **Attention (multi-head)** — multiple attention "heads" learn different relationships (syntax, coreference, etc.).
- **Feed-forward layers** — process the attended representations.
- Stack N of these blocks; the final layer produces the probability distribution over the next token (§1).

The scaling story: transformers parallelize (attention over the whole sequence at once), so they ride Moore's-law-plus-GPU scaling in a way RNNs couldn't — which is why "attention is all you need" (2017) unlocked the LLM era. The cost: attention is **O(n²)** in sequence length (every token attends to every other), which is why long context is expensive and why efficient-attention research exists.

### Interview framing
**Q (Nvidia, Glean):** "How do transformers work?"
- **Strong:** "The core idea is attention. For each token, the model weighs how much every other token in the context should influence it — that's how it resolves what 'it' refers to, or which earlier fact matters here. Self-attention does that across the whole sequence in parallel, which is what makes transformers scale on GPUs where the older sequential models couldn't. Architecturally: tokens get embedded, position gets added, then a stack of attention-plus-feed-forward blocks, and the final layer emits a probability distribution over the next token. The catch is attention is quadratic in sequence length, which is why long context costs so much."
- Then STOP. You've shown you understand it as a builder. Do NOT derive the softmax or the Q/K/V math unless asked — going deeper than the archetype wants is a markdown (Mistake 6).

### The follow-up
1. "Why did transformers beat RNNs?" → parallelism (whole sequence at once vs. sequential), better long-range dependencies via attention → trainable at scale on GPUs.
2. "Why is long context expensive?" → attention is O(n²) in length; KV cache memory grows with context (§10).

---

## 13. Safety, Redlines, and Human-in-the-Loop

Anthropic and safety-forward companies probe this. It's also the mark of an AI PM vs. a traditional one (Mistake 5: the deterministic PRD).

### The mechanism / PM frame
The model is confidently wrong some fraction of the time, by design. So an AI product must be **designed for being wrong**:
- **Fallback / graceful degradation** — what happens when the model fails or is low-confidence: abstain, ask a clarifying question, hand to a human, show sources, offer a deterministic path.
- **Human-in-the-loop (HITL)** — a person reviews or approves high-stakes outputs (medical, legal, financial, irreversible actions). Design *where* the human sits (pre-approval vs. spot-check vs. escalation).
- **Guardrails** — input filters (block disallowed requests) and output filters (safety classifier on the way out, §1's "safety filter").
- **Redline** — a capability threshold a model must NOT cross (e.g., providing actionable bioweapon uplift, autonomous self-exfiltration). Defining a redline means specifying the capability, how you'd measure it (evals/red-teaming), and the response if a model approaches it (don't deploy, add mitigations, restrict access).

### Interview framing
**Q (Anthropic):** "How would you define a 'redline' for a model capability?" / "How would you handle hallucinations in a generative model deployed to users?"
- **Strong (redline):** "A redline is a capability the model must never have in deployment — something like meaningful uplift on a bioweapon, or the ability to act autonomously in ways we can't oversee. Defining one means three things: specify the capability precisely enough to test, build an eval or red-team protocol to measure how close the model is, and pre-commit to a response if it approaches the line — don't ship, add mitigations, or gate access. The point is the decision is made before the capability exists, not after."
- **Strong (hallucination, deployed):** As §2, plus: "Because it's confidently wrong by design, my PRD has a fallback path — cite sources so users can verify, abstain or escalate when retrieval confidence is low, and human review for high-stakes answers. A spec that assumes the output is always right is the single biggest tell of a traditional PM in an AI role."

### The follow-up
"Users trust it too much (automation bias). What do you do?" → surface uncertainty and sources, make verification easy, design friction for high-stakes actions, and measure over-reliance (do users catch the model's errors?).

---

## 14. Multimodality and Embeddings

### Multimodality
Models that handle more than text — images, audio, video, in and out. Mechanism at PM depth: non-text inputs are encoded into the same representation space the model reasons over (an image becomes a sequence of tokens/patches). Product implications: new input modalities (screenshot → answer, voice → action), higher token cost (images are many tokens), and new eval and safety surfaces. "Design a system for Gemini to answer a query with an image" → tokenize/encode the image alongside text, attend jointly, generate.

### Embeddings
A number vector capturing the meaning of text (or an image), such that similar meanings sit near each other in vector space. The workhorse behind RAG retrieval (§7), semantic search, clustering, classification, and recommendations. PM-relevant: choosing/evaluating the embedding model is a real lever on retrieval quality; embeddings are cheap to compute and store relative to generation.

### Interview framing
**Q:** "How does semantic search work vs. keyword search?"
- **Strong:** "Keyword search matches literal terms; semantic search matches meaning. You embed the query and the documents into the same vector space and return nearest neighbors, so 'how do I cancel' finds a doc titled 'ending your subscription' even with no shared words. In practice I'd run hybrid — keyword for exact matches like error codes and IDs, semantic for intent — then rerank. Pure semantic misses exact strings; pure keyword misses paraphrase."

---

## 15. The 30-Second Glossary

Fast definitions for mid-answer recall. Each is a phrase you can drop correctly.

- **Token** — ~¾ of a word; the unit the model reads and generates.
- **Autoregressive** — generates one token at a time, each conditioned on all prior tokens.
- **Temperature** — randomness knob; low = deterministic, high = varied.
- **Context window** — working memory for one conversation; knowledge outside it must be retrieved or is frozen in weights.
- **Knowledge cutoff** — the date training data ends; the model knows nothing after it without grounding.
- **Hallucination** — a confident, plausible, wrong output; statistically inevitable from next-token training.
- **Grounding** — giving the model real info (prompt/retrieval/tools) so it doesn't rely on frozen weights.
- **RAG** — retrieval-augmented generation; grounding against a corpus via embeddings + vector search.
- **Embedding** — a meaning-vector; nearby vectors = similar meaning.
- **Vector database** — stores embeddings for fast nearest-neighbor (semantic) search.
- **Reranker** — reorders retrieved candidates for precision (retrieve wide, rerank narrow).
- **Chunking** — splitting documents for embedding; a top RAG failure surface.
- **Faithfulness** — does the answer trace to the retrieved source (RAG's core quality metric).
- **Golden set** — curated eval inputs with known-good outputs; the offline regression harness.
- **LLM-as-judge** — a model grading outputs against a rubric; calibrate against humans; watch verbosity/position/self bias.
- **Function calling / tools** — the model emits a structured request; YOUR code executes and validates.
- **MCP** — Model Context Protocol; open standard so any tool works with any model (USB-C for tools).
- **Agent vs. workflow** — agent directs its own path dynamically; workflow follows a fixed, deterministic path. Prefer the simplest.
- **Orchestration** — coordinating multiple steps/tools/agents (sequencing, retries, state, routing).
- **Skill** — packaged, reusable task know-how (routing logic + context checks + structure rules) that persists across sessions.
- **Router** — a function that sends each query to the right (often cheapest sufficient) model or path.
- **Fine-tuning** — updating weights for behavior/style/skill; NOT a reliable way to add fresh facts.
- **Quantization** — lower-precision weights to cut memory/cost at small accuracy loss.
- **KV cache** — stored attention state for prior tokens; grows with context length and concurrency (a cost driver).
- **TTFT / TPOT** — time to first token / time per output token; stream to hide TTFT; design to p95.
- **Prompt caching** — reuse a repeated prompt prefix cheaply (~10× off cached tokens).
- **Gradient boosted trees (XGBoost)** — the default for tabular prediction; cheap, fast, interpretable.
- **Attention** — the transformer's core: weigh how much each token influences each other token; O(n²) in length.
- **Redline** — a capability a model must not cross in deployment; defined, measured, and pre-committed against.
- **HITL** — human-in-the-loop; a person reviews/approves high-stakes outputs.
- **Task resolution** — did the user get what they came for; the north-star output metric (not sessions/prompts).
