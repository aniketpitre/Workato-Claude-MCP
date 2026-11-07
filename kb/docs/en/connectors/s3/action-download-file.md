---
url: 'https://docs.workato.com/en/connectors/s3/action-download-file.md'
description: The Download file action downloads contents of a file in Amazon S3.
---

# Amazon S3 - Download file action

This action downloads contents of a file in Amazon S3. File contents can be used in subsequent steps of the recipe to upload the file into other applications.

This action uses [streaming mechanism](/en/features/file-streaming) and can support large file. However, the maximum file size you can download depends on how long the download takes. It is limited to Workato's job runtime quota (**5400 seconds**). Consider enabling [Amazon S3 transfer acceleration](https://docs.aws.amazon.com/AmazonS3/latest/dev/transfer-acceleration.html) to speed up the download.

![Amazon S3 - Download file action](/assets/download-file-action.BLq4JS22.png)_Amazon S3 - Download file action_

## Input

| Field name | Description |
| --- | --- |
| Region | Select the bucket's region to download the file from. For example, `us-west-2`. In Amazon S3, go to **Bucket > Properties > Static website hosting** to find your region in the Endpoint URL. |
| Bucket name | Enter the bucket name to download the file from. The bucket name is case sensitive. |
| Object name | Enter the name of the file to download. |
| Use accelerated endpoint | Select **true** if [Transfer Acceleration](https://docs.aws.amazon.com/AmazonS3/latest/dev/transfer-acceleration.html) is enabled for your Amazon S3 instance. |
| Download chunk size in kilobytes | Enter the chunk size. File contents are [streamed](/en/features/file-streaming) in chunks. The default chunk size is 1024 KB and the minimum is 32 KB. Workato manages the chunk size automatically by default. Configure this when you want to optimize the data throughput yourself. Larger chunk size increases throughput, but may exceed API quotas. |

## Output

| Field name | Description |
| --- | --- |
| File contents | The contents of the file. This is a [streaming object](/en/features/file-streaming). |
| Size | The size of the file in bytes. |

---
