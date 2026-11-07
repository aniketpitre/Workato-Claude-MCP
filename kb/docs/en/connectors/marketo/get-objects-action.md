---
url: 'https://docs.workato.com/en/connectors/marketo/get-objects-action.md'
description: >-
  The Get objects action in the Marketo connector lets you retrieve object
  schemas, channels, programs, lead activities, folders, and smart campaigns.
---

# Marketo - Get objects action

This action retrieves objects in your Marketo instance based on your search criteria.

## Input

| Field | Description |
| --- | --- |
| Object | Options include **Object schema**, **Channel**, **Program**, **Lead activities**, **Folder**, and **Smart campaign**. |

Refer to the relevant sections to learn how to configure the input fields for the object you plan to retrieve:

- [Object schema](#object-schema-input-fields)
- [Channel](#channel-input-fields)
- [Program](#program-input-fields)
- [Lead activities](#lead-activities-input-fields)
- [Folder](#folder-input-fields)
- [Smart campaign](#smart-campaign-input-fields)
- [Tokens](#tokens-input-fields)

### Object schema input fields

| Field | Description |
| --- | --- |
| Schema to retrieve | Select the schema you plan to retrieve. Options include **Leads**, **Companies**, **Opportunities**, **Roles**, **SalesPersons**, and **Custom Objects**. |
| Output fields | Choose the fields of the selected objects you plan to use in your recipe. All fields are returned if left blank. |

### Channel input fields

| Field | Description |
| --- | --- |
| Channel name | Provide the name of the channel you plan to retrieve. |

### Program input fields

| Field | Description |
| --- | --- |
| Program name | Provide the name of the program you plan to retrieve. |

### Lead activities input fields

| Field | Description |
| --- | --- |
| Activity | Select the activity type to retrieve. You can select a maximum of ten activities. |
| List | Select activities from this list. If left blank, lead activities from all lists are retrieved. |
| Lead IDs | Provide a comma-separated list of lead IDs. |
| Since | Select a starting date. If left blank, lead activities from the last 30 days are retrieved. |
| Next page token | Specify the paging token to return the next page of results and override the **Since** input field. |

### Folder input fields

| Field | Description |
| --- | --- |
| By ID | Expand this field to retrieve the folder by its ID. |
| Folder ID (By ID) | Provide the folder ID or select the folder. |
| Folder type (By ID) | Provide or select the type of folder. Accepted values include **Folder** and **Program**. |
| Name | Enter the name of the folder you plan to retrieve. |

### Smart campaign input fields

| Field | Description |
| --- | --- |
| Smart campaign ID / Select campaign | Enter the smart campaign's unique identifier or select the smart campaign. The smart campaign ID is the first contiguous set of numbers after the `SC` in the URL. For example, if the URL ends with `SC1900A1`, the smart campaign ID is `1900`. |
| Name | Enter the name of the smart campaign. Only one of either the smart campaign ID or name is required. If both are provided, the ID takes precedence. |

### Tokens input fields

| Field | Description |
| --- | --- |
| Folder ID | Provide the folder ID or select the folder. |
| Folder type | Provide or select the type of folder. Accepted values include **Folder** and **Program**. |

## Output

The output fields vary depending on the object you select for the action.

### Object schema output fields

| Field | Description |
| --- | --- |
| Object name | The name of the object schema returned by the action. |
| Object label | The label or display name of the object schema. |
| Custom object? | Indicates whether the object is a custom object. |
| Fields | A list of fields associated with the object schema. |
| Field name (fields) | The name of each field within the object schema. |
| Field label (fields) | The label or display name of each field. |
| Length (fields) | The length of each field, specifying the maximum number of characters. |
| Original type (fields) | The original data type of each field in the schema. |
| Mapped type (fields) | The data type each field is mapped to in Marketo. |
| Updateable (fields) | Indicates whether each field can be updated. |
| CRM managed (fields) | Indicates whether each field is managed by the CRM. |
| Custom field? (fields) | Indicates whether each field is a custom field. |

### Channel output fields

| Field | Description |
| --- | --- |
| ID | The unique identifier of the channel. |
| Name | The name of the channel. |
| Description | A description of the channel. |
| Applicable program type | The type of programs that can use this channel. |
| Program statuses | A list of statuses applicable to programs within this channel. |
| Name (program statuses) | The name of each program status within the channel. |
| Step (program statuses) | The step or stage of each program status. |
| Description (program statuses) | A description of each program status. |
| Hidden (program statuses) | Indicates whether each program status is hidden. |
| Success (program statuses) | Indicates whether each program status represents a successful outcome. |
| Created date | The date when the channel was created. |
| Updated date | The date when the channel was last updated. |

### Program output fields

| Field | Description |
| --- | --- |
| ID | The unique identifier for the program. |
| Name | The name of the program. |
| Description | The description of the program. |
| URL | The URL of the program in the Marketo UI. |
| Type | The type of the program. For example, `default`, `event`, `webinar`, and `nurture`. |
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

### Lead activities output fields

| Field | Description |
| --- | --- |
| Lead activities | A list of activities associated with the lead. |
| Activity ID (lead activities) | The unique identifier of the activity. |
| Lead ID (lead activities) | The unique identifier of the lead associated with the activity. |
| Activity type ID (lead activities) | The unique identifier of the activity type. |
| Activity date (lead activities) | The date when the activity occurred. |
| Primary attribute value ID (lead activities) | The ID of the primary attribute value associated with the activity. |
| Activity primary attribute (lead activities) | The primary attribute associated with the activity. |
| Attributes (lead activities) | A list of additional attributes related to the activity. |
| Name (attributes) | The name of each attribute related to the activity. |
| Value (attributes) | The value of each attribute related to the activity. |
| More results (lead activities) | Indicates if there are additional results available beyond the current set. |
| Next page token (lead activities) | A token used to retrieve the next page of results if available. |

### Folder output fields

| Field | Description |
| --- | --- |
| Name | The name of the folder. |
| Description | A description of the folder. |
| Created at | The date and time when the folder was created. |
| Updated at | The date and time when the folder was last updated. |
| URL | The URL where the folder can be accessed. |
| Folder ID | The unique identifier of the folder. |
| ID (folder ID) | The ID assigned to the folder. |
| Type (folder ID) | The type of the folder ID. |
| Folder type | The type of the folder. |
| Parent | The name of the parent folder, if applicable. |
| ID (parent) | The unique identifier of the parent folder. |
| Type (parent) | The type of the parent folder. |
| Path | The path or location of the folder within the folder hierarchy. |
| Is archive | Indicates whether the folder is an archive. |
| Is system | Indicates whether the folder is a system folder. |
| Access zone ID | The ID of the access zone where the folder is located. |
| Workspace | The workspace where the folder is located. |
| ID | The unique identifier of the folder. |

### Smart campaign output fields

| Field | Description |
| --- | --- |
| ID | The unique identifier for the smart campaign. |
| Name | The name of the smart campaign. |
| Description | The description of the smart campaign. |
| Type | The type of smart campaign. For example, `batch`, `default`, `trigger`. |
| Is system | Indicates whether the smart campaign is a system-level smart campaign. |
| Is active | Indicates whether the smart campaign is currently active. |
| Is requestable | Indicates whether the smart campaign can be requested through an API. |
| Recurrence | The recurrence object for the smart campaign. |
| Start at (recurrence) | The datetime of the first scheduled campaign to run. |
| End at (recurrence) | The datetime after which no further runs will be automatically scheduled. |
| Interval type (recurrence) | The type of interval for recurrence. For example, `Daily`, `Weekly`, or `Monthly`. |
| Interval (recurrence) | The number of interval units between recurrences. |
| Weekday only (recurrence) | Indicates whether the smart campaign only runs weekdays. |
| Weekday mask (recurrence) | A string array containing one or more of the following days: `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday`, `Saturday`, or `Sunday`. The array can also be empty. |
| Day of month (recurrence) | The day of the month for the recurrence. |
| Day of week (recurrence) | The day of the week for the recurrence. |
| Week of month (recurrence) | The week of the month for the recurrence. |
| Qualification rule type | The type of qualification rule for the smart campaign. For example, `once`, `any`, or `interval`. |
| Qualification rule interval | The interval for the qualification rule. |
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

### Tokens output fields

| Field | Description |
| --- | --- |
| Success | Indicates whether the tokens were successfully retrieved. |
| Request ID | The unique identifier for the request to retrieve tokens by folder ID. |
| Errors | Contains any errors encountered during the request. |
| Code (errors) | The error code associated with the error, indicating the type of error. |
| Message (errors) | A descriptive message providing more details about the error. |
| Warnings | Contains any warnings that do not necessarily prevent the request from succeeding but should be noted. |
| Result | The overall result of the request, including any retrieved tokens or folders. |
| Tokens (result) | An array of tokens retrieved in the response. |
| Name (tokens) | The name assigned to the token. |
| Type (tokens) | The type of the token. |
| Value (tokens) | The value associated with the token. |
| Computed URL (tokens) | The URL generated for accessing the token's resource. |
| Section (tokens) | The section to which the token belongs. |
| Group ID (tokens) | The identifier of the group that the token is associated with. |
| Sort order (tokens) | The order in which the tokens should be sorted or displayed. |
| Last modified (tokens) | The timestamp indicating when the token was last modified. |
| Folder (result) | An object representing the folder from which the tokens were retrieved. |
| Type (folder) | The type of folder. |
| Value (folder) | The value or name of the folder. |

---

---
url: >-
  https://docs.workato.com/en/connectors/marketo/remove-leads-from-list-action.md
description: >-
  The Remove leads from lead list action in the Marketo connector lets you
  remove selected leads or lead IDs from a list in your instance.
---

# Marketo - Remove leads from lead list action

This action removes leads from a lead list in Marketo.

## Input

| Field | Description |
| --- | --- |
| List / List ID | Select or provide the ID of the list you plan to remove leads from. |
| Leads / Lead IDs | Select or provide the leads or lead IDs you plan to remove from the list. If selecting leads, only the first 300 leads are displayed. |

## Output

| Field | Description |
| --- | --- |
| Result | The result of the action. |
| Lead ID (result) | The ID of the lead that was removed. |
| Status (result) | The status of the operation. |
| Success | Whether the operation was successful. |
| Request ID | The request ID of the operation. |

---

---
url: >-
  https://docs.workato.com/en/connectors/marketo/return-data-to-marketo-self-service-flow-step-action.md
description: >-
  The Return data to Self Service Flow Step action in the Marketo connector lets
  you send lead updates back to Marketo from a flow step invocation.
---

# Marketo - Return data to Marketo Self Service Flow Step action

This action returns data to Marketo from a Self Service Flow Step invocation.

It must be used with the [New Marketo Self Service Flow Step trigger](/en/connectors/marketo/new-marketo-self-service-flow-step-trigger). Together, these create a [Marketo Self Service Flow Step](https://experienceleague.adobe.com/en/docs/marketo/using/product-docs/core-marketo-concepts/smart-campaigns/flow-actions/flow-step-service). The recipe must be started in Workato before you can continue setting up the flow step in Marketo.

If any changes are made to the trigger or action configurations, a new flow step service must be created in Marketo, and the old service should be deprecated. To specify which values are returned to Marketo, you must first select the corresponding fields in the trigger configuration.

## Input

| Field | Description |
| --- | --- |
| Callback URL | The callback URL. This input field must be mapped from the [New Marketo Self Service Flow Step trigger](/en/connectors/marketo/new-marketo-self-service-flow-step-trigger). |
| Callback API key | The callback API key. This input field must be mapped from the [New Marketo Self Service Flow Step trigger](/en/connectors/marketo/new-marketo-self-service-flow-step-trigger). |
| Callback token | The callback token. This input field must be mapped from the [New Marketo Self Service Flow Step trigger](/en/connectors/marketo/new-marketo-self-service-flow-step-trigger). |
| Outgoing lead attributes | Lead data that Workato sends to Marketo to update each lead. |
| Outgoing lead attributes source list (outgoing lead attributes) | Input a list datapill from which outgoing lead attributes are derived. Learn more about [list input](/en/features/list-management#list-batch-action). |
| Lead attributes (outgoing lead attributes) | Expand to configure the lead attributes fields. |
| ID (lead attributes) | Provide the lead ID to specify which lead to update. |

## Output

There is no output for this action.

> **FURTHER READING**
> 
> - [Self-service Flow Steps](/en/connectors/marketo/self-service-flow-steps)
> - [New Marketo Self Service Flow Step trigger (real-time)](/en/connectors/marketo/new-marketo-self-service-flow-step-trigger)

---
