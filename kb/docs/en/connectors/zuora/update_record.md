---
url: 'https://docs.workato.com/en/connectors/zuora/update_record.md'
description: >-
  The Update record action in the Zuora connector lets you select a record by
  its unique Zuora ID and update it with the data you provide.
---

# Zuora - Update record action

## Update record action

This action selects a record and updates it with the data provided. The record is identified using the unique Zuora ID. First, select the object type in Zuora and specify the ID. Subsequently, Workato will dynamically generate input fields relevant to the object selected.

![Update record action](/assets/update_record_action.DkRtqc3M.gif)_Update parameters are dynamically generated based on the object selected._

### Input

| Field | Description |
| --- | --- |
| Object | Select the object type in Zuora you hope to create. |
| ID | The ID of the object which you want to update. This corresponds to the unique internal ID in Zuora. |
| Object-level input fields | The attributes of the object which you want to update. Any fields left blank will not be changed from its original value. |

### Output

| Field | Description |
| --- | --- |
| Success | Evaluates to "true" if the action was successful. |
| ID | The internal ID of the object created if successful. |
| Errors | Array of errors in the case that the action was unsuccessful. |

## Downstream actions

When updating a record in Zuora, the attributes of this object are not returned immediately. To work with the attributes of this newly updated record, use the "search records" action and search using the ID returned in this step.

---
