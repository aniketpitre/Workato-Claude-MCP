---
url: >-
  https://docs.workato.com/en/connectors/odoo-json2/new-updated-object-trigger.md
description: >-
  Triggers when a record of the selected Odoo object is created or updated in
  Odoo.
---

# Odoo (JSON-2) - New/updated object trigger

The **New/updated object** trigger runs when a record of the selected object is created or updated in Odoo (JSON-2). Each poll returns up to 100 new or updated records, ordered by their last-modified date.

## Input

| Input field | Description |
| --- | --- |
| Object type | Select the object you plan to monitor, such as **Contact** or **Sales order**. The list of objects is populated dynamically from your environment. |
| Trigger poll interval | Select the frequency at which trigger checks for new events, from the drop-down menu. Defaults to minutes if left blank. The minimum value allowed is 5 minutes. Refer to [Polling intervals](/en/recipes/polling-intervals) for more information. |

## Output

Output fields are dynamically generated based on the object you select. Refer to the [Odoo](https://www.odoo.com/documentation/19.0/developer/reference/external_api.html) documentation for a complete list of output fields.
