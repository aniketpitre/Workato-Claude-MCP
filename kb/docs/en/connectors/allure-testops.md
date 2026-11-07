---
url: 'https://docs.workato.com/en/connectors/allure-testops.md'
description: >-
  Allure TestOps is a test management platform by Qameta Software that provides
  end-to-end test management capabilities.
---

# Allure TestOps

[Allure TestOps](https://qameta.io/testops/) is a test management platform by Qameta Software that provides end-to-end test management capabilities, including test case management, test plan creation, launch execution, and result tracking. The Allure TestOps connector enables you to create, search, update, and delete projects, test cases, test plans, launches, and test results, and to retrieve and search custom fields and their values.

## Install Allure TestOps from the community library

Complete the following steps to install the Allure TestOps connector from the [community library](https://www.workato.com/browse/connectors):

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

The Allure TestOps connector uses Bearer token authentication.

### Allure TestOps setup

Complete the following steps to set up an instance URL and an API token to establish a connection to Allure TestOps in Workato:

1. Sign in to your Allure TestOps account.
   
2. Click the profile icon to open your profile settings.
   
3. Go to **API Tokens** and click **Generate a token**.
   
4. Copy and securely store the token for use in Workato.
   

### Connect to Allure TestOps using Bearer token authentication

Complete the following steps to connect to Allure TestOps in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Allure TestOps` as your connection on the New connection page.
   
3. Provide a name for your connection in the **Connection name** field.
   
   ![Create an Allure TestOps connection.](/assets/allure-testops-create-connection.ClUguidC.png)_Create an Allure TestOps connection._
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter your full Allure TestOps URL in the **Instance URL** field, for example `https://yourcompany.testops.cloud`.
   
6. Enter the **API token** you generated in Allure TestOps.
   
7. Click **Connect**.

---
