---
url: 'https://docs.workato.com/en/accelerator-approval-bot-recipes.md'
description: >-
  Reference for the recipes in the Approval bot accelerator that route approval
  requests through Slack and Microsoft Teams.
---

# Recipes for the Approval bot accelerator

This accelerator contains a set of recipes to implement the Approval bot in Slack and a separate set of recipes to implement the Approval bot in Microsoft Teams.

- [Recipes for Slack](#slack-recipes) (located in approval-bot-slack.zip)
- [Recipes for Microsoft Teams](#teams-recipes) (located in approval-bot-msteams.zip)

## Recipes for Slack

<dl><dt>ABS | REC-001 | Slack Request Parent Recipe</dt><dd>This recipe triggers from a new/updated row in Google Sheets and calls the <strong>ABS | CALL-002 | Request to Slack</strong> recipe.</dd><dt>ABS | CALL-002 | Request to Slack</dt><dd>Sends the approval request to Slack.</dd><dt>ABS | REC-003 | Approve/Reject Request from Slack</dt><dd>After a request is approved or denied, this recipe updates the result and prompts the Slack workbot to post a message in Slack.</dd><dt>ABS | REC-004 | Slack homepage Event</dt><dd>This recipe calls the <strong>ABS | CALL-006 | Slack Update Homepage</strong> recipe.</dd><dt>ABS | REC-005 | Pending Approval Summary</dt><dd>Send reminders to the approvers you designate.</dd><dt>ABS | CALL-006 | Slack Update Homepage</dt><dd>Updates the dashboard overview with approval request outcomes.</dd></dl>

## Recipes for Microsoft Teams

<dl><dt>ABT | REC-001 | Requests from Source System</dt><dd>This recipe triggers from a new/updated row in Google Sheets and calls the <strong>ABT | REC-002 | Approve/Reject Request from Microsoft Teams</strong> recipe.</dd><dt>ABT | REC-002 | Approve/Reject Request from Microsoft Teams</dt><dd>ends the approval request to Microsoft Teams.</dd><dt>ABT | REC - 003 | Approvals Home Tab</dt><dd>Searches for new approval requests and posts updates as workbot in Microsoft Teams.</dd><dt>ABT | REC - 004 | Sub Menu items</dt><dd>Updates <strong>Approval Bot- Microsoft Teams</strong> lookup table.</dd><dt>ABT | REC - 005 | Show requests</dt><dd>Posts requests to Microsoft Teams as workbot.</dd><dt>ABT | REC-006 | Pending Requests Reminders</dt><dd>Send reminders to the approvers you designate.</dd><dt>ABT | CALL-007 | Request to Microsoft Teams</dt><dd>Updates Microsoft Teams with approval request outcomes.</dd></dl>

---
