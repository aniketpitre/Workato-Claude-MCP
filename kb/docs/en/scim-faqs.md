---
url: 'https://docs.workato.com/en/scim-faqs.md'
description: >-
  Answers to common questions about using SCIM 2.0 with Workato, including
  benefits, prerequisites, provisioning, and supported features.
---

# SCIM FAQs

Get answers to frequently asked questions (FAQs) about System for Cross-domain Identity Management (SCIM).

What is SCIM 2.0, and how does Workato support it?

[SCIM 2.0](/en/scim#overview) (System for Cross-domain Identity Management) is a protocol for automating the exchange of user identity data between identity providers and Workato. Workato supports SCIM 2.0 in compliance with the IETF SCIM specification. This enables secure automation of user identity data exchange between your organization's identity provider and Workato. SCIM also facilitates automatic provisioning, deprovisioning, and user profile management.

What are the benefits of using SCIM 2.0 with Workato for my organization?

SCIM 2.0 provides the following [benefits](/en/scim#overview):

- Automatic provisioning of users in Workato through your identity provider
- Updates to custom user attributes, such as `workato_role`, directly from your identity provider
- Automatic deprovisioning of users from Workato through your identity provider
- Assigns users to collaborator groups through the `workato_user_groups` attribute

Is SCIM support included in Workato, or is it an additional feature?

[SCIM support](/en/scim#overview) is an additional feature in Workato. You must have the **Data Monitoring/Advanced Security & Compliance** capability to use SCIM. Contact your customer support representative to learn more about using SCIM 2.0 in your organization.

What are the prerequisites for using SCIM 2.0 with Workato?

To use SCIM 2.0 with Workato, you must meet the following [prerequisites](/en/scim#prerequisites):

- **Enablement in Workato**: SCIM 2.0 is part of the Data Monitoring/Advanced Security & Compliance capability. Contact your account executive to learn more.
  
- **Enablement in your identity provider**: Ensure that SAML SSO is enabled on your identity provider.
  

What happens when SCIM is enabled, and roles are updated manually on Workato?

When [SCIM is enabled](/en/scim#enable-manual-update), temporary role changes made manually on Workato may be overwritten during synchronization. Role changes can occur when a user logs in through SAML (`saml_auto_sync`) or when a user's profile is updated from the Identity Provider (`scim_auto_sync`).

What happens when SCIM is enabled, and collaborators are removed manually from Workato?

If [collaborators are manually removed](/en/scim#enable-remove-manual) from Workato but SCIM is enabled and the SCIM connection is valid, the user will be re-provisioned into the workspace the next time they log in to Workato, provided they have not been deprovisioned in the organization's identity provider.

How can I turn off SCIM provisioning?

You must do one of the following to [disable SCIM provisioning](/en/scim#turn-off):

- Disable the SCIM configuration in your identity provider's provisioning settings (recommended).
  
- Refresh your SCIM token value in Workato. This invalidates the existing provisioning token, and causes subsequent SCIM calls to fail.

---
