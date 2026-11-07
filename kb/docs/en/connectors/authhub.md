---
url: 'https://docs.workato.com/en/connectors/authhub.md'
description: >-
  The AuthHub connector lets you automate access management: search records, get
  record details, and add or remove members from groups.
---

# AuthHub

[AuthHub](https://techdocs.broadcom.com/) is a policy-driven authentication and authorization service used in Broadcom security tools such as SiteMinder. It manages user authentication flows and supports integration with multiple authentication methods.

## Prerequisites

You must have the following to use the AuthHub connector in Workato:

1. An active Broadcom account with the necessary permissions to access the Users API. Refer to the Broadcom [Docs Portal](https://techdocs.broadcom.com/) for additional information.
2. A Broadcom **Client ID** and **Client secret**. Refer to the Broadcom [Registering Clients with the OAuth Manager](https://techdocs.broadcom.com/us/en/ca-enterprise-software/layer7-api-management/api-management-oauth-toolkit/4-6/registering-clients-with-the-oauth-manager.html) guide to generate these values.

## How to connect to AuthHub

Complete the following steps to establish an AuthHub connection in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `AuthHub` as your connection on the **New connection** page.
   
3. Provide a name for your connection in the **Connection name** field.
   
   ![AuthHub connection setup](/assets/authhub-connection-setup.CNiXbKPk.png)_AuthHub Connection Setup_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Select your **Connection type** from the drop-down menu.
   
6. Enter the **Client ID** and **Client Secret** for your AuthHub account. Refer to the Broadcom [Registering Clients with the OAuth Manager](https://techdocs.broadcom.com/us/en/ca-enterprise-software/layer7-api-management/api-management-oauth-toolkit/4-6/registering-clients-with-the-oauth-manager.html) guide to generate these values.
   
7. Enter the **URL** for your AuthHub account, for example, `abc.broadcom.net`.
   
8. Click **Connect**.

---
