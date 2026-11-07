---
url: 'https://docs.workato.com/en/user-accounts-and-teams/troubleshoot-sso.md'
description: >-
  Troubleshoot common SAML-based Single Sign-On errors in Workato, including
  workspace switching, login, and case-sensitive username issues.
---

# Troubleshoot Single Sign-On

Use this guide to troubleshoot errors that occur when you use Single Sign-On (SSO) in Workato.

## Unable to switch workspace error message

You may encounter the following error message if you are a **workspace account owner** attempting to access the workspace using SAML-based SSO:

```text
Unable to switch workspace: the user doesn't belong to the workspace
```

This message means that you can't authenticate with Workato using SAML-based SSO because you are the workspace account owner. You must sign in to the workspace using your username and password instead of using SAML-based SSO.

## Unable to log in: the user doesn't belong to the Team

You may encounter the following error message when attempting to log in using SAML-based SSO:

```text
Unable to login: the user doesn't belong to the Team
```

This error occurs when a **workspace account owner** attempts to authenticate using SAML-based SSO. Workspace account owners must authenticate using their username and password instead of SAML-based SSO.

## Unable to log in error message

You may encounter the following error message when attempting to log in with SAML-based SSO:

```
Unable to log in: Email invited user is already a member
```

This error typically occurs when a user was provisioned through SAML Just-In-Time (JIT) provisioning or SCIM, removed, and then tries to log in again using SAML SSO. Workato's backend is case-sensitive and automatically converts usernames to lowercase.

You must update the SAML configuration on your identity provider (IdP) to convert email addresses to lowercase to fix this issue. This ensures that your IdP format matches the format in Workato's backend. For example, in Okta, use the expression `toLowerCase(user.email)`. In Microsoft Entra ID, apply the `ToLower()` function to the `user.mail` attribute.

## SAML issuer and SP issuer should be unique

You may receive a `SAML issuer and SP issuer should be unique` error message when you enable SSO for multiple workspaces in Workato. This error occurs because at least one workspace already has the same Identity Provider (IdP) and Service Provider (SP) Entity ID registered.

Complete the following troubleshooting steps to resolve this error:

1. Create a SAML SSO app on your identity provider platform for each workspace.
   
2. Select **Other SAML IdP** from the **SAML provider** menu to generate a unique Entity ID for each workspace.
   
3. Enter the Workspace handle.
   
4. Enter the Metadata URL.
   
5. Click **Save**.
   
6. Change the SAML provider to the identity provider you plan to use.
   
7. Click **Save**. The Entity ID is fixed and can't be changed after you click **Save**.

---
