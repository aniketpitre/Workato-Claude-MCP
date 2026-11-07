---
url: 'https://docs.workato.com/en/connectors/smartpm/create-record-action.md'
description: The Create record action enables you to create a new record on SmartPM.
---

# SmartPM - Create record action

The **Create record** action enables you to create a new record in SmartPM.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the object for the new record. Fields load dynamically based on the object you select. |

For example, if you select the **Project** object, fields such as **Name**, **City**, **State**, **Zip code**, **Project plan**, and **Project metadata** appear.

## Output

The output schema depends on the selected object. Use the output fields to map datapills to downstream steps.

For example, if you select the **Project** object, the output includes the following:

| Output field | Description |
| --- | --- |
| Project ID | Unique identifier of the created project. |
| Message | Status message for the operation. |
| Files | File details associated with the project. |

---
