---
url: 'https://docs.workato.com/en/connectors/clay/search-companies-action.md'
description: >-
  Search for companies in Clay by industry, size, funding, location, revenue, or
  type.
---

# Clay - Search companies action

The **Search companies** action uses firmographic filters to search for companies in Clay. It returns one page of results per run.

## Input

You must provide at least one firmographic filter (**Industries**, **Employee size**, **Funding amount**, **Annual revenue**, **Locations**, **Company type**, or **Company identifiers**) or a **Search ID**.

| Input field | Description |
| --- | --- |
| Industries | Optional. Enter a comma-separated list of industries, such as `Software Development`. Leave blank to skip this filter. |
| Employee size | Optional. Use the drop-down menu to select one or more employee size values, or enter a comma-separated list of values. Leave blank to skip this filter. |
| Funding amount | Optional. Use the drop-down menu to select one or more funding amount values, or enter a comma-separated list of values. Leave blank to skip this filter. |
| Annual revenue | Optional. Use the drop-down menu to select one or more annual revenue ranges, or enter a comma-separated list of ranges. Leave blank to skip this filter. |
| Locations | Optional. Enter a comma-separated list of cities, states, or countries. Leave blank to skip this filter. |
| Company type | Optional. Use the drop-down menu to select one or more company types, or enter a comma-separated list of types. Leave blank to skip this filter. |
| Company identifiers | Optional. Enter a comma-separated list of domains or company LinkedIn URLs to include. The action doesn't accept company names. Leave blank to skip this filter. |
| Limit | Optional. Enter the number of companies to return, from `1` to `500`. Leave blank to use the default of `20`. |
| Search ID | Optional. Enter the **Search ID** from a previous run to retrieve the next page of results. The action ignores the filters when you provide a **Search ID**. Leave blank to start a new search. |

## Output

The following are a representative set of output fields. Refer to the output datapills in the recipe editor to view the remaining fields.

| Output field | Description |
| --- | --- |
| Items | The list of companies that match the filters. |
| Name (Items) | The name of the company. |
| Domain (Items) | The domain of the company. |
| LinkedIn URL (Items) | The LinkedIn URL of the company. |
| Industry (Items) | The industry of the company. |
| Company size (Items) | The employee count range of the company. |
| Location (Items) | The location of the company. |
| Has more | Indicates whether more results are available. Use the **Search ID** in a later run to retrieve the next page. |
| Search ID | The ID of the search. |
| Period quota | The usage quota for your Clay account in the current period. |

---
