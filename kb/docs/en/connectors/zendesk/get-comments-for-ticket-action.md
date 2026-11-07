---
url: >-
  https://docs.workato.com/en/connectors/zendesk/get-comments-for-ticket-action.md
description: >-
  The Get comments for ticket action in the Zendesk connector lets you retrieve
  the comments on a specific ticket found by ticket ID.
---

# Zendesk - Get comments for ticket action (batch)

This action retrieves a specific ticket that matches a search by ticket ID. Only results in your Zendesk instance that match the criteria are returned.

![Get comments for ticket action](/assets/get-comments-ticket.0iLKCzVR.png)_Get comments for ticket action_

## Input

| Input field | Description |
| --- | --- |
| ID | The unique Zendesk ID of the ticket. |

## Output

The output of this action contains the full list of comments for this ticket, including the **description** (which is saved as the first comment of a ticket).

| Output field | Description |
| --- | --- |
| Ticket ID | The unique Zendesk ID of the ticket. This is automatically assigned when the ticket is created. |
| Type | The type of the ticket comment. Permitted values are `comment`, `incident`, or `VoiceComment`. |
| Body | The comment made by the author. |
| HTML body | The comment made by the author formatted in HTML. |
| Public | Is `True` if this comment is public, otherwise it will display `False`. |
| Date created | The time this comment was created. |
| Author ID | The unique Zendesk ID of the author of the comment. |
| Attachments | The attachments on this comment. |
| List size | The size of the list, corresponding to the number of comments retrieved. |
