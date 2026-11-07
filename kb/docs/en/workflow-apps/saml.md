---
url: 'https://docs.workato.com/en/workflow-apps/saml.md'
description: >-
  Learn how SAML-based single sign-on for the Workflow apps portal enhances
  security, supports JIT provisioning, and centralizes access.
---

# SAML-based single sign-on authentication

Enforcing SAML-based single sign-on (SSO) authentication for your [Workflow apps portal](/en/workflow-apps/portal-settings) enhances security and user experience.

With SAML SSO, a trusted identity provider (IdP) manages authentication, implementing robust security measures and reducing the risk of password-related breaches. Your organization can enforce SAML-based authentication to comply with internal security policies and regulatory requirements, ensuring only authorized users access sensitive Workflow apps.

SAML-based SSO also streamlines the user experience by allowing users to sign in once and access multiple applications without separate logins. Additionally, it allows centralized management of user identities and access controls through the IdP, ensuring consistent application of access policies.

![SSO sign in](/assets/sso-sign-in.B4dBsEbl.png)_Sign in to the Workflow apps portal through SAML-based SSO_

## Key features of SAML-based SSO for Workflow apps

SAML-based SSO for Workflow apps offers the following key features:

- Just-in-Time (JIT) Provisioning
  
- When SAML-based SSO is enforced, you can enable [JIT provisioning](/en/user-accounts-and-teams/just-in-time-provisioning) to automatically create user accounts in the Workflow apps portal when they first sign in through SSO. This eliminates the need for administrators to manually create accounts, which saves time and ensures that user information is current.
  
- Customizable attributes
  
- SAML-based SSO supports the inclusion of custom attributes, such as [group memberships](/en/workflow-apps/app-user-groups#organize-users-groups) and timeout duration, to tailor user experiences and access levels in your Workflow apps portal.
  
- Selective enforcement
  
- Your organization can choose to enforce SAML-based authentication for all users or only for specified domains. This flexibility allows for compliance with organizational policies while accommodating external users who may not have accounts with the identity provider.
  

## Compatible identity providers

Workflow apps supports SAML-based SSO with various identity providers (IdPs), including but not limited to:

- Google Workspace
- Microsoft Entra ID
- CyberArk Identity
- Okta
- OneLogin

## How it works

To enable SAML-based SSO authentication, your IdP and the Workflow apps portal must exchange SAML metadata. This involves setting up a SAML application in your IdP with specific values, such as the single sign-on URL and metadata URL. User group syncing does not take effect immediately upon configuration in Workato. Group syncing is enforced each time a user signs into the portal through their IdP.

The process of enabling SSO can vary based on your specific IdP. Refer to the following guides to learn how to enable this capability for a specific IdP. Each guide includes instructions for enabling user groups sync, which allows you to sync group assignments between the Workflow apps portal and your IdP.

- [Enforce SAML-based SSO authentication for Okta](/en/workflow-apps/saml-sso-okta)
- [Enforce SAML-based SSO authentication for Microsoft Entra ID](/en/workflow-apps/saml-sso-entra)

## Set up SAML-based authentication

Complete the following steps to set up SAML-based authentication for Workflow apps:

> **VIRTUAL PRIVATE WORKATO (VPW) CUSTOMERS**
> 
> This feature requires configuration steps that are specific to your Virtual Private Workato (VPW) instance. If you are a VPW customer, refer to your VPW private documentation for the configuration details for your instances.

> **NOT FOR WORKATO IDENTITY SAML-BASED SSO**
> 
> This documentation is specific to Workflow apps. Refer to [Workato Identity SAML-based SSO](/en/workato-identity/saml-sso) to configure SAML authentication for Workato Identity features, such as [Agent Studio](/en/agentic/agent-studio), [Workato GO](/en/agentic/workato-go), and [MCP](/en/mcp).

1. Sign in to your Workato account.
   
2. Go to **Platform > Workflow apps portal > Portal settings > Security**.
   
3. In the **Authentication method** field, select `SAML based SSO`.
   
   ![Workato SAML setup](/assets/workato-saml-setup._hTQes9j.png)_Workato SAML setup_
   
4. After you select `SAML based SSO`, the portal settings display the **Single Sign-On URL** and **Audience URI (SP Entity ID)**. Use these values to set up a SAML application in your IdP.
   
   The **Single Sign-On URL** and **Audience URI (SP Entity ID)** formats vary and are unique to your Workflow apps portal subdomain/domain and the data center in which your account is located.
   
   **Default domain URL formats**
   
   If you are using the default domain, the **Single Sign-On URL** follows this format:
   
   ```html
   https://{subdomain}.workato.app/portal/sso/saml/acs
   ```
   
   Where `{subdomain}` is your portal's subdomain.
   
   If you are using the default domain, the **Audience URI (SP Entity ID)** follows this format:
   
   ```html
   https://{subdomain}.workato.app/portal/sso/saml/metadata
   ```
   
   Where `{subdomain}` is your portal's subdomain.
   
   **Custom domain URL formats**
   
   If you are using a [custom domain](/en/workflow-apps/custom-domain-email-server), the **Single Sign-On URL** follows this format:
   
   ```html
   https://{custom-domain}/portal/sso/saml/acs
   ```
   
   Where `{custom-domain}` is your custom domain name.
   
   If you are using a [custom domain](/en/workflow-apps/custom-domain-email-server), the **Audience URI (SP Entity ID)** follows this format:
   
   ```html
   https://{custom-domain}/portal/sso/saml/metadata
   ```
   
   Where `{custom-domain}` is your custom domain name.
   
5. Provide metadata from your IdP. In the **Do you have your identity provider metadata URL** field, select `Yes` or `No`.
   
   **If you select yes**
   
   The steps to obtain the **Identity provider metadata URL** can vary depending on your identity provider. Refer to your IdP's documentation to learn how to obtain this value.
   
   1. Sign in to your IdP and locate your **Identity provider metadata URL**.
      
   2. Copy and paste this value into its corresponding field in Workato.
      
   
   **If you select no**
   
   The steps to obtain the **Single Sign On URL**, **Identity provider issuer**, and **x509 certificate** can vary depending on your IdP. Refer to your IdP's documentation to learn how to obtain these values.
   
   1. Sign in to your IdP and locate the **Single Sign On URL**, **Identity provider issuer**, and **x509 certificate**.
      
   2. Download the **x509 certificate**.
      
   3. Open the downloaded file in a text editor and verify that the certificate starts with `-----BEGIN CERTIFICATE-----` and ends with `-----END CERTIFICATE-----`.
      
   4. Copy the **Single Sign On URL**, **Identity provider issuer**, and **x509 certificate** and paste them into their corresponding fields in Workato.
      
   
6. In the **Enforce SAML authentication for** field, decide whether to enforce SAML authentication for all Workflow apps users or only specific domains.
   
   Users outside those domains can sign in using password authentication. This approach is useful for complying with organizational SSO policies while allowing external users without an identity provider account to access Workflow apps.
   
7. Optionally, click **Enable JIT (Just-In-Time) provisioning** to automatically add users to the portal after identity provider authentication.
   
   When JIT is enabled, any user signing in to Workato through SSO for the first time is automatically added to the portal.
   
8. Optionally, click **Enable user groups syncing** to sync user groups from your IdP. This step is mandatory if you plan to manage user groups through your IdP.
   
   _**User group syncing does not take effect immediately. Group syncing is enforced each time a user signs into the portal through their IdP.**_
   
   If you plan to enable user groups syncing
   
   1. Specify the following SAML attributes in your identity provider:
      
      |  | Name | Value |
      | --- | --- | --- |
      | Attribute 1 | `workato_app_user_name` | `user.displayName` |
      | Attribute 2 | `workato_app_user_groups` | `appuser.workato_app_user_groups` |
      
   
9. Optionally, customize the session duration for the Workflow apps portal by modifying the `SessionNotOnOrAfter` parameter in your identity provider. Otherwise, the default session timeout is seven days if you haven't enabled group syncing through your IdP. When group syncing is enabled through your IdP, the default session timeout is one day if you don't customize this parameter.
   
   Refer to your IdP's documentation to learn how to enable this capability for your app integration.
   
10. Click **Save changes**.

---
