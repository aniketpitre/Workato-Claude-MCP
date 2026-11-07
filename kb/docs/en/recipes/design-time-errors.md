---
url: 'https://docs.workato.com/en/recipes/design-time-errors.md'
description: >-
  Learn how to find and fix design-time errors in Workato recipes that prevent
  you from testing or starting the recipe.
---

# Design-time errors

During the development phase of your Workato recipe, errors known as design-time errors can prevent you from testing or starting your recipe. Design-time errors typically appear when you select **Test recipe** or **Start recipe**. You must resolve these errors to prevent job failures when the recipe is executed.

## How to find the error

When you start a recipe, you may see an error message near the recipe name. This error prevents the recipe from starting completely. Complete the following steps to locate and fix the error:

1. Click the **Edit recipe to fix errors** button to access the editor view.
   
   ![Edit recipe](/assets/recipe-errors.Cikh3sj2.png)_Edit recipe to fix errors_
   
2. View error notifications displayed at the top of the screen in the editor view.
   
   ![Error notifications](/assets/error-notifications.DCoQPgLq.png)_View error notifications_
   
3. Click on the highlighted step numbers to quickly navigate and fix these errors by going directly to the incorrect step.
   

## Common design-time errors

Unaddressed design-time errors can lead to operational failures, incorrect data processing, or other significant issues during recipe execution. The following examples are some of the most common design-time errors you may face when building and configuring your recipe:

### Unestablished connectivity

Errors related to unestablished connectivity occur when a recipe cannot establish a valid connection with external services or apps. Invalid credentials, permissions, or missing configurations can cause connectivity issues that must be resolved before the recipe can run. Learn more about [unestablished connectivity](/en/recipes/design-time-errors/unestablished-connectivity).

### Empty actions

Actions within a recipe without the required configuration or data can result in errors that prevent the recipe from starting. Each action must have all necessary fields filled out to function correctly. Learn more about [empty actions](/en/recipes/design-time-errors/empty-actions#empty-actions).

### Missing input fields

Triggers and actions require configuration to function correctly in a recipe. If a required input field does not have values or datapills, the recipe raises a design-time error and cannot start until the field is filled. Learn more about [missing input fields](/en/recipes/design-time-errors/empty-actions#missing-input-fields).

### Unavailable fields

You may receive a design-time error if your recipe uses data fields that aren't available in your app. This can happen if a field in your app is deleted or renamed. Learn more about [unavailable fields](/en/recipes/design-time-errors/empty-actions#unavailable-fields).

### Invalid datapills

Datapills can become invalid or missing if their source trigger or action is modified or deleted. The recipe cannot start without accurate data mapping, and the missing datapills must be replaced with valid ones. Learn more about [invalid datapills](/en/recipes/design-time-errors/empty-actions#invalid-datapills).

### Incorrect formulas

Formulas with syntax errors, misspellings, or logical issues can generate errors. Ensuring proper syntax, operator spacing, and logical correctness is crucial to resolving formula errors. Learn more about [incorrect formulas](/en/recipes/design-time-errors/incorrect-formulas#incorrect-formulas).

### Incorrect code actions & SQL statements

Errors in Python, Ruby, JavaScript, SQL code actions, and other programming languages can prevent the recipe from starting. Coding actions must be free of syntax and logical issues before testing or running the recipe. Learn more about [incorrect code actions and SQL statements](/en/recipes/design-time-errors/incorrect-formulas#incorrect-code-actions-and-sql-statements).

### On-prem agent (OPA) errors

Integrating on-prem agents (OPA) with your recipe requires careful setup. Common issues include configuration details in the `config.yml` file, account permissions, and access to the logs folder. We recommend checking the OPA logs as a starting point for troubleshooting. Learn more about [On-prem agent (OPA) errors](/en/recipes/design-time-errors/opa-errors).

---

---
url: >-
  https://docs.workato.com/en/recipes/design-time-errors/unestablished-connectivity.md
description: >-
  Learn how to resolve unestablished connectivity errors in Workato recipes
  caused by changed credentials, missing permissions, or wrong configurations.
---

# Unestablished connectivity

Unestablished connectivity errors occur when your recipe cannot establish or maintain a valid connection with external apps or services. These errors prevent the recipe from starting and can occur due to incorrect credentials, permissions, or configurations.

## Common causes of app connection errors

Common reasons for app connection invalidation include:

- App credentials were changed, but you did not update the connection in Workato.
- You lack the appropriate permissions to read/write records.
- Your permissions were modified to a reduced scope.

In these cases, reconnect the app or verify that you have the necessary permissions to resolve the issue.

## Troubleshooting steps

If you experience connection issues, ensure all connections associated with the recipe are correctly established:

1. Select the correct connection from the drop-down menu.
   
2. Assign a unique **Connection name** for easy reference in future recipes.
   
3. Choose the correct **Authentication type**, such as OAuth 2.0, if required.
   

![Establish your connection](/assets/establish-connection.DOJ0k_L-.png)_Establish your connection_

Even if the connection appears established, an invalid connection can prevent the recipe from starting. Review the user account to ensure that it has the required permissions and privileges.

![Review your account](/assets/review-account.BIk9jY1v.png)_Review your account_

---
