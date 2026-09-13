# Agent Ecosystem — The Coordination Problem

An ecosystem combines agents with shared objectives or dependencies. Its benefit may come from parallel work, specialized tools, context separation, or complementary methods. Its costs include orchestration, latency, state management, verification, and failure recovery.

The relevant distributed-systems questions are familiar: who may change state, how work is delivered, what happens during a partial failure, and how the system knows an action completed. AI adds uncertain interpretation and output, but does not replace these obligations.

## A dependency can hide behind separate agents

Illustration: a pricing agent returns a quote, a recommendation agent uses it, and an order agent completes checkout. If a price changes by 15% after a two-second-old read, the system needs a quote-validity policy and a check at commitment. The age and percentage are examples, not universal stale-data thresholds. A failed or surprising order follows from a missing business rule, not merely from having several agents.

Agents reading the same immutable snapshot can be independent for that task. Shared mutable data, quotas, infrastructure, or external effects may create dependencies even when agents never message one another. Draw those dependencies explicitly.

## Four architectural views

- **Pipeline:** A → B → C. Sequential completion time includes each stage plus communication, queueing, validation, and retries. A failure stops downstream work only if the workflow enforces the dependency. Correctly passing a malformed result can propagate a failure.
- **Broadcast:** A emits an event to several subscribers, such as notification, analytics, and personalization. The subscribers may finish independently. Waiting for all branches takes at least the slowest branch plus relevant overhead; a broadcast need not wait for all. Shared input does not guarantee synchronized processing or state.
- **Shared-state mesh:** several agents interact through a mutable resource. It can support concurrent work, but read/write and business-invariant semantics determine how much coordination is necessary.
- **Orchestrated:** a coordinator owns transitions and progress. A workflow engine such as Temporal can make recovery explicit; durability, replay, and activity semantics must be verified for the chosen implementation. A coordinator is a logical concentration of responsibility, not inevitably one unprotected process.

These views can overlap. The main skill's supervisor, pipeline, fan-out/fan-in, and peer categories describe control flow; this guide also highlights broadcast and shared-state access.

## Five ways to govern state

**Single writer or owning service.** Other components request changes rather than directly editing state. This simplifies coordination but does not make conflicts impossible: concurrent requests, duplicate delivery, restarts, and invalid business commands still need handling.

**Version-checked updates.** Two agents read version 5. One atomic conditional update succeeds and creates version 6; the other's condition fails. The second re-reads and recomputes or escalates. Both must not be allowed to succeed on the same old version for a conflicting change. A retry should not repeat an already completed external action.

**Locks and transactions.** Acquire required locks in a consistent order, for example User before Order before Payment where this order fits the design. Handle timeouts and transaction aborts. The specific order is illustrative; every participant must follow the chosen policy. Long model calls while holding locks can create avoidable contention.

**Partitioning.** Use nonoverlapping boundaries, such as user IDs [0, 50,000) and [50,000, 100,000). The old inclusive wording assigned the boundary user to both owners. Repartitioning is possible with an ownership-transfer protocol; stable partitions are not a universal prerequisite. Cross-partition transactions require separate treatment.

**CRDTs.** A suitable replicated data type can converge under concurrent updates. A supported counter can merge an increment of one and another of two into three. A last-write-wins register resolves concurrent values for the same key to one winner under its ordering rule; it does not expose both values as the original example claimed. Separate keys or a multi-value register have different semantics. Convergence does not ensure that a sale never exceeds stock or that a payment was authorized.

## Four handoff mechanisms

Request–reply gives a caller a direct response but needs a deadline and a way to resolve unknown completion. Pub–sub distributes events, with durability and delivery semantics chosen explicitly. Queues can provide persistent work distribution with leases, acknowledgements, redelivery, and dead-letter handling. Polling retrieves changes periodically, often with a cursor or version.

An asynchronous receiver cannot proceed with missing prerequisites merely because it does not block a thread. A queue is durable only if configured and operated accordingly. Acknowledgement proves the agreed processing stage, not automatically a successful business result. Five-second polling is an example cadence, not a fixed latency guarantee; processing and service delays add time.

## Contain partial failures

A five-second timeout, a breaker opening after three failures for sixty seconds, and retry delays of one, two, four, and eight seconds are illustrative settings. Derive real values from workload, deadlines, recovery behavior, and risk. Backoff and jitter reduce synchronized pressure; bounded retries and idempotency protect against repeated effects.

Separate processes or resource pools can limit a crash or overload, but shared hosts and services remain common failure points. A fallback can be a pause or clear failure. Continuing with stale data or a default value is safe only when the task permits it.

## Five corrected failure scenarios

1. **Order, billing, and fulfillment.** Keep the order in a pending state until payment status is established under the business policy. A timeout can conceal a successful charge, so query or reconcile with an idempotency key before retrying. Do not ship merely because a billing call returned no result. Compensation may release a reservation or refund a confirmed charge; it is not an automatic rollback of a shipped package.
2. **Recommendation feedback.** Delayed click logs can affect training, but they do not necessarily worsen every model. Track event time, completeness, duplicate handling, and validation. Separate serving and training lifecycles where useful, with an appropriate freshness policy; deliberate lag alone is not a repair.
3. **Inventory race.** With stock of five, two orders each requesting five can oversell if both validate against the same stale count. Stock might record zero after a lost update or become negative after separate decrements; the result depends on implementation. Use an atomic reservation/check or a suitable transaction. Two one-unit orders from stock five would not by themselves create negative five stock.
4. **Lock inversion.** Agent A holds User and waits for Order while B holds Order and waits for User. A consistent acquisition order helps prevent this pattern; transaction recovery is still needed.
5. **Subscriber failure.** A notification consumer can miss an event in an ephemeral system. Durable delivery, replay, acknowledgements, deduplication, and dead-letter review can improve recovery. A subscriber crash does not inherently lose an event in every pub-sub design.

These are illustrations, not documented incidents. Test slow workers, dropped or duplicated messages, network partitions, stale versions, and uncertain action completion in the actual design.

## Intellectual lineage

Distributed-systems work on consistency, transactions, replication, CRDTs, and partial failure informs these patterns. CAP concerns consistency and availability during a partition; it is not a rule that every system permanently picks two of three features. Raft and Paxos are consensus protocols, not replacements for an application workflow engine. Airflow and Temporal address orchestration with different execution assumptions.

Little's Law is L = λW under the relevant stable-system conditions: average work in the chosen system equals arrival rate times average time in it. State the boundary and consistent units. Queue depth divided by throughput describes average queue waiting time only with matching queue measures and assumptions; it does not directly estimate P95 end-to-end latency.

See [SKILL.md](SKILL.md) for the coordination design and [research notes](references/research-and-operating-notes.md) for primary references and evidence limits.
