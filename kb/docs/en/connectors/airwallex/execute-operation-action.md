---
url: 'https://docs.workato.com/en/connectors/airwallex/execute-operation-action.md'
description: >-
  The Execute operation action enables you to execute available operations that
  are not CRUD operations in Airwallex.
---

# Airwallex - Execute operation action

The **Execute operation** action enables you to execute available operations that are not CRUD operations, Create (add new data), Read (retrieve data), Update (modify existing data), and Delete (remove data), in Airwallex.

## Input

| Input field | Description |
| --- | --- |
| Operation | Specify the operation to perform. Fields load dynamically based on the operation you select. |

Refer to the following example input schema for **Retrieve a current rate**:

| Input field | Description |
| --- | --- |
| Buy currency | Enter the three-letter ISO-4217 currency code the client buys. |
| Sell currency | Enter the three-letter ISO-4217 currency code the client sells. This must be sent by the settlement cutoff time. |
| Buy amount | Specify the amount the client buys in the buy currency. This field must be left blank if the sell amount is specified. This field defaults to `10,000` if neither the buy amount nor the sell amount is specified. |
| Conversion date | Enter the date on which the conversion will be settled. Defaults to the current date if funding is available, unless specified. |
| Sell amount | Specify the amount the client sells in the selling currency. Must be blank if buy amount is specified. |

## Output

The output fields are determined by the operation selected in the input. Map the relevant datapill from the data tree to subsequent steps. Refer to the example output fields for the **Retrieve a current rate** operation:

| Output field | Description |
| --- | --- |
| Buy currency | Currency bought by the client in three-letter ISO-4217 code. |
| Conversion date | Date on which the conversion was settled. |
| Created at | Date and time when the conversion record was created. |
| Currency pair | Currency pair for the conversion. For example, `AUD/USD`. |
| Dealt currency | Currency in which the deal was executed. |
| Rate | Conversion rate applied for the transaction. |
| Rate details | Detailed breakdown of rate information. |
| Buy amount | Amount bought in buy currency under rate details. |
| Level | Pricing level applied. For example, `CLIENT`. |
| Rate (nested) | Specific conversion rate under rate details. |
| Sell amount | Amount sold in the selling currency under the rate details. |
| List size | Total number of entries in the rate details list. |
| List index | Position of the rate detail entry in the list. |
| Sell currency | Currency sold by the client in three-letter ISO-4217 code. |

---

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

---
