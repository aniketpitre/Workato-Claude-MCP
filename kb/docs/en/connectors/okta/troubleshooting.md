---
url: 'https://docs.workato.com/en/connectors/okta/troubleshooting.md'
description: >-
  Troubleshoot common Okta connection errors in Workato, including 302 Found,
  400 Bad Request, and 403 Forbidden OAuth 2.0 setup issues.
---

# Okta troubleshooting guide

Use this guide to troubleshoot Okta connection setup issues.

## Issue: 302 Found error

A 302 Found error can occur when establishing an OAuth 2.0 connection to Okta. This can happen if the value entered in the **Okta domain** field includes `-admin`, such as `mycompany-admin.okta.com`. This URL is used to access the Okta admin console and isn't a valid OAuth endpoint.

Complete the following steps to resolve this error:

1. Go to your Okta connection in Workato.
   
2. Review the **Okta domain** field to ensure that `-admin` isn't included in the domain.
   
3. Click **Connect**.
   

## Issue: 400 Bad Request error

A 400 Bad Request error can occur when establishing an OAuth 2.0 connection to Okta. This error can be caused by Demonstrating Proof-of-Possession (DPoP) for OAuth 2.0, which is now enabled by default for new app integrations in Okta. Disable DPoP for your Okta app integration to ensure successful connection.

Complete the following steps to resolve this error:

1. Sign in to your Okta Admin Console.
   
2. Go to **Applications > Applications** and select your app integration.
   
3. Go to **General > General Settings** and ensure the **Proof of possession** field is deselected.
   

## Issue: 403 Forbidden error

A 403 Forbidden error can occur when establishing a client credentials OAuth 2.0 connection to Okta, even when Okta logs show that an access token was successfully granted to your app integration. This error indicates that the app integration doesn't have sufficient permissions to call the Okta API.

This can mean that there is a mismatch between the scopes assigned in Workato and the scopes defined in Okta. It could also mean that your app integration lacks the `Read-only Administrator` role in Okta, which is required if your connection uses more than the [minimum required scopes](/en/connectors/okta#client-credentials-scopes).

Complete the following steps to resolve this error:

1. Go to **Applications > Applications** and select your app integration.
   
2. Verify assigned API Scopes
   
   1. Go to the **Okta API Scopes** tab.
      
   2. Go to **Consent > Granted**. Ensure that the granted scopes with the scopes specified in Workato on the connection setup page.
      
   3. Optional. Go to **Consent > Any** and add missing scopes as required.
      
   
3. Verify admin role assignments
   
   1. Go to the **Admin roles** tab and review the existing **Admin assignments granted to this app**.
      
   2. Click **Edit assignments** if `Read-only Administrator` or an applicable custom role is missing from the existing assignments.
      
   3. Use the **Roles** drop-down menu to select `Read-only Administrator`. Alternatively, select a custom role if you are assigning a custom role.
      
   4. Click **Save changes**.
      
   

Refer to the following resources for more information:

- [Okta Release Notes on DPoP](https://help.okta.com/en-us/content/topics/releasenotes/archive/oce-relnotes-2024.htm)
- [Configure OAuth 2.0 Demonstrating Proof-of-Possession](https://developer.okta.com/docs/guides/dpop/oktaresourceserver/main/)

---
