---
url: 'https://docs.workato.com/en/connectors/s3-lake/list-tables-action.md'
description: >-
  The List tables action in the S3 Data Lake connector lets you retrieve all
  tables from a specified database in your AWS Glue data catalog.
---

# S3 Data Lake - List tables action

The **List tables** action retrieves all tables from a specified database in your AWS Glue Data catalog.

![S3 Data Lake – List tables action](/assets/s3-list-tables.CqcSMo3N.png)_S3 Data Lake – List tables action_

## Input

| Input field | Description |
| --- | --- |
| Database name | Select the name of the database to retrieve tables from. |
| Catalog | Select the data catalog. If left blank, the AWS account ID is used by default. |
| Expression | Provide a pattern to filter table names using a regular expression. |
| Max results | Set the maximum number of tables to return in the response. The minimum value is `1`, and the maximum value is `100`. |
| Transaction ID | Specify the transaction ID at which to read the table contents. |
| Query as of time | Provide a timestamp to query table contents as of a specific time. |
| Include status details | Choose whether to include AWS Glue view creation or update status. |
| Attributes to get | Select which table fields to include in the result. |

## Output

| Output field | Description |
| --- | --- |
| Tables | List of tables returned from the database. |
| Catalog ID | AWS Glue catalog ID used in the query. |
| Database name | Name of the database the tables belong to. |
| Is registered with lake formation | Indicates if the table is managed by Lake Formation. |
| Is row filtering enabled | Indicates if row-level filtering is enabled. |
| Name | Name of each table in the result. |
| Retention | Retention setting for each table. |
| Table type | Table type. |
| List size | Total number of results in the list. |
| List index | Position of each result in the returned list. |

---
