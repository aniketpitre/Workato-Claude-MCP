---
url: 'https://docs.workato.com/en/connectors/bluesky/upload-image-action.md'
description: >-
  The Upload image action enables you to upload an image blob for use in posts
  in Bluesky.
---

# Bluesky - Upload image action

The **Upload image** action uploads an image blob you can attach to a post or thread.

## Input

| Input field | Description |
| --- | --- |
| File content | Enter the binary contents of the image file. Maximum size is `2,000,000` bytes. |
| Content type | Select the MIME type of the image, such as `PNG`, `JPEG`, `GIF`, or `WebP`. |

## Output

| Output field | Description |
| --- | --- |
| Blob | Uploaded image blob, including the following properties. |
| Type | Blob type. |
| MIME type | MIME type of the uploaded image. |
| Size | Size of the uploaded image, in bytes. |
| Reference | Content-addressed reference to the uploaded blob, including the following property. |
| Link | Reference link to pass into the Images field of the [Create record](/en/connectors/bluesky/create-record-action) or [Create thread](/en/connectors/bluesky/create-thread-action) action. |

---
