# Feedback Flywheel — Concept Guide

A feedback flywheel connects experience to an assessed improvement. Real usage reveals situations that internal or synthetic tests may miss. The interface influences which signals become visible, but it is only one part of the evaluation system. Independent tests, research, operational outcomes, and qualified review remain necessary.

## Two definitions

**Business:** a repeatable way to learn from use and improve customer outcomes. Better results may attract or retain users and produce further learning, but compounding growth and a competitive moat are possibilities to demonstrate.

**Technical:** an instrumented and governed path from permitted observations through interpretation, evaluation, experiments, release, and outcome measurement. It can improve prompts, retrieval, tools, rules, interaction design, or models. It does not require model retraining or automatic production updates.

## Three common traps

**Evaluation in a vacuum.** An offline test can omit important production situations. A hypothetical gap between 92% offline accuracy and 75% in use prompts an investigation of population, rubric, task, and system differences. The two numbers are not a documented benchmark or proof of a single cause.

**The feedback graveyard.** Ratings accumulate without an owner or a decision path. Collection is useful only insofar as it serves an allowed purpose. Assign ownership to important findings and follow them through to an outcome; do not maximize raw labeling for its own sake.

**The unexamined correction.** Before-and-after edits can reveal terminology, missing facts, style, or user preferences. They do not always show a uniquely correct answer. Human escalations likewise need validation before becoming reference labels.

## Two illustrative cases

**Document editing.** Suppose a drafting tool collects 50,000 permitted edit pairs over three months. Review finds excessive jargon, dense paragraphs, and missing company terminology. The team tests prompt and retrieval changes and observes acceptance rise from 40% to 68% over six months. That is a 28-percentage-point association; attribution requires a suitable comparison and checks for changing users or tasks. The next question is whether reduced editing reflects better work or less scrutiny. This is an illustration, not a verified Amazon case.

**Support escalation.** Suppose three categories dominate a sample of 10,000 escalations. The team investigates missing knowledge, failed tools, policies, and cases that properly require a person before choosing a retrieval change. An overall escalation rate falling from 10% to 5.5% is a 45% relative decline. A category rate falling from 35% to 8% has a different denominator. Neither establishes improvement without checking successful resolution and missed necessary escalations. These are illustrative figures, not a measured customer case.

## Intellectual connections

Eugene Yan’s evaluation work and Aman Khan’s observability practice motivate links between production signals and evaluation. Human-feedback training shows one way feedback can influence a model; it does not make every product feedback loop RLHF. The general business flywheel metaphor describes a reinforcing cycle, not a guarantee that more usage yields better data or profitable growth. Interpretability research addresses different questions and should not be presented as direct evidence of loop effectiveness.

Use the [skill](SKILL.md) for the workflow and the [research reference](references/evidence-and-examples.md) for evidence limits. The practical question is: which observed experience changed a decision, what was tested, and what happened afterward?
