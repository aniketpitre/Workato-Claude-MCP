---
url: 'https://docs.workato.com/en/connectors/s3/action-upload-file-streaming.md'
description: >-
  The Upload file action (streaming) uploads a file to a bucket or folder in
  Amazon S3.
---

# Amazon S3 - Upload file action (streaming)

The **Upload file** action (streaming) uploads a file to a bucket or folder in Amazon S3. If a file with the same name and path already exists in that location, uploading a new file overwrites the existing file.

> **WHICH UPLOAD ACTION SHOULD YOU USE?**
> 
> The **Upload file** [non-streaming](/en/connectors/s3/action-upload-file) and streaming actions both upload files, but they differ in how they process data and what they return.
> 
> - Use the non-streaming action for **smaller files** where you need a simple confirmation after the upload completes.
> - Use the streaming action for **larger files or continuous data streams**. This action processes the file in chunks and returns the file location instead. This method is better for handling large datasets, real-time processing, or incremental uploads. Learn more about [file streaming](/en/features/file-streaming).

## Input

| Input field | Description |
| --- | --- |
| Bucket name | Select the bucket where you plan to upload the file or enter the bucket name directly. This field is case-sensitive. |
| Object name | Enter the name of the file you plan to upload. For objects in folders, specify the object path. |
| Region | Provide the region of the bucket where you plan to upload the file, such as `us-west-2`. You can locate this value in Amazon S3 by going to **Bucket > Properties > Static website hosting**. The region is in the endpoint URL. |
| Contents | Provide the contents of the file to upload. This field accepts a datapill, such as File content, or raw text. |
| Use accelerated endpoint | Enter `true` if [Transfer Acceleration](https://docs.aws.amazon.com/AmazonS3/latest/dev/transfer-acceleration.html) is enabled for your Amazon S3 instance. |
| Canned ACL | Use [Amazon's Canned Access Control List](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl) to specify permissions for this uploaded file. |

## Output

| Output field | Description |
| --- | --- |
| Location | The location where the file was uploaded. |

---
