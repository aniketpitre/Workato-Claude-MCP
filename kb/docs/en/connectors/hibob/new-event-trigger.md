---
url: 'https://docs.workato.com/en/connectors/hibob/new-event-trigger.md'
description: 'The New event trigger monitors HiBob for new events in real-time. '
---

# HiBob - New event trigger (real-time)

The **New event** trigger monitors HiBob for new events in real-time.

> **PREREQUISITES**
> 
> You must have at least one employee in HiBob to use this trigger. Create an employee, then re-connect to HiBob if an employee doesn't already exist.

## Input

| Input field | Description |
| --- | --- |
| Object | Select a HiBob object to monitor. |
| Event type | Select an event type to monitor. |

### Configuration in HiBob

Complete the following steps to register this webhook URI in HiBob:

1. Configure the [Input fields](#input) for this trigger. A webhook URI generates in the **Help** section.
   
2. Copy the webhook URI for use in HiBob.
   
3. Sign in to HiBob as an administrator.
   
4. Go to **System Settings Integrations > Webhooks**.
   
5. Click **Manage**.
   
6. Enter a **Name** for the webhook.
   
   ![The Add webhook modal](/assets/add-webhook.DRC2nKMZ.png)_The **Add webhook** modal_
   
7. Enter the **Endpoint URL** generated in Workato.
   
8. Use the **Events** drop-down menu to select the **Event type** you specified in Workato.
   
9. Click **Add**.
   

## Output

Output fields load dynamically based on the object and event type you select. For example, the following fields appear if you select the **Task** object and **Task status updated** event:

| Output field | Description |
| --- | --- |
| Company ID | Unique identifier of the company within HiBob where the task status update occurred. |
| Type | Event type indicating that the `To Do` status of a task has changed. |
| Triggered by | Unique identifier of the user or system that performed the task update. |
| Triggered at | Date and time (with timezone) when the task status was updated. |
| Version | API event version, specifying the schema version for this event data. |
| To do IDs | Unique identifiers of the `To Do` tasks impacted by this event. |
| To do requested for IDs | Identifier of the user for whom the "To Do" task was created/requested. |
| To do assignee IDs | Identifier of the user assigned to complete the `To Do` task. |
| New status | Updated status of the task, indicating it has been marked as `Closed`. |

---

---
url: >-
  https://docs.workato.com/en/connectors/hibob/new-updated-timeoff-request-trigger.md
description: Triggers when a time off request is created or updated in HiBob.
---

# HiBob - New/updated timeoff request trigger

The **New/updated timeoff request** trigger runs when a time off request is created or updated in HiBob.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Select how frequently trigger should check for new events. The minimum value allowed is 5 minutes. [Learn more](/en/recipes/polling-intervals) |
| When first started, this recipe should pick up events from | Select the date and time from calendar. The recipe picks up records from the date and time you specify when you start it for the first time. This value can't be changed after you run or test the recipe. |
| Include pending | Select the boolean value from the drop-down menu. Indicates whether to include pending requests in the results. Defaults to **true** if left blank. |

## Output

| Output field | Description |
| --- | --- |
| Request ID | Unique identifier of the time off request. |
| Employee ID | Unique identifier of the employee associated with the time off request. |
| Change type | Specifies whether the time off request was _Created_, _Updated_, or _Deleted_. |
| Total duration | Total length of the time off requested. |
| Policy type display name | Name of the leave policy under which the time off is requested. |
| Change reason | Reason provided for the creation or update of the time off request. |
| End date | The last date of the requested time off. |
| Employee email | Email address of the employee requesting the time off. |
| Type | Unit type used for time off measurement. |
| Start portion | Portion of the day when the time off begins. |
| Employee display name | Display name of the employee requesting the time off. |
| Duration unit | The unit in which the total duration is measured. |
| End portion | Portion of the day when the time off ends. |
| Total cost | Cost associated with the requested time off. |
| Start date | The first date of the requested time off. |
| Date | Specific date associated with the daily breakdown of the request. |
| Hours on date | Number of hours taken off on the specified date. |
| Daily hours | Standard working hours in a day for the employee. |
| Day portion | Indicates whether the day off is full-day, half-day, or custom hours. |

---
