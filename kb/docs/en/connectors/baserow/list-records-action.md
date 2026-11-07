---
url: 'https://docs.workato.com/en/connectors/baserow/list-records-action.md'
description: >-
  List the tables in your Baserow workspace or the fields defined on one of your
  tables.
---

# Baserow - List records action

The **List records** action returns a workspace's tables, or a table's fields, in Baserow. To list a table's rows instead, use the [Search records](/en/connectors/baserow/search-records-action) action.

## Input

| Input field | Description |
| --- | --- |
| Object type | Select the object type. Options are **Table** or **Field**. |
| Table ID | Select the table to list fields for. The **Table ID** field is required when **Object type** is **Field**. The **Table ID** isn't available when **Object type** is **Table**. |

## Output

Output fields dynamically generate based on the object type you select. The following are a representative set of output fields. Refer to the Baserow [Database API](https://baserow.io/docs/apis/rest-api) documentation for a list of output fields.

| Output field | Description |
| --- | --- |
| Tables | The **Tables** field is only available when **Object type** is **Table**. |
| ID (Tables) | The table's unique identifier. |
| Name (Tables) | The table's name. |
| Order (Tables) | The table's sort position among other tables in the same database. |
| Database ID (Tables) | The database the table belongs to. |
| Fields | The **Fields** field is only available when **Object type** is **Field**. |
| Field ID (Fields) | The field's unique identifier. |
| Table ID (Fields) | The table the field belongs to. |
| Name (Fields) | The field's name. |
| Type (Fields) | The field's type, for example `text`, `number`, or `date`. |

---
