---
url: 'https://docs.workato.com/en/connectors/workato-webhooks.md'
description: >-
  The Webhooks connector enables you to trigger Workato recipes from real-time
  event notifications that applications send to a target URL.
---

# Webhooks

![Webhooks trigger](/assets/begin-setup.Cjg7i3U4.png)

Webhooks are notifications sent by an application to a target URL as soon as an event happens. Typically, you can define specific events to receive notifications for.

For example, you can [configure a webhook trigger](/en/connectors/workato-webhooks/config) to create new trigger events when **Urgent** tickets are created. Your recipe can then send an SMS message to notify the corresponding account manager.

> **INFO**
> 
> This connector doesn't require you to establish a connection.

The Workato webhooks gateway listens to all events. When an event is received, the gateway will direct this to the appropriate recipe. This trigger event will result in a job and execute the actions in that recipe.

## Rate limits

This trigger is subject to our [webhook gateway's quotas](/en/troubleshooting/webhook-gateway-limits).

## Additional considerations

Consider the following information before you use the Webhooks connector:

| Description | Quota |
| --- | --- |
| Maximum number of recipes subscribed to the same webhook URL | 100 |

- Webhook recipes can't use the same URL for different webhook types.
  
  - For example, you can't use the same webhook address `https://webhooks.workato.com/webhooks/rest/{UNIQUE_ID}/lead` with **PUT/POST with JSON payload** as the **Webhook type** in one recipe and **GET request** as the **Webhook type** in another recipe.
  
  ![Webhook types must be the same across all identical URLs](/assets/webhook-type.Dt-nsEcM.png)_Webhook types must be the same across all identical URLs_
  

## Create your own webhook trigger

- [Set up webhook using wizard](/en/connectors/workato-webhooks/wizard)
- [New event via HTTP webhook trigger](/en/connectors/workato-webhooks/config)
- [Debug common errors](/en/connectors/workato-webhooks/common-errors)

---
