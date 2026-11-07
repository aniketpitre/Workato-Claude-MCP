---
url: >-
  https://docs.workato.com/en/connectors/databricks/upload-file-to-internal-stage.md
description: >-
  The Upload file to volume action uploads a file to a specified Databricks
  volume.
---

# Databricks – Upload file to volume action

The **Upload file to volume** action uploads a file to a specified Databricks volume.

Use this action to stage large datasets in a Databricks volume before you load them into physical tables. After you upload the data, run the **Run custom SQL** action to execute SQL commands that load the staged data into Databricks tables.

## Input

| Input field | Description |
| --- | --- |
| Source Type | Select how to provide the file. Choose **File Contents** to pass binary file data from a previous step. Choose **Workato Files path** to reference a file stored in Workato FileStorage. |
| File contents | Provide the binary file data to upload. This field appears when you select **File Contents** as the **Source Type**. Map this field from a previous step that outputs a file object. |
| Workato FileStorage path | Enter the path to the file in Workato FileStorage. For example, `/folder/subfolder/filename.csv`. Use a datapill to reference a dynamic path from a previous step. This field appears when you select **Workato FileStorage path** as the **Source Type**. |
| Volume | Select the Databricks Unity Catalog volume where the file is stored. |
| Overwrite | Choose to overwrite the file if another file with the same name already exists in the target location. |

## Output

| Output field | Description |
| --- | --- |
| Upload Status | The result of the upload request. |
| Target File Path | The full path of the uploaded file in the Databricks volume. |
| Target File Size (Bytes) | The size of the uploaded file in bytes. |
