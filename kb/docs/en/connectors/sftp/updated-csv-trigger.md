---
url: 'https://docs.workato.com/en/connectors/sftp/updated-csv-trigger.md'
description: >-
  The New/updated CSV file in directory trigger in the SFTP connector fires when
  a CSV file is created or updated in a directory, processing rows in batches.
---

# SFTP - New/updated CSV file in directory trigger (batch)

This trigger is activated when a CSV file is created or updated in a specified directory. Workato collates CSV lines and processes them in batches. Each batch is processed as a job. The default batch size is `100` and max batch size is `1000`.

> **PREVENTING TRIGGER ERRORS**
> 
> This trigger monitors the entire folder and parses the CSV content in the new or updated file before validating the trigger conditions. Therefore, adding a file with a different CSV format (header names, column count) from one provided in the trigger might lead to errors in the job. To prevent trigger errors, ensure that only the files with the CSV format that matches the trigger conditions are added to the folder.

![New/updated CSV in directory trigger](/assets/updated-csv-trigger.DmI91Mg8.png)_New/updated CSV in directory trigger_

## Input

| Input field | Description |
| --- | --- |
| Directory | Select the folder that you want to track. You can choose from the drop-down menu or enter the folder path directly. Files in this directory are processed from oldest to newest, based on when they were modified. |
| Column names | Enter CSV headers. You can enter them manually or provide a sample CSV file. |
| Column delimiter | Select the character that separates columns in the CSV file. The default is **,** (comma). |
| Contains header row? | Set to **Yes** if the first CSV row is a header row containing column names. |
| Batch size | Number of CSV rows to process per batch. The default batch size is `100` and the max batch size is `1000`. |
| Expected encoding | Expected encoding type of the CSV files. Default is **UTF-8** and typically does not need to be changed. |
| Ignore missing files? | Set to **Yes** to ignore or skip files that are currently unavailable. This is useful if your recipe involves moving files to a different location after they are processed. Default is **No**. |
| Keep track of columns by | Configure this if the CSV file does not have a fixed column order or column names. Default is **Column order**. If **Column order** is set: Your CSV file must have a fixed column order for the recipe to work. Column names don't need to be fixed., If **Column name** is set: Your CSV file must have fixed column names for the recipe to work. Column order doesn't need to be fixed. |
| Quote character | The character used to quote CSV cell values. Select **None** if no quote character is used. Default is **Double quote**. |

## Output

The output of this trigger is a **list of records**, with each record containing the schema as defined in the **CSV column names**. Because this is a list datapill, you must use a [repeat action](/en/recipes/steps#repeat-step) to iterate through each record.

| Output field | Description |
| --- | --- |
| Filename | The filename of the CSV. |
| First batch | Whether this is the first batch of CSV rows. |
| Last batch | Whether this is the last batch of CSV rows. |
| Lines | A [list datapill](/en/features/list-management) representing the list of records. |
| _List schema_ | Datapills defined by your CSV column names. |
| List size | Total number of rows. |
| List index | Position of each row in the list, starting at `0`. |

---
