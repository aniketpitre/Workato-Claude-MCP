---
url: >-
  https://docs.workato.com/en/connectors/google-sheets/action-update-rows-in-bulk.md
description: >-
  The Update rows in bulk action in the Google Sheets connector lets you update
  up to 50,000 rows of a sheet in batches of 500.
---

# Google Sheets - Update rows in bulk action

This action updates multiple rows of a selected sheet in Google Sheets. This action supports up to 50,000 records and updates in batches of 500.

## Input

| Input field | Description |
| --- | --- |
| Google Drive | Select either your personal drive or a team drive. Your personal drive is selected by default. |
| Spreadsheet | Choose the spreadsheet where you plan to update rows in bulk. |
| Sheet | Specify the sheet where you plan to update rows in bulk. Ensure the sheet contains at least one header row and one data row. |
| Row number | Enter the row number from which the values must be updated, or use the Row number datapill from the output of other Google Sheets triggers and actions. |
| Rows | Enter the values for the updated rows. |

## Output

| Output field | Description |
| --- | --- |
| Spreadsheet ID | The unique identifier of the spreadsheet. |
| Sheet name | The name of the sheet within the spreadsheet. |
| All rows successfully updated? | Indicates whether all rows were successfully updated. |
| Number of rows updated | The number of rows that were updated. |
| Number of rows failed | The number of rows that failed to update. |
| CSV contents of failed rows | The CSV contents of the failed rows. |
| List of batches | Information about the batches of updated rows. |
