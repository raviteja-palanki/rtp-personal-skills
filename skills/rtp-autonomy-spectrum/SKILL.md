---
name: rtp-autonomy-spectrum
version: v1.8.1_latest
description: 'Choose how much an AI system may decide and do for each interaction. Use when designing an AI feature, evaluating an agent, changing execution rights, or checking whether human oversight works as intended. Keep the shared seven labels: Feature, Chatbot, Assistant, Copilot, Agent, Autonomous Agent, and Multi-Agent. Pair the label with actual planning rights, action permissions, scope, duration, oversight, and accountability; multiple agents do not automatically have greater authority. Compare designed and observed behavior, assess consequences and task-specific performance, choose a supervision mode, and define escalation and recovery. Produce a per-interaction map with the current arrangement, recommendation, evidence, and open decisions. Covers progressive trust, permission granularity, meaningful review, dissent, and preserving human practice. Pairs with ai-use-case-readiness, trust-ladder, agent-spec, agent-risk, tool-architecture, agent-harness, and judgment-guard.'
imports:
  - determinism-compass
  - tool-architecture
  - agent-risk
  - judgment-guard
---

# Autonomy Spectrum

Choose the authority that lets an interaction deliver useful work with acceptable consequences. Consider demonstrated capability, human effort, cost, uncertainty, and recovery together. Greater autonomy is neither the goal nor automatically more dangerous; less autonomy can also create delay, review overload, or preventable human error.

Start with the action contract: **who chooses the next step, who may execute it, within what scope, and who can intervene?** The first question distinguishes a fixed workflow from model-directed planning. The full set establishes practical autonomy.

Use the seven labels below to communicate, then state the actual rights. This is the RTP library's shared taxonomy, not an industry standard, a risk score, or a universal ranking. Level 7 describes multiple agents and can coexist with tightly restricted authority. A non-AI solution remains a valid alternative; call it Level 0 when a comparison needs that label.

## 1. Define the interaction before assigning a level

For each meaningful interaction, record:

- **Goal and completion:** what the user needs, what counts as done, and how that is checked.
- **Planning rights:** fixed sequence, human-selected steps, or model-selected plan and tools.
- **Action rights:** read, draft, modify, send, publish, approve, purchase, delete, or other precise verbs.
- **Scope and duration:** authorized people, records, systems, budget, time, and persistence.
- **Oversight:** pre-action approval, sampling, exception handling, or monitoring; who does it and whether they have capacity.
- **Accountability and recovery:** who owns the result, who may stop or override, and what can actually be undone.

Respect authorization already given. Do not turn “human oversight” into repeated permission requests for actions within an agreed scope. Seek a new decision when required authority or consequential information is missing, or when the proposed action exceeds that scope.

## 2. Teach the seven levels through the division of work

| Level | Library label | Typical AI contribution | Typical human contribution |
|:--:|---|---|---|
| **1** | **AI Feature** | Makes a narrow prediction or suggestion within an existing flow. | Uses, edits, or ignores it; the surrounding system controls execution. |
| **2** | **Chatbot** | Handles a bounded dialogue or scripted routing flow, sometimes using a model. | States the need and uses a supported route or escalation. |
| **3** | **AI Assistant** | Responds to a request with information, analysis, or a draft. | Chooses the request and decides what to do with the result. |
| **4** | **Copilot** | Helps within ongoing work, typically proposing actions or changes. | Retains the specified consequential decisions and approvals. |
| **5** | **Agent** | Plans and executes a bounded task using permitted tools. | Sets or accepts the goal and boundaries; reviews results and specified exceptions. |
| **6** | **Autonomous Agent** | Performs sustained or recurring work with broader delegated execution within a defined contract. | Sets that contract and oversees outcomes, exceptions, and changes. |
| **7** | **Multi-Agent System** | Several agents divide or jointly solve work and coordinate results. | Oversees the system and its authority boundaries through accountable owners. |

The same experience can fit more than one label. Autocomplete can be called a feature or part of a copilot; a chat interface can invoke an agent. Label the **interaction's behavior**, not the product name, interface, marketing claim, or model family.

### Everyday examples and failure implications

- **L1, sentence completion:** the user accepts a phrase. That may be low consequence, but predictions used in medical, financial, access, or ranking decisions can be consequential. A narrow feature is not inherently harmless.
- **L2, support routing:** the dialogue offers orders, returns, or shipping. Off-script handling and escalation must be designed; a chatbot does not necessarily detect its own errors or always hand over successfully.
- **L3, email drafting:** the assistant supplies a draft. The user controls sending, but reading it does not guarantee catching invented facts or unsuitable wording.
- **L4, code suggestions:** the person accepts, changes, or rejects proposed code. Plausible code can be approved without meaningful checking, so test the review process as well as the generator.
- **L5, research briefing:** the agent selects searches and sources, then writes a document. Specify data access, evidence expectations, and stopping conditions. A research agent need not have external write authority.
- **L6, coding ticket to pull request:** the system makes authorized edits, runs checks, and opens a reviewable result. This does not automatically authorize merging or deployment. Long duration alone does not establish broader rights.
- **L7, claims workflow:** specialist agents extract evidence, check policy, assess the case, and draft a reply. One accountable owner or supervisor can still own the complete outcome; define who may decide or send anything.

In a hypothetical chain of 20 independent steps, each with a 95% success probability and no recovery, all-step success is `0.95^20 ≈ 35.8%`. Actual workflows can have dependent errors, recovery, and steps that are not all critical. Measure the end-to-end result rather than treating this calculation as an agent failure forecast.

## 3. Understand the planning boundary around Levels 4 and 5

Moving from suggestions or predefined flows to model-selected steps often changes the architecture. The system must manage plans, tool choice, intermediate state, budgets, and recovery. Inspect those obligations when crossing the boundary.

| Concern | Fixed or human-directed workflow | Model-directed workflow |
|---|---|---|
| Sequence | Predetermined or selected by the person. | Selected dynamically within allowed boundaries. |
| Validation | Check inputs, predictions, and resulting actions. | Also check intermediate choices, state, continuation, and stopping. |
| Failures | Can be silent, consequential, or cascading. | Can add planning, tool-selection, and long-run coordination failures. |
| Cost | Depends on workload and implementation. | May add calls and monitoring; can also reduce work or use cheaper paths. |
| Authority | Can already include consequential automated actions. | Must be granted and enforced explicitly; planning alone grants no rights. |

A fixed rules engine can send money without human approval. A model can plan entirely inside a read-only sandbox. These are why workflow control, action authority, and risk must be stated separately. There is no universal tenfold cost jump at L4→5, and the lower levels do not guarantee immediate visible failure.

The stakeholder analogy is a colleague working to an agreed brief and authority limits. Use it to explain delegation, without implying the system has a person's judgment, accountability, or ability to understand every exception.

## 4. Set controls from consequences and available evidence

Assess the action's possible harm, likelihood and uncertainty, affected people, detectability, scale, and reversibility. Include privacy and disclosure in read access. Record risk tolerance by domain: experimentation on an internal draft can have different boundaries from access control or a customer commitment. “Take more risks” is too vague to define an execution policy.

| Action profile | Candidate arrangement to evaluate |
|---|---|
| Low consequence, contained, readily recoverable | Bounded execution with proportionate checks and visibility. |
| Recoverable but meaningful cumulative exposure | Limits on amount and volume; relevant validation, monitoring, and sampled review where sufficient. |
| High consequence, uncertain recovery, or weak detection | Stronger pre-action checks, narrowed scope, qualified approval, or a different workflow. |
| Prohibited or outside authorization | Prevent execution; route to the authorized owner when appropriate. |

Set thresholds for the actual business and affected parties. The source's dollar bands (`<$1`, `$1–100`, `$100–10k`, `>$10k`) and 24-hour audit window are illustrative, not policy. A small action repeated widely can be material. An irreversible action is not automatically forbidden: even sending an authorized routine email is irreversible. It needs an appropriate decision and control contract, not an invented universal ban.

### Verify setup and outcomes

Check goals, permissions, limits, escalation routes, and the evidence behind the design. Also verify consequential outcomes through automated checks, human review, sampling, reconciliation, or other suitable means. A sound setup does not guarantee each result.

If every output needs expert review, include that effort and review quality in the value case. It may still be worthwhile if drafting, analysis, or turnaround improves. If reliable review is unavailable, reduce scope, change the workflow, or decline the deployment. “Verify the setup instead of every output” is a design question, not a universal ceiling or exemption from ongoing oversight.

### Design stopping and recovery before execution

Specify how to prevent new actions, cancel supported in-flight work, revoke access, and reconcile uncertain operations. A kill switch stops what it controls; it may not reverse a completed payment, publication, or downstream action. Use rollback where possible and compensation or incident response where it is not. Test the response within the time harm can develop.

## 5. Choose and revise the supervision mode

“Leash length” is shorthand for the work permitted between human interventions. Use plain language with users.

| Mode | Operating arrangement | Main condition to check |
|---|---|---|
| **Supervised** | A person reviews the specified consequential decisions before execution. | They have evidence, time, expertise, and real authority. |
| **Spot-check** | The system acts within scope; selected results receive later review. | Sampling and detection are sufficient for the consequence and exposure. |
| **Exception-based** | The system executes within limits and routes defined uncertainties or anomalies. | Escalation catches the relevant failures and has an available responder. |
| **Autonomous within scope** | Routine execution proceeds under standing authorization and outcome monitoring. | The scope, controls, and ongoing oversight support the required assurance. |

A workflow can combine modes by action. Progressive trust means using evidence to grant, hold, or reduce rights. It does not require every deployment to pass through every mode, nor require broad authority only for low-cost tasks. Human-only operation and permanent assistance are finished design choices when they best serve the goal.

Define promotion, restriction, and re-evaluation criteria before a change. Use representative task results, severe failures, calibrated uncertainty where available, exposure, drift, review performance, and recovery tests. Do not promote from a clean streak alone or reset an arbitrary number of levels after any error. A severe event may require immediate suspension; a minor error may call for a targeted repair.

A record such as “246 of 247 reviewed cases passed” needs the task set, timeframe, selection method, failure severity, and uncertainty. It does not automatically justify 30 days of exception-based operation. Explain changes in rights clearly and obtain authorization for any expansion not already covered.

Context size is one operating signal. Test freshness, retrieval, instruction retention, and long-run performance on the actual configuration. Do not reduce autonomy at universal 40–60%, 60–80%, or 80% window thresholds; context utilization alone does not establish competence or danger. Route context-policy design to `agent-harness` / `context-spec`.

## 6. Compare designed oversight with observed behavior

Report the **designed arrangement** and **observed arrangement** side by side. A human checkpoint can lose effectiveness through overload, insufficient evidence, persuasion, weak authority, or routine approval. The formal permission still exists; the assurance it was meant to supply may not.

Acceptance rate, edit rate, override rate, and review time are useful signals, not proofs. High acceptance can reflect correct work. Low editing can be appropriate for a binary decision or an already good draft. Check sampled correctness, important errors caught or missed, evidence used, and the reviewer's ability to reject.

Useful probes include:

- Ask whether the code selected the outcome, the person independently decided, or the model proposed a default the person reviewed. A ratifier with meaningful rejection power can exercise judgment; the answer alone does not assign a level.
- Where the task warrants it, compare independent human assessment before exposure to the AI result, separate evidence checks, and a clear drafting/decision split. Evaluate the cost and benefit; no single review pattern works everywhere.
- Preserve reviewer engagement through relevant hands-on work, targeted checks, and context-rich escalation. Skill loss is a risk to assess, not an inevitable consequence of every longer run. See `judgment-guard`.
- Inspect whether constraints are needlessly blocking useful work. In a sandbox or an approved low-risk experiment, varying a **non-safety** limit can reveal sensitivity to that limit. Movement toward a new boundary does not by itself prove good judgment or a lower effective level; the system may simply follow the changed rule. Compare quality, compliance, and outcomes.

Never relax a safety, legal, or authorization boundary merely to measure autonomy. The corpus's medication-reminder 7-to-14-day example is a single reported case, not permission to experiment on patients or regulated controls.

## 7. Make permissions and disagreement understandable

### Grant rights at a useful grain

Separate actions with different consequences: draft versus send; recommend an inventory move versus execute it; read versus create versus delete. Include the recipient, resource, tenant, amount, purpose, and duration when those define the real boundary.

A tool can already expose one precise action, so tool-level permission is not inherently inadequate. The test is whether a person can authorize the useful scope without granting unrelated consequential access. Avoid fragments so small that the user must repeatedly approve routine authorized steps.

### Decide what happens when the AI disagrees

Distinguish **advice**, **a warning requiring acknowledgment**, and **a policy-enforced block**. An assistant may fact-check a person and remain advisory. Expressing disagreement does not create veto rights or automatically make it an autonomous agent.

For consequential disagreements, state who may proceed, whether another sign-off is needed, and which policy controls. Capture the decision and evidence under the relevant record policy. An override is not automatically a mistake, and a model's contrary opinion is not automatically authoritative. Logs may support governance and also carry other obligations; do not present those as mutually exclusive choices.

## 8. Apply the same judgment to a person's work

The source offers a useful four-mode planning lens, not a validated ranking:

| Mode | What to preserve | Example use |
|---|---|---|
| **Leader-owned** | Judgment and accountability. | High-consequence trade-offs or relationship decisions. |
| **Leader-shaped, AI-assisted** | Intended meaning and voice. | Important communication supported by AI structure or drafting. |
| **AI-enabled, human review** | Contact with original signals and effective review. | Repeatable analysis or synthesis at useful scale. |
| **AI-handled, bounded** | Capacity for other work, with accountable execution. | Specific tasks whose consequences and controls support delegation. |

Before selecting bounded delegation, ask whether the task and a good result are clear, whether errors can be detected and corrected, and whether the AI will represent the organization. Also establish reversibility, authority, and an accountable owner. Internal work can be consequential; outward-facing work can sometimes be appropriately delegated.

Routing inbound requests or drafting routine answers may fit bounded work. A key-customer apology often needs the relationship owner's judgment, even if AI helps draft it. Treat these as examples to assess, not permanent bans by document type.

### Preserve capabilities that depend on practice

Some capability develops through making decisions; some also depends on hands-on execution, observation, feedback, and teaching. The ledger calls these **decision-fed** and **exercise-fed** mechanisms. They can overlap.

Identify the skill that must remain available, the practice that sustains it, and how to assess retention and transfer. Automate supporting work when useful while preserving sufficient meaningful practice. Do **not** infer that preserving execution requires automating the decision: diagnosis and execution often develop together. Manual toil without learning value is not automatically worth retaining. Route the learning design to `judgment-guard`.

## 9. Plan change without assuming a smooth ladder or an inevitable jump

Formal work on “automation cliffs” shows how optimal routing can change abruptly under particular assumptions about performance and limited human attention. It is a reason to test thresholds and reviewer capacity, not proof that gradual rollout is wrong. Both staged changes and larger shifts can be appropriate.

When an assistant becomes a more capable execution system, measure **new kinds of work attempted**, successful outcomes, quality, and workload as well as time and cost. More machine activity is not itself more value. Broader access and longer unattended operation are useful dimensions to inspect, but an agent need not span many systems or run for hours.

Capabilities, user behavior, and governance change over time. Re-evaluate the deployment; do not infer its authority from a model announcement. The taxonomy itself can also be improved when its categories stop helping. It is not a permanent scientific law.

Three product design patterns can help:

1. **Make modes and rights visible.** Distinguish suggest, draft, execute, and recurring execution. Progressive introduction may help users; prior assistant use is not mandatory for every new agent user.
2. **Manage model dependencies.** Stable interfaces and representative evals can ease substitution. A provider change still needs validation of quality, tools, permissions, latency, cost, and terms; it is not an automatic upgrade or guaranteed outage fallback.
3. **Check integration depth.** Compare an add-on with a deeper redesign against required data and action access. An add-on can have broad integration, and an AI-centered product can be tightly restricted. Neither architecture determines a fixed autonomy ceiling.

## Deliver a per-interaction map

Use a table as the core output. Include a spectrum graphic or designed/observed comparison with `excalidraw-svg` when it improves understanding; one or several diagrams are optional.

| Interaction | Designed label and rights | Observed behavior and evidence | Recommended contract | Consequence and open decision |
|---|---|---|---|---|
| Returns triage, illustrative | L4; propose refund, person approves. | 96% accepted, <2% edited; review effectiveness is **unknown** until sampled. | Retain rights while checking errors and review quality; evaluate bounded refunds separately. | Define amount, aggregate exposure, owner, and pre-action conditions. |
| Billing dispute | L3; analyze and draft. | Person decides and sends, if confirmed in workflow evidence. | Keep or change based on task results and rights needed. | Resolve required policy and expertise. |
| Document creation | L5; research and write within authorized access. | Verified artifacts and source coverage; observed recovery limits. | Consider sustained delegation where it adds value. | Name the evidence and owner for any added access or duration. |

Use a range where labels overlap and **OPEN: decision needed** where a consequential question remains unresolved. A range does not replace a clear permission boundary. Avoid averaging several interactions into a misleading product-level number.

Before closing, check that the map includes actual authority, evidence and uncertainty, task-specific consequences, meaningful oversight, stop/recovery behavior, and the next decision owner. State the recommendation, main trade-off, largest remaining risk, and next action. Use the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md) proportionately.

For deeper readiness use `ai-use-case-readiness`; for trust changes use `trust-ladder`; for execution design use `agent-spec`, `agent-harness`, and `tool-architecture`; for risk and fixed controls use `agent-risk` and `determinism-compass`. `ai-product-metrics` supports measurement, `trust-under-fog` supports communication, and `harness-operating-model` / `capability-tracking` support program and dependency decisions. Confidence-based routing needs task-specific evaluation rather than untested self-reported percentages.

See [research and case notes](references/research-and-case-notes.md) and the [concept guide](CONCEPT.md) for evidence limits and worked examples.
