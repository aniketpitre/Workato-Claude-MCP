---
url: 'https://docs.workato.com/en/connectors/youtube/get-record-action.md'
description: >-
  The Get record action retrieves details for a video or channel you specify in
  YouTube.
---

# YouTube - Get record action

The **Get record** action retrieves details for a video or channel you specify in YouTube.

## Input

| Field | Description |
| --- | --- |
| Object type | Select the type of record to retrieve. Options are **Video details** and **Channel info**. |
| Video ID | Enter the video ID, for example `dQw4w9WgXcQ`. This field is required when **Object type** is **Video details**. |
| Channel ID | Enter the channel ID, for example `UCxxxxxx`. This field is required when **Object type** is **Channel info**. |

## Output

Output fields are dynamically generated based on the object you select. The following fields are common to all object types:

| Field | Description |
| --- | --- |
| Kind | The API resource type, for example `youtube#video` or `youtube#channel`. |
| Etag | The ETag of the resource. |
| Snippet | Contains details about the video or channel, such as `Title` and `Description`. |
| Content details | Contains details specific to the object you select. |
| Statistics | Contains statistics such as `View count`. |

---
