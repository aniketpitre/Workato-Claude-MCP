---
url: 'https://docs.workato.com/en/connectors/ramp/update-record-action.md'
description: >-
  Update an existing Ramp record by ID, with input fields generated live from
  Ramp's own API schema for the object you select.
---

# Ramp - Update record action

The **Update record** action updates an existing record in Ramp.

## Input

Input fields dynamically generate based on the object you select and the update operation. The following fields are common to all objects. Refer to the Ramp [REST API](https://docs.ramp.com/developer-api/v1/api/) documentation for a list of input fields.

| Input field | Description |
| --- | --- |
| Object | Select the Ramp object to update, for example **Departments**, **Locations**, or **Users**. |
| ID | Enter the record's unique identifier. This field is available after you select **Object**, and matches that object's ID path parameter. |

For example, a `department_uuid` path parameter and a required `name` field are available after you select **Departments**. This matches Ramp's `PATCH /developer/v1/departments/{department_uuid}` endpoint.

## Output

Output fields dynamically generate based on the object you select. Refer to the Ramp [REST API](https://docs.ramp.com/developer-api/v1/api/) documentation for a list of output fields.

For example, output fields for `id` and `name` are available after you select **Departments**.

---
