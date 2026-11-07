---
url: 'https://docs.workato.com/en/workbot/workbot-triggers.md'
description: >-
  Learn how Workbot for Slack triggers process commands, events, shortcuts, and
  mentions to start Workato recipes from Slack.
---

# Workbot triggers for Slack

Workbot for Slack allows you to send commands to Workbot on Slack. Workbot will handle these commands and interact with your connected apps to do things, such as display details of a customer account, close opportunities, display a list of invoices or tickets, or create/update existing tickets.

Each Workbot command is processed using a Workato recipe. The recipe trigger picks up the Workbot command as a trigger event, and the recipe determines the actions to carry out. With Workbot, you can create custom workflows that execute through your Slack commands, and optionally retrieve relevant data for you back to Slack.

The Workbot for Slack connector has 5 triggers:

- [New command](#new-command-trigger-building-custom-commands)
- [New help message](#new-help-message-trigger)
- [New event (real-time)](#new-event-trigger)
- [New shortcut trigger](#new-shortcut-trigger)
- [New URL mention](#new-url-mention)
- [New dynamic menu event](#new-dynamic-menu-event)

## New command trigger (building custom commands)

This trigger involves configuring a custom Workbot command. When a recipe with this trigger starts, Workbot monitors for the new command. When it's called, Workbot proceeds to carry out the recipe actions.

### New command trigger input fields

The following table lists the configurable input fields in the trigger, and what each field does.

| New command trigger input field | Description |
| --- | --- |
| App | 1st part of the Workbot command. The app that the Workbot command is working with for example, `Salesforce` |
| Action | 2nd part of the Workbot command. What the Workbot command is doing with the action data, for example, `show`, `create`, `update`. |
| Action data | 3rd part of the Workbot command. The record that the Workbot command works with, for example, `invoice`, `customer`, `ticket`. |
| Command input fields | The input to ask from the user so as to successfully carry out recipe actions, defined in a specific format. Parameters may have the type `file`, which accepts file content (for example, text, binary content) as input. This can be uploaded into Slack. You can use this file in subsequent operations using the Workbot action [Download Attachment.](/en/workbot/workbot-actions.html) |
| Command hint | Short description of what the command does. Shows up in the Workbot app page under **Commands**. |
| Hidden command | If **yes**, command will not show up as a button in the Slack channel when the user types app name. If **no**, command will show up as a button in the Slack channel when the user types app name. |

#### Workbot command format

The Workbot command is created by piecing 3 elements together, the `app`, `action`, and `action data`:

```
app action action-data
```

In the following case, the application is **Salesforce**, the command action is `Show`, and the business data is `Account`. Workbot will respond to the following command:

```
Salesforce show account
```

#### Workbot command input parameters format

The **command input fields** field lets you decide what data is needed from the user to carry out the recipe actions successfully.

Each input parameter has to be provided in the following format:

```
param_name optional:true prompt:false type:string hint:hint_to_help_users sample:example_data
```

| Command input fields | Description |
| --- | --- |
| Name | Required. Needs to be a single word. |
| Optional | Not required. If not defined, defaults to `optional:true`. Input parameter will be optional. |
| Prompt | Not required. If not defined, defaults to `prompt:false`. No prompt will be generated. |
| Data Type | Not required. If not defined, defaults to `type:string`. Possible types are `string`, `boolean`, `number`, `file`, and `date_time`. |
| Hint | Not required. If not defined, defaults to no hint. |
| Example | Not required. If not defined, defaults to no sample data. |

In this case, to successfully retrieve Salesforce account data, we need the full account name from the Slack user.

```
name optional: false prompt: false type: string hint: Exact account name sample: IBM
```

The configured command input fields will be displayed as follow up questions for the user after the Workbot command.

![Salesforce show account input parameters](/assets/salesforce-show-account-input-params-display.CMZM5Ct9.png)_A command input field displayed on Slack_

### New command trigger output datapills

The **New command** trigger also provides a set of datapill variables that holds data about the command, such as the user making the command, the channel the command was made it, and so on. The following table details these datapill variables.

![New command trigger output datatree](/assets/new-bot-command-trigger-datatree.UznLYSLh.png)_New bot command output datatree_

The following table lists the output datapills from the trigger, and what data each field contains.

| New command trigger datapill variables | Description |
| --- | --- |
| App | 1st part of the Workbot command. The app that the Workbot command is working with for example, `Salesforce` |
| Action data | 2nd part of the Workbot command. What the Workbot command is doing with the action data, for example, `show`, `create`, `update`. |
| Action | 3rd part of the Workbot command. The record that the Workbot command works with, for example, `invoice`, `customer`, `ticket`. |
| Message ID | The epoch time when the Workbot command was sent. Can be used to populate **Thread ID** input fields to create a thread under this Workbot command message. Can also be used in **Message to update**, to overwrite a previously posted message. |
| Context | Slack data about this Workbot command, for example, the team and channel it was posted in, the user who posted it, ID of the thread it was in, if applicable. |
| Command input parameters | Data obtained from the user by asking follow up questions to their Workbot command. |

The following table holds additional information about the **Context** object and the data it correspondingly holds.

| Context datapill variables | Description |
| --- | --- |
| Team | Slack team ID |
| User | Slack user ID |
| Reply Channel | Slack channel ID where message was posted |
| User handle | Slack user handle |
| User email | Slack user email |
| User name | Slack user friendly name |
| Thread ID | Thread ID if message was posted to thread, `null` otherwise |

The following table holds additional information about the **Modals** object and the data it correspondingly holds.

| Modal datapills | Description |
| --- | --- |
| View ID | View ID of view from which command was invoked, a.k.a. the active view. If the command was invoked from a view submission, then this view ID cannot be used for updating/pushing views as the view has already closed on submission. If only 1 view is active, then this view ID will be identical to the root view ID. |
| Root View ID | View ID of the root view. |
| Previous View ID | View ID of the view beneath the current view |
| Private metadata | Private data you can optionally use to pass to downstream recipes. This field is encrypted and hidden from users. |
| Hash | A unique value you can optionally use when updating modals. When provided, the hash is validated such that only the most recent view is updated, ensuring the correct view is being updated when updates are happening asynchronously. |

Triggers may contain **Message ID** in their output. Message ID has a value only when **New command** was triggered by a button action. If the command was triggered as a result of a manually typed command, this field will be empty.

### Example: Salesforce show account command

In the following gif, we're chatting directly with Workbot through a DM. When we type in the app name "Salesforce", Workbot generates a list of available commands and displays them as buttons. You can also type the command into the DM manually as `Salesforce show account`.

![Salesforce show account command](/assets/salesforce-show-account-command.IRfs14Tz.gif)_Salesforce show account command_

When the `Salesforce show account` command is called, by clicking the button or typing the command, a corresponding recipe with a Workbot for Slack **New command** trigger starts a job. This recipe has a Workbot **New command** trigger that listens specifically to the command `Salesforce show account`. Reference this [pre-built Workbot for Slack recipe](https://www.workato.com/recipes/57662) with this functionality for usage inspiration and guidance.

![Salesforce show account command recipe](/assets/salesforce-show-account-recipe.B0kCDCFm.png)_Salesforce show account command recipe [Example recipe](https://www.workato.com/recipes/57662)_

The trigger configuration for the `Salesforce show account` command is as follows.

![Salesforce show account command trigger configuration 1](/assets/salesforce-show-account-config-1.CPOKMKQE.png)_Salesforce show account command trigger configuration_

We know that Workbot commands are created by piecing three elements together, the `app`, `action`, and `action data`. In this case, application is "Salesforce", the command action is `Show`, and the business data is `Account`. Workbot responds to the following command: `Salesforce show account`.

The **command input parameters** field lets you decide what data is needed from the user to carry out the recipe actions successfully. In this case, to successfully retrieve Salesforce account data, we need the full account name from the Slack user, so we define the parameter as follows:

![Salesforce show account command trigger configuration 2](/assets/salesforce-show-account-config-2.PmLc187P.png)_Salesforce show account command input field configuration_

The configured command input parameter will be displayed as follow up questions for the user after the Workbot command.

![Salesforce show account input parameters](/assets/salesforce-show-account-input-params-display.CMZM5Ct9.png)_Input parameters display on Slack_

When the user has finished providing all the required input, the recipe actions will be executed. In this case, the recipe action was to display the Salesforce account details as a message attachment in a grid format.

![Salesforce show account command results](/assets/salesforce-show-account-results.D0PTpvqQ.png)_Salesforce show account command results_

## New help message trigger

The **New help message** trigger executes when a `help` message is sent to your bot through a direct message (DM) or channel (when mentioned by the user, for example `\@workbot help`). Use this trigger if you want to fully customize your bot's `help` message response rather than use the Workbot default help message.

> **WHO CAN USE THIS TRIGGER?**
> 
> You can use the **New help message** trigger if you have an [Enterprise Workbot](/en/workbot/workbot-custom-bots#create-a-slack-enterprise-workbot). You cannot use this trigger if you have a built-in Workbot.

We recommend that you use this trigger with the [Post command reply](/en/workbot/workbot-command-reply) so that users will see the new `help` message when using the `help` command.

Only one **New help message** trigger recipe can be active at a time for each bot.

> **WARNING**
> 
> This trigger overrides both the default `help` message and the custom help JSON in the bot connection.

### Reasons to use New help message trigger

We highly recommended that you customize your bot's help message based on its unique functionality. You can do this by responding to a **New help message** event with a **Post command reply**. The context contained within the trigger can be used to:

- Personalize the message to the user by using **User ID**
- Show different `help` messages if the user is the bot admin or an end-user by using **Is bot admin?**
- Provide alternative `help` messages using text that the user submits along with their `help` command, for example `help Salesforce`
- Display bot commands, personal connections, and links to bot recipes and jobs

With the customized help message now defined within a Post command reply action, you can:

- Describe your bot's unique functionality in greater detail
- Include information from other apps (for example: Salesforce, ServiceNow, Jira) that can be scoped to the user
- Build multi-step `help` flows that can open modals or bring users to your bot app home

### Inputs

No inputs required.

### Outputs

| Field | Description | Example |
| --- | --- | --- |
| Help message text | Text supplied by the user that comes after \`help\`. | "@workbot help me with salesforce" ==> "me with salesforce" |
| Message ID | Message ID of the help message | 1490915654.038365 |
| Personal connections command | Command that can be used to display the user's personal connections. Use when defining the command to invoke in buttons or other interactive component. | connections |
| Bot info command |  | uname |
| Is bot admin? | True if invoking user is a bot admin, false otherwise. | true |
| Bot commands (array) | Recipe ID | Recipe ID of bot command recipe. | 42 |
| Recipe name | Name of the bot command recipe. | Create Salesforce opportunity |
| Command | Full command name | salesforce create opportunity |
| Description | Command hint | creates salesforce opportunity |
| Recipe URL | URL of recipe. | https://app.workato.com/recipes/42 |
| Recipe jobs URL | URL of recipe jobs page. | https://app.workato.com/recipes/42#jobs |
| Context | Slack-related information like team info, user info, message or modal/app home view info. | See the [Context datapill variables table](/en/workbot/workbot-triggers.html#new-command-trigger-output-datapills) |

### Help message priority

Help messages use the following priority:

1. Custom help in recipe
2. Custom help JSON in connection level
3. Default help

## New event trigger

The **New event** trigger executes when the specified event occurs in your Slack workspace. The trigger works with Slack's [Events API](https://api.slack.com/events-api) and [interactive components](https://api.slack.com/messaging/interactivity#components) (like block actions and modal submissions). Each trigger subscribes to one type of event.

> **EVENTS API TRIGGERS**
> 
> Your bot must be subscribed in Slack to any events in the Events API you plan to trigger from.

![New event trigger](/assets/new-event-trigger.jYJRkNBh.png)_Workbot for Slack new event trigger_

By default, this trigger contains a list of the most frequently subscribed events. If the event you're looking for is not on the list, you can switch to **Enter custom value** to manually configure the event.

![Custom event](/assets/custom-event.Cuya-ehN.png)_Event name points the event to the recipe and is useful in providing context — otherwise, no syntax is enforced_

You may also choose to generate the event payload by specifying a sample JSON by clicking on **Use a sample JSON** under **Event schema**.

![Event sample JSON](/assets/event-sample-json.C5vpHKl3.png)_Sample JSON event_

![Custom event JSON](/assets/custom-event.Cuya-ehN.png)_Custom JSON event_

Refer to the list of events you can subscribe to over at Slack's [API Event Types documentation](https://api.slack.com/events).

Use this trigger with [Enterprise bots](/en/workbot/workbot-custom-bots), as it allows you to specify which bot or workspace events your bot subscribes to. To subscribe to events, [head over to your bot in Slack](https://api.slack.com/apps) and navigate to **Event Subscriptions**. Subscribe to the events you need, then hit **Save Changes**.

![Event subscription](/assets/event-subscription.DIy7uvEL.png)_Event Subscriptions in Slack_

## New shortcut trigger

The **New shortcut** trigger is a powerful way to kickstart your workflows. Launch a workflow from a global shortcut, or turn any Slack message into a task or a ticket using a message shortcut. This trigger works for both **Global** & **Message** shortcuts requires you to [create shortcuts in your Enterprise bot](/en/workbot/workbot-shortcuts#creating-shortcuts-on-your-enterprise-bot-in-slack).

![Shortcuts example](/assets/shortcuts-example.tD4OGn9u.jpg)_Workbot Shortcuts example_

Watch Workbot Shortcuts in Action!

[Video](https://www.youtube.com/embed/OHu1uNxOAq8?rel=0&rel=0)

When triggered, shortcuts launch a dialog to collect command input fields from the user. The original contents of the message (along with input obtained from the dialog) can be used to create tasks, tickets, and more. To start using shortcuts, check out our [shortcuts documentation](/en/workbot/workbot-shortcuts).

If required, launch a dialog box to collection more information from the user.

![Shortcuts trigger](/assets/shortcut-trigger.Cmdosq4L.png)_New shortcut trigger_

To start using shortcuts, check out our [Shortcuts documentation](/en/workbot/workbot-shortcuts).

## New URL mention

This trigger monitors certain types of URLs in Slack and pulls pre-defined, formatted data into the channel when such an URL is mentioned. Currently, Salesforce and GitHub URLs are supported.

When you send a URL in Slack, you can have Workbot provide certain information into the channel for everyone to see. For example, you can send a Salesforce lead URL into your sales channel and Workbot will automatically send a message showing more information about that particular lead.

![workbot triggers](/assets/workbot-url.DN020Wlg.gif)_Workbot URL mention_

Select the application in the trigger (Currently only Salesforce and GitHub), and select the Document, and set up your actions as you prefer. By default, providing a Salesforce or GitHub URL in a channel that Workbot is in triggers a prompt from Workbot. This prompt asks if you plan to display details of the content of the URL that you have sent. Select **yes** to trigger the recipe. You can also edit the recipe in Workato if you plan to have more or fewer fields included in the message.

![workbot triggers](/assets/workbot-url-mention.BkoWKhBs.gif)_Workbot URL details_

## New dynamic menu event

In Workbot command recipes that invoke dialogs, a `select` field can be defined with dynamic menu options.

![Dynamic menu](/assets/dynamic-menu.BgqZkC0A.png)_A Workbot command recipe with dynamic menu options_

This trigger executes when a user types in such a field and returns what the user typed (for example, the `typeahead` value). You must type at least five characters to trigger an event.

Use this `typeahead` value to retrieve a list of records (from another app such as Salesforce) to return to the main recipe (for example, the recipe that posts the dialog where the `select` field is).

![Typeahead example](/assets/typeahead-example.CeArrArm.png)_`Typehead` example_

You can return the list of records to the dynamic menu by using the [Return menu options](/en/workbot/workbot-actions#return-menu-options) action. This trigger should be paired with a **Return menu options** action.

### Input

#### Dynamic menu name

Identifier for this menu.

#### Command input fields

A Workbot command recipe with dynamic menu options can pass parameters to a Dynamic menu recipe through the **Dynamic menu recipe params** field. The dynamic menu recipe can use these additional parameters in generating menu options.

![Dynamic menu recipe params](/assets/dynamic-menu-recipe-params.D4BLkgmW.png)_A Workbot command recipe with a dynamic menu options field passing a 'stagename' parameter with value 'Closed Won'_

Correspondingly, the trigger must also have the same parameter defined.

![Params in dynamic menu trigger](/assets/params-in-dynamic-menu-trigger.jwb5Y2fn.png)_The corresponding dynamic menu recipe with the same 'stagename' parameter defined_

The dynamic menu recipe is then able to utilize the additional parameters in generating menu options. In the example below, the parameter `stagename` is passed to the dynamic menu recipe, allowing the SOQL search to be further refined.

![Dynamic menu param example](/assets/dynamic-menu-param-example.DUIRPpRq.png)_'stagename' parameter is passed to refine the SOQL search_

### Output

| Fields | Description |
| --- | --- |
| Event context | Team | Team ID and domain where command was invoked. |
| User | User ID and name of user who invoked command |
| Channel | Channel ID and name where command was invoked. |
| State | System message containing dynamic menu recipe ID and parameter name-value pair. |
| Action ts | Timestamp of when action was invoked. |
| Typeahead | Name | Name of parameter where dynamic menu event was received from. |
| Value | Characters typed by user in the dynamic menu options field. |
| Callback ID | System message |
| Parameters | Name-value pairs passed by a Workbot command recipe with dynamic menu options. |

## FAQs

What is Workbot for Slack, and what are its primary functions?

Workbot for Slack is a tool that lets you send commands to Workbot within Slack. Workbot then interacts with connected apps to perform various tasks, such as:

- Retrieve customer account details
- Close opportunities
- Create and update tickets

How are Workbot commands processed, and what role does a Workato recipe play?

Each Workbot command is processed using a Workato recipe. The recipe's trigger picks up the Workbot command as an event, and the recipe determines the actions to be carried out in response to the command. This allows you to create custom workflows executed through Slack commands.

What are the available triggers in the Workbot for Slack connector?

The Workbot for Slack connector provides five triggers:

- New command
- New help message
- New event (real-time)
- New shortcut trigger
- New URL mention

These triggers enable various interactions and automated workflows within Slack.

How does the New command trigger work, and what input fields can be configured for it?

The **New command** trigger is used to configure custom Workbot commands. It monitors Slack for the specified command and executes recipe actions when the command is called. You can configure input fields, such as:

- App
- Action
- Action data
- Command input fields
- Command hint

What is the format for creating a Workbot command, and how are input parameters defined?

Workbot commands are created by combining three elements:

- App
- Action
- Action data

Input parameters for commands are defined using a specific format that includes fields, such as:

- Name
- Prompt
- Data type
- Hint
- Example

What output datapills are available from the New command trigger, and what information do they provide?

The **New command** trigger generates output datapills, including information about the command, such as:

- App
- Action data
- Action
- Message ID
- Context

The output datapills created for the **New command** can be used in subsequent recipe actions.

How can I customize the help message for Workbot in Slack using the New help message trigger?

The **New help message** trigger allows you to fully customize Workbot's help message response when users request help. You can:

- Personalize messages
- Display different help messages based on user roles
- Provide alternative help messages

What events can be subscribed to using the New event trigger, and can it work with Slack's Events API?

The **New event** trigger executes when a specified event occurs in a Slack workspace. Users can subscribe to various events and configure how the trigger responds to a specific event. This trigger works with Slack's Events API and allows for event customization.

How does the New shortcut trigger work, and what are its applications?

The **New shortcut** trigger lets you launch workflows from global shortcuts or convert Slack messages into tasks or tickets using message shortcuts. It collects input fields from users and then creates tasks or tickets based on the user input.

What is the purpose of the New URL mention trigger, and which types of URLs are supported?

The **New URL mention** trigger monitors certain types of URLs in Slack and retrieves pre-defined, formatted data when those URLs are mentioned. Currently, this trigger supports Salesforce and GitHub URLs and can be used to display additional information based on the mentioned URL.

How does the New dynamic menu event trigger work, and what are its applications?

The **New dynamic menu event** trigger is used in Workbot command recipes with dynamic menu options. This trigger executes when a user enters information into a dynamic menu field, and then returns the user's input. This trigger is often used to refine search results or perform actions based on user input.

---
