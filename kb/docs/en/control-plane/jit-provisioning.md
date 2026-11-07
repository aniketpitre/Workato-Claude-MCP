---
url: 'https://docs.workato.com/en/control-plane/jit-provisioning.md'
description: >-
  Configure Just-in-Time (JIT) provisioning in Control plane to automatically
  create and manage user accounts when users first authenticate through
  SAML-based SSO.
---

# JIT provisioning

Just-in-Time (JIT) provisioning automatically creates user accounts when users first authenticate through SAML-based single sign-on. This eliminates the need for administrators to manually pre-create accounts and ensures user information stays current with your identity provider.

## Prerequisites

You must have the following configurations before you can enable JIT provisioning:

- A [configured SAML-SSO provider](/en/control-plane/authentication#set-up-a-saml-sso-provider) for Control plane

## Enable JIT provisioning

Complete the following steps to enable JIT provisioning:

> **NOT FOR WORKFLOW APPS SAML-BASED SSO**
> 
> This documentation is specific to Control plane. Refer to [SAML-based single sign-on authentication](/en/workflow-apps/saml) to configure SAML authentication for [Workflow apps](/en/workflow-apps).

1. Sign in to your Workato account.
   
2. Expand the workspaces menu.
   
3. Click **Control plane**.
   
4. Sign in using your Control plane credentials or SSO.
   
5. Go to **Control plane settings > Authentication**.
   
6. Go to the **Identity provider (IdP) for SAML SSO** section and click the provisioning **Setup now** link for the IdP where you plan to enable JIT.
   
   ![Click the provisioning Setup now link](/assets/setup-provisioning.ClymhkJA.png)_Click the provisioning **Setup now** link_
   
7. Click **JIT provisioning** in the **Provisioning** modal.
   
8. Click **Continue**.
   
9. Complete the JIT configuration setup.
   
10. Click **Done**.

---
