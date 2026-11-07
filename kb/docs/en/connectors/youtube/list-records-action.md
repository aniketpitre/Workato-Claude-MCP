---
url: 'https://docs.workato.com/en/connectors/youtube/list-records-action.md'
description: >-
  The List records action lists videos, playlist items, comment threads,
  replies, caption tracks, or playlists in YouTube.
---

# YouTube - List records action

The **List records** action lists videos, playlist items, comment threads, replies, caption tracks, or playlists in YouTube.

## Input

| Field | Description |
| --- | --- |
| Object type | Select the type of records to list. Options are **Channel videos**, **Playlist items**, **Comment threads**, **Thread replies**, **Caption tracks**, and **Playlists**. |
| Channel ID | Enter the ID of the channel. Required when **Object type** is **Channel videos** or **Playlists**. |
| Playlist ID | Enter the ID of the playlist. Required when **Object type** is **Playlist items**. |
| Video ID | Enter the ID of the video. Required when **Object type** is **Comment threads** or **Caption tracks**. |
| Comment thread ID | Enter the ID of the comment thread to retrieve replies for. Required when **Object type** is **Thread replies**. |
| Order | Select the sort order for comment threads. Options are `time` (chronological) or `relevance`. Defaults to `time` if left blank. This field is only available when **Object type** is **Comment threads**. |
| Max results | Enter the maximum number of results to return. Valid values are 1-50. Default is 25. Not available when **Object type** is **Caption tracks**. |
| Page token | Enter the token for retrieving a specific page of results. This field isn't available when **Object type** is **Caption tracks**. |

## Output

Output fields are dynamically generated based on the object you select. The following fields are common to all object types:

| Field | Description |
| --- | --- |
| Kind | The API resource type of the object, for example `youtube#playlistItemListResponse`. |
| Etag | The ETag of the object. |
| Items | An array of search results for the object. |

---
