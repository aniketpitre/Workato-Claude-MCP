---
url: 'https://docs.workato.com/en/connectors/aws-comprehend/create-record-action.md'
description: The Create record action creates a record in AWS Comprehend.
---

# AWS Comprehend - Create record action

The **Create record** action creates a record in AWS Comprehend.

## Input

Input fields are dynamic and based on the type of object you select. By default, the following fields are available.

| Input fields | Description |
| --- | --- |
| Object | Select an AWS Comprehend object. Options include **Document classifier** and **Endpoint**. |

## Output

This action returns the ARN of the object that was created.

| Output fields | Description |
| --- | --- |
| {Object} ARN | The ARN that identifies the created object. |

---

---
url: >-
  https://docs.workato.com/en/connectors/aws-comprehend/get-record-details-action.md
description: >-
  The Get record details action retrieves the details of a record, such as a
  document classification job using AWS Comprehend in Workato.
---

# AWS Comprehend - Get record details action

The **Get record details** action retrieves the details of a record, such as a document classification job using AWS Comprehend in Workato.

## Input

| Input fields | Description |
| --- | --- |
| Object | Select the object to retrieve details for, such as a document classification job. |
| Job ID | Enter the identifier for the AWS Comprehend job. |

## Output

| Output fields | Description |
| --- | --- |
| Document classification job properties | Data access role ARN: The ARN of the IAM role that grants Amazon Comprehend read access to your input data.; Document classifier ARN: The ARN that identifies the document classifier.; End time: The time that the document classification job completed.; Flywheel ARN: The ARN of the flywheel.; Input data config: The input data configuration that you supplied when you created the document classification job.; Job ARN: The ARN of the document classification job.; Job ID: The identifier assigned to the document classification job.; Job name: The name that you assigned to the document classification job.; Job status: The current status of the document classification job. If the status is `FAILED`, the message field shows the reason for the failure.; Message: A description of the status of the job.; Output data config: The output data configuration that you supplied when you created the document classification job.; Submit time: The time that the document classification job was submitted for processing.; Volume KMS Key ID: ID for the AWS KMS key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instances that process the analysis job.; VPC Config: Configuration parameters for a private VPC containing the resources you are using for your document classification job. |

---

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

---
