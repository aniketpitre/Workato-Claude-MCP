---
url: >-
  https://docs.workato.com/en/features/filestorage/new-csv-lines-in-file-trigger.md
description: >-
  Trigger Workato recipes in real time when new lines are added to a CSV file in
  Workato FileStorage, returning the rows in batches.
---

# Workato FileStorage - New lines in CSV file trigger (batch)

This trigger is initiated immediately, in real time, when new lines are added to an existing CSV file in [Workato FileStorage](/en/features/workato-filestorage). The trigger returns rows and columns from the CSV file in [batches](/en/features/batch-processing).

All existing lines in the file will be processed when the recipe starts. Updating the data in the file externally without using the connector actions may cause the trigger to stop tracking the new lines correctly.

![New lines in CSV file in FileStorage trigger](/assets/filestorage-new-csv-lines-in-file.Bx3vuoKo.png) _New lines in CSV file in FileStorage trigger_

> **FILE AND DIRECTORY ACCESS**
> 
> Currently, all users in a workspace can access all FileStorage files and directories in the workspace when they use the [FileStorage connector](/en/features/filestorage/filestorage-connector). Workato does not restrict access based on role unless the files are accessed from the [FileStorage UI](/en/features/filestorage/filestorage-console#rbac).

## Input

| Field | Description |
| --- | --- |
| File to monitor | Choose a CSV file to monitor from the drop-down menu or enter the file path directly (for example, `samplepath/filename.csv`). If you choose a file from the drop-down menu, only CSV files stored with column schema are displayed. Note that for a CSV file to be identified and picked up by this trigger, it must be stored using the [Create file](/en/features/filestorage/create-file-action) action with the **Create CSV file** option set to **Yes**, or the [Append to file](/en/features/filestorage/append-to-file-action) action with **Append CSV content** set to **Yes**. |
| Batch size | Number of CSV rows to retrieve per job. Instead of reading records one by one, Workato reads a batch of CSV records at the same time to increase throughput. Refer to [Batch processing](/en/features/batch-processing) for more information. Defaults to `1000` if not specified. Maximum is `50000`. If the records are very large, the trigger automatically reduces the number of records retrieved to optimize processing. |
| Columns to retrieve | Select the CSV columns that you plan to use in your recipe. If this field is left blank, Workato retrieves all columns. Otherwise, Workato retrieves only the columns you select. |

## Output

| Field | Description |
| --- | --- |
| File name | Name of the new CSV file. |
| File path | Path of the new CSV file. |
| Batch size | Number of CSV rows in the processed batch. |
| Batch number | ID of the processed batch. |
| First batch | Whether the batch was the first one processed. |
| Rows | A list of new rows from the CSV file, in addition to **List size** and **List index**. Data from the CSV is shown under the **Columns** object. |
