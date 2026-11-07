---
url: >-
  https://docs.workato.com/en/connectors/bamboo-hr/get-company-report-by-id-action.md
description: >-
  The Get company employee report by ID action in the BambooHR connector lets
  you fetch an existing employee report by its report ID.
---

# BambooHR - Get company employee report by ID action

This action fetches an existing employee report from the user's BambooHR instance.

> **DEPRECATION NOTICE**
> 
> This action is deprecated. Use the [Get report by ID (v2) action](/en/connectors/bamboo-hr/get-report-by-id-v2-action) to fetch reports using BambooHR's Custom Reports API instead.

## Input

![ Get company employee report by ID action](/assets/get-company-report-action.C07w9fie.png) \_ Get company employee report by ID action\_

| Input field | Description |
| --- | --- |
| Report ID | The ID of the existing report. You can get the report number by hovering over the report name and noting the ID from the URL. Supports only reports from my reports and manage reports. |
| Only current | Limits the report to only current employees. Setting to no/false will include future-dated employees in the report. |
| Output fields | Provide a sample JSON of the expected output fields from the report, or enter them manually. |

## Output

The output of this action is the set of data for all the employees as configured in the report.

For more information, read the [BambooHR documentation](https://documentation.bamboohr.com/reference/get-company-report-1).
