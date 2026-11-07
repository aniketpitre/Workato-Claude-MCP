---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-business-central/new-updated-record-batch-trigger.md
description: >-
  Monitor for new or updated records in Microsoft Dynamics Business Central,
  returning results in batches. Triggers when records are created or updated.
---

# Microsoft Dynamics Business Central - New/updated record (batch) trigger

Use the **New/updated record (batch)** trigger to monitor Microsoft Dynamics Business Central for new or updated records and return results in batches. When records are created or updated, the trigger activates with a batch of records. The trigger checks for new events every five minutes.

## Input

| Input field | Description |
| --- | --- |
| Entity name | Select the entity type to monitor from the drop-down menu. Examples include Item, Customer, Vendor, Sales Order, Purchase Order, and more. |
| Batch size | The number of records to return per batch. Defaults to 30 if left blank. Maximum batch size is 100. |
| Company ID | Enter the Company ID to monitor records from. If provided, this overrides the Company ID from the connection settings. Leave blank to use the Company ID specified in the connection. |
| Filter criteria | Additional OData filter expression to further filter the records. For example, `totalTaxAmount lt 96.5`. Refer to the [OData Filter](https://docs.microsoft.com/en-us/odata/concepts/queryoptions-overview#filter) documentation for filter syntax help. Don't include `systemModifiedAt` or `lastModifiedDateTime` as part of the filter, because these are automatically handled by the trigger. |
| Expand | Specify additional related objects to be returned in the output. For example, enter `purchaseOrderLines` to include purchase order lines in the results. |
| When first started, this recipe should pick up events from | When you start the recipe for the first time, it picks up trigger events from this specified date and time. Leave empty to get records created or updated one hour ago. |

## Output

| Output field | Description |
| --- | --- |
| Records | An array of records that were created or updated. Each record includes the complete record data with all fields returned by Business Central, the entity tag (ETag) for the record, the unique identifier (ID) of the record, and the date and time when the record was last modified. For Company entities, the last modified field is named **System modified at**. |
