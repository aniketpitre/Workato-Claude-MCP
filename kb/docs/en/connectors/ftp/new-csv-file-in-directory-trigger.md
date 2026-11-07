---
url: >-
  https://docs.workato.com/en/connectors/ftp/new-csv-file-in-directory-trigger.md
description: This trigger monitors a server directory for newly added CSV files.
---

# FTP/FTPS - New CSV file added in directory on FTP/FTPS server (batch)

The **New CSV file added in directory on FTP/FTPS server** trigger monitors a server directory for newly added CSV files. Jobs are only triggered from CSV files located at the first level of the directory that contains rows.

Use the [New/updated file in directory trigger](/en/connectors/ftp/new-updated-file-in-directory-trigger) to instead monitor new and updated files.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Specify how frequently to check for new events. Defaults to five minutes if left blank. The minimum value allowed is five minutes. Refer to the [Polling intervals](/en/recipes/polling-intervals) documentation for more information. |
| Directory path | Select a directory from the menu, or enter it manually. The trigger processes files in this directory by time last modified in ascending order. |
| Column names | Provide the column names in the CSV file. Input the columns manually or upload a sample CSV file to enter them all at once. |
| Column delimiter | Select the column delimiter in the CSV file. The following options are available: comma (`,`), space, tab, colon (`:`), semicolon (`;`), and pipe (`|`). |
| Contains header row? | Set to `Yes` if the first row in the CSV file is a header row containing column names. |
| Batch size | Specify the number of CSV rows to retrieve in each batch. Refer to the [Batch processing](/en/features/batch-processing) documentation for more information. |

## Output

| Output field | Description |
| --- | --- |
| File name | The name of the CSV file. |
| First batch | Indicates if this is the first batch of rows from the file. |
| Last batch | Indicates if this is the last batch of rows from the file. |
| Lines | An array of objects representing the rows in the CSV file. Each object contains column data. |
