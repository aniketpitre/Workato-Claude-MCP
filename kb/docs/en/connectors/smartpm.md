---
url: 'https://docs.workato.com/en/connectors/smartpm.md'
description: >-
  The SmartPM connector lets you automate construction project management
  workflows: create, update, delete, search, and retrieve records.
---

# SmartPM

[SmartPM](https://smartpm.com/) is a construction project management tool that streamlines project data, analyzes key metrics, and provides real-time insights. This connector automates project and schedule management and enables your team to organize and manage work efficiently.

## Prerequisites

Ensure you have an active SmartPM account with permissions to access the SmartPM APIs before using the connector in Workato. If you don't have an account, go to the SmartPM [registration page](https://smartpm.com/demo) to sign up.

## Set up your SmartPM connection

Complete the following steps to use the SmartPM connector in Workato:

- [Generate a personal API key](#generate-a-personal-api-key)
- [Set up your SmartPM connection in Workato](#connection-setup)

### Generate a personal API key

Complete the following steps to generate a personal API key in SmartPM:

1. Log in to [SmartPM](https://smartpm.com/demo) with your credentials.
   
2. Click **Admin** in the navigation menu.
   
3. Click **Integrations**.
   
4. Click **Create integration**.
   
5. Provide a **name** for your API key and click **Add**.
   
6. Copy the generated API key. You can't access it again.
   
7. Use this API key and your company ID to authenticate with SmartPM public APIs. Refer to the [SmartPM API documentation](https://developers.smartpmtech.com/#section/Authentication) for more details.
   

## Set up your SmartPM connection in Workato

Workato uses API key authentication to connect to SmartPM. Complete the following steps to create a connection:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select **SmartPM** as your connection on the **New connection** page.
   
3. Provide a unique name for your connection in the **Connection name** field. ![SmartPM connection setup](/assets/smartpm-connection-setup._GK3eSww.png)_SmartPM connection setup_
   
4. Select the **Location** where you plan to save the connection.
   
5. Enter your SmartPM **API key**.
   
6. Enter your SmartPM **Company ID**. Refer to the [SmartPM documentation](https://developers.smartpmtech.com/#section/Authentication/Company-ID) for more details.
   
7. Click **Connect**.

---
