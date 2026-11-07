---
url: >-
  https://docs.workato.com/en/connectors/netsuite-rest/execute-suiteql-query-action.md
description: >-
  The Execute SuiteQL query action in the NetSuite REST connector lets you run a
  custom SELECT query against your database with quota and offset controls.
---

# NetSuite REST - Execute SuiteQL query action

Use the SuiteQL action to execute a custom query against your NetSuite database. This connector only supports the `SELECT` query.

## Input

| Input field | Description |
| --- | --- |
| SuiteQL query | Provide a valid SuiteQL query. |
| Limit | The number of records you plan to fetch. The maximum is 1000 and the default is 100. |
| Offset | The starting position from which records are fetched. The default offset is 0. |
| Output schema | Click **Use SUITEQL** to describe all fields in your response using SuiteQL, or click **add fields manually** to fill out the **Add new field** modal, determining the **Name**, **Label**, **Data type**, whether the parameter is **Optional**, and the **Hint** for each of the fields in your response. |

## Output

This action does not generate any output data for use in downstream recipe steps.
