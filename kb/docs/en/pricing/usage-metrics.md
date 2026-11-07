---
url: 'https://docs.workato.com/en/pricing/usage-metrics.md'
description: >-
  Learn how Workato's usage-based model works, including the usage metrics,
  counting rules, and billing units for each product capability.
---

# Understand usage

Workato measures how much you use each capability, and converts that usage into [Workato credits](/en/pricing/overview#how-usage-is-measured). This page covers the rules that apply to every capability and the pages that follow explain each individual metric in detail.

> Some plans measure usage differently. Refer to your contract or contact your Customer Success Representative for more information.

## How usage is calculated

Workato calculates usage using two principles: Only successful operations count, and usage accumulates across capabilities.

### Only successful operations count

Workato bills for operations it completes successfully on your behalf. As a general rule:

- **Skipped operations don't count**: Steps that don't run (for example, because a conditional or control step routed around them) aren't counted.
- **Failed operations and canceled jobs are excluded**: Operations that fail don't count. Operations that complete successfully before a job fails or is canceled do count.
- **Rerun-eligible operations count**: An operation that runs again as part of a rerun contributes to usage.
- **Expected errors still count**: An operation that returns an expected error response (such as a `4xx` or `5xx`) and otherwise completes as intended counts as successful.

Individual capabilities add their own specifics on top of these rules. Refer to each asset's page for more information.

### Usage accumulates across capabilities

The following rules determine how usage is calculated when your workload uses multiple capabilities:

- **Some usage is additive**: Certain capabilities are measured _in addition to_ the primary usage of the asset they run in. For example, when a recipe processes a document with IDP (Intelligent Document Processing), the pages it processes are counted on top of the recipe's own usage. They add to it, rather than replacing it.
- **Usage is counted only once**: An operation that's already counted in one metric isn't counted again in another. For example, an IDP step is counted as Pages, so it is _not_ also counted as a workflow step.

A combined workload's total usage is the sum of each capability's usage. Additive capabilities stack on top of that total, and no operation is counted twice. Refer to [Estimate usage](/en/pricing/estimate) for complete worked examples.

## Usage metrics

The following table lists each Workato asset, the metric used to measure its usage, and how that usage is calculated.

| Asset | Metric | Description |
| --- | --- | --- |
| [Workflow recipes](/en/recipes/tasks) | Tasks | Measured per action step executed in a workflow recipe job. The total Tasks for a job is the sum of all eligible action steps. |
| [Managed API](/en/pricing/usage-metrics/api-platform) | API Calls | Measured per successful API request to a Managed API. Longer response times can count as more than one API Call. Internal recipe steps do not add to API Calls. |
| [API Proxy](/en/pricing/usage-metrics/api-proxy) | API Proxy Calls | Measured per successful API request to an API Proxy (with or without transformation). Each request counts as one API Proxy Call, regardless of response time. |
| [Data pipelines](/en/pricing/usage-metrics/data-pipelines) | Rows | Measured per row extracted from the source across successful objects in each data pipeline sync. |
| [Genies](/en/pricing/usage-metrics/agent-studio) | Genie actions | Measured per prompt sent to a Genie. Prompts can be sent by users or systems, such as another Genie or an app event. |
| [Skills](/en/billing-and-usage/usage-metrics/skills) | Tasks | Non-billable when invoked by a Genie (included in the Genie action). Billed as Tasks when invoked over MCP. |
| [MCP](/en/billing-and-usage/usage-metrics/mcp) | Varies | MCP usage is measured as the usage of the asset it invokes. |
| [MCP proxy](/en/billing-and-usage/usage-metrics/mcp-proxy) | MCP Proxy Calls | Measured per successful request a Workato proxy MCP server routes to an external third-party MCP server. |
| [IDP](/en/pricing/usage-metrics/idp) | Pages | Measured per page processed, whether the page is standalone or part of a larger document. IDP usage is added on top of the usage of the asset it runs in. |
| [Event streams](/en/pricing/usage-metrics/event-streams) | Events | Measured per message published, whether individually or as part of a batch. Consumed messages don't count. Event streams usage is added on top of the usage of the asset it runs in. |
| [Workato GO](/en/pricing/usage-metrics/workato-go) | Seats | Measured by the number of seats assigned to end-users of Workato GO. Any assets invoked by Workato GO are measured separately, following their own usage metric. |
| [Workflow apps](/en/pricing/usage-metrics/workflow-apps) | Seats | Measured by the number of seats assigned to end-users of Workflow apps. Any assets invoked by a Workflow app are measured separately, following their own usage metric. |

---
