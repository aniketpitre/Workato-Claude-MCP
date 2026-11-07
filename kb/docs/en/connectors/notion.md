---
url: 'https://docs.workato.com/en/connectors/notion.md'
description: >-
  The Notion connector lets you automate workflows: create, update, search, and
  get records, query databases, and trigger on new or updated database records.
---

# Notion

[Notion](https://www.notion.com/) is a project management and note-taking platform that enables you to create databases, manage projects, take notes, and leverage AI to improve your workflows.

## API version

The Notion connector uses the [Notion REST API](https://developers.notion.com/reference/intro).

## Connection setup

The Notion connector supports the following authentication types:

- [OAuth 2.0](#oauth2)
- [API key](#api-key)

### Download the Notion connector from the community library

View steps to download the Notion connector from the community library

Complete the following steps to install the Notion connector from the [community library](https://www.workato.com/browse/connectors):

1. Open the recipe editor and search for a connector. Alternatively, you can search for a connector in the [community library](https://www.workato.com/browse/connectors).
   
   ![Search for recipe editor](/assets/search-on-recipe-editor.VrZpf8zl.png)_Search for community connectors in the recipe editor_
   
2. Select the community connector you plan to install.
   
3. Click **Install** to install the connector from the community library.
   
   ![Click install](/assets/install-connector.BXpGZP9K.png)_Click **Install**_
   
4. Select **Release connector**. Alternatively, select **Review code** to review and modify the connector code before releasing it to the workspace.
   
   ![Release connector](/assets/release-and-review.kWToLwmF.png)_Release the connector_
   
5. Summarize any changes you made to the connector, then click **Release** to allow workspace collaborators to use the connector in recipes.
   
   ![The Confirm release dialog](/assets/release.CpEhhA-6.png)_The **Confirm release** dialog_
   

### OAuth 2.0 authentication

Use OAuth 2.0 to create a public integration that accesses multiple Notion workspaces.

Complete the following steps to set up an OAuth 2.0 connection to Notion in Workato:

- [Generate a client ID and client secret](#generate-client-id-and-secret)
- [Connect to Notion with OAuth 2.0](#oauth2-connect)

#### Generate a client ID and client secret

Complete the following steps to generate a client ID and client secret in Notion:

1. Sign in to the Notion [Integrations Dashboard](https://www.notion.so/profile).
   
2. Click **Integrations** under **Listings**.
   
3. Click **\+ Create a new integration**.
   
4. Enter an **Integration name**.
   
5. Upload an icon to identify the integration.
   
6. Use the **Associated workspace** drop-down menu to scope the connection to a specific workspace.
   
7. Enter `https://www.workato.com/oauth/callback` in the **Redirect URIs** field.
   
8. Click **Create**.
   
9. Click **Configure integration settings** in the modal that appears.
   
10. Copy and save the **OAuth Client ID** and **OAuth Client Secret** for use in Workato.
    
    > **SAVE YOUR CREDENTIALS**
    > 
    > The client secret is only displayed once. If you lose it, you must refresh it or create a new integration.
    

#### Connect to Notion with OAuth 2.0 authentication

Complete the following steps to set up an OAuth 2.0 connection to Notion in Workato:

1. Click **Create > Connection**.
   
2. Search for `Notion` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Notion Connection](/assets/notion-oauth-connection.C_1sdhTh.png)_Notion Connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authentication type** drop-down menu to select **OAuth (Public integration)**.
   
6. Use the **API version** drop-down menu to select the API version.
   
7. Enter the **Client ID** and **Client secret** for your Notion integration. Refer to [Generate a client ID and client secret](#generate-client-id-and-secret) to obtain these values.
   
8. Click **Connect**.
   

### API key authentication

Use an API key authentication to create an internal integration accessible only in a specific Notion workspace.

Complete the following steps to set up an API key connection to Notion in Workato:

- [Generate an integration token](#generate-integration-token)
- [Connect to Notion with API key](#api-key-connect)

#### Generate an integration token

1. Sign in to the Notion [Integrations Dashboard](https://www.notion.so/profile/integrations/public).
   
2. Select **Internal integrations**.
   
3. Select **Create a new integration**.
   
4. Enter an **Integration name**.
   
5. Upload an icon to identify the integration.
   
6. Use the **Associated workspace** drop-down menu to scope the connection to a specific workspace.
   
7. Click **Create**.
   
8. Click **Configure integration settings** in the modal that appears.
   
9. Copy and save the **Internal integration secret** for use in Workato.
   

#### Connect to Notion with API key authentication

Complete the following steps to set up an API key connection to Notion in Workato:

1. Click **Create > Connection**.
   
2. Search for `Notion` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Notion Connection](/assets/notion-api-key-connection.CLHmNdWd.png)_Notion Connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authentication type** drop-down menu to select **API Key (Internal integration)**.
   
6. Use the **API version** drop-down menu to select the API version.
   
7. Enter the **Integration Token** for your Notion integration. Refer to [Generate an integration token](#generate-integration-token) to obtain this value.
   
8. Click **Connect**.

---

---
url: >-
  https://docs.workato.com/en/connectors/notion/new-or-updated-database-record-trigger.md
description: >-
  The New/updated database record trigger in the Notion connector fires when a
  record is created or updated in the database you monitor.
---

# Notion - New/updated database record trigger

The **New/updated database record** trigger monitors a Notion database for new or updated records.

## Input

| Field | Description |
| --- | --- |
| Trigger poll interval | Specify how frequently to check for new events. |
| Database | Select the database to monitor. |
| When first started, this recipe should pick up events from | Set the date and time to start picking up trigger events. This enables your recipe to capture past events. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

## Output

| Field | Description |
| --- | --- |
| Object | The type of object created or updated. |
| Page ID | The unique identifier of the associated page. |
| Created time | The timestamp when the record was created. |
| Last edited time | The timestamp when the record was last updated. |
| Created by | Contains information about the user who created the record, such as their `User ID` and the `Object` type. |
| Last edited by | Contains information about the user who last updated the record, such as their `User ID` and the `Object` type. |
| Icon | Contains information about the new or updated record's icon, such as its `Type` and associated `Emoji`. |
| Parent | Contains information about the new or updated record's parent, such as its `Type` and `ID`. |
| Archived | Indicates whether the database is archived. |
| In trash | Indicates whether the record is in Notion's trash folder. |
| Properties | Contains information about the new or updated record's properties, such as its `Title`, `Type`, and `ID`. |
| URL | The new or updated record's URL. |

---
