---
url: 'https://docs.workato.com/en/connectors/files-dot-com.md'
description: >-
  The Files.com connector enables you to automate cloud file storage workflows,
  including uploads, downloads, searching, and folder organization.
---

# Files.com

[Files.com](https://www.files.com/) is a cloud-based file sharing and storage platform that enables businesses to securely store, manage, and collaborate on files. This connector enables you to automate file and folder operations, including uploads, downloads, searching, and file organization across your workflows. This connector supports file and folder objects.

This connector has the following capabilities:

- Automatically upload files to Files.com when new documents are created in a document management system
- Download files from Files.com folders and process them in other applications
- Sync files between Files.com and other cloud storage platforms
- Create organized folder structures when new projects are initiated in a project management system
- Move or copy files between folders based on workflow events
- Extract ZIP files for further processing or distribution
- Create ZIP archives from multiple files for backup or distribution purposes

## Prerequisites

To connect to Files.com in Workato, ensure that you have the following:

- Your Files.com API key
- Your Files.com API key location

### Generate a Files.com API key

Complete the following steps to generate a Files.com API key:

1. Go to Files.com.
   
2. Log in to your Files.com account.
   
3. Navigate to your Files.com profile.
   
4. Go to **My Account > Authentication > API Keys**.
   
5. Click **Create API key**.
   
6. Save the newly generated API key to use when completing the connection in Workato.
   

### Download Files.com from the community library

Complete the following steps to install the Files.com connector from the [community library](https://www.workato.com/browse/connectors):

1. Open the recipe editor and search for a connector. Alternatively, you can search for a connector in the [community library](https://www.workato.com/browse/connectors).
   
   ![Search for recipe editor](/assets/search-on-recipe-editor.VrZpf8zl.png)_Search for community connectors in the recipe editor_
   
2. Select the community connector you plan to install.
   
3. Click **Install** to install the connector from the community library.
   
   ![Click install](/assets/install-connector.BXpGZP9K.png)_Click **Install**_
   
4. Select **Release connector**. Alternatively, select **Review code** to review and modify the connector code before releasing it to the workspace.
   
   ![Release connector](/assets/release-and-review.kWToLwmF.png)_Release the connector_
   
5. Summarize any changes you made to the connector, then click **Release** to allow workspace collaborators to use the connector in recipes.
   
   ![The Confirm release dialog](/assets/release.CpEhhA-6.png)_The **Confirm release** dialog_
   

## Set up connection in Workato

Complete the following steps to establish a connection to Files.com in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select Files.com as your connection on the **New Connection** page.
   
3. Provide a unique name for the connection in the **Connection name** field.
   
   ![Files.com Connection](/assets/files-dot-com-connection-setup.DJvzGlCf.png)_Create your Files.com connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter the **Subdomain** of your Files.com instance. For example, if your Files.com instance URL is **acme.files.com**, enter **acme**.
   
6. Enter your Files.com **API key**. Refer to the [Prerequisites](#prerequisites) section to generate this value.
   
7. Use the **API key location** drop-down menu to select where to send the API key. Use **Header** for standard authentication or **Basic auth** for legacy systems.
   
8. Click **Connect**.

---
