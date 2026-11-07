---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-365/monitor-changes-entities-trigger-batch.md
description: >-
  The Monitor changes in entities batch trigger in the Microsoft Dynamics 365
  connector tracks entity changes using delta links and returns them in batches.
---

# Microsoft Dynamics 365 - Monitor changes in entities trigger (batch)

The Monitor Changes in Entities Trigger (Batch) in Microsoft Dynamics 365 monitors changes in entities using delta links and retrieves changes in batches.

## Input

| Field | Description |
| --- | --- |
| Entity | Select a standard or custom Microsoft Dynamics 365 object to monitor. For example, `Lead`. Only objects eligible for change tracking are supported. |
| Output fields | Select the fields of the selected objects you plan to use in your recipe. All fields are returned if left blank. |
| Fetch only new changes? | Choose `Yes` to return only changes in the records after the recipe has started. Defaults to `Yes`. Recommended to avoid large number of initial jobs. |
| Batch size | Maximum number of records per trigger event. Minimum is 1, maximum is 200, default is 200. |
| Trigger poll interval | Determine how frequently to check for new events. This defaults to five minutes if left blank. The minimum value allowed is five minutes. |

## Output

| Field | Description |
| --- | --- |
| Range | The range of record IDs retrieved from the search. |
| Records | This contains a list of records. Each record contains information about the changed object, including the fields specified in the output fields. |
