---
url: 'https://docs.workato.com/en/connectors/zendesk/search-tickets-action.md'
description: >-
  The Search tickets action in the Zendesk connector lets you retrieve a list of
  all tickets that match your search criteria.
---

# Zendesk - Search tickets action (batch)

This action retrieves a list of all tickets that matches your search criteria. Only records in your Zendesk instance that matches all the criteria will be returned.

![Search tickets action](/assets/search-ticket-action.DyO532j0.png)_Search tickets action_

## Input

| Input field | Description |
| --- | --- |
| Status | The status of the ticket. Permitted values are `>open`, `pending`, `hold`, `solved`, or `closed`. |
| Type | The type of the ticket. Permitted values are `problem`, `incident`, `question`, or `task`. |
| Priority | The priority of the ticket. Permitted values are `urgent`, `high`, `normal`, or `low`. |
| Subject | The subject of the ticket. |
| Description | The description of the ticket. |
| Earliest created time | The earliest the ticket was created. |
| Latest modified time | The latest the ticket was updated. |
| Requester | The requester of the ticket. You can define users with the full name, user ID, email, or phone number. You can also use 'none' and 'me'. |
| Submitter | The submitter of the ticket. You can define users with the full name, user ID, email, or phone number. You can also use 'none' and 'me'. |
| Organization | The organization of the requester. You can define the organization with the name or organization ID. You can also use 'none' and 'me'. |
| Tags | The tags applied to this ticket. You can query multiple tags with the `,` separator. |
| Channels | Information about how the ticket was created. Some possible values are "_web_", "_mobile_", "_API_" etc. |

Click here a full list of [ticket inputs](/en/connectors/zendesk/ticket-fields#ticket-input-fields).

## Output

The output of this action contains a list of tickets with their respective outputs. Here are some commonly used outputs.

| Output field | Description |
| --- | --- |
| Ticket ID | The unique Zendesk ID of the ticket. This is automatically assigned when the ticket is created. |
| Subject | The subject of the ticket. |
| Type | The type of the ticket. Permitted values are `problem`, `incident`, `question`, or `task`. |
| Priority | The priority of the ticket. Permitted values are `urgent`, `high`, `normal`, or `low`. |
| Ticket custom fields | Includes data of ticket custom fields. |
| List size | The size of the list, corresponding to the number of tickets retrieved. |

Click here for a full list of [ticket outputs](/en/connectors/zendesk/ticket-fields#ticket-output-fields).

---
