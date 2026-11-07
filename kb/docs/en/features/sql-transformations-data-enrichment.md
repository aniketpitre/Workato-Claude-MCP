---
url: 'https://docs.workato.com/en/features/sql-transformations-data-enrichment.md'
description: >-
  Build a recipe that fetches Salesforce opportunities, enriches them with data
  from other sources using SQL Transformations, and sends them to SFTP.
---

# Sample use case - Data enrichment

Before you send data extracted from a source to a destination, there are often requirements to enrich the data with additional information from one or many sources. As the volume of the data grows, it becomes challenging to temporarily store and enrich the data and then load it to the destination.

SQL Transformations provides users the ability to pipeline any number of data sources and work with large volumes of data easily. Users can merge/aggregate data across files with SQL join operations and enrich incoming data with additional information, perform manipulations on the fly, and send it to any destination or store it within Workato FileStorage.

## Sample recipe: Fetch opportunities from Salesforce, enrich the fetched data and send it to SFTP server

Consider the following scenario:

A company must extract all opportunity information from Salesforce in bulk, enrich it with additional product details, including cost, price, and specific region details, and send the enriched data to a partner file system in an external SFTP server.

With SQL Transformations, you can easily perform these complex processes in just five steps!

![Recipe workflow](/assets/enrich-workflow.CoIpIRMA.png)

1. Set up a scheduler trigger that runs at a frequency you specify.
   
2. Set up the bulk action in Salesforce that can fetch all required opportunity records in bulk as a CSV content.
   
3. If the data you plan to use for enrichment is available at different sources, including Google Drive, you use download actions to fetch those contents as well.
   
4. Set up the **Query CSV** action from the SQL Transformations connector. During this step you can pipeline in the data from all the different sources and write a query that can enrich the opportunities with the additional data.
   
5. In the final step, Workato sends the data to the destination, which is the SFTP server.
   

## How to leverage SQL Transformations for data enrichment

This section describes how to set up different sections of the **Query CSV** action, enabling you to leverage SQL Transformations for data enrichment.

> **Follow along**
> 
> See this [recipe link](https://app.workato.com/recipes/4126608-etl-extract-opportunities-from-salesforce-enrich-with-product-price-details-and-load-to-destination?community=us#recipe) to follow along and modify a sample recipe to suit your own workflow.

### Data Source setup

Connect the different data sources on which SQL Transformations performs the query. In this example, there are three different data sources.

1. To connect **Source #1**, fill in the following fields. In our example, **Source #1** is the incoming extract from an on-prem system.
   
   - Data source name
     
   - Give a meaningful name for the **Data source name**, for example **contacts\_extract**.
     
   - Data source type
     
   - Select the **Data source type**. In our example, this is **CSV content stream**.
     
   - CSV stream input
     
   - After you set the data source as **CSV content stream**, you can now set the CSV stream input. This is where you pass the file contents coming from the on-prem files trigger.
     
   - Data schema
     
   - Set the **Data schema**. You can do this easily by importing a CSV file containing a few sample contacts data.
     
   - Ignore CSV header row
     
   - This allow users to specify whether the incoming data has a heading column that must be ignored and not considered as part of the data.
     
   - Column delimiter
     
   - Select the delimiter used in the CSV file to separate columns.. Available options include a **,** (comma), **;** (semicolon), and more.
     
   
   ![Data source #1](/assets/enrich-ds-1.DFpSC_fJ.png)
   
2. To connect **Source #2**, fill in the following fields. This is the source that points to the product price list data, which is used to enrich the data extracted from the source.
   
3. - Data source name
     
   - Give a meaningful name for the **Data source name**, for example **product\_price\_lookup**.
     
   - Data source type
     
   - Select the **Data source type**. In our example, this is **CSV content stream**.
     
   - CSV stream input
     
   - Provide the CSV reference datapill to fetch the data. Our example uses contents from a Google drive download action.
     
   - Data schema
     
   - Set the **Data schema**. You can do this easily by importing a CSV file containing a few sample contacts data.
     
   
   ![Data source #2](/assets/enrich-ds-2.CxjjDT_O.png)
   
4. Configure **Source #3**.
   
   In this step, our example fetches specific region details which we plan to use to enrich the opportunities data. Because we plan to reuse this data quite often and it does not change much, it is easy to store and handle this data using FileStorage, Workato's own internal persistent file storage system.
   
   Configure the following fields:
   
   - Data source name
     
   - Give a meaningful name for the **Data source name**, for example **region\_lookup**.
     
   - Data source type
     
   - Select the **Data source type**. In our example, this is **FileStorage file**.
     
   - FileStorage file path
     
   - Provide the path within FileStorage where the historical data file is available.
     
   - Data schema
     
   - Set the **Data schema**. You can do this easily by importing a CSV file containing a few sample contacts data. The schema is matched to the order of the columns coming from the source from left to right.
     
   
   ![Data source #3](/assets/enrich-ds-3.D30aGrkK.png)
   

### Query setup

Next, set up the query that works on the data sources and produces the transformed output. In this example, the query joins the data across all three data sources, and then calculates the total revenue, total cost, and total profit with the help of the product pricing data. Additionally, country and region details are also added by joining with the **region\_lookup** data source. The WITH ... AS ... function helps write a subquery and use that data in the main query easily.

![Query setup](/assets/enrich-query.CQylrPlF.png)

### Output setup

Define the format of the output.

Our example sends the enriched records file to the SFTP server. Because our example sends the enriched records file to the SFTP server, we chose the output type as **CSV contents stream**. This means that we can pass the CSV contents output datapill from **Query CSV data** action into the contents input section of the SFTP upload file action, and the contents stream automatically from **Query CSV** action to SFTP server. Also, similar to data source setup, here we have the options to choose what delimiter to use in the output CSV content, and whether to include a column header.

1. Fill in the following fields:
   
   - Output type
     
   - Select the type of the output. Use **CSV content stream** to share the contents as a streamable datapill to downstream actions.
     
   - Include header row
     
   - Set to **Yes** if the column names from the data must be added as header rows in the file. This is useful if you plan to use the file for generating reports. The default value is **No**.
     
   - Column delimiter
     
   - Select the delimiter used in the CSV file to separate columns. Available options include a **,** (comma), **;** (semicolon), and more.
     
   
   ![Output setup](/assets/enrich-output.C8-wdjAh.png)
   
2. Select the **Upload file to SFTP** action.
   
3. Fill in the following fields:
   
   - File name
     
   - Provide the full path, including the folder. The folder must exist before you add a file to it.
     
   - Append
     
   - If **Yes**, appends contents to existing file. If **No**, overwrites if the file already exists. Defaults to **No**.
     
   - File contents
     
   - The file contents you plan to upload. Pass the CSV contents datapill from **Step 4 Query CSV data** action.
     
   
   ![SFTP upload action setup](/assets/enrich-output-2.BVKlzidS.png)
   

## Read next

To view more sample use cases, read the following guides:

- [Change data capture](/en/features/sql-transformations-cdc)
- [Data validation and cleansing](/en/features/sql-transformations-data-validation-cleansing)

---

---
url: >-
  https://docs.workato.com/en/data-orchestration/data-transformation/sql-transformations/sql-collection.md
description: >-
  Use SQL Collection by Workato to create temporary tables and run SQL queries
  that manipulate and synchronize data across multiple systems.
---

# SQL Collection

SQL Collection by Workato is a robust native application that provides you with the tools to manipulate table data. You can use SQL Collection to synchronize related data across multiple systems, such as databases, web services, and more.

![SQL Collection by Workato](/assets/query-list-in-collection-export.4NYfkeYG.png)_SQL Collection by Workato_

## Why use SQL Collection

SQL Collection allows you to run SQL statements with data from multiple sources. You can create temporary tables from a list input or CSV file. Subsequently, you can perform a variety of SQL queries to arrive at the required output for your use case.

SQL Collection tables (also called **SQL Collection lists**) are temporary. This means they exist only for the duration of the job and do not persist across multiple jobs. Load the data directly to your target system after you complete data processing.

## SQL Collection quotas

SQL Collection has the following quota:

| Description | Quota |
| --- | --- |
| Recommended maximum number of records | 50,000 |

### Transformation

SQL Collection is built on SQL lite and functions like any database. You can create lists and query them using standard SQL syntax. Use common SQL keywords like `WHERE`, `GROUP BY`, and `JOIN` to manipulate data from tables into your planned format.

Subsequently, load them directly into your target system with the SQL Collection output or export the data as a CSV file.

### Handle large datasets with SQL Collection

SQL Collection supports large datasets, but performance depends on the structure of your data, including row size and column count. We recommend that you use datasets that don't exceed **50,000 records** per SQL Collection list to ensure reliable performance.

SQL Collection can handle larger datasets, such as 100,000 to 200,000 records, if the rows are small and have fewer columns. Datasets that exceed the recommended quotas may impact performance or stability. Split tables into smaller chunks or use parallel recipes to process larger datasets efficiently.

SQL Collection integrates seamlessly with Workato, allowing you to load and process data directly without third-party tools.

## Connection setup

No connection setup is required. Simply select **App** > **SQL Collection by Workato** to get started.

## Actions

### Create list in SQL Collection action

This action creates a SQL Collection list in the recipe from a list input. The SQL Collection list contains the column headers according to the schema of the list.

Note that the **List source** field must be in [formula mode](/en/formulas/formula-mode) when you add a list datapill.

For example, you can take a list of all workers from **Workday**.

![Create list in SQL Collection](/assets/create-list-in-collection.WjQjW1Oj.png)_Create list in SQL Collection_

| Input field | Description |
| --- | --- |
| List source | Select a list `datapill`. **Ensure that this field is in formula mode.** |
| List name | The name of the list. |
| Index primary | Select one or more columns as the primary index of your list. |
| Index secondary | Select one or more columns as the secondary index of your list. |

> **COLLECTION DATE ERROR**
> 
> You may receive an invalid format error for the `Date` field when using **SQL Collection**. This error occurs because SQLite does not provide a storage class for dates and times. To correct this error, you must use [Mapper by Workato](/en/connectors/mapper#mapper-by-workato) to do one of the following:
> 
> - Update the date to the following format: `YYYY-MM-DD HH:MM:SS.SSS`
> - Skip the date fields if the date is not required in downstream applications

> **COLLECTION BOOLEAN VALUES**
> 
> SQL Collection stores `Boolean` field values as the text values `t` (true) and `f` (false), not as native booleans. A `WHERE` clause that compares a boolean column to `true` or `false` (for example, `WHERE is_active = true`) matches no rows, because the column holds the string `t` or `f` rather than a boolean literal. Compare boolean columns to the string values instead: `WHERE is_active = 't'` or `WHERE is_active = 'f'`.

### Insert rows in SQL Collection action

This action inserts rows into a SQL Collection list in the recipe from a list input. The SQL Collection list contains the column headers according to the schema of the list. You can use this in a repeat loop.

![Insert rows into list in SQL Collection](/assets/insert-rows-into-collection.Ca3PsK5a.png)_Insert rows into SQL Collection_

| Input field | Description |
| --- | --- |
| List source | Select a list `datapill`. Ensure that this field is in formula mode. |
| List name | The name of the list. |
| Create table if table doesn't exist? | Creates a table if table does not exist. |
| Index primary | Select one or more columns as the primary index of your list. |
| Index secondary | Select one or more columns as the secondary index of your list. |

### Create list in SQL Collection from CSV

This action creates a SQL Collection list from a CSV input. The newly-created list contains the column headers according to the schema of the CSV string.

For example, if you plan to retrieve files from your **on-prem** systems, you can download a CSV file and use it directly with SQL Collection.

![Create list in SQL Collection from CSV](/assets/create-list-in-collection-from-csv.BKt32Skk.png)_Create list in SQL Collection from CSV_

| Input field | Description |
| --- | --- |
| CSV source | Select a CSV string as source input. |
| List name | The name of the list. |
| File encoded type | Select the file encoded type. The default value is UTF-8. |
| Column names | The column headers in your CSV source input. Select **use a sample CSV file** to define your schema with a CSV file. |
| Ignore CSV header row | Select `Yes` if the CSV source has a header row, otherwise select `No`. |
| Column delimiter | Select the character used to separate value in each line of the CSV. |
| Index primary | Select one or more columns as the primary index of your list. |
| Index secondary | Select one or more columns as the secondary index of your list. |

### Insert rows in SQL Collection from CSV file action

This action inserts rows into a SQL Collection list in the recipe from a CSV file. It will contain the column headers according to the schema of the CSV string.

![Insert rows into list in SQL Collection from CSV file](/assets/insert-rows-into-collection-from-csv.Ybbs7zX-.png)_Insert rows into SQL Collection from CSV file_

| Input field | Description |
| --- | --- |
| CSV source | Select a CSV string as source input. |
| List name | The name of the list. |
| File encoded type | Select the file encoded type. The default value is UTF-8. |
| Column names | The column headers in your CSV source input. Select **use a sample CSV file** to define your schema with a CSV file. |
| Ignore CSV header row | Select `Yes` if the CSV source has a header row, otherwise select `No`. |
| Column delimiter | Select the character used to separate value in each line of the CSV. |
| Index primary | Select one or more columns as the primary index of your list. |
| Index secondary | Select one or more columns as the secondary index of your list. |

### Query list in SQL Collection

This action allows you to perform standard SQL queries on your lists.

![Query list in SQL Collection](/assets/query-list-in-collection.BkO29mTl.png)_Query list in SQL Collection_

| Input field | Description |
| --- | --- |
| SQL query | Write your SQL query. Normal SQL syntax applies. |
| Output list schema | Define the schema according to your column headers in your output list. Select **use sample JSON** to define your schema with JSON. |
| Write to CSV | Select `Yes` to convert the query results to a CSV string, this will display the input fields below. To use this query output in further SQL queries, select `No`. |
| Add CSV header | Select `Yes` to use the column names as a CSV header row, otherwise select `No`. |
| Column delimiter | Select the character used to separate values in each line of the CSV. |

Here are some commonly used SQL keywords that can be used in the **Query list** action.

| SQL keywords | Description |
| --- | --- |
| SELECT | Use the SQL wildcard `*` to call all the columns in this list. |
| WHERE | Define conditions that specify what data you want to retrieve from the list. |
| JOIN | Use `JOIN`, `LEFT JOIN`, `INNER JOIN` to combine lists. |
| INSERT INTO | Define new entries for your list. |
| DELETE | Define rows to remove from your list. |

Remember to query the full list before exporting or loading it into your target systems. Some SQL keywords (for example, `INSERT INTO`, `DELETE`) do not return list outputs. Therefore, datapills from these actions do not contain all the rows/columns in your SQL Collection list.

A `WHERE` clause on a boolean column requires a string comparison, not a boolean literal. Refer to [Create list in SQL Collection action](#create-list-in-sql-collection-action) for the required syntax.

#### Example query: delete rows from list

For example, you can tailor your workers list from **Workday** to exclude certain groups of people.

![Delete rows with Query list in SQL Collection](/assets/query-list-in-collection-delete.D937v_Gx.png)_Delete rows with Query list in SQL Collection_

Since a `DELETE` query does not return a list output, datapills from this step **should not be used** to export your list.

#### Example query: Export SQL collection as CSV

![Export rows as CSV](/assets/query-list-in-collection-export.4NYfkeYG.png)_Export rows as CSV_

Run a `SELECT` query to retrieve all rows from that SQL collection.

```sql
SELECT * FROM workers_list
```

Next, select **Write to CSV** in the action configuration. The output of this action can be directly exported as a CSV file.

---
