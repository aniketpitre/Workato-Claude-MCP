---
url: 'https://docs.workato.com/en/connectors/salesloft/create-record-action.md'
description: The create record action enables you to create a record in Salesloft.
---

# Salesloft - Create record action

The **Create record** action enables you to create a record in Salesloft.

## Input

| Input field | Description |
| --- | --- |
| Object name | Select the object to be created from the drop-down menu. |

Workato dynamically populates additional fields depending on the object you select. For example, if you select the **Person to cadence** object, fields such as **Person ID**, **Cadence**, and **User ID** appear.

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the data tree to subsequent steps. For example, if the selected object is **Person to cadence**, then the output schema is as follows.

| Output fields | Description |
| --- | --- |
| Cadence Membership ID | Unique identifier assigned to the membership of a person in a cadence. |
| Added at | Timestamp indicating when the person was added to the cadence. |
| Created at | Timestamp when the cadence membership was originally created. |
| Updated at | Timestamp of the most recent update made to the cadence membership. |
| Person deleted | Boolean value indicating if the person has been deleted from the cadence. |
| Current state | The current stage or status of the person within the cadence. |
| Cadence | The cadence details to which the person is assigned or enrolled. |
| Person | The individual contact associated with the cadence membership. |
| User | The Salesloft user responsible for managing the cadence membership. |
| Latest action | The most recent action taken within the cadence for that particular person. |
| Counts | Statistics related to the cadence membership. |

---
