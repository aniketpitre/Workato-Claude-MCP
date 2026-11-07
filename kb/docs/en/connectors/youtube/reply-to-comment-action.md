---
url: 'https://docs.workato.com/en/connectors/youtube/reply-to-comment-action.md'
description: >-
  The Reply to comment action posts a reply to an existing comment thread on a
  video in YouTube.
---

# YouTube - Reply to comment action

The **Reply to comment** action posts a reply to an existing comment thread on a video in YouTube.

> **PREREQUISITES**
> 
> This action requires OAuth 2.0 authentication with a scope that includes **Force SSL (secure access)** (`youtube.force-ssl`).

## Input

| Field | Description |
| --- | --- |
| Parent comment ID | Enter the ID of the comment thread to reply to. |
| Reply text | Enter the text content of the reply. |

## Output

| Field | Description |
| --- | --- |
| Kind | The API resource type, for example `youtube#comment`. |
| Etag | The ETag of the resource. |
| Comment ID | The ID of the new reply. |
| Snippet | Contains details about the reply, such as its `Text display`, `Text original`, `Parent ID`, `Channel ID`, `Video ID`, `Author display name`, `Author channel URL`, `Like count`, `Published at` date, and `Updated at` date. |

---
