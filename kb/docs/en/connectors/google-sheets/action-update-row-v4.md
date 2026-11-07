---
url: 'https://docs.workato.com/en/connectors/google-sheets/action-update-row-v4.md'
description: >-
  The Update row action in the Google Sheets connector lets you update a row in
  a sheet, often paired with the Search rows action.
---

# Google Sheets - Update row action

This action allows you to update a row in a sheet. It is often used with the [Search rows action](/en/connectors/google-sheets/action-search-rows-v4).

## Input

| Input field | Description |
| --- | --- |
| Google Drive | Select either your personal drive or a team drive. Your personal drive is selected by default. |
| Spreadsheet | Select a spreadsheet from the drop-down, or use the Spreadsheet ID datapill from the output of other Google Sheets triggers and actions. |
| Sheet | Select a sheet from the drop-down, or use the Sheet name datapill from the output of other Google Sheets triggers and actions. |
| Row number | Indicate the row you plan to update. |
| Columns | After you select a spreadsheet, a sheet, and a row in the sheet, the columns appear in this field. Enter the new values for Workato to update. |

## Output

| Output field | Description |
| --- | --- |
| Spreadsheet ID | ID of the spreadsheet. You can map this into the `Spreadsheet` input field of other Google Sheets actions instead of selecting the spreadsheet from the drop-down menu. |
| Spreadsheet name | Name of the spreadsheet. |
| Sheet name | Name of the sheet. You can map this into the `Sheet` input field of other Google Sheets actions instead of selecting the sheet from the drop-down menu. |
| Updated range | The range in the sheet that this action has updated. |
| Updated columns count | The number of columns this action has updated. |
| Columns | This contains the values of all updated columns in the selected row. |

## How to use this action

The following example demonstrates how to use the **Update row** action with the [Search rows action](/en/connectors/google-sheets/action-search-rows-v4).

Our sample sheet is a list of items from different countries. For the Google Sheets connector to work, your sheet must have at least one header row and one data row.

![Sample sheet](/assets/sample-sheet.BSdhs1e5.png)_Sample sheet_

In this example, there is a mistake in cells A3 and A4: these values should be `Australia and Oceania`, not `Asia`.

To fix this, our recipe must search for rows where **Country** equals `Australia` and **Region** equals `Asia`. Then, it must update the **Region** to `Australia and Oceania` instead.

![Sample recipe of Google Sheets Search and Update ](/assets/sample-search-update-recipe.6CwjIOak.png)_Sample recipe of Google Sheets Search and Update_

Complete the following steps to configure the **Search rows** and **Update row** actions:

### Configure the Search rows action

This action searches for rows in the Google Sheet that match the conditions you specify in the **Columns** fields.

1. Select the **Search rows** action and expand the **Columns** section.
   
2. Enter `Asia` in the **Region** field.
   
3. Enter `Australia` in the **Country** field.
   
   ![Configure the Search rows action](/assets/sample-search-rows.BSFtOIuh.png)_Configure the Search rows action_
   

### Configure the Repeat action

For each row in the sheet, this action checks if there are any matches based on the search criteria specified in the **Search rows** action.

1. Click `+` **Add step** and select **Repeat for each**.
   
2. Map the Rows (Step 2) datapill to the **Input list** field.
   
   ![Configure the Repeat for each action](/assets/sample-loop-rows.Cd-MAr7W.png)_Configure the Repeat for each action_
   

### Configure the Update row action

Complete the following steps to configure the **Update row** action:

1. Select the **Update row** action and map the Row number (Step 3) datapill to the **Row number** field.
   
   ![Configure the Update row action](/assets/sample-update-row.O9k4ZAvy.png)_Configure the Update row action_
   
2. Enter `Australia and Oceania` in the **Region** field to update cells matching the search criteria.
   
3. Click **Save** to save your recipe.
   

### Test the recipe

Click **Test recipe** to test the recipe.

After running the recipe, you'll find that cells A3 and A4 are correctly updated to `Australia and Oceania`:

![Cells A3 and A4 are correctly updated](/assets/sample-sheet-updated.B9XyNAdq.png)_Cells A3 and A4 are correctly updated_

---

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

---
