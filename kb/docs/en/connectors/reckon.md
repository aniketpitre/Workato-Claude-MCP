---
url: 'https://docs.workato.com/en/connectors/reckon.md'
description: >-
  The Reckon connector enables you to automate workflows using your Reckon One
  account. Create and update records, retrieve accounting data, and trigger
  recipes on record changes.
---

# Reckon

[Reckon](https://www.reckon.com) is an accounting software platform for small to medium businesses. It helps manage finances, payroll, inventory, and other accounting operations.

The Reckon connector lets you automate accounting workflows by integrating Reckon data into your recipes. You can create or update records, fetch financial information, and respond to changes in real-time.

## How to connect to Reckon

Complete the following steps to register credentials and then set up the connection in Workato:

- [Step 1: Register API credentials in Reckon](#register-credentials)
- [Step 2: Complete the setup in Workato](#complete-setup)

## Register API credentials in Reckon

Complete the following steps to obtain your client ID, client secret, and subscription key:

1. Sign up for a free [Reckon Developer Portal](https://developer.reckon.com/) account.
   
2. Submit an application to register your integration. You must receive approval before you can access credentials.
   
3. Go to your application dashboard in the Developer Portal after approval.
   
4. Register your callback URL. Then, locate or generate your **Client ID** and **Client secret** from the application details page.
   
5. Copy the **Subscription key** from your profile. You can use either the primary or secondary key.
   

## Complete the setup in Workato

Complete the following steps to create a Reckon connection in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Reckon` as your connection on the **New connection** page.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Connect to Reckon](/assets/connect-to-reckon.BxT9hLZy.png)_Connect to Reckon_
   
4. Use the **Location** drop-down to select the project or folder to store this connection.
   
5. Enter your **Client ID** and **Client secret**.
   
   Retrieve these credentials from the Reckon developer portal after registering your callback URL. Refer to the [Reckon developer portal](https://developer.reckon.com/) for more information.
   
6. Enter your **Subscription key**. Use the primary or secondary API V2 subscription key from your Reckon developer portal profile.
   
7. Select the required **OAuth scopes** from the drop-down menu. Scopes define the access level for the connection.
   
8. Click **Connect**.

---
