---
url: 'https://docs.workato.com/en/connectors/kissflow/upload-attachment-action.md'
description: >-
  The Upload attachment action enables you to upload an attachment to a record
  in Kissflow.
---

# Kissflow - Upload attachment action

The **Upload attachment** action enables you to upload an attachment to a record in Kissflow.

## Input

| Input field | Description |
| --- | --- |
| Object | Specify the object to upload an attachment to its record. Fields load dynamically based on the object you select. |

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the datatree to subsequent steps.

---

---
url: >-
  https://docs.workato.com/en/connectors/kissflow/upsert-dataset-records-in-batch-action.md
description: >-
  The Upsert dataset records in batch action enables you to create or update
  dataset records in batches in Kissflow.
---

# Kissflow - Upsert dataset records in batch action

The **Upsert dataset records in batch** action enables you to create or update dataset records in batches in Kissflow.

## Input

| Input field | Description |
| --- | --- |
| Dataset ID | The unique identifier for each dataset. |
| Batch size | The number of records in a single batch. The maximum is 300, and the default is 100. |
| Data | An array of dataset records to upsert. Includes the record **ID** and custom input fields specific to the dataset. |

## Output

| Output field | Description |
| --- | --- |
| Records ingested | An array of dataset records that were created or updated successfully. It includes metadata fields such as **ID,** **flow name,** **flow type, created and updated** timestamps, and custom output fields specific to the dataset. |
| Records failed | An array of bulk operations that failed during execution. Includes the error code and the corresponding array of records. |
| Success | Returns **false** if any batch operation fails; otherwise, returns **true**. |

---

---
url: >-
  https://docs.workato.com/en/connectors/kissflow/upsert-dataset-records-in-bulk-action.md
description: >-
  The Upsert dataset records in bulk action enables you to create or update
  dataset records in bulk in Kissflow.
---

# Kissflow - Upsert dataset records in bulk action

The **Upsert dataset records in bulk** action enables you to create or update dataset records in bulk in Kissflow.

## Input

| Input field | Description |
| --- | --- |
| Dataset ID | The unique identifier for each dataset. |
| Data | An array of dataset records to upsert. Includes the record **ID** and custom input fields specific to the dataset. |

## Output

| Output field | Description |
| --- | --- |
| Data | An array of dataset records that were created or updated successfully. It includes metadata fields such as **ID,** **flow name,** **flow type, created and updated** timestamps, and custom output fields specific to the dataset. |

---
