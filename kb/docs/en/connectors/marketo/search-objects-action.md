---
url: 'https://docs.workato.com/en/connectors/marketo/search-objects-action.md'
description: >-
  The Search objects action in the Marketo connector lets you find
  opportunities, programs, leads, campaigns, and smart campaigns by your
  criteria.
---

# Marketo - Search objects action (batch)

This action searches for objects in your Marketo instance by a given search criteria.

## Input

| Field | Description |
| --- | --- |
| Object | Select the object you plan to search for. Options include **Opportunities**, **Opportunity roles**, **Programs**, **Leads**, **Campaigns**, and **Smart campaign**. |

Refer to the relevant sections to learn how to configure the input fields for the object you plan to search for:

- [Opportunities](#opportunities-input-fields)
- [Opportunity roles](#opportunity-roles-input-fields)
- [Programs](#programs-input-fields)
- [Leads](#leads-input-fields)
- [Campaigns](#campaigns-input-fields)
- [Smart campaigns](#smart-campaigns-input-fields)

### Opportunities input fields

| Field | Description |
| --- | --- |
| Filter type | Choose the filter criterion for the search. The search matches on this field. Options include **ID** or **External Opportunity ID**. |
| Filter values | Enter the values to match, separated by commas. |

### Opportunity roles input fields

| Field | Description |
| --- | --- |
| Filter type | Choose the filter criterion for the search. The search matches on this field. Options include **ID**, **External Opportunity ID**, and **Lead ID**. |
| Filter values | Enter the values to match, separated by commas. |

### Programs input fields

| Field | Description |
| --- | --- |
| Filter type | Choose the filter criterion for the search. The search matches on this field. Options include **ID**, **Program ID**, **Folder ID**, and **Workspace**. |
| Filter values | Enter values to match, separated by commas. |
| Earliest updated at | Exclude programs updated prior to this date. |
| Latest updated at | Exclude programs updated after this date. |
| Maximum results | Set the maximum number of programs to return. Default and maximum value is 200. |
| Offset | Set an integer offset for paging. Default is 0. |

### Leads input fields

| Field | Description |
| --- | --- |
| Filter type | Choose the filter criterion for the search. The search matches on this field. Options include **Email**, **ID**, **Cookie**, **Twitter ID**, **Facebook ID**, and **LinkedIn ID**. |
| Filter values | Enter values to match, separated by commas. |
| Output fields | Select the fields to use in your recipe. All fields are returned if this field is left blank. However, leaving this field blank isn't recommended as it can result in timeout errors. |

Refer to the Marketo documentation for a [list of standard fields](https://experienceleague.adobe.com/en/docs/marketo-developer/marketo/rest/assets/list-of-standard-fields) available through the API. This list includes common fields but may not cover all input fields specific to this action.

### Campaigns input fields

| Field | Description |
| --- | --- |
| Campaign name | Provide the campaign name to search. |
| Program name | Provide the program name. |

### Smart campaigns input fields

| Field | Description |
| --- | --- |
| Earliest updated at | Exclude smart campaigns updated prior to this date. |
| Latest updated at | Exclude smart campaigns updated after this date. |
| Is active | Set true to return only active campaigns. Default is false. |
| Max return | Set the maximum number of smart campaigns to return. Default is 20, maximum is 200. |
| Offset | Set an integer offset for paging. Default is 0. |

## Output

The output fields vary depending on the object you select for the action.

### Opportunities output fields

| Field | Description |
| --- | --- |
| Opportunities | A list of opportunities that matched the search criteria. |
| Created at (opportunities) | The datetime the opportunity was created. |
| External opportunity campaign ID (opportunities) | The campaign ID associated with the opportunity from an external source. |
| External opportunity ID (opportunities) | The unique ID for the opportunity in an external system. |
| Marketo GUID (opportunities) | The unique identifier assigned to the opportunity in Marketo. |
| Updated at (opportunities) | The datetime when the opportunity was updated. |
| Amount (opportunities) | The total amount for the opportunity. |
| Close date (opportunities) | The date when the opportunity is expected to close. |
| Description (opportunities) | The description of the opportunity |
| Expected revenue (opportunities) | The estimated revenue expected from the opportunity. |
| External company ID (opportunities) | The external ID for the company associated with this opportunity. |
| External created date (opportunities) | The date when the opportunity was created in an external system. |
| External sales person ID (opportunities) | The ID of the salesperson from an external system. |
| Fiscal (opportunities) | The fiscal period for this opportunity. |
| Fiscal quarter (opportunities) | The fiscal quarter when this opportunity falls. |
| Fiscal year (opportunities) | The fiscal year for the opportunity. |
| Forecast category (opportunities) | The forecast category for this opportunity. |
| Forecast category name (opportunities) | The name of the forecast category for the opportunity. |
| Is closed (opportunities) | Indicates whether the opportunity is closed. |
| Is won (opportunities) | Indicates whether the opportunity has been won. |
| Last activity date (opportunities) | The date of the last activity related to this opportunity. |
| Lead source (opportunities) | The source from which the lead originated. |
| Name (opportunities) | The name of the opportunity. |
| Next step (opportunities) | Details about the next step for this opportunity. |
| Probability (opportunities) | The probability of winning this opportunity (as a percentage). |
| Quantity (opportunities) | The quantity of items or services in the opportunity. |
| Stage (opportunities) | The current stage of the opportunity. |
| Type (opportunities) | The type or classification of the opportunity. |

### Opportunity roles output fields

| Field | Description |
| --- | --- |
| Opportunity roles | A list of opportunity roles that matched the search criteria. |
| Created at (opportunity roles) | The datetime the opportunity role was created. |
| External contact ID (opportunity roles) | The external contact ID associated with the lead. |
| External ID (opportunity roles) | The external system ID related to the lead. |
| Marketo GUID (opportunity roles) | The unique identifier assigned to the opportunity role in Marketo. |
| Updated at (opportunity roles) | The datetime the opportunity role was updated. |
| External created date (opportunity roles) | The date when the role was created in the external system. |
| External opportunity ID (opportunity roles) | The unique ID for the opportunity role in an external system. |
| Is primary (opportunity roles) | Indicates whether this is the primary role for the opportunity. |
| Lead ID (opportunity roles) | The unique ID for the lead associated with the opportunity. |
| Role (opportunity roles) | The role of the lead in relation to the opportunity. |

### Programs output fields

| Field | Description |
| --- | --- |
| Success | Indicates whether the search operation was successful. |
| Request ID | The ID associated with the request to search for programs matching the search criteria. |
| Errors | Any errors that occurred during the request. |
| Code (errors) | The error code, if any, related to the request. |
| Message (errors) | A descriptive message for any errors encountered. |
| Warnings | Any warnings related to the request. |
| Result | A list of programs that matched the search criteria. |
| ID (result) | The unique identifier for the program. |
| Name (result) | The name of the program. |
| Description (result) | The description of the program. |
| URL (result) | The URL of the program in the Marketo UI. |
| Type (result) | The type of the program. For example, `default`, `event`, `webinar`, or `nurture`. |
| Channel (result) | The channel of the program. |
| Status (result) | The status of the program. |
| Workspace (result) | The name of the workspace. |
| Tags (result) | The list of associated program tags. |
| Tag type (tags) | The type of the tag. |
| Tag value (tags) | The value of the corresponding tag type. |
| Folder (result) | The folder where the program is stored. |
| Folder name (folder) | The name of the folder. |
| Type (folder) | The type of folder. |
| Value (folder) | The value of the folder. |
| Created at (result) | The datetime the program was created. |
| Updated at (result) | The datetime the program was updated. |
| SFDC ID | The Salesforce ID associated with the program that matched the search criteria. |
| SFDC name | The Salesforce name associated with the program that matched the search criteria. |

### Leads output fields

| Field | Description |
| --- | --- |
| Leads | A list of leads that matched the search criteria. |

Refer to the Marketo documentation for a [list of standard fields](https://experienceleague.adobe.com/en/docs/marketo-developer/marketo/rest/assets/list-of-standard-fields) available through the API. This list includes common fields but may not cover all output fields specific to this action.

### Campaigns output fields

| Field | Description |
| --- | --- |
| Campaigns | A list of campaigns that matched the search criteria. |
| ID (campaigns) | The unique identifier for the campaign. |
| Name (campaigns) | The name of the campaign. |
| Description (campaigns) | The description of the campaign. |
| Type (campaigns) | The type of campaign. |
| Program ID (campaigns) | The unique identifier of the program associated with the campaign. |
| Program name (campaigns) | The name of the program associated with the campaign. |
| Active (campaigns) | Indicates whether the campaign is active. |
| Workspace name (campaigns) | The name of the workspace in which the campaign is located. |
| Updated at (campaigns) | The datetime when the campaign was updated. |
| Created at (campaigns) | The datetime when the campaign was created. |

### Smart campaigns output fields

| Field | Description |
| --- | --- |
| Result | A list of smart campaigns that matched the search criteria. |
| ID (result) | The unique identifier for the smart campaign. |
| Name (result) | The name of the smart campaign. |
| Description (result) | The description of the smart campaign. |
| Type (result) | The type of smart campaign. For example, `batch`, `default`, or `trigger`. |
| Is system (result) | Indicates whether the smart campaign is a system-level smart campaign. |
| Is active (result) | Indicates whether the smart campaign is currently active. |
| Is requestable (result) | Indicates whether the smart campaign can be requested through an API. |
| Recurrence (result) | The recurrence object for the smart campaign. |
| Start at (recurrence) | The datetime of the first scheduled campaign to run. |
| End at (recurrence) | The datetime after which no further runs will be automatically scheduled. |
| Interval type (recurrence) | The type of interval for recurrence. For example, `Daily`, `Weekly`, or `Monthly`. |
| Interval (recurrence) | The number of interval units between recurrences. |
| Weekday only (recurrence) | Indicates whether the smart campaign only runs weekdays. |
| Weekday mask (recurrence) | A string array containing one or more of the following days: `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday`, `Saturday`, or `Sunday`. The array can also be empty. |
| Day of month (recurrence) | The day of the month for the recurrence. |
| Day of week (recurrence) | The day of the week for the recurrence. |
| Week of month (recurrence) | The week of the month for the recurrence. |
| Qualification rule type (result) | The type of qualification rule for the smart campaign. For example, `once`, `any`, or `interval`. |
| Qualification rule interval (result) | The interval for qualification rule. |
| Qualification rule unit (result) | The unit of time for the qualification rule. |
| Max members (result) | The maximum number of members allowed in the smart campaign. |
| Is communication limit enabled (result) | Indicates whether communication limits are applied to the smart campaign. |
| Smart list ID (result) | The unique identifier for the smart list associated with the smart campaign. |
| Flow ID (result) | The unique identifier for the flow in the smart campaign. |
| Parent program ID (result) | The unique identifier for the parent program. |
| Folder (result) | The folder where the smart campaign is stored. |
| ID (folder) | The unique identifier for the folder. |
| Type (folder) | The type of folder. |
| Created at (result) | The datetime when the smart campaign was created. |
| Updated at (result) | The datetime when the smart campaign was updated. |
| Workspace (result) | The workspace in which the smart campaign is located. |
| Computed URL (result) | The URL where the smart campaign can be accessed or viewed. |
| Status (result) | The status of the smart campaign. |

---
