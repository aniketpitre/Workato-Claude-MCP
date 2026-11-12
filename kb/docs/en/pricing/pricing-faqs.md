---
url: 'https://docs.workato.com/en/pricing/pricing-faqs.md'
description: >-
  Find answers to common questions about Workato pricing, including how usage is
  counted in recipe jobs and what contributes to it.
---

# Billing and usage FAQs

Get answers to frequently asked questions (FAQs) about Workato billing and usage.

## What is usage in Workato?

View answer

Workato uses a usage-based billing model where you pay only for what you use. A common billing unit, the [Workato credit](/en/pricing/overview#how-usage-is-measured), applies across all platform capabilities. You allocate credits based on what your business needs.

Workato tracks usage separately for each product capability using [standard usage metrics](/en/pricing/usage-metrics).

## How is usage counted in a Workato recipe job?

View answer

Workato calculates usage based on the recipe's usage metric, such as Tasks or API Calls. Successfully executed operations that meet the metric's eligibility rules contribute to usage. Failed operations and skipped branches don't count.

Some operations are measured by their own metric, such as IDP pages or Event streams events, and are counted in addition to the recipe's main metric. Recipe function steps count toward the calling recipe's metric.

Refer to [Understand usage](/en/pricing/usage-metrics#rules) for the full set of calculation rules.

## How is Agent Studio usage measured?

View answer

Agent Studio usage is measured in Genie actions. Each prompt sent to a Genie counts as one Genie action, regardless of the prompt's complexity or which LLM the Genie uses.

A Genie's internal operations, including skills, reasoning, knowledge retrieval, and handoffs to other Genies, are included in the Genie action and aren't counted separately. The following operations are counted independently: Recipe functions called from a skill contribute to Tasks.

Refer to [Genie usage](/en/pricing/usage-metrics/agent-studio) for more information.

## Do failed actions contribute to usage?

View answer

No. Failed actions are not counted as usage. Only successfully executed actions contribute to your usage.

Actions that complete successfully before a job fails or is canceled do count.

## Does rerunning jobs add to my usage?

View answer

Yes. Rerun jobs contribute to usage in the same way as the original job run.

## How do I find usage per job?

View answer

You can view usage at the job level in Job history. Each job displays its usage in the usage column. A contextual summary for the selected time period is also shown at the top of the page.

If a recipe calls other recipes, the parent job does not display total usage across all child jobs. Each child job reports its own usage separately.

Refer to [Recipe jobs](/en/recipes/jobs) for more information.

---
