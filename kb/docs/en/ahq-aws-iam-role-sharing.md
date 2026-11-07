---
url: 'https://docs.workato.com/en/ahq-aws-iam-role-sharing.md'
description: >-
  Enable AWS IAM role sharing in Automation HQ to propagate the admin
  environment external ID to child workspaces for easier IAM role management.
---

# AWS IAM role sharing

Use IAM external IDs to manage your IAM roles on AWS. You can enable AWS IAM role sharing from the AHQ admin settings to propagate the external ID of the AHQ admin environment to child workspace environments in multiple locations, AWS Secrets Manager, and all AWS connections that support an IAM role. This means that all child workspaces inherit the external ID of the parent workspace for a more convenient approach to managing IAM roles on AWS.

> **PARENT WORKSPACE PROJECT-LEVEL EXTERNAL ID SCOPE**
> 
> You can't change the scope of a parent IAM external ID to project level after you enable external ID sharing with child workspaces.

AWS IAM role sharing defaults to no. This means that each child workspace environment has a unique external ID that is generated automatically. You can simplify child workspace management by enabling external ID propagation.

> **CHILD WORKSPACE CONNECTIONS MUST BE RECONFIGURED**
> 
> Current child workspace connections are invalidated after you enable AWS IAM role sharing for AHQ. You must manually disconnect and then reconnect all child connections. You must call the `clear_cache` API to ensure that your dependent connections don't break if your child workspace connections were made using AWS Secrets Manager.

Some child workspaces may already use a project-level external ID. In this case, the child workspace displays an external ID with a project-level scope but applies the parent workspace's external ID.

## Enable AWS IAM role sharing for AHQ

Complete the following steps to enable AWS IAM role sharing:

1. Sign in to your Workato account.
   
2. Go to **Automation HQ > Settings**.
   
3. Click **AWS IAM role sharing**.
   
4. Click the **Use AHQ-level external ID for all managed workspaces** toggle.
   
   ![Use AHQ-level external ID for all managed workspaces](/assets/ahq-external-id-managed-workspaces.K58lcsY2.png)_**Use AHQ-level external ID for all managed workspaces** toggle_
   
5. Select the **Use AHQ-level external ID for all managed workspaces?** checkbox and click **Use AHQ-level external ID**. This confirms your understanding that all child workspace connections with workspace-level or project-specific external IDs in your managed workspaces will break and must be manually reconfigured.
   
   ![Use AHQ-level external ID for all managed workspaces? checkbox](/assets/ahq-external-id-checkbox.Ck97LSXQ.png)_**Use AHQ-level external ID for all managed workspaces?** checkbox_
   
6. Click **Save**.
   
7. Go to **Workspace admin > Settings**.
   
8. Locate the **Security** section in the sidebar and click **Amazon Web Services IAM**. The **Amazon Web Services (AWS) access** page displays. A green badge labeled **Managed by AHQ** appears next to your AWS account.
   
   ![Workspace admin AHQ managed](/assets/workspace-admin-aws-ahq-managed.BZ3njIep.png)_**Managed by AHQ** badge_
   

## Create an IAM role for AHQ

Refer to the [Use IAM role-based authentication for AWS Services](/en/security/data-protection/secrets-management/iam-role-based-authentication-for-aws#use-iam-role-based-authentication-for-aws-services) documentation for information on how to [create an IAM role](/en/security/data-protection/secrets-management/iam-role-based-authentication-for-aws#create-an-iam-role), [set the external ID scope](/en/security/data-protection/secrets-management/iam-role-based-authentication-for-aws#select-the-scope-of-iam-external-id), and complete other configuration steps for your AHQ workspace.

---
