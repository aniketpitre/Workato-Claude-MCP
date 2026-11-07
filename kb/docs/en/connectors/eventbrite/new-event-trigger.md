---
url: 'https://docs.workato.com/en/connectors/eventbrite/new-event-trigger.md'
description: >-
  The New event created trigger in the Eventbrite connector checks for new
  events created in a selected organization in Eventbrite.
---

# Eventbrite - New event created trigger

The **New event created** trigger checks for new events created in Eventbrite.

![New event created trigger](/assets/new-event-trigger.CQKsKr7P.png)_Eventbrite - New event created trigger_

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Specify how frequently Workato checks for new events. This field defaults to every 30 minutes if not set. |
| When first started, this recipe should pick up events from | Set a start date for the trigger to begin fetching events. After you test or run the recipe, you cannot change this value. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Organization | Choose the organization within Eventbrite to monitor for event creation. This field defaults to the organization specified in the connection if left blank. |

## Output

| Output field | Description |
| --- | --- |
| Event ID | The unique identifier for the new event. |
| Status | The status of the event. |
| Date created | The timestamp when the event was created. |
| Event start | The start time and date for the event. |
| Event end | The end time and date for the event. |
| Timezone | The timezone in which the event is set. |
| Event URL | The URL to the event page on Eventbrite. |
| Organization ID | The identifier for the organization hosting the event. |
| Date modified | The timestamp when the event was last modified. |
| Capacity | The total capacity for the event. |
| Capacity is custom | Indicates if the event capacity is a custom value. |
| Currency | The currency for the event pricing. |
| Listed | Whether the event is listed publicly. |
| Shareable | Whether the event page is shareable. |
| Invite only | Whether the event is invite-only. |
| Online event | Whether the event is an online event. |
| Show remaining | Whether to show the remaining number of tickets. |
| Time limit | The time limit for ticket sales. |
| Hide start date | Whether to hide the start date of the event. |
| Hide end date | Whether to hide the end date of the event. |
| Locale | The locale for the event. |
| Is locked | Whether the event is locked from editing. |
| Privacy setting | The privacy setting of the event. |
| Is series | Whether the event is part of a series. |
| Is series parent | Whether the event is the parent of a series. |
| Is reserved seating | Whether the event has reserved seating. |
| Show pick a seat | Whether the pick-a-seat option is enabled. |
| Show seatmap thumbnail | Whether a seatmap thumbnail is shown. |
| Show colors in seatmap thumbnail | Whether colors are displayed in the seatmap thumbnail. |
| Source | The source of the event creation. |
| Is free | Whether the event is free. |
| Version | The version of the event details. |
| Logo ID | The identifier for the event's logo. |
| Organizer ID | The identifier for the event's organizer. |
| Venue ID | The identifier for the venue of the event. |
| Category ID | The identifier for the event's category. |
| Subcategory ID | The identifier for the event's subcategory. |
| Format ID | The identifier for the event's format. |
| Resource URL | The URL for the event resource on Eventbrite. |
| Logo | The logo for the event. |
| Name | The name of the event. |
| Description | The description of the event. |
| Organizer | The details of the organizer. |
| Venue | The details of the venue. |
| Category | The details of the event's category. |
| SubCategory | The details of the event's subcategory. |
| Format | The details of the event's format. |

---
