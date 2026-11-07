---
url: 'https://docs.workato.com/en/connectors/veeva-vault/create-record-action.md'
description: 'The Create record action creates a record, such as a product, in Veeva Vault.'
---

# Veeva Vault - Create record action

The **Create record** action creates a record, such as a product, in Veeva Vault. Veeva returns a per-record response.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the Vault object, for example **Product**. This list is populated dynamically from your Vault. |
| Field values | Provide values for the new record fields. |

## Output

| Output field | Description |
| --- | --- |
| Response status | The status of the write operation. |
| ID | The ID of the created record. |
| URL | The URL of the created record. |
| Event | Either `created__sys` or `updated__sys`. |
| ID param value | The value of the field used to match the record, if applicable. |

---
