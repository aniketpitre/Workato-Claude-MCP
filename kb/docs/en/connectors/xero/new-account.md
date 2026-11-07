---
url: 'https://docs.workato.com/en/connectors/xero/new-account.md'
description: >-
  The New/updated account trigger in the Xero connector fires when a bank
  account or general ledger account is created or updated.
---

# Xero - New/updated account trigger

The **New/updated account** trigger activates when a bank account or G/L account is created or updated.

![New/updated account trigger](/assets/new-account-trigger.CwA-JVFK.png)_Xero - New/updated account trigger_

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Choose how often Workato checks for new or updated events. This field defaults to five minutes if left blank. The minimum value allowed is five minutes. |
| When first started, this recipe should pick up events from | Determine the starting point for the trigger to fetch events. You cannot change this value after the recipe has been run or tested. |

## Output

| Output field | Description |
| --- | --- |
| Code | The unique code for the account. |
| Name | The name of the account. |
| Type | The type of account. |
| Status | The current status of the account. |
| Description | A description of the account. |
| Tax type | The tax type assigned to the account. |
| Enable payments to account | Indicates whether the account can receive payments. |
| Shown in expense claims | Specifies if the account should be shown in expense claims. |
| Account ID | The unique identifier for the account. |
| Class | The classification of the account. |
| System account | Indicates if it is a system account. |
| Bank account number | The bank account number if applicable. |
| Bank account type | The type of bank account. |
| Currency code | The currency code associated with the account. |
| Reporting code | The reporting code for the account. |
| Reporting code name | The name of the reporting code. |
| Has attachments | Indicates whether there are attachments for the account. |
| Updated date | The date the account was last updated. |

---
