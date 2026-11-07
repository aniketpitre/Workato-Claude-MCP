---
url: 'https://docs.workato.com/en/connectors/nocodb.md'
description: >-
  Connect Workato to NocoDB Cloud or self-hosted instances to search, create,
  update, and delete table rows, and trigger recipes when records change.
---

# NocoDB

[NocoDB](https://nocodb.com) is an open-source no-code platform that presents tables from databases such as Postgres and MySQL as editable grids, forms, and views. The NocoDB connector enables you to read and write table rows in NocoDB Cloud or a self-hosted instance, and trigger recipes when records change.

## Install NocoDB from the community library

Complete the following steps to install the NocoDB connector from the [community library](https://www.workato.com/browse/connectors):

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

The NocoDB connector uses API token authentication.

### NocoDB setup

Complete the following steps to set up API token authentication in NocoDB:

1. Log in to your NocoDB instance. For NocoDB Cloud, go to the [NocoDB sign-in page](https://app.nocodb.com/signin/).
   
2. Copy your NocoDB instance URL from the browser address bar.
   
   Use one of the following formats:
   
   - NocoDB Cloud: `https://app.nocodb.com`
   - Self-hosted instance with a public URL: your public URL. For example, `https://nocodb.example.com`.
   - Self-hosted instance on a private network or localhost: your in-network URL. For example, `http://localhost:8080`. This connection type requires an [on-prem agent](/en/on-prem/agents). `localhost` refers to the host where the agent runs.
3. Create a NocoDB API token:
   
   1. Go to **Account Settings > API Tokens**.
      
   2. Enter a name for your API token in the **Name** field.
      
   3. Configure access to the API token in the **Resource scope** field.
      
   4. Configure permissions for the API token in the **Scopes** field.
      
   5. Click **Create new token**.
      

### Connect to NocoDB using an API token

Complete the following steps to connect to NocoDB in Workato:

1. Click **Create > Connection**.
   
2. Search for `NocoDB` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![NocoDB connection setup](/assets/nocodb-connection-setup.-qPdC_xA.png)_NocoDB connection setup_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Connection type** drop-down menu to select **Cloud**, or select an [on-prem group](/en/on-prem/groups) to connect to a self-hosted instance on a private network or localhost.
   
6. Enter the URL of your NocoDB instance in the **Instance URL** field.
   
7. Enter your NocoDB API token in the **API token** field.
   
8. Enter your workspace ID in the **Workspace ID** field. The workspace ID is in your NocoDB URL. For example, `wxxxx`.
   
9. Click **Connect**.

---
