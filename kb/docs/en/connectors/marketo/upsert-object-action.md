---
url: 'https://docs.workato.com/en/connectors/marketo/upsert-object-action.md'
description: >-
  The Upsert object action in the Marketo connector lets you create or update a
  lead, opportunity, opportunity role, or custom object.
---

# Marketo - Upsert object action

This action creates or updates an object in Marketo.

## Input

| Field | Description |
| --- | --- |
| Object | The type of object to upsert. |

Refer to the relevant sections to learn how to configure the input fields for the object you plan to upsert:

- [Lead](#lead-input-fields)
- [Opportunity](#opportunity-input-fields)
- [Opportunity role](#opportunity-role-input-fields)
- [Custom object](#custom-object-input-fields)

### Lead input fields

| Field | Description |
| --- | --- |
| Lookup field (dedup) | This field is used to identify unique records. Options include **Cookies**, **Email address**, **Marketo Social Twitter ID**, **Marketo Social Facebook ID**, **Marketo Social LinkedIn ID**, **SFDC Account ID**, **SFDC Contact ID**, **SFDC Lead ID**, and **SFDC Lead Owner ID**. |
| Lead fields | Expand to configure the fields associated with the lead for the upsert action. |

Refer to the Marketo documentation for a [list of standard fields](https://experienceleague.adobe.com/en/docs/marketo-developer/marketo/rest/assets/list-of-standard-fields) available through the API. This list includes common fields but may not cover all input fields specific to this action.

### Opportunity input fields

| Field | Description |
| --- | --- |
| Opportunity fields | Expand to configure the fields associated with the opportunity for the upsert action. |
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
| Opportunity role fields | Expand to configure the fields associated with the opportunity role for the upsert action. |
| External opportunity ID | The unique identifier for the opportunity from an external system. |
| Lead ID | The unique identifier for the lead associated with the opportunity role. |
| Role | The role of the lead in the opportunity. |
| External contact ID | The unique identifier for the contact from an external system. |
| External ID | A general external identifier for the opportunity role, if applicable. |
| External created date | The date when the opportunity role was created in the external system. |
| Is primary | Indicates whether this role is the primary role for the opportunity. |

### Custom object input fields

| Field | Description |
| --- | --- |
| Custom object / Custom object name | Select a custom object name from the list, or enter a custom object name with the suffix `_c`. |
| Custom object fields | Expand to configure the fields associated with the custom object for the upsert action. |

## Output

The output fields vary depending on the object you select for the action.

### Lead output fields

| Field | Description |
| --- | --- |
| Marketo GUID | The unique identifier assigned to the lead in Marketo. |

### Opportunity output fields

| Field | Description |
| --- | --- |
| Marketo GUID | The unique identifier assigned to the opportunity in Marketo. |

### Opportunity role output fields

| Field | Description |
| --- | --- |
| Marketo GUID | The unique identifier assigned to the opportunity role in Marketo. |

### Custom object output fields

| Field | Description |
| --- | --- |
| Marketo GUID | The unique identifier assigned to the custom object in Marketo. |

---
