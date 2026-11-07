---
url: 'https://docs.workato.com/en/recipes/version-management.md'
description: >-
  Learn how Workato tracks recipe versions, logs recipe and schema changes, and
  lets you compare versions with Recipe Diff.
---

# Recipe version management

Every time a recipe is saved, a version of the recipe is created. Previous versions of a recipe can be restored at any time. Recipe versions can be viewed in the **Versions** tab and are denoted by their version number.

In the version history view, each version is attributed to the user who made the change (relevant for multi-user team accounts), with a timestamp when the version was saved, as well as the change type associated with that version.

![Recipe versions](/assets/recipe-versions.DHU48yW5.png)_Recipe versions as viewed from the Versions tab_

* * *

## Change Types

There are two types of changes:

- [Recipe changes](#recipe-changes)
- [Schema changes](#schema-changes)

### Recipe Changes

A **Recipe change** is logged when a user actively changes the recipe. For example, adding, or removing steps and changing field mappings, will create a new version of the recipe when the recipe is saved.

### Schema Changes

A **Schema change** is logged when Workato detects that the underlying schema of objects in the recipe have changed. For example, when a Salesforce custom object has a new field added.

Such [schema refreshes](/en/recipes/editor#refresh-schema) will automatically create a new version of the recipe.

* * *

## Comparing And Reviewing Changes

Using the **Recipe Diff** feature, you can visually compare two recipe versions and review the changes. Check out the [Recipe Diff](/en/recipe-development-lifecycle/compare-versions-with-recipe-diff) guide for more info.

* * *

## Restoring A Version

To restore a previous version of a recipe:

1. In your Workato account, open a recipe.
   
2. Click the **Versions** tab.
   
3. Click a **non-current** recipe version to open the **Version details** page.
   
4. Click the **Restore this version** button, located in the top right corner of the page:
   
   ![Restoring a recipe version](/assets/restored-version.CarklL7X.png)_Restore this recipe button, located on the Version details page_
   
5. When prompted, click **Yes** to restore the recipe version.
   

If successful, the recipe version will be copied and made into the **current** version of the recipe.

---
