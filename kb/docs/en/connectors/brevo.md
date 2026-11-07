---
url: 'https://docs.workato.com/en/connectors/brevo.md'
description: >-
  Brevo is a cloud-based communication platform that supports customer messaging
  across multiple channels.
---

# Brevo

[Brevo](https://www.brevo.com/) is a cloud-based communication platform that supports customer messaging across multiple channels. Brevo enables you to create campaigns, automate workflows, manage contacts, and track communication activity.

This connector provides the following actions:

- [Send transaction emails](/en/connectors/brevo/send-transactional-email-action)
- [Delete a record](/en/connectors/brevo/delete-record-action)
- [Create a record](/en/connectors/brevo/create-record-action)
- [Update record details](/en/connectors/brevo/update-record-action)

## Install Brevo from the community library

Complete the following steps to install the Brevo connector from the [community library](https://www.workato.com/browse/connectors):

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

The Brevo connector uses API key authentication.

### Brevo setup

Complete the following steps to generate an API key from your Brevo account settings:

1. Go to your Brevo account and click **SMTP & API** settings.
   
2. Click **Generate a new API key**.
   
3. Enter a name for your API key in **Name your API key**.
   
4. Click **Generate**.
   
5. Securely store the API key to use in Workato.
   

### Connect to Brevo in Workato using API key authentication

Complete the following steps to connect to Brevo in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select **Brevo** on the **New connection** page.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Brevo connection](/assets/brevo-connection-setup.Bc0HiqvR.png)_Set up a Brevo connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter your API key in the **API key** field.
   
6. (Optional) add an external secret
   
   1. Click **Add external secret**.
      
   2. Enter your **Key name** and **Secret ARN**.
      
   
7. Click **Connect**.

---
