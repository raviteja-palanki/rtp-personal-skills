---
name: rtp-breach-ready
version: v1.0.1_latest
description: 'Prepare a system and its people to contain a security incident, maintain essential service where safe, and recover from trusted resources. Review five resilience dimensions: isolation, graceful degradation, manual or independent fallback, communication, and recovery. Use a realistic outage scenario, including a 48-hour exercise when relevant, to test dependencies, staffing, data integrity, backup restoration, and recovery objectives. Pair resilience with prevention; neither guarantees that every incident is avoided or quickly resolved. Use for sensitive-data systems, services with material downtime consequences, continuity planning, and post-incident reviews. Scale the effort for low-impact experiments while checking their access and dependencies. Triggers include "breach readiness", "ransomware recovery", "business continuity", "manual fallback", "backup restore", and "what if our systems go down".'
imports: [stress-test, failure-modes]
---

# Breach Ready

Design for containment, safe continuity, and trusted recovery alongside prevention. The practical question is: **if an important system or dependency becomes unavailable or untrustworthy, what essential work can continue, for how long, and how will we restore it?**

Do not promise that every organization will be breached or that resilience guarantees a rapid recovery. Prevention can reduce incident likelihood and impact; preparation addresses the failures that remain. Both are part of security risk management.

## Start with the service and failure scenario

Identify the data, essential service, affected people, dependencies, cost and harm of interruption, and applicable obligations. Reuse known context. A brief audit can follow the six diagnostic questions; a full review runs the six process steps and produces a continuity/recovery plan.

Scale effort to consequences, not whether a system is called “internal.” An experiment with privileged credentials or sensitive data can create a wider incident. Conversely, a disposable isolated system may reasonably have a minimal recovery plan.

For an active incident, work within the established incident command and authorized scope. Prioritize containment, evidence preservation, and safety. A planning task does not authorize shutting down live systems, sending customer messages, or running disruptive exercises. The shared Universal Skill Protocol is at the AI-PM library root or packaged plugin root; adapt format and depth to the requested decision.

## Five resilience dimensions

| Dimension | What the design should establish | Typical gap |
|---|---|---|
| Isolation | A compromise has enforceable limits across systems, identities, data, and suppliers. | Separate servers share credentials or an administration path that defeats the boundary. |
| Degradation | A defined minimum service can continue safely, or the system can stop safely. | One optional dependency disables the essential service. |
| Manual/independent fallback | People or an independent service can perform the necessary work with available resources. | The fallback depends on the same unavailable database, identity service, or network. |
| Communication | Staff, customers, and partners can receive accurate, authorized updates. | The only contact channel is compromised or requires the failed login system. |
| Recovery | Trusted systems and data can be restored, validated, and reconciled in the required order. | A backup exists but cannot restore a usable, clean service. |

## What the FedEx/TNT case actually supports

The original skill described a complete 48-hour FedEx recovery from the 2017 NotPetya incident, attributed to an isolated mainframe and a rehearsed paper process. That account is not supported by the company's disclosures.

FedEx's **17 July 2017** update said TNT continued to face widespread service and invoicing delays, with manual processes supporting substantial operations and no estimate for full restoration. Other FedEx companies were reported unaffected, and contingency plans used both networks. This supports examining boundaries and continuity arrangements; it does not establish the claimed mainframe architecture or a two-day recovery. The [source note](references/continuity-cases-and-calculations.md) preserves the correction and dated financial context.

## The six-step process

### 1. Test an interruption that matters

Use the **48-hour test** as a scenario prompt, not a universal survival requirement: “If these specified systems became unavailable or unsafe to trust, could we sustain essential work for 48 hours?” Choose a different duration when the service's consequences require it.

State exactly what fails: the AI provider, application, identity service, payment processor, communications, cloud region, power, or several connected dependencies. Distinguish an outage from compromise or corrupted data. If the exercise removes all digital systems, email, phones, SMS, and cloud backups may not be available either; do not quietly depend on them.

Check whether the organization can:

- Receive and prioritize orders, requests, or urgent cases.
- Fulfill essential commitments with a safe minimum service.
- Identify current customers, entitlements, work in progress, and affected obligations.
- Communicate, staff operations, and meet time-sensitive payroll or other commitments.

For a SaaS service, delayed signup or a temporary pause may be better than improvising payment collection. Use only approved payment procedures; do not write down card details as a generic workaround. If the API is unavailable, define which service can continue and which cannot. A current, securely accessible customer list may help but must have a purpose and appropriate handling.

For a healthcare service, ask whether authorized staff can use current downtime records, receive results, and coordinate medication processes under established clinical procedures. Do not invent a fax, PDF, or telephone workflow without confirming its safety, acceptance, and dependencies.

Record the first failure, time until impact becomes unacceptable, fallback capacity, and what must be restored. Acknowledging that some work must pause is a useful result, not an automatic failure of the exercise.

### 2. Map and verify isolation

Draw actual trust boundaries, access, data flows, administrative paths, and dependencies. A firewall or separate database label is not evidence of an effective boundary.

| Boundary | Questions to test |
|---|---|
| Network | Can a compromised endpoint reach critical services or their control plane? Are permitted paths necessary and enforced? |
| Data | Are sensitive stores separately authorized, and can shared backups, credentials, or integrations bypass that separation? |
| Human/identity | Do roles, delegated agents, and administrators have task-appropriate privileges? Can compromised credentials cross boundaries? |
| Infrastructure | Are batch and interactive services, cloud/on-premises environments, and recovery resources sufficiently separated for the scenario? |
| Supplier | What can a compromised model provider, library, integration, or support account reach? Are incoming results treated as untrusted data? |

For an ML service, examine whether the endpoint can modify databases, whether model/API access exposes training or customer data, and what privileges a compromised dependency could obtain. Test through an authorized security process. Separate agent instructions from externally retrieved content, and constrain tool effects through enforceable controls.

Keep a protected copy of the dependency and recovery map accessible during the assumed outage. Check shared identity, DNS, keys, storage, observability, and backup administration; these can connect apparently isolated components.

### 3. Define safe degradation

For each critical service, specify full function, minimum acceptable function, temporary restrictions, stop conditions, and the return-to-normal criteria. Degraded operation can mean lower capacity, read-only access, selected features disabled, or a controlled pause.

**Support example:** if AI normally handles 90% of tickets and people handle 10%, sending all tickets to the same human team creates roughly ten times its prior ticket volume, before differences in case complexity. “Humans handle everything” is not a capacity plan. Define priority routing, queue limits, expected wait, staffing, alternatives, and customer commitments.

Static recommendations or previously approved content may substitute for a model. Confirm freshness, permissions, accessibility, and suitability. A compromised retrieval store may make cached or default output unsafe too. Prefer an honest unavailable state when no acceptable fallback exists.

### 4. Make fallback executable and sustainable

Describe who performs each essential step, with which information, tools, authorization, and staffing. Measure throughput, error checks, backlog growth, shift coverage, fatigue, and the maximum sustainable duration. “Manual” describes who performs work; it does not necessarily mean no digital dependency.

Examples include approved invoice deferral or alternate payment handling, bounded manual stock checks and order intake, or rules-based recommendations. Each depends on the scenario. Email invoicing is an alternative only if email, customer identity, records, and fraud controls remain trustworthy. Inventory workarounds need a method to prevent duplicate sales and commitments.

Keep forms, instructions, contact information, necessary records, and emergency access appropriately protected and reachable. Record work done during the outage with unique references so it can later be reconciled without duplicate charges, shipments, or messages. A slower process can be successful if it meets the defined minimum service safely.

### 5. Establish dependable communication

Identify the incident lead, authorized spokesperson, internal response channel, customer channel, and relevant partner contacts. Prepare concise templates that distinguish confirmed facts, unknowns, affected services, protective actions, and the next update time.

Possible alternatives include published phone numbers, a separately operated status page, an approved SMS channel, and established social accounts. Test their real independence: a different domain may share the same identity provider, hosting, DNS account, or administrator. A phone channel also needs staffing and sufficient capacity.

Keep contact lists current and protected. Authenticate urgent instructions so an attacker cannot easily impersonate the response team. Do not claim that data leaked—or that it did not—before the evidence supports that statement. Use current legal, contractual, and organizational requirements to determine notifications and timing with the responsible owner.

During a planning exercise, draft messages and test delivery through an agreed test group or environment. Send actual customer or public communications only within explicit authorization. Do not assume every incident requires an SMS to every customer.

### 6. Restore a trusted service and reconcile the work

Define three linked properties:

- **Backup integrity:** the required data, configuration, software, keys, and dependencies can be accessed and restored from a trusted point.
- **Recovery time objective (RTO):** the target time to restore a defined service level. Distinguish this target from measured recovery time and complete business normalization.
- **Recovery point objective (RPO):** the tolerated loss of recent data, expressed as a time or other agreed measure. Backup frequency alone does not prove the RPO is met.

Hourly backups may support an approximately one-hour recovery point only when the relevant backups succeed, remain intact, are accessible, and are sufficiently clean. Late discovery of corruption, failed jobs, replication of bad data, or missing dependencies can require an older point or cause greater loss. A live replica is not automatically an independent clean backup.

Use protected recovery resources—such as offline or suitably isolated/immutable backups—appropriate to the threat and obligations. Verify encryption and key recovery, identity separation, retention, and restoration. Rebuild or restore into a trusted environment, address the compromise path and affected credentials as needed, and validate service/data integrity before reconnecting. Coordinate these actions with the incident team; preserve necessary evidence.

Prioritize **safety and essential service**, then dependencies and other business functions. Revenue is one input, not always the first priority. The historical two/eight/twenty-four-hour recovery tiers are examples, not universal targets. A two-hour RTO does not inherently require hot replication, and hourly backups alone do not establish an eight-hour restore time.

After systems return, reconcile offline work, queues, payments, inventory, customer records, and agent actions. Restore the relevant model/prompt/tool configuration and check for poisoned context or persisted memory where applicable. Track residual backlog and customer impact. Availability recovery does not reverse data disclosure or complete incident remediation.

## Exercise the plan and record evidence

Start with a tabletop discussion where appropriate, then test the important assumptions through bounded restores, failovers, access checks, and operational rehearsals. A tabletop can reveal missing decisions; it cannot demonstrate restoration speed. Choose safe production-representative conditions and authorized scope for disruptive tests.

Record scenario, date, participants, expected service, actual result, restoration point, duration, data loss, staffing, failures, owner, and corrective action. Test on a cadence justified by risk and change frequency, and after changes that could invalidate the plan. Monthly backup tests, quarterly drills, and annual recovery reviews are possible schedules, not mutually compatible proof requirements or universal minimums.

Keep the plan usable if normal systems fail. Review vendor changes, emergency contacts, access, dependencies, and employee familiarity. One successful rehearsal does not prove all incident scenarios are covered.

## Six diagnostic questions

1. Under the defined outage or compromise, what essential work can continue, for how long, and what fails first?
2. Which identities or connections could carry compromise across a boundary we rely on?
3. What did the latest restore test recover, from which point, in how much time, and with what gaps?
4. Can the fallback meet minimum service with available people and trustworthy information through the required duration?
5. How will staff and customers receive authenticated updates if the primary channel is unavailable?
6. What are the direct and indirect consequences of interruption, corruption, or disclosure, and which investment reduces them most?

“It depends” is a cue to name the dependency. Low publicity or absence of a specific regulation does not make operational or personal harm immaterial.

## Cost the trade-off and decide

Estimate prevention, isolation, backup, alternate-service, exercise, staffing, and recovery costs against credible loss scenarios and alternatives. Separate revenue delayed from revenue lost, include customer and safety consequences, and avoid counting the same loss twice.

There is no general 2–3× infrastructure multiplier or 10–100× return. In the original example, $10 million potentially avoided against $1 million one-time cost is a 10:1 gross benefit/cost ratio; if the entire loss is actually avoided, net ROI is 900% before other costs. A recurring $1 million annual cost over ten years is a different comparison. Neither establishes expected ROI without incident likelihood, control effectiveness, timing, and residual loss.

Where the risk is low, a simple documented restore or safe shutdown can be proportionate. Accept remaining risk explicitly through the accountable owner within applicable obligations. Comparing backup cost only with the purchase price of a system misses the value and harm of its data and service.

## Readiness and output

Confirm the relevant seven areas: a realistic continuity scenario, verified boundaries, a demonstrated restore, an executable fallback or safe pause, dependable communication, prioritized recovery objectives, and a current exercised response plan. State what was designed, tested, or merely assumed. If evidence is incomplete, recommend a bounded next test or restriction rather than reporting readiness as proven.

```markdown
# Breach Readiness: [Service]
Decision: [ready within bounds / improve / test / accept specified risk]
Scenario and consequences: [failed/untrusted systems, duration, affected work]
Essential service: [minimum capacity, safety limits, maximum interruption]
Isolation: [boundaries, shared dependencies, verification]
Degradation/fallback: [steps, staffing, capacity, stop conditions]
Communication: [owners, independent channels, authorized draft/process]
Recovery: [priority, RTO, RPO, trusted source, keys/dependencies]
Reconciliation: [offline work, external effects, backlog, residual harm]
Exercise evidence: [date, scope, measured results, limitations]
Cost and accepted risk: [alternatives, accountable owner]
Next action: [owner, bounded test/fix, success condition, review trigger]
```

Use `stress-test` and `failure-modes` to challenge dependencies and scenarios; connect agent containment to `agent-risk` and detection to `production-observability`. Hand off the plan when part of a wider continuity or response workflow. Explore unresolved recovery assumptions, invest where protection matters, and reduce or accept residual exposure when justified. The sequence has no mandatory one-quarter schedule.

Close with the recommendation, trade-off, main untested assumption, and next action. A diagram can clarify dependencies, fallback steps, or the measured recovery sequence; it should show actual targets rather than importing the example times.
