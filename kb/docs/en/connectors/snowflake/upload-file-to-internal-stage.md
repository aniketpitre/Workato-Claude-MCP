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
