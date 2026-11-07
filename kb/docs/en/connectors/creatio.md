---
url: 'https://docs.workato.com/en/connectors/creatio.md'
description: >-
  The Creatio connector lets you automate CRM workflows: create, update, delete,
  and search records, manage file attachments, and trigger on new events.
---

# Creatio

[Creatio](https://www.creatio.com/company/about?activity=adwords_brand_apac) is a no-code platform that enables non-technical users to build workflows and manage CRM with minimal restrictions. It can help organizations digitize workflows, enhance customer and employee experiences, and boost efficiency across all business units.

## Prerequisites

To establish a connection to Creatio you must have an active sandbox or general instance.

## Connection setup

Establishing a connection to Creatio involves the following steps:

1. [Download the Creatio connector from the Community library](#community-download)
2. [Complete setup in Workato](#workato-setup)

### Download the Creatio connector from the Community library

Complete the following steps to install the Creatio connector from the [community library](https://www.workato.com/browse/connectors):

1. Open the recipe editor and search for a connector. Alternatively, you can search for a connector in the [community library](https://www.workato.com/browse/connectors).
   
   ![Search for recipe editor](/assets/search-on-recipe-editor.VrZpf8zl.png)_Search for community connectors in the recipe editor_
   
2. Select the community connector you plan to install.
   
3. Click **Install** to install the connector from the community library.
   
   ![Click install](/assets/install-connector.BXpGZP9K.png)_Click **Install**_
   
4. Select **Release connector**. Alternatively, select **Review code** to review and modify the connector code before releasing it to the workspace.
   
   ![Release connector](/assets/release-and-review.kWToLwmF.png)_Release the connector_
   
5. Summarize any changes you made to the connector, then click **Release** to allow workspace collaborators to use the connector in recipes.
   
   ![The Confirm release dialog](/assets/release.CpEhhA-6.png)_The **Confirm release** dialog_
   

### Complete setup in Workato

Workato supports the following types of connections to Creatio.

1. [OAuth 2.0](#oauth2)
2. [Authentication cookies](#authentication-cookies)

#### OAuth 2.0

Complete the following steps to establish a connection to Creatio using OAuth 2.0 authentication.

1. Deploy the Identity Service (for Creatio on-site). Refer to [Deploy the Identity Service](https://academy.creatio.com/documents?id=2466) for more information.
   
2. Connect the Identity Service to Creatio (for Creatio on-site). Refer to [Connect the Identity Service to Creatio](https://academy.creatio.com/documents?id=2467) for more information.
   
3. Generate OAuth 2.0 client credentials. Refer to [Generate OAuth 2.0 client credentials](https://academy.creatio.com/documents?id=2508&anchor=title-2508-1) and [OAuth 2.0](https://academy.creatio.com/docs/8.x/setup-and-administration/on-site-deployment/deployment-additional-setup/identity-service/set-up-the-identity-service-instruction) for more information.
   
   ![Creatio OAuth 2.0](/assets/creatio-oauth2.DDxRgfpS.png)_Creatio OAuth 2.0_
   

Complete the following steps to establish your Creatio connection in Workato using OAuth 2.0 authentication:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Creatio` as your connection on the **New connection** page.
   
3. Provide a name for your connection in the **Connection name** field.
   
4. In the **Auth type** field select `OAuth 2.0` as the connection type.
   
5. Supply your app's **Client ID** and **Client secret** into their corresponding fields in Workato.
   
6. Provide the Creatio base URL in the **Creatio base URL** field.
   
7. Click **Connect**.
   

#### Authentication cookies

Creatio recommends cookie-based authentication (forms authentication) to integrate external services with Creatio. Forms authentication is implemented using the [AuthService.svc web service](https://academy.creatio.com/docs/developer/integrations_and_api/authentication/authentication_basics/overview#reference-1390). Use the cookies received in response from the AuthService.svc web service in subsequent requests to Creatio.

![Creatio authentication cookies](/assets/creatio-authentication-cookies.DP7_2vf4.png)_Creatio authentication cookies_

Complete the following steps to establish your Creatio connection in Workato using authorization cookies authentication.

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Creatio` as your connection on the **New connection** page.
   
3. Provide a name for your connection in the **Connection name** field.
   
4. In the **Auth type** field select `Authentication cookies` as the connection type.
   
5. Supply the provisioned Creatio user's name in the **Username** field.
   
6. Enter your Creatio user password in the **Password** field.
   
7. Provide the Creatio base URL in the **Creatio base URL** field.
   
8. Click **Connect**.

---
