---
url: 'https://docs.workato.com/en/connectors/gong/add-call.md'
description: >-
  The Add call action in the Gong connector lets you add a call by supplying a
  media download URL or uploading media with the Add call media action.
---

# Gong - Add call action

This action will add call in Gong. To add a call, you will either need to provide a media download URL which Gong can download the file from or use the **Add call media** action after this to upload call media. Audio or video file in the media download URL must be a maximum of **1.5 GB**.

## Input

The set of input fields is as below.

| Field | Description |
| --- | --- |
| Client unique ID | A call's unique identifier in the PBX or the recording system. Gong uses this identifier to prevent repeated attempts to upload the same recording. |
| Actual start | The date and time the call actually started. |
| Primary user | The Gong internal user ID of the team member who hosted the call. |
| Parties | A list of the call's participants. A party must be provided for the primaryUser. |
| Direction | Whether the call is inbound (someone called the company), outbound (a rep dialed someone outside the company), or a conference call. |
| Workspace | Select the workspace to add the call to. |
| Meeting URL | The URL of the conference call by which users join the meeting. |
| Title | The title of the call. This title is available in the Gong system for indexing and search. |
| Purpose | The purpose of the call. This optional field is a free text of up to 255 characters. |
| Scheduled start | The date and time the call was scheduled to begin. |
| Scheduled end | The date and time the call was scheduled to end. |
| Duration | The actual call duration in seconds. |
| Disposition | The disposition of the call. The disposition is free text of up to 255 characters. |
| Media download URL | The URL from which Gong can download the media file. The URL must be unique, the audio or video file must be a maximum of 1.5GB. You can either provide a friendly URL or add call media directly using the add call media action. |
| Context | A list of links to external systems such as CRM, Telephony System, Case Management, etc. |
| Speakers timeline | Describe the segments of time where individual parties were speaking. |
| Custom data | Optional metadata associated with the call (represented as text). Gong stores this metadata and it can be used for troubleshooting. |

## Output

| Field | Description |
| --- | --- |
| Call ID | Unique ID of the Call added to Gong |
| Request ID | UUID that is created to ensure the call is created only once. |

---
