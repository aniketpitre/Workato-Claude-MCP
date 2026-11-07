---
url: 'https://docs.workato.com/en/connectors/reckon/new-updated-record-trigger.md'
description: >-
  The New/updated record trigger initiates a recipe when a record is created or
  updated in Reckon.
---

# Reckon - New/updated record trigger

The **New/updated record** trigger initiates a recipe when a selected object is created or updated in Reckon.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the Reckon object to monitor for changes. |
| Book ID | Enter the Reckon One Book ID. You can find it in the Reckon One URL. For example, `https://app.reckonone.com/{BookID}/Core`. |
| Since | Optional. Specify a timestamp to begin fetching records from. Defaults to 1 hour prior if left empty. |
| Select | Optional. Enter a comma-separated list of fields to return. |
| Filter | Optional. Enter a filter expression to narrow the matched results. |

Additional input fields may appear depending on the selected object type.

## Output

The output varies depending on the selected object type. For example, if you select **Invoices** as the **Object**, output fields include the following:

| Output field | Description |
| --- | --- |
| ID | Unique identifier of the invoice. |
| Invoice number | Reference number for the invoice. |
| Customer | Customer associated with the invoice. |
| Billing address | Billing address for the invoice. |
| Shipping address | Shipping address for the invoice. |
| Invoice date | Date when the invoice was issued. |
| Due date | Payment due date. |
| Total amount | Total invoice amount. |

---
