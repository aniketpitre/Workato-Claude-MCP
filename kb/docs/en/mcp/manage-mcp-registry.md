---
url: 'https://docs.workato.com/en/mcp/manage-mcp-registry.md'
description: >-
  Set up an MCP server registry to enable teams to browse, search, and add MCP
  servers from a single catalog.
---

# Manage an MCP registry

Create and manage an MCP registry to enable teams to browse, search, and add MCP servers from a single catalog. Each MCP server entry includes the name, description, available tools, and ownership metadata.

> **MCP REGISTRY IS ENVIRONMENT SPECIFIC**
> 
> An MCP registry is available only within the environment where you created it. MCP registries aren't shared across workspaces, AHQ managed workspaces, or Embedded customer accounts.

## Set up an MCP server registry

Complete the following steps to set up an MCP server registry:

1. Go to **AI Hub > Enterprise MCP > Custom servers**.
   
2. Click **Set up MCP registry**.
   
3. Enter a name for the registry in the **Registry name** field.
   
   ![Set up your registry](/assets/set-up-mcp-registry.C_9znm8h.png)_Set up your registry_
   
4. Enter the registry URL in the **Registry URL** field.
   
5. Click **Create registry**.
   
6. Click **Copy** to copy the MCP registry URL.
   
7. Click **Done**.
   

## Manage your MCP server registry

Complete the following steps to manage your MCP server registry:

1. Go to **AI Hub > Enterprise MCP > Custom servers**.
   
2. Click **Manage MCP registry**.
   
3. Optional. Change the name of your MCP server registry, update the Registry URL, or copy your Registry MCP endpoint.
   
   ![Access and manage your MCP server registry information](/assets/manage-mcp-registry.A83jFub1.png)_Access and manage your MCP server registry information_
   
4. Click **Save changes** to save your edits.
   

## Manage MCP server permissions

You must enable permissions to publish and unpublish MCP servers from the MCP server registry at the project-role level.

Complete the following steps to enable publish and unpublish permissions:

1. Sign in to your Workato account.
   
2. Go to **Workspace admin > Project roles**.
   
3. Select the role you plan to provide with MCP server permissions.
   
4. Go to the **MCP servers** section and select the **Publish / Unpublish** checkbox.
   
   ![Select the Publish / Unpublish checkbox](/assets/publish-unpublish-permissions._bg7fg_2.png)_Select the **Publish / Unpublish** checkbox_
   

## Publish an MCP server

Complete the following steps to publish an MCP server to your registry:

1. Go to **AI Hub > Enterprise MCP > Custom servers**.
   
2. Select the MCP server you plan to publish.
   
3. Go to the **Visibility on MCP registry** section and click **Publish**.
   

## Unpublish an MCP server

Complete the following steps to unpublish an MCP server from your registry:

1. Go to **AI Hub > Enterprise MCP > Custom servers**.
   
2. Select the MCP server you plan to unpublish.
   
3. Go to the **Visibility on MCP registry** section and click **Unpublish**.

---
