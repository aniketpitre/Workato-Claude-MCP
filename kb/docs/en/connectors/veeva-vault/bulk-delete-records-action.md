---
url: >-
  https://docs.workato.com/en/connectors/veeva-vault/bulk-delete-records-action.md
description: >-
  The Bulk delete records (batch) action deletes up to 500 records by ID in a
  single request in Veeva Vault.
---

# Veeva Vault - Bulk delete records (batch) action

The **Bulk delete records (batch)** action deletes up to `500` records by ID in a single request in Veeva Vault.

## Input

Input fields are generated dynamically based on the object you select. Refer to the [Veeva Vault](https://developer.veevavault.com/api/26.1/) documentation for a complete list of input fields. The following field is common to all objects.

| Input field | Description |
| --- | --- |
| Object | Select the Vault object you plan to delete. For example, **Product**. This list is populated dynamically from your Vault. |

## Output

| Output field | Description |
| --- | --- |
| Response status | The overall status of the bulk delete operation. |
| Success count | The number of records successfully deleted. |
| Warning count | The number of records evaluated but not changed. |
| Failure count | The number of records that failed to delete. |
| Data | An array with one entry per record in the batch: **Response status**, **ID**, **Errors** (array of **Type** and **Message**), and **Warnings** (array of **Warning type** and **Message**). |
