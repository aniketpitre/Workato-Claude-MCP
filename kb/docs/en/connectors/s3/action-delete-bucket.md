---
url: 'https://docs.workato.com/en/connectors/s3/action-delete-bucket.md'
description: >-
  Permanently delete an empty Amazon S3 bucket with the Delete bucket action,
  optionally specifying the bucket's Region.
---

# Amazon S3 - Delete bucket action

Use the **Delete bucket** action to permanently delete an Amazon S3 bucket. You can delete a bucket only after all of its objects have been removed.

## Input

| Input field | Description |
| --- | --- |
| Bucket | Select the bucket to delete. |
| Region | Specify the AWS Region of the bucket. For example, `us-west-2`. Leave this field blank to use the Region configured in the connection. |

## Output

| Output field | Description |
| --- | --- |
| Success | Indicates whether the bucket was deleted successfully. |

---
