---
url: >-
  https://docs.workato.com/en/connectors/gainsight-nxt/get-upsert-request-status-action.md
description: >-
  The Get upsert request status action retrieves the processing status of a bulk
  person upsert request in Gainsight NXT by status ID.
---

# Gainsight NXT - Get upsert request status action

The **Get upsert request status** action retrieves the processing status of the [Upsert persons in bulk](/en/connectors/gainsight-nxt/upsert-persons-in-bulk-action) action. The status displays as `INIT` or `INPROGRESS` until the upsert completes. Output updates automatically when the upsert process is `COMPLETED`. Successfully upserted records are returned in the **People** output list. Error details for any failed records are returned in the **Error details** output list.

## Input

| Input field | Description |
| --- | --- |
| Status ID | Enter the status ID returned by the **Upsert persons in bulk** action. |

## Output

| Field | Description |
| --- | --- |
| Status | The processing status of the request, for example, `INIT`, `INPROGRESS`, or `COMPLETED`. |
| Count | The number of records processed. |
| Error details | A list of errors for records that failed to upsert. Each entry includes the row number and the field name, values, and error messages and codes for the failure. |
| People | A list of the successfully upserted person records. |
