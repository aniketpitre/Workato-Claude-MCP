---
url: 'https://docs.workato.com/en/connectors/freshservice.md'
description: >-
  Connect Freshservice to Workato to automate IT service management workflows,
  streamlining service delivery across your ITIL-based processes.
---

# Freshservice

[Freshservice](https://www.freshworks.com/freshservice/) is a cloud-based IT Service Management solution that was designed using ITIL (Information Technology Infrastructure Library) best practices. Freshservice helps IT organizations streamline their service delivery processes with a strong focus on user experience and employee happiness.

## Prerequisites

You must provide authentication credentials and API details to establish a connection to Freshservice.

### Obtain an API key from Freshservice

1. Sign in to your Freshservice account.
   
2. Navigate to **Profile Settings**.
   
3. Locate the **API Key** in the **Your API Key** section.
   
4. Copy and securely store the API Key for use in Workato.
   

## Connection setup

Establishing a connection to Freshservice involves the following steps:

1. [Download the Freshservice connector from the Community library](#community-download)
2. [Complete setup in Workato](#workato-setup)

### Download the Freshservice connector from the Community library

Complete the following steps to install the Freshservice connector from the [community library](https://www.workato.com/browse/connectors):

1. Open the recipe editor and search for a connector. Alternatively, you can search for a connector in the [community library](https://www.workato.com/browse/connectors).
   
   ![Search for recipe editor](/assets/search-on-recipe-editor.VrZpf8zl.png)_Search for community connectors in the recipe editor_
   
2. Select the community connector you plan to install.
   
3. Click **Install** to install the connector from the community library.
   
   ![Click install](/assets/install-connector.BXpGZP9K.png)_Click **Install**_
   
4. Select **Release connector**. Alternatively, select **Review code** to review and modify the connector code before releasing it to the workspace.
   
   ![Release connector](/assets/release-and-review.kWToLwmF.png)_Release the connector_
   
5. Summarize any changes you made to the connector, then click **Release** to allow workspace collaborators to use the connector in recipes.
   
   ![The Confirm release dialog](/assets/release.CpEhhA-6.png)_The **Confirm release** dialog_
   

### Complete setup in Workato

Complete the following steps to establish a connection to Freshservice.

1. Click **Create > Connection** or press C twice.
   
2. Search for and select Freshservice as your connection on the New connection page.
   
3. Provide a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Provide the helpdesk name in **Helpdesk** field, as found in your Freshservice URL.
   
6. Provide the **API key** from the Freshservice support portal.
   
7. Click **Connect**.
   
   ![Connection](/assets/freshservice-connection.DGhpXBPH.png)_Freshservice connection_

---
