---
url: 'https://docs.workato.com/en/features/callable-recipes/recipe-functions-faq.md'
description: >-
  Answers to common questions about Recipe functions in Workato, including what
  changes in the recipe wizard and recipe builder.
---

# Recipe Functions FAQ

On **December 3, 2021**, we’re introducing a new recipe type: **Recipe functions**. Recipe functions provide a simple and streamlined way to build reusable recipe components with minimum overhead.

To build a recipe function you need only define the required input and an optional output. You can invoke a recipe function from any other Workato recipe. Recipe functions are reusable components that you can create for:

- Standardization of logic and process
- Improving speed-of-use and productivity
- Simplify testing, debugging, and maintenance
- Improve readability of your recipes

Future improvements to Recipe functions will give you the ability to easily refactor steps from any recipe into a recipe function and the ability to independently test recipe functions.

* * *

## What's changing?

Here's a look at what's changing in Workato to accommodate this new recipe type:

- [Recipe wizard starting point](#recipe-wizard-starting-point)
- [Recipe builder](#recipe-builder)

### Recipe Wizard Starting Point

The **Build callable recipe** recipe starting point option has been replaced with **Build recipe function**:

![New Build a recipe function recipe starting point](/assets/recipe-functions-starting-point.CAhrYkvw.png)

### Recipe Builder

To create and use reusable components when building recipes, use the **Recipe function by Workato** app:

![The Recipe functions app in the Recipe builder](/assets/recipe-functions-recipe-builder.Bn5TwbFY.gif)

* * *

## FAQ

- [Are callable recipes and recipe functions the same?](#are-callable-recipes-and-recipe-functions-the-same)
- [Do I need to replace my existing callable recipes with recipe functions?](#do-i-need-to-replace-my-existing-callable-recipes-with-recipe-functions)
- [Are recipe functions billable on recipe-based plans?](#are-recipe-functions-billable-on-recipe-based-plans)
- [Is there a way to convert callable recipes into recipe functions?](#is-there-a-way-to-convert-callable-recipes-into-recipe-functions)
- [Can I continue using existing callable recipes from new recipes?](#can-i-continue-using-existing-callable-recipes-from-new-recipes)
- [I’m using the same callable recipe as an API endpoint and as a reusable component. Will that still work?](#i-m-using-the-same-callable-recipe-as-an-api-endpoint-and-as-a-reusable-component-will-that-still-work)
- [Can I use callable recipes to create reusable components as before?](#can-i-use-callable-recipes-to-create-reusable-components-as-before)

### Are callable recipes and recipe functions the same?

No. While callable recipes filled multiple functions in Workato, including the creation of API endpoints, recipe functions are focused solely on creating reusable recipe components. For this reason, recipe functions have a much simpler data structure and less design overhead.

See example data structures

![Comparison of data structures between callable recipes and recipe functions](/assets/recipe-functions-data-comparison.Ei8zmsXL.png)

Unlike callable recipes, recipe functions can't be used to create API endpoints. Instead, use the new dedicated [API recipe type](/en/api-mgmt/api-recipes/). Check out the [API recipe FAQ](/en/api-mgmt/api-recipes/api-recipes-faq)

### Do I need to replace my existing callable recipes with recipe functions?

No. Your existing recipes continue to work. Recipe functions provide new capabilities, such as one-click refactoring of multiple steps into a single recipe function. You don't need to convert callable recipes that already work.

### Are recipe functions billable on recipe-based plans?

No, recipe functions aren't billable recipes.

### Is there a way to convert callable recipes into recipe functions?

Currently, no. However, there’s no need to convert recipes, as callable recipes will continue to work as before.

### Can I continue using existing callable recipes from new recipes?

Yes. Even though you can’t create new callable recipes, the **Callable Recipes by Workato** app will continue to be available in the Recipe builder. If you need to call one of your existing callable recipes, just select the app and choose the appropriate action and recipe.

As you start to build recipe functions, remember that legacy callable recipes are accessed via the **Callable recipes by Workato** app, while new recipe functions are accessed via the **Recipe function by Workato** app. If you can’t find the recipe you’re looking for, make sure you’re using the right app.

### I’m using the same callable recipe as an API endpoint and as a reusable component. Will that still work?

Yes. An existing callable recipe can still be used both as an API endpoint and to be called from other Workato recipes. However, this is quite rare in practice.

To support this use case with API recipes and recipe functions, you’ll need to create two recipes. To retain modularity, you can keep the bulk of your logic inside the recipe function and invoke it from your API recipe.

### Can I use callable recipes to create reusable components as before?

No. Callable recipes will be phased out.

Until now, the callable recipe type and the [**Callable Recipes by Workato**](/en/features/callable-recipes) app have been used to create API endpoints, among other purposes. With the release of a dedicated reusable component recipe type, we’ll gradually phase out the use of callable recipes.

From December 3 2021 onward, you will no longer be able to create new callable recipes. When building new recipes, choosing **Build an API Endpoint** will instead create an API recipe.

**This is a non-breaking change**. All of your existing callable recipes continue to work.

---
