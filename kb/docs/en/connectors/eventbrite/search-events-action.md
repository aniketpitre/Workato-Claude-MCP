---
url: 'https://docs.workato.com/en/connectors/eventbrite/search-events-action.md'
description: >-
  The Search events batch action in the Eventbrite connector lets you find
  events by name or event ID and retrieve a list of matching events.
---

# Eventbrite - Search events action (batch)

The **Search events** [batch action](/en/features/batch-processing) allows you to search for events by name or event ID in Eventbrite. This action retrieves a list of events that match your search criteria, typically limited to around 50 events. This quota can vary based on the size of the event object.

![Search events action](/assets/search-events-action.CSJLWTng.png)_Eventbrite - Search events action_

## Input

| Input field | Description |
| --- | --- |
| Organization | Choose the organization for which you plan to search events. If left blank, the organization specified in the connection is used. |
| Event ID | Enter the event ID to search for specific events. |

## Output

| Output field | Description |
| --- | --- |
| Events | A list of events that match the search criteria such as event names, dates, and IDs. |

---
