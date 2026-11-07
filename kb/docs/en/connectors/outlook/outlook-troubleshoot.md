---
url: 'https://docs.workato.com/en/connectors/outlook/outlook-troubleshoot.md'
description: >-
  Troubleshoot the admin consent prompt that can appear when you connect the
  Outlook connector in Workato with a non-admin account.
---

# Outlook - Troubleshooting

Use this guide to troubleshoot issues when you connect to Outlook through the Workato Outlook connector.

## Prompted for admin consent when connecting to Outlook

You may see a `Need admin approval` message when you connect to Outlook using a service account.

### Why it happens

This issue occurs when the Outlook connection uses a non-admin account that hasn't received tenant-wide admin consent for the Workato enterprise application in the Azure portal. Manual consent attempts, such as constructing an admin consent URL, don't apply the required permissions. The connection fails with a `Need admin approval` or `Workato OAuth authorization failed` message when tenant-wide admin consent isn't granted in the Azure portal, because Workato's Microsoft Graph scopes require approval from a Microsoft 365 administrator.

### How to troubleshoot

Complete the following steps to grant admin consent correctly:

1. Sign in to the Azure portal with an admin account.
   
2. Go to **Azure portal > Enterprise applications**.
   
3. Locate the Workato enterprise application using the **Client ID**.
   
4. Open the **Workato** application and select **Permissions** from the left menu.
   
5. Review the list of Microsoft Graph API permissions. Confirm that each permission matches the required Outlook scopes.
   
6. Click **Grant admin consent for \[Tenant name\]** to approve access on behalf of your organization.
   
7. Return to Workato and reconnect to Outlook. The connection completes without another admin approval prompt.
   

When the consent is granted correctly, the **Permissions** page for the Workato enterprise application lists the Microsoft Graph APIs with the updated status.

![Grant admin consent for Workato in Microsoft Entra ID](/assets/grant-admin-consent.D6_XPdGV.png)_Grant admin consent for Workato in Microsoft Entra ID_

---
