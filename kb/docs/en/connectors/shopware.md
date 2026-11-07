---
url: 'https://docs.workato.com/en/connectors/shopware.md'
description: >-
  The Shopware connector enables you to automate e-commerce workflows, syncing
  orders, customers, and opportunities across your platforms.
---

# Shopware

[Shopware](https://www.shopware.com/en/company/) is a modular e-commerce platform available both as open-source software and in commercial editions. Use this connector to receive updates for new customers and orders in Shopware, sync order data, and create or update opportunities in other platforms.

## Prerequisites

Before using the Shopware connector in Workato, ensure you have an active account with appropriate permissions to access APIs. If you don't already have an account, complete the following steps to register for one.

### Register an account in Shopware

Complete the following steps to register for a Shopware account:

1. Go to the [registration](https://auth.shopware.com/registration?return_to=https:%2F%2Faccount.shopware.com) page.
   
   ![Shopware account](/assets/shopware-account.nQpsZnh4.png)_Shopware Account_
   
2. Fill in the required fields.
   
3. Click **Create account**. Shopware sends an email confirming your registration.
   
4. Enter the verification code that Shopware sends to your email address and click **Verify**.
   
5. Complete your Shopware profile.
   

For details on linking your shop to your account and downloading extensions, refer to the [Shopware documentation](https://docs.shopware.com/en/shopware-6-en/getting-started/create-shopware-account?category=shopware-6-en/getting-started).

### Retrieve client credentials

To connect external applications to your Shopware store using the Shopware 6 API, you must first retrieve client credentials.

Complete the following steps to retrieve your client credentials:

1. Sign in to your Shopware account.
   
2. Go to **Settings > System > Integrations**.
   
3. Click **Create integration** to add a new integration.
   
4. Enter the name for your integration in the **Name** field.
   
   ![Shopware credentials](/assets/shopware-credentials.DpnQnyJ4.png)_Shopware Credentials_
   
5. Click the **Administrator** toggle to assign administrator permissions to the integration, if required.
   
6. Select roles to assign the integration from the **Roles** drop-down menu.
   
7. Copy the **Access key ID** and **Secret access key**.
   
8. Click **Save integration**.
   

## How to connect to Shopware

Complete the following steps to establish a Shopware connection in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select **Shopware** as your connection on the **New connection** page.
   
3. Provide a name for your connection in the **Connection name** field.
   
   ![Shopware connection setup](/assets/shopware-connection-setup.CmpTOzgn.png)_Shopware Connection Setup_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter the **Access key** for your Shopware account.
   
6. Enter the **Secret access key** for your Shopware account.
   
7. Enter the subdomain where your shop is hosted in the **Shopware URL** field.
   
8. Click **Connect**.

---
