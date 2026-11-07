---
url: 'https://docs.workato.com/en/data-tables/user-interface/create.md'
description: >-
  Create a new Workato data table within a project by building the table
  structure from scratch or by importing a CSV file.
---

# Create a new table

Tables exist at the level of the individual project. Go to **Projects > {Project name} > Data tables** to access the **Data tables** interface.

![Data tables Creation](/assets/data-table-create.DE8DrnJ7.png)_Create a new data table within a project_

> **NEED AN EXAMPLE?**
> 
> Refer to the [Build a data table to store genie conversation IDs use case](/en/getting-started/use-cases/data-tables/store-agent-conversation-ids-in-a-data-table) for a step-by-step recipe example.

Complete the following steps to create a new table:

You can create a data table by building the table structure from scratch or by importing a CSV file.

1. Create a new project, or select one of your saved projects.
   
2. Click **Create > Data table** or press C+T.
   
3. Enter a name for the table in the **Data table name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the data table.
   
5. Select one of the following creation methods:
   
   **Create empty table**
   
   Select **Create empty table** to define the table structure manually, then click **Start building**. The new data table displays.
   
   ![Create empty table](/assets/create-empty-table.23lNr_m7.png)_Create empty table_
   
   Refer to the following documentation to configure the new data table:
   
   - [Create a column](/en/data-tables/user-interface/column-create)
   - [Edit a column](/en/data-tables/user-interface/column-edit)
   - [Delete a column](/en/data-tables/user-interface/column-delete)
   - [Edit table data](/en/data-tables/user-interface/edit)
   
   **Import CSV**
   
   1. Select **Import CSV** to create a data table with columns and data from an existing CSV file, then click **Start building**. The **Import CSV** dialog displays.
      
      ![Import CSV](/assets/import-csv.CUz7W7fX.png)_Import CSV_
      
   2. Configure your CSV settings before adding your file. You can't change these settings after the import completes.
      
      ![Configure CSV settings](/assets/configure-csv-settings.BjjFl3me.png)_Configure CSV settings_
      
      1. Use the **CSV encoding** drop-down menu to select the format used to encode the CSV file. Defaults to `UTF-8`.
         
      2. Use the **Column delimiter** drop-down menu to select the character used to separate column values in each line. Defaults to **Comma**.
         
      3. Use the **Quote character** drop-down menu to select the character used to quote CSV cell values. Defaults to **Double**. Refer to [Quote characters](#quote-characters) for more information.
         
      4. Use the **Use first row as headers** drop-down menu to determine whether Workato uses the first row of the CSV file as column headers. Workato generates generic column names (`column 1`, `column 2`, and so on) when you set this option to **No**.
         
   3. Upload your CSV file in the **CSV file** field.
      
   4. Review the schema preview. Workato auto-detects the column type for each column based on the CSV data. You can click the edit icon next to a column to change the column name, column type, or required flag before you confirm the import. Supported column types include short text, long text, integer, decimal, boolean, date, and datetime. File, relations, and multi-value relations column types aren't supported when you import from CSV.
      
      The field names `Record ID`, `Created time`, and `Last modified time` are reserved and can't be assigned to new columns. Rename any columns with these names in your CSV file before you import it.
      
   5. Click **Upload and preview** to start the import.
      
      Workato processes the import asynchronously and displays a progress bar with the record count and percentage. You can continue to use the table during the import. If the import fails, Workato displays the row where the error occurred and preserves all records up to that row.
      
   

You can also import a CSV file from the data table view by clicking **Import CSV**. This option is only available when the table has no existing columns.

## Quote characters

Quote characters enclose CSV cell values that contain delimiter characters, newline characters, or the quote character itself. Workato uses the quote character you select to determine how to parse your CSV data correctly.

For example, the value `"San Francisco, CA"` contains a comma. The quote characters tell Workato to treat the comma as part of the value rather than as a column separator.

The following example demonstrates additional scenarios. When you use the double quote (`"`) as the quote character and the comma (`,`) as the delimiter, Workato parses the following CSV data as one row with five columns:

```text
abc,"abc","def,ghk","klm""nop","qr
st"
```

Workato interprets each value in the following way:

- `abc`: A value without quote characters. Workato parses this value as-is.
- `"abc"`: A value enclosed in quote characters. Workato removes the surrounding quotes and parses the value as `abc`.
- `"def,ghk"`: A value that contains a comma. Workato treats the comma as a normal character because the value is enclosed in quote characters, and parses it as `def,ghk`.
- `"klm""nop"`: A value that contains an escaped quote character. You can escape a quote character by doubling it. Workato parses this value as `klm"nop`.
- `"qr\nst"`: A value that contains a newline character. Workato treats the newline as part of the value because it's enclosed in quote characters, and parses it as a single cell that spans two lines. This means Workato treats the data as one row, not two.

## Auto-generated columns

Workato automatically generates certain columns for each record when you create a new table. These columns are read-only, and you cannot edit them.

Workato hides these columns by default. To view hidden columns, click **Hide columns**, and select the columns you plan to view.

![Autogenerated columns](/assets/autogenerated-columns.qqdOdDjn.png)_View auto-generated columns_

### Common auto-generated columns

The following columns are part of any data table, but Workato may add other auto-generated columns to your data tables in certain scenarios.

- Record ID
  
- Workato automatically generates a unique ID for each record in a data table. Workato requires the Record ID to perform certain Data table connector actions, including the [update record](/en/data-tables/connector/update-record-action) and [delete record](/en/data-tables/connector/delete-record-action) actions. The field name `Record ID` is reserved and can't be assigned to new columns.
  
- Created time
  
- The creation time of the record. The field name `Created time` is reserved and can't be assigned to new columns.
  
- Last modified time
  
- The last edit time of the record. The field name `Last modified time` is reserved and can't be assigned to new columns.
  

![Data tables](/assets/autogenerated-columns-2.af3KIzw_.png)_Auto-generated columns common to all data tables_

---
