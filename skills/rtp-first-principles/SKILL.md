---
name: rtp-first-principles
description: >
  Decomposes any AI product problem to its ONE irreducible operation by stripping vendor
  features, marketing language, and implementation details. Use when evaluating new feature
  proposals, diagnosing why a product failed, starting any product analysis, or when someone
  says "we should add AI to X", "is this feature necessary", "what's the real problem here",
  or "break this down to basics". Also triggers on reviewing competitive features or when
  a team wants to migrate to a different model/technology. Do NOT use when the problem is
  already well-decomposed by the team, when speed of iteration matters more than depth
  (early prototyping phase), or when making a low-stakes decision with reversible consequences.
imports: []
---

# First Principles

## DEPTH DECISION

**Go deep if:** Evaluating a new AI feature proposal or deciding between competing technical approaches. **Skim to questions if:** Quick check that decomposition was done (not just solution applied). **Skip if:** Problem is already well-decomposed and team is executing.

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../../../UNIVERSAL-SKILL-PROTOCOL.md):
1. Ask the Grounding Questions (Section 1) — at minimum: Who is the customer? What problem? What are we saying YES to and NO to?
2. Route depth: Executive Summary or Comprehensive Analysis?
3. Identify output format: Document, presentation, spreadsheet, or inline?

Then proceed with the skill-specific analysis below.

## THE TRAP

You will skip decomposition and jump to solutions. The bias is **anchoring** — whatever solution you saw first (a competitor's feature, a stakeholder's suggestion, a demo you liked) becomes the invisible frame for everything that follows.

The trap is most seductive when:
- A competitor just launched something similar
- A senior stakeholder already has a preferred solution
- The technology is exciting and you want to use it
- The deadline feels too tight for "abstract thinking"

Every AI feature killed in production traces back to this moment: someone skipped decomposition and jumped to "let's add AI to X."

### Solution Anchoring in AI

The most pernicious variant is **solution anchoring** specific to AI: You see a compelling demo (Claude handling customer support, GPT-4 writing marketing copy, an agent framework automating workflows) and then reverse-engineer a problem to justify building it. The feature feels inevitable because you've already fallen in love with the solution.

**Test for solution anchoring:** "Would I have identified this problem independently, or did I find it because I already had a solution in mind?" If you discovered the problem *after* encountering the solution, you have anchoring. Go back and find unbiased evidence that the problem exists (user research, support tickets, quantified friction). Otherwise, you're building because the technology is cool, not because users need it.

### Complexity Bias

Equally dangerous is **complexity bias** — the assumption that harder problems need more sophisticated solutions. In AI specifically: the belief that because LLMs can do amazing things, they're the right tool for every problem.

Sometimes the right answer is:
- A **lookup table** (FAQ routing: "Does user mention billing?" → escalate to billing queue)
- A **regex or string matcher** (email classification: identify spam keywords)
- A **simple heuristic** (prioritization: "tasks due today" → sort by deadline)
- A **decision tree** (eligibility: "income < $50k AND age > 65?" → eligible)

Ask: **"What's the simplest solution that solves 80% of cases?"** Often it's not AI. AI shines at the remaining 20% — the edge cases, ambiguous inputs, novel scenarios. Building a fancy neural classifier when a regex handles 95% of your traffic is overengineering.

## THE PROCESS

1. **State the user's actual problem in one sentence.** No technology words allowed. If you can't state it without mentioning AI, LLMs, agents, or models — you haven't found the problem yet.

2. **Decompose to the atomic operation.** Ask: "What is the ONE thing this user needs to accomplish?" Strip away interface, technology, workflow. Find the irreducible unit.

3. **Test for necessity.** For each component of the proposed solution:
   - If I remove this, does the atomic operation still complete? → YES = decoration, NO = load-bearing

4. **Map the determinism spectrum.** For each load-bearing component:
   - Solvable with rules? → Rules engine. No AI.
   - Requires pattern recognition on unstructured input? → AI candidate.
   - Requires judgment under ambiguity? → AI + human oversight.
   - "It depends"? → Hybrid. Define the boundary explicitly.

5. **State the first principle.** One sentence: "The irreducible operation is [X], which requires [rules/AI/hybrid] because [specific reason]."

6. **For AI components, separate model capability from product value.** Many features confuse what the model does with what the user needs:
   - **What the model actually does:** Generates tokens, ranks items, classifies inputs
   - **What the product needs:** Answers questions correctly, finds relevant results, prevents harmful outputs
   - **Gap:** Everything between. Model generates 95% accurate medical advice, but product needs 99.5% because users act on it. Model can classify toxicity, but product needs to explain *why* it's flagged. Confusing these kills products.

## WHAT THE MODEL ACTUALLY DOES

Here's what happens inside the black box. Strip the abstraction layer. At the bottom, every LLM:

- **Predicts the next token based on patterns in training data.** That's it. No understanding, no reasoning in a human sense. Token-by-token prediction.
- **Has no persistent memory between sessions** (unless you engineer memory: vector stores, databases, context carryover). Every conversation starts from zero.
- **Cannot access real-time information** (unless you give it tools: APIs, web search, knowledge bases). It only knows what was in its training data (and that data has a cutoff).
- **Cannot reason about things outside its training distribution.** If the problem requires knowledge from a domain not well-covered in training, it will hallucinate.
- **Gets worse as tasks require more sequential reasoning steps.** Chain-of-thought helps, but each step compounds error. A 10-step reasoning task is fragile.
- **Is probabilistic** — the same input yields different outputs (depending on temperature, randomness). You don't get deterministic results.

### Product Implication

Every feature that violates these fundamentals requires EXTRA engineering. That extra engineering IS your product. The model is just one component.

Examples:
- Need real-time data? → Build a RAG pipeline (retrieval-augmented generation). The product is the integration, not the model.
- Need consistent outputs? → Add verification layers, post-processing rules, feedback loops.
- Need memory of past conversations? → Build a session system, store context, manage token budgets.
- Need reasoning over complex workflows? → Decompose into smaller steps, use tools, build fallbacks for when the model fails.

The model does one thing well: predicting plausible completions. Everything else is architecture around it.

## REALITY CHECK

- **Failure mode:** Decomposing too far, losing sight of user context. An atomic operation extracted from its workflow is useless.
- **Cost trap:** First-principles takes time. Use for consequential decisions. Don't use to decide button colors.
- **Monitoring:** Track how many features survive decomposition unchanged. If "all of them" — you're rubber-stamping, not decomposing.

## THE LOOKUP TABLE TEST

Before committing to AI, ask: **"Could a lookup table, decision tree, or rules engine solve 80% of this?"** If yes, build that first, then add AI for the remaining 20%.

| Signal | Likely Answer | Example |
|--------|--------------|---------|
| Finite, enumerable inputs | Lookup table | FAQ routing, category classification with <50 categories, predefined templates |
| Clear if/then logic | Rules engine | Eligibility checks, compliance rules, pricing tiers, access control |
| Needs pattern matching on unstructured input | AI candidate | Free-text understanding, image analysis, anomaly detection, open-ended classification |
| Requires judgment under genuine ambiguity | AI + human | Risk assessment, content moderation, medical triage, editorial decisions |

### When AI is Technically Possible But Not Necessary

The hardest decision is when AI is technically possible but not necessary. An AI system that handles 95% of cases with 5% errors often underperforms a hybrid:
- **Rules engine** handles 80% reliably
- **Human escalation** handles 20% with judgment

Why? Because AI errors are unpredictable and destroy trust. A user who gets a wrong recommendation 1 in 20 times loses confidence in the whole system. A user who sees "escalating to a human" understands the boundary — it's explicit, not a mystery.

Example: Fraud detection
- **80/20 split:** Rule-based (obvious patterns: card used in two countries 6 hours apart, transaction 100x above average) handles 80%. ML handles edge cases.
- **95% AI:** Single ML model achieves 95% accuracy but fails unpredictably on novel attack patterns. Users distrust it. You build the 80/20 system instead.

## QUALITY GATE

- [ ] Problem stated without technology words
- [ ] Atomic operation identified in one sentence
- [ ] Each component tested for necessity (load-bearing vs decoration)
- [ ] Determinism spectrum mapped for load-bearing components
- [ ] First principle stated with specific reasoning

## DECOMPOSITION FOR AI AGENTS

Agent systems (systems that take sequential actions to accomplish a goal) need their own decomposition discipline. Not all sub-tasks within an agent need AI evaluation.

**Step 1: What is the end-to-end task?**
Example: "Research a company and write a 2-minute brief"

**Step 2: Decompose into sub-tasks**
- Search for company info → Filter results by relevance → Extract key facts → Synthesize into narrative → Format as brief

**Step 3: For each sub-task, ask: "Does this require ML, or is it deterministic?"**

| Sub-task | Type | Approach | Eval |
|----------|------|----------|------|
| Search | Deterministic | API call to knowledge base | Unit tests |
| Filter | Hybrid | Rules (relevance keywords) or semantic similarity | Rules: unit tests; ML: benchmark on held-out queries |
| Extract | ML candidate | NER or structured extraction | Precision/recall on labeled examples |
| Synthesize | ML (judgment) | LLM prompt + chain-of-thought | Human review, factuality checks |
| Format | Deterministic | Template + string substitution | Unit tests |

**Step 4: Only the ML components need AI evaluation.** The rest need unit tests.

This is Mahesh's "component decomposition" principle — not all sub-agents need AI evals. A search API doesn't need prompt engineering. Extraction does. Separate the wheat from the chaff, and you'll spend engineering budget wisely.

## CAPABILITY GAP ANALYSIS (Step 6 Expanded)

For each AI component, explicitly map:

**Model capability:** What the model CAN do (based on benchmarks, testing, documentation)
**Product requirement:** What the product NEEDS (user-acceptable quality, regulatory requirements, business SLAs)
**Gap:** The distance between capability and requirement
**Gap-closing options:** Better prompting, RAG, fine-tuning, human-in-the-loop, redesign the product, or accept the gap

**Example: Medical advice chatbot**

| Dimension | Value |
|-----------|-------|
| **Model capability** | 95% accuracy on medical Q&A benchmarks (e.g., MEDQA) |
| **Product requirement** | 99.5% accuracy (users act on advice; wrong advice causes harm) |
| **Gap** | 4.5 percentage points |
| **Gap-closing options** | Better prompting? (won't close 4.5pp). RAG? (requires curated medical DB, still probabilistic). Fine-tuning? (medical data is proprietary, regulatory issues). Human-in-the-loop? (doctor review for every answer = defeats automation goal). |
| **Conclusion** | This gap is likely unfillable with current models. **Redesign the product:** Position as "medical information assistant" (not "advisor"), add mandatory "consult your doctor" disclaimer flows, include trusted sources, build escalation to human doctors. Accept 95% capability; engineer the product around it. |

The moment you map this explicitly, you see the real constraint. Many products fail because teams confuse "95% accuracy on a benchmark" with "safe to deploy." The gap analysis makes the hard choice obvious.

## DIAGNOSTIC QUESTIONS

Before greenlit-ing any AI component, ask yourself:

1. **"If I remove the AI from this feature, what breaks?"** If the answer is "nothing essential" — you don't need AI. You thought the technology was cool, not that the problem required it.

2. **"What is the model ACTUALLY doing here?"** Not "it's answering questions" or "it's routing tickets." Think primitively: "It's classifying the input text into one of 10 categories" or "It's ranking a list of results by relevance score." State it in irreducible operations. If you can't state it primitively, you don't understand the component.

3. **"What percentage of inputs could be handled by a lookup table, regex, or decision tree?"** Be honest. If it's >70%, you're overbuilding. Start with the 70%, add AI for the tail.

4. **"Where is the model likely to fail?"** Think through failure modes:
   - Novel inputs outside training distribution?
   - Multi-step reasoning (unreliable)?
   - Edge cases (rarely seen in training)?
   - Adversarial inputs?
   - What's your fallback when it fails?

5. **"Am I building AI because the problem requires it, or because the roadmap says 'add AI'?"** This is the most honest question. If the roadmap is the driver, pause and decompose first.

## OUTPUT FORMAT

When you run first-principles decomposition on a feature, structure your output:

```
## First Principles Decomposition: [Feature Name]

**User problem (no tech words):**
[One sentence describing what the user is trying to accomplish, without mentioning AI, LLM, or technology]

**Atomic operation:**
[The irreducible unit the user needs completed]

**Components:**

| Component | Load-bearing? | Determinism | Approach | Eval type |
|-----------|--------------|-------------|----------|-----------|
| [Example] | YES | Rules | Regex matcher | Unit test |
| [Example] | YES | ML (unstructured → structured) | NER model | Precision/recall |
| [Example] | YES | Hybrid | Prompt + rules | Human review |
| [Example] | NO | Deterministic | Remove (decoration) | N/A |

**Capability gap (if applicable):**
Model can do X (benchmark: Y%). Product needs Z (requirement: W%). Gap = |W% - Y%|. Gap-closing strategy: [list options, recommend one].

**First principle:**
"The irreducible operation is [atomic operation], requiring [approach] because [specific reason]. Do not use [approach] because [specific reason]."
```

## WHEN WRONG

- Problem is genuinely novel with no precedent to decompose from
- Speed of iteration matters more than depth (early prototyping)
- Team has already done rigorous decomposition and needs to execute
- Problem is primarily political, not technical

---

## TRADE-OFF LEDGER

Complete the Trade-Off Ledger from the [Universal Skill Protocol](../../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 3.

## CONCLUSION

Follow the Conclusion Protocol from the [Universal Skill Protocol](../../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 5:
1. State the recommendation
2. Name the key trade-off
3. Acknowledge the biggest risk
4. Define the next action

---

## VISUAL SUMMARY

After completing the primary output, invoke the **excalidraw-svg** skill to create a single Excalidraw SVG visual summary. This diagram captures the essence of the analysis in one glanceable image — making the deliverable 10x more impactful. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.
