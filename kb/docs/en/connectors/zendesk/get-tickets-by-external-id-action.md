---
url: >-
  https://docs.workato.com/en/connectors/zendesk/get-tickets-by-external-id-action.md
description: >-
  The Get list of tickets by external IDs action in the Zendesk connector lets
  you retrieve tickets that match a search by external IDs.
---

# Zendesk - Get list of tickets by external IDs action (batch)

This action retrieves a list of tickets that matches a search by external IDs. Only records in your Zendesk instance that match all the criteria are returned.

![Get list of tickets by external IDs action](/assets/get-ticket-external-id.CttVhkKE.png)_Get list of tickets by external IDs action_

## Input

| Input field | Description |
| --- | --- |
| External ID | The external ID of the tickets. You can query multiple external IDs with the `,` separator. |

## Output

The output of this action contains the full set of columns from the list of tickets. Here are some commonly used outputs.

| Output field | Description |
| --- | --- |
| Ticket ID | The unique Zendesk ID of the ticket. This is automatically assigned when the ticket is created. |
| Subject | The subject of the ticket. |
| Type | The type of ticket. Permitted values are `problem`, `incident`, `question`, or `task`. |
| Priority | The priority of the ticket. Permitted values are `urgent`, `high`, `normal`, or `low`. |
| Ticket custom fields | Includes data of ticket custom fields. |
| List size | The size of the list, corresponding to the number of tickets retrieved. |

Click here for a full list of [ticket outputs](/en/connectors/zendesk/ticket-fields#ticket-output-fields).
