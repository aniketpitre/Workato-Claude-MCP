---
url: 'https://docs.workato.com/en/connectors/hive/update-record.md'
description: >-
  The Update record action in the Hive connector lets you update an existing
  record, such as a project or action, by its ID.
---

# Hive - Update record action

The **Update record** action updates an existing Hive record, such as a **Project** or **Action**.

## Input

| Input field | Description |
| --- | --- |
| Object | Select a Hive object, such as **Project** or **Action**. Additional fields load dynamically based on the selected object. |
| Record ID | Enter the ID of the record to update. |

## Output

The output fields depend on the object you select in the input. Each object returns a unique set of fields based on its type. Common fields may include the following:

| Output field | Description |
| --- | --- |
| ID | Unique identifier of the record. |
| Name | Name of the record, if applicable. |
| Created at | Timestamp indicating when the record was created. |
| Created by | ID of the user who created the record. |
| Modified at | Timestamp indicating when the record was last updated. |
| Modified by | ID of the user who last modified the record. |

---
