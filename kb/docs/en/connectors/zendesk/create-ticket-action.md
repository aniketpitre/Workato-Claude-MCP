---
url: 'https://docs.workato.com/en/connectors/zendesk/create-ticket-action.md'
description: >-
  The Create ticket action in the Zendesk connector creates a single new ticket
  record in your Zendesk instance, including standard and custom fields.
---

# Zendesk - Create ticket action

This action creates a single ticket in your Zendesk instance.

![Create ticket action](/assets/create-ticket-action.CClvKtSS.png)_Create ticket action_

## Input

Here are some commonly used inputs.

| Input field | Description |
| --- | --- |
| Ticket form | Select a ticket form to use preconfigured custom fields. |
| Comment | A description of the ticket. |
| Subject | The subject of the ticket. |
| Type | The type of ticket. Permitted values are `problem`, `incident`, `question`, or `task`. |
| Priority | The priority of the ticket. Permitted values are `urgent`, `high`, `normal`, or `low`. |
| Status | The status of the ticket. Permitted values are `>open`, `pending`, `hold`, `solved`, or `closed`. |
| Tags | The tags applied to this ticket. You can add multiple tags with the `,` separator. |
| Ticket custom fields | Provide data for ticket custom fields. |

Click here a full list of [ticket inputs](/en/connectors/zendesk/ticket-fields#ticket-input-fields).

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

---
