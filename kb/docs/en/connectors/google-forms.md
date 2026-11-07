---
url: 'https://docs.workato.com/en/connectors/google-forms.md'
description: >-
  The Google Forms connector enables you to automate workflows for forms,
  surveys, and quizzes, collecting responses and routing the data to other apps.
---

# Google Forms

[Google Forms](https://workspace.google.com/intl/en_in/products/forms/) is a free, web-based application from Google that allows users to create and distribute forms, surveys, and quizzes. The collected data is automatically stored in a spreadsheet.

## Prerequisites

To establish a connection to Google Forms, you must complete the following prerequisite steps:

1. [Create a project in Google Cloud Console](#console)
2. [Enable the Google Forms API](#api)
3. [Create OAuth 2.0 credentials](#oauth2)

After you complete these prerequisites, proceed to [connect to Google Forms on Workato](#connection-setup).

### Create a project in Google Cloud Console

Complete the following steps to create a project in Google Cloud Console:

1. Sign in to your [Google Cloud Console](https://console.cloud.google.com/welcome/new).
   
2. Click the **Select a project** drop-down menu and select **New project**.
   
3. Give the project a name and click **Create**.
   

### Enable the Google Forms API

Complete the following steps to enable the Google Forms API:

1. In the **Cloud Console**, go to the **API & Services > Library**.
   
2. Search for **Google Forms API** and click **Enable**.
   

### Create OAuth 2.0 credentials

Complete the following steps to create OAuth 2.0 credentials:

1. Go to **API & Services > Credentials**.
   
2. Click **Create Credentials > OAuth Client ID**.
   
3. If prompted, configure the **OAuth consent screen**:
   
   - Choose **External** as the **User type**. Learn more about [user types](https://support.google.com/cloud/answer/15549945?sjid=3043175652946470283-NC&authuser=1).
   - Fill in the required fields, including **App name** and **Support email**.
   - Click **Save and Continue**.
4. Select **Web application** as the **Application type**.
   
5. Enter a name for the OAuth client.
   
6. Enter `https://www.workato.com/oauth/callback` in the **Authorized redirect URIs** field.
   
7. Click **Create**.
   
8. Click **Edit OAuth client** (pencil icon) to view the client ID and client secret.
   
9. Copy the **Client ID** and **Client secret** and store these values securely, as they are required to [complete setup in Workato](#connection-setup).
   
   Refer to the [Google Identity](https://developers.google.com/identity/protocols/oauth2#1.-obtain-oauth-2.0-credentials-from-the-dynamic_data.setvar.console_name.) documentation for further details on obtaining OAuth 2.0 credentials from the Google API console.
   

## How to connect to Google Forms

Workato supports OAuth 2.0 authentication to connect to Google Forms.

Complete the following steps to establish a Google Forms connection:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select **Google Forms** as your connection on the **New connection** page.
   
3. Provide a name for your connection in the **Connection name** field. ![Google Forms connection](/assets/connection.B32mMa18.png)_Google Forms connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter the client ID in the **Client ID** field.
   
6. Enter the downloaded client secret in the **Client secret** field.
   
7. Click **Sign in with Google**.

---
