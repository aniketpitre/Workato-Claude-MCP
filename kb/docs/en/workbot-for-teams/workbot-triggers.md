---
url: 'https://docs.workato.com/en/workbot-for-teams/workbot-triggers.md'
description: >-
  Reference for Workbot triggers in Microsoft Teams, including new command, help
  message, tab opened, and new message triggers for recipes.
---

# Workbot for Microsoft Teams triggers

Workbot for Microsoft Teams has the following triggers:

- [New command trigger](#workbot-command-trigger)
- [New help message trigger](#new-help-message-trigger)
- [Tab opened trigger](#tab-opened-trigger)
- [New message trigger](#new-message-trigger) (beta)

## New command trigger

Workbot commands allow you to trigger recipes from Microsoft Teams. These recipes can then perform actions in your apps (for example, creating new ServiceNow tickets, or listing Salesforce opportunities).

This means you can from perform actions in your apps from within Microsoft Teams.

![Command example](/assets/workbot-command-example.DR5KdNkL.png)_Sending a 'newissue' command with additional parameters in Teams, then receiving a reply_

When a command is sent to Workbot in Microsoft Teams, it will trigger the Workbot recipe and execute its actions.

![Command recipe](/assets/command-recipes.r9E_LXdi.png)_A Workbot recipe with a Workbot command trigger_

### Configuring the command

![New command](/assets/new-command.BK0S3wms.png)_Example 'newissue' command_

### Input

The table below lists the input fields in the trigger and what they do.

| Input field | Description |
| --- | --- |
| [Command name](#command-name) | Name of the command. |
| [Parameters](#parameters) | Parameter can store additional data that can be used as datapills in follow-up recipe actions. |
| Command hint | Display this instead of command name in response to **help** messages. |
| Hidden command | If **Yes**, command will not show up as a command in **help** messages. Defaults to **No**. |

#### Command name

Workbot commands can invoke their recipes by:

1. Sending the command name in a direct message to Workbot, for example, **newissue**
2. Sending the command name in a channel and tagging Workbot, for example, **@workbot newissue**
3. Submitting a button with the command name configured: ![Command name in button](/assets/button-command.BEaEEKM8.png)_A button can be configured to invoke a Workbot command of another recipe_

![Command name in button example](/assets/button-submission.BDqVoJlT.png)_The 'Create issue' button invokes the 'newissue' command and executes the recipe when submitted_

#### Parameters

Each parameter can store additional data that can be used as datapills in follow-up recipe actions.

For example, to create an incident in ServiceNow, you may want to prompt users for additional info like **Urgency**, **Summary**, and **Description**. By adding **Urgency**, **Summary**, and **Description** as parameters, Workbot will open a task module and prompt the user for each parameter.

![Task module](/assets/task-module-snow.BKLnEezm.png)_Workbot can ask users for info if you specify additional parameters in your command_

Users can also skip the prompts by supplying the parameters together with the command.

![Command with in-line parameters](/assets/workbot-command-example.DR5KdNkL.png)_Sending a 'newissue' command with additional parameters Urgency, Summary, and Description_

##### Defining parameters

![Parameters configured](/assets/parameters-configured.fquG1W4U.png)_3 parameters configured for the 'newissue' command_

When you define parameters, Workbot opens a task module to collect each parameter's value from the user.

To add a parameter, select the **+Add parameter** button under the **Parameters** section of a Workbot command trigger.

![Adding a parameter](/assets/adding-a-parameter.Cbrsxeqi.png)_Adding a new parameter_

By configuring the parameter, you can control how the users interact with the parameter in the task module.

![Parameter form empty](/assets/parameter-form-filled.ChUdd1dh.png)_Configuring a parameter_

The table below describes in further detail what each parameter configuration field does.

| Input field | Description |
| --- | --- |
| Name | Name of the parameter. This is the name you use to reference the parameter in: In-line commands ![](/assets/workbot-command-example.DR5KdNkL.png), Choice parameters ![](/assets/choice-param-recipe.COZvsFYT.png), Additional parameters in buttons ![](/assets/button-command.BEaEEKM8.png)  |
| Data type | Data type of the parameter. Currently supports the following data types: `string`, `date`, `file` The data type will influence the input type presented to the user in a task modules. For example, if `Date` is chosen, a date picker will be presented to the user. The `file` parameter is only available for Enterprise Workbot. [Learn more](/en/workbot-for-teams/files-for-bots.html). |
| Optional? | If set to **Yes**, users can skip this input. If set to **No**, users are required to provide this input. |
| Hint | Hints are displayed just below the input field for users when filling in the input field. |
| Example input value | Displays a placeholder for the field in the task module. Useful in giving the user a sense of what the requested input should look like, as well as the desired format. |
| Visible? | If **Yes**, command will not show up in task modules. Useful if the parameter is a record ID that is not human-readable. Defaults to **No**. |
| Options | Comma-separated list of options, for example, **APPROVED, REJECTED, EXPIRED**. If the display name and the value are different, separate the two by a colon, for example, **High:1,Medium:2,Low:3**. |

##### Advanced methods to pass parameter values

Parameter values can also be passed by buttons and task modules as they invoke a Workbot command. Typically, you use parameters to pass context to the invoked Workbot recipe.

![Button with params example](/assets/button-with-params.8r1JP7aF.png)_The 'Re-open issue' button not only invokes the 'reopen\_issue' command - it's also passing parameters!_

![Button with params recipe](/assets/button-with-params-recipe.CxVqWkjs.png)_The 'Re-open issue' button is configured to pass the 'sys\_id' so that the 'reopen\_issue' recipe knows which issue to re-open_

Another way to pass a parameter is by using a pick list **Choice parameter**.

![Choice param recipe](/assets/choice-param-recipe.COZvsFYT.png)_The choice parameter will take its value from a choice (if it's chosen)_

The choice parameter is passed when a button from the same message is submitted (along with any other parameters the button may have).

![Choice param](/assets/choice-param.Dx4F0jO4.png)_The 'Next' button also passes the 'opportunity\_id' of 'Google' onto the command recipe that it invokes_

##### Files for Enterprise Workbot

End users can [upload files](/en/workbot-for-teams/files-for-bots) to [Enterprise Workbots](/en/workbot-for-teams/guides/creating-enterprise-workbot) when `file` parameters are defined in the bot commands. These files are uploaded to the user's **OneDrive for Business** storage, and its data can then be used in follow-up recipe actions. The file portion of the trigger output looks like this:

| Output fields | Description | Example |
| --- | --- | --- |
| contentType | Indicates that a file was uploaded to OneDrive and ready for download. | application/vnd.microsoft.teams.file.download.info |
| downloadUrl | OneDrive URL for fetching the content of the file. You can issue an HTTP GET directly from this URL. | [https://download.link](https://download.link) |
| uniqueId | Unique file ID. This will be the OneDrive drive item ID. | 1150D938-8870-4044-9F2C-5BBDEBA70C9D |
| contentUrl | Link to the file in Sharepoint. | [https://contoso.sharepoint.com/personal/johnadams\_contoso\_com/Documents/Applications/file\_example.txt](https://contoso.sharepoint.com/personal/johnadams_contoso_com/Documents/Applications/file_example.txt) |
| name | Name of the file | file\_example.txt |
| file\_comment | The message sent by the user along with the file upload. | This is an example file upload. |

> **Updating Workbots created before 30th Oct 2021**
> 
> Enterprise Workbots created before 30th Oct 2021 typically would not have `supportsFiles` property set to `true` in their manifest. [Learn how to update it](/en/workbot-for-teams/files-for-bots#enabling-files-for-older-bots).

## New help message trigger

The **New help message** trigger executes when a `help` message is sent to your bot via DM or channel (when mentioned by the user, e.g. "@workbot help"). Use this trigger if you want to fully customize your bot's `help` message response, instead of utilizing the Workbot default help message.

It is recommended to pair this trigger with the [Post reply](/en/workbot-for-teams/workbot-actions#post-reply-and-post-simple-reply) action. The reply will then become the `help` message users will see when invoking `help` for your bot.

Only 1 New help message trigger recipe can be active at a time for each bot.

### Reasons to use New help message trigger

It is highly recommended to customize your bot's help message based on its unique functionality. This is done by responding to a **New help message** event with a **Post reply**. The context contained within the trigger can be used to:

- Personalize the message to the user by using **User ID**
- Show different `help` messages if the user is the bot admin or an end-user by using **Is bot admin?**
- Provide alternative `help` messages using text that the user submits along with their `help` command, e.g. `help Salesforce`
- Display bot commands, personal connections, and links to bot recipes and jobs

With the customized help message now defined within a Post reply action, you are now able to:

- Describe your bot's unique functionality in greater detail
- Include information from other apps (e.g. Salesforce, ServiceNow, Jira) that can be scoped to the user
- Build multi-step `help` flows that can open task modules or bring users to specific tabs

### Inputs

No inputs required.

### Outputs

| Field | Description | Example |
| --- | --- | --- |
| Help message text | Text supplied by the user that comes after \`help\`. | "@workbot help me with salesforce" ==> "me with salesforce" |
| Personalized connections command | Command that can be used to display the user's personal connections. Use when defining the command to invoke in buttons or other interactive component. | connections |
| Is bot admin? | True if invoking user is a bot admin, false otherwise. | true |
| Bot commands (array) | Recipe ID | Recipe ID of bot command recipe. | 42 |
| Recipe name | Name of the bot command recipe. | Create Salesforce opportunity |
| Command | Full command name | salesforce create opportunity |
| Description | Command hint | creates salesforce opportunity |
| Recipe URL | URL of recipe. | https://app.workato.com/recipes/42 |
| Recipe jobs URL | URL of recipe jobs page. | https://app.workato.com/recipes/42#jobs |
| Context | Microsoft Teams-related information, including message information, tenant/channel/team information, user information, and more. |
| Advanced | Parameter name for commands in choice sets | Use this pill in the **Parameter** field if a **Bot commands** array is used in a choice set. |
| Submit command for commands in choice sets | Use this pill in the **Submit button command** field if a **Bot commands** array is used in a choice set. |

#### Help message priority

Help messages follow the following priority:

1. Custom help in recipe
2. Default help

## Tab opened trigger

This trigger executes when a user opens a tab in your enterprise Workbot. To learn more about how tabs work, see [Tabs](/en/workbot-for-teams/guides/tabs).

### Input

| Input field | Description | Example |
| --- | --- | --- |
| Entity ID | Entity ID of the tab. Can be found in your app's `manifest.json` file. To learn more, see [Tabs](/en/workbot-for-teams/guides/tabs). Must be 1 word. Case sensitive, and must be identical to tab's entityId in manifest. | PendingPTORequests |

### Output

| Output field | Description | Example |
| --- | --- | --- |
| Entity ID | Entity ID of the tab. | PendingPTORequests |
| Context | Microsoft Teams-related information, including message information, tenant/channel/team information, user information, and more. |

## New message trigger

![New message trigger](/assets/new-message-trigger.8EzBVmIw.png)_New message trigger_

The **New message** trigger activates when a user sends a direct message (DM) to Workbot or mentions Workbot in a channel, provided there are no active [new command triggers](/en/workbot-for-teams/workbot-triggers#workbot-command-trigger) that match the user's message. If no specific command triggers are set up to respond to that message, the New message trigger runs.

For example, if you send `@workbot hello` to Workbot and have no active recipes configured with the `hello` command, the **New message** trigger picks up the event and proceeds with the workflow defined in your recipe. This trigger takes precedence over the default `Command not found` response.

This trigger is compatible with [Post message](/en/workbot-for-teams/workbot-actions#post-message-and-post-simple-message) and [Post simple message](/en/workbot-for-teams/workbot-actions#post-message-and-post-simple-message) actions. Use it to customize your Workbot’s response to a new message. You can have multiple recipes with the **New message** trigger active at the same time. Additionally, you can use trigger conditions to filter for a specific channel.

> **PUBLIC BETA**
> 
> This trigger is in public beta. Public beta features are those that have passed the development phase and are now ready for customer use. Our goal is to gather your input to ensure their reliable release in upcoming enhancements.
> 
> During the public beta release, Workato may update its functionality or change its availability to customers without prior notice.

### Input

This trigger does not require user input. However, you can set a [trigger condition](/en/recipes/triggers#trigger-conditions) to configure Workbot to respond to messages in one or more specific channels only.

### Output

| Field | Description |
| --- | --- |
| Message ID | The ID of the user-supplied message. |
| Message Text | The message content. This is the message the user sends to Workbot. |
| Timestamp | The time the initial message was sent to Workbot. |
| Conversation ID | The unique ID of the conversation. This is typically the channel ID and associated metadata. |
| Conversation Type | The type of message between the user and Workbot. For example, `channel` or `groupchat`. |
| Sent From ID | The ID of the user who sent the message to Workbot. |
| Sent From Name | The name of the user who sent the message to Workbot. |
| User ID | The user ID of the user who sent the message to Workbot. |
| Recipient ID | The ID of the Workbot that received the message. If your workspace has multiple Workbots, this value helps differentiate between them. |
| Recipient Name | The name of the Workbot that received the message. If your workspace has multiple Workbots, this value helps you differentiate between them. |

### How it works

This trigger is useful in situations where your users interact with Workbot, but their input does not match any existing commands. It enables you to create more interactive and dynamic conversations between Workbot and your users.

The following example pairs the **New message** trigger with a **Post message** action. This action allows users to complete their tasks by selecting an option, such as filing a ticket, searching for records, or talking to support.

**Configuration in Workato**

1. Add the **New message** trigger to your recipe.
   
2. _Optional._ Select **Set trigger condition** to control which specific channels Workbot responds to new messages in. This allows Workbot to respond to messages posted to a specific channel. For example, you can configure Workbot to only respond to messages in the `IT requests` channel.
   
   To configure a trigger condition:
   
   1. Map the Conversation ID (Step 1) datapill into the **Trigger data** field.
      
   2. Select **contains** in the **Condition** field.
      
   3. Enter the channel ID into the **Value** field. Learn how to [obtain a channel ID](#channel-id) from Microsoft Teams.
      
      ![Configure an IF condition](/assets/trigger-condition.C-nHqd4w.png)_Configure an IF condition to control where Workbot can post messages_
      
3. Click **`+`** (plus) to add a **Post message** action to your recipe.
   
4. Select a **Message recipient**. Choose **Select from list** to send messages to a specific channel, or **Enter custom value** to send messages to a specific user.
   
   ![Select a message recipient](/assets/message-recipient.SUx1CvWs.png)_Select a message recipient_
   
5. Draft your message. For example, you can create a message that allows users to supply further information to Workbot, enabling it to help them complete their tasks.
   
   This example adds an action on button block which allows users to select from the following options:
   
   - **File a ticket**: Runs a command supported by a different recipe.
   - **Search for records**: Opens a URL.
   - **Talk to support**: Continues the recipe which includes logic for notifying support staff.

**Flow in Teams**

![Action on button block](/assets/text-with-button-teams.f8oK_4TK.png)_Workbot responds to user prompts_

#### How to obtain a channel ID

A channel ID corresponds to a specific channel in Microsoft Teams. You can use the channel ID to configure trigger conditions that filter events by channel and control which channels prompt a response from Workbot. This ensures Workbot's actions are relevant to the context of those channels.

Complete the following steps to obtain a channel ID from Microsoft Teams.

1. Go to the channel where you plan for Workbot to monitor messages.
   
2. Click the **...** (ellipsis) on the right of the channel name.
   
3. Click **Get link to channel**.
   
4. Copy the channel ID from the modal. The modal displays the entire link to the channel. The channel ID is included in this link as a path parameter following the `channel` path segment.
   
   ![Copy the channel ID](/assets/channel-id.BXMuW23J.png)_Copy the channel ID_
   
   In the following example, everything between `channel/` and `/%5BDocs` is the channel ID.
   
   ```html
   https://teams.microsoft.com/l/channel/19%3Aae37e692418942c28c2c97cd38493cf5%40thread.tacv2/%5BDocs%5D%20Test?groupId=55563081-256e-4922-8f4e-e2a760294320&tenantId=76a89289-583c-40a2-9709-e076eed5d680
   ```
   
5. Decode the channel ID. You can use a tool such as [Dupli Checker](https://www.duplichecker.com/online-url-encoder-decoder.php) or a similar tool for this purpose.
   
   For example, the following string should change from this:
   
   ```
   19%3Aae37e692418942c28c2c97cd38493cf5%40thread.tacv2
   ```
   
   To this:
   
   ```
   19:ae37e692418942c28c2c97cd38493cf5@thread.tacv2
   ```
   
6. Split the resulting string to remove the metadata from the channel ID. The metadata include the `@` symbol and everything after it.
   
   For example, the string:
   
   ```
   19:ae37e692418942c28c2c97cd38493cf5@thread.tacv2
   ```
   
   Should be split to:
   
   ```
   19:ae37e692418942c28c2c97cd38493cf5
   ```
   
   The result is the channel ID you can use to configure the trigger condition.
   

> **FURTHER READING**
> 
> - [Using Workbot for Microsoft Teams](/en/workbot-for-teams/using-workbot-for-teams)
> - [Workbot actions](/en/workbot-for-teams/workbot-actions)
> - [Workbot buttons, pick lists, and task modules](/en/workbot-for-teams/buttons-choices-task-modules)

---
