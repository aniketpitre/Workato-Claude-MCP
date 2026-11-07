---
url: 'https://docs.workato.com/en/connectors/postgresql/update.md'
description: >-
  The Update rows action in the PostgreSQL connector applies one set of values
  to all rows in a table that match a WHERE condition.
---

# PostgreSQL - Update rows action

The **Update rows** action updates one or more rows in a PostgreSQL table with a single set of values. This action applies the same update to rows that match the specified `WHERE` condition.

![Update rows action](/assets/update-row-action.BIYcW5l9.png)_Update rows action_

## Input

| Input Field | Description |
| --- | --- |
| Table | Select the target table from the picklist, or enter the full table name. |
| WHERE condition | Define the condition to filter the rows you plan to update. All matching rows receive the same updated values. You can use simple expressions like `id = 123`, or complex expressions with subqueries. Refer to the [WHERE condition](/en/connectors/postgresql#where-condition) guide for more information. |
| Columns | Map datapills into the input fields that correspond to the table columns. |

> **CHARACTER LIMITS**
> 
> Columns in your PostgreSQL table have a character limit. The connector stores only the characters up to the defined limit if you map a value that exceeds it. It doesn't return an error. PostgreSQL returns an error when you insert the same value directly.

## Output

| Output field | Description |
| --- | --- |
| Number of rows updated | The number of rows that matched the condition and were updated. |

---
