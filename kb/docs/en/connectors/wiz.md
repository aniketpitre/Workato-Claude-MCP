---
url: 'https://docs.workato.com/en/connectors/wiz.md'
description: >-
  The Wiz connector enables you to automate cloud security workflows by
  retrieving records using the Wiz API.
---

# Wiz

[Wiz](https://www.wiz.io/) is a cloud security platform that provides visibility into risks across cloud infrastructure, applications, and workloads.

The Wiz connector enables you to automate security workflows by retrieving records from your Wiz account.

## Prerequisites

You must have the following to establish a Wiz connection in Workato:

- An active Wiz account.
- A registered OAuth client with Wiz.
- A client ID and client secret issued by Wiz.
- Your Wiz regional data center identifier (for example, `us1`, `us2`, `eu1`, `eu2`).

### Register a service account in Wiz

Complete the following steps to register a service account and retrieve your client credentials:

1. Sign in to the Wiz console using an account with appropriate permissions.
   
2. Click the **Settings** icon, then select **Service accounts** in the navigation menu.
   
3. Click **\+ Add Service Account**.
   
4. Enter a descriptive **Name** for the service account.
   
5. Optional. Select one or more **Projects** this service account can access.
   
6. Select the required permissions in the **API scopes** field. For integrations, select read-only scopes such as `read:projects` and `read:issues`.
   
7. Click **Add Service Account**.
   
8. Copy the **Client ID** and **Client secret**. You can only view these values once.
   
9. Store the credentials securely. You must enter these credentials in the connection setup in Workato.
   
10. Click **Finish**.
    

## How to connect to Wiz

Complete the following steps to create a Wiz connection:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Wiz` as your connection on the **New connection** page.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Connect to Wiz](/assets/connect-to-wiz.Dj2AV7Dd.png)_Connect to Wiz_
   
4. Use the **Location** drop-down menu to select the project or folder to store this connection.
   
5. Enter your Wiz **Client ID**.
   
6. Enter your Wiz **Client secret**.
   
7. Enter your **Tenant data center** identifier. For example: `us1`, `us2`, `eu1`, or `eu2`.
   
8. Select your **Environment** from the drop-down menu.
   
9. Click **Connect** to save and authorize the connection.

---
