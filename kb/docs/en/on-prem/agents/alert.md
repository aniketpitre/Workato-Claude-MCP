---
url: 'https://docs.workato.com/en/on-prem/agents/alert.md'
description: >-
  Configure automatic email alerts for an on-prem group to get notified when an
  agent disconnects or a certificate nears expiration.
---

# Automatic alerts

You can enable automatic alerts to stay informed about the status of your on-prem agent (OPA). This feature sends email notifications when a certificate nears expiration or the OPA disconnects from Workato. This ensures that you receive prompt alerts on issues with your OPA, and prevents disruptions by allowing you to [update certificates](/en/on-prem/agents/key) before they expire.

## OPA disconnection types

There are two types of agent disconnections:

| Type | Description |
| --- | --- |
| Unexpected disconnection | This type of disconnection occurs without prior notice and is usually caused by unforeseen issues such as network outages on the user side, connectivity issues, or hardware failures. Unexpected disconnections can cause immediate disruptions to recipes relying on the OPA. |
| Expected disconnection | This type of disconnection occurs when you manually shut down the OPA. |

## Configure automatic alerts

Complete the following steps to configure automatic alerts for an on-prem group:

1. Go to **Tools > On-prem groups** and select the on-prem group that you plan to enable notifications for.
   
2. Go to **Settings > Email alerts**.
   
   ![The Email alerts tab](/assets/automatic-email-alerts-opa.C1tgFwRf.png)_The **Email alerts** tab_
   
3. Optional. Go to the **Recipients** section to view the email addresses of the [technical contacts](/en/user-accounts-and-teams/admin-email#technical-contacts) who are configured to receive alerts for this workspace.
   
   Configure technical contacts
   
   Workspace administrators can complete the following steps to configure a workspace's technical contacts:
   
   1. Go to **Workspace admin > Settings > Notifications > Admin notifications**.
      
   2. List the emails to notify about [OPA](/en/on-prem/agents#on-prem-agent) and [API platform](/en/api-management#api-platform) incidents in the **Technical contacts** field.
      
   3. Click **Save**.
      
   
4. Use the **Unexpected agent disconnection** and **Manual agent shutdown** options to toggle alerts for different [disconnection types](#disconnection-types). The **Unexpected agent disconnection** option is enabled by default.
   
5. Use the **Expiring agent certificate** option to toggle alerts sent 90 days and 30 days before a certificate expires. This option is enabled by default.
   
   > **KEEP EXPIRATION NOTIFICATIONS ENABLED**
   > 
   > We strongly recommend you keep notifications enabled for expiring certificates. An agent stops processing jobs when its certificate expires. This can cause recipe interruptions if it's the only active agent in the on-prem group.
   > 
   > Refer to the [Agent key management](/en/on-prem/agents/key) guide to replace keys with zero downtime or the [Active on-prem group](/en/on-prem/groups/group-status#active-on-prem-group) guide to enhance fault tolerance.
   
6. Click **Save**.
   

## Email notifications

Workato emails your workspace's [technical contacts](/en/user-accounts-and-teams/admin-email#technical-contacts) based on the conditions toggled in an on-prem group's [Email alerts](#configure-automatic-alerts) tab.

![Email notification - unexpected disconnection](/assets/unexpected-disconnection-email-opa.CnHVaoN7.png)_The email notification for an unexpected disconnection._

You can click **View on-prem agent** in the email alert to view the relevant in-app agent.

![Disconnected agent on OPA page](/assets/disconnected-agent-opa.C9wXPoT8.png)_Disconnected agent on OPA page_

---
