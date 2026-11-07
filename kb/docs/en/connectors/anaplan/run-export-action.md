---
url: 'https://docs.workato.com/en/connectors/anaplan/run-export-action.md'
description: >-
  The Run data export batch action in the Anaplan connector lets you run a data
  export process from a model and track its progress to completion.
---

# Anaplan - Run data export batch action

The **Run data export** batch action allows you to run a data export process from a model in Anaplan.

![Run data export in Anaplan action](/assets/run-data-export-action.D70M9LjH.png)_Anaplan - Run data export action_

## Input

| Input field | Description |
| --- | --- |
| Workspace | Select the workspace in Anaplan where the model is located. |
| Model | Choose the Anaplan model that contains the data you plan to export. |
| Export process | Select the export process you plan to execute within the selected model. |
| Wait for export process to complete? | Decide if Workato should wait for the export to finish before moving to the next step. Choose **Yes** to pause until completion, or **No** to continue to the next step immediately after starting the export. |

## Output

| Output field | Description |
| --- | --- |
| Task ID | The unique identifier for the export task within Anaplan. |
| Task state | The current state of the export task. |
| Export succeeded? | Indicates whether the export was successful. |
| Current step | The current step of the export process. |
| Progress | The progress percentage of the export task. |
| Result | The final result of the export task. |

---
