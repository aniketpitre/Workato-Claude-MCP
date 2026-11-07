---
url: 'https://docs.workato.com/en/connectors/wiz/new-updated-record-trigger.md'
description: >-
  The New/updated record trigger monitors a selected Wiz object and initiates a
  recipe when new or updated records are detected.
---

# Wiz - New/updated record trigger

The **New/updated record** trigger creates a job when it detects a new or updated record for a Wiz object you specify.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the Wiz object to monitor. |
| When first started, this recipe should pick up events from | Set the date and time for the trigger to start picking up items when the recipe runs for the first time. Defaults to 1 hour ago if left blank. You can't change this value after the recipe runs or tests successfully. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Nodes | Expand this section to retrieve related nested data. |

Additional fields may appear depending on the selected object.

## Output

The output includes the record data from the selected object. Fields returned vary by object type. Common output fields may include the following:

| Output field | Description |
| --- | --- |
| ID | Unique identifier of the record. |
| Name | Name of the record. |
| Description | Description of the record. |
| Created at | Timestamp when the record was created. |
| Updated at | Timestamp when the record was last updated. |

The full set of output fields depends on the selected object and its schema.

---
