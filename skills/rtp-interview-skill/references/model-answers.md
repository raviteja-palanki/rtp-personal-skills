# AI PM Technical Interview — Model Answers

Full gold-standard answers, annotated move-by-move against the **5 Laws** (Commit → Depth → Experience → Nuance → Succinct), plus **weak-vs-strong pairs** and the **likely follow-up** for the most common questions.

Use these to (a) show the user the target shape in Answer mode, (b) model rewrites in Grade mode, and (c) calibrate your own follow-ups in Mock mode. Hand the user the answer, then the annotation — they need to see *why* it lands, not just memorize it.

Every answer is written to be said in **under 120 seconds**. Read them aloud; if you can't, they're too long.

---

## The template every answer follows

> **[Commit]** in one sentence → **[Depth]** the mechanism/structural reason in correct jargon → **[Experience]** the operational tell ("I'd put…", "the first thing I'd check…") → **[Nuance]** the second consideration / the hybrid / the trade-off → land. Keep it two short paragraphs. If it must go longer, check in.

---

## 1. LLM or ML for churn prediction? ★ (the canonical question)

**A+ answer:**
> "ML model, but let me explain. Churn is tabular — structured features, a clean yes/no label. I'd put gradient boosted trees on it, XGBoost, because they're cheaper, faster, and more interpretable. The first question after I ship is *why didn't an account get flagged* — trees answer that well, an LLM does not. Where an LLM earns a seat is the language layer — turning messy support tickets into a feature, or drafting the save email once an account trips the threshold. So the real system is hybrid. Trees predict, the LLM reads and writes."

**Annotation:**
- *Commit:* "ML model, but let me explain" — direction first, zero fence-sitting.
- *Depth:* "tabular," "structured features," "clean yes/no label" — correct terms making the structural case for trees.
- *Experience:* "I'd put… the first question after I ship is why an account didn't get flagged" — operational phrasing that proves he's shipped one.
- *Nuance:* the hybrid — LLM in the language layer. This is the B+→A+ move. Without it, "ML" alone is a junior answer.
- *Succinct:* ~90 words. Two beats.

**Weak answer:** "I'd use an LLM, they're really powerful for this kind of prediction." → reaches for the frontier model reflexively, no structural reasoning, no interpretability, no hybrid.

**Follow-up:** "When would you NOT use trees here?" → sparse labels + rich text, or when the whole value is in language. "How do you evaluate each half?" → AUC/PR + drift for the tree; faithfulness/quality for the LLM text.

---

## 2. Your AI feature calls a tool — what happens under the hood? ★

**A+ answer:**
> "The model never runs the tool — that's the part most people get backwards. I give it a list of tools, each with a name, a description, and a JSON schema for its arguments. The description is what it uses to decide when to reach for one, so a vague description is a real bug. When it decides a tool is needed, its output is a structured request — the function name plus arguments. My code runs that, gets the result, validates it, and passes it back into the conversation, and then the model writes the final answer using my data. The intelligence sits in deciding to call and with what. Execution and validation live in my code — which is where I check it, because it can absolutely pass the wrong arguments."

**Annotation:**
- *Commit:* "The model never runs the tool" — the counterintuitive thesis up front.
- *Depth:* "JSON schema," "structured request," "function name plus arguments" — the mechanism, correctly.
- *Experience:* "a vague description is a real bug," "it can absolutely pass the wrong arguments" — the tells of someone who debugged this.
- *Nuance:* the clean line between model (decides) and code (executes + validates). That boundary is the whole insight.
- *Succinct:* one tight paragraph.

**Weak answer:** "The model calls the API and returns the result." → wrong; the model doesn't execute anything. This is a Law 2 ✗ and a bluff risk.

**Follow-up (the trap):** "Does orchestration come into this?" → **No** for a single call — request/response in app code. Orchestration shows up only with multiple tools to sequence, retries, state across turns, or multiple agents to route. Reaching for the sophisticated answer here fails it.

---

## 3. Why do models hallucinate, and what's your move as PM? ★

**A+ answer:**
> "It's the model working as designed. It predicts the next most plausible token — it isn't looking anything up — so with nothing to ground it, it produces something false with complete confidence. Ungrounded factual recall is above 50% error on benchmarks like SimpleQA, and OpenAI's own research frames hallucination as a statistically inevitable byproduct of next-token training. So I don't treat it as a prompt problem. When the answer has to be right, I ground it — retrieval to pull in real content, or a tool to fetch live data — which drops hallucination below 1% on grounded benchmarks. Then I measure whether the answer actually traces back to what I retrieved. A longer prompt doesn't fix this. Grounding does."

**Annotation:**
- *Commit:* "working as designed" — reframes it from bug to mechanism immediately.
- *Depth:* "next most plausible token," "statistically inevitable," the SimpleQA >50% and grounded <1% numbers.
- *Experience:* "I don't treat that as a prompt problem," "I measure whether the answer traces back" — a builder's instinct.
- *Nuance:* prompt vs. grounding — names the wrong fix and the right one.
- *Succinct:* two beats, lands on "grounding does."

**Weak answer:** "You fix hallucinations with better prompting and more training data." → the trap. Prompting doesn't fix it; better data alone can't remove it. Law 2 ✗.

**Follow-up:** "How would you measure grounding?" → see answer #10.

---

## 4. Explain how RAG works ★ (Perplexity)

**A+ answer:**
> "The model can't hold the whole corpus and its knowledge is frozen at training, so I retrieve at query time. Offline, I chunk the documents and embed each chunk into a vector store. When a query comes in, I embed it, pull the nearest chunks — usually hybrid, keyword plus semantic, with a reranker on top to reorder for relevance — stuff them into the prompt, and have the model answer with citations. The thing that makes or breaks it isn't the LLM, it's retrieval quality: chunking and the reranker. If the answers are wrong, I look there before I touch the prompt."

**Annotation:**
- *Commit:* opens with *why* RAG exists, then the pipeline — no meandering.
- *Depth:* "chunk," "embed," "vector store," "hybrid," "reranker" — the real pipeline, in order.
- *Experience:* "if the answers are wrong, I look there before I touch the prompt" — the debugging instinct that separates built-from-read.
- *Nuance:* retrieval quality > the LLM. Most people credit the model; the operator credits retrieval.
- *Succinct:* ~90 words.

**Weak answer:** "RAG is when you give the AI extra documents so it knows more." → true but shallow; no mechanism, no failure surface, no follow-up survival.

**Follow-up:** "Answers cite the wrong source — retrieval or generation?" → faithfulness vs. retrieval quality (answer #10). "Improve retrieval." → chunking, embedding model, hybrid search, query rewrite, reranker, top-k.

---

## 5. How do transformers work? ★ (Nvidia, Glean)

**A+ answer:**
> "The core idea is attention. For each token, the model weighs how much every other token in the context should influence it — that's how it resolves what 'it' refers to, or which earlier fact matters right here. Self-attention does that across the whole sequence in parallel, which is exactly what let transformers scale on GPUs where the older sequential models — RNNs — couldn't. Architecturally: tokens get embedded, position gets added, then a stack of attention-plus-feed-forward blocks, and the final layer emits a probability distribution over the next token. The one catch worth naming is that attention is quadratic in sequence length, which is why long context gets expensive."

**Annotation:**
- *Commit:* "The core idea is attention" — one anchor, not a history lecture.
- *Depth:* "self-attention," "embedded," "positional," "quadratic in sequence length" — correct, and the coreference example proves understanding, not memorization.
- *Experience:* connects to cost ("long context gets expensive") — a PM's lens on an architecture question.
- *Nuance:* the O(n²) catch — shows he knows the limitation, not just the mechanism.
- *Succinct:* then STOP. Do **not** derive Q/K/V or softmax. Overshooting here is Mistake 6.

**Weak answer:** "Transformers use neural networks with lots of layers to understand language." → says nothing specific; survives no follow-up.

**Follow-up:** "Why did they beat RNNs?" → parallelism + long-range dependencies + GPU-scalable. "Why is long context expensive?" → O(n²) attention + KV cache memory.

---

## 6. Explain how GPUs are used in deep learning ★ (Nvidia)

**A+ answer:**
> "Neural nets are billions of matrix multiplications, and GPUs do those massively in parallel — thousands of cores versus a CPU's handful — which is the whole reason deep learning is practical. Two regimes to separate: training is one huge parallel job across many GPUs, the big one-time cost; inference is the recurring cost of serving users, and it's usually memory-bandwidth-bound rather than compute-bound — the bottleneck is shuttling the weights and the KV cache through GPU memory. So the product levers I care about are quantization to shrink the memory footprint, batching to keep the GPUs saturated, and watching VRAM, because the model has to fit."

**Annotation:**
- *Commit:* "billions of matrix multiplications… in parallel" — the answer in one line.
- *Depth:* "memory-bandwidth-bound," "KV cache," "quantization," "VRAM" — infra vocabulary used correctly. This is what Nvidia is checking.
- *Experience:* frames it as "the product levers I care about" — a PM who's had the cost conversation.
- *Nuance:* training vs. inference, compute- vs. memory-bound. The distinction is the depth.
- *Succinct:* three levers, done.

**Weak answer:** "GPUs are faster than CPUs so we use them for AI." → true and useless. No mechanism, no cost lever.

**Follow-up:** "Which dominates a live product's cost?" → inference (recurring). "Inference too expensive?" → quantize, batch, route, cap context (shrinks KV cache).

---

## 7. Walk me through the unit economics of an LLM feature ★ (Microsoft, Amazon)

**A+ answer:**
> "Cost per inference is input tokens times the input price plus output tokens times the output price — and output usually runs 3 to 5 times the input price. So my system prompt, my RAG context, and how verbose I let the model be all land straight in COGS. At volume, two levers: prompt-cache the repeating prefix, which is often about 10x cheaper on those tokens, and route the easy majority to a small model — GPT-4o to 4o-mini is roughly a 17x spread, so that's real money. On latency I design to p95, not p50, and I stream to hide time-to-first-token. If it's a real-time surface I'll trade some quality for speed — smaller model, shorter outputs, maybe drop the reranker; if it's batch I'll spend the latency for quality and optimize purely on cost."

**Annotation:**
- *Commit:* the cost formula, stated cleanly, first.
- *Depth:* "output 3–5× input," "prompt cache ~10×," "17x spread," "p95," "TTFT," "streaming" — the numbers prove he's read a real bill.
- *Experience:* "how verbose I let the model be lands straight in COGS" — a margin owner's instinct.
- *Nuance:* real-time vs. batch changes the whole build. That's the senior move.
- *Succinct:* dense but under 120s if paced.

**Weak answer:** "LLMs cost money per API call, so we'd want to keep usage efficient." → no formula, no levers, no numbers.

**Follow-up:** "Losing money per user — levers in order?" → cut context/output, cache, route, small fine-tuned model, pricing. Order = kill waste before re-architecting.

---

## 8. Whiteboard an evaluation framework with human-in-the-loop ★ (Meta)

**A+ answer:**
> "Two layers. Offline: a golden set of representative inputs with graded criteria — faithfulness, correctness, format — that I run on every model or prompt change to catch regressions before they ship. I'd score it with an LLM-as-judge, but only after calibrating that judge against human labels, because judges have known biases — they favor longer answers and the first option. Online: task resolution as the north star, plus guardrail signals — escalation rate, correction rate, thumbs-down — sampled for human review. And I close the loop: those human labels flow back to expand the golden set. Human-in-the-loop sits at two points — calibrating the judge, and reviewing the online sample."

**Annotation:**
- *Commit:* "Two layers" — the structure declared up front.
- *Depth:* "golden set," "faithfulness," "LLM-as-judge," "verbosity/position bias," "task resolution" — the eval vocabulary, correctly.
- *Experience:* "only after calibrating the judge against human labels" — the step people who've actually run evals never skip.
- *Nuance:* the closed loop (online labels → golden set) and the two HITL insertion points.
- *Succinct:* organized enough to say fast.

**Weak answer:** "We'd track accuracy and user satisfaction." → vanity metrics, no offline/online split, no judge calibration, no HITL design.

**Follow-up:** "North-star's up — how do you know it's quietly worse?" → answer #9.

---

## 9. North-star metric is up — how do you know the model is quietly getting worse? ★

**A+ answer:**
> "The north-star can rise while quality drops — users retry more, or a specific cohort degrades and the aggregate hides it. So I don't trust the top-line alone. I watch the guardrails: correction and regeneration rate — if people are re-asking, the first answer failed — escalation rate to a human or the strong model, and faithfulness on a rolling sample of real traffic. And I segment: a model change can help the median and quietly break a cohort, like non-English queries or a specific document type. Silent degradation is the AI PM's nightmare, so I design the dashboard to catch it before the north-star ever moves."

**Annotation:**
- *Commit:* "the north-star can rise while quality drops" — names the trap immediately.
- *Depth:* "correction/regeneration rate," "faithfulness on a rolling sample," "segment by cohort."
- *Experience:* "if people are re-asking, the first answer failed" — a real read of behavioral signal.
- *Nuance:* aggregate vs. segment; leading vs. lagging.
- *Succinct:* tight.

**Weak answer:** "I'd keep monitoring the metrics and run A/B tests." → generic, no specific silent-failure signals.

**Follow-up:** "Give me one concrete cohort you'd worry about." → forces specificity — non-English, long documents, a new customer segment.

---

## 10. How would you measure grounding / is it retrieval or generation? ★

**A+ answer (the "name the edge" gold standard):**
> "Honestly, I'd confirm the exact metric with the team before locking one in. My instinct is two separate checks. Faithfulness — does the answer actually trace back to the retrieved text. And retrieval quality — did we pull the right snippet in the first place. Those are different failures, and I wouldn't want to chase one when it's actually the other. If faithfulness is high but answers are still wrong, my retrieval is fetching the wrong chunks — that's a chunking, embedding, or reranker problem. If retrieval is good but the answer drifts from it, that's a generation problem. Different fix each way."

**Annotation:**
- *Commit:* commits to a *method* while honestly flagging he'd confirm the exact metric — this is the "name the edge" move, and it scores **higher** than a confident guess.
- *Depth:* "faithfulness," "retrieval quality," the two-failure decomposition.
- *Experience:* "I wouldn't want to chase one when it's actually the other" — hard-won.
- *Nuance:* the whole answer is nuance — two failure modes, two fixes.
- *Succinct:* clean.

**Why this is a gold standard:** it demonstrates the single highest-value behavior in the round — *naming the edge of your knowledge and what you'd check* beats a confident wrong metric every time. Teach this pattern explicitly.

**Follow-up:** "Retrieval's fetching wrong chunks — where first?" → chunking strategy, embedding model, hybrid search, reranker, top-k.

---

## 11. You have a model with 10× capability at 10× cost. What do you do with it? ★ (OpenAI)

**A+ answer:**
> "I don't roll it out everywhere — that's paying a 10x premium on queries that never needed it. I'd find where 10x capability creates 10x-or-more value and route only those there. That's the hard, high-stakes, long-horizon work — complex agentic tasks, deep research, hard coding, high-value reasoning where a better answer is worth real money. The easy majority — simple lookups, classification — stays on the cheap model, because the expensive one adds cost, not value, there. So it's a routing and segmentation problem: segment by task value and willingness to pay, put the frontier model behind the queries that clear the bar, and price the premium tier to the users who get 10x value. The trap is treating a capability jump as a blanket upgrade."

**Annotation:**
- *Commit:* "I don't roll it out everywhere" — a stance, immediately.
- *Depth:* routing, segmentation, value-per-query — the right mental model.
- *Experience:* names concrete high-value use cases vs. low.
- *Nuance:* capability ≠ blanket upgrade; tie price to who gets the value.
- *Succinct:* one paragraph.

**Weak answer:** "10x capability is amazing, I'd upgrade all our users to it." → ignores cost/value matching; a margin disaster.

---

## 12. Define a redline for a model capability ★ (Anthropic)

**A+ answer:**
> "A redline is a capability the model must never have in deployment — something like meaningful uplift on a bioweapon, or the ability to act autonomously in ways we can't oversee. Defining one is three things. Specify the capability precisely enough to actually test for it. Build an eval or red-team protocol to measure how close the model is to it. And pre-commit to a response if it approaches the line — don't ship, add mitigations, or gate access. The whole point is that the decision is made before the capability exists, not after, so you're never negotiating with a shipping deadline about safety."

**Annotation:**
- *Commit:* defines the redline in the first sentence.
- *Depth:* "eval / red-team protocol," "pre-commit," specificity-to-test.
- *Experience:* "never negotiating with a shipping deadline about safety" — a real product-safety tension.
- *Nuance:* the three-part structure; decision-before-capability.
- *Succinct:* tight.

**Follow-up:** "How would you know it's approaching the line?" → evals + red-teaming + capability trend across model versions. "It's close — what do you do?" → the pre-committed response.

---

## 13. Have you built an end-to-end agentic system? ★ (Glean, DeepMind)

**How to answer (this needs the user's REAL experience — never fabricate):**
Structure: name the task → the three layers (instruction / tools / skill) → why you chose workflow-vs-agent → what broke and how you handled the model being wrong.

**A+ shape (fill with the user's real build):**
> "Yes — [the task, e.g., a digest agent that summarizes my unread Slack every morning]. Three layers: a system prompt with the standing instructions — group by channel, urgent first; the tools it's allowed to call — just the Slack API to read messages; and a skill layer for the packaged know-how — what counts as urgent, the digest format, when to ask instead of guess. I deliberately built it as a mostly-deterministic workflow, not a free-roaming agent, because the path was predictable and autonomy would just cost me reliability. Where it broke was [X] — [e.g., it flagged everything as urgent] — so I added [Y] — [a tighter urgency rule / a verifier step]. The one place I let it act on its own was [Z]."

**Annotation / coaching:** the interviewer wants evidence you've *shipped*, not a definition. If the user hasn't built one, the coaching move is: go build a tiny one this week (a Slack/email digest, a one-tool agent) so this answer is real. A fabricated agent story collapses under one follow-up ("what was in the skill layer, exactly?").

**Follow-up:** "Why not a full agent?" → workflow sufficed; autonomy costs predictability/eval/tokens. "What was in the skill layer?" → routing logic + context check + structure rules (tests whether the story is real).

---

## Weak-vs-Strong Quick Reference

| Question | Weak (dies on follow-up) | Strong (survives) |
|----------|--------------------------|-------------------|
| LLM or ML for churn? | "LLM, they're powerful." | "ML — tabular, trees, interpretable; LLM in the language layer; hybrid." |
| Tool call under the hood? | "Model calls the API." | "Model emits a structured request; my code executes + validates." |
| Why hallucinate? | "Bad prompt / needs more data." | "Working as designed; ground it; measure faithfulness." |
| How does RAG work? | "You give it extra docs." | "Chunk→embed→retrieve (hybrid+rerank)→cite; retrieval quality is the game." |
| Transformers? | "Deep neural nets for language." | "Attention weighs token influence; parallel; O(n²) catch." STOP. |
| GPUs in deep learning? | "Faster than CPUs." | "Parallel matmul; inference memory-bandwidth-bound; quantize/batch/VRAM." |
| Unit economics? | "Costs per call, keep it efficient." | "in+out tokens, output 3–5×, cache ~10×, route 17×, design to p95." |
| Eval framework? | "Track accuracy + CSAT." | "Golden set + calibrated judge offline; task-resolution + guardrails online; HITL loop." |
| Measure grounding? | "Check if it's accurate." | "Faithfulness vs. retrieval quality — two failures — and I'd confirm the metric with the team." |
| Cut cost? | "Use it efficiently." | "Route the easy majority to a small model (17× spread), cache the prefix." |
