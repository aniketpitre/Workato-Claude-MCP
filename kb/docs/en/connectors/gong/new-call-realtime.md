---
url: 'https://docs.workato.com/en/connectors/gong/new-call-realtime.md'
description: >-
  The New call trigger in the Gong connector fires in real time when a new call
  matches the automation rule you set up in Gong.
---

# Gong - New call trigger (real-time)

The **New call** trigger monitors Gong for new calls in real-time. You must [create an automation rule](https://help.gong.io/hc/en-us/articles/360041630212-Create-a-webhook-rule) in Gong to use this trigger. You can assign filters to this rule to only pick up calls that match the criteria you specify.

## Input

| Field | Description |
| --- | --- |
| Event name **Required** | Provide a unique event name to generate endpoint URL. |

## Output

Call specific output fields will be dynamically rendered base on the calls you select. A sample response structure is below.

| Field | Description |
| --- | --- |
| Collaboration | An object containing a list of public comments. Each public comment contains details like audio start time, audio end time, comment user ID, and the comment text, among other fields. |
| Content | An object with the information pertaining to structure, topic, trackers, and points of interest. |
| Context | List of objects that contains the relevant fields, object ID, object type, as well as source system details. |
| Interaction | An object with the information pertaining to interaction stats, questions, speakers, and video. |
| Media | An object containing the video and audio URL of the call, as applicable. |
| Metadata | Contains all the metadata of the call including title, duration, workspace, etc. |
| Parties | List of parties that were involved in the call. Each party object contains details like name, email address, affiliation, etc. |

---
