---
url: 'https://docs.workato.com/en/connectors/youtube/update-record-action.md'
description: >-
  The Update record action updates an existing playlist or a video's metadata on
  the connected channel in YouTube.
---

# YouTube - Update record action

The **Update record** action updates the metadata of an existing playlist or video on the connected channel in YouTube.

> **PREREQUISITES**
> 
> This action requires OAuth 2.0 authentication. API key authentication isn't supported for actions that modify data. Your OAuth connection needs a scope that grants write access, such as **Manage YouTube account**, **Force SSL (secure access)**, or **YouTube Partner access**.

## Input

| Field | Description |
| --- | --- |
| Object type | Select the type of YouTube record to update. Options are **Playlist** or **Video metadata**. |
| Playlist ID | Enter the ID of the playlist to update. This field is required when **Object type** is **Playlist**. |
| Video ID | Enter the ID of the video to update. This field is required when **Object type** is **Video metadata**. |
| Title | Enter the new title. Workato preserves the existing value if you leave this field blank. |
| Description | Enter the new description. Workato preserves the existing value if you leave this field blank. |
| Tags | Enter the new list of tags. Replaces existing tags. Workato preserves the existing tags if you leave this field blank. Only available when **Object type** is **Video metadata**. |

> **PLAYLIST UPDATES**
> 
> Provide a value for at least one of **Title** or **Description** when **Object type** is **Playlist**. YouTube rejects the request if you leave both fields blank.

## Output

Output fields are dynamically generated based on the object you select. The following fields are common to all object types:

| Field | Description |
| --- | --- |
| Kind | The API resource type, for example `youtube#playlist`. |
| Etag | The ETag of the resource. |
| Snippet | Contains details about the resource, such as `Title`, `Description`, `Published at` date, `Channel ID`, `Channel title`, and `Thumbnails`. |

---
