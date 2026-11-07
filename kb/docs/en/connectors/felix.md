---
url: 'https://docs.workato.com/en/connectors/felix.md'
description: >-
  The Felix connector lets you automate vendor workflows: search records and
  suspend or unsuspend vendors for procurement and compliance.
---

# Felix

Felix is a vendor management and procurement platform for construction. This connector allows you to automate vendor management workflows including, vendor search, compliance document management, and vendor suspension processes.

## API version

This connector uses the [Felix API](https://api-docs.felix.net).

## How to connect to Felix

You must complete the steps in each of the following sections to connect to Felix:

### Download the Felix connector from the community

Complete the following steps to install the Felix connector from the [community library](https://www.workato.com/browse/connectors):

1. Open the recipe editor and search for a connector. Alternatively, you can search for a connector in the [community library](https://www.workato.com/browse/connectors).
   
   ![Search for recipe editor](/assets/search-on-recipe-editor.VrZpf8zl.png)_Search for community connectors in the recipe editor_
   
2. Select the community connector you plan to install.
   
3. Click **Install** to install the connector from the community library.
   
   ![Click install](/assets/install-connector.BXpGZP9K.png)_Click **Install**_
   
4. Select **Release connector**. Alternatively, select **Review code** to review and modify the connector code before releasing it to the workspace.
   
   ![Release connector](/assets/release-and-review.kWToLwmF.png)_Release the connector_
   
5. Summarize any changes you made to the connector, then click **Release** to allow workspace collaborators to use the connector in recipes.
   
   ![The Confirm release dialog](/assets/release.CpEhhA-6.png)_The **Confirm release** dialog_
   

### Generate an API key in Felix

You must generate an API key in Felix to create a connection in Workato. Refer to the [Felix documentation](https://enterprise.help.felix.net/support/solutions/articles/35000154009-how-to-generate-api-tokens) for detailed instructions.

### Complete setup in Workato

Complete the following steps to establish a connection to Felix in Workato:

1. Provide a **Connection name** that identifies which Felix instance Workato is connected to.
   
   ![Felix Connection](/assets/felix-connection-setup.CqZPkeyl.png)_Create your connection_
   
2. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
3. Enter your API token.
   
4. Click **Connect**.

---
