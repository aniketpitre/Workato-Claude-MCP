---
url: 'https://docs.workato.com/en/connectors/google-vault.md'
description: >-
  The Google Vault connector enables you to automate information governance and
  eDiscovery workflows, retaining, holding, searching, and exporting Workspace
  data.
---

# Google Vault

[Google Vault](https://developers.google.com/vault) is an information governance and eDiscovery tool for Google Workspace. Vault allows you to retain, hold, search, and export Google Workspace data.

## API version

The Google Vault connector uses the [Google Vault API v1](https://developers.google.com/vault/reference/rest)

## Prerequisites

Before you establish a connection to Google Vault, complete the following steps:

- [Create an admin role with Vault privileges](#create-admin-role)
- [Assign Vault roles to users](#assign-vault-role)
- [Configure OAuth 2.0 for authorization](#configure-oauth2)
- [Delegate domain-wide authority to the service account](#domain-wide-delegation)

After you complete these prerequisites, proceed to [connect to Google Vault on Workato](#connection-setup).

### Create an admin role with Vault privileges

Complete the following steps to create an admin role with the required Vault privileges:

1. [Sign in](https://admin.google.com/) to the [Google Admin console](https://support.google.com/a/answer/182076) using a super administrator account. You must use a super administrator account to complete these steps.
   
2. Go to **Menu** > **Account** > **Admin roles** in the admin console.
   
3. Click **Create a new role**.
   
4. Enter a name and description for the role. For example, name the role based on the privileges it grants.
   
5. Click **Continue**.
   
6. Expand the **Google Vault** section.
   
7. Select the required privileges for the role. Refer to the Vault [Privileges reference](https://support.google.com/vault/answer/2799699#reference) for more information.
   
8. Click **Continue**.
   
9. Review the privileges you selected, then click **Create Role**.
   

### Assign Vault roles to users

Complete the following steps to assign Vault roles to users:

1. Go to **Menu** > **Directory** > **Users** in the admin console.
   
2. Find the user in the list. Refer to the [Find a user account](https://support.google.com/a/answer/33324) article for more details.
   
3. Click the user’s name to open their account page.
   
4. Scroll to and click **Admin roles and privileges**.
   
5. Click **Turn on** next to the prebuilt or custom role. If **Turn on** doesn’t appear, click under **Roles** to reveal the switches.
   
6. Click **Save**.
   

### Configure OAuth 2.0 for authorization

Complete the following steps to configure OAuth 2.0 for your app:

1. Open the Google Cloud console and go to **Menu > APIs & Services > OAuth consent screen**.
   
2. Select the user type for your app, then click **Create**.
   
3. Click **Add or Remove Scopes**. Select the minimum scopes required for your app. For this connector, include the following:
   
   - [https://www.googleapis.com/auth/ediscovery](https://www.googleapis.com/auth/ediscovery)
   - [https://www.googleapis.com/auth/ediscovery.readonly](https://www.googleapis.com/auth/ediscovery.readonly)
4. Click **Save and Continue** after selecting the required scopes.
   

### Delegate domain-wide authority to the service account

Complete the following steps to delegate domain-wide authority:

1. Open the [Google Admin console](https://admin.google.com/) and go to **Menu > Security > Access and data control > API Controls**.
   
2. Select **Manage Domain Wide Delegation** in the **Domain wide delegation** pane.
   
3. Click **Add new**.
   
4. Enter the service account’s Client ID in the **Client ID** field. You can find your service account's client ID on the [Service accounts page](https://console.developers.google.com/iam-admin/serviceaccounts).
   
5. Enter the required scopes in the **OAuth** scopes field. For this connector, include the following scope:
   
   - `https://www.googleapis.com/auth/ediscovery`.
6. Click **Authorize**.
   

> **SERVICE ACCOUNT AUTHENTICATION**
> 
> You can use a service account to authenticate without a personal user account. For consistent use, Workato recommends service account authentication.

## Create a connection to Google Vault on Workato

Workato supports JWT authentication to connect to Google Vault.

Complete the following steps to connect Google Vault to Workato:

1. Click **Create** > **Connection**.
   
2. Search for and select **Google Vault** on the **New connection** page.
   
3. Provide a name for your connection in the **Connection name** field.
   
   ![Google Vault connection](/assets/google-vault-connection.BFpBEedh.png)_Google Vault connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter your service account email address in the **Issuer** field.
   
6. Paste the private key from the downloaded JSON file in the **Private key** field.
   
7. Enter the user email address that serves as the primary subject of the JWT in the **Email address** field.
   
8. Click **Sign in with Google** to complete the connection.

---

---
url: >-
  https://docs.workato.com/en/connectors/google-vault/add-accounts-to-hold-action.md
description: >-
  The add accounts to hold action enables you to add accounts to an
  accounts-based hold in Google Vault.
---

# Google Vault - Add accounts to hold action

The **Add accounts to hold** action enables you to add accounts to an account-based hold in Google Vault.

![Google Vault Add accounts to hold action](/assets/google-vault-add-accounts-to-hold-action.BOtWWXEX.png)_Google Vault **Add accounts to hold** action_

## Input

| Input Field | Description |
| --- | --- |
| Hold ID | Use the **Hold ID** drop-down menu to select a hold from Google Vault, or enter the ID manually |
| Matter ID | Use the **Matter ID** drop-down menu to select a hold from Google Vault, or enter the ID manually |
| Account emails | Enter a comma-separated list of email addresses for the accounts to add to the hold. |
| Account IDs | Enter a comma-separated list of account IDs to add to the hold. Specify either emails or account IDs, not both. |
| Details output field | Describe custom output fields present in the details of the output schema. |

## Output

| Output Field | Description |
| --- | --- |
| Account ID | ID of the account added to the hold. |
| Hold time | Timestamp of when the account was put on hold. |
| Email | The primary email address of the account. |
| First name | The first name of the account holder. |
| Last name | The last name of the account holder. |
| Code | The HTTP response status code. |
| Message | A developer-facing error message, if any. |
| Details | A list of messages that contains additional error details, if any. |

---
