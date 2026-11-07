---
url: 'https://docs.workato.com/en/connectors/odoo-json2/run-wizard-action.md'
description: >-
  Complete a guided process in Odoo, such as registering a payment or creating a
  credit note.
---

# Odoo (JSON-2) - Run wizard action

The **Run wizard** action completes a guided process (an Odoo wizard) in Odoo (JSON-2), such as registering a payment or creating a credit note.

## Input

| Input field | Description |
| --- | --- |
| Wizard | Select the wizard you plan to run. Select **Use custom value** to enter any transient wizard model name, for example `sale.advance.payment.inv`. |

## Output

For most wizards, the action returns the following action-window fields:

| Output field | Description |
| --- | --- |
| Wizard ID | The ID of the wizard that was run. |
| Result ID | The ID of the result the wizard generates. |

---

---
url: >-
  https://docs.workato.com/en/connectors/odoo-json2/quotations-by-validity-date-action.md
description: Retrieve quotations (sales orders) from Odoo filtered by their validity date.
---

# Odoo (JSON-2) - Quotations by validity date action

The **Quotations by validity date** action retrieves quotations (sales orders) from Odoo filtered by their validity date.

## Input

| Input field | Description |
| --- | --- |
| Validity date from | Select a validity date to return quotations on or after the selected date. |
| Validity date to | Select a validity date to return quotations on or before the selected date. |
| Include sent | Select `Yes` or `No` to include quotations already sent to the customer. Only draft quotations are returned by default. |
| Limit | Enter the maximum number of quotations to return. Defaults to 100. |
| Custom fields | Upload a JSON file to define extra fields. Custom fields are added alongside the auto-detected ones, and duplicates are skipped. |

## Output

| Output field | Description |
| --- | --- |
| Result | An array of quotation (sales order) records, sorted by validity date. |

---
