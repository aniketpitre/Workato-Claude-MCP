---
url: 'https://docs.workato.com/en/connectors/hibob/search-records-action.md'
description: >-
  The **Search records** action retrieves the list of records matching the
  specified criteria from HiBob.
---

# HiBob - Search records action

The **Search records** action retrieves the list of HiBob records matching the criteria you specify.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the object from the drop-down menu. |

Input fields are dynamically loaded based on the selected object. The following example shows the input schema for the **Tasks** object:

| Input fields | Description |
| --- | --- |
| Query type | Select any Task query type, such as My task. |

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the data tree to subsequent steps. The following example shows the output schema for the **Tasks** object:

| Output fields | Description |
| --- | --- |
| ID | Unique identifier of the task within HiBob. |
| Title | The name or headline of the task, summarizing its purpose. |
| Set | The task set or category the task belongs to, such as Onboarding or Compliance. |
| Description | Detailed information or instructions related to the task. |

---
