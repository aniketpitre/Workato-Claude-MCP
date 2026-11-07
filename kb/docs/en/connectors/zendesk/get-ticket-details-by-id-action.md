---
url: >-
  https://docs.workato.com/en/connectors/zendesk/get-ticket-details-by-id-action.md
description: >-
  The Get ticket details by ID action in the Zendesk connector lets you retrieve
  a specific ticket that matches a search by ticket ID.
---

# Zendesk - Get ticket details by ID action

This action retrieves a specific ticket that matches a search by ticket ID. Only records in your Zendesk instance that matches the criteria will be returned.

![Get ticket details by ID action](/assets/get-ticket-details-by-id.Cg6bBfwr.png)_Get ticket details by ID action_

## Input

| Input field | Description |
| --- | --- |
| Ticket ID | The unique Zendesk ID of the ticket. |

## Output

The output of this action contains the full set of columns from the selected ticket. Here are some commonly used outputs.

| Output field | Description |
| --- | --- |
| Ticket ID | The unique Zendesk ID of the ticket. This is automatically assigned when the ticket is created. |
| Subject | The subject of the ticket. |
| Type | The type of ticket. Permitted values are `problem`, `incident`, `question`, or `task`. |
| Priority | The priority of the ticket. Permitted values are `urgent`, `high`, `normal`, or `low`. |
| Ticket custom fields | Includes data of ticket custom fields. |

Click here for a full list of [ticket outputs](/en/connectors/zendesk/ticket-fields#ticket-output-fields).
