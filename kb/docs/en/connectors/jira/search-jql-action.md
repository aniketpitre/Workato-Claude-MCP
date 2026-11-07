---
url: 'https://docs.workato.com/en/connectors/jira/search-jql-action.md'
description: >-
  This action searches Jira for issues that match the JQL query string you
  provide and retrieves the results in batches.
---

# Jira - Search issues by JQL action (batch)

The **Search issues by JQL (batch)** action searches Jira for issues that match the JQL query string you provide and retrieves the results in batches. Use this action to return one or more Jira issues, optionally filter fields, and handle paginated results for large datasets.

> **RESULTS FOR RECENT CHANGES**
> 
> Jira search results may not reflect recent changes. Use the **Reconcile Issue IDs** field to return real-time results for up to `50` issues. Alternatively, add a short delay after steps that create or update records. For example, using the **Ruby snippets by Workato** `sleep` function or the **Scheduler by Workato** **Wait for time duration** action.

## Input

| Input field | Description |
| --- | --- |
| JQL query string | Specify a valid JQL query. The action only returns issues that match the query exactly. The action fails if no query is entered. |
| Output fields | Select the fields to retrieve from Jira or enter them manually. If you select **Enter fields**, you must supply a comma-separated list of IDs for the fields you plan to use in the recipe. For example: `parent,lastViewed` |
| Max result (Pagination) | Enter the maximum number of issues to return. The minimum value is `1`, the maximum value is `5000`, and the default value is `100`. |
| Reconcile Issue IDs | Provide up to `50` issue IDs (comma-separated) to return consistent results immediately after updates. Consistency is only ensured for specified issues. |

> **SEARCH CRITERIA USES AND LOGIC**
> 
> The search criteria you provide is combined using `AND` logic. Only issues matching _all_ values are returned. Partial matches aren't returned.

## Output

| Output field | Description |
| --- | --- |
| Expand | Issue data expanded in the response. |
| Start at | The index of the current results page in the results list. |
| Max results | The maximum number of results returned in each page. |
| Total | The total number of results retrieved. |
| Next page token | The token to use in the **Next page token** input field to retrieve the next batch. |
| Issues | Array of issue objects that matched the query. |

---
