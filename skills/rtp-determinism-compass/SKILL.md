---
name: rtp-determinism-compass
description: 'Deterministic vs probabilistic classification: what must stay consistent, what can vary, where variation is risk/value. Quality gates, testing, caching. Use when: architecting, QA design, spec review. Triggers: ''variation acceptable'', ''test AI component'', ''cache'', ''reproducible'''
---
# Determinism Compass

## DEPTH DECISION

**Go deep if:** Classifying components of a new feature as deterministic vs probabilistic (architecture design phase). **Skim if:** Quick check on whether testing approach matches system type. **Skip if:** System is fully deterministic or the architecture is already locked.

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md):
1. Ask the Grounding Questions (Section 1) — at minimum: Who is the customer? What problem? What are we saying YES to and NO to?
2. Route depth: Executive Summary or Comprehensive Analysis?
3. Identify output format: Document, presentation, spreadsheet, or inline?

Then proceed with the skill-specific analysis below.

## THE TRAP

**Over-determinism:** Treating all AI outputs as if they need exact reproducibility. You over-invest in seed pinning, versioning, and snapshot testing for components where variation is a feature, not a bug. You kill generative value by forcing false consistency.

**Under-determinism:** Ignoring that most features are hybrids — deterministic routing/formatting wrapped around probabilistic generation. You test the whole thing as if it's all probabilistic and miss bugs in the deterministic parts. You fail to pin seeds where reproducibility matters.

Reality: **Most features sit on a spectrum.** Routing is deterministic. Classification temperature matters. Generation range is acceptable. Formatting is deterministic. Output caching is probabilistic with deterministic fallback.

### Non-Determinism Compounds in Multi-Agent Systems

A single model call with 5% variation is manageable. Chain 4 agents sequentially and variation compounds: the downstream agent operates on a different input each time. A pipeline that passes 95% of the time per step passes only ~81% end-to-end across 4 steps. This is why Anthropic measures **pass^k** (all k trials succeed) not just **pass@k** (at least one succeeds). For customer-facing agents, consistency matters as much as capability.

## DIAGNOSTIC QUESTIONS

For each component, ask:
1. **Input:** Structured (email, ID, date) or unstructured (free text, conversation)?
2. **Output:** One right answer (deterministic) or acceptable range (probabilistic)?
3. **Variation tolerance:** Is the same input ever allowed different outputs? Is consistency a feature requirement or a testing convenience?
4. **Risk zone:** Where does variation create customer risk vs product value? (E.g., legal docs require determinism; creative writing requires variation.)
5. **Reproducibility need:** Must this be pinned for debugging? Or is majority voting + fallback enough?
6. **Compounding risk:** If this component feeds another, does variation propagate? What's the end-to-end pass rate?

### Q4 Nudge Block: Variation Tolerance

**Think through:** What level of output variation is acceptable for this feature? Consider: user expectation of consistency, downstream system dependencies, regulatory requirements, brand voice consistency.

**Low:** Product recommendations — users expect some variety; 20–30% variation is acceptable.

**Mid:** Customer support responses — tone should be consistent but exact wording can vary; 5–10% variation acceptable.

**High:** Financial calculations, medical dosing, legal compliance — zero tolerance for variation. Must be deterministic (rules/lookup).

**Red flag:** You haven't tested variation across 100+ runs of the same input. Variation looks acceptable on 5 tests but catastrophic at scale.

**Sharpen it:** Run the same input 50 times. Measure the variance in output. If variance exceeds your tolerance, you need deterministic constraints (rules, templates, structured output) — not more prompting.

### Spectrum Anchors for Q4

Not all "variation tolerance" is the same. Use these anchors to calibrate where your feature sits:

**Low variation risk (deterministic end):**
- Code autocomplete: Wrong completion is annoying, not dangerous. Users verify before accepting.
- Grammar suggestions: User reviews every change. Variation is expected and fine.
- Search ranking: Different results per query is the feature, not a bug.

**High variation risk (probabilistic → requires guardrails):**
- Medical symptom triage: Two users with identical symptoms should get the same safety guidance. Variation = liability.
- Legal contract review: Flagging a clause one day and missing it the next destroys trust.
- Financial calculations: "Approximately correct" is not acceptable for numbers users act on.
- Safety-critical instructions: Assembly instructions, medication dosage, emergency procedures.

**The test:** "Would a user feel betrayed if they got a different answer to the same question tomorrow?" If yes, you're in high variation risk territory. Design accordingly: deterministic outputs for the critical path, AI-generated only for low-stakes suggestions.

## THE PROCESS

**Step 1: Temperature calibration by domain**
- Legal/compliance: 0 (always deterministic, always pinned)
- Support response: 0.2–0.3 (consistent style, variation acceptable in facts)
- Classification/extraction: 0.3–0.5 (structured output, low temperature)
- Personalization/reasoning: 0.5–0.7 (variation expected, but within guardrails)
- Creative generation: 0.7–1.0 (variation is the goal)

**Step 2: Hybrid pattern checklist**
Most real features are: **[Deterministic wrapper] → [Probabilistic core] → [Deterministic formatter]**
- Validation & routing: Always deterministic
- Generation/classification: Probabilistic (or rules if high-confidence)
- Output formatting/cleanup: Deterministic (guardrails, truncation, escaping)

**Step 3: Apply classification matrix** (refined)

| Input | Output Type | Variation Cost | Pattern |
|-------|-------------|-----------------|---------|
| Structured | Deterministic | High risk | RULES |
| Unstructured | Deterministic (classes) | Medium risk | AI + seed pin |
| Unstructured | Probabilistic (text) | Low risk | AI + version pin |
| Either | Partially deterministic | Medium | HYBRID (pin + test range) |

**Step 4: Production quality gates by variation level**
- **Full determinism** (legal, routing): Version pin, snapshot tests, seed pin, exact match assertions
- **Pinned variation** (support, classification): Seed pin, output cache, majority voting fallback
- **Bounded variation** (generation): Version pin, confidence threshold, output range tests
- **Acceptable drift** (creative): Version pin only (no seed pin)

**Step 5: Snapshot & reproducibility strategy**
- Pin model version (always)
- Pin seed for classification/extraction (if reproducibility needed for debugging)
- Cache outputs for high-frequency calls (deterministic by definition once cached)
- Use majority voting (3+ samples) when seed-pinning is too expensive
- Never snapshot-test probabilistic generation as exact matches; test output properties instead (length, format, presence of required fields)

## PASS@K vs PASS^K: CONSISTENCY METRICS (Anthropic Framework)

Two metrics capture different quality dimensions:

**pass@k** = probability of at least one correct solution in k attempts
- "Shot on goal" success
- Measures: Can the system solve this problem at all?
- Use for: capability evaluation, frontier testing, internal benchmarks

**pass^k** = probability that ALL k trials succeed
- Measures: consistency and reliability
- Use for: customer-facing features, production readiness, regression testing
- If pass@1 = 90%, pass^3 ≈ 73%. That means 27% of the time, at least one of three tries fails.

**PM Decision:** For customer-facing features, optimize for pass^k. For internal tools where retries are cheap, optimize for pass@k.

| Feature Type | Primary Metric | Threshold | Rationale |
|-------------|---------------|-----------|-----------|
| Customer-facing agent | pass^3 > 85% | Consistency matters more than capability | Users don't retry 3x |
| Internal code review | pass@3 > 95% | At least one good review is enough | Developer picks best |
| Batch classification | pass@1 > 90% | Per-item accuracy | No retry loop |
| Safety filter | pass^10 > 99.9% | Must ALWAYS catch harmful content | One miss is a failure |

## STATISTICAL QA FOR NON-DETERMINISTIC SYSTEMS

Traditional QA (exact match testing) doesn't work for AI. Replace with:

**Property-based testing:** Instead of "output must be X," test "output must have properties A, B, C"
- Is it valid JSON/format?
- Does it contain required fields?
- Is length within expected range?
- Does it pass safety filters?
- Is confidence score within bounds?

**Distribution testing:** Run the same input 10 times. Check:
- Are all outputs within acceptable range?
- Is variance within tolerance?
- Do outliers exceed safety thresholds?

**Regression via eval sets:** Don't compare exact outputs. Compare eval scores.
- Maintain a frozen eval set of 200+ examples with binary pass/fail criteria
- Run before every model update or prompt change
- If pass rate drops >2%, investigate before deploying
- This IS your regression suite for probabilistic systems

## WORKED EXAMPLE

**Feature: AI contract clause extractor**

| Component | Type | Temperature | Test Strategy | Pin Strategy |
|-----------|------|-------------|---------------|-------------|
| PDF parser | Deterministic | N/A | Unit tests, exact match | Version pin library |
| Clause classifier | Hybrid | 0.3 | Property tests (valid categories), majority vote (3x) | Seed + version pin |
| Risk scorer | Probabilistic | 0.5 | Distribution test (10 runs, variance < 0.2), eval set | Version pin |
| Summary generator | Probabilistic | 0.6 | Property tests (length, required fields, no PII), human eval sample | Version pin |
| Output formatter | Deterministic | N/A | Snapshot tests, exact template match | Version pin |

**End-to-end pass rate:** If each step passes 95%, pipeline passes 77% (0.95^5). Need 98%+ per step for 90% end-to-end. This drives the decision to use majority voting on the classifier.

### Q6 Nudge Block: Compounding Risk

**Think through:** If this feature's output feeds into another step, what's the compounded error rate? Each AI step multiplies uncertainty.

**Low:** Single-step output consumed directly by user. Error rate = model error rate. (Example: search results.)

**Mid:** 2–3 step chain. Compounded accuracy = step1 × step2 × step3. A 95% → 95% → 95% chain yields 85.7% end-to-end accuracy. (Example: extract → summarize → recommend.)

**High:** 4+ step chain or loop. Compounded accuracy drops fast: 95%^5 = 77.4%. At 90% per step: 90%^5 = 59%. (Example: agent with planning → tool calls → evaluation → retry.)

**Red flag:** You're quoting per-step accuracy to stakeholders. The number they care about is end-to-end accuracy, which is always lower.

**Sharpen it:** Calculate your chain's end-to-end accuracy: multiply each step's accuracy. If the result is below your quality bar, add deterministic checkpoints (validation rules, human review) between steps.

### The Compounding Math

Single-step accuracy feels fine until you chain steps together.

**The formula:** If each step succeeds at rate r, an n-step pipeline succeeds at r^n.

| Per-step accuracy | Steps | End-to-end success rate |
|---|---|---|
| 99% | 5 | 95.1% |
| 95% | 5 | 77.4% |
| 90% | 5 | 59.0% |
| 85% | 5 | 44.4% |
| 80% | 5 | 32.8% |

**What this means in practice:**
A 5-step agent pipeline where each step is 95% reliable produces the correct final answer only 77% of the time. That's a 1-in-4 failure rate — even though every individual step looks fine.

**This is why majority voting (pass^k) exists:**
If you run the same pipeline 3 times and take the majority answer, you need all 3 to agree. For a pipeline with 77% end-to-end accuracy:
- Pass^3 (all 3 agree on correct answer): ~0.77^3 = 45.7%
- But if you're selecting the majority: probability of at least 2 correct in 3 = ~84%

**The design implication:** Before building a 5-step agent pipeline, calculate the expected end-to-end accuracy. If per-step accuracy is below 90%, consider: (a) reducing pipeline length, (b) adding a verification step, or (c) accepting that some steps need human review.

## GENERATE THE DELIVERABLE

Follow the **Deliverable Protocol** from the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md), Section 11:
- Choose format: spreadsheet matrix, specification document, or presentation
- Embed the classification matrix (Step 3 from THE PROCESS) as the core artifact
- For each component, document: determinism level, temperature, test strategy, pin strategy, pass@k/pass^k target
- Calculate and display end-to-end pass rates for multi-step pipelines using the compounding math formula
- Include explicit variation budget allocation and reproducibility requirements
- Surface trade-offs: cost of pinning vs value of reproducibility, testing investment vs variation tolerance

## OUTPUT FORMAT

```
## Determinism Classification: [Feature Name]

| Component | Determinism Level | Temperature | Test Strategy | Pin Strategy | pass@k target |
|-----------|------------------|-------------|---------------|-------------|---------------|

End-to-end consistency: pass^[k] = [target]
Variation budget: [which components allowed to vary, how much]
Reproducibility: [what must be exactly reproducible for debugging]
Regression strategy: [eval set size, cadence, threshold]
```

## REALITY CHECK

- **Snapshot test trap:** Most AI engineers snapshot exact outputs from probabilistic systems, then flake when re-training. Instead, test output properties (is it valid JSON? Does it have a title? Is length <500 chars?).
- **Hybrid complexity is real:** Each deterministic-to-probabilistic handoff is a failure point. Document the contract: what inputs trigger the boundary? What's the fallback?
- **Caching IS determinism:** Cached output = deterministic by definition. Use liberally for deterministic wrappers and high-call APIs.
- **Economics still matter:** If you're pinning seeds and caching every generation to ensure reproducibility, ask: is reproducibility actually required here, or are you optimizing for test convenience?
- **Non-determinism is not a bug.** For generative and creative features, variation is the product. Don't engineer it out. Design your tests to embrace it.

## QUALITY GATE (7 binary checks)

- [ ] Each feature component classified: deterministic, probabilistic, or hybrid (with handoff contract)
- [ ] Temperature/variation tolerance documented for each probabilistic component
- [ ] Testing strategy assigned: snapshot (deterministic only), property tests (probabilistic), majority voting (variable), or caching (hybrid wrapper)
- [ ] Reproducibility requirements explicit: "must be pinned" vs "acceptable drift" vs "cache enough"
- [ ] Production patterns chosen: seed pinning, version pinning, output caching, majority voting, confidence thresholding — match to risk level
- [ ] pass@k vs pass^k decision made for each customer-facing component
- [ ] End-to-end pass rate calculated for multi-step pipelines

## WHEN WRONG

- Early-stage exploration (prototyping for learning, not production readiness)
- Pure-generative features (where determinism has no customer value)
- After architecture is locked (this is a design-time skill)
- Low-stakes personalization (where drift is a feature)

---

## TRADE-OFF LEDGER

Complete the Trade-Off Ledger from the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md), Section 3.

## CONCLUSION

Follow the Conclusion Protocol from the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md), Section 5:
1. State the recommendation
2. Name the key trade-off
3. Acknowledge the biggest risk
4. Define the next action

---

## VISUAL SUMMARY

After completing the primary output, invoke the **excalidraw-svg** skill to create a single Excalidraw SVG visual summary. This diagram captures the essence of the analysis in one glanceable image — making the deliverable 10x more impactful. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.
