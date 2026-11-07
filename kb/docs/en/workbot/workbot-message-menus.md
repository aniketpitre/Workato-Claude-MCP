---
url: 'https://docs.workato.com/en/workbot/workbot-message-menus.md'
description: >-
  Learn how Workbot message menus collapse multiple actions into a Slack
  drop-down so users trigger recipes without remembering commands.
---

# Workbot message menus

Message menus are an important building block in designing conversational interfaces that simplify complex workflows.

Workbot commands require specific keywords to trigger. This unique language needs to be communicated and picked up by users to execute Workbot commands successfully.

Message menus allow multiple calls to action to be collapsed into a single drop-down menu. Each menu option can execute a command in one click, allowing the user to quickly decide what they want, without having to remember additional Workbot commands.

![Anatomy of message menus](/assets/message-menus.Bg4dpSYR.png)_Message menus use menu option clicks to trigger another recipe or workflow_

## Features

Message menus can:

1. Trigger another recipe that has a Workbot post command trigger
   
2. Pass command input values to that recipe
   
3. Invoke dialogs, as covered in the [Using dialogs with Workbot](/en/workbot/using-dialogs-with-workbot) guide.
   
4. Be posted as a set list, or a [dynamically generated one](#message-menus-with-a-dynamic-list-of-menu-options).
   

Message menus can be used in either a Workbot post command reply or a post message action.

To ensure a good conversational interface, keep the number of menu options to less than 5.

## Message menus with a static list of menu options

![Button fields](/assets/message-menu-fields.Cun4Jiso.png)

The following table shows what goes into the message menu fields:

| Input field | Value | Description |
| --- | --- | --- |
| Menu name | Menu name for example, Accounts | Key in the name of the menu to be displayed. ![](/assets/menu-name.Ehp1SZfE.png) |
| Menu options |
| Display text | Menu option text for example, Account Name | The text of the menu option to be displayed. ![](/assets/menu-options-example.5-WHzO9m.png) |
| Submit menu option command | Workbot command to execute when menu option is clicked, for example,
```
salesforce update account
```

 | Choose from a list of existing post command triggers (from different recipes), or key in your own 3-word command. Clicking on this menu option will trigger the recipe with the corresponding command trigger. |
| Command input values | Command input values to pass onto the next recipe when menu option is clicked, for example, **account\_id**: Account ID**account\_description**: Account Description | Key in name-value pairs to pass onto the next recipe as command input fields. |

When a menu option is clicked, it triggers another recipe and passes onto it any command input values you define in each menu option field.

For example, in the message menu fields below, where:

- **Menu name**: `Accounts`
- **Menu options**
  - **Display Text**: `Edge Communications`
  - **Submit menu option command**: `salesforce update account`
  - **Command input values**: `account_id`, `account_description`

![Message menu example](/assets/message-menu-example.B2aLd345.png)

This posts a message menu to the user like so:

![Menu option Slack](/assets/menu-option-slack.CkhdxxpO.png)

When clicked, the menu option triggers the following recipe:

![Triggered recipe](/assets/triggered-recipe.B4jS4Dip.png)_The recipe triggered by the menu option_

Notice that the command trigger:  
`salesforce update account`  
of the triggered recipe matches the **Submit menu option command** of the menu option.

## Message menus with a dynamic list of menu options

The menu options of message menus can also be generated dynamically using a list datapill (for more information on lists, see the [list management guide](/en/features/list-management)).

From **Message menu**, under **Menu options**, select the horizontal ellipsis on the top-right and choose 'Dynamic List'. This should bring up the dynamic menu options fields.

![Dynamic menu options](/assets/dynamic-menu-options.BaJ59-UW.png)

The following table shows what goes into the dynamic menu options fields:

| Input field | Value | Description |
| --- | --- | --- |
| Menu name | Menu name for example, Accounts | Key in the name of the menu to be displayed. ![](/assets/menu-name.Ehp1SZfE.png) |
| Menu options |
| Menu options source list | Input an Accounts list datapill. | List datapills have a list icon next to them in the datatree, for example, Salesforce Accounts, a list: ![](/assets/list-datapill.CjKAPD8d.png) |
| Display text | Display text. For example, Account Name | The text of the menu option to be displayed. Typically, you want to use datapills from the list datapill, for example, Salesforce Account name, a datapill from the Salesforce Accounts list: ![](/assets/datapill-from-list-datapill.CnuTA83E.png) |
| Submit menu option command | Workbot command to execute when menu option is clicked, for example,
```
salesforce update account
```

 | Choose from a list of existing post command triggers (from different recipes), or key in your own 3-word command. Clicking on this menu option will trigger the recipe with the corresponding command trigger. |
| Command input values | Command input values to pass onto the next recipe when the menu option is clicked, for example, **account\_id**: Account ID**account\_description**: Account Description | Key in name-value pairs to pass onto the next recipe as command input fields. |

In the example below, the user wants to update a Salesforce 'Direct Customer' account by clicking on a menu option associated with that account. As this list changes every day, a static list of menu options wouldn't work. In the dynamic message menu fields below, where:

- **Menu name**: Accounts
- **Menu options**
  - **Menu options source list**: Accounts
  - **Display Text**: Account Name
  - **Submit menu option command**: `salesforce update account`
  - **Command input values**: `account_id`: Account ID, `account_description`: Account Description

![Dynamic menu option fields example](/assets/dynamic-menu-option-fields-example.DdJwIHD0.png)

This posts a dynamically generated list of menu options in the message menu to the user like so:

![Dynamic menu options slack example](/assets/dynamic-menu-options-slack-example.BC79HqeV.png)

---
