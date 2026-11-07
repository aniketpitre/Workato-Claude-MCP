---
url: 'https://docs.workato.com/en/connectors/google-slides.md'
description: >-
  The Google Slides connector lets you automate updates to presentations by
  retrieving and modifying slide content in real time.
---

# Google Slides

[Google Slides](https://www.google.com/slides/about/) is a cloud-based presentation software that enables real-time collaboration and editing. Teams can create, share, and present decks directly from their browsers without additional software.

Use the Google Slides connector in Workato to retrieve slide content, update text, or replace images in existing decks. For example, you can populate a sales presentation template with CRM data or update a report deck with metrics pulled from a spreadsheet.

## API version

The Google Slides connector uses the [Google Slides API v1](https://developers.google.com/slides/reference/rest).

## How to connect to Google Slides

The Google Slides connector supports the following authentication methods:

- [OAuth 2.0](#oauth-2-0)
- [Service account](#service-account)

> **SERVICE ACCOUNT AUTHENTICATION**
> 
> You can use a service account to authenticate without a personal user account. For consistent use, Workato recommends service account authentication.

### OAuth 2.0

Complete the following steps to set up an OAuth 2.0 connection:

> **PREREQUISITES**
> 
> OAuth 2.0 authentication requires that you add the following redirect URI to your credentials in the [Google Developers Console](https://console.developers.google.com/): `https://www.workato.com/oauth/callback`

1. Click **Create > Connection** or press C twice.
   
2. Provide a name for your connection in the **Connection name** field.
   
   ![OAuth 2.0 connection fields](/assets/oauth-connection.DOuI3Woe.png)_OAuth 2.0 connection fields_
   
3. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
4. Search for and select **Google Slides** as your connection.
   
5. Use the **Auth type** drop-down menu to select `OAuth 2.0`.
   
6. Enter your **Client ID** and **Client secret**. You can retrieve these from the [Google Developers Console](https://console.developers.google.com/) under **APIs & Services > Credentials**.
   
7. Click **Sign in with Google**.
   
8. Sign in with your Google account and click **Allow** to grant Workato access.
   

### Service account

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
   

The email associated with your service account must have access to the Google Slides presentations used in recipes. You can share presentations directly from the Google Slides UI.

#### Complete setup in Workato

Service account authentication requires the following:

- [Create a service account and generate a private key](#set-up-a-google-service-account)
- [Enable the Google Slides API](https://console.developers.google.com/)

1. Click **Create > Connection** or press C twice.
   
2. Search for and select **Google Slides** as your connection.
   
3. Provide a name for your connection in the **Connection name** field.
   
   ![Google Slides service account connection fields](/assets/service-account-connection.CZj4nPFp.png)_Google Slides service account connection fields_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Auth type** drop-down menu to select `Service account`.
   
6. Enter the **Service account email**.
   
7. Paste the entire **Private key**, including `-----BEGIN PRIVATE KEY-----` and `-----END PRIVATE KEY-----\n`.
   
8. Click **Sign in with Google**.

---
