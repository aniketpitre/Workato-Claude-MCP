---
url: 'https://docs.workato.com/en/troubleshooting/webhook-gateway-migration.md'
description: >-
  Learn about the Workato webhook gateway migration to new subdomain URLs by
  data center, the impact, and affected connectors and triggers.
---

# Webhook Gateway Migration

Our webhook triggers are critical for many of our customer's automations that are time-sensitive, such as order confirmation integrations. Stability, security and availability are core principles of our webhook gateway and we are making some exciting updates to improve the Quality of Service (QoS), security and manageability of the webhook gateway.

## What is changing?

On May 31, 2023, Workato began showing new static webhook URLs in US DCs which point toward a new subdomain. Previously, webhook urls started with `https://www.workato.com`. The following list contains each new webhook URL. The webhook URL you use depends on the [data center](/en/datacenter/datacenter-overview#data-center-locations) you use.

- US Data Center: `https://webhooks.workato.com/`
- EU Data Center: `https://webhooks.eu.workato.com/`
- JP Data Center: `https://webhooks.jp.workato.com/`
- SG Data Center: `https://webhooks.sg.workato.com/`
- AU Data Center: `https://webhooks.au.workato.com/`

## What is the impact of the change?

This change doesn’t impact any recipes using the old domain for webhook URLs. All existing recipes will support both old and new domains for the webhook URLs at the same time. Any event sent to either URL will be sent to the relevant recipes. **We will support webhook urls using the old subdomain until the end of May 2024.**

> **WARNING**
> 
> If you are trying to create new recipes using the new webhook URLs and you have domain allowlists set up, you need to allowlist the new webhooks domain for the data center you use.

## Why are we doing this?

Separating our webhook URLs through a separate subdomain allows us to optimize the events and remove extra load balancers to differentiate between browser traffic and webhook traffic. This also allows traffic to go through a separate load balancer layer, enabling us to provide better Quality of Service and decoupling our webhooks from the main website. Furthermore, separate domains from `https://www.workato.com` allows us to provide better security and manageability to our webhooks gateway, ensuring our services are highly available and secure for your automations.

This webhook URL subdomain change also sets the webhook gateway up for further service improvements and features.

## Affected connectors and triggers

This change will be effective for the following connectors’ triggers and actions:

- Workato Webhooks: New Event
- Azure Blob Storage: New Blob
- BambooHR: New Employee (Real-time), New/updated Employee (Real-time)
- Gong: New Call
- Greenhouse: New Event
- Jira: New Event
- Microsoft Dynamics 365: New Object, New/updated Object
- Salesforce: New Outbound message, New Record, New/updated Record
- Slack: New Event
- All Custom connectors that utilize [Static webhook triggers](/en/developing-connectors/sdk/guides/building-triggers/static-webhook)

## Deprecation date

Workato will deprecate support for the old domain URL on May 31st, 2024.

## How to migrate your webhook triggers

1. Find the recipes that require migration in your given Workato workspace by reaching out to your Workato AE or CSM to find out more. You can also submit a request ticket to our Support Portal to find recipes that require migration.
   
2. After finding the recipes that need migration, if the recipe is a standard connector, find the new webhook URL found in the help description of the recipe. ![Help section for webhooks](/assets/webhook-migration-help.Dj5gBhOh.png) _The help description of the recipe_
   
   If the recipe is a custom connector, find your static webhook URL in the SDK connector page, under the **Test code** tab. ![SDK Test code tab for webhooks](/assets/static_webhook_url.B8S2rZCc.png) _Webhook URL on SDK connector page_
   
   After finding your webhook URL, find the event subscription for the app that relates to your recipe. See [How to find your event subscription in various apps](#how-to-find-your-event-subscription-in-various-apps) for guides to find event subscriptions in specific apps.
   
3. Edit the current webhook URL to your new webhook URL.
   
4. Save your subscription. You've migrated your webhook trigger.
   

## How to find your event subscription in various apps

- **Workato Webhooks: New Event via Webhook and Custom connectors**
  
  - Find the Webhook provider that sends events to your recipe.
  - Find the specific event subscription in the provider that relates to your recipe.
- **Azure Blob Storage: New Event**
  
  - On your Azure Storage account linked to your connection, navigate to **Events > Event Subscriptions**.
  - Find the specific event subscription that relates to your recipe.
- **BambooHR: New/Updated Employee, New Employee**
  
  - In BambooHR, go to your **Account Settings > Webhooks**
  - Find the Webhook subscription that relates to your recipe.
- **Gong.io : New Call**
  
  - In Gong, go to **Company setting > Automation rules**.
  - Find the Automation rule that relates to your recipe.
- **Greenhouse: New Event**
  
  - In Greenhouse, go to **Configure > Dev Center > Webhooks**.
  - Scroll down to find the list of webhooks.
  - Find the webhook that relates to your recipe.
- **Jira: New Event**
  
  - Select the **Gear icon > System**. Under **Advanced**, select **WebHooks**.
  - Find the webhook that relates to your recipe.
  
  > **PERMISSIONS REQUIRED**
  > 
  > You must have Administer Jira global permissions to find your event subscription in Jira.
  
- **Microsoft Dynamics 365: New Object, New/Updated Object**
  
  - In Microsoft Dynamics 365, create a solution containing the particular service endpoint related to the recipe.
  - Export the solution.
  - Extract it and modify the URL in the customizations XML.
  - Save and import the solution again.
- **Salesforce: New Outbound Message, New record, New/Updated record**
  
  - In Salesforce, go to **Setup > Process Automation > Workflow Actions > Outbound messages**.
  - Find the outbound message related to your recipe.
    - You can find the outbound message by searching or filtering based on the “Endpoint URL” for your old webhook URL. If your new URL is [https://webhooks.workato.com/webhooks/notify/salesforce?sobject=Account&org\_id=00D2w000009aBOk](https://webhooks.workato.com/webhooks/notify/salesforce?sobject=Account&org_id=00D2w000009aBOk), then your old webhook URL is [https://www.workato.com/webhooks/notify/salesforce?sobject=Account&org\_id=00D2w000009aBOk](https://www.workato.com/webhooks/notify/salesforce?sobject=Account&org_id=00D2w000009aBOk).
- **Slack: New event**
  
  - In Slack go to **App page > Features > Event subscriptions**.
  - Select **Change** on the “Request URL Input”.

---
