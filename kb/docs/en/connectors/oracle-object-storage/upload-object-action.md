---
url: >-
  https://docs.workato.com/en/connectors/oracle-object-storage/upload-object-action.md
description: The Upload object action uploads an object to Oracle Object Storage.
---

# Oracle Object Storage - Upload object action

The **Upload object** action uploads an object to Oracle Object Storage. This action is recommended for small files up to 100 MiB. For larger files, use the [Upload object (stream) action](/en/connectors/oracle-object-storage/upload-object-stream-action).

## Input

| Input field | Description |
| --- | --- |
| Bucket name | Select or enter the name of the bucket. |
| Object name | Select or enter the name of the object to upload. |
| Contents | Specify a binary string of the object to upload to the object store. |
| Headers | Specify custom request headers to send with the request. Includes if match, if none match, client request ID, content length, content MD5, content type, content language, content encoding, content disposition, cache control, SSE customer algorithm, SSE customer key, SSE customer key SHA256, KMS key OCID and storage tier. |

## Output

| Output field | Description |
| --- | --- |
| Headers | Response headers. This includes the entity tag (ETag), last modified, client request ID, multipart MD5, request ID and version ID. |
| Status | Whether the file was uploaded successfully or not. |
