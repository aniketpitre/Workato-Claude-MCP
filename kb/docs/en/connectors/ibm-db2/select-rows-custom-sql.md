---
url: 'https://docs.workato.com/en/connectors/ibm-db2/select-rows-custom-sql.md'
description: >-
  The Select rows using custom SQL action in the IBM Db2 connector lets you
  retrieve rows that match a custom SQL query with bind variables.
---

# IBM Db2 - Select rows using custom SQL action

This action lets you select rows that match a custom SQL query.

Learn about some [Improving the performance of SQL procedures](https://www.ibm.com/docs/en/db2/11.5?topic=procedures-improving-performance-sql).

> **50,000 RECORD QUOTA**
> 
> Starting February 8, 2026, the **Select rows using custom SQL** action returns a maximum of 50,000 records for all **new recipes and existing recipes that don't currently exceed this quota**. Starting March 15, 2026, this quota extends to **all recipes** using this action, including existing recipes that currently exceed the quota.
> 
> Recipes configured to retrieve more than 50,000 records will be truncated to this quota.
> 
> This change improves platform reliability and performance while preventing large queries from overloading database connections or impacting upstream systems.

## Input

<dl><dt>SQL</dt><dd>Required field</dd><dd><span>The custom SQL statement that runs on selected rows. This generates the output datatree.<br><br>Wrap datapills in single quote characters, <code>'</code>.<br><br>Do not add a <code>;</code> at the end of your SQL query; this causes the step to fail.<br><br>Do not add a LIMIT clause to restrict query size. Use the Limit input field instead.</span></dd></dl>

<dl><dt>Parameters</dt><dd>Optional field</dd><dd><span>Assign values to your bind variables</span></dd></dl>

<dl><dt>Order by</dt><dd>Optional field</dd><dd><span>Order of rows to return, such as <code>updated_at DESC</code>.</span></dd></dl>

<dl><dt>Quota</dt><dd>Optional field</dd><dd><span>The maximum number of rows to return. The default is 100, and the maximum is 50,000 rows.</span></dd></dl>

<dl><dt>Offset</dt><dd>Optional field</dd><dd><span>The option to fetch only a page of results from the entire results set.<br><br>For example, to skip the first 100 rows of the selected results set, input 100 to this field.<br><br>The default is 0.</span></dd></dl>

<dl><dt>Output fields</dt><dd>Optional field</dd><dd><span>Define the expected fields of each retrieved Document. Enables users to generate datapills for use in downstream systems, or to drive Recipe logic.</span></dd></dl>

<dl><dt>Output CSV?</dt><dd>Optional field</dd><dd><span>Select <strong>Yes</strong> to output a CSV string of the selected data.</span></dd></dl>

## Output

<dl><dt>rows</dt><dd>Array of JSON objects, where each object represents a retrieved row.</dd></dl>

<dl><dt>rows_count</dt><dd>Number of retrieved rows.</dd></dl>

---
