---
url: 'https://docs.workato.com/en/connectors/conga-composer.md'
description: >-
  Conga Composer is a Salesforce application that allows users to create and
  deliver pixel-perfect documents, presentations, and reports using data from
  Salesforce. Conga Composer generates customized documents using templates.
---

# Conga Composer

[Conga Composer](https://conga.com/) is a Salesforce application that allows users to create and deliver pixel-perfect documents, presentations, and reports using data from Salesforce. Conga Composer generates customized documents using templates.

This connector has the following capabilities:

- Merge a document with new leads in a CRM application
- Download a document and save with On-prem location

## Install Conga Composer from the community library

Complete the following steps to install the Conga Composer connector from the [community library](https://www.workato.com/browse/connectors):

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

The Conga Composer connector uses OAuth 2.0 authentication.

### Conga Composer setup

Complete the following steps to get a client ID and client secret in Conga Composer:

1. Sign in to your Conga account.
   
2. Go to **Org Management > Conga API Connections**.
   
3. Click **Add API to API Connection**.
   
4. Select **External Identifier**.
   
5. Click **Save and Generate Client Secret**. You use these values to create a connection in Workato.
   

### Connect to Conga Composer in Workato using {auth-type}

Complete the following steps to connect to Conga Composer in Workato:

1. Click **Create > Connection**.
   
2. Search for `Conga Composer` and select it as your app on the **New connection** page.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Conga Composer connection](/assets/conga-composer-connection-setup.DSYBC7qj.png)_Create a Conga Composer connection._
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter your **Client ID**.
   
6. Enter your **Client secret**.
   
7. Select the **Environment** to use in your connection.
   
8. Click **Connect**.

---

---
url: >-
  https://docs.workato.com/en/connectors/conga-composer/compose-document-action.md
description: >-
  The Compose document action generates a document by merging one or more
  templates with data collected from multiple sources in Conga Composer.
---

# Conga Composer - Compose document action

The **Compose document** action generates a document by merging one or more templates with data collected from multiple sources in Conga Composer.

## Input

| Input field | Description |
| --- | --- |
| JSON data | Enter the JSON data to include in the document. |
| Destinations | Enter information about the sources you plan to use to compose a document. |
| Template sources | Enter information about sources for the template you plan to use. |
| Salesforce request | Enter a **Session ID** for a salesforce request you plan to use to compose a document. |
| Activity | Enter the **Attach operation** you plan to use to compose a document. |

## Output

| Output field | Description |
| --- | --- |
| Status code | A code indicating the status of the document. |
| Is successful | A message indicating if the action was successful. |
| Pre signed create response model | Information about the response model, including `Correlation ID` and `File info details list`. |

---

---
url: >-
  https://docs.workato.com/en/connectors/conga-composer/download-document-action.md
description: >-
  The Download document action downloads a document that you specify in Conga
  Composer.
---

# Conga Composer - Download document action

The **Download document** action downloads a document that you specify in Conga Composer.

## Input

| Input field | Description |
| --- | --- |
| File download URL | Enter the ID for the document you plan to download. |

## Output

| Output field | Description |
| --- | --- |
| File contents | The contents fo the downloaded file. |

---
