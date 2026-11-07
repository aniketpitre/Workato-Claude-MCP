---
url: 'https://docs.workato.com/en/connectors/anaplan/run-import-action.md'
description: >-
  The Run data import batch action in the Anaplan connector lets you import data
  into a model and track the import process to completion.
---

# Anaplan - Run data import batch action

The **Run data import** batch action allows you to import data into an Anaplan model.

![Run data import in Anaplan action](/assets/run-data-import-action.QmvsQoIM.png)_Anaplan - Run data import action_

## Input

| Input field | Description |
| --- | --- |
| Workspace | Select the workspace in Anaplan where the model is located. |
| Model | Choose the Anaplan model where you plan to run the data import process. |
| Import process | Select the specific process within the model that you plan to import data. |
| Wait for import process to complete? | Decide if Workato should wait for the import to finish before moving to the next step. Choose **Yes** to pause until completion, or **No** to continue to the next step immediately after starting the import. |

## Output

| Output field | Description |
| --- | --- |
| Task ID | The identifier for the import task within Anaplan. |
| Task state | The status of the import task. |
| Import succeeded? | Indicates whether the import was successful. |
| Current step | The current step of the import process. |
| Progress | The import task completion percentage. |
| Result | The outcome of the import process. |

---
