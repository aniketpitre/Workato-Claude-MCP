---
url: >-
  https://docs.workato.com/en/connectors/gcp-biglake-iceberg/list-tables-action.md
description: >-
  The List tables action lists all tables in the specified GCP BigLake Iceberg
  database.
---

# GCP BigLake Iceberg - List tables action

The **List tables** action lists all tables in the specified GCP BigLake Iceberg database.

## Input

| Input field | Description |
| --- | --- |
| Catalog ID | Enter the ID of the BigLake Metastore catalog that contains the database. |
| Database ID | Enter the database whose tables you plan to list. |
| Project ID | Enter the ID of the project that contains the database. Defaults to the connection project ID. |
| Location | Enter the region of the catalog. Defaults to the connection location. |
| View | Select the level of detail to return, such as `BASIC` or `FULL`. Defaults to `BASIC`. |
| Page size | Enter the maximum number of tables to return (1-1000). |
| Page token | Enter the token from a previous response to fetch the next page. |

## Output

| Output field | Description |
| --- | --- |
| Tables | A list of tables. Each table includes its name, type, ETag, timestamps, and Hive options such as the storage descriptor and parameters. |
| Next page token | Token to fetch the next page of results, if more tables are available. |
