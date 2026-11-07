---
url: 'https://docs.workato.com/en/connectors/postgresql/export-query-result.md'
description: >-
  The Export query result action in the PostgreSQL connector runs a SQL query
  and exports the results as a CSV file to a stream or storage.
---

# PostgreSQL - Export query result action

## Export query result

This bulk long action executes a SQL query and exports the results as a CSV file. If you are using a cloud connection, you can stream the exported CSV content via the File Contents datapill. When using a cloud connection, the maximum timeout is **120 minutes**. If you are using an OPA connection, you can upload the CSV file to a local directory or a cloud storage like an S3 bucket.

If the CSV file is uploaded to a local directory, the query results are processed and stored locally. This means that your data doesn't leave your secure network.

> **On-prem profile configuration**
> 
> Remember to configure a staging area in your on-prem agent profile. Learn how to set up a staging area in the [OPA server profile](/en/on-prem/agents/connection/profile#server-profile).

![Export query result action (OPA)](/assets/export-query-result-opa.DTLe7jCK.png)_Export query result action (OPA)_

![Export query result action (Cloud)](/assets/export-query-result-cloud.CtJ3Ez-y.png)_Export query result action (Cloud)_

## Input

| Input field | Description |
| --- | --- |
| SQL | A valid SQL query. for example, `SELECT * FROM PUBLIC.ACCOUNTS` |
| Column delimiter | Choose a delimiter character. CSV files typically use comma. |
| Upload URL (**OPA connection only**) | Export the CSV file to this URL. Generate this url using [On-prem files](/en/connectors/on-prem-files/generate-on-prem-file-url) or [Amazon S3](/en/connectors/s3/action-presign-url). |

## Output

| Output field | Description |
| --- | --- |
| Number of rows exported | The number of rows exported. |
| Column names | Column headers in the CSV file. |
| File Contents (**Cloud connection only**) | CSV stream of the contents of the file. |

---
