---
url: >-
  https://docs.workato.com/en/connectors/google_cloud_storage/upload-object-with-file-streaming.md
description: >-
  The Upload object with file streaming action in the Google Cloud Storage
  connector uploads an object to a bucket using parallel uploads for any file
  size.
---

# Google Cloud Storage - Upload object with file streaming action

This action uploads an object to your Google cloud storage instance. This action sets up parallel uploads for files of all sizes for faster uploads.

## Input

| Field | Description |
| --- | --- |
| Bucket name **Required** | The name of the bucket to upload to. |
| Name **Required** | The name of the object to be uploaded. |
| Object content **Required** | Content of object to be uploaded. |

## Output

| Field | Description |
| --- | --- |
| Location | The location of the streaming upload. |
