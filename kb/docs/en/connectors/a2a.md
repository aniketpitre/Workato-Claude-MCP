---
url: 'https://docs.workato.com/en/connectors/a2a.md'
description: >-
  Agent2Agent (A2A) Protocol is an open standard that enables communication and
  collaboration between AI agents.
---

# A2A Protocol

[Agent2Agent (A2A) Protocol](https://a2a-protocol.org/latest/) is an open standard that enables communication and collaboration between AI agents. A2A Protocol is the common language for agent interoperability with frameworks and different vendors.

This connector has the following capabilities:

- Workato recipes can communicate with any A2A-compliant AI agent server.
- Invoke AI agents as steps inside an automation workflow, wait for results, and act on the output.
- Cover the full range of integration patterns from synchronous blocking calls, to fire-and-check async workflows.
- Agents built on different frameworks can discover each other, delegate tasks, and exchange results over HTTP/JSON-RPC.

Refer to the [A2A Protocol](https://a2a-protocol.org/latest/topics/key-concepts/) documentation for information about the protocol's core concepts.

## A2A Protocol compatible agents

The following agents are compatible with the A2A Protocol connector:

| Agent | Framework | Authentication |
| --- | --- | --- |
| Google ADK Purchasing Concierge | Google ADK (Python) | N/A |
| LangGraph / LangSmith A2A Endpoint | LangChain / LangGraph | Bearer token |
| CrewAI + Vertex AI | CrewAI + Gemini 2.5 | Google OAuth2 / Bearer |
| Amazon Bedrock AgentCore | AWS | AWS SigV4 / Bearer. Bedrock AgentCore connection using A2A Protocol requires additional configuration. |
| Azure AI Foundry A2A | Azure | Microsoft Entra ID Bearer token |
| a2a-samples (GitHub) | Python or JS | Configurable |

## Multi-agent architecture

A2A Protocol supports using multiple agents with the following architecture:

- One Agent Card per domain
- Distinct paths for each agent on the same server
- Separate Agent Cards for each agent on the same server
- One connection per agent. You must create separate connections for each agent.

## Skills

Skills used in A2A Protocol connections are only shown in hint text on the **Message** input field. The connector doesn't send a skill ID or skill reference in the message payload.

## Install A2A Protocol from the community library

Complete the following steps to install the A2A Protocol connector from the [community library](https://www.workato.com/browse/connectors):

1. Open the recipe editor and search for a connector. Alternatively, you can search for a connector in the [community library](https://www.workato.com/browse/connectors).
   
   ![Search for recipe editor](/assets/search-on-recipe-editor.VrZpf8zl.png)_Search for community connectors in the recipe editor_
   
2. Select the community connector you plan to install.
   
3. Click **Install** to install the connector from the community library.
   
   ![Click install](/assets/install-connector.BXpGZP9K.png)_Click **Install**_
   
4. Select **Release connector**. Alternatively, select **Review code** to review and modify the connector code before releasing it to the workspace.
   
   ![Release connector](/assets/release-and-review.kWToLwmF.png)_Release the connector_
   
5. Summarize any changes you made to the connector, then click **Release** to allow workspace collaborators to use the connector in recipes.
   
   ![The Confirm release dialog](/assets/release.CpEhhA-6.png)_The **Confirm release** dialog_
   

## Obtain required credentials

Each agent defines its own authentication requirements. Review your agent's documentation to determine which authentication method it supports and how to obtain the required credentials. The following table includes A2A Protocol supported authentication methods:

| Authentication method | When to use | Required credentials |
| --- | --- | --- |
| OAuth 2.0 client credentials | Use for server-to-server authentication. | Client ID, Client secret, Token URL, Scope |
| OAuth 2.0 authorization code | Use for agents that act on behalf of the authenticated user. | Client ID, Client secret, Authorization URL, Token URL, Scope |
| Bearer token | Use for simple API gateways. | Bearer token |
| API key | Use for self-hosted or internal agents. | API key |
| None | Use if the API is public and doesn't require authentication. | None |

### Register Workato as an OAuth client

OAuth 2.0 connections require you to register Workato as an OAuth client.

Complete the following steps to register Workato as an OAuth client in your A2A Protocol compliant agent:

1. Go to your application’s **Developer** or **API settings** page.
   
2. Create a new **OAuth client** or **application**.
   
3. Set the **Redirect URI** to: `https://www.workato.com/oauth/callback`
   
4. Copy the authentication values, such as **Client ID**, **Client secret**, **Authorization URL**, and **Token URL** from your application.
   

### Verify your credentials

Test your credentials using a tool such as `curl` or Postman before establishing your connection to confirm your credentials are valid.

Ensure you can:

- Call the `/a2a` endpoint successfully
- Receive a valid JSON response
- Retrieve an access token (for OAuth connections)

## Connect to A2A Protocol in Workato

Complete the following steps to set up an A2A Protocol connection in Workato:

1. Click **Create > Connection**.
   
2. Search for `A2A Protocol` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![A2A Protocol connection setup](/assets/a2a-connection-setup.CX5soPs8.png)_Set up your A2A Protocol connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter the full URL of the A2A Protocol agent endpoint in the **Agent URL** field. For example, `https://agent.acme.com/a2a/billing`.
   
6. Use the **Authentication type** drop-down menu to select an authentication type and provide the required credentials for your selection.
   
   **OAuth 2.0 client credentials**
   
   1. Enter your client ID in the **Client ID** field.
      
   2. Enter your client secret in the **Client secret** field.
      
   3. Enter your token URL in the **Token URL** field.
      
   4. Enter the scopes in the **Scope** field.
      
   
   **OAuth 2.0 (authorization code grant)**
   
   1. Enter your client ID in the **Client ID** field.
      
   2. Enter your client secret in the **Client secret** field.
      
   3. Enter your Authorization URL in the **Authorization URL** field.
      
   4. Enter your token URL in the **Token URL** field.
      
   5. Enter the scopes in the **Scope** field.
      
   
   **Bearer**
   
   1. Enter your bearer token in the **Bearer token** field.
      
   
   **API key**
   
   1. Enter your API key in the **API key** field.
      
   
   **None**
   
   This authentication method does not require additional fields.
   
7. Click **Connect**.

---
