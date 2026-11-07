---
url: 'https://docs.workato.com/en/connectors/s3/action-copy-file.md'
description: >-
  Copy a file between Amazon S3 buckets with the Copy file action, optionally
  into a different Region and with a canned ACL.
---

# Amazon S3 - Copy file action

Use the **Copy file** action to copy an Amazon S3 file from a source bucket to a destination bucket. This action supports single-copy operations for files up to 5 GB. If you don't specify a destination Region, the action uses the Region configured in the connection.

## Input

| Input field | Description |
| --- | --- |
| Bucket | Select the bucket that contains the file to copy. |
| Object name | Enter the file path (object key) of the file to copy. For example, `subfolder001/filename.csv`. Ensure the path is exact because object names are case-sensitive. Refer to the [AWS prefix documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-prefixes.html) for more information. |
| Destination bucket | Select the bucket to store the copied file. |
| Destination object name | Enter the file path (object key) to assign to the copied file. For example, `subfolder001/filename.csv`. Ensure the path is exact because object names are case-sensitive. Refer to the [AWS prefix documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-prefixes.html) for more information. |
| Canned ACL | Select a [canned ACL](https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-overview.html#canned-acl) to apply to the copied file. |
| Destination region | Specify the AWS Region of the destination bucket. For example, `us-west-2`. Leave this field blank to use the Region configured in the connection. |

## Output

| Output field | Description |
| --- | --- |
| Last modified | Returns the creation date and time of the copied file. |
| E tag | Returns the ETag of the copied file. This reflects changes to the file's contents, not its metadata. |

---
