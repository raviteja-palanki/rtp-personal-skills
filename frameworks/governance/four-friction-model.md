# Four-Friction Model
**Authors:** Rahul Telang, Muhammad Zia Hydari, Raja Iqbal (HBR, 2026)
**Source:** "To Scale AI Agents Successfully, Think of Them Like Team Members"
**Maps to skills:** `safety-by-design`, `agent-harness`, `friction-audit`, `agent-risk`

---

## The Framework

Four frictions that must be designed INTO agentic systems at inception, not bolted on after:

**1. Identity** — Does each agent have a unique identity with narrowly scoped permissions? Can every action be traced to a specific agent? Shared accounts and broad permissions are governance landmines.

**2. Context** — Are data sources authoritative with captured provenance? External inputs treated as potential attack vectors? Agents that ingest unvalidated data create cascading trust failures.

**3. Control** — Is there a deterministic validation layer between "AI wants to act" and "action happens"? AI proposes → software validates compliance → execution. Without this, the agent is an uncontrolled system.

**4. Accountability** — Can you reconstruct any decision the agent made? Comprehensive audit trail: who authorized, what data informed, what happened. Without this, you have liability without evidence.

## Evidence

- Replit incident: Agent deleted database despite restrictions (Identity + Control gap)
- Moffatt v. Air Canada: Company held liable for chatbot behavior (Accountability gap)
- ServiceNow cascade: Multi-agent system compromised via second-order prompt injection (Context gap)

## When to Use

Pre-launch audit for any agentic system. Quick diagnostic (30 minutes): check all four. If any friction is missing, stop and fix before shipping.

## When This Fails

- Read-only advisory systems (no actions = no control/accountability needed)
- Early prototypes where friction slows learning (apply at production gate, not prototype)
- Simple automation (Level 1-2) where deterministic code already provides all four

## Evolution Log

- 2026-04-05: Captured from HBR Batch 2 synthesis. Linked to Replit, Air Canada, ServiceNow cases.
