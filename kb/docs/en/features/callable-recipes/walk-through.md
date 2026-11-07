---
url: 'https://docs.workato.com/en/features/callable-recipes/walk-through.md'
description: >-
  Walk through building a callable recipe that reuses shared logic, using a
  Salesforce to QuickBooks Online invoice scenario as the example.
---

# Callable recipes by Workato - Walkthrough

Let’s take a look at an example to see how this works. Say you want to automate the process of creating an invoice in Quickbooks Online (QBO) when an opportunity is closed-won in Salesforce. The recipe logic would be **Create a new customer if the customer does not exist**.

> **THIS CONNECTOR IS DEPRECATED**
> 
> The **Callable recipes** connector has been replaced by the [**Recipe functions**](/en/connectors/recipe-functions) connector.
> 
> **Existing callable recipes continue to function**, but you can't create new ones. You can continue to use callable recipes in other recipes.
> 
> Check out the [migration guide](/en/features/callable-recipes/migrating-to-recipe-functions-api-recipes) and [Recipe functions FAQ](/en/features/callable-recipes/recipe-functions-faq) for more info.

In order to create a QBO invoice, you’ll need to create a new customer if the customer does not already exist in QBO. Now, this snippet of logic: “creating a customer in QBO when they don’t already exist,” is a process that is necessary not only with your Salesforce to QBO integrations, but also when you have Point Of Sale (POS) transactions flowing into QBO, invoices you receive from your vendors and more. Instead of recreating the logic for “creating a customer in QBO when they don’t already exist,” you can make this snippet of logic into a Callable Recipe.

* * *

## Create a new recipe

Create a recipe as you normally would, and for the trigger, select **Callable Recipe** under the application picklist.

![Select callable recipe trigger](/assets/callable-recipe-trigger.CSbX2T9D.png)_Select callable recipe connector and call recipe action_

Fill in a Name for the recipe, and fill up the Input Schema and the Response Schema in the JSON Format.

In simple terms, the input schema determines what fields will be shown and need to be filled in when a callable recipe action is created in the calling recipe. The Response schema determines what pills will be available for use in the calling recipes Output data.

Refer to [New call for recipe trigger](/en/features/callable-recipes/new-call-trigger) for more information.

* * *

## Add steps to the recipe

Next, create your set of actions for the recipe. For this example, you would create a set of standard de-duplication steps, run a search, and if the search gives no results, create a customer. If an existing customer is found, update the customer.

* * *

## Call recipe

Create a recipe that requires the logic from the callable recipe we created earlier. Set up the trigger as required, and when created the actions you need. When you need to call the callable recipe, simply select Add a new step, select **call recipe**, choose the recipe you created earlier, and you will see the fields from your **input schema** appear. Simply drag and drop the required pills and you'll be good to go!

Refer to [Call recipe actions](/en/features/callable-recipes/call-recipe-action) for more information.

---
