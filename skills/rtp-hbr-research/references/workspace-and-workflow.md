# Research workspace and resumable workflow

Reference revision 3.7.1 — reviewed 13 September 2026. Paths below are relative to `~/Desktop/Claude` unless stated otherwise. Verify live paths before reading or writing; this map does not authorize unrelated corpus maintenance.

## Source and state map

Let `RESEARCH` mean `3_Research/09_hbr-and-journals/` in this reference.

| Location | Purpose |
|---|---|
| `3_Research/00_NEW/` | Intake awaiting the librarian's classification and metadata checks |
| `RESEARCH/mit-sloan/` | MIT Sloan material; inspect the actual publication and dated intake folder |
| `RESEARCH/hbr-articles/<topic>/` | Topic shelves, including leadership-and-workforce, strategy, ai-agents, customer-and-market, responsible-ai, data-and-measurement, innovation-and-rnd, and adoption-and-roi |
| `RESEARCH/ARTICLE-GRAPH.csv` | Generated graph of source paths and note, card, framework, case, routing, and status fields |
| `RESEARCH/_synthesis-engine/START-HERE-NEXT-SESSION.md` | Live continuation instructions and dated state |
| `RESEARCH/_synthesis-engine/queue_2026.csv` | Current named queue; verify whether a later year has a new queue |
| `RESEARCH/_synthesis-engine/PROMPT-FOR-NEW-ACCOUNT.md` | A continuation handoff, not authority to override the current user request |
| `RESEARCH/_synthesis-engine/NOVEL-INSIGHTS.md` | Dated cross-source claims, refinements, and counterexamples |
| `RESEARCH/_synthesis-engine/OPEN-ASSUMPTIONS.md` | Consequential unknowns and decisions needing resolution |
| `RESEARCH/SYNTHESIS-COVERAGE-TRACKER.md` | Coverage of source reading and associated output |
| `RESEARCH/_frameworks/EXTRACTION-SPEC.md` | Shared extraction schema for frameworks and cases |

The `_synthesis-engine/Q2_2026/` folder is the June run's historical home. It contains `EXISTING-WRITING-INDEX.md`, `MASTER-TRACKER.md`, `APPLICATION-TRACKER.md`, `RUNNING-PATTERNS.md`, `GLOSSARY.md`, and `00-METHOD.md`. Some remain shared references; consult the live continuation note to identify which current run owns updates. Do not automatically write new work into an old month's tracker because it appears in this list.

The earlier `1_hbr-ai-2026/` and `hbr-synthesis/runs/<month>/` paths are retired layouts. The `1_Projects/2_Playbook_AI/hbr-synthesis-engine-state_Q2-2026/` directory contains historical orchestration machinery and progress markers, not research articles. Keep it outside source shelves.

### Generated indexes and reconciliation

Current tools include `_synthesis-engine/tools/rebuild-graph.py`, `rebuild-queue.py`, and `3_Research/_tools/index-check.py` and `rebuild-map.py`. Read tool usage and inspect current state before a mutation. Generated files should be rebuilt through their source workflow, not hand-edited to make counts agree. Report counts with their scope and observation time; historical counts may remain when clearly labeled.

Distinguish forward failures, reverse coverage gaps, and policy exclusions. A real file excluded from an index by policy is not necessarily a dead path. Compare Unicode names consistently and review proposed repairs before changing an index. The earlier index incident confused these categories and almost removed valid rows.

For a duplicate stem or a platform that cannot represent an existing filename, preserve the stable article identity and record an explicit, reviewable mapping. Do not silently slugify or overwrite one source with another. Improve tooling where practical; portability constraints still need an honest solution.

## Destination map

- **Skills:** AI-PM sources commonly live at `2_Skills/ai-pm-skills/<cluster>/skills/<skill>/SKILL.md`; other personal skills live elsewhere under `2_Skills/`. Resolve the actual source through the registry. The `/skills/` segment matters for cluster skills. Mirror and deployment names can differ intentionally, and not every source is deployed to `.claude/skills/`.
- **Website:** current article files live under `1_Projects/1_my-personal-website/1_My Series-MD-FILES/My Website all latest MD files/`. Current folders include `agentic-stack-md`, `harness-engineering-md`, `environment-series-md`, `evals-series-md`, `ai-pm-os-md`, `site-pages-md`, and `frontier-companies-md`. Confirm actual paths rather than relying on old chapter numbering. The sibling `version1/` is a historical archive, not the current editing target.
- **Public URLs:** use `1_Projects/1_my-personal-website/WEBSITE-URL-INDEX.md` and verify the appropriate mapping. Do not derive a public slug from a source filename or assume every page follows one URL pattern.
- **Playbook:** `1_Projects/2_Playbook_AI/AI_Playbook.md`. Use the named current section and inspect the relevant build workflow before regenerating HTML or PDF.

A historical title or slug can help find a candidate; reading the actual file confirms the target. A source-to-target map is useful only when it remains connected to the content.

## The cycle

1. **Frame:** read live state, choose a bounded set, verify source keys and paths, establish the objective, and identify what downstream work is authorized.
2. **Read and extract:** read each selected source fully and produce the agreed records. A normal full-cycle unit includes the note, frameworks, cases, and application card. Record any deliberately deferred stage.
3. **Review:** check source fidelity, method, framework completeness, scope, claims, and clarity. Record completion per file and source version.
4. **Reconcile:** compare patterns across the selected set and earlier relevant work. Include every in-scope source in the coverage ledger, including useful notes outside an older manifest. A source excluded from the selected set should be named as such, not silently pulled into an unrelated run.
5. **Apply:** use the reviewed cards for authorized changes. Skills can be updated as coherent batches finish; combine changes to one website article or playbook section to avoid collisions and repetition. Follow a specific run's agreed order when cards or application are deferred.
6. **Close:** verify artifacts, update reading and application state, reconcile ledgers, refresh relevant indexes, synchronize intended copies, and record pending publication or builds. Give the next session an accurate continuation point.

A provisional synthesis can be useful before every source is finished if it is labeled with coverage limits. A final synthesis of the selected set requires each source's agreed review. Notes and artifacts are durable work; in-memory reports alone are not a recovery plan.

## Optional delegation and historical orchestration

The historical `_army-deep-synthesis.js` was built for a particular environment and Workflow tool. Its existence does not mean the current host can run it, or that it should be launched for this request. Inspect its inputs, writes, resume behavior, and current compatibility before use.

When delegation is explicitly appropriate, use bounded independent reading or extraction tasks. Give each worker the exact sources and destinations, the extraction contract, a relevant exemplar, evidence rules, current insight entries, writing guidance, and a clear report format. Require named source references and uncertainty reporting. Keep cross-source reconciliation central, while allowing workers to propose connections from the material they actually read. Do not claim that only one agent is capable of pattern finding.

Review returned files against their sources and record the covered versions. Preserve useful work after interruptions. A `.pass` marker must identify the review it represents; it cannot make a subsequently changed note permanently exempt from review. A single search is not a universal citation check.

The June run's excessive fan-out, lost reviews, orphaned progress artifacts, and near-missed rich notes explain the emphasis on bounded work, durable state, and complete coverage. Historical defaults such as batches of twelve or clusters of seven to ten are starting points, not current capacity measurements. Ravi's request for sequential main-agent work takes precedence.

## Topic organization

Use the [theme taxonomy](theme-taxonomy.md) as a discovery and routing aid. It is separate from the filesystem shelf policy. A title can suggest a provisional theme, but final classification follows the source's actual argument. Sources may need secondary tags, and a stable identifier is more important than forcing one theme to describe everything.
