---
url: >-
  https://docs.workato.com/en/connectors/oracle-object-storage/download-object-stream-action.md
description: >-
  The Download object (stream) action downloads an object from Oracle Object
  Storage.
---

# Oracle Object Storage - Download object (stream) action

The **Download object (stream)** action downloads an object from Oracle Object Storage. Subsequent recipe steps can use the file contents to upload the file into another app.

There is no fixed limit on file size. The maximum file size depends on whether the download can finish within the [job timeout limit](/en/recipes/jobs#timeouts).

## Input

| Input field | Description |
| --- | --- |
| Bucket name | Select or enter the name of the bucket to download from. |
| Object name | Select or enter the name of the object to download. |
| Version ID | Enter a version ID to specify a version of the object. |
| HTTP response content disposition | Specify the value of content disposition. |
| HTTP response cache control | Specify the value of cache control to override it in the response headers. |
| HTTP response content type | Specify the value of content type to override it in the response headers. |
| HTTP response content language | Specify the value of content language to override it in the response headers. |
| HTTP response content encoding | Specify the value of content encoding to override it in the response headers. |
| HTTP response expires | Specify the value of expires to override it in the response headers. |
| Headers | Specify custom request headers to send with the request. Includes if, if none match, client request ID, SSE customer algorithm, SSE customer key, SSE customer key SHA256. |

## Output

| Output field | Description |
| --- | --- |
| Headers | Response headers. Includes entity tag (ETag), archival state, cache control, content disposition, content encoding, content language, content length, content MD5, content range, content type, expires, last modified, client request ID, multirt MD5, request ID, storage tier, time of archival and version ID. |
| Contents | File contents. |
| Name | Name of the object. |
