---
url: 'https://docs.workato.com/en/connectors/youtube/remove-from-playlist-action.md'
description: >-
  The Remove from playlist action removes an item from a playlist on the
  connected channel in YouTube.
---

# YouTube - Remove from playlist action

The **Remove from playlist** action removes an item from a playlist on the connected channel in YouTube.

> **PREREQUISITES**
> 
> This action requires OAuth 2.0 authentication. API key authentication isn't supported for actions that modify data. Your OAuth connection needs a scope that grants write access, such as **Manage YouTube account**, **Force SSL (secure access)**, or **YouTube Partner access**.

## Input

| Field | Description |
| --- | --- |
| Playlist item ID | Enter the playlist item ID to remove. Use the **List records** action with the **Playlist items** object to obtain the `id` for each returned item. |

## Output

| Field | Description |
| --- | --- |
| Success | Indicates whether the playlist item was removed. |
| Playlist item ID | The ID of the removed playlist item. |

---
