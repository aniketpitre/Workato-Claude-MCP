---
url: 'https://docs.workato.com/en/workbot/using-dialogs-with-workbot.md'
description: >-
  Learn how to invoke Slack dialogs with Workbot to collect information from
  users interactively using a set of trigger and action recipes.
---

# Using Dialogs with Workbot

Workbot can be used to invoke [Slack Dialogs](https://api.slack.com/dialogs); an awesome Slack feature that allows you to elicit info in a more interactive way.

![Dialog gif](/assets/dialog-gif.B8ms8kEA.gif)

Workbot can invoke dialogs to, say, collect info from a user to open a ticket in Github, among other things.

## Concept

To create a dialog workflow, you need 3 recipes to perform 3 high-level functions:

1. **Trigger a post dialog recipe** When triggered, the action in this recipe _**triggers**_ the second recipe which in turn invokes the dialog. We'll call this the **Trigger recipe**.
   
2. **Post dialog** When triggered, the action in this recipe _**posts**_ the dialog.
   
3. **Execute actions** When the dialog is submitted, the actions in this recipe _**executes**_ the follow-up actions.
   

![Dialog diagram](/assets/anatomy-of-a-dialog.CxO7pS1T.png)

From a recipe standpoint, the first recipe triggers the **Trigger recipe**, which in turn triggers the **Execute actions** recipe.

This is because invoking dialogs requires `Trigger ID`, something that's only generated from button or menu option click events on Slack.

Check out these simple recipes to see dialogs in action: [Trigger recipe](https://www.workato.com/recipes/673215-1-invoke-dialog#recipe), [Post dialog](https://www.workato.com/recipes/673218-2-configure-dialog#recipe), and [Execute actions](https://www.workato.com/recipes/673219-3-actions#recipe)

### Triggering a post dialog recipe

To trigger a post dialog recipe, use either the **Post command reply** or **Post message** Workbot actions.

Regardless of which Workbot action you choose, the dialog recipe can be triggered via 2 methods:

#### 1\. Buttons

![Buttons](/assets/invoke-with-buttons.xuarHi5x.png)

The **Submit button command** field is especially important - this command will trigger the recipe that posts the dialog (i.e. the **Trigger recipe**).

![Submit button command](/assets/submit-button-command.D63ls3ci.png)

#### 2\. Menu options

![Menu options](/assets/invoke-with-menu-options.m9wPTVzA.png)

The **Submit menu option command** field is especially important - this command will trigger the recipe that posts the dialog (i.e. the **Trigger recipe**)

![Submit menu option command](/assets/submit-menu-option-command.BN4u_OWk.png)

Clicking either buttons or menu options in Slack triggers an event that comes with a `Trigger ID`, a parameter necessary for invoking dialogs.

In the example above, both the button and the menu option sends a Workbot command to `collect issue details`.

### Posting a dialog

To ensure that the dialog in this recipe is the one to be invoked, the submit button or menu option commands in the **Trigger recipe** must map to the **Post command** trigger in this post dialog recipe.

![Mapping invocation with dialog](/assets/mapping-invocation-to-dialog.R7xU6CPy.png)

The **Post dialog** recipe uses the Workbot **Post command** trigger to receive commands from the buttons or menu options in the **trigger** recipe.

In this example **Post dialog** [recipe](https://www.workato.com/recipes/673218-2-configure-dialog#jobs), both the submit button and submit menu option commands `collect issue details` are identical to the **Post dialog** trigger `collect issue details`.

![Mapping invocation with dialog](/assets/mapping-invocation-to-dialog-2.D_L7-Um4.png)

#### Setting up the post dialog

Use the **Post dialog** action to set up the post dialog.

The following table lists the available fields in the **Post dialog** action.

| Field | Explanation | What goes in here |
| --- | --- | --- |
| Trigger ID | The ID of a submit button or submit menu option triggered event. | Use the Trigger ID (Step 1) datapill from the **Post command** trigger. |
| Callback ID | Identifier for the dialog. Maximum length of 255 characters. | Pass command input values from the **Submit button** or **Submit menu option** commands defined in the trigger recipe. ![](/assets/button-command-input-values.Tp2m1-Z9.png)![](/assets/menu-option-command-input-values.BmdQ8o9X.png) Ensure that the parameter names in the trigger recipe match the command input fields in the recipe that _posts_ the dialog. |
| Dialog title | The title of the invoked dialog. Maximum length of 24 characters. | Explain the purpose of the dialog, for example, _Create a ticket_ |
| Submit button label | Text label to display on the dialog **Submit** button. Single word input only. | Defaults to **Submit** when left blank. All dialogs will have a **Cancel** button by default.![](/assets/default-dialog-submit-cancel.BDzkswNO.png) |
| Submit button command | Workbot command to execute when Slack user clicks on the **Submit** button in the dialog | Use a Workbot command that matches the **Post command** trigger of the recipe to execute. |
| Dialog form fields | this will be **automatically** generated upon selecting a command in **Submit button command** input field. Max of 5 fields | This defines the fields that appear in the dialog. Modify this to include hints, error handling, picklist options, etc. for your dialog. Do not change the "name" values as they should match that of the command input fields of the recipe executed from the **Submit button command** above. See the example JSON from the **Post dialog** [recipe](https://www.workato.com/recipes/673218-2-configure-dialog#recipe). |

The **Submit button command** field is especially important - this command will trigger the recipe that executes the actions (i.e. the Execute actions recipe).

### Executing actions

To ensure that this recipe is the one to be executed by the dialog, the submit button command in the **Post dialog** recipe must map to this recipe's **Post command** trigger.

![Mapping dialog to another recipe](/assets/mapping-dialog-to-another-recipe.ox8FKzTH.png)

The last recipe (responsible for executing follow-up actions) uses the Workbot **Post command** trigger to receive commands from the submit button command in the **Post dialog** recipe.

In this example, the **Post dialog** [recipe's](https://www.workato.com/recipes/673218-2-configure-dialog#recipe) submit button command `github new issue` is identical to the **Execute actions** [recipe's](https://www.workato.com/recipes/673219-3-actions#recipe) **Post command** trigger `github new issue`.

![Mapping invocation with dialog](/assets/mapping-dialog-to-another-recipe-2.d0_GrWpX.png)

## Common pitfalls when using dialogs

Given that dialogs involve using multiple recipes, it's normal to encounter some issues at the start. Here are some common pitfalls when using dialogs.

### 1\. Using the same Post command trigger words on more than 1 recipe

![App, action, action data](/assets/app-action-actiondata.CiH2fRDe.png)

Ensure that the combination of all 3 **App**, **Action**, and **Action data** of Post command triggers in any of your recipes are unique across your Workato account. Any submit button or submit menu option command should only be mapped to 1 recipe.

For example, the recipe above should be the only recipe in that Workato account to have `github report bug` as its Post command trigger.

### 2\. Submit button / menu option commands incorrectly mapped

Ensure that the **Submit button command** and/or **Submit menu option command** of a recipe is correctly mapped to the Post command trigger of the secondary (or tertiary) recipe.

### 3\. Incorrect mapping of dialog form fields with command input fields of subsequently triggered recipe

Ensure that dialog form field names from the **Post dialog** recipe correspond with the command input fields of the subsequently triggered recipe.

![Mapping dialog form fields with command input fields](/assets/mapping-dialog-form-fields-to-command-input-fields.B_ZGElD1.png)

## Try it out

Try dialogs out by adding these example **[Trigger recipe](https://www.workato.com/recipes/673215-1-invoke-dialog#recipe)**, **[Post dialog](https://www.workato.com/recipes/673218-2-configure-dialog#recipe)** and **[Execute actions](https://www.workato.com/recipes/673219-3-actions#recipe)** recipes, invoking them from Slack.

![Invoke, post, execute](/assets/invoke-post-execute.CxPVb5LN.gif)

---
