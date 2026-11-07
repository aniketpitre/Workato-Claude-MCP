---
url: 'https://docs.workato.com/en/connectors/ghost/update-record-action.md'
description: The Update record action updates a post in Ghost.
---

# Ghost - Update record action

The **Update record** action updates a post in Ghost. The action fetches the post's current state first and sends it along with your changes to avoid overwriting concurrent edits.

## Input

Input fields dynamically generate based on the object you select. The following fields are common to all objects. Refer to the [Ghost Admin API](https://docs.ghost.org/admin-api) documentation for more information on available input fields.

| Input field | Description |
| --- | --- |
| Object type | Select the object to update. `Post` is currently the only available object. |
| ID | Enter the ID of the record to update. |

## Output

Output fields dynamically generate based on the object you select. Refer to the [Ghost Admin API](https://docs.ghost.org/admin-api) documentation for more information on available output fields.

---
