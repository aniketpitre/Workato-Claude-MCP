---
url: 'https://docs.workato.com/en/connectors/filevine/get-record-details-action.md'
description: >-
  The Get record details by ID action retrieves a specific record from Filevine
  based on the selected object and identifier.
---

# Filevine - Get record details by ID action

The **Get record details by ID** action retrieves information for a specific record in Filevine based on the selected object type and project type ID.

## Input

| Input field | Description |
| --- | --- |
| Object type | Select the Filevine object to retrieve. |
| Project type ID | Select the ID of the project type for the object. |

Additional input fields may appear depending on the selected object type.

## Output

The output varies depending on the selected object type. For example, if you select **Project** as the **Object type**, output fields include the following:

| Output field | Description |
| --- | --- |
| Object ID | Unique identifier of the project. |
| Timestamp | Time when the event occurred. |
| Object | Snapshot of the project record. |
| Event | Type of event associated with the retrieval. |
| Organization ID | ID of the organization the project belongs to. |
| Project ID | ID of the project. |
| User ID | ID of the user associated with the event. |
| User type | Type of user. |

The full set of fields depends on the selected object and its schema.

---
