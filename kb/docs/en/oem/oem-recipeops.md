---
url: 'https://docs.workato.com/en/oem/oem-recipeops.md'
description: >-
  Use the Embedded RecipeOps connector to monitor and manage active recipes and
  customer usage thresholds across all customers at scale.
---

# Embedded RecipeOps

The RecipeOps connector supports building recipes that monitor and manage active recipes and account-related activities. RecipeOps enables you to implement automating and monitoring operations on a large scale.

Embedded-specific actions and triggers monitor events across all customers, so connections do not need to be established one at a time.

## Customer threshold reached

The **Customer threshold reached** trigger enables partners to obtain near real-time events across all customers when the customers reach their task threshold. To use this trigger, your customers must be on a task-based pricing plan. Contact your Workato representative for plan set up.

To begin using the trigger, set up a RecipeOps connection and select **My account** in the **Whose account are you managing?** field.

The trigger receives events when customers reach usage thresholds determined by plan limits. The trigger tracks usage thresholds in 10% increments. For example, you could configure the trigger to take an action when customers reach 50%, 60%, or 70% of their 20,000 task quota. After that, partners can use recipe logic to automatically:

- Stop all recipes within the customer workspace.
- Send notifications to themselves or customers.
- Log this information into the partner's external logging system.

![Task counting simple](/assets/recipeops-task-threshold.DXggkYuc.png)_Customer threshold reached trigger recipe example_

## Actions

<dl><dt>Stop all recipes</dt><dd>Stop all recipes when the customer reaches their quota by using recipe logic filters to filter out the 100% and use the API to list and stop all recipes. See <a href="https://docs.workato.com/oem/oem-api/recipes.html#list-recipes-in-a-customer-account">List recipes API</a> and <a href="https://docs.workato.com/oem/oem-api/recipes.html#stop-recipe-in-a-customer-account">Stop recipes API</a> for more information.</dd><dt>Notify customers</dt><dd>Map the datapills from the output into the message field to send a notification directly to the customer. You can use a message template/Sendgrid or craft a message in the email body directly.</dd><dt>Notify the partner's team</dt><dd>Map the datapills from the output into the message field to send a notification to the partner's team. For example, you could send the message to a specified Slack channel. You can also use this method to send a message directly to the partner's analytic/logging platform.</dd></dl>

---
