---
url: 'https://docs.workato.com/en/recipes/start-and-stop.md'
description: >-
  Learn how to test, start, and stop recipes in Workato, including how recipes
  resume processing and when Workato stops them.
---

# Testing, starting, and stopping recipes

[Video](https://www.youtube.com/embed/W9X8nWWfEN4?rel=0&rel=0)

In Workato, you can manage recipes in several ways:

- **Test a recipe**: Run a single trigger event through the recipe’s logic to ensure it behaves as expected.
- **Start a recipe**: Activate the recipe to begin processing trigger events.
- **Stop a recipe**: Deactivate the recipe to halt the processing of new trigger events.
- **Use skip step**: Build and test your recipes incrementally by bypassing specific steps during testing.

* * *

## Testing recipes

Workato's integrated testing environment allows you to verify that your recipe's logic and data processing work correctly before starting it. Testing ensures that your automation functions properly, helping you avoid extensive clean-up later.

During recipe development, we recommend building and testing in small chunks. To enter test mode, click **Test jobs** or the **Test** button in the recipe editor:

![Test mode toggle and button in the recipe editor](/assets/test-mode-toggle.DfyGX4cL.png)_Test mode toggle and button in the recipe editor_

Refer to the [Testing recipes guide](/en/recipes/testing) for a detailed look at Workato's test environment.

* * *

## Starting recipes

Starting a recipe enables it to pick up and process trigger events. When you start a recipe, it becomes **active**.

### Starting a recipe for the first time

When you start a recipe for the first time, Workato fetches trigger events based on the [When first started, this recipe should pick up events from](/en/recipes/triggers#since-from) configuration. After this initial fetch, it continues to process subsequent events. If you set a **When first started, this recipe should pick up events from** date during testing, you cannot change this date after the recipe is started.

If you tested your recipe in test mode, it won't reprocess any trigger events picked up during testing. This prevents data duplication in your apps. Start your recipe only after fully testing it. Refer to the [testing recipes](/en/recipes/start-and-stop#test-mode) section for more information.

![Default start button](/assets/default-start-button.DvJrn23t.png)_Start recipe_

### Starting a recipe for the second time

Most Workato recipes continue processing from the point they were stopped. For example, if you stop a recipe on Monday and restart it on Thursday, it fetches and processes all trigger events that occurred from Monday onward.

However, this does not apply to recipes with real-time triggers powered by webhooks. Trigger events occurring while the recipe was stopped may not be captured. Learn more about [real-time triggers and webhooks](/en/recipes/triggers#real-time-triggers).

* * *

## Stopping recipes

Stopping a recipe makes it **inactive** and means the recipe no longer picks up trigger events. You must stop a recipe to make changes to it, or to rename the recipe.

Most Workato recipes continue where they have left off when a recipe is restarted from a stopped state. This behavior depends on the trigger the recipe has. For most Workato triggers, the recipe continues to process jobs from when it stopped. For example, if the recipe was stopped on Monday, and started again from Thursday, the recipe fetches all trigger events that have occurred since Monday and processes them.

However, this behavior may vary for recipes with real-time triggers powered by webhooks. In these cases, trigger events that occur while the recipe is stopped may not be picked up. Learn more about [real-time triggers and webhooks](/en/recipes/triggers#real-time-triggers).

### Recipes stopped by Workato

Workato may stop one or more recipes in your account under certain conditions. In these cases, Workato sends you an email notification about the stopped recipe.

Workato may stop a recipe for the following reason:

- The recipe has encountered 60 consecutive errors when trying to fetch trigger events. This can occur for various reasons, such as disconnected connections due to password changes or downtime on the app's API server. You must fix the underlying issue before the recipe can run successfully.

### Notification emails

When Workato stops a recipe, it sends an email to the login email associated with your Workato account. You can change this email and/or add additional email recipients in the following locations:

- **Workspace admin > Settings > Notifications**
- **Workspace admin > Settings > Error alerts**

---
