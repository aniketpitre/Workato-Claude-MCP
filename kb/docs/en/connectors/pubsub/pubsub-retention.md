---
url: 'https://docs.workato.com/en/connectors/pubsub/pubsub-retention.md'
description: >-
  Configure the retention period for a Workato Event streams topic to control
  how long subscribers can access published messages.
---

# Retention period configuration

Event topic stores messages for a specific duration defined by the topic retention period. Subscribers of the topic cannot access messages older than the retention period. So, any new recipe can access all messages, published during the retention period.

## Configure the retention period

You can change the retention period in the **Settings** tab. The retention period is subject to the following quota:

| Description | Quota |
| --- | --- |
| Maximum message retention period | 90 days |

> **RETENTION PERIOD AND RESTARTING RECIPES**
> 
> If you stop a recipe with an Event streams trigger for a time period longer than the retention period, it cannot pick up new messages after it restarts. If you experience this issue, clone the recipe and try again.

![Topic retention settings](/assets/retention-setting.BmyLfWVC.png)_Topic retention settings_

---
