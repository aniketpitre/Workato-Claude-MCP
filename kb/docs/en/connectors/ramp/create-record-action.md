---
url: 'https://docs.workato.com/en/connectors/ramp/create-record-action.md'
description: >-
  Add a new Ramp record, with required fields generated live from Ramp's own API
  schema for the object you select.
---

# Ramp - Create record action

The **Create record** action creates a new record in Ramp.

## Input

Input fields dynamically generate based on the object you select and the create operation. The following field is common to all objects. Refer to the Ramp [REST API](https://docs.ramp.com/developer-api/v1/api/) documentation for a list of input fields.

| Input field | Description |
| --- | --- |
| Object | Select the Ramp object to create, for example **Departments**, **Locations**, or **Users**. |

For example, a single required `name` field is available after you select **Departments**. This matches Ramp's `POST /developer/v1/departments/` endpoint.

## Output

Output fields dynamically generate based on the object you select. Refer to the Ramp [REST API](https://docs.ramp.com/developer-api/v1/api/) documentation for a list of output fields.

For example, output fields for `id` and `name` are available after you select **Departments**.

---
