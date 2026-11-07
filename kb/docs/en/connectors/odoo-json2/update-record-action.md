---
url: 'https://docs.workato.com/en/connectors/odoo-json2/update-record-action.md'
description: Update an existing record of any Odoo object in Odoo.
---

# Odoo (JSON-2) - Update record action

The **Update record** action updates an existing record, such as a contact or a sales order, in Odoo (JSON-2).

## Input

| Input field | Description |
| --- | --- |
| Object type | Select the object you plan to update a record for, such as **Contact** or **Sales order**. The list of objects is populated dynamically from your environment. |
| ID | The ID of the record to update. |

Additional input fields are dynamically generated based on the object you select. Refer to the [Odoo](https://www.odoo.com/documentation/19.0/developer/reference/external_api.html) documentation for a complete list of input fields.

## Output

Output fields are dynamically generated based on the object you select. Refer to the [Odoo](https://www.odoo.com/documentation/19.0/developer/reference/external_api.html) documentation for a complete list of output fields.

---

---
url: >-
  https://docs.workato.com/en/connectors/odoo-json2/run-object-function-action.md
description: The Run object function action performs a function on a record in Odoo.
---

# Odoo (JSON-2) - Run object function action

The **Run object function** action performs a function on a record in Odoo (JSON-2).

## Input

| Input field | Description |
| --- | --- |
| Object type | Select the object to run the function on. Options include **Sales order**, **Purchase order**, and **Journal entry**. |
| Object function | Select the function to run on the selected object. The available options depend on the selected **Object type**. |

## Output

| Output field | Description |
| --- | --- |
| Result | The raw response returned after running the function. |

---
