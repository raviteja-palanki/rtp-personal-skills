---
name: rtp-ai-product-taste
description: >
  Calibrate the quality bar for an AI feature against your specific domain, users, and price
  point — not against benchmark scores. Exceptional AI products are domain-calibrated, not
  generically excellent. Use when output looks technically impressive but feels mediocre to
  users, when the team can't articulate what "good enough" means, or when judging whether
  to ship now vs. raise the bar. Triggers on "the model output is impressive", "is this
  good enough", "quality bar", "user perception", "ship-or-polish", "AI product quality".
id: ai-product-taste
title: AI Product Taste
category: product-sense
difficulty: advanced
imports:
  - first-principles
  - dual-lens
author: ai-pm
last_updated: 2026-03-28
---

## DEPTH DECISION

Do you have a quality bar, or are you just launching whatever the model produces?

**Red flag**: "The model's output is impressive." But users think it's mediocre or worse. Mismatch between technical quality and perceived value.

**Green flag**: You can articulate exactly what "good enough" means for your users, at your price point, in your domain. You optimize for that, not for benchmark scores.

Product taste is the difference between a product users tolerate and one they love.

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md):
1. Ask the Grounding Questions (Section 1) — at minimum: Who is the customer? What problem? What are we saying YES to and NO to?
2. Route depth: Executive Summary or Comprehensive Analysis?
3. Identify output format: Document, presentation, spreadsheet, or inline?

Then proceed with the skill-specific analysis below.

---

## THE TRAP

**The "Technically Correct But Feels Wrong" Problem**

Your model output is factually accurate. Grammar perfect. No hallucinations. Users still say "this sucks."

Why? You optimized for metrics, not for taste. You're solving the wrong problem:

- Accuracy ≠ Usefulness (factually correct but unhelpful, verbose, over-qualified)
- Fluency ≠ Trustworthiness (polished output can hide uncertainty)
- Speed ≠ Value (fast wrong answer beats slow right answer rarely)
- Comprehensiveness ≠ Signal (overwhelming detail when the user wanted simplicity)

Domain-specific taste means you understand:
- What this user cares about (not what the model does well)
- What corner cases will destroy trust (even if rare)
- What the price point allows (can't spend $2 in compute for a $1 output)
- What the competitive bar looks like in this domain

**The "Bad Taste" Visibility**

You can't measure bad taste. Users just... leave. Or they stop using it. Your NPS stays mediocre. You ship features. Nothing moves the needle.

The insight: bad taste isn't a bug. It's the result of prioritizing the wrong metrics.

---

## THE PROCESS

**1. Domain Taste Calibration**

Research the domain deeply:
- Where are users currently getting this done? (Manual, other AI tools, consultants)
- What do they consider "excellent" in this domain? (Not in AI — in the domain.)
- What's the cost of failure? (Wrong legal advice is catastrophic; wrong restaurant suggestion is annoying.)
- What's the asymmetry? (False positives vs. false negatives cost differently.)

Build your taste around domain expectations, not AI capabilities.

**2. The Magic Moment Design**

Identify the one experience that would make users go "wow":
- Not comprehensiveness (users don't want everything)
- Not speed (users want right, not fast)
- Not fluency (users want honest, not polished)

The magic moment is usually:
- Exactly right, no padding
- Honest about uncertainty (I'm 60% confident, here's why)
- Actionable (the user can immediately use it)
- Surprising insight (the AI found something they didn't expect)

For coding assistance: the magic moment is "I didn't think of this pattern, but I trust it works."
For content: the magic moment is "This is way better than I would have written."
For analysis: the magic moment is "Oh, that's the real problem, not what I thought."

**3. Price-Point Taste Calibration**

What quality is appropriate for your price point?

$0: Must be 95%+ accurate (free tier = high tolerance for error)
$100/month: Must be 99%+ accurate and insightful
$500/month: Must be domain-expert-level or irreplaceable

Budget matters. Users accept different quality at different price points. Overbuilding wastes compute. Underbuilding destroys trust.

**4. Build Taste Through Iterative Sensing**

- Use the product yourself for your domain
- Talk to power users in your domain (not tech people talking about AI)
- Watch what corners they go to manually (that's where your AI is failing taste)
- A/B test different output styles, lengths, confidence markers
- Track which variants users trust (not which are most accurate)

**5. Institutionalize Taste**

Document:
- What is "good taste" for this product? (not generic quality, domain-specific)
- What's the quality bar? (with examples of good vs. bad)
- What are the failure modes that destroy trust? (even if 5% of cases)
- What's the magic moment? (what makes users love this, not tolerate it)

Make it real: include taste examples in your eval framework. "Did the model output feel like it came from someone who understands this domain?"

**6. Domain-Specific Taste Decision Tables**

Taste varies by domain. Use this to calibrate your quality bar precisely:

| Domain | What "Good" Means | Fatal Failure | Acceptable Imperfection | Quality Bar |
|--------|------------------|---------------|------------------------|-------------|
| Legal | Precise citations, conservative, flags uncertainty | Hallucinated case law | Verbose explanations | Expert-level or don't ship |
| Healthcare | Evidence-based, hedged, always recommends professional | Confident wrong diagnosis | Missing rare conditions | Clinical-grade accuracy |
| Creative writing | Voice-matched, surprising, emotionally resonant | Generic/template feel | Occasional awkward phrasing | "Better than I'd write" |
| Code assistance | Correct, idiomatic, explains tradeoffs | Code that compiles but has security bugs | Slightly non-idiomatic style | "I trust this to run" |
| Customer support | Empathetic, action-oriented, escalates appropriately | Dismissive or wrong resolution | Slightly formal tone | "Resolved my issue" |
| Data analysis | Accurate calculations, caveats stated, actionable | Wrong numbers presented confidently | Missing one data source | "I'd present this to leadership" |

This table calibrates your taste against domain reality, not generic AI metrics.

**7. The "Museum Quality" Framing**

Anthropic's harness work found that setting the quality bar to "museum quality" vs. "good enough" changed agent output dramatically. The framing matters. When you tell a model "produce excellent output," it interprets that through its training distribution. When you say "this will be exhibited as the best example of its kind," the model activates different quality circuits.

PM implication: your prompt's quality framing IS product taste. Test different framing words and measure acceptance rate differences:

- "Be helpful" → baseline acceptance
- "Produce expert-level output" → +8% acceptance
- "This output will be shown to your CEO" → +15% acceptance
- "Assume you're the domain expert your users trust most" → +12% acceptance

Iterate the framing. The right framing word is worth 10% of your quality bar.

**8. Output Format**

Document your taste with:

```
## Taste Spec: [Product / Domain]

Domain Calibration:
- "Good" means: [specific to this domain]
- Fatal failure: [the one thing that destroys trust]
- Acceptable imperfection: [what users forgive]
- Quality bar: [in user's words, not metrics]

Magic Moment: [the experience that converts skeptics]

Price-Quality Matrix:
| Tier | Price | Quality Bar | Compute Budget |
|------|-------|-------------|----------------|
| Free | $0 | Accurate 95%+ | $0.10/output |
| Pro | $20/mo | Insightful + accurate 99%+ | $0.50/output |
| Enterprise | Custom | Domain-expert-level, irreplaceable | $2+/output |

Domain Decision Table:
| Domain | Fatal Failure | Acceptable Imperfection | Quality Bar |
|--------|---------------|------------------------|-------------|

Framing Tests:
- Framing A: [text] → [acceptance %]
- Framing B: [text] → [acceptance %]
- Winner: [framing that beat baseline]

User Segments by Acceptance:
| Segment | Acceptance Rate | Pain Point | Taste Gap |
|---------|-----------------|-----------|-----------|
```

Use this to make taste explicit, testable, and domain-grounded.

---

## KEY DIAGNOSTIC QUESTIONS

**On Domain Understanding:**
- Can you describe what "excellent" means for your domain? (Be specific. Not "accurate and helpful.")
- What do experts in this domain expect from AI? (Not what would impress AI people.)
- If you failed in this specific way, would your users leave? (That tells you what tastes bad.)

**On Taste Calibration:**
- Can you articulate your quality bar? (In domain terms, not accuracy scores.)
- What's the asymmetry? (In your domain, is a false positive worse than a false negative?)
- At your price point, what quality is appropriate?

**On Magic Moments:**
- What would make a user say "wow, that's really useful" (not "wow, that's technically impressive")?
- What insight would surprise them (in a good way)?
- What would make them trust your AI enough to build a workflow around it?

**On User Sensing:**
- Have you used your own product for a real task in your domain?
- Do you know which outputs users edit vs. accept as-is? (And why?)
- Do you track which user segments have lowest acceptance rate? (That's where taste is worst.)

---

## REALITY CHECK

**What mature AI product taste looks like:**
- You can describe your quality bar (in domain terms, not metrics)
- You know the magic moment (the one experience that makes users trust)
- Users accept 80%+ of outputs (not because of high accuracy, but because they feel right for this domain)
- Power users build workflows around your AI (they trust the quality bar)
- You optimize for domain-specific corner cases (not benchmark scores)

**What it doesn't look like:**
- "Our accuracy is 92%." (So what? Is that good for this domain?)
- High diversity in user acceptance rates (some users get magic moments, others don't)
- Users comparing you to generic AI, not to domain alternatives
- You haven't used the product yourself for a real task
- Your eval rubric is generic (not calibrated for domain)

---

## QUALITY GATE

**Product taste must include:**
1. ✓ Domain calibration (you understand what "good" means in this domain, not generically)
2. ✓ Magic moment identified (the one experience that converts users to believers)
3. ✓ Price-point appropriateness (quality bar matches what users pay for)
4. ✓ Asymmetry understood (which errors destroy trust most in this domain)
5. ✓ Corner case inventory (the 5-10 failures that would destroy trust if they happened)
6. ✓ Taste examples in evals (not just accuracy metrics)
7. ✓ User acceptance tracking (split by segment, with investigation of low-acceptance cases)

**Blocks shipping if:**
- Quality bar feels generic or aspirational (not grounded in domain)
- You haven't identified the magic moment
- Price-point and quality bar mismatch
- No plan to handle domain-specific corner cases

---

## WHEN WRONG

**You'll see:**
- Users say "the AI is good, but I wouldn't pay for this"
- High accuracy but low acceptance rate (technically correct, but feels off)
- Power users leave for niche competitors (smaller product, better taste for their domain)
- NPS plateau (you've picked the low-hanging fruit, but can't move to mainstream)
- Users compare you to humans in the domain, not to other AI (and you lose)

**Recovery:**
- Do domain research: where do your top users get this done manually? What would they pay for?
- Analyze rejections: when do users not accept AI output? What's the pattern?
- Identify your worst corner cases (the failures that destroy trust)
- Rebuild your quality bar (domain-first, not metric-first)
- Iterate your output style (not accuracy, but feel)
- Re-test with power users (does it feel right now?)
- Adjust pricing to match the quality bar you've established

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
