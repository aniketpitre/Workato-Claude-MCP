---
url: 'https://docs.workato.com/en/connectors/wrike/create-blueprint-action.md'
description: >-
  The Create from blueprint action in the Wrike connector creates a folder or
  task from an existing Wrike blueprint.
---

# Wrike - Create from blueprint action

The **Create from blueprint** action creates a folder or task in Wrike from a blueprint.

## Input

| Input field | Description |
| --- | --- |
| Blueprint type | Select the type of blueprint you plan to use. Options include **Folder** and **Task**. |
| Blueprint | Select the blueprint to use. Toggle to **Enter a blueprint ID** to enter a blueprint ID instead. |
| Folder title / Task title | Enter a title for the created folder. |
| Parent folder | Select a parent folder to create the folder or task in. Either this field or **Super task** is required when you create a task. Wrike doesn't allow you to set both fields simultaneously. |
| Super task | Select a super task to create the task in. Either this field or **Parent folder** is required when you create a task. Wrike doesn't allow you to set both fields simultaneously. |
| Title prefix | Enter a prefix to apply to all copied tasks. |
| Copy descriptions? | Select **Yes** to copy descriptions from the blueprint. Defaults to **Yes**. |
| Notify responsibles? | Select **Yes** to notify responsible users. Defaults to **Yes**. |
| Copy responsibles? | Select **Yes** to copy responsible users from the blueprint. Defaults to **Yes**. |
| Copy custom fields? | Select **Yes** to copy custom fields from the blueprint. Defaults to **Yes**. |
| Copy attachments? | Select **Yes** to copy attachments from the blueprint. Defaults to **No**. |
| Reschedule date | Enter a reschedule date for the created folder or task. |
| Reschedule mode | Select **Start** or **End** to define how the blueprint reschedules tasks. Defaults to **Start**. |
| Entry limit | Set the maximum number of tasks or folders copied. Must be between **1** and **250**. |

## Output

| Output field | Description |
| --- | --- |
| Job ID | Unique identifier for the blueprint job. |
| Job status | Status of the job execution. |
| Job result | Outcome of the job execution. |
| Job error | Details of any errors encountered during execution. |
| Job progress | Percentage of completion for the job. |
| Total count | Total number of items processed in the job. |
| Processed count | Number of items successfully processed. |
| Type | Type of created object, such as **Folder** or **Task**. |

---
