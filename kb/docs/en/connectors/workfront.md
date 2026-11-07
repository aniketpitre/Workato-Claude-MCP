---
url: 'https://docs.workato.com/en/connectors/workfront.md'
description: >-
  The Workfront connector lets you automate work management: create, update, and
  search objects, and trigger recipes on new or updated objects and events.
---

# Workfront

[Workfront](http://workfront.com/) is an online work management software that is designed to connect people to work and accelerate organizational success across enterprises.

## API version

The Workfront connector uses the [Workfront API version 19.0](https://experienceleague.adobe.com/en/docs/workfront/using/adobe-workfront-api/workfront-api).

## How to connect to Workfront

The Workfront connector supports the following authentication methods:

- [OAuth 2.0](#oauth-2-0)
- [API key](#api-key)

### OAuth 2.0

Complete the following steps to establish a Workfront connection using OAuth 2.0 authentication:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Workfront` on the **New connection** page.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Connect to Workfront with OAuth 2.0](/assets/oauth2.BnqlK67x.png)_Connect to Workfront with OAuth 2.0_
   
4. Use the **Location** drop-down menu to select the project or folder to store your connection.
   
5. Use the **Authentication type** drop-down menu to select `OAuth 2.0`.
   
6. Enter your **Client ID** in the **Client ID** field.
   
   Refer to [Manage custom OAuth2 applications](https://experienceleague.adobe.com/en/docs/workfront/using/administration-and-setup/configure-integrations/manage-custom-oauth2-apps#manage-custom-oauth2-applications) in the Adobe Workfront documentation to create a client ID and secret.
   
7. Enter your **Client secret** in the **Client secret** field.
   
8. Enter your Workfront subdomain in the **Subdomain** field.
   
   Your Workfront subdomain name is found in your Workfront URL. For example, if your URL is `https://mycompany.workfront.com`, enter `mycompany`.
   
9. Enter the API version to use in your connection in the **API version** field.
   
   The default version is 19.0. Refer to the Adobe [API versioning and support schedule](https://experienceleague.adobe.com/en/docs/workfront/using/adobe-workfront-api/api-notes/api-version-support-schedule) for supported versions.
   
10. Use the **Account timezone** drop-down menu to select your account timezone.
    
    This timezone is needed for consistency with Workfront. All date and time fields are converted to this timezone.
    
11. Click **Connect**.
    

### API key

Complete the following steps to establish a Workfront connection using API key authentication:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Workfront` on the **New connection** page.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Connect to Workfront with API key](/assets/api-key.Dp4D35Sr.png)_Connect to Workfront with API key_
   
4. Use the **Location** drop-down menu to select the project or folder to store your connection.
   
5. Use the **Authentication type** drop-down menu to select `API key`.
   
6. Enter your Workfront API key in the **API key** field.
   
   Refer to [Manage API keys](https://experienceleague.adobe.com/en/docs/workfront/using/administration-and-setup/manage-wf/security/manage-api-keys) in the Adobe Workfront documentation to generate or manage API keys.
   
7. Enter your Workfront subdomain in the **Subdomain** field.
   
   Your Workfront subdomain name is found in your Workfront URL. For example, if your URL is `https://mycompany.workfront.com`, enter `mycompany`.
   
8. Enter the API version to use in your connection in the **API version** field.
   
   The default version is 19.0. Refer to the Adobe [API versioning and support schedule](https://experienceleague.adobe.com/en/docs/workfront/using/adobe-workfront-api/api-notes/api-version-support-schedule) for supported versions.
   
9. Use the **Account timezone** drop-down menu to select your account timezone.
   
   This timezone is needed for consistency with Workfront. All date and time fields are converted to this timezone.
   
10. Click **Connect**.

---
