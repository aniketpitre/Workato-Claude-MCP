---
url: 'https://docs.workato.com/en/control-plane/scim-provisioning.md'
description: >-
  Configure SCIM provisioning in Control plane to automatically sync users and
  groups from your IdP.
---

# SCIM provisioning

SCIM (System for Cross-domain Identity Management) provisioning automatically synchronizes user accounts and groups between your identity provider and Workato Control plane. This eliminates the need for administrators to manually create or update accounts, and allows you to manage Workato Control plane users and groups entirely from your existing identity provider.

## Prerequisites

You must have the following configurations before you can enable SCIM provisioning:

- A [configured SAML-SSO provider](/en/control-plane/authentication#set-up-a-saml-sso-provider) for Control plane

## Enable SCIM provisioning

Complete the following steps to enable SCIM provisioning:

> **NOT FOR WORKFLOW APPS SAML-BASED SSO**
> 
> This documentation is specific to Control plane. Refer to [SAML-based single sign-on authentication](/en/workflow-apps/saml) to configure SAML authentication for [Workflow apps](/en/workflow-apps).

1. Sign in to your Workato account.
   
2. Expand the workspaces menu.
   
3. Click **Control plane**.
   
4. Sign in using your Control plane credentials or SSO.
   
5. Go to **Control plane settings > Authentication**.
   
6. Go to the **Identity provider (IdP) for SAML SSO** section and click the provisioning **Setup now** link for the IdP where you plan to enable SCIM.
   
7. Click **SCIM provisioning** in the **Provisioning** modal.
   
8. Click **Continue**.
   
9. Copy the **Base URL** and **SCIM token** values in the **Get your SCIM credentials** modal. Store the token securely. You won’t be able to view it again. You must re-generate the token if you lose it.
   
10. Click **Done**.
    
11. Refer to the following IdP resources for IdP-specific SCIM provisioning configuration information and examples:
    
    - [SCIM provisioning in Okta](https://help.okta.com/en-us/content/topics/apps/apps_app_integration_wizard_scim.htm)
    - [SCIM provisioning in Microsoft Entra ID (Azure Active Directory)](https://learn.microsoft.com/en-us/entra/identity/app-provisioning/use-scim-to-provision-users-and-groups#getting-started)
    - [SCIM provisioning in OneLogin](https://developers.onelogin.com/scim/define-user-schema)

## Rotate SCIM token

You can rotate your SCIM token in Control plane.

Complete the following steps to rotate your SCIM token:

1. Go to **Enterprise controls** and click **Control plane**.
   
2. Sign in using your Control plane credentials or SSO.
   
3. Go to **Settings > Authentication**.
   
4. Go to the **Identity provider (IdP) for SAML SSO** section and click the **...** (ellipsis) option menu of the IdP with SCIM token you plan to rotate.
   
5. Click **Provisioning** to open the **Provisioning** modal.
   
6. Click **Rotate**.
   
   ![Click Rotate](/assets/rotate-scim.CjhHT2Xb.png)_Click **Rotate**_
   
7. Click **Save changes**.

---
