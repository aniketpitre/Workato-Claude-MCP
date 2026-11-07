---
url: 'https://docs.workato.com/en/api-mgmt/api-recipes.md'
description: >-
  API recipes are a Workato recipe type you can call as API endpoints to share
  data and logic with other recipes or external users.
---

# API recipe endpoints

API recipes are a type of [recipe](/en/recipes/building-recipes) that you can call as API endpoints. You can use these endpoints in other recipes or share the endpoints with external users. For example, you can create an API endpoint that provides inventory status to your suppliers.

> **CALLABLE RECIPES**
> 
> API recipes replace the API endpoint functionality of [Callable recipes](/en/features/callable-recipes). Refer to the [FAQ](/en/api-mgmt/api-recipes/api-recipes-faq) for more information.

> **ACCESS REQUIREMENTS**
> 
> API recipes require access to the [API Platform](/en/api-management) feature. Contact your Customer Success Manager if you don't have access to the **Platform > API platform** page in Workato.

## API recipes

API recipes define recipe logic, request schemas, and response schemas for the API. Refer to the [Create an API recipe](/en/api-mgmt/api-recipes/walkthrough) guide to configure an API recipe.

![API recipe](/assets/api-recipe.CkEqu1UN.png)_API recipe_

### Triggers and actions

The **API platform by Workato** connector contains the following resources:

- The [New API request](/en/api-mgmt/api-recipes/trigger-new-api-request) trigger defines a request and response structure and creates a job when it receives an API request.
- The [Response to API request](/en/api-mgmt/api-recipes/action-response-to-api-request) action ends the current job and sends one of the responses defined by the trigger.

API recipes require both steps to complete successfully. Workato automatically creates a recipe with the **New API request** trigger when you select **Build an API endpoint** as a recipe's starting point.

## Recipe endpoints

Recipe endpoints define the HTTP method, endpoint name, endpoint path, request timeout, schema validation, and cache response for the API. Refer to the [Configure a new API recipe endpoint](/en/api-mgmt/configure-recipe-endpoint) guide to configure a recipe endpoint.

![Recipe endpoint](/assets/recipe-endpoints.B3CZ3z0r.png)_Recipe endpoint_

## API collections

API collections group API recipe endpoints to streamline access control for users and applications. Refer to the [API collections](/en/api-mgmt/api-collections) guide to configure an API collection.

![Endpoints in an API collection](/assets/api-collection-endpoints-list.BDVDbKJx.png)_Endpoints in an API collection_

## API performance

You can improve API performance using the following methods:

- **Disable logs**: Go to a recipe's **Settings > Data retention** tab and configure the **Jobs data retention** setting to disable log creation. Refer to the [Defining data retention for recipes](/en/security/data-protection/data-retention/configure-retention-for-recipes) guide for more information.
  
- **Enable API caching**: Go to an endpoint's **Settings** tab and enable **Cache response** to enable API caching. Refer to the [API endpoint caching](/en/api-mgmt/api-caching) guide for more information.

---
