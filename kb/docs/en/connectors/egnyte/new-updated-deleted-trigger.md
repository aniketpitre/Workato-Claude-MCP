---
url: 'https://docs.workato.com/en/connectors/egnyte/new-updated-deleted-trigger.md'
description: >-
  The New/updated/deleted events trigger in the Egnyte connector fires when a
  file or folder is created, updated, or deleted.
---

# Egnyte - New/updated/deleted events trigger

The **New/updated/deleted events** trigger runs when a new file or folder is detected or when an existing file or folder is updated or deleted in Egnyte.

![New/updated/deleted events trigger](/assets/new-updated-deleted-trigger.CSR0kJsD.png)_New/updated/deleted events trigger_

## Input

| Input field | Description |
| --- | --- |
| Event types | Select the event types you plan to monitor. |
| Folder | Select the folder you plan to monitor for events. |

## Output

| Output field | Description |
| --- | --- |
| ID | The ID of the trigger event. For example: `11`. |
| Timestamp | The timestamp when the event occurred. For example: `2024-02-26T23:06:36.000000+00:00`. |
| Actor | The ID of the user who performed the action. |
| Type | The action type performed. |
| Action | The specific action that was performed. For example: `create`. |
| Target path | The path where the action was targeted. For example: `/Shared/Egnyte Reports`. |
| Is folder | Indicates if the target path is a folder or not. Values are `true` or `falase`. |
| Action source | The source of the action. For example: `System`. |
| Object detail | The detail URL of the object involved in the action. For example: `https://example.egnyte.com/pubapi/v1/fs/Shared/Egnyte%20Reports` |

---
