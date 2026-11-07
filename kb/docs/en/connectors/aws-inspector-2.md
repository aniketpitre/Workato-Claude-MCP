---
url: 'https://docs.workato.com/en/connectors/aws-inspector-2.md'
description: >-
  The AWS Inspector2 connector enables you to automate vulnerability management
  workflows by retrieving and responding to security findings in AWS.
---

# AWS Inspector2

[AWS Inspector](https://aws.amazon.com/inspector/) is a vulnerability discovery service that automates continuous scanning for security vulnerabilities within your Amazon EC2, Amazon ECR, and Amazon Web Services Lambda environments.

## Prerequisites

Ensure you have an active AWS account with the proper permissions to set up and manage AWS Inspector2 before using the AWS Inspector2 connector in Workato:

- **Enable Amazon Inspector:** Ensure that Amazon Inspector is enabled for your AWS account. You can activate it in the Inspector dashboard of the AWS Management Console.
  
- **IAM Permissions:** Grant the necessary permissions to users or roles that will manage and operate Amazon Inspector. Key managed policies include: `AmazonInspector2FullAccess` and `AmazonInspector2ReadOnlyAccess`.
  
- **Set up and Configure Amazon EC2:** Ensure you have EC2 instances running in your AWS environment. Inspector 2 scans workloads such as EC2 instances and container images in the Amazon Elastic Container Registry (ECR).
  
- **Install Systems Manager Agent (SSM Agent):** Install and configure the AWS Systems Manager Agent (SSM Agent) on all EC2 instances so that Inspector 2 can gather data. For supported operating systems, it is either pre-installed or needs manual installation.
  
- **Enable Resource Scanning:** Configure which resources Amazon Inspector should scan:
  
  - EC2 Instances: Activate scanning for operating system vulnerabilities.
  - ECR Repositories: Ensure repositories are connected for image vulnerability assessments.
- **Review VPC Configurations:** Ensure that network configurations (such as, firewalls, security groups) allow Amazon Inspector2 to access the required resources.
  
- **Service Quotas:** Check your service quotas to ensure you have sufficient quotas for scanned resources, findings, etc.
  

## Connection Setup

Workato supports the following types of connections to AWS Inspector2.

- [Access key authentication](#access-key-authentication)
- [IAM role authentication](#iam-role-authentication)

### Access key authentication

The AWS access key ID and secret are required for access key authentication. Go to **AWS account name > Credentials > Users** to find an existing user's credentials or create a new user.

Complete the following steps to establish a connection to AWS Inspector2 in Workato using IAM role authentication:

1. Install the **AWS Inspector2** connector from the community library. Refer to the [Install a connector from the community library](/en/community-library/install-connectors) guide for more information.
   
2. Click **Create > Connection** or press C twice.
   
3. Search for and select `AWS Inspector2` as your connection on the **New Connection** page.
   
4. Provide a name for your connection in the **Connection name** field.
   
   ![AWS Inspector 2 Access key connection](/assets/aws-inspector-2-connection-access-key.BtQZV2Ct.png)_AWS Inspector 2 Access key connection_
   
5. Use the **Auth type** field to select **Access key** as the connection type.
   
6. Enter your app's **Access key ID** and **Secret access key**.
   
7. Provide the AWS inspector **Region**, such as `us-west-2`.
   
8. Click **Connect**.
   

### IAM role authentication

IAM roles provide temporary credentials for accessing AWS Inspector without long-term access keys. This method is recommended for applications running in AWS environments like EC2, Lambda, ECS, or EKS.

Complete the following steps to establish a connection to AWS Inspector2 in Workato using IAM role authentication:

1. Install the **AWS Inspector2** connector from the community library. Refer to the [Install a connector from the community library](/en/community-library/install-connectors) guide for more information.
   
2. Click **Create > Connection** or press C twice.
   
3. Search for and select `AWS Inspector2` as your connection on the **New Connection** page.
   
4. Provide a name for your connection in the **Connection name** field.
   
5. Use the **Auth type** field to select **IAM Role** as the connection type.
   
6. Enter the provisioned IAM role's ARN in the **IAM role ARN** field.
   
7. Provide the AWS inspector **Region**, such as `us-west-2`.
   
8. Click **Connect**.
   
   ![AWS Inspector 2 IAM role connection](/assets/aws-inspector-2-connection-iam-role.Dl8RarzH.png)_AWS Inspector 2 IAM role connection_

---
