---
url: 'https://docs.workato.com/en/connectors/datadog/new-event-trigger.md'
description: >-
  The New event trigger uses webhooks to monitor Datadog for events in
  real-time.
---

# Datadog - New event trigger (real-time)

The **New event** trigger uses webhooks to monitor Datadog for events in real-time.

## Set up the New event trigger in Datadog

Complete the following steps to configure the **New event** trigger in Datadog:

1. Copy the static webhook URI from the trigger's **HELP** section.
   
   ![Static webhook URI](/assets/webhook-uri.ByeHXZ5W.png)_Static webhook URI_
   
2. Open [Datadog](https://app.datadoghq.com/) and go to **Integration > Webhooks > Configure**.
   
3. Click **\+ New**.
   
4. Enter a **Name** for the trigger webhook.
   
5. Enter the webhook URI in the **URL** field.
   
6. Click the **Custom headers** checkbox and enter a key-value pair `Workato-Key` header. For example:
   
   ```json
   {
     "Workato-Key": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
   }
   ```
   
   Save this value for later use in Workato.
   
7. Click **Save**.
   

## Input

| Input field | Description |
| --- | --- |
| Workato-Key | Enter the `Workato-Key` value [configured in Datadog](#set-up-the-new-event-trigger-in-datadog). |

## Output

| Output field | Description |
| --- | --- |
| ID | The unique Datadog identifier for the event. |
| Title | The title of the event. |
| Date | The date and time the event occurred. |
| Last updated | The date and time the event was last updated. |
| Event type | The type of event. |
| Body | The body content of the event. |
| Org | Contains information about the organization, such as `ID` and `Name`. |

---
