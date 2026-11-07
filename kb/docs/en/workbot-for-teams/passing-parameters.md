---
url: 'https://docs.workato.com/en/workbot-for-teams/passing-parameters.md'
description: >-
  Pass parameters into Workbot recipes in Microsoft Teams using line commands,
  buttons, task modules, and pick lists to supply recipe context.
---

# Passing parameters

Parameters are additional information to be used in the recipe in the form of datapills. [Defining parameters](/en/workbot-for-teams/workbot-triggers#defining-parameters) in the Workbot trigger block is vital for the parameters to be passed successfully into the recipe, without which there will be no datapills to be used in the recipe actions.

There are two sources for these parameters - the user and another recipe - and four ways these parameters can be passed into the recipe - [line commands](#line-commands), [buttons](#buttons), [task modules](#task-modules) and [pick lists](#picklists).

## Line commands

If the parameters of the recipe are known beforehand, the user can specify them with the Workbot command after a space, with the format parameter1: value1 parameter2: value2 parameter3: value3, etc. An example can be seen in the top right corner of the screenshot below.

![Command with in-line parameters](/assets/workbot-command-example.DR5KdNkL.png)_Sending a 'newissue' command with additional parameters Urgency, Summary, and Description_

## Buttons

Buttons can be used in either a [post reply](/en/workbot-for-teams/workbot-actions#post-reply-and-post-simple-reply) or a [post message](/en/workbot-for-teams/workbot-actions#post-message-and-post-simple-message) action.

The following table shows what goes into the button fields:

| Input field | Description |
| --- | --- |
| Button text | Text to be displayed on the button. ![](data:image/png;base64,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) |
| Submit button command | Workbot command to execute when button is clicked, for example, `create_ticket`. Only after [configuring the command](https://docs.workato.com/workbot-for-teams/workbot-triggers.html#configuring-the-command) in a Workbot for Microsoft Teams trigger block can that command be visible in the drop-down list. |
| Additional parameters | Parameter values to be passed onto the next recipe when button is clicked, for example: ![](/assets/additional-parameters.zNelN6G2.png) Datapills must be enclosed within double quotes, and parameter names should be entirely lowercase. These parameters can be supplied by users. For example, you can supply parameters such as the urgency of an issue in ServiceNow, or specific recipe details like the Message ID from a previous Microsoft Teams message. |

\*Supports Markdown

![Command name in button](/assets/button-command.BEaEEKM8.png)_A button can be configured to invoke a Workbot command of another recipe_

Parameters in the **Additional parameters** field of Recipe 1 are passed to the parameters defined in Recipe 2, invoked by the command within the **Submit button command** field.

![Recipe chaining](/assets/recipe-chaining.Cu78DS2c.png)

If there are more parameters passed in Recipe 1 than defined in Recipe 2, those extra parameters are not captured by Recipe 2; they are lost.

Conversely, if there are fewer parameters passed in Recipe 1 than defined in Recipe 2, Workbot auto-fills the parameters that passed successfully and launches a [task module](#task-modules) to prompt the user to fill in the missing parameters.

![Task module with missing parameters](/assets/task-module-with-missing-params.DmIwp3HK.png)_Half-filled task module_

## Task Modules

Task modules are dialog boxes that appear when Workbot needs more parameter values from the user.

![Task module in Teams](/assets/task-module-teams.Cadnllda.png)_Task module dialog box_

After the user fills in the required fields, these values are tied to datapills that the recipe can use later on.

![Parameters in datatree](/assets/parameters-in-datatree.VRCFc59T.png)_Parameters in the datatree_

For example, to create an incident in ServiceNow, you may want to prompt users for additional info like **Urgency**, **Summary**, and **Description**. By adding **Urgency**, **Summary**, and **Description** as parameters, Workbot will open a task module and prompt the user for each parameter.

![Task module](/assets/task-module-snow.BKLnEezm.png)_Workbot can ask users for info if you specify additional parameters in your command_

## Picklists

Picklists allow users to choose between a fixed number of options. This is useful when the available options are known, for example, Urgency (High:1, Medium: 2, Low: 3), Priority (1,2,3,4,5), and so on. They are not able to pass parameters on their own and must be paired with either buttons or task modules to do so.

### Picklists with buttons

Pick lists can be found in the [post reply](/en/workbot-for-teams/workbot-actions#post-reply-and-post-simple-reply) and [post message](/en/workbot-for-teams/workbot-actions#post-message-and-post-simple-message) actions.

![Choice param](/assets/choice-param.Dx4F0jO4.png)_The 'Next' button also passes the 'opportunity\_id' of 'Google' onto the command recipe that it invokes_

The following table shows what goes into the pick list and choice fields:

| Input field | Description |
| --- | --- |
| Pick list name | Name of pick list. Displays before choices, and supports markdown. |
| Pick list style | **Compact** displays choices in a drop-down menu, while **Expanded** displays all choices with radio buttons. |
| Choice parameter | Parameter name to store the choice value. This is a required field when passing parameters to another recipe, otherwise the value will not be passed. |
| Title | Text to display for choice. Cannot contain `:` or `,`. |
| Value | Value to pass to **Choice parameter** if chosen. Cannot contain `:` or `,`. |

\*Supports Markdown

![Choice param recipe](/assets/choice-param-recipe.COZvsFYT.png)_The choice parameter will take its value from a choice (if it's chosen)_

When the user chooses from the **Choices** available in the picklist, that value is attached to the **Choice parameter**, which can then be passed on to the next recipe. Therefore, while the **Choice parameter** is labeled as optional, it must be defined for the value chosen to have a parameter to attach to. Furthermore, that same parameter must be [defined](/en/workbot-for-teams/workbot-triggers#defining-parameters) in the downstream recipe's trigger block for the **Choice parameter** to be passed successfully.

The user can define only one picklist per **post reply** or **post message** action block, meaning that only one parameter can be passed to the downstream recipe using a pick list.

### Picklists in task modules

When [defining parameters](/en/workbot-for-teams/workbot-triggers#defining-parameters) in the Workbot for Microsoft Teams trigger block, a picklist is created in the task module when the **Data type** is set to `String` and comma-separated options are added to the **Options** field.

If the display name and the value are different, separate the two by a colon, for example, High:1, Medium:2, Low: 3. That parameter's value thus takes on the option selected by the user and can be used further in the recipe as a datapill; a parameter gets passed through a pick list.

It's important to note that pick list display name and value cannot contain `:` or `,`.

![Picklist options in recipe](/assets/parameter-picklist-1.BlbYC_lH.png)_Options where display name and value are the same_

![Picklist options in recipe](/assets/parameter-picklist-1.BlbYC_lH.png)_Options where display name and value are different_

![Picklist in Teams](/assets/parameter-picklist-teams.wJqxw1Zp.png)_Options displayed in a picklist in task module_

## Learn more

- [Using Workbot for Microsoft Teams](/en/workbot-for-teams/using-workbot-for-teams)
- [Workbot triggers](/en/workbot-for-teams/workbot-triggers)
- [Workbot actions](/en/workbot-for-teams/workbot-actions)

---
