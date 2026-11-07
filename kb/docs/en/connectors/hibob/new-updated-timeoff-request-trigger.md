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
