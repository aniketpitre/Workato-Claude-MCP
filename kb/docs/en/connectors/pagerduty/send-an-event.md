---
url: 'https://docs.workato.com/en/connectors/pagerduty/send-an-event.md'
description: >-
  The Send an event action in the PagerDuty connector lets you trigger,
  acknowledge, or resolve an event to report or update a problem.
---

# PagerDuty - Send an event action

This action sends PagerDuty a trigger event to report a new problem, or update an ongoing problem, depending on the event type.

## Input

| Field | Description |
| --- | --- |
| Service key **Required** | The GUID of one of your Events API V2 integrations. This is the "Integration Key" listed on the Events API V2 integration's detail page. |
| Event type **Required** | The type of event. Can be trigger, acknowledge, or resolve. |
| Description | Fields adding additional context about the location, impact, and character of the PagerDuty event. This field is required only for trigger events. |
| Details | This field is only used for trigger events. This object contains the following fields. Ping time, Load avg |
| Client | The name of the monitoring client that is triggering this event. This field is only used for trigger events. |
| Client URL | The URL of the monitoring client that is triggering this event. This field is only used for trigger events. |
| Contexts | Contexts to be included with the trigger such as links to graphs or images. This field is only used for trigger events. This object contains the following fields. Type, Href, Text |
| Incident key | The incident's de-duplication key. This field is required for event type is acknowledge and resolve |

## Output

| Field | Description |
| --- | --- |
| Status | Returns "success" if successful, or a short error message in case of a failure. |
| Message | A description of the problem, or "Event processed" if successful. |
| Incident key | The incident's de-duplication key. |

---
