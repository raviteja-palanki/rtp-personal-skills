---
name: rtp-breach-ready
description: 'Design systems that SURVIVE being hacked — because "if," not "when." Prevention-only security fails. Resilience means: can you operate 48 hours without digital systems? Can you isolate damage? Can you restore from manual backup? FedEx survived NotPetya because of resilience planning. Use when designing systems that handle sensitive data, post-incident reviews, business continuity planning, or any system where downtime has non-trivial cost. Skip if the system has trivial impact if breached (internal tool with no sensitive data).'
---
# Breach Ready

## DEPTH DECISION

**Go deep if:** You're designing AI systems that handle sensitive data, building infrastructure for any mission-critical service, or recovering from a breach. **Skim to questions if:** Quick audit of whether your system has basic resilience (not just prevention). **Skip if:** The system is low-impact if breached (internal experiment, no sensitive data, brief downtime acceptable).

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md):
1. Ask the Grounding Questions (Section 1) — at minimum: What data does this system handle? What's the cost of 1 hour of downtime? What's your regulatory exposure?
2. Route depth: Executive Summary or Comprehensive Analysis?
3. Identify output format: Document, presentation, or both?

Then proceed with the skill-specific analysis below.

## THE TRAP

You will invest everything in prevention and nothing in survival. The bias is **prevention illusion** — the assumption that if you just secure everything tightly enough, breaches won't happen. They will. Every major company gets breached. The question is not "if" but "when" and "how fast do we recover?"

Prevention buys you time. It doesn't guarantee safety.

**The mechanism:** Prevention = building a stronger castle wall. Resilience = planning what happens when the wall falls anyway.

The trap is most seductive when:
- You've just deployed a security update and feel safe (temporary)
- Your threat model focuses on "likely" attacks (the worst attack is always the unlikely one)
- You have an incident response plan but haven't tested it
- The cost of downtime seems theoretical (until it happens)

### The FedEx NotPetya Case (2017)

In June 2017, the NotPetya ransomware hit FedEx and thousands of other companies. Ransomware encrypted critical systems. FedEx's response is a masterclass in resilience.

Most companies got hit hard because they had no fallback: systems encrypted → no shipping → no tracking → no revenue. Recovery took weeks for some. FedEx's recovery: 48 hours.

Why? Because FedEx had planned for exactly this scenario:
1. **Isolated systems**: Shipping (old mainframe-based system) was physically isolated from operational tech. Ransomware spread, but the mainframe stayed up.
2. **Manual fallback**: When digital systems went down, staff reverted to paper-based tracking (slower, but functional). Customers could still ship packages.
3. **Backup power and communication**: 48-hour manual operation didn't require digital infrastructure — just radio, phones, and paper.
4. **Tiered recovery**: Critical revenue functions came back first (shipping, tracking), non-critical later (reporting, dashboards).

Result: FedEx lost a few hundred million to the breach and recovery cost. Competitors who had no resilience plan lost billions — in downtime, lost contracts, and customer defection.

The difference? FedEx had tested "what happens if our digital systems are completely unavailable for 72 hours?" They had answers. Most companies didn't.

## THE PROCESS

### 1. THE 48-HOUR TEST

Ask: **"If all digital systems disappeared tomorrow, could we operate for 48 hours manually?"**

Not "do we want to," but "can we actually?"

**Operational integrity:**
- Can we take orders without the system?
- Can we fulfill them without the system?
- Can we communicate with customers without the system?
- Can we pay employees without the system?

**Example (SaaS company):**
- Can we take new customer signups without Stripe integration? (No — write down credit card manually? Accept COD?)
- Can we serve existing customers without the API? (No — tell them "feature unavailable for 48 hours"? Accept that?)
- Can we know which customers are active? (Do we have a backup list? Is it current?)

**Example (healthcare system):**
- Can doctors access patient records without the EHR? (Paper charts — but are they current? Are they stored where staff can access them?)
- Can we process prescriptions without the pharmacy system? (Manual PDFs to pharmacies? Do they accept that?)
- Can lab results reach doctors? (Phone calls to staff? Fax? And then what?)

Be honest. Most organizations fail this test.

### 2. THE ISOLATION DIMENSION

Ask: **"Where do breaches spread unchecked? Where are our firewalls?"**

Design systems so damage is bounded.

**Isolation taxonomy:**
- **Network**: Revenue systems isolated from non-critical systems. Ransomware can encrypt Marketing but not Billing.
- **Data**: Customer data in separate databases from operational data. Breach of one doesn't compromise the other.
- **Human**: Different teams have different access. Marketing person can't access customer payment data.
- **Infrastructure**: Batch processing isolated from real-time systems. Cloud environment separated from on-prem.
- **Supplier**: AI vendor integrations sandboxed. If vendor gets compromised, damage doesn't cascade into your core systems.

**Example (ML team hosting AI models):**
- Can a compromised model endpoint inject malicious data into your database? → Isolation needed
- Can an attacker using the model API access your training data? → Isolation needed
- Can a supply-chain attack on the ML library compromise your infrastructure? → Isolation needed

### 3. THE DEGRADATION DIMENSION

Ask: **"What happens if we lose non-critical capabilities? Can the core function still work?"**

Design graceful degradation:
- System operates at 50% capacity but stays up
- Features turn off individually instead of cascading failure
- Users see "this feature unavailable" instead of whole system down

**Example (AI-powered customer support):**
- Full function: AI handles 90% of tickets, humans handle complex ones
- Degraded state: AI unavailable, humans handle all tickets (slower, more expensive, but functional)
- Design: Graceful fallback from AI to human routing (not: AI down = support down)

### 4. THE MANUAL FALLBACK DIMENSION

Ask: **"What's the non-digital version of this process? Can humans execute it?"**

Not "how would we do this in 1995?" but "if systems fail, can people continue the essential work?"

**Examples:**
- **SaaS billing**: If payment processing goes down, can we manually invoice customers and track payment via email? (Yes, it's slow, but it works)
- **E-commerce**: If inventory system fails, can we manually check stock, email customers, and process orders? (Yes)
- **AI recommendations**: If the model service dies, can we show default recommendations (bestsellers, trending)? (Yes)

**Trap:** You design a fallback, but it requires systems or data that don't exist. A manual payroll process that requires access to "the payroll database" isn't a fallback — it's still digital-dependent.

### 5. THE COMMUNICATION DIMENSION

Ask: **"If customers can't reach us digitally, can we reach them?"**

During a breach:
- Website might be down
- Email might be compromised
- Customers panic ("Did my data leak?")

**Fallback communications:**
- Pre-established phone numbers customers can call (must be publicized in advance, not during crisis)
- SMS alerts (separate from compromised email)
- Social media backup (Twitter, LinkedIn — use accounts separate from your main ones)
- Public status page on a different domain (not your main site)

**Example (AI SaaS company):**
- Your website gets encrypted. Customers can't log in.
- But your status page (hosted on a separate domain) is up: "We're experiencing a security incident. Customers should not enter new data. Follow @yourcompanyStatus for updates."
- You SMS all customers: "Incident reported. Check our status page for details."
- Result: Panic is lower, customers aren't trying to guess what happened.

### 6. THE RECOVERY DIMENSION

Ask: **"How fast can we restore from backups? Have we tested it?"**

**Recovery has three components:**
1. **Backup integrity**: Can we actually restore? (Test monthly. Most companies discover their backups are corrupted only during recovery.)
2. **Recovery time**: How long does restoration take? (If it takes 72 hours to restore, you can't recover in 48 hours manually.)
3. **Data loss**: How much data do we lose in the gap between backup and breach? (Hourly backups = max 1 hour loss. Daily backups = max 24 hours loss.)

**Realistic recovery tiers:**
- **Tier 1 (revenue systems)**: Recover within 2 hours. Requires hot backups or real-time replication.
- **Tier 2 (operational)**: Recover within 8 hours. Can use hourly backups.
- **Tier 3 (non-critical)**: Recover within 24 hours. Daily backups acceptable.

## DIAGNOSTIC QUESTIONS

Answer these honestly to assess your breach readiness:

1. **"Can we operate for 48 hours without our digital infrastructure?"** Test it. Actually try. Have teams work through a scenario.
   - **Red flag:** "We don't know." "It depends." "Probably not."
   - **Sharpening probe:** "What's the first thing that breaks if the system goes down?"

2. **"Where would ransomware spread unchecked in our infrastructure?"** Draw the network map. Trace how a compromised endpoint can move.
   - **Red flag:** Everything is networked. No firewalls. No segmentation.
   - **Sharpening probe:** "If the payment system gets breached, can the attacker reach customer data?"

3. **"Have we tested our backups in the last 6 months?"** Not "do we have backups" — have we actually restored from them?
   - **Red flag:** "We have backups but haven't tested." "Testing is on the roadmap." "We trust they work."
   - **Sharpening probe:** "If we needed to restore right now, how confident are you we'd succeed?"

4. **"What's the manual version of our core business process?"** Describe it without using any digital systems.
   - **Red flag:** You can't describe it. "We'd just wait for systems to come back up."
   - **Sharpening probe:** "How many people and how much time would it take?"

5. **"If customers couldn't reach us digitally for 24 hours, how would they know what happened?"** Do you have out-of-band communication?
   - **Red flag:** "They'd figure it out." "They'd call." (From a working phone number that isn't in your website?)
   - **Sharpening probe:** "Where are the phone numbers and backup contact methods publicized?"

6. **"What's the cost of 1 hour of downtime for our core function?"** Revenue loss, regulatory fines, customer defection.
   - **Red flag:** "We don't know." "It's minimal." (If it's truly minimal, skip resilience planning for that system. If it's significant, do it.)
   - **Sharpening probe:** "Would this event make the news? Would customers switch to competitors?"

## REALITY CHECK

**Failure modes:**
- **Backup-only resilience**: You have backups but no redundancy. Ransomware hits, you restore, but it takes 72 hours. Damage is done.
- **Recovery plan without testing**: Plan looks good on paper. When crisis hits, people don't remember it, or it's outdated, or it doesn't actually work.
- **Isolated but fragile manual process**: You can operate manually, but the process is so labor-intensive that 48 hours exhausts the team. Day 3, everyone breaks.

**Cost traps:**
- Resilient infrastructure costs 2-3x more than basic setup (redundancy, backup systems, isolation).
- But the cost of a week of downtime can be 10-100x the annual cost of resilience infrastructure.
- Do the math: 1 week downtime = $10M loss. Resilience infrastructure = $1M. ROI over 10 years: 10x payback on your first incident.

**Monitoring:**
- Track "backup test frequency" (monthly minimum)
- Track "manual process proficiency" (practice it quarterly, time it)
- Track "recovery time objectives by tier" (publish them, test them yearly)
- Track "incident response plan date" (update quarterly, every quarter)

## THE FIVE RESILIENCE DIMENSIONS (Detailed)

| Dimension | What It Is | Why It Matters | Example Failure |
|-----------|-----------|----------------|-----------------|
| **Isolation** | Breach damage is bounded to one system | Ransomware doesn't cascade to all systems | Attacker compromises one server, then sideways-moves to 50 more. Hours to days. |
| **Degradation** | Core function works at lower capacity | Business continues, not halted | Payment system down = all revenue functions halt. Revenue stops immediately. |
| **Manual fallback** | Process can execute without digital systems | Humans can keep the business running | All processes require the system. System down = everything stops. |
| **Communication** | Customers know what's happening | Panic and speculation are reduced | Website down, no status updates. Rumors spread, trust erodes. |
| **Recovery** | Systems come back online in hours, not days | Downtime cost is capped | Backups corrupted. Recovery takes 2 weeks. Revenue lost forever. |

## QUALITY GATE

- [ ] 48-hour manual operation scenario tested (not theoretical)
- [ ] Network isolation map created (firewalls, segmentation shown)
- [ ] Backup restoration tested in last 6 months (not just verified)
- [ ] Manual process documented and timed (and feasible with your team size)
- [ ] Out-of-band communication channels established (phone, SMS, separate domain)
- [ ] Recovery tiers defined (what comes back when, in what order)
- [ ] Incident response plan has date (last reviewed/tested)

## WHEN WRONG

This skill gives bad advice when:
- **The system truly has trivial impact if breached** (low value data, fast recovery doesn't matter) — resilience investment is unnecessary overhead
- **Your environment has zero regulatory requirements** (rare in practice, but possible for internal tools)
- **Cost of resilience infrastructure exceeds cost of breach** (e.g., backup of a $10k system costs $50k annually) — accept the risk instead

## TRADE-OFF LEDGER

BY CHOOSING **resilience over prevention-only**:
  We are betting on: Breaches will happen, and recovery speed matters more than preventing them entirely.
  We are giving up: Simplicity. Resilient systems are more complex (redundancy, isolation, backups cost money and operational overhead).
  This is reversible within: Not really. Once you've built resilience, unwinding it is expensive. But you can invest in tiers (core systems first, nice-to-haves later).

THE HIDDEN TRADE-OFF:
  Building resilience requires admitting that prevention is insufficient. This changes how you think about security. Shift from "we'll never get breached" to "we will get breached, let's survive it." This is psychologically uncomfortable. Leadership may resist ("Are you saying security isn't good enough?"). Reframe: "Security is our first line. Resilience is our second line."

CONFIDENCE: **High**
  What would change our mind: If we saw compelling evidence that prevention actually stops breaches (we haven't). Every incident response post-mortem shows: even excellent prevention failed; what mattered was recovery planning.

## CONCLUSION

**The recommendation:** For any system handling sensitive data or mission-critical functions, design for resilience ALONGSIDE prevention. Do not choose between them.

**The hypothesis:** We believe that **systems designed for resilience will recover from breaches in hours to days** instead of weeks, because damage is isolated, manual operations are planned, and backups are tested.

**The 3E decision:**
- **Explore:** Run the 48-hour test scenario (2-3 weeks). Do we stay functional manually? If not, this is urgent.
- **Exploit:** If test fails, build resilience layer by layer (isolation, fallback, communication, recovery testing) over next quarter.
- **Exit:** If cost of resilience exceeds cost of breach (rare), accept the risk and document why. Make it an explicit business decision.

**The key trade-off:** We're choosing tested recovery over theoretical prevention. Resilience takes work upfront; it pays back in hours of downtime prevented.

**The biggest risk:** That you build resilience planning but never test it. Untested plans fail in real crises. Test quarterly, every quarter.

**Assumptions to watch:**
1. Manual processes are actually faster than digital processes during crisis (test this — sometimes they're slower and that's okay)
2. Team can execute manual process under stress (simulate actual incident — chaos affects performance)
3. Backup data is accurate and current (check before crises, not during)

**The next action:** Conduct a 48-hour resilience scenario test (1 day of planning, 1 day of execution, 1 day of debrief). Document what breaks. Prioritize fixes.

## GENERATE THE DELIVERABLE

Use the output prompt from the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md).
If this skill connects to downstream skills, also generate the markdown handoff file (if relevant to business continuity strategy or incident response planning).

## VISUAL SUMMARY

After completing the primary output, invoke the excalidraw-svg skill to create a single Excalidraw SVG visual summary showing:
- The five resilience dimensions (Isolation, Degradation, Manual fallback, Communication, Recovery) with examples
- System isolation map (network boundaries, data segregation, team access tiers)
- Recovery timeline (Tier 1 systems back online in 2 hours, Tier 2 in 8 hours, Tier 3 in 24 hours)
- Manual operation process flow (without digital systems — sequence of steps)
