---
url: 'https://docs.workato.com/en/connectors/akeneo/search-records-action.md'
description: >-
  The Search records action searches for records, such as products, in Akeneo
  that match the criteria and filters you provide.
---

# Akeneo - Search records action

The **Search records** action searches for records, such as products, in Akeneo that match the criteria and filters you provide.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the type of record to search. Only `Product` is available. |
| Channel | Select a channel to return product data for that channel only. Select `All channels` to retrieve a complete product representation for every channel in the `Channel values` list. Only available when **Object** is `Product`. |
| Product family | Select a product family to include its family-specific attributes, such as color, size, and material, as search criteria and in the output schema. Without a family, only the basic product structure is available. |
| Locales | Enter locales to limit attribute expansion. Leave blank to expand for all enabled locales. |
| Currencies | Enter currencies to limit priced attribute expansion. Leave blank to expand for all enabled currencies. |
| Categories | Return only products classified in the selected categories. Leave blank to search across all categories. |

## Output

| Output field | Description |
| --- | --- |
| Products | Array of matching records, such as products. Each record's fields vary based on the selected product family, locales, and currencies. Refer to the [Akeneo documentation](https://api.akeneo.com/documentation/introduction.html) for the full list of available attributes. |
| Items count | Total number of matching products. Populated when **Include total count** is enabled. |
| Current page | Page number returned by this call. Only relevant when using page pagination. |
| Next page | Page number to request next when using page pagination. Blank when there are no more pages. |
| Next cursor | Cursor for the next page when using search after pagination. Blank when there are no more pages. |

---
