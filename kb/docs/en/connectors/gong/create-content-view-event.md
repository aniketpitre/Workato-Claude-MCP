---
url: 'https://docs.workato.com/en/connectors/gong/create-content-view-event.md'
description: >-
  The Create content view event action in the Gong connector pushes content view
  events to the Gong activity timeline when an external participant views
  content.
---

# Gong - Create content view event action

Pushes content view events into Gong and display them as events in Gong’s activity timeline, when a content is viewed by an external participants. For example, when a contract is viewed by a prospect.

## Input

| Field | Description |
| --- | --- |
| Content ID | The ID of the content that was viewed in the reporting system. |
| Content title | The name of the object that was viewed. |
| Content URL | The url of the content that was viewed in the reporting system. This is the url that is was accessed by the viewer. |
| Event timestamp | The date and time when the event happened in the ISO-8601 format (e.g., 2021-08-01T02:30:00+05:00 or 2021-08-01T08:00:00Z, where Z stands for UTC) |
| Reporting system | The unique identifier of the reporting system. It is the same value in all events originating from the same system. |
| Agent platform | Select platform on which the interaction was made. eg. Mac. |
| Share ID | The ID of the action, in case there can be more than one action per content. |
| User agent | 'User-Agent' header value for browser based interaction. |
| View action title | The name of the action. For example, Document Viewed or Presentation Opened. |
| View info URL | The link to a page that presents additional information about this event. |
| Viewer | Array of objects with name and email of viewer. |
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
