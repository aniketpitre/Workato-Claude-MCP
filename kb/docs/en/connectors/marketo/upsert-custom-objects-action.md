---
url: 'https://docs.workato.com/en/connectors/marketo/upsert-custom-objects-action.md'
description: >-
  The Upsert custom objects action in the Marketo connector lets you create or
  update up to 300 custom object records by a lookup field you specify.
---

# Marketo - Upsert custom objects action

This action creates or updates custom objects in Marketo.

It searches for custom objects in Marketo by a specified lookup field. If found, this action updates the custom object with the data provided. If not found, this action creates new custom objects with the data provided. It accepts a list of maximum 300 custom object records. This action fails if more than 300 custom object records are provided.

## Input

| Field | Description |
| --- | --- |
| Custom object / Custom object name | Select a custom object name from the list, or enter a custom object name with the suffix `_c`. |

After selecting or entering the custom object name, input fields dynamically generate based on the fields associated with the custom object.

## Output

| Field | Description |
| --- | --- |
| Request ID | The unique ID of the operation request. |
| Number of records processed | The total number of records processed. |
| Number of records created | The total number of records created during the operation. |
| Number of records updated | The total number of records updated during the operation. |
| Number of records skipped | The total number of records skipped during the operation. |
| Custom objects created | An array of custom objects that were created. |
| Created at (custom objects created) | The timestamp when each custom object was created. |
| Marketo GUID (custom objects created) | The unique Marketo identifier for each created custom object. |
| Updated at (custom objects created) | The timestamp when each custom object was last updated. |
| Custom objects updated | An array of custom objects that were updated. |
| Created at (custom objects updated) | The timestamp when each custom object was created. |
| Marketo GUID (custom objects updated) | The unique Marketo identifier for each updated custom object. |
| Updated at (custom objects updated) | The timestamp when each custom object was last updated. |
| Custom objects skipped | An array of custom objects that were skipped. |
| Created at (custom objects skipped) | The timestamp when each skipped custom object was created. |
| Marketo GUID (custom objects skipped) | The unique Marketo identifier for each skipped custom object. |
| Updated at (custom objects skipped) | The timestamp when each skipped custom object was last updated. |
| Error (custom objects skipped) | An error object containing details about why custom objects were skipped. |
| Code (error) | The error code associated with any failure in the operation. |
| Message (error) | The error message providing details about the failure. |

---
