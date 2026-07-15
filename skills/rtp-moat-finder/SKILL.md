---
name: rtp-moat-finder
description: "Will your AI advantage survive copycats and the next model? Separates real moats from features. Runs a P&L pre-screen (cost line, floored at zero, vs growth line, multiplied), scores the five compounding moats — proprietary data, workflow depth, harness mastery, brand and trust, network effects — on a quarterly scorecard (three or more to survive the 18-month wall), then adds the three dynamics that make a loop compound (Vertical-Infinite, Living Software + Workspace DNA, cycle-time), the network-effects filter, the acquisition test, and the fake-moat checks (data that's just storage, loops on public data, the agent-in-the-middle squeeze). Core call: the model is the recipe; the moat is the system around it — only a loop fed by inputs no one else has survives. Use when setting strategy, judging whether an edge is defensible or just parity, or ~18 months out when models catch up. Pairs with: build-or-buy, safety-as-moat, feedback-flywheel. Triggers: 'competitive advantage', 'defensibility', 'moat', 'wrapper'."
imports: [bias-spotter, determinism-compass]
---

# Moat Finder

## THE ONE IDEA

The model is never the moat. Everyone rents the same frontier models, and every model gets better for everyone at once. So an advantage that lives in the model — a clever prompt, a fine-tune, an architecture trick — has a countdown timer on it. **The model is the recipe; the moat is the system around the recipe.** The durable advantage is a *compounding loop*: a system that gets better the more it is used, fed by inputs only you have, wrapped in a workflow that is painful to leave. Everything else is a feature. This skill sorts the loop from the features before you spend eighteen months defending the wrong thing.

## THE TRAP

You will confuse *impressive* with *defensible*. The bias is recency: a novel capability feels like a moat precisely because it is new. Three months later every competitor ships the same thing and you are racing on execution cost, which is not a strategy. In AI, moats are invisible until they hold or break — a proprietary dataset, a deep integration, a safety brand can all look defensible on launch day and be commodities by month eighteen. The test that cuts through the theater: **"Why can't a competitor with the same model beat us next quarter?"** If the honest answer names a feature, you have no moat yet. The teams that win know their moat *before* they build — roughly 5-17% of AI products survive 18 months in market, and the survivors almost all carry three or more compounding moats (⚠ directional).

## KEY TERMS (plain language)

- **Compounding moat** — a defense that gets *stronger* through normal usage: data accumulates, integrations deepen, the harness matures, trust compounds, network effects amplify. Each unit of use produces evidence a competitor cannot replicate.
- **Harness** — the orchestration + memory + skills + context + evals layer that turns raw model capability into reliable outcomes. Ravi's most under-appreciated moat.
- **Vertical-Infinite** — go deep in one vertical first, expand horizontally only after the vertical moat is durable; vertical agents beat horizontal on PMF and unit economics.
- **Living Software / Workspace DNA** — software that improves through its own use (Micro/Meso/Macro feedback), accumulating organization-specific learning that makes switching feel like "the new AI doesn't get us."
- **Indispensability Index** — the measure of workflow lock-in: how many quarters of disruption switching would cost the customer.
- **Anti-moat loop** — the same self-improving loop, but fed by public data anyone can get, so it drags everyone toward the industry average instead of ahead.
- **Long tail** — the rare, hard cases that each occur infrequently but together are common and expensive to get wrong; where a real data moat lives.
- **Model-agnostic vs model-dependent** — an advantage that survives model upgrades (loop, evals, workflow, data) versus one that fades when the base model catches up (a fine-tune, an architecture edge).
- **P&L value-line** — which line an AI feature moves: the cost line (floored at zero) or the growth line (multiplied into the valuation).

## WHAT THIS SKILL CONSUMES & PRODUCES

Defensibility is a judgment *about* the product, so this skill sits downstream of the parts that describe the product and upstream of the parts that bet on it.

**Consumes (inputs):**
- **The core value engine + candidate moats** — the irreplaceable capability, from `strategy-canvas` (the Superpowers step).
- **The data profile** — does your data cover the rare, hard cases, and how liquid/vintaged is it (from your own instrumentation).
- **Which P&L line + the margin** — cost vs growth, from `cost-model` / `token-economics` (feeds the Step 0 pre-screen).
- **The competitive position** — what rivals can and can't cheaply copy, from `competitive-map`.
- **The loop mechanics** — whether the feedback loop actually closes, from `feedback-flywheel`.

**Produces (outputs):**
- **The five-moat scorecard + the one defensible position** → `strategy-canvas` (Superpowers / Defensibility) and `ai-portfolio-management` (which bets are worth funding).
- **The trust dimension** → `safety-as-moat` (moat 4 made operational).
- **The next-quarter move** — the weakest moat that matters → the roadmap.
- **The defensibility narrative** → `vision-setting` / the board.

## STEP 0 — PRE-SCREEN: IS THIS EVEN WORTH DEFENDING?

Before the defensibility analysis, one screen: **which line of the P&L does this AI move, and what is that line's ceiling?** The lines are not equal.

- **Cost line — floored at zero.** Even the generous case (half the cost base is AI-addressable, cut it 10% = a ~5% expense cut) moves firm value only ~10%. Real, but bounded — you cannot cut a cost below zero.
- **Growth line — no ceiling, and multiplied.** Investors price the valuation *multiple* on expected growth, so a lever that touches the growth rate touches the multiple. In one valuation model (wealth-management firms), a firm growing at 5% is worth ~50% more than an identical firm at 3% (◆; mechanism generalizes, exact figure is industry-specific).
- **The bias to catch — the growth blindspot.** Executives believe AI can more than double firm value (a senior financial-services roundtable put an AI-enabled wealth firm at a ~135% premium in three years) yet almost all spend it on efficiency.

**Why it matters:** a strong moat around a *cost-line* feature still cannot move firm value much; the same effort aimed at the *growth line, behind a moat*, compounds. **When wrong:** in a thin-margin, survival-mode business the cost line is the right target — and a growth lift with *no* moat is rented, not owned. *(Source: Benartzi, Long & Puntoni, "Companies Are Using AI for Efficiency. They Should Use It to Grow.", HBR, 1 Jun 2026; the 2.35× roundtable figure is senior-exec judgment ◆/⚠.)*

## THE FIVE COMPOUNDING MOATS

The frontier model is a commodity. What is not commoditized is what the team builds *around* it. Score each moat 1 (none) to 5 (deep), with evidence.

| Moat | Mechanism | The real-vs-vanity test | Decay clock |
|---|---|---|---|
| **1. Proprietary data** | Data a competitor cannot legally or operationally replicate (customer interactions, domain labels, exclusive licensing) | Does it cover the *rare, hard cases* seen across many customers — or only the common, scrape-able body? | 12-24 mo; collapses to the mean if the loop is fed by public data |
| **2. Workflow integration depth** | Deep ties to the customer's systems; the Indispensability Index | Would migration cost multiple quarters of disruption, not an afternoon of copy-paste? | 18-36 mo; collapses in ~6 mo if a standard emerges |
| **3. Harness mastery** | The orchestration + memory + skills + context + evals layer that turns model capability into reliable outcomes | Would a rival need 6+ months to rebuild it — and can you *measure* it beats a simpler baseline? | 24+ mo; accelerates if you publish the architecture |
| **4. Brand & trust** | Privacy architecture, compliance posture, regulated-industry track record | Do buyers with equivalent alternatives still pay a premium (provable in win rates)? | 5-10 yrs if consistent; **binary** — one major incident erases it |
| **5. Network effects** | Multi-tenant patterns where each new customer makes the product better for the others | Does each new user make the product better for *existing* users within weeks (not just add to storage)? | Hardest to build, most durable once built |

Examples that anchor each: proprietary data — Duolingo's labeled interaction loop, Harvey's legal corpus (◆). Workflow — the enterprise deployment wired into 5 critical systems. Harness — the team that invested in a mature harness in 2024-25 now out-optimizing teams that didn't. Brand & trust — Apple's Private Cloud Compute, Anthropic's safety posture, SOC 2 / HIPAA / FedRAMP with measurable enterprise-sales effects (◆). Network effects — ServiceNow's 85B annual workflows of training signal no competitor has (◆).

**Harness mastery absorbs three things people list separately.** Your *eval-dataset* moat (thousands of curated production failures a rival with the same model does not have) and your *context-engineering* moat (retrieval and prompt architecture invisible in the API output) are not separate moats — they are faces of harness mastery. Score them together. The tell that it is real and not vanity: you can *measure* it beats a simpler baseline. If you cannot measure the lift, you cannot defend it either.

**Apple Intelligence stacks four of the five** — workflow (deep iOS), harness (PCC), brand & trust (privacy architecture), network effects (every iOS user produces signal) — skipping only proprietary external data, because the ecosystem is closed. Four of five is dominant.

## THE SCORECARD — A QUARTERLY ARTIFACT

Total the five scores (max 25). This is a heuristic, not an audited threshold — calibrate to your market.

- **≥ 12 — defensible** competitive position.
- **8-11 — thin.** One moat is probably carrying the rest; a competitor who matches it exposes you.
- **< 8 — exposure.** You are shipping commodity AI on a commodity model.
- **Fewer than three moats scoring ≥ 3 — fragile**, regardless of total. A team with one deep moat is exposed the moment a rival replicates that one thing; a team with three forces the rival to replicate three, each taking years.

The move each quarter: **find the weakest moat that matters and make it next quarter's investment.** A team scoring 5 on workflow but 1 on harness invests in harness, not in deepening workflow further. Run the scorecard in the same review as the harness metrics and the value model.

## WHAT MAKES A LOOP COMPOUND — THE THREE DYNAMICS

The five moats are the *what*. These are the *how* — the architectural choices that decide whether the moats compound or stall.

**Vertical-Infinite (the roadmap).** Go deep in one vertical first; expand horizontally only after the vertical moat is durable. A horizontal product competes against every AI product, including frontier labs that can ship horizontal capabilities. A vertical product competes against a small set of specialists with high switching costs. By going deep first, expansion becomes *additive*, not *substitutive*. The team that ships horizontal in 8 weeks loses to the team that ships vertical in 16 weeks, because by the 18-month wall the vertical product has 40 weeks of compounding head start (Harvey, Abridge, Gong — all vertical-deep, none displaced; the "40%+ better on PMF/unit economics" figure is ⚠ directional, a16z thesis).

**Living Software + Workspace DNA (the architecture).** Treat every user interaction as first-class training signal, not a log to archive, across three layers: **Micro** (per-trace: did the user accept, override, escalate?), **Meso** (per-workflow: which types fail consistently?), **Macro** (per-organization: the terminology, shortcuts, and edge cases the AI learns over 18+ months — *Workspace DNA*). The Macro layer is the customer-side moat: a competitor switching the customer starts from zero, and the customer feels it as "the new AI doesn't get us." Fresh data is non-negotiable — stale-data systems show ~35% more hallucinations (⚠ directional, Stanford HAI). Dogfooding is the simplest form of this architecture.

**Cycle-time is the moat (the rate).** The deepest harness moat is a system that improves *itself* at machine cycle, not human cycle: identify weakness → hypothesize → shadow-test → validate on evals and cost-per-outcome → ship → repeat (Karpathy's Autoresearch loop). Shopify's rendering pipeline improved 53% over 93 autonomous commits — ~5 years of work at human cycle (◆). The human role shifts from executing each iteration to *designing the loop's architecture* (what counts as success, what may ship autonomously, what needs review). A competitor improving quarterly cannot catch a competitor improving daily, and the gap widens each cycle. *(This is the moat side of the loop; the build mechanics live in `feedback-flywheel`, the governance in `production-observability` + `gen-ai-experimentation`.)*

## THE MODEL IS NOT THE MOAT — MODEL-AGNOSTIC VS MODEL-DEPENDENT

Sort every claimed advantage into one bucket:

- **Model-dependent (fragile).** Fine-tunes, training data whose only use is a fine-tune, architecture edges. Value = the delta over the base model. When the base model catches up — 6 to 12 months — the delta shrinks and you race to re-fine-tune on the next model.
- **Model-agnostic (resilient).** The data loop, the eval suite, the workflow integration, the harness. These work with any model you swap in, and several get *more* valuable as models improve (your evals now test harder cases; your loop compounds on a better base).

**The implication:** prefer model-agnostic moats. When a model 30% better lands in six months, you want defensibility that does not depend on the old model being special. Build the loop, the evals, the workflow, the harness. Treat fine-tuning as a temporary edge, never the strategy.

## THE ONE DIAGNOSTIC YOU CANNOT SKIP — REAL VS VANITY NETWORK EFFECTS

Most AI decks claim "data network effects." Most do not have them. Network effects require that **users get value from other users' presence** — not that the company accumulates data. Run the four-question filter:

| Question | Real network effects | Data accumulation only |
|---|---|---|
| Does each new user make the product better for *existing* users, within weeks? | Yes | No — data sits in storage |
| Would users refuse a better-featured competitor because they'd lose network value? | Yes — costly to leave | Easy — no network value |
| Can a rival with the same model and 1/10th the data match your output quality? | No — your data shape is uncopyable | Yes — synthetic data closes the gap |
| Do users pay a premium *because of* the network? | Yes | No — they pay for features |

Fail two or more and you have data, which is useful, not a moat. Single-tenant products where each customer's data improves only their own instance are **switching costs (workflow lock-in), not network effects** — different moat, different multiple. Put the right word in the deck.

## WHEN A "MOAT" IS FAKE

Run these whenever you have just identified a data, feedback-loop, or relationship moat.

**Not all data is a moat — score the tail, the liquidity, the vintage, not the volume.** General models master the *common* cases fast; the uncopyable part is the rare, expensive-to-get-wrong cases. In one field-service dataset (Bluon, HVAC), ~a third of real issues were oddballs fitting no common topic, and 27 of 59 topics held fewer than 300 examples each — that thin slice is the advantage (◆; [VERIFY] the call-count base; author holds Bluon equity). Also score data **liquidity** (ready-to-use: clean, reusable, validated — why an incumbent's agent ships faster on identical models; Caterpillar, MIT SMR, 21 May 2026, ◆) and **vintage** (how many years a rival would need to reproduce the history, even with a better model — time cannot be bought back; Lenovo, Handfield, HBR, 27 May 2026, ◆). And note: a data moat the customer can *feel* taxes its own trust premium — if the value visibly depends on harvesting the user's data, the data moat and the trust moat pull against each other (moderator ◆, [Journal of Marketing 2025](https://journals.sagepub.com/doi/10.1177/00222429251367342)).

**Fake-moat loop #1 — the anti-moat loop.** A feedback-loop moat has a condition the literature skips: the *inputs* must be yours alone. Run the loop on public signals every rival also ingests — competitor prices, web traffic, weather — and it drags you to the industry average, not ahead. The faster the loop, the faster everyone converges; the same failure appears in model training, where loops fed by model-generated or public data erase the edge cases that made the model useful. **The check:** are the inputs yours alone, or public? "Mostly public" = an anti-moat. The fix is never a new vendor; it is one signal only you can see plus one goal an off-the-shelf tool would never optimize for. *When it over-warns:* in a thin-margin commodity market, converging on the same answer can be profit-maximizing. Evidence: German gas-station margins rose ~28% only when *both* stations ran the same algorithm on the same shared signals (✅ peer-reviewed — Assad et al., *Journal of Political Economy* 2024, DOI [10.1086/726906](https://www.journals.uchicago.edu/doi/10.1086/726906)). *(Van Esch et al., HBR, 13 May 2026.)*

**Fake-moat loop #2 — the agent-in-the-middle squeeze.** Once an AI assistant sits between your brand and the buyer, a relationship you thought was safe fails on two fronts. On the **persuasion front**, the assistant answers and cites two or three sources; the human never reads your page, so your positioning never fires — being seen becomes being *quoted*. On the **choice front**, the assistant buys against the user's rules ("a mattress under $800 that ships Friday") and never feels your brand — winning the citation can still lose the sale. The only lasting defenses are structural: own the assistant, own the data it needs to decide, or be so clearly trusted it cannot route around you. *When it over-warns:* where no assistant sits in the purchase, the classic relationship moat still holds; this front is early. *(Puntoni, HBR, 23 Feb 2026.)*

## THE FORCE THE PENTAGON PREDATES — DISTRIBUTION

The five-moat pentagon is about what you build. The 2026 research adds a force it under-weights: **distribution is often a stronger moat than the AI itself, and it is the incumbent's structural weapon.** Incumbents push native assistants onto every surface so the default is "good enough" without the user ever leaving; the corollary is a warning — *if your product needs another company's data access or distribution to work, assume that access gets harder, not easier.* Agentic AI can invert this for startups in narrow windows, but the window closes. Treat distribution as a sixth question the pentagon does not score: *can you reach users somewhere a competitor cannot cheaply follow?* *(Newer and less settled than the five — [AI Moats in 2026, Valtorian](https://www.valtorian.com/blog/ai-moats-2026); [How Agentic AI Supercharges Startups and Threatens Incumbents, HBR, Jul 2026](https://hbr.org/2026/07/how-agentic-ai-supercharges-startups-and-threatens-incumbents).)*

## THE ACQUISITION = MOAT TEST

A 15-year study of ~17,000 public-company deals found that innovation a firm *bought* shows no reliable link to future growth, while capability a firm *built* compounds — "buying technology does not create innovation" (◆; Srivastava et al., HBR, 9 Jun 2026). Read against AI: the model is the buyable thing; what does *not* transfer in an acquisition is the system that makes the model productive — the harness, the evals, the context pipeline, the data loop. **So the acquisition test doubles as a moat test: if a competitor could buy the same thing in a deal, it isn't your moat.**

## THE 7 POWERS BRIDGE (for board and investor audiences)

The five moats tell the practitioner story. Helmer's 7 Powers tells the same story in the vocabulary a board already speaks. Use this table when the audience is a strategy committee — map one framework to the other rather than teaching two.

| 7 Powers (Helmer) | AI moat it maps to | One-line real-vs-vanity test |
|---|---|---|
| Scale Economies | Distribution / cost | Does *your* unit cost fall as you scale — or just your vendor's? |
| Network Effects | Network effects / data loop | Passes the four-question filter — or is it just accumulation? |
| Switching Costs | Workflow integration depth | Multi-quarter migration — or an afternoon of copy-paste? |
| Counter-Positioning | (cuts across) | Would the incumbent's response cannibalize their own margin pool — or are they just slow? |
| Branding | Brand & trust | Premium provable in win rates — or do they just know your name? |
| Cornered Resource | Proprietary data | Exclusive by contract, equity, or unique history — or buyable with capital? |
| Process Power | Harness mastery (evals) | Would a rival with the same hires and budget still ship worse for 3+ years? |

Score each Power Strong / Emerging / Absent and map it to its AI moat. A Power that scores Strong while its underlying AI moat is weak is a fragile claim — the appearance of defensibility without the mechanism. Reframe it before it reaches the deck.

## WHERE YOU ARE — OUTPUT

```
## Moat Assessment: [Product]

Value-line: [cost / growth] — ceiling: [bounded ~10% / multiplied into the valuation]
Core value engine: [the irreplaceable capability, not the feature]
Why a same-model competitor can't win next quarter: [specific, or "no moat yet"]

Five-moat scorecard (1-5 each; ≥12 defensible, <8 exposure, 3+ moats to survive):
| Moat | Score | Evidence | Decay clock |
| 1. Proprietary data      | | [rare-hard-cases Y/N; liquidity; vintage] | |
| 2. Workflow depth        | | [migration cost in quarters]              | |
| 3. Harness mastery       | | [rebuild months; measured lift Y/N]       | |
| 4. Brand & trust         | | [win-rate premium; incident count]        | |
| 5. Network effects       | | [does each user improve it for others?]   | |
Total: __/25   Moats scoring ≥3: __

Dynamics: [Vertical-Infinite Y/N | Living Software layers built: Micro/Meso/Macro | cycle-time: machine/human]
Model dependency: [high = fine-tune/training data | low = loop/evals/workflow/harness]
Distribution (unscored 6th force): [owned / default surface / partner-dependent — access getting harder?]
Fake-moat checks: [network-effects filter pass/fail | anti-moat loop | agent-in-the-middle | acquisition test]
18-month projection: [will a rival match? best / realistic / worst | probability]
Next-quarter move: [the weakest moat that matters — the one investment that deepens it]
```

Draw the "you are here" as a filled/empty bar across the five moats — it shows at a glance whether you have a *stack* or a single fragile line. Flag any moat still under debate as `OPEN: [the decision] — [what evidence would settle it]`.

## WHEN WRONG

- **Pre-market-fit.** Feature velocity beats defensibility until you have a product people want. A moat around nothing is a wall around an empty field.
- **Internal or single-customer tools.** Defensibility is irrelevant; do not run the analysis.
- **As an excuse.** "Our moat is harness mastery so execution doesn't matter" and "the moat means we can skip features customers want" are both moat-talk used to dodge the actual work. The moat justifies the strategy; it never excuses the product.

---

## GROUNDING, TRADE-OFFS & CONCLUSION

Before starting, follow the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md) Section 1 grounding questions (who is the customer, what problem, what are we saying YES and NO to) and route depth (executive vs comprehensive). Close with the Trade-Off Ledger (Section 3) and the Conclusion Protocol (Section 5): state the recommendation, name the key trade-off, acknowledge the biggest risk, define the next action.

## VISUAL SUMMARY

After the primary output, invoke the **excalidraw-svg** skill for a single visual summary — the five-moat pentagon with the product's score on each vertex overlaid against a near-empty "commodity AI" pentagon, or the compounding-loop diagram (usage → proprietary signal → better product → more usage). Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.
