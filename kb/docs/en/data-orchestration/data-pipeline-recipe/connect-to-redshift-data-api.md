---
url: >-
  https://docs.workato.com/en/data-orchestration/data-pipeline-recipe/connect-to-redshift-data-api.md
description: >-
  Configure Amazon Redshift Data API as a data pipeline destination to replicate
  records from source applications into Redshift tables, staged through Amazon
  S3.
---

# Configure Amazon Redshift Data API as your data pipeline destination

Set up Amazon Redshift Data API as a destination for your data pipeline. This connection enables Workato to replicate data from source applications into Amazon Redshift tables, staging data in Amazon S3 before loading it into Redshift through the Redshift Data API.

## Features supported

The following features are supported when using Amazon Redshift Data API as a pipeline destination:

- Automatic creation of destination tables based on source schema
- Field-level data replication without explicit field mapping
- Data staged in Amazon S3 before loading into Redshift through the Redshift Data API
- IAM role or AWS access key authentication

## Prerequisites

Connecting Amazon Redshift Data API as a data pipeline destination requires:

- An Amazon Redshift cluster or workgroup, and the AWS region it's located in
- An Amazon S3 bucket to stage data before it loads into Redshift
- AWS credentials, either an IAM role ARN to assume, or a static AWS access key ID and secret access key
- The name of the Redshift database to connect to

## Connect to Amazon Redshift Data API

Complete the following steps to connect to **Amazon Redshift Data API** as a data pipeline destination. This connection allows the pipeline to replicate and load data into Amazon Redshift.

Connect to Amazon Redshift Data API

1. Select **Create > Connection** or press C twice.
   
2. Search for `Amazon Redshift Data API` and select it as your app.
   
3. Enter a name in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authorization type** drop-down menu to select how AWS credentials are supplied, then complete the corresponding steps based on your selection:
   
   **IAM role**
   
   1. Enter the **IAM role ARN** to assume for accessing Redshift and S3.
      
   2. Optional. Enter an **External ID** for the `AssumeRole` call.
      
   
   **Access key**
   
   1. Enter your **Access key ID** and **Secret access key** for authenticating with Redshift and S3.
      
   
6. Enter the **Region** where your Redshift cluster or workgroup is located, such as `us-east-1`.
   
7. Use the **Deployment type** drop-down menu to select your Redshift deployment type:
   
   - **Serverless** for a Redshift Serverless workgroup.
   - **Provisioned** for a provisioned Redshift cluster.
8. Enter the name of your Redshift Serverless workgroup in the **Workgroup name** field, or the identifier of your Redshift cluster in the **Cluster identifier** field, depending on the **Deployment type** you selected.
   
9. Enter the name of the Redshift database to connect to in the **Database** field.
   
10. Click **Connect** to verify and establish the connection.
    

## Configure the destination action

Ensure the destination database and schema are newly created and empty before you start the pipeline. This prevents errors during the initial sync and allows the pipeline to create destination tables without conflicts.

Complete the following steps to configure the destination action:

1. Click the **Load data to target table in destination app** action. This action defines how the pipeline replicates data in the destination.
   
2. Select **Amazon Redshift Data API** from the list of available destination apps.
   
3. Choose the Amazon Redshift Data API connection to use for this pipeline. Alternatively, click **\+ New connection** to create a new connection.
   
   The **Load data to target table in destination app** action automatically replicates the object schema from the source to Redshift. Explicit field mapping isn't required.
   
4. Use the **S3 staging bucket** field to select the S3 bucket Workato uses to stage data before loading it into Redshift. Alternatively, enter the bucket name directly.
   
   ![Configure Amazon Redshift Data API destination](/assets/configure-amazon-redshift-destination.DIypTIXg.png)_Configure Amazon Redshift Data API destination_
   
5. Optional. Set the Redshift schema for target tables in the **Schema** field. Workato uses the `public` schema if you leave this field blank.
   
6. Select **Save** to save the pipeline.
