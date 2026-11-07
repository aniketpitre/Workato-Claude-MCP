---
url: >-
  https://docs.workato.com/en/connectors/google-workspace/trigger-new-admin-activity-event.md
description: >-
  This trigger runs the recipe every time a Google admin performs an activity in
  the Google Workspace.
---

# Google Workspace - New admin activity event trigger

The **New admin activity event** trigger runs the recipe every time a Google admin performs an activity in Google Workspace, such as creating a new resource in Calendar or changing a Gmail setting for an organizational unit.

### Input

| Input field | Description |
| --- | --- |
| When first started, this recipe should pick up events from | Enter the date and time when the trigger starts monitoring for events. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Event name | Locate the Google Workspace app in Google's [Admin event names](https://developers.google.com/admin-sdk/reports/v1/appendix/activity/admin-event-names) guide to find the event name. Use the value from the **Event name** row that corresponds with the activity you plan to monitor. For example, to configure the trigger to monitor for new Calendar resources, enter `CREATE_CALENDAR_RESOURCE`. |
| Filters | Select filters to narrow down the returned list of events. Separate each filer with a comma. Refer to Google's [filter parameter](https://developers.google.com/admin-sdk/reports/reference/rest/v1/activities/list#query-parameters) guide for more information. |

> **ADDITIONAL INPUT FIELDS**
> 
> The recipe editor generates additional input fields based on your **Event name** selection.

### Output

The **Create object** action's output fields vary based on your selected Object type. Refer to [Google Workspace's API documentation](https://developers.google.com/workspace) for more information about the output fields for each type.
