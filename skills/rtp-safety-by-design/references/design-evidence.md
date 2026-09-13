# Safety design: source boundaries

Reviewed 13 September 2026.

## Constitutional methods and classifiers

[Bai et al., December 2022](https://arxiv.org/abs/2212.08073) describe Constitutional AI as a training approach using principles and AI feedback. Prompt-time instructions influence behavior without themselves performing that training.

[Anthropic’s 9 January 2026 Classifiers++ account](https://www.anthropic.com/research/next-generation-constitutional-classifiers) describes a cascade combining internal probes with an exchange classifier that examines inputs and outputs together. The company reports lower harmless-query refusal and compute overhead than its previous system, while acknowledging remaining attack classes. This is direct evidence against treating all filters as keyword matchers or assuming that the model’s own safety training makes external checks unnecessary. Its specific model, traffic, test, and observation period do not supply universal coverage or latency targets. A lack of a discovered universal jailbreak at that point was not a claim that no harmful output could pass. [Research paper](https://arxiv.org/abs/2601.04603).

The original skill’s 80–90%, 90–95%, 60–70%, “near 100%,” 1–2 KB per constraint, 50–200 ms, >90% prompt-only, >95% first-two-layer, and 10% fallback limits were not established empirical standards. Neither was “exponentially harder to defeat.” Measure the actual system and consequence instead.

## Minimum viable governance

The full user-provided **Balance AI innovation and risk with ‘minimum viable governance’**, Kristin Burnham, MIT Sloan, **15 June 2026**, was read. It summarizes work by Nick van der Meulen, Jennifer Jewer, and Nadège Levallet and describes five governance domains and four design characteristics. Its trustworthy-by-design examples include prompt/output logging, masking, hallucination screening, and policy filtering. These are platform-design examples, not a validated four-control safety certificate.

The [MIT CISR glossary](https://cisr.mit.edu/research-library/glossary) confirms the five domains—principles, policies, people, processes, platforms—and the characteristics of structural agility, integrated operation, opportunity sensitivity, and oversight embedded by design. The research briefing itself was not separately evaluated in this pass. The article’s earlier minimum-viable-policy performance comparisons should not be recast as measured effects of this AI control checklist.

The Novel Insights passage at lines 433–454 raises a useful question about who can change or weaken controls. Its claims that embedded controls catch only anticipated violations, that adaptable governance necessarily loses authority, and that tooling necessarily removes reviewer standing are hypotheses with counterexamples, not established design laws. Embedded authorization can prevent an entire action class; classifiers can generalize. Keep competent ownership, change controls, response authority, and evidence without dismissing automated protection.

## Interaction style and override attempts

The full user-provided **Does Your AI Have a Personality Problem?**, HBR, **24 June 2026**, by Przegalinska and colleagues, was read. It reports 58 participants, with 31 assigned a supportive servant-leader style and 27 a hostile dark-triad style, in a simulated marketing task with AI framed as supervisor. It reports 13% versus 1% resistance messages, 72% higher peak skin conductance in the hostile condition, about one point lower expert-rated quality on a seven-point scale, roughly twice the variability, and little difference in standard self-reports.

The article says override attempts were four times more frequent and later describes attempts to ignore rules or change character as occurring only in the hostile condition. Those sentences may use different categories or denominators; the article does not resolve them. Its linked [underlying SSRN paper](https://ssrn.com/abstract=6804219) was not accessible in this pass. Keep the exact ratio unresolved rather than combining both sentences into one precise claim.

This is evidence for investigating interaction design alongside behavior and output quality. It is not a field estimate of malicious activity, a stress detector for individual users, or proof that every override is benign. The article itself notes the extreme persona and cautions against sycophancy as the replacement.
