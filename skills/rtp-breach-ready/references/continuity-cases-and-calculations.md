# Continuity: case correction and source notes

Editorial review: 13 September 2026. This revision checks documentation and reasoning, not a live recovery environment.

## FedEx/TNT, 2017

[FedEx's 17 July 2017 disclosure](https://investors.fedex.com/news-and-events/investor-news/investor-news-details/2017/FedEx-Files-10-K-with-Additional-Disclosure-on-Cyber-Attack-Affecting-TNT-Express-Systems/default.aspx) reports continuing widespread TNT service/invoicing delays, substantial manual operations, and uncertainty about full restoration. Other FedEx companies were reported unaffected. This directly contradicts a complete 48-hour recovery. The source does not establish the original isolated-mainframe, radio/paper-only architecture or claimed 72-hour rehearsal. The useful supported lesson concerns continuity arrangements and uneven effects across connected businesses, without attributing all outcomes to one control.

[FedEx's 19 September 2017 earnings release](https://investors.fedex.com/news-and-events/investor-news/investor-news-details/2017/FedEx-Corp-Reports-First-Quarter-Earnings-20170919000000/default.aspx) estimates a $300 million operating-results impact from the cyberattack for that quarter. That is a company estimate with a defined period, not an audited counterfactual or the final lifetime cost. The original comparison claiming unprepared competitors lost billions is not supported by an identified comparison group and is not retained as fact.

## Primary guidance checked

[CISA's StopRansomware Guide](https://www.cisa.gov/stopransomware/ransomware-guide) recommends protected backups and restore tests, critical-asset/dependency inventories, segmentation, prepared communication, and recovery into a clean environment. It explains that accessible backups can be attacked and that shared connections can defeat segmentation. The main skill adapts these principles to a planning workflow; exact implementation requires the system's authorized responders and constraints.

[NIST SP 800-61 Revision 3](https://www.nist.gov/publications/incident-response-recommendations-and-considerations-cybersecurity-risk-management-csf), finalized 3 April 2025, integrates preparation, detection, response, and recovery with cybersecurity risk management. It supersedes Revision 2. This supports treating prevention and recovery as complementary rather than claiming prevention never works.

## Planning examples, not benchmarks

- Forty-eight hours is a scenario duration; the original also mentioned a 72-hour rehearsal. Neither establishes a universal required manual capacity.
- Two/eight/twenty-four-hour recovery tiers illustrate prioritization. Derive actual targets from harm and dependencies, with safety-critical functions considered alongside revenue.
- Monthly/quarterly/annual checks and a six-month restore lookback are historical examples. Specify an internally consistent test plan and evidence of what each exercise establishes.
- At 90% AI ticket handling, the remaining 10% human workload becomes roughly ten times larger if all volume is transferred unchanged. Case mix, staffing, service times, and triage change the actual capacity requirement.
- $10 million gross avoided loss divided by $1 million one-time cost is 10:1; net ROI is ($10m − $1m)/$1m = 900%, assuming the benefit actually occurs and omitting other costs. Ten annual $1 million payments total $10 million before discounting; there is no automatic ten-year 10× ROI.

## Novel Insights connection

The ledger's platform/stop-authority and routing entries suggest testing whether technical controls, accountable decision rights, and operational access remain usable together. For recovery, apply that to restoring, isolating, communicating, and resuming service. An independent organization chart alone is not a working control, and a different model provider or domain alone is not an independent fallback. Verify the dependency and authority needed by the actual scenario.
