---
url: >-
  https://docs.workato.com/en/connectors/google-sheets/trigger-new-updated-row-my-drive.md
description: >-
  The New/updated row in sheet in My Drive trigger in the Google Sheets
  connector picks up changed rows and new rows in a My Drive sheet, up to 10,000
  rows.
---

# Google Sheets - New/updated row in sheet in My Drive trigger

This trigger detects changes made to rows in your selected sheet, as well as new rows added at the bottom of your sheet.

This trigger can monitor up to 10,000 rows. New or updated rows after row 10,000 are not picked up.

> **LIMITATIONS**
> 
> This trigger works exclusively with My Drive. Use the [New/updated row in sheet in Team Drive trigger](/en/connectors/google-sheets/trigger-new-updated-row-team-drive) to monitor Team Drive.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Specify how frequently to check for new events. This field defaults to five minutes if left blank. The minimum value allowed is five minutes. |
| Spreadsheet | Select the spreadsheet to monitor for new/updated rows. |
| Sheet | Choose the sheet to monitor for new/updated rows. The sheet must have at least one header row and one data row. |
| Column to monitor | Select the column to monitor for changes. |
| Add column names manually? | Indicate whether to add column names manually. Defaults to `No`. |

## Output

| Output field | Description |
| --- | --- |
| Spreadsheet ID | The unique identifier for the spreadsheet. |
| Spreadsheet name | The name of the spreadsheet. |
| Sheet name | The sheet name. |
| Row number | The row number. |
