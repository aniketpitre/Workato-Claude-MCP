---
url: >-
  https://docs.workato.com/en/security/data-protection/secrets-management/iam-role-based-authentication-for-aws.md
description: >-
  Use IAM role-based authentication to grant Workato scoped access to AWS
  services without sharing AWS security credentials.
---

# Use IAM role-based authentication for AWS Services

AWS IAM role authentication allows you to provide a dedicated role in your AWS instance for Workato to use. By provisioning a dedicated IAM profile, the owner of the AWS instance can grant Workato access to AWS resources without sharing AWS security credentials. This also helps to maintain permission boundaries, including controlled access to specific AWS services and actions that are permitted by the third-party application (for example, Workato). When configuring connections using IAM role-based authentication, the external ID's used can be scoped to either the **workspace or project level**.

Configuring the IAM role using external ID's scoped at the project level allows you to give individual projects more granular access to your AWS resources. For example, only allowing Amazon SQS access to your "DevOps" project instead of being accessible to all projects in your workspace.

## Supported connectors

We support IAM role-based authentication for the following AWS Services and universal connectors:

- Amazon Lex
- Amazon S3
- Amazon SES
- AWS Lambda
- AWS SQS
- AWS SNS
- Cloud Watch
- HTTP Universal Connector

## Prerequisites

You must have the following:

- **In Amazon Web Services (AWS)**:
  - Permissions that allow you to create and modify IAM permissions policies
  - Permissions that allow you to create and modify IAM roles

## Select the scope of IAM External ID

1. Sign in to Workato.
   
2. Go to **Workspace admin > Settings > Amazon Web Services IAM**.
   
3. Use the **External ID scope** drop-down menu to select either **Single external ID for the workspace** or **Separate external ID for each project**.
   
   ![External scope for AWS access](/assets/secrets-management-aws-external-id-scope.DdWVuZbJ.png)_External scope_
   
   If you have existing connection credentials that use the workspace’s external ID, Workato prompts you to confirm your selection by displaying a list of active connections for which you must update the IAM roles. The reverse is true if you are switching from multiple project-level external ID's to a single external ID for the workspace.
   
   ![Confirm separate external IDs](/assets/secrets-management-aws-external-id-scope-confirm.CxmGbkXh.png)_Confirm external ID selection_
   
4. Click **Use separate external IDs** or **Use single external ID** to confirm your selection.
   

## Create an IAM role

To create an IAM role:

1. Navigate to the **AWS Console** and select **Security Credentials**.
   
   ![Security Credentials](/assets/security-credentials.-AMZzedD.png)_Security credentials_
   
2. Select **Roles > Create role**.
   
   ![Create role](/assets/create-role.CAwa2HEZ.png)_Create role_
   
3. Select **AWS account** under **Trusted entity type**.
   
4. Select **Another AWS account** and enter the **Workato AWS account ID**: `353360065216`.
   
5. Select the **Require external ID** check box and provide the Workato-generated **External ID**.
   
   - Every Workato user will have a unique **External ID** (for example, `workato-user-84762`). If you would like more granular control of how AWS is used in Workato, you may choose to configure the connection at the project level by changing the scope of the external ID. Refer to [secrets management](/en/security/data-protection/secrets-management/iam-role-based-authentication-for-aws) for more information.
   
   ![Amazon Account ID](/assets/aws-account.Du3fyxDX.png)_Amazon account ID_
   
   FIND YOUR WORKATO EXTERNAL ID
   
   To find the external ID in Workato:
   
   1. Sign in to Workato.
      
   2. Go to **Workspace admin > Settings > Amazon Web Services IAM**.
      
   
   If you have switched the scope of external IDs from workspace level to project level or vice versa, you are required to update the external IDs for the role in order for your AWS connection in Workato to be valid. You may do so by selecting "Trust relationships" and changing the value of the accepted external ID. For example, replacing the external ID value from `workato_iam_external_id_12345` to a project level scoped external ID like `workato_iam_external_id_12345_6789`.
   
6. Select appropriate permissions for Workato to run automated workflows in your account.
   
7. Provide a **Role name** and **Description** for the IAM role.
   
   - Workato recommends that role name avoids using a non-guessable `resource-id` in the ARN and does not include the external ID.
8. Optional. At the **Select trusted entities** step, click **Edit** to add or edit policies for trusted entities.
   
9. Optional. At the **Add permissions** step, click **Edit** to add or edit permissions.
   
10. Optional. If you are using object tags, select an appropriate tag for this IAM role.
    
    ![Review and create](/assets/name-review-create.D0pP8MDc.png)_Review and create role_
    
11. Click **Create role**.
    

## Create an IAM permissions policy

1. Navigate to the **AWS Console** and open the [IAM console](https://console.aws.amazon.com/iam).
   
2. Select **Access management > Policies**.
   
3. Click **Create Policy**.
   
4. Find and select the AWS service that you plan to allow Workato to access.
   
5. Select the necessary permissions in the **Actions** field.
   
6. Specify the resources to which you plan to allow the role access to.
   
   > **BEST PRACTICE**
   > 
   > Workato recommends that you grant access to specific resources. Refer to [Amazon's documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) for more info about using condition keys to accomplish granting minimal permissions.
   > 
   > The page should look similar to the following:
   > 
   > ![Configured IAM access policy in the AWS Create Policy screen](/assets/aws-sqs-trust-policy.D0Re2X5f.png)
   
7. Click **Next** until you reach the **Review policy** page.
   
8. Enter the **Name** for the policy.
   
9. Click **Create policy** when finished.
   

## Retrieve IAM role ARN

To retrieve the **Role ARN** required for the connection setup:

1. Navigate to the **AWS Console > My Security Credentials > Roles**.
   
   ![Security Credentials](/assets/security-credentials.-AMZzedD.png)_Security credentials_
   
2. Use the search box to locate the IAM role with ARN you plan to use for the connection and then select the role to view the summary.
   
   ![Select IAM role](/assets/select-iam-role.CkEg9D9j.png)_Select IAM role_
   
3. Copy the **Role ARN**. You must use this in the connection setup when creating an Amazon connection in Workato.
   
   ![Copy role ARN](/assets/copy-arn.DgXJ_K95.png)_Copy role ARN_
   

### Add the Role ARN in Workato

1. Sign in to Workato.
   
2. Go the **Connections** tab and click **Create > Connection** or press C twice.
   
3. Search for and select a [supported connector](#supported-connectors) on the **New connection** page.
   
4. Enter a name for your connection in the **Connection name** field.
   
5. Use the **Location** drop-down menu to select the project or folder where you plan to store the connection.
   
6. Select **IAM role** from the **Authorization type** drop-down menu.
   
7. Paste the ARN value in the **IAM Role ARN** field and complete any other required fields for the AWS service, for example **Region**.
   
   ![Add Role ARN to Workato](/assets/add-arn.DWHH2dy3.png)
   
8. Click **Connect**.
