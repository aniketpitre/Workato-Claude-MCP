---
url: 'https://docs.workato.com/en/connectors/conga/update-record-action.md'
description: The Update record action updates an existing record in Conga.
---

# Conga - Update record action

The **Update record** action updates an existing record in Conga.

## Input

Input fields generate dynamically based on the object you select. The following are common input fields for all object types.

| Input field | Description |
| --- | --- |
| Object | Select the Conga object to update, such as `Contract`, `Account`, `Template`, and more. |
| ID | Enter the ID of the object to update. |
| Name | Enter the name of the object to update. |
| Include record payload in response | Select `Yes` or `No` to specify whether to include the full record details in the response. |
| Enforce optimistic locking | Select `Yes` or `No` to enforce optimistic locking. |

## Output

Output fields generate dynamically based on the object you select. The following are common output fields for all object types.

| Output field | Description |
| --- | --- |
| Success | A boolean response that indicates if the action was successful. |
| Data | ID: The ID of the updated record., Name: The name of the updated record., Created by: The ID and name of the user that created the record., Created date: The date the record was created., Modified by: The ID and name of the user that modified the record., Modified date: The date the record was modified., E tag: The E tag associated with the updated record., External ID: The external ID of the updated record. |
| Status code | A code indicating the status of the action, such as `OK`, `BadRequest`, `Unauthorized`, and more. |

---
