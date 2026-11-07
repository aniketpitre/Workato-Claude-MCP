---
url: >-
  https://docs.workato.com/en/connectors/gcp-biglake-iceberg/query-data-action.md
description: >-
  The Query data action runs a SQL query against GCP BigLake Iceberg tables
  using a BigQuery query job.
---

# GCP BigLake Iceberg - Query data action

The **Query data** action runs a SQL query against GCP BigLake Iceberg tables using a BigQuery query job. This is a long-running action that polls until the job completes and returns rows.

## Input

| Input field | Description |
| --- | --- |
| SQL query | Enter the GoogleSQL query you plan to use. |
| Project ID | Enter the ID of the project you plan to query. Defaults to the connection project ID. |
| Location | Enter the job location. Defaults to the connection location. |
| Max results | Enter the maximum number of rows to return. |

## Output

| Output field | Description |
| --- | --- |
| Kind | The resource type, such as `bigquery#getQueryResultsResponse`. |
| ETag | The checksum used for concurrency control. |
| Schema | An object listing the field names, types, modes, and descriptions for the returned rows. |
| Rows | An array of result rows. Each row contains a list of cell values in the same order as the schema fields. |
| Total rows | The total number of rows in the query result. |
| Job complete | Whether the query job has completed. |
| Cache hit | Whether the query results were fetched from the query cache. |
| Total bytes processed | The total number of bytes processed for the query. |
| Job reference | An object containing the project ID, job ID, and location of the job. |
