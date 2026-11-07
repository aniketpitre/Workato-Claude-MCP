---
url: 'https://docs.workato.com/en/connectors/teams/get-team-action.md'
description: The Get team action gets details of a specified team in Microsoft Teams.
---

# Microsoft Teams - Get team action

The **Get team** action gets full details for a team in Microsoft Teams.

## Input

| Input field | Description |
| --- | --- |
| Team name (or team ID) | Enter the team name or ID. Only teams you're a member of are options. You can retrieve the team ID from the **List teams** action output. |

## Output

| Output field | Description |
| --- | --- |
| @odata.context | The metadata URL property in the OData JSON response. It describes the structure, type, and location of the returned data. |
| Team ID | The team unique identifier. |
| Created date | The date the team was created. |
| Display name | The team name. |
| Description | The team description. |
| Internal ID | The Office 365 Group unique identifier (a GUID). Backend actions, such as those using the Microsoft Graph API, require this unique identifier. |
| Web URL | The direct link to the team. |
| Is archived | A boolean response (`true` or `false`) that indicates if the team is archived. |
| Is membership limited to owners | A boolean response (`true` or `false`) that indicates if the team membership is restricted to team owners. |

---
