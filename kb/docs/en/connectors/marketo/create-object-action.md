---
url: 'https://docs.workato.com/en/connectors/marketo/create-object-action.md'
description: >-
  The Create object action in the Marketo connector lets you create
  opportunities, leads, programs, smart campaigns, and other objects in your
  instance.
---

# Marketo - Create object action

This action creates a new object in your Marketo instance.

## Input

| Field | Description |
| --- | --- |
| Object | Select the object you plan to create. Options include **Opportunity**, **Opportunity role**, **Lead**, **Program**, **Smart campaign**, and **Custom object**. |

Refer to the relevant sections to learn how to configure the input fields for the object you plan to create:

- [Opportunity](#opportunity-input-fields)
- [Opportunity role](#opportunity-role-input-fields)
- [Lead](#lead-input-fields)
- [Program](#program-input-fields)
- [Smart campaign](#smart-campaign-input-fields)
- [Custom object](#custom-object-input-fields)

### Opportunity input fields

| Field | Description |
| --- | --- |
| External opportunity ID | Provide the unique ID for the opportunity in an external system. |
| External opportunity campaign ID | Enter the campaign ID associated with the opportunity from an external source. |
| Amount | Fill in the total amount for the opportunity. |
| Close date | Enter the date when the opportunity is expected to close. |
| Description | Provide a brief description of the opportunity. |
| Expected revenue | Fill in the estimated revenue expected from the opportunity. |
| External company ID | Enter the external ID for the company associated with this opportunity. |
| External created date | Provide the date when the opportunity was created in an external system. |
| External sales person ID | Enter the ID of the salesperson from an external system. |
| Fiscal | Specify the fiscal period for this opportunity. |
| Fiscal quarter | Provide the fiscal quarter when this opportunity falls. |
| Fiscal year | Enter the fiscal year for the opportunity. |
| Forecast category | Specify the forecast category for this opportunity. |
| Forecast category name | Enter the name of the forecast category for the opportunity. |
| Is closed | Indicate whether the opportunity is closed. |
| Is won | Indicate whether the opportunity has been won. |
| Last activity date | Provide the date of the last activity related to this opportunity. |
| Lead source | Enter the source from which the lead originated. |
| Name | Fill in the name of the opportunity. |
| Next step | Provide details about the next step for this opportunity. |
| Probability | Enter the probability of winning this opportunity (as a percentage). |
| Quantity | Specify the quantity of items or services in the opportunity. |
| Stage | Provide the current stage of the opportunity. |
| Type | Enter the type or classification of the opportunity. |

### Opportunity role input fields

| Field | Description |
| --- | --- |
| Lead ID | Provide the unique ID for the lead associated with the opportunity. |
| Role | Enter the role of the lead in relation to the opportunity. |
| External contact ID | Provide the external contact ID associated with the lead. |
| External ID | Enter the external system ID related to the lead. |
| External created date | Provide the date when the role was created in the external system. |
| Is primary | Indicate whether this is the primary role for the opportunity. |

### Lead input fields

Refer to the Marketo documentation for a [list of standard fields](https://experienceleague.adobe.com/en/docs/marketo-developer/marketo/rest/assets/list-of-standard-fields) available through the API. This list includes common fields but may not cover all input fields specific to this action.

### Program input fields

| Field | Description |
| --- | --- |
| Folder ID | Provide the ID of the folder where you plan to create the program. |
| Folder type | Specify the type of folder. Accepted values include `Folder` and `Program`. |
| Name | Enter the name of the program you plan to create. |
| Program type | Specify the type of the program. Accepted values include `Default`, `Event`, `Event with Webinar`, `Engagement`, and `Email`. |
| Channel | Provide the marketing channel associated with the program. |
| Costs | Enter the total costs associated with the program. |
| Costs source list (costs) | Input a list datapill from which the program costs are derived. Learn more about [list input](/en/features/list-management#list-batch-action). |
| Cost (costs) | Provide the cost associated with the program. |
| Note (costs) | Enter any notes related to the costs of the program. |
| Start date (costs) | Provide the start date for the program costs. |
| Description | Provide a description of the program. |
| Tags | Enter tags associated with the program for categorization. |
| Tags source list (tags) | Specify the source list for program tags. |
| Tag type (tags) | Enter the type of tag for the program. |
| Tag value (tags) | Provide the value associated with the program's tag. |

### Smart campaign input fields

| Field | Description |
| --- | --- |
| Name | Provide the name of the smart campaign. |
| Folder | Enter the name of the folder where the smart campaign is located. |
| Folder type (folder) | Specify the type of folder. |
| Folder ID (folder) | Provide the unique ID of the folder where the smart campaign is stored. |
| Description | Enter a description of the smart campaign. |

### Custom object input fields

| Field | Description |
| --- | --- |
| Custom object name | Provide the name of the custom object. |

## Output

The output fields vary depending on the object you select for the action.

### Opportunity output fields

| Field | Description |
| --- | --- |
| Marketo GUID | The unique identifier assigned to the opportunity in Marketo. |

### Opportunity role output fields

| Field | Description |
| --- | --- |
| Marketo GUID | The unique identifier assigned to the opportunity role in Marketo. |

### Lead output fields

| Field | Description |
| --- | --- |
| Lead ID | The unique identifier assigned to the lead in Marketo. |

### Program output fields

| Field | Description |
| --- | --- |
| Success | Indicates whether the program was created successfully. |
| Request ID | The ID associated with the request to create the program. |
| Errors | Any errors that occurred during the request. |
| Code (errors) | The error code, if any, related to the request. |
| Message (errors) | A descriptive message for any errors encountered. |
| Warnings | Any warnings related to the request. |
| Result | A list of programs created or affected by the request. |
| ID (result) | The ID of the program created or affected. |
| Name (result) | The name of the program created or affected. |
| Description (result) | The description of the program created or affected. |
| URL (result) | The URL where the program can be accessed. |
| Type (result) | The type of the program created or affected. |
| Channel (result) | The channel associated with the program created. |
| Status (result) | The status of the program created or affected. |
| Workspace (result) | The workspace where the program was created or modified. |
| Tags (result) | Tags associated with the program created or affected. |
| Tag type (tags) | The type of tag associated with the program. |
| Tag value (tags) | The value of the tag associated with the program. |
| Folder (result) | The folder where the program is located. |
| Folder name (folder) | The name of the folder where the program is stored. |
| Type (folder) | The type of folder where the program is located. |
| Value (folder) | The value associated with the folder. |
| Created at | The datetime when the program was created. |
| Updated at | The datetime when the program was last updated. |
| SFDC ID | The Salesforce ID associated with the program created. |
| SFDC name | The Salesforce name associated with the program created. |

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
| End at (recurrence) | The datetime after which no further runs will be automatically scheduled. |
| Interval type (recurrence) | The type of interval for recurrence. For example, `Daily`, `Weekly`, or `Monthly`. |
| Interval (recurrence) | The number of interval units between recurrences. |
| Weekday only (recurrence) | Indicates whether the smart campaign only runs weekdays. |
| Weekday mask (recurrence) | A string array containing one or more of the following days: `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday`, `Saturday`, `Sunday`. The array may also be empty. |
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

### Custom object output fields

| Field | Description |
| --- | --- |
| Marketo GUID | The unique identifier assigned to the custom object in Marketo. |

---

---
url: >-
  https://docs.workato.com/en/connectors/marketo/create-update-upsert-leads-action.md
description: >-
  The Create/update/upsert leads action in the Marketo connector lets you
  create, update, or upsert up to 300 leads at once by a lookup field.
---

# Marketo - Create/update/upsert leads action (batch)

This action searches for leads in Marketo using a specified lookup field. If a matching lead is found, Workato updates the lead with the provided data. If no match is found, Workato creates new leads with the provided data. To create only new leads or to update only existing leads, configure the **Operation type** field. The action can handle a maximum of 300 leads in a single request. The action fails if more than 300 leads are provided.

## Input

| Field | Description |
| --- | --- |
| Lookup field | Select the field to identify unique leads. The default is email. |
| Operation type | Select the type of operation. The default is **Create or update**. |
| Leads | List of Lead objects. Select the leads fields you plan to create/update/upsert by clicking **Show optional fields**. |
| Leads source list (leads) | Input a list datapill. Learn more about [list input](/en/features/list-management#list-batch-action). |

Refer to the Marketo documentation for a [list of standard fields](https://experienceleague.adobe.com/en/docs/marketo-developer/marketo/rest/assets/list-of-standard-fields) available through the API. This list includes common fields but may not cover all input fields specific to this action.

## Output

| Field | Description |
| --- | --- |
| Request ID | The ID associated with the request to create/update/upsert leads. |
| Number of records processed | The total number of lead records processed in the batch. |
| Number of records created | The total number of leads that were successfully created. |
| Number of records updated | The total number of leads that were successfully updated. |
| Number of records skipped | The total number of leads that were skipped due to errors or invalid data. |
| Leads created | A list of leads that were created in the batch. |
| Lead (leads created) | The individual lead details for each lead created. |
| Leads updated | A list of leads that were updated in the batch. |
| Lead (leads updated) | The individual lead details for each lead updated. |
| Leads skipped | A list of leads that were skipped in the batch. |
| Lead (leads skipped) | The individual lead details for each lead skipped. |
| Error (leads skipped) | A list of errors encountered for the leads that were skipped. |
| Code (error) | The error code for any issues encountered during processing. |
| Message (error) | A descriptive message explaining the error encountered. |

---
