---
url: 'https://docs.workato.com/en/features/callable-recipes.md'
description: >-
  Callable recipes are recipes invoked from another recipe to reuse a repeatable
  set of steps and keep recipes shorter and easier to maintain.
---

# Callable recipes by Workato

**Callable recipes** are a type of recipe that can be called from another recipe. This helps to reduce the length of your recipes by separating a repeatable set of actions into a callable recipe that can be called from other recipes that require the same steps.

> **THIS CONNECTOR IS DEPRECATED**
> 
> On **December 3, 2021**, the [**Recipe functions**](/en/connectors/recipe-functions) and [**API platform**](/en/api-mgmt/api-recipes/) connectors replaced Callable recipes by Workato.
> 
> **Existing callable recipes continue to work, but you can't create new ones.**.
> 
> Check out the [migration guide](/en/features/callable-recipes/migrating-to-recipe-functions-api-recipes), [Recipe functions FAQ](/en/features/callable-recipes/recipe-functions-faq), and [API recipes FAQ](/en/api-mgmt/api-recipes/api-recipes-faq) for more info.

A callable recipe is triggered by a call from another recipe instead of a trigger event in an application.

Callable recipes can also be exposed as REST endpoints using the [API Platform feature](/en/api-management).

## Advantages of using callable recipes

| Advantages | Details |
| --- | --- |
| Easier to test | By grouping a set of actions into a separate recipe instead of repeating them in the same recipe, you reduce the effort needed to change and test the steps. |
| More readable | Instead of having really long recipes, break it out into smaller recipes that can be called. |
| Sharing across recipes | If you have a standard error notification policy, you can create a recipe and then have all recipes call this recipe for error notification. |
| Share across accounts and with partners | You can expose REST APIs to your business partners. For example, a REST API that provides inventory status to your suppliers. |

---

---
url: >-
  https://docs.workato.com/en/features/callable-recipes/migrating-to-recipe-functions-api-recipes.md
description: >-
  Migrate callable recipes to Recipe functions and API Platform, with guidance
  on the new recipe types and how their triggers and actions compare.
---

# Migrate to recipe functions and API recipes

Previously, the callable recipe type and the **Callable Recipes by Workato** connector were used to create both API endpoints and reusable recipe components. Now that dedicated recipe types exist for each use case, use [Recipe Functions](#recipe-functions) and [API Platform](#api-recipes) components instead.

In this guide, we'll cover:

- [The impact on existing callable recipes](#impact-on-existing-callable-recipes)
- [The new recipe types](#understanding-the-new-recipe-types)
- [How the new triggers and actions compare](#comparing-triggers-and-actions)

* * *

## Impact On Existing Callable Recipes

Effective as of **December 3, 2021**, you can't create new callable recipes. Existing callable recipes still work, and new recipes can call them. You can migrate to new recipe types or continue using your existing callable recipes.

* * *

## Converting Callable Recipes

While there isn't a way to automatically convert existing callable recipes to the new recipe types, there isn't a need. **Your callable recipes continue to work as before.**

However, consider migrating to [the new recipe types](#understanding-the-new-recipe-types) if you want to take advantage of some new features. For example: For recipes that function as API endpoints, you can now define non-standard response codes using the [API recipe type](#api-recipes).

* * *

## Understanding The New Recipe Types

All callable recipe functionality has been split into two new recipe types. Everything you could do with callable recipes you can still do with [Recipe Functions](#recipe-functions) and [API Platform](#api-recipes) components.

### Recipe Functions

The **Recipe Functions** connector focuses on recipe reusability, readability, and maintenance. Recipe functions provide a simple and streamlined way to build reusable recipe components with minimum overhead.

Using this connector's triggers and actions, you can build a workflow once and re-use it across recipes in your workspace with ease. Learn more in the [Recipe Functions docs](/en/connectors/recipe-functions).

### API Recipes

The **API Platform** connector is dedicated to creating and deploying automations as API endpoints. API recipes include new features to enable you to build to the full functionality of the OpenAPI Specification, including:

- Custom request and response headers
- Multiple responses and support for all HTTP response codes
- Sending a response automatically stops the current job

This release confirms API as a first-class citizen in the Workato ecosystem and lays the groundwork for more improvements in the future, like improved auto-documentation and the ability to automatically generate API Collections from any valid OpenAPI specification. Learn more in the [API Platform docs](/en/api-mgmt/api-recipes/).

* * *

## Comparing Triggers And Actions

Callable recipe triggers and actions are fully compatible with the new API Platform and Recipe Functions triggers and actions.

**Not sure where to start?** Use the table below to find the trigger or action that replaces the callable recipe version:

| Callable Recipe trigger or action | New trigger or action |
| --- | --- |
| [New call trigger (recipe component)](/en/features/callable-recipes/new-call-trigger.html) | [Recipe Functions - New function call trigger](/en/connectors/recipe-functions/triggers/new-function-call.html) |
| [New call trigger (API endpoint)](/en/features/callable-recipes/new-call-trigger.html) | [API Platform - New API request trigger](/en/api-mgmt/api-recipes/trigger-new-api-request.html) |
| [Call recipe action (synchronous)](/en/features/callable-recipes/call-recipe-action.html#call-recipe-synchronous) | [Recipe Functions - Call recipe function action (synchronous)](/en/connectors/recipe-functions/actions/call-recipe-function-synchronously.html) |
| [Call recipe action (asynchronous)](/en/features/callable-recipes/call-recipe-action.html#call-recipe-asynchronous) | [Recipe Functions - Call recipe action (asynchronous)](/en/connectors/recipe-functions/actions/call-recipe-function-asynchronously.html) |
| [Return data from a recipe action](/en/features/callable-recipes/return-response-action.html) | [Recipe Functions - Return data from a recipe function action](/en/connectors/recipe-functions/actions/return-data-from-a-recipe-function.html) |
| [Wait for async calls action](/en/features/callable-recipes/wait-for-async-action.html) | [Recipe Functions - Wait for async calls action](/en/connectors/recipe-functions/actions/wait-for-async-calls.html) |

---
