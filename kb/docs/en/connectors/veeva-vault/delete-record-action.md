---
url: 'https://docs.workato.com/en/connectors/veeva-vault/delete-record-action.md'
description: >-
  The Delete record action deletes a single record, such as a product, by its ID
  in Veeva Vault.
---

# Veeva Vault - Delete record action

The **Delete record** action deletes a single record, such as a product, by its ID in Veeva Vault.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the Vault object, for example **Product**. This list is populated dynamically from your Vault. |
| Record ID | Enter the Vault record ID you plan to delete. |

## Output

| Output field | Description |
| --- | --- |
| Response status | The status of the delete operation. |
| ID | The ID of the deleted record. |
| URL | The URL of the deleted record. |

---

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

---

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

---
