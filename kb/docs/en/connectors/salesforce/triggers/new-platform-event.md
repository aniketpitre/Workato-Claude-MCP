---
url: >-
  https://docs.workato.com/en/connectors/salesforce/triggers/new-platform-event.md
description: This trigger monitors Salesforce in real-time for new platform events.
---

# Salesforce - New platform event trigger (real-time)

This trigger monitors Salesforce in real-time for new platform events. The trigger fetches platform events created in the last 24 hours when the recipe first starts.

> **PLATFORM EVENTS ARE TEMPORARY**
> 
> Platform events are temporary. Any events not picked up within 24 hours are not processed. For example, events are not picked up if the recipe is stopped for over 24 hours.

## Input

| Input fields | Description |
| --- | --- |
| Platform event | Select the platform event to monitor. |
| SOQL WHERE clause | Enter a SOQL query to filter events by. For example: `Amount__c > 22.34 AND (City__c = 'San Francisco' OR City__c = 'New York')`. Refer to the [SOQL](/en/connectors/salesforce/salesforce-soql) guide for more information. |

## Output

| Output fields | Description |
| --- | --- |
| Created By ID | The Salesforce ID of the user who created the platform event. |
| Created Date | The data and time the event was created in Salesforce. |
| Event UUID | The Salesforce UUID (Universally Unique Identifier) for the event. |
| Replay ID | A number indicating the sequence of event notifications. |

Additional outputs load dynamically based on the selected platform event.
