---
url: 'https://docs.workato.com/en/connectors/s3-lake/table-definition-action.md'
description: >-
  The Get table definitions action in the S3 Data Lake connector lets you
  retrieve metadata for a table you specify in the AWS Glue data catalog.
---

# S3 Data Lake - Get table definitions action

The **Get table definitions** action retrieves metadata for a table you specify in the AWS Glue data catalog.

![Get table definitions](/assets/s3-get-table-definitions.D3j84fMl.png)_S3 Data Lake – Get table definitions action_

## Input

| Input field | Description |
| --- | --- |
| Database name | Select the catalog database where the table resides. |
| Table name | Enter the name of the table to retrieve metadata for. |
| Catalog | Select the data catalog where the table is stored. If left blank, AWS uses the default catalog for your account. |
| Transaction ID | Enter the transaction ID to read the table as of a specific transaction state. |
| Query as of time | Specify a timestamp to read the table contents as of that point in time. If omitted, the latest state is used. |
| Include status details | Choose whether to include status details for AWS Glue data catalog view operations. |

## Output

| Output field | Description |
| --- | --- |
| Table | Object containing the full table definition. |
| Catalog ID | The AWS catalog ID that owns the table. |
| Catalog identifier | Alias or identifier for the catalog source. |
| Create time | Timestamp when the table was created. |
| Created by | User or role that created the table. |
| Database ID | Unique ID of the associated database. |
| Database name | Name of the catalog database. |
| Description | Description of the table. |
| Is multi dialect view | Indicates if the table supports multiple dialects. |
| Is registered with lake formation | Shows whether the table is registered with lake formation. |
| Is row filtering enabled | Indicates if row-level filtering is active. |
| Name | Table name. |
| Parameters | Key-value map of table parameters. |
| Retention | Retention period of the table. |
| Storage descriptor | Information about the table's storage format, schema, and location. |
| Table type | Classification of the table. |
| Update time | Timestamp of the most recent update. |
| Version ID | ID for the version of the table definition. |

---
