---
url: 'https://docs.workato.com/en/connectors/youtube/create-playlist-action.md'
description: >-
  The Create playlist action creates a new playlist on the connected channel in
  YouTube.
---

# YouTube - Create playlist action

The **Create playlist** action creates a new playlist on the connected channel in YouTube.

> **PREREQUISITES**
> 
> This action requires OAuth 2.0 authentication. API key authentication isn't supported for actions that modify data. Your OAuth connection must include a scope that grants write access, such as **Manage YouTube account**, **Force SSL (secure access)**, or **YouTube Partner access**. The Google account associated with the connection must also have an existing YouTube channel.

## Input

| Field | Description |
| --- | --- |
| Title | Enter the title of the new playlist. |
| Description | Enter the description of the new playlist. |
| Privacy status | Select the playlist visibility. Allowed values are `public`, `private`, and `unlisted`. Defaults to `public` if left blank. |

## Output

| Field | Description |
| --- | --- |
| Kind | The API resource type, for example `youtube#playlist`. |
| Etag | The ETag of the resource. |
| Playlist ID | The ID of the created playlist. |
| Snippet | Details about the playlist, such as its `Title`, `Description`, `Published at` date, `Channel ID`, `Channel title`, and `Thumbnails`. |
| Content details | The playlist `Item count`. |
| Status | The playlist `Privacy status`. |

> **PLAYLIST CREATION LIMIT**
> 
> YouTube enforces a separate rate limit on how many playlists a channel can create in a given period, independent of your project’s general API quota. If you exceed the playlist creation limit, YouTube returns an error with the reason `RATE_LIMIT_EXCEEDED`.

---

---
url: >-
  https://docs.workato.com/en/connectors/youtube/download-caption-track-action.md
description: >-
  The Download caption track action retrieves the transcript content for a
  caption track you specify in YouTube.
---

# YouTube - Download caption track action

The **Download caption track** action retrieves the transcript content for a caption track you specify in YouTube.

> **PREREQUISITES**
> 
> This action requires OAuth 2.0 authentication with a scope that includes **Force SSL (secure access)** (`youtube.force-ssl`). You can download caption tracks for videos that the connected account owns or third-party-contributed caption tracks that the video owner has enabled for download.

## Input

| Field | Description |
| --- | --- |
| Caption ID | Enter the ID of the caption track to download. Use the **List records** action with the **Caption tracks** object to obtain the caption track ID. |
| Format | Select the caption file format. Allowed values are `srt`, `sbv`, or `vtt`. Defaults to the caption track's native format if left blank. |

## Output

| Field | Description |
| --- | --- |
| Caption ID | The ID of the downloaded caption track. |
| Format | The format of the returned caption content. |
| Content | The raw text content of the caption track. |

---
