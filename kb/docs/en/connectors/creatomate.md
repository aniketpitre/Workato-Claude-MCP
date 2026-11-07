---
url: 'https://docs.workato.com/en/connectors/creatomate.md'
description: >-
  The Creatomate connector lets you render videos, images, and GIFs from
  templates or RenderScript, and manage templates in Workato.
---

# Creatomate

[Creatomate](https://creatomate.com) is a programmatic media generation service. This connector enables you to render videos, images, and GIFs from reusable templates or from RenderScript, a JSON scene description. You can also create, search, update, and delete templates.

## Install Creatomate from the community library

Complete the following steps to install the Creatomate connector from the [community library](https://www.workato.com/browse/connectors):

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

The Creatomate connector uses API key authentication.

### Creatomate setup

1. Sign in to your [Creatomate dashboard](https://creatomate.com/).
   
2. Open the project you plan to use, then go to **Project Settings**.
   
3. Copy the project **API key**.
   

### Connect to Creatomate using API key

Complete the following steps to connect to Creatomate in Workato:

1. Click **Create > Connection**.
   
2. Search for `Creatomate` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Creatomate connection setup](/assets/creatomate-connection-setup.BTBlMTqX.png)_Creatomate connection setup_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Paste the API key you copied earlier into the **API key** field. The key is scoped to that project, so only that project's templates and renders are available. The API allows 30 requests per 10-second window.
   
6. Click **Connect**.

---
