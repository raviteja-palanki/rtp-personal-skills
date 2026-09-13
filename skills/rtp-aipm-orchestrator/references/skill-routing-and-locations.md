# Skill routing and workspace references

Read the relevant sections when selecting a companion skill or locating source material. Paths are relative to `/Users/ravitejapalanki/Desktop/Claude/` unless otherwise stated. In another installation, locate the equivalent workspace. `CLAUDE.md` section 4 is the authority for write targets and known location exceptions.

This roster is organized for retrieval, with some skills repeated where they serve another decision. It is not a category-count authority or a workflow requiring every listed skill. Check `2_Skills/SKILL-REGISTRY.md` and the actual skill for current availability, version, and behavior. Use the generated `rtp-personal-skills-repo/diagrams/skill-map.svg` for a visual overview, and derive reported counts from the current inventory.

Names can differ across installations. The source orchestrator `rtp-orchestrator` is packaged and deployed as `rtp-aipm-orchestrator`. Extended thinking maps from `rtp-ravi-thinking-skills` to packaged `rtp-thinking-skills` and deployed `ravi-thinking-skills`; branding maps from `rtp-ravi-personal-branding` to packaged `rtp-personal-branding` and deployed `ravi-personal-branding`. Resolve the installed name and read its file. Preserve existing deployment subsets rather than assuming every source skill must be installed in every host.

## Domain roster

### thinking-core | how to reason about it

`rtp-first-principles` · `rtp-judgment-guard` (formation, retention, use, and assessment of human judgment) · `rtp-alignment-check` (links from purpose to operating systems) · `rtp-stress-test` · `rtp-falsification` · `rtp-bias-spotter` · `rtp-determinism-compass` (rules, models, and appropriate guarantees) · `rtp-dual-lens` · `rtp-problem-type` · `rtp-gossip-mode`

`rtp-failure-design` is a retired redirect, not an active companion to invoke or count. Follow its verified destination, `rtp-failure-modes`.

### ai-strategy | value and defensibility

`rtp-strategy-canvas` · `rtp-moat-finder` (defensibility, stocks and flows, and value capture) · `rtp-build-or-buy` (ownership and sourcing choices) · `rtp-capability-tracking` (build, adapt, wait, and capability evidence) · `rtp-ai-portfolio-management` (investment types and shared foundations) · `rtp-adoption-launch` (adopter value, readiness, rollout, and possible learning curves) · `rtp-token-economics` · `rtp-signal-scanner` · `rtp-trendslop-check` (empirical claims, source scope, and numerical reasoning) · `rtp-vision-setting` · `rtp-purpose-dialogue` · `rtp-marketing-to-ai-agents`

### product-sense | should this exist, and for whom

`rtp-problem-ai-fit` (diagnose the bottleneck before prescribing AI) · `rtp-ai-use-case-readiness` (task suitability and practical readiness) · `rtp-ai-ux-patterns` (interaction patterns, engagement, and evidence-aware review) · `rtp-uncertainty-research` · `rtp-fit-signal` · `rtp-jtbd-analysis` · `rtp-opportunity-solution-tree` · `rtp-attitudinal-segmentation` · `rtp-needs-guard` · `rtp-feedback-flywheel` · `rtp-feedback-triage` · `rtp-failure-modes` · `rtp-invisible-stack` · `rtp-interview-synthesis` · `rtp-ai-product-taste`

### agent-design | how the machine is built

`rtp-agent-harness` (MHTE, operating contracts, and failure diagnosis) · `rtp-agent-ecosystem` (topologies, interactions, and coordination costs) · `rtp-autonomy-spectrum` (non-AI baseline, AI roles, actual permissions, and graduated autonomy) · `rtp-tool-architecture` (tools as contracts) · `rtp-harness-operating-model` (program ownership and shared capabilities) · `rtp-multi-modal-product-design`

### eval-and-quality | how to assess quality

`rtp-eval-framework` (criteria, representative cases, evidence, and meaningful discrimination) · `rtp-eval-driven-development` (evaluation across development stages) · `rtp-ai-product-metrics` (user outcomes, operational measures, and decision quality) · `rtp-production-observability` · `rtp-observability-stack` · `rtp-confidence-tuner` · `rtp-gen-ai-experimentation`

### safety-and-trust | what happens when it goes wrong

`rtp-responsible-ai-program` (SHARP, preventive controls, practical authority, and accountable response) · `rtp-safety-by-design` · `rtp-safety-as-moat` · `rtp-agent-risk` · `rtp-trust-ladder` · `rtp-trust-under-fog` · `rtp-breach-ready`

### craft | the artifacts

`rtp-ai-prd` · `rtp-agent-spec` · `rtp-context-spec` · `rtp-prompt-craft` · `rtp-prompt-as-product` · `rtp-user-stories` · `rtp-cost-model` · `rtp-ship-decision` · `rtp-competitive-map` · `rtp-stakeholder-communications` (the 5 types, candor as a payoff problem) · `rtp-fit-signal`

### writing, design and governance | everything else

`rtp-thinking-writing` (the standing thinking and writing guidance) · `rtp-humanizer` (supporting reference for recurring writing problems) · `rtp-ravi-thinking-skills` (the extended judgement set) · `rtp-deep-dive-writer` · `rtp-hbr-research` (the synthesis and apply loop) · `rtp-research-synthesiser` · `rtp-research-librarian` (filing) · `rtp-ravi-personal-branding` (all visual surfaces) · `rtp-ux-design-systems` · `rtp-design-spec` · `rtp-excalidraw-svg` · `rtp-lucid-boards` (Lucid print posters; use the skill's five-seat review and acceptance criteria) · `rtp-cinematic-presentations` · `rtp-frontend-slides` · `rtp-readme-storytelling` · `rtp-email-mastery` · `rtp-interview-skill` · `rtp-ravis-resume-builder` · `rtp-product-thinking` · `rtp-ai-fluent-brand` · `rtp-skill-refresh` · `rtp-claude-admin` (use for explicitly requested administration, including "admin mode," and established authorized governance reviews)

## Choose skills by the decision

| Task | Starting skills and order |
|---|---|
| Is AI appropriate for this problem? | Start with `rtp-problem-ai-fit`; use `rtp-ai-use-case-readiness` to examine the proposed task and operating conditions. Readiness evidence can change the fit judgment. |
| Product economics | Use `rtp-cost-model` for cost per outcome and `rtp-token-economics` for pricing and value capture. Add `rtp-moat-finder` when defensibility is part of the question. |
| Agent design | Clarify the task and actual permissions with `rtp-autonomy-spectrum`; use `rtp-agent-harness` for the system and `rtp-agent-ecosystem` for interactions. Bring tool, evaluation, cost, safety, and recovery work in before consequential actions are designed. |
| Empirical numbers that support a conclusion | `rtp-trendslop-check`; use direct checks for arithmetic, file counts, and version numbers |
| Writing or a reply | `rtp-thinking-writing`; consult `rtp-humanizer` for specific recurring patterns |
| Lucid board, classroom poster, or board reproduced as a handout | `rtp-lucid-boards`; verify actual exports and delivered size. Use a document workflow for a worksheet or a separately designed reading handout. |
| Interview preparation or personal work claims | `rtp-interview-skill` and relevant experience records; distinguish actual ownership, authored analysis, and hypothetical approaches. Add the resume builder when an application artifact is requested. |
| Research intake, synthesis, or maintenance | `rtp-research-librarian` for filing, `rtp-hbr-research` for the defined source-analysis cycle, and `rtp-research-synthesiser` for cross-source synthesis. Use `rtp-skill-refresh` for an authorized review of reusable guidance. |

Prefer the relevant RTP skill when it fits. Host and specialist skills can supply complementary tooling or mandatory workflows.

## Current writing and playbook locations

Read current article markdown under `1_Projects/1_my-personal-website/1_My Series-MD-FILES/My Website all latest MD files/`. Superseded folders such as `Archive/version1_All series/` are for historical tasks.

Within the website project, `ask-ravi-bot/corpus/url-map.json` is the retrieval system's live-URL authority. `WEBSITE-URL-INDEX.md` is the human-readable list, and `ask-ravi-bot/corpus/website-urls.csv` is another machine-readable reference. Verify the exact URL; filenames and slugs can differ.

| Series | Hub |
|---|---|
| Agentic Stack | https://ravitejapalanki.com/writing/agentic |
| Harness Engineering | https://ravitejapalanki.com/writing/harness |
| Environment Engineering | https://ravitejapalanki.com/writing/environment |
| AI Evals | https://ravitejapalanki.com/writing/evals |
| AI PM OS | https://ravitejapalanki.com/writing/ai-pm-os |
| Frontier companies | https://ravitejapalanki.com/writing/frontier |

Finished playbooks and their interview companions live in `1_Projects/1_my-personal-website/1_My Series-MD-FILES/Important playbooks/`. Read its `CONTEXT.md` for the current per-file state and use the final editions identified there.

The established final files are:

- `playbook-harness. engg/final playbook/The-Harness-Engineering-Playbook-Definitive-Draft-6.md`
- `playbook-harness. engg/final playbook/How-I-Explain-Harness-Engineering-Interview-Definitive-Draft-6.md`
- `Frontier playbook/The-Frontier-Companies-Playbook-Draft-6-Combined.md`
- `AI_Playbook.md`, with its appendix and print editions

`AI_Playbook.md` is edited in `1_Projects/2_Playbook_AI/`, its separate authoritative workshop. Refresh the shelf and generated research copies after rebuilding. New company cases and measurement findings often belong in "The Operator's View." Quote the legacy `playbook-harness. engg` path carefully; use null-delimited traversal for filename batches.

Treat Ravi's playbooks and published work as primary sources for his positions. Read the project source when editing, and check its current status before citing it.

A playbook's argument or an authored case analysis does not, by itself, establish that Ravi deployed the described system. For his experience, verify role, dates, scope, and outcomes against personal records and his account. For an external company's results, inspect the underlying evidence rather than treating the playbook's retelling as independent corroboration.

## Research indexes

| File | Purpose |
|---|---|
| `3_Research/INDEX.csv` | Authoritative file locations |
| `3_Research/MAP.md` | Generated coverage and current counts |
| `3_Research/PODCAST-INDEX.csv` | Episode and guest retrieval; search the `themes` column |
| `3_Research/BOOKS-INDEX.csv` | Chapter retrieval; check `early_release` before citing |
| `3_Research/09_hbr-and-journals/ARTICLE-GRAPH.csv` | Article notes, framework and case extraction, and synthesis status |
| `3_Research/09_hbr-and-journals/_synthesis-engine/NOVEL-INSIGHTS.md` | Patterns developed across sources, with support and conditions for reconsideration |

## Examples of synthesis to investigate

The prior orchestrator used these examples to illustrate connections. They are inherited interpretations, not findings newly verified by this wording revision. Read the ledger and underlying sources before reusing an empirical claim.

- **Similar ideas can arise through different mechanisms.** Retrieval may favor familiar material while people may also anchor on an early suggestion. If both mechanisms operate, changing retrieval alone may leave the human contribution unresolved.
- **A continuously refreshed corpus has upstream conditions.** A business relying on recurring contributions needs to examine consent, rights, incentives, and compensation. The useful question is what makes that flow sustainable in its actual setting.
- **Time savings depend on what happens next.** Faster work creates a business result only when the organization can use the released capacity. Examine workflow changes, demand, and measurement rather than treating saved hours as realized value.

Use such connections when they answer the question, and retain their alternative explanations and limits.
