---
url: 'https://docs.workato.com/en/connectors/jira/get-issue-schema-action.md'
description: This action retrieves the name and schema of all fields in a Jira object.
---

# Jira - Get issue schema action

The **Get issue schema** action retrieves the name and schema of all fields in a Jira object. You can use this action to replicate the schema to your database or data warehouse.

## Input

| Input field | Description |
| --- | --- |
| Output fields | Select the fields to retrieve from Jira or enter them manually. If you select **Enter fields**, you must supply a comma-separated list of IDs for the fields you plan to use in the recipe. For example: `parent,lastViewed` |

## Output

| Output field | Description |
| --- | --- |
| Object name | The name of the object. |
| Object label | The display label of the object. |
| Field name (Fields) | The name of the field. |
| Field label (Fields) | The display label of the field. |
| Original type (Fields) | The data type of the field in Jira. |
| Mapped type (Fields) | The data type that the `original type` maps to in Workato. This type determines the column's data type when it loads into a database. |
| Orderable (Fields) | Indicates whether this field is orderable. |
| Navigable (Fields) | Indicates whether this field is navigable. |
| Searchable (Fields) | Indicates whether this field is searchable. |
| Custom field (Fields) | Indicates whether this field was created by a user. |
| List size (Fields) | The total number of fields retrieved. |
| List index (Fields) | The position of the current field in the results list. |

---
