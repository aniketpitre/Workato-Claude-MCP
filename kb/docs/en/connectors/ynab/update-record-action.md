---
url: 'https://docs.workato.com/en/connectors/ynab/update-record-action.md'
description: The Update record action updates a category or transaction in a plan in YNAB.
---

# YNAB - Update record action

The **Update record** action updates a record of a selected object type in a plan in YNAB. Supported objects include categories and transactions. For a category, you can set the budgeted amount for a month and update category settings, such as the name, note, group, and goal. Enter amounts in milliunits, where `1000` equals one currency unit. For example, `150000` equals `$150.00`.

## Input

Input fields dynamically generate based on the object you select. The following fields are common to all objects. Refer to the [YNAB API](https://api.ynab.com/v1) documentation for more information on available input fields.

| Input field | Description |
| --- | --- |
| Object | Select the YNAB object you plan to update. |
| Plan | Optional. Select the plan (budget) to use. Defaults to your last-used plan. Select **Default** only if a default budget is enabled in your YNAB account. |

## Output

Output fields dynamically generate based on the object you select. Refer to the [YNAB API](https://api.ynab.com/v1) documentation for more information on available output fields.

---
