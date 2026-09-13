# Illustrative AI PM interview answers

These examples demonstrate reasoning and delivery. They are **hypothetical approaches, not Ravi’s experience**, unless verified personal evidence is added separately. A polished answer is not proof that its speaker built the system. Adapt the depth to the question; do not memorize a uniform script.

A useful shape is an early answer, its decisive mechanism, relevant evidence or assumptions, and the trade-off that matters. Not every definition needs all four moves. Review with the same six criteria as the main skill.

## 1. LLM or predictive ML for churn?

**Illustrative answer:** For a labeled tabular churn problem, I would start with simple rules or logistic regression and compare gradient-boosted trees before choosing an LLM. I would use a time-based evaluation, check leakage and delayed labels, and measure calibration and the value of the action the score triggers. If support conversations contain useful signals, an LLM could extract structured features or draft an explanation grounded in the customer record. I would evaluate those stages separately and then test whether the intervention improves the customer outcome. A feature attribution is not proof that changing that feature prevents churn.

**Weak pattern:** choosing an LLM because it is newer, or claiming trees are always transparent and cheaper by a fixed ratio.

**Follow-up:** when would text-heavy data or limited labels change your baseline, and how would you test that change?

## 2. What happens when an AI feature calls a tool?

**Illustrative answer:** The model receives an allowed tool description and schema, then may emit a structured request with arguments. An executor validates the arguments, checks authorization and preconditions, and performs the permitted operation. It returns a result or error that the application uses to continue or answer. The executor might be our service or a provider-managed component. For a write, I would account for duplicate requests and verify an ambiguous outcome before retrying. A syntactically valid tool call is not permission, and retrieved tool output cannot override the application’s instructions.

**Weak pattern:** saying the model directly executes whatever it requests, or validating only after an irreversible action.

**Follow-up:** two tools overlap; how would you diagnose wrong selection without assuming a fixed failure rate?

## 3. Why do models hallucinate, and what would you do?

**Illustrative answer:** A model can produce a plausible answer that is false or unsupported. Learned language patterns do not guarantee access to the needed fact, and training or evaluation can reward guessing. I would first identify the product’s failure type and stakes. For an evidence-based assistant, I would inspect source quality, retrieval, answer support, and whether it should have clarified or abstained. Then I would repair the responsible stage and measure both harmful errors and useful coverage. Grounding helps, but a retrieved source can itself be wrong. A better prompt may help; it is one intervention to test, not a complete reliability guarantee.

**Weak pattern:** “Just tell it not to hallucinate,” or “every system must hallucinate, so there is nothing to do.”

**Follow-up:** which errors would prevent release, and what would the user experience when evidence is insufficient?

## 4. How does RAG work?

**Illustrative answer:** RAG retrieves relevant information and gives it to the generation step as evidence. I would design ingestion, source identifiers and permissions, retrieval, context assembly, and supported answers together. Depending on the task, retrieval could use keyword, vector, hybrid, or structured queries. A reranker can improve the selected evidence, but it adds cost and latency that I would measure. Permissions must be enforced before content reaches the model, including cached content. For quality, I would inspect whether we found the right material, whether it is current and correct, and whether the answer actually follows it.

**Weak pattern:** defining RAG as simply uploading documents to a vector database, or treating citations as proof of truth.

**Follow-up:** a faithful answer is wrong; what possibilities remain besides a generation failure?

## 5. How do transformers work?

**Illustrative answer:** Transformers use attention and other learned layers to build representations informed by relevant available context. Attention combines information using learned relationships; multiple heads allow different relationships to be represented. In a causal text decoder, future output is masked out. Training can process known sequence positions in parallel, while ordinary text generation still proceeds through successive output tokens. For a PM, I would connect that mechanism to the product’s context needs, quality, latency, and serving cost rather than assuming that a larger context is always better.

**Weak pattern:** saying a causal decoder sees future words, or that all output generation happens in parallel.

**Follow-up:** which parts of long-context processing and serving increase cost in the system you are considering?

## 6. How are GPUs used in deep learning?

**Illustrative answer:** GPUs are useful for parallel numerical work such as the matrix operations common in deep learning. Training updates parameters repeatedly; inference serves requests using a trained model. The bottleneck depends on the workload: prompt processing can be compute intensive, while incremental decoding may be limited by memory movement. I would measure utilization, memory needs, batch size, context length, and response targets before choosing an optimization. Quantization and batching can help, but they need quality and latency checks. Whether training or inference dominates lifetime cost depends on how much we train and serve.

**Weak pattern:** “GPUs are faster CPUs,” or “inference is always the dominant cost.”

**Follow-up:** what would make batching inappropriate for a particular user experience?

## 7. What are the unit economics of an LLM feature?

**Illustrative answer:** I would calculate cost per verified successful task. Token cost uses the actual input, output, and cache rates; if the rates are per million tokens, the token-price products must be divided by a million. Then I would add relevant tool, infrastructure, retry, and human costs. I would inspect which tasks and failure paths drive the bill before choosing levers such as removing redundant calls, caching, routing, or changing models. I would compare those changes at the required quality and latency. A pricier model can be cheaper per outcome if it avoids repeated attempts or review.

**Weak pattern:** quoting only the token bill, forgetting the pricing denominator, or assuming one universal order of cost levers.

**Follow-up:** how would the calculation change if attempted tasks stayed constant but successful completion fell?

## 8. How would you build an evaluation framework with human input?

**Illustrative answer:** I would define the user task and consequential failures first. Offline, I would assemble representative cases, difficult segments, and known failures with suitable reference answers or a clear rubric, keeping a held-out set. I would use component checks for diagnosis and end-to-end checks for the actual outcome. Human reviewers would assess cases that need judgment; any LLM judge would be calibrated against appropriate evidence and reviewed for disagreement or bias. In production, I would combine outcome and guardrail monitoring with sampled review and experiments where suitable. The person reviewing must have the information and authority to affect the result.

**Weak pattern:** treating benchmark accuracy or an unvalidated LLM judge as the entire evaluation system.

**Follow-up:** how would you distinguish model degradation from a change in the mix of users or tasks?

## 9. The north-star metric rose. Could quality still be falling?

**Illustrative answer:** Yes. Aggregate growth may reflect more users, easier tasks, or more attempts rather than better outcomes. I would compare quality and completion across task and user segments, then inspect corrections, unresolved work, latency, escalation, and source-supported answers. I would check metric definitions and sampling before attributing the change to the model. Regeneration is a useful diagnostic signal, but it can mean exploration rather than an error; escalation can be the intended safe outcome. The goal is to understand what changed for users, not automatically treat every supporting metric as a failure.

**Weak pattern:** declaring success from volume alone, or declaring failure from a rising regeneration rate alone.

**Follow-up:** which segment would you inspect first, and what result would change your interpretation?

## 10. How do you distinguish retrieval, source, and generation failures?

**Illustrative answer:** I would inspect the retrieved evidence and the answer separately. Retrieval quality asks whether we found relevant and sufficient material. Source quality asks whether that material is correct, current, and authorized. Faithfulness asks whether the answer follows it, while citation support asks whether each citation supports its claim. End-task correctness asks whether the user received the right result. A faithful wrong answer can come from a wrong source; an unfaithful one may reflect generation or confusing context. I would label concrete failures before choosing a retrieval or generation fix.

**Weak pattern:** assuming high faithfulness proves factual accuracy or that every wrong answer calls for a new embedding model.

**Follow-up:** what would you change if the correct document was retrieved but its decisive table was lost in parsing?

## 11. A model has ten times the capability at ten times the cost. What would you do?

**Illustrative answer:** I would first define what “ten times the capability” means on a valuable task. Then I would compare incremental user value, completion quality, and total delivery cost for candidate segments. A stronger model might make a previously infeasible task possible or reduce retries and human work. I would test those opportunities and route suitable tasks if a mixed approach works. Ten times the model price does not require ten times the customer value in every case; the decision depends on the baseline, incremental benefit and cost, quality requirements, and sustainable economics.

**Weak pattern:** send every task to it, reject it solely on price, or assume capability has one universal multiplier.

**Follow-up:** if cost rises from $1 to $10 per successful task, what evidence would justify the additional $9?

## 12. How would you define a redline?

**Illustrative answer:** I would define the boundary in terms of a measurable risk and a specified deployment condition, then name its owner and the response it triggers. That might mean restricted access, stronger controls, delayed deployment, or stopping a use case, depending on the current policy and evidence. I would test whether the evaluation detects the relevant failure and whether the mitigation works without unnecessarily blocking legitimate use. A threshold on paper is incomplete unless someone can act on it. I would verify the company’s current policy before claiming it uses a particular threshold.

**Weak pattern:** vague “safety first” language with no measurement, owner, or action.

**Follow-up:** how would you handle uncertain evidence near the boundary, and who decides?

## 13. Have you built an end-to-end agentic system?

This is an experience question. Do not turn the following structure into a fictional first-person story.

**If Ravi has relevant experience:** identify the real user problem, his precise role, and what the team built. Explain the control path, tools and permissions, context and state, evaluation, one actual failure and response, and the supported outcome. Distinguish prototype, pilot, and production deployment, including what he did not own. Use only details he can substantiate.

**If he has adjacent experience:** say so directly. Explain the closest actual work and its boundary, then offer an explicitly proposed design if useful: “I have built [verified scope], but I have not owned an end-to-end production agent. For this task, I would start by…”

**Weak pattern:** rebranding a prompt or tutorial as a platform, inventing a failure to sound experienced, or replacing the question with a generic architecture lecture.

**Follow-up:** what did you personally change after the first meaningful failure, and what evidence showed whether it helped?

## Compare reasoning, not polish

Strong answers make a defensible choice, explain the relevant mechanism, support their claims, and acknowledge meaningful limits. Weak answers often skip one of those steps. A smooth hypothetical can still be technically wrong, and a hesitant but accurate explanation may need delivery practice rather than a new project.

Use [the concept guide](concepts.md) for technical sources and [the rubric](grading-rubric.md) for feedback. None of these examples establishes current company interview questions, proprietary hiring standards, or Ravi’s work history.
