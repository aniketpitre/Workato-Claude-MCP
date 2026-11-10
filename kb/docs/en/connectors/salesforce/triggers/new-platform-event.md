---
url: >-
  https://docs.workato.com/en/connectors/salesforce/triggers/new-platform-event.md
description: This trigger monitors Salesforce in real-time for new platform events.
---

# Salesforce - New platform event trigger (real-time)

This trigger monitors Salesforce in real-time for new platform events. The trigger also fetches past events by default when you start the recipe. Salesforce keeps high-volume platform events for up to 72 hours, so the recipe doesn't process older events.

> **FETCHING PAST EVENTS CAN USE YOUR SALESFORCE EVENT ALLOCATION**
> 
> Fetching past events can use a significant amount of your Salesforce event allocation. Set **Events to fetch on recipe start** to **Only new events** to skip them.

## Input

| Input fields | Description |
| --- | --- |
| Platform event | Select the platform event to monitor. |
| Events to fetch on recipe start | Optional. Select whether to fetch events published in Salesforce while the recipe was inactive, on first start or restart. Defaults to **All available events (resume from last processed)** if left blank. **All available events (resume from last processed)** resumes from the last event the recipe processed. If the recipe hasn't processed any events, or the last processed event is no longer available, the trigger fetches all events Salesforce keeps. **Only new events** fetches only events published after the recipe starts. |
| SOQL WHERE clause | Enter a SOQL query to filter events by. For example: `Amount__c > 22.34 AND (City__c = 'San Francisco' OR City__c = 'New York')`. Refer to the [SOQL](/en/connectors/salesforce/salesforce-soql) guide for more information. |

## Output

| Output fields | Description |
| --- | --- |
| Created By ID | The Salesforce ID of the user who created the platform event. |
| Created Date | The date and time the event was created in Salesforce. |
| Event UUID | The Salesforce UUID (Universally Unique Identifier) for the event. |
| Replay ID | A number indicating the sequence of event notifications. |

Additional outputs load dynamically based on the selected platform event.
