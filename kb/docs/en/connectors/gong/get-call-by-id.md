---
url: 'https://docs.workato.com/en/connectors/gong/get-call-by-id.md'
description: >-
  The Get call by ID action in the Gong connector retrieves data for a specific
  call using its unique Gong ID.
---

# Gong - Get call by ID action

This action will get call by id in gong.io. Retrieves data for a specific call by Gong's unique ID.

## Input

| Field | Description |
| --- | --- |
| Call ID | Call ID to retrieve. ID can be found at the end of the URL. |

## Output

Object specific output fields will be dynamically rendered base on the objects you select. A possible set of output fields is as below.

| Field | Description |
| --- | --- |
| ID | ID of the call requested. |
| URL | Gong link to access the call. |
| Title | The title of the call in the Gong system. |
| Scheduled start | The date and time the call was scheduled to start. |
| Started | The date and time the call actually started. |
| Duration | The actual call duration in seconds. |
| Primary user | The Gong internal user ID of the team member who hosted the call. |
| Workspace ID | ID of the Workspace the call resides in. |
| Direction | Whether the call is inbound (someone called the company), outbound (a rep dialed someone outside the company), or a conference call. |
| Disposition | The disposition of the call. The disposition is free text of up to 255 characters. |
| Custom data | Optional metadata associated with the call (represented as text). |

---
