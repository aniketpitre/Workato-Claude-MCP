---
url: 'https://docs.workato.com/en/connectors/ramp/get-record-details-by-id-action.md'
description: >-
  Retrieve a single Ramp record by ID, with fields generated live from Ramp's
  own API schema for the object you select.
---

# Ramp - Get record details by ID action

The **Get record details by ID** action retrieves a single record by ID in Ramp.

## Input

Input fields dynamically generate based on the object you select and the get operation. The following fields are common to all objects. Refer to the Ramp [REST API](https://docs.ramp.com/developer-api/v1/api/) documentation for a list of input fields.

| Input field | Description |
| --- | --- |
| Object | Select the Ramp object to retrieve, for example **Transactions**, **Cards**, or **Users**. |
| ID | Enter the record's unique identifier. This field is available after you select **Object**, and matches that object's ID path parameter. |

For example, a single `transaction_id` input field is available after you select **Transactions**. This matches Ramp's `GET /developer/v1/transactions/{transaction_id}` endpoint.

## Output

Output fields dynamically generate based on the object you select. Refer to the Ramp [REST API](https://docs.ramp.com/developer-api/v1/api/) documentation for a list of output fields.

The following are a representative set of output fields available after you select **Transactions**: `id`, `amount`, `currency_code`, `merchant_name`, `card_holder`, `state`, and `memo`.

---
