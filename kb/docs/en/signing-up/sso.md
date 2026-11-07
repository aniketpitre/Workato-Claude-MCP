---
url: 'https://docs.workato.com/en/signing-up/sso.md'
description: >-
  Learn how single sign-on works in Workato using SAML 2.0 with identity
  providers such as Google Workspace, Microsoft Entra ID, and Okta.
---

# Single Sign-On (SSO)

Single sign-on allows users to use a single set of credentials, like a username and password, to log in to multiple applications. This simplifies password management and enhances security when two-factor authentication or SAML SSO is configured. Security Assertion Markup Language (SAML) is a security standard for managing authentication and access.

![SAML-based SSO configuration](/assets/sso-config.DOt2LjvL.png)_SAML-based SSO configuration_

Workato supports SAML-based single sign-on with various identity providers (IdPs), including:

- Google Workspace
- Microsoft Entra ID
- CyberArk Identity
- Okta
- OneLogin

When using SAML SSO, users sign in to their Workato workspace through their organization's identity provider.

> **DEPRECATION NOTICE**
> 
> OAuth SSO is set for deprecation. We recommend configuring **2FA** or **SAML SSO** as your authentication method to enhance account security. SAML-based SSO supports JIT provisioning and SSO from your organization's IdP.

#### OAuth SSO providers scheduled for deprecation

- Google
- Office 365
- Wrike
- Salesforce

![OAuth SSO](/assets/saml-oauth-sso.CDVkkHw0.png)_OAuth SSO providers_

For more details on setting up SAML SSO, including JIT provisioning, visit [SAML SSO setup](/en/user-accounts-and-teams/single-sign-on).

---
