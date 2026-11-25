---
url: 'https://docs.workato.com/en/airo/acumen.md'
description: >-
  Use Acumen to monitor your workspace, investigate incidents and failures, and
  forecast usage.
---

# Acumen

Acumen helps you operate your Workato workspace in production. It continuously monitors your automations, surfaces active incidents, traces failures to their cause, and answers questions about automation health and usage.

Acumen combines three types of context to identify what's happening and what's at risk:

- **Runtime activity**: job volumes, latencies, error patterns, connection health, and the typical baseline for each automation.
- **Automation relationships**: dependencies between recipes, connections, APIs, MCP servers, genies, skills, and other automation assets.
- **Business context**: the processes your automations support, the people who own them, and the KPIs they contribute to.

This context lets Acumen show which business outcome is at risk when something fails, which downstream automations are affected, and who owns the relevant automation.

## Detect and surface incidents

Acumen continuously monitors for conditions that could interrupt or degrade automations, including:

- **Silent failures**: An automation stops processing jobs without reporting an error, for example when a trigger stalls, a webhook rejects a changed schema, or an upstream system stops sending events.
- **Failure patterns**: Bursts of job errors, repeated connection failures, retry storms, or schema mismatches affecting one or more recipes.
- **Unusual volume**: A sudden increase or decrease in job throughput compared with an automation's typical baseline.

When Acumen detects an issue, it raises an **active incident** on your [homepage](/en/airo/homepage) and through the AIRO chat interface, so the right operator can investigate before a business user reports a problem.

**Active incidents**

![Active incidents on homepage](/assets/smart-recommendations.CHrYSiRb.png)_Active incidents on homepage_

**Chat with Acumen through AIRO**

![Investigating an incident through chat](/assets/acumen-chat-incident.BnZmFuEg.png)_Investigating an incident through chat_

## Investigate failures and assess impact

Acumen traces a failing recipe's upstream triggers, parent recipes, shared connections, and data dependencies to help identify the root cause.

You can also use Acumen to assess the likely impact of a change before making it. Ask which recipes use a specific connection or which automations could be affected by an API version change. Acumen identifies the relevant recipes and connections instead of returning only a generic connector match.

![Acumen troubleshooting](/assets/acumen-troubleshooting.Ddm2Psi4.png)_Acumen troubleshooting_

## Analyze automation health

Use Acumen to investigate recent errors, performance degradation, and deployment status, or to compare an automation's performance over time. It weighs current activity against each automation's typical baseline to put results in context.

For example, you can compare the success rate of an HR-Onboarding project with its performance over the previous 60 days, review recent errors, or check the status of a recent deployment.

![Ask Acumen about recent errors](/assets/ask-acumen-about-errors.DPD5MOUl.png)_Ask Acumen about recent errors_

## Monitor and forecast usage

Use Acumen to generate an ad hoc usage report for a custom time period, filtered by project or asset tags. You can also ask Acumen to forecast expected usage through the end of your current billing period based on recent consumption patterns.

![Use Acumen to monitor and forecast usage](/assets/acumen-usage.lX4wk2X9.png)_Use Acumen to monitor and forecast usage_

---
