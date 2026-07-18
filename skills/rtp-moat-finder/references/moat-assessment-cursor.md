# Moat Assessment: Cursor (Anysphere) — the cold-run exemplar

*Produced in cold-start mode (~35 min, public knowledge only, no company access) as moat-finder's v2.2 stress test. Every score is ⚠ provisional by construction — the point of this document is to show what an honest cold run looks like: tagged scores, named evidence gaps, OPEN flags, and a verdict that discriminates. Chosen deliberately: Cursor is the live "is it just a wrapper?" debate — a moat framework that can't produce a non-obvious verdict here isn't earning its keep.*

**Value-line:** growth — developer-productivity spend, seat + usage expansion; multiplied into the valuation.
**Core value engine:** the AI-native *editing loop* — tab-completion trained on edit-acceptance traces plus an agentic mode, fused into the editor itself. Not "access to models" (everyone has that).

**The two brutal tests, answered first:**
- *Why can't a same-model competitor beat us next quarter?* The tab model trained on proprietary accept/reject edit traces at enormous scale, plus iteration speed and installed habit. Honest note: the *agent* mode alone would not survive this test — that layer is near-parity across rivals on the same frontier models.
- *Would anyone actually miss us tomorrow?* Yes — a large cohort of developers whose muscle memory and daily flow live in it. That's real, and it's mostly *habit + speed*, which decays faster than data or contract lock.

**Five-moat scorecard** (band anchors: 1 none · 2 replicable in 1–2 qtrs · 3 ~a year · 4 measured + multi-year · 5 compounding):

| Moat | Score | Evidence | Decay clock |
|---|---|---|---|
| 1. Proprietary data | **4** ⚠ | Edit-acceptance traces at scale feeding the custom tab model — rare-hard-case coverage across languages/codebases; the loop closes daily (◆ scale claims are company-reported) | 12–24 mo; holds only while the tab model's measured lift over frontier defaults persists |
| 2. Workflow depth | **3** ⚠ | It *is* the editor (habit, keybindings, rules/memories) — but migration to a rival fork or VS Code + rival plugin is an afternoon, not quarters. Habit ≠ integration | Fast — 6–18 mo if a rival matches tab quality |
| 3. Harness mastery | **3** ⚠ | Codebase indexing, retrieval, apply-model, background agents — real engineering, but rivals on the same models sit within a quarter or two on most of it; measured-lift evidence not public | 12 mo, under active assault |
| 4. Trust & reliability | **2** ⚠ | Enterprise motion (privacy mode, SOC 2 ◆) but visible trust dings: the 2025 support-bot hallucination incident and opaque pricing-change backlash (the "trust trap" case in token-economics). Binary moat, currently scratched | Rebuild is slow; one more visible incident is expensive |
| 5. Network effects | **1–2** | Single-tenant learning; team features are collaboration, not cross-customer compounding. Fails the four-question filter (data accumulation, not network) | — |

**Total: ~13/25 ⚠ · Moats scoring ≥3: 3 (data, workflow, harness) → defensible-but-thin.** Exactly the discriminating answer the wrapper debate needs: *not* a wrapper (the tab-data loop is a real compounding moat), but carried by one deep moat plus two contested ones.

**Dynamics:** Vertical-Infinite — yes (code, deep) · Living Software — Micro ✅ (accept/reject), Meso partial, **Macro (Workspace/org DNA) emerging only** — the biggest unbuilt moat · cycle-time — fast human cycle; the tab-model retrain loop is the machine-cycle part.
**Model dependency:** split — tab model proprietary (resilient *and* a treadmill); agent layer model-agnostic but commodity.
**Distribution (6th force):** strong dev mindshare, **but the defining squeeze applies: its model suppliers ship competing coding agents downstream.** Multi-model neutrality is a hedge, not a moat. Access assumed to get harder, not easier.
**Fake-moat checks:** anti-moat loop — pass (edit traces are theirs alone) · agent-in-the-middle — N/A today, watch agent-marketplaces · acquisition test — the trace-loop + habit would partially transfer; the iteration culture would not.
**18-month projection:** frontier-lab agents commoditize the agent layer (near-certain); survival hinges on tab-loop lift staying measurable + Macro Workspace DNA shipping + trust repair in enterprise. Realistic: defends the editor niche, loses the "agent" halo. `OPEN:` does the tab model's lift over frontier defaults still measure ≥ meaningful in 2026? — the one number that settles moat #1's score.
**Next-quarter move (the weakest moat that matters):** trust & reliability — enterprise-visible reliability + pricing transparency. It gates the enterprise expansion the growth line is priced on, and it's the only moat currently *scratched* rather than merely thin.

---
*Cold-run friction log (what this run taught the skill — all fixed in v2.2): needed a run-mode router (added), needed scoring band anchors to score alike cold (added), the supplier-competes-downstream squeeze needed naming (added), the two brutal tests belonged in the OUTPUT template, not just the trap (added).*
