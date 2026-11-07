---
url: 'https://docs.workato.com/en/connectors/netsuite/delete-standard-records.md'
description: >-
  The Delete standard records batch action allows you to delete standard records
  in batches using their NetSuite internal IDs.
---

# NetSuite SOAP - Delete standard records action (batch)

The **Delete standard records** batch action allows you to delete standard records in batches using their NetSuite internal IDs.

## Input

| Input field | Description |
| --- | --- |
| Standard record | Select the NetSuite standard record type to delete. |
| Records | Expand this section to specify the standard records to delete from NetSuite. |
| Records source list (records) | Input a list datapill that contains the records to delete. [Learn more about list input](/en/features/list-management#list-batch-action). |
| Record ID (records) | Provide the NetSuite internal ID of the record to delete. |

## Output

| Output field | Description |
| --- | --- |
| Successful deletions | A list of internal IDs of successfully deleted records. |
| Internal ID (successful deletions) | The internal ID of the deleted record. |
| Failed deletions | A list of internal IDs of records that couldn't be deleted. |
| Internal ID (failed deletions) | The internal ID of the record that couldn't be deleted. |
| Error message (failed deletions) | An error message that explains why the record deletion failed. |

---
