---
url: 'https://docs.workato.com/en/connectors/ibm-db2/select-rows.md'
description: >-
  The Select rows action in the IBM Db2 connector lets you retrieve rows from a
  table using WHERE, ORDER BY, LIMIT, and OFFSET filter options.
---

# IBM Db2 - Select rows action

Select specific data using common filter operators, such as `WHERE`, `LIMIT` and `OFFSET`. You can also specify which columns to return using the `Output columns` field.

Returns rows that match the `WHERE` condition from the selected table.

## Input

<dl><dt>Table</dt><dd>Required field</dd><dd><span>Select the target table or view. You can also toggle the input to text mode, and enter the name of the table or view.</span></dd></dl>

<dl><dt>WHERE condition</dt><dd>Optional field</dd><dd><span>The <code>WHERE</code> condition to filter rows.</span></dd></dl>

<dl><dt>Parameters</dt><dd>Optional field</dd><dd><span>Use in conjunction with the <code>WHERE</code> condition to prevent SQL injection attacks. After declaring the named bind variables in your <code>WHERE</code> input, assign values to these variables using this input field.</span></dd></dl>

<dl><dt>Order by</dt><dd>Optional field</dd><dd><span>Order of rows to return, such as <code>updated_at DESC</code>.</span></dd></dl>

<dl><dt>Quota</dt><dd>Optional field</dd><dd><span>The maximum number of rows to return. The default is <strong>100</strong>, and the highest possible number of rows is <strong>50000</strong> rows.</span></dd></dl>

<dl><dt>Offset</dt><dd>Optional field</dd><dd><span>The option to fetch only a page of results from the entire results set.<br><br>For example, to skip the first 100 rows of the selected results set, input 100 to this field.<br><br>The default is 0.</span></dd></dl>

<dl><dt>Output columns</dt><dd>Optional field</dd><dd><span>Define specific columns to retrieve from the target table. By default, retrieves all columns.</span></dd></dl>

<dl><dt>Output CSV?</dt><dd>Optional field</dd><dd><span>Select <strong>Yes</strong> to output a CSV string of the selected data.</span></dd></dl>

## Output

<dl><dt>rows</dt><dd>Array of JSON objects, where each object represents a retrieved row.</dd></dl>

<dl><dt>rows_count</dt><dd>Number of reetrieved rows</dd></dl>

---
