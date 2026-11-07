---
url: >-
  https://docs.workato.com/en/agentic/agent-studio/chat-interface/chat-interface.md
description: >-
  Chat interface is the genie component visibly exposed to your end users, and
  supports Slack, Microsoft Teams, Workato GO, and internal systems with custom
  chatbots.
---

# Chat interface

The chat interface is the genie component visibly exposed to your end users. You can integrate the chat interface into platforms where your organization works, such as Slack, Microsoft Teams, Workato GO, and internal systems with custom chatbots. You can also add a custom chat interface with configurable authentication. The chat interface includes the following capabilities:

- A user-friendly interface for employees to interact with the genie
- Customizable UI elements to match your brand and user experience preferences
- Real-time communication between users and the genie

The interface you select determines where users can discover and interact with the genie, which features are available, and how conversations behave. Slack and Microsoft Teams chat interfaces include channel support. Workato GO provides a dedicated enterprise AI interface with search, Action Board, and KPI dashboards.

> **USING AN EXTERNAL AI CLIENT?**
> 
> You can expose the genie as an MCP server if your users work in an external AI client, such as Claude, ChatGPT, Cursor, or a custom-built UI. The external AI client becomes the interface with users interacting with their AI client as normal. The AI client calls the genie's capabilities through the MCP server when needed. See [MCP server configuration](/en/mcp/genies-as-mcp-clients) for more information.

## Direct message support

Slack, Microsoft Teams, and Workato GO support direct messaging (DMs). Genies respond to every message in DMs. DMs behave the same regardless of the [channel mode](/en/agentic/agent-studio/chat-interface/channel-support#channel-modes) you select.

## Channel support

Genies support participation in Slack and Microsoft Teams channels in addition to DMs. This enables use cases for IT help desks, HR support, and project assistance channels. Workato GO doesn't provide channel support. Refer to [Channel support options](/en/agentic/agent-studio/chat-interface/channel-support#channel-support-options) for more information.

## Chat intermediate updates

You can disable chat intermediate updates, such as intermediate messages and tool calls. These processes continue to run, but are invisible to end-users chatting with the genie when disabled.

### Intermediate messages

Intermediate messages are automatically enabled on all supported chat interfaces.

Each genie sends intermediate messages with real-time status updates and partial findings as it works through a task before it returns the final response. For example, if a user asks your genie to summarize the knowledge base, the genie first sends an intermediate message, such as `I'll search the knowledge base and provide you with a summary` before returning the final two-sentence summary.

#### Disable intermediate messages

You can disable intermediate messages for genies at the project level.

Complete the following steps to disable genie intermediate messages within a project:

1. Go to **Projects** and select the project where you plan to disable intermediate messages.
   
2. Click the **Settings** tab.
   
3. Select **Project properties** and click **\+ Add new property**.
   
4. Go to the **Property name** field and enter `intermediate_messages_disabled`.
   
5. Go to the **Value** field and enter `true`.
   
6. Click the checkmark to save your changes.
   

### Intermediate tool calls

Intermediate tools calls are automatically enabled on all supported chat interfaces.

Each genie displays intermediate tool calls in real-time as it works through a task before it returns the final response or confirmation.

![Intermediate tool call](/assets/intermediate-tool-call.GGY9LxDP.png)_Intermediate tool call_

#### Disable intermediate tool calls

You can disable intermediate tool calls for genies at the project level.

Complete the following steps to disable genie intermediate tool calls within a project:

1. Go to **Projects** and select the project where you plan to disable intermediate tool calls.
   
2. Click the **Settings** tab.
   
3. Select **Project properties** and click **\+ Add new property**.
   
4. Go to the **Property name** field and enter `tool_call_streams_disabled`.
   
5. Go to the **Value** field and enter `true`.
   
6. Click the checkmark to save your changes.
   

## Getting started with a chat interface

Refer to [Create your first genie](/en/agentic/agent-studio/create-a-genie) for complete steps on how to create a genie with a job description, AI model, chat interface, knowledge base, knowledge base recipe, and skills.

Complete the following steps to configure your chat interface:

1. Sign in to Workato.
   
2. Go to **AI Hub > Agent Studio**.
   
3. Click **Create** to build your own genie.
   
4. Enter a request or goal for your genie in the **What would you like your genie to help with?** field.
   
   ![Create a genie](/assets/genie-start-building.BqOHwuGZ.png)_Create a genie_
   
5. Use the **Save genie in** drop-down menu to select a location for your genie.
   
6. Click **Start building**. The genie **Build** page displays.
   
   ![Genie build page](/assets/genie-build-page.DQ8_sDC8.png)_Genie build page_
   
7. Go to the **Triggers** section and select the chat interface you plan to use for this genie. You can add additional chat interfaces by clicking **\+ Add**.
   
   ![Select your chat interface](/assets/chat-interface-triggers.DnacsW-D.png)_Select your chat interface_
   
8. Optional. Click **\+ Add** to add additional chat interfaces to the genie. Genies support multiple chat interfaces from multiple clients. For example, a genie can have multiple chat interfaces connected, including multiple unique Slack Workspaces, multiple unique Teams Tenants, multiple custom chat interfaces, and a single Workato GO chat interface.
   
   ![Multiple chat interfaces can be added to a single genie](/assets/multiple-chat-interfaces.pss_5gYd.png)_Multiple chat interfaces can be added to a single genie_
   
9. Slack
   
   ### Configure Slack as your chat interface
   
   Complete the following steps to configure Slack as your chat interface:
   
   1. Select Slack as your chat interface.
      
   2. Go to **Step 1** and click **Create new app**. Workato opens the selected app and prompts you to create a new app. Follow the instructions in Workato to create the Slack app for your genie.
      
   3. Go to **Step 2** and enter your **Client ID**. Locate this value in the **Basic Information** or **App Credentials** section of your app.
      
      ![Chat interface step 2](/assets/chat-interface-step-2.wiFnIkce.png)_Chat interface Step 2 configuration_
      
   4. Enter your **Client Secret**. You can find this in the **Basic Information** or **App Credentials** section of your app.
      
   5. Provide your **Signing Secret**. This is used to verify that interactive messages and events requests originate from your app. You can find this in the **Basic Information** or **App Credentials** section of your app.
      
   6. Click **Save app** details.
      
   7. Go to your app's **App Manifest** and use the **Click here to verify** link to verify your app's URL for Step 3.
      
   8. Click **Add Slack trigger**.
      
   
   Microsoft Teams
   
   ### Configure Microsoft Teams as your chat interface
   
   Complete the following steps to configure Microsoft Teams as your chat interface:
   
   1. Select Microsoft Teams as your chat interface.
      
   2. Go to **Step 1** and click **Create new app**. Follow the instructions in Workato to create the Microsoft Teams app for your genie.
      
      ![Go to Step 1 and click Create new app](/assets/microsoft-teams-step-1.Cqb0LPai.png)_Go to **Step 1** and click **Create new app**_
      
   3. Go to **Step 2** and enter your app ID in the **App ID** field.
      
      ![Go to Step 2 and enter your app ID in the App ID field](/assets/microsoft-teams-step-2.CYeOsYlw.png)_Go to **Step 2** and enter your app ID in the **App ID** field_
      
   4. Enter your bot ID in the **Bot ID** field. You can find your app's bot ID by going to **Tools > Management** in Microsoft Teams.
      
   5. Enter your client secret in the **Client secret** field.
      
   6. Enter your tenant ID in the **Tenant ID** field. This is your unique Microsoft Entra ID tenant ID. You can find your tenant ID in the [Microsoft Azure Portal](https://portal.azure.com/#view/Microsoft_AAD_IAM/TenantProperties.ReactView).
      
   7. Click **Save app details**.
      
   8. Go back to [Apps](https://dev.teams.microsoft.com/apps) and select your app.
      
   9. Click **Publish > Publish to your org**. Your Microsoft Teams admin may need to approve the publish request.
      
   10. Return to trigger configuration and click **Connect Microsoft Teams trigger**.
       
   
   Workato GO
   
   ### Configure Workato GO as your chat interface
   
   Complete the following steps to configure Workato GO as your chat interface:
   
   1. Select Workato GO as your chat interface.
      
   2. Click **Connect interface**.
      
   
   Custom chat interface
   
   ### Configure a custom chat interface
   
   Complete the following steps to configure a custom chat interface:
   
   1. Select **Custom interface**.
      
      > **INTERFACE TYPE CAN'T BE CHANGED**
      > 
      > You can't change the chat interface type after you save the app details.
      
   2. Enter a name for the interface in the **Interface name** field. This name is visible to builders only and isn't shown to end users.
      
   3. Use the **Authentication method** drop-down menu to select the authentication method for the chat interface.
      
      Your app authenticates users via API key
      
      The API key authorizes requests to this genie. End users don't interact with Workato directly if you select this option.
      
      1. Select **Your app authenticates users via API key**.
         
      2. Optional. Enter the IP addresses or ranges allowed to call this genie in the **Allowed IPs** field. Separate multiple entries with commas. Requests from any IP are permitted if you leave this field empty.
         
      3. Click **Connect interface**. The **API key generated** modal opens.
         
      4. Click **Copy** to copy the API key.
         
      5. Store this API key securely and click **Next: Test your interface**. Don't share or embed the API key in visible code.
         
      6. Optional. Complete the steps to test your chat interface.
         
      7. Click **Add chat interface**.
         
      
      Workato authenticates users via OAuth 2.0
      
      End users authenticate through a Workato-hosted login form. End users are redirected to a URL you choose after successful authentication.
      
      1. Select **Workato authenticates users via OAuth 2.0**.
         
      2. Optional. Add allowlisted IP addresses to the **Allowed IPs** field. Separate multiple entries with commas. Requests from any IP are permitted if you leave this field empty.
         
      3. Enter the URLs where you plan to redirect users after they authenticate in the **OAuth redirect URLs** field.
         
      4. Optional. Enter the IP addresses or ranges allowed to call this genie in the **Allowed IPs** field. Separate multiple entries with commas. Requests from any IP are permitted if you leave this field empty.
         
      5. Click **Connect interface**. The **API key generated** modal opens.
         
      6. Copy the **Client ID**.
         
      7. Copy the **Redirect your user to the authorization URL**.
         
      8. Use the **Client ID** and **Redirect your user to the authorization URL** values you copied to configure the OAuth exchange between your app and this genie in your app settings.
         
      9. Click **Add chat interface**.
         
      
   
10. Optional. Enable channel responses for Slack.
    
    ### Enable channel responses for Slack
    
    You must connect to your Slack account before you can enable channel responses.
    
    Complete the following steps to enable channel responses for Slack:
    
    1. Click your connected chat interface on the genie build page.
       
    2. Go to the configured chat interface where you plan to enable responses.
       
    3. Click the **Enable channel responses** toggle to enable it.
       
    4. Add additional scopes in your app settings if prompted. We recommend that you manually add missing Slack scopes in the Slack directory:
       
       1. Go to the Slack app in the Slack directory.
          
       2. Add the missing scopes to your app settings.
          
          ![Add additional scopes](/assets/additional-scopes.DbPBPdd5.png)_Add additional scopes_
          
       3. Click **Install App > Reinstall to \[Workspace name\]**.
          
       4. Return to the channel responses section in Workato and refresh the page to sync the new scopes to your app.
          
    5. Go to the **Genie can chat in** section and select **Specific channels only** or **Any channel it's invited to**. Refer to [Channel support options](/en/agentic/agent-studio/chat-interface/chat-interface#channel-support-options) for more information.
       
       **Specific channels only**
       
       Use the **Channels** drop-down menu to select the channels where the genie is allowed to chat if you select **Specific channels only**. Your genie must still be invited to a channel by a user before it can chat.
       
       **Any channel it's invited to**
       
       No additional configuration is required. Your genie must still be invited to a channel by a user before it can chat.
       
       ![Configure channel responses](/assets/response-mode.BuZb7RYH.png)_Configure channel responses_
       
    6. Go to the **In channels, genie responds to** section and select **@mentions only** or **Every message posted**. Refer to [Channel modes](/en/agentic/agent-studio/chat-interface/chat-interface#channel-modes) for more information.
       
       > **EVENT SUBSCRIPTIONS REQUIREMENT FOR EVERY MESSAGE POSTED**
       > 
       > You must enable [Event subscriptions scopes](/en/agentic/agent-studio/chat-interface/chat-interface#event-subscription-scopes) in Slack if you select **Every message posted**.
       
       ![Add Event Subscriptions](/assets/event-subscriptions.Bi0ejT2W.png)_Add Event Subscriptions_
       
    7. Click **Save**.
       
    
11. Optional. Enable channel responses for Microsoft Teams.
    
    ### Enable channel responses for Microsoft Teams
    
    You must connect to your Microsoft Teams account before you can enable channel responses.
    
    Complete the following steps to enable channel responses for Microsoft Teams:
    
    1. Click your connected chat interface on the genie build page.
       
    2. Select **Chat interface** in the sidebar.
       
    3. Click the **Enable channel responses** toggle to enable it.
       
    4. Add additional scopes in your app settings if prompted. Refer to the [Microsoft Teams required scopes](/en/agentic/agent-studio/chat-interface/chat-interface#microsoft-teams) section for more information.
       
    5. Go to the **Genie can chat in** section and select **Specific channels only** or **Any channel it's invited to**. Refer to [Channel support options](/en/agentic/agent-studio/chat-interface/chat-interface#channel-support-options) for more information.
       
       **Specific channels only**
       
       Use the **Channels** drop-down menu to select the channels where the genie is allowed to chat if you select **Specific channels only**. Your genie must still be invited to a channel by a user before it can chat.
       
       **Any channel it's invited to**
       
       No additional configuration is required. Your genie must still be invited to a channel by a user before it can chat.
       
    6. Go to the **In channels, genie responds to** section and select **@mentions only** or **Every message posted**. Refer to [Channel modes](/en/agentic/agent-studio/chat-interface/chat-interface#channel-modes) for more information.
       
    7. Click **Save**.
