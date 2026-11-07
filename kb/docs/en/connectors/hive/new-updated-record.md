---
url: 'https://docs.workato.com/en/connectors/hive/new-updated-record.md'
description: >-
  The New/updated record trigger in the Hive connector fires when an action or
  project is created or an existing one is updated.
---

# Hive - New/updated record trigger (real-time)

The **New/updated record** trigger monitors changes in a Hive action or project and runs when a new action or project is created or an existing action or project is updated.

## Input

| Input field | Description |
| --- | --- |
| Object | Select a Hive object, such as **Project** or **Action**. |
| Trigger events | Select one or more events that trigger this action. |
| Trigger when specific fields are updated | Select the event that triggers when a specific field updates. If left blank, the trigger runs when any field updates. |
| Projects | Select one or more projects where Workato monitors for updates. Alternatively, enter project IDs as a comma-separated string. |

## Output

| Output field | Description |
| --- | --- |
| Trigger event | The event that triggered the action, such as **New project** or **Updated action**. |
| Object type | The type of Hive object, such as **Action** or **Project**. |
| Record | The record data based on the selected object. This Includes fields such as `ID`, `Name`, `Created at`, and other relevant attributes. |

---
