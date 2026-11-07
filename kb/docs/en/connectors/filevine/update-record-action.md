---
url: 'https://docs.workato.com/en/connectors/filevine/update-record-action.md'
description: >-
  The Update record action modifies an existing Filevine record based on the
  selected object type.
---

# Filevine - Update record action

The **Update record** action modifies an existing record in Filevine based on the selected object type, project type, and section selectors.

## Input

| Input field | Description |
| --- | --- |
| Object type | Select the Filevine object to update. |
| Project type ID | Select the ID of the project type related to the object. |
| Sections | Select the section that contains the record to update. |

Additional input fields may appear based on the selected object type.

## Output

The output fields vary based on the selected **Object type**. For example, if you select **Project** as the **Object type**, common output fields include the following:

| Output field | Description |
| --- | --- |
| Project ID | Unique ID of the updated project. |
| Project type ID | ID of the project type. |
| Client ID | ID of the client linked to the project. |
| Phase ID | ID of the current phase of the project. |
| Teams | Team assignments associated with the project. |
| Links | Relevant navigation or reference links. |

---
