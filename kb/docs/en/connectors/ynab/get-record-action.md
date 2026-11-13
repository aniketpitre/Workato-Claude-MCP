---
url: 'https://docs.workato.com/en/connectors/ynab/get-record-action.md'
description: >-
  The Get record action retrieves a record of a selected object type from a plan
  in YNAB.
---

# YNAB - Get record action

The **Get record** action retrieves a record of a selected object type from a plan in YNAB. Supported objects include categories and budget months. For a month, the **To be budgeted** output field is the Ready to Assign amount.

## Input

Input fields dynamically generate based on the object you select. The following fields are common to all objects. Refer to the [YNAB API](https://api.ynab.com/v1) documentation for more information on available input fields.

| Input field | Description |
| --- | --- |
| Object | Select the YNAB object you plan to retrieve. |
| Plan | Optional. Select the plan (budget) to use. Defaults to your last-used plan. Select **Default** only if a default budget is enabled in your YNAB account. |
| Month | Enter the budget month you plan to retrieve. Enter `current` or an ISO date. For example, `2026-10-01`. |

## Output

Output fields dynamically generate based on the object you select. Refer to the [YNAB API](https://api.ynab.com/v1) documentation for more information on available output fields.

---
