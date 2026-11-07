---
url: 'https://docs.workato.com/en/connectors/shopify/list-locations.md'
description: >-
  The List locations action in the Shopify connector lets you retrieve a list of
  all locations in your store.
---

# Shopify - List locations action

This action lists all locations in Shopify.

## Input

| Field | Description |
| --- | --- |
| Page size | The maximum number of results to show in a page. Defaults to 50 if left blank. Minimum page size is 1 and maximum allowed page size is 50. |
| Next page URL | Enter the next page URL obtained from action output in order to paginate through the results. |

## Output

The output to this action is a list of locations. Each location includes the following datapills.

| Field | Description |
| --- | --- |
| Name | The name of the location. |
| ID | The ID for the location. |
| Address 1 | The first line of the address. |
| Address 2 | The second line of the address. |
| City | The city the location is in. |
| Zip | The zip or postal code. |
| Province | The province the location is in. |
| Country | The country the location is in. |
| Phone | The phone number of the location. This value can contain special characters like `-` and `+`. |
| Country code | The two-letter country code. |
| Country name | The name of the location's country. |
| Province code | The two-letter code corresponding to province or state the location is in. |
| Admin GraphQL API ID | A unique Admin GraphQL API ID. |
| Legacy | Whether this is a fulfillment service location. If true, then the location is a fulfillment service location. If false, then the location was created by the merchant and isn't tied to a fulfillment service. |
| Localized country name | The localized name of the location's country. |
| Localized province name | The localized name of the location's region. Typically a province, state, or prefecture. |
| Created at | The date and time when the location was created. |
| Updated at | The date and time when the location was updated. |
| Next page URL | The URL to paginate through the next set of results. |

---
