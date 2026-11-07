---
url: >-
  https://docs.workato.com/en/connectors/gcp-biglake-iceberg/create-table-action.md
description: >-
  The Create table action registers a new table in a GCP BigLake Iceberg
  database.
---

# GCP BigLake Iceberg - Create table action

The **Create table** action registers a new table in a GCP BigLake Iceberg database. Point the metadata location at the table metadata JSON in Cloud Storage for GCP BigLake Iceberg tables.

## Input

| Input field | Description |
| --- | --- |
| Project ID | Enter the ID of the project you plan to create the table in. Defaults to the connection project ID. |
| Location | Enter the region of the catalog, such as `us-central1`. Defaults to the connection location. |
| Catalog ID | Enter the catalog that contains the database. |
| Database ID | Enter the database that contains the table. |
| Table ID | Enter the ID for the new table. |
| Storage location URI | Enter the Cloud Storage location of the table data, such as `gs://bucket/warehouse/db/table`. |
| Iceberg metadata location | Enter the Cloud Storage path to the Iceberg metadata JSON, such as `gs://bucket/warehouse/db/table/metadata/v1.metadata.json`. Optional. |

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
| Hive options | An object containing the table type, storage descriptor, including the location URI, input/output format, and serialization library, and parameters such as table type and Iceberg metadata location. |
