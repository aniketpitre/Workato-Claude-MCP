---
url: >-
  https://docs.workato.com/en/connectors/concur/actions/get-all-expense-group-configurations-batch.md
description: >-
  The Get all expense group configurations batch action retrieves all expense
  group configurations from SAP Concur.
---

# SAP Concur - Get all expense group configurations action (batch)

The **Get all expense group configurations** batch action retrieves all expense group configurations from SAP Concur.

> **DEPRECATION NOTICE**
> 
> This action uses the SAP Concur v3 API, which is deprecated. Migrate to the [Get expense group configuration](/en/connectors/concur/actions/get-expense-group-v4) action.

## Input

This action doesn't require any input configuration.

## Output

| Output field | Description |
| --- | --- |
| Expense group configurations | List of all expense group configurations retrieved from SAP Concur. |
| ID (Expense group configurations) | The unique identifier of the expense group configuration. |
| Name (Expense group configurations) | The name of the expense group configuration. |
| URI (Expense group configurations) | The URI to the resource. |
| Attendee list form ID (Expense group configurations) | The unique identifier for the attendee list form. |
| Attendee list form name (Expense group configurations) | The name of the attendee list form. |
| Allow user register yodlee (Expense group configurations) | Indicates whether users in the expense group are allowed to register Yodlee credit cards. |
| Allow user digital tax invoice (Expense group configurations) | Indicates whether users are allowed to upload digital tax invoices. |
| Cash advance (Expense group configurations) | Cash advance configuration settings for the expense group. |
| Allow user carry balance (Cash advance) | Indicates whether users can carry forward their cash advance balance. |
| Allow user link multiple (Cash advance) | Indicates whether users can link multiple cash advances. |
| Allow user update exchange rate (Cash advance) | Indicates whether users can update the exchange rate for cash advances. |
| Name (Cash advance) | The name of the cash advance workflow. |
| Workflow ID (Cash advance) | The unique identifier for the cash advance workflow. |
| Payment types (Expense group configurations) | The payment types available in the expense group. |
| ID (Payment types) | The unique identifier of the payment type. |
| Name (Payment types) | The name of the payment type. |
| Is default (Payment types) | Indicates whether this is the default payment type. |
| Policies (Expense group configurations) | The expense policies associated with the expense group. |
| ID (Policies) | The unique identifier of the policy. |
| Name (Policies) | The name of the policy. |
| Is default (Policies) | Indicates whether this is the default policy. |
| Is inheritable (Policies) | Indicates whether the policy can be inherited. |
| Expense types (Expense group configurations) | The expense types available in the expense group. |
| Expense type code (Expense types) | The code for the expense type. |
| Name (Expense types) | The name of the expense type. |
| Expense code (Expense types) | The expense code associated with the expense type. |
| Attendee types (Expense group configurations) | The attendee types available in the expense group. |
| Attendee type code (Attendee types) | The code for the attendee type. |
| Name (Attendee types) | The name of the attendee type. |
