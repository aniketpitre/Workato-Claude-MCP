---
url: 'https://docs.workato.com/en/airo/build/mcp-servers.md'
description: >-
  Create an MCP server and tools by describing the skills and MCP server to AIRO
  in Workato or through AIRO Connect.
---

# Build MCP servers with AIRO

You can build an MCP server and tools by describing what you need to AIRO in plain language. Create or identify the skills, recipe functions, and API recipes you plan for the MCP server to expose first. Then ask AIRO to create the MCP server and attach the assets you created.

> **AIRO CONNECT CAN'T EDIT AN EXISTING MCP SERVER**
> 
> AIRO Connect can attach supported Workato assets to an MCP server only when it creates the server. It can't add or remove tools, change the MCP server description, or manage the MCP server's authentication credentials afterward.
> 
> Use AIRO in Workato, the MCP server interface, or the Developer API MCP server to modify an existing MCP server.

## Prerequisites

You must have the following before you create an MCP server and tools with AIRO or AIRO Connect:

- AIRO enabled in your workspace. Connect your MCP client to [AIRO Connect](/en/airo/mcp) if you work outside Workato.
- Access to the target project, plus the **MCP servers** privilege with **Create** access. You also need **Edit** access to add or remove tools on an existing MCP server, and **Manage access** if you plan to configure end-user access.
- The **Recipes** privilege with **Create** and **Edit** access to create or change skills, recipe functions, or API recipes, and **Test/Start/Stop** access to start a skill. Refer to [MCP servers privileges](/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference#mcp-servers) and [Project asset privileges](/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference#project-assets).
- Active connections for the apps your tools use. The example in this guide uses Salesforce.
- All skills, recipe functions, and API recipes you attach must be in the same project as the MCP server.

Confirm that AIRO Connect points to the intended workspace and environment before making a change from an MCP client. Review each write-tool confirmation rather than approving changes automatically.

## Example: Build a sales tools MCP server

This example creates a sales tools MCP server that exposes the following read-only Salesforce skills to an external AI client:

- Enrich lead skill
- Score deal skill

### Build the skills

Start with the skills. An MCP server can only attach project assets from its own project, so create both skills in the project where you plan to create the MCP server.

Both skills use an existing Salesforce connection. You can build the skills in the recipe editor or from an MCP client connected to AIRO Connect.

**Enrich lead**

```text
Create a read-only skill called "Enrich lead". It accepts a Salesforce lead ID and returns the lead's industry, annual revenue, and number of employees. Use my existing Salesforce connection. This skill doesn't require user confirmation.
```

**Score deal**

```text
Create a read-only skill called "Score deal". It accepts a Salesforce opportunity ID and returns a priority score from 1 to 10 and a short reason based on the opportunity's amount, stage, and days until the close date. Use my existing Salesforce connection. This skill doesn't require user confirmation.
```

Review each skill before continuing. Ensure the skill description explains when an AI client should use it, and that the inputs and result fields include only the data the MCP client needs.

### Create the MCP server

Attach the skills when you create the MCP server.

- **In Workato**: Tell AIRO to attach the skill by name. If AIRO can't resolve a name to a handle, create the MCP server without that skill, then refer to [Add tools to an existing server](#add-tools-to-an-existing-server) to add it manually.
- **In an MCP client**: AIRO Connect already has the handle for a skill it just built in this chat. For an existing skill, call the [Developer API MCP server](/en/mcp/developer-api-mcp)'s **List skills** tool (`GET /api/agentic/skills`) to look up its handle. The API client role behind that MCP server needs **List skills** enabled.

Complete the following steps to create the MCP server:

1. Use this prompt:
   
   ```text
   Create an MCP server called "Sales Tools" and attach these skills:
   - Enrich lead (skill handle: skl-...)
   - Score deal (skill handle: skl-...)
   ```
   
2. Open the MCP server in Workato after AIRO creates it.
   
3. Copy the [remote MCP URL](/en/mcp/mcp-servers#create-an-mcp-server-with-project-assets) from the server details.
   
4. Confirm that each expected tool appears and is active before you configure an AI client or share access.
   

Refer to [AIRO reports "Tools contains invalid asset(s)"](#airo-reports-tools-contains-invalid-assets) if AIRO can't attach a skill.

## Complete setup in Workato

Complete the remaining configuration and test the MCP server after AIRO creates it before sharing the URL:

- **Start the skills**: A skill can be attached to a server while it is inactive, but it can't run until it is started. Start the skill manually in Workato. MCP clients can use the [Developer API MCP server](/en/mcp/developer-api-mcp)'s **Start recipe** tool (`PUT /api/recipes/:id/start`) with the skill's recipe ID, if **Start** is enabled in the API client role.
- **Configure end-user access**: Go to **Settings > End user access** on the MCP server and assign the appropriate group. Configure OAuth and verified user access when the tools need to run with each user's identity. Refer to [MCP verified user access configuration](/en/mcp/verified-user-access-configuration).
- **Test from the intended client**: Configure the client with the server's MCP URL, confirm that both tools are discovered, and run a safe read-only request before giving the URL to other users.

## Add tools to an existing server

The way you manage tools changes after the MCP server exists.

- **In Workato**: Ask AIRO to add or remove a tool, or open the server from **AI Hub > Enterprise MCP > Custom servers**. Select **\+ Add** or **Remove tools** in the **Tools** section. Refer to [Manage MCP server tools](/en/mcp/manage-tools).
- **In an MCP client**: AIRO Connect can't make this change. Use the [Developer API MCP server](/en/mcp/developer-api-mcp)'s **Assign tools to an MCP server** tool to add one, or **Delete a tool** to remove one, if those are enabled in your API client role.

## Limitations

AIRO and AIRO Connect have the following limitations when creating MCP servers and skills:

- AIRO Connect can't delete a server, renew its token, or start or stop a skill. Do this manually in Workato, or with the Developer API MCP server from an MCP client.
- AIRO Connect can't attach tools from an external, proxied MCP server while it creates a new server. Add that tool source [in Workato](/en/mcp/mcp-servers#create-an-mcp-server) instead.

## Troubleshooting

Most issues come from an invalid asset reference, an asset AIRO can't locate, a tool that hasn't been started, or a missing privilege.

### AIRO reports "Tools contains invalid asset(s)"

Complete the following steps to resolve the error:

1. Check that each tool uses the right asset type and identifier:
   
   | Tool asset | Identifier to provide |
   | --- | --- |
   | Skill | Its `skl-...` handle |
   | Recipe function | Its numeric recipe ID |
   | API recipe | Its numeric recipe ID |
   
2. Confirm that every asset is in the same project and workspace as the server. An inactive skill can still be attached, but it won't be callable until you start it.
   

### AIRO can't find the skill, recipe function, or API recipe you expect

Complete the following steps to locate the asset:

1. Check that the asset wasn't renamed or saved in a different folder.
   
2. Look up the asset by type:
   
   - **Skill**: Ask AIRO to search by a partial or approximate name, or call the Developer API MCP server's **List skills** (`GET /api/agentic/skills`) tool directly.
   - **Recipe function or API recipe**: Browse by folder or project, or call the **List recipes** (`GET /api/recipes`) tool directly.
   
   The MCP server and every project asset it exposes must be in the same project.
   

### A tool is listed but isn't callable

Start the skill in Workato, then check the MCP server's end-user access settings and any required app connections. Tools that use verified user access require each user to complete the required OAuth connection.

### An operation is denied

Confirm that the identity AIRO is using has access to the target workspace and project. MCP server creation requires **Create** access for **MCP servers**, and adding or removing tools on an existing MCP server requires **Edit** access. Creating or editing the tools requires **Create** and **Edit** access for **Recipes**, and starting a skill requires **Test/Start/Stop** access. Refer to [MCP servers privileges](/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference#mcp-servers) and [Project asset privileges](/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference#project-assets).

---
