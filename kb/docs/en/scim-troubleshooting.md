---
url: 'https://docs.workato.com/en/scim-troubleshooting.md'
description: >-
  Use this guide to troubleshoot errors that occur when using System for
  Cross-domain Identity Management (SCIM) provisioning in Workato.
---

# SCIM troubleshooting

Use this guide to troubleshoot errors that occur when using System for Cross-domain Identity Management (SCIM) provisioning in Workato.

## UserName has already been taken error

You may encounter the `userName has already been taken` error message when you enable SCIM provisioning for a user. This happens because the user was already registered on the workspace with a different method, or the user exists on the platform, but confirmation of the invitation is required.

Follow these troubleshooting methods to resolve the issue:

1. Remove the collaborator from the workspace.
   
2. Enable SCIM provisioning again.
   
3. Wait until the user accepts the SCIM invitation.
   
4. Confirm that the user was added and has access to the workspace.

---
