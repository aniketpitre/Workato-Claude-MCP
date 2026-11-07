---
url: 'https://docs.workato.com/en/connectors/google-calendar.md'
description: >-
  Google Calendar is a cloud-based calendar application that enables scheduling,
  event tracking, reminders, and more. You can use Workato to synchronize data
  with Google Calendar automatically as part of a workflow.
---

# Google Calendar

[Google Calendar](https://www.google.com/calendar/) is a cloud-based calendar application that enables scheduling, event tracking, reminders, and more.

You can use Workato to synchronize data with Google Calendar automatically as part of a workflow. For example, you can create events in your calendar when a meeting is scheduled in another platform or app. You can also retrieve details about calendar events and synchronize them with other tools, such as CRMs or project management platforms.

> **FEATURE AVAILABILITY**
> 
> The Google Calendar connector isn't available to workspaces in the CN data center. This reflects local regulatory requirements and applies to our multi-tenant and [Virtual Private Workato (VPW)](/en/cloud-hosting-editions/hosting-editions#virtual-private-workato) offerings.

## API version

The Google Calendar connector uses the [Google Calendar API v3](https://developers.google.com/calendar/api/v3/reference).

## How to connect to Google Calendar

Workato supports the following types of connections to Google Calendar:

- [OAuth 2.0 authentication](#oauth)
- [Service account authentication](#service-account-authentication)
  - [Minimum scopes for service account connections](#minimum-scopes-for-service-account-connections)
  - [Set up a Google service account](#set-up-a-google-service-account)
  - [Enable the Google Calendar API](#api-setup)
  - [Complete setup in Workato](#setup)

You can use a service account to authenticate without a personal user account. Workato recommends service account authentication for consistent use.

### OAuth 2.0 authentication

Complete the following steps to set up your Google Calendar connection using OAuth 2.0:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Google Calendar` as your connection on the **New connection** page.
   
3. Provide a name for your connection in the **Connection name** field.
   
4. Select the project where you plan to store the connection from the **Location** drop-down menu.
   
5. Select **OAuth 2.0** as the **Authentication type**.
   
6. Click **Sign in with Google**, then sign in to your Google account. Ensure your Google account has sufficient permissions to manage the events and calendars you plan to use in Workato. ![Click Sign in with Google](/assets/google-calendar-sign-in-with-google.DQ57V-DM.png)_Click **Sign in with Google**._
   

### Service account authentication

A Google service account is a specialized Google account associated with a Google Cloud Project (GCP) that can run API requests on your behalf.

Service accounts provide the following benefits:

- **Continuous operation:** Service accounts ensure that operations continue even if individual user permissions change.
- **Dedicated permissions:** Service accounts can only access projects that you share with them.
- **Dedicated API quotas:** You can manage a service account's API quotas through GCP and request quota increases directly from Google.

Refer to the [Google service account documentation](https://cloud.google.com/iam/docs/understanding-service-accounts) to learn more about service accounts.

Service account authentication consists of the following actions:

- [Set up a Google service account](#set-up-a-google-service-account)
- [Enable the Google Calendar API](#api-setup)
- [Complete setup in Workato](#setup)

#### Minimum scopes for service account connections

The following scopes are required to connect to Google Calendar using a service account:

- `https://www.googleapis.com/auth/calendar`
- `https://www.googleapis.com/auth/calendar.events`
- `https://www.googleapis.com/auth/admin.directory.resource.calendar`
- `https://www.googleapis.com/auth/tasks`
- `https://www.googleapis.com/auth/userinfo.email`

A `401 Unauthorized error` may occur when the service account uses the `Owner` role or lacks required scopes. Assign the `Editor` role to the service account in the Google Cloud Console and confirm it includes all required scopes listed above. This ensures the service account can authenticate and access Google Calendar successfully.

Refer to the [Google Calendar API scopes](https://developers.google.com/calendar/api/auth) documentation for a complete list of supported scopes.

#### Set up a Google service account

Complete the following steps to set up a Google service account:

1. [Create a service account](https://cloud.google.com/iam/docs/creating-managing-service-accounts#creating) in your GCP project.
   
2. Go to **IAM & Admin > Service accounts**. Ensure your dashboard is scoped to the project that contains your service account. ![Check the scope of your dashboard.](/assets/service-project-scope.8Rf50DK2.png)_Check the scope of your dashboard._
   
3. Click the **Email** of the service account you intend to use. ![Click the email of the service account you intend to use.](/assets/service-email-button.C9qaZFkJ.png)_Click the **Email** of the service account you intend to use._
   
4. Copy the service account's **Email** and save it to configure your connection later. ![Copy the account's email](/assets/service-account-email.DM6BBBhN.png)_Copy the account's **Email**._
   
5. Go to the **KEYS** tab.
   
6. [Generate a private key](https://cloud.google.com/iam/docs/creating-managing-service-account-keys#creating_service_account_keys) and download it in JSON format. You can only download the key once.
   
7. Open the JSON file, then copy the entire private key from `-----BEGIN PRIVATE KEY-----` to `-----END PRIVATE KEY-----\n` (inclusive) and save it to configure your connection later.
   

#### Enable the Google Calendar API

You must enable the Google Calendar API before you return to Workato to finish setting up your connection.

1. Sign in to Google's [API library](https://console.developers.google.com/apis/library).
   
2. Search for and select the `Google Calendar API`.
   
3. Click **Enable** to enable the API. ![Enable the Google Calendar API](/assets/google-calendar-api.DMWBkrRb.png)_**Enable** the `Google Calendar API`_
   

#### Complete setup in Workato

Complete the following steps in Workato to set up your Google Calendar connection using a service account:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Google Calendar` as your connection on the **New connection** page.
   
3. Provide a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Select **Service account** as the **Authentication type**.
   
6. Enter your service account's **Private key**.
   
7. Provide the **User email** of the account you plan to impersonate.
   
   User impersonation lets the service account act on behalf of a designated user, accessing and managing events in their Google Calendar. Impersonating a user ensures data accuracy and enforces the permissions and access controls set for that user in Google Calendar. Refer to Google's [Service account impersonation](https://cloud.google.com/iam/docs/service-account-impersonation) guide for more information.
   
8. Click **Sign in with Google** to complete the setup. ![Configure Google Calendar service account connection](/assets/service-account-connection.CG2N5lxI.png)_Configure Google Calendar service account connection_

---
