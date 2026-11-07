---
url: 'https://docs.workato.com/en/workbot/configuring-slash-commands.md'
description: >-
  Learn how to configure and use slash commands with Workbot for Slack to
  trigger Workato recipes, including step-by-step setup with Jira as an example.
---

# Slash commands

You can configure slash commands to trigger the Workbot for Slack **New command** trigger.

![Slash command in Slack](/assets/slash-command-in-slack-1.C6CUMxHw.png)

You can configure slash commands using the following methods:

- By connecting an [Enterprise Workbot](/en/workbot/workbot-custom-bots) (recommended)
- By using a [legacy custom integration](/en/workbot/legacy-slash-commands)

We strongly recommend using Enterprise Workbots to configure your slash command, as custom integration is a legacy feature that may be deprecated in the future.

## Prerequisites

To use slash commands, you must have the following:

- Access to custom OAuth profiles in Workato.
  
- An [Enterprise Workbot](/en/workbot/workbot-custom-bots) in Workato that's set up with [Slack Enterprise Grid](/en/workbot/guides/setup-workbot-for-slack-enterprise-grid).
  
- Org-readiness enabled on your Slack app profile. The bot can't integrate with Slack Enterprise Grid without this setting.
  
  ![Enable org-readiness](/assets/enable-org-readiness.RKMuNf7L.png)_Enable org-readiness_
  

## Example: Create a Jira issue slash command

This example demonstrates how to configure a slash command that lets you create new Jira issues from within Slack.

1. [Define the slash command in Workato](#define-the-slash-command-in-workato)
2. [Create the slash command in Slack](#creating-the-slash-command-on-slack)
3. [Complete your recipe](#complete-your-recipe)
4. [Test your recipe](#test-your-recipe)

### Define the slash command in Workato

Complete the following steps to define the slash command in Workato:

1. Create a new recipe using **Build a Slack bot command** as your starting point. This adds the Workbot for Slack [New command](/en/workbot/workbot-triggers#new-command-trigger-building-custom-commands) trigger and [Post command reply](/en/workbot/workbot-actions#post-command-reply) action to your recipe.
   
   ![Build a new Slack bot command](/assets/build-slack-bot-command.C1P-5HjR.png)_Build a new Slack bot command_
   
2. Select the trigger.
   
3. Select **Jira** from the **App** drop-down menu.
   
4. Select **Create** as the action for the command to perform from the **Action** drop-down menu.
   
5. Select **Issue** as the data the command works with from the **Action data** drop-down menu.
   
6. In the **Parameters** field, click **Add command input**. This field lets you define the parameters you expect to receive from an upstream bot command, such as the Jira project key and issue type.
   
7. Create the following parameters:
   
   - `project_issue_type`
     
     - **Label**: Project issue type
     - **Data type**: String
     - **Optional?**: No
     - **Hint**: Enter the project key and issue type separated by two hyphens
     - **Example input value**: IM--Task
   - `summary`
     
     - **Label**: Summary
     - **Data type**: String
     - **Optional?**: No
     - **Hint**: Enter the summary for the Jira issue
   - `description`
     
     - **Label**: Description
     - **Data type**: String
     - **Optional?**: Yes
     - **Hint**: Enter the description for the Jira issue
   
   Example schema
   
   ```json
   [
     {
       "control_type": "text",
       "label": "Project issue type",
       "name": "project_issue_type",
       "type": "string",
       "optional": false,
       "hint": "Enter project key and issue type separated by two hyphens",
       "sample": "IM--Task"
     },
     {
       "control_type": "text",
       "label": "Summary",
       "name": "summary",
       "type": "string",
       "optional": false,
       "hint": "Enter the summary for the Jira issue"
     },
     {
       "control_type": "text",
       "label": "Description",
       "name": "description",
       "type": "string",
       "optional": true,
       "hint": "Enter the description for the Jira issue"
     }
   ]
   ```
   
8. Expand the **Slash command** section and set **Enable Slash Command** to **Yes**.
   
9. Enter `/createissue` in the **Command name** field. This name is used to invoke the slash command. The command name must begin with a `/` and contain no spaces.
   
10. Scroll to the top of the trigger configuration and copy the **URL**. Workato generates this request URL after you enable the slash command and enter a valid command name.
    
    ![Request URL](/assets/request-url.Ch7gFmMs.png)_Copy the request URL_
    
11. Optional. Fill in the **Auto-reply message** field. For example, you can enter `Command received, working...` in this field.
    
    When the command is invoked, Workbot for Slack automatically sends this reply to the user only. If left empty, Workbot for Slack's reply mirrors the user's command to confirm receipt. You can't use datapills in this field.
    
12. Optional. Select **Yes** in the **Dialog for missing parameters** field. This lets users enter missing parameters in a dialog.
    
    ![Dialog for missing command input fields](/assets/dialog-for-missing-command-input-fields-1.BeadhBdb.png)
    
    If you select **No**, Workbot collects these values in a conversation.
    
    ![Dialog for missing command input fields](/assets/dialog-for-missing-command-input-fields-no.YO5q8cKi.png)
    
13. Optional. Enter `Create new issue in Jira` in the **Dialog title** field.
    
14. Click **Save**.
    

### Create the slash command in Slack

Complete the following steps to create the slash command in Slack:

1. Go to the [Slack API website](https://api.slack.com) and select **Your apps**.
   
2. Select the app that corresponds to your Enterprise Workbot.
   
   ![Custom bot](/assets/custom-bot.Cy01ia68.png)_Select your Enterprise bot_
   
3. Click **Slash Commands**.
   
4. Click **Create New Command**.
   
   ![Create new command](/assets/create-new-slash-command-slack.Bm62KfZf.png)_Select **Create New Command**_
   
5. Enter `/createissue` in the **Command** field.
   
   ![Mapping command name](/assets/map-command-name.B2Iz6YTf.png)
   
6. Paste the [URL](#define-the-slash-command-in-workato) from Workato in the **Request URL** field.
   
   ![Mapping request URL](/assets/map-request-url.DbXc5k43.png)
   
7. Enter a description in the **Short description** field. For example, `Creates a new issue in Jira`.
   
8. Optional. Enter the parameters that can be passed in the slash command in the **Usage hint** field.
   
9. Select the **Escape channels, users, and links sent to your app** checkbox. This instructs Slack to escape users and channels in their request payload to Workato.
   
10. Click **Save**.
    

### Complete your recipe

Complete the following steps to add actions that create the issue in Jira and post a message with details about the Jira issue:

1. Return to your recipe in Workato and click **Select an app and action**.
   
2. Search for and select `Jira` as your app.
   
3. Select the **Create issue** action.
   
4. Select your [Jira connection](/en/connectors/jira#how-to-connect-to-jira-on-workato).
   
5. Switch the **Project issue type** field to **Enter project and issue type** and map the Workbot for Slack Project issue type (Step 1) datapill.
   
6. Map the Workbot for Slack Summary (Step 1) datapill to the **Summary** field.
   
7. Map the Workbot for Slack Description (Step 1) datapill to the **Description** field.
   
   ![Configure the Create issue action](/assets/create-issue-config.h2KOZJe4.png)_Configure the Create issue action_
   
8. Click **\+ Add step** and select **Action in app**.
   
9. Search for and select `Jira` as your app.
   
10. Select the **Get issue** action.
    
11. Map the Jira ID (Step 2) datapill to the **Issue ID or key** field.
    
12. Select the Workbot for Slack **Post command reply** action.
    
13. [Configure the reply](/en/workbot/workbot-actions#post-command-reply) to include details about the newly created Jira issue.
    
14. Click **Save**.
    

### Test your recipe

Complete the following steps to test your recipe:

1. Click **Test recipe**.
   
2. Open Slack and select a channel where your Enterprise Workbot is added.
   
3. Enter `/createissue` and press Return to send the command and open the **Create new issue in Jira** dialog.
   
   ![Dialog for missing command input fields](/assets/dialog-for-missing-command-input-fields-1.BeadhBdb.png)
   
   > **INLINE PARAMETER INPUT**
   > 
   > You can also pass parameters directly in the slash command.
   > 
   > Command input parameters follow this format:
   > 
   > ```plaintext
   > /slashcommand name1: value 1 name2: value 2 name3: value 3...
   > ```
   > 
   > Here, `name` is the parameter name and `value` is the parameter's value.
   > 
   > For example:
   > 
   > ```plaintext
   > /createissue project_issue_type: UI--Bug summary: Button is misaligned description: At the registration page, the registration button is misaligned.
   > ```
   
4. Fill out the fields and click **Submit**.
   

If you configured the [Post command reply](/en/workbot/workbot-actions#post-command-reply) action, Workbot sends a confirmation reply with details about the newly created Jira issue.

You can add more slash commands to the same Enterprise Workbot. Slash commands aren't namespaced, so be sure to give each command a unique name.

## Troubleshooting

If you encounter a `dispatch_failed` error, your Workbot might be misconfigured. If your Enterprise Workbot has Slack Enterprise Grid functionality, you must install the bot at the organizational level rather than within a single Slack workspace.

---
