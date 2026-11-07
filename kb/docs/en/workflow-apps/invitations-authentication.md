---
url: 'https://docs.workato.com/en/workflow-apps/invitations-authentication.md'
description: >-
  Learn how users are invited to Workflow apps and how they authenticate using
  passwords, SAML single sign-on, or just-in-time provisioning.
---

# Invitations and authentication

Unless you have configured the end-user portal for SAML authentication with [JIT (Just-in-time)](/en/user-accounts-and-teams/just-in-time-provisioning#jit-enable) provisioning enabled, a Workato Administrator must invite all users to the application through the Workato UI or programmatically using the [Invite user action](/en/workflow-apps/workflow-apps-connector/invite-user-action). Users do not require a Workato account to access published Workflow apps.

When you invite users through email, users must accept the invitation by following the link provided in the email. If you have set up password authentication for the user, the user must set their password at this time.

_Follow the link provided in the email_

Depending on the portal settings determined by the Workato Administrator, users can log into the portal by entering their password or logging in with their Identity Provider (Single Sign-On).

---
