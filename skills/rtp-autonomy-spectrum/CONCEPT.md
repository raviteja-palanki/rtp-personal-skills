# autonomy-spectrum: The Trust Spectrum in Agent Design

## The Dual Definition

**Business lens:** Autonomy is the axis on which you trade user control for product latency. More autonomy = less waiting, more errors. Less autonomy = safer, slower. The sweet spot is where trust recovery cost equals latency gain.

**Technical lens:** Autonomy is a decision gate: given action A and confidence level C, which approval route executes? The gate is deterministic, queryable, and auditable. It's not "did the agent decide to act?" but "did the governance layer permit execution?"

---

## The Trap: Autonomy as Capability

The instinct is backwards: "The agent has write access to the database, so it should execute writes autonomously." This treats autonomy as a property of the agent's power, not of the trust relationship.

The fix: Reverse the logic. Start with the failure cost. "If the agent writes bad data, we lose $50k and 2 days of remediation. Therefore, agent write access requires pre-approval from a human." Now autonomy is a function of business risk, not capability.

**Why this matters:**
- A read-only agent can be given near-total autonomy (observation is safe).
- A write agent needs careful gatekeeping (action has consequences).
- A deletion agent needs locks (consequences are permanent).

The trap catches teams when they scale: you give one agent 95% autonomy, it works, so you copy the rule to ten agents, and suddenly one bad decision cascades through all ten. Autonomy escalation needs to be intentional, not inherited.

---

## Progressive Trust: The Confidence-Autonomy Curve

Production agents earn autonomy over time. This is not metaphorical. It's measurable:

1. **Probation (0-20 decisions):** All actions trigger human approval. Agent is black box.
2. **Observation (20-100 decisions):** Agent gets read access. No approval gates. You observe its analysis quality.
3. **Co-pilot (100-500 decisions):** Agent gets write access to non-reversible, low-cost actions. Asks for approval on medium-blast decisions. You track approval acceptance rate.
4. **Autopilot (500+ decisions):** Agent gets autonomous execution on high-confidence decisions. Still audited, still locked down on locked-category actions.

**The metric:** acceptance rate. If you approve 95% of agent requests, the agent is undershooting. If you approve 5%, it's asking too much. Target is 70-85%—agent is making useful recommendations that you trust enough to sign off on.

---

## Consequence Magnitude: The Real Boundary

Autonomy isn't about what the agent can do. It's about what can go wrong.

**Reversibility:**
- Reading a file: fully reversible (just read again if needed)
- Modifying a dev database: reversible (restore from backup)
- Publishing to production: conditionally reversible (rollback possible, but user-facing)
- Deleting a backup: irreversible (data is gone)

**Scope of impact:**
- Single user, single operation: low blast (mistake affects one)
- Batch job across all users: high blast (mistake affects thousands)
- Cross-system cascade (delete triggers cleanup): medium-to-high blast (unintended side effects)

**Decision rule:**
```
IF reversible AND low_blast:
  → Autonomy can be high (95%+)
ELSE IF reversible AND medium_blast:
  → Autonomy is conditional (80-90%, drops on error)
ELSE IF irreversible AND medium_blast:
  → Autonomy is conditional on explicit approval (60%, expert gate)
ELSE IF irreversible AND high_blast:
  → Autonomy is denied (0%, locked)
```

This is not policy. It's a decision tree. Different agents, different actions will flow through different paths.

---

## Confidence: The Empirical Gate

The agent tells you: "I'm 92% confident in this recommendation."

What does that number mean? Not philosophical confidence. Empirical: "In my training, when I was 92% confident, I was right 91% of the time."

Your job: validate that number. Run the agent on held-out test cases. Plot confidence vs accuracy. If 92% confidence actually predicts 91% accuracy, trust it. If it predicts 60% accuracy, the agent is miscalibrated and you lower its autonomy threshold.

**The curve matters:**
- Well-calibrated agent: confidence = accuracy. Raise thresholds based on the curve.
- Overconfident agent: claims 95%, delivers 70%. Lower all thresholds. Investigate.
- Underconfident agent: claims 60%, delivers 92%. Raise thresholds (latency gain without risk).

---

## Progressive Escalation Protocol

Don't hardcode autonomy. Measure it.

**Phase 1 (Weeks 1-2):** Agent runs in sandbox with full logging. No production access.
**Phase 2 (Weeks 3-4):** Agent gets read-only access to non-critical prod systems. Audit decisions.
**Phase 3 (Weeks 5-6):** Agent gets write access to dev environments. Low-blast, reversible actions only.
**Phase 4 (Weeks 7+):** Agent escalates based on accuracy metrics.
- Accuracy >95% for 50+ decisions → autonomy on reversible, medium-blast actions
- Accuracy >98% for 100+ decisions → autonomy on irreversible, medium-blast actions (with human audit)
- Never autonomy on high-blast, irreversible actions (human signature always)

**Reset rule:** One critical failure drops autonomy by 2 levels. You don't rebuild trust fast.

---

## The User Experience of Autonomy

High autonomy should feel invisible when working. Invisible means:
- Agent acts without asking, but user can see what it did (transparency)
- User can override decisions retroactively (control)
- Agent explains its reasoning when asked (explainability)

Low autonomy should feel interactive:
- Agent asks before acting
- Ask is specific ("approve write to X?" not "continue?")
- User can ask for recommendation, disagree, and the agent learns

The failure mode is "silent autonomy": agent acts without user knowing, user discovers it later, trust evaporates.

---

## Intellectual Lineage

- **From control theory:** Feedback loops that adjust autonomy based on error signals (Wiener, 1948).
- **From organizational behavior:** Progressive empowerment as trust metric (McGregor's Theory Y).
- **From Bayesian decision theory:** Confidence thresholds tied to cost functions (DeGroot, 1962).
- **From AI safety:** Specification gaming (Goodhart's Law): if you measure only accuracy, agent optimizes for appearing accurate, not being accurate.

The synthesis: Autonomy is a dynamically adjusted control parameter that depends on (action reversibility, consequence magnitude, measured confidence calibration, progressive trust track record). It is not a property of the agent. It is a property of the (agent, action, user, context) tuple.

---

## Real-World Pitfalls

**Uber eats dispatching:** Agent autonomy on delivery assignments is high (reversible, low-blast). Trust earned over millions of deliveries. But when consequence magnitude spiked during COVID (surge pricing, limited drivers), autonomy stayed the same → prices exploded → user backlash.

**Medical AI diagnostics:** Agent has 99% accuracy on test set. Gains full autonomy. But test set was selected; real patients have different distribution. Autonomy should have been conditional on real-world calibration.

**Autonomous vehicles:** Tested in California, deployed in Arizona. Different weather, different roads, different drivers. Autonomy didn't transfer. The mistake: treating autonomy as a global property instead of a context-dependent one.

**Slack bot moderation:** Bot had high autonomy on message deletion (reversible-ish, medium-blast). But users didn't expect automated deletion, trust broke. The fix: give autonomy, but make it visible (log it, let user recover it).

---

## Decision Checkpoints

**When setting initial autonomy:**
1. What's the failure mode? (What's the worst decision?)
2. What's the cost? (Time, money, data, reputation?)
3. Is it reversible? (Can we undo it?)
4. How many users are affected?
5. Can we detect the failure quickly?

**When escalating autonomy:**
1. Is the agent consistently accurate? (Not lucky.)
2. Is confidence calibrated? (Not overconfident.)
3. Are failure modes understood? (Not unknown unknowns.)
4. Can we still detect and recover from failure? (Reversibility still holds.)
5. Is the user expecting and accepting this level of autonomy?

Miss any of these, autonomy becomes liability.
