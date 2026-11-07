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
