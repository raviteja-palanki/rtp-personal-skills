# Evidence and Review Notes

Reviewed 13 September 2026.

## Primary research and practice references

[Shankar et al., Who Validates the Validators?](https://arxiv.org/abs/2404.12272), submitted April 18, 2024, describes EvalGen and criteria drift: seeing outputs can help people refine evaluation criteria. This does not mean no requirements can be written beforehand, or that a rubric must change every month. Document the reason and preserve comparability when it does change.

[Anthropic's agent evaluation guide](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents), January 9, 2026, distinguishes capability from regression evaluation and describes successful cases graduating into regression protection. It also describes teams adding evaluations after early development, including Claude Code and Bolt. Early evaluation is useful; “before the first prompt or the product is invalid” is stronger than the reported practice. A high regression score is useful even when it no longer provides an improvement target.

[Constitutional AI](https://arxiv.org/abs/2212.08073), December 2022, is a primary source for related assistant-alignment work. Helpful/Harmless/Honest provides a broad lens, not a complete product rubric or a proof that three scores establish safety. The older source URL in the skill was not retrievable in this pass; use the paper link.

The original also points to Braintrust's eval-driven-development article and a third-party promptfoo CI/CD post. Treat these as implementation/practice leads, not evidence that one precise deployment pattern is universally standard. Check current official tool documentation if implementing the pipeline.

## Schneider Electric: preserve denominators and the limits of the case

The complete user-supplied primary MIT SMR PDF, “How Schneider Electric Scales AI in Both Products and Processes,” by Thomas H. Davenport and Randy Bean, is dated **March 16, 2026**. A regional search result carries a later March 25 date. The primary article describes vision, ideation, incubation, and deployment at scale, with business plans/cases reconfirmed at gates. It also describes an adoption KPI and performance KPI for internal applications, with business stakeholders owning the value proposition and helping develop the measures.

The reported mix is about **60% analytical AI in overall AI work**, **40% generative AI among customer-facing applications**, and **70% generative AI among internal employee tools**. These are different denominators and possibly differently weighted concepts of work/applications; do not add them or force them to reconcile as one portfolio pie chart. They are one company's self-report, not independently audited proportions or guidance for another organization.

The article's stage-gating comparison is the authors' observation, not a measured prevalence study of AI teams. It reports confidential value estimates, so it does not establish a publicly reproducible return on the platform. Its preference for deployment at scale does not show that incubation involved no testing or that pilots are never appropriate. Its executive's 80–90% accuracy comment is a contextual view about reviewed work, not a general safety or release threshold.

## Source lineage and process degradation

Holweg and Davenport's “Don't Let AI Slop Muck Up Your Company's Processes,” HBR, June 16, 2026, is the original source lead for upstream transformation concerns. The cited 42% rise in Organization Science submissions and declining writing quality was attributed through a Forbes article, not verified here against a journal dataset. Keep it as a source-reported illustration, not a measured causal effect of the number of AI passes.

Source tags make provenance inspectable. They do not certify a source as true or guarantee that a retrieval-grounded transformation preserved it faithfully. Multi-step systems can add value as well as accumulate errors; evaluate the actual transformations and outcome.

## Novel Insights reconciliation

The ledger passage at lines 129–148 identifies Vanguard's evaluation stack as a response to models already spreading through the organization. It is a useful counterexample to a rigid “evaluation must precede any development” chronology. Starting later does not remove the value of adopting the loop now.

The adjacent claim that a monitoring platform probably cannot compound because it is “a control” is too categorical: monitoring can feed recurring release, remediation, and investment decisions. Similarly, eight company narratives from common authors are not eight independent causal confirmations of platform ROI. Carry the recurring-decision question forward without turning it into an automatic platform-first or use-case-first verdict.

## Original diagnostic numbers and conflicting rules

The examples of 90% summary success, two-second latency, 70% thumbs-up, 20–50 initial cases, 50–100 golden cases, weekly 10–20 additions, monthly 20–30% replacement, three-month age limits, and 2–4-week rubric reviews were not validated universal cutoffs. The same applies to correlation bands 0.3/0.7, coverage bands 30/50/70%, one-hour feedback, and daily full-suite runs. State local reasons, samples, and uncertainty.

The original alternately said to preserve mastered cases forever and to remove trivial golden cases quarterly. The revision preserves **purposeful coverage**, with versioned retirement reasons. It also resolves “run the full suite before every iteration” versus “do not run it until a small slice passes”: choose the smallest useful check for iteration, then sufficient checks for release and interaction risk.

Illustrative score changes 76→81, 79→84, or 72→89 do not prove product gains without a comparable dataset and scorer. Nor does a gap between an eval percentage and a satisfaction percentage establish misalignment: their units, population, and construct may differ. A “missing detail” cannot be assigned medium severity merely by assuming users retain 80% of the value.

The source's Goodhart wording is a common shorthand for target-induced measurement failure, not a guarantee that every optimized measure stops being useful. Do not infer gaming from any rubric revision or legitimate few-shot example. Protect held-out claims, inspect real outcomes, and disclose contamination when it occurs.
