---
url: 'https://docs.workato.com/en/connectors/netsuite/delete-custom-records.md'
description: >-
  The Delete custom records batch action allows you to delete custom records in
  batches using their NetSuite internal IDs.
---

# NetSuite SOAP - Delete custom records action (batch)

The **Delete custom records** batch action allows you to delete custom records in batches using their NetSuite internal IDs.

## Input

| Input field | Description |
| --- | --- |
| Custom record | Select the NetSuite record type to delete. |
| Records | Expand this section to specify the custom records to delete from NetSuite. |
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

---
url: >-
  https://docs.workato.com/en/connectors/netsuite/netsuite-export-new-custom-records.md
description: >-
  The Export new custom records trigger in the NetSuite SOAP connector exports
  newly created custom records as a CSV each polling interval for data
  replication.
---

# NetSuite SOAP - Export new custom records trigger

This record exports a CSV of newly created custom records from NetSuite every polling interval. Each field in the record represents a column in the resultant CSV. Use this trigger to replicate records from NetSuite to your data warehouse like Snowflake.

![Export custom records](/assets/export-created-custom-record.DXdluDGr.png)

## Input

| Input field | Description |
| --- | --- |
| Custom object | The NetSuite custom object to export |
| When first started, this recipe should pick up events from | _Optional_ When this recipe starts for the first time, this trigger picks up newly created records from this specified date and time. These records will formatted as a single CSV for the first job of this recipe. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Schedule settings | This allows you to schedule this trigger to run only every set time interval. We recommend exporting records on a longer time interval. |
| Output field configuration | _Optional_ Select the standard fields, custom fields, line item custom fields, that you want to export. |
| When exporting records to form the CSV, fetch them in batches of | _Optional_ The batch size when we export records from NetSuite. Make this batch size smaller if your recipe is facing timeout issues. |

## Output

| Output field | Description |
| --- | --- |
| File content | The CSV file representing the records. |
| Object name | The name of the selected object |
| Object schema | An array representing the schema of the record, allowing you to replicate schema in our Database connectors. |
| Created from | The timestamp from which this trigger started pulling records from. |

---

---
url: >-
  https://docs.workato.com/en/connectors/netsuite/netsuite-export-new-updated-standard-records.md
description: >-
  The Export new/updated standard records trigger in the NetSuite SOAP connector
  exports newly created or updated standard records as a CSV each polling
  interval.
---

# NetSuite SOAP - Export new/updated standard records trigger

This record exports a CSV of newly created or updated standard records from NetSuite every polling interval. Each field in the record represents a column in the resultant CSV. Use this trigger to replicate records from NetSuite to your data warehouse like Snowflake.

![Export standard records](/assets/export-updated-standard-record.B7rIJ8VX.png)

## Input

| Input field | Description |
| --- | --- |
| Standard object | The NetSuite standard object to export |
| When first started, this recipe should pick up events from | _Optional_ When this recipe starts for the first time, this trigger picks up newly created or updated records from this specified date and time. These records will formatted as a single CSV for the first job of this recipe. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Schedule settings | This allows you to schedule this trigger to run only every set time interval. We recommend exporting records on a longer time interval. |
| Output field configuration | _Optional_ Select the standard fields, custom fields, line item custom fields, that you want to export. |
| When exporting records to form the CSV, fetch them in batches of | _Optional_ The batch size when we export records from NetSuite. Make this batch size smaller if your recipe is facing timeout issues. |

## Output

| Output field | Description |
| --- | --- |
| File content | The CSV file representing the records. |
| Object name | The name of the selected object |
| Object schema | An array representing the schema of the record, allowing you to replicate schema in our Database connectors. |
| Created or Updated from | The timestamp from which this trigger started pulling records from. |

---

---
url: >-
  https://docs.workato.com/en/connectors/netsuite/netsuite-export-new-updated-custom-records.md
description: >-
  The Export new/updated custom records trigger in the NetSuite SOAP connector
  exports newly created or updated custom records as a CSV each polling
  interval.
---

# NetSuite SOAP - Export new/updated custom records trigger

This record exports a CSV of newly created or updated custom records from NetSuite every polling interval. Each field in the record represents a column in the resultant CSV. Use this trigger to replicate records from NetSuite to your data warehouse like Snowflake.

![Export custom records](/assets/export-updated-custom-record.CUrwp6CP.png)

## Input

| Input field | Description |
| --- | --- |
| Custom object | The NetSuite custom object to export |
| When first started, this recipe should pick up events from | _Optional_ When this recipe starts for the first time, this trigger picks up newly created or updated records from this specified date and time. These records will formatted as a single CSV for the first job of this recipe. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Schedule settings | This allows you to schedule this trigger to run only every set time interval. We recommend exporting records on a longer time interval. |
| Output field configuration | _Optional_ Select the standard fields, custom fields, line item custom fields, that you want to export. |
| When exporting records to form the CSV, fetch them in batches of | _Optional_ The batch size when we export records from NetSuite. Make this batch size smaller if your recipe is facing timeout issues. |

## Output

| Output field | Description |
| --- | --- |
| File content | The CSV file representing the records. |
| Object name | The name of the selected object |
| Object schema | An array representing the schema of the record, allowing you to replicate schema in our Database connectors. |
| Created or Updated from | The timestamp from which this trigger started pulling records from. |

---

---
url: >-
  https://docs.workato.com/en/connectors/netsuite/netsuite-export-new-standard-records.md
description: >-
  The Export new standard records trigger in the NetSuite SOAP connector exports
  newly created standard records as a CSV each polling interval.
---

# NetSuite SOAP - Export new standard records trigger

This record exports a CSV of newly created standard records from NetSuite every polling interval. Each field in the record represents a column in the resultant CSV. Use this trigger to replicate records from NetSuite to your data warehouse like Snowflake.

![Export standard records](/assets/export-created-standard-record.DdIWRBVw.png)

## Input

| Input field | Description |
| --- | --- |
| Standard object | The NetSuite standard object to export |
| When first started, this recipe should pick up events from | _Optional_ When this recipe starts for the first time, this trigger picks up newly created records from this specified date and time. These records will formatted as a single CSV for the first job of this recipe. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Schedule settings | This allows you to schedule this trigger to run only every set time interval. We recommend exporting records on a longer time interval. |
| Output field configuration | _Optional_ Select the standard fields, custom fields, line item custom fields, that you want to export. |
| When exporting records to form the CSV, fetch them in batches of | _Optional_ The batch size when we export records from NetSuite. Make this batch size smaller if your recipe is facing timeout issues. |

## Output

| Output field | Description |
| --- | --- |
| File content | The CSV file representing the records. |
| Object name | The name of the selected object |
| Object schema | An array representing the schema of the record, allowing you to replicate schema in our Database connectors. |
| Created from | The timestamp from which this trigger started pulling records from. |

---
