# Safety by Design: make the whole system support the boundary

Safety by design means translating the intended use and foreseeable harms into architecture, operating practice, and evidence. Instructions help a model handle situations flexibly. Permissions constrain actions. Retrieval supplies appropriate information. Validators check releases. Monitoring and people maintain and improve the system. Each has a role; none deserves trust solely because of its label.

## Intellectual lineage

The framework combines established software design and security principles, adversarial machine learning, and work such as Anthropic’s Constitutional AI. These are related ideas, not interchangeable methods. The old “testing catches 80% while architecture prevents 99%” attribution was unsupported. Security can be improved after deployment, although designing important boundaries early can avoid rework and exposure.

Constitutional AI uses principles in training with AI feedback. A prompt can express similar principles without becoming that training method. Neither approach makes jailbreaks impossible or guarantees improvement as capability increases. Output validators can use learned models and contextual evidence; they are not inherently limited to keywords or known exact attacks.

The business question is whether people can use the product within acceptable boundaries. The engineering question is how each boundary is implemented, tested, maintained, and recovered when it fails. Claims about the model “understanding why” do not replace observed behavior and system-level evidence.

## Why a single-filter design can fail—and why filters still matter

A keyword rule can block a legitimate historical discussion while missing a harmful paraphrase. A clear instruction can improve contextual handling but can also fail under a new framing. A learned classifier may catch that failure. The appropriate design evaluates the combined system on allowed and prohibited cases.

A stated educational, fictional, professional, or commercial purpose is relevant context, not automatic authorization for dangerous operational assistance. Define the content boundary and evaluate what the response enables. Do not rely on a benign label to make the same hazardous instructions acceptable.

Independent iteration of filters can be useful. Compare architectures in safe evaluation settings; do not remove critical protection from real users simply to run an on/off experiment. Measure unnecessary blocking alongside harmful misses and end-to-end outcomes.

## Three illustrative designs

### Medical support

Define the clinical or informational role with appropriate expertise. Specify what the system may explain, when it must seek more information, and which decisions need qualified review. Use authorized, current reference material, calibrated uncertainty where supported, and a safe route for urgent or out-of-scope needs.

The previous prompt’s “85% confident,” “always show three alternatives,” and “consult a doctor” were not sufficient controls. Invented precision can mislead, extra diagnoses can confuse, and a referral can be unhelpful without context. Evaluate the actual clinical workflow, not just whether the model refused. Do not remove a needed drug reference database and assume that less information means safer support.

### Code assistance

Instruct the system to avoid exposing secrets, explain material security trade-offs, and use approved credential mechanisms. Enforce execution permissions, package policies, network boundaries, and access to repositories independently. Supply relevant security guidance and current vulnerability information through authorized sources. Use secret detection, code analysis, and appropriate review as additional checks.

Removing an `install_arbitrary_package` tool does not prevent installation if a shell or other network route still allows it. A vulnerability-checking tool is only as current and complete as its source. A secret scanner can miss a key, and an environment variable can still be exposed by an unsafe command. Test those paths before claiming that a backdoor or leak is impossible.

### Community content

Define respectful participation and prohibited assistance, including how to distinguish discussion, quotation, targeted abuse, and encouragement of harm. Use contextual moderation, appropriate reference material, and appeal paths for mistakes. Restrict publishing or amplification actions where the product’s role does not authorize them.

A polite response is useful but not proof that the content is harmless. A classifier’s block can be correct even when the model’s instructions failed. Evaluate users’ legitimate expression as well as evasion, and inspect effects across relevant languages and communities.

## A reusable instruction structure

Specify purpose, relevant principles, decision rules, uncertainty handling, helpful alternatives, and authority. For a legal-information product, for example, distinguish sourced general information from an individualized conclusion outside its remit. Ask for jurisdiction when it materially changes the answer; verify current law; state unresolved questions and appropriate professional next steps. Avoid promising that a disclaimer alone changes the legal character or consequences of the service.

Use concise explanations of uncertainty and trade-offs that help the recipient act. Do not request invented confidence scores or treat an explanation as direct access to the model’s internal reasoning.

## Scale, monitoring, and the limits of the pattern

Capability changes can improve or weaken different protections. More requests can expose rare failures, while new tools can create entirely new paths to harm. Version and test the whole configuration rather than relying on model-generation labels or assuming that principles automatically scale.

Monitor refusals, harmful misses, legitimate work blocked, incidents, and useful corrections with explicit denominators. The fraction routed to a validator is not a jailbreak rate: many benign requests may be checked, and routing can be preventive. A low observed failure count may reflect strong protection, low exposure, weak detection, or an easy test.

When a model struggles, choose controls that meet the requirement: clearer guidance, constrained workflows, reliable tools, validators, restricted scope, qualified review, another model, or a non-AI alternative. Do not automatically replace effective filters with prompts as models improve. For fresh facts, use current evidence with provenance and freshness checks. For audits, preserve appropriate evidence of actual behavior, versions, and control operation; a published prompt alone proves little.

Use the seven-step process in [SKILL.md](SKILL.md) to turn these ideas into an implementable design and an explicit decision. The aim is appropriate protection that supports useful work, with known limits and a practical response when those limits are reached.
