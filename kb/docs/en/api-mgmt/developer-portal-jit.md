---
url: 'https://docs.workato.com/en/api-mgmt/developer-portal-jit.md'
description: >-
  Configure JIT user settings to set the authentication method and policy for
  API clients created when users log in to the developer portal via SSO.
---

# JIT user settings

JIT user settings define the authentication method and policy applied to API clients created through JIT provisioning. When a Workato Identity end user logs in through SSO for the first time, Workato Identity creates the end user record, and then the portal creates an API client for that user using these settings.

JIT users land on the **Discover new APIs** page on first login with no collection access. They can browse available collections and submit access requests, which an admin must approve before they can interact with any APIs.

## Prerequisites

Complete the following before configuring JIT user settings:

1. [Configure SAML-based authentication](/en/workato-identity/saml-sso#configure-saml-based-authentication) in your workspace through Workato Identity, then follow your IdP-specific guide: [Okta](/en/workato-identity/identity-provider-user-access), [Google Workspace](/en/workato-identity/google-workspace-saml-configuration), [Microsoft Entra ID](/en/workato-identity/microsoft-entra-id-saml-configuration), or [OneLogin](/en/workato-identity/onelogin-saml-configuration).
2. [Enable JIT provisioning](/en/workato-identity/jit-provisioning#enable-jit-provisioning) in your SAML SSO configuration. This allows Workato Identity to automatically create end user records when users first authenticate through SSO.

> **END-USER GROUPS**
> 
> Create [end-user groups](/en/workato-identity/user-groups) before configuring JIT user settings if you plan to assign JIT-provisioned clients to specific groups.

## Configure JIT user settings

Complete the following steps to configure JIT user settings for the developer portal:

1. Go to **Platform > API platform > Settings > Developer Portal > JIT user settings**.
   
   ![JIT user settings](/assets/jit-user-settings.B1VOu0cp.png)_JIT user settings — not yet configured_
   
2. Select an authentication method from the **Authentication method** drop-down menu. This applies to all clients provisioned through JIT.
   
   > **AUTHENTICATION METHOD**
   > 
   > You cannot change the authentication method after a client is created. Refer to [available authentication methods](/en/api-mgmt/access-tokens) for more information.
   
3. Optional. Select a policy from the **Policy** drop-down menu to govern API usage for JIT-provisioned clients. Go to the **Policies** tab to create a policy first if needed, then refresh the drop-down menu.
   
4. Click **Save**.
   
   > **BEFORE DIRECTING USERS**
   > 
   > JIT user settings must be saved before end users can log in to the portal. Complete these settings before directing users to the portal.

---
