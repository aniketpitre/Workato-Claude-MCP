---
url: >-
  https://docs.workato.com/en/connectors/notion/new-or-updated-database-record-trigger.md
description: >-
  The New/updated database record trigger in the Notion connector fires when a
  record is created or updated in the database you monitor.
---

# Notion - New/updated database record trigger

The **New/updated database record** trigger monitors a Notion database for new or updated records.

## Input

| Field | Description |
| --- | --- |
| Trigger poll interval | Specify how frequently to check for new events. |
| Database | Select the database to monitor. |
| When first started, this recipe should pick up events from | Set the date and time to start picking up trigger events. This enables your recipe to capture past events. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

## Output

| Field | Description |
| --- | --- |
| Object | The type of object created or updated. |
| Page ID | The unique identifier of the associated page. |
| Created time | The timestamp when the record was created. |
| Last edited time | The timestamp when the record was last updated. |
| Created by | Contains information about the user who created the record, such as their `User ID` and the `Object` type. |
| Last edited by | Contains information about the user who last updated the record, such as their `User ID` and the `Object` type. |
| Icon | Contains information about the new or updated record's icon, such as its `Type` and associated `Emoji`. |
| Parent | Contains information about the new or updated record's parent, such as its `Type` and `ID`. |
| Archived | Indicates whether the database is archived. |
| In trash | Indicates whether the record is in Notion's trash folder. |
| Properties | Contains information about the new or updated record's properties, such as its `Title`, `Type`, and `ID`. |
| URL | The new or updated record's URL. |
