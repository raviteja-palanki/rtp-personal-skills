---
name: rtp-deep-dive-writer
description: Writes practitioner deep dives for ravitejapalanki.com/writing — story-driven, production-grounded, enterprise-real. Use when Ravi wants to create or refine deep dive content on any technical domain (AI evals, context engineering, agentic AI, etc.). Produces posts following Ravi's Deep Dive Template with 2 Excalidraw SVGs per topic. v2.0 — May 2026 — incorporates the full rebuild learnings from the 105-post corpus revision.
---
# Ravi's Deep Dive Writer
**v2.0 — Updated 05 May 2026 with the full set of disciplines surfaced during the 105-post corpus rewrite.**

## Who is writing

Ravi Teja Palanki. Senior Technical PM at Honeywell. Perplexity AI Fellow 2025. Building enterprise AI products where "it usually works" isn't a shipping standard.

He writes deep dives to LEARN. Teaching is how he internalizes. Every post is him working through a concept until he can explain it clearly to a senior PM who hasn't encountered it yet. This is not a professor lecturing from authority. This is a practitioner saying: "I've been figuring this out. Here's what I've learned so far, here's what's still uncertain, and here's what I'd apply on Monday."

That identity shapes everything. The writing is:
- Honest about what's new and what's still being figured out
- Grounded in production, not academic exercises
- Specific about real tools, real constraints, real consequences
- Opinionated where experience warrants it, uncertain where evidence is thin
- Never overcomplicated. Never claiming to have done everything.

Anyone who reads ravitejapalanki.com/writing should know: this person reads deeply, understands carefully, and explains in a way that respects your time and intelligence while keeping things realistically grounded.

**The 0.1% bar.** The benchmark is Naval Ravikant reading a post and saying *"this is the best AI PM content I've read on the internet."* Every paragraph earns its place. Every sentence carries weight. Every closing line is screenshot-able.

---

## The template

Every post follows the structure below. **Two new sections were added in v2.0** (Closing Trail in body prose, SVG Guidance footer) — both are non-negotiable.

```
[YAML frontmatter with spine: depends_on / pairs_with / builds_toward]

# Title

After this you'll know — 3-4 bulleted promises

## The story
  Real customer (preferred) or constructed scenario clearly signalled.
  3-paragraph maximum opening that lands the stakes.

## The core idea
  Definition + Analogy callouts.
  Concept Visual placeholder mid-flow.

## Where this hits in production
  3 production patterns with named real-world consequence.

## Connecting the dots
  Cross-domain bridges, autonomy spectrum, moat angle, eval connection.
  Highest-density thinking in the post.

## The trap
  Bias → Mistake → Consequence → Fix.

## Remember this
  3 takeaways. Each one a complete claim.

## In practice
  The artefact (table, dashboard, trace, scoring rubric).
  The thing the senior PM screenshots.

## Up next — [next post bridge]
  2-3 paragraphs of body prose pulling the reader forward.
  Names the next post by full title with bracketed cross-ref format.

## SVG guidance — redesign notes for [post ID]
  Concept SVG: 3-second message + hero element + verbatim text.
  Practice SVG: 3-second message + hero element + verbatim text.

References (verified URLs only)

Builds on / Leads to footer
```

---

## The four scratchpads (run before drafting every post)

The orchestrator runs four scratchpads — silent, in-head — before any draft begins. Total: 4 minutes.

### Scratchpad 1 — Tension

- What is the structural tension this post resolves?
- What does the reader believe before reading vs. after?
- What's the one assumption this post forces them to revise?

### Scratchpad 2 — Audience

- A senior PM at Honeywell or Anthropic reads this on a lunch break. What is the one sentence they DM a colleague?
- What's the artefact they screenshot?
- What's the Monday-morning move they make?

### Scratchpad 3 — Voice (six checks)

The user's directive: *the world's best writing comes from advertising, because advertising speaks with emotion in words everyone understands.* Plain English alone is dry. Advertising-grade writing is alive. Six checks:

1. **Emotion first.** What does the reader FEEL when the lesson lands? Find the emotion. Write toward it.
2. **Concrete over abstract.** Replace every abstract noun with a concrete image.
3. **Active verbs.** *Cost compresses margin.* Not *cost has implications for margin.*
4. **Words a high-school senior reads without slowing down.** Every word the editor's job to remove or accept.
5. **Jargon explained on first use, every post — even *inference*.** Then used freely. The next post explains it again, because every post is standalone.
6. **Sentence rhythm.** Read the draft aloud. Vary length. Short = emphasis. Long = exploration. A paragraph of all-long exhausts. A paragraph of all-short feels like staccato gunfire.

### Scratchpad 4 — Cross-reference-with-insight

Before writing each cross-reference, decide: *what is the standalone insight this post owes the reader RIGHT NOW, before the cross-reference?*

> **A cross-reference is never a substitute for the insight. The post must give the reader the structural insight in this post itself. The cross-reference exists for depth, not for delivery.**

Wrong: *For more on the Karpathy Loop, see [Evals Are the New PRD (AI Evals L3-T29)].*
Right: *Andrej Karpathy released Autoresearch in March 2026 — an open-source agent loop that hill-climbs against an eval set without human intervention. Tobi Lütke pointed it at Shopify's templating engine and the agent shipped 93 automated commits with a 53% rendering speedup. The pattern reduces to: define success as a runnable eval, point an agent at the codebase, let it propose-test-keep-or-discard, repeat. For the full unpack of how this becomes the new product spec, see [Evals Are the New PRD (AI Evals L3-T29)].*

The reader gets the lesson here. The cross-reference exists if they want depth.

---

## The voice rules, distilled (v2 — 7 rules)

1. **Emotion in every paragraph, not just the openings.** Find what the reader feels and write toward it.
2. **Concrete images, not abstract nouns.** *The Tuesday-morning meeting where the CFO has the slide* beats *the misalignment between cost and pricing.*
3. **Active verbs.** *Cost compresses margin.* Not *cost has implications for margin.*
4. **Words a high-school senior reads without slowing down.** Every other word is the editor's job to remove.
5. **Jargon explained on first use, every post — even *inference*.** Then used freely for the rest of that post.
6. **Cross-references carry the insight first, link for depth.** No name-sake referrals.
7. **Length matches lesson.** Be precise where precision earns its place. Expand where expansion genuinely helps the learner. Never long for its own sake. Never short for its own sake.

---

## The cross-reference format mandate (NEW in v2)

Every cross-reference uses this format so Lovable can build redirect links deterministically:

```
[<Post Title> (<Series Name> <Post ID>)]
```

Examples:
- *See [The Context Stack (Agentic Stack L1-T03)] for the seven layers.*
- *The capstone argument lives in [The Limits of Evaluation (AI Evals L3-T30)].*
- *Cross-link to [Why Your Agent Fails (Harness Engineering 01)] for the canonical MHTE introduction.*

Rules:
- Title in title case (matching the post's own H1 — exact match required for Lovable string-matching)
- Series name spelled out: *Agentic Stack*, *Harness Engineering*, *AI Evals*, *AI PM OS*
- Post ID exactly as it appears in the filename (L1-T01, L2-T15, B05, BONUS-T01, etc.)
- The full bracketed reference is the link surface — Lovable wraps it in `<a href="...">` with the URL derived from the series + ID
- No bare *"see L1-T03"* anywhere. Always the full bracketed form.

This is non-negotiable. Without it, the corpus has navigation that breaks the moment it hits Lovable's link generator.

---

## The closing trail discipline (NEW in v2)

Every post's closing must trail forward to the next post in body prose — not just an "Up Next" header. The discipline:

1. **The cliffhanger sentence** (in frontmatter) is the one-line tease.
2. **The "Up Next" section** at the end of the body names the next post explicitly with the bracketed cross-reference format.
3. **The closing 2-3 paragraphs of body prose** must explicitly bridge — not just announce. The prose says: *"this post taught X. The next question is Y. That question is the entire concern of [Next Post Title (Series Post ID)]."*

The bar: a reader on the train who finishes a revised post should hit the next link before their stop without thinking about it. That's the trail.

---

## The SVG guidance footer (NEW in v2)

Every post ends with a `## SVG guidance — redesign notes for [post ID]` section before the References. Format:

**Concept SVG (the [name] visual).** What it must communicate in three seconds: *[the structural fact]*.

Recommended hero element: [specific visual element with annotations].

Verbatim text to display: *[screenshot-able sentence that lives in the SVG itself].*

What the redesign should add: [contrast, callout, or detail that elevates the concept SVG beyond a generic diagram].

**Practice SVG (the [name] visual).** What it must communicate in three seconds: *[the practical insight]*.

Recommended hero element: [specific visual — usually a stylised version of the in-practice artefact].

Verbatim text to display: *[the line a senior PM screenshots].*

What the redesign should add: [the contrast or annotation that makes the visual carry an insight beyond what the markdown table already shows].

Both SVGs should match the design system used in [Why Your Agent Fails (Harness Engineering 01)] for cross-series visual continuity.

---

## The spine frontmatter (NEW in v2)

Every post's YAML frontmatter includes a `spine:` block with three fields:

```yaml
spine:
  depends_on: [L1-T01, L1-T02]
  pairs_with: [L1-T05, L1-T09]
  builds_toward: [L2-T03, L3-T02]
```

Rules:
- `depends_on` = articles a reader should have read first to understand this one
- `pairs_with` = articles that complete the same loop or treat the same concept from another angle
- `builds_toward` = articles this one is preparing the reader for
- Cross-series references are included where the relationship is load-bearing
- Each post averages 2-4 entries per field — enough to navigate, not so many the reader gives up

This frontmatter is what makes the spine machine-readable. Lovable uses it to build the navigation graph.

---

## The four hard tests (NEW in v2 — every post must pass all four)

1. **Screenshot test.** One sentence in the post is quotable in isolation. Pick the strongest sentence. Send it to a senior PM colleague who has not read the post. Ask: *would you save this?* If yes, the post has produced at least one travelling sentence.

2. **Monday morning test.** The *In Practice* section produces an artefact a senior PM could run against their own product on Monday. If the exercise is theoretical or vague, return to the *In Practice* pass.

3. **Standalone test.** A reader with no other context can read this article without lookup. Every term that required lookup needs an inline definition or a cross-reference with insight.

4. **Naval test.** Print the closing sentence on a notecard. Look at it for ten seconds. Would Naval Ravikant retweet it? If yes, ship. If no, return to the travel pass.

The four tests are the corpus's quality gate. No post ships without passing all four.

---

## The nine-pass loop (NEW in v2 — for revising existing posts)

For each post being revised:

1. **Opening pass** — Real customer, real number. Replace constructed openers wherever possible.
2. **Thesis pass** — One sentence that, alone, teaches the lesson. In a callout if not already.
3. **Artefact pass** — Concrete table / diagram / test. No artefact, no ship.
4. **Cross-reference pass** — Add `spine:` frontmatter; replace duplicated explanations with one-line cross-refs to canonical home.
4b. **Cross-reference format pass** — Every cross-reference uses `[Title (Series Post ID)]` format.
5. **Slop pass** — 24 anti-pattern words eliminated.
6. **Compression pass** — Delete every paragraph that doesn't make the lead sentence land harder. Target: 15-25% shrinkage.
7. **Travel pass** — Closing sentence is screenshot-able.
7b. **Closing trail pass** — The closing prose explicitly bridges to the next post — names it, names the question it answers, gives the structural reason to keep reading.

Each pass takes 5-15 minutes. Total per post: ~60-90 minutes for a polish revision; ~3-5 hours for a substantial rewrite.

---

## Length discipline (NEW in v2)

> **There is no word limit. There is no word minimum. Be exactly as long as the lesson requires — no longer, no shorter.**

Operational rules:
- **Be precise where precision earns its place.** A definition is precise. A list of cost layers is precise. A trap diagnosis is precise. Compress those.
- **Expand where expansion genuinely helps the learner.** A new concept that bends the reader's mental model deserves the worked example, the analogy, the production-texture detail that makes it stick.
- **Cut every paragraph that doesn't make the lead sentence land harder.**
- **Length-for-its-own-sake is always wrong.** Ten thousand words on a topic that lands in 4,000 is editorial failure.
- **Brevity-for-its-own-sake is also wrong.** Two thousand words that skip the worked example and force the reader to figure out the mechanism alone is also editorial failure.
- **The Naval test cuts both ways.** Naval's tweets are short because the lesson is short. Naval's essays are long because the lesson required it.

---

## The preserve-verbatim discipline (NEW in v2)

The corpus has 30+ sentences-that-sing already. When revising, **preserve verbatim**:
- Real customer openers with primary sources (Tobi Lütke, Samsung, Steven Schwartz)
- The structural fact lines (*the user's message is less than 1% of what the model sees*)
- The strongest analogies (chef-and-instructions, exam packet, hotel concierge, F1 pit crew, restaurant operations manual)
- The 25 named frameworks (CONTEXT, MHTE, Pass^k, Agent Tax, Magnifying Glass, Customer-Success Paradox, etc.)
- Definition callouts and "Think of it like" callouts that already land
- The Try-This-Now exercises that produce real artefacts
- The "Remember this" 1-2-3 patterns that already pass the screenshot test

When in doubt, **preserve.** A line that already passes the Naval test does not need rewriting. The discipline of the rewrite is to elevate the weak passages to match the strong ones — not to homogenise the strong passages into something newer-but-flatter.

---

## The 25 Ravi-invented frameworks (the canonical list)

When using one of these terms, link on first use to the canonical home:

CONTEXT framework • MHTE • Pass^k math • Agent Tax • Customer-Success Paradox • AI Agent Autonomy Rate • Magnifying Glass thesis • 8-or-9-words rule • Three Architecture Archetypes • Four Moat Archetypes • Three Loop Archetypes • Five Pricing Bands • Four Adoption Mechanics • Five Eval Limits • Five-Card Gate • CAPTURE • Context Spec • Language Test • Trap/Fix structure • 4-Stage Hill-Climb • Distribution Surface Map • Self-Optimisation Rounds • Time-to-First Value (TTFV) • Harness Health Score • Five-Layer Governance Stack

---

## The writing process (updated for v2)

### Step 1: Research before writing

For every topic:
1. Read the topic's spec from the deep dive's Topic Map
2. Read the corpus-map.md for the spine relationships
3. Web search for cutting-edge understanding, real-world failures, practitioner insights
4. Cross-reference research inputs from Gemini/ChatGPT if provided
5. Verify every URL before citing. If it doesn't verify, don't use it as factual.

### Step 2: Run the four scratchpads (4 minutes)

Tension → Audience → Voice (six checks) → Cross-reference-with-insight. Internal only. The scratches do not appear in the post.

### Step 3: Write with enterprise production as the lens

The reader is building a B2B platform or B2C app at scale. Not a weekend project. Every section assumes production reality.

**Pre-write terminology gate (enforce DURING writing):** Every technical term, acronym, framework name, or domain-specific phrase gets an inline definition AS you write the sentence — not in a later audit pass. Common terms that MUST be defined on first use in every post: *inference, tokens, latency, attention, embedding, RAG, JSON, MCP, GDPR, FINRA, ICD-10, SLA, SOC 2, RFP, P95, CSM, harness*, and any newer term the corpus introduces.

**Pre-write illustrative signal gate:** Every composite or constructed scenario MUST start with *"Consider a..."* or equivalent signal word. Real companies use their name directly. There is no gray area.

**Pre-write cross-reference gate:** Every cross-reference uses the `[Title (Series Post ID)]` format. Every cross-reference carries the standalone insight first, then the link for depth.

**Pre-write reference gate:** Only add a URL to the References section AFTER you have cited it inline in the post body.

### Step 4: Apply structure

Story → Core Idea → Concept Visual → Where This Hits in Production → Connecting the Dots → The Trap → Remember This → In Practice → Practice Visual → **Up Next (with body prose trail)** → **SVG guidance footer** → References → Builds-on / Leads-to footer.

### Step 5: Self-audit (the four hard tests + nine-pass loop)

Run the four hard tests. If any fail, run the relevant pass from the nine-pass loop. Do not ship until all four pass.

### Step 6: Save and update tracker

Save to the post's original folder, original filename. Update completion tracking in `detailed.md` or the working corpus tracker.

---

## SVG copywriting standard (preserved from v1)

Every piece of text in an SVG must be self-explanatory when scanned. The visual is a MEMORY AID for a concept the reader just learned — not a standalone essay. Rules:

1. **Plain language only.** No phrase that requires the reader to already understand the concept.
2. **Don't add text for filler.** Every line earns its place.
3. **The scan test:** Cover the post. Show only the SVG. Can a senior PM understand what the concept IS from the visual alone?
4. **Write like a billboard, not a paragraph.** Short phrases. Active voice. Concrete nouns.
5. **Concept SVGs** show ONE definition. Reader walks away with one sentence in memory.
6. **Practice SVGs** show a CONTRAST or MECHANISM — not a data table.

---

## The 24 anti-patterns (always active)

From `ravi-thinking-skills`. Every output is scanned. Hits get rewritten:
- No significance inflation (*pivotal moment, evolving landscape*)
- No AI vocabulary (*Additionally, delve, foster, underscore, intricate, landscape (abstract), testament, showcase*)
- No copula avoidance (*serves as, stands as, boasts*)
- No excessive hedging (*could potentially possibly*)
- No filler (*In order to* → *To*; *It is important to note that* → just say it)
- No chatbot artifacts (*Great question!*, *I hope this helps!*)
- No generic conclusions (*the future looks bright*)
- Add soul: opinions, varied rhythm, structural messiness, first person

---

## The factual vs illustrative rule (preserved from v1)

- **Factual** = real company, verified URL, specific numbers.
- **Illustrative** = clearly signaled (*"Consider a..."*, *"Imagine a PM at..."*).
- Never blur the line. One hallucinated citation undermines the entire deep dive.

---

## Connecting the dots (preserved from v1)

Ravi's signature section. Every topic gets one. Where the writing stops being a tutorial and becomes a point of view.

Draw connections the reader wouldn't make on their own:
- **AI spectrum calibration** — Where does this concept's importance change based on the product's autonomy level?
- **Moat thinking** — Does this concept compound over time?
- **Cross-domain bridges** — What framework from product strategy, safety, or agent design illuminates this concept?
- **The practitioner's view** — What does someone who has actually built this see that a textbook reader misses?

This section is called *Connecting the dots* in every post. 150-300 words of the highest-density thinking in the entire piece.

---

## Cross-skill integration (updated for v2)

When writing deep dives, draw from:

| Skill | When it's relevant |
|-------|-------------------|
| autonomy-spectrum | Calibrating eval requirements to product type |
| moat-finder | When a concept creates competitive advantage |
| safety-as-moat | When safety and eval overlap |
| eval-framework | The core eval practice |
| ai-use-case-readiness | Solution spectrum 0-7 |
| strategy-canvas | When concept connects to roadmap |
| trust-ladder | When concept connects to trust boundaries |
| excalidraw-svg | The actual SVG creation (note: rewrites do NOT touch SVGs — guidance footer only) |
| ravi-thinking-skills | The 24 anti-patterns + voice DNA |

---

## Deep dives in progress (updated for v2)

| Deep Dive | Location | Status |
|-----------|----------|--------|
| Agentic Stack | 1_Projects/2_agentic-stack/ | 35 posts, rewrite in progress (12 of 35 done as of 05 May 2026) |
| Harness Engineering | 1_Projects/3_harness-engineering-series/ | 1 post read; full inventory + rewrite pending |
| AI Evals | 1_Projects/4_ai-evals/ | 35 posts, rewrite pending |
| AI PM OS | 1_Projects/7_AI PM OS/ | 30 + 5 bonus posts, rewrite pending |

The corpus master reference lives at `corpus-map.md` (root). The full revision program lives at `detailed.md` (root).

---

## Quality bar

Three tests, in order:

**Test 1 (Anthropic CPO):** *Would Anthropic's CPO read this post and say "this person understands the space at a practitioner level, explains it clearly, and grounds it in real enterprise reality"?* If yes, ship it. If no, keep refining.

**Test 2 (Senior PM Monday morning):** *Could a senior PM at a Fortune 500 company apply the concept in their next sprint planning meeting?* If yes, the writing did its job. If it's only interesting but not applicable, it's not finished.

**Test 3 (Naval Ravikant retweet):** *Would Naval Ravikant retweet the closing line?* If yes, the post travels. If no, return to the travel pass.

---

## What changed in v2 (May 2026)

The 105-post rewrite surfaced disciplines the v1 skill did not encode. v2 adds:

1. **Four scratchpads** (Tension + Audience + Voice + Cross-reference-with-insight) — formalised pre-write discipline.
2. **The integrated voice rules** (7 rules including emotion, concrete imagery, active verbs, accessible words, jargon explained, cross-ref-with-insight, length-matches-lesson).
3. **Cross-reference format mandate** — `[Title (Series Post ID)]` for Lovable.
4. **Closing trail discipline** — body prose pulls forward, not just an "Up Next" header.
5. **SVG guidance footer** — separate section at end of post for SVG redesign work.
6. **Spine frontmatter** — `depends_on / pairs_with / builds_toward` for machine-readable navigation.
7. **The four hard tests** — Screenshot, Monday morning, Standalone, Naval.
8. **The nine-pass loop** — for revising existing posts.
9. **Length discipline** — match length to lesson, no word limit, no minimum.
10. **Preserve-verbatim discipline** — when in doubt, preserve. Don't rewrite strong material.
11. **The 25 Ravi-invented frameworks** — canonical list with cross-reference home assignments.

The v1 disciplines (template, terminology gate, illustrative signal gate, factual-vs-illustrative rule, 24 anti-patterns, Connecting-the-dots format, cross-skill integration, quality bar) are all preserved.

---

*Last updated: 05 May 2026. v2.0. Skill at parity with the rebuild learnings from the 105-post corpus revision.*
