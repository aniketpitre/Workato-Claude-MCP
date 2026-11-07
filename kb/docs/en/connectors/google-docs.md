---
url: 'https://docs.workato.com/en/connectors/google-docs.md'
description: >-
  The Google Docs connector enables you to automate document workflows,
  creating, editing, and collaborating on cloud-based documents in real time.
---

# Google Docs

[Google Docs](https://workspace.google.com/intl/en_in/products/docs/) is a cloud-based word processor that enables users to create, edit, and collaborate on documents in real-time. It integrates seamlessly with Google Workspace and offers features like commenting, version history, and smart editing tools to enhance productivity.

## API version

The Google Docs connector uses the [Google Docs API v1](https://developers.google.com/workspace/docs/api/reference/rest).

## Connection setup

The Google Docs connector supports the following authentication types:

- [OAuth 2.0](/en/connectors/google-docs#oauth2)
- [Service account](/en/connectors/google-docs#service-account)

> **SERVICE ACCOUNT AUTHENTICATION**
> 
> You can use a service account to authenticate without a personal user account. For consistent use, Workato recommends service account authentication.

### Download the Google Docs connector from the Community library

View steps to download the Google Docs connector from the community library

Complete the following steps to install the Google Docs connector from the [community library](https://www.workato.com/browse/connectors):

1. Open the recipe editor and search for a connector. Alternatively, you can search for a connector in the [community library](https://www.workato.com/browse/connectors).
   
   ![Search for recipe editor](/assets/search-on-recipe-editor.VrZpf8zl.png)_Search for community connectors in the recipe editor_
   
2. Select the community connector you plan to install.
   
3. Click **Install** to install the connector from the community library.
   
   ![Click install](/assets/install-connector.BXpGZP9K.png)_Click **Install**_
   
4. Select **Release connector**. Alternatively, select **Review code** to review and modify the connector code before releasing it to the workspace.
   
   ![Release connector](/assets/release-and-review.kWToLwmF.png)_Release the connector_
   
5. Summarize any changes you made to the connector, then click **Release** to allow workspace collaborators to use the connector in recipes.
   
   ![The Confirm release dialog](/assets/release.CpEhhA-6.png)_The **Confirm release** dialog_
   

### OAuth 2.0

Complete the following steps to connect to Google Docs in Workato with OAuth 2.0 authentication:

- [Configure the OAuth consent screen](#consent-screen)
- [Delegate domain-wide authority to the service account](#delegate-authority-to-the-service-account)
- [Generate a client ID and client secret](#generate-client-id-and-secret)
- [Connect to Google Docs with OAuth 2.0](#oauth2-connect)

#### Google Docs setup

Complete the following steps to set up Google docs for OAuth 2.0 authentication:

##### Configure the OAuth consent screen

View OAuth consent screen steps

Complete the following steps to configure the OAuth consent screen:

1. Open the [Google Cloud Console](https://console.cloud.google.com) and go to **APIs & Services > OAuth consent screen**.
   
2. Click **Get started**.
   
3. Enter `Workato` in the **App name** field.
   
4. Enter an email in the **User support email** field.
   
5. Click **Next**.
   
6. Select **External** as the **Audience**. Refer to [Manage App Audience](https://support.google.com/cloud/answer/15549945?sjid=3043175652946470283-NC&authuser=1) to learn more about user types.
   
7. Click **Next**.
   
8. Enter an email address in the **Contact information** section.
   
9. Select the checkbox to agree to Google API Services User Data Policy and click **Continue**. Refer to [Google API Services User Data Policy](https://developers.google.com/terms/api-services-user-data-policy) for more information.
   
10. Click **Create**.
    
11. Click the **Data access** tab and select **Add or Remove Scopes**.
    
12. Select the necessary scopes, such as:
    
    - `https://www.googleapis.com/auth/documents`
    - `https://www.googleapis.com/auth/documents.readonly`
13. Click **Save**.
    

##### Delegate domain-wide authority to the service account

View delegate domain-wide authority to the service account steps

Complete the following steps to delegate domain-wide authority to the service account:

1. Open the [Google Admin console](https://admin.google.com/) and go to the **Main menu**.
   
2. Go to **Security > Access and data control > API Controls**.
   
3. Go to **Security > Access and data control > API Controls > Domain-wide Delegation**.
   
4. Click **Manage Domain Wide Delegation**.
   
5. Click **Add new**.
   
6. Enter the **Client ID** from the service account JSON file.
   
7. Add the necessary scopes for your [OAuth consent screen configuration](#consent-screen) in the **OAuth scopes (comma-delimited)** field.
   
8. Click **Authorize**.
   

##### Generate a client ID and client secret

Refer to the Google [Manage OAuth Clients](https://support.google.com/cloud/answer/15549257?hl=en&ref_topic=15540269&sjid=11430921100578225870-NC) guide to create a client ID and secret using `https://www.workato.com/oauth/callback` as the redirect URI.

#### Connect to Google Docs with OAuth 2.0

View connect to Google Docs with OAuth 2.0 steps

Complete the following steps to set up your connection with OAuth 2.0 authentication:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Google Docs` and select it as your app.
   
3. Provide a name for your connection in the **Connection name** field. ![OAuth 2.0 connection](/assets/oauth2.BZplQRFm.png)_OAuth 2.0 connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter the **Client ID** and **Client secret**. Refer to the Google [Manage OAuth Clients](https://support.google.com/cloud/answer/15549257?hl=en&ref_topic=15540269&sjid=11430921100578225870-NC) guide to generate these values using `https://www.workato.com/oauth/callback` as the redirect URI.
   
6. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
7. Click **Sign in with Google**.
   

### Service account authentication

A Google service account is a specialized Google account associated with a Google Cloud Project (GCP) that can run API requests on your behalf.

Service accounts provide the following benefits:

- **Continuous operation:** Service accounts ensure that operations continue even if individual user permissions change.
- **Dedicated permissions:** Service accounts can only access projects that you share with them.
- **Dedicated API quotas:** You can manage a service account's API quotas through GCP and request quota increases directly from Google.

Refer to the [Google service account documentation](https://cloud.google.com/iam/docs/understanding-service-accounts) to learn more about service accounts.

> **PREREQUISITES**
> 
> You must [Enable the Google Docs API](https://support.google.com/googleapi/answer/6158841) in the Google Cloud API console before you can connect to Google Docs with service account authentication.

Complete the following steps to connect to Google Docs in Workato with service account authentication:

- [Create a service account and generate a private key](/en/connectors/google-docs#set-up-a-google-service-account)
- [Share Google Docs with the service account](/en/connectors/google-docs#share-docs)
- [Connect to Google Docs with service account authentication](#service-account-connect)

#### Google Docs setup

Complete the following steps to set up Google Docs for service account authentication:

##### Set up a Google service account

View set up a Google service account steps

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
   

##### Share Google Docs with the service account

View share Google Docs with the service account steps

Complete the following steps to share a Google Doc with the service account:

1. Open Google Docs and select the document you plan to integrate.
   
2. Click **Share** and enter the service account email.
   
3. Assign the appropriate permissions.
   
4. Click **Send**.
   

#### Connect to Google Docs with service account authentication

View connect to Google Docs with service account authentication steps

Complete the following steps to set up your connection with a service account:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Google Docs` and select it as your app.
   
3. Provide a name for your connection in the **Connection name** field. ![Service account connection](/assets/service-account.BTGgHdjM.png)_Service account connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Auth type** drop-down menu to select **Service account**.
   
6. Enter your service account email address in the **Service account email** field.
   
7. Enter your private key from the downloaded JSON in the **Private key** field. Refer to [Create a service account and generate a private key](#set-up-a-google-service-account) for more information.
   
8. Click **Sign in with Google**.

---
