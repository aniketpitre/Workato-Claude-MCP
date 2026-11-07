---
url: 'https://docs.workato.com/en/accelerator-approval-bot-start.md'
description: >-
  Start the recipes in the Approval bot accelerator in the correct order for
  Slack or Microsoft Teams implementations.
---

# Start the recipes

You must start the recipes in the **Approval bot accelerator** in a specific order.

## Start the recipes for Microsoft Teams

If you implement the Approval bot in Microsoft Teams, you must start the recipes in this accelerator in the following order:

1. ABT | REC-001 | Requests from Source System
2. ABT | CALL-007 | Request to Microsoft Teams
3. ABT | REC-002 | Approve/Reject Request from Microsoft Teams
4. ABT | REC-003 | Approvals Home Tab
5. ABT | REC-004 | Sub Menu items
6. ABT | REC-005 | Show requests
7. ABT | REC-006 | Pending Requests Reminders

## Start the recipes for Slack

If you implement the Approval bot in Slack, you must start the recipes in this accelerator in the following order:

1. ABS | REC-001 | Slack Request Parent Recipe
2. ABS | CALL-002 | Request to Slack
3. ABS | REC-003 | Approve/Reject Request from Slack
4. ABS | REC-004 | Slack Homepage Event
5. ABS | REC-005 | Pending Approval Summary
6. ABS | CALL-006 | Slack Update Homepage

---
