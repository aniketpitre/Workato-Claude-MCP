---
url: 'https://docs.workato.com/en/connectors/odata.md'
description: >-
  The OData connector lets you automate workflows with any OData API: create,
  update, delete, search, and get records, and trigger on new or updated
  records.
---

# OData

The OData connector is a universal connector you can use with any application that describes its API endpoints using OData. This connector parses a user-provided OData document and uses the content to generate a user interface, including actions, input and output fields, and objects in Workato. Use this connector when no app-specific connector is available and the application exposes an OData document.

## API version

The connector uses the following APIs:

- [OData v4 API](https://www.odata.org/odata-services/)
- [OData v2 API](https://www.odata.org/odata-services/): Select the `OData v2` tab.

## How to connect to

Connecting to the involves the following procedures:

- [Download the connector from the community](#community-download)
- [Complete setup in Workato](#setup)

### Download OData from the community

Complete the following steps to install the connector from the [community library](https://www.workato.com/browse/connectors):

1. Open the recipe editor and search for a connector. Alternatively, you can search for a connector in the [community library](https://www.workato.com/browse/connectors).
   
   ![Search for recipe editor](/assets/search-on-recipe-editor.VrZpf8zl.png)_Search for community connectors in the recipe editor_
   
2. Select the community connector you plan to install.
   
3. Click **Install** to install the connector from the community library.
   
   ![Click install](/assets/install-connector.BXpGZP9K.png)_Click **Install**_
   
4. Select **Release connector**. Alternatively, select **Review code** to review and modify the connector code before releasing it to the workspace.
   
   ![Release connector](/assets/release-and-review.kWToLwmF.png)_Release the connector_
   
5. Summarize any changes you made to the connector, then click **Release** to allow workspace collaborators to use the connector in recipes.
   
   ![The Confirm release dialog](/assets/release.CpEhhA-6.png)_The **Confirm release** dialog_
   

### Authentication

You can authenticate the connector using the following methods:

- None
- Basic
- Header
- Query params
- OAuth 2.0 client credentials
- OAuth 2.0 authorization code
- Client certificate based security policy

### Complete setup in Workato

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Connector name` as your connection in the **New connection** page.
   
3. Provide a name for your connection in the **Connection name** field.
   
   ![OData Connection](/assets/odata-connection-setup.BO7PA6Hq.png)_Create your connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Select the **Connection type** from the drop-down menu to specify a cloud or on-prem connection.
   
6. Select the **OData document source**, such as **Document URL** or **Document content**. The document source defines how to provide the OData document to the connector. Workato recommends selecting **Document URL**.
   
7. Select an **Authentication method** from the drop-down menu. Refer to [Authentication](#authentication) for a list of supported authentication methods.
   
8. Enter the **Server URL** that links to the target host or service.
   
9. Click **Connect**.

---
