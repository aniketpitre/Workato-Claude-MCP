---
url: 'https://docs.workato.com/en/connectors/calcom.md'
description: >-
  Cal.com is an open-source scheduling platform for booking meetings and
  appointments.
---

# Cal.com

[Cal.com](https://cal.com) is an open-source scheduling platform for booking meetings and appointments. The Cal.com connector lets you check availability, create, reschedule, and cancel bookings, and react in real time when a booking changes.

## Install Cal.com from the community library

Complete the following steps to install the Cal.com connector from the [community library](https://www.workato.com/browse/connectors):

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

The Cal.com connector uses API key authentication.

### Cal.com setup

Complete the following steps to create an API key to connect to Cal.com:

1. Log in to your [Cal.com](https://cal.com/) account.
   
2. Go to **Settings > Developer > API Keys**.
   
3. Click **New API key**.
   
4. Provide a **Name** for your API key.
   
5. Select an expiration date for your API key.
   
6. Click **Save**.
   
7. Copy and securely store the API key for use in Workato.
   

### Connect to Cal.com using API key

Complete the following steps to connect to Cal.com in Workato:

1. Click **Create > Connection**.
   
2. Search for `Cal.com` and select it as your connection.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Create a Cal.com connection in Workato.](/assets/calcom-connection-setup.BGPDipLD.png)_Create a Cal.com connection in Workato._
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter your API key in the **API key** field.
   
6. Click **Connect**.

---
