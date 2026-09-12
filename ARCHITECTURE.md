# Architecture

**What this library is.** A set of reasoning lenses, written as Claude Code skills, that an always-on orchestrator composes for whatever question turns up. Not a reference manual. Not a prompt collection. The unit is a lens: a few sharp tenets that reasoning starts from when a situation nobody wrote a rule for arrives at work.

**The test every skill is held to:** handed a situation it never anticipated, does reasoning that starts from this skill beat reasoning that would have started without it? A skill that is merely accurate fails that test. A skill that changes what you do on Monday passes it.

Everything below follows from three design choices:

1. **Skills compose rather than route.** No lookup table decides which skill runs. The orchestrator reads the situation and picks two to four, and each skill names the companions it works with and why.
2. **A skill declares what it depends on.** An `imports:` line in the frontmatter makes the dependency explicit, which is what turns a pile of documents into a graph you can reason about.
3. **The plugin is one artifact.** One marketplace entry, one manifest, one version. An earlier multi-plugin layout is gone, and the single manifest is now enforced on every release.

---

## The shape of it

Three stages of work, seven layers on disk, one orchestrator.

| Stage | What it decides | Layers on disk | Skills |
|---|---|---|---:|
| **Think** | Is this the right problem, and what is actually true | `thinking-core` 10 + `product-sense` 14 | **24** |
| **Judge** | Is it worth doing, can it be held, and how will we know | `ai-strategy` 12 + `agent-design` 6 + `safety-and-trust` 7 + `eval-and-quality` 7 | **32** |
| **Craft** | The artifact someone else can act on | `craft` 11 | **11** |
| **Plus** | Writing, research, design and library governance | general-purpose folders | **22** |
| **Orchestrator** | Reads the situation, composes the rest, reviews the output | always on | **1** |

**The stages are a lens, not a folder.** On disk there are seven skill layers plus the general-purpose set, and `rtp-personal-skills:diagrams/skill-map.svg` draws them from the filesystem. Counts in this document are re-derived from the repository, and `scripts/governance-check.py` fails if they drift.

**Why the stage boundary matters more than the folder.** Most bad AI product decisions are stage confusion. A team argues about eval thresholds (Judge) when nobody has established whether the bottleneck is information or judgment (Think). A PRD gets written (Craft) for a use case whose autonomy level was never chosen (Judge). The orchestrator's first move is to name the stage.

---

## The orchestrator

`rtp-aipm-orchestrator` loads at the start of every session, whatever the topic, and it is the only skill that does.

**What it carries:** eleven thinking algorithms that run silently on every input, the routing map for the whole roster, the rules for reasoning across a corpus rather than summarising one file, the live reference set (published URLs, corpus indexes, playbook paths), and the output gate everything ships through.

**The eleven algorithms:** first principles, everyday analogy, the invisible ninety percent, trap and fix, dual definition, red team, determinism compass, cross-domain import, production reality, graceful degradation, pre-mortem. They are not a checklist to recite. They are the passes that have already run by the time an answer is written.

**Five rules govern its behaviour.** Zero invented facts, and anything unverifiable is named as unverifiable. Never please: no fake enthusiasm, because flattery corrupts the feedback loop. Constructive criticism by default, so every plan gets stress-tested. A pre-mortem before any commitment that is hard to reverse. Limits admitted cleanly, separating what can be grounded, what is inference, and what needs a primary source.

**Acting under uncertainty**, which is where most assistants stall:

| Situation | Move |
|---|---|
| Damage low, reversible | Assume. Name the assumption in one line. Proceed. |
| Damage high, reversible | Nudge. Recommend a read. Proceed on confirmation. |
| Damage high, irreversible | Nudge and wait. |
| Genuinely no reasonable read | Ask one surgical question, framed with options. |

**Four routing rules that prevent the common mistakes:**

- **"Should we build this?"** goes to `problem-ai-fit` before `ai-use-case-readiness`. The first asks whether AI is the right instrument at all. The second scores a use case that already passed that test.
- **Anything about money** pairs `cost-model` (what it costs) with `token-economics` (what you charge), and runs `moat-finder`'s value-line pre-screen before either. Do not optimise a cost line nobody should be aiming at.
- **"Let's build an agent"** starts at `autonomy-spectrum` to place it, then `agent-harness` for the machine and `agent-ecosystem` for the seams between agents.
- **Anything with a number in it** goes through `trendslop-check`.

---

## What is in each layer

One line each, in the skill's own terms.

### Think

**`thinking-core`**, the reasoning primitives everything else leans on.

| Skill | The question it answers |
|---|---|
| `first-principles` | What is the one irreducible operation here |
| `stress-test` | Does this survive 10x users, hostile inputs, a degraded provider and a finance review, or only the demo |
| `falsification` | Turns "this will work" into a claim that can lose, with kill conditions |
| `determinism-compass` | Which parts must answer identically every time, and which may vary |
| `bias-spotter` | Names the bias that makes a flawed decision feel obvious |
| `problem-type` | Technical problem or adaptive challenge, because the second does not yield to expertise |
| `judgment-guard` | Decides on purpose where human judgment sits, before it erodes by default |
| `alignment-check` | Organisational readiness before technology spend |
| `dual-lens` | One concept, actionable for the leader and checkable by the engineer |
| `gossip-mode` | Turns venting into memory the system can use |

**`product-sense`**, whether this should exist and for whom.

| Skill | The question it answers |
|---|---|
| `problem-ai-fit` | AI, or rules and search. Start here |
| `ai-use-case-readiness` | The minimum autonomy that captures the value |
| `failure-modes` | What breaks, what it costs, what the user experiences |
| `invisible-stack` | The hidden parts that decide answer quality |
| `ai-ux-patterns` | Interfaces for output whose confidence varies |
| `feedback-flywheel` | How user behaviour becomes the improvement loop |
| `feedback-triage` | Frequency times severity times fit, plus an AI-failure axis |
| `jtbd-analysis` | The job the user is actually hiring this for |
| `opportunity-solution-tree` | Teresa Torres's tree with an AI-feasibility filter |
| `uncertainty-research` | How to research a product whose outputs vary |
| `interview-synthesis` | Open, axial and selective coding of what people said |
| `attitudinal-segmentation` | Embracer, Neutral, Skeptic, and why they need different products |
| `needs-guard` | Autonomy, competence, belonging, and what automation takes from each |
| `ai-product-taste` | The quality bar, set against domain, users and price |

### Judge

**`ai-strategy`**, is it worth doing and can you hold it.

| Skill | The question it answers |
|---|---|
| `strategy-canvas` | What to solve, why you, and what happens when the model changes |
| `moat-finder` | What survives copycats and the next model release |
| `build-or-buy` | Five gates, and what the vendor learns from your usage |
| `capability-tracking` | Build now, or wait for model uplift |
| `ai-portfolio-management` | Stage gates and Buy, Sell, Hold across the portfolio |
| `adoption-launch` | Adoption run as a product launch, not a training plan |
| `token-economics` | Pricing when your best users cost you the most |
| `trendslop-check` | Trendy advice against advice that fits your context |
| `signal-scanner` | Weak signals worth watching before they are obvious |
| `vision-setting` | The destination that survives contact with a roadmap |
| `purpose-dialogue` | Commitment rather than compliance |
| `marketing-to-ai-agents` | Being retrieved rather than remembered |

**`agent-design`**, how the machine is built.

| Skill | The question it answers |
|---|---|
| `autonomy-spectrum` | Whether code or the model decides what happens next, across seven levels |
| `agent-harness` | The machine around the model, and how to diagnose it |
| `agent-ecosystem` | Coordination, handoff and the seams between agents |
| `tool-architecture` | Tools as contracts, not as functions |
| `harness-operating-model` | Funding and staffing the harness as a program |
| `multi-modal-product-design` | Modality chosen by verification cost |

**`safety-and-trust`**, what happens when it goes wrong.

| Skill | The question it answers |
|---|---|
| `agent-risk` | Value against worst-case harm, plus a kill switch that works |
| `trust-ladder` | Whether trust matches reliability, in both directions |
| `trust-under-fog` | Communicating while you still do not know |
| `safety-by-design` | Rules that live in the core instructions, not the wrapper |
| `safety-as-moat` | When safety is the product advantage |
| `responsible-ai-program` | SHARP, and the three gaps that sink programs |
| `breach-ready` | Surviving being hacked, before it happens |

**`eval-and-quality`**, how you know it is any good.

| Skill | The question it answers |
|---|---|
| `eval-framework` | How do you know it is good, made concrete |
| `eval-driven-development` | The rubric is the spec |
| `ai-product-metrics` | Acceptance, correction, regeneration, cost per successful outcome |
| `production-observability` | Catching silent degradation |
| `observability-stack` | A platform choice without lock-in |
| `confidence-tuner` | User trust calibration and judge calibration, as one discipline |
| `gen-ai-experimentation` | Macro and micro experiments, and the J-curve |

### Craft

Generators. Each produces a document that has already been stress-tested by the skills it imports.

| Skill | What it produces |
|---|---|
| `ai-prd` | A spec for output that varies |
| `agent-spec` | The agent design document |
| `context-spec` | Information architecture for reasoning |
| `prompt-as-product` | Prompts versioned like code |
| `prompt-craft` | The writing of the prompt itself |
| `user-stories` | Sprint-ready items |
| `cost-model` | True cost at 10x |
| `ship-decision` | Go or no-go, against severity thresholds and monitoring |
| `competitive-map` | Where you actually stand |
| `fit-signal` | Earned dependence, or a lucky stretch |
| `stakeholder-communications` | Audience-tailored comms, plus the relationship substrate underneath |

### Plus

Writing (`thinking-writing`, `humanizer`, `deep-dive-writer`, `email-mastery`, `readme-storytelling`), research (`hbr-research`, `research-librarian`, `research-synthesiser`), visual work (`excalidraw-svg`, `lucid-boards`, `ux-design-systems`, `design-spec`, `cinematic-presentations`, `frontend-slides`, `ravi-personal-branding`, `ai-fluent-brand`), judgment (`ravi-thinking-skills`, `product-thinking`), career (`interview-skill`, `ravis-resume-builder`), and library governance (`skill-refresh`, `claude-admin`).

**`thinking-writing` is the default gate on every human-facing output**, ahead of every other writing check. `humanizer` is secondary verification, opened when a specific line needs a named slop pattern to convict it.

---

## The import graph

A skill declares its dependencies in frontmatter:

```yaml
---
name: rtp-ship-decision
version: v1.4_latest
description: ...
imports: [stress-test, safety-as-moat, failure-modes, cost-model]
---
```

**What the graph looks like today.** 151 edges declared by 59 of the 90 skills, reaching 44 distinct targets. Ten skills declare `imports: []` deliberately, meaning they stand alone. Twenty-one carry no key at all, which is the honest state for most of the general-purpose set.

**Four skills are the centre of gravity:**

| Imported by | Skill | What that tells you |
|---:|---|---|
| 18 | `determinism-compass` | Almost every decision eventually asks which part must be deterministic |
| 16 | `first-principles` | The strip-the-framing move is upstream of everything |
| 14 | `eval-framework` | You cannot ship what you cannot measure |
| 14 | `stress-test` | The demo-to-production gap is the recurring failure |

Three of those four are `thinking-core` primitives, which is the graph agreeing with the stage model: judgment and craft both bottom out in reasoning, not in domain knowledge.

**The graph crosses domains on purpose.** `adoption-launch` (strategy) imports `needs-guard` (product sense). `agent-risk` (safety) imports `failure-modes` (product sense) and `autonomy-spectrum` (agent design). `attitudinal-segmentation` (product sense) imports `ai-product-metrics` (eval). A skill that only imported from its own folder would be a chapter, not a lens.

**What the craft layer actually pulls in:**

| Generator | Imports |
|---|---|
| `ai-prd` | determinism-compass, bias-spotter, stress-test, prompt-as-product |
| `agent-spec` | trust-ladder, failure-modes, determinism-compass |
| `context-spec` | invisible-stack, determinism-compass, stress-test |
| `cost-model` | stress-test, token-economics |
| `ship-decision` | stress-test, safety-as-moat, failure-modes, cost-model |
| `stakeholder-communications` | ai-product-metrics, eval-framework, problem-ai-fit, trust-under-fog, confidence-tuner |
| `prompt-craft` | determinism-compass, prompt-as-product, eval-framework |
| `prompt-as-product` | eval-framework, determinism-compass |
| `user-stories` | ai-prd, determinism-compass |
| `competitive-map` | moat-finder, first-principles |
| `fit-signal` | falsification, feedback-flywheel, stress-test |

Read that table as the argument for the whole design. `ship-decision` does not ask whether you feel ready. It asks what breaks (`failure-modes`), what it costs at scale (`cost-model`), whether it survives the hostile case (`stress-test`) and whether safety is load-bearing here (`safety-as-moat`). The document is pre-tested because its inputs are.

**Every declared import resolves.** `scripts/governance-check.py` G3 fails the build if one does not, which is how two dangling imports were found and fixed on 12 SEP 2026.

---

## A worked example, illustrative

A PM asks for a PRD for an AI feature that drafts customer replies. What the orchestrator composes, and why:

1. **`problem-ai-fit`** first. Is the bottleneck information, judgment or incentives? If agents are slow because approval takes two days, drafting is the wrong fix.
2. **`determinism-compass`** next. The greeting, the account number and the refund amount must be identical every time. The explanation may vary. That split becomes a section of the PRD rather than a discovery made in QA.
3. **`failure-modes`** and **`stress-test`**. What does a wrong draft cost, who sees it first, and what happens on the day the provider is degraded and the queue is four times normal?
4. **`ai-prd`** generates the document, and it already carries the three answers above rather than placeholders.
5. **`eval-framework`** defines "good" before anyone writes a prompt, because the rubric is the spec.
6. **`thinking-writing`** runs over the finished document, since a spec nobody wants to read does not get followed.

This is an illustration of composition, not a fixed pipeline. The next question will pull a different set.

---

## What a skill file contains

Every skill is one `SKILL.md` with YAML frontmatter (`name`, `version`, `description`, optional `imports`) and a body. Thirty-four skills also carry a `CONCEPT.md`, the longer argument behind the lens, and six carry a `references/` folder.

**There is no fixed section template, and that is deliberate.** A template applied to ninety skills produces ninety documents with the same skeleton, which reads as machine-written whatever the words say. What exists instead is a set of sections that earn their place often enough to have become conventional. Counted across the 90 shipped skills:

| Section | Skills carrying it | What it does |
|---|---:|---|
| `WHEN WRONG` | 64 | States the conditions under which this skill's advice is wrong |
| `VISUAL SUMMARY` | 62 | The whole lens in one diagram |
| `QUALITY GATE` | 57 | What the output must satisfy before it ships |
| `CONCLUSION` | 57 | The Monday-morning move |
| `TRADE-OFF LEDGER` | 56 | What you give up by following this |
| `REALITY CHECK` | 42 | Where the framework meets production |
| `THE TRAP` | 40 | The mistake this skill exists to prevent |
| `DEPTH DECISION` | 35 | How much of this skill the situation deserves |

**`WHEN WRONG` is the one that matters most.** A framework without its failure conditions is decoration, and a skill that cannot say when to ignore it has not been thought through.

---

## Workflows and commands

**Six multi-skill workflows** live in `workflows/`, each a sequence with a timeline:

| Workflow | Timeline |
|---|---|
| `new-ai-feature` | 12 days, concept to launch |
| `ai-discovery-sprint` | 5 days |
| `quarterly-strategy-review` | 5 days |
| `eval-ops-setup` | 5 days |
| `agent-launch-checklist` | 3 to 5 days |
| `ai-incident-response` | Hours to days |

**A caveat worth stating.** These files were written against an earlier roster and their internal skill lists have not been regenerated since. Treat the sequence and the timeline as current, and verify a named skill against the roster above before relying on it. Logged in `ACTION-PLAN.md`.

**Eleven slash commands** in `commands/` are the short path into common work: `ai-prd-flow`, `brief-me`, `design-ai-feature`, `discover`, `plan-launch`, `retro`, `rtp-setup`, `stakeholder-update`, `strategy-review`, `triage-feedback`, `weekly-digest`.

---

## Packaging and installation

**One plugin, one manifest.**

```
/plugin marketplace add github:raviteja-palanki/rtp-personal-skills
/plugin install rtp-personal-skills@rtp-personal-skills
```

Every skill is then addressable as `rtp-personal-skills:rtp-{name}`.

To update later, use the fully qualified name, because the short form fails silently:

```
claude plugin marketplace update rtp-personal-skills
claude plugin update rtp-personal-skills@rtp-personal-skills
```

**The skills live in three trees, and all three must agree.**

| Tree | Role |
|---|---|
| `2_Skills/` in the author's workspace | Source of truth. Edited here |
| `rtp-personal-skills-repo/skills/` | The mirror this repository ships |
| `.claude/skills/` | The subset deployed to local sessions |

Two things make a naive comparison wrong. The frontmatter `name:` line differs between trees by design, so a sync that rewrites it must replace the first match only. And three skills change folder name between source and mirror, so a comparison keyed on exact name silently skips them.

**Release is one command,** `./scripts/plugin-release.sh`, which validates, bumps the version, audits, commits, pushes and refreshes the installed plugin. Pushing is not the finish line: an installed plugin lags until the update runs.

**Governance is code, not prose.** `scripts/governance-check.py` re-derives every claim this document makes that a machine can verify: the three-way sync, `references/` parity, import resolution, registry versions, the counts and links in this file, and whether the weekly health check has actually run. It exits non-zero on any failure.

---

## Design decisions, and what each one costs

**Composition over routing.** No table maps a question to a skill. The orchestrator reads the situation and picks. The cost is that behaviour is less predictable than a lookup. The gain is that a question nobody anticipated still gets a considered set, which is the whole point of a lens.

**Explicit imports.** A skill names its dependencies, so the library is a graph rather than a pile. The cost is maintenance: an import that stops resolving is a broken promise, which is why a check now fails the build on one.

**Depth over breadth.** One finished skill beats five half-done ones. The visible cost is coverage gaps in areas that would be easy to fill with thin content.

**Every rule carries its "when wrong."** A skill that cannot state its own failure conditions has not been thought through, and a reader who cannot tell when to ignore advice will eventually follow it off a cliff.

**Descriptions are capped at 1024 characters and must be valid YAML.** One malformed description blocks the whole plugin install. The colon trap is the common one: an unquoted parenthetical like `(v3.0: comprehensive)` parses as a nested mapping and breaks silently.

**`rtp-` on every folder.** It marks what is the author's own work, which matters the moment a generic skill with a similar name is installed alongside it.

---

## Diagrams

| File | What it shows |
|---|---|
| [`diagrams/skill-map.svg`](diagrams/skill-map.svg) | The full roster by stage and layer. Generated by `diagrams/build-skill-map.py`, never drawn by hand |
| [`diagrams/02-orchestrator-workers.svg`](diagrams/02-orchestrator-workers.svg) | How the orchestrator composes specialists and what each returns |
| [`diagrams/03-pretested-prd.svg`](diagrams/03-pretested-prd.svg) | Why a craft artifact arrives pre-tested |

Other SVGs in `diagrams/` are samples for `rtp-excalidraw-svg` and carry counts from the roster as it stood when they were drawn. They are not architecture documentation, and `governance-check.py` will fail this file if it starts citing one.

---

*This file is checked by `scripts/governance-check.py` G8 on every governance pass. If a count here disagrees with the repository, the check fails and the file is wrong.*
