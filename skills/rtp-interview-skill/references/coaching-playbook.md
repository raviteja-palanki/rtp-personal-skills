# AI PM Technical Interview — Coaching Playbook

How to get better at the AI PM technical round — the diagnosis-to-drill map, study plans by timeline, the "run it tonight" self-interviewer, and the one truth that underlies all of it: **real depth comes from building, not rereading.** You can memorize this whole library and still get exposed on the second follow-up. The candidates who pass have shipped small things and can say "the first thing that broke was…"

Use this file for Coach mode and for end-of-session next steps.

---

## The one thing that actually moves the needle

Reading a guide teaches you the *answers*. It cannot teach you how you *sound under a follow-up* — and this round is 80% follow-ups. Two moves matter more than any fact in `concepts.md`:

1. **Practice out loud, under pressure.** Not in your head. Dictate your answers, or run the self-interviewer below. The gap between "I know this" and "I can say this in 90 seconds while someone pushes back" is the entire game.
2. **Build one small real thing** in your weak area. Ship a churn model with XGBoost. Wire up a single tool call. Stand up a 20-document RAG. Then your answers carry the operational tells ("I'd put…", "the first question after I ship…") that can't be faked, because you'll have actually shipped it.

Aakash's own read on his mock answers: "about an 8.5 out of 10 — you could go deeper on all of them, and that depth comes from actually running the demos, not from rereading this guide." Model that honesty for the user. The library gets them to a B+. Building gets them to an A.

---

## The 5 Laws as a practice loop

Coach the user to self-check every answer against the sticky-note version:

**Commit → Depth → Experience → Nuance → Succinct.**

Have them write it on an actual sticky note in front of them during practice and the real interview. After every practice answer, ask them to grade themselves ✓/✗ on each. The most common failures, in order:
1. **No commit** (fence-sitting) — the #1 tell of not knowing.
2. **No nuance** (one-dimensional) — the B+ ceiling.
3. **Too long** (word salad) — the anxiety tell.
4. **Told, didn't show** (no experience texture) — the "stood near a project" tell.
5. **Wrong jargon** (bluff) — the only unrecoverable one.

---

## Diagnosis → Drill Map

Match the user's pattern (from `interview-history.md` or observed in a mock) to the fix.

| Pattern you observe | Diagnosis | Drill |
|---------------------|-----------|-------|
| Recites definitions, dies on "okay, now apply it" | Knowledge without application | Mock in Engineer-in-the-Room mode; every answer must end in a decision or a trade-off, not a definition. Study §-by-§ then immediately answer a Topic question from `question-bank.md`. |
| Confidently states wrong facts | Bluffing (auto-fail) | Drill the "name the edge" answer (#10 in model-answers). Practice saying "I'd confirm with the team, but my instinct is X, and here's what I'd check." Re-study the mis-stated concept in `concepts.md`. |
| Rambles past 2 minutes | Verbosity / anxiety | 90-second timer on every answer. Force two-paragraph structure. Practice the check-in: "does this make sense so far?" |
| Great mechanism, no "so what" | Over-answering / wrong archetype | Mock in Product-Layer mode. After each mechanism, force the day-two playbook: eval, fallback, cost, UX. |
| Reaches for the fanciest answer | Over-engineering | Drill the "does orchestration come into a single tool call?" trap. Reward saying "no, and here's when it would." |
| Names sessions/prompts as success | Input-metric habit (Mistake 3) | Drill: "which metric goes on the CEO's dashboard?" → task resolution. Study §8. |
| Designs assume the model is always right | Deterministic PRD (Mistake 5) | For every design, force: "what happens when the model is confidently wrong?" → fallback, cite, escalate, HITL. Study §13. |
| "We built our own platform/model" | Wrapper-as-platform (Mistake 2) | Rewrite their project story to claim exactly what they did. "I configured and evaluated connectors" > a false infra claim. |
| Can't answer "what would you do differently" | Perfect-record (Mistake 4) | Prep one real killed feature / lesson with the takeaway. |
| Vague on ML vs LLM | Foundational gap | Study §3; drill churn, fraud, and one language task until the tabular/hybrid logic is reflexive. |
| Vague on evals | The most common applied gap | Study §8; drill the eval-framework question and the "quietly getting worse" question until fluent. |
| Can't talk cost | Business-layer gap | Study §9; memorize the formula (in+out, output 3–5×), caching ~10×, routing 17×, p95. |

---

## Study Plans by Timeline

### T-minus 1 day (cram)
- Read the **30-second glossary** (§15 of concepts) twice, out loud.
- Read **all 13 model answers** aloud, once. Feel the shape: commit → depth → experience → nuance → stop.
- Memorize the **5 Laws sticky note** and the **six mistakes**.
- Run the **self-interviewer** below once, Engineer archetype, 5 questions.
- Pick your ONE real project story and rehearse the agent/experience answer (#13).
- Sleep. Do not cram new concepts you'll half-remember and bluff.

### T-minus 1 week
- Day 1–2: Read `concepts.md` §1–§5 (LLMs, hallucination, ML-vs-LLM, tools/MCP, agents). Answer the matching Topic questions aloud.
- Day 3–4: §6–§9 (routing, RAG, evals, unit economics). These are where applied roles push hardest. Drill each.
- Day 5: §10–§13 (GPUs, fine-tuning, transformers, safety) — depth-lab and infra material. Skim if your target is applied; go deep if it's Nvidia/OpenAI/Anthropic/DeepMind/Glean.
- Day 6: Run **two full mocks** — one Engineer, one Product-Layer — on the same questions. Feel the archetype gap.
- Day 7: Fix your weakest pattern (diagnosis map). Build one tiny thing if you can.

### T-minus 1 month (do it right)
- Weeks 1–2: Work through all of `concepts.md`, one topic per session, always ending in spoken answers.
- Week 2–3: **Build.** Pick one: an XGBoost churn model on a Kaggle dataset, a single-tool function-calling demo, a small RAG over your own docs, a Slack/email digest agent. This is the highest-leverage week. It converts memorized answers into experienced ones.
- Week 3: Company-specific — load your target's section in `question-bank.md`, match the archetype, drill their real questions.
- Week 4: Mock loops. Alternate archetypes. Grade against the rubric. Target: five clean answers in a row that survive two follow-ups each, under 120 seconds.

---

## The Self-Interviewer (run it tonight)

Give this to the user to paste into any Claude or ChatGPT window and answer **out loud**. It's the single best between-session drill because it delivers what a static guide can't: adaptive follow-ups.

```
You are running a technical interview for an AI Product Manager role.
Your job is to find out whether I understand the systems I build on, or whether I only use them.

HOW TO RUN THIS
- Ask one question at a time. Wait for my full answer before responding.
- After every answer, push exactly one level deeper on the weakest part of it.
- Do not accept a definition as an answer. Make me apply it.
- If I bluff, name it immediately.
- Run 5 questions, then score me.

PICK AN ARCHETYPE, and tell me which one you are before you start:
- The Engineer in the Room. You want the mechanism. Every answer earns a follow-up one layer down.
- The Product Layer PM. You ask a mechanism question but listen for what I do with it. If I go deep on implementation detail instead of validation, failure handling, and user experience, mark me down for it.

QUESTION BANK
- Design a high-level system for how an assistant responds to a user query.
- Users complain the assistant is confident but wrong. How would you fix it?
- How do you decide what is a good task for an LLM and what is not?
- Your feature calls a tool. Walk me through what actually happens under the hood.
- Walk me through the unit economics of an LLM feature. How do cost per inference and p95 latency change what you build?
- Walk me through your eval harness. What is in the offline set, and what do you watch online after launch?
- You ship an assistant and the north-star metric goes up. How would you know the model is quietly getting worse anyway?

SCORE ME 1 TO 5 ON EACH
1. Mechanism fluency. Did I say what happens between the prompt and the answer, and where the model's job ends and my code begins?
2. Probabilistic instinct. Did I treat the output as a distribution, and design for being wrong some of the time?
3. Day-two playbook. Did I describe an eval harness, a fallback path, and a rule for shipping the AI version over the deterministic one?
4. Edges. When I hit the end of what I knew, did I name the edge and what I would check, or did I guess confidently?

SCORING RULES
- Be harsh. A comfortable score is useless to me.
- A confident wrong answer scores lower than "I don't know, here is what I would check."
- Quote my exact words back when you mark something down.
- End with the single highest-leverage thing to fix before a real loop.

Start by telling me which archetype you are, then ask question one.
```

**Coach the user to run it twice — once against each archetype.** The same answer that lands with the Engineer in the Room often gets marked down by the Product-Layer PM, and feeling that gap yourself is worth more than any list of tips.

---

## The Six Mistakes That End Loops (memorize the list)

Detail and detectors are in `grading-rubric.md`. The sticky-note version:

1. **Bluffing a detail** — the only unrecoverable one. Name the edge instead.
2. **Calling a wrapper a platform** — claim exactly what you did.
3. **Reporting input metrics** — task resolution is the number.
4. **The perfect record** — have one real failure/lesson ready.
5. **The deterministic PRD** — design for the model being wrong.
6. **Going too deep** — read the archetype; depth is only an asset when asked for.

Mistakes 1 and 5 are the two most common and most fatal: the bluff (kills credibility) and the deterministic PRD (marks you as a traditional PM, not an AI PM).

---

## How to Build Real Experience (so depth is earned)

Prescribe one small build matched to the weak area. Each is a weekend, and each makes a whole category of answers real:

- **Weak on ML vs LLM →** train an XGBoost churn/fraud model on a public dataset (Kaggle telco churn). Now "trees are cheaper, faster, interpretable" is something you've *seen*, and you can answer "why wasn't this account flagged" because you've pulled feature importances.
- **Weak on tools/MCP →** build a single function-calling demo (weather, or a calculator tool) with any model's API. Now you know the model emits a request and *your* code runs it — because you wrote the code that ran it.
- **Weak on RAG →** stand up a 20–50 document RAG over your own notes (LlamaIndex/LangChain quickstart + a vector store). Now chunking and reranking are real tuning knobs you've turned, not words.
- **Weak on agents →** build a Slack or email digest agent with a system prompt, one tool, and a skill file. Now the three-layer answer (#13) is your actual project.
- **Weak on evals →** write a 20-example golden set for any of the above and grade outputs with an LLM-judge. Now you've felt judge bias firsthand.
- **Weak on cost →** run 1,000 queries through two models and compare the bills. Now the unit-economics answer has your numbers in it.

The point isn't to become an engineer. It's to have *stood close enough to the fire* that your answers carry heat. That's the difference between a B+ library user and an A candidate.

---

## Session-End Coaching Template

At the end of a Coach session, deliver:

```markdown
## Your AI Technical Round — Coaching Plan

**Target:** [company / role / date]  ·  **Archetype to expect:** [X]

**Your top weakness pattern:** [name it, quote evidence]
**Why it's costing you:** [tie to a specific mistake or law]

**This week:**
1. Study: [concepts.md §X, §Y]
2. Drill: [question-bank Topic Z / a Set from Part C]
3. Build: [the one small project matched to the weakness]
4. Run the self-interviewer twice (both archetypes), out loud.

**Your one sticky note:** Commit → Depth → Experience → Nuance → Succinct.
**Your one trap to avoid:** [the specific mistake they're prone to].

Come back and run `/ai-pm-tech mock` when you've done the build — your answers will be different.
```

---

## Final Word (for the user)

The AI PM technical round has no ceiling — even an A+ answer earns another follow-up, because AI keeps pulling PMs closer to engineering. That's not a threat; it's the opportunity. You don't need to out-engineer the engineer. You need to understand the systems you build on well enough to be a credible partner — and to know, honestly, where your edge is. Name that edge, ground your claims in things you've actually built, commit, layer the nuance, and keep it short. Do that and you'll clear a round almost no one has prepared for.
