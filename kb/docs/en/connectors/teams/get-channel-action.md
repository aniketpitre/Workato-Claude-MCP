---
url: 'https://docs.workato.com/en/connectors/teams/get-channel-action.md'
description: The Get channel action gets details of a specified channel in Microsoft Teams.
---

# Microsoft Teams - Get channel action

The **Get channel** action gets details of a specified channel in Microsoft Teams.

## Input

| Input field | Description |
| --- | --- |
| Team name (or team ID) | Enter the team name or ID. Only teams you're a member of are options. You can retrieve the team ID from the **List teams** action output. |
| Channel ID | Enter the channel ID. |

## Output

| Output field | Description |
| --- | --- |
| @odata.context | The metadata URL property in the OData JSON response. It describes the structure, type, and location of the returned data. |
| Channel ID | The channel unique identifier. |
| Created date | The date the channel was created. |
| Display name | The channel name. |
| Description | The channel description. |
| Is favorite by default | A boolean response (`true` or `false`) that indicates if the channel was automatically marked as a favorite for team members. |
| Email | The channel email address. |
| Tenant ID | The channel tenant unique identifier. |
| Web URL | The direct link to the channel. |
| Membership type | The channel membership type. Types include `standard`, `private`, and `shared`. |
| Layout type | The channel conversation format. Layout types include `post` and `chat`. |
| Is archived | A boolean response (`true` or `false`) that indicates if the channel is archived. |

---
