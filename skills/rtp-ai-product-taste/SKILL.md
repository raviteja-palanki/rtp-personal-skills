---
name: ai-product-taste
version: v1.2_latest
description: 'Calibrate the quality bar for an AI feature against your specific domain, users and price point, not against benchmark scores. Exceptional AI products are domain-calibrated, not generically excellent: ''good'' is a domain word, not a benchmark number. The trap is technically-correct-but-feels-wrong: factually accurate, grammar-perfect, zero hallucinations, and users still say ''this sucks'', because you optimized for metrics instead of taste (accuracy ≠ usefulness; fluency ≠ trustworthiness). Design the magic moment and put taste examples in your evals. Use when output looks impressive but feels mediocre, when the team can''t say what ''good enough'' means, or when judging ship-now vs. raise-the-bar. Pairs with: eval-framework (taste sets the bar, evals measure it), jtbd-analysis (the job vs. the quality bar), ai-product-metrics (acceptance/correction as taste signals), confidence-tuner (honest-about-uncertainty). Triggers: ''is this good enough'', ''the output is impressive'', ''quality bar'', ''ship or polish''.'
imports:
  - first-principles
  - dual-lens
---

# AI Product Taste

**The objective:** calibrate the quality bar for an AI feature to *your* domain, users, and price point — not to benchmark scores — for the team whose output looks impressive and still feels mediocre. Taste is the difference between a product users tolerate and one they love.

## The one idea

Your model output is factually accurate. Grammar perfect. No hallucinations. The eval scores are strong. And users say "this sucks."

That sentence is the whole problem, and here is why it happens: **you optimized for metrics, and metrics are not taste.** Accuracy is not usefulness (factually correct but verbose, over-qualified, unhelpful). Fluency is not trustworthiness (polished prose hides uncertainty). Comprehensiveness is not signal (a wall of detail when the user wanted one clear answer). You hit every number and missed the thing the number was supposed to stand for.

The core idea is that **"good" is a domain word, not a benchmark number.** Exceptional AI products are *domain-calibrated*, not *generically excellent*. What "excellent" means for a legal-research tool (precise citations, conservative, flags its own uncertainty) is not what it means for a creative-writing tool (voice-matched, surprising, emotionally resonant) — and neither is captured by "92% accuracy." The PM with taste builds the bar around what experts *in the domain* call excellent, what corner cases would destroy trust even if rare, and what the price point allows — then optimizes for *that*, not for the leaderboard.

And bad taste is invisible in your dashboard, which is what makes it dangerous: you can't measure it directly. Users just… leave. NPS stays mediocre. You ship features and nothing moves the needle. Bad taste isn't a bug — it's the compounding result of prioritizing the wrong metrics, and it only shows up as absence.

## How to use this skill

1. **Calibrate to the domain** — research what "excellent" means to experts *in the domain* (not to AI people), the cost of failure, and the error asymmetry. (Step 1.)
2. **Design the magic moment** — the one experience that converts a skeptic to a believer, and calibrate the bar to the price point. (Steps 2–3.)
3. **Sense, then institutionalize** — use the product yourself, watch what users edit vs. accept, then write the taste spec and put taste examples *in the eval rubric* so the bar is testable, not aspirational. (Steps 4–5, and the handoff to `eval-framework`.)

## KEY TERMS (plain language)

- **Product taste** — a calibrated sense of what "good" means for *this* product, in *this* domain, at *this* price — the thing that decides whether users love it or merely tolerate it.
- **Domain calibration** — building the quality bar from what domain experts call excellent, not from generic AI metrics.
- **The magic moment** — the single experience that converts a skeptic into a believer ("I didn't think of this pattern, but I trust it works"); not comprehensiveness, speed, or polish.
- **Error asymmetry** — in a given domain, a false positive and a false negative cost differently; the bar must reflect which one destroys trust.
- **Price-point calibration** — matching the quality bar to what users pay (a free tier tolerates more error than a $500/month tier); over-building wastes compute, under-building destroys trust.
- **Framing (museum-quality)** — the quality bar you *communicate to the model* in the prompt; "this will be exhibited as the best of its kind" activates different output than "be helpful."
- **Evidence tiers used below** — ◆ vendor-disclosed · ⚠ practitioner estimate. The acceptance-lift and price/accuracy numbers below are ⚠ illustrative — teaching devices to test in your context, not measured constants.

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../../../UNIVERSAL-SKILL-PROTOCOL.md). At minimum: name the domain and the user, and answer the diagnostic — *can you articulate what "good enough" means in domain terms, or are you launching whatever the model produces?* If the honest answer is the latter, that gap is the work. Then route depth and output format.

## THE TRAP — technically correct but feels wrong

You will optimize for the metrics you can see and miss the taste you can't. The four confusions that produce impressive-but-mediocre output:

- **Accuracy ≠ usefulness** — factually correct but verbose, over-qualified, unhelpful.
- **Fluency ≠ trustworthiness** — polished output can hide the uncertainty the user needed to see.
- **Speed ≠ value** — a fast wrong answer rarely beats a slow right one.
- **Comprehensiveness ≠ signal** — overwhelming detail when the user wanted simplicity.

Domain-specific taste means understanding what *this* user cares about (not what the model does well), which corner cases destroy trust (even if rare), what the price point allows, and what the competitive bar is *in this domain*.

## THE PROCESS

**1. Calibrate to the domain.** Research it deeply: where do users get this done today (manually, other AI, consultants)? What do they consider excellent *in the domain*, not in AI? What's the cost of failure (wrong legal advice is catastrophic; a wrong restaurant pick is annoying)? What's the error asymmetry? Build the bar around domain expectations, not AI capabilities.

**2. Design the magic moment.** The one experience that makes users go "wow" — and it's rarely comprehensiveness, speed, or fluency. It's usually: *exactly right, no padding · honest about uncertainty ("60% confident, here's why") · immediately actionable · a surprising, correct insight.* For coding: "I didn't think of this pattern, but I trust it works." For analysis: "Oh — that's the real problem, not what I thought."

**3. Calibrate to the price point** (⚠ illustrative thresholds — set your own): a free tier can tolerate more error; a $20/month tier must be insightful and reliably accurate; a $500/month tier must be domain-expert-level or irreplaceable. Over-building wastes compute; under-building destroys trust.

**4. Build taste through iterative sensing.** Use the product yourself for a real task in the domain. Talk to power users in the domain (not tech people talking about AI). Watch which corners they still do manually — that's where your AI fails taste. A/B test output styles, lengths, and confidence markers, and track which variants users *trust*, not which are most accurate.

**5. Institutionalize it.** Write down what "good taste" means for this product (domain-specific, with good/bad examples), the failure modes that destroy trust, and the magic moment — then **put taste examples in the eval rubric** ("did this output feel like it came from someone who understands this domain?"). This is the handoff to `eval-framework`: taste defines the bar; evals hold the line on it.

**Domain taste decision table** — calibrate against domain reality, not generic metrics:

| Domain | What "good" means | Fatal failure | Acceptable imperfection | Quality bar |
|---|---|---|---|---|
| Legal | Precise citations, conservative, flags uncertainty | Hallucinated case law | Verbose explanations | Expert-level or don't ship |
| Healthcare | Evidence-based, hedged, recommends a professional | Confident wrong diagnosis | Missing a rare condition | Clinical-grade |
| Creative writing | Voice-matched, surprising, resonant | Generic/template feel | Occasional awkward phrasing | "Better than I'd write" |
| Code assistance | Correct, idiomatic, explains tradeoffs | Compiles but has a security bug | Slightly non-idiomatic style | "I trust this to run" |
| Customer support | Empathetic, action-oriented, escalates well | Dismissive or wrong resolution | Slightly formal tone | "Resolved my issue" |
| Data analysis | Accurate, caveated, actionable | Wrong numbers, stated confidently | Missing one data source | "I'd show this to leadership" |

**The framing lever (museum quality).** Anthropic's harness work found that setting the bar to "museum quality" vs. "good enough" changed agent output dramatically (◆ Anthropic engineering write-up). The quality bar you *communicate to the model is itself product taste*: "be helpful" activates one output distribution; "this will be exhibited as the best example of its kind" activates another. Test framing words and measure the acceptance difference (⚠ illustrative lifts — "produce expert-level output" ~+8%, "this will be shown to your CEO" ~+15%; measure your own). *The craft of writing those prompts lives in `prompt-craft`; the decision about what bar to express is taste.*

## THE ONE-WEEK RECALL PROBE — a cheap instrument for the thing this skill argues about

This skill argues that technically-correct output can still feel wrong, and that argument is easy to make and hard to instrument. Here is an instrument, borrowed from experience design, that costs one message and settles a lot of debate.

**The probe.** A week after someone used the feature, ask them to describe it. Then ask one question of their answer:

**Did their recall center on the spectacle, or on the significance?**

- **Spectacle recall** sounds like: it was fast, it was impressive, it wrote the whole thing, the animation was nice. The person is describing the *machine*.
- **Significance recall** sounds like: it caught something I would have missed, it saved me the argument with legal, I sent it as-is. The person is describing *what changed for them*.

**Spectacle-only recall a week later is a design failure, not a marketing gap**, and it is the specific failure this skill exists to catch. It reliably shows up in products with excellent demo metrics.

**Why a week, and why not a survey.** Immediately after use, everyone reports the spectacle, because that is what is salient. At a week, only the things that changed something survive. And an open recall question beats a rating scale here for a structural reason: a scale supplies the dimension, so it tells you how they felt about the thing you already thought mattered. Recall tells you which thing mattered.

**One honest limit.** Some genuinely good products are legitimately invisible in recall, because they removed a step rather than adding a result. If the feature's job is to make something stop happening, ask about the absence directly, and do not read a blank as a failure.

**Where it fits the audience question.** People accept AI most readily where it produced something with **no non-AI version**, and resist it where it displaced a human-made thing they can compare against. Significance recall is what you get in the first case. If the recall keeps landing on spectacle, check whether you have built the second case: a thing whose non-AI version the user still remembers and preferred.

*(Source: the recall probe is HBR, Nunes & Heimann, "Why the Best Immersive Experiences Succeed," Aug 2026 — ⚠ framework-tier, prescriptive, no validation data for the probe itself. Adapted here from museum and live-experience design to AI surfaces, which is this corpus's move. Pairs with `rtp-ai-ux-patterns` section 8, the sequencing law, where meaning-making is the sixth and last stage and therefore the one most often capped by an unfixed earlier failure. Ledger pattern X.)*

## THE PROVEN-BETTER-NEW DISCIPLINE — pick your one bet, copy the rest

Teams with real innovation budget still spend it badly: they spread it thin across every surface instead of concentrating it where it counts. Zynga co-founder Mark Pincus describes a working discipline for this on HBR IdeaCast. For any feature, name the single dimension you are actually trying something new on, and for everything else, copy the best existing implementation you can find. Don't reinvent onboarding, checkout, or navigation because the product you're building has a different, specific idea at its core.

**The rule.** Name your one innovation dimension before you start building. Everything that isn't that dimension gets the best-known pattern in the category, not a fresh design.

**The mechanism.** Innovation budget, meaning design and engineering time, is finite. Spread it across several "let's rethink this too" surfaces and each one gets a fraction of the attention a proven pattern already had behind it. The surfaces that carry no novelty end up shipping worse than the boring, copied version would have. Pincus's worked example: two competing social games died on unbuilt onboarding, not on the genuinely novel features they were racing to ship. Onboarding wasn't the bet. It ate the budget anyway.

**Where it breaks.** This is a heuristic from one founder's retrospective account on a podcast, not a controlled comparison. A case where broad, unfocused innovation beat a single-bet-plus-copy-the-rest approach on a comparable product, with an outcome measure attached, would break this claim. No such case appears in this source. Treat "pick one bet" as a discipline to test in your own context, not a validated finding.

**The user-stupidity asset warning.** A related trap from the same discipline: your own fluency with the product decays your read on what users need. Whoever builds the product gets faster at using it than any first-time user ever will, and that gap compounds within roughly a quarter, until the builders can no longer predict where a naive user actually gets stuck. This deepens the "invisible until it's absence" problem this skill already names: for AI products specifically, the failure hides inside a metric that looks fine. A user who typed a bad prompt and got a weak answer still generated a "completed" interaction. Nothing in your completion rate flags it. Budget for watching someone genuinely new to the product, on a cadence, because your own sense of what's obvious keeps drifting away from theirs.

*(Source: HBR IdeaCast, Mark Pincus interview, Jul 2026. Tier: ⚠ unverified anecdote, entirely survivorship-selected. Pincus's claims about which decisions caused which outcomes at Zynga are not audited data and should not be cited as such. The discipline and the user-stupidity-asset mechanism are worth testing on their logic even though the source that names them is not evidence.)*

## PORTFOLIO VS. DEPTH — is this judged as best-of-many or the one that matters?

Not every output category responds to AI assistance the same way, and the reason isn't the model, it's the structure of what "good" means for that category. HBR's Cold Call podcast, discussing the Atlantic's licensing deal with OpenAI, surfaces a distinction worth building into your taste diagnostic directly.

**The rule.** Ask whether the thing you're building is portfolio-structured or depth-structured. Portfolio-structured output has its value in the best of many draws: generate many variants and ship whichever tests best, and nobody cares that the rest were mediocre. Depth-structured output has its value in one artifact's singular quality, a single investigative feature or a single legal brief that has to be right and distinctive on its own, with no second draw to hide behind.

**The mechanism.** The same generation technology helps the first category and flattens the second. More draws genuinely raise the best-of-many ceiling, so portfolio-structured work gets a real lift from AI assistance. Depth-structured work doesn't get more draws. It gets one shot, and a model-assisted shot tends toward the model's central tendency: competent, on-genre, and indistinguishable from what anyone else generating from the same model would produce. The same technology is a gift or a threat, decided entirely by which structure you're building for, not by how capable the model is.

**Where it breaks.** A depth-structured category, a single essay, a single piece of reporting, a single legal argument, where AI assistance measurably improved that one artifact's distinctiveness instead of flattening it toward the mean, would break the homogenization half of this claim for that category. This source names the pattern without offering that counter-case.

*(Source: HBR Cold Call podcast, Caroline Elkins interview on the Atlantic/OpenAI licensing arrangement, Jul 2026. Tier: ⚠ podcast transcript, no disclosed deal terms; the licensing specifics are not independently verifiable from this source. The portfolio-vs-depth distinction is the reusable part; the deal commentary around it is not.)*

**Add to your taste spec:** before you set the quality bar, name which structure you're building. A portfolio-structured feature can lean on AI's breadth. A depth-structured one needs the taste spec to actively defend against the model's default output, because "on-genre and safe" is exactly what depth-structured taste has to beat.

## WHERE THIS SKILL MEETS THE REST OF YOUR STACK

Taste decides *what good means*. Trace where that bar travels: it becomes eval cases, and those eval cases are what a trust curve later proves right or wrong.

**Where the bar gets set and held:**
- **`rtp-eval-framework` / `rtp-eval-driven-development`** — taste sets the bar; evals *measure against it and hold the line*. The taste spec's magic-moment and fatal-failure definitions become eval cases. Without this handoff, taste stays aspirational.
- **`rtp-confidence-tuner`** — "honest about uncertainty" is a core taste element; this designs the trust signals that express it without over- or under-warning.
- **`rtp-prompt-craft`** *(boundary)* — owns the craft of *writing* prompts; taste owns the *decision* of what quality bar to express in them (the framing lever above).

**The distinct-but-adjacent question:**
- **`rtp-jtbd-analysis`** *(distinct objective)* — JTBD names *what job* the user hires the AI for; taste calibrates *how good the output must feel* to do that job. Different questions; run JTBD first.

**Where a taste gap becomes visible, two hops downstream:**
- **`rtp-ai-product-metrics`** — acceptance, correction, and regeneration rates are the *measurable shadow* of taste; low acceptance despite high accuracy is the immediate signature of a taste gap.
- **`rtp-fit-signal`** — taste's own open loop, closed. This skill warns that a taste gap is *invisible until it's absence* (churn, flat NPS) — fit-signal's trust curve is the instrument that catches that absence weeks later. A strong eval score with a trust curve that never inflects is a taste gap the dashboard hid. Feed the magic moment into fit-signal's magic-moment cohort measurement so it tests the right thing.

**Imports (run before setting a bar):**
- **`rtp-first-principles`, `rtp-dual-lens`** *(imports)* — strip the feature to its atomic job before setting a bar; translate the bar so business and engineering mean the same "good."

## DIAGNOSTIC QUESTIONS

- **Can you describe what "excellent" means in your domain — specifically, not "accurate and helpful"?**
- **What's the error asymmetry — is a false positive worse than a false negative here?**
- **What would make a user say "wow, that's useful" (not "wow, that's technically impressive")?**
- **Have you used your own product for a real task in the domain?**
- **Do you know which outputs users edit vs. accept as-is — and which segment has the lowest acceptance?** That segment is where your taste is worst.
- **Is the thing you're building judged as "best of many" or "the one that matters"?** Portfolio-structured output gets a real lift from AI assistance; depth-structured output tends to flatten toward the model's default unless the taste spec actively defends against it.

## REALITY CHECK

- **Mature taste** looks like: you can state the bar in domain terms; you know the magic moment; users accept 80%+ of outputs because they *feel right*, not because accuracy is high; power users build workflows around your AI; you optimize for domain corner cases, not benchmarks.
- **It is NOT**: "our accuracy is 92%" (good for *this* domain?); high variance in acceptance across segments; users comparing you to generic AI instead of domain alternatives; an eval rubric that's generic; a team that hasn't used its own product.
- **Bad taste is invisible until it's absence** — you won't see it in a metric, you'll see it in churn and a flat NPS. Instrument acceptance by segment so it stops being invisible.

## QUALITY GATE

- [ ] Domain calibration — you understand "good" in this domain, not generically
- [ ] Magic moment identified — the one experience that converts skeptics
- [ ] Price-point appropriateness — the bar matches what users pay
- [ ] Error asymmetry understood — which failure destroys trust most here
- [ ] Corner-case inventory — the 5–10 failures that would destroy trust
- [ ] Taste examples in the eval rubric (not just accuracy metrics) — the eval-framework handoff is made
- [ ] User acceptance tracked by segment, with low-acceptance cases investigated

## WHEN WRONG

- Users say "the AI is good, but I wouldn't pay for this" — the bar isn't calibrated to the price point.
- High accuracy but low acceptance — technically correct, feels off (the core signature).
- Power users leave for a smaller competitor with better taste for their niche.
- NPS plateaus — you've taken the low-hanging fruit and can't reach mainstream.
- Users compare you to humans in the domain, not to other AI — and you lose.

**Recovery:** research where top users do this manually and what they'd pay for; analyze the pattern in rejections; inventory your worst corner cases; rebuild the bar domain-first, not metric-first; iterate output *style* (feel, not accuracy); re-test with power users; align pricing to the bar you've established.

## OUTPUT FORMAT

```
## Taste Spec: [Product / Domain]

Domain calibration:  "good" means [domain-specific] · fatal failure [the one trust-destroyer] · acceptable imperfection [what users forgive] · quality bar [in the user's words, not metrics]
Magic moment:        [the experience that converts skeptics]
Error asymmetry:     [false positive vs. false negative — which costs more here]
Price–quality:       | tier | price | quality bar | compute budget |
Corner-case inventory: [the 5–10 failures that would destroy trust]
Framing test:        A [text] → [acceptance %] · B [text] → [acceptance %] · winner
Acceptance by segment: | segment | acceptance | pain point | taste gap |
```

## TRADE-OFF LEDGER

By calibrating to the domain instead of the benchmark, you bet that users judge you against domain alternatives (a human expert, a specialist tool), not against generic AI — and that "feels right here" beats "scores high everywhere." You give up the clean, defensible benchmark number and the comfort of a generic bar. **Reversible?** Yes — it reshapes what you optimize, not your architecture. **The hidden trade:** taste is invisible in dashboards, so the failure mode is *complacency* — a strong eval score masking a churning user base; the fix is instrumenting acceptance by segment so the gap becomes visible. **Confidence: High** — domain calibration is what separates loved AI products from tolerated ones. What would change it: a genuinely generic, low-stakes utility where users really do compare you to other AI on a benchmark.

## CONCLUSION

Follow the Conclusion Protocol from the [Universal Skill Protocol](../../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 5: state the recommendation (the domain-calibrated quality bar and whether to ship or raise it), name the key trade-off (domain fit vs. benchmark defensibility), acknowledge the biggest risk (a strong eval score hiding a taste gap), and define the next action (write the taste spec, put its cases in the eval rubric, instrument acceptance by segment).

## VISUAL SUMMARY

After the primary output, invoke the **excalidraw-svg** skill for one visual: two axes — technical quality (accuracy/fluency) rising on one, perceived value (does it feel right in the domain?) on the other — with the "impressive but mediocre" gap shown where technical quality is high and perceived value is low, and the magic moment marked as the point that closes it. So a viewer sees that taste, not accuracy, is the axis that decides love. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.
