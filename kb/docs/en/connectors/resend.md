---
url: 'https://docs.workato.com/en/connectors/resend.md'
description: >-
  Connect Resend to Workato to send and manage transactional emails, track
  delivery events, and manage scheduled emails.
---

# Resend

[Resend](https://resend.com) is an email API that supports sending transactional email from your own domain. It also manages sending domains, schedules emails, and tracks delivery activity such as bounces and complaints. The Resend connector enables you to send and manage emails and respond to delivery events in Workato.

Use the Resend connector to:

- Send an email to one or more recipients, or send a batch of up to 100 emails.
- Schedule emails, update their scheduled time, or cancel them before delivery.
- Retrieve an email or list emails and sending domains.
- Trigger recipes when an email bounces, receives a complaint, is delayed, or fails.

You can also use [custom actions](/en/developing-connectors/custom-actions) to build a custom HTTP request to any Resend API endpoint. Refer to the Resend [API](https://resend.com/docs/api-reference/introduction) documentation for endpoint details.

## Install Resend from the community library

Complete the following steps to install the Resend connector from the [community library](https://www.workato.com/browse/connectors):

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

The Resend connector uses API key authentication. Workato sends the API key as a bearer token in the `Authorization` header.

### Resend setup

Complete the following steps to generate an API key in Resend:

1. Sign in to your [Resend](https://resend.com/login) account.
   
2. Click **API Keys > Create API Key**.
   
3. Enter a **Name** for the API key.
   
4. Use the **Permission** drop-down menu to select a permission. **Full access** grants access to create, delete, get, and update any resource. **Sending access** grants access only to send emails.
   
5. Optional. Use the **Domain** drop-down menu to select the domain to restrict access to if you selected **Sending access** in the preceding step.
   
6. Click **Add**.
   
7. Copy and save the **API Key** for use in Workato.
   
   > **SAVE THE API KEY**
   > 
   > Resend only displays the API key once. You must create a new one if you lose it.
   

### Connect to Resend using an API key

Complete the following steps to connect to Resend in Workato:

1. Click **Create > Connection**.
   
2. Search for `Resend` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Resend connection setup](/assets/resend-connection-setup.acwyXGxU.png)_Create a Resend connection in Workato._
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter the **API key**. Refer to [Resend setup](#resend-setup) for more information.
   
6. Click **Connect**.

---
