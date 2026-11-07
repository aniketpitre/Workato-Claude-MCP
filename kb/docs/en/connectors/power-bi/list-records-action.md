---
url: 'https://docs.workato.com/en/connectors/power-bi/list-records-action.md'
description: 'Retrieve a list of records, for example- Tables in Power BI.'
---

# Power BI - List records action

The **List records** action retrieves a list of records, such as tables, in Power BI.

## Input

| Input field | Description |
| --- | --- |
| Object | Select an object from the drop-down menu. |
| Dataset | Select a dataset from the drop-down menu. |
| Workspace | Select a workspace from the drop-down menu. |

## Output

| Output field | Description |
| --- | --- |
| Name | The record name. |
| Description | The record description. |
| Is hidden | Indicates whether the record is hidden. |
| Columns | A dataset column. Refer to the [Column](https://learn.microsoft.com/en-us/rest/api/power-bi/push-datasets/datasets-get-tables#column) section for schema details. |
| Measures | A Power BI measure. Refer to the [Measure](https://learn.microsoft.com/en-us/rest/api/power-bi/push-datasets/datasets-get-tables#measure) section for schema details. |
| Rows | A data row in a dataset. The ID parameter is the unique row ID. |
| Source | A dataset table source. The source parameter contains the source expression. |

---
