---
url: 'https://docs.workato.com/en/api-mgmt/api-recipes/api-recipes-faq.md'
description: >-
  Answers to common questions about Workato API recipes, the recipe type for
  building and deploying automations as API endpoints.
---

# API Recipes FAQ

On **December 3, 2021**, we’re releasing **API recipes**: a new recipe type dedicated to creating and deploying automations as API endpoints. API recipes include new features to enable you to build to the full functionality of the OpenAPI Specification, including:

- Custom request and response headers
- Multiple responses and support for all HTTP response codes
- Sending a response automatically stops the current job

This release confirms API as a first-class citizen in the Workato ecosystem and lays the groundwork for more improvements in the future, like improved auto-documentation and the ability to automatically generate [API Collections](/en/api-mgmt/api-collections) from any valid OpenAPI specification.

* * *

## What's changing?

Here's a look at what's changing in Workato to accommodate this new recipe type:

### Recipe Wizard Starting Point

The **Build an API endpoint** recipe starting point is still available, but selecting it now creates a recipe of the new [API recipe type](/en/api-mgmt/api-recipes/) instead of a callable recipe.

**Note**: After December 3 2021, you'll [no longer be able to create callable recipes as API endpoints](#can-i-create-callable-recipes-for-api-endpoints-as-before). Existing callable recipes still run but are no longer supported.

### Creating An API Collection

When creating a new API collection, you’re prompted to select a folder to source recipes from.

Previously, Workato would pick up callable recipes in the selected folder and create matching API endpoints. As of December 3 2021, Workato will create an endpoint for each callable recipe and API recipe in the selected folder.

**Note**: There isn't a visual distinction between the two recipe types:

![The Recipe functions app in the Recipe builder](/assets/api-recipes-no-distinction.uhmANAyk.png)

### Editing An API Endpoint

When editing an API endpoint, you could previously select any callable recipe to assign to the endpoint.

You can now select from any API recipe or callable recipe. Recipes are displayed by name, with no visual distinction between the two types:

![The Recipe functions app in the Recipe builder](/assets/api-recipes-edit-endpoint.D6bthmsJ.gif)

## Do I need to replace my existing callable recipes with API recipes?

View answer

No. Your existing recipes still work. You may wish to replace an existing callable recipe with an API recipe if you want to take advantage of the newly supported features, like support for a non-standard response code.

## Is there a way to convert callable recipes into the new types?

View answer

Currently, no. However, there’s no need to convert recipes, as callable recipes will continue to work as before.

## Are API recipes billable on recipe-based plans?

View answer

Yes, API recipes are billable recipes.

## I’m using the same callable recipe as an API endpoint and as a reusable component. Will that still work?

View answer

Yes. An existing callable recipe can still be used both as an API endpoint and to be called from other Workato recipes. However, this is quite rare in practice.

To support this use case with API recipes and recipe functions, you’ll need to create two recipes. To retain modularity, you can keep the bulk of your logic inside the recipe function and invoke it from your API recipe.

## Can I create callable recipes for API endpoints as before?

View answer

No. Callable recipes will be phased out.

Until now, the callable recipe type and the [**Callable Recipes by Workato**](/en/features/callable-recipes) app have been used to create API endpoints, among other purposes. With the release of a dedicated [API recipe type](/en/api-mgmt/api-recipes/), we’ll gradually phase out the use of callable recipes.

From December 3 2021 onward, you will no longer be able to create new callable recipes. When building new recipes, choosing **Build an API Endpoint** will instead create an API recipe.

**This is a non-breaking change**. All existing callable recipes still work.

## Where can I find out more?

View answer

Check out the [API recipe docs](/en/api-mgmt/api-recipes/) for more info.

To learn more about recipe functions, check out the [Recipe functions FAQ](/en/features/callable-recipes/recipe-functions-faq).

---
