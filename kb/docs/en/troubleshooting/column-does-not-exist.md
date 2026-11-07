---
url: 'https://docs.workato.com/en/troubleshooting/column-does-not-exist.md'
description: >-
  Learn why the UndefinedColumn SQL error occurs in Workato when a query
  references a missing column, and how to troubleshoot and resolve it.
---

# UndefinedColumn - Column does not exist

You may encounter the following SQL error when you run queries:

```text
UndefinedColumn - Column does not exist
```

This error indicates that the database can't find the specified column. It often occurs when the underlying table has changed column names.

![Example of Column does not exist](/assets/column-does-not-exist.M0BclztH.png)_Example of Column does not exist_

## Why it happens

This error can occur for the following reasons:

- A column name in the SQL statement doesn't match any column in the table.
- The query includes unintended column names in **Order by** or **Where** conditions.
- The recipe uses outdated schema information from a previous step.

## How to troubleshoot

Complete the following steps to resolve the issue:

1. Verify the column names in your query. Ensure that each column exists in the table schema.
   
2. Check the input fields for unintended column names. Columns in **Order by** or **Where** clauses can also cause this error.
   
3. Confirm with your database administrator that the required columns exist in the table.
   
4. Refresh the recipe to update the schema from your connections if your recipe uses a datapill from a previous step.

---
