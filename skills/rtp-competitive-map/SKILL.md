---
name: competitive-map
description: "Map competitive positioning for an AI product across the dimensions that actually decide defensibility — model, safety, privacy, unit economics, switching cost, trust — not feature parity and pricing tiers. The core reframe: in AI, features and model capability commoditize in 3–6 months (yesterday's breakthrough is today's table stakes), so advantage lives in moat durability, cost structure, and trust — and two products with identical UIs can differ 3× in defensibility by substrate. Different economics = different markets — you compete where YOUR economics work. Use when evaluating competitive threats, designing a defensible position, or deciding which AI game to play. Do NOT use pre-PMF, for feature-level comparisons (use first-principles), or to justify a price war. Pairs with: moat-finder (your own defensibility), strategy-canvas (the strategy), cost-model (the unit-economics math), signal-scanner (weak-signal detection). Triggers: 'competitive analysis', 'competitive positioning', 'battlecard'."
imports:
  - moat-finder
  - first-principles
---

# Competitive Map — AI-Native Analysis

**The objective:** map where you actually stand against AI competitors — and where your position is defensible — for the PM deciding which threats are real and which game to play.

## The one idea

Two AI products have nearly identical UIs, the same core features, the same demo. One is three times more defensible than the other. The difference is invisible on the product surface, because it isn't *on* the surface — it's in the substrate: which model, trained on whose data, with what trust posture, at what unit cost.

That's the reframe this skill exists to force, and its enemy is **commodity blindness** — mapping AI competitors the way you'd map traditional software (feature parity, pricing tier, segment) and treating *model capability* as a durable advantage. It isn't: capability commoditizes in 3–6 months (⚠ practitioner rule), so yesterday's breakthrough model is today's table stakes, and the teams that lose are the ones still celebrating last year's model differentiation. In AI, **competitive advantage doesn't live in features — it lives in moat durability, cost structure, and trust capital.** A competitor with lower unit economics out-executes you regardless of feature superiority; a competitor with a data flywheel out-learns you; a competitor with enterprise trust charges 3× your price.

And the sharpest consequence: **different unit economics = different markets.** You're not competing to be "best" in the abstract — you're competing in the market where *your* economics work. A rival who can serve at $0.018/user/day plays a price-sensitive game you can't win; you at $0.05 play a mid-market game they can't afford to enter; a rival at $0.095 must play premium/regulated. Map the substrate, and the competitive picture stops being "who has more features" and becomes "who can profitably own which market" — which is the only competitive question that survives the next model release.

## How to use this skill

1. **Score the substrate** — rate each competitor AI-native vs. AI-enhanced across the maturity dimensions; that reveals durable positioning. (MATURITY SCORING.)
2. **Analyze the dimensions that decide defensibility** — model, safety/trust, privacy, unit economics, switching cost, trust capital — reverse-engineering competitor cost. (THE DIMENSIONS.)
3. **Synthesize and position** — the three 2×2s locate your defensible market; Dunford's five components + a battlecard make it sayable in a deal. (SYNTHESIS + POSITIONING + BATTLECARD.)

## KEY TERMS (plain language)

- **Commodity blindness** — treating model capability as a durable moat when it commoditizes in months; the central trap.
- **AI-native vs. AI-enhanced** — built *for* AI (high maturity, higher switching cost + moat durability) vs. AI bolted on as a feature (cheaper to build, commoditizes faster).
- **Moat durability / cost structure / trust capital** — the three places AI advantage actually lives (not features).
- **Unit-economics-as-market** — your effective cost/user determines which price games you can profitably play; different economics serve different markets.
- **Switching cost premium** — high lock-in (data history, fine-tunes, deep integration) supports a +30–50% price multiplier.
- **Trust capital** — brand + sentiment + enterprise relationships + certifications; slow to build, fast to destroy, and worth a premium in regulated markets.
- **Positioning (Dunford)** — the five answers (alternatives, unique attributes, value, who-cares, category) that make your advantage sayable.
- **Battlecard** — the one-page field artifact that turns positioning into what a rep says Tuesday morning.
- **Evidence tiers below** — cost/day figures and the 3–6-month commoditization are ⚠ illustrative; build your own from real benchmarks.

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../../../UNIVERSAL-SKILL-PROTOCOL.md). **Go deep** when evaluating threats, designing a defensible position, or choosing which AI game to play. **Skip** pre-PMF (no competitors yet) or for feature-level comparisons (use `first-principles`). Then route depth and output format.

## MATURITY SCORING — AI-native vs. AI-enhanced

Score each competitor 1–4 (absent → mature) across the substrate dimensions: model quality (off-the-shelf API → proprietary fine-tune), hallucination mitigation (none → RAG + fact-check + override), latency, cost structure, evals/monitoring, safety posture, data flywheel, trust design, regulatory readiness (SOC 2 / HIPAA / FedRAMP), model diversity, infrastructure customization (third-party API → on-prem/fine-tune), moat clarity. **AI-native** averages >3.0 (built FOR AI — wins on quality, cost, and accumulated trust); **AI-enhanced** averages <2.5 (a feature bolt-on — cheaper to build, commoditizes faster). The gap between the two is where durable positioning lives.

## THE DIMENSIONS THAT DECIDE DEFENSIBILITY

Work each competitor across these; the substrate ones matter more than the surface:

- **Arena & model.** Define the *specific* problem ("enterprise knowledge retrieval, <2s latency, 98% privacy compliance, zero hallucination tolerance"), not "AI for knowledge workers." Name each competitor's base model (public / proprietary fine-tune / hybrid), and **benchmark on YOUR use case** — 20–30 real test queries against 3–4 competitors, scored on accuracy/completeness/latency/cost; be honest about parity. Assume any capability lead expires at the next foundation-model upgrade (6–12 months).
- **Safety & trust posture** (refusal policy, hallucination tolerance, transparency, incident-response track record). High safety supports premium pricing; low safety undercuts but risks regulatory pressure. Does trust matter in *your* market? (Healthcare: yes. Entertainment: maybe.)
- **Data & privacy** (retention, "will they train on your data?", SOC 2 / HIPAA / GDPR, transparency). Privacy is enterprise trust capital: a competitor with SOC 2 Type II can sell to regulated customers, one without cannot — so estimate what % of your TAM requires high privacy (that slice is closed to low-privacy rivals).
- **Unit economics — the moat that matters.** Reverse-engineer each competitor's cost (token price × usage; or pricing tier ÷ assumed users; freemium margin math) and compare on model, context size, cache-hit rate, retry rate → **effective cost/user/day.** Then compute who can play which game: at $0.05 you can charge $0.15–0.30 (mid-market); a rival at $0.018 can charge $0.06–0.12 (price-sensitive); a rival at $0.095 needs $0.28+ (premium/regulated). *(The deep math is `cost-model` / `token-economics`.)*
- **Switching cost & lock-in** (API integration depth, data history, workflow coupling, whose value is in fine-tunes vs. the base model). High lock-in supports a +30–50% price premium; low lock-in means you compete on capability and price.
- **Trust capital & brand** (recognition, sentiment/NPS, 5-year enterprise relationships, published certs). Built slowly, destroyed quickly — one incident can erase three years in three months; estimate each rival's trust-collapse trigger.

## SYNTHESIS — three 2×2s locate your defensible market

- **Capability × Cost** — which market do you own? (high-capability/low-cost vs. high-capability/high-cost vs. DIY.)
- **Trust × Price** — regulatory defensibility (high-trust/high-price = enterprise/regulated; low-trust/high-price = premium UX only).
- **Moat type × Runway** — whose advantage expires first? (weak-moat/short-runway competitors are the ones a model release erases.)

Your competitive position is the *intersection* of the three — that's your defensible market, not a single "we're the best" claim.

## POSITIONING — Dunford's five components (how to talk about it)

The matrices tell you where you stand; positioning tells you how to say it. Answer five, each testable:

1. **Competitive alternatives** — what would the customer use if you didn't exist? *Not just other AI products* — rule-based automation, human BPO, other LLM agents, in-house build, and the strongest one: **status quo/do-nothing** (inertia is a competitor). Each needs different positioning; comparing yourself only to AI startups when the buyer is comparing you to a $40/hr contractor is malpractice.
2. **Unique attributes** — what do you have no alternative has? *Attributes, not features* ("the only product that retrieves your contracts AND CRM AND email in one query"). Test each: can a rival add it in 6 months (then it's a temporary lead, not unique)? is it visible at decision time? does it map to a value the customer cares about? *Cross-check against your own unit-economics and trust-capital scores — if a rival is within 0.5 of you on a dimension, it's not your unique attribute.*
3. **Value** — the *outcome* the attributes deliver ("finds liability clauses across all three systems in 90 seconds — work that took associates 4 hours"), with a specific outcome, time delta, and user. "We have RAG" is not value.
4. **Who cares** — the segment where the value is most acute (pain intensity × decision authority × buying readiness × reference-ability), *not the largest segment*. The best-fit is rarely the biggest TAM; it's where your unique attribute solves the sharpest pain and the deal moves in weeks.
5. **Market category** — the box the customer mentally puts you in, which sets the comparison. "AI assistant" compares you to ChatGPT (you lose); "contract intelligence platform" compares you to Kira/Evisort (you can win). The category is a lever — narrow it until your unique attributes are category-defining. If you don't pick the frame, your competitor picks it for you.

**Assemble:** *"For [who cares] who struggle with [the pain your unique attributes solve], [product] is the [category] that [value]. Unlike [alternatives], we [unique attributes]."* If it passes the dimensional cross-checks, it's defensible; if not, usually "unique attributes" is claiming uniqueness the unit-economics or trust scores already disproved.

## BATTLECARD — positioning made operational (one page, sales-ready, quarterly)

Six sections, in order: **(1) Positioning snapshot** (the statement, 3 sentences — the lede, the answer to "why you over them?"). **(2) Strengths vs. this competitor** — 3 bullets, each a customer-language claim with evidence (eval scores, customer quotes, deployment counts); no evidence, no bullet. **(3) Weaknesses** — 3 honest bullets, *each with a reframe* (acknowledge + pivot: "their UI is mature; ours moves faster — our last 6 sprints shipped what they're still planning") — a weakness without a reframe leaves the rep stuck. **(4) Objection handling** — the 5 objections the rival's reps plant, each with a specific answer ("been doing this longer" → "longer means optimized for an older problem; our architecture was built for 2026 workloads"). **(5) Proof points** — 3–5 concrete artifacts, each defensible if the buyer says "send me the source" (customer outcome, eval comparison, analyst reference, cost comparison). **(6) Talk track** — 2–3 verbatim sentences the rep delivers head-to-head; if reps won't say it because it sounds fake, it's wrong — rewrite until they will. **Hygiene:** one card per direct competitor, owned by product marketing, refreshed quarterly (monthly during a surge), versioned/dated, adoption-tracked (unused sections are wrong — fix or cut).

## WHERE THIS SKILL MEETS THE REST OF YOUR STACK

- **`rtp-moat-finder`** *(import)* — this maps the *competitive landscape*; moat-finder assesses *your own* defensibility (the four moat types). Use moat-finder's concepts as the substrate dimensions here.
- **`rtp-cost-model` / `rtp-token-economics`** — the deep unit-economics reversal behind the "different economics = different markets" call.
- **`rtp-strategy-canvas`** — competitive-map is an input to strategy; the canvas turns the defensible market into the plan and the conditional bets.
- **`rtp-signal-scanner`** — detects the weak signals (a competitor's new model, a pricing move) that expire this map; budget quarterly refreshes.
- **`rtp-gossip-mode`** *(informal upstream)* — signal-scanner is the *systematic* refresh; gossip-mode is the *informal* one. "Heard at a meetup that [competitor] is doing X" or "a customer said they're also evaluating [rival]" is competitive intel (gossip's signal 7) that catches a move *between* quarterly refreshes — with a confidence tag, low for a rumor, higher for a direct customer signal. Gossip catches it sideways and routes it here; this map is where it lands as an updated dimension.
- **`rtp-first-principles`** *(import)* — for feature-level "is this actually different?" cuts beneath the positioning claims.
- **`rtp-trust-under-fog`** — when the "trust matters here" dimension is load-bearing and you're communicating a probabilistic advantage to a certainty-seeking buyer.

## REALITY CHECK

- **Benchmarks are only as good as your test queries** — 20–30 per use case minimum, common AND edge cases.
- **Asymmetric information** — you can't see competitor internals (fine-tuning, data retention); make inferences *visible* and labeled as assumptions.
- **This map decays in 3–6 months** — a competitor's model launch invalidates the capability row; budget quarterly refreshes.
- **Upstream consolidation** — if all rivals use the same base model, a model upgrade levels everyone equally; the differentiation must be elsewhere.
- **Economic sustainability** — a VC-backed rival with lower unit economics can outlast a bootstrapped you in a price war; don't start one.

## QUALITY GATE

- [ ] Arena defined specifically (not "AI for knowledge workers")
- [ ] 5–8 direct competitors; base models named; capability benchmarked on 20+ real cases
- [ ] Safety, privacy, and regulatory posture compared; switching cost calculated
- [ ] Unit economics reverse-engineered per competitor (assumptions explicit)
- [ ] Trust capital scored; the three 2×2s completed; your defensible segment identified
- [ ] Positioning statement assembled and cross-checked; battlecard drafted if sales-facing

## WHEN WRONG

- Very early exploration where competitive threats don't yet exist, or a genuine monopoly market.
- When competitive analysis becomes a way to avoid shipping (perfectionism).
- When the analysis fixates on feature parity rather than moat durability — this is a strategic tool, not a feature comparison.
- When used to justify a price war — competing on price is a race to the bottom in commoditized AI.

## TRADE-OFF LEDGER

By mapping the substrate instead of the surface, you bet that defensibility lives in moat/cost/trust, not features — that the durable question is "who can profitably own which market," not "who has more features." You give up the comfort of a clean feature-comparison grid for the harder work of reverse-engineering economics and trust. **Reversible?** It's analysis — cheap to redo, and it *must* be redone quarterly as capability commoditizes. **The hidden trade:** the failure mode is *commodity blindness dressed as rigor* — a beautiful feature matrix that celebrates a model lead expiring in three months. **Confidence: High** — capability commoditization is the defining dynamic of AI markets. What would change it: a genuine, durable model moat (rare) where capability really is the advantage.

## CONCLUSION

Follow the Conclusion Protocol ([Universal Skill Protocol](../../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 5): the recommendation (your defensible market — the intersection of the three 2×2s — and the position to claim), the key trade-off (which game your economics let you win), the biggest risk (a capability lead you're mistaking for a moat), and the next action (the positioning statement + battlecard, with an owner and a quarterly-refresh date).

## VISUAL SUMMARY

After the primary output, invoke the **excalidraw-svg** skill for one visual: the three synthesis 2×2s (Capability×Cost, Trust×Price, Moat×Runway) with each competitor and you plotted, and the intersection — your defensible market — highlighted; plus a small "substrate vs. surface" icon showing two identical UIs sitting on different-sized moats. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.
