---
url: 'https://docs.workato.com/en/connectors/akeneo/get-record-action.md'
description: >-
  The Get record action retrieves the details of a record, such as a product,
  from Akeneo using its identifier or UUID.
---

# Akeneo - Get record action

The **Get record** action retrieves the details of a record, such as a product, from Akeneo using its identifier or UUID. Values are returned for all available channels and can be accessed through the **Channel values** list.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the type of record to retrieve. Currently, only `Product` is available. |
| Product family | Select a product family to include its family-specific attributes, such as color, size, and material, in the output schema. |
| Locales | Enter locales to limit attribute expansion. Leave blank to expand for all enabled locales. |
| Currencies | Enter currencies to limit priced attribute expansion. Leave blank to expand for all enabled currencies. |

## Output

| Output field | Description |
| --- | --- |
| UUID | Unique identifier of the record. |
| Identifier | Human-readable identifier (SKU) of the record. |
| Enabled | Whether the record is enabled. |
| Family | The product family code. |
| Channel values | Attribute values for the record across channels. Fields vary based on the selected product family, locales, and currencies. Refer to the [Akeneo documentation](https://api.akeneo.com/documentation/introduction.html) for the full list of available attributes. |
| Quality scores | Quality score per channel and locale. Populated when **Include quality scores** is enabled. |
| Completeness | Completeness percentage per channel and locale. Populated when **Include completeness** is enabled. |
| Categories | Categories the record is classified in. |
| Created | Date and time the record was created. |
| Updated | Date and time the record was last updated. |

---
