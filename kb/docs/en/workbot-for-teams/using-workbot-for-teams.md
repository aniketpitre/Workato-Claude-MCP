---
url: 'https://docs.workato.com/en/workbot-for-teams/using-workbot-for-teams.md'
description: >-
  Run Workbot commands in Microsoft Teams to perform app actions and post event
  notifications using buttons, task modules, and Post message.
---

# Using Workbot for Microsoft Teams

## Workbot commands

You can perform actions in your apps, for example, creating new ServiceNow tickets or listing Salesforce opportunities, by sending Workbot commands from within Microsoft Teams.

![Command example](/assets/workbot-command-example.DR5KdNkL.png)_Send a 'newissue' command with additional parameters in Microsoft Teams, then receive a post message reply_

A Workbot command is a trigger that allows you to run a Workbot command recipe.

![New command](/assets/new-command.BK0S3wms.png)_Example 'newissue' command in a recipe_

Refer to [Workbot commands](/en/workbot-for-teams/workbot-triggers) to learn more about Workbot commands.

### Workbot help command

If you get stuck, you can run the **help** command in Workbot. Workbot responds with a list of commands available to you.

![Workbot help](/assets/workbot-help.D9fnOY8p.png)_Ask Workbot for help_

### Invoking Workbot commands in Microsoft Teams

Workbot commands can be invoked in three distinct ways:

- Send the command **in a direct message to Workbot or in a channel** (in a channel, this requires tagging Workbot, for example, **@workbot your\_command**)  
  ![Command recipes](data:image/png;base64,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)  
  
- Send the command **when a button is clicked**  
  ![Command recipes](data:image/png;base64,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)
  
- Submit a **task module form**.
  

Refer to [Buttons, choices, and task modules](/en/workbot-for-teams/buttons-choices-task-modules) to learn more about how buttons, choices, and task modules work.

Commands can also prompt users for additional parameters. For example, to create a new ServiceNow incident, you must provide the urgency, summary, and description of the incident. In this case, you can add three parameters; `urgency`, `summary` & `description`. When the command is invoked, Workbot opens a task module and prompts you for each parameter.

![Task module](/assets/task-module-sf.CdMIRqme.png)_Workbot can ask users for info if you specify additional parameters in your command_

## Event notifications using Post message action

Workbot can also be used to notify you when any events occur in your apps. This can be done through the **Post message** action.

![Closed SNow incident](/assets/closed-snow-incident.DL_yjKV0.png)_A Post message action notifying user about a closed ticket in ServiceNow_

The **Post message** action allows you to post a message to a user or in a channel.

![Notification recipe](/assets/notification-recipe.DPaFA3hD.png)_A recipe where a Post message action notifies the user when a ServiceNow incident is closed_

Refer to [Workbot actions](/en/workbot-for-teams/workbot-actions) to learn more about how the Post message action works.

## Learn more

- [Getting started](/en/workbot-for-teams/getting-started)
- [Workbot triggers](/en/workbot-for-teams/workbot-triggers)
- [Workbot actions](/en/workbot-for-teams/workbot-actions)
- [Workbot buttons, pick lists, and task modules](/en/workbot-for-teams/buttons-choices-task-modules)

---
