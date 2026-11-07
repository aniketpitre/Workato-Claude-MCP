---
url: 'https://docs.workato.com/en/connectors/anaplan.md'
description: >-
  The Anaplan connector lets you automate planning and forecasting: run import,
  export, process, and deletion batches and upload or download files.
---

# Anaplan

[Anaplan](https://www.anaplan.com) enables you to connect data, people, and plans to drive informed decision-making and streamline business planning processes through its cloud-based platform.

## API version

Anaplan's connector uses Anaplan's API v2.0 for integration. For more information, refer to [Anaplan's API documentation](https://help.anaplan.com/integration-api-v20-399496b0-d66e-4a84-895a-8d1ffdee2e6b).

## Connection setup

The Anaplan connector supports the following authentication types:

- [Username/password](#username-password)
- [OAuth 2.0](#oauth2)
- [Certificate authentication](#certificate)

Each authentication type includes a **Data Centre** field that identifies the data centre hosting your Anaplan instance. This field defaults to **Anaplan Data Center** if left blank. The available options are **Anaplan Data Center**, **AWS Australia**, **GCP Canada**, and **AWS Indonesia**.

### Username/password

Use username/password authentication to connect with your Anaplan account credentials.

#### Connect to Anaplan with username/password

Complete the following steps to set up a username/password connection to Anaplan in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Anaplan` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Connect to Anaplan using username/password](/assets/anaplan-connection-setup.CxFvb-2e.png)_Set up a username/password connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authentication type** drop-down menu to select **Username/password**.
   
6. Enter your Anaplan **Username**.
   
7. Enter your Anaplan **Password**.
   
8. Use the **Data Centre** drop-down menu to select the data centre that hosts your Anaplan instance. If you leave this field blank, it defaults to **Anaplan Data Center**.
   
9. Click **Connect**.
   

### OAuth 2.0

Use OAuth 2.0 to connect with an OAuth 2.0 client configured in your Anaplan account.

#### Connect to Anaplan with OAuth 2.0

Complete the following steps to set up an OAuth 2.0 connection to Anaplan in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Anaplan` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Connect to Anaplan using OAuth 2.0](/assets/oauth-2.D-dF7H6C.png)_Set up an OAuth 2.0 connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authentication type** drop-down menu to select **OAuth 2.0**.
   
6. Enter your application's **Client ID**. Refer to the Anaplan [Create an OAuth 2.0 client](https://help.anaplan.com/create-an-oauth-20-client-0984a799-a667-4e70-8759-a134be32f48c) documentation for more information.
   
7. Enter your application's **Client secret**. You can find this value in Anaplan under **Administration > Security > OAuth Clients**.
   
8. Use the **Data Centre** drop-down menu to select the data centre that hosts your Anaplan instance. If you leave this field blank, it defaults to **Anaplan Data Center**.
   
9. Click **Connect**.
   

### Certificate authentication

Use certificate authentication to connect with a PEM-format certificate and private key.

#### Connect to Anaplan with certificate authentication

Complete the following steps to set up a certificate authentication connection to Anaplan in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Anaplan` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Connect to Anaplan using certificate authentication](/assets/certificate-auth.Rk4gAPXN.png)_Set up a certificate authentication connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authentication type** drop-down menu to select **Certificate authentication**.
   
6. Enter a PEM-format certificate string in the **Certificate** field. Refer to the Anaplan [Procure CA certificates](https://help.anaplan.com/anapedia/Content/Administration_and_Security/Tenant_Administration/Security/ProcuringCACertificates.htm) documentation for more information.
   
7. Enter a PEM-format private key string in the **Private key** field.
   
8. Use the **Data Centre** drop-down menu to select the data centre that hosts your Anaplan instance. If you leave this field blank, it defaults to **Anaplan Data Center**.
   
9. Click **Connect**.

---
