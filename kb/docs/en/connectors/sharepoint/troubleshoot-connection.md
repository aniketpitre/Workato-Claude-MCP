---
url: 'https://docs.workato.com/en/connectors/sharepoint/troubleshoot-connection.md'
description: >-
  Use this guide to troubleshoot errors that occur when establishing a
  SharePoint connection in Workato.
---

# Troubleshoot SharePoint connection errors

Use this guide to troubleshoot errors that occur when establishing a SharePoint connection in Workato.

## 401 Unauthorized error

The `401 Unauthorized` error may occur when connecting to SharePoint in Workato. To resolve it, make sure to enter the client secret **Value**—not the **Secret ID**—in the **Client secret** field.

![SharePoint client secret ID](/assets/sharepoint-troubleshoot.DPBGyl4B.png)_The client secret ID and secret ID for your Sharepoint instance_

Refer to the [SharePoint](/en/connectors/sharepoint#client-creds) connector documentation for more information about registering the Workato app in the Azure Portal.

---
