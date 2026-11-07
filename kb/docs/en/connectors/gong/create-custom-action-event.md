---
url: 'https://docs.workato.com/en/connectors/gong/create-custom-action-event.md'
description: >-
  The Create custom action event action in the Gong connector pushes engagement
  events tied to a deal onto the deal's event timeline.
---

# Gong - Create custom action event action

Pushes engagement events into Gong which are tied to deals. This action allows you to tie any events to a deal's event timeline.

## Input

| Field | Description |
| --- | --- |
| Content ID | The ID of the content on which the custom action took place in the reporting system. |
| Content title | The name of the object upon which a custom action was performed. |
| Content URL | The url of the content upon which a custom action was performed. |
| Event timestamp | The date and time when the event happened in the ISO-8601 format (e.g., 2021-08-01T02:30:00+05:00 or 2021-08-01T08:00:00Z, where Z stands for UTC) |
| Reporting system | The unique identifier of the reporting system. It is the same value in all events originating from the same system. |
| Action name | The name of the action. For example, Document Viewed or Presentation Opened. |
| Actor | List of objects with name and email of viewer. |
| Agent platform | Select platform on which the interaction was made. eg. Mac. |
| Event info URL | The link to a page that presents additional information about this event. |
| User agent | 'User-Agent' header value for browser based interaction. |
| Content properties | Dynamic properties to display for the object fields and values that describe the object. |
| Crm context | A list of references to external systems such as CRM, Telephony System, Case Management, etc. |
| Event ID | Object ID. The original ID of the event as designated in the reporting system. |
| Event properties | Dynamic properties to display for the event fields and values that describe the event. |
| Mobile app ID | The application identification string in case of interaction via mobile application (bundle identifier or package name). |
| Workspace ID | If your Gong account has multiple Workspaces, enter here the relevant Workspace to send these events to. If left blank, this will be decided by Gong. |

## Output

| Field | Description |
| --- | --- |
| Request ID | UUID of the request sent to Gong to create the content view engagement event. |

---
