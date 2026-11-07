---
url: 'https://docs.workato.com/en/connectors/google-sheets.md'
description: >-
  The Google Sheets connector enables you to automate spreadsheet workflows,
  writing and reading rows to move data between Google Sheets and other apps.
---

# Google Sheets

[Google Sheets](https://www.google.com/sheets/about/) is a powerful cloud application that enables real-time team collaboration on spreadsheets, available on any device.

Workato enables you to automate data entry into Google Sheets as part of a workflow. For example, configure this connector to add completed lead intake forms to a spreadsheet automatically. You can also read data from Google Sheets and transfer it to another app, such as moving respondents who completed a Google Form into a marketing campaign app or a CRM (customer relationship management) system.

> **FEATURE AVAILABILITY**
> 
> The Google Sheets connector isn't available to workspaces in the CN data center. This reflects local regulatory requirements and applies to our multi-tenant and [Virtual Private Workato (VPW)](/en/cloud-hosting-editions/hosting-editions#virtual-private-workato) offerings.

## API version

The Google Sheets connector uses [Google Sheets API v4](https://developers.google.com/sheets/api/reference/rest).

## How to connect to Google Sheets on Workato

The Google Sheets connector supports the following authentication methods:

- [OAuth 2.0](#oauth-2-0)
- [Service account](#service-account)

> **SERVICE ACCOUNT AUTHENTICATION**
> 
> You can use a service account to authenticate without a personal user account. For consistent use, Workato recommends service account authentication.

### OAuth 2.0

Complete the following steps to set up an OAuth 2.0 connection:

1. Click **Create > Connection** or press C twice.
   
2. Provide a name for your connection in the **Connection name** field.
   
   ![OAuth 2.0 connection fields](/assets/connection.C-Rm0AtF.png)_OAuth 2.0 connection fields_
   
3. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
4. Search for and select **Google Sheets** as your connection on the **New connection** page.
   
5. Use the **Authentication type** drop-down menu to select `OAuth 2.0`.
   
6. Optional. Use the **Disable formula** drop-down menu to select whether to disable adding and updating rows with formulas.
   
7. Optional. Use the **Custom OAuth profiles** drop-down menu to select a custom OAuth profile for this connection.
   
8. Click **Sign in with Google**.
   
9. Sign in with your Google account.
   
10. Click **Allow** to enable Workato to access your Google account.
    
    ![Click Allow to enable Workato to access your Google account](/assets/allow.DBxsc8xF.png)_Click **Allow** to enable Workato to access your Google account_
    

### Service account

A Google service account is a specialized Google account associated with a Google Cloud Project (GCP) that can run API requests on your behalf.

Service accounts provide the following benefits:

- **Continuous operation:** Service accounts ensure that operations continue even if individual user permissions change.
- **Dedicated permissions:** Service accounts can only access projects that you share with them.
- **Dedicated API quotas:** You can manage a service account's API quotas through GCP and request quota increases directly from Google.

Refer to the [Google service account documentation](https://cloud.google.com/iam/docs/understanding-service-accounts) to learn more about service accounts.

> **REAL-TIME TRIGGER LIMITATIONS**
> 
> Service accounts don't support real-time triggers for Google Sheets. Use [OAuth 2.0](#oauth-2-0) authentication to monitor Google Sheets in real-time.

#### Set up a Google service account

Service account authentication requires the following prerequisites:

- [Create a service account and generate a private key](#set-up-a-google-service-account)
- [Enable the Google Sheets API](https://support.google.com/googleapi/answer/6158841)

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
   

The email associated with your service account must have access to the Google Sheets you plan to use in recipes. You can share specific sheets from within Google Sheets.

![Share Google Sheets spreadsheets with your service account email](/assets/share.BjIcNo1z.png)_Share Google Sheets spreadsheets with your service account email_

#### Complete setup in Workato

Complete the following steps to set up a service account connection:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select **Google Sheets** as your connection.
   
3. Provide a name for your connection in the **Connection name** field.
   
   ![Google Sheet service account connection fields](/assets/SAconnection.CFNAkoVh.png)_Google Sheets service account connection fields_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authentication type** drop-down menu to select `Service account`.
   
6. Enter your service account email in the **GCP Project service account email** field.
   
7. Enter the entire **Private key** for your service account, including `-----BEGIN PRIVATE KEY-----` and `-----END PRIVATE KEY-----\n`.
   
8. Optional. Go to **Advanced settings** and use the **Requested permissions (Service auth scopes)** drop-down menu to adjust the scopes for your connection. Workato requests the **See and download all your Google Drive files** and **See, edit, create, and delete all your Google Sheets spreadsheets** permissions by default. The permissions you select from the drop-down menu overwrite the default permissions.
   
9. Optional. Use the **Disable formula** drop-down menu to select whether to disable adding and updating rows with formulas.
   
10. Optional. Use the **Custom OAuth profiles** drop-down menu to select a custom OAuth profile for this connection.
    
11. Click **Sign in with Google**.
    
12. Sign in with your Google account.
    
13. Click **Allow** to enable Workato to access your Google account.

---

---
url: >-
  https://docs.workato.com/en/connectors/google-sheets/trigger-new-row-my-drive.md
description: >-
  The New row in sheet in My Drive trigger in the Google Sheets connector picks
  up new rows added at the bottom of a sheet stored in My Drive.
---

# Google Sheets - New row in sheet in My Drive trigger

This trigger detects new rows added at the bottom of your selected sheet. When you start your recipe for the first time, this trigger picks up all existing rows in the sheet, excluding the header row. Subsequently, the trigger picks up new rows added to the end of the sheet.

Note that rows added in the middle of the sheet are not detected. Don't delete any row from the sheet when this trigger is active, as it can disrupt tracking.

> **LIMITATIONS**
> 
> This trigger works exclusively with My Drive. Use the [New row in sheet in Team Drive trigger](/en/connectors/google-sheets/trigger-new-row-team-drive) to monitor Team Drive.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Specify how frequently to check for new events. This field defaults to five minutes if left blank. The minimum value allowed is five minutes. |
| Spreadsheet | Select the spreadsheet to monitor for new rows. |
| Sheet | Choose the sheet to monitor for new rows. The sheet must have at least one header row and one data row. |
| Add column names manually? | Indicate whether to add column names manually. Defaults to `No`. |

## Output

| Output field | Description |
| --- | --- |
| Spreadsheet ID | The unique identifier for the spreadsheet. |
| Spreadsheet name | The name of the spreadsheet. |
| Sheet name | The sheet name. |
| Row number | The row number. |

---
