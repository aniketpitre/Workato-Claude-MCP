---
url: 'https://docs.workato.com/en/connectors/workday-asor.md'
description: >-
  Workday ASOR is a cloud-based Human Capital Management (HCM) and financial
  management platform. The Workday Agent System of Record (ASOR) connector
  enables you to manage agent definitions in Workday's Agent-to-Agent (A2A)
  framework.
---

# Workday Asor

[Workday ASOR](https://www.workday.com/) is a cloud-based Human Capital Management (HCM) and financial management platform. The Workday Agent System of Record (ASOR) connector enables you to manage agent definitions in Workday's Agent-to-Agent (A2A) framework. You can register and configure AI agent capabilities to integrate with Workday's intelligent automation ecosystem.

This connector has the following capabilities:

- Create agent definitions when deploying new AI agents that integrate with Workday
- Retrieve all registered agents to monitor and manage your agent ecosystem
- Get agent details by ID to verify agent configurations, capabilities, and skills

## Install Workday ASOR from the community library

Complete the following steps to install the Workday ASOR connector from the [community library](https://www.workato.com/browse/connectors):

1. Open the recipe editor and search for a connector. Alternatively, you can search for a connector in the [community library](https://www.workato.com/browse/connectors).
   
   ![Search for recipe editor](/assets/search-on-recipe-editor.VrZpf8zl.png)_Search for community connectors in the recipe editor_
   
2. Select the community connector you plan to install.
   
3. Click **Install** to install the connector from the community library.
   
   ![Click install](/assets/install-connector.BXpGZP9K.png)_Click **Install**_
   
4. Select **Release connector**. Alternatively, select **Review code** to review and modify the connector code before releasing it to the workspace.
   
   ![Release connector](/assets/release-and-review.kWToLwmF.png)_Release the connector_
   
5. Summarize any changes you made to the connector, then click **Release** to allow workspace collaborators to use the connector in recipes.
   
   ![The Confirm release dialog](/assets/release.CpEhhA-6.png)_The **Confirm release** dialog_
   

## Connection setup

The Workday ASOR connector uses OAuth 2.0 authentication.

### Workday ASOR setup for OAuth 2.0 authentication

You must create an API client to generate a client ID, client secret, and Workday tenant for OAuth 2.0 authentication.

1. Sign into your Workday account.
   
2. Use an existing API client.
   
   1. Search for **View API Clients** in the search bar.
      
   2. Select an existing API client, if available.
      
3. Create a new API client.
   
   1. Search for **Register API Client** in the search bar.
      
   2. Enter a **Client Name**.
      
   3. Select **Authorization Code Grant** for **Client Grant Type**.
      
   4. Select **Bearer** for **Access Token Type**.
      
   5. Enter `https://www.workato.com/oauth/callback` in **Redirection URL**.
      
   6. Select **Agent System Of Record** in **Scope (Functional Areas)**.
      
4. Save your **Client ID** and **Client Secret** to use in Workato.
   

### Connect to Workday ASOR with OAuth 2.0

Complete the following steps to connect to Workday ASOR in Workato:

1. Click **Create > Connection**.
   
2. Search for `Workday ASOR` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Workday ASOR connection setup](/assets/workday-asor-connection-setup.Bc2m-UKZ.png)_Set up your Workday ASOR connection_\--->
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter your **Client ID** and **Client secret**.
   
6. Enter your **Workday tenant**. For example, if your Workday URL is [https://impl.workday.com/company\_abc1](https://impl.workday.com/company_abc1), the tenant name is `company_abc1`.
   
7. Click **Connect**.
   
8. Sign in to Workday when prompted.
   
9. Click **Allow** to grant access.

---

---
url: >-
  https://docs.workato.com/en/connectors/workday-asor/create-agent-definition-action.md
description: >-
  The Create agent definition action creates an agent definition in Workday
  ASOR.
---

# Workday ASOR - Create agent definition action

The **Create agent definition** action creates an agent definition in Workday ASOR.

## Input

| Input field | Description |
| --- | --- |
| Name | The agent name. |
| Description | The agent description. |
| URL | The agent URL. |
| Provider | The service provider of the agent. |
| Platform | The platform the agent executes on. |
| Version | The version of the agent. |
| Skills | The skills the agent can perform. |
| Workday config | The configuration of the Workday instance, including the skill ID. |

## Output

| Output field | Description |
| --- | --- |
| ID | The agent ID. |
| Capabilities | The agent's capabilities. |
| Skills | The agent's skills. |
| Platform | The platform the agent runs on. |
| Description | The agent description. |
| URL | The agent URL. |
| Name | The agent name. |
| Version | The agent's version. |
| Provider | The agent provider of the Workday agent. |
| Workday config | The Workday instance configuration, including the skill ID. |
| Supports authenticated extended card | Indicates if the agent supports having an authenticated extended card. |

---
