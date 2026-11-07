---
url: 'https://docs.workato.com/en/connectors/ibm-db2/upsert-rows.md'
description: >-
  The Upsert rows action in the IBM Db2 connector lets you insert or update
  multiple rows in a single batch step using a unique key to deduplicate rows.
---

# IBM Db2 - Upsert rows action (batch)

This action allows you to perform an upsert (insert or update) of multiple rows in a single step.

The action checks if input data is in the table. If present, the system performs an update. Otherwise, it adds the data as a new row (insert).

## Input

<dl><dt>Table</dt><dd>Required field</dd><dd>Select the target table or view. You can also toggle the input to text mode, and enter the table or view name as text.</dd></dl>

<dl><dt>Rows &gt; Rows source list</dt><dd>Required field</dd><dd>The datapill that is the source of the batch of rows to insert into the table. Can originate from any trigger or action that returns a list datapill.</dd></dl>

<dl><dt>Rows &gt; Rows fields</dt><dd>Optional field</dd><dd>Dynamically-generated list of input fields, based on the columns in the target table. Map the data from the Rows source list datapill.</dd></dl>

<dl><dt>Unique key</dt><dd>Required field</dd><dd>Select a unique key column to deduplicate rows.&lt;br/ &gt;&lt;br/ &gt;When you index the selected unique key, it improves the performance of the upsert action.</dd></dl>

## Output

<dl><dt>Rows affected</dt><dd>Number of upserted rows.</dd></dl>

---
