---
url: 'https://docs.workato.com/en/connectors/datadog.md'
description: >-
  The Datadog connector connects your recipes with real-time metrics, traces,
  and logs from Datadog.
---

# Datadog

[Datadog](https://www.datadoghq.com) is a cloud-based security and analytics platform that monitors metrics, traces, and logs in real-time across your infrastructure.

The **Datadog** connector integrates Datadog insights into your Workato recipes.

## Prerequisites

Ensure you meet the following requirements before you begin:

- A [Datadog API key](https://docs.datadoghq.com/account_management/api-app-keys/#add-an-api-key-or-client-token)
- A [Datadog application key](https://docs.datadoghq.com/account_management/api-app-keys/#add-application-keys) if you plan to perform read actions.

## Connection setup

Complete the following steps to connect your Datadog account in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Provide a name for your connection in the **Connection name** field.
   
   ![Datadog connection](/assets/datadog-connection.DGl2E3ES.png)_Datadog connection fields_
   
3. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
4. Search for and select **Datadog** as your connection on the **New connection** page.
   
5. Enter your Datadog **API key**. Refer to the Datadog [Add an API key](https://docs.datadoghq.com/account_management/api-app-keys/#add-an-api-key-or-client-token) guide to generate this value.
   
6. Optional. Enter your Datadog **Application key** if you plan to perform read actions. Refer to the Datadog [Add application keys](https://docs.datadoghq.com/account_management/api-app-keys/#add-application-keys) guide to generate this value.
   
7. Use the **Region** drop-down menu to select the location for your Datadog account. This field defaults to `US 1` if left blank.
   
8. Click **Connect**.

---
