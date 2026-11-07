---
url: 'https://docs.workato.com/en/connectors/s3-lake.md'
description: >-
  S3 Data Lake is a centralized AWS service that stores and manages structured
  and unstructured data at scale using Amazon S3 and AWS Glue.
---

# S3 Data Lake

[S3 Data Lake](https://aws.amazon.com/data-lake/) is a centralized repository that allows you to store your structured and unstructured data at any scale. You can use the S3 Data Lake connector in Workato to run custom AWS Glue jobs and manage datasets in your AWS environment.

## Prerequisites

Ensure you meet the following requirements before you set up a connection:

- An active AWS account
- IAM user or role with the following required permissions:
  - `glue:GetDatabases`
  - `glue:GetDatabase`
  - `glue:GetTables`
  - `glue:GetTable`
  - `glue:CreateTable`
  - `glue:CreateJob`
  - `glue:DeleteJob`
  - `glue:StartJobRun`
  - `glue:GetJobRun`
  - `glue:GetCatalogs`
  - `s3:GetObject`
  - `s3:PutObject`
  - `s3:DeleteObject`
  - `s3:ListBucket`

## Connection setup

You can create a connection to your S3 Data Lake account using either **Access key** or **IAM role** authentication:

**Access key**

1. Sign in to your Workato account.
   
2. Create a new connection and select the **S3 Data Lake** connector.
   
3. Enter a **Connection name** to identify the connection.
   
   ![Connection name for S3 Data Lake](/assets/configure-s3-lake.CuDh47HO.png)_Configure S3 Data Lake connection in Workato_
   
4. Select the **Location** where you plan to store the connection.
   
5. Select **Access key** as the **Authentication type**. Refer to the [Identity and access management for AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/security-iam.html) guide for more information about IAM-based access.
   
6. Enter the **Access key ID** and **Secret access key** from your IAM user. Go to **IAM > Users > \[your user\] > Security credentials** in the AWS console to retrieve these credentials. Refer to [Use IAM role-based authentication for AWS Services](/en/security/data-protection/secrets-management/iam-role-based-authentication-for-aws#use-iam-role-based-authentication-for-aws-services) for more information.
   
7. Enter the AWS **Region** where your S3 buckets and Glue jobs reside. For example, your region is `us-east-1`, if your console URL is `https://us-east-1.console.s3.amazon.com`.
   
8. Click **Connect**.
   

**IAM role**

1. Create a new connection and select the **S3 Data Lake** connector.
   
2. Enter a **Connection name** to identify the connection. ![Connection name for S3 Data Lake](/assets/configure-s3-lake.CuDh47HO.png)_Connection name_
   
3. Select the **Location** where you plan to store the connection.
   
4. Select **IAM role** as the **Authentication type**. Refer to the [Identity and access management for AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/security-iam.html) guide for more information about authentication and access control.
   
5. Create a new IAM role in your AWS account and add the following settings:
   
   - Use your **Workato AWS Account ID** as the **Principal**.
   - Use your **Workato External ID** as the **External ID**.
6. Enter the newly created **IAM role ARN**.
   
7. Enter the AWS **Region** where your S3 buckets and Glue jobs reside.
   
8. Click **Connect**.

---
