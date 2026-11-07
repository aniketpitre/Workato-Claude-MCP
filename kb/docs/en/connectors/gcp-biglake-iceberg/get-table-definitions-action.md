---
url: >-
  https://docs.workato.com/en/connectors/gcp-biglake-iceberg/get-table-definitions-action.md
description: >-
  The Get table definitions action retrieves the definition of a table
  registered in GCP BigLake Iceberg.
---

# GCP BigLake Iceberg - Get table definitions action

The **Get table definitions** action retrieves the definition of a table registered in GCP BigLake Iceberg.

## Input

| Input field | Description |
| --- | --- |
| Catalog ID | Enter the BigLake Metastore catalog that contains the database. |
| Database ID | Enter the database that contains the table. |
| Table ID | Enter the table you plan to retrieve. |
| Project ID | Enter the project you plan to retrieve tables from. Defaults to the connection project ID. |
| Location | Enter the region of the catalog. Defaults to the connection location. |

## Output

| Output field | Description |
| --- | --- |
| Table name | The full resource name of the table. |
| Type | The table type, such as `HIVE`. |
| ETag | The checksum used for concurrency control. |
| Create time | The timestamp when the table was created. |
| Update time | The timestamp when the table was last updated. |
| Delete time | The timestamp when the table was soft-deleted, if applicable. |
| Expire time | The timestamp when the table is permanently deleted, if applicable. |
| Hive options | An object containing the table type, storage descriptor, including location URI, input/output format, and serialization library, and parameters such as table type and Iceberg metadata location. |
