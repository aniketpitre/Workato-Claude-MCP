---
url: 'https://docs.workato.com/en/connectors/gong/add-call-media.md'
description: >-
  The Add call media action in the Gong connector uploads a media file of up to
  60 MB to a call you previously added with the Add call action.
---

# Gong - Add call media action

This action will add call media in Gong. To upload call media, you will first need to add the call and its details via the **Add call** action.  
  
If uploading a dual-channel (stereo) file separated by speaker, make sure to specify which channel corresponds to the company team member (rep) in the parties input fields of the **Add call** action.  
  
This endpoint supports files up to a maximum of 60 MB. To upload files up to 1.5 GB, provide the media download URL directly in the **Add call** action. The media download URL can be created from videos stored in any of our cloud storage systems like S3.

## Input

| Field | Description |
| --- | --- |
| Call ID | The call ID returned from the Add call action. |
| Media file | Contents of the file. |

## Output

| Field | Description |
| --- | --- |
| Call ID | Unique ID of the call added to Gong |
| Request ID | UUID that is created to ensure the call is created only once. |
| URL | URL of the call |

---

---
url: >-
  https://docs.workato.com/en/connectors/gong/create-content-share-engagement-event.md
description: >-
  The Create content share engagement event action in the Gong connector pushes
  events into Gong when a user shares content with external participants.
---

# Gong - Create content share engagement event action

This action pushes engagement events into Gong when a Gong user shares content with external participants. For example, when a contract was shared by an account executive with their prospects.

## Input

| Field | Description |
| --- | --- |
| Content ID | The ID of the content that was shared in the reporting system. |
| Content title | The name of the object that was shared. |
| Content URL | The url of the content that was shared in the reporting system. This is the url that is was accessed by the viewer. |
| Event timestamp | The date and time when the event happened in the ISO-8601 format (e.g., 2021-08-01T02:30:00+05:00 or 2021-08-01T08:00:00Z, where Z stands for UTC) |
| Reporting system | The unique identifier of the reporting system. It is the same value in all events originating from the same system. |
| Action name | The name of the action. For example, Shared the contract or Downloaded the presentation. |
| Recipients | Array of objects with name and email of recipients. Email is required |
| Share ID | The ID of the share action, in case there can be more than one share per content. |
| Share info URL | The link to a page that presents additional information about this event. |
| Sharer | Additional details about the sharer like email, name, and Gong ID. |
| Sharing message body | The share message body. Can contain HTML and will be cleaned when it is presented. |
| Sharing message subject | The subject of share email / message. |
| Content properties | Dynamic properties to display for the object fields and values that describe the object. |
| Crm context | A list of references to external systems such as CRM, Telephony System, Case Management, etc. |
| Event ID | Object ID. The original ID of the event as designated in the reporting system. |
| Event properties | Dynamic properties to display for the event fields and values that describe the event. |
| Mobile app ID | The application identification string in case of interaction via mobile application (bundle identifier or package name). |
| Workspace ID | If your Gong account has multiple Workspaces, enter here the relevant Workspace to send these events to. If left blank, this will be decided by Gong. |

## Output

| Field | Description |
| --- | --- |
| Request ID | UUID of the request sent to Gong to create the content share engagement event. |

---
