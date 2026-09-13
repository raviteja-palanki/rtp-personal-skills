# Token Economics — Concept Guide

Pricing connects customer value and willingness to pay to the costs and risks of delivering the service. AI often adds material usage-dependent costs, but conventional software also has variable support, hosting, storage, payment, and delivery costs. Neither category has one universal marginal-cost curve.

In business terms, choose an offer customers value and can buy that supports the intended business model. In technical terms, define how activity and outcomes map to metered units, billing, delivery cost, limits, and evidence. Fairness and predictability matter alongside economics because they influence customer choice and trust.

## Why each model can work or fail

Flat-rate and seat pricing make the bill predictable but leave the seller exposed to included usage. A few expensive users can matter; they do not automatically make the portfolio unprofitable or indicate abuse. Stated limits, pooling, and a suitable price can make the model work.

Usage pricing connects the bill to a meter. Customers may hesitate when they cannot estimate the bill, but transparency does not inevitably reduce adoption or force a price war. Workload estimates, caps, and meaningful units can help.

Outcome pricing can align incentives when the result is observable and valuable. It is not inherently suitable for medicine or law or unsuitable for routine high-volume tasks. An invoiceable output may be easier to count than its correctness. Risk, attribution, verification, and the actual agreement matter.

Hybrid pricing combines predictable access with variable entitlements. It can improve fit or create confusion; test whether buyers can explain a normal bill and an unusually heavy one.

## Corrected break-even examples

All numbers below are illustrative, not current provider prices or verified company results. These simplified calculations exclude costs unless expressly listed.

### Subscription with fixed and variable costs

Fixed monthly cost is $100,000, price is $50 per user, and variable cost is $5 per user. Contribution is $45 per user. Break-even is:

```text
100,000 / (50 - 5) = 2,222.22 users
At least 2,223 whole paying users are needed under these assumptions.
```

The earlier 2,500 result was an arithmetic error. Contribution margin remains 90% if price and variable cost remain constant. Operating margin rises as fixed cost is spread over more customers; it does not stay constant. At 25,000 users, revenue is $1.25 million, variable cost $125,000, and operating result $1.025 million, or 82% of revenue.

### Usage grows under a fixed revenue commitment

Assume one blended token rate of $0.000001 and 2,000 tokens per request. Cost is $0.002 per request. One million monthly requests cost $2,000; with $50,000 fixed cost, total modeled cost is $52,000. Ten million requests cost $20,000; total modeled cost is $70,000.

Revenue must be compared with both variable and fixed costs. Exceeding $2,000 alone does not establish profitability. If revenue remains fixed, the result depends on its amount: it is not automatically negative at tenfold usage. If customer count also grows, model the corresponding revenue. In real systems, distinguish input/output, cached/uncached, model, and context rates instead of assuming one blended token price.

### Customer-support routing

Assume 100 agents each handle 200 tickets per day, at 500 tokens per ticket. That is 10 million tokens daily. At $2 per million tokens, model cost is $20 daily, or $600 for a 30-day month. At $150 per agent monthly, revenue is $15,000 and contribution before all other variable costs is $14,400. Fixed and other delivery costs still determine profitability.

The old example mixed agent counts, ticket counts, and tokens and incorrectly reached $12,000 monthly. A 100–400 ticket range is 4× from minimum to maximum, not 3.5×; it does not prove most agents are within 2× of one another. The earlier 50–300 range is 6×. Use an actual distribution rather than declaring either range tight.

### A high-value decision service

Suppose an output is estimated to create $500 of customer value, the seller charges $50, and model cost is $2. Revenue less model cost is $48, or 96% of revenue, before verification, professional work, support, insurance, and other costs. The $498 difference between claimed customer value and model cost is not seller margin. A $50–$200 price range is a hypothetical offer to test, not a recommended diagnosis price.

The former diagnosis example does not establish clinical usefulness, authorized use, willingness to pay, or the measurability of a correct result. Independent calls can still have different costs and outcomes; usage distributions remain relevant.

### Research analysis with an 80× token spread

A light user makes 50 monthly requests at 500 tokens each: 25,000 tokens. A heavy user makes 1,000 requests at 2,000 tokens each: 2 million tokens. The token ratio is 80×. At $0.005 per 1,000 tokens, model costs are $0.125 and $10.

At a $100 monthly price, both customers have positive revenue less model cost: $99.875 and $90. This directly contradicts the earlier claim that the usage spread necessarily rules out flat pricing. Other costs and heavier tails might change the conclusion. Compare measured total costs and value rather than treating a ratio as a verdict.

The separate example of 500 tokens daily versus 50,000 quarterly used mismatched periods. Over a 90-day quarter the first is 45,000 tokens, so the totals differ by only about 1.11×, not 100×. Specify active days when relevant.

## Reading and evidence

The earlier lineage named Marc Andreessen's software essay, Dan Ariely's pricing-psychology work, and OpenAI and Anthropic commercial models. Use these as perspectives or examples. They do not establish why every provider chose a pricing model or a universal customer response to transparency. Read current official rates for the actual service, and use a spreadsheet or equivalent model to test the chosen workload scenarios.

Return to [SKILL.md](SKILL.md) for the decision process and [case notes](references/cases-and-evidence.md) for current versus historical examples.
