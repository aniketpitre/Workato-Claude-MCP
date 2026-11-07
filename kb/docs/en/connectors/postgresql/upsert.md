---
url: 'https://docs.workato.com/en/connectors/postgresql/upsert.md'
description: >-
  The Upsert rows batch action in the PostgreSQL connector inserts or updates
  multiple rows in one call based on primary key values.
---

# PostgreSQL - Upsert rows action (batch)

The **Upsert rows** batch action inserts or updates multiple rows in a single call. The action uses a list datapill as the source of rows and determines whether to insert or update based on the provided primary key values.

![Upsert batch of rows action](/assets/upsert-rows-batch-action.BTCPTKX3.png)_Upsert batch of rows action_

## Input

| Input field | Description |
| --- | --- |
| Table | Select the target table from the picklist, or enter the full table name. |
| Rows source list | Provide a list datapill from a trigger or previous action as the source of rows. If you provide a non-list datapill, the action upserts only one row. |
| Columns | Map datapills from the source list into the table columns. Each row in the list must include the primary key values to determine whether to insert or update. Only datapills from the list source are iterated. Datapills mapped from outside the list apply the same value to all rows. Refer to the [List management](/en/features/list-management) guide for more information about working with batches. |

> **CHARACTER LIMITS**
> 
> Columns in your PostgreSQL table have a character limit. The connector stores only the characters up to the defined limit if you map a value that exceeds it. It doesn't return an error. PostgreSQL returns an error when you insert the same value directly.

## Output

| Output field | Description |
| --- | --- |
| Number of rows upserted | The number of rows that were inserted or updated. |

---
