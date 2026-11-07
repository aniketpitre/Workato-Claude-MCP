---
url: 'https://docs.workato.com/en/connectors/google-drive.md'
description: Connects Workato to Google Drive to build automations.
---

# Google Drive

[Google Drive](https://www.google.com/drive/) is a popular file storage and collaboration environment. The Google Drive connector enables you to build powerful automations around Google Drive and connect with other applications.

> **FEATURE AVAILABILITY**
> 
> The Google Drive connector isn't available to workspaces in the CN data center. This reflects local regulatory requirements and applies to our multi-tenant and [Virtual Private Workato (VPW)](/en/cloud-hosting-editions/hosting-editions#virtual-private-workato) offerings.

## API version

The Google Drive connector uses the [Google Drive API v3](https://developers.google.com/drive/api/reference/rest/v3).

## Connection setup

The Google Drive connector supports the following authentication types:

- [OAuth 2.0 authentication](/en/connectors/google-drive#oauth2)
- [Service account](/en/connectors/google-drive#service-account)

### OAuth 2.0 authentication

#### Minimum and default scopes

Workato requests the following scopes by default in addition to the scopes you select:

- `drive`: See, edit, create, and delete all your Google Drive files
- `drive.readonly`: See and download all your Google Drive files

Additionally, your Google account must have the `Edit` permission for all files and folders that you plan to use in Workato recipes.

#### Connect to Google Drive using OAuth 2.0

Complete the following steps to set up an OAuth 2.0 connection to Google Drive in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select **Google Drive** as your connection on the **New Connection** page.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Connection setup](/assets/google-drive-connection-setup.o_esWDm7.png)_Google Drive connection setup_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authentication type** drop-down menu to select **OAuth 2.0**.
   
6. Optional. Expand the **Advanced settings** section and use the **Requested permissions** drop-down menu to specify OAuth scopes to request for your connection.
   
7. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile to use for the connection.
   
8. Click **Sign in with Google**.
   
9. Click **Allow** to authorize Workato to access your Google Drive.
   

### Service account authentication

A Google service account is a specialized Google account associated with a Google Cloud Project (GCP) that can run API requests on your behalf.

Service accounts provide the following benefits:

- **Continuous operation:** Service accounts ensure that operations continue even if individual user permissions change.
- **Dedicated permissions:** Service accounts can only access projects that you share with them.
- **Dedicated API quotas:** You can manage a service account's API quotas through GCP and request quota increases directly from Google.

Refer to the [Google service account documentation](https://cloud.google.com/iam/docs/understanding-service-accounts) to learn more about service accounts.

#### Set up a Google service account

Complete the following steps to set up a Google service account:

1. [Create a service account](https://cloud.google.com/iam/docs/creating-managing-service-accounts#creating) in your GCP project.
   
2. Go to **IAM & Admin > Service accounts**. Ensure your dashboard is scoped to the project that contains your service account.
   
   ![Check the scope of your dashboard.](/assets/service-project-scope.8Rf50DK2.png)_Check the scope of your dashboard._
   
3. Click the **Email** of the service account you intend to use.
   
   ![Click the email of the service account you intend to use.](/assets/service-email-button.C9qaZFkJ.png)_Click the **Email** of the service account you intend to use._
   
4. Copy the service account's **Email** and save it to configure your connection later.
   
   ![Copy the account's email](/assets/service-account-email.DM6BBBhN.png)_Copy the account's **Email**._
   
5. Go to the **KEYS** tab.
   
6. [Generate a private key](https://cloud.google.com/iam/docs/creating-managing-service-account-keys#creating_service_account_keys) and download it in JSON format. You can only download the key once.
   
7. Open the JSON file, then copy the entire private key from `-----BEGIN PRIVATE KEY-----` to `-----END PRIVATE KEY-----\n` (inclusive) and save it to configure your connection later.
   

#### Connect to Google Drive using service account authentication

Service account authentication requires the following prerequisites:

- [Create a service account and generate a private key](#service-account-setup)
- [Enable the Google Workspace API](https://support.google.com/googleapi/answer/6158841)

Complete the following steps to set up a service account connection to Google Drive in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Google Drive` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authentication type** drop-down menu to select **Service account**.
   
6. Enter the service account's email address in the **GCP project service account email** field.
   
   ![Retrieve your GCP Project service account email](/assets/service-auth-email.BdQybqOr.png)_Retrieve your GCP Project service account email_
   
7. Enter the **Private key**. Retrieve the private key from the downloadable JSON. Include both `-----BEGIN PRIVATE KEY-----` and `-----END PRIVATE KEY-----\n`.
   
8. Optional. Enter the **User email** of the account to impersonate. If left blank, Workato accesses the service account's Drive.
   
   User impersonation lets the service account act on behalf of a designated user, accessing and managing events in their Google Drive. Impersonating a user ensures data accuracy and enforces the permissions and access controls set for that user in Google Drive. Refer to Google's [Service account impersonation](https://cloud.google.com/iam/docs/service-account-impersonation) guide for more information.
   
9. Optional. Expand the **Advanced settings** section and use the **Requested permissions** drop-down menu to specify OAuth scopes to request for your connection.
   
10. Click **Sign in with Google**.

---
