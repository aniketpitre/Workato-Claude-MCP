---
url: >-
  https://docs.workato.com/en/connectors/airwallex/get-record-details-by-id-action.md
description: >-
  The Get record details by ID action enables you to retrieve the details of a
  specific record in Airwallex.
---

# Airwallex - Get record details by ID action

The **Get record details by ID** action enables you to retrieve the details of a record you specify in Airwallex.

## Input

| Input field | Description |
| --- | --- |
| Object | Specify the object to retrieve its details. Fields load dynamically based on the selected object. |

Refer to the example input schema for the **Refund** object:

| Input field | Description |
| --- | --- |
| Refund ID | Select or enter the refund ID to retrieve refund details. |

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the data tree to subsequent steps. Refer to the following example output fields for the **Refund** object:

| Output field | Description |
| --- | --- |
| Acquirer reference number | Reference number provided by the acquirer for the refund. |
| Amount | Amount that has been refunded. |
| Created at | Date and time when the refund was created. |
| Currency | Currency in which the refund was processed. |
| ID | Unique identifier for the refund. |
| Metadata | Set of key-value pairs attached to the refund. |
| Key | Metadata key. |
| Value | Metadata value. |
| List size | Total number of metadata entries. |
| List index | Position of the metadata entry in the list. |
| Payment attempt ID | ID of the payment attempt against which this refund was created. |
| Payment intent ID | ID of the payment intent against which this refund was created. |
| Reason | Reason provided for the refund. |
| Request ID | Unique identifier for the refund request. |
| Status | Current status of the refund. For example: `ACCEPTED`. |
| Updated at | Date and time when the refund was updated. |
