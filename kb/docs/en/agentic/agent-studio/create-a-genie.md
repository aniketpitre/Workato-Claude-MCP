---
url: 'https://docs.workato.com/en/agentic/agent-studio/create-a-genie.md'
description: >-
  Create your first genie in Agent Studio, an AI-powered agent that performs
  contextual, goal-oriented tasks using LLMs, knowledge bases, and skills.
---

# Create your first genie

Agent Studio enables you to build genies. Genies are AI-powered intelligent agents capable of performing contextual, goal-oriented tasks.

Watch a quick video guide: Genie basics

[Video](https://www.youtube.com/embed/ohxEyECsOUY?rel=0&si=S4KCXcQXhSb0IVwe)

Genies use LLMs and a detailed prompt to learn new information. The knowledge base recipes and skills that you configure continuously learn from new inputs and adapt to handle dynamic situations effectively.

Get started with step-by-step use cases

Review the [Validate Coupa expenses with an expense genie](/en/getting-started/use-cases/agent-studio/genies/expense-genie-coupa-use-case) use case for a step-by-step guide for building a genie manually, including uploading files and images.

Or refer to the [Connect your knowledge base to Confluence](/en/getting-started/use-cases/agent-studio/knowledge-bases/knowledge-base-confluence-use-case) use case for a step-by-step guide on how to create and connect your knowledge base to Confluence with a knowledge recipe.

Complete the following steps to create your genie:

Watch a quick video guide: Deploy a genie to Slack

[Video](https://www.youtube.com/embed/YJkghyBJsNU?rel=0&si=fj1Uf5pqkobp7eal)

1. Sign in to Workato.
   
2. Go to **AI Hub > Agent Studio** and click **\+ Create genie**. Alternatively, go to the **Projects** page and click **Create > Genie** or press C+G.
   
3. Select **New genie** to create a blank genie.
   
4. Use the **Location** drop-down menu to select a location for your genie.
   
5. Enter a request or goal for your genie in the **What would you like your genie to help with?** field.
   
   ![Create a genie](/assets/genie-start-building.BqOHwuGZ.png)_Create a genie_
   
6. Click **Start building**. The genie **Build** page displays.
   
   > **JOB DESCRIPTIONS ARE AUTOMATICALLY GENERATED**
   > 
   > The **Job description** is automatically generated based on the input you provide to the **What would you like your genie to help with?** field during genie setup and can be edited to suit your requirements.
   
   ![Genie build page](/assets/genie-build-page.DQ8_sDC8.png)_Genie build page_
   

## Change your genie's name

Your genie is assigned a name automatically. You can change the name to better represent the purpose of the genie. For example, you can change your genie's name from `Onxy_8` to `Sales Team`.

Complete the following steps to change the name of a genie:

1. Sign in to Workato.
   
2. Go to **AI Hub > Agent Studio**. A list of your existing genies displays.
   
3. Select the genie you plan to rename.
   
4. Click the genie name.
   
   ![Click the genie name](/assets/rename-a-genie.BfRRTcHB.png)_Click the genie name_
   
5. Enter a new name for your genie.
   
6. Click **✓** (Save) to save your changes.
   
   ![Click Save](/assets/save-name.DJInWrNe.png)_Click Save_
   

## Create a job description

The **Job description** section is where you provide detailed prompts to enable your genie to understand its role, personality, and goals. The **Job description** is automatically generated based on the input you provide to the **What would you like your genie to help with?** field during genie setup and can be edited to suit your requirements. Refer to [Add a detailed job description](/en/agentic/agent-studio/knowledge-bases/knowledge-base-and-database-best-practices#add-a-detailed-job-description) for more information.

Complete the following steps to configure a job description for your genie:

1. Go to the **Job description** section.
   
   ![Go to the Job description section](/assets/go-to-job-description.DECn-Oxr.png)_Go to the **Job description** section_
   
2. Review the detailed instructions generated for your genie in **Job description**. For example:
   
   ```plaintext
   
   What's my job?
   Example: "You are a recruiting coordinator who schedules interviews and keeps candidates informed. Your goal is to reduce time-to-hire while ensuring a positive candidate experience."
   
   Who will need my help?
   Example: "Hiring managers need interview coordination, HR recruiters want automated communications, and job candidates need timely updates and interview details."
   
   How do I get things done?
   Example: "Check calendars first, propose 3 time slots, send invites once confirmed. Pull latest info from ATS for status updates. Always confirm details before acting and follow up within 24 hours."
   
   What should I avoid?
   Example: "Don't make hiring decisions, share salary ranges, or promise specific timelines. Never share candidate info between candidates. Escalate sensitive situations to hiring managers immediately."
   
   What results do you want me to track?
   Example: "Same-day interview scheduling, 90%+ candidate response rates within 48 hours, and hiring manager satisfaction scores."
   
   How should I talk to people?
   Example: "Be warm with nervous candidates, concise with busy hiring managers. Use 'your interview is scheduled' language and always include next steps."
   
   Any extra tips?
   Example: "Double-check calendar availability to avoid conflicts. Over-communicate with candidates rather than leaving them wondering. Keep common Q&A responses ready."
   ```
   
3. Optional. Click **Edit** to update the job description and then click **Save**.
   
   ![Edit the job description](/assets/add-job-description.Cjk4InbO.png)_Edit the job description_
   

## Add an AI model

The AI large language model (LLM) that powers your genie’s core functionality is set to Anthropic Claude by default. You can switch your LLM to OpenAI GPT or to your own LLM.

Complete the following steps to add or update the AI model for your genie:

1. Go to the genie where you plan to add your AI model.
   
2. Click **Edit**.
   
3. Click **AI model**.
   
   ![Click AI model](/assets/change-ai-model.xlfWQHSz.png)_Click **AI model**_
   
4. Select whether to use your own LLM or an LLM hosted by Workato:
   
   **Select from LLMs hosted by Workato**
   
   Select the AI model to use.
   
   ![Select an AI model](/assets/ai-model-selection.DMWaq4yG.png)_Select an AI model_
   
   **Use your own LLM connection**
   
   1. Select **Use your own LLM connection**.
      
   2. Click **\+ New connection**.
      
      ![Click New connection](/assets/new-llm-connection.ClxH_nzc.png)_Click **\+ New connection**_
      
   3. Provide a name for your connection in the **Connection** field.
      
      ![LLM connection configuration](/assets/configure-llm-connection.rSRLIJ5w.png)_LLM connection configuration_
      
   4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
      
   5. Use the **LLM Provider** drop-down menu to select your LLM provider.
      
   6. Refer to [Connect to your own LLM](#connect-to-your-own-llm) to configure your LLM connection.
      
   7. Click **Connect**.
      
   
5. Optional. Click **Use as default for new genies** to use this model as the workspace default.
   
6. Click **Select LLM**.
   
7. Optional. Click **Test** to test the accuracy of the LLM for your scenarios.
   

### Connect to your own LLM

Complete the following steps to configure a connection to your LLM:

**Anthropic**

1. Provide your API key in the **API key** field.
   
2. Provide your API base URL in the **API URL** field. Defaults to `https://api.anthropic.com/v1` if left blank.
   
3. Use the **Model** menu to select or enter your LLM model.
   

**OpenAI Compatible**

1. Provide your API key in the **API key** field.
   
2. Provide your API base URL in the **API URL** field. Defaults to `https://api.openai.com/v1` if left blank.
   
3. Optional. Enter your organization ID in the **Organization ID** field if your OpenAI account has multiple organizations.
   
4. Optional. Enter a project ID in the **Project ID** field if your OpenAI account has multiple projects.
   
5. Use the **Model** menu to select or enter your LLM model.
   

**Azure OpenAI**

1. Provide your API key in the **API key** field.
   
2. Provide your Azure service endpoint URL in the **Endpoint URL** field.
   
3. Use the **Model** menu to select or enter your LLM model.
   
4. Enter the Azure API version to use in the **API Version** field. Defaults to `2024-08-01-preview` if left blank.
   

**AWS Bedrock**

1. Provide your AWS access key ID in the **AWS Access Key ID** field.
   
2. Provide your AWS secret access key in the **AWS Secret Access Key** field.
   
3. Optional. Enter the AWS session token for temporary credentials in the **AWS Session Token** field.
   
4. Use the **AWS Region** menu to select where your Bedrock model is hosted.
   
5. Use the **Model** menu to select or enter your LLM model.
   

## Add a chat interface

The **Chat interface** is the platform through which end users access and interact with your genie. Chat interfaces can only be changed after you stop your genie. Refer to [Getting started with genies: Chat interface](/en/agentic/agent-studio/chat-interface/chat-interface) for more information.

> **CHAT INTERFACE CONFIGURATION**
> 
> The genies feature can only be configured to use Slack, Microsoft Teams, or [Workato GO](/en/agentic/workato-go) as the chat interface. Support for additional chat interface apps is in development.

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
       
    

## Create a knowledge base

Knowledge bases store and organize company-specific information and domain knowledge, enabling your genie to provide more contextualized and accurate responses. Your knowledge base can only be assigned to one genie. Knowledge bases can contain multiple knowledge recipes.

[Knowledge base configuration](/en/agentic/agent-studio/knowledge-bases/knowledge-base-configuration) and [document preparation](/en/agentic/agent-studio/knowledge-bases/knowledge-base-configuration#knowledge-base-document-preparation) ensure that your knowledge base retrieves information efficiently. Refer to [Knowledge base best practices](/en/agentic/agent-studio/knowledge-bases/knowledge-base-and-database-best-practices#knowledge-base-and-database-best-practices) and [Knowledge bases versus databases](/en/agentic/agent-studio/knowledge-bases/knowledge-bases-and-databases#knowledge-bases-versus-databases) for more information.

Complete the following steps to create a knowledge base:

1. Sign in to Workato.
   
2. Go to **AI Hub > Agent Studio**.
   
3. Select the genie where you plan to create a knowledge base.
   
4. Go to the **Knowledge base** section and click **\+ Add**.
   
5. Select **\+ New knowledge base**.
   
6. Enter a name for your knowledge base in the **Knowledge base name** field.
   
   ![Create a knowledge base](/assets/add-knowledge-base.D7qlZXNz.png)_Create a knowledge base_
   
7. Use the **Location** drop-down menu to select a location for your knowledge base.
   
8. Enter a description for your knowledge base in the **Description** field. Genies use descriptions to understand the context and purpose of the knowledge base to determine when to use it.
   
9. Go to the **How will you add data** section and select the data source you plan to use to sync the information in your knowledge base.
   
   **Uploads and recipes**
   
   **Uploads and recipes** is selected by default. No additional configuration is required.
   
   ![Knowledge recipes](/assets/sync-knowledge-recipes.CSsrmDs3.png)_Sync with Knowledge recipes_
   
   **Choose from connected data sources**
   
   1. Click **Choose from connected data sources**.
      
      ![Click Workato GO data sources](/assets/sync-workato-go-data-sources.DE5n9fkX.png)_Click **Workato GO data sources**_
      
   2. Use the **Data sources** drop-down menu to select the data sources Workato GO uses with your genie.
      
   
10. Click **Create knowledge base**.
    

## Create a knowledge recipe

Knowledge base recipes sync and update information from your various applications to your knowledge base. The knowledge base recipe ensures that your genie has access to the latest data and stays aligned with your business requirements. Refer to [Knowledge base](/en/agentic/agent-studio#knowledge-base) for more information.

Complete the following steps to create a knowledge recipe:

1. Sign in to Workato.
   
2. Go to **AI Hub > Agent Studio**.
   
3. Select the genie where you plan to create a knowledge base recipe.
   
4. Go to the **Knowledge bases** section and select the knowledge base where you plan to add your knowledge recipe.
   
5. Click **\+ Add knowledge**.
   
6. Select **New knowledge recipe**.
   
7. Enter a name for your knowledge recipe in the **Recipe name** field.
   
8. Use the **Location** drop-down menu to select a location for your knowledge recipe.
   
   ![Set up your knowledge recipe](/assets/set-up-knowledge-recipe.DSLepKGW.png)_Set up your knowledge recipe_
   
9. Click **Start building**. The recipe editor opens with the [Store knowledge](/en/agentic/agent-studio/connectors/workato-genie-connector/actions/store-knowledge) action automatically selected.
   
10. Configure your trigger.
    
    ![Knowledge recipe with Store knowledge in a knowledge base action automatically selected](/assets/knowledge-recipe.CqTvF1Cz.png)_Knowledge recipe with **Store knowledge in a knowledge base** action automatically selected_
    
11. Test your recipe to ensure workflow compatibility with your genie.
    
12. Click **Save**.
    

### Add knowledge to a genie

Complete the following steps to add an existing knowledge base to your genie:

1. Go the genie where you plan to add knowledge.
   
2. Click **Edit**.
   
3. Go to the **Knowledge bases** section and click **\+ Add**.
   
   ![Add knowledge](/assets/add-knowledge.Df-IqV0W.png)_Click **\+ Add**_
   
4. Search for and select the knowledge you plan to add to your genie.
   

## Create skills

You can create skills to define workflows for your genie. This gives your genie different skills, such as starting a workflow or returning a response. Skills equip your genie with a comprehensive toolset to take action and respond to end users. Refer to [Design skills for databases](/en/agentic/skills/design-skills-for-databases) if you plan to use a database to store the data your genie references.

Genies can interpret text within document files and use this content in skills using the **File** input parameter type. This input passes file data to the recipe as a datapill.

Refer to [Create a skill with a File input parameter](/en/agentic/agent-studio/upload-files-and-images#create-a-skill-recipe-with-a-file-input-parameter) for more information.

Skills use [Verified user access](/en/agentic/agent-studio/verified-user-access) to allow each end user to authenticate with their own credentials when a skill runs. This ensures that the skill performs actions using the individual user's identity and permissions.

Your end users have the ability to manage their runtime user connection through the genie chat interface.

Skills can consume [MCP servers](/en/mcp). This enables you to access external APIs and integrate with third-party tools without custom skill development. Skills can call custom MCP servers and common provider MCP servers.

You can [share your skills in the Community Library](/en/community-library#community-library).

### Create a new skill

Complete the following steps to create and add a skill to your genie:

1. Sign in to Workato.
   
2. Go to **AI Hub > Agent Studio**.
   
3. Select the genie where you plan to add the skill.
   
4. Go to the **Enterprise skills** section and click **\+ Add**.
   
5. Select **Skill**.
   
6. Select **New skill** and click **Create new skill**.
   
   ![Select New skill](/assets/create-new-skill.DRmGQ4Wd.png)_Select **New skill**_
   
   Alternatively, you can create a skill from the **Projects** page by clicking **Create > Skill** or pressing C+S.
   
7. Provide a name for your skill in the **Skill name** field.
   
8. Use the **Location** drop-down menu to select a location for your skill.
   
9. Click **Start building**. The recipe editor opens with the [Start workflow](/en/agentic/agent-studio/connectors/workato-skill-connector/start-workflow) trigger and [Return response](/en/agentic/agent-studio/connectors/workato-skill-connector/return-response) action automatically selected.
   
10. Use the **Require user confirmation before executing skill?** drop-down menu to determine whether a skill must be confirmed by a user before executing.
    
11. Provide a description for your skill workflow in the **When should your genie run this skill?** field. The genie uses this description to decide when to trigger this workflow.
    
12. Go to the **What inputs will your genie require to run this skill?** section and click **Use JSON** or **Add fields manually** to provide a description of the schema recipe parameters.
    
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
       
    
13. Go to the **Result schema** section and click **Use JSON** or **Add fields manually** to provide a description for the recipe return value.
    
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
       
    
14. Click **Select an app and action** step in the recipe.
    
15. Search for and select the app you plan to use. A list of available actions for the app displays.
    
16. Select the action you plan to use.
    
17. Select the connection type you plan to use for the skill.
    
    ![Connection type](/assets/users-connection.DrJMnyxd.png)_Choose a connection type_
    
    - **End user's connection**: Skills perform actions based on the identity and permissions of the user who connects to the application. Users authenticate with their own credentials to execute the skill.
    - **This recipe's connection**: This option uses the connection established by the recipe builder and follows the same principles as normal app connections.
    
    > **VERIFIED USER ACCESS AUTHENTICATION REQUIREMENTS**
    > 
    > Only app connections that use OAuth 2.0 authorization code grant are available for user's connection. Refer to [Verified user access](/en/agentic/agent-studio/verified-user-access) for more information.
    
18. Provide a name for your connection in the **Name** field.
    
19. Use the **Location** drop-down menu to select the project where you plan to store the connection.
    
20. Provide information for all required app connection fields. Connection configuration fields vary based on the app you select.
    
21. Click **Connect**.
    
22. Test your recipe to ensure workflow compatibility with your genie.
    
23. Click **Save**.
    

### Add existing skills to a genie

Complete the following steps to add existing skills to your genie:

1. Go the genie where you plan to add an existing skill.
   
2. Click **Edit**.
   
3. Go to the **Enterprise skills** section.
   
4. Click **+Add > Skill**.
   
5. Select **Add existing skills**.
   
   ![Select Add existing skills](/assets/add-skills.D4h9Sq6E.png)_Select **Add existing skills**_
   
6. Search for and select the skill you plan to add to your genie.
   
   ![Select skills](/assets/add-skills.D4h9Sq6E.png)_Select skills_
   
7. Click **Add skills**.
   

### Add MCP server skills to a genie

Complete the following steps to add MCP server skills to your genie:

1. Sign in to Workato.
   
2. Go to **AI Hub > Agent Studio**.
   
3. Select the genie to edit.
   
4. Click **Edit**.
   
5. Go to the **Enterprise skills** section and click **\+ Add**.
   
6. Select **MCP server**.
   
7. Select a common provider MCP server or click **\+ Custom MCP server**.
   
   ![Select an MCP server option](/assets/add-mcp-server.DBvtu3EL.png)_Select an MCP server option_
   
8. Configure your MCP server:
   
   **Custom MCP server**
   
   #### Add skills from a custom MCP server
   
   1. Click **\+ Custom MCP server > Next**.
      
   2. Provide a name for your MCP server connection in the **Connection name** field.
      
      ![Set up your MCP server connection](/assets/add-a-custom-mcp-server._Gf5dUvn.png)_Set up your MCP server connection_
      
   3. Use the **Location** drop-down menu to select a location for your MCP server connection.
      
   4. Provide your MCP server URL in the **MCP Server URL** field.
      
   5. Use the **Authentication Type** drop-down menu to select your authentication method provide the necessary credentials. OAuth2 authentication is required if you plan to use [Workato Identity for your MCP server authentication](/en/mcp/mcp-authentication#oauth2-authentication-with-workato-identity).
      
   6. Click **Connect**.
      
   7. Select the checkbox for each tool you plan to add as a skill to your genie.
      
      ![Select MCP server tools](/assets/select-mcp-server-tools.HEk9Cf5a.png)_Select MCP server tools_
      
   8. Click **Done**. The MCP server tools you selected display in the **Enterprise skills** section on your genie **Overview** page.
      
   
   **Common provider MCP server**
   
   #### Add skills from a common provider MCP server
   
   1. Select the common provider MCP server you plan to use.
      
   2. Click **Next**.
      
   3. Provide a name for your MCP server connection in the **Connection name** field.
      
   4. Use the **Location** drop-down menu to select a location for your MCP server connection.
      
   5. Complete the remaining connection fields. These fields vary by provider and authentication method.
      
      ![Atlassian provider MCP server](/assets/atlassian-provider-mcp-server-example.BnXuiabO.png)_Atlassian provider MCP server_
      
   6. Click **Connect**.
      
   7. Select the checkbox for each tool you plan to add as a skill to your genie.
      
      ![Select MCP server tools](/assets/select-mcp-server-tools.HEk9Cf5a.png)_Select MCP server tools_
      
   8. Click **Done**. The MCP server tools you selected display in the **Enterprise skills** section on your genie **Overview** page.
      
   

## Upload files and images

You can upload files and images to your genies through your chat interface. This enables your end users to use files and images with text prompts when interacting with your genie.

Complete the following steps to upload a file or image in Agent Studio:

1. Go to the chat interface configured for your genie. For example: Workato GO.
   
2. Go to **AI Genies** and select the genie you plan to use.
   
3. Start a chat with your genie.
   
4. Click the attachment icon (paperclip).
   
   ![Click the attachment icon](/assets/upload-file-in-genie-chat.ZRX9jqpA.png)_Click the attachment icon_
   
5. Go to the file or image you plan to upload in your file system.
   
6. Click the file or image and click **Open**.
   

## Advanced features

Agent Studio includes the following advanced features to enhance your genie's abilities:

### Create an app event

App events enable genies to act proactively by responding to triggers from external systems, such as Salesforce or Zoom, instead of waiting for a user to initiate a conversation. These events help embed genies directly into existing workflows and allow genies to anticipate user needs and offer assistance without being prompted.

Refer to [Create an App event](/en/agentic/agent-studio/app-events#create-an-app-event) for more information.

### Create an approval request with Business approvals

Business approvals in Agent Studio let you build skills with approval workflows. Business approvals rely on the following actions:

- [**Create approval request**](/en/agentic/agent-studio/connectors/workato-genie-connector/actions/create-approval-request): Use this action to create a new approval request in a data table you specify. The information from this request is shared with the user assigned to the approval task.
- [**Assign task to user**](/en/agentic/agent-studio/connectors/workato-genie-connector/actions/assign-task-to-user): Use this action to assign a task to a user. The assignee receives a prompt within the chat interface you configured to approve or reject the request. The skill waits until the task is completed or expires.

Refer to [Business approvals](/en/agentic/agent-studio/business-approvals#business-approvals) for more information.

### Assign a task to a genie

Agent orchestration enables your genies to work autonomously within recipes. Recipes assign tasks to genies without user input. Genies process tasks while the recipe job runs.

Use the **Assign task to genie** action to assign a task to a genie. This enables your genie to trigger a recipe autonomously, perform the assigned task, and return a response.

Refer to [Assign task to genie action](/en/agentic/agent-studio/agent-orchestration#assign-task-action) for more information.

### Create a KPI and Action Board for Workato GO

A KPI (Key Performance Indicator) enables you to measure progress toward goals. KPIs can help highlight areas of success and areas that require improvement with your genies. The KPI tab is only visible on the **Overview** page of genies that use the Workato GO chat interface.

Refer to [Create a KPI](/en/agentic/agent-studio/action-board#create-a-kpi) for more information.

---
