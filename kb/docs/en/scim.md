---
url: 'https://docs.workato.com/en/scim.md'
description: >-
  Workato supports SCIM 2.0 to securely automate user provisioning,
  deprovisioning, and profile updates from identity providers like Okta and
  OneLogin.
---

# System for Cross-domain Identity Management (SCIM 2.0)

Workato supports the System for Cross-domain Identity Management (SCIM 2.0) in accordance with the [IETF SCIM specification](https://datatracker.ietf.org/doc/html/rfc7644), to manage user identity information. The implementation of the SCIM 2.0 protocol ensures that we securely automate the exchange of user identity data between your organization's identity provider and Workato. This enables automatic enterprise-level provisioning and deprovisioning of accounts and user profile management from your identity provider, such as [Okta](/en/scim-okta) or [OneLogin](/en/scim-onelogin).

> **FEATURE AVAILABILITY**
> 
> SCIM 2.0 is included in specific pricing plans. Refer to your pricing plan and contract to learn more.

> **SUMMARY**
> 
> - Workato supports SCIM 2.0 for automated user identity data exchange with identity providers like Okta, OneLogin, and Microsoft Entra ID.
> - SCIM 2.0 offers automatic user provisioning, deprovisioning, and updates to user attributes through your identity provider.
> - SCIM 2.0 usage requires its enablement in Workato and SAML SSO activation in your identity provider.
> - Using SCIM involves configuring it in Workato and your identity provider, managing users, and disabling SCIM when not needed.

SCIM 2.0 provides the following benefits to your organization:

- Automatically provisions users with Workato through your identity provider
- Updates custom user attributes, such as `workato_role`, directly from the identity provider
- Automatically de-provisions users from Workato through your identity provider
- Assigns users to collaborator groups through the `workato_user_groups` attribute

> **INFO**
> 
> SCIM support is an additional feature in Workato.

* * *

## Prerequisites

- **Enablement in Workato**: SCIM 2.0 is part of the **Data Monitoring/Advanced Security & Compliance** capability. Contact your account executive to learn more about using SCIM 2.0 in your organization.
- **Enablement in your identity provider**: SAML SSO Enabled on your identity provider

* * *

## Using SCIM

To use SCIM, follow these general steps:

1. [Configure SCIM in Workato](/en/scim-workato#configure-workato)
   
2. In the **Okta** identity provider:
   
   - [Configure SCIM in Okta](/en/scim-okta#configure-okta)
   - [Configure Workato roles](/en/scim-okta#configure-workato-role)
   - [Provision users](/en/scim-okta#provision)
   - [Convert user assignments to group](/en/scim-okta#convert-user-group)
   - [Update users](/en/scim-okta#update)
   - [Deprovision users](/en/scim-okta#deprovision)
   
   In the **OneLogin** identity provider:
   
   - [Configure for generic SAML applications](/en/scim-onelogin#generic)
   - [Configure SCIM in OneLogin](/en/scim-onelogin#configure-onelogin)
   - [Provision users](/en/scim-onelogin#provision)
   - [Update users](/en/scim-onelogin#update)
   - [Deprovision users](/en/scim-onelogin#deprovision)
   
   In the **Microsoft Entra ID** identity provider:
   
   - [Prerequisites](/en/scim-azure-ad#prerequisites)
   - [Step 1: Configure custom extension attributes](/en/scim-azure-ad#step-1-extension-attributes)
   - [Step 2: Configure automatic provisioning on Microsoft Entra ID](/en/scim-azure-ad#step-2-auto-provisioning)
   - [Step 3: Configure attribute mappings between Microsoft Entra ID and Workato](/en/scim-azure-ad#step-3-attribute-mappings)
   - [Step 4: Provision users](/en/scim-azure-ad#step-4-provision)
3. [Disable SCIM in Workato](/en/scim-workato#disable), in [Okta](/en/scim-okta#disable), in [OneLogin](/en/scim-onelogin#disable), or in [Microsoft Entra ID](/en/scim-azure-ad#disable)
   

## FAQ

- [What happens when SCIM is enabled and roles are updated manually on Workato?](#enable-manual-update)
- [What happens when SCIM is enabled and collaborators are removed manually from Workato?](#enable-remove-manual)
- [How can I turn off SCIM provisioning?](#turn-off)
- [How is deprovisioning handled on Workato with SCIM?](#deprovision-how)
- [Why is my profile name unexpectedly long?](#profile-name-length)

### What happens when SCIM is enabled and roles are updated manually on Workato?

Temporary role changes are overwritten from user profile data stored on Workato, the sync can happen in either scenarios:

- User logs in through SAML SSO: role changed by 'saml\_auto\_sync'
- User’s profile is updated from IdP: role change by 'scim\_auto\_sync'

### What happens when SCIM is enabled and collaborators are removed manually from Workato?

The user is re-provisioned back into the workspace on the next login, provided that the SCIM connection is valid and the user is not deprovisioned on the organization's identity provider.

### How can I turn off SCIM provisioning?

There are two approaches for turning off SCIM Provisioning:

- **Recommended**: In your identity provider, disable the SCIM configuration from your provisioning settings. Refer to individual identity provider steps for more detailed information: in [Okta](/en/scim-okta#disable), in [OneLogin](/en/scim-onelogin#disable), and in [Microsoft Entra ID](/en/scim-azure-ad#disable).
- In Workato, refresh your SCIM token value. This invalidates your existing provisioning token and subsequent SCIM calls fail. Refer to [Workato](/en/scim-workato#disable).

### How is deprovisioning handled on Workato with SCIM?

Workato handles deprovisioning in the same manner for users who are deactivated or temporarily suspended from the identity provider, or if their Workato app access is removed. All scenarios trigger a deprovisioning event on Workato, and the user is no longer able to access Workato workspaces. All of their recipes and connections remain accessible to other collaborators.

### Why is my profile name unexpectedly long?

When a user is provisioned in Workato through SCIM or Just-in-Time (JIT) provisioning, their account is created using the `userName` value provided by your identity provider. Workato then assigns a profile name using additional identity attributes.

If certain attributes are missing during provisioning, Workato may use `displayName` or `userName` as a fallback. These fields can include additional context such as job title or department, which may lead to unusually long profile names:

![SCIM long profile names](/assets/scim-long-profile-name.DN1q_xA_.png)_SCIM long profile names_

#### Why this matters

- A long profile name can cause issues when accessing features like Workato Academy, which enforce quotas on name length.
- Profile names aren't updated automatically after initial provisioning, even if SCIM mappings change.

#### How to resolve this

- Update your profile name manually in [Profile settings](/en/workspace#my-profile) in Workato.
- Check how your identity provider is sending name attributes during SCIM provisioning. Using broad fields like `displayName` can result in long names that may cause issues in the future.
- If needed, adjust your attribute mappings to send more concise values when users are provisioned.

---
