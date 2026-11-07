---
url: 'https://docs.workato.com/en/connectors/reckon/get-record-action.md'
description: >-
  The Get record by ID action retrieves a specific record from Reckon using its
  unique ID.
---

# Reckon - Get record by ID action

The **Get record by ID** action retrieves a specific record from Reckon using its unique identifier.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the Reckon object to retrieve. |
| Book ID | Enter the Reckon One Book ID. You can find it in the Reckon One URL. For example: `https://app.reckonone.com/{BookID}/Core`. |
| Object ID | Enter the unique ID of the selected object. |
| Select | Optional. Enter a comma-separated list of fields to return. For example, `id, name`. |

Additional input fields may appear depending on the selected object type.

## Output

The output varies based on the selected object type. For example, if you select **Contact** as the **Object**, output fields include the following:

| Output field | Description |
| --- | --- |
| ID | Unique identifier of the contact. |
| Name | Display name of the contact. |
| Salutation | Salutation of the contact. |
| Department | Department associated with the contact. |
| Position | Contact's job position or role. |

---
