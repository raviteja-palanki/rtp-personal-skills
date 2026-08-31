---
name: moat-finder
version: v2.14_latest
description: 'Will your AI advantage survive copycats and the next model? Separates real moats from features. Runs a P&L pre-screen, then scores five compounding moats on a quarterly scorecard: proprietary data, workflow depth, harness mastery, trust and reliability, network effects. Three or more clear the 18-month wall. Adds the network-effects filter, the acquisition test, and fake-moat checks that catch data which is only storage and loops fed by public signals everyone else has. Closes by asking which complementary input is scarcest, because that is where the margin actually sits. The core call: the model is the recipe, the moat is the system around it. Use when setting strategy, judging whether an edge is defensible or merely parity, or about 18 months out when models catch up. Pairs with: build-or-buy, safety-as-moat, feedback-flywheel. Triggers: ''defensibility'', ''moat'', ''competitive advantage''.'
imports: [bias-spotter, determinism-compass]
---

# Moat Finder

## THE ONE IDEA

The model is never the moat. Everyone rents the same frontier models, and every model gets better for everyone at once. So an advantage that lives in the model — a clever prompt, a fine-tune, an architecture trick — has a countdown timer on it. **The model is the recipe; the moat is the system around the recipe.** The durable advantage is a *compounding loop*: a system that gets better the more it is used, fed by inputs only you have, wrapped in a workflow that is painful to leave. Everything else is a feature. This skill sorts the loop from the features before you spend eighteen months defending the wrong thing.

## DEPTH DECISION

**Go deep** (all sections) if: setting annual strategy, a board/investor defensibility narrative, or a competitor just raised on "the same thing but faster."

**Skim to the scorecard + fake-moat checks** if: quarterly review of a product already assessed — re-score the five, re-run the checks, find the weakest moat that matters.

**Cold-start mode (30–45 min — board meeting tomorrow, new market, an acquisition target):** run the OUTPUT template top-to-bottom directly. Answer the two brutal tests first, score the five moats with the band anchors below, tag every ungrounded score ⚠ with what evidence would firm it, and flag unresolved calls as `OPEN:`. A tagged provisional scorecard today beats a certain one after the decision. Worked example of exactly this mode: `references/moat-assessment-cursor.md`.

**Scoring band anchors (so two people score alike, especially cold):** 1 = doesn't exist · 2 = exists, a rival replicates it in one or two quarters · 3 = real, replication costs ~a year · 4 = measured lift + multi-year replication · 5 = measured, compounding, and getting *harder* to copy each quarter. Harness and trust never score ≥4 without production evidence (the strict rule below).

## THE TRAP

You will confuse *impressive* with *defensible*. The bias is recency: a novel capability feels like a moat precisely because it is new. Three months later every competitor ships the same thing and you are racing on execution cost, which is not a strategy. In AI, moats are invisible until they hold or break — a proprietary dataset, a deep integration, a safety brand can all look defensible on launch day and be commodities by month eighteen. Two tests cut through the theater. **"Why can't a competitor with the same model beat us next quarter?"** — if the honest answer names a feature, you have no moat yet. And the one operators use right now: **"Would anyone actually miss us if we disappeared tomorrow?"** — if the answer is no, you don't own the workflow or the experience, and there is nothing to defend. The teams that win know their moat *before* they build — roughly 5-17% of AI products survive 18 months in market, and the survivors almost all carry three or more compounding moats (⚠ directional).

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
- **Complementary input** — the resource whose cost isn't falling alongside a rented AI capability; margin concentrates wherever this input sits, not in the AI capability itself.
- **Corpus stock vs. flow** — a one-time archive (stock) versus a continuously refreshed production pipeline (flow); only the flow gives its owner recurring leverage, because a model degrades without fresh material.
- **Process knowledge** — the tacit third part of any technology, alongside tooling and written instruction, that lives only in hands and between heads and transfers solely through observation, never through a transaction.

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

## THE SCARCEST INPUT — WHAT DOESN'T GET CHEAPER

Before scoring the five moats, ask a sharper version of the Step 0 question: when this AI capability is rented and available to every competitor, where does the value actually land? A productivity gain from a capability nobody holds exclusively converts to price competition, not durable profit; the surplus flows to whoever holds a complementary input whose cost is not also falling. Where no such input exists, the surplus dissipates entirely to the buyer. Two historical illustrations show the shape of this, not a number to cite: US auto margins fell from roughly 30% to razor thin over seven decades, and US food spending fell from about 40% to 13% of household budgets over a comparable span (both ⚠, historical illustrations, not verified inside this corpus). The concrete AI-era instance: NBER research finds that writing 17.3 times more code produced only 1.3 times more shipped product releases (◆), a gain that never converted to proportional output value because writing code was never the scarce input.

**Run the complementary-input checklist before scoring moat 1.** Ask which of these you actually own, because one of them is where your real margin sits: capital and scale, a skilled user base, regulatory permission, societal acceptance, market structure, or proprietary data. Two places this checklist already hides inside your own stack. Vendors selling "digital colleagues" define the product as rented AI (falling cost) plus enterprise rules and data (non-falling, non-rentable). In a 132-enterprise MIT Sloan CISR survey (◆, Sept 2025), that second half is the actual moat, named inside the industry's own standard definition. Most buyers never notice it is the reason two vendors on the same base model perform differently. Under agent-mediated buying, the non-falling input is compute itself: agents rent inference from a handful of concentrated compute clusters, so falling rented-inference cost concentrates supply the way electricity or cloud storage does, not the way owning a personal computer distributed control in the 1980s. The "agents are the new PCs" analogy gets this backward: PCs moved control because they were owned; agents move control toward whoever owns the clusters they rent from.

**This reframe puts a boundary on moat 1.** A proprietary data corpus defends relative position, who survives the shakeout, but it does not stop the pool itself from shrinking, unless its exclusivity is enforced by something a rival literally cannot buy: a regulation, an exclusive sensor or distribution contract, a structural lock. Absent that enforcement, score the corpus as a relative shield, not a margin shield.

**Falsifier:** an industry-level price deflation where firm-level margin concentration among the leaders held or rose anyway, with the mechanism traced to something other than a non-falling complementary input. *(Source: BCG economists in HBR, "AI and the Looming Competition for Margin," Jul 2026; historical figures ⚠; NBER code-to-release figure ◆; MIT Sloan CISR digital-colleague survey, n=132, Sept 2025, ◆.)*

## THE FIVE COMPOUNDING MOATS

The frontier model is a commodity. What is not commoditized is what the team builds *around* it. Score each moat 1 (none) to 5 (deep), with evidence.

| Moat | Mechanism | The real-vs-vanity test | Decay clock |
|---|---|---|---|
| **1. Proprietary data + the ability to use it** | Specialized, accumulated data a rival can't legally or operationally replicate (customer interactions, domain labels, exclusive licensing) *plus* a proven ability to turn it into a measurable business result | Does it cover the *rare, hard cases* seen across many customers — or only the common, scrape-able body? | 12-24 mo; collapses to the mean if the loop is fed by public data |
| **2. Workflow integration depth** | Deep ties to the customer's systems; the Indispensability Index | Would migration cost multiple quarters of disruption, not an afternoon of copy-paste? | 18-36 mo; collapses in ~6 mo if a standard emerges |
| **3. Harness mastery** | Everything you build *around* the model call: tools, memory, context management, permissions, evals, retries, routing, caching, approvals, budgets, failure recovery, observability — the system that turns raw model output into reliable work | Would a rival need 6+ months to rebuild it — and can you *measure* it beats a simpler or open harness on the same model? | 24+ mo; accelerates if you publish the architecture |
| **4. Trust & reliability** | A track record of *working in production* — reliability, safety, audit trails, approval steps, failure recovery, spend controls (the "proof it won't blow up" buyers now pay for) | Do buyers who saw a flashier demo still pick you because you don't fail in production (provable in win rates)? | 5-10 yrs if consistent; **binary** — one major incident erases it |
| **5. Network effects** | Multi-tenant patterns where each new customer makes the product better for the others | Does each new user make the product better for *existing* users within weeks (not just add to storage)? | Hardest to build, most durable once built |

Examples that anchor each: proprietary data — Duolingo's labeled interaction loop, Harvey's legal corpus (◆). Workflow — the enterprise deployment wired into 5 critical systems. Harness — the team that invested in a mature harness in 2024-25 now out-optimizing teams that didn't. Trust & reliability — Apple's Private Cloud Compute, Anthropic's safety posture, SOC 2 / HIPAA / FedRAMP with measurable enterprise-sales effects (◆). Network effects — ServiceNow's 85B annual workflows of training signal no competitor has (◆).

**The decay clock above describes how fast an advantage erodes once it exists. It says nothing about a choice the holder actually controls: when to reveal the advantage in the first place.** For an advantage that already fails every protectability test in this skill, unpatentable, fully observable the moment it is used, the decay clock starts the instant it is revealed, not the instant a rival finally matches it. A useful three-question test for that timing decision, adapted from Harvard Business School's "A Winning Strategy: Innovation in Olympic Speed Skating" case: (1) is this genuinely secret, or are rivals plausibly already close to the same idea independently, a "twin innovation"? (2) What does a rival actually learn by seeing you use it, mere awareness that it exists, or performance validation that it works? (3) Would you act any differently depending on the answers to (1) and (2)? If the honest answers are "rivals are probably close already," "they'd mainly learn it works, not how," and "no, I'd reveal it either way," then delay buys little and reveal timing should be set by what disclosure itself can win you internally, buy-in from your own best people, or resources you cannot otherwise unlock, rather than by imitation risk alone. **When wrong:** this assumes the discloser has actually checked whether rivals are close to independent discovery, rather than assuming it for convenience; a wrong assumption here (rivals are not actually close) means early disclosure gives away years, not months. *(Source: HBR Cold Call, "Innovations in Olympic Speed Skating: When to Reveal a Novel Approach," Feb 2026, case HBS 725-391.)*

**A proprietary-data moat can also be an annotation or index layer over content that already exists elsewhere, not the raw content itself.** In one MIT Sloan case study (Warner Bros. Discovery, ⚠, single case, no disclosed methodology), the raw library had already leaked into training data through unauthorized use, so the defensible asset turned out to be the scene- and shot-level annotation layer over the library, not the footage. That layer is a real moat only while off-the-shelf video-understanding models cannot do the annotation themselves; once they can, the layer stops being scarce. Estimate that expiry date on the decay clock rather than assuming the layer is permanent.

**Harness mastery absorbs three things people list separately.** Your *eval-dataset* moat (thousands of curated production failures a rival with the same model does not have) and your *context-engineering* moat (retrieval and prompt architecture invisible in the API output) are not separate moats — they are faces of harness mastery. Score them together. The tell that it is real and not vanity: you can *measure* it beats a simpler baseline. If you cannot measure the lift, you cannot defend it either. This is the moat operators name most often in 2026 — the model is interchangeable, the system around it is not.

**Why trust & reliability is rising fast.** Once the model is good enough, the thing that wins the deal is no longer intelligence — it is *confidence*: does it work every time, can you see why, can it not blow up the budget. Enterprise money is flowing to the product that fails less in production, not the one that demos best. The proof is a clean track record and win rates against flashier competitors — not a safety page.

**Trust compounds only if every extension inherits the mechanism, not just the badge.** Moat 4 says a track record takes years to build and one incident to erase. It says nothing about the moment a company deliberately widens its own surface area, which is when most trust assets actually get spent. Porsche makes the mechanism visible, and it is not an AI company at all. Porsche went from roughly 10,000 cars a year in the early 1990s to more than 300,000 by 2024 (310,718 in FY2024, ◆) while extending from the 911 into SUVs, an entry-level model under $100,000, and EVs, and the premium held across all of it. The governing rule was never "carry the crest and meet the new category's own norms." Every extension had to clear the same driving-performance bar that earned the premium on the 911: "it's not just an SUV, but a Porsche SUV that has certain performance requirements." An SUV wearing the crest without the performance floor would have grown revenue while quietly converting a six-decade trust asset into a generic premium-badge play. For an AI product line the translation is direct. When a coding agent picks up a new task type or a support bot picks up a new channel, the extension protects the trust moat only if the new use case is held to the same eval bar, the same human-in-the-loop check, and the same reliability guarantee that earned the original trust. Ship the extension under the same product name with a visibly looser gate and Moat 4's binary property attaches to the whole brand, not just the new surface. **When wrong:** Porsche's bar is externally testable by the customer, a lap time anyone can verify, which makes it unusually easy to enforce and to notice when it slips. Most AI quality guarantees are not externally checkable by the buyer, so the mechanism may depend on verifiability in a way this case cannot show. *(Source: HBR Cold Call, "The Evolution of Luxury Brand Porsche," Mar 2025, case HBS 625-038. FY2024 deliveries: Porsche AG annual press conference materials, 12 Mar 2025.)*

**How operators rank these right now (mid-2026):** harness first (the model is interchangeable; the system around it is not), then specialized data + workflow depth, with trust & reliability rising fast and distribution/ecosystem treated as a first-class force. The weighting above reflects that. The deeper dynamics below — Vertical-Infinite, Living Software, cycle-time — are still ahead of the public conversation; they are your edge, keep them.

**Apple Intelligence stacks four of the five** — workflow (deep iOS), harness (PCC), trust & reliability (privacy architecture), network effects (every iOS user produces signal) — skipping only proprietary external data, because the ecosystem is closed. Four of five is dominant.

## KNOW WHICH KIND OF AI COMPANY YOU ARE, BECAUSE THE MOAT DIFFERS BY TYPE

**Sorting by industry or by technology tells you almost nothing about defensibility. Sorting by how the company creates and extracts value does.** Six types, and each has a different moat and a different failure:

| Type | What they do | Where the moat is, if anywhere |
|---|---|---|
| **Originators** | build commercially deployed foundation models | capital and talent. **Models are converging and commoditizing**, so this moat is eroding from underneath |
| **Explorers** | invent tomorrow's AI rather than commercialize today's | research position on a 5 to 10 year horizon. **Measured in benchmarks and milestones, not revenue** |
| **Infrastructure builders** | the picks and shovels: data, APIs, developer frameworks, chips | **ecosystem adoption and workflow integration**, not raw model quality |
| **Enhancers** | application layer wrapping a foundation model for a vertical | **proprietary data, domain focus and UX.** Never technical superiority. Hypercompetitive |
| **Optimizers** | use AI internally to improve their own operations | operational excellence. **Not an AI moat at all**, and that is fine |
| **Experimenters** | piloting tools with no budget, roadmap or integration plan | none. **The largest cohort by far, and many stay here indefinitely** |

**Three things this map is good for.**

**It stops the wrong comparison.** An Enhancer benchmarking itself against an Originator's model quality is measuring the axis it does not compete on. Its moat is data, domain and UX.

**It names the commoditization risk honestly.** The Originator layer is the one where the asset is converging fastest. Anyone whose moat story depends on model quality alone should read that row twice.

**It exposes the Experimenter problem.** The challenge there is not adoption. **It is scale**, and no amount of additional piloting produces it.

*(Source: Shay & Davenport, MIT Sloan Management Review, Feb 2026 — ⚠ taxonomy-tier. The types are the authors' own sorting with named example companies and no comparative outcome data. They map the types onto McKinsey's makers/shapers/takers and similar schemes, so treat it as a useful lens rather than a measured segmentation.)*

## THE SCORECARD — A QUARTERLY ARTIFACT

Total the five scores (max 25). This is a heuristic, not an audited threshold — calibrate to your market.

- **≥ 12 — defensible** competitive position.
- **8-11 — thin.** One moat is probably carrying the rest; a competitor who matches it exposes you.
- **< 8 — exposure.** You are shipping commodity AI on a commodity model.
- **Fewer than three moats scoring ≥ 3 — fragile**, regardless of total. A team with one deep moat is exposed the moment a rival replicates that one thing; a team with three forces the rival to replicate three, each taking years.

**Score harness mastery and trust & reliability strictly.** They only earn a 4 or 5 with a *measured* lift over a simpler baseline and a *production* track record — never on a demo or an intention. These two are where 2026 buyers actually spend, so the bar to claim them is higher.

**The most common surviving combination in 2026** is harness + specialized data + workflow depth (with trust & reliability often the fourth). Keep the "three or more moats scoring ≥ 3" filter as the survival test.

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

**Not all data is a moat — score the tail, the liquidity, the vintage, not the volume.** General models master the *common* cases fast; the uncopyable part is the rare, expensive-to-get-wrong cases. In one field-service dataset (Bluon, HVAC), ~a third of real issues were oddballs fitting no common topic, and 27 of 59 topics held fewer than 300 examples each — that thin slice is the advantage (◆; [VERIFY] the call-count base; author holds Bluon equity). Also score data **liquidity** (ready-to-use: clean, reusable, validated — why an incumbent's agent ships faster on identical models; Caterpillar, MIT SMR, 21 May 2026, ◆) and **vintage** (how many years a rival would need to reproduce the history, even with a better model — time cannot be bought back; Lenovo, Handfield, HBR, 27 May 2026, ◆).

**A single company can run this test on itself, and Duolingo did.** Its language product and its newer math and music products share the same team, the same modeling technique (a Markov-model difficulty engine it calls BirdBrain), and even the same reused gamification infrastructure by design. The only thing that differs is twelve years of accumulated per-exercise behavioral data versus almost none, and the newer products "will admit they're probably" not yet at the mature product's quality bar (◆, HBR Cold Call, "How Duolingo Aims to Diversify Beyond Language Learning," Apr 2025, case-disclosed via the case's own co-author). When a same-team, same-model comparison still shows a quality gap, vintage is the more honest read than capability. *When it over-warns:* if the newer product closes the gap in a year or two rather than needing a comparable decade, the gap was more about content-space size or transfer learning from the mature product than about vintage itself, so treat this as a strong illustration, not proof the two are always separable.

And note: a data moat the customer can *feel* taxes its own trust premium — if the value visibly depends on harvesting the user's data, the data moat and the trust moat pull against each other (moderator ◆, [Journal of Marketing 2025](https://journals.sagepub.com/doi/10.1177/00222429251367342)).

**A flow only exists if the people producing it consented and are being paid. That is the condition the stock-versus-flow lens is missing.**

Two AI media platforms faced the same technical possibility and got opposite outcomes, and the difference was contract structure rather than model capability. One lets anyone generate work in a named artist's style with no consent and no path to paying them. The other operates inside an industry's existing consent-and-payment contracts, and **that is what bought it access to the top talent**, at a price it paid willingly.

**Access and payment are one mechanism, not two.** A platform with no consent mechanism cannot commission new high-quality material, which means **it is structurally limited to whatever it already scraped. It is a stock business by construction, whatever it says about its data advantage.**

**The pyramid observation, and it generalizes past creative work.** Students in the case work out how to commercialize an AI-generated track, and then someone realizes that if it were a hit, someone would copy them exactly as they copied others. **The whole pyramid falls.** If your differentiated output can be reproduced by anyone who can see it, your position is bounded by reproduction cost no matter how good the output is.

**So the defensible positions are narrower than "we have data":** either the input is contractually gated, or the output cannot be observed without also being paid for. **Ask a supplier of training data which of the two they have.** If neither, you are buying a stock at flow prices.

*(Source: HBR Cold Call with Zoe Cullen on the case "Metaphysic AI: Rethinking the Value of Human Expertise," Aug 2026 — ⚠ podcast case discussion. **No deal terms, license values or production figures are disclosed anywhere**; the "very high price" for consent is characterized and never quantified. Carry the mechanism and no number. The join to stock-versus-flow is this corpus's. Falsifier: an AI product built on non-consented training data that sustained a quality advantage through several model generations without licensing new material.)*

**Add one more question before accepting a "we have proprietary data" claim: is this corpus a stock or a flow?** The Atlantic licensed its content to OpenAI and used the proceeds to pay its top journalists two to three times industry salary, because a model degrades without continuously refreshed high-quality material: the real purchase was a subscription to ongoing production, not a one-time archive. A corpus that must be continuously refreshed gives its producer recurring leverage a static archive never earns, which reverses the standard "build the archive, own the moat" advice for any organization that is archive-rich but production-poor. Score the flow, not just the stock. **Falsifier:** a substantial AI training-data license renewed at or above its original price for a fixed historical archive with no new material added during the term. *(All figures here are ⚠, a podcast transcript with no disclosed deal terms; carry the mechanism, not a number. Source: HBR Cold Call podcast, Caroline Elkins on The Atlantic/OpenAI licensing.)*

**Question Zero, and it runs before you score anything.** Before assessing any data asset's moat quality, **write down the problem frame the asset serves, and date-stamp when that frame was last genuinely challenged.**

**If the frame is more than 12 months unchallenged, the moat score is provisional regardless of which quadrant it lands in.** A defensible moat built around a stale or wrong problem is still a stale or wrong problem, and nothing else in this skill catches that. Every test below assumes the question is right and measures how well you have answered it.

**Why this matters more now than it used to.** Generative AI drove the cost of generating options toward zero, which moved the scarce resource from ideation to framing. **A competitor who reframes the problem does not have to beat your moat. They route around it.** See `rtp-first-principles` for the three-step protocol.

**The tail test is necessary and not sufficient. Add the race window.** Scoring the tail tells you whether the data *could* be an advantage. It says nothing about **how long you have to act on it**, and that is the term a startup competes on. Second test, and make it mandatory alongside the first: **can this data be operationalized into a live, agent-mediated feedback loop before a competitor builds an equivalent loop from a clean workflow?** An incumbent's workflows, data and roles evolved for stability, specialization and control. A team starting today designs the workflow around the agent. If your data is real but the workflow around it is too siloed or too brittle to wire up inside the competitive window, **the data advantage is theoretical whatever its volume**, and an agent dropped into a messy process reproduces the mess faster. The corollary that stings: skipping re-architecture before agent deployment destroys moat rather than building it, because bad data ingested at agent speed gets reinforced instead of merely repeated. *(Evidence for the compression is ◆ and self-interested: a venture firm's own portfolio reaching Series A on roughly $2M, about 80% less capital than its pre-AI startups, on a 20-40% shorter timeline, disclosed by the article's co-author who runs that firm, no independent audit **[VERIFY]**. Carry the mechanism, never these figures. HBR, "How Agentic AI Supercharges Startups and Threatens Incumbents," Aug 2026.)*

**The expertise moat has a precondition, and your own default tools can break it.** The most actionable test here, because the fix costs nothing and almost nobody runs the audit.

Domain expertise pays off through recombination, and recombination needs unfamiliar material. Standard search, discovery and recommendation systems are built on exploitation logic: they surface the popular, the relevant, and what your history predicts you want. In a field experiment, on a **standard search tool, domain experts showed no statistically significant advantage over novices** at generating creative solutions. Swap in a retrieval algorithm that deliberately surfaces semantically distant results and the same experts pulled away. The cleanest measure is the count of distinct solution clusters generated:

| | standard search | exploration-based retrieval |
|---|---:|---:|
| Novices | 1 | 2 |
| **Experts** | 2 | **5** |

**So domain expertise is an asset whose value is contingent on tool configuration, and a firm can hold the asset and capture nothing from it.** Your experts are on the payroll, the moat is on the scorecard, and the default search stack is quietly flattening them to novice output.

**The organizational version is worse, and it is invisible from inside.** When several people work the same challenge on the same exploitation-based tool, they are independently channelled to the same material and independently produce similar ideas. Each one is working alone and believes their independence is producing diversity. **The check:** semantically cluster the ideas a group produced independently. One or two clusters from a room of experts is the signal, and it looks like consensus.

*(Source: MIT SMR Research Highlight, Aug 2026 — ◆ and thinly reported. Written by the researchers, not refereed, underlying paper not named. Field n=245 across at least four cells, so roughly 60 per cell: **the expert-versus-novice null is underpowered and consistent with a modest undetected effect.** The four cluster counts carry no dispersion, no interval and no test, and clustering parameters are unstated. How expertise was classified is never stated, and the whole result turns on it. Use this to justify running the audit, not to size the effect. Ledger patterns K and O.)*

**A moat category this skill's language has been missing.** Any technology has three parts: tooling and equipment, written instruction (blueprints, patents, and this skill's own "corpus" language), and process knowledge, everything that lives in hands and between heads and cannot easily be conveyed to someone who has not observed the work. The first two are recordable, and this skill already scores them under moats 1 and 3. Process knowledge is the missing third: it transfers only through observation, never through a transaction, so it cannot be bought, licensed, or stolen because there is no artifact to take. This is exactly what the expertise-retirement test above is protecting, stated as an asset class rather than a symptom.

**Treat any claim about it as unfalsifiable until you name the transfer channel.** Process knowledge is defined by its own unrecordability, which makes it dangerously easy to blame for any decline and impossible to rule out as the cause of any other. Never assert the asset directly; assert a countable proxy for how it moves, for example hours per month of junior staff observing seniors perform the work, and score that proxy instead. *(Source: Dan Wang, HBR podcast, "What Makes Chinese Companies So Competitive?")*

**A second, non-technology example sharpens the same boundary, and splits process knowledge into two transfer speeds.** USA Speedskating's men's team pursuit trio invented an unpatentable, fully observable technique (one skater stays at the front the entire race while the other two physically push, eliminating the traditional method's rotation-drag penalty) and revealed it publicly two years before the Olympics it was built for. The case's own author draws the line precisely: the technique is "highly replicatable" by mere spectating, no embedded observer, no defection, just watching a race, yet perfecting it still needs "some more specialized knowledge." Rivals matched the concept fast enough to beat the US at its first Olympic outing, two years after the US had already revealed it publicly at the World Championships (Norway and the Russian Olympic Committee both beat the US in 2022). But the deeper layer, actually executing the push in sync at world-record pace, stayed exclusively the US program's for four more years, until a well-resourced, motivated rival finally closed that gap in 2026. **Mass, low-fidelity observation (watching a competition, not working alongside someone) transfers the concept layer of process knowledge quickly and the execution-quality layer only over years, if at all, on its own separate timetable.** *(Source: HBR Cold Call, "Innovations in Olympic Speed Skating: When to Reveal a Novel Approach," Feb 2026, case HBS 725-391.)*

**The fork that decides your architecture: is your data a corpus you retrieve from, or weights you own?** Executives routinely say "our model" and mean "our data," and the difference picks three downstream decisions at once.

One asset-management CEO put the common version plainly: *"I don't think everyone will have the same models. Training the model is all going to be about your own data."* **Read literally, that commits you to proprietary trained weights as the source of differentiation.** It also forecloses provider failover, because **you cannot switch models when your differentiation is your model.**

**The reconciliation, and a worked case makes it concrete.** One firm's procurement advantage came from holding 40 companies' contracts in a single queryable corpus. **Any competent model does the comparison. Only that firm has the corpus.** So the asset was retrieval, not weights.

**Proprietary data generally works better as a corpus you retrieve from than as weights you own.** If it lives in retrieval, failover is fine and the "our model" claim was about data all along.

**Pick the fork explicitly, because it decides three things:**

| | Corpus (retrieval) | Weights (trained) |
|---|---|---|
| Can you stay model-agnostic? | yes | no |
| Does the moat go stale when the frontier moves? | no, the corpus keeps compounding | yes, retraining is the tax |
| Can you name which model handled a given decision? | yes | harder |

**When weights genuinely win:** where the task is narrow, the data is enormous, and latency or unit cost at scale makes a general model uneconomic. That is a real case and a much smaller one than the number of firms claiming it.

*(Source: HBR, "Transforming Investing With AI at Franklin Templeton," Jun 2026, with the procurement case from a sibling article in the same batch — ◆ both single-company and self-reported. The fork and the reconciliation are this corpus's reading, not either article's claim.)*

**Fake-moat loop #1 — the anti-moat loop.** A feedback-loop moat has a condition the literature skips: the *inputs* must be yours alone. Run the loop on public signals every rival also ingests — competitor prices, web traffic, weather — and it drags you to the industry average, not ahead. The faster the loop, the faster everyone converges; the same failure appears in model training, where loops fed by model-generated or public data erase the edge cases that made the model useful. **The check:** are the inputs yours alone, or public? "Mostly public" = an anti-moat. The fix is never a new vendor; it is one signal only you can see plus one goal an off-the-shelf tool would never optimize for. **The same convergence trap shows up disguised as resilience, inside multi-model pipelines.** Running agents across Claude, GPT and Gemini decorrelates a firm's own errors, but does nothing to decorrelate that firm's aggregate behavior from the market's if every competitor in the sector diversifies across the same three or four frontier labs. A team can clear every item on an internal resilience checklist while staying fully exposed to sector-wide convergence. Diversification within a pipeline is not diversification from the market. *(Source: HBR, "The Strongest Teams of AI Agents Will be Built Using Different Models," Jun 2026.)* *When it over-warns:* in a thin-margin commodity market, converging on the same answer can be profit-maximizing. Evidence: German gas-station margins rose ~28% only when *both* stations ran the same algorithm on the same shared signals (✅ peer-reviewed — Assad et al., *Journal of Political Economy* 2024, DOI [10.1086/726906](https://www.journals.uchicago.edu/doi/10.1086/726906)). *(Van Esch et al., HBR, 13 May 2026.)*

**Fake-moat loop #2 — the agent-in-the-middle squeeze.** Once an AI assistant sits between your brand and the buyer, a relationship you thought was safe fails on two fronts. On the **persuasion front**, the assistant answers and cites two or three sources; the human never reads your page, so your positioning never fires — being seen becomes being *quoted*. On the **choice front**, the assistant buys against the user's rules ("a mattress under $800 that ships Friday") and never feels your brand — winning the citation can still lose the sale. The only lasting defenses are structural: own the assistant, own the data it needs to decide, or be so clearly trusted it cannot route around you. *When it over-warns:* where no assistant sits in the purchase, the classic relationship moat still holds; this front is early. *(Puntoni, HBR, 23 Feb 2026.)*

**The mechanism behind this squeeze, and the conflict of interest attached to it.** An agent negotiating on a buyer's behalf has no attention to capture and perfect recall of every alternative, so any differentiator that isn't a machine-readable fact (price, latency, refund terms) stops working, while brand, interface, and relationship effects get filtered out before they can register. The corollary: under agent intermediation, the moat moves from possessing an advantage to the rate at which you update it, because the agent re-checks constantly and a stale advantage is invisible to it. *(Source: MIT Sloan, "Who will own the AI agent economy?," Jul 2026, one researcher's position; he runs the initiative his own forecast favors, no data or study behind the claim. Flag it as a thesis, not a finding, and re-test the corollary before betting a roadmap on it.)*

**Fake-moat loop #3 — a corpus you cannot move is partly the vendor's moat.** The corpus is the asset, and where it accumulates decides who owns it. If your accumulated interaction history, tuned prompts, eval sets and rule stores live inside a vendor's system in a form you cannot export, the compounding is real and **the ownership is shared**. Two tests, both cheap:

- **The portability test.** What would it cost, in months and in money, to reconstitute this corpus somewhere else? If the answer is "we don't know," that is the finding.
- **The expertise-retirement test.** Your own competent in-house practitioners are the substitute that keeps a supplier honest. Retiring them transfers pricing power, and **the supplier's maximum-leverage moment is the first renewal after the last one has gone.** Keep people capable of executing the core function even when they are not doing it daily; that capability is the negotiating position.
- **The pre-AI test, and it is cheaper than the other two.** Would this corpus exist if AI had never been invented? Atlassian's HR team built an internal AI onboarding agent in a single day, with no prior coding experience, and it reached over 70% employee adoption (◆ company-disclosed). The tool's entire value came from a corpus assembled years earlier for an unrelated reason: page-led meeting decisions recorded in Confluence as an organizational habit, not an AI-readiness project. A corpus that would exist regardless of AI is usually a genuine asset, because whatever discipline built it is hard to copy on demand. A corpus assembled specifically to feed a model is a weaker claim: a competitor optimizing for the same model has the same incentive to assemble something similar, on roughly the same timeline. *(Source: HBR Cold Call, "Atlassian Anchors Remote Flexibility in Structured Daily Practices," Aug 2025, case HBS 925-029.)*

**The portability test cuts both ways.** A codified-expertise or process asset portable enough for you to reconstitute elsewhere is, by the same property, portable enough to walk out with a departing employee or get replicated by a competitor. Before counting it as a moat, ask whether it is a moat at all or just a head start before the elicitation method itself gets productized. A "portable expertise" claim is often self-defeating, since a moat by definition resists portability, and model-agnostic markdown judgment files that any foundation model can execute are exactly as portable out of the firm as they are valuable inside it. *(Source: HBR, "Teach Your AI How You Make Decisions," Jun 2026; ◆ company-disclosed cases.)*

**Fake-moat loop #4 — universality and exclusivity are different defenses and teams confuse them.** An exclusive corpus a rival cannot get earns margin. A **universal** corpus, product and service data published in the open standard machine buyers read, earns nothing in margin and buys you **presence in the consideration set**. Those are not substitutes. Failing at universality gets you excluded from decisions you never see, and no amount of exclusivity fixes an exclusion. Score them separately, and notice the direction: the exclusive asset is a source of profit, the universal one is a defense against disappearing. **Interpretability is a universality asset**, so see `rtp-marketing-to-ai-agents` for what makes a brand legible to a machine buyer in the first place. *(Source: HBR, "Algorithmic Shopping Is Here," Aug 2026 — ⚠ framework-tier, five-pillar maturity audit, no outcome data. Pairs with the portability test above. Ledger patterns K and W.)*

**Expertise held by employees is exclusive without being owned, a distinction this skill's taxonomy has been missing.** Acemoglu, Autor, and Johnson's five-category taxonomy of AI's effect on workers names expertise-leveling: letting a less-experienced person do work that used to require a specialist. That category surfaces a moat problem neither of this skill's existing ownership frames catches. An expertise-based advantage can be exclusive, a rival cannot simply acquire it, while still being rented rather than owned, because the people who carry the expertise can leave. It appreciates in a departing employee's hands, or a competitor's, at exactly the rate it appreciated in yours. This is a different axis from the exclusivity-vs-universality question above, which asks whether outsiders can access an asset, and from the corpus stock-vs-flow question, whether an asset needs continuous refreshing. It is about who owns an asset that is already exclusive, the firm or the individuals who carry it. **Falsifier:** an organization whose expertise-based advantage survived losing a substantial share of the people who held it, through codification into a durable, transferable artifact, would show this fragility can be engineered away, at least in part. *(Source: Acemoglu, Autor, and Johnson, five-category taxonomy of AI's effect on workers, ⚠ reported in this pass, not independently verified against the primary source.)*

## THE FORCE THE PENTAGON PREDATES — DISTRIBUTION

The five-moat pentagon is about what you build. The 2026 research adds a force it under-weights: **distribution is often a stronger moat than the AI itself, and it is the incumbent's structural weapon.** Incumbents push native assistants onto every surface so the default is "good enough" without the user ever leaving; the corollary is a warning — *if your product needs another company's data access or distribution to work, assume that access gets harder, not easier.*

Score distribution with three plain questions the pentagon doesn't ask:
- **Do you own a default surface or a developer ecosystem** — a place users already are, or tools/APIs that others build on?
- **Does more usage make the product better for other users**, or only for you? (The first is a real ecosystem effect; the second is just your own data pile.)
- **Is your reach partner-dependent — and is that access getting harder?** The 2026-defining case: **your model supplier competing downstream with its own customers** (frontier labs shipping coding agents against the IDE startups built on their APIs). If the company you rent intelligence from also sells your product's category, price that squeeze into the 18-month projection — neutrality across models is a partial hedge, not a moat.

**A subtler distribution asset sits inside training data itself: how often your brand already appears in the corpus a model was trained on.** That presence functions as a distribution channel a new entrant cannot buy the way it buys search-ad placement. In a randomized-label field experiment (n is about 1,000 US adults, ◆, a real identification strategy), Vanguard and iShares appeared unprompted in AI financial-advice responses at 6% and 3.4% respectively, while fewer than 0.4% of prompts named either brand, a 15x and 8x unprompted amplification. That kind of presence concentrates surplus toward incumbents already deeply represented pre-training. One open confound to flag honestly, not settle: the study does not fully rule out that these were implicit references users already made, describing an employer's Vanguard 401k plan without naming it, so treat the mechanism as plausible and the exact multiplier as unconfirmed. *(Source: Choukhmane et al., MIT Sloan working paper on AI financial advice, unrefereed, ◆.)*

One live move worth naming: **open-sourcing your harness or tools can be a distribution play, not charity.** More builders adopt it → more usage → faster iteration and an ecosystem competitors have to fight — the CUDA and Android pattern (the read on xAI open-sourcing Grok Build). *(Newer and less settled than the five — [AI Moats in 2026, Valtorian](https://www.valtorian.com/blog/ai-moats-2026); [How Agentic AI Supercharges Startups and Threatens Incumbents, HBR, Jul 2026](https://hbr.org/2026/07/how-agentic-ai-supercharges-startups-and-threatens-incumbents).)*

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
| Branding | Trust & reliability | Premium provable in win rates — or do they just know your name? |
| Cornered Resource | Proprietary data | Exclusive by contract, equity, or unique history — or buyable with capital? |
| Process Power | Harness mastery (evals) | Would a rival with the same hires and budget still ship worse for 3+ years? |

Score each Power Strong / Emerging / Absent and map it to its AI moat. A Power that scores Strong while its underlying AI moat is weak is a fragile claim — the appearance of defensibility without the mechanism. Reframe it before it reaches the deck.

## WHERE YOU ARE — OUTPUT

```
## Moat Assessment: [Product]

Value-line: [cost / growth] — ceiling: [bounded ~10% / multiplied into the valuation]
Core value engine: [the irreplaceable capability, not the feature]
The two brutal tests, answered first:
  Why can't a same-model competitor beat us next quarter? [specific, or "no moat yet"]
  Would anyone actually miss us if we disappeared tomorrow? [who, and what exactly would they miss]

Five-moat scorecard (1-5 each; ≥12 defensible, <8 exposure, 3+ moats to survive):
| Moat | Score | Evidence | Decay clock |
| 1. Proprietary data      | | [rare-hard-cases Y/N; liquidity; vintage] | |
| 2. Workflow depth        | | [migration cost in quarters]              | |
| 3. Harness mastery       | | [rebuild months; measured lift Y/N]       | |
| 4. Trust & reliability   | | [win-rate premium; incident count]        | |
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
