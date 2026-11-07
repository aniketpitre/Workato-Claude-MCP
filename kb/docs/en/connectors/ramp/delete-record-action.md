---
url: 'https://docs.workato.com/en/connectors/ramp/delete-record-action.md'
description: >-
  Remove an existing Ramp record by ID, with input fields generated live from
  Ramp's own API schema for the object you select.
---

# Ramp - Delete record action

The **Delete record** action deletes an existing record in Ramp.

## Input

Input fields dynamically generate based on the object you select and the delete operation. The following fields are common to all objects. Refer to the Ramp [REST API](https://docs.ramp.com/developer-api/v1/api/) documentation for a list of input fields.

| Input field | Description |
| --- | --- |
| Object | Select the Ramp object to delete, for example **Users**, **Vendors**, or **Accounts**. |
| ID | Enter the record's unique identifier. The **ID** field is available after you select **Object**, and matches that object's ID path parameter. |

For example, a `user_id` input field is available after you select **Users**. This matches Ramp's `DELETE /developer/v1/users/{user_id}` endpoint.

## Output

Output fields dynamically generate based on the object you select. Many delete operations return no response body, so the output may be empty. Refer to the Ramp [REST API](https://docs.ramp.com/developer-api/v1/api/) documentation for a list of output fields.

For example, no output fields are available after you select **Users**, because Ramp's delete endpoint for this object returns an empty `204 No Content` response.

---
