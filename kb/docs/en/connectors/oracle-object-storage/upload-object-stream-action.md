---
url: >-
  https://docs.workato.com/en/connectors/oracle-object-storage/upload-object-stream-action.md
description: The Upload object (stream) action uploads an object to Oracle Object Storage.
---

# Oracle Object Storage - Upload object (stream) action

The **Upload object (stream)** action uploads an object to Oracle Object Storage. The minimum file size is 64 MiB.

There is no fixed limit on maximum file size. The maximum file size depends on whether the upload can finish within the [job timeout limit](/en/recipes/jobs#timeouts).

## Input

| Input field | Description |
| --- | --- |
| Bucket name | Enter the name of the bucket to upload to. |
| Object name | Enter the name of the object to upload. |
| Contents | Specify a binary string of the object to upload to the object store. |

## Output

| Output field | Description |
| --- | --- |
| Success | Whether the file was uploaded successfully or not. |
| Object name | Name of the object. |
| Upload ID | ID of the upload operation. |
| Parts uploaded | Number of parts uploaded to complete the multipart file upload. |
| Total bytes uploaded | Size of the uploaded files in bytes. |
