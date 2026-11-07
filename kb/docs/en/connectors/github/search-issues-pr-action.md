---
url: 'https://docs.workato.com/en/connectors/github/search-issues-pr-action.md'
description: >-
  The Search issues and pull requests (batch) action searches for a issues or
  pull requests in a repository.
---

# GitHub - Search issues and pull requests (batch) action

The **Search issues and pull requests** batch action searches for issues or pull requests (PRs) in a repository.

## Input

| Input field | Description |
| --- | --- |
| Organization | Select from the drop-down menu or manually enter the organization name. You can find the organization name in your GitHub URL. For example, `https://github.com/organization/repo_name/`. |
| Repository name | Enter the repository name you plan to monitor for new issues or PRs. |
| Type | Select or manually enter the type associated with the issue or PR you plan to search for. |
| Assignee username | Enter the GitHub username of the assignee. |
| Status | Select or manually enter the status associated with the issue or PR you plan to search for. |
| Closed after | Select a date to return items closed after that date. |
| Label | Enter labels to filter results. For multi-word labels, use quotes. Separate multiple labels with commas. |

## Output

| Output field | Description |
| --- | --- |
| Total count | The total number of issues or PRs that meet the search criteria. |
| Issues | Information about the issues that meet the search criteria. |

---
