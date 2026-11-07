---
url: 'https://docs.workato.com/en/connectors/zoho-crm.md'
description: >-
  Connect to Zoho CRM to manage customer relationships, track sales activities,
  and automate business processes.
---

# Zoho CRM

[Zoho CRM](https://www.zoho.com/crm/) is a cloud-based customer relationship management (CRM) platform designed to help businesses manage their sales, marketing, and customer support activities.

## API version

The Zoho CRM connector uses the following Zoho CRM API versions:

- [V2](https://www.zoho.com/crm/developer/docs/api/v2/)
- [V5](https://www.zoho.com/crm/developer/docs/api/v5/)
- [V7](https://www.zoho.com/crm/developer/docs/api/v7/)

## How to connect to Zoho CRM

The Zoho CRM connector uses OAuth 2.0 authentication.

Complete the following steps to establish a Zoho CRM connection in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Zoho CRM` on the **New connection** page.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Connect to Zoho CRM](/assets/connect.Ci6gBkOa.png)_Connect to Zoho CRM_
   
4. Use the **Location** drop-down menu to select the project or folder to store your connection.
   
5. Use the **Account timezone** drop-down menu to select your account timezone as specified in Zoho CRM.
   
6. Use the **Data center** drop-down menu to select your data center. You can find your data center at the end of your Zoho URL.
   
7. Expand the **Advanced settings** section to configure **Scopes** for your connection.
   
   The following scopes are requested by default:
   
   - `ZohoCRM.modules.contacts.READ`
   - `ZohoCRM.settings.modules.READ`
   
   Defaults to `ZohoCRM.modules.all`, `ZohoCRM.settings.all` if left blank.
   
8. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
9. Click **Connect**.
   

## Standard modules and fields

Refer to the Zoho [CRM Platform Modules & Fields](https://www.zoho.com/developer/help/api/modules-fields.html) documentation for information about standard modules and their available fields in Zoho CRM.

---
