---
url: 'https://docs.workato.com/en/connectors/bigquery/select.md'
description: >-
  The Select rows batch action retrieves rows from a Google BigQuery table using
  WHERE predicates.
---

# Google BigQuery - Select rows action (batch)

The **Select rows** batch action retrieves rows from a Google BigQuery table using `WHERE` predicates. This action filters rows that meet the specified criteria. If the query takes longer than 60 seconds and **Wait for query to complete?** is set to **No**, the action returns only the job ID. Use the [Get batch of rows by Job ID action](/en/connectors/bigquery/get-query-result-action) to retrieve results later.

## Input

| Input field | Description |
| --- | --- |
| Project | Select the project to bill for the query. |
| Dataset | Select the dataset that contains the target table. |
| Table | Select the table to query from the dataset. |
| Location | Choose the region to run the query. |
| Output columns | Select the columns to return. Limiting output fields can improve performance. |
| WHERE Predicates | Define filter conditions to retrieve matching rows. All predicates are joined with `AND`. For complex filtering, use custom SQL. |
| Order by | Specify the column(s) and sort direction. For example: `priority asc, created_date desc`. |
| Limit | Set the maximum number of rows to return. The default and maximum is `50000`. Leave blank to return the full result set. |
| Offset | Skip a number of rows in the result. For example, input `100` to skip the first 100 rows. The default is `0`. |
| Wait for query to complete? | Set to **Yes** to wait for the query to finish. If set to **No**, the action returns after 60 seconds with only the job ID. Use the [Get batch of rows by Job ID action](/en/connectors/bigquery/get-query-result-action) to retrieve results. |
| Table Fields | Required if the **Table** field uses a datapill. Specify the table schema. It must match across all possible values of the datapill. |

## Output

| Output field | Description |
| --- | --- |
| Output contains rows? | Indicates whether the result includes row data. |
| Rows | An array of row objects. Each datapill represents a column value. |
| Kind | The type of job executed. This should be `queryResponse`. |
| Job reference | Includes the project ID, job ID, and query location. You can use the [Get batch of rows by Job ID action](/en/connectors/bigquery/get-query-result-action) to retrieve additional rows. |
| Total rows | Total number of rows returned by the query. |
| Page token | Token to retrieve the next page of results. |
| Schema | The schema of the query result. |
| Etag | A hash representing the result schema. |
| Total bytes processed | The number of bytes the query processed. This contributes to your BigQuery billing. |
| Job complete | Status of the query job. Returns `Done` if the job completed successfully. |
| Cache hit | Returns `true` if the result came from the query cache. Returns `false` otherwise. |

---
