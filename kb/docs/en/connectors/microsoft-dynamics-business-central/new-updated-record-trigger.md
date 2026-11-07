---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-business-central/new-updated-record-trigger.md
description: >-
  Monitor for new or updated records in Microsoft Dynamics Business Central.
  Triggers when a record is created or updated.
---

# Microsoft Dynamics Business Central - New/updated record trigger

Use the **New/updated record** trigger to monitor Microsoft Dynamics Business Central for new or updated records. When a record is created or updated, the trigger activates and provides the complete record information. The trigger checks for new events every five minutes.

## Input

| Input field | Description |
| --- | --- |
| Entity name | Select the entity type to monitor from the drop-down menu. Examples include Item, Customer, Vendor, Sales Order, Purchase Order, and more. |
| Company ID | Enter a Company ID to monitor records from. If provided, this overrides the Company ID from the connection settings. Leave blank to use the Company ID specified in the connection. |
| Filter criteria | Additional OData filter expression to further filter the records. For example, `totalTaxAmount lt 96.5`. Refer to the [OData Filter](https://docs.microsoft.com/en-us/odata/concepts/queryoptions-overview#filter) documentation for filter syntax help. Don't include `systemModifiedAt` or `lastModifiedDateTime` as part of the filter, because these are automatically handled by the trigger. |
| Expand | Specify additional related objects to be returned in the output. For example, enter `purchaseOrderLines` to include purchase order lines in the results. |
| When first started, this recipe should pick up events from | When you start the recipe for the first time, it picks up trigger events from this specified date and time. Leave empty to get records created or updated one hour ago. |

## Output

| Output field | Description |
| --- | --- |
| Record data | The complete record data that was created or updated, including all fields returned by Business Central. The structure depends on the entity type selected. |
| ETag | The entity tag (ETag) for the record. |
| ID | The unique identifier of the record. |
| Last modified date time | The date and time when the record was last modified. For Company entities, this field is named **System modified at**. |
