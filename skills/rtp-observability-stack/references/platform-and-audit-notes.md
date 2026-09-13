# Platform and audit notes

Editorial check: 13 September 2026. These are documentation checks, not runtime benchmarks or a production-data audit.

## Current primary documentation

- [OpenInference repository](https://github.com/Arize-ai/openinference) describes AI instrumentation, semantic conventions, and conversion processors. [OpenTelemetry GenAI conventions](https://github.com/open-telemetry/semantic-conventions-genai) separately define GenAI spans, metrics, and events. Pin and test the conventions actually used; a shared transport does not guarantee identical semantics.
- [Phoenix repository](https://github.com/Arize-ai/phoenix) describes tracing, datasets, evaluation, and experiments and identifies Elastic License 2.0. This revision uses “self-hosted” without claiming an unrestricted or OSI-approved license. [Deployment configuration](https://arize.com/docs/phoenix/self-hosting/configuration) is a starting point for an installation review, not evidence of no data egress.
- [LangSmith OpenTelemetry documentation](https://docs.langchain.com/langsmith/trace-with-opentelemetry) supports tracing from different frameworks and describes mappings and endpoints. [Self-hosted documentation](https://docs.langchain.com/langsmith/self-hosted) identifies an Enterprise add-on. Verify the current language SDK and deployment documentation together; do not copy an old tracing configuration blindly.
- [EU AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng), Article 12, concerns logging capabilities for covered high-risk systems. Establish the applicable consolidated text, implementation date, system category, and organizational role before treating it as a requirement for a specific deployment.
- [NIST AI RMF Playbook, Manage](https://airc.nist.gov/airmf-resources/playbook/manage/) describes MANAGE 2.1 as considering risk-management resources and viable alternatives. The earlier claim that this provision itself obliges event logging was incorrect. Contractual or organizational adoption can create additional requirements; identify that basis separately.

## Historical Arize findings: retain as leads

The original skill's author stated that they inspected Arize skill sources on 29 July 2026 and reported: an export fallback that removed a row bound; trace fields capable of holding personal data; a bulk-annotation operation with a 1,000-item limit; and a compliance-report destination under `/tmp`. The original wording also reported a 6–12-hour indexing delay as vendor-disclosed.

This revision did not re-inspect those exact tool versions or recover a primary source supporting that numerical delay. Do not relabel the observations as current tested defaults. Capture tool version/commit and relevant implementation or documentation when verifying them. Test with synthetic or appropriately minimized data and bounded operations.

## Novel Insights connection

The ledger's model-routing/accountability entry suggests making model identity a first-class field when providers change during failover. Preserve that practical link: log the actual served provider/model/version when available, distinguish it from the requested alias, and connect it to the decision and route. This makes investigation more useful. It does not by itself authorize a provider change, prove sovereignty, or satisfy every audit obligation. The ledger's claim that this is always cheap and universally overlooked is a hypothesis, not an established industry fact.
