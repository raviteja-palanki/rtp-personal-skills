---
name: rtp-ai-portfolio-management
description: "Manage AI initiatives as an interconnected investment portfolio with stage gates, dual-lens oversight, and Buy/Sell/Hold scoring. Prevents the 'too many pilots, no strategic coherence' failure mode. Triggers: 'AI portfolio', 'AI initiatives prioritisation', 'stage gate AI', 'AI investment review', 'AI project governance', 'OPEN framework'"
imports: ["strategy-canvas", "moat-finder", "build-or-buy"]
version: "1.0"
framework_source: "Harvard Business Review — Hoque, Nelson, Davenport & Scade, 'Manage Your AI Investments Like a Portfolio', January 2026"
---

# AI Portfolio Management

## DEPTH DECISION

**Go deep if:** You have 3+ active or planned AI initiatives and no systematic way to prioritise, sequence, or review them. Or you're setting up an AI Centre of Excellence, governance board, or executive review process.

**Skim to the stage gate checklist if:** You have a single AI project and need to know what gates it should pass through before scaling.

**Skip if:** You're pre-product and exploring your first AI use case — portfolio management at that stage is premature overhead.

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md).

---

## THE TRAP

Here is what AI chaos looks like from the inside: five departments running pilots simultaneously, each sponsored by a different VP, none of them talking to each other. Engineering is stretched across all five. None is resourced well enough to reach production. Leadership gets quarterly updates that all say "promising." Nobody asks "should we stop this one?"

Two years later, the company has learned a lot and shipped nothing.

The problem is not the technology. It is the management system. AI requires exactly the same discipline as any other investment portfolio — clear criteria for what gets in, explicit gates for what advances, and a regular process that forces hard choices about what to stop. The difference is that most organisations apply rigorous investment thinking to their financial portfolios and almost none to their AI portfolios.

The fix: treat AI initiatives as an interconnected investment portfolio, not a collection of independent experiments.

---

## The Dual Lens: Why Both Views Are Necessary

> **Attribution:** The dual-lens framework is from Hoque, Nelson, Davenport & Scade, "Manage Your AI Investments Like a Portfolio," Harvard Business Review, January 2026. The authors implemented this approach across Northrop Grumman, PepsiCo, and units within the U.S. Army.

Every AI portfolio must be viewed through two lenses simultaneously:

**Lens 1 — The Pipeline (Project Level)**
Each initiative progresses through defined stages with explicit go/no-go gates. This ensures rigour at the individual project level. No project advances without meeting the gate criteria.

**Lens 2 — The Dashboard (Portfolio Level)**
All initiatives are visible on a single dashboard showing: risk/return balance, time horizon mix, capability dependencies, and strategic alignment. This enables portfolio-level optimisation — ensuring the mix of projects makes sense as a whole, not just individually.

```
LENS 1 — PIPELINE (Project Level)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Opportunity → [Gate 1] → Design & Partner → [Gate 2] → Experiment → [Gate 3] → Scale & Operate
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LENS 2 — DASHBOARD (Portfolio Level)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Near-term    Medium-term    Long-term
  ████           ███            █          → Time horizon balance
High risk    Medium risk    Low risk
  ██             ████           ████       → Risk/return balance
Foundation   Transformation  Moonshot
  ██████         ███            █          → Portfolio composition
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## The Four Stages: The OPEN Framework

> The OPEN framework (Outline, Partner, Experiment, Navigate) was introduced in an earlier HBR article and maps to the four portfolio stages below. The portfolio management approach described here is framework-agnostic — it works with OPEN or other methodologies.

### Stage 1: Opportunity Portfolio (Outline)
**What happens here:** Ideas are collected, framed, and ranked. Problem framing, initial value and risk hypotheses, dependency mapping.

**Output:** A scored, ranked backlog of opportunity ideas — not a list of projects you've already committed to.

**Gate 1 — Strategic Fit and Technical Feasibility:**
- Does this address a real business need (not a technology looking for a problem)?
- Is there reason to believe the technical approach is feasible?
- Does it connect to a strategic priority?

---

### Stage 2: Design & Partnership Portfolio (Partner)
**What happens here:** Outlined projects enter detailed shaping. Teams build extensive business cases, map dependencies, identify technical skills and data requirements, and establish preliminary governance.

**The partnership question:** Even organisations with strong internal capabilities typically need external partnerships — with technology vendors, academic researchers, ethics advisors, or industry peers — to realise AI ambitions. This is also the stage to map the human-AI relationship the project will create: How does it change staffing, work patterns, reporting structures, and individual roles?

**Output:** Business case with expected benefits, required investments, success metrics, capability plan, and preliminary governance model.

**Gate 2 — Readiness to Experiment:**
- Is required data available, of sufficient quality, and properly governed?
- Are necessary skills in place or clearly sourced?
- Have ethical guidelines and security controls been defined? *(Responsible AI check — mandatory)*
- Does the business case still hold at this level of detail?

---

### Stage 3: Experimental/Prototyping Portfolio (Experiment)
**What happens here:** Structured experiments — not generic pilots. Each experiment tests not just technical feasibility, but enterprise viability (can we integrate at reasonable cost?) and human desirability (will users adopt and find value?).

Rapid, bounded trials enable multidimensional learning: paper models, minimum viable products, limited pilots. Multiple parallel experiments can explore different technical approaches.

**The key distinction:** Structure experiments as **learning journeys**, not validation exercises. The goal is to discover what's true, not to prove the business case you wrote in Stage 2.

*(See `gen-ai-experimentation` skill for how to design these experiments properly.)*

**Output:** Validated learning: does this work, for whom, under what conditions, at what cost?

**Gate 3 — Ready to Scale:**
- Rigorous system testing passed?
- Red-team scrutiny (deliberate attempts to break or misuse the system) completed?
- Integration costs and process redesign requirements confirmed?
- User adoption validated?

---

### Stage 4: Scale & Operate Portfolio (Navigate)
**What happens here:** Production deployment. Scaling for multiple users, upskilling employees, redesigning processes, integrating with existing technical environment.

**The mindset shift:** Scale & Operate is fundamentally different from Experiment. The focus shifts from discovery to reliability, cost management, and continuous monitoring.

**Key practices:**
- Establish guardrails that prevent system misuse
- Implement cost-tracking to understand total cost of ownership
- Measure actual mission impact (not assumed benefits)
- Maintain service management and knowledge capture

---

## The Three Mechanisms

### Mechanism 1: Buy/Sell/Hold Scoring

Every initiative in the portfolio is scored against objective criteria. This transforms subjective debates ("I think this is more important") into structured conversations about trade-offs.

**Scoring dimensions:**
| Dimension | What it assesses |
|-----------|-----------------|
| Strategic alignment | How well does this serve core business objectives? |
| Feasibility | What is our technical capability and organisational readiness? |
| Risk/reward | What is the potential upside vs. implementation challenges? |
| Resource requirements | What does this need across financial, human, and technical dimensions? |

**How scoring drives decisions:** When capacity opens (a project advances to production, a new team is formed), leaders select the next item from the highest-scoring backlog entries that have passed the relevant gate. No pet projects. No squeaky-wheel prioritisation.

**The Buy/Sell/Hold distinction:**
- **Buy (add to portfolio):** Score meets threshold + gate criteria met + capacity available
- **Hold (continue as-is):** Good progress, appropriate pace, no reallocation needed
- **Sell (exit or archive):** Strategic misalignment, performance shortfall, or better alternatives available

### Mechanism 2: Stage Gates

Gates are not bureaucratic hurdles. They protect the organisation from the two failure modes that kill AI programs: advancing projects that shouldn't advance, and failing to kill projects that should be stopped.

**Universal gate question (applies at every stage):**
"Is the business case still valid at this level of investment?"

**Responsible AI gate (mandatory at Gate 2 and Gate 3):**
- Has the AI use case risk assessment been completed? (See `responsible-ai-program`)
- Are ethical guidelines and security controls defined?
- Who is accountable at the project level if this AI causes harm?

### Mechanism 3: The 3E Hypothesis Gate — Explore, Exploit, or Exit?

> **Framework:** Ravi Teja Palanki's original framework for hypothesis-driven portfolio decisions (5 APR 2026). Designed to prevent the "perpetual pilot" failure mode — initiatives that never reach a clear decision.

Every AI initiative is a hypothesis. At every stage gate, the portfolio review must declare one of three decisions. There is no default "keep going."

| Decision | When it applies | What it means | Next step |
|----------|----------------|---------------|-----------|
| **Explore** | Evidence is promising but incomplete. Unknowns are significant but manageable. | More signal is needed before committing to scale. | Define the specific experiment or data point that would move this to Exploit. Set a hard time bound: "We decide by [date]." |
| **Exploit** | Evidence is clear. The use case works, for these users, at this cost, under these conditions. | Stop discovering. Start executing. | Move to Scale & Operate with full resource commitment. |
| **Exit** | Unknowns are numerous. Effort is high. Multiple signals point against viability at this time. | Do not proceed — but do not simply stop. | **Pivot check first:** What asset, model, data, or learning from this initiative could redirect toward an adjacent problem that IS viable? Exit is a redirection question, not just a stop. |

**How the 3E gate maps to portfolio stages:**

```
Stage 1 (Opportunity)       → 3E Gate: Explore or Exit
Stage 2 (Design & Partner)  → 3E Gate: Explore further, or Exit with pivot check
Stage 3 (Experiment)        → 3E Gate: Exploit (scale) or Exit
Stage 4 (Scale & Operate)   → 3E Gate: Exploit (sustain) or Exit (sunset)
```

**The pivot check on exit:** Before any initiative is archived, the portfolio team must answer one question: *"Is there an adjacent use case where the work done so far — the data pipeline, the model, the process redesign, the user understanding — has transferable value?"* If yes, that adjacent pivot becomes a new Stage 1 Opportunity entry with an accelerated gate (it inherits validated learnings).

**Why this matters:** Most AI portfolios fail not because of bad technology but because of bad decision hygiene. Teams run pilots indefinitely because nobody has the authority or the framework to call Explore, Exploit, or Exit. The 3E gate makes the decision explicit at every review cycle and ensures no work dies without first checking whether it has transferable value.

---

### Mechanism 4: Regular Portfolio Reviews

Portfolio reviews rebalance the whole portfolio, not just individual projects. They are distinct from project status updates — which only look at individual initiatives.

**Portfolio health questions (ask at every review):**
- Are we maintaining appropriate balance across time horizons? (near / medium / long-term)
- Do we have sufficient investment in foundational capabilities — the data infrastructure, governance structures, and internal skills that every other initiative depends on?
- Do early-warning signals (schedule slippage, cost overruns, performance shortfalls, declining user adoption) suggest intervention before a gate?
- Are there initiatives we should exit now to free up resources for higher-priority work?
- Has the **3E decision** been declared for every initiative that has completed a stage? No initiative should sit in limbo between gates.

**Review cadence:** Monthly lightweight dashboard review + Quarterly deep rebalancing session with 3E decisions logged for every initiative reviewed.

---

## Case Study: Lloyds Banking Group's GenAI Control Tower

> *Source: HBR, Hoque et al., January 2026*

Lloyds Banking Group's "GenAI Control Tower" demonstrates portfolio management at enterprise scale:
- A **cross-functional forum** that prioritises use cases across the organisation, allocates resources, and ensures alignment with strategic priorities
- Explicitly balances **long-term transformation with short-term value delivery**
- Recognises that **rapid technology changes can warrant abandoning ongoing projects** and switching rapidly to new use cases
- Each initiative passes through rigorous reviews — risk assessment, legal review, ethics, bias, and security — **before** advancing to production
- A **centralised playbook** for AI development alongside **clear decision rights** (build or buy) ensures structured yet adaptive advancement

**The lesson:** Portfolio management works at enterprise scale when it has real authority, cross-functional representation, and genuine willingness to kill projects.

---

## Portfolio Composition: Balancing the Mix

A healthy AI portfolio is not all moonshots and not all incremental. It requires deliberate balance across three types:

| Type | Characteristics | Horizon | Risk | What it does for you |
|------|----------------|---------|------|---------------------|
| **Confidence builders** | Near-term, clear ROI, builds internal capability | 3-6 months | Low | Generates buy-in, proves AI can work, builds skills |
| **Capability builders** | Medium-term, deeper integration, meaningful transformation | 6-18 months | Medium | Creates operational AI capability that becomes foundation |
| **Transformation bets** | Long-term, transformative potential, higher uncertainty | 18+ months | High | Potential for step-change advantage |

**The imbalance traps:**
- Too many moonshots: No short-term wins to sustain executive support; team burns out chasing breakthroughs
- Too many confidence builders: Never develops the deep capability needed for transformation; competitors with more ambition pull ahead
- No foundational investment: Later, more sophisticated initiatives fail because the prerequisite capabilities were never built

---

## Responsible AI Integration

> AI portfolio management is not complete without responsible AI being embedded as a structural requirement — not an afterthought.

**At every stage gate, the following Responsible AI checks are mandatory:**

| Gate | Responsible AI Requirement |
|------|---------------------------|
| Gate 1 (Opportunity) | Initial AI risk classification: Low / Medium / High impact |
| Gate 2 (Design & Partner) | Full AI Use Case Risk Assessment completed; ethics + security controls defined; project-level RAI owner named |
| Gate 3 (Experiment) | Red-team scrutiny includes responsible AI dimensions (bias, misuse, unintended consequences); human oversight verified |
| Scale & Operate | Ongoing monitoring includes responsible AI metrics; quarterly ethics review scheduled |

*These checkpoints are derived from the `responsible-ai-program` skill (MIT Sloan SHARP framework). The portfolio management system is the structural mechanism that ensures responsible AI checks happen at every project — not just high-profile ones.*

---

## OUTPUT FORMAT

```
## AI Portfolio Assessment: [Organisation/Team]

### Portfolio Snapshot
| Initiative | Stage | Score (/100) | Buy/Sell/Hold | 3E Decision | RAI Check | Notes |
|-----------|-------|-------------|---------------|-------------|-----------|-------|

### Portfolio Balance
Time horizon mix: [Near / Medium / Long breakdown — target: 50% / 30% / 20%]
Risk/return balance: [Low / Medium / High breakdown]
Foundational vs. transformational: [% in confidence builders / capability builders / transformation bets]

### Gate Review (Current Cycle)
| Initiative | Gate | 3E Decision | Criteria Met? | Next Step | Owner |
|-----------|------|-------------|--------------|-----------|-------|

### 3E Decisions Log
| Initiative | Decision | Rationale | Time Bound / Pivot Check |
|-----------|----------|-----------|--------------------------|

### Portfolio Rebalancing Recommendations
[What to add (Buy), advance (Hold + Exploit), or exit (Sell + pivot check) and why]

### Next Review Date: [date]
```

---

## WHEN WRONG

- **Governance becomes bureaucracy:** Stage gates that take longer than the work they govern. Calibrate gate rigor to project risk — lighter for low-risk, heavier for high-risk.
- **Scoring is gamed:** Teams learn what scores well and optimise for the criteria, not for genuine strategic value. Refresh criteria quarterly.
- **Portfolio grows without exits:** Adding projects without a disciplined exit process means the portfolio expands until nothing is properly resourced. "Selling" projects is as important as buying.
- **Pre-PMF stage:** Building a portfolio governance structure before you have any validated AI use cases is premature. Find your first successful AI application, then build the portfolio discipline around it.

---

## TRADE-OFF LEDGER

Complete the Trade-Off Ledger from the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md), Section 5.

## CONCLUSION

Follow the Conclusion Protocol from the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md), Section 6.

---

## VISUAL SUMMARY

After completing the primary output, invoke the **excalidraw-svg** skill to create a single Excalidraw SVG visual summary. The most useful visuals for this skill: the OPEN pipeline with gates, and the portfolio balance dashboard. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.

---

*Version 1.0 — 5 APR 2026*
*Framework Source: Harvard Business Review, Hoque, Nelson, Davenport & Scade, "Manage Your AI Investments Like a Portfolio", January 2026*
*Part of: AI PM Skills / ai-strategy layer*
