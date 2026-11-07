---
url: 'https://docs.workato.com/en/features/account-properties.md'
description: >-
  Learn how Workato environment properties store account-wide configuration
  parameters that all recipes can use as values in the data tree.
---

# Environment properties

Environment properties enable you to store account-wide recipe configuration parameters. Environment properties appear in all recipes as usable values as a child of the **Properties** datatree.

Environment-level properties are also known as environment variables or configuration variables. They are useful for complex deployment models across connections and recipes.

For example, you can have a property that indicates where to send a notification email. All recipes can look this value up from the data tree (properties section) and send an email to the same recipient.

The environment properties feature is enabled only for certain users. Reach out to your Customer Success Manager to learn more.

Go to **Tools > Environment properties** to create property values (name-value pairs).

![Environment properties option](/assets/environment-properties-nav.B_rbZHlS.png)_Environment properties in Tools_

## Quotas

| Description | Quota |
| --- | --- |
| Maximum number of environment properties per environment | 1,000 |
| Maximum length of an environment property name | 100 characters |
| Maximum length of an environment property value | 1,024 characters |

## Create property

To use environment properties in recipes, you must create them in the **Environment properties** interface. A property is a name and its corresponding value.

![Create property](/assets/environment-properties-create.D6Oek3G5.png)_Create property_

## Update property

To update a property, hover your mouse cursor over the property. Workato displays the icons to edit or delete an existing property.

> **ENVIRONMENT PROPERTY JOB EXECUTION BEHAVIOR**
> 
> [Jobs](/en/recipes/jobs#recipe-jobs) do not dynamically detect and update changes to environment property values. Environment property values are frozen at the beginning of job execution by design. You can use [Lookup tables](/en/features/lookup-tables#lookup-tables) if you require dynamic detection for environment property values.

![Update delete property](/assets/environment-properties-edit.CbsO-rJy.png)_Updating or deleting an account property_

## Using properties in recipes

Environment properties appear in all recipes within the Workato account, under the **Properties** datatree. Their values correspond to the values defined in the **Environment properties** interface.

When a recipe is active, Workato looks up its value in the **Environment properties** interface.

![Environment properties datatree](/assets/environment-properties-recipe.BcDs_ZEH.png)_Using properties in a recipe_

---
