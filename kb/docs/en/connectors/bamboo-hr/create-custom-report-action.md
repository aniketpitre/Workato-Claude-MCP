---
url: >-
  https://docs.workato.com/en/connectors/bamboo-hr/create-custom-report-action.md
description: >-
  The Create custom employee report action in the BambooHR connector lets you
  build a report on employees from selected fields to fetch large volumes of
  data.
---

# BambooHR - Create custom employee report action

This action creates a custom report on employees in BambooHR based on the selected fields.

Use this action if you are trying to fetch a large volume of employees data in one action.

## Input

![Create custom employee report action](/assets/create-custom-report-action.BDz8LS2K.png)_Create custom employee report action_

| Input field | Description |
| --- | --- |
| Fields | Select fields that will be returned as outputs to this action. |
| Only current | Limits the report to only current employees. Setting to no/false will include future-dated employees in the report. |
| Last changed | Include only the records that have been changed since given date. |

## Output

The output of this action is all the selected set of data for all the employees fetched by the report.

For more information, read the [BambooHR documentation](https://documentation.bamboohr.com/reference/request-custom-report-1).
