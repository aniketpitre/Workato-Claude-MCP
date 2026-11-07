---
url: >-
  https://docs.workato.com/en/connectors/concur/actions/get-all-payment-types-batch.md
description: >-
  The Get all payment types batch action retrieves all payment types from SAP
  Concur.
---

# SAP Concur - Get all payment types action (batch)

The **Get all payment types** batch action retrieves all payment types from SAP Concur.

> **DEPRECATION NOTICE**
> 
> This action uses the SAP Concur v3 API, which is deprecated. Migrate to the [Get payment types](/en/connectors/concur/actions/get-payment-types-v4) action.

## Input

This action doesn't require any input configuration.

## Output

| Output field | Description |
| --- | --- |
| Payment types | List of all payment types retrieved from SAP Concur. |
| ID (Payment types) | The unique identifier of the payment type. |
| Name (Payment types) | The name of the payment type. |
| Is default (Payment types) | Indicates whether this is the default payment type. |
