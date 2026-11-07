---
url: 'https://docs.workato.com/en/connectors/eventbrite/updated-order-trigger.md'
description: >-
  The New/updated order for event trigger in the Eventbrite connector checks for
  new or updated orders and retrieves the attendees in each order.
---

# Eventbrite - New/updated order for event trigger

The **New/updated order for event** trigger checks for new or updated orders in Eventbrite. This trigger also retrieves a list of attendees included within each order. Initially, only the first 50 events are shown in the picklist, but you can search for all events using the **Event** field.

![New/updated order for event trigger](/assets/new-updated-order-trigger.Cbz6MuOw.png)_Eventbrite - New/updated order for event trigger_

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Set the frequency at which Workato checks for new or updated orders. This field defaults to 30 minutes if left blank. |
| When first started, this recipe should pick up events from | Choose the start date and time from which the trigger begins fetching orders. After you test or run the recipe, you cannot change this value. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Organization | Select the organization to monitor for new or updated orders. This field defaults to the organization specified in the connection if left blank. |
| Event | Choose the specific event to fetch new or updated orders. This field monitors orders for all events owned by the connected Eventbrite user if left blank. |

## Output

| Output field | Description |
| --- | --- |
| Costs | The cost details associated with the order. |
| Name | The name of the individual who placed the order. |
| Time remaining | The time left for the order to be completed. |
| Event ID | The unique identifier for the event associated with the order. |
| Event | Details of the event for which the order was placed. |
| Resource URI | The URI for the order resource on Eventbrite. |
| ID | The unique identifier for the order. |
| Date changed | The timestamp when the order details were last updated. |
| Date created | The timestamp when the order was created. |
| First name | The first name of the person who placed the order. |
| Last name | The last name of the person who placed the order. |
| Email | The email address of the person who placed the order. |
| Status | The status of the order. |
| Attendees | A list of attendees associated with the order. |

---
