---
url: 'https://docs.workato.com/en/features/activity-audit-log.md'
description: >-
  Learn how Workato activity audit logs let administrators track user logins,
  recipe changes, and other account activity over time.
---

# Activity audit log

Administration and user management are must-haves for any integration project, big or small. As team size and complexity grows around your projects, control and activity visibility within your Workato workspace becomes critical.

With **Activity audit logs**, you can view changes made by users in your account over time.

> **FEATURE AVAILABILITY**
> 
> The activity audit log is included in specific pricing plans. Refer to your pricing plan and contract to learn more.

* * *

## Basics

- [What is the activity audit log?](#explanation)
- [How can I use activity audit logs?](#how-to-use)
- [How do I get the activity audit log feature?](#how-to-get)
- [How are AIRO-driven changes attributed?](#airo-attribution)
- [How long are logs retained?](#log-retention)
- [Who can view activity audit logs?](#view-logs)

### What is the activity audit log?

Activity audit logs provide a simple, powerful interface for Workato administrators to comprehensively track changes in their accounts. These changes include user activity such as logins and invitations, recipe modifications and events, and more.

### How can I use activity audit logs?

Using activity audit logs, you can quickly identify changes made in your account and analyze their impact.

For example: Imagine there was an unplanned stoppage of a business-critical recipe that onboards new employees. Using Activity audit logs, you can identify when the recipe was stopped and the user that stopped it.

### How do I get the activity audit log feature?

The Activity audit log feature is included with certain pricing plans. Refer to your pricing plan and contract to learn more.

### What activities are included?

Refer to the [Activity reference article](/en/features/activity-audit-log-reference) for a comprehensive list of activities included in the Activity audit log.

### How are AIRO-driven changes attributed?

The activity audit log attributes each action [AIRO](/en/airo) takes to a user account and adds a `(via AIRO)` label to the entry. This applies whether you interact with AIRO through the [Workato UI](/en/airo/chat) or the [AIRO MCP server](/en/airo/mcp). Actions from an AIRO MCP server API token connection are attributed to the workspace owner.

![Activity audit log entries for a recipe edit and create, both attributed to a user via AIRO.](/assets/airo-activity-audit-log.BmOOgr9Y.png)_Activity audit log entries attributed via AIRO_

### How long are logs retained?

**Default retention period:** The Workato platform automatically stores all Activity audit logs for **one year** from the event's date. This ensures you have ample time to review and analyze your activity logs for security and operational insights.

**Option to extend log availability:** You can leverage the [Audit log streaming](/en/features/activity-audit-log-streaming) feature to maintain access to your logs beyond the default retention period. This feature allows you to replicate and store log data at your chosen destination, ensuring long-term accessibility according to your organizational requirements.

### Who can view activity audit logs?

After you enable the Activity audit log feature, the following users can view the logs:

- The workspace owner (root login)
- Users with the **Admin** role
- Users with the **Activity audit** privilege

> **Further READING**
> 
> - [View activity audit logs](/en/features/activity-audit-log-view)
> - [Stream activity audit logs](/en/features/activity-audit-log-streaming)
> - [User activities included in logs](/en/features/activity-audit-log-reference)

---
