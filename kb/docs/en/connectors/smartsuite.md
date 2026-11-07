---
url: 'https://docs.workato.com/en/connectors/smartsuite.md'
description: >-
  The SmartSuite connector lets you automate collaborative work management:
  create, update, delete, search, and retrieve records.
---

# SmartSuite

[SmartSuite](https://www.smartsuite.com/) is a collaborative work management platform that combines the capabilities of spreadsheets, databases, and project management tools into one flexible and intuitive solution. It allows teams to manage workflows, track data, and build custom solutions.

## Prerequisites

Before using the SmartSuite connector in Workato, ensure you have an active SmartSuite account with appropriate permissions to access APIs and use the Developer Portal.

### Generate an API key

Complete the following steps to generate an API key in SmartSuite:

1. [Sign in](https://app.smartsuite.com/authenticate/login) to your SmartSuite account.
   
2. Click your username/avatar in the top-right corner.
   
3. Click **My Profile**.
   
4. Select **API Key**.
   
5. Click **Generate New Key**.
   
   ![Generate a SmartSuite API key](/assets/smartsuite-api-key.DRqMK5pf.png)_Generate a SmartSuite API key_
   
6. Copy the API key and store it in a secure location.
   

Refer to the SmartSuite [Generating an API Key](https://help.smartsuite.com/en/articles/4855681-generating-an-api-key) documentation for more information.

## How to connect to SmartSuite

The SmartSuite connector supports API key authentication to connect to SmartSuite.

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `SmartSuite` as your connection on the **New connection** page.
   
3. Provide a unique name for your connection in the **Connection name** field.
   
   ![Connect to SmartSuite](/assets/smartsuite-connection.WjJ-fGdY.png)_Connect to SmartSuite_
   
4. Use the **Location** drop-down menu to select the project or folder where you plan to store your connection.
   
5. Enter the first 8 characters after `https://app.smartsuite.com/` in the **Account ID** field. For example, if your URL is `https://app.smartsuite.com/12345678/home`, enter `12345678`. Refer to [Retrieving your Workspace ID](https://help.smartsuite.com/en/articles/6096587-retrieving-your-api-key-and-workspace-id#h_1464466de1) for more information.
   
6. Enter the **API Key** for your SmartSuite account.
   
7. Click **Connect**.

---
