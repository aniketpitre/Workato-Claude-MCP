---
url: 'https://docs.workato.com/en/connectors/akeneo/new-updated-record-trigger.md'
description: >-
  The New/updated record trigger monitors Akeneo for records, such as products,
  that are created or updated.
---

# Akeneo - New/updated record trigger

The **New/updated record** trigger monitors Akeneo for records, such as products, that are created or updated. Each record creates a separate recipe job, and you can select an object to access its properties directly in the recipe.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Select an interval in minutes to specify how frequently to check for new events. |
| Object | Select the type of record to monitor. Only `Product` is available. |
| Channel | Select a channel to monitor product data for that channel only. Select `All channels` to retrieve a complete product representation for every channel in the `Channel values` list. |
| Product family | Select a product family to load its family-specific attributes, such as color, size, and material. Only the basic product structure is shown without a family selected. |
| Locales | Enter locales to limit attribute expansion. Leave blank to expand for all enabled locales. |
| Currencies | Enter currencies to limit priced attribute expansion. Leave blank to expand for all enabled currencies. |
| When first started, this recipe should pick up events from | Select a date/time to begin picking up trigger events from. Defaults to the current time. |
| Attributes | Select the product attributes to include in the output. Leave blank to return all attributes of the selected family. Only available when a product family is selected. |

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
