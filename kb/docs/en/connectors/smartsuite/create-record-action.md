---
url: 'https://docs.workato.com/en/connectors/smartsuite/create-record-action.md'
description: The Create record action enables you to create a new record in SmartSuite.
---

# SmartSuite - Create record action

The **Create record** action enables you to create a new record in SmartSuite.

## Input

| Input field | Description |
| --- | --- |
| Object | Specify the object to create the record. Fields load dynamically based on the object you select. |

For example, if you select **Field**, the input schema is the following:

| Input field | Description |
| --- | --- |
| Solution ID | Provide the SmartSuite solution ID. |
| Table ID | Provide the SmartSuite table ID. |
| Field | Provide details of the field. |
| Field ID | Provide a random 10-digit alphanumeric value for the child parameter of the ‘Field’. |
| Label | Provide the field name. |
| Field type | Provide the field type. |
| Params | Provide field-specific parameters. |
| Is required | Select `Yes` or `No` from the drop-down menu. This indicates whether the field is required or not. |
| Is unique | Select `Yes` or `No` from the drop-down menu. This indicates whether the field is unique or not. |
| Is hidden | Select `Yes` or `No` from the drop-down menu. This indicates whether the field is hidden or not. |
| Default value | Provide the default value for the field. |
| Placeholder | Provide the placeholder for the field. |
| Help text display format | Provide the help text to display the format of the field. |
| Help doc | Provide the help doc for the field. |
| Width | Provide the width of the field. |
| Is valid | Select `Yes` or `No` from the drop-down menu. This indicates whether the field is valid or not. |
| Is migrating | Select `Yes` or `No` from the drop-down menu. This indicates whether the field is migrating or not. |
| Secondary email | Provide the secondary email ID of the contact. |
| Field position | Provide the position of the field. |
| Previous field slug | Provide the previous field’s value. |
| Auto fill structure layout | Select `Yes` or `No` from the drop-down menu. This indicates whether the structure layout will be auto-filled. |
| Add params | Provide the expected other parameters for the structure that will be added in the output. |

## Output

The output fields are determined by the object selected in the input.

For example, if you select **Field**, the output schema is the following:

| Output field | Description |
| --- | --- |
| Success | Success message. |

Refer to the [SmartSuite documentation](https://developers.smartsuite.com/docs/solution-data/fields/add-field) for more information.

---
