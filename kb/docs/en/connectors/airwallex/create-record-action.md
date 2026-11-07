---
url: 'https://docs.workato.com/en/connectors/airwallex/create-record-action.md'
description: >-
  The Create record action enables you to create the specified record in
  Airwallex.
---

# Airwallex - Create record action

The **Create record** action enables you to create a record in Airwallex.

## Input

| Input field | Description |
| --- | --- |
| Object | Specify the object to create its record. Fields load dynamically based on the selected object. |

For example, the input schema is as follows if you select the **Refund** object:

| Input field | Description |
| --- | --- |
| Amount | Specify the amount of the refund. The remaining captured amount not yet refunded is used if not specified. |
| Metadata | Specify key-value pairs to attach as metadata to the refund. |
| Key | Enter the metadata key. |
| Value | Enter the metadata value. |
| Payment attempt ID | Select the payment attempt ID for which this refund is created. Either the payment attempt ID or the payment intent ID must be provided. |
| Payment intent ID | Select the payment intent ID for which this refund is created. The payment intent ID or the payment attempt ID must be provided. |
| Reason | Provide the reason for the refund. |

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the data tree to subsequent steps. Refer to the following example output for the **Refund** object:

| Output field | Description |
| --- | --- |
| Acquirer reference number | Reference number provided by the acquirer for the refund. |
| Amount | Amount refunded. |
| Created at | Date and time when the refund was created. |
| Currency | Currency in which the refund was processed. |
| ID | Unique identifier for the refund. |
| Metadata | A set of key-value pairs attached to the refund. |
| Key | Metadata key. |
| Value | Metadata value. |
| List size | Total number of metadata entries. |
| List index | Position of the metadata entry in the list. |
| Payment attempt ID | ID of the payment attempt for which this refund was created. |
| Payment intent ID | ID of the payment intent for which this refund was created. |
| Reason | Reason provided for the refund. |
| Request ID | Unique identifier for the refund request. |
| Status | Current status of the refund. For example, `ACCEPTED`. |
| Updated at | Date and time when the refund was updated. |

---
