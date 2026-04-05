# Context-Spec — Concept Guide

## FIRST PRINCIPLES

The CONTEXT framework is an insight about how production AI systems are actually structured: **the model (the visible, impressive part) is roughly 10% of the system. The other 90% — context assembly, orchestration, guardrails, state management, observability — is invisible but determines whether the model's outputs are any good.**

This invisible 90% is where most AI products fail in production. A team ships a feature that works great in demo, where the engineer hand-assembled the perfect context. Then it goes into production, where context assembly is broken (retrieval returns the wrong documents), or guardrails are bypassed (the model generates something unsafe), or state management fails (conversation history gets lost), or observability is missing (nobody knows why the feature broke).

The atomic insight: **Context engineering is the most important, least documented, and most underestimated part of any AI product. A context-spec is the production blueprint that makes the invisible visible.**

## DUAL DEFINITION

**Business definition:** A context-spec is the detailed specification of how a feature assembles and manages the information that an AI model sees — covering where that information comes from (user session? database? external API?), how fresh it must be, how it's assembled into the model's context window, what guardrails constrain the model's behavior, and how the system detects and recovers when anything in the pipeline fails.

**Technical definition:** A seven-layer architecture specification (Constitution → Observations → kNowledge → Tracks → Equipment → eXecution → Template) that documents, for each layer: the data sources, latency budget, reliability guarantees, failure modes, fallback behaviors, cost model, and monitoring/alerting strategy. This specification is precise enough that an engineer can implement it without asking clarifying questions.

## THE TRAP (Expanded)

### The Invisible Stack Blindness

Teams ship an AI feature with:
- A constitution that says "be helpful" (vague, unmeasurable)
- No specification of what real-time context is passed (surprise: the model doesn't know the user's account status, so it makes up an account ID)
- A retrieval system that was built by one engineer and never documented (that engineer leaves, nobody knows what the retriever is optimized for)
- No state machine (conversation history is stored in a local Redis that gets wiped on restart)
- Equipment (tool calls) that timeout frequently but nobody built a fallback
- Orchestration that's ad-hoc (check guardrails here? check before retrieval? after?)
- Output that lacks citations (user sees confident-sounding answer with no source)

In production: the feature works 70% of the time and is unpredictable the other 30%. But since 90% of the code is invisible (retrieval, context assembly, state management), the team assumes the model is the problem. They swap out Claude for GPT-4. Still 70% reliable. They swap the retriever. Still 70%. Because the actual problems are in the invisible layers that were never designed.

### The Prompt-Focused Fallacy

Teams optimize the prompt while ignoring context quality. "Let me add a system prompt that says 'cite your sources.'" But if the knowledge layer is retrieving the wrong documents, citation instructions don't help. The model cites the wrong source confidently. Or the system prompt says "use the provided context" but the context is missing (Observations layer didn't populate it). Or the template says "output must include confidence" but the orchestration doesn't enforce it (outputs are returned without going through the format validation layer).

### The Latency Trap

Each layer adds latency. A naive context spec might have:
- 500ms to retrieve documents
- 100ms to check guardrails
- 3 seconds to generate
- 200ms to filter output
- Total: 3.8 seconds

That might be acceptable. But then you add:
- User session context (50ms fetch)
- Recent conversation history (100ms database query)
- Product recommendations (200ms external API)
- Total: now 4.5 seconds

Add 10x load, and latency doubles because layers are hitting timeouts and retrying. Now you're at 9 seconds. User experience collapses. The team panics and removes features (drops user context, drops recommendations) to get latency down. But they never built a latency budget in the first place, so it's chaotic cuts rather than informed tradeoffs.

### The Observability Gap

Production breaks. You get paged at 2 AM. The feature that was working fine is now returning garbage. Was it:
- The retriever breaking? (Knowledge layer)
- The user session not loading? (Observations layer)
- The model hallucinating? (eXecution layer)
- The formatter broken? (Template layer)

Nobody knows. Because nobody logs what's flowing through each layer. The team adds logging retroactively (which is expensive at production scale). Or they give up and disable the feature.

### Cost Surprise

A feature that costs $0.01 per request sounds fine until you realize: 10 requests per user per day × 10,000 users = 100,000 requests per day × $0.01 = $1,000/day = $30,000/month. That was supposed to be a small feature. But nobody did the math on context assembly costs:
- Retrieval: 500 tokens to fetch context from 10 documents
- Generation: 1,000 tokens
- Filtering: 200 tokens
- Plus all the infra overhead

A good context-spec catches this before implementation. A bad or missing spec ships the feature, realizes it's expensive, then scrambles.

## INTELLECTUAL LINEAGE

**Ravi's CONTEXT Framework** — A seven-layer model for how production AI systems actually work. The framework maps to real implementation concerns:
- **C**onstitution: behavioral rules and safety guardrails (prompt engineering, filtering)
- **O**bservations: real-time context from user session, database, APIs
- **K**nowledge: retrieved documents, knowledge bases, facts
- **T**racks: workflow state, conversation history, multi-turn tracking
- **E**quipment: tools, external APIs, function calling
- **X**ecution: orchestration logic, error handling, retries
- **T**emplate: output formatting, structure, presentation

**Anthropic's Constitutional AI** — The Constitution layer isn't just a system prompt. It's a set of rules that can be enforced at multiple stages (in the prompt, in the output filtering, in the API response). A good context-spec specifies where each rule is enforced and what happens if a rule is violated.

**Amazon's Operational Excellence Pillar** (from AWS Well-Architected Framework) — Document your architecture, anticipate failure, and monitor everything. Applied to AI: the context-spec is the documentation, the failure modes are the anticipated failures, and the observability strategy is the monitoring.

**Google's Site Reliability Engineering (SRE)** — Latency budgets are a core SRE concept. If your system has a 1-second SLA, and you have 7 layers, each layer gets roughly 140ms. If one layer uses 500ms, it breaks the budget. A good context-spec enforces this discipline.

**Martin Fowler on Microservices** — Each layer is a concern that can be designed, tested, and monitored independently. If the Observations layer is broken, the rest of the stack should degrade gracefully (not crash). This requires explicit failure modes and fallbacks for each layer.

## REAL-WORLD EXAMPLES

### Example 1: Customer Support Chatbot (Medium Complexity)

**Bad context-spec (or no spec at all):**
- Constitution: "Be helpful and friendly" (vague)
- Observations: (none documented; engineer adds user name to the prompt but nobody knows where it comes from)
- Knowledge: (retrieval happens somewhere; maybe)
- Tracks: (conversation history stored in... local Redis? sessionStorage?)
- Equipment: (no tools; pure generation)
- eXecution: (generate the response, format it, send it)
- Template: (whatever the model outputs; no validation)

**Result:** In production, user sessions timeout and history is lost. The chatbot has access to user name but not account status. Retrieval occasionally returns irrelevant docs. Hallucinations happen because the model doesn't have grounding. Nobody detects the problems until customers complain.

**Good context-spec:**
```
Constitution:
- Rule: Never provide account numbers, passwords, or payment info
  Enforcement: Post-hoc filter (check response for account patterns)
  Failure mode: Rare but catastrophic (customer data leaked)
  Test: 100 adversarial prompts asking for account info; verify 100% filtered

- Rule: Cite all product information from knowledge base
  Enforcement: Prompt guidance (instruction to cite sources)
  Failure: Model cites training knowledge instead of KB; acceptable with confidence caveat
  Test: 50 product questions; verify >80% have citations with matching KB content

Observations:
- User name (from session)
- Account type (free/paid) — determines what features user can access
- Support tier (standard/priority) — determines escalation path
- Source: user session object, <1ms, no PII beyond what's already in UI
- Fallback: if session unavailable, treat as anonymous user (minimal features)

Knowledge:
- Product documentation (markdown, 500 articles, updated daily)
- Common issues and resolutions (FAQ)
- Retriever: vector embedding + BM25, top 3 documents
- Freshness: max 24 hours old; acceptable staleness
- Failure: timeout after 2 seconds, use cached results if available
- Grounding requirement: product-specific Qs must cite KB, general advice doesn't need KB

Tracks:
- State: New request → Clarifying (if ambiguous) → Generating → Done
- History: store last 5 turns (user message + assistant response)
- Persistence: database (PostgreSQL), survive restarts
- Timeout: 1 hour per conversation, then archive
- Resumption: if user comes back within 1 hour, recover full history

Equipment:
- Escalation tool: create support ticket (calls internal service)
- Requirement: only if user asks or AI confidence <50%
- Timeout: 2 seconds; if timeout, show human support link
- Cost: $0.05 per ticket created

eXecution:
1. Load user session → Observations layer
2. Retrieve KB docs (parallel) → Knowledge layer
3. Check constitution rules → guardrails
4. Generate response (T=0.5 for consistency, max 500 tokens)
5. Filter output (harmful content, policy violations)
6. Format response (citations, suggested actions)
Latency budget: 50ms load + 500ms retrieval + 50ms guardrails + 3000ms generation + 200ms filter + 50ms format = 3.85s max

Monitoring:
- Log every request: timestamp, user_id, input, retrieved_docs, generation_latency, output
- Alert if P95 latency > 5 seconds
- Alert if retrieval failure rate > 5%
- Daily report: failure modes encountered, escalation rate, user satisfaction

Template:
- Required: title, body, suggested_actions (list)
- Optional: citations, followup_questions, escalation_link
- Validation: must have all required fields, citations must be valid URLs
- Example:
  ```
  Title: How to reset your password
  Body: Go to [Login](https://app.example.com/login) → click "Forgot password" → check email for reset link.
  Suggested actions:
  - Having trouble with the email link? [Click here for troubleshooting]
  - Need to update your email address? [Contact support]
  Confidence: High (from KB)
  ```

Cost model:
- Retrieval: ~200 tokens per request
- Generation: ~300 tokens per request (average)
- Total: ~500 tokens per request = $0.0001/request
- 100 requests per day from 1000 users = 100,000 requests/day = $10/day = $300/month
- Acceptable cost for customer support savings

Stress test:
- Failure at scale: if retriever times out at 10x load, fall back to generation without grounding (acceptable for support)
- Cost at 10x: 10x load = $3000/month (acceptable if support cost savings are >$3000/month)
- P95 latency: set to 5 seconds; acceptable for support context (humans are slower)
- Monitoring: all four dimensions pass with documented fallbacks
```

### Example 2: Code Generation (High Complexity, High Consequence Magnitude)

**Good context-spec would address:**

```
Constitution (elaborate because code safety is critical):
- Rule: Never generate insecure code (SQL injection, hardcoded secrets, etc.)
  Enforcement: Pre-hoc (prompt) + post-hoc (syntax checking)
  Failure: insecure code generation
  Cost: 1 in 10,000 (rare but catastrophic if user ships it)

Observations:
- Language context (what language is user coding in?)
- File context (what imports, classes, functions exist in current file?)
- User expertise level (inferred from interaction pattern)
- Cost: 500ms to build file context from IDE

Knowledge:
- Standard library docs for the language
- Company coding standards
- Common patterns (authentication, database queries, API calls)
- Retriever: keyword match on function names + vector similarity
- Freshness: must be current (standards update monthly)
- Requirement: 90%+ accuracy on code that matches standard patterns

Tracks:
- Keep multi-turn code refinement history
- Allow user to say "fix the bug you just generated"
- State: Draft → Testing (user has clicked test button) → Published

Equipment:
- Code formatter (linter, applies company style)
- Syntax checker (compile-time check)
- Documentation link generator (link to relevant docs)
- Security scanner (checks for known vulnerabilities)

eXecution:
1. Load file context (2 seconds)
2. Retrieve relevant code examples and docs (1 second)
3. Generate code (2 seconds, temperature 0.1 for precision)
4. Run syntax checker and linter (1 second)
5. Run security scanner (2 seconds)
6. Format with citations (500ms)
Budget: 8.5 seconds (high, but code generation is worth it)

Monitoring: Log every generated code snippet, result of security scan, user acceptance
Alert: If security scanner finds vulnerability in accepted code (means user shipped insecure code)

Risk: If security scanner is slow (2 seconds) and times out often, the feature becomes unreliable
Solution: Cache security scan results, run async, return "checking security" in real-time, push results asynchronously
```

### Example 3: Medical AI Diagnostic Assist (Highest Complexity, Highest Risk)

**Context-spec critical because wrong output = patient harm:**

```
Constitution:
- This is NOT a diagnosis system; it's a review-assist system
- Never make autonomous decisions; always require physician confirmation
- Rule: Output must be marked as "findings for review" not "diagnosis"
  Enforcement: Template layer (format field says "findings" not "diagnosis")
- Rule: Confidence <80% → escalate to specialist
  Enforcement: eXecution layer (conditional routing)

Observations:
- Patient demographics (age, sex, prior conditions)
- Imaging modality (CT, MRI, X-ray)
- Physician expertise level (radiologist specialist or general practitioner)
- Cost: 100ms database query

Knowledge:
- Medical imaging atlas (thousands of annotated examples)
- Condition profiles (symptoms, imaging findings, prevalence)
- Treatment guidelines
- Retriever: content-based image retrieval (CBIR) for similar cases
- Requirement: 99%+ accuracy on common conditions (high sensitivity, not high specificity)
- Reasoning: false negative (miss diagnosis) is worse than false positive (flag for review)

Tracks:
- Per-patient case history
- Prior imaging studies (to check for progression)
- Radiologist's review notes (what did human expert conclude?)
- Use to validate model over time

Equipment:
- DICOM image processor (read medical imaging format)
- Severity scorer (internal tool)
- Escalation system (routes to senior radiologist)
- Patient notification system (if findings are escalated)

eXecution (strict sequence because order matters):
1. Load patient context (100ms)
2. Retrieve similar cases from atlas (2 seconds, CBIR)
3. Generate findings (4 seconds, model specifically trained for this)
4. Run confidence analysis (200ms)
5. If confidence <80%, mark for specialist review → equipment layer escalates
6. Format output with severity, confidence, references to similar cases
7. Require physician sign-off before any action
Budget: 7 seconds (high, acceptable for medical context)

Monitoring (critical):
- Log every finding with physician's confirmation/override
- Override rate >20% for any condition → trigger model retraining
- Accuracy on specialist reviews (ground truth)
- Patient outcome tracking (6-month follow-up: was diagnosis accurate?)
- Alert: if any misdiagnosis detected, immediate review of similar recent cases

Cost:
- Imaging processing: $0.01/image
- Model inference: $0.10/image
- Storage: $0.01/image
- Per patient: 5 images over diagnostic period = $0.80/patient
- Acceptable if prevents 1 misdiagnosis per 100 patients (cost of misdiagnosis >> $80)
```

## THE LATENCY BUDGET DISCIPLINE

This is where most context-specs fail. Teams design each layer in isolation, then connect them and discover: total latency is 12 seconds when the SLA is 2 seconds.

**The discipline:**
1. Start with your SLA. If users expect a response in 2 seconds, that's your budget.
2. Allocate top-down: retrieval gets 500ms, generation gets 1000ms, overhead gets 500ms.
3. Design each layer to FIT the allocation, not to "be optimized."
4. When you exceed the budget, you redesign (drop features, cache aggressively, parallelize).
5. Budget is sacred. If you're over, you don't add logging; you change architecture.

A context-spec that doesn't have a latency budget by layer is not a spec; it's a list of hopes.

## FURTHER READING

- Ravi Teja Palanki, "The Invisible Stack" — Foundational concept for this skill
- Ravi Teja Palanki, "The CONTEXT Framework" — Seven-layer architecture
- Google, "Site Reliability Engineering" (SRE Book), Chapter 6 on Monitoring — How to instrument each layer
- Anthropic, "Constitutional AI" — How to design the Constitution layer
- Tom Limoncelli, "The Practice of Cloud System Administration" — Latency budgeting and compound failures
- NIST AI Risk Management Framework — Risk assessment for layered systems
