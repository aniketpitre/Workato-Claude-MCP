---
url: 'https://docs.workato.com/en/connectors/conga/new-updated-record-trigger.md'
description: The New/updated record trigger monitors Conga for new or updated records.
---

# Conga - New/updated record trigger

The **New/updated record** trigger monitors Conga for new or updated records.

## Input

Input fields generate dynamically based on the object you select. The following are common input fields for all object types.

| Input field | Description |
| --- | --- |
| Object | Select the object type to monitor Conga for. |
| When first started, this recipe should pick up events from | Set the date and time to start picking up trigger events. This enables your recipe to capture past events. The recipe processes events from the past hour if left blank. Once the recipe is run or tested, you can't change the value. |

## Output

Output fields generate dynamically based on the object you select. The following are common output fields for all object types.

| Output field | Description |
| --- | --- |
| ID | The ID of the new/updated record. |
| Name | The name of the new/updated record. |
| Created by | The ID and name of the user that created the record. |
| Created date | The date the record was created. |
| Modified by | The ID and name of the user that modified the record. |
| Modified date | The date the record was modified. |
| E tag | The E tag associated with the new/updated record. |
| External ID | The external ID of the new/updated record. |

---
