---
url: 'https://docs.workato.com/en/connectors/stacklet.md'
description: >-
  The Stacklet connector enables you to automate governance workflows, integrate
  compliance monitoring with business processes, and streamline cloud resource
  management through GraphQL-based operations.
---

# Stacklet

[Stacklet](https://stacklet.io/) is a cloud governance and cost management platform that helps you enforce policies, manage security, and optimize cloud costs across your infrastructure. This connector enables you to automate governance workflows, integrate compliance monitoring with business processes, and streamline cloud resource management through GraphQL-based operations.

This connector allows you to:

- Query data from Stacklet's GraphQL API
- Perform mutations to create, update, or delete records
- Execute custom GraphQL operations with variables

## Prerequisites

You must have an AWS Cognito client ID and a Stacklet instance to establish a connection to Stacklet.

### Obtain your AWS Cognito client ID

Complete the following steps to retrieve your AWS Cognito client ID:

1. Sign in to your [AWS Management Console](https://console.aws.amazon.com/).
   
2. Search for `Cognito` and select Amazon Cognito.
   
3. Select **User Pools** in the left-hand navigation pane.
   
4. Select the user pool that contains the app client your Stacklet instance is associated with.
   
5. Click **App Integration**.
   
6. Go to the **App clients** section to view a list of all of the clients associated with the user pool.
   
7. Copy your **Client ID** from the **App clients** section to use when setting up your connection in Workato. If your client is confidential, you can click **Show details** to reveal your **Client ID**.
   

### Obtain Stacklet account information

Complete the following steps to obtain your Stacklet account information:

1. Sign in to Stacklet and open the Stacklet API console in your browser.
   
2. Copy the domain from the URL. For example, `api.acme.stacklet.io`. This is your **Base URL**.
   
3. Click the profile icon in the bottom left corner of the Stacklet API console to obtain your Stacklet **Username**.
   

## Connection setup

Connecting to the Stacklet involves the following steps:

- [Download the Stacklet from the community](#community-download)
- [Complete setup in Workato](#workato-setup)

### Download Stacklet from the Community library

Complete the following steps to install the Stacklet connector from the [community library](https://www.workato.com/browse/connectors):

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

Complete the following steps to establish a connection to Stacklet in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select Stacklet as your connection on the **New Connection** page.
   
3. Provide a unique name for the connection in the **Connection name** field.
   
   ![Stacklet Connection](/assets/stacklet-connection-setup.BCG1sMMc.png)_Create your connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Connection type** drop-down menu to select the connection type.
   
6. Enter your Stacklet **Username**.
   
7. Enter your AWS Cognito **Client ID** for Stacklet.
   
8. Enter your **Base URL**. This is your Stacklet instance URL. For example, `api.acme.stacklet.io`.
   
9. Click **Connect**.

---
