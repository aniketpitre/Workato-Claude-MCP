---
url: 'https://docs.workato.com/en/connectors/ibm-db2/insert-rows.md'
description: >-
  The Insert rows action in the IBM Db2 connector lets you insert multiple rows
  into a table or view in a single step and return inserted primary keys.
---

# IBM Db2 - Insert rows action

This action enables you to insert multiple rows in a single step.

## Input

<dl><dt>Table</dt><dd>Required field</dd><dd>Select the target table or view. You can also toggle the input to text mode, and enter the name of the table or view as text.</dd></dl>

<dl><dt>Rows &gt; Rows source list</dt><dd>Required field</dd><dd>The datapill is the source of the batched rows inserted into the table. Can originate from any trigger or action that generates a list datapill.</dd></dl>

<dl><dt>Rows &gt; Rows fields</dt><dd>Optional field</dd><dd>Dynamically-generated list of input fields, based on the columns in the target table. The Rows source list datapill provides the map for inserting data.</dd></dl>

## Output

<dl><dt>keys</dt><dd>Primary Key IDs of inserted rows. If inserting into a table without primary keys, this field is empty.</dd></dl>

<dl><dt>keys_count</dt><dd>Number of rows with inserted primary keys.</dd></dl>

---
