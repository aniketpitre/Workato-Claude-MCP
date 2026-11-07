---
url: 'https://docs.workato.com/en/features/filestorage/append-to-file-action.md'
description: >-
  Reference for the Workato FileStorage Append to file action, including CSV
  schema, header, delimiter, and encoding input and output fields.
---

# Workato FileStorage - Append to file action

This action appends content to an existing file in [Workato FileStorage](/en/features/workato-filestorage). If a file does not exist at the provided path, the action creates the file and adds the content to it.

Like the [Create file](/en/features/filestorage/create-file-action) action, this action can be paired with streaming or non-streaming download actions, or with bulk actions and triggers, and so on. This is useful for working with CSV or JSON data, such as when you have to fetch the contents from the source at a regular frequency or in batches, and store it in a single intermediary file that can be streamed to the destination.

![Append to file in FileStorage action](/assets/filestorage-append-to-file.DODR4LWj.png) _Append to file in FileStorage action_

> **HOW TO USE THE APPEND ACTION EFFECTIVELY**
> 
> Because the Append file action creates a new file if no file exists at the provided path, you can use this action to create a file during a recipe's first job and append data to the same file in later jobs. You do not need to use a separate [Create file](/en/features/filestorage/create-file-action) action in the recipe. This can simplify recipe design.

> **FILE AND DIRECTORY ACCESS**
> 
> Currently, all users in a workspace can access all FileStorage files and directories in the workspace when they use the [FileStorage connector](/en/features/filestorage/filestorage-connector). Workato does not restrict access based on role unless the files are accessed from the [FileStorage UI](/en/features/filestorage/filestorage-console#rbac).

## Input

| Input fields | Description |
| --- | --- |
| Append CSV content | Select **Yes** if you are creating a CSV file with column schema or appending data to an existing CSV file that is stored with column schema in FileStorage. Defaults to **No** if not specified. |
| Select file/File path | Choose a file or enter the full path of the file where the contents should be appended. If the file does not exist at the provided path at recipe run time, Workato creates a new file. If **Append CSV content** is set to **Yes**, the drop-down only displays existing CSV files stored with column schema. To append to an existing CSV file in FileStorage, you must have created it using the [Create file](/en/features/filestorage/create-file-action) action or a previous **Append to file** action. |
| Content to append | Use a datapill from an upstream action, such as a download or bulk export action, to append data to the selected file. You can also directly paste the content to be appended. |
| CSV column schema setup | Required if **Append CSV content** is set to **Yes**. Select how to define the column schema. Select **Auto infer** to automatically detect column names and data types from the incoming header row and data. Workato relaxes column types if it encounters a data type mismatch when it appends data to the file. This behavior doesn't apply when the action retrieves data from the file. Select **Set schema** to manually define column names and data types. Schema validation is strict when the action retrieves the file contents using the **Get lines from CSV file** action. To avoid validation errors, ensure the sample data includes all expected data types, or set columns to the most relaxed type, such as string. Defaults to **Auto infer** if not specified. |
| Column schema | Required if you set **CSV column schema setup** to **Set schema**. Select an option to describe the data types of the columns in the appended data: **Add column name**: Manually add a single column at a time.; **Use a sample CSV file**: Input all column names at one time by uploading a CSV file from your computer or by pasting up to 10 rows of a CSV sample, including a required header row. The recipe returns an error if the appended data types defined here do not match the schema of the existing file. |
| Contains header row | Select **Yes** if the CSV content to be appended has a header row. Defaults to **No** if not specified. This optional field is only displayed if **Append CSV content** is set to **Yes**. |
| Add header at file creation | Choose whether to add the header row when the **Append to file** action _creates a new file_: **Yes:** Add the header row to the CSV file., **No:** Remove the header row from the CSV file. Note that the header row is removed when the **Append to file** action _appends to an existing_ file. Defaults to **No** if not specified. This optional field is only displayed if **Contains header row** is set to **Yes**. |
| Column delimiter | Choose the character that separates the column values in the CSV content to be appended. Defaults to **Comma** (`,`) if not specified. This optional field is only displayed if **Append CSV content** is set to **Yes**. |
| Quote character | Choose whether the quotation marks used as escape characters are single or double in the CSV content to be appended. Defaults to **Double** (`"`) if not specified. This optional field is only displayed if **Append CSV content** is set to **Yes**. |
| File encoding | Select the encoding of the content to be appended. Defaults to **UTF-8**. This optional field is only displayed if **Append CSV content** is set to **Yes**. |

## Output

| Output fields | Description |
| --- | --- |
| File path | Complete path of the file that was appended to or created. |
| Appended size | The size of the file that was appended to or created, in bytes. |

---
