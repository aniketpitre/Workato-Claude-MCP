---
url: 'https://docs.workato.com/en/workbot-for-teams/buttons-choices-task-modules.md'
description: >-
  Configure Workbot buttons, task modules, and pick lists in Microsoft Teams to
  invoke commands and pass parameters to your recipes.
---

# Workbot buttons, Task modules and Pick lists

Workbot commands can be invoked via button or task module submissions.

![Command name in button example](/assets/button-submission.BDqVoJlT.png)_The 'Create issue' button invokes the 'newissue' command and executes the recipe when submitted_

Additional parameters can also be passed by buttons and task modules as they invoke a Workbot command. Typically, you use parameters to pass context to the invoked Workbot recipe.

![Button with params example](/assets/button-with-params.8r1JP7aF.png)_The 'Re-open issue' button not only invokes the 'reopen\_issue' command - it's also passing parameters!_

![Button with params recipe](/assets/button-with-params-recipe.CxVqWkjs.png)_The 'Re-open issue' button is configured to pass the 'sys\_id' so that the 'reopen\_issue' recipe knows which issue to re-open_

While choices in a pick list cannot invoke Workbot commands, they can pass their choice parameter together with button or task module submissions in the same message.

![Choice param recipe](/assets/choice-param-recipe.COZvsFYT.png)_The choice parameter will take its value from a choice (if it's chosen)_

The choice parameter is passed when a button from the same message is submitted (along with any other parameters the button may have).

![Choice param](/assets/choice-param.Dx4F0jO4.png)_The 'Next' button also passes the 'opportunity\_id' of 'Google' onto the command recipe that it invokes_

## Configuring buttons

Buttons can be used in either a [post reply](/en/workbot-for-teams/workbot-actions#post-reply-and-post-simple-reply) or a [post message](/en/workbot-for-teams/workbot-actions#post-message-and-post-simple-message) action.

![Command name in button](/assets/button-command.BEaEEKM8.png)_A button can be configured to invoke a Workbot command of another recipe_

The following table shows what goes into the button fields:

| Input field | Value | Description |
| --- | --- | --- |
| Title | Button title for example, Create ticket | Title of the button to be displayed. ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOMAAAA5CAMAAADz9Ww3AAABFFBMVEUAAABbW1ttbW1SUlJSUlJTU1NYWFhSUlJSUlJTU1NSUlJTU1NTU1NTU1NUVFRUVFRTU1NTU1NSUlJTU1NUVFRZWVlfX19TU1NbW1tSUlJSUlJTU1NSUlJTU1NTU1NxcXFSUlJTU1NSUlJSUlJTU1NVVVVSUlJSUlJTU1NWVlZTU1NSUlJUVFTBwt3Aw91UVFTIyORSUlJTU1NTU1NTU1PBw93////Awtz9/f5SUlL6+vzS0+a+v9vp6fOPkcGKi76DhLp+gLdnaarx8fjLy+JzdLG6utijpMxucK7i4u/HyODExd+gocqbnMdiZKff4O7Z2eqoqc719fq2t9eur9KVlsTk5fB3ebN2eLPU1eiztNXQ0eVkH1UZAAAANnRSTlMACwTBx20W7eh7XLasd0VKcmlgVzwcB4UR++Kh2rKUAppR07wnIPLLry32pzTmpkEcro1laO1FRqvrAAAEhElEQVRo3uyT2aqbUABF11GPGjVqo3GeU9NmgNDkvuT/f6xVMCKU0IKFFrpelM1m63LgP//5VwhPAFcdULxEhvwGV58R/8oboirBu/Ir0+6DiX7XKqzEvQPE+Q54Z6F+Wlwy4C07jZEvFm8Qzz1FzjT9bn1bvh59UanaWpLhs4fAzICmZHkj8WYtxySap+f1N451hGKeWIfalPBVGiFkO1Qpc1lD0DQnXM32T8CHCzcJfQxu1XjgPUCvRkexuTxGR1HpEN31RWVyfLiDY725Efl5nACM6/Rx7keMBHkcl8zJ/qizEo2NOOtNxTXVUTNpZZLA8WJD3L44u8+APIBtCLYXPopAZj4bBz4/R0dVbf2zBWDHEHxZVibHr9vBsXEU1MvN7xRgXO+NbXvQagCZybYoeSWnYsdaeKmwDrhZvVFBlRB/BaiNkG8bBvapSLJvLVqL6YF1rGfH8KlP36pnRqjWorJ0jO0I1xR1rYbAuF7lIFIPwPwE23JOtIDViI6t/YFihJrP+NPIA1zj/OhNjmjtrrJy/SiS5x72z/3s+OiYHOmskxktKgvHLD2BNO0fvBwPPqD5QPL8PDjOSZWwHs7lrENzefYvx9i+6cXsuM3LUJgPByV1IXyKbTk5BrMjH1+qeFlZvkfZCdqOgcnRaQDTApT0NDpOybpY6QFw046XY+HSGx75XVEA+qyAsgjAcfTkYhMYCZvRsU9DwqPFgDAMfVlZOpI7JGaL0kbAuB6Y13p31AG0O4lWMiXKVmc9kvQDUIx4dvTNQ2N73MzMZaC7g5UK0L8ahq2j2Ofu03lwRB6L6mIx0lxgWVk6RtqWsMvMXACM6xvDKFwGToWpypIp6dOWP4sQDCgRC+ZIzIHyOsuuy8rPEco8taiJxVHwN/KdPTg2AQCEoSiYQlzAFWwTfiPZfzOXEAPh3a1h7e1pAAAAwGMKzwIesl90sshtz9x2FYXBKOwL7X03i6YFhEI5lbMIqO//HlMsREZNZq60s+W7gaxVLr7wk5D218skvy1G8QYos753L+LLongL1PravQjLwpuwrN1zNsfNcXP8Gz/SMWBZj39EptDU9n/kSDruuYnb4pEuwAoaAxANNPYeK06h0Y5nkQIkwxN8Byt6fxLFU8fubLJjy8N5+MJT0YPlcQX0TZGBWLyLiE4UTiwiRQ+wOK6vjiyCrk+eG/XmOtYlnV+M7x4C2w/ZkLaelMkFsjxIopOr4yilHDPYQ8hiohzZ4EDXtXeUjrmOIV+GT1AgYUDUQJE3IKWzTkIfgJepRM9qPd7q48HkWU3L4PaBBaWrOCCIYj+fHJdk5djqB2yedFhqwx2p6G6OhDtQVEPmNNpxTlaOhPd6uZPUS224I0J+Dki1dyZHFAVB5XTKz80BXtE5gYKNoMoRxwK4ELX8IoKlzhtCDHZE7XHuS1wd26MYvTQVe1d5okl8qhMoqJ/Ek2OwF0NBp+Vnj8x1nYiTyY4AoXf3pJ0H+c+WLlfy8DAhJs/qAz/yf/WOzXFz3Bzv2Ry3vceP3UP+hLOADzjT+Q2PfWxwV2ipigAAAABJRU5ErkJggg==) |
| Submit button command | Workbot command to execute when button is clicked, for example, `create_ticket` | Choose from a list of existing recipes that can be invoked by a Workbot command. |
| Parameters | Parameter values to pass onto the next recipe when button is clicked, for example,
{   "sys\_id": "sys\_id"   "summary": "Summary",   "description": "Description" }

 | Key in name-value pairs to pass onto the next recipe as parameter values. Remember to wrap datapills with double quotes. |

## Configuring a pick list and choices

While choices cannot invoke Workbot commands, they can pass their choice parameter together with button or task module submissions in the same message.

![Choice param recipe](/assets/choice-param-recipe.COZvsFYT.png)_The choice parameter will take its value from a choice (if it's chosen)_

The choice parameter is passed when a button from the same message is submitted (along with any other parameters the button may have).

![Choice param](/assets/choice-param.Dx4F0jO4.png)_The 'Next' button also passes the 'opportunity\_id' of 'Google' onto the command recipe that it invokes_

The following table shows what goes into the pick list and choice fields:

| Input field | Description |
| --- | --- |
| Pick list name | Name of pick list. Displays before choices, and supports markdown. |
| Pick list style | **Compact** displays choices in a drop-down menu, while **Expanded** displays all choices with radio buttons. |
| Choice parameter | Parameter name to store the choice value. This name-value pair will be passed on as additional parameters. |
| Title (choice) | Title of the choice to be displayed. |
| Value (choice) | Value of the choice. If chosen, passes its value to the **Choice parameter**. |

## Task modules

When parameters are defined in the Workbot command, Workbot will launch a task module within Teams to collect parameter values from the user.

![Parameters in recipe](/assets/task-module-recipe.CIHFzVfw.png)_Parameters in recipe_

Here's how the task module looks like when prompting users for parameter values.

![Task module in Teams](/assets/task-module-teams.Cadnllda.png)_Parameters in recipe_

### Adding hints and example values in task modules

Hints and example values can be configured for each parameter. Hints appear below the input field; example values will appear inside the input field.

![Parameters schema](/assets/task-module-recipe.CIHFzVfw.png)_Parameters in recipe_

Here's how the task module looks like when prompting users for parameter values.

![Hints & examples in Teams](/assets/task-module-teams.Cadnllda.png)_Hints below input fields; example values inside input fields_

### Hiding parameters

Parameters can be hidden in task modules by setting **Optional** to **Yes**, and **Visible?** to **No**. This is useful when passing record IDs that are not human-readable.

![Hidden parameter](/assets/hidden-parameter.C5y5Zf37.png)

The parameter will be hidden from the task module.

![Hidden parameter](/assets/hidden-parameter-teams.e6N-3Ds_.png)

## Adding picklist options in task modules

Picklist options can be configured so that users can pick from a finite list of choices. This is useful when the available options are known, for example, Urgency (High:1, Medium: 2, Low: 3), Priority (1,2,3,4,5), and so on.

To add a picklist, simply add comma-separated options in the **Options** field. If the display name and the value are different, separate the two by a colon, for example, **High:1, Medium:2, Low: 3**.

It's important to note that pick list display name and value cannot contain `:` or `,`.

![Picklist options in recipe](/assets/parameter-picklist-1.BlbYC_lH.png)_Options where display name and value are the same_

![Picklist options in recipe](/assets/parameter-picklist-2.BuQp2BDO.png)_Options where display name and value are different_

![Picklist in Teams](/assets/parameter-picklist-teams.wJqxw1Zp.png)_Options displayed in a picklist in task module_

## Dynamic buttons & fact sets

Buttons and fact sets can also be generated dynamically using a list datapill (for more information on lists, see the [list management guide](/en/features/list-management))

From the button (or fact set) fields, select the horizontal ellipsis on the top-right and choose 'Dynamic List'. This should bring up the dynamic list option.

![Dynamic buttons](/assets/dynamic-buttons.BeWUtkb7.png)

The following table shows what goes into the dynamic buttons fields:

| Input field | Value | Description |
| --- | --- | --- |
| Button source list | Input a list datapill, for example, Users. | List datapills have a list icon next to them in the datatree, for example, Salesforce users: ![](/assets/list-datapill.BrilKYgf.png) |
| Title | Button title for example, Assign users | The title of the button to be displayed. Typically, you want to use datapills from the list datapill, for example, Salesforce user name, a datapill from the Salesforce users list: ![](/assets/dynamic-button-title.CKlYbqz8.png) |
| Submit button command | Workbot command to execute when button is clicked, for example, `assign_user` | Choose from a list of existing Workbot command recipes or key in a new command. Clicking on this button will trigger the recipe with the corresponding command trigger. |
| Additional parameters | Pass additional parameters when user submits by clicking a button. Format should be JSON with name-value pairs, for example,
{   "opportunity\_id": "Opportunity ID",   "stage": "Stage" }

 | Key in name-value pairs to pass onto the next recipe as additional parameters. |

## Learn more

- [Using Workbot for Microsoft Teams](/en/workbot-for-teams/using-workbot-for-teams)
- [Workbot triggers](/en/workbot-for-teams/workbot-triggers)
- [Workbot actions](/en/workbot-for-teams/workbot-actions)

---
