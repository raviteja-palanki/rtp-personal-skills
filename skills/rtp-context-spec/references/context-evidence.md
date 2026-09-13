# Context Spec — Evidence and Limits

Reviewed 13 September 2026. These notes explain why some earlier rules were narrowed or corrected. They do not replace evaluation on the intended model, corpus, and workflow.

## Context capacity and memory strategy

[Anthropic, Effective context engineering for AI agents, 29 September 2025](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) supports deliberate context curation, compaction, external notes, and selective retrieval. Its account of degradation is gradual, with differences across models and tasks. It does not establish a universal 50–60% operating limit, a fixed number of visible tools, or the old percentage-savings estimates.

[Anthropic, Harness design for long-running application development, 24 March 2026](https://www.anthropic.com/engineering/harness-design-long-running-apps) describes an evolution in one development harness: Sonnet 4.5 needed resets, while Opus 4.5 largely removed the cited context-anxiety behavior and allowed continuous sessions with automatic compaction. This contradicts the earlier universal claim that full resets outperform compaction. Role separation is an engineering pattern, not proof that evaluators should never inspect implementation details.

## Codifying judgment

**Stave, Kurt, and Winsor, “Teach Your AI How You Make Decisions,” HBR, 25 June 2026.** Read the full article text in the user’s research PDF. It describes ITA Group, AWP Safety, a controller, and Ramp, and recommends moderated discussion of actual scenarios. The transcript is presented as a first draft. Company accounts and productivity anecdotes are not an independently audited estimate of a general effect.

Preserve the useful method without treating its stronger rhetoric as a capability boundary. Agents can learn from examples and observations; individual case-based interviews can elicit judgment; agreement may be informative; unresolved authority disputes need not resolve in one session. A curated precedent record adds scope and approval to the transcript.

**Wilson and colleagues, “4 Steps to Transform the ‘Middle Office’ with AI,” HBR, 20 August 2026.** Full article text read from the user’s PDF. The authors describe proprietary analysis and experiments involving unnamed clients. They report targeted expert questions, rules linked to the exchanges that produced them, and testing against good and bad cases. The nearly-quarter-of-decisions estimate and the claimed generalization from one correction lack enough disclosed method for a transferable forecast.

The pattern supports a controlled learning loop. Add independent error detection and counterexamples: a system need not recognize every exception itself, and one expert answer is not blanket permission to deploy a new policy. Treat expert skill retention and redeployment as questions to measure.

## Research retrieval and organizational readiness

**Davenport and Dörfler, “How GenAI Can and Can’t Help Manage Customer Insights,” MIT Sloan Management Review, 13 July 2026.** Full article text read from the user’s PDF, including the creation/analysis examples and four organizational conditions. The research involved eight consumer-oriented companies, several vendors, and an agency; no sampling frame or causal comparison is given.

The article explicitly discusses tools for creating and analyzing insights as well as storing and accessing them. It does not establish that only storage/access benefit from AI or that all organizational barriers must be fixed before any tool can help. Shared vocabulary matters, but embedding-based retrieval is not categorically unable to handle different meanings of the same term.

Novartis’s WatchOut example flags limited scope, including Europe-only findings. The article does not specify that this happens before generation. It reports $29 million saved on primary market research costs in one year, not a demonstrated recurring annual causal effect of WatchOut. The skill retains the scope-warning mechanism without carrying that number as a forecast.

**“Warner Bros. Discovery: Seeking Growth With Generative AI,” MIT Sloan Management Review, July 2026.** Read the substantive marketing, metadata, and pilot-outcome sections in the user’s PDF. Scene- and shot-level descriptions became a useful content-understanding layer and were handed to the media supply-chain team for production deployment. The broader program had mixed pilot results, including successful production tools. “The pilot mostly failed” is too coarse a description of the reported work.

**Argenti, “To Thrive Alongside AI, Focus on Mindset—Not Skillset,” HBR, 12 June 2026.** The readiness argument informed the earlier skill. Its GDPval figures were not verified here against the benchmark and are unnecessary to the context architecture decision. Do not use them as current capability evidence or as proof that enterprise-wide data unification must precede every scoped deployment.

## Novel Insights cross-check

Re-read the exception-interrogation passage for this revision. Preserve the warning that unrecognized errors can leave a misleadingly clean provenance trail. Narrow the stronger claims: observation is not the only transfer mechanism, a targeted case interview is still an interview, and exception detection can come from people or independent checks as well as the model. A lack of observed reversals is weak validation without adequate error detection and follow-up.

All token, latency, availability, and cost examples in this revision are labeled illustrations or explicit arithmetic. None supplies a vendor price, clinical performance threshold, universal context limit, or guaranteed savings rate.
