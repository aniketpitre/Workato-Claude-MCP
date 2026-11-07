---
url: >-
  https://docs.workato.com/en/connectors/veeva-vault/bulk-upsert-records-action.md
description: >-
  The Bulk upsert records (batch) action posts up to 500 records in a single
  request to the Vault bulk endpoint in Veeva Vault.
---

# Veeva Vault - Bulk upsert records (batch) action

The **Bulk upsert records (batch)** action posts up to `500` records in a single request to the Vault bulk endpoint in Veeva Vault.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the Vault object you plan to upsert. For example, **Product**. This list is populated dynamically from your Vault. |
| Match field | Select the unique field used to match existing records. Defaults to **External ID**. This list is populated dynamically from the selected object's unique fields. |
| Migration mode | Set to enable record migration mode. Requires the Record Migration permission in Vault. Defaults to unchecked. |
| Records | List of records to upsert. Maximum `500` per batch. |

## Output

| Output field | Description |
| --- | --- |
| Response status | The overall status of the bulk write operation. |
| Success count | The number of records successfully written. |
| Warning count | The number of records evaluated but not changed, for example an upsert no-op. |
| Failure count | The number of records that failed to write. |
| Data | An array with one entry per record in the batch: **Response status**, **ID**, **URL**, **Event**, **ID param value**, **Errors**, and **Warnings**. |
