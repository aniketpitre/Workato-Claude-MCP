---
url: >-
  https://docs.workato.com/en/data-orchestration/data-pipeline-recipe/pipeline-triggers.md
description: >-
  Build Workato recipes that monitor data pipelines, automate error handling,
  and send alerts when object syncs fail.
---

# Monitor data pipelines using recipes

You can use recipes to orchestrate monitoring workflows for your data pipelines. These recipes help you respond to pipeline sync results, automate error handling, and send alerts when syncs fail.

## Use case: Monitor pipeline failures

A common use case is error monitoring. You can configure a recipe to notify teams when any object in a pipeline fails to sync.

Workato recommends triggering recipes on every sync completion, rather than failed syncs. This ensures object-level failures are captured. Failed syncs only detect sync-level issues, which may exclude failures within individual objects.

### Configure pipeline triggers in recipes

Complete the following steps to build a pipeline monitoring recipe:

1. Sign in to Workato.
   
2. Select the project where you plan to create the recipe.
   
3. Create connections for PipelineOps by Workato:
   
   Set up your PipelineOps connection
   
   ### Set up your PipelineOps connection
   
   1. Select **Create > Connection** or press C twice.
      
   2. Search for `PipelineOps by Workato` and select it as your app.
      
   3. Provide a name for your connection in the **Connection name** field.
      
   4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
      
   5. Click **Connect**.
      
   
4. Set up your Gmail connection
   
   ### Set up your Gmail connection
   
   Workato supports two types of connections to Gmail:
   
   - [OAuth 2.0 authentication](#authentication-oauth)
   - [Service account authentication](#connect-to-a-service-account-in-workato)
   
   #### OAuth 2.0 authentication
   
   Complete the following steps to set up an OAuth 2.0 connection:
   
   1. Sign in to your Workato account and go to the project where you plan to add your Gmail connection.
      
   2. Click **Create > Connection** (or press C twice), then select **Gmail** as your connection.
      
   3. Provide a **Connection name** that uniquely identifies the Gmail connection instance.
      
   4. Click the **Authentication type** menu and select **OAuth 2.0**.
      
   5. Optional. Click **Advanced settings** and select additional **OAuth 2.0 scopes**. If left blank, the following scopes are requested:
      
      - **See your primary Google Account email address**
      - **See and edit your email labels**
      - **Send email on your behalf**
      - **View your email messages and settings**
      - **Read, compose, and send emails from your Gmail account**
   6. Click **Sign in with Google** and sign in to your Google account to complete the setup.
      
   
   #### Connect to a service account in Workato
   
   Complete the following steps to set up a service account connection:
   
   1. Sign in to your Workato account and navigate to the project where you plan to add your Gmail connection.
      
   2. Click **Create > Connection** (or press C twice), then select **Gmail** as your connection.
      
   3. Select the **Authentication type** drop-down menu.
      
   4. Click **Sign in with Google** and sign in to your Google account to complete the setup.
      
   
5. Go back to your project and click **Create > Recipe** or press C+R.
   
   ![Create a new recipe](/assets/create-recipe-standard.CiyoivKN.png)_Create a new recipe_
   
6. Click **Pick a starting point**, then select **Select an app and trigger event**.
   
7. Set up your data pipeline sync trigger
   
   ### Set up the data pipeline trigger
   
   This trigger monitors the sync status of a pipeline. It fires every time a sync completes.
   
   1. Search for `PipelineOps by Workato` and select it as your app.
      
   2. Select the **Sync completed** real-time trigger.
      
      ![Set up the data pipeline trigger](/assets/set-up-pipeline-trigger.NR6OUdAC.png)_Set up the data pipeline trigger_
      
   3. Choose the **Data pipeline** you plan to monitor.
      
   4. Select **Every sync completion** in the **Trigger on** field .
      
      Workato recommends selecting **Every sync completion** instead of **Failed syncs**. This ensures you capture object-level failures, which may not be tracked under sync-level failures.
      
   
8. Set up your trigger condition
   
   ### Set up a trigger condition
   
   You can set a trigger condition directly in the trigger setup.
   
   1. Enable the **Set trigger condition** toggle.
      
   2. Map the Sync state (Step 1) datapill to the **Trigger data** field.
      
      ![Set up your trigger condition](/assets/set-up-trigger-condition.CaClIN8a.png)_Set up your trigger condition_
      
   3. Set **Condition** to `contains`.
      
   4. Set **Value** to `ERROR`.
      
   
9. Click **\+ Add step**, then select **Action in an app**.
   
   ![Select Gmail](/assets/set-up-pipeline-gmail.CKxyki1v.png)_Select Gmail_
   
10. Search for `Gmail` and select it as your app.
    
11. Set up a Gmail alert
    
    ### Send an email when a pipeline sync fails
    
    This step sends an email from your connected Gmail account when a pipeline sync fails.
    
    1. Select the **Send email** action.
       
    2. Enter one or more recipients in the **To** field. Separate multiple email addresses with commas.
       
       ![Configure your Gmail action](/assets/configure-gmail-pipeline.QER_-8b8.png)_Configure your Gmail action_
       
    3. Enter a subject in the **Subject** field, such as `Pipeline Sync Failure Alert`.
       
    4. Select **Text** or **HTML** in the **Email type** field.
       
    5. Enter the message body in the **Message** field.
