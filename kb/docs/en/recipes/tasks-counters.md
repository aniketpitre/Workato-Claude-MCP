---
url: 'https://docs.workato.com/en/recipes/tasks-counters.md'
description: >-
  Find where to view Workato task counts by job, recipe, and account, and learn
  how to monitor and manage task usage.
---

# Task counters

The number of [tasks](/en/recipes/tasks) run in a Workato account can be found in several places on the platform.

## Tasks per job

For information on how many tasks are run per job, select a job to view the total number of tasks used.

![Task count job](/assets/task-counting-ui-job-report.C-TC8oFZ.png)_Task information available on job report page_

A recipe that contains one or more calls to other recipes will not see the total number of tasks across all child jobs. Each child job has its own total number of tasks.

## Tasks per recipe

When navigating in the recipe page, use the link in the `Settings` tab to be taken to the dashboard view that is filtered for the specific recipe.

![Task count recipe](/assets/recipe-settings.CM_nXwvy.png)_Link to the dashboard in Settings tab_

Alternatively, select the folder or recipe from the drop-down on top of the dashboard. Perform date or time manipulations to see the number of tasks done by folder or recipe in a specific amount of time. Learn more in the documentation on the [Operations hub dashboard](/en/features/admin-dashboard).

![Task count recipe](/assets/filtered-dashboard.DTuCl_XW.png)_Task count by recipe in the dashboard_

Lastly, call [the Workato Recipes API](/en/workato-api) with recipe ID or use [the RecipeOps connector](/en/connectors/recipeops#recipeops-by-workato). Response of the API calls includes lifetime task count data. The RecipeOps connector provides a Lifetime task count datapill in certain actions.

## Tasks per account

The monthly account usage is available in the [Subscription](https://www.workato.com/users/current/edit#subscription) tab in **Workspace admin**. The total number of tasks is broken down to a calendar monthly quota and is based on subscription plan types. If your Workato account is not on a task-based plan, this graph is not available to you.

![Task count account](/assets/subscription-page.4jVrYipQ.png)_Total number of tasks in subscription_

## Task usage management by recipe

You can manage task usage at the recipe level by using the [RecipeOps connector](/en/connectors/recipeops#recipeops-by-workato) or by calling the [Workato Recipes API](/en/workato-api/recipes). You can use RecipeOps connector or the Recipes API to set a data quota. Your recipe automatically stops running when the lifetime task count data exceeds the quota you set.

![Manage task usage per recipe](/assets/managing-task-usage-per-recipe.CSy5HOGL.png)_Managing task usage per recipe.[Example recipe](https://app.workato.com/recipes/1477200?st=f1b427)_

The preceding recipe is an example of managing task usage per recipe with the RecipeOps connector. The recipe checks the task usage of each active recipe in your Workato account every 120 minutes. If any active recipes consume more tasks than a certain quota, those recipes will stop automatically and send an email notification. In the recipe, the quota is set as 100,000 and can be adjusted based on your use case. The recipe trigger interval also can be modified. The recipe can be broken down into following basic steps:

- Trigger the recipe every 120 minutes.
- Retrieve data for all active recipes.
- Search for existing data by recipe in a designated lookup table.
- If the data does not exist, create a new row and insert correct data for each column.
- If the data does exist, calculate the difference between previous task usage and new task usage per recipe.
- If the difference is greater than the task usage quota you set, stop the recipe and send an email notification.
- If the difference is smaller than the quota, update a relevant column.

---

---
url: >-
  https://docs.workato.com/en/connectors/telegram/answer-callback-query-action.md
description: >-
  Show a notification, alert, or URL to a Telegram user after they tap an inline
  keyboard button on your bot's message.
---

# Telegram - Answer callback query action

The **Answer callback query** action responds to a callback query sent when a user taps an inline keyboard button in Telegram.

## Input

| Input field | Description |
| --- | --- |
| Callback query ID | Enter the unique identifier of the query to answer. |
| Text | Optional. Enter the text of the notification. Leave this field blank to not display a notification. |
| Show alert | Optional. Select **Yes** or **No** to show an alert instead of a notification at the top of the chat screen. |
| URL | Optional. Enter a URL to open in the user's client, such as a link to a game accepted through @BotFather. |
| Cache time | Optional. Enter the maximum number of seconds that the result of the callback query may be cached client-side. Defaults to `0`. |

## Output

| Output field | Description |
| --- | --- |
| Is answered? | A boolean response (`true` or `false`) that indicates if the request was successful. |

---
