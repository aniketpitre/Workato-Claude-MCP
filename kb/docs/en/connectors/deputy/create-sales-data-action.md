---
url: 'https://docs.workato.com/en/connectors/deputy/create-sales-data-action.md'
description: >-
  The Create sales data action in the Deputy connector creates a new sales data
  record with a transaction date, area, sales reference, and amount.
---

# Deputy - Create sales data action

This action creates a new sales data record in your Deputy instance.

![Create sales data action](/assets/create-sales-data-action.rAYdOtQH.png)_Create sales data action_

## Input

<dl><dt>Transaction date</dt><dd>The transaction date of the sales data.</dd><dt>Area/Department ID</dt><dd>The ID of the area/department associated with the sales data.</dd><dt>Sales reference</dt><dd>Accepts invoice number or docket ID.</dd><dt>Employee ID</dt><dd>The employee ID associated with the sales data.<br>Optional field.</dd><dt>Sales quantity</dt><dd>The sales quantity.<br>Optional field.</dd><dt>Sales amount</dt><dd>The sales amount.<br>Optional field.</dd><dt>Sales payload</dt><dd>The sales data payload.<br>Optional field.</dd></dl>

## Output

The output of this action is a datatree that contains information about the new sales data object.

Find out more about [sales data object](https://www.deputy.com/api-doc/Resources/SalesData/).

---
