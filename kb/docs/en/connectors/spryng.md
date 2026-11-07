---
url: 'https://docs.workato.com/en/connectors/spryng.md'
description: >-
  Connect Spryng in Workato to automate messaging workflows: retrieve account
  balance, cancel messages, create subaccounts, and list or search messages.
---

# Spryng

[Spryng](https://www.spryng.nl/) is a messaging platform that enables you to send messages globally. Spryng provides a reliable, secure, and scalable cloud-based solution for sending transactional SMS, bulk messaging, and managing subaccounts.

This connector enables you to:

- Retrieve account balance
- Cancel messages
- Create a subaccount
- Retrieve a list of all messages
- Search for specific messages

## API version

The Spryng connector uses the [Spryng REST API](https://docs.spryngsms.com/#intro).

## Prerequisites

You must generate a REST API key in Spryng before you can establish a connection in Workato.

### Generate an API key for Spryng

Complete the following steps to generate a REST API key to use with the Spryng connector:

1. Log in to your [Spryng account](https://www.spryng.nl/).
   
2. Go to **Profile > Security > Generate a new API key**.
   
3. Click **Generate a new API key**.
   

Refer to the [Spryng documentation](https://docs.spryngsms.com/#1-authorization) for more information.

## How to connect to Spryng

Connecting to the Spryng connector involves the following steps:

1. [Download the Spryng connector from the community](#community-download)
2. [Complete setup in Workato](#workato-setup)

### Download the Spryng connector from the community

Complete the following steps to install the Spryng connector from the [community library](https://www.workato.com/browse/connectors):

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

Complete the following steps to establish a connection to Spryng in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Spryng` as your connection on the **New connection** page.
   
3. Provide a **Connection name** that identifies which Spryng instance Workato is connected to.
   
   ![Spryng Connection](/assets/spryng-connection-setup.BomkQp0S.png)_Create your connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter your **API token**.
   
6. Click **Connect**.

---
