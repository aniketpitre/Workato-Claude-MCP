---
url: >-
  https://docs.workato.com/en/connectors/oracle-fusion-cloud/actions/upsert-record.md
description: The Upsert record action creates or updates a record.
---

# Oracle Fusion Cloud - Upsert record action

The **Upsert record** action creates or updates a record. If the primary key, such as the Invoice ID, is present, the record is updated. If no primary key is provided, the action creates a new record.

The same logic applies to child objects:

- If the primary key is present, the record is updated.
- If no primary key is provided, the record is inserted into the existing or new parent object.

Common use cases include:

- Adding new invoice lines to an existing invoice
- Updating a specific invoice line
- Updating an invoice with new currency rates
- Inserting or updating products from a Google Sheet based on Inventory item ID

## Input

| Input field | Description |
| --- | --- |
| Object | Select the object type of the record you plan to upsert. |

Additional fields load dynamically based on the object you select.

## Output

The output of this action includes details about the upserted record.
