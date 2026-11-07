---
url: 'https://docs.workato.com/en/connectors/gainsight-nxt/upsert-person-action.md'
description: The Upsert person action upserts a single person record in Gainsight NXT.
---

# Gainsight NXT - Upsert person action

The **Upsert person** action upserts a single person record in `Gainsight NXT`. You can apply an import lookup configuration to populate GSIDs into a field by referencing it from another object.

## Input

| Input field | Description |
| --- | --- |
| Email | Enter the email address of the person. This field is required. |
| First name | Enter the first name of the person. |
| Last name | Enter the last name of the person. |
| Middle name | Enter the middle name of the person. |

Refer to the [Gainsight NXT API](https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs/Company_and_Relationship_API/Company_API_Documentation) documentation for additional input fields.

## Output

This action has many output fields. Refer to the [Gainsight NXT API](https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs/Company_and_Relationship_API/Company_API_Documentation) documentation for a complete list of output fields.

---

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

---

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

---
