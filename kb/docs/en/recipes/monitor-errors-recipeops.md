---
url: 'https://docs.workato.com/en/recipes/monitor-errors-recipeops.md'
description: >-
  Set up RecipeOps triggers to monitor failed jobs and recipes stopped by
  Workato across your workspace, then send alerts or restart workflows.
---

# Monitor errors with RecipeOps

RecipeOps enables you to detect and respond to failures that occur outside a single recipe's scope. This includes job-level failures and cases where Workato stops a recipe entirely. This section covers two triggers:

- [Job failed](#monitor-failed-jobs-with-recipeops): Triggers when a monitored recipe encounters a failed job.
- [Recipe stopped by Workato](#monitor-stopped-recipes-with-recipeops): Triggers when repeated or critical errors stop a recipe.

Each trigger returns error details and recipe context, which let you send alerts, raise incidents, or restart workflows.

## Monitor failed jobs with RecipeOps

Use the RecipeOps [Job failed trigger](/en/connectors/recipeops/triggers/new-failed-job) to monitor failed jobs across your workspace. This trigger runs at the workspace level and centralizes failure tracking across multiple recipes. You can monitor all recipes, specific recipe IDs, or recipes with selected tags.

The trigger provides metadata and error details, including the error type, message, app, action, step, and timestamps. These fields help you send alerts, escalate issues, and review patterns across failed jobs.

### Example: Send alerts when any monitored recipe fails

This recipe demonstrates how to use the **Job failed** trigger to send an error alert when any monitored recipe fails:

1. Add the **Job failed** trigger from the RecipeOps connector.
   
2. Use the **Recipes to monitor** drop-down menu to select how you plan to monitor recipes:
   
   - Choose **All** to monitor all recipes in the workspace.
   - Choose **Selected** and enter specific recipe IDs.
   - Choose **Tags** and enter one or more tags.
   
   ![Configure the Job failed trigger](/assets/configure-recipeops-job-trigger.CA7V4j8l.png)_Configure the Job failed trigger_
   
3. Enable the **Set trigger condition** toggle to filter job failures at the trigger level. For example, filter by error type, errored app, or recipe ID to capture only specific failure scenarios.
   
4. Click **\+ Add step** and select **Action in app**.
   
   ![Add action](/assets/add-step-standard.DEbq8cJp.png)_Click **Add step > Action in app**_
   
5. Add the **Send email** action.
   
6. Map datapills from the trigger output into the email fields. You can include details such as Recipe ID, Job ID, Error type, and Error message to provide recipients full context.
   
   ![Map datapills to email fields](/assets/map-datapills-email.DnEMRQv4.png)_Map datapills to email fields_
   

## Monitor stopped recipes with RecipeOps

Use the RecipeOps [Recipe stopped by Workato](/en/connectors/recipeops/triggers/recipe-stopped-by-workato#input) trigger to detect when Workato stops a recipe due to repeated or critical errors, such as 60 consecutive trigger authentication failures.

The trigger provides context such as the recipe ID and error attributes like type, connector, error count, and flags for authorization or rate limiting issues. You can monitor all recipes, specific recipe IDs, or recipes with matching tags.

### Example: Send an alert when a recipe stops due to an authorization error

This example demonstrates how to use the **Recipe stopped by Workato** trigger to detect authorization errors and notify your team:

1. Add the **Recipe stopped by Workato** trigger from the RecipeOps connector.
   
2. Use the **Recipes to monitor** drop-down menu to select how you plan to monitor recipes:
   
   - Choose **All** to monitor all recipes in the workspace.
   - Choose **Selected** and enter specific recipe IDs.
   - Choose **Tags** and enter one or more tags.
   
   ![Configure the Recipe stopped by Workato trigger](/assets/configure-recipeops-stopped-trigger.CywQsKL-.png)_Configure the Recipe stopped by Workato trigger_
   
3. Enable the **Set trigger condition** toggle to filter for authorization-related stops. Use the Is authorization error datapill and set it to **is true**.
   
   ![Set trigger condition](/assets/configure-recipeops-condition.BuxP8ZzI.png)_Set trigger condition_
   
4. Click **\+ Add step** and select **Action in app**.
   
   ![Add action](/assets/add-step-standard.DEbq8cJp.png)_Click **Add step > Action in app**_
   
5. Add the **Send email** action.
   
6. Map datapills from the trigger output to the message, such as the Recipe ID, Error message, and Error connector.
   
   ![Map datapills to email fields](/assets/map-datapills-email-2.BhiiSwbE.png)_Map datapills to email fields_

---
