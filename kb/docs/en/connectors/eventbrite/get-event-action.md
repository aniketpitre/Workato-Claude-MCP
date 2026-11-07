---
url: 'https://docs.workato.com/en/connectors/eventbrite/get-event-action.md'
description: >-
  The Get event attendees batch action in the Eventbrite connector lets you
  retrieve a list of attendees for a specific event using the event's ID.
---

# Eventbrite - Get event attendees action (batch)

The **Get event attendees** [batch action](/en/features/batch-processing) allows you to retrieve a list of attendees for a specific event using the event's unique ID. The [Eventbrite API](https://www.eventbrite.com/platform/api) typically limits the number of results to 50, but the actual number may be fewer if the attendee record has many custom fields.

![Get event attendees action](/assets/get-event-attendees-action.DOYSYL5k.png)_Eventbrite - Get event attendees action_

## Input

| Input field | Description |
| --- | --- |
| Event ID | Enter the unique identifier for the event to fetch attendees. |
| Status | Specify the registration status of the attendees to retrieve. |
| When first started, this recipe should pick up events from | Choose the starting date and time to begin fetching new or updated attendees. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Attendee IDs | Input the unique identifiers for specific attendees. Use a list datapill to fetch multiple attendee IDs. |

## Output

| Output field | Description |
| --- | --- |
| Attendees count | The number of attendees retrieved for the event. |
| Attendees | A list of attendees, including details such as names, emails, and ticket information. |

---
