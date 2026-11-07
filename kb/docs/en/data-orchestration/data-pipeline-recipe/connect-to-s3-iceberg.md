---
url: >-
  https://docs.workato.com/en/data-orchestration/data-pipeline-recipe/connect-to-s3-iceberg.md
description: >-
  Configure S3 Iceberg as a data pipeline destination to replicate records from
  source applications into Iceberg tables backed by AWS Glue or a REST catalog.
---

# Configure S3 Iceberg as your data pipeline destination

Set up S3 Iceberg as a destination for your data pipeline. This connection enables Workato to replicate data from source applications into Iceberg tables in Amazon S3, backed by either AWS Glue Data Catalog or an Iceberg REST catalog such as Snowflake Horizon Catalog, Apache Polaris, or Databricks Unity Catalog.

## Features supported

The following features are supported when using S3 Iceberg as a pipeline destination:

- Automatic creation of destination tables based on source schema.
- Field-level data replication without explicit field mapping.
- Choice of AWS Glue Data Catalog or an Iceberg REST catalog (Snowflake Horizon Catalog, Apache Polaris, Databricks Unity Catalog, or a self-hosted iceberg-rest server).
- Static key or vended credential AWS authentication, and Bearer token or OAuth 2.0 catalog authentication for REST catalogs.

## Prerequisites

You must have the following configuration and access:

- An Amazon S3 bucket to store Iceberg data files, and the AWS region it's located in
- An Iceberg catalog. Either an AWS Glue Data Catalog, or a REST catalog such as Snowflake Horizon Catalog, Apache Polaris, Databricks Unity Catalog, or a self-hosted iceberg-rest server
- AWS credentials, either as a static access key ID and secret, or through vended credentials issued by your REST catalog. Refer to [Create AWS credentials for S3 Iceberg](#create-aws-credentials-for-s3-iceberg) for the required permissions.
- A supported catalog authentication method if you use a REST catalog

## Create AWS credentials for S3 Iceberg

Create a dedicated IAM user if you use **AWS Glue** as your catalog type, or **Static keys** as your AWS authentication method with a REST catalog. Skip this section if you use vended credentials, because S3 Iceberg requests temporary, per-table credentials from your REST catalog instead.

1. Create an IAM policy in AWS with the following permissions:
   
   ```json
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Effect": "Allow",
               "Action": [
                   "s3:ListBucket*",
                   "s3:GetBucketLocation",
                   "s3:GetObject*",
                   "s3:PutObject",
                   "s3:PutObjectAcl",
                   "s3:DeleteObject"
               ],
               "Resource": [
                   "arn:aws:s3:::<your-bucket>/*",
                   "arn:aws:s3:::<your-bucket>"
               ]
           },
           {
               "Effect": "Allow",
               "Action": [
                   "glue:TagResource",
                   "glue:UnTagResource",
                   "glue:BatchCreatePartition",
                   "glue:BatchDeletePartition",
                   "glue:BatchDeleteTable",
                   "glue:BatchGetPartition",
                   "glue:CreateDatabase",
                   "glue:CreateTable",
                   "glue:CreatePartition",
                   "glue:DeletePartition",
                   "glue:DeleteTable",
                   "glue:GetDatabase",
                   "glue:GetPartition",
                   "glue:GetPartitions",
                   "glue:GetTable",
                   "glue:GetTables",
                   "glue:UpdateDatabase",
                   "glue:UpdatePartition",
                   "glue:UpdateTable"
               ],
               "Resource": ["*"]
           },
           {
               "Effect": "Allow",
               "Action": [
                   "athena:StartQueryExecution",
                   "athena:GetQueryExecution",
                   "athena:GetQueryResults",
                   "athena:StopQueryExecution",
                   "athena:GetWorkGroup",
                   "athena:ListWorkGroups"
               ],
               "Resource": ["*"]
           }
       ]
   }
   ```
   
   Scope the S3 statement's `Resource` values to your warehouse bucket. The `s3` actions apply to every catalog type. The `glue` and `athena` actions apply only if you use **AWS Glue**.
   
2. Create an IAM user and attach the policy from the previous step.
   
3. Generate an access key for the user. Use the resulting **access key ID** and **secret access key** when you configure the connection.
   

For REST catalogs, grant access through the catalog itself instead of an IAM policy. For example, Snowflake Horizon Catalog requires a role with `CREATE ICEBERG TABLE` privileges and usage on an [external volume](https://docs.snowflake.com/en/user-guide/tables-iceberg-configure-external-volume-s3) configured for your S3 bucket, plus a programmatic access token to use as either the **Bearer token** or the **OAuth 2.0 credential** value.

## Connect to S3 Iceberg

Complete the following steps to connect to **S3 Iceberg** as a data pipeline destination:

Connect to S3 Iceberg

1. Select **Create > Connection** or press C twice.
   
2. Search for `S3 Iceberg` and select it as your app.
   
3. Enter a name in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter the **AWS region** of your S3 bucket and Glue catalog, if applicable. Workato requires this value even if you use vended credentials.
   
6. Enter a value in the **Warehouse** field:
   
   - **AWS Glue**: an S3 URI where Iceberg data files land, such as `s3://my-bucket/warehouse`.
   - **REST catalogs**: a catalog-specific value. For Snowflake, enter the database name, such as `MY_DATABASE`. For Databricks Unity Catalog or a self-hosted iceberg-rest catalog, enter an S3 URI.
7. Use the **Catalog type** drop-down menu to select the Iceberg catalog backing the destination, then complete the corresponding steps based on your selection:
   
   **AWS Glue**
   
   Select **AWS Glue** for tables stored in AWS Glue Data Catalog.
   
   1. Use the **AWS authentication** drop-down menu to select **Static keys**. AWS Glue requires the access key ID and secret you provide, rather than vended credentials.
      
   2. Enter your AWS access key ID and secret access key.
      
   
   **REST**
   
   Select **REST** for Iceberg REST catalogs, such as Snowflake Horizon Catalog, Apache Polaris, Databricks Unity Catalog, or a self-hosted iceberg-rest server.
   
   1. Enter the base URI of the Iceberg REST catalog endpoint in the **Catalog URI** field.
      
   2. Use the **Catalog authentication** drop-down menu to select an authentication method for the REST catalog:
      
      - **Bearer token**: sends a personal access token directly as an `Authorization: Bearer <token>` header. Supported by Snowflake Horizon Catalog, Databricks Unity Catalog, and some self-hosted iceberg-rest catalogs.
      - **OAuth 2.0**: exchanges a credential at a token endpoint for a session token on every catalog initialization. Supported by Apache Polaris and Snowflake Horizon Catalog.
   3. Enter your token in the **Bearer token** field when you select **Bearer token** as the authentication method. Workato sends this value as `Authorization: Bearer <token>` on every catalog request. Use a Databricks personal access token for Databricks Unity Catalog, or a programmatic access token (PAT) for Snowflake Horizon Catalog.
      
   4. Complete the following fields when you select **OAuth 2.0** as the authentication method:
      
      - **OAuth 2.0 credential**: the credential Workato exchanges at the token endpoint for a session token. For Snowflake Horizon Catalog, use the raw programmatic access token (PAT). For other catalogs, this is usually a `client_id:client_secret` pair.
      - **OAuth 2.0 scope**: the scope requested for the catalog token. For Snowflake Horizon Catalog, use `session:role:<ROLE>`, such as `session:role:iceberg_role`.
      - **OAuth 2.0 server URI**: the OAuth 2.0 token endpoint that exchanges the credential for a session token.
   5. Use the **AWS authentication** drop-down menu to select how AWS credentials are supplied:
      
      - **Static keys**: uses the access key ID and secret you provide. Select this option if your REST catalog doesn't vend credentials.
      - **Vended credentials**: requests per-table temporary credentials from the REST catalog (Snowflake Horizon Catalog, Apache Polaris, Databricks Unity Catalog). Doesn't require AWS keys.
   6. Enter your **AWS access key ID** and **AWS secret access key** when you select **Static keys** as the AWS authentication method.
      
   
8. Click **Connect** to verify and establish the connection.
   

## Configure the destination action

Ensure the destination warehouse and catalog are newly created and empty before you start the pipeline. This prevents errors during the initial sync and allows the pipeline to create destination tables without conflicts.

1. Click the **Load data to target table in destination app** action. This action defines how the pipeline replicates data in the destination.
   
2. Select **S3 Iceberg** from the list of available destination apps.
   
3. Choose the S3 Iceberg connection you plan to use for this pipeline. Alternatively, click **\+ New connection** to create a new connection.
   
   The **Load data to target table in destination app** action automatically replicates the object schema from the source to S3 Iceberg. Explicit field mapping isn't required.
   
4. Enter a value in the **Namespace** field. This sets the Iceberg namespace under which target tables are created:
   
   - **AWS Glue**: the Glue database name, such as `sales_pipeline`. Glue database names must be 1-255 characters. Refer to the [AWS Glue Table API reference](https://docs.aws.amazon.com/glue/latest/webapi/API_GlueTable.html) for the full naming pattern.
   - **REST catalogs**: a catalog-specific value. For Snowflake, enter the schema name inside the database given as the warehouse, such as `SALES_PIPELINE_SCHEMA`. Naming limits depend on your catalog, so refer to your catalog vendor's identifier rules.
   
   ![Configure S3 Iceberg destination](/assets/configure-s3-iceberg-destination.DWkL4zdd.png)_Configure S3 Iceberg destination_
   
   Workato creates tables under the `workato` namespace if you leave this field blank.
   
5. Select **Save** to save the pipeline.
