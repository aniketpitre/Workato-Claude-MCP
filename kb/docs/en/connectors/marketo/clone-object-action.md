---
url: 'https://docs.workato.com/en/connectors/marketo/clone-object-action.md'
description: >-
  The Clone object action in the Marketo connector lets you clone a program or
  smart campaign into a destination folder you specify.
---

# Marketo - Clone object action

This action clones an object you specify within your Marketo instance.

## Input

| Field | Description |
| --- | --- |
| Object | Select the object you plan to clone. You can select **Program** or **Smart campaign**. |
| Cloned asset name | Provide the cloned asset name. |
| Cloned asset description | Provide the cloned asset description. |
| Destination folder | Expand this field to configure the destination folder fields for this action. |
| Folder type (destination folder) | Specify or select the type of folder where this object is cloned. Accepted values include **Folder** and **Program**. |
| Folder ID (destination folder) | Provide the folder ID of the destination folder, or select the destination folder from the drop-down menu. |

Refer to the relevant sections to learn how to configure the input fields for the object you plan to clone:

- [Program](#program-input-fields)
- [Smart campaign](#smart-campaign-input-fields)

### Program input fields

| Field | Description |
| --- | --- |
| Program ID / Program | Enter the program ID or select the program you plan to clone. |

> **ASSET RESTRICTIONS FOR PROGRAM CLONING**
> 
> This action doesn't support cloning programs that contain the following asset types:
> 
> - Push notifications
> - In-app messages
> - In-app programs
> - Reports
> - Social assets

### Smart campaign input fields

| Field | Description |
| --- | --- |
| Smart campaign ID / Select campaign | Enter the smart campaign's unique identifier or select the smart campaign. The smart campaign ID is the first contiguous set of numbers after the `SC` in the URL. For example, if the URL ends with `SC1900A1`, the smart campaign ID is `1900`. |

## Output

The output fields vary depending on the object you select for the action.

### Program output fields

| Field | Description |
| --- | --- |
| ID | The unique identifier for the program. |
| Name | The name of the program. |
| Description | The description of the program. |
| URL | The URL of the program in the Marketo UI. |
| Type | The type of the program, such as, `default`, `event`, `webinar`, or `nurture`. |
| Channel | The channel of the program. |
| Status | The status of the program. |
| Workspace | The name of the workspace. |
| Tags | The list of associated program tags. |
| Tag type (tags) | The type of the tag. |
| Tag value (tags) | The value of the corresponding tag type. |
| Folder | The folder where the program is stored. |
| Folder name (folder) | The name of the folder. |
| Type (folder) | The type of folder. |
| Value (folder) | The value of the folder. |
| Created at | The datetime the program was created. |
| Updated at | The datetime the program was updated. |

### Smart campaign output fields

| Field | Description |
| --- | --- |
| ID | The unique identifier for the smart campaign. |
| Name | The name of the smart campaign. |
| Description | The description of the smart campaign. |
| Type | The type of smart campaign. For example, `batch`, `default`, or `trigger`. |
| Is system | Indicates whether the smart campaign is a system-level smart campaign. |
| Is active | Indicates whether the smart campaign is currently active. |
| Is requestable | Indicates whether the smart campaign can be requested through an API. |
| Recurrence | The recurrence object for the smart campaign. |
| Start at (recurrence) | The datetime of the first scheduled campaign to run. |
| End at (recurrence) | The datetime after which no further runs are automatically scheduled. |
| Interval type (recurrence) | The type of interval for recurrence. For example, `Daily`, `Weekly`, or `Monthly`. |
| Interval (recurrence) | The number of interval units between recurrences. |
| Weekday only (recurrence) | Indicates whether the smart campaign runs on weekdays only. |
| Weekday mask (recurrence) | A string array containing one or more of the following days: `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday`, `Saturday`, or `Sunday`. The array can also be empty. |
| Day of month (recurrence) | The day of the month for the recurrence. |
| Day of week (recurrence) | The day of the week for the recurrence. |
| Week of month (recurrence) | The week of the month for the recurrence. |
| Qualification rule type | The type of qualification rule for the smart campaign. For example, `once`, `any`, or `interval`. |
| Qualification rule interval | The interval for qualification rule. |
| Qualification rule unit | The unit of time for the qualification rule. |
| Max members | The maximum number of members allowed in the smart campaign. |
| Is communication limit enabled | Indicates whether communication limits are applied to the smart campaign. |
| Smart list ID | The unique identifier for the smart list associated with the smart campaign. |
| Flow ID | The unique identifier for the flow in the smart campaign. |
| Parent program ID | The unique identifier for the parent program. |
| Folder | The folder where the smart campaign is stored. |
| ID (folder) | The unique identifier for the folder. |
| Type (folder) | The type of folder. |
| Created at | The datetime when the smart campaign was created. |
| Updated at | The datetime when the smart campaign was updated. |
| Workspace | The workspace in which the smart campaign is located. |
| Computed URL | The URL where the smart campaign can be accessed or viewed. |
| Status | The status of the smart campaign. |

---
