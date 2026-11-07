---
url: 'https://docs.workato.com/en/features/filestorage/create-file-action.md'
description: >-
  Reference for the Workato FileStorage Create file action, including file
  contents, CSV schema, and overwrite input and output fields.
---

# Workato FileStorage - Create file action

This action creates a new file in [Workato FileStorage](/en/features/workato-filestorage) by uploading the file contents provided. The action is compatible with both streaming and non-streaming actions.

![Create file in FileStorage action](/assets/filestorage-create-file.D_WYcjRs.png) _Create file in FileStorage action_

> **FILE AND DIRECTORY ACCESS**
> 
> Currently, all users in a workspace can access all FileStorage files and directories in the workspace when they use the [FileStorage connector](/en/features/filestorage/filestorage-connector). Workato does not restrict access based on role unless the files are accessed from the [FileStorage UI](/en/features/filestorage/filestorage-console#rbac).

## Input

| Input fields | Description |
| --- | --- |
| File name | Enter the name of the file you plan to create. |
| File path | Choose a directory or enter the directory path where you plan to create the file in FileStorage. If the path does not exist, Workato returns an error. |
| File contents | Use a datapill from an upstream action, such as a download or bulk export action, to specify the new file's contents. You can also directly paste the contents. |
| Create CSV file | Select **Yes** if the new file should be stored as CSV and should match a specific column schema. You must select this option to fetch CSV file data in batches using FileStorage triggers. |
| CSV column schema setup | Required if **Create CSV file** is set to **Yes**. Choose how to define the column schema. Select **Auto infer** to automatically detect column names and data types from the incoming header row and data. Workato relaxes column types if it encounters a data type mismatch when it creates the file. This behavior doesn't apply when the action retrieves data from the file. Select **Set schema** to manually define column names and data types. Schema validation is strict when the action retrieves the file contents using the **Get lines from CSV file** action. To avoid validation errors, ensure the sample data includes all expected data types, or set columns to the most relaxed type, such as string. Defaults to **Auto infer** if not specified. |
| Column schema | Required if you set **CSV column schema setup** to **Set schema**. Select an option to describe the data types of the columns in the new file: **Add column name**: Manually add a single column at a time.; **Use a sample CSV file**: Input all column names at one time by uploading a CSV file from your computer or by pasting up to 10 rows of a CSV sample, including a required header row. |
| Contains header row | Select **Yes** if the incoming CSV content has a header row. Defaults to **Yes** if not specified. This optional field is only displayed if **Create CSV file** is set to **Yes**. |
| Column delimiter | Choose the character that separates the column values in the incoming CSV content. Defaults to **Comma** (`,`) if not specified. This optional field is only displayed if **Create CSV file** is set to **Yes**. |
| Quote character | Choose whether the quotation marks used as escape characters are single or double in the incoming CSV content. Defaults to **Double** (`"`) if not specified. This optional field is only displayed if **Create CSV file** is set to **Yes**. |
| File encoding | Select the encoding of the incoming CSV content. Defaults to **UTF-8**. This optional field is only displayed if **Create CSV file** is set to **Yes**. |
| Overwrite existing file | Choose **Yes** to overwrite the file if it already exists in the specified directory. Defaults to **No**. |

## Output

| Output fields | Description |
| --- | --- |
| File name | The name of the created file. |
| File path | Complete path of the created file. |
| File size (bytes) | The size of the created file in bytes. |

---
