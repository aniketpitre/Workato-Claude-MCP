---
url: 'https://docs.workato.com/en/connectors/concur/actions/get-payment-types-v4.md'
description: >-
  The Get payment types batch action retrieves payment types for a specific user
  from SAP Concur using the v4 API.
---

# SAP Concur - Get payment types batch action

The **Get payment types** batch action retrieves all payment types applicable to the specified user from SAP Concur using the v4 API.

This action replaces the deprecated [Get all payment types](/en/connectors/concur/actions/get-all-payment-types-batch) action.

> **PREREQUISITES**
> 
> Your SAP Concur OAuth 2.0 connection must include the following scope to use this action:
> 
> - `expense.config.paymenttypes.restricted.read`

## Input

| Input field | Description |
| --- | --- |
| User ID | The unique identifier of the SAP Concur user. Use the [Get user](/en/connectors/concur/actions/get-user) action to retrieve the user ID. |

## Output

| Output field | Description |
| --- | --- |
| Payment types | List of payment types available to the specified user. |
| Payment type ID (Payment types) | The unique identifier of the payment type. |
| Payment type name (Payment types) | The name of the payment type. |
| Is default (Payment types) | Indicates whether this is the default payment type. |
| List size | The total number of payment types returned. |
| List index | The index of the current item in the list. |

---
