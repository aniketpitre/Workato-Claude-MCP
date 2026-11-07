---
url: 'https://docs.workato.com/en/connectors/ibm-db2/delete-rows.md'
description: >-
  The Delete rows action in the IBM Db2 connector lets you delete rows that
  match a WHERE condition, permanently removing matching data from a table.
---

# IBM Db2 - Delete rows action

This action lets you delete rows based on certain criteria defined by a `WHERE` condition.

> **WARNING**
> 
> This action should be tested and used with care, as it will PERMANENTLY delete rows in your table.

## Input

<dl><dt>Table</dt><dd>Required field</dd><dd><span>Select the target table or view. Optionally, toggle the input to text mode to enter the name of the table or view name as text.</span></dd></dl>

<dl><dt>WHERE condition</dt><dd>Optional field</dd><dd><span>Specify the condition that must match the rows that the system deletes.<br><strong>Warning:</strong> If this field is blank, the system deletes all rows.</span></dd></dl>

## Output

<dl><dt>Rows affected</dt><dd>The number of deleted rows.</dd></dl>

---
