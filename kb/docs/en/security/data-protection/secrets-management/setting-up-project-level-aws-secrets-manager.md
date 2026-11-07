---
url: >-
  https://docs.workato.com/en/security/data-protection/secrets-management/setting-up-project-level-aws-secrets-manager.md
description: >-
  Set up AWS Secrets Manager at the project level to scope connection
  credentials and IAM roles to individual Workato projects.
---

# Set up AWS Secrets Manager for projects

As an alternative to an individual secret for each user, you can manage access at the level of the project.

You must change secrets manager settings so that connections in the project can use the specified role in the project settings. Customers can then create project-specific IAM roles to limit the use of secrets to connections within the project.

> **WARNING**
> 
> Switching to project-specific secrets management causes all previously configured external secrets references to stop working. Projects that use secrets stored in AWS Secrets Manager must be set up individually in Project settings.

> **INFO**
> 
> In the example used in this article, we chose to demonstrate a simple example of configuring the AWS external role ID **without** changing the IAM permissions policy.
> 
> If your organization requires different roles scoped to different access permissions, we recommend that you configure these new permissions by setting the scope to specific secret resources. This enables you to have more granular control over which connection credentials to use in each project.

After your AWS Secrets Manager successfully connects to Workato, you can start using [secrets when configuring connections](/en/security/data-protection/secrets-management/using-aws-secrets-in-connections).

* * *

## Prerequisites

To complete the steps in this guide, you must have the following:

- Permissions that allow you to create and modify IAM permissions policies
- Permissions that allow you to create and modify IAM roles

## Select the scope for secrets management

1. Sign in to Workato.
   
2. Go to **Workspace admin > Settings > External secrets manager**.
   
3. Click the **Use external secrets manager** toggle.
   
4. Select the **Set up secrets management for each project individually** option from the **Scope** drop-down menu.
   
   ![Workato secrets management, selecting project scope](/assets/secrets-management-scope-project.d-05a3me.png)
   
5. Click **Save**.
   
6. If you switch secrets management scopes, Workato notifies you that existing external secret references scoped to the project level will no longer function.
   
   To proceed with switching from workspace-level to project-level secrets management, select the checkbox to acknowledge the impact and click **Use project-specific secrets**.
   
   ![Workato secrets management, confirm project level](/assets/secrets-management-scope-project-confirm.Dnrb3Ljn.png)
   

Note that you must now set up secrets in each project individually.

## Select the project

1. Go to **Projects** and select the project that you plan to configure with secrets management.
   
2. Click **Settings**, then click **Secrets management**.
   
   ![Secrets management interface of a project](/assets/secrets-management-project-settings.Ci4qsd4F.png)
   
3. Click the **Use external secrets manager** toggle.
   
4. Select the **AWS Secrets Manager** option from the **Which secrets manager do you want to use?** drop-down menu.
   
5. Choose a guide for next steps in the process:
   
   - Create a new permission policy and role in AWS
   - Add the role to your Workato account
   
   ![Next steps in Workato](/assets/secrets-management-scope-project-guides.CncBZMXu.png)
   

## Select the AWS Account ID and external ID

1. In the **Create a new permission policy and role in AWS** guide detail, Workato displays the IAM details. Note them to use in the following steps:
   
   <dl><dt>AWS Account ID</dt><dd>Copy the <strong>AWS Account ID</strong> value, to use in ongoing configuration of the secrets manager.</dd><dt>External ID for ProjectName</dt><dd>Copy the value, to use in ongoing configuration of the secrets manager.</dd><dd>Here, we configure access to the project <strong>WorkatoDB_Project1</strong>.</dd><dd>The value should be of the form <code>workato_iam_external_id__</code>, where <code></code>is the ID of the Workato workspace, and <code></code>is the ID of the project.</dd></dl>
   
   ![ID values for AWS project secrets manager](/assets/secrets-management-scope-project-aws-ids.PZMTUT_q.png)
   

## Create an AWS IAM role for your Workato project

Refer to the [IAM role-based authentication for AWS](/en/security/data-protection/secrets-management/iam-role-based-authentication-for-aws) for instructions on how to create an IAM role for Workato and an IAM permissions policy (if needed).

## Retrieve and add the role ARN in Workato

You must complete the following steps to finalize the setup:

- [Step 5.1: Retrieve the role ARN in AWS](/en/security/data-protection/secrets-management/iam-role-based-authentication-for-aws#retrieve-iam-role-arn)
- [Step 5.2: Add the role ARN in Workato](/en/security/data-protection/secrets-management/iam-role-based-authentication-for-aws#add-the-role-arn-in-workato)
