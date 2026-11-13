---
url: 'https://docs.workato.com/en/connectors/ynab.md'
description: >-
  YNAB (You Need A Budget) is a personal budgeting application built on
  zero-based budgeting that helps individuals and households plan their
  spending.
---

# YNAB

[YNAB](https://www.ynab.com) (You Need A Budget) is a personal budgeting application built on zero-based budgeting that helps individuals and households plan their spending. The YNAB connector lets you retrieve categories and budget months, search and update categories and transactions, and start recipes when transactions are created or updated.

## Install YNAB from the community library

Complete the following steps to install the YNAB connector from the [community library](https://www.workato.com/browse/connectors):

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

The YNAB connector uses personal access token authentication.

### YNAB setup

Complete the following steps in YNAB to create a personal access token. Refer to the [YNAB API](https://api.ynab.com/#personal-access-tokens) documentation for more information.

1. Go to **Account Settings > Developer Settings** in YNAB.
   
2. Click **New Token** to generate a token.
   
3. Enter a name for your token in the **Name** field.
   
4. Enter your account password when prompted.
   
5. Copy the token to use in Workato.
   

### Connect to YNAB using a personal access token

Complete the following steps to connect to YNAB in Workato:

1. Click **Create > Connection**.
   
2. Search for `YNAB` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![YNAB connection setup](/assets/ynab-connection-setup.BIEjHFQV.png)_YNAB connection setup_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter the token you created in YNAB in the **Personal access token** field.
   
6. Click **Connect**.

---
