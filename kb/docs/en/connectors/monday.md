---
url: 'https://docs.workato.com/en/connectors/monday.md'
description: >-
  The Monday connector enables you to automate work management and project
  collaboration workflows across the Monday cloud work platform.
---

# Monday

[Monday](https://monday.com/) provides a cloud platform for teams to build applications and manage work. It enables teams to design workflows, manage projects, and collaborate in one place to simplify business operations.

## Prerequisites

Set up a [Monday](https://monday.com/) account with API access before using the Monday connector in Workato. Verify that your account includes permissions to access API tokens. Follow the steps in the [Access API tokens in Monday account](#accessing-api-tokens) section to retrieve your token.

Refer to the Monday [documentation](https://support.monday.com/hc/en-us/articles/115005305649-Get-started-with-monday-com) for more information.

### Access API tokens in Monday

Complete the following steps to retrieve your API token from Monday:

1. Log in to your [Monday](https://auth.monday.com/auth/login_monday/) account.
   
2. Click your profile picture.
   
3. Go to **Administration > Connections > API**.
   
   ![Monday Dashboard](/assets/monday-api-token.DlUq1Mp-.png)_Monday API Token_
   
4. Copy your personal token and store it securely. This token is required to set up your Workato connection.
   

Refer to the [Monday authentication](https://developer.monday.com/api-reference/docs/authentication) documentation for more information.

## Connection setup

The Monday connector supports custom authentication to connect to Monday. Complete the following steps to set up a connection in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select **Monday** as your connection on the **New connection** page.
   
3. Provide a name for your connection in the **Connection name** field. ![Monday connection setup](/assets/monday-connection-setup.uBdN70h4.png)_Monday connection setup_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter the **API v2 Token** for your Monday account from which you saved during the preceding steps.
   
6. Click **Connect**.
   

## Actions

![Monday Actions](/assets/monday-actions.B3Ujx0a7.png)_Monday actions_

---
