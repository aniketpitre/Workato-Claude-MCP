---
url: 'https://docs.workato.com/en/connectors/jira/search-issues-batch-action.md'
description: >-
  This action searches Jira for issues that exactly match the criteria you
  specify and retrieves the results in batches.
---

# Jira - Search issues action (batch)

The **Search issues (batch)** action searches Jira for issues that exactly match the criteria you specify and retrieves the results in batches.

> **RESULTS FOR RECENT CHANGES**
> 
> Jira search results may not reflect recent changes. Use the **Reconcile Issue IDs** field to return real-time results for up to `50` issues. Alternatively, add a short delay after steps that create or update records. For example, using the **Ruby snippets by Workato** `sleep` function or the **Scheduler by Workato** **Wait for time duration** action.

## Input

| Input field | Description |
| --- | --- |
| Issue key | Enter the issue key to search by. |
| Summary | Enter the summary to search by. |
| Output fields | Select the fields to retrieve from Jira or enter them manually. If you select **Enter fields**, you must supply a comma-separated list of IDs for the fields you plan to use in the recipe. For example: `parent,lastViewed` |
| Reconcile Issue IDs | Provide up to `50` issue IDs (comma-separated) to return consistent results immediately after updates. Consistency is only ensured for specified issues. |

> **SEARCH CRITERIA USES AND LOGIC**
> 
> The search criteria you provide is combined using `AND` logic. Only issues matching _all_ values are returned. Partial matches aren't returned.

## Output

| Output field | Description |
| --- | --- |
| ID | The numeric Jira identifier for the issue. |
| Self | The API URL of the issue. |
| Key | The human-readable Jira identifier for the issue. |
| Fields | Contains information about the object's fields, including its `Parent` and `Last Viewed` time. Workato automatically fetches and expands all parameters. Refer to the Jira Cloud REST API documentation on [resource expansion](https://developer.atlassian.com/cloud/jira/platform/rest/#expansion) for more information. |
| List size | The total number of issues retrieved. |
| List index | The position of the current issue in the results list. |

---
