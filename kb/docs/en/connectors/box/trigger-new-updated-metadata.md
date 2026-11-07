---
url: 'https://docs.workato.com/en/connectors/box/trigger-new-updated-metadata.md'
description: >-
  The New/updated file metadata in folder trigger starts a recipe when a file
  metadata instance is created, updated, or deleted in a specified Box folder.
---

# Box - New/updated file metadata in folder trigger

The **New/updated file metadata** trigger starts a recipe when a file metadata instance is created, updated, or deleted in a specified Box folder. You must have admin level designation in the Box connection and the ability to scope manage enterprise properties to retrieve metadata changes.

## Input

| Input field | Description |
| --- | --- |
| Folder | Select the folder to monitor. You can select from the drop-down menu or enter a folder ID. |
| File metadata changes | Select the metadata change events to monitor. Options include **Metadata instance created**, **Metadata instance updated**, and **Metadata instance deleted**. |

## Output

| Output field | Description |
| --- | --- |
| Source | Source of the event. |
| Created by | User who triggered the event. |
| Action by | Action that matched the trigger condition. |
| Created at | Date and time the event occurred. |
| Event ID | Unique ID of the metadata event. |
| Event type | Type of metadata event. For example, `METADATA_INSTANCE_UPDATED`. |
| IP address | IP address of the user who triggered the event. |
| Type | Object type. For example, `event`. |
| Session ID | Unique ID of the event session. |
| Additional details | Extra metadata about the event, if available. |

---
