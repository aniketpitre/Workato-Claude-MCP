---
url: 'https://docs.workato.com/en/connectors/google-sheets/trigger-new-row.md'
description: >-
  The New row in sheet in My Drive (real-time) trigger in the Google Sheets
  connector picks up new rows added at the bottom of a sheet in real time.
---

# Google Sheets - New row in sheet in My Drive trigger (real-time)

This trigger detects new rows added at the bottom of your selected sheet. When you start your recipe for the first time, this trigger picks up all existing rows in the sheet, excluding the header row. Subsequently, the trigger picks up new rows added to the end of the sheet in real time.

Note that rows added in the middle of the sheet are not detected. Don't delete any row from the sheet when this trigger is active, as it can disrupt tracking.

> **LIMITATIONS**
> 
> Real-time triggers only work with OAuth 2.0 connections, not service accounts.
> 
> This trigger works exclusively with My Drive. Use the [New row in sheet in Team Drive trigger](/en/connectors/google-sheets/trigger-new-row-team-drive) to monitor Team Drive.

## Input

| Input field | Description |
| --- | --- |
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

## How to use this trigger

Complete the following steps to set up and use the **New row in sheet in My Drive (real-time)** trigger:

### Set up the Google Sheet

To retrieve sheet data, the sheet must include at least one header row and one data row:

![Google sheet sample](/assets/sample-google-sheet.Dkg-QFd-.jpg)_Sample Google Sheet with one header row and one data row_

### Configure the trigger

Complete the following steps to configure the trigger:

1. Select the **New row in sheet in My Drive (real-time)** trigger.
   
   ![Set up application](/assets/application-and-trigger.B8-au229.png)_Set up the application and the trigger_
   
2. Select a spreadsheet in the **Spreadsheet** drop-down menu to dynamically generate the list of sheets in your spreadsheet.
   
   ![Blank Trigger](/assets/trigger-setup-blank.CEcrP8xo.png)_Select the spreadsheet to monitor for new rows_
   
3. Select the specific sheet to monitor for new rows in the **Sheet** field.
   
   ![Filled trigger](/assets/trigger-setup-filled.CHtKTjPH.png)_Once the spreadsheet has been selected, an additional picklist is generated asking for the specific sheet to monitor_
   
4. Click **`+` Add step > Action in app**.
   
5. Search for and select `Scheduler by Workato`.
   
6. Select the **Get current time** action.
   
   ![Scheduler action](/assets/scheduler-action.D_dYn9Em.png)_Scheduler action_
   

### Test the trigger

After the trigger is configured, you can finalize and run the recipe.

This test aims to verify that the trigger detects new rows in the sheet. The action is not critical to this test, so you can use the **Get current time** Scheduler action.

Click **Test recipe** to test your recipe. Your recipe should resemble the following screenshot:

![Google spreadsheet sample](/assets/configured-recipe.C3BVrS9W.png)_Configured recipe with scheduler action for testing_

While the recipe is running, any new rows added at the bottom of the sheet are detected almost immediately. If the recipe is stopped and later restarted, it resumes picking up new rows from where it left off. Consequently, any new rows added when the recipe was stopped are also detected upon restarting.

---

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

---

---
url: >-
  https://docs.workato.com/en/connectors/google-sheets/trigger-new-updated-row.md
description: >-
  The New/updated row in sheet in My Drive (real-time) trigger in the Google
  Sheets connector picks up changed and new rows in a sheet in real time.
---

# Google Sheets - New/updated row in sheet in My Drive trigger (real-time)

This trigger detects changes to rows in your selected sheet and new rows added at the bottom in real time.

This trigger can monitor up to 10,000 rows. New or updated rows after row 10,000 will not be picked up.

> **LIMITATIONS**
> 
> Real-time triggers only work with OAuth 2.0 connections, not service accounts.
> 
> This trigger works exclusively with My Drive. Use the [New/updated row in sheet in Team Drive trigger](/en/connectors/google-sheets/trigger-new-updated-row-team-drive) to monitor Team Drive.

## Input

| Input field | Description |
| --- | --- |
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

## How to use this trigger

Complete the following steps to set up and use the **New/updated row in sheet in My Drive (real-time)** trigger:

### Set up the Google Sheet

To retrieve sheet data, the sheet must include at least one header row and one data row:

![Google sheet sample](/assets/sample-google-sheet.Dkg-QFd-.jpg)_Sample Google Sheet with one header row and one data row_

### Configure the trigger

1. Select the **New/updated row in sheet in My Drive (real-time)** trigger.
   
2. Select a spreadsheet in the **Spreadsheet** drop-down menu to dynamically generate the list of sheets in your spreadsheet.
   
   ![configured sheet trigger](/assets/configured-sheet-trigger.BgdOU_nj.png)_Configured new/updated sheet row trigger_
   
3. Select the specific sheet to monitor for new or updated rows in the **Sheet** field.
   
4. Select a column to monitor for changes in the **Column to monitor** field. Every time the data in a cell in this column changes, the recipe picks up the entire row of data.
   
   Alternatively, you can select the `All columns` option, which activates the trigger whenever a row is changed.
   

### Test the trigger

After configuring the trigger, you can finalize and run the recipe.

This test aims to verify that the trigger detects new rows in the sheet. The action is not critical to this test, so you can use the **Get current time** Scheduler action.

Click **Start recipe** to run your recipe. Your recipe should resemble the following screenshot:

![configured recipe](/assets/configured-recipe-with-scheduler-action.C2B02rhx.png)_Configured recipe with Scheduler action for testing_

In this example, the trigger detects all four rows of data in the spreadsheet. You can [customize the jobs report](/en/recipes/jobs#customizing-job-reports) to display the information relevant to you:

![new job report](/assets/customized-job-report.Bx4HXjdr.png)_Customized job report displaying selected information about the trigger event processed_

The following shows the customization of the job report:

![customize job report](/assets/customization-job-report.CwccpyWb.png)_Customizing the job recipe's job report with data from Google Sheets_

If the sheet is configured to monitor only changes to the **Date registered** column, changes to other columns (like Andy's shirt size) won't trigger the recipe.

![modified google sheets](/assets/modified-sheet.DFQl9mRU.jpg)_Edited sample sheet with changed field highlighted_

However, if you edit Xander's **Date registered** value in cell E5, the recipe detects it as a trigger event and processes row 5 with the latest data.

![edited sheet](/assets/edited-sheet.Ci5Q3ybS.jpg)_Edited sheet. Cells in rows 3 and 5 (highlighted) have been updated with new values_

Row 5 is processed as a trigger event, as seen in the job details:

![date sheet](/assets/date-sheet.D7ysIWJ0.png)_Only row 5 will be picked up as "Date registered"- the only column we are monitoring changes for_

While the recipe is running, any new or updated rows are picked up almost immediately. If the recipe is stopped and restarted, it continues processing from where it left off. This means that any changes made while the recipe was stopped are detected and processed when the recipe starts again.

Note that only the latest version of a row is picked up. For example, if a row is created and updated multiple times while the recipe is stopped, only the most recent version triggers an event when the recipe restarts.

---

---
url: >-
  https://docs.workato.com/en/connectors/google-sheets/trigger-new-row-team-drive.md
description: >-
  The New row in sheet in Team Drive trigger in the Google Sheets connector
  picks up new rows added at the bottom of a sheet stored in a Team Drive.
---

# Google Sheets - New row in sheet in Team Drive trigger

This trigger detects new rows added at the bottom of your selected sheet. When the recipe starts for the first time, it detects all existing rows in the sheet, excluding the header row. Subsequently, it picks up new rows added at the end of the sheet.

Note that rows added in the middle of the sheet are not detected. Don't delete any row from the sheet when this trigger is active, as it can disrupt tracking.

> **LIMITATIONS**
> 
> This trigger works exclusively with Team Drive. Use the [New row in sheet in My Drive trigger](/en/connectors/google-sheets/trigger-new-row-my-drive) to monitor Team Drive.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Specify how frequently to check for new events. This field defaults to five minutes if left blank. The minimum value allowed is five minutes. |
| Google Drive | Select a team drive. |
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

---

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

---
