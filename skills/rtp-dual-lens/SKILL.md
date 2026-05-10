---
name: rtp-dual-lens
description: Ensures any AI concept is simultaneously actionable for business leaders AND technically validatable by engineers, preventing misalignment that leads to wasted sprints. Use when writing PRDs, strategy docs, presentations to mixed audiences, communicating with board, or when there's disagreement between business and engineering about "what we're building". Triggers on 'business doesn't understand what we're building', 'engineering doesn't see the business case', 'the spec doesn't match what we shipped', or when business and technical teams have conflicting interpretations of the same concept. Also use before committing quarterly roadmap resources. Do NOT use for pure engineering specifications (internal architecture docs), pure business memos (financial forecasts), or when both audiences are already deeply aligned. Do NOT use when speed matters more than cross-functional clarity, or in organizations with strong silos where bridge-building will be resisted.
---
# Dual-Lens

## DEPTH DECISION

**Go deep if:** Explaining a new AI concept (model choice, retrieval strategy, output format) to mixed audiences. **Skim to questions if:** Quick check that technical and business teams use the same language. **Skip if:** Decision is entirely within one domain (pure infra, pure commercial).

## THE TRAP

You will communicate in one language. The bias is **curse of knowledge** — once you understand something, you can't imagine not understanding it. Engineers write specs that executives can't act on. Executives write strategies that engineers can't validate. Both sides think they were clear.

In AI products, the gap is wider than traditional software because:
- AI concepts have no visual analog (what does "attention mechanism" look like?)
- AI failure modes are probabilistic (executives hear "95% accuracy" and think "always works")
- AI costs are novel (per-token pricing has no precedent in most leaders' experience)

### The Translation Loss Problem

The core failure mode is **translation loss** — when PMs translate between audiences, nuance disappears in both directions:

- **Engineers → Executives:** Engineers say "We need to reduce latency by optimizing the context window." Executives hear "Make it faster." The actual business problem (users abandon chats after 3 seconds) gets replaced with a vague optimization direction.

- **Executives → Engineers:** Executives say "Reduce perceived wait time." Engineers interpret this as "Optimize inference speed." But the real solution might be streaming output, progress indicators, or early results rather than absolute speed.

- **Technical Jargon → Business Impact:** "95% accuracy" hides critical nuance. If that 5% failure hits specific user segments (e.g., non-English names, edge cases), the impact isn't evenly distributed. One executive hears "we're ready"; another understands "5% of Black users experience wrong output."

Examples of translation loss:
- "The model hallucinates" → Real problem: "Factual correctness varies by domain (medical: 2% hallucination rate vs. general knowledge: 8%)"
- "We need better RAG" → Real problem: "Retrieval latency is 1.5s, pushing total response time above our 3s target"
- "Scaling to 100k users" → Real problem: "Per-user cost rises from $0.02 to $0.08 at volume, breaking unit economics"

## THE PROCESS

1. **Write the business definition first.** In one paragraph, answer: "What does this mean for revenue, risk, competitive position, or customer trust?" No technical terms. If a Fortune 500 CFO can't act on it, rewrite.

2. **Write the technical definition second.** In one paragraph, answer: "What does this mean for architecture, latency, cost per request, failure modes, or monitoring?" No business euphemisms. If a senior engineer can't validate it, rewrite.

3. **Test the bridge.** Ask: "Can someone read the business definition, then the technical definition, and understand how they connect?" If the two definitions feel like separate documents about different things — the bridge is broken.

4. **Add the translation layer.** For each key technical decision, write the business implication. For each key business requirement, write the technical constraint.
   - "Using RAG instead of fine-tuning [technical] means we can update knowledge daily without retraining [business implication]"
   - "Reducing response time to under 2 seconds [business requirement] means we need streaming output and smaller context windows [technical constraint]"

5. **Validate with both audiences.** Show the business definition to a business stakeholder: "Can you act on this?" Show the technical definition to an engineer: "Can you build from this?"

6. **Add model empathy — understand model strengths/weaknesses.** When explaining AI capability, specify difficulty tier and use the Model Empathy Framework (see section below) to map what's easy/hard for the model to the business implications.

## REALITY CHECK

- **Failure mode:** Oversimplifying for business readers until the technical content is wrong. Dual-lens means both definitions are accurate, not that one is dumbed down.
- **Time cost:** Writing two definitions takes 2x the time. For important concepts, this is an investment. For minor decisions, a single audience is fine.
- **Cultural risk:** Some organizations punish PMs for "being too technical" or "being too business-y." Dual-lens requires organizational permission to speak both languages.

## QUALITY GATE

- [ ] Business definition written — actionable by a non-technical leader
- [ ] Technical definition written — validatable by a senior engineer
- [ ] Bridge tested — both definitions connect to the same underlying concept
- [ ] Translation layer added for key decisions
- [ ] Validated with at least one representative from each audience

## MODEL EMPATHY FRAMEWORK

When explaining AI capability, don't just say "accuracy." Map the task type to what models find easy/hard, then translate that into business constraints:

| Task Type | What Model Finds Easy | What Model Finds Hard | PM Implication |
|-----------|---|---|---|
| **Classification** | Binary yes/no on clear categories | Ambiguous categories, boundary cases, context-dependent decisions | Set clear taxonomy before building; don't ask models to learn nuance from examples alone |
| **Generation** | Structured output (JSON, summaries), paraphrasing | Novel creative work, factual precision under uncertainty | Verify facts independently; use schemas to constrain output format |
| **Reasoning** | Single-hop logic, pattern matching in training data | Multi-step reasoning, temporal chains, constraints | Decompose complex requests into steps; validate each step independently |
| **Retrieval** | Keyword matching, semantic similarity on dense text | Negation ("not red"), temporal ordering ("before 2020"), counting ("exactly 3") | Pre-filter results; don't rely on models for filtering/ranking |
| **Tool Use** | Single API calls, straightforward sequences | Multi-tool orchestration, error recovery, deciding which tool fits | Build a tool management harness; don't ask models to debug failed API calls |

**How to use this:** When a stakeholder says "We need AI to extract clauses from contracts," translate: "That's classification (easy). But if we need to extract conflicting clauses (reasoning + comparison), that's hard. We'll need human review for 15% of documents."

## TRANSLATION PATTERNS

Common business-to-technical and technical-to-business translations:

| Business Language | Technical Reality | PM Action |
|---|---|---|
| "The AI is slow" | P95 latency exceeds 3s, likely due to context window size or retrieval latency hitting rate limits | Measure and diagnose: Which component is slow? Token count? API response? |
| "Users don't trust it" | Acceptance rate is 34% (target: 60%); correction rate is high; users override output frequently | Dig deeper: Is distrust about hallucinations? Wrong domain? Or visibility (users can't explain why AI chose X)? |
| "Make it smarter" | Reduce hallucination rate in [specific category] from 8% to 3%; improve F1 score on edge cases | Specify the failure mode and acceptable improvement; "smarter" is not a metric |
| "It costs too much" | Per-query cost at $0.04 exceeds the $0.02 unit economics threshold at current volume | Identify the cost driver: API pricing, latency (longer context = more tokens), or volume scaling assumptions |
| "We need more AI features" | Which user problem requires probabilistic output that rules can't solve? | Challenge scope creep; AI doesn't fix vague requirements |

## AUDIENCE-SPECIFIC COMMUNICATION PATTERNS

Different stakeholders need different emphasis. Adapt your technical/business framing:

**Board / C-Suite:**
- Lead with business impact, risk, competitive position
- One number. One decision.
- Translate to: "This AI feature reduces churn by 5% ($2M annually) and blocks two competitor advantages. Risk: model failure in 5% of edge cases requires human review (add 1 FTE)."

**Engineering Leads:**
- Lead with architecture, constraints, failure modes
- Be specific, not visionary
- Translate to: "We're using RAG because fine-tuning would add 3-week training cycles. Precision target: 95% (miss a risk = liability). Recall target: 80%. P95 latency must be under 2s for 50-page documents."

**Data Scientists:**
- Lead with model performance, evaluation methodology, data quality
- Show the evals
- Translate to: "Classification accuracy is 94%, but we're measuring macro-F1. For minority classes, recall drops to 68%. We need stratified evaluation by user segment before shipping."

**Designers:**
- Lead with user impact, uncertainty UX, failure states
- Show the edge cases
- Translate to: "When confidence is below 70%, show a confidence band and offer 'Let me refine' option. When the model conflicts with user input, surface the conflict explicitly."

**Customer Success:**
- Lead with user-visible behaviors, known limitations, escalation paths
- Translate to: "AI accurately handles standard contracts but will hallucinate on novel clauses. Flag any output with <80% confidence. Escalation: Manual review available within 24h."

## DIAGNOSTIC QUESTIONS

Use these to test whether the bridge is working:

1. **Cross-audience clarity:** "If I showed this spec to our CTO and our VP Sales simultaneously, would they both know what to do next?"
   - If VP Sales says "Build this," and CTO says "That's not buildable," the bridge is broken.

2. **Feasibility check:** "Can an engineer estimate effort from the business definition alone? If yes, the bridge is working."
   - If the business definition omits latency/cost constraints, effort estimates will be wildly wrong.

3. **Hidden technical risk:** "Does the business definition hide technical risk?"
   - Example: "Real-time personalization" sounds simple until you realize it requires sub-100ms latency, which requires caching, which requires freshness trade-offs.
   - Example: "Hallucination-free AI" sounds good until you realize no model achieves this; you're actually building a verification harness.

*Think through:* What technical constraints exist that stakeholders can see — and which ones are invisible until you're deep in implementation? Focus on latency, data access, integration complexity, and model reliability.

*Low end:* The team has already scoped the technical approach. Known dependencies are documented. No surprises expected.

*Mid range:* Some unknowns remain. The data pipeline exists but hasn't been tested at scale. Integration is feasible but untested with the target system.

*High end:* Real-time personalization sounds simple until you realize it requires sub-100ms latency with live user context — which means re-architecting the data layer. Or vision processing assumes clean images; production uploads are blurry phone photos.

*Red flag:* The technical team says "that should be straightforward" without having done a spike. "Straightforward" is the most expensive word in software.

*Sharpen it:* "What's the cheapest experiment that would confirm or invalidate the technical risk? Can you build a 1-day prototype that tests the riskiest assumption?"

4. **Hidden business constraints:** "Does the technical definition hide business constraints?"
   - Example: "RAG pipeline" hides the actual business requirement: "Data must be updated daily without retraining." (RAG enables this; fine-tuning doesn't.)
   - Example: "3-second latency" hides the constraint: "Users abandon after 3 seconds of waiting; we measured it."

5. **Failure mode ownership:** "When this fails, who owns the problem—product or engineering?"
   - Bad answer: "It depends."
   - Good answer: "Model hallucinations below 5% are product's problem (scope, data quality). Below that, engineering's problem (model choice, inference optimization)."

*Think through:* When this feature fails — and it will fail — who finds out? Who fixes it? Is there a runbook? Is there a person whose job it is to respond within 30 minutes?

*Low end:* There's a named owner, a monitoring dashboard, an on-call rotation, and a documented escalation path. The team has already done a pre-mortem.

*Mid range:* Someone informally "owns" this. Monitoring exists but isn't wired to alerts. Failure would be noticed within a day, not an hour.

*High end:* Nobody explicitly owns AI failures. The feature silently degrades (outputs wrong answers, hallucinations increase) and nobody knows until a user escalates. There's no monitoring because "AI doesn't fail like traditional software."

*Red flag:* The launch plan doesn't include a rollback trigger, a monitoring threshold, or a named person who gets paged at 2am.

*Sharpen it:* "For the top 3 failure modes, who gets paged first? Is ownership assigned to a person (not a team) for the first 72 hours post-launch? What's the escalation sequence when the first on-call person is unavailable?"

## WORKED EXAMPLE: AI-Powered Contract Review

**Feature Concept:** "AI-powered contract review"

**Business Definition:**
"Reduces legal review time by 60% by flagging high-risk clauses (indemnification gaps, unusual payment terms, IP ownership issues) before human review. Saves $2M/year in outside counsel by catching issues at draft stage. Risk: Missed high-risk clauses create liability; false flags waste lawyer time. Success metric: Lawyers flag 95% of actual issues with <10% false flag rate."

**Technical Definition:**
"NER (Named Entity Recognition) + multi-class classification pipeline on contract PDFs. Converts PDFs to text, chunks by section, embeds sections, uses RAG to retrieve similar high-risk clauses from training set, classifies each section as high/medium/low risk. Precision target: 95% on high-risk classification (miss a risk = liability). Recall target: 80% (miss a non-risk = extra review, acceptable cost). P95 latency: 30s for 50-page document. Per-document cost: $0.15 (includes embedding + classification)."

**Bridge:**
"The 60% time reduction only works if precision is 95%. If we drop to 90%, lawyers see more false flags and spend extra time verifying. That cuts savings from $2M to $1.2M—still good, but changes ROI story. The 30s latency is acceptable because lawyers queue documents for review anyway; real-time isn't required. The $0.15 per-document cost scales to $30k/year at 200 documents/year, well under the $2M savings."

**Translation Layer:**
- Business requirement ("Reduce legal review time by 60%") → Technical constraint ("Precision ≥95% on high-risk classification")
- Technical constraint ("30s latency per document") → Business implication ("Batch processing is fine; no need for streaming or real-time inference")
- Business requirement ("Catch issues at draft stage") → Technical design choice ("RAG from historical high-risk clauses, not generic fine-tuning")

**Model Empathy:**
"Classification is easy for models. But classification of ambiguous contract language is hard — edge cases (unusual but legal payment terms) will confuse the model. We'll train on high/medium/low, but lawyers will still need to review anything flagged as medium."

---

## WHEN WRONG

- Pure engineering decisions with no business stakeholders
- Pure business decisions with no technical implications
- When both audiences are already deeply aligned (rare but possible)
- When speed matters more than precision in communication

---

## GENERATE THE DELIVERABLE

Once you've worked through the diagnostic questions and built clarity between business and technical definitions, synthesize your output according to the Universal Skill Protocol Section 11.

**Core deliverable:** Complete the template below, then create a visual summary using the **excalidraw-svg** skill. The diagram should show the bridge between business and technical definitions at a glance, making the dual-lens analysis immediately actionable for stakeholders. Reference the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md` for diagram standards (ravi-personal-branding palette, clear hierarchy, minimal text).

---

## OUTPUT FORMAT

Use this template when writing specs, PRDs, or strategy docs that must work for both audiences:

```
## Dual-Lens Brief: [Concept Name]

**Business Definition:**
[1 paragraph, no technical terms. Answer: What does this mean for revenue, risk, competitive position, customer trust?]

**Technical Definition:**
[1 paragraph, no business euphemisms. Answer: What does this mean for architecture, latency, cost, failure modes?]

**Bridge:**
[2-3 sentences explaining how technical constraints drive business outcomes. Where do they trade off?]

**Translation Layer:**
[3-5 key mappings between business requirements and technical constraints]

**Model Empathy:**
[Which task type (classification, generation, reasoning, retrieval, tool use)? Easy or hard? What's the business implication?]
```

**Example filled out above:** See "AI-Powered Contract Review" worked example above.

---

## VISUAL SUMMARY

After completing the primary output, invoke the **excalidraw-svg** skill to create a single Excalidraw SVG visual summary. This diagram captures the essence of the analysis in one glanceable image — making the deliverable 10x more impactful. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.
