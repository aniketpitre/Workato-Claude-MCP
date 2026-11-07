---
url: 'https://docs.workato.com/en/connectors/jdbc/export-query-result.md'
description: >-
  The Export query result action in the JDBC connector lets you export the data
  from a SQL query to a CSV or delimited file at an upload URL.
---

# JDBC - Export query result action

This action exports the data from a valid SQL query to a specific file.

> **On-prem profile configuration**
> 
> Remember to configure a staging area in your on-prem agent profile. Learn how to set up a staging area in the [OPA server profile](/en/on-prem/agents/connection/profile#server-profile).

![Export query result](/assets/export-query-result.pn2j77Vi.png)_Export query result_

## Input

### SQL

First, you must enter into the field a table to export from. If you are having trouble finding a table, you can change the action to select rows and find a value from the table section there. After a valid table is entered, it should be limited by something such as select so it can be exported to a file.

### Column delimiter

For the column delimiter, you can choose between several options to separate the table. CSV files typically use comma.

### Upload URL

This is the CSV file that the result of the query is going to be exported to. You can generate this url using [On-prem files](/en/connectors/on-prem-files/generate-on-prem-file-url) or [Amazon S3](/en/connectors/s3/action-presign-url).

## Example recipe

If you are having trouble figuring out how to do this, view this [example recipe.](https://www.workato.com/recipes/1204600?st=445148)

---
