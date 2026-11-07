---
url: 'https://docs.workato.com/en/connectors/youtube/add-to-playlist-action.md'
description: >-
  The Add to playlist action adds a video to a playlist on the connected channel
  in YouTube.
---

# YouTube - Add to playlist action

The **Add to playlist** action adds a video to a playlist on the connected channel in YouTube.

> **PREREQUISITES**
> 
> This action requires OAuth 2.0 authentication. API key authentication isn't supported for actions that modify data. Your OAuth connection needs a scope that grants write access, such as **Manage YouTube account**, **Force SSL (secure access)**, or **YouTube Partner access**.

## Input

| Field | Description |
| --- | --- |
| Playlist ID | Enter the ID of the playlist to which you plan to add the video. |
| Video ID | Enter the video ID to add to the playlist. |

## Output

| Field | Description |
| --- | --- |
| Kind | The API resource type, for example `youtube#playlistItem`. |
| Etag | The ETag of the resource. |
| Playlist item ID | The ID of the new playlist item. |
| Snippet | Details about the added item, such as `Title`, `Description`, `Published at` date, `Channel ID`, `Playlist ID`, `Position` in the playlist, and `Resource ID` (the underlying video's `Video ID`). |
| Content details | The added video's `Video ID` and `Video published at` date. |

---
