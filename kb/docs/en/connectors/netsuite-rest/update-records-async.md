---
url: 'https://docs.workato.com/en/connectors/netsuite-rest/update-records-async.md'
description: >-
  The Update records batch (async) action updates multiple records
  asynchronously in NetSuite REST.
---

# NetSuite REST - Update records (async) batch action

The **Update records (async)** action updates multiple records in NetSuite REST asynchronously. All records submit as a single batch async request, and NetSuite returns one job ID for the entire batch.

Use this action to process large batches without blocking the recipe. The maximum number of records per batch is 100.

## Input

| Input field | Description |
| --- | --- |
| Record | Select the NetSuite record to update. Only [REST Web Services supported records](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/chapter_1558962745.html#Web-Services-Supported-Records) appear in the list. Enable custom records if required. |
| Record data | Provide the list of records to update in NetSuite. |

Additional fields appear based on the **Record** you select. The structure of **Record data**, **Record data source list**, and **Record data fields** changes dynamically to match the **Record** you select.

## Output

| Output field | Description |
| --- | --- |
| Async job ID | The identifier for the batch async job. Pass this value to the [Get async job result action](/en/connectors/netsuite-rest/get-async-job) to retrieve the job status and per-record results after NetSuite processes the batch. |
| Job enqueued at | The timestamp when NetSuite enqueued the batch job for processing. |

---

---
url: >-
  https://docs.workato.com/en/connectors/netsuite-rest/upsert-custom-record-action.md
description: >-
  The Upsert custom record action in the NetSuite REST connector lets you upsert
  a custom record in NetSuite.
---

# NetSuite REST - Upsert custom record action

The **Upsert custom record** action allows you to upsert a custom record in NetSuite REST.

Refer to the NetSuite [Prerequisites and Setup for REST Web Services](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/article_5085602973.html) guide for more information.

## Input

| Input field | Description |
| --- | --- |
| Custom record | Select a NetSuite custom record type, or toggle to enter a custom value. The list populates from the custom record types located in your account at **Customization > Records > Record Types**. |
| External ID | The external ID of the record to upsert. |

Additional optional fields appear based on the **Custom record** type you select.

## Output

| Output field | Description |
| --- | --- |
| Location | The location ID of the record upserted. |
| Internal ID | The internal ID of the record upserted. |

---
