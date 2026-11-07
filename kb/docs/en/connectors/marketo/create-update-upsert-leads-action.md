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
