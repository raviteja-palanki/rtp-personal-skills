---
name: harness-operating-model
version: v1.3_latest
description: 'How to fund, staff, run, and future-proof a harness as a multi-year program: the discipline around the machine, not the machine. Covers the cost shape (front-load/plateau/compound), the five cost centers, the reliability dividend (failure getting cheap is the business case), the lock-in and runtime wedges, and the stopping rule. Then the maturity ladder, nine-day kit and stakeholder scripts. Then the four org models and deployment shapes, the Harness PM role, build against buy, and open against closed. Finally the longevity layer: permanent residents against the dissolving ladder, and why the harness is the moat. Use when budgeting or defending a harness program, deciding open/closed or build/buy, naming the harness owner, or placing your team on the maturity ladder. Sibling: agent-harness (the machine). Pairs with: cost-model, adoption-launch, alignment-check, capability-tracking, moat-finder. Triggers: ''harness cost'', ''harness ROI'', ''harness owner'', ''open vs closed harness'', ''human in the harness''.'
imports: [agent-harness, cost-model, capability-tracking]
---

# The Harness Program: Economics, Org & Longevity

**The objective:** turn a harness from a science project into a funded, staffed, compounding program — one that survives the CFO's month-fourteen question, gets a named owner before it needs one, and invests only in the parts that outlive the next model generation. This skill is the *program*. Its sibling, `agent-harness`, is the *machine* (the anatomy, diagnosis, and patterns). Build the machine there; here you decide what it costs, who owns it, and what stays yours.

## THE ONE IDEA

**A harness does not change the model's judgment. It changes what a wrong judgment *costs* — from an unrecoverable incident to a recoverable, auditable event.** That repricing of failure is the whole business case, because *an organization grants autonomy in exact proportion to how cheaply the system fails.* Three consequences reorganize how you run the program:

1. **The reliability dividend is the argument that survives a CFO who already knows tokens are cheap.** Productivity ("faster") is the surface pitch and it dies under scrutiny. The durable pitch: with a real harness a wrong decision at 3 AM is caught by an eval gate, routed to a human, reversed in a defined window, and logged for the auditor — so the autonomy limit moves from 5% to 30% *without the org flinching*, and the gain compounds from 5× more volume, not 5× faster completion. The cleanest demonstration: same Opus-class model, same prompt — no harness = $9 / 20 min / unusable; full harness = $200 / 6 hrs / a shippable product. The extra $191 didn't buy intelligence. It bought output the organization can act on. *(Practitioner-reported ⚠; trust the shape, not the decimals.)*
2. **The moat is the harness, not the model.** Mitchell Hashimoto (creator of Terraform, who has watched more infrastructure layers commoditize than almost anyone): *"Models are now commodities. Harness is the moat: business rules, data pipelines, verification logic. None of this transfers when you swap models."* Rent a closed harness for a differentiating workflow and you are renting the moat.
3. **At some point the org organizes *around* the harness — deliberately or reactively.** Three of the four MHTE layers already have owners (Model → Applied AI, Tools → Platform, Environment → Security). The harness is the one layer without a default owner, and "shared responsibility is another word for nobody's job." Naming the owner is the first org decision; every other one is downstream.

The machine wins a sprint. The program wins the eighteen months that decide whether your agents get renewed or quietly wound down.

## A WORKED OPERATING MODEL, WITH THE PART EVERYONE SKIPS STAFFED

This skill argues in the abstract for how to staff and run a harness program. Here is one financial-services firm's actual structure, useful because **it is the only one in this corpus that staffs adoption as a function rather than as an afterthought.**

**Four units, all reporting through a chief AI officer who owns product management, engineering, research and adoption together:**

| Unit | Shape | What it owns |
|---|---|---|
| **Embedded product teams** | one per business unit, run "AI-first" | product management, engineering and data science **fused into one team**, not three functions collaborating across boundaries |
| **Common AI platform team** | shared, central | the shared substrate |
| **Research team** | shared, central | scope not described in the source |
| **Adoption and solutions team** | shared, central | drives employee implementation **and** ties the tools back to a business benefit |

**Two things worth taking from this, and one worth noticing about what is missing.**

**Take the fusion.** Embedding product, engineering and data science in a single unit per business line is the structural answer to handoff latency, which is the failure this skill's org section already names.

**Take the staffed adoption function.** Most programs treat adoption as change management bolted onto a launch. Giving it a standing team with two explicit mandates, usage *and* business-benefit alignment, is the version that survives past the launch quarter. Route to `rtp-adoption-launch` for what that team should actually do.

**Notice what is not described.** The source names the platform team and then never explains it. **That absence is the finding**, not an omission in the write-up: the platform layer is the one everyone agrees they need and nobody specifies, which is exactly why this skill exists.

**One design principle from the same firm, carried with its own tension attached.** The stated objective is **"copilot, not autopilot"**: support investment advice rather than automate it, through better information and faster iteration. Hold that against the systems the same source describes, which can contradict a human analyst. **A stated copilot posture and a system with standing to dissent are not automatically compatible**, and the resolution rule is the thing to specify. See the launch gate in `rtp-trust-ladder`.

*(Source: HBR, "Transforming Investing With AI at Franklin Templeton," Jun 2026 — ◆ single company, self-described, no outcome data attached to the structure. Carry it as one worked example, not as a reference architecture.)*

## KEY TERMS (plain language)

- **Reliability dividend** — the return that isn't productivity: failure becomes cheap and recoverable, so the org trusts the system with more volume. "95% cheaper and worth zero, vs 22× more expensive and worth a product."
- **The cost shape** — front-loaded (Year 1), plateau (Year 2, the political danger zone), compounding (Year 3). Any other shape means the budget is lying.
- **The five cost centers** (in order of magnitude): eval infrastructure + ground-truth authoring; staff-engineer + PM attention during ramp; observability + trace storage; human review for high-stakes paths; harness maintenance/migration debt — with token spend usually the *fifth*, not the first.
- **Lock-in wedge** — the Year-3 cost of a Year-1 convenience: a closed harness that owns your memory policy compounds rent every quarter and never shows on a purchase order.
- **Runtime wedge** — even an open harness pays for the runtime beneath it (durable execution, checkpoints, audit-grade observability); a budget with no runtime line undercounts by ~30–40%.
- **Maturity ladder** — five rungs: Prompt → Retry → Eval Suite → Harness → Harness Discipline. Most teams are at Rung 2 acting like Rung 4.
- **Harness PM** — the named owner of the harness product: its failure modes, eval suite, cost envelope, autonomy envelope, and change policy. The single highest-leverage AI-native hire.
- **Human-in-the-harness** — the replacement for "human in the loop": humans are a *component* the harness routes to (review queue, escalation, feedback channel), not a synchronous gate on every action.
- **Permanent residents vs dissolving ladder** — the five capabilities no model absorbs (your evals, workflows, audit trail, cost controls, user context) vs the ones it does (structured output, tool-calling, long context, multi-step reasoning, generic safety).
- **Open vs closed harness** — you author the five clusters (open) vs you configure a vendor's (closed). The first org decision, and it's per-workflow.

## THE ECONOMICS — What It Costs, What It Returns

### The cost shape (front-loaded → plateau → compounding)

**Year 1 is front-loaded** — you're paying for the infrastructure that makes AI *usable*, not for AI. Harness infrastructure typically runs **3–5× the token-spend budget**; if your AI line-item leads with token cost, the ratio is inverted. **Year 2 is the plateau** — the most politically dangerous phase: visible spend drops, returns haven't compounded, and the honest answer to "what's it done for us?" is "it stopped costing us what the unmanaged version cost." Reframe *before* the meeting: "we eliminated the incident class costing us $X/quarter; Year 3 converts that recovered floor into new throughput." **Year 3 is where the return lives** — the harness absorbs new-workflow onboarding, evals catch regressions before users, autonomy limits rise because failure is now recoverable. Most programs die on the plateau — not because the harness was wrong, but because the budget was shaped wrong and the CFO lost patience on month fourteen. *If your CFO hasn't pushed back yet, you haven't built the real budget.*

### The five cost centers most budgets miss

Every budget ranks tokens first; every program that *runs* has the opposite ranking. In order of magnitude: **(1) eval infrastructure + ground-truth authoring** — the largest and least-budgeted; if you cut one line, not this one (it's the training data for everything else). **(2) Staff-engineer + PM attention during ramp** — your best engineer off the ship-rate for a quarter; invisible on the token bill, load-bearing. **(3) Observability + trace storage** — compounds at production volume; the day you realize you needed 90-day retention not 14, the bill has a shape nobody planned. **(4) Human review for high-stakes paths** — structural, doesn't disappear as models improve (moves up the stack to harder cases); the *queue* is infrastructure — 3% of 10k daily sessions at 5 min each = 25 person-hours/day, plus review tooling, escalation routing, and calibration dashboards. **(5) Maintenance + migration debt** (tokens live here) — cheap to do, ruinous to skip; skip it and every model upgrade becomes a month-long migration exactly when you want to ride the next frontier model.

**The token-ledger paradox:** per-token prices fell ~67% YoY ($18.40 → $6.07/M, FinOps Foundation, 2.4B calls) while enterprise bills *tripled* ($1.2M → $7M), because agentic/reasoning workloads consume 5–30× the tokens of a chat turn. Unit price is not the story; consumption is — and consumption is a harness decision (model routing, effort dials, per-cluster attribution). Recall Datadog's finding: 69% of production input tokens are system prompts — context-rot manufactured at industrial scale, and a Memory-Policy choice, not a vendor price.

### The wedges, the trilemma, the stopping rule

- **Lock-in wedge** — two programs with identical Year-1 cost can diverge 3× by Year 3 on the open-vs-closed choice alone. **60% of workflows** (internal productivity, non-differentiating CX) belong on a closed stack without remorse; the **40%** (agents that *are* the product, regulated data, proprietary-evals-as-moat) should pay the Year-1 open cost or underwrite a Year-3 migration nobody wants. Classification test: *would we be hurt if this vendor changed their memory policy next quarter?* If yes, it's 40% territory.
- **Runtime wedge** — buy the runtime (most should), but *know* you bought it and have an exit story; a budget with no runtime line undercounts ~30–40%.
- **The trilemma** — cost / quality / speed trade against each other; a budget claiming all three improve on the same axis hasn't been stress-tested. Name the one you're paying for this quarter.
- **The stopping rule** — the dividend has a ceiling. Stop engineering a harness capability when (a) it's on the frontier lab's roadmap (buy time with a thin wrapper, don't build deep), (b) the eval curve has gone flat (last three edits moved reliability <1pp), or (c) the next dollar buys more *coverage* (a new workflow) than *depth* (a workflow already at 95%). Year-3 compounding is *one harness applied to five more workflows*, not one harness that keeps getting deeper.

### Break-even: three signs, none numerical

Break-even is legible in behavior a quarter before the dashboard shows it. **(1)** Engineers stop rewriting prompts every sprint (the eval suite absorbed the drift). **(2)** The eval suite catches regressions before users do (the loop runs backwards; incident cost drops 1–2 orders of magnitude). **(3)** The CFO stops asking for the business case and starts asking for the *expansion* plan ("can we run compliance on it too?"). Watch the CFO; the CFO will tell you.

## THE AI SPINE: A THIRD ORG SHAPE, AND THE FUNDING TRICK THAT MAKES IT WORK

Most companies pick one of two shapes and both have a known failure. **A center of excellence hoards the expertise and never learns the business process. Business-unit squads learn the process and rebuild the same plumbing five times.** A third shape sits between them.

**The AI spine is a permanent cross-functional structure that owns use cases end to end**, centralizing technical and business-process knowledge in the same body rather than splitting them across two.

**Inside the spine, three permanent roles:**

- **A technology owner**, who prevents fragmentation of data and tools and runs the shared platform: prompt libraries, models, evaluation, and cost metrics including token consumption.
- **AI developers and engineers.**
- **A risk and compliance role that lives inside the spine**, not an outside compliance group consulted at gates. That placement is the design decision, because a reviewer who is not in the room reviews artifacts rather than choices.

**Connected in from each business unit, three more:**

- **A business owner** who identifies use cases, sets nontechnical targets (a minimum star rating, say), and is **accountable for killing underperforming use cases.**
- **A knowledge owner** who curates ground truth, captures tacit knowledge, and holds **the authority to declare a solution good enough even when it is not technically perfect.** That authority has to sit somewhere or nothing ever ships.
- **End users** who validate usefulness and surface edge cases.

Overseen by a C-suite leader who keeps it aligned to strategy. Cadence: biweekly standups inside the spine, a monthly summit with end users for demos and feedback.

**The funding mechanism is the part worth stealing.** Top management allocates capital, **and the spine keeps a cut of the revenue or cost savings it generates.** Two things follow that no governance document achieves on its own: ROI discipline becomes self-interested rather than imposed, and **killing a weak use case stops being political**, because the spine is spending its own future budget by keeping it alive.

**The three practices this structure institutionalizes:** expand a use case across a whole process rather than one task, treat every use case as continual work in progress, and kill underperformers fast.

*(Source: Schmitt, Vial & Blohm, in the MIT Sloan Management Review special report "Scaling AI in the Enterprise," Summer 2026, sponsored by Workhuman — ⚠ and the sponsorship matters: a vendor-sponsored special report is not neutral ground. The spine is the authors' own model, diagrammed rather than measured, with no comparative outcome data against centers of excellence or unit squads. Falsifier: a company that scaled generative AI across many processes on a hub-and-spoke center of excellence with no cross-functional owner.)*

## THE MATURITY LADDER + THE MONDAY KIT

**Five rungs:** (1) *"We have a prompt"* — a string and a model call; nobody owns the prompt file. (2) *"We have a retry"* — naive retries, some parsing; where 60–70% of enterprise teams sit, stalled on drift. (3) *"We have an eval suite"* — ground truth exists, structured output enforced, drift detection live; **the highest-ROI transition in the whole program — most of the pain disappears here.** (4) *"We have a harness"* — all clusters exist, observability traces every call, the team has a name and a diagram for it. (5) *"We have a harness discipline"* — everything versioned, migrations written, a named owner whose job is to *tend* the harness, not ship the next feature. Rung 5 teams are rare and are the ones whose agents get renewed year after year. *Most teams are at Rung 2 acting like Rung 4; the ladder is a diagnosis of which problems you're equipped to solve.*

**The nine-day audit** (diagnosis before surgery, fits one sprint): map the eleven components (what exists / where / "missing") → read 50 production traces (tally the failure signatures) → interview the staff engineer + on-call ("what do you quietly work around?") → catalog tools + MCP servers + agent-identity → find the eval gap (where production failures and eval coverage don't overlap = eval debt) → write the maturity diagnosis paragraph → write four tickets → **evals onboarding day** (the day most teams skip and regret: stand up trace storage, author 5 evals, wire one to CI, calibrate the judge to >90% agreement on a 50-case sample) → **open-harness audit** (score each cluster portable / partial / locked-in; a harness locked-in on 3+ clusters isn't yours). The single metric to watch: **drift-recovery rate** (fraction of errored sessions that return to a valid output with no human) — the closest number to "how reliable is my harness"; expect 30–50% before the patterns, 70–80% after, and *held there* as you add features.

**The stakeholder scripts** — one investment, four translations: to **Engineering** ("we're reducing the surface area of random failures"), to **Design** ("the harness is how users get consistent behavior — what your research calls trust"), to the **Exec team** ("every dollar into the harness buys the *option* to raise autonomy next year without a rewrite"), to **Security/Compliance** ("the harness is your audit trail — every interception hook is an audit entry, every trace a compliance artifact"). The words matter; the same plan freezes or ships depending on which room you're translating for. *(This is the Bridger discipline; the full translation craft is `stakeholder-communications`.)*

## THE ORG — Rebuilding Around the Harness

### Four org models (pick one deliberately; the shape decides what you can ship)

| Model | Thesis | Best-fit | Failure mode |
|---|---|---|---|
| **Harness-as-Platform** | Central team owns orchestrator/evals/registry; product teams build thin logic on top. | 12+ product teams sharing infra. | The queue → shadow harnesses in product repos; you pay platform cost *and* the duplication. |
| **Harness-as-Feature** | Each product team owns its slim harness; no central layer. | 2–8 teams, diverse workflows, early. | Drift — six teams, six retry strategies; learning doesn't propagate. Extract a thin platform when >30% of eng time goes to harness maintenance. |
| **Harness-as-Operating-Model** | The harness *is* the product; PMs write harness specs, evals are the system of record. | AI-native, <500 people, one dominant workflow. | Culture debt; near-impossible to retrofit onto an incumbent — the transformation-office illusion. |
| **Harness-as-Deployment** | A Forward-Deployed Engineer maintains a customer-specific harness inside the customer. | Vendors of vertical agents; regulated buyers. | Customer atrophy; harness authority migrates out of the buyer. |

**MDASH vs FDE — know which you are.** *Are you buying AI or selling it?* If **buying** (banks, retailers, hospitals — most of the Global 2000), your problem is MDASH: your own employees use agents, so name a harness owner, register every agent, contain tool calls, DLP outputs, route across vendors. FDE is then just a *procurement* question you ask your vendor. If **selling** (Palantir, Harvey, Sierra, the labs), FDE is your *delivery model* — a named track with a rotation policy so customers can't poach the engineer. The failure mode: a Fortune 500 CEO reads a Palantir case study, stands up an internal "FDE team," and staffs MDASH work with the wrong people, the wrong metric, and the wrong reporting line. Name what you are first.

### The Harness PM — the role that didn't exist 18 months ago

Owns the harness *product*: its failure modes, eval suite, cost envelope, tool catalog, escalation surface, and — critically — the **autonomy envelope** (every request to widen what the agent may do lands here; they say yes based on whether the harness has the verification, rollback, and escalation to *contain* the new surface, not on what the model *can* do). Differs from an ML PM (who owns model selection/benchmarks — a line item here) and a platform PM (measured on adoption; the Harness PM is measured on *production reliability*). Sits at the intersection of reliability engineering, product, and applied AI. *A Harness PM who can't state their current eval-coverage %, top three uncovered failure modes, and last five closed eval cases isn't yet operating at the level the role demands.*

### Human-in-the-loop → human-in-the-harness

"Human in the loop" implies a synchronous gate; it works at a few actions/day, breaks at 10, fails at 100, and is a fiction at 1,000. **Human-in-the-harness:** the human is a *component the harness routes to* — the review queue, the escalation path, the feedback channel — engaged when confidence/anomaly/policy triggers say so, not on every action. Human attention becomes a resource the harness *allocates*, like tokens or retries. The operating tell: *what is your human-review throughput?* If the answer is a queue length, a latency, and an SLA, you're running human-in-the-harness; if it's "someone looks at most things," you're still in human-in-the-loop and will eventually either stop looking or stop scaling. This is more precisely safe, not less — but it lands differently in a board review than a product retro, and landing it in both rooms is the Harness PM's translation job.

### The build/buy boundary + the Assembler pattern

**Keep in-house (compounds for you):** harness design discipline, eval philosophy & quality rubric, domain failure-mode taxonomy, org-specific workflow logic, autonomy-envelope decisions, escalation routing. **Outsource (commodity):** observability/trace plumbing, model providers, base retrieval/RAG libraries, standard scaffolds, cost dashboards, generic tool libraries. The one-line test: *if a role can be written as a short spec, outsource it; if it requires domain-specific judgment every week, keep it.* The **Assembler pattern** scales the function past ~10 workflows: one PM + one engineer maintain a library of harness *primitives* (Identity templates, Memory modules, Orchestration patterns, Interception stacks, Obs/Evals infra); new workflows compose a harness in days. The trap: the library starts owning workflow logic and becomes Model One in disguise — the Assembler owns primitives, workflow teams own composition.

### The execution-environment decision — managed ≠ accountable

"Agent platform" bundles four separable layers, and the build/buy call is made *per layer*: **model service** (inference), **agent runtime** (the loop, sessions, retries, persistence), **execution environment** (filesystem, shell, sandbox, resource isolation), and **business environment** (internal systems, production data, identities, approvals, financial limits). A vendor can run the first three; **the business environment is always yours**. That yields four deployment shapes:

- **A — Vendor-managed** (model + runtime + sandbox operated by the vendor, e.g. a managed-agents product): fastest to production; the vendor runs the room.
- **B — Hybrid** (vendor runs the model + runtime; the *sandbox and tool execution run in your infrastructure*): data-local execution, but note — execution locality is *not* data invisibility (tool arguments and results still flow to the vendor's control plane so the model can keep reasoning).
- **C — Composed** (runtime from one platform, sandbox from that or another provider): maximum flexibility, but *you* own verifying no gap exists between orchestration, isolation, access, and approval.
- **D — Customer-managed** (you operate everything): maximum control and residency fit, highest engineering/security burden — and self-hosting a "sandbox" that's really a container with an open network and inherited credentials is false confidence.

Three lines govern the choice: **managed infrastructure is not managed accountability** (a vendor can operate the computer; it cannot decide which consequences your org should permit — your refund limits, consent rules, change-freeze policy stay yours); **orchestration is not isolation** (a durable runtime survives failures; a sandbox stops damage — different problems, often both needed); and **a sandbox is not safety** (it may isolate files while exposing network, credentials, data, or irreversible external APIs). So: **choose the boundary before the vendor** — decide where files, processes, credentials, tool results, session state, and logs are *allowed to exist*, then pick the configuration that satisfies it. And choose by **consequence, not org size**: low-consequence knowledge work → managed cloud is fine; production mutation (money, records, deploys, external comms) → the execution environment alone is insufficient (needs tool-boundary policy, task-scoped credentials, approval thresholds, independent verification, recovery); regulated/high-sensitivity → hybrid or self-hosted, analyzed boundary by boundary. Write an explicit **shared-responsibility matrix** — most environment failures happen because both parties assumed the other owned the control. *(The per-tool contract that enforces the business-environment boundary is `tool-architecture`; the sandbox/blast-radius containment is `safety-by-design` / `agent-risk`. Source: Ravi's Harness "Environment Is the Product Boundary" bonus.)*

The line that ties it to this skill's spine: **buy the commodity, design the consequence.** Sandbox provisioning, session queues, and runtime recovery are becoming platform capabilities you can reasonably rent — but authority, approval, blast-radius budgets, and recovery from *business* harm are organization-specific and cannot be outsourced by selecting a managed product.

### Open vs closed is the *first* org decision

Before the org models, before the Harness PM: *for this workflow, are we rebuilding around a harness we own or one we rent?* If "rent," the org models are irrelevant — the Harness PM becomes a vendor-relationship manager, the flywheel becomes "file a feature request." Fine for the 60%; catastrophic for the 40%. June 2026 supplied four proof points to carry into any vendor review: buy the identity/containment floor (Claude Tag) and build above it; the lab may ship *your* vertical (Claude Science) so differentiate on what it can't see — your workflows, ground truth, compliance surface; never rent the eval layer (OpenAI retired hosted Evals with ~6 months' notice — the vendor didn't raise the price, it deleted the shelf); and model-portability became a *continuity* requirement the week Fable 5 was suspended for 19 days with zero notice.

## LONGEVITY — What Survives the Model, and the Meta-Skill

### The dissolving ladder (two destinations)

Capabilities migrate off your harness in one of two directions, and they price differently. **Destination A — Model absorption** (a *gift*: you delete code, keep your architecture; structured output, tool-calling, long-context RAG, multi-step reasoning, generic safety have already crossed). **Destination B — Vendor-harness absorption** (a *trade*: you shed engineering cost and take on vendor coupling in the same motion; parallel fan-out didn't become an API parameter, it became dynamic workflows inside Claude Code, on the vendor's pricing/availability/roadmap). Every dissolving capability also drags a *quieter* capability out with it — the JSON validator guarded semantic drift; the ReAct trace was your explainability artifact; RAG enforced freshness/governance. Find that residue and put it somewhere permanent.

### The five permanent residents (invest here relentlessly)

No model absorbs these because they depend on information, incentives, or obligations the model structurally cannot have: **(1) domain-specific evals & ground truth** (your product's opinion of "good" — outsource it and you have a wrapper, not a product); **(2) org-specific workflows** (your approval hierarchy, your 2017 ERP↔CRM bridge); **(3) observability & audit** (a stateful, tamper-evident, court-defensible record — the model is a stateless transformation); **(4) cost controls** (the harness is *adversarial to the model on spend* — spending more is the model's revenue; correct, forever); **(5) user-specific context & memory** (privacy-scoped per-user state a general model cannot legally carry). *(Candidate sixth, written in 19 days of Fable-5 downtime: model-availability insurance — routing policy + capability-degradation map + fallback evals that let the product survive a dark model.)*

### The meta-skill — four questions that predict what dissolves by 2027

For any capability in your harness: **(1) Is it generic or org-specific?** **(2) Does it benefit from scale?** **(3) Does the frontier lab have economic pressure to absorb it?** — and the 2026 fourth question: **(4) Has it entered the self-improving tier** (can the harness evaluate and improve it autonomously — worker/evaluator/evolution loops)? Three yeses on 1–3 → it dissolves, plan accordingly (build cheap, don't architect a team around it). Two or fewer → it stays, invest seriously. A yes on 4 → your job shifts from *authoring* to *supervising* (you set the rubric the evolution agent optimizes against, and you audit the audit trail). The third question is the one most-often gotten wrong: *the question is not what feels generic — it's what the labs will make money on generalizing.*

### The moat, and why the eval suite is the last line

*The eval suite is the skeleton of the moat; the flywheel is the moat itself.* A static eval suite a patient competitor can approximate; a flywheel wired from *your* production traces to *your* evals to *your* harness edits runs on data nobody else has (LangChain moved a coding agent rank 30 → top-5, +13.7pp, with no model change, on harness edits the flywheel proposed). The blind spot: proprietary evals can't be benchmarked against peers, so self-assessed quality drifts — keep a 50–100-item **calibration subset**, de-sensitized enough to run against public benchmarks, or you inherit the BloombergGPT-style surprise two years later. And the final bet, as vendor fine-tuning pipelines start absorbing workflows, audit, cost, and context: *a vendor can absorb the behavior; they cannot absorb the arbiter of whether the behavior is right.* Organizations that keep rigorous evals always have something worth protecting; those that let evals decay have already handed over the moat and just haven't been sent the invoice.

**The transferable instincts** (the patterns expire; these compound): probabilistic systems need deterministic wrappers; trust is engineered, not assumed; economics and reliability are the same problem (the invoice and the incident are two views of one phenomenon); the gap between demo and production is a first-class design concern. *The one line for your next planning meeting: the model reasons, but the harness decides what that reasoning is allowed to touch — still true in Q4 2027, whichever layer owns the primitive by then.*

## WHERE THIS SKILL ENDS — the boundary, and the siblings it routes to

This skill is the **program** — the money, the org, the years. It routes to:

- **The machine itself → `agent-harness`** (the sibling): MHTE, the five clusters, the Anatomy Atlas, failure signatures, the four shippable patterns, the paradoxes. *That skill decides what to build and how to diagnose it; this one decides how to fund, staff, and future-proof it.*
- **Deep unit economics at 10× → `cost-model` / `token-economics`**; **build-now vs wait-for-the-model on a specific capability → `capability-tracking`**.
- **Rolling the harness out to an org → `adoption-launch`**; **whether the org is structurally ready → `alignment-check`**; **the four stakeholder translations in depth → `stakeholder-communications`**.
- **Safety as competitive defensibility → `safety-as-moat`**; **where the durable advantage sits across the stack → `moat-finder`**.

The spine: **the machine wins the sprint; this program wins the eighteen months.** A harness with no named owner, no cost shape, and no permanent-residents list is a science project that will be wound down when reliability never arrives — no matter how good the machine is.

## DIAGNOSTIC QUESTIONS

1. What *phase* is your program in — front-loaded, plateau, or compounding — and are you narrating the CFO accordingly? (Naming it wrong is how programs die on the plateau.)
2. Rank your five cost centers against your actual line items. Which are you under-budgeting (usually evals + human review) and over-budgeting (usually tokens)?
3. Which rung of the maturity ladder are you on, by evidence — and is your team acting like a higher rung than the evidence supports?
4. Who is the *named* Harness owner with authority to modify prompts, gate hooks, approve skills, and sign eval scorecards? If it's "whoever's interested in AI," that's the gap.
5. For each workflow: open or closed, and is that the right call for *Year 3*? (Misclassification is a migration bill nobody underwrote.)
6. Can you name your five permanent residents and, for every other meaningful component, its retire-by trigger? (If not, half your roadmap has an unpriced timer.)
7. Which of the three break-even signs have you seen, and which are you still waiting for?
8. Is your eval suite a static artifact or a living flywheel wired from production traces — and do you keep a calibration subset so self-assessment doesn't drift?

## QUALITY GATE

- [ ] The program's cost shape is named (front-load / plateau / compound) with a Year-2 reframe ready before the budget meeting.
- [ ] All five cost centers are budgeted, with tokens correctly ranked (usually fifth) and a runtime line included.
- [ ] The team's maturity rung is diagnosed from evidence, with the next-rung move named.
- [ ] A single Harness owner is named, with authority and a career ladder — not enthusiasm.
- [ ] Every workflow is classified open vs closed, deliberately, with the Year-3 cost of being wrong acknowledged.
- [ ] "Human in the harness" is real: human review has a throughput, latency, and SLA (not "someone looks at most things").
- [ ] The five permanent residents are written down; every other component carries a retire-by trigger (the meta-skill four questions run each quarter).
- [ ] The eval suite is a flywheel (traces → evals → edits), with a shareable calibration subset guarding against self-assessment drift.

## WHEN WRONG

This skill over-applies when the workflow is genuinely commodity (the 60%): internal productivity, non-differentiating CX, or a low-stakes agent where the harness is not your advantage — run those on a closed stack with a small procurement-oriented team, and do *not* stand up a Harness PM, an open-harness program, or a permanent-residents review for them. It also mis-fires if used to *delay*: the maturity ladder and the nine-day kit are diagnostic, not a gate to hide behind while not shipping. And be honest about the evidence tier — the cost multiples, the $191 delta, the 3–5× front-load, and the failure-share percentages are practitioner-reported field patterns (⚠), not audited universals; use them to shape the argument and the budget, then measure your own numbers against your own baseline.

---

## TRADE-OFF LEDGER

Complete the Trade-Off Ledger from the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 3.

## CONCLUSION

Follow the Conclusion Protocol from the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 5: state the recommendation, name the key trade-off, acknowledge the biggest risk, define the next action.

---

## VISUAL SUMMARY

After completing the primary output, invoke the **excalidraw-svg** skill to create a single Excalidraw SVG visual summary — ideally the three-year cost curve crossing the compounding-return curve at break-even, or the permanent-residents vs dissolving-ladder split. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.
