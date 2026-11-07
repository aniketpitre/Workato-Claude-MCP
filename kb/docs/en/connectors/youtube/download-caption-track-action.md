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
