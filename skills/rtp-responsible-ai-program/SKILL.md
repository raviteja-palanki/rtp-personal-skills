---
name: rtp-responsible-ai-program
description: "Build or audit an enterprise Responsible AI program using the MIT Sloan 3 Gaps framework and SHARP implementation system. Diagnoses organisational accountability, strategy, and resource gaps. Designs governance structures that hardwire ethics into product development. Triggers: 'responsible AI', 'AI governance program', 'ethics program', 'SHARP framework', 'accountability gap', 'AI governance structure', 'AI ethics by design'"
imports: ["safety-as-moat", "safety-by-design", "dual-lens"]
version: "1.1"
framework_source: "MIT Sloan Management Review — Öykü Işık & Ankita Goswami, 'The Three Obstacles Slowing Responsible AI', October 2025"
---

# Responsible AI Program

## DEPTH DECISION

**Go deep if:** Building or overhauling an enterprise AI governance program, diagnosing why responsible AI initiatives are failing despite policy documents existing, preparing for board or regulatory scrutiny of AI practices, or embedding ethics into a product development lifecycle.

**Skim to the SHARP checklist if:** You already have a governance program and need a quick health check, or you're coaching a stakeholder on why their "AI ethics committee" isn't working.

**Skip if:** Pre-PMF startup with no external AI risk, internal tool with no customer-facing AI, or context where AI governance is genuinely premature.

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md):
1. Ask the Grounding Questions — at minimum: Who is the customer? What problem? What does YES mean saying NO to?
2. Route depth: Executive Summary or Comprehensive Analysis?
3. Identify output format: Document, presentation, stakeholder brief?

---

## THE TRAP

Most organisations build **responsible AI programs that exist to be seen, not to function**.

They create ethics committees that meet quarterly but have no veto power. They publish AI principles that nobody checks before shipping. They hire ethics officers who write policies but aren't in the room when product decisions are made.

The result is three structural gaps that MIT Sloan's research identified in enterprise AI programs:

1. **The Accountability Gap** — When AI causes harm, nobody claims responsibility. The model vendor blames fine-tuning. The fine-tuning team blames the product. The product team blames the business requirement. The business blames market pressure.

2. **The Strategy Gap** — The company has AI initiatives everywhere but no AI governance strategy. Ethics is reactive (we'll add guardrails when something breaks) rather than proactive (ethics reviews are a gate before launch).

3. **The Resource Gap** — Ethics teams are resourced to *write* policies but not to *implement* or *enforce* them. They have influence but not authority. They produce documents but cannot stop a launch.

The hard truth: **These three gaps don't close through awareness campaigns or workshops.** They close through structural change — who owns what, who can stop what, what gets measured.

That's what the SHARP framework is for.

---

## The 3 Gaps Diagnostic

Before prescribing SHARP, diagnose which gaps your organisation actually has.

### Accountability Gap Diagnostic

Ask these questions. If you answer NO to any, the gap exists:

| Question | YES | NO |
|---------|-----|-----|
| Is there a named individual (not a committee) accountable for AI ethics outcomes — with it in their job description? | | |
| When an AI incident occurs, is the escalation path clear within 24 hours? | | |
| Do product teams know whose approval they need before launching a customer-facing AI feature? | | |
| Has anyone been held accountable (positively or negatively) for an AI ethics outcome in the last 12 months? | | |

**Gap severity:** 0 NOs = No gap. 1-2 NOs = Partial gap. 3-4 NOs = Full accountability gap.

### Strategy Gap Diagnostic

| Question | YES | NO |
|---------|-----|-----|
| Does the company have a written AI ethics strategy (not principles — a strategy with goals, timelines, and owners)? | | |
| Are ethics reviews part of the product development process — as a gate, not an audit after launch? | | |
| Does the AI ethics strategy cascade from company values to team-level practices to individual decisions? | | |
| Has leadership made explicit trade-offs about what AI use cases the company will NOT pursue, and why? | | |

**Gap severity:** 0 NOs = No gap. 1-2 NOs = Partial gap. 3-4 NOs = Full strategy gap.

### Resource Gap Diagnostic

| Question | YES | NO |
|---------|-----|-----|
| Does the ethics/AI governance team have authority to delay or block a product launch? | | |
| Do ethics reviewers have technical AI literacy sufficient to evaluate model behavior? | | |
| Is there a dedicated budget for falsificationing, bias auditing, and ethics-related engineering? | | |
| Are ethics reviews resourced proportionally to AI risk level (more review for higher-risk AI)? | | |

**Gap severity:** 0 NOs = No gap. 1-2 NOs = Partial gap. 3-4 NOs = Full resource gap.

---

## The SHARP Framework — Closing the Gaps

> **Attribution:** SHARP was developed by Öykü Işık (Professor at IMD) and Ankita Goswami (external researcher at IMD), published in MIT Sloan Management Review, October 2025. The full framework is titled "The Three Obstacles Slowing Responsible AI." Cite as: Işık, Ö. and Goswami, A. (2025). "The Three Obstacles Slowing Responsible AI." *MIT Sloan Management Review*, 67205.

SHARP is an implementation framework for responsible AI governance. Each letter maps to a structural change, not a workshop. The five strategies are not sequential steps or universal templates — they reflect varied ways organisations reconfigure their structures, incentives, and routines to make responsible AI operational.

**The five strategies:**
- **S** — Structure ownership at the project level
- **H** — Hardwire ethics into everyday procedures
- **A** — Align ethical risk with business risk
- **R** — Reward responsible behaviour
- **P** — Practice ethical judgment, not just compliance

### S — Structure Ownership (at the project level)

**What it means:** Assign a specific individual — not a committee, not a team, not a working group — as personally accountable for AI ethics outcomes. Committees diffuse accountability. One named person concentrates it.

**The problem with committees:** The Accountability Gap exists precisely because committees give everyone cover. When something goes wrong, every committee member can say "I raised it." Nobody can say "I stopped it." A committee can advise. It cannot be held accountable.

**What to do:**
- Designate a Chief AI Ethics Officer (or embed this in an existing role: CPTO, CDO) with explicit AI governance authority in their job description
- Define their authority clearly: Can they delay a launch? (Yes.) Can they kill a feature? (Yes, with CEO agreement.) What requires their sign-off?
- Create a tiered accountability map:
  - Tier 1 (product team): Responsible for completing ethics self-assessment before every AI feature launch
  - Tier 2 (ethics function): Responsible for reviewing high-risk AI (defined by your risk matrix) before launch
  - Tier 3 (CAEO/leadership): Responsible for enterprise AI risk posture and regulatory compliance

**What good looks like:** Every AI incident has a clear owner within 1 hour. Every AI launch has a documented approval trail. Accountability is traceable, not diffuse.

**Where this breaks:**
- Ownership is assigned but authority is not. Owner can flag issues but cannot act on them.
- Owner lacks technical AI literacy and must defer to engineering on every substantive question.
- Accountability map is documented but not actually used when incidents occur.

---

### H — Hardwire Ethics into Everyday Procedures

**What it means:** Embed ethics into everyday product development procedures — not as a separate audit layer bolted on at the end. Ethics steps must feel like "something we do," not "something someone else makes us do." (Direct quote from an engineering lead at a health care analytics company, MIT Sloan research.)

The word "everyday" is intentional. This is not about quarterly ethics reviews. It is about ethics showing up in sprint templates, pull request checklists, design reviews, and deployment gates — the daily rhythm of building.

**The problem with post-hoc ethics:** Most enterprise AI ethics programs are audits: they review AI systems after they're built, deployed, and have users. By then, the cost of change is high, teams are defensive, and "responsible AI" becomes "document why we're fine."

**Ethics as a gate looks like this:**

```
Discovery                Build              Pre-Launch         Post-Launch
    │                      │                    │                  │
    ▼                      ▼                    ▼                  ▼
AI Use Case           Technical          Ethics Review       Ongoing
Risk Assessment       Review             (MANDATORY         Monitoring
(self-assessment      (data, model,      gate — cannot      (monthly
by product team)      architecture)      ship without       review of
                                         sign-off)          live behavior)
```

**The AI Use Case Risk Assessment** — what product teams complete before development begins:

| Dimension | Low Risk | Medium Risk | High Risk |
|-----------|----------|-------------|-----------|
| Who does it affect? | Internal users only | External users, limited scope | Broad public; vulnerable populations |
| What decisions does it influence? | Operational efficiency | Customer experience | Access, safety, legal rights |
| What if it fails? | Inconvenience | Financial loss, reputational damage | Physical harm, discrimination, legal liability |
| Is it human-in-the-loop? | Human reviews every output | Human reviews exceptions | Fully automated decisions |
| Is training data documented? | Fully documented | Partially documented | Unknown provenance |

**Scoring:** Mostly Low → Self-certified. Any Medium → Ethics team review before launch. Any High → CAEO sign-off required before development begins, not just before launch.

**What hardwiring requires:**
- Ethics checkpoints appear in every sprint template, PRD template, and launch checklist
- Product teams cannot mark a launch-ready without completing the risk assessment
- High-risk AI features require ethics sign-off in the same way they require legal and security sign-off

**Where this breaks:**
- The gate exists on paper but isn't enforced. Teams mark "reviewed" without actual review.
- Risk assessments are filled out to pass, not to discover risk.
- Ethics reviewers are overloaded and rubber-stamp to keep pipelines moving.

---

### A — Align Ethical and Business Risk

**What it means:** Frame every ethical risk as a business risk — in the language executives already use — so governance decisions get the same attention as revenue decisions.

**The problem with ethics-only framing:** When an ethics concern is presented as a values question, executives weigh it against quarterly targets and values lose. When the same concern is presented as business risk with a dollar estimate, it gets a line item and an owner.

**The translation table:**

| Ethical Risk | Business Risk Translation | Quantification Approach |
|---|---|---|
| Algorithmic bias in credit scoring | Regulatory fine (CFPB enforcement) + class action liability + brand damage in affected demographic | Estimate fine range from precedent cases + NPS impact in affected segment |
| AI-generated content without disclosure | FTC enforcement risk + user trust collapse when discovered | FTC fine precedents + churn model if trust breaks |
| Data used to train model without consent | GDPR/CCPA fine + contract breach + reputational exposure | Maximum fine calculation + estimated customer defection rate |
| Hiring AI that screens out protected classes | EEOC investigation + lawsuit + brand damage in talent market | Legal cost estimates + reduced talent pool quality |
| Medical AI that fails silently | FDA enforcement (if classified as medical device) + malpractice liability + patient harm | Regulatory timeline + insurance/legal estimate |

**The alignment protocol:**
1. For every high/medium risk AI use case, complete the Ethical-Business Risk Translation
2. Present ethics recommendations with the dollar risk estimate, not just the values argument
3. Frame governance investment as risk mitigation, not cost: "Ethics review costs $50K/year. One CFPB enforcement action costs $500K–$50M."

**The Inner/Outer World lens:** Ethical risk lives in both worlds. The *inner world* (what you can control) is whether your process generates the risk. The *outer world* (what you adapt to) is whether regulators, users, or press expose it. Responsible AI programs manage both — they don't just watch the outer world; they design the inner world to not create the risk in the first place.

**Where this breaks:**
- Translation is done once for a presentation but not embedded into ongoing risk management
- Estimates are too vague to act on ("reputational damage" without a dollar range)
- Business risk framing works for cost-conscious executives but alienates values-driven stakeholders who feel the ethics are being commodified

---

### R — Reward Responsible Behaviour

**What it means:** Incentive structures must reward ethical decision-making, not just speed and output. If teams are measured only on shipping velocity, ethics reviews will always feel like friction.

**The problem with misaligned incentives:** You can write all the responsible AI principles you want. If the team that skips the ethics review ships a week faster and gets praised for it, the message is clear: ethics is optional when it's inconvenient.

**What rewarding responsible behaviour looks like:**

| Practice | What to Add or Change |
|---------|----------------------|
| Performance reviews | Add ethics hygiene metric: "Completed required AI risk assessments without prompting." Weight it alongside delivery metrics. |
| Launch retrospectives | Standard retrospective question: "Did our ethics review process catch anything we would have missed?" Make findings visible to leadership. |
| Incident response | When a team self-reports an AI risk before it causes harm, treat it as a positive signal — document it as a near-miss prevented, not a failure. |
| Recognition | Publicly recognise teams that voluntarily deepened ethics review beyond the minimum. |
| Promotion criteria | For senior PMs and engineers, include demonstrated ethics judgment as a criterion. |

**What NOT to do:**
- Don't create a separate "ethics bonus" — it signals ethics is add-on, not core
- Don't measure ethics compliance only through audits — that creates paperwork compliance, not judgment
- Don't penalise teams for raising concerns that delay launches if the concern was legitimate — you'll get silence next time

**The judgment muscle:** Reward structures build habits. You're not just rewarding individual decisions — you're building the organisational muscle for ethical judgment at scale. Teams that regularly practice ethics reasoning make better decisions faster over time. Teams that treat ethics as a checklist never develop the judgment.

---

### P — Practice Ethical Judgment, Not Just Compliance

**What it means:** The goal is not compliance — it is building people's capacity to make ethical judgments. Few processes can entirely replace the need for human judgment, especially in contexts where ethical tensions are subtle or evolving. Checklists tell you what to check. Practice builds the ability to handle what isn't on the checklist.

**The compliance trap:** A team trained only on compliance policies freezes when they face a genuinely novel situation. A team that has practiced judgment can reason through novel cases because they've built the muscle — they've done it before in a low-stakes setting.

The MIT Sloan research found that organisations overly reliant on AI-enabled decision-making were at particular risk: without intentional reinforcement of ethical reasoning through practice, even well-designed systems can degrade individual competence over time. People become passive recipients of system suggestions rather than active moral agents.

**The problem with rules-only ethics:** Rules handle known cases. AI creates novel cases that existing rules don't cover. Teams that only know the rules freeze when they face something new. Teams that have practised judgment can reason through novel cases.

**The Practice Protocol:**

**Monthly Case Study Reviews (Team Level)**
- Each team reviews one real-world AI ethics case (internal near-miss or external public incident) per month
- Discussion format: What happened? What was the ethical failure? What structural change would have prevented it? What would we do differently in our context?
- Time: 30 minutes. No slides. Discussion only.
- Outcome: 1 documented learning per session, added to team retrospective

**Quarterly Tabletop Simulations (Cross-Functional)**
- A facilitated scenario: "Our AI system [specific scenario] has just been reported by a journalist. It's 6 PM Friday."
- Participants: Product, Engineering, Legal, Comms, Ethics, and one senior business leader
- The exercise: Work through the first 24 hours. Who calls who? What gets checked? What gets communicated to users? What gets escalated to the board?
- Outcome: Updated incident response playbook + revealed gaps in escalation paths

**Annual Responsible AI Review (Executive Level)**
- Review: AI portfolio risk map, incidents from the year, near-misses, regulatory changes on the horizon
- Decision point: Any AI use cases to sunset, restrict, or redesign based on year's learning?
- Output: Updated enterprise AI ethics strategy for following year

**Where this breaks:**
- Simulations are one-time events, not recurring practice
- Case studies are too generic (Harvard case studies about other companies) rather than grounded in the team's actual AI systems
- Senior leaders attend the annual review but aren't in the monthly practices — judgment builds from the bottom up, not just from strategy documents

---

## The SHARP Self-Assessment

Score each letter 0-2 and identify your weakest area.

| Letter | What you're assessing | Score (0 = not present, 1 = partial, 2 = fully implemented) |
|--------|----------------------|-------------------------------------------------------------|
| **S** — Structure | Is there a named individual with authority and accountability for AI ethics? | |
| **H** — Hardwire | Are ethics reviews a mandatory gate before launch, not an optional audit? | |
| **A** — Align | Are ethical risks translated into business risk language with estimates? | |
| **R** — Reward | Do incentive structures reward ethical decision-making, not just speed? | |
| **P** — Practice | Do teams regularly practice ethical judgment through case studies and simulations? | |

**Scoring:**
- 8-10: Mature program. Focus on deepening, not building.
- 5-7: Developing program. Address the lowest-scoring letter first.
- 3-4: Early-stage program. Start with S (structure) — without ownership, the other letters won't hold.
- 0-2: Program doesn't exist in functional form. Begin with the 3 Gaps Diagnostic before SHARP.

**The sequencing rule:** S before everything else. You cannot hardwire (H) ethics reviews without someone to enforce them. You cannot align (A) risk without someone accountable for the assessment. You cannot reward (R) without someone defining what responsible behavior looks like. You cannot practise (P) without someone designing the exercises. SHARP is sequential, not simultaneous.

---

## Connecting to the Broader Safety Ecosystem

This skill pairs with:

- **Safety-as-Moat** — When your Responsible AI Program creates enterprise switching costs through demonstrably superior governance posture
- **Safety-by-Design** — The technical implementation layer; Responsible AI Program defines the governance; Safety-by-Design encodes it into the product architecture

**The layered view:**

```
Responsible AI Program (SHARP)          ← Organisational governance layer
        │
        ▼
Safety-by-Design (4-Layer Model)        ← Technical architecture layer
        │
        ▼
Safety-as-Moat (Enterprise Positioning) ← Commercial differentiation layer
```

Most organisations get the layers backwards — they try to build a safety moat before they have a functional governance program. The result is safety theater: impressive external positioning, hollow internal practice.

---

## OUTPUT FORMAT

```
## Responsible AI Program Assessment: [Organisation/Product]

### 3 Gaps Diagnosis
| Gap | Severity | Key Evidence |
|-----|----------|-------------|
| Accountability Gap | [None/Partial/Full] | [What's missing] |
| Strategy Gap | [None/Partial/Full] | [What's missing] |
| Resource Gap | [None/Partial/Full] | [What's missing] |

### SHARP Assessment
| Letter | Score (0-2) | Key Gap | Recommended Action |
|--------|------------|---------|-------------------|
| S — Structure | | | |
| H — Hardwire | | | |
| A — Align | | | |
| R — Reward | | | |
| P — Practice | | | |
| **Total** | **/10** | | |

### Priority Actions (Sequenced)
1. [Highest-leverage change — always start with lowest SHARP score]
2. [Second priority]
3. [Third priority]

### Business Risk Translation
[Top 2-3 ethical risks translated into business risk language with estimated financial exposure]

### 90-Day Implementation Plan
| Week | Action | Owner | Definition of Done |
|------|--------|-------|-------------------|
```

---

## WHEN WRONG

This skill gives bad advice if:
- **Pre-PMF with no external exposure:** Building SHARP before you have product-market fit is premature governance. Ship, learn, then build the program as AI risk materialises.
- **Regulation is the primary driver (not values):** If the goal is compliance theater for regulators, SHARP will feel like overkill. But if that's the goal, name it — compliance theater is a conscious business choice.
- **The organisation has no actual AI in production:** Responsible AI programs for hypothetical future AI use cases waste governance resources better spent when AI is real.
- **Leadership is performatively committed:** If the CEO wants a "responsible AI program" for press releases but won't give the function any authority, SHARP won't work — no enforcement mechanism. Name this explicitly rather than designing a program that fails.

---

## TRADE-OFF LEDGER

Complete the Trade-Off Ledger from the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md), Section 3.

## CONCLUSION

Follow the Conclusion Protocol from the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md), Section 5:
1. State the recommendation
2. Name the key trade-off
3. Acknowledge the biggest risk
4. Define the next action

---

## VISUAL SUMMARY

After completing the primary output, invoke the **excalidraw-svg** skill to create a single Excalidraw SVG visual summary. This diagram captures the essence of the analysis in one glanceable image — making the deliverable 10x more impactful. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.

---

*Version 1.0 — 5 APR 2026*
*Framework Source: MIT Sloan Management Review — Responsible AI Research (3 Gaps + SHARP)*
*Part of: AI PM Skills / safety-and-trust layer*
