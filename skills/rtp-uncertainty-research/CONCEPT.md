# Uncertainty Research — Concept Guide

## FIRST PRINCIPLES

User research was built for deterministic products. Show 10 users a button — all 10 see the same button. Test a workflow — every participant experiences the same workflow. This assumption of consistency enables controlled experiments, usability benchmarking, and reliable A/B testing.

AI products violate this assumption fundamentally. Show 10 users the same AI feature and they may experience 10 different outputs. The "product" is not a fixed artifact — it's a probability distribution. This requires new research methods, or at minimum, significant adaptations of existing ones.

The atomic insight: **you can't user-test a probability distribution with methods designed for fixed artifacts.** The research method must account for the same uncertainty that the product does.

## DUAL DEFINITION

**Business definition:** Uncertainty research is user research methodology adapted for AI products — accounting for the fact that the product behaves differently every time, that user trust develops over repeated interactions (not single sessions), and that "quality" is subjective for generative AI output.

**Technical definition:** Research design that controls for non-deterministic system output by stratifying participants across output quality bands, measuring behavioral trust signals alongside self-reported satisfaction, and using statistical methods robust to high within-subject variance.

## THE TRAP (Expanded)

**The Single-Session Illusion.** A usability session shows the AI performing well. The PM declares the feature validated. But the session captured one sample from the output distribution — possibly a good sample. A different session with a different random seed might have produced mediocre output, and the participant's reaction would have been completely different.

**The Satisfaction-Trust Gap.** Users report high satisfaction after the AI generates a good response. But satisfaction and trust are different constructs. Satisfaction is momentary ("this answer was good"). Trust is longitudinal ("I believe this will be good next time"). AI products need trust research, which requires repeated exposure over time — not just satisfaction surveys after a single session.

**The Wizard-of-Oz Ceiling.** Teams use Wizard-of-Oz testing (a human generating responses that users think come from AI) to validate demand. The problem: the human generates perfect responses. Users calibrate expectations to human-quality output. When the real AI launches at 85% quality, the gap between expectation and reality destroys trust — even though 85% accuracy is genuinely impressive.

## INTELLECTUAL LINEAGE

- **Teresa Torres** — Continuous discovery habits. Adapted for AI: discovery must account for non-deterministic output.
- **Don Norman** — Mental models. Users form mental models of AI that differ from how AI actually works, creating systematic expectation mismatches.
- **Trust literature (Lee & See, 2004)** — Trust in automation develops through calibration: users learn when to rely on the system and when to verify. This calibration requires repeated interaction, not single exposure.

## REAL-WORLD EXAMPLES

**Longitudinal trust calibration study (4-week window).** A team deployed an AI writing assistant to 20 users for 4 weeks, measuring both behavioral trust and self-reported confidence. Week 1: users verified every output before submitting (100% verification rate). Week 2: verification dropped to 60% — users started trusting routine paragraphs. Week 3: 25% verification overall, but users verified complex sections (data-heavy, nuanced arguments). Week 4: stable at 20% verification — trust calibrated to task complexity. Trust curve: near-linear decay over first 3 weeks, plateau at week 4. Single-session usability test would have captured only Week 1 (high verification) and concluded "users don't trust this," missing the fact that trust develops through repeated positive interaction. Product implication: this AI needed 2-3 weeks of onboarding before it provided value; launch strategy needed to account for the calibration period.

**Stratified quality evaluation (hidden ceiling effect).** A team evaluated AI search quality across 200 queries. No stratification: 72% average satisfaction. Stratified by query complexity: Tier 1 (simple factual, e.g., "What is glucose?"): 94% satisfaction. Tier 2 (multi-step reasoning, e.g., "Compare glucose and fructose in terms of blood sugar impact"): 67% satisfaction. Tier 3 (ambiguous/creative, e.g., "How should I reframe my company's sugar substitute positioning?"): 41% satisfaction. The 72% average hid a critical satisfaction cliff: power users (researchers, analysts) primarily used Tier 3 queries and experienced failure rates 2.3x higher than the average suggested. Product decision: focus Tier 3 improvements, not general quality (which was already acceptable). Without stratification, resources would have been wasted.

**Wizard-of-Oz ceiling effect (expectation mismatch).** A team used Wizard-of-Oz testing to validate demand for an AI email assistant. Humans generated email responses; users believed it was AI. Response quality: perfect (humans took 2 minutes per email). Users loved it. Launch plan: ship AI model (expected 80% quality). Reality: AI generated emails at 78% quality (slightly worse than projected). User satisfaction: 45% (vs 95% in Wizard-of-Oz). Root cause: users calibrated expectations to human-perfect responses in WoZ; 78% quality felt like failure even though it was impressive. Lesson: WoZ is useful for demand validation, but the quality ceiling it establishes creates a trap. When shipping real AI, account for expectation gap. Mitigation: either (a) under-promise and over-deliver in marketing, or (b) use staged rollout + quality calibration messaging ("this AI will get emails 70-80% correct; you'll need to review each one").

## FURTHER READING

- Teresa Torres, *Continuous Discovery Habits* — Adapted for AI uncertainty
- Lee & See, "Trust in Automation" (2004) — Foundational trust calibration research
- Google PAIR, "People + AI Guidebook" — Research methods for human-AI interaction
- Gero et al., "Designing for AI Uncertainty" (CHI) — UX research with non-deterministic systems
