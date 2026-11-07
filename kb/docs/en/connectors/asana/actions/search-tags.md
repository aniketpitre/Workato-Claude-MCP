---
url: 'https://docs.workato.com/en/connectors/asana/actions/search-tags.md'
description: The Search tags batch action searches tags in Asana.
---

# Asana - Search tags action (batch)

The **Search tags** batch action searches tags in Asana. You can specify the workspace ID to retrieve tags from only one workspace.

## Input

| Input field | Description |
| --- | --- |
| Workspace ID | Enter the workspace ID. |
| Team ID | Enter the team ID. You can find this value in the URL of a team conversation. |

## Output

| Output field | Description |
| --- | --- |
| Tags | Array of tags belonging to the workspace (if you specify the workspace ID) or the organization. |
| ID (Tags) | The unique identifier of each tag. |
| Name (Tags) | The name of each tag. |

---
