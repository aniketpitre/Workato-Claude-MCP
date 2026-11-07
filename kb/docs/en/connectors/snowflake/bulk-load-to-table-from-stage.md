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
