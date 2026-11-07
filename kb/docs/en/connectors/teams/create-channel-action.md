---
url: 'https://docs.workato.com/en/connectors/teams/create-channel-action.md'
description: The Create channel action creates a channel in a Microsoft Teams team.
---

# Microsoft Teams - Create channel action

The **Create channel** action creates a new channel in the specified Microsoft Teams team.

## Input

| Input field | Description |
| --- | --- |
| Team name (or team ID) | Enter the team name or ID. Only teams you're a member of are options. You can retrieve the team ID from the **List teams** action output. |
| Channel name | Enter the channel name. Must be unique within the team and no more than 50 characters. |
| Description | Optional. Enter a channel description. |
| Channel type | Enter the channel type. Available types include `standard`, `private`, and `shared`. |

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
| Web URL | The direct link to the channel. |
| Membership type | The channel membership type. Types include `standard`, `private`, and `shared`. |
| Layout type | The channel conversation format. Layout types include `post` and `chat`. |
| Is archived | A boolean response (`true` or `false`) that indicates if the channel is archived. |

---
