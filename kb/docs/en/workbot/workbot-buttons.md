---
url: 'https://docs.workato.com/en/workbot/workbot-buttons.md'
description: >-
  Learn how Workbot buttons let Slack users trigger recipes and pass command
  inputs in one click, simplifying conversational workflows.
---

# Workbot buttons

Buttons are important building blocks in designing conversational interfaces that simplify complex workflows.

Workbot commands require specific keywords to trigger. This unique language needs to be communicated and picked up by users to execute Workbot commands successfully. Buttons allow a call to action to be performed in one click, allowing the user to quickly decide what they want, without having to remember additional Workbot commands.

![Buttons](/assets/buttons.DbEriZSS.png)_Buttons use button clicks to trigger another recipe or workflow_

## Features

Buttons can:

1. Trigger another recipe that has a Workbot post command trigger
   
2. Pass command input values to that recipe
   
3. Invoke dialogs, as covered in the ['Using dialogs with Workbot'](/en/workbot/using-dialogs-with-workbot) guide.
   
4. Be posted as a set list, or a [dynamically generated one](#dynamic-list-of-buttons).
   

To ensure a good conversational interface, keep the number of buttons less than 5.

## Anatomy of a button

Buttons can be used in either a Workbot [post command reply](/en/workbot/workbot-command-reply) or a [post message action](/en/workbot/workbot-actions#post-message).

![Button fields](/assets/buttons-fields.Dx7dz8QM.png)

The following table shows what goes into the button fields:

| Input field | Value | Description |
| --- | --- | --- |
| Button title | Button title for example, Cancel | Key in the title of the button to be displayed. ![](/assets/button-title.Dy4oaItl.png) |
| Submit button command | Workbot command to execute when button is clicked, for example,
salesforce update account

 | Choose from a list of existing post command triggers (from different recipes), or key in your own 3-word command. Clicking on this button will trigger the recipe with the corresponding command trigger. |
| Command input values | Command input values to pass onto the next recipe when button is clicked, for example, **account\_id**: Account ID**account\_description**: Account Description | Key in name-value pairs to pass onto the next recipe as command input fields. |

When a button is clicked, it triggers another recipe and passes onto it any command input values you define in the button fields.

For example, in the button fields below, where:

- **Title**: `Highest`
- **Submit button command**: `ui_feature highest priority`
- **Command input values**: `project`: Project, `issue_type`: Issue type, `priority`

![Button 4 fields](/assets/button-4-fields.ZG7T9J_r.png)

This posts the button (along with 3 other buttons 'High', 'Low' and 'Lowest') to the user like so:

![Button 4 Slack](/assets/button-4-slack.BmaCimV-.png)

When clicked, the button triggers the following recipe:

![Triggered recipe](/assets/triggered-recipe.DxBH3ZHZ.png)_The recipe triggered by the button_

Notice that the command trigger `ui_feature highest priority` of the triggered recipe matches the **Submit button command** of the button.

## Dynamic list of Buttons

Buttons can also be generated dynamically using a list datapill (for more information on lists, see the [list management guide](/en/features/list-management))

From the button fields, select the horizontal ellipsis on the top-right and choose 'Dynamic List'. This should bring up the dynamic buttons fields.

![Dynamic buttons](/assets/dynamic-buttons.BBDJq33Z.png)

The following table shows what goes into the dynamic buttons fields:

| Input field | Value | Description |
| --- | --- | --- |
| Button source list | Input an Accounts list datapill. | List datapills have a list icon next to them in the datatree, for example, Salesforce Accounts, a list: ![](/assets/list-datapill.CjKAPD8d.png) |
| Button title | Button title. For example,Account Name | The title of the button to be displayed. Typically, you want to use datapills from the list datapill, for example, Salesforce Account name, a datapill from the Salesforce Accounts list: ![](/assets/datapill-from-list-datapill.CnuTA83E.png) |
| Submit button command | Workbot command to execute when button is clicked, for example,
salesforce update account

 | Choose from a list of existing post command triggers (from different recipes), or key in your own 3-word command. Clicking on this button will trigger the recipe with the corresponding command trigger. |
| Command input values | Command input values to pass onto the next recipe when button is clicked, for example, **account\_id**: Account ID**account\_description**: Account Description | Key in name-value pairs to pass onto the next recipe as command input fields. |

In the example below, the user wants to update a Salesforce 'Direct Customer' account by clicking on a button associated with that account. As this list changes every day, a static list of buttons wouldn't work. In the dynamic button fields below, where:

- **Buttons source list**: Accounts
- **Button Title**: Account Name
- **Submit button command**: `salesforce update account`
- **Command input values**: `account_id`: Account ID, `account_description`: Account Description

![Dynamic buttons fields](/assets/dynamic-buttons-fields-example.BT9o6RvM.png)

This posts a dynamically generated list of buttons to the user like so:

![Dynamic buttons slack example](/assets/dynamic-buttons-slack-example.BrWQYmvB.png)

---
