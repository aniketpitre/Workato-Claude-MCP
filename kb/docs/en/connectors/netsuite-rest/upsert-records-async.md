---
url: 'https://docs.workato.com/en/connectors/netsuite-rest/upsert-records-async.md'
description: >-
  The Upsert records batch (async) action creates or updates multiple records
  asynchronously in NetSuite REST.
---

# NetSuite REST - Upsert records batch (async) action

The **Upsert records batch (async)** action creates or updates multiple records in NetSuite REST asynchronously. All records submit as a single batch async request, and NetSuite returns one job ID for the entire batch.

Use this action to process large batches without blocking the recipe. The maximum number of records per batch is 100.

## Input

| Input field | Description |
| --- | --- |
| Record | Select the NetSuite record to upsert. Only [REST Web Services supported records](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/chapter_1558962745.html#Web-Services-Supported-Records) appear in the list. Enable custom records if required. |
| Record data | Provide the list of records to create or update in NetSuite. |

Additional fields appear based on the **Record** you select. The structure of **Record data**, **Record data source list**, and **Record data fields** changes dynamically to match the **Record** you select.

## Output

| Output field | Description |
| --- | --- |
| Async job ID | The identifier for the batch async job. Pass this value to the [Get async job result action](/en/connectors/netsuite-rest/get-async-job) to retrieve the job status and per-record results after NetSuite processes the batch. |
| Job enqueued at | The timestamp when NetSuite enqueued the batch job for processing. |

---
