---
url: 'https://docs.workato.com/en/connectors/databricks/export-result.md'
description: >-
  The Export query result as CSV file action executes a SQL query and writes the
  result to a CSV file.
---

# Databricks – Export query result as CSV file action

The **Export query result as CSV file** action runs a SQL `SELECT` query and writes the result to a downloadable CSV file.

## Input

| Input field | Description |
| --- | --- |
| SQL | Enter the SQL `SELECT` query to export. |
| Column delimiter | Select the character that separates each column in the CSV file. Most CSV files use a comma. |
| Timeout limit (minutes) | Set the maximum time to wait for the export job to complete. Workato moves to the next step without waiting if the job takes longer than this limit. Maximum allowed is 120 minutes. |

## Output

| Output field | Description |
| --- | --- |
| Number of rows exported | The number of rows returned by the query and written to the CSV file. |
| Column names | The list of column headers from the query result. |
| File content | The binary content of the generated CSV file. Use this with file actions or exports. |

---
