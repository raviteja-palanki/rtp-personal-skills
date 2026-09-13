# Research and analogy notes

These notes preserve the skill's evidence and examples while separating research findings, company reports, and the library's proposed applications. Review date: 13 September 2026.

## Configuration-level evidence

[Harness-Bench v1](https://arxiv.org/html/2605.27922v1) is dated **27 May 2026**, not July. It uses 106 sandboxed offline tasks, six configurable harnesses, eight model backends, and 5,194 trajectories; a model-bound coding agent is reported separately. Common task environments and budgets support comparisons of complete configurations. Native prompting and execution behavior vary, so the authors explicitly do not claim causal isolation of individual harness mechanisms. Its results do not establish that 90% of production failures are harness faults. Record the model and full execution configuration when interpreting a benchmark.

[Anthropic's NIST response on agentic security](https://www-cdn.anthropic.com/43ec7e770925deabc3f0bc1dbf0133769fd03812.pdf) and [Trustworthy agents in practice](https://www.anthropic.com/research/trustworthy-agents) discuss defenses across model, tools, harness, and environment. The practical implication is defense across boundaries, not a claim that a runtime hook defeats every injection or that the other layers cannot fail. The original news URL did not resolve during this pass; do not use its asserted date as an independently verified historical milestone.

## Diversity and verification

[DEI, arXiv:2408.07060](https://arxiv.org/abs/2408.07060) reports 34.3% versus 27.3% on SWE-bench Lite: a 7 percentage-point difference, approximately 25.6% relative. Its ensembles include different agent frameworks and shared-model configurations. It is not proof that only cross-lab teams can improve error diversity.

[arXiv:2602.03794](https://arxiv.org/abs/2602.03794) studies heterogeneity in models, prompts, and tools. Its two-diverse-versus-sixteen-homogeneous result applies to the studied settings, not every workflow. Neither paper guarantees evaluator independence. Use task-specific held-out checks and inspect shared blind spots.

## Implementation examples and unverified effect sizes

[LangChain's middleware documentation](https://docs.langchain.com/oss/python/langchain/middleware/custom) describes `before_agent`, `before_model`, `wrap_model_call`, `wrap_tool_call`, `after_model`, and `after_agent`. These are framework extension points, not six universally required services or a guarantee of policy enforcement. Pin the framework version before implementation.

The original Vercel tool-reduction anecdote (roughly 80%), Shopify 20–50-tool heuristic, structured-retry 60% improvement, tool-description-injection approximately 93% success, and Claude Code approximately 1,000-worker cap lack sufficiently established primary scope in this pass. Preserve them as historical research leads, not design limits, expected effects, or current product specifications. Tool descriptions themselves can carry untrusted instructions; that threat remains relevant without an unsupported rate.

Likewise, the Sonnet 4.5 context-anxiety / Opus 4.5 workaround-retirement anecdote is a historical illustration requiring its original configuration and source before reuse as fact. The transferable practice is to retest model-specific workarounds after changes. It does not follow that every workaround expires after one generation.

Examples of managed execution offerings in the source include LangSmith Deployment, Bedrock AgentCore, Vertex Agent Engine, and Anthropic Managed Agents. Treat these as research starting points. Current capabilities, names, interfaces, tenancy guarantees, and responsibility divisions need verification for a purchasing decision.

## Human-team analogies

**Atlassian:** the corpus cites HBR Cold Call, “Atlassian Anchors Remote Flexibility in Structured Daily Practices” (August 2025, HBS 925-029). Page-led meetings and recorded decisions illustrate how flexible location can coexist with shared working practices. Do not inflate this into “every meeting has exactly two pages,” “every employee has unrestricted location choice,” or proof that a documentation habit causes all AI value. Human practices also differ from technically enforced permissions.

**Surgical teams:** the corpus cites “What Operating Rooms Can Teach Leaders About Team Design” (HBR, May 2026), reporting a 20–40-minute difference for the same surgical case across teams and an on-time-start pilot improving from 85% to 96%. That is 11 percentage points, approximately 12.9% relative, from one reported hospital/pilot without a control arm in the account. It motivates checking component interactions, not a validated formula converting prompt/model/reviewer familiarity into agent risk.

**Three-question updates:** the source attributes the completed/next/blocker framing to Ron Friedman's HBR-reported team research (July 2026), while acknowledging that the practice predates it. Proprietary survey evidence does not establish that requiring three fields prevents agent failures. The machine-readable contract and repair behavior are this library's proposals; test them against relevant context-loss failures.

## Novel Insights applied

The ledger's control-scope observation is useful: ask what a control actually establishes and what people assume it establishes. A schema checks a contract, a test checks selected behaviors, a log records events under its integrity model, and a sandbox constrains configured resources. None should silently stand in for the others.

The ledger's platform and shared-documentation cases suggest looking below a visible use case for reusable capabilities. They do not establish that every company must build a platform first, that all such platforms are moats, or that buying one cannot work. Its discussion of tool-dependent measurement also supports recording the evaluation configuration. Escalation rate and handoff count remain different measures.
