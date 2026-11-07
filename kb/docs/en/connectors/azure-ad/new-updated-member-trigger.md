---
url: 'https://docs.workato.com/en/connectors/azure-ad/new-updated-member-trigger.md'
description: >-
  The New/updated member (real-time) trigger monitors Microsoft Entra ID for new
  or updated members.
---

# Microsoft Entra ID - New/updated member (real-time) trigger

The **New/updated member (real-time)** triggers immediately when a member is added, updated, or removed from a group in Microsoft Entra ID for new or updated members.

> **WEBHOOK ACCESSIBILITY**
> 
> Your webhook endpoint must be publicly accessible by HTTPS and respond within 3 seconds.

## Input

| Input field | Description |
| --- | --- |
| Group | Select the group to monitor for new or updated members. |

## Output

| Output field | Description |
| --- | --- |
| Notification ID | The ID of the new/updated member notification. |
| Change type | The type of change. |
| Client state | The client state of the new/updated event. |
| Subscription ID | The subscription ID for the new/updated member. |
| Resource | The resource, such as an app, that the new/updated member uses. |
| Resource data | Details about the resource data, including ID and OData type. |
| Member | Information about the member that is new/updated. |
| Group ID | The ID of the group being monitored for new/updated members. |
| Subscription expiration date time | The date and time that the subscription expires. |
| Tenant ID | The ID of the tenant associated with the new/updated member. |

---
