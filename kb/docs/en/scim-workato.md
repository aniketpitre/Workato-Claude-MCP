---
url: 'https://docs.workato.com/en/scim-workato.md'
description: >-
  Set up SCIM 2.0 in Workato by generating a SCIM token and base URL to connect
  your identity provider for automated user provisioning.
---

# Configure SCIM in Workato

The **SCIM Provisioning** page becomes available under **Workspace admin > Settings** after you enable SCIM for your workspace.

> **VIRTUAL PRIVATE WORKATO (VPW) CUSTOMERS**
> 
> This feature requires configuration steps that are specific to your Virtual Private Workato (VPW) instance. If you are a VPW customer, refer to your VPW private documentation for the configuration details for your instances.

* * *

## Prerequisites

Your organization must have the **Data Monitoring/Advanced Security & Compliance** capability to configure and use SCIM in Workato. Contact your Customer Success Representative to learn more about using SCIM 2.0 in your organization. Additionally, to complete the steps in this guide, you must have one of the following

- You are signed in with the root email address of the workspace
- You have the admin role
- You have a custom role with the **SCIM provisioning** privilege

* * *

Complete the following steps to configure SCIM 2.0 in Workato:

1. Go to **Workspace admin > Settings > Authentication > SCIM Provisioning**. ![SCIM provisioning](/assets/scim-provisioning-navigation.D5ctQTRE.png)_SCIM provisioning_
   
2. Click **Generate SCIM token** to generate the **SCIM token** and **Base URL**. ![Generate SCIM token](/assets/generate-scim-token.BoA_MjOH.png)_Generate SCIM token_
   
3. **Copy** the **SCIM token** and **Base URL** and save them for configuring SCIM in your identity provider.
   
   - **SCIM token**: The security token for configuring an automatic sync between your identity provider and Workato. The SCIM token in this example is obscured.
   - **Base URL**: The base URL of Workato's SCIM API endpoint. The base URL in this example is `https://workato.com/scim/v2`, but can vary based on the [data center](/en/datacenter/datacenter-overview) in which your workspace is located. For example, `https://app.eu.workato.com/scim/v2`. ![Supply Base URL and SCIM token from Workato](/assets/copy-url-and-scim-token.ByGe6vpP.png)_Supply Base URL and SCIM token from Workato_
4. Configure SCIM 2.0 in your identity provider:
   
   - [Configure SCIM 2.0 in Okta](/en/scim-okta)
   - [Configure SCIM 2.0 in OneLogin](/en/scim-onelogin)
   - [Configure SCIM 2.0 in Microsoft Entra ID](/en/scim-azure-ad)

## Disabling SCIM

Complete the following steps to invalidate the SCIM configuration by refreshing or revoking the SCIM token. To complete this task, you must be signed in with the root email address, have the **Environment admin** role, the legacy **Admin** collaborator role, or a custom role with the **SCIM provisioning** privilege.

1. In Workato, go to **Workspace admin > Settings > Authentication > SCIM Provisioning**.
   
2. **Refresh the SCIM token**
   
   1. Click **Refresh Token**. ![Click Refresh Token](/assets/refresh-scim-token.oROI8V6Y.png)_Click **Refresh Token**_
      
   2. Click **Refresh Token** in the **Are you sure?** modal to generate a new SCIM token and invalidate the previous token and configuration. ![Click Refresh Token](/assets/confirm-refresh-scim-token.ToXAem08.png)_Click **Refresh Token**_
      
   
   **Revoke the SCIM token**
   
   1. Click **Revoke token**. ![Click Revoke token](/assets/revoke-token-scim.vr2zW7Oj.png)_Click **Revoke token**_
      
   2. Click **Revoke** to invalidate the previous SCIM token and configuration. ![Click Revoke](/assets/confirm-revoke-scim-token.DoKtL_1b.png)_Click **Revoke**_
      
   

> **DISABLE SCIM EXTERNALLY**
> 
> You can also disable SCIM 2.0 externally through your identity provider:
> 
> - [Disable SCIM 2.0 in Okta](/en/scim-okta#disable)
> - [Disable SCIM 2.0 in OneLogin](/en/scim-onelogin#disable)
> - [Disable SCIM 2.0 in Microsoft Entra ID](/en/scim-azure-ad#disable)

---
