---
url: 'https://docs.workato.com/en/connectors/reckon/search-records-action.md'
description: >-
  The Search records action retrieves records from Reckon using filters and
  selected fields.
---

# Reckon - Search records action

The **Search records** action retrieves a list of records from Reckon based on the selected object.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the Reckon object to search. |
| Book ID | Enter the Reckon One Book ID. You can find it in the Reckon One URL. For example, `https://app.reckonone.com/{BookID}/Core`. |
| Select | Optional. Enter a comma-separated list of fields to return. |

Additional input fields may appear based on the selected object.

## Output

The output varies depending on the selected object. For example, if you select **Contact** as the **Object**, output fields include the following:

| Output field | Description |
| --- | --- |
| ID | Unique identifier of the contact. |
| Name | Display name of the contact. |
| Salutation | Contact's salutation. |
| Department | Department the contact belongs to. |
| Position | Contact’s position or title. |

---
