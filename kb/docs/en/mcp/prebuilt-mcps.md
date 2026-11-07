---
url: 'https://docs.workato.com/en/mcp/prebuilt-mcps.md'
description: >-
  Workato prebuilt MCP servers integrate AI tooling into your workflows with
  customizable tools, business logic, user provisioning, and rate limits.
---

# Start with a prebuilt MCP server

MCP (Model Context Protocol) servers lets LLMs interact with external tools and services. Workato prebuilt MCP servers provide a trusted framework for integrating AI-enabled tooling into development, automation, and operational workflows, and security and compliance controls. Workato prebuilt MCP servers transform static API models into active agents capable of executing real work.

Many vendor-provided MCP servers are essentially API wrappers that expose a fixed set of actions with no ability to add business logic, enforce custom checks, or adapt tools to your workflows. Workato's prebuilt MCP servers take a different approach. The prebuilt MCP server collection can be deployed in minutes and fully customized to match your specific use cases. You can add, modify, or remove tools, and build in logic such as validation steps, conditional routing, or approval flows using skill recipes. Access is controlled through user provisioning and rate limits, and each agent action is tied to an authenticated user for full traceability.

## Use a prebuilt MCP server

Prebuilt MCP servers must be added in Workato and in your MCP client, such as Cursor, ChatGPT, or Claude.

### Custom connector prerequisites

Prebuilt MCP servers that use custom connectors must be installed in your workspace before you install the prebuilt MCP server.

Complete the following steps to install an MCP server custom connector:

1. Go to **AI Hub > Enterprise MCP > Custom servers** and click **\+ Create MCP server**.
   
2. Go to the **Start with pre-built MCP Servers using your connected apps** section and select the prebuilt MCP server you plan to use.
   
3. Click **Use this server**.
   
4. Go to the **Installations** section. This section only appears for prebuilt MCP servers that use a custom connector.
   
   ![Go to the Installations section](/assets/click-install-custom-connector.5eJ-Vf_1.png)_Go to the **Installations** section_
   
5. Click **Install**. A blue checkmark appears when the custom connector installs successfully.
   
   ![Click Install](/assets/custom-connector-installed.Bbj-m63t.png)_Click **Install**_
   
6. Complete the remaining configuration steps in the [Install a prebuilt MCP server in Workato](/en/mcp/prebuilt-mcps#install-a-prebuilt-mcp-server-in-workato) section.
   

### Install a prebuilt MCP server in Workato

Complete the following steps to install a prebuilt MCP server in your Workato project:

1. Sign in to your Workato account.
   
2. Go to **AI Hub > Enterprise MCP > Custom servers**.
   
3. Click **\+ Create MCP server**.
   
4. Go to the **Start with pre-built MCP Servers using your connected apps** section and select the template you plan to use.
   
   ![Start with pre-built MCP Servers using your connected apps](/assets/start-with-template.DXlG3-ZP.png)_Go to the **Start with pre-built MCP Servers using your connected apps** section_
   
5. Click **Use this server**.
   
6. Use the **Project** drop-down menu to select the project where you plan to add your prebuilt MCP server.
   
7. Provide a name for your MCP server in the **MCP Server name** field.
   
   > **CUSTOM CONNECTOR INSTALLATION**
   > 
   > The **Installations** section appears for prebuilt MCP servers that require a custom connector. Complete the [custom connector prerequisites](#custom-connector-prerequisites) steps before going to **Connections**.
   
8. Go to the **Connections** section and connect to your app account.
   
9. Select the connection type you plan to use for the prebuilt MCP server.
   
   - **User's connection**: MCP server tools perform actions based on the identity and permissions of the user who connects to the application. Users authenticate with their own credentials to execute the skill.
   - **Your connection**: This option uses the connection established by the recipe builder and follows the same principles as normal app connections.
   
   > **VERIFIED USER ACCESS AUTHENTICATION REQUIREMENTS**
   > 
   > Only app connections that use OAuth 2.0 authorization code grant are available for user's connection. Refer to [Verified user access](/en/mcp/verified-user-access) for more information.
   
10. Use the [Prebuilt MCP servers page](/en/mcp/prebuilt-mcps/mcp-servers) to find app-specific connection documentation.
    

### LLM-facing MCP server description

Prebuilt MCP servers include a default MCP server description with detailed information. This description is automatically shared with your LLM when you connect the MCP server. You can update the description for your specific use cases and to include any tool customization you perform.

#### Edit LLM-facing MCP server description

Complete the following steps to edit the MCP server description shared with your LLM:

1. Sign in to your Workato account.
   
2. Go to **AI Hub > Enterprise MCP > Custom servers**.
   
3. Select the MCP server where you plan to edit the LLM-facing MCP server description.
   
4. Go to the **Description** section and click the edit icon.
   
5. Update the description.
   
   ![Update the LLM-facing description](/assets/edit-llm-facing-description.Dhhjsnze.png)_Update the LLM-facing description_
   
6. Click the save icon.
   

## Add a prebuilt MCP server to an AI model

Refer to [AI model configuration](/en/mcp/prebuilt-mcps/ai-model-configuration) for instructions on how to add and configure your MCP server in an AI model, such as Cursor, Claude, or ChatGPT.

## Manage MCP server tools

View and manage your MCP server tools in the **Details** tab **Tools** section. Tool management provides the following capabilities:

- [Start tools](/en/mcp/manage-tools#start-tools)
- [Remove tools](/en/mcp/manage-tools#remove-tools)
- [Edit tools](/en/mcp/manage-tools#edit-tools)
- [Add tools](/en/mcp/manage-tools#add-tools)
- [Edit your LLM-facing MCP server description](/en/mcp/prebuilt-mcps#edit-llm-facing-mcp-server-description)

> **TOOLS MUST BE STARTED**
> 
> Your LLM can only access active tools in your MCP server connector.

## Add users to an MCP server

You can provision end users with access to your MCP server. Refer to [Workato Identity](/en/workato-identity) for more information.

## Configure MCP server quotas

You can add custom rate limits, usage quotas, and IP restrictions for your MCP server.

Rate limits control request frequency and prevent traffic bursts.

Refer to [Configure MCP server quotas](/en/mcp/mcp-server-access-and-configuration#configure-mcp-server-limits) for more information.

---
