---
url: 'https://docs.workato.com/en/agentic/workato-go/data-sources/google-suite.md'
description: >-
  Set up Google Workspace prerequisites in Workato GO to let agents search
  content across Gmail, Google Calendar, and Google Drive data sources.
---

# Google Workspace data sources

Google Workspace data sources allow Workato Go to search content from [Gmail](/en/agentic/workato-go/data-sources/gmail), [Google Calendar](/en/agentic/workato-go/data-sources/google-calendar), and [Google Drive](/en/agentic/workato-go/data-sources/google-drive).

## Prerequisites

You must complete the following tasks before you add a Google Workspace data source to Workato Go:

- [Enable APIs](#enable-apis)
- [Create a custom admin role](#create-a-custom-admin-role)
- [Create a service account in Google Cloud Console](#create-a-service-account-in-google-cloud-console)
- [Add API scopes](#add-api-scopes)

### Enable APIs

Complete the following steps to enable your Google Workspace API:

1. Go to the [Google Cloud Console API library](https://console.cloud.google.com/apis/library) using the Google Workspace account that provides the service accounts.
   
   ![Go to the Google Cloud Console API library](/assets/google-cloud-library.CRA6D27H.png)_Go to the Google Cloud Console API library_
   
2. Search for and select **Admin SDK API**.
   
   ![Select Admin SDK API](/assets/select-admin-api.MFZbGp02.png)_Select **Admin SDK API**_
   
   > **REQUIRED FOR INDEX CRAWLING**
   > 
   > You must enable the Admin SDK to allow index crawling.
   
3. Click **Enable**.
   
   ![Enable Admin SDK API](/assets/enable-admin-api.jOfB8Ed8.png)_Enable Admin SDK API_
   
4. Search for and enable the APIs for the Google Workspace data sources you plan to add:
   
   - **Gmail API**
   - **Google Calendar API**
   - **Google Drive API**

### Create a custom admin role

After you enable the required APIs, you must create a service account to access them. This requires creating a custom admin role and assigning it to the appropriate user account.

Complete the following steps to create a custom Super Admin role for your service account:

1. Go to the Google admin [roles page](https://admin.google.com/ac/roles).
   
2. Click **Create new role** to create a custom admin role.
   
   ![Create new role](/assets/create-google-role.Av4lJGlJ.png)_Create new role_
   
3. Name the role `Workato AI`.
   
   ![Name the role](/assets/name-google-role.BX4LOt36.png)_Name the role_
   
4. Optional. Add a **Description** for the role.
   
5. Click **Continue**.
   
6. Go to **Admin Console Privileges** and select the following permissions:
   
   - **Users > Read**
   - **Services > Drive and Docs > Settings**
   
   ![Select permissions](/assets/select-permissions.BNZG8HDe.png)_Select permissions_
   
7. Go to **Admin API Privileges** and select the following permissions:
   
   - **Reports**
   - **Groups > Read**
   - **Users > Read**
8. Click **Continue > Create Role**. Google redirects you to a page where you can assign users to the Workato AI role you created in the preceding steps.
   
9. Click **Assign members** and then add a Google Workspace user. This user must have logged in at least once to the Google Workspace and accepted the Terms of Service.
   
   ![Assign members](/assets/assign-members.DYHfH0Gl.png)_Assign members_
   
10. Click **Assign role**. Store the email to use for your data source configuration.
    
11. Copy the **Client ID** from the service account details page in Google Cloud Console.
    

### Create a service account in Google Cloud Console

Complete the following steps to create a service account:

1. Go to [Google Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts) in Google Cloud Console and select an existing project or create a new project if one doesn't already exist.
   
   > **USE THE SAME SERVICE ACCOUNT FOR YOUR GOOGLE APPS**
   > 
   > You can use the same service account for the Gmail, Google Calendar, and Google Drive Workato GO data sources.
   
2. Click **CREATE SERVICE ACCOUNT** and skip the optional steps.
   
   ![Create service account](/assets/create-service-account.C8SljZOj.png)_Create service account_
   
3. Open the service account in **Google Cloud Console**.
   
4. Copy and store the **OAuth 2.0 Client ID** in a secure location. You must provide this value when you configure the data source.
   
5. Go to the **Actions** column for the service account and click the **manage** menu (three dots).
   
   ![Click the manage menu](/assets/click-manage-menu.CtR198q7.png)_Click the manage menu_
   
6. Click **Manage keys**. The **Keys** page automatically displays.
   
   ![Manage keys](/assets/manage-keys.Ohea8tyH.png)_Manage keys_
   
7. Click **Add key > Create new key**. The **Create private key** modal opens.
   
   ![Create new key](/assets/create-new-key.BYqRHQfk.png)_Create new key_
   
8. Select **JSON** and click **Create**. A JSON file automatically downloads to your computer. Store the file safely as its contents are required for the Service Account JSON section in the Workato GO platform.
   
   ![Create private key](/assets/create-private-key.Dxgu62Z-.png)_Create private key_
   

### Add API scopes

Now that we have a service account we now need to grant the service account specific permissions.

Complete the following steps to add API scopes to your service account:

1. Go to Google Admin Console and sign in as an admin.
   
2. Go **Menu > Security > Access and data control > API controls > Manage Domain Wide Delegation**.
   
3. Click **Add new**.
   
   ![Add API scopes](/assets/add-api-scopes.Crb56Nkr.png)_Add API scopes_
   
4. Enter the OAuth 2.0 Client ID that you created in the [preceding steps](/en/agentic/workato-go/data-sources/google-suite#create-a-service-account-in-google-cloud-console) into the **Client ID** field.
   
   ![Enter the Client ID](/assets/enter-client-id.BwQU2D31.png)_Enter the **Client ID**_
   
5. Copy and paste the following values into the **OAuth scopes (comma-delimited)** field:
   
   | Scope | Product | Description | Documentation |
   | --- | --- | --- | --- |
   | https:// www. googleapis. com/auth/ admin.directory .group.readonly | Admin SDK | View groups on your domain. | [Admin SDK API Scopes](https://developers.google.com/admin-sdk/directory/v1/guides/authorizing) documentation |
   | https:// www. googleapis. com/auth/ admin.directory .user.readonly | Admin SDK | View information about users on your domain. | [Admin SDK API Scopes](https://developers.google.com/admin-sdk/directory/v1/guides/authorizing) documentation |
   | https:// www .googleapis. com/ auth/admin.reports .audit.readonly | Admin SDK | View audit reports for your Google Workspace domain. | [Admin SDK API Scopes](https://developers.google.com/admin-sdk/directory/v1/guides/authorizing) documentation |
   | https:// www .googleapis. com/auth/drive .readonly | Google Drive API | View and download all Drive files. | [Google Drive API Scopes](https://developers.google.com/drive/api/guides/api-specific-auth) documentation |
   
6. Click **Authorize**.

---
