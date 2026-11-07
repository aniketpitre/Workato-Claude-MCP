---
url: >-
  https://docs.workato.com/en/connectors/mastercard/get-status-of-merchant-enrollment-action.md
description: >-
  The Get status of merchant enrollment action enables you to fetch the status
  of enrolled merchants.
---

# Mastercard - Get status of merchant enrollment action

The **Get status of merchant enrollment** action enables you to fetch the status of enrolled merchants.

## Input

| Input fields | Description |
| --- | --- |
| Transaction ID | Provide the transaction ID of the merchant enrolled. |
| Limit | Enter the number of records to fetch. |
| Offset | Determine the offset of the records. |

## Output

| Output fields | Description |
| --- | --- |
| Message type | Type of the message. |
| Total records | Total number of records uploaded. |
| Offset | Offset of the records to be returned. This number must be equal or greater than zero. |
| Limit | Number of records to fetch per request. This number should be less than or equal to the configured quota on the API side, which is `1000`. |
| Transaction ID | Unique ID of the transaction. |
| Processor name | Name of the processor. |
| Report status | Indicates whether the status is completed or failed. |
| Success records | Number of successful records in the current page. |
| Failed records | Number of failed records in the current page. |
| Merchant data | An array of merchant data outbound objects containing the status response details. |
| Acquirer BIN | Acquirer reference ID number. |
| Acquirer CID | Acquirer company ID. |
| Acquirer ICA | Acquirer ICA number. |
| Acquirer name | The acquirer name. |
| Merchant ID | Acquirer merchant ID. |
| Merchant name | Name of the merchant. |
| Identity check express | Flag for Identity Check Express. Valid values are `Y` or `N`. |
| Delete reason | Reason for deleting the merchant enrollment. Only required if the selected action is delete. |
| Status | Status of the record. This is either `Successful` or `Rejected`. |
| Reason | Contains either new record data for successful merchant enrollment or the reason for failure for rejected records. |
