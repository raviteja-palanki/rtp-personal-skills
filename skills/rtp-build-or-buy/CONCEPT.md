# Build or Buy — Concept Guide

## FIRST PRINCIPLES

Every AI PM gets asked: "Should we fine-tune?" The question is asked a hundred times before the answer is truly needed, and the answer changes based on five variables that nobody usually measures.

The historical answer (from ML literature) is useless: "fine-tune if you have labeled data." Of course you have labeled data. The question is whether the ROI justifies the infrastructure, maintenance, and drift cost.

The atomic insight: **The build-or-buy decision is not about capabilities, it's about the cost of the decision being wrong.** Prompt-engineering wrong costs you 30 minutes. Fine-tuning wrong costs you six months of maintenance. Buy an API wrong, and you're hostage to vendor pricing. Get it right and you're outsourcing something you can't afford to build.

## DUAL DEFINITION

**Business definition:** The choice between developing a custom AI capability (fine-tuning, RAG, prompt engineering) versus licensing a pre-built API, based on accuracy requirements, cost tolerance, data availability, latency constraints, and long-term maintenance burden.

**Technical definition:** A decision framework that maps problem characteristics (input structure, output determinism, data volume, latency SLA, cost per transaction) to one of four implementation approaches (prompt engineering, RAG retrieval, fine-tuning, or API purchase), optimizing for total cost of ownership rather than single-axis optimization.

## THE TRAP (Expanded)

**"We have the data, so we should fine-tune."** This is the most common mistake. Having data is necessary but not sufficient. You also need: the latency budget to absorb training time, the cost budget to afford fine-tuning service, the accuracy upside to justify custom maintenance, and the team stability to maintain the model 18+ months.

Many teams have all four and still choose wrong. Why? Because fine-tuning *feels* like the "right" answer. It's more sophisticated than prompting. It plays to the strengths of the ML team. It feels defensible in a postmortem ("we did everything we could").

**"APIs are too expensive."** This discounts the cost of building wrong. A team fine-tunes a model to save 30% on tokens. They spend 4 months on training infrastructure, 2 months on eval, and 1 month on deployment. Total cost: $300k in engineering time. Token savings: $2k per month. Payback period: 150 months.

**"We need latency under 100ms, so we have to build."** True, if your requirement is genuinely <100ms. False if you've set an arbitrary latency goal without validating it matters to users. Many teams discover that 500ms is fine, or that fallback chains (API → cached response → degraded mode) meet the requirement without building custom inference.

**"Vendor lock-in is bad."** Correct, but vendor lock-in from poor fine-tuning is worse. A fine-tuned model that drifts, requires constant retraining, and nobody understands locks you in harder than an API contract.

## FOUR APPROACHES (Deep Analysis)

### 1. Prompt Engineering

Write a good prompt, maybe add few-shot examples, call the API.

**Strengths:**
- Fastest to iterate. Change prompt, test in 5 minutes.
- Cheapest upfront. No infrastructure or data labeling needed.
- Easiest to debug. Failures are obvious from prompt + output.
- Vendor-agnostic. Switch models by changing the API call.

**Weaknesses:**
- Accuracy ceiling is low for domain-specific tasks. General models have generalizable knowledge but miss domain nuance.
- No learning loop. Each request is independent; you don't get better over time.
- Hard to standardize. "Good prompts" are written by the person who found them; hard to transfer knowledge.

**When to choose:**
- Accuracy requirement is +10% over baseline, or less
- Latency budget is >200ms
- Problem is not domain-specific
- You want to launch in weeks, not months

**Example:** Customer intent classification for support routing. Prompt: "Classify this support message as one of: billing, technical, account, sales." Few-shot examples: three labeled examples. Cost: $0.0001 per call. Accuracy: 87%. Sufficient for most cases; hard cases go to human.

### 2. Retrieval-Augmented Generation (RAG)

Retrieve relevant documents/examples, insert them into the context window, prompt the model to generate an answer using that context.

**Strengths:**
- Accuracy boost without training. By injecting domain knowledge, you get domain-specific answers from a general model.
- Interpretable. The retrieved documents explain the answer; humans can validate.
- Lower cost than fine-tuning. No training infrastructure needed.
- Knowledge updates are simple. Change the document base, retrieval improves immediately.

**Weaknesses:**
- Latency is higher. Retrieval + embedding + inference = 500-5000ms typical.
- Retrieval quality is brittle. Bad retrieval → bad answer. The model can't fix wrong context.
- Token cost increases. Every request includes the retrieved documents in the context window.
- Requires curated document base. The quality of retrieval is bounded by document quality.

**When to choose:**
- Accuracy requirement is +20-30% over baseline
- You have high-quality documents to retrieve from
- Latency budget is >500ms
- Cost per call can tolerate increased context window tokens

**Example:** Customer support answers. RAG: retrieve relevant FAQ/docs by semantic similarity, include in prompt, ask Claude to answer. Cost: $0.0005-0.002 per call (depends on doc length). Accuracy: 92%. Customer sees both the AI answer and the source documents.

### 3. Fine-Tuning

Train a custom model on your labeled data. Deploy that model, call it like an API.

**Strengths:**
- Highest accuracy for domain-specific tasks. Model learns the nuance of your domain.
- Lowest latency possible. Once trained, inference is fast.
- Cost per call is lower than APIs if query volume is high. Smaller model, fewer tokens.
- Learning loop is possible. Collect user corrections, retrain monthly.

**Weaknesses:**
- Highest upfront cost. Infrastructure, data labeling, training, eval: $50-500k depending on model size.
- Highest maintenance cost. Drift happens; retraining is mandatory.
- Brittleness. Fine-tuned models fail in unexpected ways if the input distribution changes.
- Model updates are forced. Base model improves; you must retrain or your model stagnates.

**When to choose:**
- Accuracy requirement is +30% or more
- Query volume is 10k+ per month (cost per call breaks even)
- You have 1k+ labeled examples and can maintain them
- You have the team (ML engineer + infra) to maintain 18+ months
- Latency budget is <200ms

**Example:** Medical diagnosis support. Fine-tune Claude on 10k labeled patient cases. Accuracy: 96%. Cost: $200k training + $0.001 per call + $10k per year maintenance. ROI: justified only if each correct diagnosis is worth >$20. If not, RAG might be better.

### 4. Buy an API (General Purpose)

OpenAI's GPT-4, Anthropic's Claude, Google's Gemini — models optimized for general capability.

**Strengths:**
- Broadest capability. These models were trained on everything; they generalize.
- Zero maintenance. Vendor handles updates, scaling, reliability.
- Fastest to ship. Use today, no delays.
- Aligned by default. These models are already trained on Constitutional AI or RLHF to be safe.

**Weaknesses:**
- Cost at massive scale. Per-token pricing adds up if volume is high.
- Vendor dependency. Pricing can change; feature availability is vendor-controlled.
- No learning loop. Can't improve over time with your data.
- Latency is variable. Dependent on vendor infrastructure.

**When to choose:**
- Accuracy requirement is acceptable from a general model
- You want to ship fast
- Query volume is unpredictable
- Problem is not specialized enough to justify custom training

**Example:** General writing assistant, code generation, summarization. Use Claude API. Cost: $0.0015 per 1k input tokens. Accuracy: sufficient for most use cases. Maintenance: none.

## GATES vs AXES

The SKILL applies gates (sequential filters) rather than weighted scoring. Why? Because gates force yes/no clarity on hard problems, and they prevent the most common failure mode: "we're optimizing on one axis while failing on another."

Example: A team scores well on "we have labeled data" (Gate 2) but fails Gate 5 (maintenance team). They ignore Gate 5 because they scored well on Gate 2. Result: six months of unmaintained model. Gates force you to pass ALL or revise the decision.

## THE ECONOMICS OF WRONG DECISIONS

**If you BUY when you should BUILD:**
- You pay $X per user per month forever.
- Total cost: $X × users × 60 months.
- At 10k users: $600k over five years.
- But you ship in two weeks instead of two months.

**If you BUILD when you should BUY:**
- You spend $Y in engineering to save Z% on tokens.
- Y = (ML engineer salary × months) + (infrastructure) + (data labeling)
- Typical: $200k + $50k + $30k = $280k.
- Z% token savings = $5k per month for a 10k user base.
- Payback period: 56 months.
- But the model drifts at month 18, and you've committed to fixing it.

Most teams underestimate Y and overestimate Z%.

## REAL-WORLD EXAMPLE: Three Companies, Three Answers

**Company A: Customer Support Routing**
- Problem type: Deterministic classification
- Gate 1: ✓ Yes, deterministic
- Gate 2: ✓ Yes, 5k labeled support tickets
- Gate 3: ✓ 500ms acceptable
- Gate 4: ✓ $0.10/user/month < budget
- Gate 5: ✗ No ML engineer
- **Decision: PROMPT-ENGINEER + RAG.** Retrieve relevant FAQ, prompt for classification. Cost: $2k/month. Accuracy: 88%. Shipping in 2 weeks.

**Company B: Medical Recommendation**
- Problem type: Deterministic ranking of treatment options
- Gate 1: ✓ Yes, deterministic
- Gate 2: ✓ Yes, 50k labeled medical cases
- Gate 3: ✓ 2s acceptable for medical
- Gate 4: ✓ $5/user/month budget (justified by medical value)
- Gate 5: ✓ Yes, has ML team
- **Decision: FINE-TUNE.** Train on 50k cases. Cost: $250k + $20k/month maintenance. Accuracy: 96%. Shipping in 4 months.

**Company C: Content Translation**
- Problem type: Probabilistic generation
- Gate 1: ✗ No, output is creative/variable
- **Decision: BUY.** Call Claude API with instructions. Cost: $0.50/call. Accuracy: sufficient. Shipping in 1 week.

## INTELLECTUAL LINEAGE

- **Andrew Ng, "Machine Learning Yearning"** — The foundational thinking on when to collect data vs when to improve algorithms. Build-or-buy is an extension of this.
- **Hugging Face, "Training/Inference Trade-offs"** — Technical economics of fine-tuning vs prompt engineering.
- **Peter Norvig, "Unreasonable Effectiveness of Data"** — When data beats algorithms. Prerequisite for deciding to build.

## FURTHER READING

- Andrew Ng, "Machine Learning Yearning" (free online)
- Hugging Face, "Fine-tuning vs Prompting" blog post
- OpenAI, "Fine-tuning vs Prompt Engineering" documentation
- Your own cost modeling spreadsheet (the most important reference)
