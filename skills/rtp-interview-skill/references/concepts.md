# AI PM interview concept guide

Use the section needed for the question, then connect its mechanism to a product decision. Definitions support reasoning; they are not phrases to memorize or evidence that Ravi implemented a system. Examples are illustrative unless a dated source is attached. Verify live model specifications, prices, framework features, and company policies when preparing a particular answer.

## 1. How an LLM produces an answer

Most text-generation LLMs used in these examples are autoregressive: they produce a next-token distribution from the available input and previously generated output, choose a token, and continue. A token can be a word, part of a word, punctuation, or another encoded unit. English word-to-token approximations do not transfer reliably across languages, code, or modalities.

Training adjusts parameters so the model learns patterns and capabilities from data; later training can shape instruction following and other behavior. At inference, the model uses those parameters and the actual request context. It is not ordinarily looking up a stored sentence for every response. A deployed assistant may also retrieve documents, call tools, or use other components, so describing the model alone does not explain the whole product.

Temperature changes the distribution used in sampling. Lower values generally make sampling more concentrated; they do not guarantee that an entire deployed system returns identical answers. Model versions, numerical implementation, request context, retrieval, routing, and other sources of variation can matter. For extraction, test consistency and schema compliance; do not treat temperature zero as proof of correctness. For brainstorming, greater variation can be useful, but assess relevance too.

**Follow one level deeper:** what information was actually available in this request, what chose the next action, and which component introduced the variation? Avoid invented token probabilities or unsupported claims about a named model’s current context capacity.

## 2. Hallucination, knowledge, and context

A hallucination is false or unsupported generated content presented as an answer. Definitions vary by evaluation: distinguish factual correctness from support in a supplied source. Fluency and confidence do not establish truth. Training patterns, incomplete information, reasoning errors, and incentives to guess can contribute. It is too strong to say every deployment must hallucinate: abstention and bounded tasks can avoid particular errors, although reliability remains a practical challenge. [OpenAI’s research discussion](https://openai.com/index/why-language-models-hallucinate/) explains why rewarding guesses can discourage appropriate uncertainty.

**Weights** contain learned patterns; they are not an auditable database. A **knowledge cutoff** describes training-data coverage, not a guarantee of everything before that date or an inability to infer anything afterward. **Context** is the information available to a particular request. The application may select, summarize, or omit conversation history. If an input exceeds a limit, behavior depends on the system: an API may reject it, or the application may truncate or summarize it. It does not always silently drop the oldest content.

Grounding supplies task-relevant evidence through inputs, retrieval, or tools. It can improve reliability, but irrelevant, stale, unauthorized, or incorrect sources can still produce bad answers. Prompting, training, validation, uncertainty handling, and retrieval are complementary controls. A citation may be present yet fail to support the claim.

**Product response:** classify the failure; inspect available evidence and output; measure source support and correctness separately; repair the responsible stage; and choose clarification, abstention, escalation, or restricted use according to the task’s consequences. Monitor coverage as well as error rates so that refusing everything does not look like success.

For a document that does not fit, consider selective retrieval, a larger supported context, staged extraction, or summaries with traceability. Test omissions and relevance. More context can distract, but “lost in the middle” and context degradation are model- and task-dependent, not a universal fixed percentage threshold. Do not compare a closed-book benchmark’s error rate with a grounded product’s error rate as though they were a controlled treatment comparison.

## 3. Choosing predictive ML, an LLM, or a hybrid

An LLM is a kind of machine-learning model. The practical question is which method best serves the task. For labeled tabular churn prediction, compare sensible baselines such as rules, logistic regression, and gradient-boosted trees. Evaluate time-based splits, leakage, delayed labels, class imbalance, calibration, intervention value, latency, and operating cost.

Trees can be effective on tabular data, but an ensemble is not automatically transparent or causal. Feature-attribution tools describe a model’s associations; they do not establish that changing a feature will prevent churn. Sparse labels or substantial unstructured text may justify other approaches; they do not automatically make an LLM the winner.

A hybrid may extract structured signals from support text, use a predictive model to rank risk, and draft an explanation or action for review. Evaluate each stage and the resulting intervention: prediction quality, extraction accuracy, source support, decision usefulness, and customer outcome. Use analogous reasoning for fraud: fast structured detection and language-based evidence review can play different roles.

**Follow-up:** when would the simpler baseline win, and what evidence would change the choice? Avoid universal cost ratios or claims that one model family always wins.

## 4. Tools, function calling, and MCP

A typical tool interaction follows this sequence:

1. The application makes an allowed tool and its input schema available.
2. The model or application selects a tool and produces structured arguments.
3. The executing system validates arguments, authorization, scope, and relevant preconditions **before** execution.
4. The permitted executor performs the operation and returns a result or error.
5. The application records the outcome and decides whether to respond, continue, retry, or escalate.

Execution may run in your application, a provider service, or a remote tool server. A model’s valid-looking request is not permission to act. Treat tool results as data, not authority to replace governing instructions. For side effects, account for duplicate requests and ambiguous outcomes; verify whether a write occurred before retrying an unknown result.

Ambiguous descriptions, overlapping capabilities, poor schemas, stale tool definitions, and an unsuitable task can all cause wrong selections. Inspect failures before adding a framework or a tool-retrieval layer. Tool count alone does not supply a universal “30–50 tools” trigger. Even one tool call may involve orchestration in the ordinary sense of coordination; calling it orchestration is not a technical mistake.

**MCP** standardizes interactions between compatible hosts, clients, and servers that expose capabilities such as tools and resources. It reduces repeated integration work; it does not make every model support every tool or automatically solve authorization, reliability, or UX. Check the [current protocol specification](https://modelcontextprotocol.io/specification/latest) and the actual client’s capabilities. Reuse a suitable connector when it fits; build a server when the required capability or controls justify it.

**Research example, not a performance promise:** the May 2025 [RAG-MCP abstract](https://arxiv.org/abs/2505.03275) reports 43.13% tool-selection accuracy against a 13.62% baseline in its benchmark setting. That is not evidence that any pair of overlapping tools has 13.62% accuracy, or that the result generalizes to today’s models. Read the methods before using it to defend an architecture.

## 5. Agents, workflows, and orchestration

A useful design distinction concerns **who chooses the next step**. A workflow encodes much of the control path in advance; an agent gives the model more discretion to select actions within defined bounds. A workflow can contain probabilistic model outputs, and an agent can contain fixed steps. Neither label establishes a product’s risk or quality. This framing follows [Anthropic’s engineering guidance](https://www.anthropic.com/engineering/building-effective-agents).

Start with the simplest design that can complete the job. A fixed sequence is useful when the path is known; dynamic selection helps when relevant steps depend on what the system discovers. More autonomy adds state, permission, evaluation, latency, and recovery questions.

Keep five useful patterns available:

- **Prompt chaining:** break a task into stages with explicit intermediate checks.
- **Routing:** select a specialized path for the input.
- **Parallelization:** run independent work or perspectives, then reconcile results.
- **Orchestrator and workers:** allocate subtasks dynamically and integrate their results.
- **Evaluator and optimizer:** use feedback to revise output within a bounded loop.

Choose a pattern because it addresses a diagnosed need. Retries can repeat an error; a verifier can miss it. Set stopping conditions, budgets, permissions, and escalation paths, then measure the complete task.

The original three-layer teaching shorthand—**instructions, tools, and reusable skills**—helps describe what an agent draws on. A working system also needs a runtime and appropriate state, context, evaluation, and operational controls. A skill packages reusable task guidance; its availability across sessions depends on the host’s loading and persistence mechanisms.

A raw SDK can be sufficient for a small integration. LangChain, LangGraph, n8n, or another framework may help with particular integrations, state, or workflow needs. Do not make the number of calls a categorical framework rule or assume current capability limits without checking. Explain what the dependency buys and what complexity it introduces.

## 6. Routing and model selection

Select for the actual task: quality, latency distribution, total cost, context handling, tool reliability, supported modalities, privacy, deployment constraints, and operational support. Benchmark representative examples, difficult cases, and consequential segments. The latest or largest model is not automatically the right choice.

A router can send tasks to different models or paths. Set its decision rule using measured task performance and a quality requirement, accounting for misroutes, escalations, extra calls, and routing latency. Do not assume most queries are easy, that model confidence is calibrated, or that escalation recovers every error. Some tasks are better routed directly to a reliable method rather than tried cheaply first.

The [RouteLLM paper](https://arxiv.org/abs/2406.18665) reports cost reductions while preserving performance in its evaluated settings. Use that as evidence that routing can work, not a universal savings rate. Price ratios for old model pairs and attributed company cost anecdotes need a dated source before reuse. Calculate current economics from the prices and workloads at hand.

## 7. RAG and context engineering

Retrieval-augmented generation retrieves relevant information and uses it to support generation. It need not use a vector database: keyword search, hybrid search, SQL, and other authorized retrieval methods may fit. It can be useful even when a corpus fits in context, for relevance, freshness, access control, or cost.

Design the full path:

1. Ingest and update sources with identifiers, provenance, and permissions.
2. Parse or chunk where useful; preserve headings, tables, and relationships needed for interpretation.
3. Index using retrieval methods suited to the task.
4. Interpret or rewrite the query where justified, retrieve candidates, and enforce access before material reaches the model.
5. Rerank or filter when it improves quality enough to justify its cost.
6. Assemble the context with clear source boundaries; generate a supported response and useful citations.
7. Check output, record relevant evidence, and handle missing or conflicting information.

Retrieving 50 candidates and keeping five is an example to test, not a default truth. Retrieval and generation may run on different infrastructure; RAG does not require every component to occupy GPU memory.

Diagnose wrong answers with **retrieval relevance and coverage, source correctness and freshness, answer faithfulness, citation support, and end-task correctness**. High faithfulness with a wrong answer may mean the source itself is wrong. Low faithfulness may reflect generation behavior or confusing context. Improving retrieval may involve parsing, chunking, hybrid search, query interpretation, reranking, or metadata—not just a new embedding model.

Cache only with appropriate invalidation and permission checks. A previously authorized document or answer is not permanently authorized for every user. Fine-tuning and RAG can complement one another; fine-tuning can encode information, but updating volatile facts and tracing their provenance is often easier through retrieval.

## 8. Evaluation and product metrics

Define the user task and the failure consequences before choosing metrics. An offline evaluation set should represent normal work, hard cases, important cohorts, permission boundaries, and known failures. Some tasks have a known answer; open-ended tasks may need a rubric and expert assessment. Keep a held-out set and avoid tuning solely to the examples used for development.

Evaluate components where they aid diagnosis and the full system where the user experiences the result. Online evidence may include experiments, sampled review, incidents, and operational observations; not every production assessment is an A/B test.

LLM judges can scale review, but calibrate them against suitable human or objective evidence. Inspect disagreement and possible position, verbosity, or self-preference effects; these are risks to test, not laws that every judge always follows. Randomization and blinded review can help. Humans also disagree, so improve the rubric and adjudication rather than treating any one rating as infallible.

Pair a meaningful outcome with guardrails and diagnostic measures. Verified task resolution can be valuable; accuracy, customer satisfaction, retention, safety, and cost may also matter. Sessions or prompts alone do not establish value, while a correctly resolved ticket can be an outcome. Rising usage can coexist with deteriorating quality. Segment results and examine corrections, repeat attempts, escalation, unresolved work, latency, and supported-answer quality. A regeneration may express curiosity or preference rather than failure; an escalation may be the safe intended result.

## 9. Unit economics and latency

If prices are quoted per million tokens:

```text
uncached token cost = (input tokens × input price + output tokens × output price) / 1,000,000
cost per successful task = total relevant operating cost / verified successful tasks
```

Account separately for provider-specific cache reads and writes, tool charges, retries, retrieval, hosting, observability, and human work. Define the accounting period and what “successful” means. Output/input price ratios and cache discounts vary; do not memorize “3–5×” or “10×” as universal rules. A cache saves money only when reuse, pricing, freshness, and authorization support it.

Useful levers include reducing unnecessary context or output, eliminating redundant calls, caching appropriate work, routing, choosing a suitable smaller or adapted model, batching, changing the workflow, and revisiting pricing. Diagnose the dominant cost before ordering the levers. Compare quality and cost per outcome, not token price alone. A more expensive call can reduce total cost by avoiding retries or review.

**TTFT** is time to first token; **TPOT** is time per output token. Streaming displays output progressively after it starts; it does not by itself remove the initial wait or reduce total completion time. Measure the user-visible path, including tools and retrieval. A voice experience may need tight initial and ongoing response budgets; a batch job still has deadlines, throughput, and resource constraints.

Use percentiles appropriate to the service promise, and inspect tails and important cohorts. p95 is a useful measure, not a universal SLO. Removing a reranker or shortening output can improve latency while harming usefulness; test the effect. Required safety and correctness floors remain constraints, not benefits to trade away for speed.

## 10. GPUs, training, and inference

GPUs perform many suitable numerical operations in parallel and are useful for the matrix operations in deep learning. CPU and GPU “core” counts describe different architectures and are not directly comparable measures of performance.

Training repeatedly updates model parameters; inference uses a trained model to serve requests. Training cost may recur through new runs or adaptation, and inference cost accumulates with use. Which dominates depends on the system and its lifetime workload, not a universal rule.

Inference includes processing the prompt and generating output. Bottlenecks depend on phase, model, batch size, hardware, and context. Processing a large prompt can be compute intensive; incremental decoding can be limited by moving weights and attention state through memory. Do not describe all training and inference as either purely compute-bound or purely memory-bound.

Weights, activations, and stored attention state consume memory. A KV cache commonly avoids recomputing prior attention keys and values during decoding; its size and behavior depend on architecture, sequence length, and concurrency. Models may be sharded or offloaded rather than fitting on one GPU.

Quantization reduces numerical precision and can lower memory or bandwidth demands; measure its quality and performance effects. Batching can improve utilization but affect response latency. Routing, context management, model choice, and serving configuration also matter. Tie hardware choices to workload measurements rather than a vendor’s market valuation or a memorized hardware slogan.

## 11. Prompting, fine-tuning, or retrieval

**Prompting and context design** change the instructions and information supplied at runtime. They are often quick to test, but can materially change behavior and cost.

**Fine-tuning** changes parameters using training examples. It can improve behavior, format, task performance, or domain patterns, and can encode information. It is not a reliable substitute for a maintained source of rapidly changing facts; citations and provenance require deliberate design.

**Retrieval** makes relevant external information available at request time. It brings source and permission management, retrieval errors, and latency concerns.

Use the diagnosed problem, data, update frequency, evidence requirements, quality, and total cost to choose. There is no requirement to exhaust every prompt and RAG attempt before considering fine-tuning. A combination may be best; compare it with a simpler baseline and evaluate maintenance needs.

## 12. Transformers and attention

Transformers use attention and other learned layers to build contextual representations. Attention forms weighted combinations of available information using learned queries, keys, and values. Multiple heads allow different learned relationships; do not assign each head a guaranteed human-readable role such as “syntax.” Position information is represented in ways that vary by architecture.

In a causal text decoder, a prediction cannot attend to future output tokens. Training can process known sequence positions in parallel with masking; ordinary autoregressive generation still produces successive output tokens. Dense self-attention over an input sequence has quadratic attention interactions, but this does not mean every operation in every modern model or decoding step has the same scaling. [The original Transformer paper](https://arxiv.org/html/1706.03762) explains masking, attention, and the encoder–decoder architecture.

A pronoun-resolution example can illustrate the need to connect distant words. It does not prove that a particular attention weight is the causal explanation for an answer. In an interview, connect the architecture to parallel computation, context handling, serving cost, and actual product requirements.

## 13. Safety, redlines, and human review

A redline is a defined boundary on behavior, capability-related risk, or deployment conditions that triggers a specified response. State what is measured, in which setting, who owns the decision, and what action follows. A capability threshold may trigger stronger controls or restricted deployment rather than a claim that the model must never possess that capability. Consult current company policy before attributing a specific threshold or response to it.

Evaluate both harmful failures and unnecessary restrictions on legitimate use. Use representative tests, adversarial testing, monitoring, and independent review where appropriate. A threshold without a credible measurement and response process is incomplete.

Human review helps when the reviewer has the evidence, expertise, time, and authority to intervene. Place it before consequential actions when required; measure errors, review burden, and missed escalations. A review checkbox, generic disclaimer, or confident-looking probability does not establish safety. Address over-reliance with appropriate evidence, uncertainty, interaction design, and action controls, then test whether people make better decisions.

## 14. Multimodal systems and embeddings

Multimodal systems can process or produce combinations of text, images, audio, or other inputs. Their architectures, representations, limits, and pricing differ. A text-plus-image task requires attention to image resolution, relevant regions, source quality, ambiguity, and what the model can actually perceive; do not assume one universal token conversion or that all image requests cost more than all text requests.

An embedding maps an input into a numerical representation useful for a trained similarity task. Nearby vectors may indicate useful similarity, not guaranteed shared meaning, truth, or absence of bias. Vector search retrieves by that representation; keyword search preserves exact terms and identifiers. Hybrid search can combine their strengths. Compare retrieval quality on actual tasks rather than assuming semantic search is always superior or cheap enough to ignore.

## 15. The 30-second glossary

- **Token:** an encoded unit processed or generated by a model; not a fixed fraction of every language’s words.
- **Autoregressive:** generates successive output units conditioned on available earlier information.
- **Temperature:** a sampling control; lower values do not guarantee end-to-end determinism.
- **Context window:** the supported information capacity for a request, under the model and API’s rules.
- **Knowledge cutoff:** training-data coverage information, not a completeness or truth guarantee.
- **Hallucination:** false or unsupported generated content; define the evaluation criterion.
- **Grounding:** supplying relevant evidence to support an answer or action.
- **RAG:** generation supported by retrieved information; vectors are optional.
- **Embedding:** a learned numerical representation for tasks such as similarity.
- **Vector database:** a system for storing and searching vectors, often with metadata.
- **Reranker:** a method for reordering retrieved candidates by another relevance assessment.
- **Chunking:** dividing content into useful units while preserving necessary context.
- **Faithfulness:** support of an answer by the supplied source; not the same as source truth.
- **Golden set:** curated evaluation cases with reference answers or defined assessment criteria.
- **LLM-as-judge:** a model used to assess outputs under a rubric that requires validation.
- **Function calling / tools:** structured requests executed by an authorized, validating system.
- **MCP:** a protocol for compatible applications to access exposed capabilities; not universal tool compatibility.
- **Agent vs. workflow:** different degrees of dynamic versus predetermined control, often combined.
- **Orchestration:** coordinating execution, state, routing, tools, and recovery as needed.
- **Skill:** reusable task guidance and resources whose loading depends on the host.
- **Router:** a mechanism selecting a model or execution path according to a policy.
- **Fine-tuning:** updating model parameters using training examples.
- **Quantization:** reducing numerical precision; verify memory, speed, and quality effects.
- **KV cache:** stored attention keys and values reused during common decoding designs.
- **TTFT / TPOT:** time to first token / time per output token, alongside complete user-visible latency.
- **Prompt caching:** provider- or application-supported reuse with specific price, validity, and permission rules.
- **Gradient-boosted trees / XGBoost:** a predictive model family / an implementation; useful tabular candidates, not automatically causal or interpretable.
- **Attention:** learned weighting and combination of permitted information in a sequence or representation.
- **Redline:** a measurable boundary tied to an accountable deployment or control response.
- **HITL:** human participation in a system; specify what the person can inspect and change.
- **Task resolution:** completion of the intended task under defined quality conditions; one possible outcome metric.

Editorial review: September 13, 2026. Historical benchmark examples are bounded to their sources. Current product specifications and prices are intentionally not frozen into this guide.
