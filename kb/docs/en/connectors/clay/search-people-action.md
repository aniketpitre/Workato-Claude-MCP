---
url: 'https://docs.workato.com/en/connectors/clay/search-people-action.md'
description: 'Search for people in Clay by company, job title, seniority, location, or name.'
---

# Clay - Search people action

The **Search people** action uses role and company filters to search for people in Clay. It returns one page of results per run.

## Input

You must provide at least one filter (**Company identifier**, **Job title**, **Seniority**, **Location**, or **Names**) or a **Search ID**.

| Input field | Description |
| --- | --- |
| Company identifier | Optional. Enter the domain, such as `stripe.com`, or the LinkedIn URL of the company. The action doesn't accept company names. Leave blank to skip this filter. |
| Job title | Optional. Enter job title keywords, such as `VP Sales`. Leave blank to skip this filter. |
| Seniority | Optional. Use the drop-down menu to select one or more seniority levels, or enter a comma-separated list of levels. Leave blank to skip this filter. |
| Location | Optional. Enter the name of a city or country, such as `San Francisco`. Leave blank to skip this filter. |
| Names | Optional. Enter a comma-separated list of first names, last names, or full names. Leave blank to skip this filter. |
| Limit | Optional. Enter the number of people to return, from `1` to `500`. Leave blank to use the default of `20`. |
| Search ID | Optional. Enter the **Search ID** from a previous run to retrieve the next page of results. The action ignores the filters when you provide a **Search ID**. Leave blank to start a new search. |

## Output

The following are a representative set of output fields. Refer to the output datapills in the recipe editor to view the remaining fields.

| Output field | Description |
| --- | --- |
| Items | The list of people that match the filters. |
| Name (Items) | The full name of the person. |
| LinkedIn URL (Items) | The LinkedIn URL of the person. |
| Company domain (Items) | The domain of the person's company. |
| Location (Items) | The location of the person. |
| Latest experience title (Items) | The job title of the person's latest experience. |
| Latest experience company (Items) | The company of the person's latest experience. |
| Has more | Indicates whether more results are available. Use the **Search ID** in a later run to retrieve the next page. |
| Search ID | The ID of the search. |
| Period quota | The usage quota for your Clay account in the current period. |

---
