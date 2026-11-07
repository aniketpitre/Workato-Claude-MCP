---
url: 'https://docs.workato.com/en/connectors/veeva-vault/upsert-record-action.md'
description: >-
  The Upsert record action creates a new record in Veeva Vault, or updates the
  existing record if a match is found.
---

# Veeva Vault - Upsert record action

The **Upsert record** action creates a new record in Veeva Vault, or updates the existing record if a match is found. The value of the **Match field** determines which record to match.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the Vault object you plan to upsert. For example, **Product**. This list is populated dynamically from your Vault. |
| Match field | Select the unique field used to match existing records. Defaults to **External ID**. This list is populated dynamically from the selected object's unique fields. |
| Field values | Field values for the record. Include the value for the **Match field** to match an existing record. |

## Output

| Output field | Description |
| --- | --- |
| Response status | The status of the write operation. |
| ID | The ID of the created or updated record. |
| URL | The URL of the created or updated record. |
| Event | Either `created__sys` or `updated__sys`. |
| ID param value | The value of the **Match field** used to match the record. |

---
