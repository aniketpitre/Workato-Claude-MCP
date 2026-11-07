---
url: 'https://docs.workato.com/en/connectors/pagerduty.md'
description: >-
  The PagerDuty connector lets you search, get, update, and annotate incidents,
  send events, and trigger recipes on new incidents and notifications.
---

# PagerDuty

[PagerDuty](https://www.pagerduty.com/) is an incident response platform and on-call management service.

## API version

This connector uses the [PagerDuty REST API](https://developer.pagerduty.com/api-reference/reference/REST/openapiv3.json).

## Prerequisites

You must have the following to establish a connection to PagerDuty:

- API key
- Write and read permissions

### Create an API key

You must create an API key (PagerDuty integration key) to connect to Workato. PagerDuty supports the following types of API keys:

- **General access API key**: This API key has access to all objects in your PagerDuty instance.
- **Personal API key**: This API key is restricted according to the user's permissions. This requires PagerDuty [advanced permissions](https://support.pagerduty.com/docs/advanced-permissions).

Complete the following steps to create a PagerDuty API key:

1. Go to **Integrations > Developer Tools > API Access Keys** and click **Create New API Key**.
   
   Alternatively, go to **Profile > User settings** to create a Personal API key.
   
2. Enter a description that helps identify the key, such as **Workato integration key**. Ensure that you don't select `Read-only API Key`. This connection requires read and write permissions to function properly.
   
   ![Provide the API key with write permissions](/assets/api-key-permissions.DCypS1mp.png)_Provide the API key with write permissions_
   
3. Store the API key in a secure location. Use this API key to authenticate with Workato.
   

### Permissions

You must have an Admin, Global Admin, or Account Owner role in PagerDuty to create an API key. Contact an Admin or Account Owner in your organization to create this key if you don't have one of these roles.

## How to connect to PagerDuty on Workato

Complete the following steps to connect to PagerDuty in Workato:

1. Select **Create > Connection** or press C twice.
   
2. Search for `PagerDuty` on the **New connection** page and select it.
   
3. Enter a name in the **Connection name** field.
   
   ![Connect to PagerDuty](/assets/pagerduty-connection-setup.DEV0ftqU.png)_Connect to PagerDuty_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter the API key you generated in the **API key** field.
   
6. Select **Connect** to verify and save the connection. Workato displays a success message when the connection is established.

---
