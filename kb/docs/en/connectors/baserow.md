---
url: 'https://docs.workato.com/en/connectors/baserow.md'
description: >-
  Connect Baserow to Workato to create, update, search, and delete table rows,
  and trigger recipes when rows change.
---

# Baserow

[Baserow](https://baserow.io) is an open-source no-code database. The Baserow connector lets you create, update, search, and delete table rows, list tables and fields, and trigger recipes when rows change.

Use the Baserow connector to:

- Create, update, search, get, or delete rows in a Baserow table.
- Batch-update up to 200 rows in one request.
- List the tables and fields in your Baserow database.
- Trigger a recipe when a row is created, updated, or deleted.

You can also use [custom actions](/en/developing-connectors/custom-actions) to build a custom HTTP request to any Baserow API endpoint. Refer to the Baserow [Database API](https://baserow.io/docs/apis/rest-api) documentation for endpoint details.

## Install Baserow from the community library

Complete the following steps to install the Baserow connector from the [community library](https://www.workato.com/browse/connectors):

1. Open the recipe editor and search for a connector. Alternatively, you can search for a connector in the [community library](https://www.workato.com/browse/connectors).
   
   ![Search for recipe editor](/assets/search-on-recipe-editor.VrZpf8zl.png)_Search for community connectors in the recipe editor_
   
2. Select the community connector you plan to install.
   
3. Click **Install** to install the connector from the community library.
   
   ![Click install](/assets/install-connector.BXpGZP9K.png)_Click **Install**_
   
4. Select **Release connector**. Alternatively, select **Review code** to review and modify the connector code before releasing it to the workspace.
   
   ![Release connector](/assets/release-and-review.kWToLwmF.png)_Release the connector_
   
5. Summarize any changes you made to the connector, then click **Release** to allow workspace collaborators to use the connector in recipes.
   
   ![The Confirm release dialog](/assets/release.CpEhhA-6.png)_The **Confirm release** dialog_
   

## Connection setup

The Baserow connector uses a database token for authentication.

### Baserow setup for database token authentication

Complete the following steps to create a Baserow database token:

1. Sign in to your [Baserow](https://baserow.io) account.
   
2. Select your workspace name in the sidebar or the workspace drop-down menu.
   
3. Go to **Settings > Database tokens**.
   
4. Click **Create token +**.
   
5. Enter a descriptive name, for example `Workato integration`.
   
6. Select the target workspace.
   
7. Click **Create token**.
   
8. Save the token for use in Workato.
   

### Connect to Baserow with database token authentication

Complete the following steps to set up a Baserow connection in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Baserow` and select it as your app.
   
3. Provide a name for your connection in the **Connection name** field.
   
   ![Baserow connection setup details](/assets/baserow-connection-setup.Duqyk6DO.png)_Baserow connection setup_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter the **Database token**. Refer to [Baserow setup for database token authentication](#baserow-setup) for more information.
   
6. Optional. Enter your self-hosted instance URL in the **Instance URL** field, for example `https://baserow.example.com`, with no trailing slash. This field defaults to `https://api.baserow.io` if left blank.
   
7. Click **Connect**.

---
