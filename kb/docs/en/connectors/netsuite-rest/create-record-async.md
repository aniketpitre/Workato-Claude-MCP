---
url: 'https://docs.workato.com/en/connectors/netsuite-rest/create-record-async.md'
description: >-
  The Create records batch (async) action creates multiple records
  asynchronously in NetSuite REST.
---

# NetSuite REST - Create records (async) batch action

The **Create records batch (async)** action creates multiple records in NetSuite REST asynchronously. All records submit as a single batch async request, and NetSuite returns one job ID for the entire batch.

Use this action to process large batches without blocking the recipe. The maximum number of records per batch is 100.

## Input

| Input field | Description |
| --- | --- |
| Record | Select the NetSuite record type to create. Only [REST Web Services supported records](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/chapter_1558962745.html#Web-Services-Supported-Records) appear in the list. Enable custom records if required. |
| Record data | Provide the list of records to write to NetSuite. This field changes based on the selected **Record**. |

Additional fields appear based on the **Record** you select. The structure of **Record data**, **Record data source list**, and **Record data fields** changes dynamically to match the **Record** you select.

## Output

| Output field | Description |
| --- | --- |
| Async job ID | The identifier for the batch async job. Pass this value to the [Get async job result action](/en/connectors/netsuite-rest/get-async-job) to retrieve the job status and per-record results after NetSuite processes the batch. |
| Job enqueued at | The timestamp when NetSuite enqueued the batch job for processing. |

---

---
url: >-
  https://docs.workato.com/en/connectors/netsuite-rest/delete-custom-record-action.md
description: >-
  The Delete custom record action in the NetSuite REST connector lets you remove
  a custom record from NetSuite.
---

# NetSuite REST - Delete custom record action

The **Delete custom record** action allows you to remove a custom record from NetSuite REST.

Refer to the NetSuite [Prerequisites and Setup for REST Web Services](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/article_5085602973.html) guide for more information.

## Input

| Input field | Description |
| --- | --- |
| Custom record | Select a NetSuite custom record type, or toggle to enter a custom value. The list populates from the custom record types located in your account at **Customization > Records > Record Types**. |
| Internal ID | The internal ID of the record to delete. |

## Output

There is no output for this action.

---
