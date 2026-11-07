---
url: 'https://docs.workato.com/en/connectors/glean.md'
description: >-
  The Glean connector lets you automate enterprise search workflows: create,
  update, delete, search, and get records to power knowledge retrieval.
---

# Glean

[Glean](https://app.glean.com/) is an AI-driven platform that consolidates company data, personalizes information retrieval based on user context, and streamlines the search process to enhance productivity.

## Prerequisites

To connect to Glean in Workato, ensure you have the following:

- An active Glean instance
- Appropriate permissions to access Glean APIs. If you do not have a Glean account with the required permissions, contact your app administrator.

### Create an API Token

Complete the following steps to [create an API token](https://developers.glean.com/docs/client_api/client_api_scopes/#glean-issued-tokens) in the Glean admin console:

1. Sign in to Glean with an admin account.
   
2. Click on the wrench icon in the navigation bar to open the **Admin console**.
   
3. Go to **Setup** and select **API Tokens**.
   
4. Go to the **Client Tokens** or **Indexing tokens** tab, depending on which API you are using. This tab contains token metadata. The token itself isn't visible yet.
   
5. Click **Add New Token** to create a new token.
   
6. Define the token's **Description**, **Permissions**, **Scopes**, and **Expires** fields, then click **Save**. ![The Glean token's definition fields](/assets/glean-key.jmDotUoU.png)_The Glean token's definition fields_
   
7. Copy and save the token for use in Workato. The newly created token is only visible once after its creation and you can't retrieve it later.
   

## Connection Setup

Workato supports the following authentication methods to connect to Glean:

- [Client API Token](#client-token)
- [Indexing API Token](#indexing-token)

### Client API Token

1. Click **Create > Connection** or press C twice.
   
2. Search for and select **Glean** as your connection in the **New connection** page.
   
3. Provide a name for your connection in the **Connection name** field. ![Glean connection fields](/assets/glean-client-token.CbMiEZOI.png)_Glean connection fields_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter the **Client API Token** for your Glean account.
   
6. Enter the **Subdomain** for your Glean account.
   
7. Click **Connect**.
   

### Indexing API Token

1. Click **Create > Connection** or press C twice.
   
2. Search for and select **Glean** as your connection in the **New connection** page.
   
3. Provide a name for your connection in the **Connection name** field. ![Glean connection fields](/assets/glean-indexing-token.BjdExtrz.png)_Glean connection fields_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter the **Indexing API Token** for your Glean account.
   
6. Enter the **Subdomain** for your Glean account.
   
7. Enter the **Data source** of your Glean account.
   
8. Enter the **Username** of your Glean account. If you are using a global token, enter the email address of the associated user.
   
9. Click **Connect**.
   

## Actions

The Glean connector supports the following actions:

- [Create record](/en/connectors/glean/create-record-action)
- [Delete record](/en/connectors/glean/delete-record-action)
- [Execute operation](/en/connectors/glean/execute-operation-action)
- [Get record details by ID](/en/connectors/glean/get-record-details-by-id-action)
- [Search records](/en/connectors/glean/search-records-action)
- [Update record](/en/connectors/glean/update-record-action)

![Glean Actions](/assets/glean-actions.DqZGs8_M.png)_Glean Actions_

---
