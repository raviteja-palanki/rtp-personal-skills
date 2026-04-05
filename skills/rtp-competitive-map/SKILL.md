---
name: rtp-competitive-map
description: "Maps competitive positioning: base model, safety, privacy, economics, switching cost, trust, moat, regulatory. Use when: evaluating threats, defensibility, positioning (premium vs budget). Triggers: 'competitive analysis', 'competitive positioning'"
imports:
  - moat-finder
  - first-principles
---

# Competitive Map: AI-Native Analysis Framework

## DEPTH DECISION

**Go deep if:** Evaluating competitive threats to your AI product, designing a defensible market position, or deciding which AI game to play (premium vs. budget, model-heavy vs. data-heavy, regulated vs. consumer).

**Skim to Phase 8 if:** Quick threat assessment or you've already mapped competitive landscape and just need to update one dimension.

**Skip if:** Pre-PMF, no competitors yet, or making feature-level comparisons (use first-principles instead).

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md):
1. Ask the Grounding Questions (Section 1) — at minimum: Who is the customer? What problem? What are we saying YES to and NO to?
2. Route depth: Executive Summary or Comprehensive Analysis?
3. Identify output format: Document, presentation, spreadsheet, or inline?

Then proceed with the skill-specific analysis below.

---

## AI Maturity Scoring (12 Dimensions)

After completing the primary output, invoke the **excalidraw-svg** skill to create a single Excalidraw SVG visual summary. This diagram captures the essence of the analysis in one glanceable image — making the deliverable 10x more impactful. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.

## AI Maturity Scoring (12 Dimensions)

Before Phase 1, score each competitor on the AI maturity grid. This reveals **AI-native** vs **AI-enhanced** positioning:

| Dimension | Mature (4) | Developing (3) | Initial (2) | Absent (1) |
|-----------|-----------|----------------|-----------|-----------|
| **Model quality** | Fine-tuned, proprietary | Public model + prompt optimization | Generic public model | Off-the-shelf API only |
| **Hallucination mitigation** | RAG + fact-checking + user override | RAG or fact-checking | API disclaimers only | No mitigation |
| **Latency optimization** | <500ms P95, caching | <2s P95 | <5s P95 | >5s P95 |
| **Cost structure** | Sub-$0.05/user/day | $0.05-0.15/user/day | $0.15-0.50/user/day | >$0.50/user/day |
| **Evals & monitoring** | Continuous eval suite, drift detection | Weekly eval, incident response | Manual QA | None visible |
| **Safety posture** | Constitutional AI + guardrails + transparency | Refusal policy + disclaimers | Disclaimers only | None visible |
| **Data flywheel** | User corrections → retraining cycle | Manual label collection | No feedback loop | None |
| **Trust design** | Confidence displays, reasoning traces | Limitations documented | Generic "beta" label | No disclosure |
| **Regulatory readiness** | FedRAMP, HIPAA, SOC 2 published | One cert in progress | Planning phase | Not applicable |
| **Model diversity** | Multiple models per task | One model family | Single model | API-dependent |
| **Infrastructure customization** | Deployable on-prem, fine-tune APIs | Cloud API only, limited config | Cloud API, no config | Third-party API only |
| **Moat clarity** | Clear (data moat, proprietary model, brand) | Developing (growing data) | Unclear | None |

**AI-native** = scores >3.0 on avg (product is built FOR AI). **AI-enhanced** = scores <2.5 on avg (AI is a feature bolt-on).

AI-native competitors have higher switching cost and moat durability. They win on quality, cost, and trust accumulation. AI-enhanced competitors are cheaper to build but commoditize faster.

## THE TRAP

You will map competitors the way you'd map traditional software products: feature parity, pricing tier, customer segment. This misses the entire competitive layer in AI. The trap is **commodity blindness** — treating model capability as if it were a durable advantage when it commoditizes in 3-6 months. Yesterday's breakthrough model is today's table stakes. The teams that lose are the ones still celebrating last year's model differentiation.

The dangerous variant: comparing only the product surface (UI, features, pricing) while ignoring the substrate (which model, what safety posture, what data privacy stance). Two products with identical UI can have wildly different defensibility depending on whether one is built on proprietary data and the other on open-source models.

In AI, competitive advantage doesn't live in features. It lives in moat durability, cost structure, and trust capital. A competitor with lower unit economics can out-execute you regardless of feature superiority. A competitor with a data flywheel can outlearn you. A competitor with enterprise trust can charge 3x your price.

## THE PROCESS

### Phase 1: Define the Competitive Arena

1. **Identify the specific problem your product solves.** Not "AI assistant for knowledge workers" (too broad). "Enterprise knowledge retrieval with <2 second latency, 98% privacy compliance, 0 hallucination tolerance."

2. **List direct competitors.** These solve the same problem with similar economics:
   - Build a matrix with columns: Company, Product Name, Model Used, Go-to-Market, Estimated Users
   - Include 5-8 direct competitors (more is noise)
   - Row per competitor

3. **List adjacent threats.** These solve a superset or subset of your problem:
   - Broader: Generic AI assistants that could extend into your domain
   - Narrower: Specialists who could undercut on cost or trust
   - Internal: Build-it-yourself options (open-source models, in-house teams)

### Phase 2: Analyze Model Capability Layer (Import first-principles)

4. **For each competitor, identify the base model:**
   - Public: Which foundation model (GPT-4, Claude 3.5, Llama 3.1, etc.)?
   - Proprietary: Is it their own fine-tune, or a published model?
   - Hybrid: Do they use multiple models for different tasks?
   - Unknown: If unknown, what inferences can you make from product behavior?

5. **Benchmark capability on your specific use case:**
   - Design 20-30 test queries that represent real user problems
   - Run the same queries against 3-4 competitor products (and your product)
   - Score on: Accuracy (is the answer right?), Completeness (did it address the full question?), Latency (how fast?), Cost (per-token or per-request price)
   - Be honest about tie results — if capability is feature parity, say so

6. **Assess capability trajectory:**
   - Are competitors spending on fine-tuning and model training? (Product quality improving)
   - Are they stuck on public models from 6+ months ago? (Lower investment)
   - Do they have published research or clear R&D signals? (Moat-building trajectory)
   - Assume: foundational model upgrades come every 6-12 months. Your capability advantage expires.

### Phase 3: Analyze Safety & Trust Posture (Import moat-finder)

7. **Map safety positioning on three axes:**

   | Axis | Questions | Low Safety | Medium Safety | High Safety |
   |------|-----------|-----------|---------------|-------------|
   | **Refusal Policy** | Will it answer contentious questions? What refuses? | "No limits" or unclear | Refuses on some categories (hate, violence) | Explicit refusal policy, tested against adversarial inputs, published guidelines |
   | **Hallucination Tolerance** | What happens when it doesn't know? | Confidently guesses | Sometimes says "I don't know" | Consistent refusal with "I cannot verify" or retrieval-required architecture |
   | **Transparency** | What does it disclose about limitations? | Marketing only | Some disclaimers buried | Clear user-facing limitation docs, model card, capability boundaries |
   | **Incident Response** | What's their track record when they ship failures? | Radio silence or denial | Public acknowledgment, fix delayed | Rapid patch + transparent post-mortem |

8. **Estimate trust durability:**
   - A competitor with high safety posture can charge premium pricing
   - A competitor with low safety can undercut on price but may face regulatory pressure
   - Zero-trust competitors (you don't trust their safety claims) have short runways in regulated industries
   - For your market: Does trust matter? (Healthcare: yes. Entertainment: maybe.)

### Phase 4: Analyze Data & Privacy Layer

9. **Map data handling across three dimensions:**

   | Dimension | Questions | Your Stance | Competitor A | Competitor B |
   |-----------|-----------|-----------|--------------|--------------|
   | **Data Retention** | How long do they keep user inputs? | _____ days | _____ days | _____ days |
   | **Model Training** | Will they use your data to improve their model? | Yes / No | Yes / No | Yes / No |
   | **Regulatory Compliance** | Published SOC 2? HIPAA ready? GDPR certified? | _____ | _____ | _____ |
   | **Transparency** | Do they disclose privacy terms clearly? | Clear / Buried / Marketing-only | Clear / Buried / Marketing-only | Clear / Buried / Marketing-only |

10. **Calculate privacy switching cost:**
    - Enterprise customers view privacy as trust capital
    - A competitor with SOC 2 Type II can sell to regulated customers; one without cannot
    - Migrating from "data used to train" to "data never retained" is a switching trigger
    - Estimate: What percentage of your addressable market requires high privacy? That's the TAM accessible to high-privacy competitors only.

### Phase 5: Analyze Unit Economics (The Moat That Matters)

11. **Reverse-engineer competitor unit cost:**

    **Token-based pricing:** Divide token price by usage
    - Competitor A charges $0.03/1K tokens, user averages 50K tokens/month = $1.50/month cost to them
    - This is their FLOOR if they're using that model

    **Flat pricing:** Estimate by pricing tier + assumed users
    - $99/month × target 1,000 users = $99K revenue. If their real users are 2,000, they're actually $49.50/user/month

    **Freemium:** Free tier costs them money; paid tier funds it
    - If they have 90% free users and 10% paid, paid users subsidize the platform. Margin math is hidden.

12. **Compare against your unit cost.**

    | Factor | Your Cost | Competitor A | Competitor B | Implication |
    |--------|----------|--------------|--------------|-------------|
    | Model used | Claude 3.5 | GPT-4o | Llama 3.1 | Claude 3.5 is ~15% cheaper; GPT-4o is 30% more |
    | Context size | 8K avg | 32K avg | 2K avg | Competitor A burns 4x your tokens; Competitor B is lean |
    | Caching hit rate | 30% | 15% | 60% | Competitor B wins on repeated queries |
    | Retry rate | 8% | 5% | 12% | You and Competitor A are solid; Competitor B has infra issues |
    | **Effective cost** | **$0.050/user/day** | **$0.095/user/day** | **$0.018/user/day** |

    If Competitor B can undercut you by 60%, they will. Does your margin survive that?

13. **Calculate who can play which game:**
    - You at $0.05 cost: Can charge $0.15-0.30/user/day profitably (SMB, mid-market)
    - Competitor B at $0.018: Can charge $0.06-0.12/user/day profitably (price-sensitive SMB, developer tools)
    - Competitor A at $0.095: Needs $0.28+ pricing (must play premium, high-trust market)

    **Different unit economics = different markets.** You're not competing to be "best" — you're competing in the market where YOUR economics work.

### Phase 6: Analyze Switching Cost & Lock-In

14. **Map switching cost across dimensions:**

    | Lock-In Type | Example | Competitor A | Competitor B | Your Product |
    |--------------|---------|--------------|--------------|--------------|
    | **API Standardization** | Switching APIs is expensive if deeply integrated | High / Medium / Low | High / Medium / Low | High / Medium / Low |
    | **Data Lock-in** | How much customer data lives in their system? | Years of history | Months of history | Real-time, portable |
    | **Workflow Integration** | How tightly coupled to customer internal tools? | Deeply integrated | Loosely integrated | Standard API |
    | **Model Fine-tuning** | Is the customer's value in the base model or in their fine-tunes? | In fine-tunes (sticky) | In base model (portable) | Open for fine-tuning |

15. **Calculate switching cost premium:**
    - High switching cost allows premium pricing: +30-50% price multiplier
    - Low switching cost means you compete on capability and price
    - Example: If Competitor A has high switching cost and you don't, they can charge 1.5x your price and still win on total cost of ownership

### Phase 7: Trust Capital & Brand Moat

16. **Score trust capital on three signals:**

    | Signal | Definition | Your Score | Competitor A | Competitor B |
    |--------|-----------|-----------|--------------|--------------|
    | **Brand Recognition** | Percentage of target market that's heard of you | ___% | ___% | ___% |
    | **User Sentiment** | Aggregate user reviews and NPS proxy | ___/10 | ___/10 | ___/10 |
    | **Enterprise Relationships** | Number of customers with 5+ year relationships | ___ | ___ | ___ |
    | **Regulatory Approvals** | Published certifications (FedRAMP, HITRUST, etc.) | _____ | _____ | _____ |

17. **Assess trust decay risk:**
    - Trust is built slowly and destroyed quickly
    - One major incident (data breach, hallucination at scale, misaligned behavior) can erode years of trust
    - Estimate: What would need to happen to a competitor for their trust to collapse?
    - Example: Competitor built trust over 3 years. One incident could erase it in 3 months.

### Phase 8: Synthesize Into Action

18. **Map your competitive position on three 2x2s:**

    **CAPABILITY vs COST (which market do you own?)**
    ```
         Low Cost          High Cost
    High Capability:  Competitor B?        You?
    Low Capability:   DIY (internal)       Competitor A?
    ```

    **TRUST vs PRICE (regulatory defensibility)**
    ```
         Low Price         High Price
    High Trust:       (rare)               You (enterprise, regulated)
    Low Trust:        Competitor B         Competitor A (premium UX)
    ```

    **MOAT TYPE vs RUNWAY (whose advantage expires first?)**
    ```
              Weak Moat        Strong Moat
    Short (6mo):   Competitor B   (N/A)
    Long (24mo+):  (N/A)          You, Competitor A
    ```

    Your competitive position = intersection of these three matrices. That's your defensible market.

## REALITY CHECK

- **Data quality:** Capability benchmarks are only as good as your test queries. 20-30 queries per use case is minimum; test both common cases and edge cases.
- **Asymmetric information:** You often can't see competitor internals (fine-tuning, safety testing, data retention). Make inferences visible; label assumptions as such.
- **Competitive velocity:** This map decays in 3-6 months in AI. If a competitor launches a new model, your capability row is out of date. Budget for quarterly refreshes.
- **Upstream consolidation risk:** If your competitors all use the same base model from the same provider, a model upgrade affects everyone equally. This levels the playing field.
- **Economic sustainability:** A competitor with lower unit economics can absorb losses longer. If they're VC-backed and you're bootstrapped, they can outlast you in a price war.

## QUALITY GATE

Before using this to make strategy decisions:

- [ ] **Arena definition:** Specific problem ("enterprise knowledge retrieval with <2s latency"), not vague ("AI for knowledge workers")
- [ ] **Competitor list:** 5-8 direct competitors identified; base models named; capability benchmarked on 20+ real test cases
- [ ] **Safety posture mapped:** Refusal policy, hallucination tolerance, transparency, incident response all compared
- [ ] **Privacy & compliance:** Data retention, training use, regulatory certs (SOC 2, HIPAA) compared; switching cost calculated
- [ ] **Unit economics reversed:** Cost per user estimated for each competitor; cost structure assumptions explicit
- [ ] **Switching cost quantified:** Lock-in sources identified; price premium defendable or not
- [ ] **Trust capital scored:** Brand recognition, user sentiment, enterprise relationships, certifications all measured
- [ ] **Position synthesized:** Three 2x2 matrices completed; your market segment identified; competitive runway estimated

## WHEN WRONG

- Very early exploration where competitive threats don't yet exist
- Monopoly markets where you have no real competitors (internal tools, single-vendor solutions)
- When competitive analysis is used to avoid shipping (perfectionism bias) rather than to de-risk strategy
- When the analysis focuses on feature parity rather than moat durability — this is a strategic tool, not a feature comparison
- When used to justify price wars rather than moat-building — competing on price is a race to the bottom in commoditized AI

---

## TRADE-OFF LEDGER

Complete the Trade-Off Ledger from the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 3.

## CONCLUSION

Follow the Conclusion Protocol from the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 5:
1. State the recommendation
2. Name the key trade-off
3. Acknowledge the biggest risk
4. Define the next action

---

## VISUAL SUMMARY

After completing the primary output, invoke the **excalidraw-svg** skill to create a single Excalidraw SVG visual summary. This diagram captures the essence of the analysis in one glanceable image — making the deliverable 10x more impactful. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.
