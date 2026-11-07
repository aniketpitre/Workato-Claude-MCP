---
url: 'https://docs.workato.com/en/connectors/gmail.md'
description: Gmail is a popular email service used by both consumers and businesses alike.
---

# Gmail

[Gmail](https://www.google.com/gmail) is a popular email service used by both consumers and businesses alike. Users can access Gmail on the web and using third-party programs that synchronize email content through POP or IMAP protocols.

The Gmail connector enables you to build powerful automation around Gmail and connect with other applications.

> **FEATURE AVAILABILITY**
> 
> The Gmail connector isn't available to workspaces in the CN data center. This reflects local regulatory requirements and applies to our multi-tenant and [Virtual Private Workato (VPW)](/en/cloud-hosting-editions/hosting-editions#virtual-private-workato) offerings.

## API version

The Gmail connector uses the [Gmail REST API v1](https://developers.google.com/gmail/api/v1/reference/).

## How to connect to Gmail on Workato

Workato supports two types of connections to Gmail:

- [OAuth 2.0 authentication](/en/connectors/gmail#authentication-oauth)
- [Service account authentication](/en/connectors/gmail#authentication-service-account)

> **SERVICE ACCOUNT AUTHENTICATION**
> 
> You can use a service account to authenticate without a personal user account. For consistent use, Workato recommends service account authentication.

### Minimum and default scopes

The **See your primary Google Account email address** scope is required to establish a connection at a minimum.

Workato requests the following scopes by default if you don't request specific scopes:

- **See your primary Google Account email address**
- **See and edit your email labels**
- **Send email on your behalf**
- **View your email messages and settings**
- **Read, compose, and send emails from your Gmail account**

Ensure your Google Workspace Admin grants [domain-wide authority delegation](https://developers.google.com/cloud-search/docs/guides/delegation#delegate_domain-wide_authority_to_your_service_account) to your service account if you plan to use a service account to connect to Gmail. This allows it to impersonate the user email entered during connection setup, with the necessary scopes and permissions.

### OAuth 2.0 authentication

Complete the following steps to set up an OAuth 2.0 connection:

1. Sign in to your Workato account and navigate to the project where you plan to add your Gmail connection.
   
2. Click **Create > Connection** (or press C twice), then select **Gmail** as your connection.
   
3. Provide a **Connection name** that uniquely identifies the Gmail connection instance.
   
4. Click the **Authentication type** menu and select **OAuth 2.0**.
   
5. Optional. Click **Advanced settings** and select additional **OAuth 2.0 scopes**. If left blank, the following scopes are requested:
   
   - **See your primary Google Account email address**
   - **See and edit your email labels**
   - **Send email on your behalf**
   - **View your email messages and settings**
   - **Read, compose, and send emails from your Gmail account**
6. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
7. Click **Sign in with Google** and sign in to your Google account to complete the setup.
   

### Service account authentication

A Google service account is a specialized Google account associated with a Google Cloud Project (GCP) that can run API requests on your behalf.

Service accounts provide the following benefits:

- **Continuous operation:** Service accounts ensure that operations continue even if individual user permissions change.
- **Dedicated permissions:** Service accounts can only access projects that you share with them.
- **Dedicated API quotas:** You can manage a service account's API quotas through GCP and request quota increases directly from Google.

Refer to the [Google service account documentation](https://cloud.google.com/iam/docs/understanding-service-accounts) to learn more about service accounts.

![Getting GCP Project service account email](/assets/service-auth-email.BdQybqOr.png)_Obtain a GCP Project service account email_

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
   

#### Connect to a service account in Workato

Complete the following steps to set up a service account connection:

1. Sign in to your Workato account and navigate to the project where you plan to add your Gmail connection.
   
2. Click **Create > Connection** (or press C twice), then select **Gmail** as your connection.
   
3. Select the **Authentication type** drop-down menu.
   
4. Click **Sign in with Google** and sign in to your Google account to complete the setup.

---
