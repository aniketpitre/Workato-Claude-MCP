---
url: 'https://docs.workato.com/en/connectors/bigquery/run-custom-sql.md'
description: >-
  The **Run custom SQL** action allows you send a SQL string to Google BigQuery
  to be executed.
---

# Google BigQuery - Run custom SQL action

The **Run custom SQL** action allows you to send an SQL string to Google BigQuery to be executed. You can use this action when your SQL transaction spans multiple queries or when you need to run DML statements.

> **1 MB QUERY SIZE QUOTA**
> 
> Starting 1 December 2025, the **Run custom SQL** action in this connector enforces a 1 MB query size quota. This change improves platform reliability, increases performance, and avoids large queries that overload database connections or impact upstream systems.

> **OUTPUT DOES NOT CONTAIN ROWS**
> 
> This action does not return any row data. For custom SQL that does return rows, use our **Get batch of rows by Job ID** action to retrieve the resultant rows.

## Input

| Input field | Description |
| --- | --- |
| Project | Select the project to bill for the query. |
| Dataset | Select the dataset to pull tables from. |
| Location | Select the geographical location of where the job should run. This field isn't required in most cases. |
| Query | Enter the SQL Statement to execute. The query size is limited to 1 MB. |
| Use legacy SQL | Toggle to `true` to use legacy SQL. Normally not configured. |

## Output

| Output field | Description |
| --- | --- |
| ID | The ID of the job completed. |
| Kind | The type of the Google BigQuery job. |
| Job Reference | Contains information about the job, such as the project ID, job ID and location. |
| State | State of job. Most often, this value will be "DONE". |
| Statistics | Contains information about the query time and total bytes processed by the job. |
| Configuration | Contains information about the query configuration. |
| Status | Contains error results and messages if any. |
| User email | Email of the user who ran the job. |

## Permission denied while getting Drive credentials

You may see the following error when you run a run custom SQL action in Google BigQuery:

```text
Access Denied: BigQuery BigQuery: Permission denied while getting Drive credentials
```

### Why it happens

This error occurs when the BigQuery service account doesn't have permission to access Google Drive files referenced in your query.

### How to troubleshoot

Complete the following steps to resolve the issue:

1. Check if your SQL query references an external table or file stored in Google Drive.
   
2. Open each linked file in Google Drive, click **Share**, and add the BigQuery service account email with **Viewer** or **Editor** access.
   
3. Go to your Google Cloud Console and confirm that Drive access is enabled for the BigQuery project.
   
4. Contact your Google Cloud administrator or support to verify Drive access configuration if the issue continues.

---
