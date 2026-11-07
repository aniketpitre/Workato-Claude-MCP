---
url: 'https://docs.workato.com/en/connectors/power-bi/upload-pbix-file-action.md'
description: This action uploads a PBIX (Power BI Extension) file in Power BI.
---

# Power BI - Upload PBIX file action

The **Upload PBIX file** action uploads a PBIX (Power BI Extension) file to Power BI.

## Input

| Input field | Description |
| --- | --- |
| File contents | Enter the contents of the PBIX file to upload. |
| File name | Enter the name of the PBIX file. |
| Dataset display name | Enter the dataset display name, including the file extension. |
| Workspace | Select a workspace from the drop-down menu. |
| Name conflict | Choose an action if a dataset with the same name exists. The default is **Ignore**. **Abort** and **Overwrite** are only supported for RDL (Report Definition Language) files. |
| Skip report | Choose whether to skip report import. If specified, the value must be `true`. Supported only for PBIX files. |

## Output

| Output field | Description |
| --- | --- |
| ID | The unique identifier for the uploaded file. |

---
