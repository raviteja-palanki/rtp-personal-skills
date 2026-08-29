---
name: rtp-user-stories
version: v1.0_latest
description: 'Write sprint-ready backlog items for AI and non-AI systems the way a senior principal product owner does at enterprise scale. Owns the story craft ai-prd deliberately doesn''t: typing the work honestly (user story vs. technical enabler vs. time-boxed spike), INVEST applied with judgment, acceptance criteria written the way a world-class QE thinks (happy path, negative, boundary, non-functional, with every criterion binary pass/fail), High/Medium/Low effort labels that map to story points without estimation theater, and vertical slicing. AI stories *inherit* the probabilistic block (thresholds, behavior examples, failure owner, drift trigger, cost) from ai-prd, never recomputed here. Use when: grooming a backlog, breaking a PRD into stories, a story keeps bouncing back from QA, or estimation debates outlast the work. Pairs with: ai-prd (the upstream spec), eval-framework (AI acceptance criteria become eval cases). Triggers: ''user story'', ''acceptance criteria'', ''tech spike'', ''story points'', ''backlog grooming'
imports:
  - ai-prd
  - determinism-compass
---

# User Stories: The Conversation Contract

## THE ONE IDEA

**A user story is not a requirement written small — it's a contract that lets a builder, a tester, and an owner agree on "done" before work starts.** The template is the cheap part. The craft is in three decisions most teams skip: picking the right *work type* (story, enabler, or spike — mistyping is the root of most grooming fights), writing acceptance criteria the way a QE thinks (what breaks, not just what works), and sizing with honest labels instead of precision theater. The story is the last cheap moment to catch ambiguity — every unasked "what happens when...?" gets asked again later, in production, at 100× the price.

## DEPTH DECISION

**Go deep** if: you're breaking a PRD into a sprint-ready backlog, a story bounced back from QA twice, or your team's AI stories keep shipping deterministic acceptance criteria.

**Skim to Step 4 (QE-grade acceptance criteria)** if: your stories are well-typed and sliced but keep failing in test — the scenario grid alone fixes most of it.

**Skip** if: solo prototyping, pure exploration (write a spike and go), or ops/kanban work where a checklist beats a story.

## THE TRAP

You write stories that pass the template check and fail the sprint. Five failure modes:

1. **Template theater.** "As a user, I want the API refactored so that the API is refactored." The spine is decorative wrapping on a task. If the "so that" doesn't name a user-visible or measurable outcome, it's not a user story — type it honestly as an enabler or a task.
2. **Happy-path acceptance criteria.** ACs describe success only. The negative scenarios — invalid input, downstream outage, permission revoked mid-session, double-submit — get discovered by QA in week 2 or by customers in week 6. A world-class QE reads a story and asks "what breaks?"; a world-class story answers before they ask.
3. **Horizontal slicing.** "Build the database layer," then "build the API," then "build the UI." Three sprints, nothing shippable, integration risk parked at the end where it's most expensive. Slice vertically: every story cuts through all layers and ships something a user (or a monitor) can touch.
4. **Estimation precision theater.** Twenty minutes arguing 5 vs. 8 points on a story full of unknowns. The honest answer was "we don't know" — which is a spike, not a debate. Precision belongs where knowledge is; labels (High/Medium/Low) belong where it isn't yet.
5. **The AI costume.** Deterministic ACs on a probabilistic feature: "the model returns the correct answer." Which confidence band? What happens below it? Who owns the miss? For AI stories, the probabilistic block is *inherited from the AI-PRD*, never improvised in grooming (see Step 5).

## KEY TERMS (plain language)

- **Work type** — the first decision: user story (user-visible value), technical enabler (a capability the next story depends on, with a verifiable outcome), or spike (a time-boxed question whose output is a decision, not code).
- **Acceptance criteria (ACs)** — the binary pass/fail conditions that define done for *this story*. Different from the **Definition of Done** (the team-wide bar: tested, reviewed, instrumented — applies to every story, so don't repeat it in each one).
- **Given / When / Then** — the AC format that forces testability: Given [state], When [action], Then [observable outcome].
- **INVEST** — the six-point health check: Independent, Negotiable, Valuable, Estimable, Small, Testable. Applied with judgment (Step 3), not as dogma.
- **Vertical slice** — a story that cuts through every layer (UI → logic → data) and ships observable value. The opposite of a layer-by-layer plan.
- **Negative scenario** — an AC for what the system does when the input, the user, or a dependency misbehaves.
- **Boundary condition** — the edges: empty, maximum, concurrent, duplicate, expired, first-time, last-one.
- **H/M/L effort labels** — honest sizing buckets that map to story-point ranges once the team's velocity is stable (Step 6). Low ≈ 1–3 points, Medium ≈ 5–8, High ≈ 13+ (which means: split it or spike it).
- **Story inheritance (AI stories)** — the mechanism from `ai-prd`: confidence thresholds, behavior examples, named failure owner, drift trigger, and cost target flow *down* into the story as ACs.

## WHAT THIS SKILL CONSUMES & PRODUCES

**Consumes (upstream inputs):**
- **For AI features: the AI-PRD** — the 13-section document, especially §4 behavior contract, §7 thresholds, §9 owners, §10 event schema, §11 cost — from `ai-prd`. The six AI story types and worked examples live in `ai-prd/references/ai-user-stories.md`; this skill supplies the craft they're written with.
- **For non-AI features: the spec/PRD** — scope, non-goals, success metrics with thresholds.
- **The outcome clause** — what the user is actually hiring this for, from `jtbd-analysis` (feeds every "so that").
- **The determinism map** — which parts are rules vs. model, from `determinism-compass` (decides whether Step 5 applies).
- **Team context** — velocity, Definition of Done, dependency map (feeds Step 6 sizing and Step 3's Independent check).

**Produces (outputs → downstream):**
- **Sprint-ready backlog items** in three honest types — user stories, technical enablers, spikes — each with QE-grade ACs and an H/M/L label → sprint planning.
- **The scenario grid per story** — happy/negative/boundary/non-functional — which for AI stories doubles as **eval cases** → `eval-framework` (every AC is a test; every AI AC is an eval).
- **Spike questions with decision deadlines** — the unknowns extracted out of stories so the stories left behind are estimable.
- **A grooming verdict per item** — ready / send back (with the named gap) / retype.

## THE PROCESS

### Step 1: Type the work before you write it

The most common grooming fight is a mistyped item. Decide the type first:

| Type | It exists because... | Output | "Done" means | Common mistake |
|---|---|---|---|---|
| **User story** | A user gets observable value | Shipped behavior | ACs pass in production-like conditions | Wrapping a task in story language |
| **Technical enabler** | The *next* story is impossible without it | A capability with a verifiable outcome (an API that handles X, a pipeline that processes Y) | The dependent story is unblocked; the capability is demonstrated, not just merged | No verifiable outcome — "refactor the service" with no test for better |
| **Spike (exploration)** | A question blocks estimation or design | **A decision + a written answer**, never production code | The question is answered by the time-box, or escalated | No time-box, no question — "investigate options" that runs three weeks |

**The enabler rule:** an enabler still earns its place through the user story it unblocks — name that story in the enabler's description. An enabler that unblocks nothing is gold-plating.

**The spike rule:** a spike is scoped by a *question* ("Can the vendor API sustain 50 req/s with our payload?" not "look into the vendor API"), time-boxed (1–3 days), and its output is a written decision that re-types or re-sizes the stories waiting on it. Throw the spike code away without guilt — that was the deal.

### Step 2: Write the spine so the "so that" earns its place

```
As a [specific role — never "user"], I want [capability], so that [outcome that traces to the PRD hypothesis or a measurable result].
```

The test: cover the first two clauses and read only the "so that." If it doesn't tell you why this work matters — or you can't write it at all — the item is a task or an enabler wearing a costume. Type it honestly (Step 1) rather than forcing the template. For enablers, an honest spine is fine: "As the payments team, we need idempotent webhook ingestion so that the retry story (#214) can ship without double-charging."

### Step 3: INVEST — applied with judgment, not dogma

Each check earns its place with a why, and a when-it's-wrong:

| Check | Why it matters | When it's wrong (and what to do instead) |
|---|---|---|
| **I**ndependent | Dependencies hide integration risk until sprint's end | Enterprise integration work is often genuinely dependent. Don't fake independence — *declare* the dependency on the card and sequence it |
| **N**egotiable | The story is a conversation starter, not a contract on implementation | Compliance and regulatory ACs are not negotiable. Mark them "fixed — legal" so nobody trades them away in grooming |
| **V**aluable | Kills gold-plating and orphan enablers | Enablers carry indirect value — name the story they unblock, that's their value line |
| **E**stimable | If the team can't size it, it contains a hidden unknown | Don't force an estimate — extract the unknown into a spike and re-estimate after |
| **S**mall | Big stories hide big surprises; feedback loops shrink with size | Some vertical slices have an irreducible core (a schema migration). If splitting destroys the value, keep it whole, label it High, and give it the sprint's first slot |
| **T**estable | An untestable AC is an opinion | If you can't write the Then-clause, the requirement isn't understood yet — that's a conversation with the PM, not a story defect |

### Step 4: Acceptance criteria the way a world-class QE thinks

Happy-path ACs are the entry fee. The craft is the scenario grid — run every story through all five rows, write Given/When/Then for each scenario that applies, and make every criterion binary pass/fail:

| Scenario class | The QE questions | Example Then-clause |
|---|---|---|
| **Positive (happy path)** | Does the core behavior work for the primary segment? For each supported variation? | "Then the approval routes to the cost-center owner within 30s" |
| **Negative** | Invalid input? Unauthorized user? Downstream system down? Permission revoked mid-session? Malformed payload? | "Given the ERP is unreachable, When the user submits, Then the request queues with visible 'pending sync' status — never a silent drop" |
| **Boundary** | Empty state? Maximum (10MB file, 10K rows)? Concurrent edits? Double-submit? Duplicate record? Expired session? First-ever use? | "When the user double-clicks Submit, Then exactly one invoice is created (idempotency key verified)" |
| **Non-functional** | Latency at P95? Accessibility (keyboard, screen reader)? Audit trail? Localization? Data retention? | "Then the audit log records who/what/when, retrievable within 5 min" |
| **State & data variation** | Legacy data formats? Migrated accounts? Feature-flag off? Partial rollout cohort? | "Given an account created before the 2024 migration, Then the legacy address format renders without truncation" |

**Two disciplines:**
- **Every AC is binary.** "Handles errors gracefully" is an opinion; "returns a retryable 503 with a user-visible retry affordance" passes or fails.
- **Don't restate the Definition of Done.** Code review, unit coverage, and instrumentation standards live in the team-wide DoD. The story's ACs are what's *specific to this story*.

The payoff: the grid is where a story earns its enterprise scale. Two stories with identical spines are separated entirely by their negative and boundary rows — that's where the outage, the double-charge, and the audit finding were hiding.

### Step 5: AI stories — inherit, never improvise

If the determinism map says a story touches a model, the probabilistic block comes *down from the AI-PRD* as ACs — confidence thresholds as UI logic, ≥3 linked behavior examples, the named failure owner, the drift trigger, the cost-per-outcome target. The six AI story types (capability, eval, fallback, guardrail, instrumentation, rollout) and the paste-ready template live in `ai-prd` (Phase 3) and its `references/ai-user-stories.md`.

What *this* skill adds on top: run the Step 4 grid against the AI story too, with the AI-flavored rows —

- **Negative:** model timeout, malformed output, hallucination flag fired, safety filter triggered.
- **Boundary:** confidence exactly at a threshold, out-of-scope intent, input at the context-window limit, first request after a prompt version change.
- **Non-functional:** P95 latency per confidence band, cost per request logged, trace ID present.

**The send-back rule (inherited):** an AI story missing thresholds, examples, owner, drift trigger, or cost target is a deterministic story in an AI costume. Send it back to the PRD, not to the engineer.

### Step 6: Size with honest labels, then converge

Size in two passes — labels first, points only when they're cheap:

| Label | Meaning | Point range (stable-velocity teams) | Rule |
|---|---|---|---|
| **Low** | Known pattern, one surface, no new dependency | 1–3 | Batch them; don't debate them |
| **Medium** | Multiple surfaces, or one new pattern, or one external dependency | 5–8 | The default sprint workhorse |
| **High** | New territory, multiple dependencies, or irreducible size | 13+ | **Not sprintable as-is: split it (Step 7) or spike the unknown (Step 1)** |

**Why labels first:** points imply precision the team doesn't have yet on novel work — twenty minutes of 5-vs-8 debate is estimation theater that a label settles in twenty seconds. Convert labels to points only where the team has velocity history on similar work. **The two escalation rules:** any item the team can't label in two minutes contains a hidden unknown → extract a spike. Any High entering a sprint unsplit is a bet, not a plan → the PO signs it explicitly or it splits.

### Step 7: Slice vertically

Split heuristics, in order of preference: by **scenario** (happy path ships first, negative scenarios as fast-follow stories — visible in the backlog, not forgotten), by **segment** (one region/tier first), by **data variation** (new records first, migration second), by **workflow step** (submit before approve before report), and for AI features by **degradation rung** (the >0.85 experience, then the fallback rung, then the refusal UX — each rung is already a story in the ai-prd taxonomy). Never by layer.

## WORKED EXAMPLES (enterprise-grade, one per type)

### Example 1 — User story (non-AI): invoice approval routing

> As a **regional finance approver**, I want invoices above my delegation limit to route automatically to the next approval tier, so that month-end close isn't blocked on manual re-assignment (target: re-assignment tickets −80%).

**ACs (the grid at work):**
- Given an invoice 1¢ above the approver's limit, When it's submitted, Then it routes to the next tier within 60s and the submitter sees the new approver. *(boundary + positive)*
- Given the next-tier approver's delegation expired yesterday, Then routing skips to the following tier and logs the skip reason. *(state variation)*
- Given the org-hierarchy service is down, Then the invoice queues with visible "routing pending" status, retries for 4h, then alerts finance-ops — never silently drops. *(negative)*
- When the same invoice is submitted twice (double-click or API retry), Then exactly one approval workflow exists. *(boundary/idempotency)*
- Then every routing decision writes an audit record (who/what/when/rule-version) retrievable within 5 min. *(non-functional — SOX)*
- Fixed — legal: delegation limits are read from the controlled table; no story-level override. *(N in INVEST, marked non-negotiable)*

**Label: Medium (5–8).** Known workflow engine, one new rule type, one external dependency (org hierarchy).

### Example 2 — Technical enabler: idempotent webhook ingestion

> As the **payments platform team**, we need webhook ingestion to be idempotent under vendor retries, so that story #214 (auto-reconciliation) can ship without double-posting payments.

**Verifiable outcome (what makes it an enabler, not a task):** replaying the vendor's 500-event retry storm from staging produces exactly 500 ledger entries, zero duplicates; a chaos test that kills the consumer mid-batch recovers with no loss and no dupes. Unblocks: #214 (named). **Label: Medium.**

### Example 3 — Spike (exploration): vendor OCR fitness

> **Question:** can the vendor's OCR API sustain 50 req/s on our invoice PDFs (scanned, multi-language) at ≥95% field accuracy — or do we need the self-hosted tier?
> **Time-box:** 2 days. **Output:** a one-page decision (go vendor / go self-hosted / escalate) with the measured accuracy table, and re-labels for the three blocked stories. Code is throwaway by agreement.

### Example 4 — AI story (inheritance + grid): high-confidence draft replies

The full version is Story A1 in `ai-prd/references/ai-user-stories.md` (the Athena example). What this skill adds on grooming day is the grid check on top of the inherited block: confidence exactly 0.85 → which band renders? *(boundary)*; safety filter fires on a legal-threat ticket → no draft, Legal-queue banner *(negative, links REJECT example #1)*; prompt version changed this morning → first request logs new version + regression suite passed *(state variation)*; P95 ≤2s in the >0.85 band *(non-functional)*. Inherited lines verified present: thresholds, ≥3 behavior examples, failure owner M. Chen, drift trigger, $0.031 cost target. **Label: High → split by degradation rung before sprint.**

## QUALITY GATE (binary checklist)

- [ ] Every item typed honestly — user story / enabler / spike — and every enabler names the story it unblocks; every spike has a question + time-box + decision output
- [ ] Every "so that" traces to a measurable outcome or the PRD hypothesis (no decorative spines)
- [ ] Every story ran the 5-row scenario grid; negative and boundary ACs present wherever they apply, all ACs binary pass/fail
- [ ] INVEST applied with the exceptions *declared* (dependencies named, fixed-legal ACs marked), not hidden
- [ ] AI stories carry the full inherited block from ai-prd (thresholds, examples, owner, drift, cost) — send-back enforced
- [ ] Every item labeled H/M/L; no High enters a sprint unsplit without explicit PO sign-off; un-labelable items became spikes
- [ ] Slices are vertical — each story ships something observable

## WHEN WRONG

- **Ops/kanban and incident work** — a checklist and a runbook beat story ceremony.
- **Solo or throwaway prototyping** — the conversation contract has no second party; write the hypothesis and build.
- **Fully spec'd compliance implementations** — when the regulator wrote the acceptance criteria, INVEST's Negotiable is dead and the grid is the regulation itself; use a traceability matrix.
- **Discovery-stage AI work** — before the AI-PRD exists there is nothing to inherit; write spikes against the open questions (§13 of the PRD), not stories against a guess.

---

## GROUNDING, TRADE-OFFS & CONCLUSION

Before starting, follow the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md) Section 1 grounding questions and confirm output format. Close with the Trade-Off Ledger (Section 3) and the Conclusion Protocol (Section 5):

- **Recommendation:** adopt the type-first + scenario-grid discipline for every backlog item, AI and non-AI; adopt H/M/L labels with the two escalation rules.
- **Key trade-off:** grooming gets ~20% slower per story; QA bounce-backs and mid-sprint discoveries drop far more. You're moving cost from week 3 to hour 1.
- **Biggest risk if skipped:** the backlog fills with happy-path stories and mistyped tasks — outages, double-charges, and audit findings hide exactly in the negative and boundary rows nobody wrote.
- **Next action (Monday):** take the top 10 items in your backlog. Re-type them (Step 1), run the grid on the top 3 (Step 4), and count how many AI items carry the inherited block. The gap you find is your grooming agenda this week.

## VISUAL SUMMARY

After the primary output, invoke the **excalidraw-svg** skill for a single "Story Quality Funnel" diagram: raw PRD intent entering at the left → the three type gates (story / enabler / spike) → the scenario grid as a filter grate (happy / negative / boundary / non-functional / state) → H/M/L sizing scales → sprint-ready cards exiting right, with the AI lane showing the inherited block flowing down from the AI-PRD above. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.
