---
url: 'https://docs.workato.com/en/connectors/workday-rest/connection-setup.md'
description: >-
  Set up and connect Workday REST in Workato using OAuth API clients, including
  integration system users and refresh tokens for ISU access.
---

# Workday REST Connection

## How to connect to Workday on Workato

The Workday REST connector uses the [Workday REST API](https://doc.workday.com/reader/wsiU0cnNjCc_k7shLNxLEA/HvgwLwxCHVdBlZUTNd9s7A). Workday recommends using an Integration System User (ISU) for integration using third party services like Workato.

### Connect to Workday on Workato

![Workday connection fields](/assets/workday-rest-connection.Du0SxAGH.png)_Workday connection fields_

| Connection field | Description |
| --- | --- |
| Connection name | Give this Workday connection a unique name that identifies which Workday tenant it is connected to. |
| REST API endpoint | This is the base URL of all requests made to your Workday instance. |
| Authorization endpoint | Authorization endpoint of your Workday instance. |
| Token endpoint | Token endpoint of your Workday instance. |
| Client ID | Client ID of the API Client you created to connect to Workato. |
| Client secret | Client secret of the API Client you created to connect to Workato. |
| Refresh token | Provide a refresh token if this connection is restricted to an integration user instead of a user account. See [API Client](#api-client) for more details. |

## API Client

You will need to create an API client to connect to Workday REST API. There are 2 ways to connect using API clients:

1. Authorize using a user account
2. Use an API Client for Integration

### API Client for user account

Use a regular **API Client** to authorize a connection to the REST API using a user account.

First, navigate to the **View API Clients** page by typing it into the search bar. You should see this screen. Here, you will see the endpoints required for the connection. Take note of **REST API endpoint**, **Token endpoint** and **Authorization endpoint**.

![View API Clients](/assets/view-api-client-endpoints.CtDdoRpB.png)_View API clients_

Select an existing API Clients that is available to integration if there are any. Otherwise, you need to create a new one. Navigate to **Register API Client** in your Workday instance.

![Register API Client](/assets/register-api-client.Y8YAmXal.png)_Registering a new client_

- Enter a meaningful name to indicate that this API client is used for Workato recipes
- Select **Authorization Code Grant** for **Client Grant Type**
- Select **Bearer** for **Access Token Type**
- Use `https://www.workato.com/oauth/callback` as the Redirection URL
- Select all the **OAuth2 scopes** and **Functional Area scope** that you need for the recipes you intend to create

![API Client credentials](/assets/api-client-details.8GTwgx-o.png)_API client details_

Remember to save the **Client ID** and **Client Secret** before clicking **Done**. This will be required to create a Workday REST connection.

### API Client for Integrations

If you wish to use a manually generated token to connect to Workday, you will need to register an **API client for integration**. This is required when using an ISU that does not have login access and is used only for API access.

Navigate to **Register API Client for integration** in your Workday instance.

![Register API Client for Integrations](/assets/register-api-client-for-integration.DgTBkPTZ.png)_Registering a new client for Integrations_

- Enter a meaning name to indicate that this API client is used for Workato recipes
- Select **Non-Expiring Refresh Tokens** to avoid regenerating and reconnecting
- Select all the **OAuth2 scopes** and **Functional Area scope** that you need for the recipes you intend to create

![API client details](/assets/api-client-for-integration-details.C178GYGo.png)_API client details_

Remember to save the **Client ID** and **Client Secret** before clicking **Done**. This will be required to create a Workday REST connection.

Lastly, navigate to **Action** > **API Client** > **Manage Refresh Tokens for Integrations**.

![Generate refresh token](/assets/generate-refresh-token.8cWHfd1c.png)_Generate refresh token_

Select the Integration user to perform all recipe actions.

![Select refresh token for ISU](/assets/choose-isu.B3X_CSc-.png)_Select refresh token for ISU_

If there are no existing refresh tokens, select **Generate new refresh token** and copy the new **Refresh token**. This will be required to create a Workday REST connection.

![Refresh token for ISU](/assets/isu-refresh-token.UtQI_tSj.png)_Refresh token for ISU_

---
