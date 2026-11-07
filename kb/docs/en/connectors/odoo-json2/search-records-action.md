---
url: 'https://docs.workato.com/en/connectors/odoo-json2/search-records-action.md'
description: Search for records of any Odoo object based on specified criteria.
---

# Odoo (JSON-2) - Search records action

The **Search records** action searches for records, such as contacts or sales orders, in Odoo (JSON-2) based on specified criteria.

## Input

| Input field | Description |
| --- | --- |
| Object type | Select the object you plan to search, such as **Contact** or **Sales order**. The list of objects is populated dynamically from your environment. |
| Limit | Enter the maximum number of records to return. Defaults to 100. |
| Offset | Enter the number of records to skip before returning results for pagination. |
| Order | Enter the order to sort records by. |
| Custom fields | Upload a JSON file to define extra fields. Custom fields are added alongside the auto-detected ones, and duplicates are skipped. |

## Output

| Output field | Description |
| --- | --- |
| Result | An array of records for the selected object. |

Output fields are dynamically generated based on the object you select. Refer to the [Odoo](https://www.odoo.com/documentation/19.0/developer/reference/external_api.html) documentation for a complete list of output fields.

---
