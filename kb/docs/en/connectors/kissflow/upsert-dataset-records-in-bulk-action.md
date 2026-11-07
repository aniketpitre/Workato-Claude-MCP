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
