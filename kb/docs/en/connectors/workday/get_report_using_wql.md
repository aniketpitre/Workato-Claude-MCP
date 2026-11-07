---
url: 'https://docs.workato.com/en/connectors/workday/get_report_using_wql.md'
description: >-
  The Get report using WQL action in the Workday connector lets you query
  Workday data with Workday Query Language and retrieve paginated results.
---

# Workday - Get report using WQL action

## What is WQL?

Workday Query Language (WQL) is a SQL-like query language offering higher-performing Workday data querying capabilities. Since WQL is SQL-like, you may construct the query manually within Workday, or convert an existing report to WQL using the "Convert report to WQL" option.

## WQL vs. RaaS

Both Workday Report-as-a-Service (RaaS) and WQL support retrieval of large volumes of information. However, unlike Workday RaaS which returns the result one-shot, WQL supports pagination. This provides both data retrieval flexibility and performance improvements.

## Inputs

![Get report using WQL](/assets/get_report_wql.CarZpNCS.png)_Get report using WQL_

| Input field | Description |
| --- | --- |
| Report WQL _required_ | Provide WQL of the report from the Convert Report to WQL action in Workday. Otherwise, construct the WQL manually in Workday. |
| Count | Set the count of the objects to be retrieved in a single batch/page, up to 1000. Minimum is 200. If left blank, defaults to 200. |
| Page | Set the page of the response. Defaults to 1, denoting the first page. |
| Report columns | Override the default report schema with your own custom report schema. |

## Outputs

The output of this action is presented as an array. Each element in this array corresponds to a row in the report. Similarly, each column in your report will be rendered as a field in the report output array.

If you configured a custom schema in **Report columns**, the custom report columns will be reflected as datapills.

---

---
url: >-
  https://docs.workato.com/en/connectors/workday/list-custom-object-definitions.md
description: >-
  The List custom object definitions action in the Workday connector lets you
  retrieve the custom object definitions available to your security profile.
---

# Workday - List custom object definitions action

This action lists all available custom object definitions in Workday. The list retrieved will be subject to the security profile assigned to the credentials used when setting up the connection.

## Inputs

![List custom object definitions action](/assets/list-custom-object-definitions.C8NYfDbS.png)_List custom object definitions action_

| Input field | Description |
| --- | --- |
| Count | Sets the count of the objects to be retrieved in a single response, up to 100. If left blank, defaults to 20. |
| Page | Sets the page offset of the response. If left blank, defaults to 1. |

## Outputs

The outputs of this action are the total count of existing records and a paginated list of custom object definitions.

---
