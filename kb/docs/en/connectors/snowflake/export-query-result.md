---
url: 'https://docs.workato.com/en/connectors/snowflake/export-query-result.md'
description: >-
  The Export query result action in the Snowflake connector runs a SQL query and
  exports the results as a CSV file you can stream.
---

# Snowflake - Export query result action

The **Export query result** bulk long action executes a SQL query and exports the results as a CSV file. You can stream the exported CSV content through the File content datapill. The maximum timeout for this action is **120 minutes**.

![Export query result action](/assets/export-query-result.C48DDtNT.png)_Export query result action_

## Input

| Input field | Description |
| --- | --- |
| SQL | Enter a valid SQL query. For example, `SELECT * FROM PUBLIC.ACCOUNTS`. |
| Column delimiter | Choose a delimiter character. CSV files typically use **comma**. |
| Timeout limit | Specify an upper limit for the action. If any asynchronous jobs exceed this limit, the recipe proceeds to the next step. The maximum timeout is 120 minutes. |

## Output

The output of this action contains metadata about the export action.

| Output field | Description |
| --- | --- |
| Number of rows exported | The number of rows exported. |
| Column names | Column headers in the CSV file. |
| File content | CSV stream of the contents of the file. |

> **REFRESH SCHEMA TO DISPLAY FILE CONTENTS DATAPILL**
> 
> If the File content datapill doesn't appear in the output datatree of this action, click **Refresh** to regenerate the output fields.
> 
> ![Click Refresh to regenerate the output fields](/assets/refresh-schema.D2esM1Kg.gif)_Click **Refresh** to regenerate the output fields_

---

---
url: >-
  https://docs.workato.com/en/connectors/snowflake/upload-file-to-internal-stage.md
description: >-
  The Upload file to internal stage action in the Snowflake connector lets you
  load a CSV or FileStorage file to an internal stage using PUT.
---

# Snowflake - Upload file to internal stage action

Workato offers bulk loading of data to an internal stage in Snowflake. This action uses the Snowflake `[PUT](https://docs.snowflake.com/en/sql-reference/sql/put)` to upload files to Snowflake internal stage. This action takes in either a CSV file, or a [Workato FileStorage](/en/features/workato-filestorage#workato-filestorage) file path, and uploads it to the specified internal stage.

This action gives you the flexibility of using any type of internal stage. It is intended to work together with Workato bulk triggers (Jira, Marketo, and so on), and also works well when building [ELT/ETL recipes](/en/features/etl-elt-guide#data-orchestration-etl-elt). It also works together with the [bulk load from stage action](/en/connectors/snowflake/bulk-load-to-table-from-stage) to bring data from an external source to a Snowflake table.

## Input

| Input field | Description |
| --- | --- |
| Source Type | Specify the source of your data. It can be the contents of a CSV file, referenced as a File Contents datapill, or a Workato FileStorage path. |
| Internal Stage | Specify the internal stage to load data into. The action provides you with a picklist of named stages. Otherwise specify the name of your stage. |
| Overwrite | Specify whether to overwrite an existing file in the internal stage with the same name during upload. **Defaults to `No`.** |
| Auto Compress | Specify whether Snowflake should use gzip to compress file(s) during upload. If left unspecified, auto compression will be applied. |

## Output

| Output field | Description |
| --- | --- |
| Status | Indicates status of file upload to internal stage returned by Snowflake. |
| Target file path | Indicates the complete file location within the internal stage. **Note:** Use this datapill to reference the file in subsequent steps of the recipe. |
| Target file size | Indicates the uploaded file size (bytes). |
| Source compression | Indicates the compression of the source file. |
| Target compression | Indicates the compression applied to the uploaded file. |

---

---
url: >-
  https://docs.workato.com/en/connectors/snowflake/bulk-load-to-table-from-stage.md
description: >-
  The Bulk load to table from stage action in the Snowflake connector lets you
  load a staged file into a target table using the COPY command.
---

# Snowflake - Bulk load to table from stage action

[Video](https://www.youtube.com/embed/QMeYjd2A0Nc?rel=0&rel=0)

Load a file from a Snowflake stage into a target table. This action uses the [COPY](https://docs.snowflake.net/manuals/sql-reference/sql/copy-into-table.html#output) command to load data directly from a stage to a target table. When working with internal stages, you should use this action together with "[Bulk load to an internal stage](/en/connectors/snowflake/upload-file-to-internal-stage)".

This action will execute the load and wait for completion before moving onto the next step. Load time depends on the size of source file, number of columns, additional validation in the target table and network speed (faster if loading data from S3 to an AWS-deployed Snowflake instance). **1 GB** CSV file with **30 columns** and **3 million rows** will take 60 seconds.

The source file can contain data in CSV format, JSON, PARQUET, and [other semi-structured file types](https://docs.snowflake.net/manuals/sql-reference/sql/copy-into-table.html#format-type-options-formattypeoptions).

## Input

| Input field | Description |
| --- | --- |
| Table | Select a target table to load data into. Typically, this is a staging table for loading data. Subsequently, rows in this table is merged into your production table. |
| Stage name | Select an existing stage in Snowflake. If a file is not specified in this stage, all new files will be loaded. If using an external stage, this external stage should contain information about file location, AWS credentials, encryption, and file format details. Learn how to create an [S3 external stage](https://docs.snowflake.net/manuals/user-guide/data-load-s3-create-stage.html). |
| File name | Specify a list of one or more file names (separated by commas) to be loaded. If left unspecified, all files from the stage will be loaded. Ensure that these files have already been staged in either the Snowflake internal or external stage. [Learn more](https://docs.snowflake.com/en/sql-reference/sql/copy-into-table#optional-parameters). |
| [File Format](#file-format) | Specify the file format you would like to apply to the data. By default, the Snowflake default format will be applied to the `COPY` command. |

## Output

| Output field | Description |
| --- | --- |
| Source file name | Relative path and name of the source file. **Sample Values:** **External Stage**: s3://bucket-name/parent\_folder/file\_name.csv **Internal Stage**: @stage\_name/folder/file\_name.csv |
| Status | 
| Values | Description |
| --- | --- |
| LOADED | All rows successfully loaded. |
| LOAD FAILED | Unsuccessful load. Entire data file was not loaded. |
| PARTIALLY LOADED | Unsuccessful load. Data file was partially loaded. Use **First error line** to find out exactly where the load failed. |

 |
| Rows parsed | Number of rows read from the source file. |
| Rows loaded | Number of rows successfully loaded from the source file into target table. |
| Error quota | If the number of errors reaches this quota, then abort the load. This is typically **0**, meaning that the load will abort on the first error. |
| Errors seen | Number of rows with error in the source file. |
| First error | Error details of the first error in the source file. |
| First error line | Line number of the first row that caused an error. |
| First error character | Position of the first character that caused an error. |
| First error column name | Column name where the first error occurred. |

---
