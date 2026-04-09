# Skill Naming Table — Complete System
**Version:** 2.0 (5-Plugin Architecture + Orchestrator)
**Date:** April 5, 2026
**Standard:** Every name + description should be instantly clear if you just woke up.
**Entry point:** `rtp-aipm-orchestrator` — the master skill that deploys all others.

---

## Architecture: Orchestrator + 5 Plugins

The **rtp-aipm-orchestrator** is the single entry point. It reads context, identifies the real problem, and deploys the right skills from the 5 plugins below. Users never navigate plugins directly — the orchestrator routes them.

**Thinking skills (first-principles through failure-design) are embedded in the orchestrator's cognitive architecture.** They're not a separate plugin — they're how the orchestrator THINKS. They remain as standalone files for direct invocation when needed, but their primary home is inside the orchestrator's reasoning.

| Plugin ID | Full Name | Plain English | Skill Count |
|---|---|---|---|
| `rtp-product-sense` | RTP Product Sense | **Understand the problem + user.** Thinking skills, customer insight, UX, use case evaluation, domain knowledge, bias detection. Includes the 7 thinking skills as the cognitive foundation. | 19 |
| `rtp-product-strategy` | RTP Product Strategy | **Decide where to invest.** Portfolio, competitive positioning, build/buy, cost reality, moat analysis, market signals, PMF. | 9 |
| `rtp-agent-design` | RTP Agent Design | **Build + control AI agents.** Autonomy levels, architecture, multi-agent coordination, control frameworks, human-agent collaboration. | 8 |
| `rtp-org-adoption` | RTP Organization & Adoption | **Get the org ready + adopting.** Safety, trust, responsible AI, change management, adoption design, psychological safety, org readiness. | 13 |
| `rtp-product-craft` | RTP Product Craft | **Prove it works + ship it.** PRDs, specs, evaluations, experiments, metrics, monitoring, cost models, ship decisions. | 13 |

**Total: 5 plugins, ~62 skills (including 8 new from HBR synthesis + orchestrator)**

### Orchestrator (Meta-Skill)

| Skill | Description |
|---|---|
| `rtp-aipm-orchestrator` | **The brain that deploys the skills.** Reads context, identifies the real problem using 10 thinking algorithms, builds an executive plan, checks alignment with user, then executes by invoking expert agents silently. CPO in front, executioner in back. The Bridger. |

---

## Skill-to-Expert-Agent Mapping

The orchestrator organizes skills into 6 expert agents that can challenge each other:

| Expert Agent | Skills | Role |
|---|---|---|
| **Sense-Maker** | first-principles, problem-ai-fit, use-case-ready, domain-decoder, hidden-value-finder, uncertainty-map, voc-accelerator, trendslop-check | Understand the problem before any solution |
| **Strategist** | strategy-canvas, moat-finder, build-or-buy, cost-reality, portfolio-manager, signal-scanner, competitive-map, fit-signal | Where to invest, what to kill |
| **System Architect** | autonomy-spectrum, agent-ecosystem, tool-architecture, agent-harness, friction-audit, multi-modal, determinism-compass | Design the right architecture + autonomy |
| **Safety Expert** | safety-by-design, rai-ops, trust-ladder, adoption-launch, needs-guard, judgment-guard, alignment-check, breach-ready, agent-risk, trust-under-fog, purpose-dialogue | Make it safe + get people to use it |
| **Evals Expert** | eval-framework, eval-first, ai-metrics, prod-watch, experiment-rig, org-ready, confidence-tuner | Prove it works with evidence |
| **Crafter** | ai-prd, context-spec, agent-spec, cost-model, ship-decision, prompt-as-product | Produce the documents that ship the product |

---

## Naming Convention Rules

1. **2-3 words max** (hyphenated as slug)
2. **Wake-up test:** Read the name + first line of description. If you can't explain it to a colleague in 5 seconds, rename it.
3. **Action or outcome oriented** — what you DO or what you FIND
4. **Interview-natural:** "I ran a [skill-name]" should sound professional
5. **No overlap:** No two skills should trigger on the same user question
6. **RTP signature:** All skills carry `author: RTP` and `plugin: rtp-[plugin-name]` in metadata

---

## RTP PRODUCT SENSE — Thinking Foundation (7 thinking skills)

The orchestrator's cognitive architecture. These skills are how the system THINKS — they run silently during every analysis. Also available for direct invocation.

| # | Skill Name | Wake-Up Description | When to Use (Trigger) | Status |
|---|---|---|---|---|
| T1 | `first-principles` | **Break any AI problem down to the ONE thing that actually matters before choosing a solution.** Strips away vendor hype, stakeholder preferences, and shiny demos to find the real problem. | Someone says "let's add AI to X" / evaluating a feature proposal / team jumped to a solution without defining the problem | Existing ✅ |
| T2 | `bias-spotter` | **Find the hidden biases — in data, in models, and in your own team's thinking — before they become product failures.** Structured audits of training data, output distributions, historical patterns. Covers data bias, algorithmic bias, and human cognitive biases. | "Is this data fair?" / auditing training data distribution / model outputs consistently skew toward demographic X / pre-launch bias audit / examining team assumptions about users | Existing ✅ |
| T3 | `red-team` | **Prove yourself wrong before the market does.** Force yourself to find evidence AGAINST your hypothesis. If you can't disprove it, it's probably real. If you can, you just saved months. Previously `falsification` — renamed because nobody wakes up knowing what falsification means. | "How do we know this works?" / team is too confident in pilot results / setting up experiments / need causal evidence, not correlation | **Renamed** 🔄 |
| T4 | `dual-lens` | **Look at every AI decision through two lenses at once: what's the business impact AND what's the technical reality?** Prevents the two most common failures: great tech that nobody needs, and great business case with impossible tech. | Bridging exec and engineering conversations / "what's the ROI?" alongside "can we build this?" / either lens missing from a proposal | Existing ✅ |
| T5 | `determinism-compass` | **Figure out how predictable your AI output actually is — and design accordingly.** Is the output guaranteed (like a lookup table) or probabilistic (like an LLM)? The answer changes everything: testing approach, user expectations, governance needs. | "How reliable is this?" / choosing between rules-based and ML / stakeholders expect guarantees from probabilistic systems / "can we promise this works every time?" | Existing ✅ |
| T6 | `stress-test` | **Push your AI to its breaking point BEFORE users do.** Test edge cases, adversarial inputs, long-running scenarios, and the 5% where things go wrong. Also checks: are humans still thinking, or just accepting AI output? | "What happens when this breaks?" / pre-launch review / team says "it works 95% of the time" without testing the 5% / signs of judgment erosion in the team | Existing ✅ |
| T7 | `failure-design` | **Design the architectural response to each failure mode — including graceful degradation.** Given a specific failure (your product hallucinates, model drifts, user gets adversarial input), what's the designed response? Does the system degrade safely? Show clear error? Escalate to human? Never take irreversible action? This is about WHAT YOU BUILD, not what you predict. | "What's the fallback?" / "System either works perfectly or breaks completely" / designing error states / high-stakes AI needs degraded-mode fallback / incident post-mortem: "Why didn't the system degrade?" | Existing ✅ |
| T8 | `alignment-check` | **Check if your organization is actually ready for AI — structure, roles, accountability — before spending on technology.** 93% of AI failures are organizational, not technical. This skill maps the 5 links (Purpose → Strategy → Capability → Architecture → Systems) and finds which one is broken. | "Why do our AI projects keep stalling?" / "We bought the tech but can't scale" / pre-initiative readiness / pilots succeed but production fails / new to a company and need to assess AI readiness fast | **New** 🆕 |
| T9 | `judgment-guard` | **Prevent your team from losing the ability to think for themselves as they rely more on AI.** Without designed friction, people accept AI outputs without engaging their own judgment. Over 6-18 months, expertise atrophies silently. This skill designs checkpoints that keep humans sharp. | "People just click Accept on everything" / "Our team's skills are getting worse" / designing high-stakes workflows / when you notice nobody questions the AI anymore | **New** 🆕 |
| T10 | `problem-type` | **Figure out if you're facing a technical problem (clear solution, known path) or an adaptive challenge (unclear solution, requires people to change).** Most AI failures happen because teams treat adaptive challenges like technical problems — they keep "solving" something that requires organizational change, not a better algorithm. | "We tried everything and it didn't work" / same problem keeps recurring / the fix is obvious but nobody implements it / leadership says "just build it" but the real barrier is organizational | **New** 🆕 |

---

## RTP PRODUCT SENSE — Customer & Market (12 skills)

How to figure out what to build with AI and for whom.

| # | Skill Name | Wake-Up Description | When to Use (Trigger) | Status |
|---|---|---|---|---|
| PS1 | `problem-ai-fit` | **Decide if this problem actually needs AI — or if a simple rule, search, or spreadsheet does it better.** The Lookup Table Test: if you can describe the input-output in a spreadsheet, you don't need AI. Includes the 10x Value Rule: 10% improvements get commoditized in 18 months. | "Should we use AI for this?" / "Let's add AI to X" / the team is excited about a demo but hasn't proven the problem needs AI | Existing ✅ |
| PS2 | `failure-catalog` | **Build a comprehensive taxonomy of failure modes specific to YOUR product.** Hallucination, drift, adversarial attack, domain mismatch, silent failures, judgment erosion. For each: probability, consequence magnitude, existing mitigations. Not design — just diagnosis. This is the INVENTORY of what could go wrong. | Risk register audit / pre-launch: "What are all the ways this breaks?" / new failure mode discovered / need to brief board on failure taxonomy / quarterly risk review | **Renamed** 🔄 (was `failure-modes`) |
| PS3 | `invisible-stack` | **Reveal the 90% of AI product work that users never see — infra, data pipelines, governance, monitoring.** When stakeholders say "this should be quick" — show them the iceberg. Maps technical + organizational + governance readiness. | "Why is this taking so long?" / "The model works in demo but not production" / stakeholders underestimate infrastructure / need to justify timeline or budget | Existing ✅ |
| PS4 | `feedback-flywheel` | **Design loops where every user interaction makes the product smarter.** Without this, your AI stays frozen at launch quality. Captures: user corrections, edge cases, segment-specific signals, adoption data by phase. | "How do we get better over time?" / "Our model isn't improving" / no system for capturing user corrections / need to design the learning loop before launch | Existing ✅ |
| PS5 | `uncertainty-map` | **Map what you don't know into a research plan — distinguish "unknown but findable" from "genuinely unknowable."** Four quadrants: predictable short-term, unpredictable short-term, predictable long-term, true unknowns. Each needs a different strategy. | "What are our unknowns?" / "How do we reduce risk?" / team is building with high uncertainty but no research plan / need to prioritize what to learn first | **Renamed** 🔄 (was `uncertainty-research`) |
| PS6 | `ai-ux-patterns` | **Design AI interfaces that feel right — preserving human agency, showing confidence honestly, and earning trust through transparency.** The research is clear: framing AI as "teammate" (not "tool") increases adoption 3x. UX that preserves autonomy, competence, and relatedness drives adoption more than capability. | "How should the UI work?" / "Users don't trust the AI" / adoption is low despite good model / need to design confidence indicators / redesigning for psychological safety | Existing ✅ |
| PS7 | `product-taste` | **Develop the intuition for what makes an AI product feel right vs. feel off — including knowing what NOT to automate.** Taste is the judgment that says "technically possible, but we shouldn't." Includes recognizing RAI theater vs real operationalization, and authenticity vs AI-polish. | "Something feels wrong but I can't articulate it" / evaluating competitor products / deciding what to automate vs preserve as human / reviewing AI-generated communications for authenticity | **Renamed** 🔄 (was `ai-product-taste`) |
| PS8 | `use-case-ready` | **Score whether a use case will actually survive from pilot to production.** Three dimensions: Structure (structured vs messy data), Repetition (repeatable vs novel tasks), Exception rate (bounded vs chaotic edge cases). Score below 6/9 = likely fails at scale. | "Should we invest in this use case?" / "Will this scale?" / portfolio prioritization / evaluating vendor claims / team excited about a use case that hasn't been scored | **Renamed** 🔄 (was `ai-use-case-readiness`) |
| PS9 | `domain-decoder` | **Map the hidden language, assumptions, and unwritten rules that generalist AI misses in specialized domains like healthcare, legal, or finance.** Generalist LLMs fail catastrophically when domain semantics diverge from everyday language. "Negative" in healthcare doesn't mean "bad." | Deploying AI in any specialized domain / AI outputs are technically correct but domain-wrong / clinicians or lawyers say "the AI doesn't understand" / building for regulated industries | **New** 🆕 |
| PS10 | `voc-accelerator` | **Use AI to extract customer needs from interviews 10x faster than manual analysis.** Fine-tuned LLMs find 100% of primary + secondary needs vs 87.5% by human experts. But requires supervised fine-tuning on 1000+ prior examples — not just prompting. | "We have 500 interview transcripts and no time" / customer discovery is bottlenecked / need to scale VOC without losing nuance / evaluating whether to fine-tune vs prompt | **New** 🆕 |
| PS11 | `hidden-value-finder` | **Find the boring, behind-the-scenes operations where AI creates 10x more value than flashy customer-facing features.** Consumer-facing AI is the hype trap. Real value is internal: claims processing, supply chain, compliance. The "toddler model" — if the task is structured, repetitive, and bounded, it's perfect for AI. | "Where should we deploy AI first?" / team keeps building consumer-facing AI that doesn't stick / need to justify AI investment with fast ROI / back-office operations haven't been evaluated | **New** 🆕 |
| PS12 | `needs-guard` | **Ensure AI deployment doesn't threaten what workers actually care about: feeling competent, having autonomy, and belonging.** 31% of workers actively resist AI. 54% use unauthorized tools. These aren't skill gaps — they're signals that psychological needs are being violated. The AWARE framework diagnoses which need is broken. | "Workers are resisting AI" / "Adoption is low despite good tech" / "People are using unauthorized AI tools" / designing change management / pre-deployment worker impact assessment | **New** 🆕 |

---

## RTP PRODUCT STRATEGY (9 skills)

Where to invest, what to kill, how to scale. `competitive-map` and `fit-signal` moved here from Craft (they're strategic analysis, not document creation).

| # | Skill Name | Wake-Up Description | When to Use (Trigger) | Status |
|---|---|---|---|---|
| AS1 | `strategy-canvas` | **Map your entire AI strategy on one page — what to invest in, what to kill, what to explore.** Links portfolio decisions to organizational readiness. Shows where you're deep (competitive) vs shallow (vulnerable). | "What's our AI strategy?" / quarterly planning / portfolio feels scattered / board wants a one-page view | Existing ✅ |
| AS2 | `moat-finder` | **Identify what makes your AI product defensible — domain expertise, proprietary data, workflow lock-in — and what doesn't.** Generic tech is never a moat. Vertical SaaS with domain expertise: 80% on profitability path. Horizontal SaaS without domain: 15%. | "What's our competitive advantage?" / "Can competitors copy this?" / build vs buy / evaluating vendors / competitive positioning | Existing ✅ |
| AS3 | `build-or-buy` | **Decide whether to build AI internally, buy from a vendor, or engineer around it.** Classifies vendors by startup archetype and profitability trajectory. Vertical SaaS + defensible data = buy. Horizontal SaaS + high churn = build or engineer around. | "Should we build this ourselves?" / vendor evaluation / RFP process / team defaults to building without assessing alternatives | Existing ✅ |
| AS4 | `cost-reality` | **Model the REAL cost of AI — not just inference tokens, but the full stack: validation, monitoring, human review, guardrails, and audit.** Most teams model AI as just inference cost. True cost is 3-5x higher when you add everything needed for production. | "How much will this really cost at scale?" / business case development / unit economics review / someone modeled cost as just API calls | **Renamed** 🔄 (was `token-economics`) |
| AS5 | `maturity-tracker` | **Assess where your organization actually sits on the AI maturity curve — and what to fix next.** Tracks five layers: organizational design, adoption, judgment preservation, governance, domain optimization. Imbalance between layers predicts failure. | "How mature are we in AI?" / quarterly health check / benchmarking against industry / joining a new company and need to assess fast | **Renamed** 🔄 (was `capability-tracking`) |
| AS6 | `portfolio-manager` | **Manage AI investments like a financial portfolio — allocate by stage, rebalance quarterly, kill what's not working.** Most orgs run 50 shallow pilots instead of 3 deep bets. Only 4% of companies take focused approach — those achieve 2x sustained ROI. Kill rate for leaders: 20-25% annually. | "How should we allocate AI budget?" / quarterly rebalancing / too many pilots, no transformation / need to justify killing a project | **Renamed** 🔄 (was `ai-portfolio-management`) |
| AS7 | `adoption-launch` | **Treat AI adoption as a product launch — with personas, phases, and phase-specific support — not as a training program.** Adoption curves are predictable: Surge (Month 1) → Dip (Months 3-4) → Rebound (Month 5+). Organizations that give one-time training see 50% churn at the dip. | "Adoption is stalling" / "We trained everyone but nobody uses it" / planning AI rollout / adoption dipped at month 3 (predictable) / designing change management | **New** 🆕 |
| AS8 | `trendslop-check` | **Catch when AI is defaulting to trendy advice instead of context-specific strategy.** Across 15,000+ trials, LLMs show systematic bias: favor differentiation over cost-leadership, augmentation over automation, long-term thinking over immediate profit — NOT based on what's right for your business, but based on what's common in training data. This is distinct from general bias; it's specifically about strategic reasoning. | LLM keeps recommending the same strategy regardless of your industry/constraints / "why does it always suggest disruption?" / strategy generated by AI feels generic / bootstrapping company getting long-term vision advice / cost-leader getting told to differentiate / using LLM for multi-scenario strategic planning | **New** 🆕 |
| AS9 | `signal-scanner` | **Detect weak signals early — the trends, threats, and opportunities that are invisible in quarterly reviews but obvious in hindsight.** Dual-speed sensing: real-time operational signals (what's happening now) + long-term strategic signals (what's emerging). Companies with systematic signal scanning achieve 5% financial lift. | "What's coming next?" / annual planning / team is reactive not proactive / competitor did something surprising / industry shift you didn't see coming | **New** 🆕 |
| AS10 | `purpose-dialogue` | **Connect AI initiatives to what your organization actually stands for — because people adopt what they believe in.** Purpose without dialogue is a poster on the wall. Dialogue drives 10% commitment lift per point. Best Buy turnaround used this: purpose conversation → adoption → results. | "People don't see why we're doing this" / "Adoption is technically fine but emotionally flat" / commitment is low despite good tools / need to make the case for AI beyond efficiency | **New** 🆕 |

---

## RTP ORGANIZATION & ADOPTION (13 skills)

How to keep AI safe, get the organization ready, and drive adoption. Combines former Safety & Trust + organizational skills from Thinking + adoption skills from Strategy.

| # | Skill Name | Wake-Up Description | When to Use (Trigger) | Status |
|---|---|---|---|---|
| ST1 | `safety-as-moat` | **Turn safety from something that slows you down into something competitors can't copy.** In regulated markets, organizations with operationalized safety win deals, earn trust, and get approved faster. Safety isn't a cost — it's a moat. | "Safety slows us down" / "Competitors ship without safety" / positioning in regulated markets / safety treated as compliance, not advantage | Existing ✅ |
| ST2 | `trust-ladder` | **Design AI that earns exactly the right amount of trust — not too much, not too little.** Over-trust: users accept bad output. Under-trust: users ignore good output. Both are dangerous. Trust is calibrated through confidence signals, transparency, and honest uncertainty. | "Users trust the AI too much" OR "Users don't trust the AI at all" / designing confidence indicators / need to signal when AI is uncertain | Existing ✅ |
| ST3 | `safety-by-design` | **Build safety INTO the architecture from day one — don't bolt it on later.** Organizations that retrofit safety see 3x longer issue resolution. Four frictions (Identity, Context, Control, Accountability) must be designed in, not patched post-launch. | Pre-launch safety review / designing guardrails / someone suggests "we'll add safety later" / agent needs kill switch / compliance review | Existing ✅ |
| ST4 | `rai-ops` | **Make responsible AI real — move from principles on a wall to practices in the code.** If your RAI program is a principles document + an ethics board that meets quarterly, it's theater. Operationalization means: named owner per project, fairness hardwired into stage-gates, incentives aligned. SHARP framework. | "We have RAI principles but nothing changes" / "Ethics board is decorative" / gap between stated values and product behavior / preparing for EU AI Act compliance | **Renamed** 🔄 (was `responsible-ai-program`) |
| ST5 | `breach-ready` | **Design systems that SURVIVE being hacked — because "if," not "when."** Prevention-only security fails. Resilience means: can you operate 48 hours without digital systems? Can you isolate the damage? Can you restore from manual backup? FedEx survived NotPetya because of resilience planning. | "What happens when we get breached?" / post-incident review / designing systems that must work during attack / regulatory requirement for resilience | **New** 🆕 |
| ST6 | `agent-risk` | **For every agent: is the value worth the potential harm? And can you pull the plug fast enough?** Proportionality analysis (value vs worst-case) + kill-switch design (manual, anomaly-triggered, time-elapsed). If you can't kill it faster than harm cascades, don't deploy it. | "Should we give this agent more autonomy?" / pre-launch risk review for any agentic system / agent's worst-case exceeds business value / designing kill switches | **New** 🆕 |
| ST7 | `trust-under-fog` | **Communicate confidently when outcomes are genuinely uncertain — without over-promising or under-delivering.** Boards want guarantees. Customers want certainty. AI outcomes are probabilistic. This skill helps you build stakeholder confidence through transparency, not false promises. | "The board wants guarantees we can't give" / "Customers are nervous about AI" / communicating AI capabilities to non-technical audiences / probabilistic outcomes but deterministic expectations | **New** 🆕 |

---

## RTP AGENT DESIGN (8 skills)

How to build, control, and deploy AI agents.

| # | Skill Name | Wake-Up Description | When to Use (Trigger) | Status |
|---|---|---|---|---|
| AD1 | `autonomy-spectrum` | **Choose the right level of AI autonomy for every interaction — from autocomplete to multi-agent orchestra.** 7 levels, from "code decides everything" to "distributed AI decisions." The question isn't "how autonomous can we make it?" — it's "what level does each interaction DESERVE?" | "Let's build an agent" / designing any AI product / evaluating competitors / deciding between copilot vs agent / "should this be autonomous?" | Existing ✅ (Rewritten v2.0) |
| AD2 | `agent-ecosystem` | **Design how multiple agents work together — handoffs, coordination, and preventing one agent's mistake from cascading through the system.** Multi-agent systems multiply both power and risk. Cascade failures grow nonlinearly with agent count. Second-order prompt injection is real. | "We need multiple agents" / multi-agent architecture / agent A feeds into agent B / need to prevent cascade failures / designing agent-to-agent protocols | Existing ✅ |
| AD3 | `tool-architecture` | **Design which tools an agent can use — and the validation layer between "AI wants to act" and "action happens."** The non-negotiable pattern: AI proposes → deterministic software validates → execute. No high-stakes agent should act without a validation layer. | "What tools should the agent access?" / designing MCP/function calling / agent needs to take real-world actions / building the middleware between AI and execution | Existing ✅ |
| AD4 | `multi-modal` | **Design AI products that work across text, voice, vision, and code — choosing the right modality for each interaction.** Not every interaction needs voice. Not every input needs vision. Match the modality to the task, the user, and the environment. | "Should we add voice?" / "How do we handle images?" / designing multi-modal interfaces / choosing between text and voice for a workflow | **Renamed** 🔄 (was `multi-modal-product-design`) |
| AD5 | `agent-harness` | **The control framework for keeping agents safe, accountable, and within bounds.** Every agent needs: unique identity, scoped permissions, audit trail, human supervisor, and a kill switch. The four-friction model (Identity, Context, Control, Accountability) is the foundation. | "How do we control this agent?" / pre-launch safety review / agent needs guardrails / designing permission models / "the agent did something unexpected" | Existing ✅ |
| AD6 | `friction-audit` | **Quick pre-launch checklist: has this agent been designed with all four frictions?** Identity (unique ID, scoped permissions)? Context (authoritative data, provenance)? Control (validation layer, deterministic checks)? Accountability (audit trail, decision reconstruction)? If any is missing: stop and fix. | "Is this agent ready for production?" / pre-launch checklist / quick 30-minute diagnostic / any friction hasn't been explicitly designed | **New** 🆕 |
| AD7 | `collab-surface` | **Design the interface where humans and agents actually collaborate — not just "agent does, human checks."** How the human interacts with the agent determines adoption more than agent capability. Can the human easily override? Can the agent explain its reasoning? Is it positioned as teammate or tool? | "The agent works but people don't use it" / designing the human-agent interaction / team + AI collaboration / "how should the human interact with this agent?" | **New** 🆕 |
| AD8 | `agent-onboard` | **Treat deploying an agent like hiring a new team member: job description, probation period, performance review.** No agent goes to production without: clear role definition, explicit authority boundaries, measurable success criteria, a named human supervisor, and an intern-to-full-time progression path. | Deploying any new agent / "how do we introduce this agent to the team?" / agent has no clear role or evaluation criteria / transitioning agent from pilot to production | **New** 🆕 |

---

## RTP EVAL & QUALITY (7 skills)

How to prove AI works — with evidence, not hope.

| # | Skill Name | Wake-Up Description | When to Use (Trigger) | Status |
|---|---|---|---|---|
| EQ1 | `eval-framework` | **Choose the right evaluation method for the right AI system.** pass@k (variability is a feature) vs pass^k (consistency is non-negotiable). Different systems need different eval approaches. What you measure shapes what you build. | "How do we evaluate this?" / choosing evaluation methodology / team is measuring the wrong thing / need to distinguish "works sometimes" from "works reliably" | Existing ✅ |
| EQ2 | `eval-first` | **Build evaluation into every stage of development — before you write the first line of code, not after.** Multi-level feedback: model performance + user adoption + business impact + ethical impact. Single-level feedback creates blind spots. | "We'll add tests later" / "The model is good enough" / development outpacing evaluation / launching without knowing if it actually works for users | **Renamed** 🔄 (was `eval-driven-development`) |
| EQ3 | `ai-metrics` | **Define what to measure — and what to STOP measuring — for AI products.** Two-KPI model: one adoption target + one performance metric. Not 47 dashboards nobody reads. Key finding: satisfaction correlates 3x more with work quality than time saved. | "What KPIs should we track?" / metrics review / drowning in metrics but missing signal / measuring time saved when you should measure quality | **Renamed** 🔄 (was `ai-product-metrics`) |
| EQ4 | `prod-watch` | **Monitor AI in production — catch drift, degradation, and silent failures before users do.** AI systems degrade silently. Models drift. Edge cases accumulate. "Users are complaining but metrics look fine" is the classic sign. Design early warning signals, not just dashboards. | "The model was working last month" / "Users complain but metrics look fine" / designing production monitoring / post-launch quality assurance / need alerting for silent degradation | **Renamed** 🔄 (was `production-observability`) |
| EQ5 | `experiment-rig` | **Design rigorous experiments that prove AI value with causal evidence — not just "it seemed to help."** The same AI tool showed 14% overall lift but 34% for juniors, near-zero for seniors. Without segmentation, you'd scale to everyone. With it, you target where it works. Org experiments (randomized, controlled) predict ROI 2x better than pilots. | "Let's run a pilot" / "How do we know this actually works?" / scaling decision / team conflates pilot enthusiasm with proven value / need to understand WHO it helps, not just IF | **Renamed** 🔄 (was `gen-ai-experimentation`) |
| EQ6 | `org-ready` | **Before running an experiment: CAN your organization actually run one?** Most can't. This skill assesses: hypothesis discipline, randomization capability, measurement infrastructure, cross-functional ownership, patient capital. If you can't run experiments properly, the results are meaningless. | "We want to run experiments but..." / experiment results keep being inconclusive / no A/B testing infrastructure / teams can't articulate a null hypothesis / "our pilots always show positive results" (sign of poor methodology) | **New** 🆕 |
| EQ7 | `confidence-tuner` | **Design trust signals so users neither over-rely on AI nor ignore it.** 49% error reduction achievable through confidence alerts alone. Show endorsements when AI is confident + correct domain. Show warnings when AI is uncertain or outside training distribution. Calibrate, don't just display. | "Users trust the AI too much" or "not enough" / designing confidence indicators / need to reduce automation bias / alert fatigue from too many warnings | **New** 🆕 |

---

## RTP CRAFT (8 skills)

The documents and artifacts that ship AI products.

| # | Skill Name | Wake-Up Description | When to Use (Trigger) | Status |
|---|---|---|---|---|
| C1 | `ai-prd` | **Write the product requirements document for an AI feature — with governance, adoption design, and judgment preservation built in from page one.** Not a standard PRD with "AI" sprinkled in. Sections: problem, technical approach, adoption personas + phases, governance requirements, judgment preservation mechanisms. | Starting any new AI product or feature / need to document requirements / want a template that covers AI-specific concerns | Existing ✅ |
| C2 | `context-spec` | **Define what goes into the AI's context window — and why.** System prompt architecture, RAG design, tool definitions, memory strategy. For specialized domains: includes domain dialect mapping. For agents: includes authority boundaries and data provenance. | Designing context architecture / building RAG / writing system prompts / domain-specific deployment / "the AI doesn't understand our industry" | Existing ✅ |
| C3 | `agent-spec` | **Write the job description for an AI agent — authority, boundaries, metrics, supervisor.** Like hiring a person: what can they do, what can't they, how do we measure performance, who's responsible. Includes: decision rights, escalation paths, progression model. | Deploying any new agent / need to document agent capabilities / compliance review / agent has unclear boundaries | Existing ✅ |
| C4 | `cost-model` | **Build the spreadsheet that shows what this AI product ACTUALLY costs — including everything nobody wants to talk about.** Five cost layers: generation + validation + human review + monitoring + audit. The uncomfortable truth: total cost often 3-5x what the team initially estimates. | Building a business case / "how much will this cost?" / unit economics review / investor pitch / reality-checking someone's optimistic cost estimate | Existing ✅ |
| C5 | `ship-decision` | **Make the launch/no-launch call with evidence, not gut.** Five-layer readiness: org design ✓, adoption design ✓, judgment preserved ✓, governance embedded ✓, domain validated ✓. Requires causal evidence from experiment, not pilot enthusiasm. | "Should we launch?" / pre-launch review / go/no-go meeting / stakeholders pushing to ship before it's ready / need a structured decision framework | Existing ✅ |
| C6 | `competitive-map` | **Map your competitive landscape by what actually matters: archetype, moat strength, profitability trajectory.** Six AI startup archetypes with different survival odds. Track regulatory trends. Update quarterly. | Competitive analysis / board prep / competitor launched something / evaluating M&A target / "who are we competing against and where do they stand?" | Existing ✅ |
| C7 | `fit-signal` | **Read the signals that tell you product-market fit is real — or an illusion.** Combines: causal evidence from experiments, five-layer readiness audit, domain expertise depth. Distinguishes: "users like it" (vanity) from "users depend on it" (PMF). | "Do we have PMF?" / growth review / metrics are ambiguous / need to distinguish real traction from polite adoption | Existing ✅ |
| C8 | `prompt-as-product` | **Treat prompts as product surfaces — designed, tested, version-controlled, and defended against bias.** Prompts aren't throwaway strings. They're the interface between your product intent and model behavior. Test for: trendslop bias, domain dialect violations, rhetorical escalation, prompt injection. | "The prompt isn't working" / prompt engineering review / prompt quality directly affects product quality / need to version and test prompts systematically | Existing ✅ |

---

## CHANGE SUMMARY

| Action | Count | Details |
|---|---|---|
| Kept as-is | 24 | Names that already work well |
| Renamed | 14 | Clearer, shorter, more intuitive names |
| New skills | 14 | Added from HBR synthesis |
| Merged | 2 | `rai-operationalization` → `rai-ops`; `adoption-readiness` → `adoption-launch` |
| Dropped | 2 | `candid-feedback-for-growth`, `change-coalition-architecture` (not AI-specific) |
| **Total** | **~54** | Across 7 RTP plugins |

---

## TRIGGER CLARITY — Updated v1.1

Based on review for **understanding and correct invocation:**

### Bias-Spotter vs Trendslop-Check — Now Distinct
- **`bias-spotter`:** Structured audit of data/model outputs for systematic skew. WHEN: "Is this training data fair?" / examining output distributions / team assumptions.
- **`trendslop-check`:** Specific to LLM-generated strategy that ignores your context. WHEN: "AI keeps recommending disruption even though we're bootstrapped" / strategy feels generic / context-blind recommendations.

**Key difference:** Bias-spotter = Are outputs systematically wrong for a demographic? Trendslop-check = Are strategy recommendations systematically wrong for THIS company?

### Failure-Catalog vs Failure-Design — Now Clearer
- **`failure-catalog`:** Build the inventory. "What could go wrong?" WHEN: Risk register / pre-launch diagnosis / stakeholder briefing.
- **`failure-design`:** Build the response. "What do we DO if it breaks?" WHEN: Designing error states / need a degraded mode / incident post-mortem.

**Sequential usage:** Do `failure-catalog` first (diagnose possibilities). Then `failure-design` for each high-severity mode (architext the response).

### Product Sense — Structure Note
12 skills is large but not incoherent. Potential future split: Customer Insight (PS9-11: domain-decoder, voc-accelerator, hidden-value-finder) | UX & Adoption (PS6-7-12: ai-ux-patterns, product-taste, needs-guard) | Core Fit (PS1-5: problem-ai-fit, failure-catalog, invisible-stack, feedback-flywheel, uncertainty-map). Monitor adoption patterns to decide if split is needed.

## ITERATION NOTES

This is v1.1 — clarity pass. Areas for future refinement:

1. **Depth description length:** The wake-up test is about the FIRST LINE being clear. Some full descriptions are 2-3 sentences when they could be tighter. Future: Separate "first-line trigger" from "full context."

2. **Skills density:** Some plugins (Product Sense at 12) are larger than others (Safety & Trust at 7). This is correct given task variety, but future organization might benefit from sub-categories within large plugins.

3. **"New" vs "Existing" status:** Watch which new skills (14 added from HBR) see adoption vs stay dormant. This will inform whether they're framed correctly or if they need repositioning.

---

*v1.0 — April 5, 2026 — Open for Ravi's review and iteration*
