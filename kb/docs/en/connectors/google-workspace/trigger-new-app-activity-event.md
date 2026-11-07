---
url: >-
  https://docs.workato.com/en/connectors/google-workspace/trigger-new-app-activity-event.md
description: >-
  The New application event trigger runs the recipe every time a specific event
  occurs in the selected Google Workspace application.
---

# Google Workspace - New application event trigger

The **New application event** trigger runs the recipe every time a specific event occurs in the selected Google Workspace application.

### Input

| Input field | Description |
| --- | --- |
| When first started, this recipe should pick up events from | Enter the date and time when the trigger starts monitoring for events. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Application name | Select the Google Workspace app you plan to monitor from the drop-down list. |
| Event name | Enter the **Event name** of the event you plan to monitor. Open the [Google Workspace API reference](https://developers.google.com/admin-sdk/reference-overview) and go to the **Reports > Activity audit** page for your workspace app to find the **Event name**. Copy the value from the **Event name** row of the activity you plan to monitor. For example, enter `change_calendar_acls` to configure the trigger to monitor changes to a calendar. |
| Filters | Enter filters to narrow down the returned list of events. Separate each filter with a comma. Refer to the [filter parameters](https://developers.google.com/admin-sdk/reports/reference/rest/v1/activities/list#query-parameters) for more information. |

> **ADDITIONAL INPUT FIELDS**
> 
> The recipe editor generates additional input fields based on your **Event name** selection.

### Output

The **Create object** action's output fields vary based on your selected Object type. Refer to [Google Workspace's API documentation](https://developers.google.com/workspace) for more information about the output fields for each type.
