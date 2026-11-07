---
url: 'https://docs.workato.com/en/connectors/ibm-db2/export-query-result.md'
description: >-
  The Export query result action in the IBM Db2 connector lets you run a SQL
  query and export its result set as a CSV file to local or cloud storage.
---

# IBM Db2 - Export query result action

The export function runs a SQL query and exports its result set as a CSV file. The system uploads the CSV file to a local directory, or to cloud storage, such as an S3 bucket.

If using a local directory to upload the CSV file, the system processes and stores the query results locally, and the data doesn't leave your secure network.

## Input

<dl><dt>SQL</dt><dd>Required field</dd><dd><span>Provide the SQL query to select data for export.<br>Wrap datapills in single quote characters, <code>'</code>.</span></dd></dl>

<dl><dt>Column delimiter</dt><dd>Required field</dd><dd><span>Choose a delimiter character. Commonly, CSV files typically use comma.</span></dd></dl>

<dl><dt>Upload URL</dt><dd>Required field</dd><dd><span>Export the CSV file to this URL. Generate this url using <a href="/connectors/on-prem-files/generate-on-prem-file-url.html">On-prem files</a>, or <a href="/connectors/s3/action-presign-url.html">Amazon S3</a>.</span></dd></dl>

## Output

<dl><dt>Number of rows exported</dt><dd>The number of rows exported to the CSV file.</dd></dl>

<dl><dt>Column names</dt><dd>Column headers in the exported CSV file.</dd></dl>

---
