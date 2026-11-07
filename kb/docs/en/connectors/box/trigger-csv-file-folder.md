---
url: 'https://docs.workato.com/en/connectors/box/trigger-csv-file-folder.md'
description: >-
  The New CSV file trigger (Batch) starts a recipe when Box adds a new CSV file
  to a specified folder. It processes CSV lines in batches.
---

# Box - New CSV file in folder trigger (batch)

The **New CSV file in folder (batch)** trigger starts a recipe when Box adds a new CSV file to a specified folder. CSV lines run in batches of 100 by default, with a maximum of 50,000. You can configure encoding, delimiters, header rows, and batch size to match your CSV format.

## Input

| Input field | Description |
| --- | --- |
| When first started, this recipe should pick up events from | Select the date and time to begin monitoring. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Folder | Select the folder to monitor. You can select from the drop-down menu or enter a folder ID. |
| Include sub-folders | Select **Yes** to include CSV files in sub-folders. |
| Sample CSV file | Select a sample CSV file for Workato to detect column names. Otherwise, toggle to provide column names manually. |
| Column delimiter | Select the character that separates column values. For example, a comma. |
| Contains header line | Select **Yes** if the first row of the CSV contains column names. |
| Batch size | Enter the number of rows per batch. By default, Workato processes 100 rows per batch. Maximum is 50,000. |
| Expected encoding | Select the encoding type of the CSV file. Default is **UTF-8**. |
| Include copied/moved files | Select **Yes** if the trigger should treat copied or moved files as new files. Default is **No**. |

## Output

| Output field | Description |
| --- | --- |
| Event | Type of trigger event. |
| ID | Unique ID of the CSV file. |
| Name | File name. |
| Type | Object type. |
| Description | File description. |
| Size | File size in bytes. |
| Shared link | Shared link details for the file. |
| Created at | Date and time the file was created. |
| Modified at | Date and time the file was last modified. |
| Trashed at | Date and time the file was moved to trash. |
| Purged at | Date and time the file was permanently deleted. |
| Content created at | Date and time the file content was created. |
| Content modified at | Date and time the file content was modified. |
| Sequence ID | Position of the file in the folder hierarchy. |
| Etag | Entity tag of the file. |
| Sha 1 | SHA-1 hash of the file. |
| Parent | Parent folder details of the file. |
| Path | Path of the file. |
| Path collection | Collection of folder paths the file belongs to. |
| Created by | User who created the file. |
| Modified by | User who last modified the file. |
| Owned by | User who owns the file. |
| Item status | Current status of the file. For example, `active`. |
| First | Indicates if this is the first batch of rows. |
| Last | Indicates if this is the last batch of rows. |
| Lines | Contains the list of CSV rows in the batch. Each row includes its columns and values. |

---
