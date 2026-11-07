---
url: 'https://docs.workato.com/en/connectors/asana/actions/search-projects.md'
description: The Search projects batch action searches projects in Asana.
---

# Asana - Search projects action (batch)

The **Search projects** batch action searches projects in Asana. You can specify the workspace ID to retrieve projects from only one workspace.

## Input

| Input field | Description |
| --- | --- |
| Workspace ID | Enter the workspace ID. |
| Team ID | Enter the team ID. You can find this value in the URL of a team conversation. |
| Archived | Specify whether you are searching for an archived project. |

## Output

| Output field | Description |
| --- | --- |
| Projects | Array of projects belonging to the workspace (if you specify the workspace ID) or the organization. |
| ID (Projects) | The unique identifier of each project. |
| Name (Projects) | The name of each project. |

---
