---
url: 'https://docs.workato.com/en/connectors/ynab/search-records-action.md'
description: >-
  The Search records action retrieves a list of plans, categories, transactions,
  or scheduled transactions from YNAB.
---

# YNAB - Search records action

The **Search records** action retrieves a list of records of a selected object type from YNAB. Supported objects include plans, categories, transactions, and scheduled transactions. You can use the **Server knowledge** value from a previous search to retrieve only the changes since that search for all objects except plans.

## Input

Input fields dynamically generate based on the object you select. The following field is common to all objects. Refer to the [YNAB API](https://api.ynab.com/v1) documentation for more information on available input fields.

| Input field | Description |
| --- | --- |
| Object | Select the YNAB object you plan to search. |

## Output

Output fields dynamically generate based on the object you select. Refer to the [YNAB API](https://api.ynab.com/v1) documentation for more information on available output fields.

---
