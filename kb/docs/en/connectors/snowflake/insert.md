---
url: 'https://docs.workato.com/en/connectors/snowflake/insert.md'
description: >-
  The Insert row action in the Snowflake connector lets you insert a single row
  into a selected table by mapping datapills to its columns.
---

# Snowflake - Insert actions

## Insert row

This action inserts a single row into the selected table.

![Insert row action](/assets/insert-row-action.D4yGq3Ww.png)_Insert row action_

### Table

First, select a table to insert a row into. This can be done either by selecting a table from the pick list, or toggling the input field to text mode and typing the full table name. Snowflake is case insensitive so you do not need to be precise with the case.

### Columns

Columns from the table you selected will be dynamically generated.

Next, map the datapills from your previous triggers or actions into their respective columns. The columns in the selected table are presented as input fields here for you to map datapills.

Data mapped into these fields will be inserted into the table when this action runs in a job.

---
