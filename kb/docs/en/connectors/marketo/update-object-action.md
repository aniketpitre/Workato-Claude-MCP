---
url: 'https://docs.workato.com/en/connectors/marketo/update-object-action.md'
description: >-
  The Update object action in the Marketo connector lets you update
  opportunities, leads, smart campaigns, and custom objects in your instance.
---

# Marketo - Update object action

This action updates an object in your Marketo instance.

## Input

| Field | Description |
| --- | --- |
| Object | Select the object you plan to update. Options include **Opportunity**, **Lead**, **Smart campaign**, and **Custom object**. |

Refer to the relevant sections to learn how to configure the input fields for the object you plan to update:

- [Opportunity](#opportunity-input-fields)
- [Lead](#lead-input-fields)
- [Smart campaign](#smart-campaign-input-fields)
- [Custom object](#custom-object-input-fields)

### Opportunity input fields

| Field | Description |
| --- | --- |
| Opportunity ID / External opportunity ID | Provide the unique ID. **Opportunity ID** is required when **Dedupe by** is set to **ID field**; **External opportunity ID** is required when set to **Deduplication fields**. |
| Dedupe by | Select the fields to deduplicate by. Options include **Deduplication fields** and **ID field**. Set to **Deduplication fields** by default. |
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

### Lead input fields

| Field | Description |
| --- | --- |
| Lead ID / Email | Enter the ID or email of the lead you plan to update. |

Refer to the Marketo documentation for a [list of standard fields](https://experienceleague.adobe.com/en/docs/marketo-developer/marketo/rest/assets/list-of-standard-fields) available through the API. This list includes common fields but may not cover all input fields specific to this action.

### Smart campaign input fields

| Field | Description |
| --- | --- |
| Smart campaign ID / Smart campaign | Enter the smart campaign ID or select the smart campaign you plan to update. |
| Name | Provide the new name for the smart campaign. |
| Description | Provide the new description for the smart campaign. |

### Custom object input fields

| Field | Description |
| --- | --- |
| Custom object name / Object name | Select or enter the name of the custom object. If entering the object name, add the suffix `_c`. |

## Output

The output fields vary depending on the object you select for the action.

### Opportunity output fields

| Field | Description |
| --- | --- |
| Marketo GUID | The unique identifier assigned to the opportunity in Marketo. |

### Lead output fields

| Field | Description |
| --- | --- |
| Lead ID | The unique identifier for the lead. |

Refer to the Marketo documentation for a [list of standard fields](https://experienceleague.adobe.com/en/docs/marketo-developer/marketo/rest/assets/list-of-standard-fields) available through the API. This list includes common fields but may not cover all output fields specific to this action.

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

### Custom object output fields

| Field | Description |
| --- | --- |
| Marketo GUID | The unique identifier assigned to the custom object in Marketo. |

---
