---
url: 'https://docs.workato.com/en/features/filestorage/new-csv-file-trigger.md'
description: >-
  Trigger Workato recipes in real time when a new CSV file matching a column
  schema is created in Workato FileStorage, returning rows in batches.
---

# Workato FileStorage - New CSV file trigger (batch)

This trigger is initiated immediately, in real time, when a new CSV file matching a given column schema is created in the [Workato FileStorage](/en/features/workato-filestorage) directory being monitored. The trigger returns segregated rows and columns from the CSV file in [batches](/en/features/batch-processing). To return a complete CSV file as a stream instead, use the [New file in Workato FileStorage](/en/features/filestorage/new-file-trigger) trigger.

You can use trigger conditions to filter trigger events based on file metadata such as name, path, or extension.

Note that the files must be created using the [Create file](/en/features/filestorage/create-file-action) action with **Create CSV file** set to **Yes**, or the [Append to file](/en/features/filestorage/append-to-file-action) action with **Append CSV content** set to **Yes**.

![New CSV file in FileStorage trigger](/assets/filestorage-new-csv-file.MCwM9H0d.png) _New CSV file in FileStorage trigger_

> **FILE AND DIRECTORY ACCESS**
> 
> Currently, all users in a workspace can access all FileStorage files and directories in the workspace when they use the [FileStorage connector](/en/features/filestorage/filestorage-connector). Workato does not restrict access based on role unless the files are accessed from the [FileStorage UI](/en/features/filestorage/filestorage-console#rbac).

## Input

| Field | Description |
| --- | --- |
| When first started, this recipe should pick up events from | When you start the recipe for the first time, it retrieves files created after the specified date and time. Events more than a week old are not picked up. Leave this field empty to retrieve files created in the last hour. After you test or run the recipe, you cannot change this value. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Directory path to monitor | Choose or enter the directory path to monitor (for example, `directory1/directory2/`). |
| Include subdirectories? | Whether to monitor subdirectories within the specified directory path. By default, the trigger does not monitor subdirectories. |
| Batch size | Number of CSV rows to retrieve per job. Instead of reading records one by one, Workato reads a batch of CSV records at the same time to increase throughput. Refer to [Batch processing](/en/features/batch-processing) for more information. Defaults to `1000` if not specified. Maximum is `50000`. If the records are very large, the trigger automatically reduces the number of records retrieved to optimize processing. |
| CSV column schema | Select an option to provide a template column schema so Workato can match and retrieve records from new CSV files in batches: **Provide with sample file**: Match the schema of a file you choose in Workato FileStorage. When you select this option, you can choose the file with the **Sample CSV file** setting that appears.; **Provide manually**: Match a schema you define manually. When you select this option, you can define the schema with the **Column schema** setting that appears. |
| Sample CSV file | Required if you set **CSV column schema** to **Provide with sample file**. Select a sample CSV file in Workato FileStorage from the drop-down menu. This trigger only processes files that match the schema in the sample, with permitted relaxations. To use a file as a sample CSV, you must create it using the [Create file](/en/features/filestorage/create-file-action) or [Append to file](/en/features/filestorage/append-to-file-action) actions. |
| Column schema | Required if you set **CSV column schema** to **Provide manually**. Select an option to describe the schema of the columns in the CSV files to be processed: **Add column name**: Manually add a single column at a time.; **Use a sample CSV file**: Input all column names at one time by uploading a CSV file from your computer or by pasting up to 10 rows of a CSV sample, including a required header row. This trigger only processes files that match the described schema, with permitted relaxations. |
| Columns to retrieve | Select the CSV columns that you plan to use in your recipe. If this field is left blank, Workato retrieves all columns. Otherwise, Workato retrieves only the columns you select. |
| Skip files with schema mismatches | Choose the behavior when the trigger encounters a CSV file that doesn't match the schema you defined: **Yes**: Skip processing a file that doesn't match the schema., **No**: Explicitly throw an error when a file doesn't match the schema. Defaults to **Yes** if not specified. |

## Output

| Field | Description |
| --- | --- |
| File name | Name of the new CSV file. |
| File path | Path of the new CSV file. |
| Batch size | Number of CSV rows in the processed batch. |
| Batch number | ID of the processed batch. |
| File size (bytes) | Size of the new CSV file in bytes. |
| First batch | Whether the batch was the first one processed. |
| Last batch | Whether the batch was the final one processed. |
| Rows | A list of rows from the new CSV file, in addition to **List size** and **List index**. Data from the CSV is shown under the **Columns** object. |

---

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

---
