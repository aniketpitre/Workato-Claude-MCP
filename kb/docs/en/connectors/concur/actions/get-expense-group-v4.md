---
url: 'https://docs.workato.com/en/connectors/concur/actions/get-expense-group-v4.md'
description: >-
  The Get expense group configuration batch action retrieves the expense group
  configuration for a specific user from SAP Concur using the v4 API.
---

# SAP Concur - Get expense group configuration action (batch)

The **Get expense group configuration** batch action retrieves the expense group configuration applicable to the specified user from SAP Concur using the v4 API, including policies, payment types, and attendee types.

This action replaces the deprecated [Get all expense group configurations](/en/connectors/concur/actions/get-all-expense-group-configurations-batch) action.

> **PREREQUISITES**
> 
> Your SAP Concur OAuth 2.0 connection must include the following scopes to use this action:
> 
> - `expense.config.groups.restricted.read`
> - `expense.config.policies.restricted.read`
> - `expense.config.expensetypes.restricted.read`

## Input

| Input field | Description |
| --- | --- |
| User ID | The unique identifier of the SAP Concur user. Use the [Get user](/en/connectors/concur/actions/get-user) action to retrieve the user ID. |

## Output

| Output field | Description |
| --- | --- |
| Group ID | The unique identifier of the expense group configuration. |
| Group name | The name of the expense group configuration. |
| Allow user digital tax invoice | Indicates whether users are allowed to upload digital tax invoices. |
| Allow user register yodlee | Indicates whether users in the expense group are allowed to register Yodlee credit cards. |
| Attendee list form ID | The unique identifier for the attendee list form. |
| Attendee list form name | The name of the attendee list form. |
| Cash advance | Cash advance configuration settings for the expense group. |
| Payment types | The payment types available in the expense group. |
| Policies | The expense policies associated with the expense group. |
| Attendee types | The attendee types available in the expense group. |

---

---
url: >-
  https://docs.workato.com/en/connectors/concur/actions/get-all-expense-types-batch.md
description: >-
  The Get all expense types batch action retrieves all expense types from SAP
  Concur.
---

# SAP Concur - Get all expense types action (batch)

The **Get all expense types** batch action retrieves all expense types from SAP Concur.

> **DEPRECATION NOTICE**
> 
> This action uses the SAP Concur v3 API, which is deprecated. Migrate to the [Get expense types](/en/connectors/concur/actions/get-expense-types-v4) action.

## Input

This action doesn't require any input configuration.

## Output

| Output field | Description |
| --- | --- |
| Expense types | List of all expense types retrieved from SAP Concur. |
| Expense type code (Expense types) | The code for the expense type. |
| Expense code (Expense types) | The code for the expense category. |
| Expense type name (Expense types) | The name of the expense type. |

---
