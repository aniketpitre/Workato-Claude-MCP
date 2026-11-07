---
url: >-
  https://docs.workato.com/en/getting-started/use-cases/data-tables/store-agent-conversation-ids-in-a-data-table.md
description: >-
  Use a Workato data table to store genie conversation IDs so your genie
  remembers previous messages from each user.
---

# Build a data table to store genie conversation IDs

This use case shows how to use a [data table](/en/data-tables) as persistent memory for a genie. Each task assigned to a genie starts a new conversation by default. Your genie needs a way to match each user to their existing genie conversation and retain context when it receives messages from multiple users through an interface, such as Telegram.

This use case demonstrates how a data table stores a mapping between each Telegram user ID and the genie's conversation ID. The recipe looks up the sender in the data table before each task and, if a record exists, continues the same conversation. The recipe upserts the conversation ID back into the table after each task.

You can add skills that use this conversation memory to your genies to carry out tasks that span multiple messages, such as scheduling a calendar event from a conversation about an upcoming appointment.

## What does this genie do?

This genie receives Telegram messages through a Workato recipe and uses a data table to store conversation IDs to match users to conversations and retain context.

```mermaid
flowchart TD
  subgraph M[" "]
    direction LR
    subgraph T[&nbsp Create a <br/> data table &nbsp]
      direction LR
    end
    subgraph TT[Add columns for <br/> Telegram ID and <br/> genie conversation ID]
        direction LR
    end
  end
  subgraph Q[" "]
    direction LR
    subgraph RR[&nbsp Create a <br/> Telegram recipe &nbsp]
        direction LR
    end
    subgraph RRR[Connect your <br/> Telegram bot and genie]
        direction LR
    end
  end
  subgraph N[" "]
    direction LR
    subgraph O[&nbsp Search and upsert <br/> data table records &nbsp]
        direction LR
    end
    subgraph OO[Look up the sender's <br/> conversation ID before the task <br/> and save it after the task]
        direction LR
    end
  end

  A([Build a genie <br/> with memory]) -- Create your data table --> M -- Create a <br/> Telegram recipe --> Q -- Add data table actions --> N --> B([Genie continues <br/> each user's conversation])
  T --> TT
  O --> OO
  RR --> RRR
  classDef default fill:#fff,stroke:#67eadd,stroke-width:2px;
  classDef WorkatoTeal fill:#67eadd,stroke:#67eadd,stroke-width:2px,color:#000;
  classDef WorkatoPink fill:#fff,stroke:#f66,stroke-width:2px;
  classDef WorkatoBlue fill:#fff,stroke:#5159f6,stroke-width:2px,color:#fff;
  classDef WorkatoPurple fill:#fff,stroke:#a99ff5,stroke-width:2px,color:#000;
  classDef SubgraphDash fill:#67eadd,stroke:#f66,stroke-width:2px,color:#000,stroke-dasharray: 5 5
  classDef SubgraphDashPurple fill:#a99ff5,stroke:#f66,stroke-width:2px,color:#000,stroke-dasharray: 5 5
  classDef SubgraphDashBlue fill:#5159f6,stroke:#f66,stroke-width:2px,color:#fff,stroke-dasharray: 5 5
  classDef SubgraphLight stroke:#68eade,stroke-width:2px
  class A,B WorkatoTeal
  class O,OO SubgraphDash
  class T,TT SubgraphDashPurple
  class N SubgraphLight
  class RR,RRR SubgraphDashBlue
  class M WorkatoPurple
  class Q WorkatoBlue
```

## Why use a data table for conversation IDs?

Data tables are a good fit for this scenario for the following reasons:

- **Persistence across recipe jobs**: Each recipe job runs independently. A data table retains the conversation ID after the job ends, so the next message from the same user can pick up where the last message left off.
- **Fast lookups by key**: The recipe searches the table by a single `telegram-id` column.
- **No external database to maintain**: Data tables are scalable and secure, so you don't need to provision or manage separate storage.
- **Easy to inspect and edit**: You can open the table in the **Data tables** interface to view stored conversation IDs or delete a record to reset a user's conversation.

> **DATA TABLE LIMITATIONS**
> 
> Data tables aren't designed to store sensitive PCI data, such as credit card numbers, or to function as large relational databases. This use case stores only user IDs and conversation IDs. Don't use data tables to store the contents of sensitive conversations.

## Build your genie with a conversation ID data table

Complete the following steps to create a Telegram-based genie that uses a data table to maintain conversation context for each user:

> **USE CASES ARE INTENDED AS EXAMPLES ONLY**
> 
> Use cases are intended to serve as examples. Modifications, such as triggers, actions, data table columns, or connection permissions may require adjustments for your specific setup.

1. Sign in to Workato.
   
2. Create a data table to store conversation IDs.
   
   ### Create a data table to store conversation IDs
   
   This step creates a data table that persists the genie's conversation ID against each Telegram user's ID. This allows the genie to retain context across multiple messages from the same user.
   
   > **FIRST-TIME USERS**
   > 
   > The first time a user messages your Telegram bot, the **Search records** action doesn't return records because the user doesn't have a conversation ID yet. Leave the genie's conversation ID empty so the genie starts a new conversation. The upsert step in the next section saves the new conversation ID for future messages.
   
   1. Go to the project where you plan to store your data table and click **Create > Data table** or press C+T.
      
   2. Enter a name for your data table in the **Data table name** field. For example: `Telegram genie conversations`.
      
   3. Use the **Location** drop-down menu to select a location for your data table.
      
   4. Click **Start building**.
      
   5. Add a column with the label `telegram-id` to store the Telegram user's sender ID.
      
   6. Add a second column with the label `genie-conversation-id` to store the genie's conversation ID.
      
      ![Add columns to your data table](/assets/create-a-data-table.MXv1Z3Y8.png)_Add columns to your data table_
      
   7. Click **Save**.
      
   
3. Set up your Telegram bot.
   
   ### Set up your Telegram bot
   
   This step creates a new Telegram bot and retrieves the API token needed to connect it to Workato.
   
   1. Sign in to your Telegram app and search for the **@BotFather** account.
      
   2. Start a conversation with **@BotFather** and enter the `/newbot` command.
      
      ![Create a new Telegram bot](/assets/create-telegram-bot.z3bFUQV5.png)_Create a new Telegram bot_
      
   3. Enter a human-readable name for your Telegram bot when prompted. For example: `Workato PA genie`.
      
   4. Enter a unique username that ends with `bot` when prompted. For example: `workato_bot`.
      
   5. Copy the secret API token that **@BotFather** provides in the confirmation message. You must use this token to connect your Telegram bot to Workato.
      
   
4. Create a Telegram connection.
   
   ### Create a Telegram connection
   
   This step installs the Telegram community connector and creates a connection between Workato and your Telegram bot.
   
   1. Sign in to your Workato account.
      
   2. Go to **Community Library > Custom Connectors**.
      
   3. Search for `Telegram` and select it as your app.
      
   4. Click **Install**.
      
      ![Install the Telegram community connector](/assets/install-telegram-community-connector.CnGRAEgg.gif)_Install the Telegram community connector_
      
   5. Enter a name for your connection in the **Name** field.
      
   6. Use the **Save connection in** drop-down menu to select a location for your connection.
      
   7. Enter the API token you received from **@BotFather** in the **API token** field.
      
   8. Click **Connect**.
      
   
5. Set up a recipe to process incoming Telegram messages.
   
   ### Set up a recipe to process incoming Telegram messages
   
   This step ensures that messages sent to your Telegram bot reach Workato and are processed correctly.
   
   1. Go to the project where you plan to store your recipe and click **Create > Recipe** or press C+R.
      
   2. Enter a name for your recipe in the **Name** field and use the **Save recipe in** drop-down menu to select a project location.
      
   3. Click **Pick a starting point > Select an app**.
      
   4. Search for `Telegram` and select it as your app.
      
   5. Select the **New Event** trigger and connect using the Telegram connection you created in the preceding steps.
      
   6. Click **\+ Add step** and search for and select `Telegram`.
      
      ![Set up your Telegram Send message action](/assets/telegram-send-message-action.AHCnUhxi.gif)_Set up your Telegram **Send message** action_
      
   7. Select the **Send message** action.
      
   8. Map the Telegram Message > Chat ID (Step 1) datapill to the **Chat ID** field.
      
   9. Enter `Message received` in the **Message to send** field.
      
   10. Optional. Click **Test recipe** and send a message to your Telegram bot. Your recipe is configured correctly if you receive a reply.
       
   
6. Add a genie to the recipe.
   
   ### Add a genie to the recipe
   
   This step creates a genie that processes incoming Telegram messages and replies to the user.
   
   1. Go to the project where you plan to store your genie and click **Create > Genie**, or press C+G.
      
   2. Enter a request or goal for your genie in the **What would you like your genie to help with?** field. For example:
      
      ```plaintext
      You are a personal assistant who responds to users' messages. If the message contains
      information about an upcoming event, you can create a calendar event for the user
      with the given information.
      ```
      
   3. Use the **Save genie in** drop-down menu to select a location for your genie.
      
      ![Create a new genie](/assets/telegram-pa-genie.ChI4azAY.png)_Create a new genie_
      
   4. Click **Start building**. The genie **Build** page displays with the **Job description** automatically generated based on the input you provided. You can edit this to suit your requirements.
      
   5. Return to the recipe editor and click **\+ Add step** _before_ the Telegram Send Message action step.
      
      ![Click + Add step before the Telegram Send Message action step](/assets/assign-task-to-genie.7yTLCF8p.gif)_Click **\+ Add step** _before_ the Telegram Send Message action step_
      
   6. Select **Action in app**, search for `Workato Genie`, and select it as your app.
      
   7. Select the **Assign task to genie** action.
      
   8. Use the **Genie** drop-down menu to select the genie you created in the preceding steps.
      
   9. Enter a description that instructs the genie to process the incoming message in the **Task Description** field.
      
   10. Map the Telegram trigger Text (Step 1) datapill after your description in the **Task Description** field.
       
       ![Configure the Task Description field](/assets/genie-task-description.DGPRTrDw.png)_Configure the **Task Description** field_
       
   11. Click **Save**.
       
   
7. Look up the sender's conversation ID in the data table.
   
   ### Look up the sender's conversation ID in the data table
   
   This step adds a Workato Data tables **Search records** action that checks whether the sender's Telegram ID has a corresponding conversation ID in the data table. An existing conversation ID indicates a previous conversation that the genie can continue.
   
   > **FIRST-TIME USERS**
   > 
   > The first time a user messages your Telegram bot, the **Search records** action doesn't return records because the user doesn't have a conversation ID yet. Leave the genie's conversation ID empty so the genie starts a new conversation. The upsert step in the next section saves the new conversation ID for future messages.
   
   1. Return to the recipe editor and click **\+ Add step** _before_ the **Assign task to genie** action step.
      
   2. Select **Action in app**, search for `Workato Data Tables`, and select it as your app.
      
   3. Select the **Search records** action.
      
   4. Use the **Data table** drop-down menu to select the data table you created in the preceding steps.
      
   5. Go to the **Filter** section and click **Add filter**.
      
   6. Use the **Column name** drop-down menu to select **telegram-id**.
      
   7. Use the **Operand** drop-down menu to select **equals**.
      
   8. Map the Telegram ID (Step 1) datapill to the **Value** field. This datapill is located under **Telegram > Message > From**.
      
      ![Configure the data table to search Telegram](/assets/telegram-data-table-configuration.BvJOfw8t.gif)_Configure the data table to search Telegram_
      
   9. Click **Save**.
      
   
8. Pass the stored conversation ID to the genie.
   
   ### Pass the stored conversation ID to the genie
   
   This step maps the conversation ID returned by the data table search to the **Assign task to genie** action. This is what allows the genie to continue an existing conversation instead of starting a new one.
   
   1. Click the **Assign task to genie** step in the recipe editor.
      
   2. Go to the **Conversation ID** field.
      
   3. Map the Workato Data tables genie-conversation-id (Step 2) datapill from the **Search records** step to the **Conversation ID** field. Use the first record in the search results.
      
   4. Click **Save**.
      
   
9. Save the conversation ID to the data table.
   
   ### Save the conversation ID to the data table
   
   This step adds a Workato Data tables **Upsert record** action that saves the conversation ID returned by the genie. The action creates a record for new users and updates the record for returning users.
   
   1. Click **\+ Add step** _after_ the **Assign task to genie** action step.
      
   2. Select **Action in app**, search for `Workato Data Tables`, and select it as your app.
      
   3. Select the **Upsert record** action.
      
   4. Use the **Data table** drop-down menu to select the data table you created in the preceding steps.
      
      ![Configure the Upsert record action](/assets/upsert-record-action.B59Jf31_.gif)_Configure the **Upsert record** action_
      
   5. Use the **Primary key** drop-down menu to select **telegram-id**.
      
   6. Go to the **Record fields** section and map the Telegram From ID (Step 1) datapill to the **telegram-id** field.
      
   7. Map the Workato Genie Conversation ID (Step 3) datapill to the **genie-conversation-id** field.
      
   8. Click **Save**.
      
   
10. Test your genie's memory.
    
    ### Test your genie's memory
    
    This step confirms that the data table is storing conversation IDs and that the genie uses them.
    
    1. Click **Test recipe** and send a message to your Telegram bot. For example: `My dentist appointment is next Tuesday.`
       
    2. Open your data table and confirm that a new record exists with your Telegram ID and a genie conversation ID.
       
    3. Send a follow-up message that depends on the first one. For example: `Actually, make that 4 PM.` The genie should respond with the earlier appointment in mind.
       
    4. Return to your data table and confirm that the same record was updated rather than a duplicate record created.
       
    
11. Optional. Extend your genie with a Google Calendar skill.
    
    ### Extend your genie with a Google Calendar skill
    
    You can give your genie skills that benefit from context with conversation memory in place. This step adds a skill that converts messages into Google Calendar events. Users can refine events across several messages because the genie remembers earlier messages.
    
    #### Create a Google Calendar connection
    
    This step creates a connection between Workato and your Google Calendar account to allow your genie to create calendar events on your behalf.
    
    Refer to the following sections to set up your Google Calendar connection:
    
    ##### OAuth 2.0 authentication
    
    Complete the following steps to set up your Google Calendar connection using OAuth 2.0:
    
    View OAuth 2.0 authentication steps
    
    1. Click **Create > Connection** or press C twice.
       
    2. Search for and select `Google Calendar` as your connection on the **New connection** page.
       
    3. Provide a name for your connection in the **Connection name** field.
       
    4. Select the project where you plan to store the connection from the **Location** drop-down menu.
       
    5. Select **OAuth 2.0** as the **Authentication type**.
       
    6. Click **Sign in with Google**, then sign in to your Google account. Ensure your Google account has sufficient permissions to manage the events and calendars you plan to use in Workato. ![Click Sign in with Google](/assets/google-calendar-sign-in-with-google.DQ57V-DM.png)_Click **Sign in with Google**._
       
    
    ##### Service account authentication
    
    View Service account authentication steps
    
    A Google service account is a specialized Google account associated with a Google Cloud Project (GCP) that can run API requests on your behalf.
    
    Service accounts provide the following benefits:
    
    - **Continuous operation:** Service accounts ensure that operations continue even if individual user permissions change.
    - **Dedicated permissions:** Service accounts can only access projects that you share with them.
    - **Dedicated API quotas:** You can manage a service account's API quotas through GCP and request quota increases directly from Google.
    
    Refer to the [Google service account documentation](https://cloud.google.com/iam/docs/understanding-service-accounts) to learn more about service accounts.
    
    Service account authentication consists of the following actions:
    
    - [Set up a Google service account](#set-up-a-google-service-account)
    - [Enable the Google Calendar API](#api-setup)
    - [Complete setup in Workato](#setup)
    
    ###### Minimum scopes for service account connections
    
    The following scopes are required to connect to Google Calendar using a service account:
    
    - `https://www.googleapis.com/auth/calendar`
    - `https://www.googleapis.com/auth/calendar.events`
    - `https://www.googleapis.com/auth/admin.directory.resource.calendar`
    - `https://www.googleapis.com/auth/tasks`
    - `https://www.googleapis.com/auth/userinfo.email`
    
    A `401 Unauthorized error` may occur when the service account uses the `Owner` role or lacks required scopes. Assign the `Editor` role to the service account in the Google Cloud Console and confirm it includes all required scopes listed above. This ensures the service account can authenticate and access Google Calendar successfully.
    
    Refer to the [Google Calendar API scopes](https://developers.google.com/calendar/api/auth) documentation for a complete list of supported scopes.
    
    ###### Set up a Google service account
    
    View Set up a Google service account steps
    
    Complete the following steps to set up a Google service account:
    
    1. [Create a service account](https://cloud.google.com/iam/docs/creating-managing-service-accounts#creating) in your GCP project.
       
    2. Go to **IAM & Admin > Service accounts**. Ensure your dashboard is scoped to the project that contains your service account. ![Check the scope of your dashboard.](/assets/service-project-scope.8Rf50DK2.png)_Check the scope of your dashboard._
       
    3. Click the **Email** of the service account you intend to use. ![Click the email of the service account you intend to use.](/assets/service-email-button.C9qaZFkJ.png)_Click the **Email** of the service account you intend to use._
       
    4. Copy the service account's **Email** and save it to configure your connection later. ![Copy the account's email](/assets/service-account-email.DM6BBBhN.png)_Copy the account's **Email**._
       
    5. Go to the **KEYS** tab.
       
    6. [Generate a private key](https://cloud.google.com/iam/docs/creating-managing-service-account-keys#creating_service_account_keys) and download it in JSON format. You can only download the key once.
       
    7. Open the JSON file, then copy the entire private key from `-----BEGIN PRIVATE KEY-----` to `-----END PRIVATE KEY-----\n` (inclusive) and save it to configure your connection later.
       
    
    ###### Enable the Google Calendar API
    
    View Enable the Google Calendar API steps
    
    You must enable the Google Calendar API before you return to Workato to finish setting up your connection.
    
    1. Sign in to Google's [API library](https://console.developers.google.com/apis/library).
       
    2. Search for and select the `Google Calendar API`.
       
    3. Click **Enable** to enable the API. ![Enable the Google Calendar API](/assets/google-calendar-api.DMWBkrRb.png)_**Enable** the `Google Calendar API`_
       
    
    ##### Complete setup in Workato
    
    View Workato setup steps
    
    Complete the following steps in Workato to set up your Google Calendar connection using a service account:
    
    1. Click **Create > Connection** or press C twice.
       
    2. Search for and select `Google Calendar` as your connection on the **New connection** page.
       
    3. Provide a name for your connection in the **Connection name** field.
       
    4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
       
    5. Select **Service account** as the **Authentication type**.
       
    6. Enter your service account's **Private key**.
       
    7. Provide the **User email** of the account you plan to impersonate.
       
       User impersonation lets the service account act on behalf of a designated user, accessing and managing events in their Google Calendar. Impersonating a user ensures data accuracy and enforces the permissions and access controls set for that user in Google Calendar. Refer to Google's [Service account impersonation](https://cloud.google.com/iam/docs/service-account-impersonation) guide for more information.
       
    8. Click **Sign in with Google** to complete the setup. ![Configure Google Calendar service account connection](/assets/service-account-connection.CG2N5lxI.png)_Configure Google Calendar service account connection_
       
    
    #### Create a skill to convert messages into Google Calendar events
    
    This step creates a custom skill that enables your genie to detect messages that should be converted into Google Calendar events.
    
    1. Go to the **Build** page of the genie you created in the preceding steps.
       
    2. Go to the **Skills** section and click **\+ Add > Skill**.
       
    3. Select **New skill** and click **Create new skill**.
       
       Alternatively, you can create a skill from the **Projects** page by clicking **Create > Skill** or pressing C+S.
       
    4. Provide a name for your skill in the **Name** field. For example: `Create Google Calendar event`.
       
    5. Use the **Location** drop-down menu to select a location for your skill.
       
    6. Click **Start building**. The recipe editor opens with the **Start workflow** trigger and **Return response** action automatically selected.
       
    7. Select the **Start workflow** trigger.
       
    8. Go to the **What inputs will your genie require to run this skill?** section and click **Add fields manually**. Add the following fields:
       
       | Label | Data type |
       | --- | --- |
       | `event_title` | String |
       | `event_date` | Date |
       | `event_time` | String |
       | `event_description` | String |
       
    9. Go to the **What should be returned to the genie after this skill is run?** section and add the following field:
       
       | Label | Data type |
       | --- | --- |
       | `created_event` | Boolean |
       
       ![Configure inputs and output](/assets/google-calendar-inputs.DRjCBEBv.png)_Configure inputs and output_
       
    10. Click **\+ Add step**, search for `Google Calendar`, and select it as your app.
        
    11. Select the **Create event** action.
        
    12. Map the Start datetime (Step 1) datapill to the **Start date time** field.
        
        ![Configure the Create event action](/assets/create-event-action.D6XicUFp.png)_Configure the **Create event** action_
        
    13. Map the End datetime (Step 1) datapill to the **End date time** field.
        
    14. Map the Event name (Step 1) datapill to the **Name** field.
        
    15. Map the Event description (Step 1) datapill to the **Event description** field.
        
    16. Click **\+ Add step** and select **IF condition** to handle the result of the calendar event creation.
        
    17. Map the Google Calendar ID (Step 2) datapill to the **Data field**.
        
    18. Use the **Condition** drop-down menu to select **is present**.
        
    19. Go to the **Yes** branch and click **Select an app and action**.
        
    20. Search `Workato Genie` and select it as your app.
        
    21. Select **Return response to genie** as your action.
        
    22. Go to the **Results** section and use the **Created Event** drop-down menu to select **Yes**.
        
        ![Set up your IF condition](/assets/if-condition-setup.BsASC_IL.png)_Set up your IF condition_
        
    23. Go to the **No** branch. The **Return response to genie** action should already be present.
        
    24. Click the **Return response to genie** action to open it.
        
    25. Configure the **Yes** and **No** paths of the **IF** block to return the appropriate `created_event` boolean response to the genie.
        
    26. Click **Save**.
        
    
    #### Update your genie task description
    
    This step updates the genie task description to include instructions on how the genie should use the Google Calendar skill.
    
    1. Click the **Assign task to genie** step in the recipe editor.
       
    2. Go to the **Task Description** field and update the description to use the following instructions:
       
       > **DON'T REMOVE THE TELEGRAM DATAPILL**
       > 
       > Don't remove the Telegram datapill you mapped to the **Task Description** field in previous steps.
       
       ```plaintext
       
       Do the following based on the user's message and conversation history:
       
       1. Identify if the message contains an event where you need to set up a calendar event.
       2. If yes, then call the skill to create the event in Google Calendar.
       3. If not, then respond normally.
       4. When responding, you do not need to include your classification of whether it was a task.
       ```
       
    3. Click **Save**.
       
       ![Update the Task Description](/assets/updated-task-description.CLVsbtwC.png)_Update the **Task Description**_
