---
url: >-
  https://docs.workato.com/en/connectors/mastercard/enroll-or-unenroll-merchants.md
description: >-
  The Enroll/unenroll merchants action enables you to add or delete merchants in
  Mastercard.
---

# Mastercard - Enroll/unenroll merchants action

The **Enroll/unenroll merchants** action enables you to add or delete merchants in Mastercard.

## Input

| Input fields | Description |
| --- | --- |
| Merchant data | Provide an array of merchant data objects containing the merchant details. |
| Processor name | Provide the name of the service provider or acquirer. For example, `MPGS`. |
| Action | Select the action to be performed, either add or delete. |
| Acquirer BIN | Provide the acquirer reference ID number. |
| Acquirer CID | Provide the acquirer company ID. |
| Acquirer ICA | Provide the acquirer ICA number. |
| Acquirer Name | Enter the acquirer name. |
| Merchant ID | Provide the acquirer Merchant ID. |
| Merchant name | Enter the name of the merchant. |
| Identity Check Express | Select a flag for Identity Check Express. Valid values are `Y` or `N`. |
| Delete reason | Provide a reason for deleting the merchant enrollment. This is only required if the selected action is delete. |

## Output

| Output fields | Description |
| --- | --- |
| Message type | Type of the message. |
| Total records | Total number of records processed. |
| Transaction ID | Unique ID of the transaction. |
