---
url: 'https://docs.workato.com/en/connectors/aws-glue.md'
description: Use the AWS Glue connector to prepare and transform data for analytics.
---

# AWS Glue

[AWS Glue](https://docs.aws.amazon.com/glue/latest/webapi/WebAPI_Welcome.html) is a fully managed extract, transform, and load (ETL) service that enables you to prepare and transform data for analytics. It provides a serverless environment to run ETL jobs, automatically discovers and catalogs your data, and generates ETL code to transform your data from source to target. AWS Glue simplifies the process of building, running, and monitoring data pipelines at scale.

This connector has the following capabilities:

- Start AWS Glue ETL jobs with custom parameters and configurations
- Stop running Glue jobs
- Monitor job status and retrieve detailed execution information
- Get job details including configuration, scripts, and execution properties
- Trigger workflows when new files are added to S3 buckets
- Monitor job run status changes for automated pipeline management

## Prerequisites

Enable the following permissions for your user or IAM account to establish a connection to AWS Glue:

View permissions

- `glue:GetJobs`
- `glue:StartJobRun`
- `glue:BatchStopJobRun`
- `glue:GetJobRun`
- `glue:GetJobRuns`
- `glue:GetJob`

Enable the following additional permissions for S3 trigger functionality:

View S3 trigger permissions

- `s3:ListBucket`
- `s3:GetObject`

## Connection setup

Workato supports the following types of connections to AWS Glue:

- [IAM role authentication](#iam-role-auth)
- [Access key authentication](#access-key-auth)

> **IAM ROLE AUTHENTICATION**
> 
> Workato recommends creating a dedicated integration role for this Workato connection. This helps maintain clear permission boundaries and control what actions Workato can access and perform in the application.
> 
> Refer to the following documentation for more information about IAM role authentication in Workato:
> 
> - [Use IAM role-based authentication for AWS Services](/en/security/data-protection/secrets-management/iam-role-based-authentication-for-aws#supported-connectors)
> - Amazon's [Create an IAM user in your AWS account](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html) documentation

### IAM role authentication

For this authentication method, you must provide the [IAM role ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html).

Complete the steps in [Use IAM role-based authentication for AWS Services](/en/security/data-protection/secrets-management/iam-role-based-authentication-for-aws#retrieve-iam-role-arn) to get the required IAM role Amazon Resource Name (ARN).

#### Connect to AWS using IAM role authentication

Complete the following steps to set up an IAM role connection to AWS Glue in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select AWS Glue as your connection on the **New Connection** page.
   
3. Provide a unique name for the connection in the **Connection name** field.
   
   ![AWS Glue Connection](/assets/aws-glue-connection-setup.BUmROvrn.png)_Create your connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authentication type** drop-down menu to select **IAM role** as the authentication type.
   
6. Enter your **IAM role ARN**.
   
7. Enter the **Region** where your AWS Glue jobs are located. The region is in your AWS Glue console URL. For example, if the console URL is `https://us-east-1.console.aws.amazon.com/glue/home?region=us-east-1`, your region is `us-east-1`.
   
8. Click **Connect**.
   

### Access key authentication

Access key authentication requires an access key ID.

#### Retrieve an access key ID

Complete the following steps to obtain the access key information from AWS:

1. Go to your **AWS account name**.
   
2. Click **Credentials > Users**.
   
3. Copy your existing **Access key ID** or create a new access key. Refer to the [AWS Glue](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) documentation for detailed steps about creating and managing access keys.
   

### Connect to AWS Glue using access key authentication

Complete the following steps set up an access key connection to AWS Glue in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select AWS Glue as your connection on the **New Connection** page.
   
3. Provide a unique name for the connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authentication type** drop-down menu to select **Access key** as the authentication type.
   
6. Enter your **Access key ID**.
   
7. Enter your **Secret access key**.
   
8. Enter the **Region** where your AWS Glue jobs are located. The region is in your AWS Glue console URL. For example, if the URL is `https://us-east-1.console.aws.amazon.com/glue/home?region=us-east-1`, your region is `us-east-1`.
   
9. Click **Connect**.

---
