---
url: 'https://docs.workato.com/en/connectors/veeva-vault/update-record-action.md'
description: 'The Update record action updates a record, such as a product, in Veeva Vault.'
---

# Veeva Vault - Update record action

The **Update record** action updates a record, such as a product, in Veeva Vault. Veeva Vault doesn't support a true single-record update API, so this action posts the supplied record ID and field values through an upsert, matching on the record ID.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the Vault object you plan to update. For example, **Product**. This list is populated dynamically from your Vault. |
| Record ID | Enter the Vault record ID you plan to update. |
| Field values | Enter field values for the record. |

## Output

| Output field | Description |
| --- | --- |
| Response status | The status of the write operation. |
| ID | The ID of the updated record. |
| URL | The URL of the updated record. |
| Event | Either `created__sys` or `updated__sys`. |
| ID param value | The value of the field used to match the record, if applicable. |

---
