---
url: 'https://docs.workato.com/en/connectors/teams/search-messages-batch-action.md'
description: The Search messages batch action searches for messages in Microsoft Teams.
---

# Microsoft Teams - Search messages batch action

The **Search messages** batch action uses Microsoft Graph Search API to search across Microsoft Teams messages (channels and chats). This action requires authorization code grant authentication. It doesn't support client credentials authentication.

## Input

| Input field | Description |
| --- | --- |
| Search query | Enter the search query string. For example, `project update`. Supports Microsoft Search KQL syntax. |

## Output

| Output field | Description |
| --- | --- |
| Hit ID | The unique identifier for a specific message that matched your search criteria. |
| Rank | The relevance score of your search result, indicating how well a message matches your query. |
| Summary | The summary of the message body. |
| Message ID | The message unique identifier. |
| Created date | The date the message was created. |
| Last modified date | The date the message was last modified. |
| Subject | The message subject. |
| Importance | The priority level assigned to a message by the sender at the time of creation. Types include `normal` (default) and `high`. |
| Web link | A clickable URL that takes you directly to that message within Microsoft Teams. |
| From | The details of the message sender. Details include `Email address` and `Name`. |

---
