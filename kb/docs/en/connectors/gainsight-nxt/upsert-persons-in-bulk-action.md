---
url: >-
  https://docs.workato.com/en/connectors/gainsight-nxt/upsert-persons-in-bulk-action.md
description: >-
  The Upsert persons in bulk action upserts up to 50 records in the Person
  object in Gainsight NXT.
---

# Gainsight NXT - Upsert persons in bulk action

The **Upsert persons in bulk** action upserts up to 50 records in the Person object in `Gainsight NXT`. Multiple person records are upserted asynchronously and may take up to 30 minutes to complete. You can apply an import lookup configuration to populate GSIDs into a field by referencing it from another object.

> **TRACK THE UPSERT STATUS**
> 
> This action runs asynchronously and returns a status ID. Use the [Get upsert request status](/en/connectors/gainsight-nxt/get-upsert-request-status-action) action with this status ID to retrieve the processing status and results.

## Input

| Input field | Description |
| --- | --- |
| Records | A list of up to 50 person records to upsert. Each record accepts the fields of the **Person** object, such as `Email (required)`, `First name`, `Last name`, `Full name`, `Location`, `Timezone`, and `associated Companies`. |

Refer to the [Gainsight NXT API](https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs/Company_and_Relationship_API/Company_API_Documentation) documentation for additional input fields.

## Output

| Field | Description |
| --- | --- |
| Status ID | The ID of the asynchronous upsert request. Use this ID with the **Get upsert request status** action to track the request. |
