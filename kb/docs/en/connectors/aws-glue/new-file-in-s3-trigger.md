---
url: 'https://docs.workato.com/en/connectors/aws-glue/new-file-in-s3-trigger.md'
description: The New file in S3 trigger monitors AWS Glue for a new file in AWS S3.
---

# AWS Glue - New file in S3 trigger

The **New file in S3** trigger monitors AWS Glue for a new file in AWS S3.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Select an interval to check AWS Glue for new results. Refer to [Polling intervals](/en/recipes/polling-intervals) for more information. |
| Bucket name | Enter the name of the S3 bucket to monitor for new files. |
| Prefix (folder path) | Enter a prefix or folder path to use to filter new files. |
| When first started, this recipe should pick up events from | Select a date and time to start picking up trigger events. This enables your recipe to capture past events. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

## Output

| Output field | Description |
| --- | --- |
| File key | The unique identifier (name and path) for the new S3 file. |
| Last modified | The date that the new S3 file was modified. |
| Size (bytes) | The size of the new S3 file in bytes. |
| ETag | Entity tag identifying the version of the new S3 file. |
| Storage class | The storage class of the new S3 file. |
| Bucket name | The bucket name where the new S3 file is located. |
| Full S3 path | The path to the new S3 file. |

---
