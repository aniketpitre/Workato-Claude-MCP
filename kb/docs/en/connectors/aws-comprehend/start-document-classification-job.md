---
url: >-
  https://docs.workato.com/en/connectors/aws-comprehend/start-document-classification-job.md
description: >-
  The Start document classification job action starts an asynchronous job to
  classify a collection of documents using a custom AWS Comprehend model.
---

# AWS Comprehend - Start document classification job action

The **Start document classification job** action starts an asynchronous job to classify a collection of documents using a custom AWS Comprehend model.

## Input

| Input fields | Description |
| --- | --- |
| Job name | Enter the name of the document classification job. |
| Document classifier | Select the document classifier model to use in the job. |
| Input data config | Configure the input data, such as the S3 URI and document reader configuration. |
| Output data config | Configure the input data, such as the S3 URI. |
| Data access role ARN | Enter the ARN of the AWS IAM role that grants AWS Comprehend read access to your input data. |
| Tags | Select any tags from the tags resource list and enter their key-value pairs. |
| VPC config | Configure any VPC settings, including security group IDs and subnets. |

## Output

| Output fields | Description |
| --- | --- |
| Document classifier ARN | The ARN of the custom classification model. |
| Job ARN | The ARN of the document classification job. It is a unique, fully qualified identifier for the job. |
| Job ID | The identifier generated for the job. |
| Job status | The status of the job. |
