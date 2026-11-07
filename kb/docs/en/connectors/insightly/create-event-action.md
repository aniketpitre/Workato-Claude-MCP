---
url: 'https://docs.workato.com/en/connectors/insightly/create-event-action.md'
description: >-
  The Create event action in the Insightly connector lets you create a new event
  with title, location, dates, and linked records.
---

# Insightly - Create event action

This action creates a new event in your Insightly instance.

## Input

| Input field | Description |
| --- | --- |
| Title | The title of the event. |
| Location | The location of the event. |
| Details | The details of the event. |
| Start date | The start date and time of the event in Coordinated Universal Time (UTC). |
| End date | The end date and time of the event in Coordinated Universal Time (UTC). |
| All day | Whether the event is all day. |
| Publicly visible | Whether the event is publicly visible. |
| Reminder date | The reminder date and time of the event in Coordinated Universal Time (UTC). |
| Reminder sent | Whether the reminder is sent. |
| Event links | The event links of the event. |
| Event links source list | The source list from which the event links are derived. This field accepts a [list datapill](/en/features/list-management#list-batch-action) as input. |
| Contact ID | The contact ID associated with the event. |
| Organization ID | The organization ID associated with the event. |
| Project ID | The project ID associated with the event. |
| Lead ID | The lead ID associated with the event. |
| Opportunity ID | The opportunity ID associated with the event. |

## Output

The output of this action is a datatree that contains information about the [event](https://api.insightly.com/v3.1/Help#!/Events/GetEntities).

---
