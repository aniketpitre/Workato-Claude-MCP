---
url: 'https://docs.workato.com/en/connectors/s3/action-presign-url.md'
description: >-
  The Generate presigned URL action creates a temporary URL to a specific object
  in your Amazon S3 bucket. This URL can be passed to third-party users to
  upload, download, or modify an existing object.
---

# Amazon S3 - Generate presigned URL action

This action creates a temporary URL to a specific object in your Amazon S3 bucket. This URL can be passed to third-party users to upload, download, or modify an existing object.

Use this action to securely share temporary access to your S3 bucket.

![Generate presign URL](/assets/generate-presign-url.BMQ-PtSg.png)_Generate presigned URL_

## Input

| Input | Description |
| --- | --- |
| Region | The region of the bucket to list the files from, for example, us-west-2. In Amazon S3, go to **Bucket > Properties > Static website hosting** to find your region in the Endpoint URL. |
| Bucket name | The bucket to list files from. |
| Object name | The name of the object, including file path and extension. |
| HTTP method | The HTTP method allowed for this URL. |
| Expires in | The duration of this presigned URL, in seconds. This field defaults to 900 seconds. |

## Output

The output of this action is a presigned URL for the specified object.

---
