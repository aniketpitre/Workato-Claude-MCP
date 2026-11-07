---
url: 'https://docs.workato.com/en/connectors/canva-connect/upload-asset-action.md'
description: >-
  The Upload asset action uploads a file to a user's content library in Canva
  Connect and returns the uploaded asset.
---

# Canva Connect - Upload asset action

The **Upload asset** action uploads a file to a user's content library in Canva Connect and returns the uploaded asset. The action waits for the upload to complete and times out after `30` minutes.

## Input

| Input field | Description |
| --- | --- |
| Name | Enter the name of the asset. Maximum length is `50` characters. Can include emojis and other special characters. |
| File content | Enter the file you plan to upload. |

## Output

| Output field | Description |
| --- | --- |
| Asset ID | The unique ID of the uploaded asset. |
| Name | The name of the asset. |
| Tags | The tags attached to the asset. |
| Type | The asset type. |
| Import status | The state of the import (`in_progress`, `success`, or `failed`), and the error code and message if it failed. |
| Created at | The date and time the asset was created. |
| Updated at | The date and time the asset was last updated. |
| Thumbnail | The width, height, and URL of the asset's thumbnail image. |

---

---
url: >-
  https://docs.workato.com/en/connectors/canva-connect/upload-asset-from-url-action.md
description: >-
  The Upload asset from URL action starts an asynchronous job to upload an asset
  from a public URL into Canva Connect and returns the job ID.
---

# Canva Connect - Upload asset from URL action

The **Upload asset from URL** action starts an asynchronous job to upload an asset from a public URL into Canva Connect and returns the job ID, instead of waiting for the upload to finish. Use the [Get record details by ID](/en/connectors/canva-connect/get-record-details-by-id-action) action with the **URL asset upload job** object to poll the job for its status and resulting asset.

## Input

| Input field | Description |
| --- | --- |
| URL | Enter the publicly accessible URL of the asset you plan to upload. Supported images are `JPG`, `PNG`, `HEIC`, `WebP`, `TIFF`, `single-frame GIF`. Supported videos are `MP4`, `MOV`, `M4V`, `MKV`, `MPEG`, `WebM`. Maximum size is `50` MB for images and `100` MB for videos. |
| Name | Enter the display name for the asset. Defaults to the last segment of the URL if left blank. |

## Output

| Output field | Description |
| --- | --- |
| Job ID | The ID of the upload job. |
| Status | The status of the upload job. |

---
