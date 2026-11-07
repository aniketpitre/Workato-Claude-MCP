---
url: 'https://docs.workato.com/en/recipes/limits.md'
description: >-
  Reference for Workato recipe design-time, run-time, and code size quotas,
  including how code size quotas vary across data centers.
---

# Recipe quotas

Recipes are subject to the following design and run time quotas.

> **DEFAULT QUOTAS**
> 
> The quotas on this page are defaults based on Workato best practices and are configured to enable optimal platform performance. Customers on Enterprise plans or above can contact their Customer Success Representative to request an extension of these quotas for their specific use cases.

## General recipe design time quotas

| Description | Quota |
| --- | --- |
| Maximum recipe name length | 255 characters |
| Maximum number of webhook recipes subscribed to same URL | 100 |

## Recipe code size quotas

Recipe code size quotas vary by data center.

View US Data Center recipe code size quotas

| Description | Quota |
| --- | --- |
| Maximum code size | 90MB |
| Maximum number of steps in recipe code | 1,000 |

View EU Data Center recipe code size quotas

| Description | Quota |
| --- | --- |
| Maximum code size (lines) | 1,000 |

View SG Data Center recipe code size quotas

| Description | Quota |
| --- | --- |
| Maximum code size (lines) | 1,000 |

View JP Data Center recipe code size quotas

| Description | Quota |
| --- | --- |
| Maximum code size (lines) | 1,000 |

View AU Data Center recipe code size quotas

| Description | Quota |
| --- | --- |
| Maximum code size (lines) | 1,000 |

View IL Data Center recipe code size quotas

| Description | Quota |
| --- | --- |
| Maximum code size (lines) | 1,000 |

View KR Data Center recipe code size quotas

| Description | Quota |
| --- | --- |
| Maximum code size (lines) | 1,000 |

View UK Data Center recipe code size quotas

| Description | Quota |
| --- | --- |
| Maximum code size (lines) | 1,000 |

View Self-service (Workato Free, Workato Pro, or Developer Sandbox) recipe code size quotas

| Description | Quota |
| --- | --- |
| Maximum code size (lines) | 1,000 |

## Job report quotas

| Description | Quota |
| --- | --- |
| Maximum number of columns in a job report | 10 |
| Maximum job report column value length | 256 characters |
| Maximum job report size | 5 KB |

## Test automation design time quotas

| Description | Quota |
| --- | --- |
| Maximum test case name length | 255 characters |
| Maximum test case description length | 1,000 characters |
| Maximum test case body length | 1,000,000 characters |
| Maximum batch size of test cases request when requested by IDs | 500 |
| Maximum number of test cases per recipe | 100 |

## General recipe run time quotas

| Description | Quota | Notes |
| --- | --- | --- |
| Job details: Maximum data storage of inputs/outputs across all steps | 1 MB | Job details are truncated if the total data exceeds 1 MB. |
| Webhook rate limits | Steady rate: 20 events per second, equivalent to 72,000 events per hour; Burst allowance: 9,000 events that can be processed beyond the steady rate in a burst | NA |
| Webhook byte quotas | 30 MB per minute, Burst allowance: 30 MB | These byte quotas represent the total memory in all your webhooks. |
| Maximum number of recipes subscribed to the same webhook URL | 100 | NA |
| Maximum recipe concurrency | Variable depending on your contract and plan. | This quota can be increased by contacting Customer Success. |
| Maximum number of recipe steps | 1,000 | NA |

## Queue size quotas

| Description | Quota | Notes |
| --- | --- | --- |
| Size of recipe function queue | 10,000 | NA |
| Size of user actions queue | 1,000 | NA |
| Size of long action queue | 10,000 | Applies to recipe jobs with long running actions. These jobs enter a sleep state and move to the long action queue where they await processing. |
| Size of poller events queue | 10,000 | NA |
| Size of webhooks events queue | 20,000 | NA |

## Timeout limits

| Description | Quota | Notes |
| --- | --- | --- |
| Standard job timeout | 90 minutes | [Workspace admins](/en/workspace-admin-settings.html#workspace-info) can configure a custom job execution time quota. If you observe a timeout that differs from 90 minutes, your workspace admin may have set a different quota. |
| HTTP action request timeout | If wait for response is `true`, the timeout is 1 hour; If wait for response is `false`, the timeout is 120 seconds | NA |
| Polling trigger timeout | 5 minutes | NA |
| Long pause/action timeout | 732 days | Recipes may fail if they exceed the total configured cumulative pause duration across all long actions. |

Specific connectors have variable timeout limits. Refer to the [Connectors quotas](/en/limits#connector-limits) section for more information.

## Payload quotas

| Description | Quota |
| --- | --- |
| Maximum trigger event payload size in bytes | 50 MB |
| Maximum payload size for callable recipes that are API platform endpoints | 1 MB (compressed) |

> **FURTHER READING**
> 
> Refer to the [Platform quotas](/en/limits) documentation for more information about Workato quotas.

---
