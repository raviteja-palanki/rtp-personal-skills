---
name: dual-lens
version: v1.0_latest
description: 'Makes one AI concept mean the same thing in two rooms: actionable for the business leader AND checkable by the engineer, so a wasted sprint never starts. Most cross-functional failures aren''t disagreement. They are two teams confidently building different readings of one sentence (the curse of knowledge). Write both the business definition and the technical definition, then test the bridge between them. Use when writing a PRD, strategy doc, or mixed-audience presentation, or when business and engineering read the same spec and picture different things. Skip pure-engineering or pure-business docs, or when both sides already agree. Pairs with: problem-ai-fit (feasibility decided first), stakeholder-communications (per-audience framing), first-principles (the one operation both lenses describe), trust-under-fog (business lens wants certainty the technical lens can''t give). Triggers: ''business doesn''t understand what we''re building'', ''engineering doesn''t see the business case''.'
imports: []
---

# Dual-Lens

**The objective:** make one AI concept mean the same thing in two rooms — actionable for the business leader AND checkable by the engineer — so a wasted sprint never starts. For the PM writing the spec, strategy, or roadmap that both sides will act on.

## The one idea

Picture the same one-page spec in front of two people. The VP of Sales reads it and says "great, build this." The CTO reads the *same page* and says "that's not buildable." Neither misread it. Neither was careless. They read the identical words and pictured two different products — and both walked away certain they were aligned.

That is the failure this skill exists to prevent, and the key insight is that **it is almost never disagreement.** Disagreement is loud and you can resolve it. This is silent: two teams confidently building different interpretations of one sentence, discovering the gap only when the demo doesn't match the deck and a sprint is already gone. The cause has a name — the **curse of knowledge**: once you understand something, you cannot imagine not understanding it, so your "clear" spec was clear only to you.

AI makes the gap wider than in ordinary software, for three specific reasons:
- **No visual analog.** What does "attention mechanism" *look* like? Ordinary software has screens and diagrams to point at; this doesn't.
- **Probabilistic failure.** "95% accuracy" reads as "always works" to one room and "one in twenty is wrong — for whom?" to the other.
- **No cost precedent.** Per-token cost has no analog in most leaders' experience, so the economics don't translate on their own.

So the move is not "explain it better in one language." It is: **write the concept twice — once for each room, both fully accurate — then test the bridge between them.** If a reader can go from the business definition to the technical definition and see how they're the same thing, the bridge holds. If the two read like documents about different products, you just found the wasted sprint before it started.

## How to use this skill

1. **Write both definitions and test the bridge** — the five-step process below. This is the spine.
2. **Reach for the right framework** when a specific gap shows up — Model Empathy (what the model finds easy vs. hard), Translation Patterns (business phrase ↔ technical reality), Audience Patterns (what each stakeholder needs to hear).
3. **Interrogate the bridge** with the diagnostic questions — most gaps hide as a business definition concealing a technical risk, or a technical definition concealing a business constraint.

## KEY TERMS (plain language)

- **Curse of knowledge** — once you understand something, you can't imagine not understanding it; the reason your "clear" spec wasn't.
- **Translation loss** — the nuance that disappears when one audience's language is converted into another's; it fails silently, in both directions.
- **RAG (retrieval-augmented generation)** — the AI looks up your documents before answering, so knowledge updates daily without retraining the model.
- **Context window** — how much text the model can consider at once; bigger costs more and runs slower.
- **Streaming output** — showing the answer as it's generated instead of after; changes *perceived* speed without changing actual speed.
- **Inference** — the act of the model producing an answer; the thing you pay for per use.
- **P95 latency** — the response time the slowest 5% of requests feel; more honest than the average.

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../../../UNIVERSAL-SKILL-PROTOCOL.md). At minimum: name the concept being defined, and name the two rooms that must act on it. Then route depth (a full two-definition brief for a new AI concept crossing into a roadmap commitment vs. a quick check that both teams use the same words) and output format. Skip it when the decision lives entirely in one domain (pure infra, pure commercial).

## THE PROCESS — write both, test the bridge

1. **Write the business definition first.** One paragraph: what does this mean for revenue, risk, competitive position, or customer trust? No technical terms. If a CFO can't act on it, rewrite.
2. **Write the technical definition second.** One paragraph: what does this mean for architecture, latency, cost per request, failure modes, monitoring? No business euphemisms. If a senior engineer can't validate it, rewrite.
3. **Test the bridge.** Can someone read the business definition, then the technical one, and see how they connect? If they feel like separate documents about different things, the bridge is broken — fix it before anyone builds.
4. **Add the translation layer.** For each key technical decision, write its business implication; for each key business requirement, its technical constraint. *"Using RAG instead of fine-tuning [technical] means we can update knowledge daily without retraining [business]." "Response under 2s [business] means streaming output and smaller context windows [technical]."*
5. **Validate with both audiences.** Show the business definition to a business stakeholder ("can you act on this?") and the technical one to an engineer ("can you build from this?"). Their answers are the test, not your confidence.

**The failure mode to guard against:** dumbing the business definition down until it's *wrong*. Dual-lens means both definitions are accurate — not that one is simplified into falsehood.

## THE THREE FRAMEWORKS — reach for the one that fits the gap

### Model Empathy — when the gap is "what can the AI actually do?"

Don't say "accuracy." Map the task type to what models find easy vs. hard, then translate to a business constraint.

| Task type | Easy for the model | Hard for the model | PM implication |
|---|---|---|---|
| Classification | Binary calls on clear categories | Ambiguous categories, boundary cases | Fix the taxonomy before building; don't expect the model to learn nuance from examples alone |
| Generation | Structured output (JSON, summaries), paraphrasing | Novel creative work, factual precision under uncertainty | Verify facts independently; use schemas to constrain format |
| Reasoning | Single-hop logic, pattern-matching in training data | Multi-step chains, temporal constraints | Decompose into steps; validate each one |
| Retrieval | Keyword and semantic similarity | Negation ("not red"), ordering ("before 2020"), counting ("exactly 3") | Pre-filter results; don't rely on the model to rank/filter |
| Tool use | Single API calls, straightforward sequences | Multi-tool orchestration, error recovery | Build a tool harness; don't ask the model to debug failed calls |

*Use it:* a stakeholder says "extract clauses from contracts." Translate: "That's classification — easy. But extracting *conflicting* clauses is reasoning + comparison — hard. Budget human review for ~15% of documents."

### Translation Patterns — when the gap is a vague business phrase

| Business language | Technical reality | PM action |
|---|---|---|
| "The AI is slow" | P95 latency exceeds 3s — context-window size or retrieval hitting rate limits | Diagnose which component: token count? API response? |
| "Users don't trust it" | Acceptance rate 34% vs. 60% target; users override often | Is it hallucination, wrong domain, or unexplained choices? |
| "Make it smarter" | Cut hallucination in [category] from 8% to 3%; raise F1 on edge cases | "Smarter" is not a metric — specify the failure mode and target |
| "It costs too much" | $0.04/query exceeds the $0.02 unit-economics threshold at volume | Find the driver: API price, context length, or scaling assumption |
| "We need more AI features" | Which user problem needs probabilistic output rules can't give? | Challenge scope creep; AI doesn't fix vague requirements |

### Audience Patterns — when the gap is "which room am I in?"

Same concept, different lead for each stakeholder:

- **Board / C-suite** — lead with business impact, risk, competitive position. One number, one decision. *"Reduces churn 5% ($2M/yr), blocks two competitor moves. Risk: 5% of edge cases need human review — add 1 FTE."*
- **Engineering leads** — lead with architecture, constraints, failure modes; specific, not visionary. *"RAG, not fine-tuning (avoids 3-week training cycles). Precision 95%, recall 80%, P95 under 2s for 50-page docs."*
- **Data scientists** — lead with model performance, eval methodology, data quality; show the evals. *"94% accuracy on macro-F1, but minority-class recall drops to 68% — need stratified eval by segment before shipping."*
- **Designers** — lead with user impact, uncertainty UX, failure states. *"Below 70% confidence, show a confidence band and a 'refine' option; surface conflicts with user input explicitly."*
- **Customer success** — lead with visible behaviors, known limits, escalation paths. *"Handles standard contracts; will hallucinate on novel clauses. Flag anything under 80% confidence; manual review within 24h."*

## DIAGNOSTIC QUESTIONS — is the bridge actually holding?

1. **Cross-audience clarity.** If the CTO and the VP of Sales read this simultaneously, would both know the next step? If Sales says "build this" and the CTO says "not buildable," the bridge is broken.
2. **Does the business definition hide a technical risk?** "Real-time personalization" sounds simple until it means sub-100ms latency → caching → freshness trade-offs. "Hallucination-free AI" sounds good until you realize no model achieves it — you're actually building a verification harness. (Watch the word "straightforward" said before anyone has run a spike — the most expensive word in software.)
3. **Does the technical definition hide a business constraint?** "RAG pipeline" hides the real requirement: "data must update daily without retraining." "3-second latency" hides "users abandon after 3 seconds — we measured it."
4. **Failure-mode ownership.** When this fails, who owns it — product or engineering? "It depends" is the wrong answer. Right: "Hallucinations above 5% are product's problem (scope, data quality); below that, engineering's (model choice, inference)." If the launch plan has no rollback trigger, no monitoring threshold, and no named person paged at 2 a.m., that gap is the finding.

## WORKED EXAMPLE — AI-powered contract review

**Business definition:** "Cuts legal review time 60% by flagging high-risk clauses (indemnification gaps, unusual payment terms, IP issues) before human review. Saves $2M/yr in outside counsel. Risk: a missed high-risk clause creates liability; false flags waste lawyer time. Success: lawyers see 95% of real issues flagged with <10% false flags."

**Technical definition:** "NER + multi-class classification on contract PDFs: PDF→text, chunk by section, embed, RAG-retrieve similar high-risk clauses, classify each section high/medium/low. Precision 95% on high-risk (a miss = liability); recall 80% (a false flag = extra review, acceptable). P95 latency 30s for a 50-page doc. Cost $0.15/document."

**Bridge:** "The 60% time saving only holds at 95% precision — drop to 90% and lawyers verify more false flags, cutting savings from $2M to $1.2M (still good, different ROI story). 30s latency is fine because lawyers batch-queue reviews; real-time isn't needed. $0.15/doc → ~$30k/yr at 200 docs, far under the $2M savings."

**Translation layer:**
- Business *"reduce review 60%"* → technical *"precision ≥95%."*
- Technical *"30s latency"* → business *"batch processing is fine, no streaming needed."*
- Business *"catch issues at draft stage"* → technical *"RAG from historical high-risk clauses, not generic fine-tuning."*

**Model empathy:** classification is easy; classification of *ambiguous* contract language is hard — unusual-but-legal terms will confuse it, so anything flagged "medium" still gets a lawyer.

## WHERE THIS SKILL MEETS THE REST OF YOUR STACK

Dual-lens gets one concept to mean the same thing in two rooms. That puts it *after* the capability question is settled and *before* the delivery happens — a translation layer, not a decision-maker — so it hands off in both directions.

**Assumes this is already decided (a boundary, not a hand-off):**
- **`rtp-problem-ai-fit`** — dual-lens translates a capability call that's already been made. If the real question is still "can AI even do this?", that's problem-ai-fit's job — writing two beautiful, aligned definitions of a feature that shouldn't be built is a wasted bridge, not a solved one.

**Goes deeper on one gap:**
- **`rtp-first-principles`** — when the two lenses keep drifting, strip the concept to the single atomic operation both must describe; if you can't, the bridge has nothing to stand on.
- **`rtp-trust-under-fog`** — when the business lens demands a certainty ("guarantee 99%") the technical lens honestly can't give; this handles communicating probabilistic reality without over-promising.
- **`rtp-stress-test`** — when diagnostic Q2 surfaces a technical risk the business definition hid (latency, cost spiral, adversarial exposure); this prices it at production scale.

**Acts on what this skill decides:**
- **`rtp-stakeholder-communications`** — once the concept is bridged, this tailors the *delivery* per audience (exec brief, eng brief, customer note) with AI-confidence framing. Dual-lens defines; this communicates.
- **The failure-ownership answer travels forward.** Diagnostic Q4 forces a named owner ("hallucinations above 5% are product's; below that, engineering's") — that answer is exactly what `rtp-stress-test`'s Dimension 4 and `rtp-production-observability`'s on-call runbook later assume already exists. Decide it once, here, so it isn't re-litigated at 2 a.m. by whoever's on call.

Run dual-lens to align the meaning; run the first group to check the meaning is worth aligning at all or needs to go deeper; run the second group once the bridge holds and it's time to deliver and monitor.

## REALITY CHECK

- **Two definitions cost 2x the writing.** For a load-bearing concept, that's an investment; for a minor decision, one audience is fine.
- **Some orgs punish speaking both languages** ("too technical," "too business-y"). Dual-lens needs the organizational permission to do it.
- **The bridge is the deliverable, not the two definitions.** Two accurate definitions that don't connect are still two wasted sprints waiting to happen.

## QUALITY GATE

- [ ] Business definition written — actionable by a non-technical leader, and still accurate
- [ ] Technical definition written — validatable by a senior engineer
- [ ] Bridge tested — both definitions demonstrably describe the same underlying concept
- [ ] Translation layer added for each key decision (business↔technical)
- [ ] Validated with at least one representative from each room
- [ ] Diagnostics run — no business definition hiding a technical risk, no technical definition hiding a business constraint; failure ownership named

## OUTPUT FORMAT

```
## Dual-Lens Brief: [Concept Name]

**Business Definition:** [1 paragraph, no technical terms — revenue, risk, position, trust]
**Technical Definition:** [1 paragraph, no business euphemisms — architecture, latency, cost, failure modes]
**Bridge:** [2–3 sentences: how technical constraints drive business outcomes, and where they trade off]
**Translation Layer:** [3–5 business↔technical mappings]
**Model Empathy:** [task type · easy or hard · business implication]
**Failure ownership:** [which failures are product's, which are engineering's, who is paged]
```

## WHEN WRONG

- Pure engineering decisions with no business stakeholders.
- Pure business decisions with no technical implications.
- When both audiences are already deeply aligned (rare, but possible).
- When speed matters more than precision in communication.

## TRADE-OFF LEDGER

By writing the concept twice, you bet that a couple of hours of dual definition now is cheaper than a sprint spent building two different products from one sentence. You give up some velocity and the comfort of a single, familiar audience. **Reversible?** Fully — it changes words, not code. **The hidden trade:** the failure isn't over-explaining, it's *false alignment* — everyone nods at the one-pager and builds divergently, and the cost lands weeks later when the demo doesn't match the deck. **Confidence: High.** What would change it: a concept living entirely in one domain, where the second lens is ceremony.

## CONCLUSION

Follow the Conclusion Protocol from the [Universal Skill Protocol](../../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 5: state the recommendation (the bridged concept, both lenses accurate), name the key trade-off (time to write twice vs. the wasted sprint avoided), acknowledge the biggest risk (false alignment — a bridge that reads fine but doesn't hold), and define the next action (validate each definition with its room, with a named owner).

## VISUAL SUMMARY

After the primary output, invoke the **excalidraw-svg** skill for one visual: the same concept in the center with two lenses — BUSINESS (revenue/risk/trust) and TECHNICAL (architecture/latency/cost) — drawn as two panels, and the BRIDGE explicitly between them showing one translation-layer mapping, so a viewer sees at a glance that these are two views of one thing, not two things. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.
