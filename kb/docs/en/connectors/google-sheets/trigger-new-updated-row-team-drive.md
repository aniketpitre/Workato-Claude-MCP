---
url: >-
  https://docs.workato.com/en/connectors/google-sheets/trigger-new-updated-row-team-drive.md
description: >-
  The New/updated row in sheet in Team Drive trigger in the Google Sheets
  connector picks up changed rows and new rows in a Team Drive sheet.
---

# Google Sheets - New/updated row in sheet in Team Drive trigger

This trigger detects changes made to rows in your selected sheet, as well as new rows added at the bottom of your sheet.

Note that rows added in the middle of the sheet are not detected. Don't delete any row from the sheet when this trigger is active, as it can disrupt tracking.

> **LIMITATIONS**
> 
> This trigger works exclusively with Team Drive. Use the [New/updated row in sheet in My Drive trigger](/en/connectors/google-sheets/trigger-new-updated-row-my-drive) to monitor Team Drive.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Specify how frequently to check for new events. This field defaults to five minutes if left blank. The minimum value allowed is five minutes. |
| Google Drive | Select a team drive. |
| Spreadsheet | Select the spreadsheet to monitor for new/updated rows. |
| Sheet | Choose the sheet to monitor for new/updated rows. The sheet must have at least one header row and one data row. |
| Add column names manually? | Indicate whether to add column names manually. Defaults to `No`. |

## Output

| Output field | Description |
| --- | --- |
| Spreadsheet ID | The unique identifier for the spreadsheet. |
| Spreadsheet name | The name of the spreadsheet. |
| Sheet name | The sheet name. |
| Row number | The row number. |
