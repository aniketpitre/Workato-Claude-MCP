---
url: 'https://docs.workato.com/en/connectors/bigquery/select-rows-custom-insert.md'
description: >-
  Run a custom SQL query in Google BigQuery and insert the results into a
  destination table. Use this action to stage or transform data for later use.
---

# Google BigQuery - Select rows using custom SQL and insert into table (batch)

The **Select rows using custom SQL and insert into table** batch action runs a custom SQL query and writes the results to a destination table. Use this to stage or transform data for downstream use. If the query takes longer than 60 seconds, the action switches to asynchronous mode unless **Wait for query to complete?** is set to **Yes**.

This action returns the first page of results and may include a next page token. Use the [Get batch of rows by Job ID action](/en/connectors/bigquery/get-query-result-action) to retrieve additional results if needed.

### Input

| Input field | Description |
| --- | --- |
| Project | Select the project to bill for the query. |
| Query | Enter the SQL query to execute. Use `@` to declare bind variables. |
| Parameters | Map bind variables declared in the query. For example, if the query is `select * from table where id = @id`, provide a parameter named `id`. |
| Output fields | Define the expected output fields. These must match the column names returned by the query. |
| Location | Select the region where the query should run. |
| Wait for query to complete? | Set to **Yes** to wait until the query finishes running. If set to **No**, the action waits 60 seconds before returning only the job ID. Use the [Get batch of rows by Job ID action](/en/connectors/bigquery/get-query-result-action) to retrieve results later. |
| Destination table | Enter the table where query results should be written. |
| Create disposition | Control whether the action creates the destination table. Click **Create if needed** to create the table if it doesn't exist. Click **Never create** to return an error if the table doesn't exist. |
| Write disposition | Control how the action writes data to the destination table. Click **Write truncate** to overwrite the table. Click **Write append** to append rows. Click **Write empty** to return an error if the table already contains data. |

### Output

| Output field | Description |
| --- | --- |
| Rows | An array of row objects. Each datapill corresponds to a column in the result. |
| Kind | The type of job executed. For successful queries, this is `queryResponse`. |
| Job reference | Contains the project ID, job ID, and location for the executed job. You can use the [Get batch of rows by Job ID action](/en/connectors/bigquery/get-query-result-action) to retrieve more results. |
| Total rows | Total number of rows returned by the query. |
| Page token | Token to retrieve the next page of results. |
| Schema | The schema of the query result. |
| Etag | A hash representing the result schema. |
| Total bytes processed | The number of bytes processed by the query. This counts toward your BigQuery billing. |
| Job complete | Status of the query job. This should be `Done` if completed. |
| Cache hit | Returns `true` if the query result was served from cache. Returns `false` otherwise. |

---
