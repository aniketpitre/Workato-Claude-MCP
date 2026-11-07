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
