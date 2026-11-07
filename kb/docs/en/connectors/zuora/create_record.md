---
url: 'https://docs.workato.com/en/connectors/zuora/create_record.md'
description: >-
  The Create record action in the Zuora connector lets you create a single
  record of a selected object type with dynamically generated fields.
---

# Zuora - Create record action

## Create record action

This action creates a single record in Zuora. First, select the object type in Zuora after which Workato will generate the appropriate input fields related to the object in Zuora.

![Create record action](/assets/create_record_action.UzvZrn2P.gif)_Input fields are dynamically generated based on the object selected._

### Input

| Field | Description |
| --- | --- |
| Object | Select the object type in Zuora you hope to create. |
| Object-level input fields | All relevant object input fields. Required input fields will be highlighted. |

### Output

| Field | Description |
| --- | --- |
| Success | Evaluates to "true" if the action was successful. |
| ID | The internal ID of the object created if successful. |
| Errors | Array of errors in the case that the action was unsuccessful. |

## Downstream actions

When creating a record in Zuora, the attributes of this object are not returned immediately. To work with the attributes of this newly created record, use the "search records" action and search using the ID returned in this step.

---
