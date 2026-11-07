---
url: 'https://docs.workato.com/en/connectors/on-prem-files/trigger-new-file.md'
description: >-
  The New file in folder trigger monitors an on-prem folder for new files on a
  schedule you define.
---

# On-prem files - New file in folder trigger

The **New file in folder** trigger monitors an on-prem folder for new files on a schedule you define. Each file is processed as a separate job. This trigger supports [streaming](/en/features/file-streaming) for transferring large files.

The trigger detects all existing files in the folder when you start the recipe for the first time. Only newly added files are processed on subsequent runs.

> **REQUIRED OPA VERSION**
> 
> This trigger requires an [on-prem agent](/en/on-prem/agents) version 2.4.2 or later.

## File renaming

This trigger appends a numerical ID and `.processing` to the names of processed files, for example: `sales_report.csv` is renamed to `sales_report.csv.1526632883663.processing`. This prevents the recipe from triggering on the same file in subsequent runs.

![Trigger renames files when processing](/assets/trigger-file-processing.CZq26gfe.gif)_Trigger renames files when processing_

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Define how frequently the recipe checks for new files. The minimum and default value is `5` minutes. |
| Trigger on | Select whether to search at a **Specific interval** or **Specific date/time**. |
| Folder | Select the folder to monitor for new files. |
| Include files in sub-folders? | Select whether to monitor subfolders for new files. |
| Filter files by naming pattern | Optional. Define a [naming pattern](/en/connectors/on-prem-files#naming-pattern) that files must use to trigger a job. |
| File encoding | Select the file's encoding type. Select **Auto-Detect** to automatically recognize encoding based on the file's content. |
| Chunk size (KB) | Define the chunk size for streaming file contents. The minimum value is 32 KB, and the maximum is 10 MB. This field defaults to 256 KB if left blank. |

> **ADDITIONAL INPUT FIELDS**
> 
> The recipe editor generates additional input fields in the **Schedule settings** section based on your **Trigger on** selection. Use these fields to specify the trigger schedule.

### How can I ignore older files?

You can exclude older files by using a [naming pattern filter](/en/connectors/on-prem-files#naming-pattern) or by manually moving older files to a different folder before starting the recipe.

## Output

| Output field | Description |
| --- | --- |
| CSV lines | Contains information about the contents of the CSV file, such as the column names and their values. |
| File path (original) | The path to the file before it was processed, for example: `C:/Program Files/sales_report.pdf`. |
| File name (original) | The name of the file before it was processed, for example: `sales_report.pdf`. |
| File path (processed) | The path to the file after it was processed, for example: `C:/Program Files/sales_report.pdf.1526632883663.processing`. |
| File name (processed) | The name of the file after it was processed, for example: `sales_report.pdf.1526632883663.processing`. |
| File contents | The contents of the file, which can be used in other actions. This datapill supports [file streaming](/en/features/file-streaming) for working with large files. |
| File size (bytes) | The size of the file in bytes. |
| Created time | The time the file was created. This value is set by your OS. |
| Last modified time | The time the file was last modified. This value is set by your OS. |

---
