---
url: 'https://docs.workato.com/en/connectors/databricks/delete-rows.md'
description: >-
  The Delete rows in table action removes one or more rows from a selected
  Databricks table.
---

# Databricks – Delete rows in table action

The **Delete rows in table** batch action removes one or more rows from a selected Databricks table. Select the target table and define a `WHERE` condition to filter the rows you plan to delete.

## Input

| Input field | Description |
| --- | --- |
| Table | Select the Databricks table where you plan to delete rows. Only the first 1,000 tables are displayed. Enter the table name if it doesn't appear in the drop-down menu. |
| WHERE condition | Enter a SQL `WHERE` clause to filter the rows you plan to delete. For example: `currency = 'USD'`. Enclose string values in single quotes. |

## Output

| Output field | Description |
| --- | --- |
| Number of rows deleted | The number of rows that matched the `WHERE` condition and were successfully deleted. |

---
