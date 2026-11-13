---
url: 'https://docs.workato.com/en/connectors/ynab/update-records-action.md'
description: >-
  The Update records (batch) action updates multiple transactions in a plan in
  YNAB in a single call.
---

# YNAB - Update records (batch) action

The **Update records (batch)** action updates multiple records of a selected object type in a plan in YNAB in a single call. Supported objects include transactions. YNAB limits API requests to `200` per hour, so updating records in a batch helps you stay within the limit.

## Input

Input fields dynamically generate based on the object you select. The following fields are common to all objects. Refer to the [YNAB API](https://api.ynab.com/v1) documentation for more information on available input fields.

| Input field | Description |
| --- | --- |
| Object | Select the YNAB object you plan to update. |
| Plan | Optional. Select the plan (budget) to use. Defaults to your last-used plan. Select **Default** only if a default budget is enabled in your YNAB account. |

## Output

Output fields dynamically generate based on the object you select. The following are a representative set of output fields. Refer to the [YNAB API](https://api.ynab.com/v1) documentation for more information on available output fields.

| Output field | Description |
| --- | --- |
| Transaction IDs | The list of IDs of the updated transactions. |
| Duplicate import IDs | The list of import IDs that YNAB identified as duplicates. |
| Transactions | The list of updated transactions. |
| Server knowledge | The YNAB server knowledge value after the update. |

---
