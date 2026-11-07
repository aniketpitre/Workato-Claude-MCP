---
url: 'https://docs.workato.com/en/connectors/postgresql/insert.md'
description: >-
  The Insert row action in the PostgreSQL connector lets you add a single row to
  a selected table and return the new row's primary key.
---

# PostgreSQL - Insert row action

The **Insert row** action adds a single row to a selected PostgreSQL table.

![Insert row action](/assets/insert-row-action.Bz9D1mis.png)_Insert row action_

## Input

| Input field | Description |
| --- | --- |
| Table | Select the target table from the picklist, or enter the full table name. |
| Columns | Map datapills into the input fields that correspond to the table columns. |

> **CHARACTER LIMITS**
> 
> Columns in your PostgreSQL table have a character limit. The connector stores only the characters up to the defined limit if you map a value that exceeds it. It doesn't return an error. PostgreSQL returns an error when you insert the same value directly.

## Output

| Output field | Description |
| --- | --- |
| Inserted key | The primary key value of the newly inserted row. |

---
