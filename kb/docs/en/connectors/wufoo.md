---
url: 'https://docs.workato.com/en/connectors/wufoo.md'
description: >-
  The Wufoo connector enables you to automate form workflows, capturing data
  from registration, contact, and payment forms you build in Wufoo.
---

# Wufoo

[Wufoo](https://www.wufoo.com/) is a cloud-based form builder that allows you to create forms for data collection, including:

- Registration forms
- Application forms
- Contact forms
- Payment forms

You can create your forms with or without code. Wufoo also allows you to process online payments through their payment partners, including PayPal, Stripe, and Authorize.Net.

## API version

Workato's Wufoo connector uses Wufoo's REST API v3. Refer to [Wufoo's API documentation](https://help.wufoo.com/articles/en_US/kb/Wufoo-REST-API-V3/v3/) for more information.

## Connection setup

[Locate your Wufoo API key](#locate-wufoo-api-key) before you set up your Workato connection. To set up your connection:

1. Provide a **Connection name** that identifies which Wufoo instance Workato is connected to.
   
   ![Wufoo connection](/assets/wufoo-connection-setup.zjhF89Za.png)_Create your connection_
   
2. Select the project where you plan to store the connection from the **Location** drop-down menu.
   
3. Enter your Wufoo **API key**. Refer to [Locate your Wufoo API key](#locate-wufoo-api-key) for more information.
   
4. Enter your Wufoo **sub-domain**. For example, if your URL is `https://testcompany.wufoo.com`, your sub-domain is `testcompany`.
   
5. Click **Connect**.
   

## Locate Wufoo API key

You must provide your Wufoo API key to connect your Wufoo instance to Workato. To locate your API key:

1. Log in to your Wufoo account.
   
2. Click **Forms** in the top navigation bar.
   
3. Click the **more options ...** (ellipses) menu in the form entry row and then select **API information** to view your API key.
   
   ![Wufoo more options](/assets/more-options-api-key.9FtjpJ1O.png)_More options > API information_

---
