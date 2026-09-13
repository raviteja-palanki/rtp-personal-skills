# Ship evidence and calculation notes

## Correct interpretation of the original numerical examples

If a task deliberately chooses the illustrative limits below, its observed results are:

| Category | Example limit | Observed | What can be said |
|---|---:|---:|---|
| Catastrophic | <0.1% | 0/150 = 0% | No observed cases; the sample does not establish this underlying rate |
| High | <1% | 2/150 = 1.33% | Observed rate exceeds the example limit |
| Medium | <5% | 8/150 = 5.33% | Observed rate exceeds the example limit; it is not a pass |
| Low | <10% | 12/150 = 8% | Observed rate is below the example limit; uncertainty still matters |

These are example thresholds, not recommended catastrophic-risk allowances. With zero observed failures in `n` independent Bernoulli trials of fixed probability and accurate detection, the exact one-sided 95% upper confidence bound is `1 − 0.05^(1/n)`. At `n=150`, it is about **1.977%**. At least **2,995 zero-failure trials** are needed to put this particular bound below 0.1%. Correlated cases, selection, changing conditions, or missed failures can invalidate the interpretation; numerical coverage is not a substitute for mechanism-based safety controls.

For a 30-day time-based availability window, total time is 43,200 minutes. Unavailability is `(1 − availability) × 43,200`: 432 minutes at 99%, 43.2 at 99.9%, and 4.32 at 99.99%. Six nines would be 99.9999%, not 99%. Contract calculations may use different windows or definitions.

At $0.08/user/day and a 30-day month, cost is $2.40/user/month. With $30 revenue, `(30 − 2.40)/30 = 92%` margin on the included cost scope. The earlier negative 26% result was incorrect. Add omitted cost categories before calling this full gross margin.

## Governance and incentive sources

The user's full primary PDF of **“6 questions to guide your AI strategy,” Betsy Vereckey, MIT Sloan Ideas Made to Matter, 3 August 2026**, was read in this pass. It reports George Westerman's account of HCA Healthcare reviewing before development, before a pilot, before scaling, and periodically thereafter. The article **also explicitly advises changing or discontinuing projects that do not deliver anticipated results**. Its favorable description of governance helping progress does not establish that HCA's committee lacks stop authority. No charter or measured governance outcomes were provided. The skill retains the review sequence and asks for evidence of actual authority without declaring the committee cosmetic.

The user's **“Bring Back Managing for Value,” HBR, August 2026**, contains the four finance capabilities and a specific shareholder-value framework separating hard and soft constraints. The relevant primary sections were read. It identifies the 760-organization survey as **Bain's survey** and gives the one-in-five figure; a separately inspectable survey instrument or dataset was not established. Its cost-of-equity band—slightly over 9%, with most large public firms within 1.5 percentage points—is Bain's dated analysis, not a universal discount-rate prescription. Other organizations may use different lawful objectives and preference structures.

The user's **“How Leaders Create the Conditions for Innovative Thinking,” HBR On Leadership, 24 June 2026**, was checked at the relevant transcript passages. Linda Hill describes several leaders rewarding the ending of ideas, including one offering a bonus for ending one's own. It is a qualitative report, not a measured effect or an HBR IdeaCast episode in this captured version.

The **Tim Ferriss career-crossroads** source, HBR Cold Call, October 2025, is autobiographical. The library's existing account motivates comparing action and inaction; it does not establish that delay is generally worse. No new full primary transcript review is claimed for that source here.

## Applicable obligations and engineering references

- [HHS Security Rule certification FAQ](https://www.hhs.gov/hipaa/for-professionals/faq/2003/are-we-required-to-certify-our-organizations-compliance-with-the-standards/index.html): private certification is not a recognized substitute for obligations under the rule. Apply the actual entity/activity scope.
- [AICPA's SOC 2 examination guide](https://www.aicpa-cima.com/cpe-learning/publication/soc-2-reporting-on-an-examination-of-controls-at-a-service-organization-relevant-to-security-availability-processing-integrity-confidentiality-or-privacy-OPL): SOC 2 reports on controls in the defined examination scope; it is not blanket approval for an AI feature.
- [FedRAMP statutory authority for agencies](https://www.fedramp.gov/2026/authority/law/agencies/): federal cloud authorization requirements are specific to the service and agency use. The current scope page returned no extractable body in this check; do not claim a detailed current eligibility determination from it.
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework): the framework supports voluntary risk management across design, development, use, and evaluation. It does not supply this skill's numerical launch thresholds or replace applicable obligations.
- [Google SRE, Canarying Releases](https://sre.google/workbook/canarying-releases/): staged exposure and monitoring need representative populations, appropriate timing, and interpretable comparisons. Current relevant sections were checked during the adjacent Prompt as Product revision.

The original concept guide's FDA Phase III analogy, unnamed Stripe practice, and unspecified Anthropic/Hoffman titles do not establish this seven-area gate. Drug trial phases are not a general AI-product approval sequence. Keep the practical method without presenting those analogies as validated lineage.
