# Evidence, calibration, and limits

This reference preserves the skill's studies, numerical examples, and product comparisons while separating observation from recommendation. A source can motivate a local test without establishing a universal UX rule.

## Measure confidence on matching scales

For a defined task and correctness criterion, collect representative outputs with numerical predicted probabilities. Group comparable predictions and compare each group's mean probability with its observed correctness rate. Report sample sizes, uncertainty, and relevant segments. Select a sample that supports the precision and decisions needed; 100 outputs is not a universal minimum or sufficient count.

Plot **mean predicted probability on X** and **observed correctness on Y**, both from 0 to 1:

- On the diagonal, observed rates match predictions within sampling uncertainty.
- Above the diagonal, the system is underconfident: predictions of 0.60 with 0.80 observed correctness understate performance.
- Below the diagonal, the system is overconfident: predictions of 0.80 with 0.60 correctness overstate performance.

A verbal label, icon, or response-pattern level is not a probability. Do not interpret a diagonal without a justified numerical mapping. Test what users understand and whether they take the intended action. Model self-reports also require validation. Aggregate calibration does not establish discrimination, acceptable severity, useful coverage, or effective human checking.

Keep decision thresholds separate from calibration. A well-calibrated 90% prediction can be inadequate for a consequential action; a lower probability can still be useful for safely generating candidates. Changes in model, data, task mix, or interface may require rechecking both signal validity and user interpretation.

## Explanations: preserve the intervention and population

The Lane/Boussioux working-paper abstract reports 228 evaluators, 48 early-stage innovation submissions, and 3,002 screening decisions, comparing human-only, black-box recommendation, and narrative-rationale conditions. Outcomes used an independent expert benchmark. The abstract reports greater decision quality for black-box recommendations and more compliance without the same quality gain for narratives. This is evidence about that screening setting, not every form of explanation. [HBS working paper](https://www.hbs.edu/ris/download.aspx?name=25-001.pdf).

Earlier local notes recorded: a 4.3-point decision-quality improvement for black-box recommendations; roughly 10-point increases in compliance with accept recommendations; rejection-compliance increases of 21.2 points for black-box and 26.9 for narrative; and an 11.9-point reduction in detection with explanation. The full numerical tables were not accessible for fresh verification in this editorial pass. Retain these as **reported local figures**, with outcome definitions, baseline, uncertainty, and paper version to be verified before quantitative reuse. Expert labels are a benchmark, not infallible objective truth about an innovation's future success.

The separate HBR “Research: The Innovation Problems AI Can't Solve” account lacks enough study identifiers in the supplied material to establish whether its screening example is independent of this paper. Do not count it as a second independent replication. The air-traffic-control simulation mentioned in a May 2026 HBR IdeaCast is likewise an indirect research lead, not verified evidence for a mandatory clicking or rotation rule.

There is relevant counterevidence to a blanket claim that explanations cannot improve review. Rieger and colleagues' 2026 *AI Error Difficulty Modulates the Effectiveness of Explainability in Decision Support Systems* reports three simulated visual-detection experiments. Explaining a known weakness reduced reliance on incorrect recommendations for difficult errors, with different effects for easy and nearly unverifiable errors. This supports distinguishing explanation content and task difficulty. It does not establish effectiveness for an arbitrary deployed rationale. [Primary ACM article](https://doi.org/10.1145/3817603).

Design tests that distinguish a rationale, source evidence, process trace, and specific weakness disclosure. Measure outcomes, useful and harmful interventions, and relevant decision directions. Required reasons or disclosures must remain available at the appropriate time; do not infer that all regulated decisions require the same explanation or that all explanations should be hidden until after a choice.

## Persona: reported effects are not production thresholds

The MIT Media Lab seminar abstract for Przegalinska and Triantoro describes a comparison of Servant Leader and Dark Triad personas with physiological and self-report measures. It reports a partial mismatch between physiological reactivity and reported experience. The abstract does not establish that every behavioral proxy or self-report fails. [Primary seminar account](https://www.media.mit.edu/events/aha-seminar-series-aleksandra-tamilla/).

The supplied HBR “Does Your AI Have a Personality Problem?” notes describe n=58, a marketing task with AI framed as supervisor, and the following figures: 72% higher peak skin conductance; resistance messages in 13% versus 1% of exchanges; approximately one point lower quality on a seven-point scale with about twice the variability; and similar satisfaction reports. Those detailed numbers remain locally reported rather than freshly verified against the underlying paper.

The older sentence “override attempts 4× more often, and only in the hostile arm” has an unresolved denominator: “only” and a finite between-arm ratio cannot both be interpreted literally when the comparison count is zero. Verify the original measure before repeating it. Do not convert physiological arousal into a diagnosis of stress for an individual or extrapolate an extreme lab persona to mild conversational brusqueness.

Behavior, output quality, self-report, and—where appropriate—physiology can offer complementary views. In production, define and inspect turn-length, rephrase, resistance, and override measures without treating them as validated stress detectors. Respect privacy and research consent.

## Competence, warmth, and goal alignment

The April 2026 *Wharton Blueprint for AI Agent Adoption* distinguishes perceived competence from capability and explicitly extrapolates some chatbot findings to agents. Its 54.2% recommendation-acceptance figure is limited to long-term or virtue-oriented choices; the discussion reports a different direction for pleasure-oriented choices. It is not a universal effect of tying any action to a goal. The earlier skill's 14.6% transparency and 7.2% collaboration figures were not located in the accessible Blueprint text and remain unverified leads. [Blueprint](https://ai.wharton.upenn.edu/wp-content/uploads/2026/04/Wharton-Blueprint-for-AI-Agent-Adoption.pdf).

The primary research is Liu, Xu, Yang, and Li, *Mindful Machines* (2025), examining perceived theory-of-mind capability and consumer recommendations. The task and manipulation matter; a system's claim to understand a person is not proof that it does. [University-hosted paper](https://eprints.soton.ac.uk/504046/1/Psychology_and_Marketing_-_2025_-_Liu_-_Mindful_Machines_Understanding_How_AI_s_Theory_of_Mind_Capabilities_Influence.pdf).

The local HBR article dated 9 September 2026 and the Concentrix executive quotation combine research and practitioner commentary. Keep employee willingness to delegate separate from customer-service frustration. Cleo was an illustrative product reference, not independent validation of a universal goal-alignment effect; verify its current behavior before teaching a specific interaction.

The practical design question is whether tone and evidence help this user act appropriately. Respectful warmth and competence need not be opposites. Do not claim a live learning process, fabricated precision, or success statistics to produce trust. A cue that improves willingness to use an unreliable system can worsen the outcome.

## Experience sequencing and disclosure

The six orientation-to-meaning questions are adapted from Nunes and Heimann's HBR “Why the Best Immersive Experiences Succeed,” July–August 2026. The supplied material offers theoretical grounding and examples but no direct outcome test of a fixed order for AI interfaces. Use the sequence as a diagnostic, not a law that every earlier failure blocks every later benefit.

Novel Insights connects disclosure cases through actionability and timing. The CBA podcast discusses a case set in 2017, published as a case in 2018 and discussed on air in 2026; its outcome is withheld. The Porsche and CBA stories therefore do not establish a causal rule about disclosure increasing sales. They suggest asking what information the recipient needs while action is still possible. Lack of recourse does not remove a right or obligation to know, and reducing short-term completion is not by itself proof that a disclosure is bad.

## Dated product comparisons

SpaceXAI's 3 September 2026 [Grok Bot design account](https://x.ai/news/designing-grok-bot) describes status, optional action detail, and a separate workspace. This is a vendor design account and reported observation, not a controlled demonstration that animation eliminates abandonment or that detailed views make novices leave.

Cursor's [Projects announcement](https://cursor.com/blog/projects) describes longer-running work; use the exact surface before attributing an interaction model to the whole product. Its [SpaceX announcement](https://cursor.com/blog/joining-spacex) concerns company status, not evidence that a particular UX pattern works. The earlier library correction distinguishes the 14 August 2026 completion announcement from an agreement date; refresh the source if the corporate detail is relevant.

The earlier xAI citation notes, checked on 9 September 2026, describe tool-returned URLs and optional inline citations. Treat API response behavior and what the grok.com interface displays as different claims. A retrieved source list can differ from the evidence used for a final claim. Verify current documentation and the actual interface before teaching precise behavior; no live interaction with these products was performed in this wording pass.

## Historical examples that must not become gates

The prior skill included a five-error/ten-user test, a 50% detection cutoff, 100 calibration outputs, a 10% calibration tolerance, and a 95% approval-rate warning. These were not established general release standards. Choose representative correct and incorrect cases, a relevant sample, and criteria proportionate to consequence. Do not expose real consequential actions to unmarked planted errors.

The former trust-recovery table claimed three to six months for enterprise tools, two to four weeks for internal tools, same-session retries for consumer tools, and permanent distrust in some regulated settings. No supporting benchmark series was supplied. Retain these only as examples of what to investigate, not as factual recovery estimates. The 24-hour/7-day return windows and 30% drop threshold are likewise illustrative. Account for task frequency, error severity, alternatives, and the possibility that lower use is appropriate.

The old under-trust example—85% accuracy with 20% use—and proposed “95% of users find this helpful” message do not justify hiding uncertainty. Use only real, relevant measures, distinguish accuracy from helpfulness, and state their population and scope. A correction can support recovery, but do not promise the fastest recovery, guaranteed renewed trust, or automatic model learning from a report.
