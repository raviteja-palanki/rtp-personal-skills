---
name: determinism-compass
version: v1.3_latest
description: 'Which parts of your AI product must give the same answer every time, and where is variety acceptable, or even the point? Sorts every component into ''must be consistent'' vs. ''may vary'', then sets the testing, caching, and autonomy rules that follow from the sort. Use when: designing the architecture, QA planning, spec reviews. Pairs with: autonomy-spectrum (how far the AI may act alone), problem-ai-fit (whether AI belongs here at all). Triggers: ''variation acceptable'', ''test AI component'', ''cache'', ''reproducible'
imports: []
---

# Determinism Compass

## DEPTH DECISION

**Go deep if:** Classifying components of a new feature as deterministic vs probabilistic (architecture design phase). **Skim if:** Quick check on whether testing approach matches system type. **Skip if:** System is fully deterministic or the architecture is already locked.

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../../../UNIVERSAL-SKILL-PROTOCOL.md):
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

## KEY TERMS (plain language)

- **Deterministic vs. probabilistic** — a task with one right answer that should never vary (deterministic) versus one where a range of outputs is acceptable (probabilistic).
- **Variation tolerance** — how much the same input is allowed to produce different outputs before it becomes a risk.
- **Temperature** — a dial on how random or creative a model's output is; low for consistency, high for variety.
- **pass@k vs. pass^k** — succeeded on at least one of k tries versus succeeded on all k tries (the bar for consistency).
- **Property-based testing** — instead of checking for an exact output, check that the output has the required properties (valid format, right fields, within length).
- **The verifiability cut line** — the point up to which you can still check how a system was set up; autonomy can rise to it and must stop where it would need checking every single output.
- **Reversibility** — whether a wrong call can be walked back cheaply (a two-way door) or is a one-way commitment. A second axis alongside predictability; see "Three 2026 Additions to the Compass" below.

## DIAGNOSTIC QUESTIONS

For each component, ask:
1. **Input:** Structured (email, ID, date) or unstructured (free text, conversation)?
2. **Output:** One right answer (deterministic) or acceptable range (probabilistic)?
3. **Variation tolerance:** Is the same input ever allowed different outputs? Is consistency a feature requirement or a testing convenience?
4. **Risk zone:** Where does variation create customer risk vs product value? (E.g., legal docs require determinism; creative writing requires variation.)
5. **Reproducibility need:** Must this be pinned for debugging? Or is majority voting + fallback enough?
6. **Compounding risk:** If this component feeds another, does variation propagate? What's the end-to-end pass rate?
7. **Reversibility:** If this component or the decision to ship it turns out wrong, can you walk it back cheaply (two-way door), or is it a one-way commitment? This is a separate question from predictability (see "Three 2026 Additions to the Compass" below).

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

### From Sourcing to Autonomy — Three 2026 Additions

**Task type maps to how much autonomy and accountability to give.** A four-way sort of *work* lands on this same spectrum. Routine, measurable, rules-based tasks are the deterministic end — high autonomy and full automation belong here. Regulated, high-liability, judgment-heavy tasks are the probabilistic, human-in-the-loop end — the AI only *assists*, a named human stays responsible, and the work is governed "through risk forums rather than simple service-level agreements" (contract targets like speed or volume). **Why it matters:** when work carries real liability, you don't manage it with a contract metric; you keep a named human accountable — the sourcing decision and the autonomy decision are the same call reached from opposite ends of the org. **When this is wrong:** a routine-looking task can still carry hidden liability (a "simple" claims-intake error that cascades), so check liability separately from how routine the task looks.
*(Source: "AI Is Rewriting the Economics of Outsourcing," Agrawal, HBR, 5 Jun 2026.)*

**The verifiability cut line — how far autonomy can go.** Checking every single output by hand doesn't scale; require a human to review every output and you cancel the efficiency that justified the AI. The fix is to move human judgment up front, to the *setup* — goals, limits, escalation paths, thresholds. So the rule: **let the AI run as far as you can still check the setup, and stop where it would need someone checking every output.** You can hand off as far as you can verify the *design*, no further. **Why it matters:** this is why over-reaching rollouts get pulled back to a human-present mode — they were pushed past the point where the setup could be checked, into territory needing per-output review, which isn't feasible. **When this is wrong:** "can I check the setup?" is itself a judgment call — a team can convince itself it verified a setup it didn't understand; the line sets the ceiling, not the guarantee.
*(Source: "Beyond Verification," Renieris, Kiron, Mills & Kleppe, MIT Sloan Management Review, 12 May 2026. Full treatment in `rtp-autonomy-spectrum`.)*

**Reversibility is the second axis this compass needs, not just predictability.** Everything above sorts components by one axis: can you predict the output (deterministic) or not (probabilistic). A July 2026 HBR management-tips compilation carried two tips that flatly contradict each other: move before you have full clarity, versus pull written dissent from the team before you execute. Neither tip names the variable that decides which applies: **reversibility**, whether the call is a two-way door you can walk back through or a one-way door you can't. Cross reversibility against predictability and the single spectrum becomes a 2x2:

| | Predictable outcome | Unpredictable outcome |
|---|---|---|
| **Reversible (two-way door)** | Just build it. Process overhead doesn't earn its cost here. | Move fast and iterate. The cost of being wrong is close to the cost of running the experiment. |
| **Irreversible (one-way door)** | Verify hard before committing, then move with confidence. | Pull written dissent first. The cost of being wrong is the whole commitment, and dissent is the cheapest signal available before you pay it. |

**Why it matters:** teams read "move fast" and "get dissent first" as competing philosophies and pick one as a personality trait. They aren't competing; they answer different cells of the same table. A team that defaults to momentum blows through irreversible commitments it never stopped to test. A team that defaults to deliberation spends a dissent-gathering process on a reversible pilot that would have taught the same lesson for the price of running it once.

**Application note:** a July 2026 Watkins enterprise-leadership podcast episode makes the same point about AI infrastructure decisions specifically, from the other direction. On those calls the probability of being wrong usually can't be reduced this early, because the team doesn't know enough yet and won't for a while, so the only lever available is cutting the price of being wrong: smaller blast radius, less sunk cost, an easier walk-back. Read against the 2x2 above, that is the same move as sliding a decision left into the reversible column when you cannot slide it up into the predictable row.

**When this is wrong:** a documented decision class where deliberation reliably beat rapid iteration on something cheaply reversible, with no irreversible side effect, would break this. Nothing in the corpus so far shows that pattern.

*(Source A: HBR management-tips compilation, Jul 2026 — 10 tips, zero statistics, no primary sources opened; the contradiction is this analysis's own cross-reading of two of its tips, not a claim from either underlying author. Tier: unverified, single compilation. Source B: Watkins enterprise-leadership podcast episode, Jul 2026. Tier: unverified, single episode.)*

**Worked example: when monitoring replaces gating on the wrong kind of action.** MIT CISR's minimum viable governance (MVG) framework defines the right amount of oversight as the least governance needed to manage risk effectively, but the framework's own diagnosis is that the risk space it must track moves faster than leaders can anticipate it. That is a design trying to minimize against two terms at once: one measurable, like friction or speed, and one that is not, risk itself. Name the trap directly: when a design minimizes against a measurable term and an unmeasurable term together, the minimization collapses onto the measurable term within roughly two quarters, and nobody has to do anything wrong for that to happen. That two-quarter figure is this skill's own inference from MVG's stated diagnosis, not a number MVG reports, and it has no population behind it.

The general rule this connects to: monitoring-over-gating, loosening a control and watching for problems instead of blocking upfront, is only sound where the actions being monitored are actually reversible. Where they are not, "we will watch for issues" quietly becomes "we accept the average case," because there is no way to unwind a bad outcome once it has happened. This is the reversibility axis added in the July 2026 sweep doing its own work: gating belongs in the irreversible column of the 2x2 above, monitoring belongs in the reversible one, and MVG's diagnosis shows what happens when a design runs that swap backward without naming the reversibility variable.

**When this is wrong:** a documented case where loosened, monitoring-only governance over irreversible actions still caught and reversed harm before it became permanent would break this. That would require a reversal path this skill does not currently name.

*(Source C: "Minimum Viable Governance," MIT Center for Information Systems Research, Talking Points briefing, 19 Mar 2026, with a public summary in MIT Sloan Management Review's Ideas Made to Matter. Tier: framework's own stated diagnosis; the two-quarter estimate is this skill's inference from that diagnosis, not a figure MVG itself publishes.)*

## A WORKED AUTONOMY PULLBACK, WITH NUMBERS

The clearest public case of a company deciding a step should **not** be probabilistic, after shipping it.

**What was built.** OpenAI launched Instant Checkout in September 2025: complete the entire purchase inside ChatGPT, with the agent handling the transaction step.

**What happened.**

- **Completion ran at roughly one third the rate of the retailer's own site.**
- **About 8% of US adult ChatGPT users** tried it in the first month.
- **Roughly a dozen** Shopify merchants integrated.

**What changed.** In **March 2026 it was scaled back**, not killed, and repositioned: **discovery inside the assistant, checkout in the retailer's own app.**

**Read it as a determinism finding, because that is what it is.** Discovery is a good fit for a probabilistic system: many acceptable answers, cheap errors, the user reviews the output anyway. **Checkout is not.** One correct outcome, an irreversible money movement, and a user who will not forgive a wrong one. The market drew the line in the same place this skill would.

**The transferable test.** When a workflow spans discovery and commitment, **the boundary between them is usually the determinism boundary.** Let the model roam on the exploration half. Make the commitment half deterministic, or at minimum put a confirmation gate on it.

**Watch for the version of this in your own product:** any step where the user is choosing among options is probabilistic-friendly; the step where the choice becomes binding usually is not.

*(Source: ◆ corroborated against primary reporting rather than a single article: [OpenAI's launch post](https://openai.com/index/buy-it-in-chatgpt/) and [CNBC, 24 Mar 2026](https://www.cnbc.com/2026/03/24/openai-revamps-shopping-experience-in-chatgpt-after-instant-checkout.html). **Some secondary coverage says "killed"; the record says scaled back to discovery-only**, and the accurate version makes the determinism boundary clearer. See `rtp-marketing-to-ai-agents` for the commercial reading of the same event.)*

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

Follow the **Deliverable Protocol** from the [Universal Skill Protocol](../../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 11:
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

## QUALITY GATE (8 binary checks)

- [ ] Each feature component classified: deterministic, probabilistic, or hybrid (with handoff contract)
- [ ] Temperature/variation tolerance documented for each probabilistic component
- [ ] Testing strategy assigned: snapshot (deterministic only), property tests (probabilistic), majority voting (variable), or caching (hybrid wrapper)
- [ ] Reproducibility requirements explicit: "must be pinned" vs "acceptable drift" vs "cache enough"
- [ ] Production patterns chosen: seed pinning, version pinning, output caching, majority voting, confidence thresholding — match to risk level
- [ ] pass@k vs pass^k decision made for each customer-facing component
- [ ] End-to-end pass rate calculated for multi-step pipelines
- [ ] Reversibility classified (two-way door vs one-way door) alongside predictability, and the pace decision (move fast vs pull dissent first) matches the 2x2 cell, not a default habit

## WHEN WRONG

- Early-stage exploration (prototyping for learning, not production readiness)
- Pure-generative features (where determinism has no customer value)
- After architecture is locked (this is a design-time skill)
- Low-stakes personalization (where drift is a feature)

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
