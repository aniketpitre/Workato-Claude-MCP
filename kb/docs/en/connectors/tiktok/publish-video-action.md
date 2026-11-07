---
url: 'https://docs.workato.com/en/connectors/tiktok/publish-video-action.md'
description: >-
  Publish a video to TikTok from a public URL or a file upload, as a direct post
  or a draft in the creator inbox.
---

# TikTok - Publish video action

The **Publish video** action publishes a video to TikTok. Select **Direct post** to publish immediately or **Upload to inbox** to send a draft to the creator inbox.

> **THE ACTION UPLOADS THE FILE FOR YOU**
> 
> Set **Source** to **File upload (stream)** to send a video file from your recipe. The action requests an upload URL from TikTok and streams the file to it in chunks, so you don't need a separate upload step.

## Input

The following are a representative set of input fields. Refer to the [TikTok API](https://developers.tiktok.com/doc/tiktok-api-v2-introduction) documentation for more information on available input fields.

| Input field | Description |
| --- | --- |
| Post mode | Select how to publish the video. Options are **Direct post** or **Upload to inbox**. |
| Source | Select where the video comes from. Options are **Pull from URL** or **File upload (stream)**. |
| Privacy level | Select who can see the video. The **Privacy level** field is required when **Post mode** is **Direct post**, and it must match one of the connected creator's privacy level options. Unaudited apps must use **Only me**. |
| Title | Optional. Enter the video's caption, up to 2200 UTF-16 runes. **Upload to inbox** doesn't accept a title. |
| Paid partnership | Optional. Select **Yes** to label the video as a paid partnership that promotes a third-party business. The **Paid partnership** field is only available when **Post mode** is **Direct post**. Defaults to **No** if left blank. |
| Brand organic | Optional. Select **Yes** to label the video as promoting the creator's own business. The **Brand organic** field is only available when **Post mode** is **Direct post**. Defaults to **No** if left blank. |
| Is AI generated content | Optional. Select **Yes** to mark the video as AI generated content. The **Is AI generated content** field is only available when **Post mode** is **Direct post**. Defaults to **No** if left blank. |
| Video URL | Enter the video's public URL on a domain you [verified in your TikTok app](/en/connectors/tiktok#url-verification). The **Video URL** field is required when **Source** is **Pull from URL**. |
| File | Map the video file to upload. The **File** field is required when **Source** is **File upload (stream)**. |
| Video size | Enter the file's total size, in bytes. The **Video size** field is required when **Source** is **File upload (stream)**. |

## Output

| Output field | Description |
| --- | --- |
| Publish ID | The post's unique identifier. Pass this value to the [Check post status](/en/connectors/tiktok/check-post-status-action) action to track publishing. |
| Upload URL | The URL the action uploaded the file to. The **Upload URL** field is only available when **Source** is **File upload (stream)**. |

---
