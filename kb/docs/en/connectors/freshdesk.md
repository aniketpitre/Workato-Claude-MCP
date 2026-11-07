---
url: 'https://docs.workato.com/en/connectors/freshdesk.md'
description: >-
  Connect Freshdesk to Workato to automate customer support and ticketing
  workflows, syncing tickets and contacts across your other apps.
---

# Freshdesk

[Freshdesk](https://freshdesk.com/) is a customer support software and ticketing system that helps companies provide a greater customer support experience. It enables ease of collaboration across agents, equips customers with the ability to self-service, and provides reporting and analytics for greater insights into your team's performance.

Freshdesk is a Workato community connector that provides bi-directional syncs for 1000+ apps. You can integrate popular apps with Freshdesk including Salesforce, Google Sheets, Trello, and Intercom.

Freshdesk integration scenarios include bi-directional syncs between new or updated:

- Freshdesk tickets to Salesforce cases
- Freshdesk tickets to ServiceNow incident
- Freshdesk contacts to Salesforce contacts
- Freshdesk users to Intercom users
- Freshdesk ticket to a message posted on a Slack channel

## Prerequisites

Ensure you have completed the following steps before using the Freshdesk connector in Workato:

- [Download Freshdesk from the community](#community-download)
- [View API key in Freshdesk](#view-api-key-in-freshdesk)

### Download Freshdesk from the community

Complete the following steps to install the Freshdesk connector from the [community library](https://www.workato.com/browse/connectors):

1. Open the recipe editor and search for a connector. Alternatively, you can search for a connector in the [community library](https://www.workato.com/browse/connectors).
   
   ![Search for recipe editor](/assets/search-on-recipe-editor.VrZpf8zl.png)_Search for community connectors in the recipe editor_
   
2. Select the community connector you plan to install.
   
3. Click **Install** to install the connector from the community library.
   
   ![Click install](/assets/install-connector.BXpGZP9K.png)_Click **Install**_
   
4. Select **Release connector**. Alternatively, select **Review code** to review and modify the connector code before releasing it to the workspace.
   
   ![Release connector](/assets/release-and-review.kWToLwmF.png)_Release the connector_
   
5. Summarize any changes you made to the connector, then click **Release** to allow workspace collaborators to use the connector in recipes.
   
   ![The Confirm release dialog](/assets/release.CpEhhA-6.png)_The **Confirm release** dialog_
   

### View API key in Freshdesk

1. Sign in to the [Freshdesk](https://login.freshworks.com/email-login/) portal.
   
2. Go to **Profile Settings** and click on **View API Key**.
   
   ![Freshdesk View API Key](/assets/view-api-key.B1-bgSFd.png)_Freshdesk View API Key_
   
3. Copy the **API Key** and store it securely for later use.
   

## How to connect to Freshdesk on Workato

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Freshdesk` as your connection on the **New Connection** page.
   
3. Provide a unique name for the connection in the **Connection name** field.
   
   ![Freshdesk Connection](/assets/freshdesk-connection.BdgfXr9U.png)_Freshdesk\_Connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter the Freshdesk **API key**. Refer to [View API key in Freshdesk](#view-api-key-in-freshdesk) to obtain this value.
   
6. Enter your Freshdesk instance subdomain in the **Helpdesk name** field.
   
7. Click **Connect**.

---
