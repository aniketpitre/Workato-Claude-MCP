---
url: 'https://docs.workato.com/en/connectors/clarity.md'
description: >-
  The Clarity connector lets you automate project and portfolio management
  workflows: search records and trigger recipes on new or updated records.
---

# Clarity

[Clarity](https://www.broadcom.com/products/software/value-stream-management/clarity) is Broadcom's enterprise project and portfolio management (PPM) solution that helps organizations align investments, resources, and business strategies to achieve desired outcomes.

## Prerequisites

You must have the following prerequisites to establish a Clarity connection in Workato:

- A Clarity instance URL. For example, `example.clarityppm.saas.broadcom.com`.
  
- Valid credentials for one of the following authentication methods:
  
  - **Basic authentication**: Username and password for a Clarity user account
  - **API key authentication**: API key and Client ID configured in your Clarity instance. Refer to the Clarity [Key-Based Authentication](https://techdocs.broadcom.com/us/en/ca-enterprise-software/business-management/clarity-project-and-portfolio-management-ppm-on-premise/16-3-3/reference/Clarity-REST-APIs/REST-API-Authentication.html#concept.dita_5ce36960-4d7e-4e06-a517-095fc625ebf8_keybasedauth) documentation to learn how to obtain these values.

## How to connect to Clarity

The Clarity connector supports the following authentication methods:

- [Basic authentication](#basic-authentication)
- [API key](#api-key)

### Basic authentication

Complete the following steps to establish a Clarity connection using basic authentication:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Clarity` as your connection on the **New connection** page.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Connect to Clarity](/assets/basic-auth.DdMO22dZ.png)_Connect to Clarity_
   
4. Use the **Location** drop-down menu to select the project or folder where you plan to store the connection.
   
5. Use the **Authentication type** drop-down menu to select **Basic authentication**.
   
6. Enter your Clarity instance URL in the **Base URL** field. For example, `example.clarityppm.saas.broadcom.com`.
   
7. Enter your **Username** and **Password** for your Clarity account.
   
8. Click **Connect**.
   

### API key

Complete the following steps to establish a Clarity connection using API key authentication:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Clarity` as your connection on the **New connection** page.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Connect to Clarity](/assets/api-key.DDd4fnOC.png)_Connect to Clarity_
   
4. Use the **Location** drop-down menu to select the project or folder where you plan to store the connection.
   
5. Use the **Authentication type** drop-down menu to select **API key**.
   
6. Enter your Clarity instance URL in the **Base URL** field. For example, `example.clarityppm.saas.broadcom.com`.
   
7. Enter the **API key** generated from your Clarity profile.
   
8. Enter the **Client ID** provided by your Clarity administrator.
   
9. Click **Connect**.

---
