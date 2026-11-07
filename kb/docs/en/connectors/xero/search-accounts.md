---
url: 'https://docs.workato.com/en/connectors/xero/search-accounts.md'
description: >-
  The Search accounts batch action in the Xero connector lets you find bank or
  general ledger accounts within your Xero organization.
---

# Xero - Search accounts batch action

The **Search accounts** batch action allows you to search for bank or general ledger accounts within your Xero organization. The list of accounts matching all search criteria is returned.

![Search accounts action](/assets/search-accounts-action.IGmppPbU.png)_Xero - Search accounts batch action_

## Input

| Input field | Description |
| --- | --- |
| Account ID | Enter the Xero internal ID to fetch the account. |
| Name | Provide the exact, case-sensitive name of the account to retrieve. |
| Code | Supply the exact, case-sensitive code of the account to retrieve. |
| Type | Enter the type of accounts to search for. Use uppercase for valid account types, such as `CURRENT` or `REVENUE`. |
| Status | Specify the status of the accounts to search for. Valid statuses are `ACTIVE` or `ARCHIVED`. |

## Output

| Output field | Description |
| --- | --- |
| Accounts | A collection of account details within Xero. |

---
