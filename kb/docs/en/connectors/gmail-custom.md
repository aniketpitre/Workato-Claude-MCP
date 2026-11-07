---
url: 'https://docs.workato.com/en/connectors/gmail-custom.md'
description: >-
  Gmail (Custom) uses a Google service account to manage Gmail settings and
  messages on behalf of a domain user.
---

# Gmail (Custom)

The [Gmail (Custom)](https://www.google.com/gmail/) connector uses a Google service account to manage Gmail settings and messages on behalf of a domain user. This connector supports actions to forward addresses, delegate, configure vacation responder settings, configure IMAP and POP settings, and enable Pub/Sub notifications for new messages. Each action specifies the mailbox to act on through a **User id** field, so a single connection can manage any mailbox the service account is authorized to impersonate.

## Install Gmail (Custom) from the community library

Complete the following steps to install the Gmail (Custom) connector from the [community library](https://www.workato.com/browse/connectors):

1. Open the recipe editor and search for a connector. Alternatively, you can search for a connector in the [community library](https://www.workato.com/browse/connectors).
   
   ![Search for recipe editor](/assets/search-on-recipe-editor.VrZpf8zl.png)_Search for community connectors in the recipe editor_
   
2. Select the community connector you plan to install.
   
3. Click **Install** to install the connector from the community library.
   
   ![Click install](/assets/install-connector.BXpGZP9K.png)_Click **Install**_
   
4. Select **Release connector**. Alternatively, select **Review code** to review and modify the connector code before releasing it to the workspace.
   
   ![Release connector](/assets/release-and-review.kWToLwmF.png)_Release the connector_
   
5. Summarize any changes you made to the connector, then click **Release** to allow workspace collaborators to use the connector in recipes.
   
   ![The Confirm release dialog](/assets/release.CpEhhA-6.png)_The **Confirm release** dialog_
   

## Connection setup

The Gmail (Custom) connector uses OAuth 2.0 authentication.

### Gmail (Custom) setup

To connect to Gmail (Custom) in Workato, set up the following:

- [Set up your Google Cloud project](#cloud-project)
- [Set up your service account](#service-account-prerequisites)

#### Set up your Google Cloud project

Complete the following steps to set up your Google Cloud project:

1. Log in to your [Google Cloud Console](https://cloud.google.com/cloud-console).
   
2. Create or select an existing Google Cloud project.
   
3. Enable the **Gmail API** in the Google Cloud Console.
   
   1. Click **APIs & Services > Enabled APIs & Services**.
      
   2. Search for and select **Gmail API** in the search bar.
      
   3. Click **Enable**.
      

#### Set up your service account

Complete the following steps to create a service account with domain-wide delegation:

1. Log in to your [Google Cloud Console](https://cloud.google.com/cloud-console).
   
2. Click **Select or create a New Project** in the project dropdown.
   
3. Go to **IAM & Admin > Service Accounts** and click **Create Service Account**.
   
4. Enter a name for the service account in the **Name** field.
   
5. Click **Create and Continue > Done**.
   
6. Click on your newly created service account and go to the Keys tab.
   
   1. Click **Add Key > Create New Key**.
      
   2. Download the service account JSON key file.
      
7. In the Google Admin console, authorize the service account's client ID and grant the following OAuth scopes:
   
   - `https://www.googleapis.com/auth/gmail.settings.sharing`
   - `https://mail.google.com/`
   - `https://www.googleapis.com/auth/gmail.modify`
   - `https://www.googleapis.com/auth/gmail.readonly`
   - `https://www.googleapis.com/auth/gmail.settings.basic`

Super admin access is required to authorize the service account's client ID and grant domain-wide delegation. Refer to the [Google Workspace admin help documentation](https://support.google.com/a/answer/162106) for more information.

### Connect to Gmail (Custom) using OAuth 2.0

Complete the following steps to connect to Gmail (Custom) in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select **Gmail (Custom)** as your connection on the **New connection** page.
   
3. Provide a unique name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter the **client\_email** value from the service account JSON key in the **Issuer** field.
   
6. Enter your JSON private key in the **Private key** field. Refer to [Google's service account documentation](https://developers.google.com/identity/protocols/oauth2/service-account/) to learn more about service accounts.
   
7. Click **Connect**.

---

---
url: >-
  https://docs.workato.com/en/connectors/gmail-custom/create-email-delegation-access-action.md
description: >-
  The Create email delegation access action adds a delegate to a Gmail mailbox
  with its verification status set to accepted.
---

# Gmail (Custom) - Create email delegation access action

The **Create email delegation access** action adds a delegate to a Gmail mailbox and sets its verification status to **accepted** without sending a verification email. The delegate must be a member of the same Google Workspace organization as the mailbox owner. This action requires the `https://www.googleapis.com/auth/gmail.settings.sharing` OAuth scope.

## Input

| Input field | Description |
| --- | --- |
| User id | Enter the user's email address. |
| Delegate email | Enter the email address of the user to add as a delegate. |

## Output

| Output field | Description |
| --- | --- |
| Delegate email | The delegate's email address. |
| Verification status | The verification status of the delegate, such as `accepted` or `pending`. |
| User id | The user's email address. |

---

---
url: >-
  https://docs.workato.com/en/connectors/gmail-custom/create-forwarding-address-action.md
description: >-
  The Create forwarding address action creates a forwarding address for a Gmail
  mailbox.
---

# Gmail (Custom) - Create forwarding address action

The **Create forwarding address** action creates a forwarding address for a Gmail mailbox. Gmail sends a message to the recipient and sets the address's verification status to **pending** if ownership verification is required. The address is created with its verification status set to **accepted** if ownership verification isn't required. This action requires the `https://www.googleapis.com/auth/gmail.settings.sharing` OAuth scope.

## Input

| Input field | Description |
| --- | --- |
| User id | Enter the user's email address. |
| Forwarding email | Enter an email address to which messages can be forwarded. |

## Output

| Output field | Description |
| --- | --- |
| Forwarding email | The forwarding address. |
| Verification status | The verification status of the forwarding address, such as `accepted` or `pending`. |
| User id | The user's email address. |

---
