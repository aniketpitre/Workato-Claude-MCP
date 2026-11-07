---
url: 'https://docs.workato.com/en/connectors/levelpath/new-event-trigger.md'
description: >-
  The New event trigger initiates a recipe in real-time when a selected event
  occurs in LevelPath.
---

# LevelPath - New event trigger (real-time)

The **New event** trigger monitors LevelPath in real-time for events you configure.

You must register a webhook in your LevelPath account to enable this trigger. Go to **Company Settings > Webhooks**, then add a new destination endpoint using your connector's static webhook URL. To find this URL, open the **Test code** tab in the connector SDK and go to the **Source code** section. Expand the **Static webhook URI** section to copy the webhook URL.

## Input

| Input field | Description |
| --- | --- |
| Event | Select the LevelPath event to monitor. |

## Output

| Output field | Description |
| --- | --- |
| Source | Source system that triggered the event. |
| Event type | Type of event that triggered the recipe. |
| Timestamp | Time when the event occurred. |
| Data | Event payload sent from LevelPath. |

---
