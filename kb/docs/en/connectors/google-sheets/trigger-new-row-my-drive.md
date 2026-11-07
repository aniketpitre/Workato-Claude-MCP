---
url: >-
  https://docs.workato.com/en/connectors/google-sheets/trigger-new-row-my-drive.md
description: >-
  The New row in sheet in My Drive trigger in the Google Sheets connector picks
  up new rows added at the bottom of a sheet stored in My Drive.
---

# Google Sheets - New row in sheet in My Drive trigger

This trigger detects new rows added at the bottom of your selected sheet. When you start your recipe for the first time, this trigger picks up all existing rows in the sheet, excluding the header row. Subsequently, the trigger picks up new rows added to the end of the sheet.

Note that rows added in the middle of the sheet are not detected. Don't delete any row from the sheet when this trigger is active, as it can disrupt tracking.

> **LIMITATIONS**
> 
> This trigger works exclusively with My Drive. Use the [New row in sheet in Team Drive trigger](/en/connectors/google-sheets/trigger-new-row-team-drive) to monitor Team Drive.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Specify how frequently to check for new events. This field defaults to five minutes if left blank. The minimum value allowed is five minutes. |
| Spreadsheet | Select the spreadsheet to monitor for new rows. |
| Sheet | Choose the sheet to monitor for new rows. The sheet must have at least one header row and one data row. |
| Add column names manually? | Indicate whether to add column names manually. Defaults to `No`. |

## Output

| Output field | Description |
| --- | --- |
| Spreadsheet ID | The unique identifier for the spreadsheet. |
| Spreadsheet name | The name of the spreadsheet. |
| Sheet name | The sheet name. |
| Row number | The row number. |
