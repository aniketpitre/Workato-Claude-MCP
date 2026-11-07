---
url: 'https://docs.workato.com/en/connectors/greenhouse/new-event-trigger.md'
description: >-
  The New event trigger in the Greenhouse connector fires in real time when a
  configured candidate, application, job, or offer event arrives via webhook.
---

# Greenhouse - New event trigger (real-time)

This trigger picks up new events that are created in your Greenhouse instance. Events are picked up via a webhook sent from Greenhouse.

Workato listens to Greenhouse webhooks and processes them in real-time.

![New event trigger](/assets/new-event-trigger.Dcb-IIGE.png)_New event trigger_

## Input

Select an event category and a specific event to listen to. This will generate a webhook endpoint URL. This will be needed to [configure a webhook in Greenhouse](#how-to-setup-a-webhook-in-greenhouse).

| Event Category | Events |
| --- | --- |
| Candidate | Candidate update Candidate stage change |
| Application | Application updated |
| Job | Job created Job updated |
| Offer | Offer created Offer updated |

## Output

The output of this trigger will be a datatree that contains information about the Greenhouse object.

Refer to the [Greenhouse object datapills](/en/connectors/greenhouse/object-types) documentation for more information.

## How to set up a webhook in Greenhouse

Complete the following steps to set up a webhook in Greenhouse:

1. Set up the Workato trigger and select the event to generate an endpoint URL.
   
   ![Retrieve Workato webhook endpint URL](/assets/workato-webhook-url.Dvyv2m_3.png)_Retrieve Workato webhook endpoint URL_
   
2. Prepare a secret key and paste it into the Workato trigger setup page. The secret key must be 32 characters in length. Keep the secret key available until the webhook is properly set up in Greenhouse as well.
   
3. Sign in to your Greenhouse instance and go to **Settings > Dev Center > Web Hooks**.
   
   ![Greenhouse Webhooks](/assets/create-webhook-in-greenhouse-1.VSIuavY6.png)_Greenhouse Webhooks_
   
4. Select **Web Hooks**.
   
   ![Create new webhook](/assets/create-webhook-in-greenhouse-2.DlnU4FaV.png)_Create new webhook_
   
5. Select the event specified in the Workato trigger.
   
6. Fill **Endpoint URL** with the endpoint provided by Workato.
   
7. Fill **Secret Key** with the secret key created while setting up the Workato trigger.
   
   ![Configure Greenhouse webhook](/assets/create-webhook-in-greenhouse-3.BY9yGnkA.png)_Configure Greenhouse webhook_
   
8. Select **Create webhook**.
   

Refer to the [Greenhouse Webhooks](https://developers.greenhouse.io/webhooks.html) documentation for more information.

---
