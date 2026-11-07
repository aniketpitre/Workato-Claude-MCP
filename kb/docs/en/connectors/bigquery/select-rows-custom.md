---
url: 'https://docs.workato.com/en/connectors/bigquery/select-rows-custom.md'
description: Run a custom SQL query in Google BigQuery and retrieve matching rows.
---

# Google BigQuery - Select rows using custom SQL action (batch)

The **Select rows using custom SQL** batch action allows you to run a custom SQL query and retrieve matching rows from Google BigQuery. This action supports parameterized queries using bind variables. If the query runs longer than 60 seconds and **Wait for query to complete?** is set to **No**, the action returns the job ID and completes asynchronously. Use the **Get batch of rows by Job ID** action to retrieve the results later.

> **50,000 RECORD QUOTA**
> 
> Starting February 8, 2026, the **Select rows using custom SQL** action returns a maximum of 50,000 records for all **new recipes and existing recipes that don't currently exceed this quota**. Starting March 15, 2026, this quota extends to **all recipes** using this action, including existing recipes that currently exceed the quota.
> 
> Recipes configured to retrieve more than 50,000 records will be truncated to this quota.
> 
> This change improves platform reliability and performance while preventing large queries from overloading database connections or impacting upstream systems.

### Input

| Input field | Description |
| --- | --- |
| Project | Select the project to bill for the query. |
| Query | Enter the SQL query to run. Use the `@` symbol to declare bind variables. |
| Parameters | Map bind variables used in the query. For example, for `select * from table where id = @id`, provide a parameter named `id`. |
| Output fields | Define the expected output fields. The names must match the columns returned by the query. |
| Location | Select the region to run the query. Optional in most cases. |
| Wait for query to complete? | Set to `true` to wait for the full query execution. Set to `false` to return only the Job ID after 60 seconds. Use the [Get batch of rows by Job ID action](/en/connectors/bigquery/get-query-result-action) to retrieve the results. |

### Output

| Output field | Description |
| --- | --- |
| Output contains rows? | Indicates whether the result includes row data. |
| Rows | An array of row objects. Each datapill corresponds to a column in the result. |
| Kind | The type of job executed. This should be `queryResponse`. |
| Job reference | Includes the project ID, job ID, and location of the job. Use this with the [Get batch of rows by Job ID action](/en/connectors/bigquery/get-query-result-action) to retrieve more rows. |
| Total rows | Total number of rows returned by the query. |
| Page token | Token to retrieve the next page of results. |
| Schema | The schema of the query result, including column names and types. |
| Etag | A hash representing the result schema. |
| Total bytes processed | The number of bytes processed by the query. This counts toward your BigQuery billing. |
| Job complete | Status of the query job. Returns `Done` if the job completed successfully. Returns `Pending` if the job is still running. |
| Cache hit | Returns `true` if the query result was served from cache. Returns `false` otherwise. |

---
