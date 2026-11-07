---
url: 'https://docs.workato.com/en/mcp/manage-tools.md'
description: >-
  Manage MCP server tools from the Details tab to start, stop, add, and remove
  tools and edit the LLM-facing server description.
---

# Manage MCP server tools

You can manage MCP tools and tool annotation within the MCP server **Details** tab. The **Details** tab provides a list of tools in your MCP server, your Remote MCP URL, and authentication method.

## Edit LLM-facing MCP server description

Your MCP server description is automatically shared with your LLM when you connect the MCP server. You can update the description for your specific use cases and to include any tool customization you perform. An accurate MCP server description helps your LLM know when to use specific tools.

Complete the following steps to edit the MCP server description shared with your LLM:

1. Sign in to your Workato account.
   
2. Go to **AI Hub > Enterprise MCP > Custom servers**.
   
3. Select the MCP server where you plan to edit the LLM-facing MCP server description.
   
4. Go to the **Description** section and click the edit icon.
   
5. Update the description.
   
   ![Update the LLM-facing description](/assets/edit-llm-facing-description.Dhhjsnze.png)_Update the LLM-facing description_
   
6. Click the save icon.
   

## Manage tools

You can start, stop, add, and remove tools in the **Details** tab. You can also edit the tool name, title, and recipe.

### Edit tool name

The tool name is used by AI agents to distinguish between multiple tools. Changes to the **Name** field don't apply to the **Title** field.

> **CHANGING TOOL NAME FORCES RESET CONSENT AND PREFERENCES**
> 
> LLM clients using a tool must rediscover the tool after the name changes. A re-named tool is treated as a new tool. Previous consent and user preferences are discarded.

Complete the following steps to edit the tool name:

1. Sign in to your Workato account.
   
2. Go to **AI Hub > Enterprise MCP > Custom servers**.
   
3. Select the MCP server where you plan to edit the tool name.
   
4. Go to the **Tools** section and click the (...) option menu.
   
   ![MCP tool option menu](/assets/mcp-tool-option-menu.P0NGgMnW.png)_MCP tool option menu_
   
5. Select **Edit tool name**.
   
6. Go to the **Name** field and make your changes.
   
   ![Edit the Name field](/assets/edit-tool-name.CyO2W5DM.png)_Edit the **Name** field_
   
7. Click **Rename tool**.
   

### Edit tool title

The tool title is an optional human-readable label for end users. Changes to the **Title** field don't apply to the **Name** field.

Complete the following steps to edit the tool title:

1. Sign in to your Workato account.
   
2. Go to **AI Hub > Enterprise MCP > Custom servers**.
   
3. Select the MCP server where you plan to edit the tool title.
   
4. Go to the **Tools** section and click the (...) option menu.
   
   ![MCP tool option menu](/assets/mcp-tool-option-menu.P0NGgMnW.png)_MCP tool option menu_
   
5. Select **Edit tool details**.
   
6. Go to the **Title** field and make your changes.
   
7. Click **Save**.
   

### Start tools

You must start MCP tools you plan to make available to AI models.

Complete the following steps to start tools:

1. Sign in to your Workato account.
   
2. Go to **AI Hub > Enterprise MCP > Custom servers**.
   
3. Select the MCP server where you plan to start tools.
   
4. Go to the **Tools** section and select the checkboxes for the tools you plan to start.
   
   ![Select the checkboxes for the tools you plan to start](/assets/start-tools.lZnTjW8s.png)_Select the checkboxes for the tools you plan to start_
   
5. Click **Start tools**.
   

### Remove tools

Complete the following steps to remove tools from an MCP server:

1. Sign in to your Workato account.
   
2. Go to **AI Hub > Enterprise MCP > Custom servers**.
   
3. Select the MCP server where you plan to remove tools.
   
4. Go to the **Tools** section and select the checkboxes for the tools you plan to remove.
   
   ![Select the checkboxes for the tools you plan to remove](/assets/remove-tools.C-K8Ift0.png)_Select the checkboxes for the tools you plan to remove_
   
5. Click **Remove tools**.
   

### Edit tool recipe

You can customize tools in your MCP server template within the recipe editor. You can add and edit actions, inputs, result schemas, error handling logic, and more. Refer to [MCP server tool design](/en/mcp/mcp-server-tool-design#mcp-server-tool-design-considerations) and [Recipe design](/en/recipes/building-recipes#recipe-design) for more information.

Complete the following steps to edit an MCP server template tool:

1. Sign in to your Workato account.
   
2. Go to **AI Hub > Enterprise MCP > Custom servers**.
   
3. Select the MCP server where you plan to edit tools.
   
4. Go to the **Tools** section and click the tool name you plan to edit. The recipe editor opens with the configured recipe.
   
   ![Click the tool name you plan to edit](/assets/edit-tools.D6mjwDLU.png)_Click the tool name you plan to edit_
   
5. Click **Edit**.
   
6. Update the recipe and click **Save**.
   
7. [Test](/en/recipes/testing#basics) the changes to your tool.
   

### Add tools

You can add customized tools using existing skills in your project or build a new skill to add as a tool.

#### Add new tools

You can [design](/en/mcp/mcp-server-tool-design#mcp-server-tool-design) and create new tools with [skills](/en/agentic/skills#skills).

Complete the following steps to create and add tools to the MCP server template:

1. Sign in to your Workato account.
   
2. Go to **AI Hub > Enterprise MCP > Custom servers**.
   
3. Select the MCP server where you plan to add tools.
   
4. Go to the **Tools** section and click **\+ Add**. The **Add new tools** modal displays.
   
5. Click **\+ Create new tool > Add tools**.
   
   ![Click Create new tool > Add tools](/assets/create-new-tool.BfKK4DVJ.png)_Click **\+ Create new tool > Add tools**_
   
6. Provide a name for your skill in the **Skill name** field.
   
7. Use the **Location** drop-down menu to select a location for your skill.
   
8. Click **Start building**. The recipe editor opens with the **Start workflow** trigger and **Return response** action automatically selected.
   
9. Provide a description for your skill workflow in the **When should your genie run this skill?** field. The genie uses this description to decide when to trigger this workflow.
   
10. Go to the **What inputs will your genie require to run this skill?** section and click **Use JSON** or **Add fields manually** to provide a description of the schema recipe parameters.
    
    **Use JSON**
    
    1. Click **Use JSON**.
       
    2. Paste the JSON schema you plan to use into the **JSON sample** field and then click **Next**.
       
    3. Review the sample JSON tree and then click **Generate schema**.
       
    
    **Add fields manually**
    
    1. Click **add fields manually**.
       
    2. Provide a name for your schema in the **Name** field.
       
    3. Optional. Provide a description of the schema in the **Description** field.
       
    4. Use the **Data type** drop-down menu to select the data type. Options include the following data types:
       
       - String
       - Number
       - Integer
       - Date
       - Time
       - Boolean
       - List
       - Object
       - File
    5. Use the **Optional** drop-down menu to determine whether the schema field is optional or required.
       
    6. Optional. Use the **Nest under** drop-down menu to determine whether the field is nested within another field.
       
    7. Optional. Provide a description of the field or expected input in the **Hint** field.
       
    8. Click **Add field**.
       
    
11. Go to the **Result schema** section and click **Use JSON** or **Add fields manually** to provide a description for the recipe return value.
    
    > **DEFINES THE RETURN RESPONSE GENIE STEP**
    > 
    > The **Result schema** section defines the `RETURN` response for the genie step at the end of your recipe.
    
    **Use JSON**
    
    1. Click **Use JSON**.
       
    2. Paste the JSON schema you plan to use into the **JSON sample** field and then click **Next**.
       
    3. Review the sample JSON tree and then click **Generate schema**.
       
    
    **Add fields manually**
    
    1. Click **add fields manually**.
       
    2. Provide a name for your schema in the **Name** field.
       
    3. Optional. Provide a description of the schema in the **Description** field.
       
    4. Use the **Data type** drop-down menu to select the data type. Options include the following data types:
       
       - String
       - Number
       - Integer
       - Date
       - Time
       - Boolean
       - List
       - Object
    5. Use the **Optional** drop-down menu to determine whether the schema field is optional or required.
       
    6. Optional. Use the **Nest under** drop-down menu to determine whether the field is nested within another field.
       
    7. Optional. Provide a description of the field or expected input in the **Hint** field.
       
    8. Click **Add field**.
       
    
12. Click **Select an app and action** step in the recipe.
    
13. Search for and select the app you plan to use. A list of available actions for the app displays.
    
14. Select the action you plan to use.
    
15. Select the connection type you plan to use for the skill.
    
    ![Connection type](/assets/users-connection.DrJMnyxd.png)_Choose a connection type_
    
    - **End user's connection**: Skills perform actions based on the identity and permissions of the user who connects to the application. Users authenticate with their own credentials to execute the skill.
    - **This recipe's connection**: This option uses the connection established by the recipe builder and follows the same principles as normal app connections.
    
    > **VERIFIED USER ACCESS AUTHENTICATION REQUIREMENTS**
    > 
    > Only app connections that use OAuth 2.0 authorization code grant are available for user's connection. Refer to [Verified user access](/en/mcp/verified-user-access) for more information.
    
16. Provide a name for your connection in the **Name** field.
    
17. Use the **Location** drop-down menu to select the project where you plan to store the connection.
    
18. Provide information for all required app connection fields. Connection configuration fields vary based on the app you select.
    
19. Click **Connect**.
    
20. Test your recipe to ensure workflow compatibility with your genie.
    
21. Click **Save**.
    

#### Add existing project tools

Complete the following steps to add existing tools from your project to the MCP server template:

1. Sign in to your Workato account.
   
2. Go to **AI Hub > Enterprise MCP > Custom servers**.
   
3. Select the MCP server where you plan to add tools.
   
4. Go to the **Tools** section and click **\+ Add**. The **Add new tools** modal displays.
   
5. Click **Add from this project**.
   
   ![Click Add from this project](/assets/add-tools-from-project.C2EAhUke.png)_Click **Add from this project**_
   
6. Select the checkboxes for the tools you plan to use.
   
7. Click **Add tools**.
   

## Manage tool annotation

Tool annotation lets you guide how AI agents treat a tool in your MCP server. You can enable the following tool annotation settings:

- **Read-only (readOnlyHint)**: Enable this setting to let an agent know it can run this tool without confirmation. This setting can only be used with **Open world (openWorldHint)**.
- **Destructive (destructiveHint)**: Enable this setting to let an agent know that the tool may delete or overwrite data. The agent shows a warning before running this tool. This setting can be used with **Safe to retry (idempotentHint)** and **Open world (openWorldHint)**.
- **Safe to retry (idempotentHint)**: Enable this setting to let the agent know it can call this tool repeatedly without side effects. This setting can be used with **Destructive (destructiveHint)** and **Open world (openWorldHint)**.
- **Open world (openWorldHint)**: Enable this setting to let the agent know that the tool uses data from outside systems. The agent treats this data as untrusted. This setting can be used with **Destructive (destructiveHint)** and **Safe to retry (idempotentHint)**.

Complete the following steps to manage tool annotation:

1. Sign in to your Workato account.
   
2. Go to **AI Hub > Enterprise MCP > Custom servers**.
   
3. Select the MCP server that contains the tools you plan to edit.
   
4. Go to the **Tools** section and select the checkboxes for the tools where you plan to configure tool annotations.
   
5. Select **Edit annotations**.
   
6. Click the individual toggles to configure tool annotation settings.
   
   ![Configure tool annotations](/assets/tool-annotation.BqZ1mx5N.png)_Configure tool annotations_
   
7. Click **Save**.

---
