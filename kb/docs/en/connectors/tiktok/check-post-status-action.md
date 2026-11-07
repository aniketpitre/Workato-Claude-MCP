---
url: 'https://docs.workato.com/en/connectors/tiktok/check-post-status-action.md'
description: >-
  Check the publish status of a TikTok post by publish ID, with optional polling
  until the post completes or fails.
---

# TikTok - Check post status action

The **Check post status** action checks a post's publish status by publish ID in TikTok.

> **POLL UNTIL THE POST REACHES A FINAL STATUS**
> 
> Set **Wait** to **Yes** to poll every 15 seconds until the post's status reaches `PUBLISH_COMPLETE`, `SEND_TO_USER_INBOX`, or `FAILED`. The action polls for a maximum of 10 minutes, then fails with a timeout error.

## Input

| Input field | Description |
| --- | --- |
| Publish ID | Enter the publish ID returned by the action that created the post. |
| Wait | Optional. Select **Yes** to poll until the post finishes publishing, is sent to the inbox, or fails. Defaults to **No** if left blank. |

## Output

| Output field | Description |
| --- | --- |
| Status | The post's publish status, for example `PUBLISH_COMPLETE`. |
| Fail reason | The reason the post failed to publish. Empty if the post didn't fail. |
| Publicly available post IDs | The IDs of the posts that are publicly available on TikTok. |
| Uploaded bytes | The number of bytes uploaded to TikTok. |
| Downloaded bytes | The number of bytes TikTok downloaded from your source URL. |

---
