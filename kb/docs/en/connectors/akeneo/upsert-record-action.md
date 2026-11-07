---
url: 'https://docs.workato.com/en/connectors/akeneo/upsert-record-action.md'
description: >-
  The Upsert record action creates or updates a record, such as a product, in
  Akeneo.
---

# Akeneo - Upsert record action

The **Upsert record** action creates or updates a record, such as a product, in Akeneo. Akeneo uses the UUID to check whether the record exists in the system. New records are created for non-existing UUIDs and updates are made to existing records with a matching UUID. Provide the UUID of an existing record to avoid creating a duplicate record by mistake.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the type of record to create or update. Only `Product` is available. |
| Product family | Select a product family to generate the attribute update schema. Only attributes belonging to the selected family can be updated, with locale, channel, and currency selectors added automatically where required. |
| Update parent values | Enable to include parent product model attributes in the input schema and allow updates to those inherited values. |
| Locales | Enter locales to limit attribute expansion. Leave blank to expand for all enabled locales. |
| Currencies | Enter currencies to limit priced attribute expansion. Leave blank to expand for all enabled currencies. |
| UUID | The UUID of the record to create or update. |

## Output

| Output field | Description |
| --- | --- |
| UUID | Unique identifier of the record. |
| Identifier | Human-readable identifier (SKU) of the record. |
| Enabled | Whether the record is enabled. |
| Family | The product family code. |
| Channel values | Attribute values for the record across channels. Fields vary based on the selected product family, locales, and currencies. Refer to the [Akeneo documentation](https://api.akeneo.com/documentation/introduction.html) for the full list of available attributes. |
| Categories | Categories the record is classified in. |
| Created | Date and time the record was created. |
| Updated | Date and time the record was last updated. |

---
