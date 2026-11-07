---
url: 'https://docs.workato.com/en/connectors/textract/start-lending-action.md'
description: >-
  The Start lending analysis action starts the classification and extraction of
  data from lending documents stored in an Amazon S3 bucket.
---

# Amazon Textract - Start lending analysis action

The **Start lending analysis** action starts the classification and extraction of data from lending documents stored in an Amazon S3 bucket.

## Input

| Input field | Description |
| --- | --- |
| S3 bucket | Enter the name of the S3 bucket containing the input document. |
| S3 object key | Enter the path/key to the object in the bucket. |
| S3 object version | Optional. Enter the version of the S3 object to analyze. |
| Client request token | Optional. Provide a unique token to prevent duplicate analysis jobs if the action runs multiple times. |
| Job tag | Optional. Enter a tag to identify the job. |
| Notification channel | Optional. Expand this section to specify an SNS topic ARN and role ARN for job completion notifications. |
| Output config | Optional. Expand this section to define the output location and S3 bucket. |
| KMS key ID/ARN | Optional. Provide a KMS key ID or ARN to encrypt the output files. |

## Output

| Output field | Description |
| --- | --- |
| Job ID | Unique identifier for the analysis job. Use this ID with the [Get lending analysis](/en/connectors/textract/get-lending-action) action to retrieve results. |

---
