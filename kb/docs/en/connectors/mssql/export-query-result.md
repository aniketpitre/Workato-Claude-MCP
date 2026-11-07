---
url: 'https://docs.workato.com/en/connectors/mssql/export-query-result.md'
description: >-
  The Export query result action in the SQL Server connector runs a SQL query
  and exports the results as a CSV file over cloud or on-prem connections.
---

# SQL Server - Export query result action

This action executes a SQL query and exports the results as a CSV file.

> **ON-PREM PROFILE CONFIGURATION**
> 
> Remember to configure a staging area in your on-prem agent profile. Learn how to set up a staging area in the [OPA server profile](/en/on-prem/agents/connection/profile#server-profile).

## On-prem and Cloud connection input fields

The **Export query result** action provides an additional input field if your connection is established through on-prem rather than using a cloud-based connection. If you have an on-prem connection, the **Upload URL** field displays. This field enables you to export your CSV file to a URL you specify.

![Export query result action on-prem connection](/assets/export-query-result.3xaEu6xm.png)_Export query result action with a on-prem connection_

![Export query result action cloud connection](/assets/sql-export-action.C3HJFxHh.png)_Export query result action with a cloud connection_

## Input

| Input field | Description |
| --- | --- |
| SQL | Enter a valid SQL query. For example: `SELECT * FROM PUBLIC.ACCOUNTS` |
| Column delimiter | Choose a delimiter character. CSV files typically use a comma. |
| Upload URL | Export your CSV file to a URL you specify. You can generate this URL by using [On-prem files](/en/connectors/on-prem-files/generate-on-prem-file-url) or [Amazon S3](/en/connectors/s3/action-presign-url). **Note** that this field is only available if you have an on-prem connection. Refer to [On-prem and Cloud connection input fields](#on-prem-and-cloud-connection-input-fields) for more information. |

## Output

The output of this action contains metadata about the file export.

| Output field | Description |
| --- | --- |
| Number of rows exported | The number of rows exported. |
| Column names | The column header names in the CSV file. |

> **CSV FILE CONTENT**
> 
> This action does NOT return the CSV file content.

---
