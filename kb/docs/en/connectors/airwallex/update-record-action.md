---
url: 'https://docs.workato.com/en/connectors/airwallex/update-record-action.md'
description: >-
  The Update record action enables you to update a record you specify in
  Airwallex.
---

# Airwallex - Update record action

The **Update record** action enables you to update a record you specify in Airwallex.

## Input

| Input field | Description |
| --- | --- |
| Object | Specify the object to update its record. Fields load dynamically based on the selected object. |

Refer to the following example input schema for the **Customs declaration** object:

| Input field | Description |
| --- | --- |
| Customs declaration ID | Enter the ID of the customs declaration to update. |
| Customs code | Enter the China customs code. |
| Merchant customs name | Enter the merchant's registered name in the customs system (maximum length 256). |
| Merchant customs number | Enter the merchant's registered number in the customs system (maximum length 32). |
| Shopper ID | Enter the Mainland China ID of the shopper. |
| Shopper name | Enter the name of the shopper in simplified Chinese. |
| Sub order amount | Enter the amount for the sub order. |

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the data tree to subsequent steps. Refer to the following example output fields for the **Customs declarations** object:

| Output field | Description |
| --- | --- |
| Available request ID | Unique identifier of the customs request. |
| Created at | Date and time when the record was created. |
| Customs details | Customs-related information for the transaction. |
| Customs code | Code assigned by customs. |
| Merchant customs name | The merchant's registered name in the customs system. |
| Merchant customs number | The merchant's registered number in the customs system. |
| Customs status message | Status message returned by customs. |
| ID | Unique identifier for the customs record. |
| Payment method type | Payment method used for the transaction. |
| Provider transaction ID | Transaction ID assigned by the provider. |
| Request ID | Unique identifier for the request. |
| Shopper identity check result | Result of the shopper identity verification. |
| Status | Current status of the customs declaration. |
| Sub order | Information related to the suborder. |
| Amount | Amount of the sub order. |
| Currency | Currency of the sub order. |
| Order number | Order number associated with the sub-order. |
| Provider order ID | Provider's unique identifier for the order. |
| Shipping fee | Shipping fee charged for the sub-order. |
| Updated at | Date and time when the record was last updated. |
| Verification department code | Code of the verification department. |
| Verification department transaction ID | Transaction ID assigned by the verification department. |

---
