---
url: 'https://docs.workato.com/en/connectors/conga.md'
description: >-
  The Conga connector lets you automate document workflows: create, update,
  search, and query records, generate and download documents, and send email.
---

# Conga

[Conga](https://conga.com/) is a platform for contract lifecycle management and document automation. Conga lets you streamline, automate, and optimize commercial operations. Conga provides end-to-end capabilities for generating documents, managing contracts, enabling eSignatures, and supporting revenue lifecycle processes.

This connector has the following capabilities:

- Create records such as contacts, contracts, proposals, accounts, opportunities, and line items.
- Retrieve and list data from Conga for objects including accounts, cart line items, contracts, contacts, opportunities, product configurations, price lists, document information, document metadata, and documents as PDF.
- Query records for key entities such as accounts, contacts, documents, and opportunities.
- Update records including accounts, contacts, contracts, and opportunities.
- Generate documents using Conga templates and automation capabilities.
- Download documents for further processing or archival.
- Send emails directly through Conga workflows.

## Prerequisites

To establish a connection to Conga, you must have the following:

- Client ID
- Client secret
- User ID
- Token URI
- Base URI

## How to connect to Conga

Workato supports [API to API authentication](#authentication-api) connections to Conga.

### API to API connection authentication

API to API connection authentication consists of the following steps:

- [Create an API to API connection](#create-api-connection)
- [Complete setup in Workato](#complete-setup-api)

> **ADMINISTRATOR ACCESS REQUIRED**
> 
> This authentication method requires administrator access in your Conga account.

#### Create an API to API connection

Complete the following steps to set up API to API Conga authentication:

1. Log into your Conga account.
   
2. Click the **App Launcher** icon from the top-left corner of the Conga platform.
   
3. Click **Admin Console > Organization**.
   
4. Click the **Conga API Connections** tab.
   
5. Click **API to API Connection**.
   
6. Enter values for the fields on the **API to API Connection** screen.
   
   Refer to the [Conga documentation](https://documentation.conga.com/en/advantage-platform-administration/current/conga-advantage-platform-for-administrators/organization-management/conga-api-connections) for descriptions of each field.
   
7. Click **Save & Generate Client Secret** to generate the Client ID and Client Secret.
   
8. Copy the **Client ID** and **Client Secret**.
   
   > **Regenerate Client secret**
   > 
   > You cannot recover the **Client Secret** after copying. You must regenerate the **Client Secret** instead.
   > 
   > Regenerate the client secret by clicking **External Identifier > Save & Regenerate Client Secret**. After regenerating the **Client Secret**, you must update the secret in all your connected API solutions.
   

Return to Workato to finish setting up your connection.

#### Complete setup in Workato

Complete the following steps to set up the Conga connection in Workato.

1. Click **Create > Connection** or press C twice.
   
   ![Conga connection](/assets/conga-connection-setup.DQa5xruO.png)_Create your Conga connection_
   
2. Search for and select `Conga` as your connection in the **New connection** page.
   
3. Provide a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter the Conga **Client ID**.
   
6. Enter the Conga **Client secret**.
   
7. Enter the Conga **User ID**.
   
8. Enter the Conga **Token URI**.
   
9. Enter the Conga **Base URI**.
   
10. Click **Connect**.

---
