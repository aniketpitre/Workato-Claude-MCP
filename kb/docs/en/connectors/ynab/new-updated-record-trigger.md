---
url: 'https://docs.workato.com/en/connectors/ynab/new-updated-record-trigger.md'
description: >-
  The New/updated record trigger monitors YNAB for new or updated transactions
  in a plan.
---

# YNAB - New/updated record trigger

The **New/updated record** trigger monitors YNAB for new or updated records of a selected object type in a plan. Supported objects include transactions. After the first poll, the trigger uses the YNAB server knowledge value to return each new or changed record once.

## Input

Input fields dynamically generate based on the object you select. The following fields are common to all objects. Refer to the [YNAB API](https://api.ynab.com/v1) documentation for more information on available input fields.

| Input field | Description |
| --- | --- |
| Object | Select the YNAB object you plan to monitor. |
| Plan | Optional. Select the plan (budget) you plan to monitor. Defaults to your last-used plan. Select **Default** only if a default budget is enabled in your YNAB account. |

## Output

Output fields dynamically generate based on the object you select. The following are a representative set of output fields. Refer to the [YNAB API](https://api.ynab.com/v1) documentation for more information on available output fields.

| Output field | Description |
| --- | --- |
| ID | The unique identifier of the transaction. |
| Date | The date of the transaction. |
| Amount | The transaction amount, in milliunits. Negative for outflow. |
| Cleared | The cleared status: cleared, uncleared, or reconciled. |
| Account name | The name of the account. |
| Payee name | The name of the payee. |
| Category name | The name of the category. |
| Deleted | Whether the transaction is deleted. |
| Subtransactions | The list of subtransactions, if the transaction is split. |
| Server knowledge | The YNAB server knowledge value at which the change occurred. |

---
